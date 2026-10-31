import yaml
import sys
import os
import re
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parents[1] / ".opencode" / "agents"
LEGACY_SLUG_RE = re.compile(r"^agent-factory-architect(?:-ultimate)?$")

# AGENT_TOPOLOGY — DAG canônica (constitution.md Art. 4.5 + registry.yaml SSOT)
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
           "agent-six-sigma-specialist", "agent-sldc-process-specialist",
           "agent-sddai-loader", "agent-sddai-engineer", "agent-sddai-trainer",
           "agent-sddai-memory", "agent-sddai-cli"],
    "L3": ["agent-reviewer", "agent-gatekeeper", "agent-project-auditor",
           "agent-clean-code-evaluator"],
    "META": ["agent-skill-master", "agent-factory-architect-ultimate"],
    "FORGE-LEGACY": ["agent-factory-architect"],
}
KNOWN_SLUGS = {a for members in AGENT_TOPOLOGY.values() for a in members}

# Vetores de agencia consolidados (health check usa para avisos)
VECTORES_AGENCIA: dict = {}


def parse_frontmatter(path: Path):
    """Extrai frontmatter YAML de um arquivo .md de agente.
    Retorna (dict|None, str|None)."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        return None, f"erro leitura: {exc}"
    if not text.startswith("---\n"):
        return None, "sem frontmatter"
    lines = text.splitlines()
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, "frontmatter aberto"
    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        return None, f"YAML inválido: {exc}"
    if not isinstance(data, dict):
        return None, "frontmatter não é mapping"
    return data, None


def validate_agent(path: Path) -> dict:
    """Valida um arquivo de agente. Retorna {'ok': bool, 'errors': [], 'slug': str}."""
    rep = {"ok": True, "errors": [], "slug": path.stem}
    contract, fm_err = parse_frontmatter(path)
    if fm_err:
        rep["ok"] = False
        rep["errors"].append(fm_err)
        return rep
    required = ("name", "version", "layer", "role", "description")
    for key in required:
        if key not in contract or contract[key] is None or contract[key] == "":
            rep["ok"] = False
            rep["errors"].append(f"chave ausente: {key}")
    slug = contract.get("name", path.stem)
    if not re.match(r"^agent-[a-z0-9]+(-[a-z0-9]+)*$", str(slug)):
        rep["ok"] = False
        rep["errors"].append(f"slug fora de kebab-case: {slug}")
    rep["slug"] = slug
    return rep


def validate_agent_yaml(file_path):
    try:
        with open(file_path, 'r') as f:
            doc = yaml.safe_load(f)
        required_keys = ['name', 'version', 'layer', 'role', 'description']
        missing = [k for k in required_keys if k not in doc]
        if missing:
            print(f"🚨 Missing keys in {file_path}: {', '.join(missing)}")
            return False
        return True
    except Exception as e:
        print(f"❌ Error validating {file_path}: {str(e)}")
        return False


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    agent_dir = os.path.join(script_dir, '..', '.ai', 'agents')
    for root, _, files in os.walk(agent_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if not validate_agent_yaml(file_path):
                    sys.exit(1)