"""Test suite do validate_nexus_yaml.py (FASE S.6 — gate da FASE S).

Execução:
  python3 -m pytest tests/agents/ -v
  python3 -m unittest discover -s tests/agents -v
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "validate_nexus_yaml.py"


def run_validator(tmp_path, files: dict, extra_args=()):
    """Escreve arquivos fake em sandbox e roda o validador sobre eles."""
    paths = []
    for fname, content in files.items():
        f = tmp_path / fname
        f.write_text(content, encoding="utf-8")
        paths.append(str(f))
    result = subprocess.run(
        [sys.executable, str(SCRIPT), *paths, *extra_args],
        capture_output=True, text=True, timeout=30
    )
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        payload = {"raw": result.stdout, "stderr": result.stderr}
    return result.returncode, payload


GOOD_CONTRACT = """---
name: agent-x
version: "1.0.0"
layer: L2
role: specialist
description: "Agente de teste sintético do pipeline."
upstream: []
downstream: []
---
# CORPO

Conteúdo livre.
"""

MISSING_KEYS = """---
name: agent-y
layer: L2
---
corpo
"""

CONTRACT_BODY = (
    "---\nname: agent-z\nversion: \"1.0\"\nlayer: L9\nrole: guru\n"
    "description: \"x\"\nupstream: agent-z\n---\ncorpo\n"
)


class TestContractValidation:
    def test_valid_contract_is_promulgated(self, tmp_path):
        rc, payload = run_validator(tmp_path, {"agent-x.md": GOOD_CONTRACT})
        rep = payload["reports"][0]
        assert rep["ok"] is True
        assert rep["status"] == "promulgado"
        assert rc == 0

    def test_missing_required_keys_is_rejected(self, tmp_path):
        rc, payload = run_validator(tmp_path, {"agent-y.md": MISSING_KEYS})
        rep = payload["reports"][0]
        assert rep["ok"] is False
        assert any("version" in e or "role" in e or "description" in e
                   for e in rep["errors"])
        assert rc == 1  # fail-closed

    def test_bad_layer_and_role_rejected(self, tmp_path):
        rc, payload = run_validator(tmp_path, {"agent-z.md": CONTRACT_BODY})
        rep = payload["reports"][0]
        assert rep["ok"] is False
        assert any("layer" in e for e in rep["errors"])
        assert any("role" in e for e in rep["errors"])
        assert rc == 1

    def test_missing_prefix_agent_rejected(self, tmp_path):
        bad = GOOD_CONTRACT.replace("name: agent-x", "name:_{agente}".replace("_", " "), 1)
        rc, payload = run_validator(tmp_path, {"agent-x.md": bad})
        assert rc == 1

    def test_self_reference_rejected(self, tmp_path):
        bad = GOOD_CONTRACT.replace("upstream: []", "upstream: [agent-x]")
        rc, payload = run_validator(tmp_path, {"agent-x.md": bad})
        rep = payload["reports"][0]
        assert rep["ok"] is False
        assert any("auto-referência" in e for e in rep["errors"])


class TestLegacyTolerance:
    def test_forge_legacy_without_frontmatter_warns_but_passes(self, tmp_path):
        # permite nome iniciar sem agent-: slug forçado como agent-factory-architect
        rc, payload = run_validator(
            tmp_path, {"agent-factory-architect.md": "# SYSTEM DIRECTIVE: AFA"})
        rep = payload["reports"][0]
        assert rep["status"] == "legacy-forge"
        assert rep["ok"] is True
        assert rc == 0

    def test_strict_all_breaks_legacy(self, tmp_path):
        rc, payload = run_validator(
            tmp_path, {"agent-factory-architect.md": "# SYSTEM DIRECTIVE: AFA"},
            extra_args=("--strict-all",))
        assert rc == 1


class TestRealScaffold:
    """Telas reais do projeto: o forjador e o archive devem validar em prod."""

    def test_current_roster_validates_against_project(self, tmp_path):
        rc, payload = run_validator(tmp_path, {})
        assert rc == 0, json.dumps(payload, ensure_ascii=False)[:400]
        # Verificar roster contra o projeto
        import validate_nexus_yaml as v
        known = v.KNOWN_SLUGS
        assert "agent-nexus-prime-ultimate" in known
        assert len(known) >= 24  # 24 agentes do plano consolidado

    def test_topology_is_complete(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import validate_nexus_yaml as v
        known = v.KNOWN_SLUGS

        assert len(known) >= 25  # 25 agentes do plano consolidado + forjador


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
