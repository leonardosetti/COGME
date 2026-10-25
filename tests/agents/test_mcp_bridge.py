"""Test suite do mcp_bridge.py (FASE S.6, ONDA 8 — stub futuro)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "mcp_bridge.py"


def run_mcp(extra_args=()):
    r = subprocess.run(
        [sys.executable, str(SCRIPT), *extra_args],
        capture_output=True, text=True, timeout=30, cwd=str(ROOT),
    )
    try:
        payload = json.loads(r.stdout)
    except json.JSONDecodeError:
        payload = {"raw": r.stdout, "stderr": r.stderr}
    return r.returncode, payload


class TestMcpBridge:
    def test_mcp_report_structure(self):
        rc, payload = run_mcp()
        assert rc == 0
        assert payload["mcp_bridge_version"].startswith("0.1.0")
        assert "capable_agents" in payload
        assert "known_slugs" in payload
        assert "transport" in payload

    def test_list_capable(self):
        r = subprocess.run(
            [sys.executable, str(SCRIPT), "--list-capable"],
            capture_output=True, text=True, timeout=30, cwd=str(ROOT),
        )
        payload = json.loads(r.stdout)
        assert "capable" in payload
        assert r.returncode == 0

    def test_validate_known_slug(self):
        rc, payload = run_mcp(["--validate-slug", "agent-nexus-prime-ultimate"])
        assert payload["known"] is True
        assert isinstance(payload["mcp_capable"], bool)

    def test_validate_unknown_slug(self):
        rc, payload = run_mcp(["--validate-slug", "agent-inexistente"])
        assert payload["known"] is False
        assert payload["mcp_capable"] is False
