#!/usr/bin/env python3
"""nexus_delivery.py — Delivery half-duplex: fecha o ciclo task → parcela (Smart SDDAI).

Lê task JSON de .ai/handoffs/task-TA-*.json, valida via nexus_dispatcher,
marca ledger como dispatched, aguarda parcela de retorno com mesmo task_id,
grave ledger com schema fixo (task_id, sender, receiver, action, exit_status,
timestamp, dod), implementa lock por task_id, watchdog timeout, retry com
idempotência e códigos de erro verbatim.

Uso:
  python3 scripts/nexus_delivery.py --once      # processa filas uma vez
  python3 scripts/nexus_delivery.py --watch     # loop contínuo (60s)
  python3 scripts/nexus_delivery.py --escalate  # escaleia timeouts pendentes
"""
import argparse
import fcntl
import json
import os
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_nexus_yaml import KNOWN_SLUGS, AGENT_TOPOLOGY, VALID_ROLES
from nexus_dispatcher import VALID_ACTIONS, TASK_ID_RE, dispatch as dispatch_task

HANDOFFS_DIR = Path(".ai/handoffs")
LEDGER = Path(".ai/agents/ledger.yaml")
LOCKS_DIR = Path(".ai/agents/locks")
PARCELS_DIR = Path(".ai/handoffs")

POLL_INTERVAL = 5
WATCH_INTERVAL = 60
DEFAULT_TIMEOUT_S = 3600
LOCK_TIMEOUT_S = 30
RETRY_BACKOFF_S = [5, 15, 60]
MAX_RETRY = 3

ERROR_CODES = {
    "TASK_ID_INVALID": "task_id fora do padrão TA-NNN",
    "TARGET_NOT_PROMULGADO": "target não promulgado na registry",
    "SELF_DELEGATION": "auto-delegação proibida (Art. 4.5)",
    "LAYER_MISMATCH": "camada incompatível para entrega",
    "TIMEOUT_EXCEEDED": "timeout de parcela excedido",
    "LOCK_ACQUIRE_FAILED": "não foi possível adquirir lock do task_id",
    "KILL_SWITCH": "kill_switch ativado",
    "CONSTITUTIONAL_VIOLATION": "violação constitucional detectada",
    "DOD_MISSING": "parcela sem dod:true ou status terminal",
    "RETRY_EXHAUSTED": "retry esgotado sem parcela",
}

VALID_STATUSES = {"accepted", "rejected", "escalated"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


SCHEMA_KEYS = ("version", "current_session", "audit_trail", "blocked_tasks")


def load_ledger() -> dict:
    """Retorna o ledger no esquema Art. 4.10.
    Retrocompatível: se o arquivo ainda for uma lista (formato legado), envolve
    automaticamente em audit_trail sem perder nenhuma entrada.
    """
    if not LEDGER.exists():
        return {"version": "2.0", "current_session": None, "audit_trail": [], "blocked_tasks": []}
    import yaml
    data = yaml.safe_load(LEDGER.read_text(encoding="utf-8")) or {}
    if isinstance(data, list):
        # ledger legado: lista simples de entradas -> envolve em audit_trail
        return {
            "version": "2.0",
            "current_session": None,
            "audit_trail": data,
            "blocked_tasks": [],
        }
    if not isinstance(data, dict):
        return {"version": "2.0", "current_session": None, "audit_trail": [], "blocked_tasks": []}
    for k in SCHEMA_KEYS:
        if k not in data or data[k] is None:
            data[k] = [] if k in ("audit_trail", "blocked_tasks") else None
    return data


def save_ledger(data: dict) -> None:
    """Persiste o ledger preservando o esquema Art. 4.10.
    Aceita tanto um dict (esquema) quanto uma lista (retrocompatibilidade).
    Nunca sobrescreve entradas existentes: apenas reescreve o arquivo inteiro
    com o mesmo conteudo de audit_trail + metadados do esquema.
    """
    import yaml
    if isinstance(data, list):
        data = {
            "version": "2.0",
            "current_session": None,
            "audit_trail": data,
            "blocked_tasks": [],
        }
    for k in SCHEMA_KEYS:
        if k not in data or data[k] is None:
            data[k] = [] if k in ("audit_trail", "blocked_tasks") else None
    LEDGER.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )


