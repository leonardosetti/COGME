import argparse
import json
import yaml
import sys
import os
import re
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parents[1] / ".opencode" / "agents"
LEGACY_SLUG_RE = re.compile(r"^agent-factory-architect(?:-ultimate)?$")

# AGENT_TOPOLOGY — DAG canônica (constitution.md Art. 4.5 + registry.yaml SSOT)
# SSOT única: derivado dos frontmatters dos agentes promulgados em .opencode/agents/
# FORGE-LEGACY é legacy-forge, não promulgado
# agent-factory-architect-ultimate: L0-adjacente independente, acionável pelo orquestrador
AGENT_TOPOLOGY = {
    "L0": ["agent-nexus-prime-ultimate"],
    "L0_ADJ": ["agent-factory-architect-ultimate"],
    "L1": [
        "agent-architect",
        "agent-business-analysis-specialist",
        "agent-pm",
        "agent-po",
        "agent-project-analyst",
        "agent-project-design-specialist",
        "agent-project-patterns-standards-specialist",
        "agent-sdd-specialist",
    ],
    "L2": [
        "agent-agile-specialist",
        "agent-ai-llm-rag-dag-mcp-roster-master-specialist",
        "agent-api-specialist",
        "agent-art-communication-marketing-pr-specialist",
        "agent-artifact-builder",
        "agent-backend-dev",
        "agent-bash-specialist",
        "agent-cobit-specialist",
        "agent-compliance-governance",
        "agent-copyright-specialist",
        "agent-dba",
        "agent-devops",
        "agent-digital-security",
        "agent-docker-specialist",
        "agent-frontend-dev",
        "agent-github-specialist",
        "agent-infrastructure-specialist",
        "agent-iso-26514-specialist",
        "agent-itil-specialist",
        "agent-python-specialist",
        "agent-qa-sdet",
        "agent-quality-architect-specialist",
        "agent-sddai-cli",
        "agent-sddai-engineer",
        "agent-sddai-loader",
        "agent-sddai-memory",
        "agent-sddai-trainer",
        "agent-six-sigma-specialist",
        "agent-sldc-process-specialist",
        "agent-ui-ux-advisor",
    ],
    "L3": [
        "agent-clean-code-evaluator",
        "agent-gatekeeper",
        "agent-project-auditor",
        "agent-reviewer",
    ],
    "META": [
        "agent-skill-master",
    ],
}
KNOWN_SLUGS = {a for members in AGENT_TOPOLOGY.values() for a in members}

# Roles válidos (conforme testes de contrato)
VALID_ROLES = {"orchestrator", "specialist", "gate", "forge"}

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


def _build_report(path: Path, strict_all: bool = False) -> dict:
    """Constrói um relatório de validação para um único arquivo."""
    rep = {"file": str(path), "ok": True, "status": "promulgado", "errors": []}
    contract, fm_err = parse_frontmatter(path)

    # Legacy-forge: nome casa com o forjador, sem frontmatter válido → ok (a menos que strict-all)
    if LEGACY_SLUG_RE.search(path.stem) and fm_err:
        if strict_all:
            rep["ok"] = False
            rep["status"] = "rejeitado"
            rep["errors"].append("forjador legacy rejeitado em modo strict-all")
        else:
            rep["ok"] = True
            rep["status"] = "legacy-forge"
            rep["errors"] = []
        return rep

    if fm_err:
        rep["ok"] = False
        rep["status"] = "rejeitado"
        rep["errors"].append(fm_err)
        return rep

    required = ("name", "version", "layer", "role", "description")
    for key in required:
        if key not in contract or contract[key] is None or contract[key] == "":
            rep["ok"] = False
            rep["status"] = "rejeitado"
            rep["errors"].append(f"chave ausente: {key}")

    slug = contract.get("name", path.stem)

    # Validar slug kebab-case (sempre, coletar todos os erros)
    if not re.match(r"^agent-[a-z0-9]+(-[a-z0-9]+)*$", str(slug)):
        rep["ok"] = False
        rep["status"] = "rejeitado"
        rep["errors"].append(f"slug fora de kebab-case: {slug}")

    # Validar layer conhecido (sempre, coletar todos os erros)
    layer = contract.get("layer")
    valid_layers = set(AGENT_TOPOLOGY.keys())
    if layer not in valid_layers:
        rep["ok"] = False
        rep["status"] = "rejeitado"
        rep["errors"].append(f"layer inválida: {layer}")

    # Validar role (sempre, coletar todos os erros)
    role = contract.get("role")
    if role not in VALID_ROLES:
        rep["ok"] = False
        rep["status"] = "rejeitado"
        rep["errors"].append(f"role inválido: {role}")

    # Detectar auto-referência em upstream/downstream (sempre, coletar todos os erros)
    upstream = contract.get("upstream") or []
    downstream = contract.get("downstream") or []
    if isinstance(upstream, str):
        upstream = [upstream]
    if isinstance(downstream, str):
        downstream = [downstream]
    for ref in upstream + downstream:
        if ref == slug:
            rep["ok"] = False
            rep["status"] = "rejeitado"
            rep["errors"].append("auto-referência upstream/downstream")
            break

    return rep


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida contratos de agentes COGME (FASE S.6)")
    parser.add_argument("targets", nargs="*", help="arquivos .md de agentes para validar")
    parser.add_argument("--strict-all", action="store_true",
                        help="aplica regras estritas inclusive a forjadores legacy")
    parser.add_argument("--report", default=None, help="salva JSON do report")
    args = parser.parse_args()

    # Se alvos especificos, validar apenas eles
    if args.targets:
        files = [Path(t) for t in args.targets]
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        agent_dir = Path(script_dir).parent / ".opencode" / "agents"
        files = sorted(agent_dir.glob("*.md"))

    reports = []
    for f in files:
        if not f.exists():
            reports.append({"file": str(f), "ok": False,
                           "status": "rejeitado",
                           "errors": [f"arquivo não encontrado: {f}"]})
            continue
        if not f.suffix == ".md":
            continue
        reports.append(_build_report(f, args.strict_all))

    total = len(reports)
    aceitos = sum(1 for r in reports if r["ok"])
    rejeitados = sum(1 for r in reports if not r["ok"])
    promulgados = sum(1 for r in reports if r["ok"] and r["status"] == "promulgado")

    summary = {
        "total": total,
        "promulgados": promulgados,
        "aceitos": aceitos,
        "rejeitados": rejeitados,
        "reports": reports,
    }
    out = json.dumps(summary, indent=2, ensure_ascii=False)
    print(out)
    if args.report:
        Path(args.report).write_text(out, encoding="utf-8")
    return 1 if rejeitados else 0


if __name__ == "__main__":
    sys.exit(main())