"""Testes adversariais para os ajustes de saneamento do ecossistema COGME.

Cobre: ledger_append com exit_status=0 (causa raiz das 7 falhas),
envelope legacy no hub de comunicacao, reply_required nao-booleano no delivery,
filtro agent-* no registro, log de uso MCP.
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / ".ai/deprecated/mcp-nexus"))

import yaml  # noqa: E402

from mcp_nexus_ledger import handle as ledger_handle  # noqa: E402
from agent_communication_hub import validate_envelope  # noqa: E402
from nexus_delivery import validate_task_for_delivery  # noqa: E402
from mcp_usage_log import log_usage  # noqa: E402


def ledger_call(task_id, sender, receiver, action, status, exit_status, notes):
    req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "ledger_append",
            "arguments": {
                "task_id": task_id,
                "sender": sender,
                "receiver": receiver,
                "action": action,
                "status": status,
                "exit_status": exit_status,
                "notes": notes,
            },
        },
    }
    return ledger_handle(req)


def test_ledger_exit_status_zero_aceito():
    """Causa raiz: exit_status=0 era rejeitado por 'not args.get(k)'."""
    resp = ledger_call("TA-ADV-001", "agent-nexus-prime-ultimate",
                       "agent-project-auditor", "audit", "accepted", 0, "ok")
    assert resp.get("error") is None, resp


def test_ledger_campos_ausentes_rejeitado():
    resp = ledger_call("TA-ADV-002", "agent-nexus-prime-ultimate",
                       "agent-project-auditor", "audit", "accepted", None, "ok")
    assert resp["error"] is not None
    assert "exit_status" in resp["error"]["message"]


def test_ledger_exit_status_texto_rejeitado():
    resp = ledger_call("TA-ADV-003", "agent-nexus-prime-ultimate",
                       "agent-project-auditor", "audit", "accepted", "zero", "ok")
    assert resp["error"] is not None


def test_hub_envelope_legacy_mapeado():
    """envelope_id/receiver/payload_ref (legacy) deve virar task_id/target/payload."""
    env = {
        "envelope_id": "TA-0999",
        "sender": "agent-nexus-prime-ultimate",
        "receiver": "agent-project-auditor",
        "payload_ref": ".ai/handoffs/HF-0010.md",
        "action": "audit",
        "handoff": "HF-0010",
    }
    rep = validate_envelope(env)
    assert rep["status"] == "aceito", rep["errors"]
    assert rep["task_id"] == "TA-0999"
    assert rep["target"] == "agent-project-auditor"
    assert rep["payload"] == ".ai/handoffs/HF-0010.md"


def test_hub_auto_delegacao_rejeitada():
    env = {
        "task_id": "TA-ADV-011",
        "sender": "agent-nexus-prime-ultimate",
        "receiver": "agent-nexus-prime-ultimate",
        "action": "audit",
        "handoff": "HF-0010",
    }
    rep = validate_envelope(env)
    assert rep["status"] == "rejeitado"
    assert any("auto-delegacao" in e for e in rep["errors"]), rep["errors"]


def test_hub_acao_invalida_rejeitada():
    env = {
        "task_id": "TA-ADV-012",
        "sender": "agent-nexus-prime-ultimate",
        "receiver": "agent-project-auditor",
        "action": "acao-inexistente",
        "handoff": "HF-0010",
    }
    rep = validate_envelope(env)
    assert rep["status"] == "rejeitado"


def test_delivery_reply_required_nao_booleano_rejeitado():
    task = {
        "task_id": "TA-ADV-020",
        "sender": "agent-nexus-prime-ultimate",
        "target": "agent-project-auditor",
        "action": "audit",
        "reply_required": "sim",
    }
    ok, errors = validate_task_for_delivery(task)
    assert not ok
    assert any("reply_required" in e for e in errors), errors


def test_delivery_task_id_fora_padrao_rejeitado():
    task = {
        "task_id": "X-1",
        "sender": "agent-nexus-prime-ultimate",
        "target": "agent-project-auditor",
        "action": "audit",
        "reply_required": True,
    }
    ok, errors = validate_task_for_delivery(task)
    assert not ok
    assert any("TA-NNN" in e for e in errors), errors


def test_registro_filtra_apenas_agent():
    """gsd-* nao conta como agente COGME (Art. 4.2)."""
    from validate_nexus_yaml import KNOWN_SLUGS
    gsd = [s for s in KNOWN_SLUGS if s.startswith("gsd-")]
    assert gsd == [], f"gsd-* vazou para KNOWN_SLUGS: {gsd}"
    agent = [s for s in KNOWN_SLUGS if s.startswith("agent-")]
    assert "agent-nexus-prime-ultimate" in agent


def test_usage_log_grava_jsonl():
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".jsonl")
    tmp.close()
    try:
        import mcp_usage_log as m
        m.LOG = Path(tmp.name)
        log_usage("mcp-test", "tools/call", "ledger_append", True, None)
        log_usage("mcp-test", "tools/call", "ledger_append", False,
                  "campo ausente")
        lines = Path(tmp.name).read_text(encoding="utf-8").splitlines()
        assert len(lines) == 2
        a = json.loads(lines[0])
        b = json.loads(lines[1])
        assert a["ok"] is True and a["error"] is None
        assert b["ok"] is False and b["error"] == "campo ausente"
    finally:
        os.unlink(tmp.name)


if __name__ == "__main__":
    import traceback
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    falhou = 0
    for t in tests:
        try:
            t()
            print(f"OK   {t.__name__}")
        except Exception as exc:  # noqa: BLE001
            falhou += 1
            print(f"FALHA {t.__name__}: {exc}")
            traceback.print_exc()
    print(f"\n{len(tests)} testes, {falhou} falha(s)")
    sys.exit(1 if falhou else 0)
