"""Gate de regressao da ONDA 7 (final): docker (documentation custody, errata docer TA-0016) + artifact-builder + skill-master (META)."""
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "scripts" / "validate_afa_output.py"
NEXUS = ROOT / "scripts" / "validate_nexus_yaml.py"
DISPATCH = ROOT / "scripts" / "nexus_dispatcher.py"
ONDA_7 = ["agent-docker-specialist", "agent-artifact-builder", "agent-skill-master"]


def fm(slug: str) -> dict:
    return yaml.safe_load((ROOT / ".opencode" / "agents" / f"{slug}.md")
                          .read_text(encoding="utf-8").split("---")[1])


def run(script: Path, *args: str):
    import json
    r = subprocess.run([sys.executable, str(script), *args],
                       capture_output=True, text=True, timeout=60)
    return r.returncode, json.loads(r.stdout)


@pytest.mark.parametrize("slug", ONDA_7)
def test_gate_promulgation(slug):
    _, payload = run(GATE, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    rep = payload["reports"][0]
    assert rep["ok"] is True, rep["errors"]
    assert rep["score"] >= 85
    assert rep["est_tokens"] <= 4000


@pytest.mark.parametrize("slug", ONDA_7)
def test_nexus_contract(slug):
    _, payload = run(NEXUS, str(ROOT / ".opencode" / "agents" / f"{slug}.md"))
    assert payload["reports"][0]["status"] == "promulgado"


def test_skill_master_meta_layer():
    """skill-master e o segundo agente META do roster (plano: YAGNI-last)."""
    assert fm("agent-skill-master")["layer"] == "META"
    assert fm("agent-skill-master")["role"] == "forge"
    assert fm("agent-skill-master")["downstream"] == []  # terminal


def test_registry_covers_onda_7():
    subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_agent_registry.py")],
                   capture_output=True, text=True, check=True)
    data = yaml.safe_load((ROOT / ".ai" / "agents" / "registry.yaml")
                          .read_text(encoding="utf-8"))
    names = {a["name"] for a in data["agents"]}
    for slug in ONDA_7:
        assert slug in names


def test_yagni_gate_in_skill_master():
    text = (ROOT / ".opencode" / "agents" / "agent-skill-master.md")\
        .read_text(encoding="utf-8").lower()
    assert "yagni" in text
    assert "skill.md" in text
    assert "injection" in text
    assert "skill-project-reader" in text  # primeiro candidato, pendente


def test_determinism_in_builder():
    text = (ROOT / ".opencode" / "agents" / "agent-artifact-builder.md")\
        .read_text(encoding="utf-8").lower()
    assert "determinism" in text
    assert "tpl-" in text
    assert "new files only" in text or "new-file" in text


def test_openapi_parity_in_docker():
    text = (ROOT / ".opencode" / "agents" / "agent-docker-specialist.md")\
        .read_text(encoding="utf-8").lower()
    assert "openapi" in text
    assert "runbook" in text
    assert "pt-br" in text


def test_onda7_chain_wiring():
    """Wire final: builder -> docker -> skill-master; auditor consome docker (drift)."""
    assert "agent-docker-specialist" in fm("agent-artifact-builder")["downstream"]
    assert "agent-skill-master" in fm("agent-docker-specialist")["downstream"]
    assert "agent-docker-specialist" in fm("agent-skill-master")["upstream"]
    assert "agent-project-auditor" in fm("agent-docker-specialist")["downstream"]


def test_roster_complete_after_onda7():
    """FECHAMENTO: 25/25 slugs do plano promulgados (missing_from_dag vazio)."""
    subprocess.run([sys.executable, str(ROOT / "scripts" / "sync_agent_registry.py")],
                   capture_output=True, text=True, check=True)
    _, report = run(DISPATCH, "--report")
    assert report["missing_from_dag"] == [], report["missing_from_dag"]
    # TA-0016 (errata ratificada): arquivo typo da custódia de documentação arquivado em archive/; roster 41 -> 40
    assert report["promulgados"] == 46  # 41 do plano + 5 SDDAI (loader, memory, engineer, trainer, cli)


def test_no_loose_ends_too_early():
    """Anti-subutilização: nenhum agente promulgado ficou sem consumo downstream
    exceto terminais declarados (auditador, skill-master)."""
    terminal = {"agent-project-auditor", "agent-skill-master"}
    import glob as _glob
    agents_dir = ROOT / ".opencode" / "agents"
def test_no_loose_ends_too_early():
    """Anti-subutilização (cápsula final): todo agente promulgado do plano declara
    consumidores de suas entregas (downstream não-vazio). Terminais declarados
    (auditor, skill-master) e legacy-forge são isenções documentadas."""
    terminal = {"agent-project-auditor", "agent-skill-master",
                "agent-factory-architect", "agent-factory-architect-ultimate",
                "agent-sddai-trainer", "agent-sddai-cli"}
    reg = yaml.safe_load((ROOT / ".ai" / "agents" / "registry.yaml")
                         .read_text(encoding="utf-8"))
    names = {a["name"] for a in reg["agents"]
             if a.get("layer") and a["name"] not in terminal}  # 25 do plano
    orphans = {slug for slug in names if not (fm(slug).get("downstream") or [])}
    assert not orphans, f"agentes sem consumidores: {orphans}"
