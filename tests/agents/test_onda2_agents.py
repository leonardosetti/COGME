"""Gate de regressão da ONDA 2: agent-pm + agent-po."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "scripts" / "validate_afa_output.py"
NEXUS = ROOT / "scripts" / "validate_nexus_yaml.py"
ONDA_2 = ["agent-pm", "agent-po"]


def run(script, *args):
    r = subprocess.run([sys.executable, str(script), *args],
                       capture_output=True, text=True, timeout=30)
    return r.returncode, json.loads(r.stdout)


@pytest.mark.parametrize("slug", ONDA_2)
def test_gate_promulgation(slug):
    _, payload = run(GATE, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["ok"] is True, rep["errors"]
    assert rep["score"] >= 85
    assert rep["est_tokens"] <= 4000


@pytest.mark.parametrize("slug", ONDA_2)
def test_nexus_contract(slug):
    _, payload = run(NEXUS, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["status"] == "promulgado", rep["errors"]


def test_registry_covers_onda_2():
    subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_agent_registry.py")],
                   capture_output=True, text=True, check=True)
    import yaml
    data = yaml.safe_load((ROOT / ".ai" / "agents" / "registry.yaml")
                          .read_text(encoding="utf-8"))
    names = {a["name"] for a in data["agents"]}
    for slug in ONDA_2:
        assert slug in names


def test_pm_po_chain_respected():
    """PM upstream de PO (plano §4): downstream do PM inclui PO, upstream do PO inclui PM."""
    import yaml
    for slug, field, expected in (
            ("agent-pm", "downstream", "agent-po"),
            ("agent-po", "upstream", "agent-pm")):
        fm = yaml.safe_load((ROOT / ".opencode" / "agents" / f"{slug}.md")
                            .read_text(encoding="utf-8").split("---")[1])
        assert expected in (fm.get(field) or [])