def ledger_has_terminal(task_id: str) -> bool:
    """Idempotência: já tem dod:true, status terminal, ou já foi dispatchado."""
    for entry in load_ledger().get("audit_trail", []):
        if entry.get("task_id") == task_id:
            if entry.get("dod") is True:
                return True
            if entry.get("status") in VALID_STATUSES:
                return True
            if entry.get("status") == "dispatched":
                return True
    return False


def append_ledger(entry: dict) -> None:
    data = load_ledger()
    data["audit_trail"].append(entry)
    save_ledger(data)


def acquire_lock(task_id: str) -> object:
    LOCKS_DIR.mkdir(parents=True, exist_ok=True)
    lock_path = LOCKS_DIR / f"{task_id}.lock"
    fh = open(lock_path, "w")
    try:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        fh.write(str(os.getpid()))
        fh.flush()
        return fh
    except (BlockingIOError, OSError):
        fh.close()
        return None


def release_lock(fh: object) -> None:
    try:
        fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
    finally:
        fh.close()


def find_pending_tasks() -> list:
    """Tasks em .ai/handoffs/task-*.json que ainda não têm parcel terminal."""
    tasks = []
    for f in sorted(HANDOFFS_DIR.glob("task-*.json")):
        try:
            task = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        tid = task.get("task_id")
        if not tid:
            continue
        # Pular arquivos que são parcels (não envelopes de task)
        if "target" not in task or "action" not in task:
            continue
        if ledger_has_terminal(tid):
            continue
        tasks.append((f, task))
    return tasks


def find_parcel(task_id: str) -> dict | None:
    """Busca parcela de retorno para task_id em .ai/handoffs/parcel-*.json."""
    for f in sorted(PARCELS_DIR.glob(f"parcel-{task_id}*.json")):
        try:
            return json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
    return None


def validate_task_for_delivery(task: dict) -> tuple[bool, list]:
    """Valida envelope antes de entregar. Regras do dispatcher + camada."""
    errors = []
    tid = task.get("task_id") or ""
    target = task.get("target") or ""
    action = task.get("action") or ""
    sender = task.get("sender", "agent-nexus-prime-ultimate") or ""

    if not TASK_ID_RE.match(tid):
        errors.append(ERROR_CODES["TASK_ID_INVALID"])
    if target not in KNOWN_SLUGS:
        errors.append(ERROR_CODES["TARGET_NOT_PROMULGADO"])
    if sender == target:
        errors.append(ERROR_CODES["SELF_DELEGATION"])
    if action not in VALID_ACTIONS:
        errors.append(ERROR_CODES["LAYER_MISMATCH"])
    # reply_required deve ser booleano quando presente (contrato half-duplex)
    reply_required = task.get("reply_required", True)
    if reply_required is not None and not isinstance(reply_required, bool):
        errors.append("reply_required deve ser booleano (contrato half-duplex)")
    # camada do target deve existir na topologia
    target_layer = None
    for layer, members in AGENT_TOPOLOGY.items():
        if target in members:
            target_layer = layer
            break
    if target_layer is None:
        errors.append(ERROR_CODES["LAYER_MISMATCH"])
    return (len(errors) == 0), errors


