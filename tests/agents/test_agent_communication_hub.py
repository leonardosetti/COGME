"""Test suite do agent_communication_hub.py (FASE S.6, ONDA 8)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "agent_communication_hub.py"


def run_hub(tmp_path, envelope: dict, extra_args=()):
    f = tmp_path / "envelope.json"
    f.write_text(json.dumps(envelope, ensure_ascii=False), encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(SCRIPT), "--check", str(f), *extra_args],
        capture_output=True, text=True, timeout=30, cwd=str(ROOT),
    )
    try:
        payload = json.loads(r.stdout)
    except json.JSONDecodeError:
        payload = {"raw": r.stdout, "stderr": r.stderr}
    return r.returncode, payload


class TestCommunicationHub:
    def test_valid_envelope_accepted(self, tmp_path):
        env = {
            "envelope_id": "ENV-0001",
            "sender": "agent-nexus-prime-ultimate",
            "receiver": "agent-sdd-specialist",
            "action": "spec",
            "handoff": "HF-0010",
            "payload_ref": ".ai/handoffs/HF-0010.md",
        }
        rc, rep = run_hub(tmp_path, env)
        assert rc == 0, json.dumps(rep, ensure_ascii=False)[:400]
        assert rep["status"] == "aceito"
        assert rep["kill_switch"] == "inherited"

    def test_self_delegation_rejected(self, tmp_path):
        env = {
            "envelope_id": "ENV-0002",
            "sender": "agent-nexus-prime-ultimate",
            "receiver": "agent-nexus-prime-ultimate",
            "action": "orchestrate",
        }
        rc, rep = run_hub(tmp_path, env)
        assert rc == 1
        assert rep["status"] == "rejeitado"
        assert any("auto-delegacao" in e for e in rep["errors"])

    def test_unknown_sender_rejected(self, tmp_path):
        env = {
            "envelope_id": "ENV-0003",
            "sender": "agent-inexistente",
            "receiver": "agent-sdd-specialist",
            "action": "spec",
        }
        rc, rep = run_hub(tmp_path, env)
        assert rc == 1
        assert rep["status"] == "rejeitado"

    def test_invalid_action_rejected(self, tmp_path):
        env = {
            "envelope_id": "ENV-0004",
            "sender": "agent-nexus-prime-ultimate",
            "receiver": "agent-sdd-specialist",
            "action": "meditar",
        }
        rc, rep = run_hub(tmp_path, env)
        assert rc == 1
        assert rep["status"] == "rejeitado"

    def test_bad_envelope_id_rejected(self, tmp_path):
        env = {
            "envelope_id": "INVALID",
            "sender": "agent-nexus-prime-ultimate",
            "receiver": "agent-sdd-specialist",
            "action": "spec",
        }
        rc, rep = run_hub(tmp_path, env)
        assert rc == 1
        assert rep["status"] == "rejeitado"

    def test_template_output(self):
        r = subprocess.run(
            [sys.executable, str(SCRIPT), "--template"],
            capture_output=True, text=True, timeout=30, cwd=str(ROOT),
        )
        payload = json.loads(r.stdout)
        assert payload["envelope_id"].startswith("ENV-")
        assert payload["sender"] == "agent-nexus-prime-ultimate"
        assert r.returncode == 0
