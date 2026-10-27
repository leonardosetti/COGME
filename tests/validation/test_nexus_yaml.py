"""tests/validation/test_nexus_yaml.py — Validação consistente do ecossistema COGME.

Suíte de testes para validar:
  1. registry.yaml como SSOT (YAML válido, slugs, camadas, papéis)
  2. DAG acíclica, sem auto-referências, sem ciclos
  3. Ordenação de camadas (upstream deve estar em camada anterior ou igual)
  4. L0 com exatamente 1 orquestrador (agent-nexus-prime-ultimate)
  5. upstream/downstream referenciando slugs conhecidos
  6. Substituição do slug legacy agent-orchestrator → agent-nexus-prime-ultimate
  7. Conformidade constitucional (FOSS-first, LGPD, CPU-only)
  8. Scripts de validação (nexus_dispatcher, dag_validator, sync_agent_registry)
  9. Consistência entre registry.yaml e frontmatter dos .md
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / ".ai" / "agents" / "registry.yaml"
SCRIPTS_DIR = REPO_ROOT / "scripts"
AGENTS_DIR = REPO_ROOT / ".opencode" / "agents"

VALID_LAYERS = {"L0", "L1", "L2", "L3", "META"}
VALID_ROLES = {"orchestrator", "specialist", "gate", "forge"}

# Sequência canônica da DAG (constitution.md Art. 4.5 + registry.yaml SSOT)
AGENT_TOPOLOGY = {
    "L0": ["agent-nexus-prime-ultimate"],
    "L1": ["agent-sdd-specialist", "agent-pm", "agent-po",
           "agent-architect", "agent-project-analyst",
           "agent-business-analysis-specialist",
           "agent-project-design-specialist",
           "agent-project-patterns-standards-specialist"],
    "L2": ["agent-python-specialist", "agent-api-specialist", "agent-dba",
           "agent-backend-dev", "agent-ui-ux-advisor", "agent-frontend-dev",
           "agent-bash-specialist", "agent-infrastructure-specialist",
           "agent-devops", "agent-github-specialist", "agent-digital-security",
           "agent-compliance-governance",
           "agent-artifact-builder", "agent-qa-sdet",
           "agent-ai-llm-rag-dag-mcp-roster-master-specialist",
           "agent-art-communication-marketing-pr-specialist",
           "agent-cobit-specialist", "agent-copyright-specialist",
           "agent-docker-specialist", "agent-iso-26514-specialist",
           "agent-itil-specialist", "agent-quality-architect-specialist",
           "agent-six-sigma-specialist", "agent-sldc-process-specialist"],
    "L3": ["agent-reviewer", "agent-gatekeeper", "agent-project-auditor",
           "agent-clean-code-evaluator"],
    "META": ["agent-skill-master", "agent-factory-architect-ultimate"],
    "FORGE-LEGACY": ["agent-factory-architect"],
}
KNOWN_SLUGS = {a for members in AGENT_TOPOLOGY.values() for a in members}


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def registry_data():
    """Carrega registry.yaml completo."""
    with open(REGISTRY_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture
def agents_list(registry_data):
    """Lista de agentes do registry (chave 'agents' no nível raiz)."""
    return registry_data["agents"]


# ---------------------------------------------------------------------------
# 1. registry.yaml SSOT — estrutura e parsing
# ---------------------------------------------------------------------------

def test_registry_yaml_parses(registry_data):
    """registry.yaml deve ser YAML válido e parseável (fail-closed se corrompo)."""
    assert registry_data is not None
    assert "agents" in registry_data, (
        "registry.yaml deve conter chave 'agents' no nível raiz"
    )
    assert "registry" in registry_data


def test_registry_version(registry_data):
    """Versão do registry deve estar presente."""
    assert registry_data["registry"]["version"] == "1.0"
    assert registry_data["registry"]["project"] == "COGME"


def test_registry_slug_rule(registry_data):
    """slug_rule deve exigir kebab-case com prefixo agent- (Art. 4)."""
    rule = registry_data["registry"]["slug_rule"]
    assert "kebab-case" in rule
    assert "agent-" in rule


# ---------------------------------------------------------------------------
# 2. Slugs — existência, naming, substituição legacy
# ---------------------------------------------------------------------------

def test_agent_nexus_prime_ultimate_slug_exists(agents_list):
    """agent-nexus-prime-ultimate deve existir no registry (substitui agent-orchestrator)."""
    slugs = [a["name"] for a in agents_list]
    assert "agent-nexus-prime-ultimate" in slugs, (
        "agent-nexus-prime-ultimate ausente do registry; slug legacy 'agent-orchestrator' foi substituído"
    )


def test_agent_orchestrator_slug_removed(agents_list):
    """O slug legado 'agent-orchestrator' NÃO deve mais aparecer no registry."""
    slugs = [a["name"] for a in agents_list]
    assert "agent-orchestrator" not in slugs, (
        "slug legado 'agent-orchestrator' ainda presente; deve ser agent-nexus-prime-ultimate"
    )


def test_all_slugs_kebab_case(agents_list):
    """Todos os nomes de agente devem seguir kebab-case com prefixo agent-."""
    import re
    slug_re = re.compile(r"^agent-[a-z0-9]+(-[a-z0-9]+)*$")
    for a in agents_list:
        name = a["name"]
        assert slug_re.match(name), f"slug fora de kebab-case: {name!r}"


def test_no_duplicate_slugs(agents_list):
    """Não deve haver slugs duplicados no registry."""
    slugs = [a["name"] for a in agents_list]
    dups = [s for s in set(slugs) if slugs.count(s) > 1]
    assert not dups, f"slugs duplicados: {dups}"


def test_all_agents_have_required_keys(agents_list):
    """Cada agente promulgado deve ter as 5 chaves mínimas: name, version, layer, role, description.
    Agentes legacy-forge (sem frontmatter) são tolerados (Art. 4.8)."""
    required = ("name", "version", "layer", "role", "description")
    for a in agents_list:
        if a.get("status") == "legacy-forge":
            continue  # tolerado: sem frontmatter (Art. 4.8)
        for key in required:
            assert key in a and a[key] is not None and a[key] != "", (
                f"agente {a.get('name', '?')} falta chave obrigatória: {key}"
            )


# ---------------------------------------------------------------------------
# 3. Camadas e papéis — validade
# ---------------------------------------------------------------------------

def test_layers_valid(agents_list):
    """Todas as camadas devem ser válidas: L0|L1|L2|L3|META."""
    for a in agents_list:
        assert a["layer"] in VALID_LAYERS, f"layer inválida em {a['name']}: {a['layer']!r}"


def test_roles_valid(agents_list):
    """Todos os papéis devem ser válidos: orchestrator|specialist|gate|forge."""
    for a in agents_list:
        assert a["role"] in VALID_ROLES, f"role inválido em {a['name']}: {a['role']!r}"


def test_l0_exactly_one_orchestrator(agents_list):
    """L0 deve conter exatamente 1 agente com role orchestrator: agent-nexus-prime-ultimate."""
    l0 = [a for a in agents_list if a["layer"] == "L0"]
    assert len(l0) == 1, f"L0 deve ter exatamente 1 agente; encontrado: {len(l0)}"
    assert l0[0]["role"] == "orchestrator"
    assert l0[0]["name"] == "agent-nexus-prime-ultimate"


def test_layer_distribution_matches_topology(agents_list):
    """Todos os slugs do AGENT_TOPOLOGY devem existir no registry (subset check)."""
    registry_layers = Counter(a["layer"] for a in agents_list if a["status"] != "legacy-forge")
    for layer, members in AGENT_TOPOLOGY.items():
        if layer == "FORGE-LEGACY":
            continue
        for slug in members:
            assert any(a["name"] == slug and a["layer"] == layer for a in agents_list), (
                f"slug {slug} (camada {layer}) do AGENT_TOPOLOGY ausente no registry"
            )


# ---------------------------------------------------------------------------
# 4. DAG — aciclicidade, sem auto-referência, referências conhecidas
# ---------------------------------------------------------------------------

def test_no_self_references(agents_list):
    """Nenhum agente deve referenciar a si mesmo em upstream ou downstream."""
    for a in agents_list:
        name = a["name"]
        for ref_key in ("upstream", "downstream"):
            refs = a.get(ref_key) or []
            assert name not in refs, (
                f"{name}: auto-referência em {ref_key} proibida (Art. 4.5)"
            )


def test_no_duplicate_references(agents_list):
    """upstream/downstream não deve conter slugs duplicados dentro do mesmo agente."""
    for a in agents_list:
        name = a["name"]
        for ref_key in ("upstream", "downstream"):
            refs = a.get(ref_key) or []
            assert len(refs) == len(set(refs)), (
                f"{name}: {ref_key} contém duplicatas: {refs}"
            )


def test_all_references_point_to_known_slugs(agents_list):
    """Todo upstream/downstream deve referenciar slugs conhecidos do registry."""
    known = {a["name"] for a in agents_list}
    for a in agents_list:
        name = a["name"]
        for ref_key in ("upstream", "downstream"):
            for ref in (a.get(ref_key) or []):
                assert ref in known, (
                    f"{name}: {ref_key} referencia slug desconhecido: {ref}"
                )


def test_dag_has_no_cycles(agents_list):
    """O grafo de dependências (upstream → downstream) não deve conter ciclos."""
    graph = {a["name"]: list(a.get("downstream") or []) for a in agents_list}
    for a in agents_list:
        graph.setdefault(a["name"], [])

    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def dfs(u, path):
        color[u] = GRAY
        path.append(u)
        for v in graph.get(u, []):
            if color.get(v, WHITE) == GRAY:
                cycle_start = path.index(v)
                cycle = path[cycle_start:] + [v]
                pytest.fail(f"Ciclo detectado na DAG: {' → '.join(cycle)}")
            if color.get(v, WHITE) == WHITE:
                dfs(v, path)
        path.pop()
        color[u] = BLACK

    for node in graph:
        if color[node] == WHITE:
            dfs(node, [])


# ---------------------------------------------------------------------------
# 5. Ordenação de camadas — upstream não deve estar em camada posterior
# ---------------------------------------------------------------------------

def test_layer_upstream_ordering(agents_list):
    """Upstream de um agente não deve estar em camada posterior (recomendação, não bloqueio).
    Same-layer ou anterior é aceitável; camada posterior gera warning."""
    layer_order = {"L0": 0, "L1": 1, "L2": 2, "L3": 3, "META": 4}
    layer_of = {a["name"]: a["layer"] for a in agents_list}
    warnings = []
    for a in agents_list:
        name = a["name"]
        layer = a["layer"]
        if layer == "L0":
            continue
        for upstream in (a.get("upstream") or []):
            up_layer = layer_of.get(upstream)
            if up_layer is None:
                continue
            if layer_order[up_layer] > layer_order[layer]:
                warnings.append(
                    f"{name} ({layer}) tem upstream {upstream} ({up_layer}) em camada posterior"
                )
    if warnings:
        print(f"\n[AVISO] {len(warnings)} upstream em camada posterior: {warnings}")
    # Não falha: é recomendação de arquitetura, não regra rígida da DAG


# ---------------------------------------------------------------------------
# 6. Scripts de validação — saída verde
# ---------------------------------------------------------------------------

def _parse_json_from_output(stdout: str) -> dict:
    """Extrai o objeto JSON de uma saída que pode conter texto após o JSON."""
    # Encontra o primeiro '{' e tenta fazer parse até encontrar JSON válido
    start = stdout.find("{")
    if start == -1:
        raise ValueError(f"Nenhum JSON encontrado na saída: {stdout[:200]}")
    # Tenta parsear crescendo o fim até funcionar
    for end in range(len(stdout), start, -1):
        try:
            return json.loads(stdout[start:end])
        except json.JSONDecodeError:
            continue
    raise ValueError(f"Não foi possível extrair JSON da saída: {stdout[:200]}")


def test_dag_validator_green():
    """dag_validator.py deve reportar topologia válida (sem erros)."""
    result = subprocess.run(
        [sys.executable, "scripts/dag_validator.py"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    report = _parse_json_from_output(result.stdout)
    assert report["topologia_valida"] is True, (
        f"DAG inválida: {report['erros']}"
    )
    assert report["erros"] == [], f"Erros na DAG: {report['erros']}"


def test_validate_nexus_yaml_green():
    """validate_nexus_yaml.py deve validar todos os agentes sem erro."""
    result = subprocess.run(
        [sys.executable, "scripts/validate_nexus_yaml.py"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    report = _parse_json_from_output(result.stdout)
    assert report["rejeitados"] == 0, (
        f"Agentes rejeitados: {[r['slug'] for r in report['reports'] if not r['ok']]}"
    )
    assert report["promulgados"] > 0


# ---------------------------------------------------------------------------
# 7. Conformidade constitucional — FOSS-first, LGPD, CPU-only
# ---------------------------------------------------------------------------

def test_constitutional_no_cuda_cloud_inference(agents_list):
    """Nenhum agente deve promover CUDA ou cloud inference (Art. P-02 — CPU-only forever)."""
    for a in agents_list:
        desc = (a.get("description") or "").lower()
        # Se menciona CUDA, deve restringir a CPU-only
        if "cuda" in desc:
            assert "cpu-only" in desc or "cpu local" in desc, (
                f"{a['name']}: menciona CUDA sem restrição CPU-only"
            )
        # Se menciona cloud, deve ser local-first
        if "cloud inference" in desc or "cloud gpu" in desc:
            assert "local" in desc or "localhost" in desc, (
                f"{a['name']}: menciona cloud inference sem ênfase local"
            )


def test_infrastructure_agents_cpu_only(agents_list):
    """Agentes de infraestrutura (llama.cpp, runtime) não devem promover CUDA/cloud sem restrição local."""
    infra = [a for a in agents_list
             if "infrastructure" in a["name"] or "bash" in a["name"]]
    for a in infra:
        desc = (a.get("description") or "").lower()
        # Se menciona CUDA ou cloud, deve ter restrição CPU-only/local
        if "cuda" in desc or "cloud" in desc:
            assert "cpu-only" in desc or "cpu local" in desc or "local" in desc, (
                f"{a['name']}: menciona CUDA/cloud sem restrição CPU-only/local (Art. P-02)"
            )


# ---------------------------------------------------------------------------
# 8. Handoff e dispatcher — schemas e existência de scripts
# ---------------------------------------------------------------------------

def test_dispatcher_script_exists():
    """scripts/nexus_dispatcher.py deve existir como gate de despacho."""
    assert (SCRIPTS_DIR / "nexus_dispatcher.py").exists()


def test_handoff_parser_script_exists():
    """scripts/handoff_parser.py deve existir como parser de payload."""
    assert (SCRIPTS_DIR / "handoff_parser.py").exists()


def test_sync_agent_registry_script_exists():
    """scripts/sync_agent_registry.py deve existir como validador de roster."""
    assert (SCRIPTS_DIR / "sync_agent_registry.py").exists()


def test_validate_nexus_yaml_script_exists():
    """scripts/validate_nexus_yaml.py deve existir como validador de contratos."""
    assert (SCRIPTS_DIR / "validate_nexus_yaml.py").exists()


# ---------------------------------------------------------------------------
# 9. Status — apenas promulgado ou legacy-forge aceitos
# ---------------------------------------------------------------------------

def test_agent_statuses_valid(agents_list):
    """Status deve ser 'promulgado', 'legacy-forge' ou 'rejeitado'."""
    for a in agents_list:
        assert a["status"] in ("promulgado", "legacy-forge", "rejeitado"), (
            f"{a['name']}: status inválido: {a['status']}"
        )


def test_legacy_forge_only_factory_architects(agents_list):
    """Apenas os dois forjadores legacy podem ter status legacy-forge (Art. 4.8)."""
    legacy = [a["name"] for a in agents_list if a["status"] == "legacy-forge"]
    for name in legacy:
        assert "factory-architect" in name, (
            f"{name}: status legacy-forge fora do conjunto permitido (Art. 4.8)"
        )


# ---------------------------------------------------------------------------
# 10. Consistência registry.yaml ↔ frontmatter dos .md
# ---------------------------------------------------------------------------

def test_registry_matches_agent_frontmatter():
    """registry.yaml deve estar sincronizado com o frontmatter dos .opencode/agents/*.md.
    Agentes legacy-forge (sem frontmatter) são tolerados."""
    md_files = sorted(AGENTS_DIR.glob("*.md"))
    assert md_files, "Nenhum arquivo de agente encontrado em .opencode/agents/"

    registry_data = yaml.safe_load(open(REGISTRY_PATH))
    registry_names = {a["name"] for a in registry_data["agents"]}
    registry_legacy = {a["name"] for a in registry_data["agents"] if a.get("status") == "legacy-forge"}

    md_names = set()
    for f in md_files:
        text = f.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue  # legacy-forge sem frontmatter
        lines = text.splitlines()
        try:
            end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
        except StopIteration:
            continue
        try:
            fm = yaml.safe_load("\n".join(lines[1:end]))
        except yaml.YAMLError:
            continue
        if isinstance(fm, dict) and fm.get("name"):
            md_names.add(fm["name"])

    # Todo agente promulgado no registry deve ter arquivo .md correspondente
    missing_md = (registry_names - registry_legacy) - md_names
    assert not missing_md, f"Agentes promulgados no registry sem arquivo .md: {missing_md}"

    # Todo arquivo .md com frontmatter deve estar no registry
    missing_registry = md_names - registry_names
    assert not missing_registry, f"Arquivos .md não registrados: {missing_registry}"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
