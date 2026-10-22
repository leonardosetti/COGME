"""Test suite do handoff_parser.py (FASE S.6)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "handoff_parser.py"

GOOD = """---
id: HF-001
agent: agent-backend-dev
status: ready
created: 2026-10-22
---
# Handoff: implementar rota de conversão

## Contexto

Cotação USD→BRL vinda do cache.
## Tarefa

Implementar `POST /simulate`.
## Critérios de Aceite
- [x] schema validado
- [ ] cobertura ≥ 80%
## Restrições

Nada de dependência nova.
"""


def run_parser(tmp_path, files: dict, extra_args=()):
    paths = []
    for fname, content in files.items():
        f = tmp_path / fname
        f.write_text(content, encoding="utf-8")
        paths.append(str(f))
    result = subprocess.run([sys.executable, str(SCRIPT), *paths, *extra_args],
                            capture_output=True, text=True, timeout=30)
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        payload = {"raw": result.stdout, "stderr": result.stderr}
    return result.returncode, payload


class TestHappyPath:
    def test_good_handoff_parses(self, tmp_path):
        rc, payload = run_parser(tmp_path, {"HF-001.md": GOOD})
        h = payload["handoffs"][0]
        assert rc == 0
        assert h["ok"] is True
        assert h["meta"]["id"] == "HF-001"
        assert h["meta"]["agent"] == "agent-backend-dev"
        assert len(h["acceptance"]) == 2
        assert h["acceptance"][0]["done"] is True
        assert h["acceptance"][1]["done"] is False
        assert "Tarefa" in h["sections"]

    def test_dir_mode(self, tmp_path):
        d = tmp_path / "handoffs"
        d.mkdir()
        (d / "HF-001.md").write_text(GOOD, encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--dir", str(d)],
            capture_output=True, text=True, timeout=30)
        payload = json.loads(result.stdout)
        assert result.returncode == 0
        assert payload["total"] == 1


class TestFailClosed:
    def test_bad_status_rejected(self, tmp_path):
        rc, payload = run_parser(tmp_path,
                                 {"HF-002.md": GOOD.replace("status: ready", "status: livewire")})
        assert rc == 1
        assert any("status" in e for e in payload["handoffs"][0]["errors"])

    def test_missing_criteria_rejected(self, tmp_path):
        rc, payload = run_parser(tmp_path,
                                 {"HF-003.md": GOOD.replace("- [x] schema validado\n- [ ] cobertura ≥ 80%\n", "")})
        assert rc == 1

    def test_no_checkbox_criteria_rejected(self, tmp_path):
        stripped = "\n".join(ln for ln in GOOD.splitlines() if not ln.startswith("- ["))
        rc, payload = run_parser(tmp_path, {"HF-004.md": stripped})
        assert rc == 1

    def test_future_date_warns_not_fails(self, tmp_path):
        rc, payload = run_parser(tmp_path,
                                 {"HF-005.md": GOOD.replace("created: 2026-10-22", "created: 2999-01-01")})
        h = payload["handoffs"][0]
        assert rc == 0
        assert any("futuro" in w for w in h["warnings"])

    def test_absent_file_rejected(self, tmp_path):
        rc, payload = run_parser(tmp_path, {})
        assert rc == 1

    def test_no_target_digits_id_fails(self, tmp_path):
        rc, payload = run_parser(tmp_path,
                                 {"HF-01.md": GOOD.replace("id: HF-001", "id: HF-01")})
        assert rc == 1
