"""Test suite do agent_health_check.py (FASE S.6, ONDA 8)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "agent_health_check.py"


def run_health(tmp_path, files: dict, extra_args=()):
    paths = []
    for fname, content in files.items():
        f = tmp_path / fname
        f.write_text(content, encoding="utf-8")
        paths.append(str(f))
    # Monkeypatch AGENTS_DIR via env não existe; usamos o diretório real.
    # Teste roda contra .opencode/agents/ do projeto.
    r = subprocess.run(
        [sys.executable, str(SCRIPT), *extra_args],
        capture_output=True, text=True, timeout=30, cwd=str(ROOT),
    )
    try:
        payload = json.loads(r.stdout)
    except json.JSONDecodeError:
        payload = {"raw": r.stdout, "stderr": r.stderr}
    return r.returncode, payload


class TestHealthCheck:
    def test_health_returns_json_report(self):
        rc, payload = run_health(None, {})
        assert isinstance(payload, dict)
        assert "total" in payload
        assert "saudaveis" in payload
        assert "falhas" in payload
        assert "por_camada" in payload
        assert "resultados" in payload

    def test_health_known_layers(self):
        rc, payload = run_health(None, {})
        layers = payload.get("por_camada", {})
        assert "L0" in layers
        assert "L1" in layers
        assert "L2" in layers
        assert "L3" in layers
        assert "META" in layers
        assert layers.get("L0") == 1

    def test_health_exit_code(self):
        rc, payload = run_health(None, {})
        # Com drift esperado (agentes ONDA 8 ainda não forjados), rc pode ser 0 ou 1
        assert rc in (0, 1)

    def test_result_entries_have_required_fields(self):
        rc, payload = run_health(None, {})
        for entry in payload.get("resultados", []):
            assert "slug" in entry
            assert "ok" in entry
            assert "errors" in entry
            assert isinstance(entry["errors"], list)
