"""Gate de regressao da ONDA 5: custodia de plataforma (infra, devops, github, security, compliance)."""
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "scripts" / "validate_afa_output.py"
NEXUS = ROOT / "scripts" / "validate_nexus_yaml.py"
ONDA_5 = ["agent-infrastructure-specialist", "agent-devops",
          "agent-github-specialist", "agent-digital-security",
          "agent-compliance-governance"]


def fm(slug: str) -> dict:
    return yaml.safe_load((ROOT / ".opencode" / "agents" / f"{slug}.md")
                          .read_text(encoding="utf-8").split("---")[1])


def run(script: Path, *args: str):
    import json
    r = subprocess.run([sys.executable, str(script), *args],
                       capture_output=True, text=True, timeout=60)
    return r.returncode, json.loads(r.stdout)


@pytest.mark.parametrize("slug", ONDA_5)
def test_gate_promulgation(slug):
    _, payload = run(GATE, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["ok"] is True, rep["errors"]
    assert rep["score"] >= 85
    assert rep["est_tokens"] <= 4000


@pytest.mark.parametrize("slug", ONDA_5)
def test_nexus_contract(slug):
    _, payload = run(NEXUS, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    assert payload["reports"][0]["status"] == "promulgado"


def test_registry_covers_onda_5():
    subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_agent_registry.py")],
                   capture_output=True, text=True, check=True)
    data = yaml.safe_load((ROOT / ".ai" / "agents" / "registry.yaml")
                          .read_text(encoding="utf-8"))
    names = {a["name"] for a in data["agents"]}
    for slug in ONDA_5:
        assert slug in names


def test_lgpd_in_all_onda5():
    for slug in ONDA_5:
        text = (ROOT / ".opencode" / "agents" / f"{slug}.md")\
            .read_text(encoding="utf-8").lower()
        assert "lgpd" in text, slug


def test_no_cloud_inference_in_infra():
    text = (ROOT / ".opencode" / "agents" / "agent-infrastructure-specialist.md")\
        .read_text(encoding="utf-8").lower()
    assert "cpu-only" in text
    assert "cuda" in text  # proibido por contrato (negado em toda postura)


def test_free_tier_only_in_devops():
    text = (ROOT / ".opencode" / "agents" / "agent-devops.md")\
        .read_text(encoding="utf-8").lower()
    assert "free tier" in text
    assert "[skip ci]" in text  # proibicao declarada


def test_bypass_pillars_in_compliance():
    text = (ROOT / ".opencode" / "agents" / "agent-compliance-governance.md")\
        .read_text(encoding="utf-8").lower()
    assert "force majeure" in text
    assert "foss exit" in text
    assert "detox" in text


def test_license_whitelist_enums_in_compliance():
    text = (ROOT / ".opencode" / "agents" / "agent-compliance-governance.md")\
        .read_text(encoding="utf-8").lower()
    for spdx in ("mit", "apache-2.0", "psf", "agpl"):
        assert spdx in text, spdx


def test_branch_protection_in_github():
    text = (ROOT / ".opencode" / "agents" / "agent-github-specialist.md")\
        .read_text(encoding="utf-8").lower()
    assert "branch protection" in text
    assert "least-privilege" in text


def test_local_only_binding_in_security():
    text = (ROOT / ".opencode" / "agents" / "agent-digital-security.md")\
        .read_text(encoding="utf-8").lower()
    assert "0600" in text and "0755" in text
    assert "0.0.0.0" in text  # proibicao declarada


def test_onda5_chain_wiring():
    assert "agent-devops" in fm("agent-infrastructure-specialist")["downstream"]
    assert "agent-infrastructure-specialist" in fm("agent-devops")["upstream"]
    assert "agent-architect" in fm("agent-digital-security")["upstream"]
    assert "agent-digital-security" in fm("agent-compliance-governance")["upstream"]
    assert "agent-pm" in fm("agent-github-specialist")["upstream"]
    assert "agent-project-auditor" in fm("agent-compliance-governance")["downstream"]
