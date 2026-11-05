#!/usr/bin/env python3
"""ledger_append.py — Acrescenta uma entrada ao ledger de sessão (Art. 4.10).

Esquema do ledger (retrocompatível):
  version: "2.0"
  current_session: <id da sessao atual | null>
  audit_trail:
    - task_id, sender, receiver, action, exit_status, timestamp, status, [dod], [notes]
  blocked_tasks: []

Regra de ouro (Art. 4.10 + vio-register): o ledger e append-only.
Este script SOMENTE acrescenta uma entrada ao audit_trail. Nunca reescreve
entradas existentes. Para corrigir uma entrada historica (ex.: TA-0113
auto-delegacao VIO-026), insira uma nova entrada de corretiva referenciando
o task_id original; nunca edite a linha original.

Uso:
  python3 scripts/ledger_append.py --task-id TA-NNN --sender X --receiver Y \
      --action Z --status W [--exit-status N] [--notes "texto"]
"""
import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

LEDGER = Path(".ai/agents/ledger.yaml")
SCHEMA = ("version", "current_session", "audit_trail", "blocked_tasks")


def load():
    data = yaml.safe_load(LEDGER.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise SystemExit("Ledger nao e mapeamento; verifique schema Art. 4.10.")
    for k in SCHEMA:
        data.setdefault(k, [] if k in ("audit_trail", "blocked_tasks") else None)
    return data


def append(entry: dict):
    data = load()
    data["audit_trail"].append(entry)
    LEDGER.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )
    print(f"Ledger: entrada acrescentada ({entry.get('task_id')} -> {entry.get('receiver')})")


def main() -> int:
    parser = argparse.ArgumentParser(description="Acrescenta entrada ao ledger (Art. 4.10, append-only)")
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--sender", required=True)
    parser.add_argument("--receiver", required=True)
    parser.add_argument("--action", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--exit-status", type=int, default=0)
    parser.add_argument("--dod", action="store_true", help="marca dod=true")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    entry = {
        "task_id": args.task_id,
        "sender": args.sender,
        "receiver": args.receiver,
        "action": args.action,
        "exit_status": args.exit_status,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "status": args.status,
    }
    if args.dod:
        entry["dod"] = True
    if args.notes:
        entry["notes"] = args.notes

    append(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
