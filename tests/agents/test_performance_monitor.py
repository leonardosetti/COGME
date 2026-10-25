"""Test suite do performance_monitor.py (FASE S.6, ONDA 8)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "performance_monitor.py"


def run_perf(extra_args=()):
    r = subprocess.run(
        [sys.executable, str(SCRIPT), *extra_args],
        capture_output=True, text=True, timeout=30, cwd=str(ROOT),
    )
    try:
        payload = json.loads(r.stdout)
    except json.JSONDecodeError:
        payload = {"raw": r.stdout, "stderr": r.stderr}
    return r.returncode, payload


class TestPerformanceMonitor:
    def test_perf_returns_json_report(self):
        rc, payload = run_perf()
        assert isinstance(payload, dict)
        assert "total" in payload
        assert "dentro_orcamento" in payload
        assert "fora_orcamento" in payload
        assert "token_budget" in payload
        assert payload["token_budget"] == 4000

    def test_each_result_has_metrics(self):
        rc, payload = run_perf()
        for entry in payload.get("resultados", []):
            assert "slug" in entry
            assert "metrics" in entry
            m = entry["metrics"]
            assert "est_tokens" in m
            assert "missing_sections" in m

    def test_no_section_missing_for_valid_agents(self):
        rc, payload = run_perf()
        for entry in payload.get("resultados", []):
            if entry["ok"]:
                assert entry["metrics"]["missing_sections"] == []
