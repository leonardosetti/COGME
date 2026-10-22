"""Gate de regressao da ONDA 6: linha de veredito (qa-sdet, reviewer, gatekeeper, auditor)."""
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "scripts" / "validate_afa_output.py"
NEXUS = ROOT / "scripts" / "validate_nexus_yaml.py"
ONDA_6 = ["agent-qa-sdet", "agent-reviewer", "agent-gatekeeper",
          "agent-project-auditor"]


def fm(slug: str) -> dict:
    return yaml.safe_load((ROOT / ".opencode" / "agents" / f"{slug}.md")
                          .read_text(encoding="utf-8").split("---")[1])


def run(script: Path, *args: str):
    import json
    r = subprocess.run([sys.executable, str(script), *args],
                       capture_output=True, text=True, timeout=60)
    return r.returncode, json.loads(r.stdout)


@pytest.mark.parametrize("slug", ONDA_6)
def test_gate_promulgation(slug):
    _, payload = run(GATE, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["ok"] is True, rep["errors"]
    assert rep["score"] >= 85
    assert rep["est_tokens"] <= 4000


@pytest.mark.parametrize("slug", ONDA_6)
def test_nexus_contract(slug):
    _, payload = run(NEXUS, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["status"] == "promulgado", rep["errors"]


def test_l3_role_is_gate():
    """L3 = role 'gate' (VALID_ROLES enum do validator)."""
    for slug in ONDA_6[1:]:
        assert fm(slug)["layer"] == "L3"
        assert fm(slug)["role"] == "gate"
    assert fm("agent-qa-sdet")["layer"] == "L2"
    assert fm("agent-qa-sdet")["role"] == "specialist"


def test_registry_covers_onda_6():
    subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_agent_registry.py")],
                   capture_output=True, text=True, check=True)
    data = yaml.safe_load((ROOT / ".ai" / "agents" / "registry.yaml")
                          .read_text(encoding="utf-8"))
    names = {a["name"] for a in data["agents"]}
    for slug in ONDA_6:
        assert slug in names


def test_rubric_cited_in_reviewer():
    text = (ROOT / ".opencode" / "agents" / "agent-reviewer.md")\
        .read_text(encoding="utf-8").upper()
    for rid in ("R-01", "R-07"):
        assert rid in text, rid
    assert "LGTM" in text  # proibicao declarada na rubrica


def test_merge_chain_slots_in_gatekeeper():
    text = (ROOT / ".opencode" / "agents" / "agent-gatekeeper.md")\
        .read_text(encoding="utf-8").lower()
    for token in ("reviewer", "qa", "coverage", "compliance", "human"):
        assert token in text, token


def test_violation_register_in_auditor():
    text = (ROOT / ".opencode" / "agents" / "agent-project-auditor.md")\
        .read_text(encoding="utf-8").lower()
    assert "vio-" in text
    assert "append-only" in text


def test_qa_trace_id_convention():
    text = (ROOT / ".opencode" / "agents" / "agent-qa-sdet.md")\
        .read_text(encoding="utf-8")
    assert "REQ-x.y::layer::case" in text


def test_onda6_chain_wiring():
    """Wire do plano 6: qa -> reviewer -> gatekeeper -> auditor (auditor terminal)."""
    assert "agent-reviewer" in fm("agent-qa-sdet")["downstream"]
    assert "agent-gatekeeper" in fm("agent-reviewer")["downstream"]
    assert "agent-reviewer" in fm("agent-gatekeeper")["upstream"]
    assert "agent-project-auditor" in fm("agent-gatekeeper")["downstream"]
    assert fm("agent-project-auditor")["downstream"] == []  # terminal
