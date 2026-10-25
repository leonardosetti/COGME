"""Test suite do dag_validator.py (FASE S.6, ONDA 8)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "dag_validator.py"


def run_dag(extra_args=()):
    r = subprocess.run(
        [sys.executable, str(SCRIPT), *extra_args],
        capture_output=True, text=True, timeout=30, cwd=str(ROOT),
    )
    # stdout pode conter JSON seguido de linha de resumo [DAG] ...; extrai apenas o JSON.
    stdout = r.stdout
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError:
        # tenta extrair o objeto JSON entre a primeira '{' e a ultima '}'
        start = stdout.find("{")
        end = stdout.rfind("}") + 1
        if start >= 0 and end > start:
            payload = json.loads(stdout[start:end])
        else:
            payload = {"raw": stdout, "stderr": r.stderr}
    return r.returncode, payload


class TestDagValidator:
    def test_dag_returns_json_report(self):
        rc, payload = run_dag()
        assert isinstance(payload, dict)
        assert "topologia_valida" in payload
        assert "total_slugs" in payload
        assert "por_camada" in payload
        assert "erros" in payload
        assert "avisos" in payload

    def test_dag_is_acyclic(self):
        rc, payload = run_dag()
        assert payload["topologia_valida"] is True, \
            f"DAG deve ser aciclica; erros: {payload.get('erros')}"
        assert payload["erros"] == []

    def test_l0_has_exactly_one_orchestrator(self):
        rc, payload = run_dag()
        layers = payload["por_camada"]
        assert layers.get("L0") == 1

    def test_total_slugs_matches_topology(self):
        rc, payload = run_dag()
        assert payload["total_slugs"] >= 25
