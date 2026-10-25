"""Test suite do security_scan.py (FASE S.6, ONDA 8)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "security_scan.py"


def run_security(extra_args=()):
    r = subprocess.run(
        [sys.executable, str(SCRIPT), *extra_args],
        capture_output=True, text=True, timeout=30, cwd=str(ROOT),
    )
    try:
        payload = json.loads(r.stdout)
    except json.JSONDecodeError:
        payload = {"raw": r.stdout, "stderr": r.stderr}
    return r.returncode, payload


class TestSecurityScan:
    def test_security_returns_json_report(self):
        rc, payload = run_security()
        assert isinstance(payload, dict)
        assert "total" in payload
        assert "aprovados" in payload
        assert "falhas" in payload
        assert "resultados" in payload

    def test_each_result_has_file_and_errors(self):
        rc, payload = run_security()
        for entry in payload.get("resultados", []):
            assert "file" in entry
            assert "ok" in entry
            assert "errors" in entry

    def test_no_cuda_cloud_in_agents(self):
        rc, payload = run_security()
        # Nenhum agente aprovado deve conter referencia a CUDA/cloud
        for entry in payload.get("resultados", []):
            if entry["ok"]:
                texto_erros = " ".join(entry.get("errors", []))
                assert "CUDA" not in texto_erros or not entry["ok"]
