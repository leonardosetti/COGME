"""Gate de regressão da ONDA 3: agent-architect + agent-project-analyst."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "scripts" / "validate_afa_output.py"
NEXUS = ROOT / "scripts" / "validate_nexus_yaml.py"
ONDA_3 = ["agent-architect", "agent-project-analyst"]


def run(script, *args):
    r = subprocess.run([sys.executable, str(script), *args],
                       capture_output=True, text=True, timeout=30)
    return r.returncode, json.loads(r.stdout)


@pytest.mark.parametrize("slug", ONDA_3)
def test_gate_promulgation(slug):
    _, payload = run(GATE, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["ok"] is True, rep["errors"]
    assert rep["score"] >= 85
    assert rep["est_tokens"] <= 4000


@pytest.mark.parametrize("slug", ONDA_3)
def test_nexus_contract(slug):
    _, payload = run(NEXUS, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["status"] == "promulgado", rep["errors"]


def test_registry_covers_onda_3():
    subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_agent_registry.py")],
                   capture_output=True, text=True, check=True)
    import yaml
    data = yaml.safe_load((ROOT / ".ai" / "agents" / "registry.yaml")
                          .read_text(encoding="utf-8"))
    names = {a["name"] for a in data["agents"]}
    for slug in ONDA_3:
        assert slug in names


def test_analyst_zero_decision_contract():
    """Analyst proíbe edit de canon (Art. 5): DON'Ts contêm ´Never edit canon´ e overlay de decisores."""
    text = (ROOT / ".opencode" / "agents" / "agent-project-analyst.md")\
        .read_text(encoding="utf-8").lower()
    assert "never edit canon files" in text
    assert "never make decisions" in text


def test_architect_r01_coownership():
    """R-01 co-ownership: CVE half sempre com digital-security."""
    text = (ROOT / ".opencode" / "agents" / "agent-architect.md")\
        .read_text(encoding="utf-8").lower()
    assert "digital-security" in text
    assert "r-01" in text
