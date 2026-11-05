#!/usr/bin/env python3
"""agent_communication_hub.py — Barramento de comunicacao half-duplex entre agentes (ONDA 8).

Imprime/valida envelopes de comunicacao entre agentes do roster, respeitando:
  - topologia AGENT_TOPOLOGY (sender/receiver devem ser slugs conhecidos)
  - anti-auto-delegacao (sender != target)
  - acao valida (VALID_ACTIONS)
  - handoff padronizado HF-NNNN
  - kill_switch herdado sempre presente

Saida: envelope JSON aceito/rejeitado. Never lança excecao; falha = envelope rejeitado.
FOSS/stdlib apenas.

Uso:
  python3 scripts/agent_communication_hub.py --check envelope.json
  python3 scripts/agent_communication_hub.py --template
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_nexus_yaml import KNOWN_SLUGS, AGENT_TOPOLOGY
from nexus_dispatcher import VALID_ACTIONS

ENV_ID_RE = re.compile(r"^(?:ENV|TA)-\d{3,4}$")
TASK_ID_RE = re.compile(r"^TA-\d{3,4}$")
HANDOFF_RE = re.compile(r"^HF-\d{3,4}$")


def _layer_of(slug: str) -> str:
    for layer, members in AGENT_TOPOLOGY.items():
        if slug in members:
            return layer
    return "UNKNOWN"


def validate_envelope(env: dict) -> dict:
    rep = {
        "status": "aceito",
        "envelope_id": env.get("task_id") or env.get("envelope_id"),
        "task_id": env.get("task_id") or env.get("envelope_id"),
        "sender": env.get("sender"),
        "receiver": env.get("target") or env.get("receiver"),
        "target": env.get("target") or env.get("receiver"),
        "action": env.get("action"),
        "handoff": env.get("handoff"),
        "payload": env.get("payload") or env.get("payload_ref"),
        "payload_ref": env.get("payload_ref") or env.get("payload"),
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "errors": [],
        "warnings": [],
    }
    eid = rep["envelope_id"] or ""
    sender = rep["sender"] or ""
    receiver = rep["receiver"] or ""
    action = rep["action"] or ""

    if not ENV_ID_RE.match(eid):
        rep["errors"].append(f"envelope_id/task_id fora do padrão ENV-NNN/TA-NNN: {eid!r}")
    if sender not in KNOWN_SLUGS:
        rep["errors"].append(f"sender fora da topologia: {sender!r}")
    if receiver not in KNOWN_SLUGS:
        rep["errors"].append(f"receiver/target fora da topologia: {receiver!r}")
    if sender == receiver:
        rep["errors"].append(f"auto-delegacao proibida: {sender!r}")
    if action not in VALID_ACTIONS:
        rep["errors"].append(f"ação inválida: {action!r}")
    handoff = rep["handoff"]
    if handoff is not None and not HANDOFF_RE.match(str(handoff)):
        rep["errors"].append(f"handoff fora do padrão: {handoff!r}")
    elif handoff is not None and HANDOFF_RE.match(str(handoff)):
        handoff_path = Path(".ai/handoffs") / f"{handoff}.md"
        if not handoff_path.exists():
            rep["errors"].append(f"handoff .md ausente: {handoff_path}")

    # reply_required: deve ser verdadeiro para half-duplex fechar ciclo
    reply_required = env.get("reply_required", True)
    if not reply_required:
        rep["warnings"].append("reply_required=False: parcela de retorno não esperada")

    # camada do receiver deve ser compatível (L3 só recebe de L0/L1/L2, nunca de META para execução)
    r_layer = _layer_of(receiver)
    s_layer = _layer_of(sender)
    if r_layer == "L3" and s_layer == "META":
        rep["warnings"].append("META -> L3 comunicação indireta: passar pelo L0 orchestrator")

    if rep["errors"]:
        rep["status"] = "rejeitado"
    return rep


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Hub de comunicacao half-duplex COGME")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", help="arquivo envelope JSON para validar")
    group.add_argument("--template", action="store_true",
                       help="imprime envelope de exemplo")
    args = parser.parse_args()

    if args.template:
        template = {
            "envelope_id": "ENV-0001",
            "sender": "agent-nexus-prime-ultimate",
            "receiver": "agent-qa-sdet",
            "action": "test",
            "handoff": "HF-0010",
            "payload_ref": ".ai/handoffs/HF-0010.md",
            "kill_switch": "inherited",
            "reply_required": True,
        }
        print(json.dumps(template, indent=2, ensure_ascii=False))
        return 0

    path = Path(args.check)
    if not path.exists():
        print(json.dumps({"status": "rejeitado",
                          "errors": [f"envelope inexistente: {args.check}"]},
                         ensure_ascii=False))
        return 1
    try:
        env = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(json.dumps({"status": "rejeitado", "errors": [f"JSON invalido: {exc}"]},
                         ensure_ascii=False))
        return 1

    rep = validate_envelope(env)
    rep["kill_switch"] = "inherited"
    print(json.dumps(rep, indent=2, ensure_ascii=False))
    return 0 if rep["status"] == "aceito" else 1


if __name__ == "__main__":
    sys.exit(main())
