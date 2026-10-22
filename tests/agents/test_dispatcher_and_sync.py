"""Test suite do nexus_dispatcher.py + sync_agent_registry.py (FASE S.6)."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
DISPATCH = ROOT / "scripts" / "nexus_dispatcher.py"
SYNC = ROOT / "scripts" / "sync_agent_registry.py"
REGISTRY = ROOT / ".ai" / "agents" / "registry.yaml"
AGENTS = ROOT / ".opencode" / "agents"


def run(script: Path, *args: str):
    r = subprocess.run([sys.executable, str(script), *args],
                       capture_output=True, text=True, timeout=30)
    try:
        return r.returncode, json.loads(r.stdout)
    except json.JSONDecodeError:
        return r.returncode, {"raw": r.stdout, "stderr": r.stderr}


def write_task(tmp_path, task: dict) -> str:
    f = tmp_path / "task.json"
    f.write_text(json.dumps(task, ensure_ascii=False), encoding="utf-8")
    return str(f)


# slug set importado da fonte única (SSOT).
sys.path.insert(0, str(ROOT / "scripts"))
from validate_nexus_yaml import KNOWN_SLUGS as KNOWN_SLUGS_SAFE


def seed_registry(agents_block: str):
    REGISTRY.write_text(
        "registry:\n  version: '1.0'\n  project: COGME\n"
        "deprecated:\n  archived_at: 2026-10-22\n  agents: [x, y]\n"
        "interim_fallback:\n  - name: agent-factory-architect\n"
        '    reason: contingencia\n'
        "agents:\n" + agents_block,
        encoding="utf-8")


@pytest.fixture()
def seeded_registry():
    """Registry própria de teste (col-0 YAML), restaurada ao final."""
    backup = REGISTRY.read_text(encoding="utf-8")
    yield REGISTRY
    REGISTRY.write_text(backup, encoding="utf-8")


class TestDispatcher:
    def test_task_valid_dispatched(self, tmp_path, seeded_registry):
        seed_registry(
            "- name: agent-orchestrator\n"
            "  version: '1.0'\n  layer: L0\n  role: orchestrator\n"
            "  description: teste\n  status: promulgado\n"
            "  upstream: []\n  downstream: []\n"
            "- name: agent-sdd-specialist\n"
            "  version: '1.0'\n  layer: L1\n  role: specialist\n"
            "  description: teste\n  status: promulgado\n"
            "  upstream: [agent-orchestrator]\n  downstream: []\n")
        rc, env = run(DISPATCH, "--check", write_task(tmp_path, {
            "task_id": "TA-001", "target": "agent-sdd-specialist",
            "action": "spec", "handoff": "001-smoke",
        }))
        assert rc == 0, json.dumps(env, ensure_ascii=False)[:400]
        assert env["status"] == "aceito"
        assert env["route"]["receiver"] == "agent-sdd-specialist"

    def test_self_delegation_rejected(self, tmp_path, seeded_registry):
        seed_registry(
            "- name: agent-orchestrator\n"
            "  version: '1.0'\n  layer: L0\n  role: orchestrator\n"
            "  description: teste\n  status: promulgado\n"
            "  upstream: []\n  downstream: []\n")
        rc, env = run(DISPATCH, "--check", write_task(tmp_path, {
            "task_id": "TA-009",
            "target": "agent-orchestrator", "action": "orchestrate"}))
        assert rc == 1
        assert any("self-delegation" in e for e in env["errors"])

    def test_unknown_target_rejected(self, tmp_path, seeded_registry):
        rc, env = run(DISPATCH, "--check", write_task(tmp_path, {
            "task_id": "TA-002", "target": "agent-inexistente", "action": "implement"}))
        assert rc == 1
        assert env["status"] == "rejeitado"
        assert any("DAG" in e for e in env["errors"])

    def test_not_promulgated_rejected(self, tmp_path, seeded_registry):
        # dialético robusto: escolhe dinamicamente um slug pendente (não-promulgado)
        import yaml as _yaml
        reg_path = REGISTRY.parent / "registry.yaml"
        reg = _yaml.safe_load(reg_path.read_text(encoding="utf-8"))
        promulgated = {a.get("name") for a in reg.get("agents", [])}
        pending = sorted(KNOWN_SLUGS_SAFE - promulgated)
        if not pending:
            pytest.skip("roster completo — sem slug pendente para simular rejeição")
        rc, env = run(DISPATCH, "--check", write_task(tmp_path, {
            "task_id": "TA-003", "target": pending[0], "action": "plan"}))
        assert rc == 1
        assert any("promulgado" in e for e in env["errors"])

    def test_bad_action_rejected(self, tmp_path, seeded_registry):
        rc, env = run(DISPATCH, "--check", write_task(tmp_path, {
            "task_id": "TA-004", "target": "agent-orchestrator", "action": "meditar"}))
        assert rc == 1
        assert any("action" in e for e in env["errors"])

    def test_topology_report(self):
        """Roster COMPLETO (25/25 do plano promulgados): DAG canônico intacto,
        pendências zero — assegurado pela ONDA 7 (skill-master fecha o plano)."""
        rc, rep = run(DISPATCH, "--report")
        assert rc == 0
        assert rep["dag_totals"]["L0"] == 1
        assert rep["dag_totals"]["L1"] == 5
        assert rep["dag_totals"]["L2"] == 15  # inclui agent-qa-sdet (execução)
        assert rep["dag_totals"]["L3"] == 3   # itens do portão: reviewer, gatekeeper, auditor
        assert rep["missing_from_dag"] == []


class TestSync:
    def test_sync_writes_and_check_passes(self):
        rc, _ = run(SYNC)
        assert rc == 0, "sync inicial deve passar"
        rc, rep = run(SYNC, "--check")
        assert rc == 0, rep

    def test_test_registry_preserves_meta_blocks(self, seeded_registry):
        before = REGISTRY.read_text(encoding="utf-8")
        assert "DEPRECATED" in before or "deprecated" in before
        run(SYNC)
        after = REGISTRY.read_text(encoding="utf-8")
        assert "deprecated" in after, "bloco deprecated não pode ser regenerado fora"

    def test_check_drift_detected(self, seeded_registry):
        run(SYNC)
        mutated = REGISTRY.read_text(encoding="utf-8").replace(
            "agent-factory-architect-ultimate", "agent-factory-architect-ultimate-x")
        REGISTRY.write_text(mutated, encoding="utf-8")
        rc, rep = run(SYNC, "--check")
        assert rc == 1
        assert rep.get("drift") is True

    def test_kebab_case_contract_in_registry(self):
        run(SYNC)
        import yaml
        data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
        for a in data["agents"]:
            name = a.get("name")
            if name:
                assert name.startswith("agent-") or a.get("status") == "legacy-forge"
                assert name == name.lower().replace("_", "-")
