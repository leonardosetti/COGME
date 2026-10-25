"""Test suite do registry_drift_monitor.py (FASE S.6, ONDA 8)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "registry_drift_monitor.py"


def run_drift(extra_args=()):
    r = subprocess.run(
        [sys.executable, str(SCRIPT), *extra_args],
        capture_output=True, text=True, timeout=30, cwd=str(ROOT),
    )
    try:
        payload = json.loads(r.stdout)
    except json.JSONDecodeError:
        payload = {"raw": r.stdout, "stderr": r.stderr}
    return r.returncode, payload


class TestRegistryDriftMonitor:
    def test_drift_returns_json_report(self):
        rc, payload = run_drift()
        assert isinstance(payload, dict)
        assert "disco" in payload
        assert "topologia" in payload
        assert "registry" in payload
        assert "drift" in payload
        assert "drift_detectado" in payload

    def test_drift_has_expected_keys(self):
        rc, payload = run_drift()
        d = payload["drift"]
        for key in ("orfao_no_disco_nao_na_topologia",
                    "nao_forjado_na_topologia",
                    "fantasma_no_registry_nao_no_disco",
                    "nao_sincronizado_no_disco_nao_no_registry"):
            assert key in d
            assert isinstance(d[key], list)

    def test_exit_code(self):
        rc, payload = run_drift()
        # Drift esperado: novos slugs na topologia ainda nao forjados
        assert rc in (0, 1)
