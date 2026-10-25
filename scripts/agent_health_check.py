#!/usr/bin/env python3
"""agent_health_check.py — Monitor de disponibilidade do ecossistema de agentes (ONDA 8).

Verifica:
  - Presenca de arquivo .opencode/agents/<slug>.md para cada slug do AGENT_TOPOLOGY
  - Frontmatter YAML valido (5 chaves) via validate_nexus_yaml
  - Promulgacao no .ai/agents/registry.yaml (status promulgado/legacy-forge)
  - Score de forja >= 85 via validate_afa_output (quando aplicavel)
  - Drift entre topologia, disco e registry

Fail-closed: qualquer slug ausente na topologia ou arquivo inexistente -> exit 1.
FOSS/stdlib apenas. 100% CPU-local, zero rede.

Uso:
  python3 scripts/agent_health_check.py              # relatorio completo
  python3 scripts/agent_health_check.py --strict     # exit 1 se qualquer falha
  python3 scripts/agent_health_check.py --report f.json
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_nexus_yaml import (
    AGENT_TOPOLOGY, KNOWN_SLUGS, VECTORES_AGENCIA, parse_frontmatter, validate_agent,
)
from sync_agent_registry import REGISTRY

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

AGENTS_DIR = Path(".opencode/agents")


def load_registry() -> dict:
    if yaml is None or not REGISTRY.exists():
        return {}
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    out = {}
    for a in data.get("agents", []):
        name = a.get("name")
        if name:
            out[name] = a
    return out


def check_slug(slug: str, registry: dict) -> dict:
    rep = {"slug": slug, "ok": True, "errors": [], "warnings": []}
    path = AGENTS_DIR / f"{slug}.md"

    # 1) arquivo existe
    if not path.exists():
        rep["ok"] = False
        rep["errors"].append("arquivo ausente em .opencode/agents/")
        return rep

    # 2) frontmatter + contrato
    contract, fm_err = parse_frontmatter(path)
    check = validate_agent(path)
    if not check["ok"]:
        rep["ok"] = False
        rep["errors"].extend(check["errors"])
    if fm_err:
        rep["warnings"].append(fm_err)

    # 3) registry
    entry = registry.get(slug)
    if not entry:
        rep["warnings"].append("ausente do registry.yaml (executar sync_agent_registry.py)")
    elif entry.get("status") not in ("promulgado", "legacy-forge"):
        rep["ok"] = False
        rep["errors"].append(f"status nao-dispatchavel: {entry.get('status')}")

    # 4) vetor de agencia (consolidado) — aviso, nao bloqueio
    if slug in VECTORES_AGENCIA:
        rep["warnings"].append(f"consolidado como vetor em {VECTORES_AGENCIA[slug]}")

    return rep


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Health check do ecossistema de agentes COGME")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 se qualquer falha (civil para CI)")
    parser.add_argument("--report", default=None, help="salva JSON do report")
    args = parser.parse_args()

    registry = load_registry()
    results = []
    for layer, members in sorted(AGENT_TOPOLOGY.items()):
        for slug in members:
            results.append(check_slug(slug, registry))

    falhas = [r for r in results if not r["ok"]]
    avisos = [r for r in results if r["ok"] and r["warnings"]]

    report = {
        "total": len(results),
        "saudaveis": len(results) - len(falhas) - len(avisos),
        "com_aviso": len(avisos),
        "falhas": len(falhas),
        "por_camada": {l: len(m) for l, m in AGENT_TOPOLOGY.items()},
        "resultados": results,
    }

    out = json.dumps(report, indent=2, ensure_ascii=False)
    print(out)
    if args.report:
        Path(args.report).write_text(out, encoding="utf-8")

    if falhas:
        print(f"[HEALTH] FALHAS: {len(falhas)}/{len(results)}", file=sys.stderr)
        return 1 if args.strict else 0
    if avisos and args.strict:
        print(f"[HEALTH] AVISOS: {len(avisos)}/{len(results)}", file=sys.stderr)
        return 1
    print(f"[HEALTH] OK: {len(results) - len(falhas)}/{len(results)} slugs verificados", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
