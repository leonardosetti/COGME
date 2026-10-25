#!/usr/bin/env python3
"""nexus_dispatcher.py — Dispositivo de despacho DAG half-duplex (FASE S.4).

Valida envelopes de task contra:
  - AGENT_TOPOLOGY (DAG canônica, importada de validate_nexus_yaml — SSOT única)
  - .ai/agents/registry.yaml (só agentes promulgados/legacy-forge são despacháveis)
  - conjunto válido de ações por camada
Saída: envelope {status: aceite|rejeitado, route, reply_contract} half-duplex.
Fail-closed: qualquer violação → exit 1.

Formato de task (JSON):
  {"task_id": "TA-001", "target": "agent-backend-dev",
   "action": "implement", "handoff": "HF-001", "payload": "..."}

Uso:
  python3 scripts/nexus_dispatcher.py --check task.json
  python3 scripts/nexus_dispatcher.py --report
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_nexus_yaml import AGENT_TOPOLOGY, KNOWN_SLUGS  # SSOT única — não duplicar

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

REGISTRY = Path(".ai/agents/registry.yaml")
VALID_ACTIONS = {
    "dispatch", "forge", "validate", "orchestrate", "spec", "plan", "analyze",
    "implement", "contract", "design", "consult", "shell", "infra",
    "pipeline", "github", "harden", "comply", "test", "review", "gate",
    "audit", "document", "build", "destill",
}
TASK_ID_RE = re.compile(r"^[A-Z]{2}-\d{3,4}$")


def load_promulgated() -> dict:
    if yaml is None:
        raise RuntimeError("PyYAML ausente")
    if not REGISTRY.exists():
        return {}
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    out = {}
    for a in data.get("agents", []):
        name = a.get("name")
        if name:
            out[name] = {
                "layer": a.get("layer"),
                "role": a.get("role"),
                "status": a.get("status", "promulgado"),
                "file": a.get("file"),
            }
    return out


def _layer_of(slug: str) -> str:
    for layer, members in AGENT_TOPOLOGY.items():
        if slug in members:
            return layer
    return "UNKNOWN"


def dispatch(task: dict, promulgated: dict) -> dict:
    """Valida UM envelope de task. Nunca lança: retorna envelope fail-closed."""
    env = {
        "status": "aceito",
        "task_id": task.get("task_id"),
        "sender": task.get("sender", "agent-orchestrator"),
        "target": task.get("target"),
        "action": task.get("action"),
        "handoff": task.get("handoff"),
        "route": {"sender": task.get("sender", "agent-orchestrator"),
                  "receiver": task.get("target")},
        "reply_contract": "half-duplex: receiver MUST return structured status parcel",
        "dispatched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "errors": [],
    }
    target = task.get("target")
    action = task.get("action")
    tid = task.get("task_id") or ""
    handoff = task.get("handoff")

    if not TASK_ID_RE.match(tid):
        env["errors"].append(f"task_id fora do padrão TA-NNN: {tid!r}")
    if target not in KNOWN_SLUGS:
        env["errors"].append(f"target fora da DAG canônica: {target!r}")
    elif target not in promulgated:
        env["errors"].append(f"target não promulgado na registry: {target!r}")
    elif promulgated.get(target, {}).get("status") not in ("promulgado", "legacy-forge"):
        env["errors"].append(f"target com status não-dispachável: {promulgated.get(target)}")
    if action not in VALID_ACTIONS:
        env["errors"].append(f"action fora do vocabulário: {action!r}")
    if handoff is not None and not re.match(r"^\d{3,4}-", str(handoff)) and \
            not re.match(r"^HF-\d{3,4}$", str(handoff)):
        env["errors"].append(f"handoff fora do padrão: {handoff!r}")

    # Half-duplex: anti self-delegation (Art. 4.5) — sender default = L0
    sender = task.get("sender", "agent-nexus-prime-ultimate")
    if sender == target:
        env["errors"].append(
            f"self-delegation proibida: {sender!r} → {target!r} (Art. 4.5)")
    if env["errors"]:
        env["status"] = "rejeitado"
    return env


def main() -> int:
    parser = argparse.ArgumentParser(description="Dispatch DAG half-duplex COGME")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", help="task.json para validar")
    group.add_argument("--report", action="store_true", help="resumo do roster e DAG")
    args = parser.parse_args()

    promulgated = load_promulgated()

    if args.report:
        by_layer = {}
        for slug in promulgated:
            by_layer.setdefault(_layer_of(slug), []).append(slug)
        out = {
            "registry": str(REGISTRY),
            "promulgados": len(promulgated),
            "by_layer": {k: v for k, v in sorted(by_layer.items())},
            "dag_totals": {k: len(v) for k, v in AGENT_TOPOLOGY.items()},
            "missing_from_dag": sorted(KNOWN_SLUGS - set(promulgated)),
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0

    task_path = Path(args.check)
    if not task_path.exists():
        print(json.dumps({"status": "rejeitado",
                          "errors": [f"task.json inexistente: {args.check}"]},
                         ensure_ascii=False))
        return 1
    try:
        task = json.loads(task_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(json.dumps({"status": "rejeitado", "errors": [f"JSON inválido: {exc}"]},
                         ensure_ascii=False))
        return 1

    env = dispatch(task, promulgated)
    print(json.dumps(env, indent=2, ensure_ascii=False))
    return 0 if env["status"] == "aceito" else 1


if __name__ == "__main__":
    sys.exit(main())