def process_task(f: Path, task: dict, wait: bool = False) -> None:
    """Processa UM task: valida, marca ledger dispatched, opcionalmente aguarda parcela."""
    tid = task.get("task_id")
    target = task.get("target")
    action = task.get("action")
    sender = task.get("sender", "agent-nexus-prime-ultimate")
    reply_required = task.get("reply_required", True)

    ok, errors = validate_task_for_delivery(task)
    if not ok:
        append_ledger({
            "task_id": tid,
            "sender": sender,
            "receiver": target,
            "action": action,
            "exit_status": 1,
            "timestamp": utc_now(),
            "dod": False,
            "status": "rejected",
            "error": "; ".join(errors),
            "notes": "rejeitado na validação de delivery",
        })
        print(f"[{tid}] REJEITADO: {'; '.join(errors)}")
        return

    # Lock por task_id
    lock_fh = acquire_lock(tid)
    if lock_fh is None:
        append_ledger({
            "task_id": tid,
            "sender": sender,
            "receiver": target,
            "action": action,
            "exit_status": 1,
            "timestamp": utc_now(),
            "dod": False,
            "status": "rejected",
            "error": ERROR_CODES["LOCK_ACQUIRE_FAILED"],
            "notes": "não foi possível adquirir lock",
        })
        print(f"[{tid}] {ERROR_CODES['LOCK_ACQUIRE_FAILED']}")
        return

    try:
        # Marca ledger como dispatched
        append_ledger({
            "task_id": tid,
            "sender": sender,
            "receiver": target,
            "action": action,
            "exit_status": 0,
            "timestamp": utc_now(),
            "dod": False,
            "status": "dispatched",
            "notes": f"entregue a {target} via nexus_delivery",
        })
        print(f"[{tid}] dispatched → {target}")

        # Se reply_required, aguarda parcela (mesmo em --once)
        should_wait = wait or reply_required
        if not should_wait:
            return

        # Aguarda parcela com timeout
        deadline = time.time() + DEFAULT_TIMEOUT_S
        while time.time() < deadline:
            parcel = find_parcel(tid)
            if parcel is not None:
                # Correlação: parcel deve ter mesmo task_id
                parcel_tid = parcel.get("task_id") or parcel.get("envelope_id")
                if parcel_tid != tid:
                    print(f"[{tid}] parcel ignorado: task_id {parcel_tid!r} != {tid!r}")
                    time.sleep(POLL_INTERVAL)
                    continue
                dod = parcel.get("parcel", {}).get("dod", False)
                pstatus = parcel.get("status", "rejected")
                append_ledger({
                    "task_id": tid,
                    "sender": parcel.get("route", {}).get("sender", target),
                    "receiver": parcel.get("route", {}).get("receiver", sender),
                    "action": action,
                    "exit_status": 0 if dod else 1,
                    "timestamp": utc_now(),
                    "dod": bool(dod),
                    "status": pstatus,
                    "artifacts": parcel.get("parcel", {}).get("artifacts", []),
                    "notes": parcel.get("parcel", {}).get("notes", "parcela recebida"),
                })
                print(f"[{tid}] parcela recebida: dod={dod}, status={pstatus}")
                return
            time.sleep(POLL_INTERVAL)

        # Timeout → escalada
        append_ledger({
            "task_id": tid,
            "sender": sender,
            "receiver": target,
            "action": action,
            "exit_status": 1,
            "timestamp": utc_now(),
            "dod": False,
            "status": "escalated",
            "error": ERROR_CODES["TIMEOUT_EXCEEDED"],
            "notes": f"sem parcela após {DEFAULT_TIMEOUT_S}s",
        })
        print(f"[{tid}] {ERROR_CODES['TIMEOUT_EXCEEDED']} → escalada")
    finally:
        release_lock(lock_fh)


def escalate_pending() -> None:
    """Escaleia tasks em dispatched há mais de DEFAULT_TIMEOUT_S sem parcela."""
    import yaml
    if not LEDGER.exists():
        return
    data = load_ledger()
    now = datetime.now(timezone.utc)
    changed = False
    for entry in data:
        if entry.get("status") != "dispatched":
            continue
        ts = entry.get("timestamp")
        if not ts:
            continue
        try:
            ts_dt = datetime.fromisoformat(ts)
        except ValueError:
            continue
        if (now - ts_dt) > timedelta(seconds=DEFAULT_TIMEOUT_S):
            entry["status"] = "escalated"
            entry["exit_status"] = 1
            entry["dod"] = False
            entry["error"] = ERROR_CODES["TIMEOUT_EXCEEDED"]
            entry["timestamp"] = utc_now()
            entry["notes"] = "escalado por watchdog (sem parcela)"
            changed = True
            print(f"[{entry.get('task_id')}] escalado por timeout")
    if changed:
        save_ledger(data)


def main() -> int:
    parser = argparse.ArgumentParser(description="Delivery half-duplex COGME")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--once", action="store_true", help="processa filas uma vez")
    group.add_argument("--watch", action="store_true", help="loop contínuo")
    group.add_argument("--escalate", action="store_true", help="escaleia timeouts")
    args = parser.parse_args()

    if args.escalate:
        escalate_pending()
        return 0

    pending = find_pending_tasks()
    if not pending:
        print("Nenhuma task pendente.")
        if args.watch:
            while True:
                time.sleep(WATCH_INTERVAL)
                pending = find_pending_tasks()
                escalate_pending()
                for f, task in pending:
                    process_task(f, task)
        return 0

    wait = args.watch
    for f, task in pending:
        process_task(f, task, wait=wait)

    if args.watch:
        while True:
            time.sleep(WATCH_INTERVAL)
            pending = find_pending_tasks()
            escalate_pending()
            for f, task in pending:
                process_task(f, task, wait=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())
