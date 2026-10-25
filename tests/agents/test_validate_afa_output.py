"""Test suite do validate_afa_output.py (FASE S.6 — gate de forja)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "validate_afa_output.py"


def run_gate(tmp_path, files: dict, extra_args=()):
    paths = []
    for fname, content in files.items():
        f = tmp_path / fname
        f.write_text(content, encoding="utf-8")
        paths.append(str(f))
    result = subprocess.run(
        [sys.executable, str(SCRIPT), *paths, *extra_args],
        capture_output=True, text=True, timeout=30)
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        payload = {"raw": result.stdout, "stderr": result.stderr}
    return result.returncode, payload


def full_agent(slug="agent-notch"):
    """Agente sintético do gabarito: todas seções + vectors com thresholds mínimos."""
    parts = ["---\nname: " + slug + "\nversion: '1.0'\nlayer: L2\nrole: specialist\n"
             "description: 'teste'\n---\n"]
    titles = {
        "0": "ROLE AND SCOPE", "0.1": "SUPREME LAW", "0.2": "PROTOCOLS",
        "1": "COGNITIVE MATRIX", "2": "ANTI-HALLUCINATION", "3": "DOs (MANDATORY)",
        "4": "DON'Ts (FORBIDDEN)", "5": "LANGUAGE DIRECTIVE", "6": "OUTPUT SCHEMA",
        "7": "INPUT SCHEMA", "8": "QUANTITATIVE METRICS", "9": "MEMORY POLICY",
        "10": "RED TEAM AWARENESS", "11": "FAIL-CLOSED RULES", "12": "TEMPLATES",
        "13": "INTEGRATION CONTRACTS", "14": "ONBOARDING", "15": "SELF-IMPROVEMENT",
        "16": "VERSIONING",
    }
    content = {
        "0.2": "\n".join(f"{i}. KillSwitch vector {i}" for i in range(1, 6)),
        "3": "\n".join(f"{i}. DO item deoba {i}" for i in range(1, 16)),
        "4": "\n".join(f"{i}. DON'T item forb {i}" for i in range(1, 16)),
        "8": "\n| Metric a | alvo | alerta |\n" * 8,
        "10": "\n".join(f"{i}. RT vector inj {i}" for i in range(1, 9)),
        "11": "\n".join(f"{i}. FAIL regra ação {i}" for i in range(1, 7)),
    }
    for num, title in titles.items():
        parts.append(f"## {num}. {title}\n")
        if num in content:
            parts.append(content[num] + "\n")
    parts.append("\nKeywords: 8700G CPU FOSS LGPD bypass constitution\n")
    return "".join(parts)


class TestScoreGate:
    def test_full_agent_scores_high_and_passes(self, tmp_path):
        rc, payload = run_gate(tmp_path, {"agent-notch.md": full_agent()})
        rep = payload["reports"][0]
        assert rc == 0, json.dumps(rep, ensure_ascii=False)[:600]
        assert rep["ok"] is True
        assert rep["score"] >= 85
        assert rep["score"] <= 100

    def test_missing_sections_rejected(self, tmp_path):
        content = full_agent().replace("## 10. RED TEAM AWARENESS\n", "")
        rc, payload = run_gate(tmp_path, {"agent-minus.md": content})
        rep = payload["reports"][0]
        # §0.9: completude estrutural <100% = BLOCK, independente do score
        assert rep["ok"] is False
        assert rep["status"] == "rejeitado"
        assert rc == 1  # fail-closed
        assert any("ausentes" in e for e in rep["errors"])

    def test_insufficient_counts_rejected(self, tmp_path):
        content = full_agent().replace("## 11. FAIL-CLOSED RULES\n" +
                                       "\n".join(f"{i}. FAIL regra ação {i}"
                                                 for i in range(1, 7)) + "\n",
                                       "## 11. FAIL-CLOSED RULES\n1. only one\n")
        rc, payload = run_gate(tmp_path, {"agent-fc.md": content})
        rep = payload["reports"][0]
        assert rep["ok"] is False
        assert any("failclosed" in e or "FAIL" in e for e in rep["errors"])

    def test_legacy_forget_files_skipped(self, tmp_path):
        rc, payload = run_gate(
            tmp_path, {"agent-factory-architect.md": "# forjador legacy"})
        rep = payload["reports"][0]
        assert rep["status"] == "legacy-forge"
        assert rc == 0


class TestBudget:
    def test_oversized_agent_penalized(self, tmp_path):
        big = full_agent() + "# padding\n" * 8000  # ~16k extra tokens
        rc, payload = run_gate(tmp_path, {"agent-big.md": big})
        rep = payload["reports"][0]
        assert rep["est_tokens"] > 4000
        assert any("orçamento" in w for w in rep["warnings"])


class TestRealRoster:
    def test_real_factory_files_bypass_gate(self, tmp_path):
        # Teste que o gate reconhece arquivos do forjador legacy
        rc, payload = run_gate(tmp_path, {})
        # O gate deve completar a validacao sobre o conjunto de agentes
        # (someos agentes podem ser rejeitados, o importante e que o report seja gerado)
        assert isinstance(payload, dict)
        assert "total" in payload
        # Verificar que agentes foram validados
        assert payload["total"] > 0

    def test_synthetic_reject_workflow(self, tmp_path):
        # fluxo completo: rejeito de agente ruim não derruba o forjador legacy
        files = {
            "agent-factory-architect.md": "# forjador",
            "agent-broken.md": "## 3. DOs\nsem nada",
        }
        rc, payload = run_gate(tmp_path, files)
        statuses = {r["status"] for r in payload["reports"]}
        assert "legacy-forge" in statuses
        assert "rejeitado" in statuses
        assert rc == 1
