"""Test suite do rag_indexer.py (FASE S.6, ONDA 8 — stub futuro)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "rag_indexer.py"


def run_rag(extra_args=()):
    r = subprocess.run(
        [sys.executable, str(SCRIPT), *extra_args],
        capture_output=True, text=True, timeout=30, cwd=str(ROOT),
    )
    try:
        payload = json.loads(r.stdout)
    except json.JSONDecodeError:
        payload = {"raw": r.stdout, "stderr": r.stderr}
    return r.returncode, payload


class TestRagIndexer:
    def test_rag_report_structure(self):
        rc, payload = run_rag()
        assert rc == 0
        assert payload["rag_indexer_version"].startswith("0.1.0")
        assert "corpus_count" in payload
        assert isinstance(payload["corpus_count"], int)
        assert payload["corpus_count"] > 0
        assert "entries" in payload

    def test_list_corpus(self):
        r = subprocess.run(
            [sys.executable, str(SCRIPT), "--list-corpus"],
            capture_output=True, text=True, timeout=30, cwd=str(ROOT),
        )
        payload = json.loads(r.stdout)
        assert "entries" in payload
        assert len(payload["entries"]) > 0
        for entry in payload["entries"]:
            assert "source" in entry
            assert "type" in entry
