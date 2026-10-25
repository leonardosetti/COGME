"""Gate de regressão da ONDA 1: agent-nexus-prime-ultimate + agent-sdd-specialist.

Pimenta a promulgação: 16 seções, thresholds quantitativos, score >= 85,
contrato YAML válido, presença no SSOT do registry (§13 dos dois agentes).
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "scripts" / "validate_afa_output.py"
NEXUS = ROOT / "scripts" / "validate_nexus_yaml.py"
ONDA_1 = ["agent-nexus-prime-ultimate", "agent-sdd-specialist"]


def run(script, *args):
    r = subprocess.run([sys.executable, str(script), *args],
                       capture_output=True, text=True, timeout=30)
    return r.returncode, json.loads(r.stdout)


@pytest.mark.parametrize("slug", ONDA_1)
def test_gate_promulgation(slug):
    rg, payload = run(GATE, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["ok"] is True, rep["errors"]
    assert rep["score"] >= 85
    assert rep["est_tokens"] <= 4000, "constitution.md Art. 4.7 budget"


@pytest.mark.parametrize("slug", ONDA_1)
def test_nexus_contract(slug):
    _, payload = run(NEXUS, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["status"] == "promulgado", rep["errors"]


def test_registry_covers_onda_1():
    subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_agent_registry.py")],
                   capture_output=True, text=True, check=True)
    import yaml
    data = yaml.safe_load((ROOT / ".ai" / "agents" / "registry.yaml")
                          .read_text(encoding="utf-8"))
    names = {a["name"] for a in data["agents"]}
    for slug in ONDA_1:
        assert slug in names
