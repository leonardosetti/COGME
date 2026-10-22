"""Gate de regressão da ONDA 4: 7 agentes de execução técnica (4a + 4b)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "scripts" / "validate_afa_output.py"
NEXUS = ROOT / "scripts" / "validate_nexus_yaml.py"
ONDA_4A = ["agent-python-specialist", "agent-api-specialist", "agent-dba",
           "agent-backend-dev"]
ONDA_4B = ["agent-ui-ux-advisor", "agent-frontend-dev", "agent-bash-specialist"]
ONDA_4 = ONDA_4A + ONDA_4B


def run(script, *args):
    r = subprocess.run([sys.executable, str(script), *args],
                       capture_output=True, text=True, timeout=60)
    return r.returncode, json.loads(r.stdout)


@pytest.mark.parametrize("slug", ONDA_4)
def test_gate_promulgation(slug):
    _, payload = run(GATE, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["ok"] is True, rep["errors"]
    assert rep["score"] >= 85
    assert rep["est_tokens"] <= 4000


@pytest.mark.parametrize("slug", ONDA_4)
def test_nexus_contract(slug):
    _, payload = run(NEXUS, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["status"] == "promulgado", rep["errors"]


def test_registry_covers_onda_4():
    subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_agent_registry.py")],
                   capture_output=True, text=True, check=True)
    import yaml
    data = yaml.safe_load((ROOT / ".ai" / "agents" / "registry.yaml")
                          .read_text(encoding="utf-8"))
    names = {a["name"] for a in data["agents"]}
    for slug in ONDA_4:
        assert slug in names


def test_money_is_decimal_everywhere():
    """LGPD + FX rule: 100% dos agentes da onda declaram Decimal para dinheiro."""
    for slug in ("agent-api-specialist", "agent-dba", "agent-backend-dev",
                 "agent-python-specialist"):
        text = (ROOT / ".opencode" / "agents" / f"{slug}.md")\
            .read_text(encoding="utf-8").lower()
        assert "decimal" in text, slug


def test_no_cdn_runtime_in_frontend():
    text = (ROOT / ".opencode" / "agents" / "agent-frontend-dev.md")\
        .read_text(encoding="utf-8").lower()
    assert "cdn" in text and "vendored" in text


def test_bash_fail_fast_rule():
    text = (ROOT / ".opencode" / "agents" / "agent-bash-specialist.md")\
        .read_text(encoding="utf-8").lower()
    assert "set -euo pipefail" in text
    assert "curl|bash" in text  # proibido por contrato


def test_wave4_chain_wiring():
    """Wire acordado no plano §4: python→api→dba→backend; advisor→frontend."""
    import yaml

    def fm(slug):
        return yaml.safe_load(
            (ROOT / ".opencode" / "agents" / f"{slug}.md")
            .read_text(encoding="utf-8").split("---")[1])
    assert "agent-backend-dev" in (fm("agent-dba")["downstream"])
    assert "agent-api-specialist" in (fm("agent-dba")["upstream"])
    assert "agent-api-specialist" in (fm("agent-python-specialist")["downstream"])
    assert "agent-frontend-dev" in (fm("agent-ui-ux-advisor")["downstream"])
