#!/usr/bin/env python3
"""dag_validator.py — Validador de topologia DAG e anti-recursao (ONDA 8).

Verifica:
  - AGENT_TOPOLOGY sem ciclos (DAG aciclica)
  - Nenhum agente referencia a si mesmo em upstream/downstream
  - Todo upstream/downstream de um agente esta em KNOWN_SLUGS
  - L0 tem exatamente 1 orquestrador
  - L3 (portoes) nao tem downstream para L2 (nao ha delegacao de portao para execucao)

Exit 1 se violacao. FOSS/stdlib apenas.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_nexus_yaml import (
    AGENT_TOPOLOGY, KNOWN_SLUGS, parse_frontmatter, validate_agent, AGENTS_DIR,
)

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


def _detect_cycle(graph: dict) -> list:
    """DFS para detectar ciclo no grafo de dependencias (upstream -> downstream)."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    stack = []

    def dfs(u):
        color[u] = GRAY
        stack.append(u)
        for v in graph.get(u, []):
            if color.get(v, WHITE) == GRAY:
                return stack[stack.index(v):] + [v]
            if color.get(v, WHITE) == WHITE:
                cyc = dfs(v)
                if cyc:
                    return cyc
        stack.pop()
        color[u] = BLACK
        return None

    for node in graph:
        if color[node] == WHITE:
            cyc = dfs(node)
            if cyc:
                return cyc
    return []


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validador de DAG e anti-recursao COGME")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 se qualquer violacao")
    parser.add_argument("--report", default=None, help="salva JSON do report")
    args = parser.parse_args()

    errors = []
    warnings = []

    # constroi grafo slug -> lista de downstream (para detecao de ciclo)
    graph = {}
    for layer, members in AGENT_TOPOLOGY.items():
        for slug in members:
            graph.setdefault(slug, [])

    # le frontmatter de cada arquivo para upstream/downstream declarados
    declared = {}
    for f in sorted(AGENTS_DIR.glob("*.md")):
        contract, _ = parse_frontmatter(f)
        if contract:
            name = str(contract.get("name") or "")
            declared[name] = {
                "upstream": list(contract.get("upstream") or []),
                "downstream": list(contract.get("downstream") or []),
                "layer": contract.get("layer"),
            }
            for ref in (contract.get("upstream") or []) + (contract.get("downstream") or []):
                if ref not in KNOWN_SLUGS:
                    warnings.append(f"{name}: referencia fora da topologia: {ref}")
                if ref == name:
                    errors.append(f"{name}: auto-referencia upstream/downstream")

    # deteccao de ciclo nas declaracoes (quando houver)
    if declared:
        dep_graph = {name: list(info["downstream"]) for name, info in declared.items()}
        ciclo = _detect_cycle(dep_graph)
        if ciclo:
            errors.append(f"ciclo detectado na DAG: {' -> '.join(ciclo)}")

    # L0 exatamente 1 orquestrador
    l0 = AGENT_TOPOLOGY.get("L0", [])
    if len(l0) != 1 or l0[0] != "agent-nexus-prime-ultimate":
        errors.append(f"L0 deve conter exatamente agent-nexus-prime-ultimate; encontrado: {l0}")

    # portoes L3 nao delegam para execucao L2 (downstream de L3 deve ser vazio ou apenas auditoria)
    for slug in AGENT_TOPOLOGY.get("L3", []):
        info = declared.get(slug, {})
        down = info.get("downstream", [])
        l2_down = [d for d in down if d in AGENT_TOPOLOGY.get("L2", [])]
        if l2_down:
            warnings.append(f"{slug} (L3) delega para L2: {l2_down} (revisar acoplamento)")

    report = {
        "topologia_valida": not errors,
        "total_slugs": len(KNOWN_SLUGS),
        "por_camada": {k: len(v) for k, v in AGENT_TOPOLOGY.items()},
        "erros": errors,
        "avisos": warnings,
    }
    out = json.dumps(report, indent=2, ensure_ascii=False)
    print(out)
    if args.report:
        Path(args.report).write_text(out, encoding="utf-8")

    if errors:
        print(f"[DAG] ERROS: {len(errors)}", file=sys.stderr)
        return 1 if args.strict else 0
    if warnings and args.strict:
        print(f"[DAG] AVISOS: {len(warnings)}", file=sys.stderr)
        return 1
    print(f"[DAG] OK: {len(KNOWN_SLUGS)} slugs, topologia aciclica")
    return 0


if __name__ == "__main__":
    sys.exit(main())
