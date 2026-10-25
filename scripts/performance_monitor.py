#!/usr/bin/env python3
"""performance_monitor.py — Monitor de performance do ecossistema (ONDA 8).

Mede:
  - Tokens estimados de cada agente (chars // 4) vs orçamento 4000
  - Contagem de secoes canonicas (16 obrigatorias)
  - Contagens quantitativas: Kill Switch >=5, Red Team >=8, FAIL-CLOSED >=6, Metricas >=8
  - Score estimado via heuristica de validate_afa_output

Gera alerta quando qualquer agente excede orçamento ou fica abaixo do minimo.
FOSS/stdlib apenas. Sem inferencia; leitura de arquivos locais somente.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_afa_output import (
    AGENTS_DIR, TOKEN_BUDGET, CUT_SCORE, SECTIONS, MIN_COUNTS, HEADER_RE, _split_sections, _count_items,
)

TOKEN_PER_CHAR = 4


def analyze_file(path: Path) -> dict:
    rep = {"file": str(path), "slug": path.stem, "ok": True, "errors": [],
           "warnings": [], "metrics": {}}
    text = path.read_text(encoding="utf-8")
    est_tokens = max(1, len(text) // TOKEN_PER_CHAR)
    rep["metrics"]["est_tokens"] = est_tokens
    rep["metrics"]["token_budget"] = TOKEN_BUDGET

    if est_tokens > TOKEN_BUDGET:
        rep["ok"] = False
        rep["errors"].append(f"orcamento estourado: ~{est_tokens} > {TOKEN_BUDGET}")
        rep["metrics"]["token_alert"] = True
    else:
        rep["metrics"]["token_alert"] = False

    bodies = _split_sections(text.splitlines())
    missing = [n for n, kw in SECTIONS.items() if n not in bodies]
    rep["metrics"]["missing_sections"] = missing
    if missing:
        rep["ok"] = False
        rep["errors"].append(f"secoes ausentes: {', '.join(missing[:8])}")

    counts = {}
    for key in MIN_COUNTS:
        sec = key.split("-", 1)[0]
        counts[key] = _count_items(bodies.get(sec, []))
        abe = MIN_COUNTS[key]
        if counts[key] < abe:
            rep["ok"] = False
            rep["errors"].append(f"{key}: {counts[key]} < minimo {abe}")
    rep["metrics"]["counts"] = counts

    return rep


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Monitor de performance de agentes COGME")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 se qualquer falha de metrica")
    parser.add_argument("--report", default=None, help="salva JSON do report")
    args = parser.parse_args()

    files = sorted(AGENTS_DIR.glob("*.md"))
    if not files:
        print("[!] Nenhum agente em .opencode/agents/", file=sys.stderr)
        return 1

    results = [analyze_file(f) for f in files]
    falhas = [r for r in results if not r["ok"]]

    report = {
        "total": len(results),
        "dentro_orcamento": len(results) - len(falhas),
        "fora_orcamento": len(falhas),
        "token_budget": TOKEN_BUDGET,
        "resultados": results,
    }
    out = json.dumps(report, indent=2, ensure_ascii=False)
    print(out)
    if args.report:
        Path(args.report).write_text(out, encoding="utf-8")

    if falhas:
        print(f"[PERF] FALHAS: {len(falhas)}/{len(results)}", file=sys.stderr)
        return 1 if args.strict else 0
    print(f"[PERF] OK: {len(results) - len(falhas)}/{len(results)} agentes dentro do orcamento")
    return 0


if __name__ == "__main__":
    sys.exit(main())
