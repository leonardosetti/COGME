#!/usr/bin/env python3
"""validate_nexus_yaml.py — Validador de contratos de agentes COGME (FASE S.1).

Valida o frontmatter YAML de cada agente em .opencode/agents/:
  - 5 chaves mínimas: name, version, layer, role, description
  - slug kebab-case (constitution.md Art. 4.2) e prefixo agent- (Art. 4.8)
  - layer válida: L0|L1|L2|L3|META
  - role válida: orchestrator|specialist|gate|forge
  - upstream/downstream refereniciando slugs da DAG (no self-reference)

Tolerância legacy: os dois arquivos do forjador (facão v2.2 / ULTIMATE sem frontmatter)
  são aceitos como legacy-forge com warning — nunca como agentes promulgados.
Fail-closed: qualquer violação → exit 1 e report JSON estruturado.
FOSS/stdlib: argparse + yaml (PyYAML).

Uso:
  python3 scripts/validate_nexus_yaml.py                  # valida todos
  python3 scripts/validate_nexus_yaml.py agent-x.md       # um arquivo
  python3 scripts/validate_nexus_yaml.py --strict-all     # sem tolerância legacy
  python3 scripts/validate_nexus_yaml.py --report out.json
"""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

AGENTS_DIR = Path(".opencode/agents")
REQUIRED_KEYS = ("name", "version", "layer", "role", "description")
VALID_LAYERS = {"L0", "L1", "L2", "L3", "META"}
VALID_ROLES = {"orchestrator", "specialist", "gate", "forge"}
SLUG_RE = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")
LEGACY_FORGE_OK = {
    "agent-factory-architect.md",
    "agent-factory-architect-ultimate.md",
}
LEGACY_SLUG_RE = re.compile(r"agent-factory-architect")

# Sequência canônica da DAG (constitution.md Art. 4.5 + docs/planos/plano-producao-agentes.md §4)
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

# Consolidados por vetor de agência (não forjados — papel absorvido por existente):
VECTORES_AGENCIA = {
    "agent-cyber-security-specialist": "agent-digital-security",
    "agent-compliance-specialist": "agent-compliance-governance",
    "agent-governance-specialist": "agent-compliance-governance",
    "agent-qa-qe-sdet-master": "agent-qa-sdet",
    "agent-sdd-master": "agent-sdd-specialist",
    "agent-tech-architect-specialist": "agent-architect",
}


def parse_frontmatter(path: Path):
    """Extrai frontmatter YAML (--- delimitado) do início do arquivo."""
    if yaml is None:
        return None, "PyYAML ausente no ambiente"
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, None  # sem frontmatter: candidato a legacy-forge
    lines = text.splitlines()
    if len(lines) < 3 or lines[1].strip() == "---":
        return None, "frontmatter degenerado: fechamento imediato"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, "frontmatter aberto: '---' de fechamento ausente"
    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        return None, f"YAML inválido: {str(exc)[:120]}"
    if not isinstance(data, dict):
        return None, "frontmatter não é mapping YAML"
    return data, None


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    return list(value) if isinstance(value, (list, tuple)) else value  # erro runtime


def validate_agent(path: Path, strict_all: bool = False) -> dict:
    """Retorna report de validação de UM agente."""
    rep = {
        "file": str(path),
        "slug": path.stem if path.stem.startswith("agent-") else f"agent-{path.stem}",
        "ok": True,
        "status": "promulgado",
        "errors": [],
        "warnings": [],
    }

    contract, fm_err = parse_frontmatter(path)

    # --- Sem frontmatter --------------------------------------------------
    if contract is None:
        if fm_err is not None:
            rep["ok"] = False
            rep["status"] = "rejeitado"
            rep["errors"].append(fm_err)
            return rep
        if LEGACY_SLUG_RE.search(path.name) and not strict_all:
            rep["status"] = "legacy-forge"
            rep["ok"] = rep["file"].endswith(tuple(LEGACY_FORGE_OK)) or path.name in LEGACY_FORGE_OK
            if rep["ok"]:
                rep["warnings"].append(
                    "sem frontmatter — tolerado apenas para o forjador (Art. 4.8)")
            else:
                rep["errors"].append(
                    "arquivo de forja fora da lista de contingência v2.2/ULTIMATE")
            return rep
        rep["ok"] = False
        rep["status"] = "rejeitado"
        rep["errors"].append("frontmatter YAML ausente (5 chaves exigidas)")
        return rep

    # --- Com frontmatter --------------------------------------------------
    name = str(contract.get("name") or "")

    # 1) chaves mínimas não-vacinas
    for key in REQUIRED_KEYS:
        if not contract.get(key):
            rep["errors"].append(f"chave vazia ou ausente: {key}")

    # 2) slug kebab-case + prefixo obligatório
    if name and not SLUG_RE.match(name):
        rep["errors"].append(f"slug fora de kebab-case: {name!r}")
    if name and not name.startswith("agent-"):
        rep["errors"].append(f"prefixo agent- ausente em: {name!r}")

    # 3) layer da DAG
    layer = str(contract.get("layer") or "")
    if layer and layer not in VALID_LAYERS:
        rep["errors"].append(f"layer inválida: {layer!r}")

    # 4) role do vocabulário
    role = str(contract.get("role") or "")
    if role and role not in VALID_ROLES:
        rep["errors"].append(f"role inválida: {role!r}")

    # 5) referências upstream/downstream devem estar na DAG conhecida
    for ref_key in ("upstream", "downstream"):
        try:
            refs = _as_list(contract.get(ref_key))
        except TypeError:
            rep["errors"].append(f"{ref_key}: lista de slugs esperada")
            continue
        for ref in refs:
            if ref not in KNOWN_SLUGS:
                rep["warnings"].append(f"{ref_key}: slug fora da DAG do plano: {ref}")

    # 6) anti-circularidade (Art. 4.5)
    up = _as_list(contract.get("upstream"))
    down = _as_list(contract.get("downstream"))
    if name and (name in up or name in down):
        rep["errors"].append("auto-referência upstream/downstream proibida")

    rep["ok"] = not rep["errors"]
    rep["status"] = "promulgado" if rep["ok"] else "rejeitado"
    return rep


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida contratos YAML de agentes COGME")
    parser.add_argument("targets", nargs="*", help="arquivos .md específicos (opcional)")
    parser.add_argument("--strict-all", action="store_true", help="desliga tolerância legacy")
    parser.add_argument("--report", default=None, help="salva JSON do report")
    args = parser.parse_args()

    files = [Path(t) for t in args.targets] if args.targets else sorted(AGENTS_DIR.glob("*.md"))
    if not files:
        print("[!] Nenhum arquivo de agente localizado em .opencode/agents/", file=sys.stderr)
        return 1

    reports = [validate_agent(f, args.strict_all) for f in files]
    promulgados = sum(1 for r in reports if r["ok"] and r["status"] == "promulgado")
    legacy = sum(1 for r in reports if r["status"] == "legacy-forge")
    rejeitados = sum(1 for r in reports if not r["ok"])

    summary = {
        "total": len(reports),
        "promulgados": promulgados,
        "legacy_forge": legacy,
        "rejeitados": rejeitados,
        "reports": reports,
    }
    payload = json.dumps(summary, indent=2, ensure_ascii=False)
    print(payload)
    if args.report:
        Path(args.report).write_text(payload, encoding="utf-8")

    return 1 if any(not r["ok"] for r in reports) else 0


if __name__ == "__main__":
    sys.exit(main())
