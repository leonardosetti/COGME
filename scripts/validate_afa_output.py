#!/usr/bin/env python3
"""validate_afa_output.py — Gate de qualidade de forja (FASE S.3, matriz §0.9 AFA).

Valida TODO agente forjado antes da promulgação (constitution.md Art. 4.7):
  1. 16 seções canônicas presentes (template §6 AFA-ULTIMATE)
  2. Orçamento: system prompt ≤ ~4000 tokens (heurística 4 chars/token)
  3. Vectors quantitativos: Kill Switch ≥5, Red Team ≥8, FAIL-CLOSED ≥6,
     Métricas ≥8, DOs ≥15, DON'Ts ≥15
  4. Score composto poids-faithful (§0.9, corte ≥ 85)

Mapeamento de score (100 pts):
  sections 15 · killswitch 10 · bypass-prox 10 · redteam 10 · metricas 10
  failclosed 8 · hardware 7 · ideological-prox 10 · language 5 · foss 5
  token 5 · integration 5

Legacy: arquivos do forjador (agent-factory-architect*) → status legacy-forge.
Fail-closed: score < 85 ou seção faltante → exit 1.
FOSS/stdlib only.

Uso:
  python3 scripts/validate_afa_output.py [agentes...] [--strict-all] [--report f.json]
"""
import argparse
import json
import re
import sys
from pathlib import Path

AGENTS_DIR = Path(".opencode/agents")
TOKEN_BUDGET = 4000
CUT_SCORE = 85
LEGACY_PREFIX = "agent-factory-architect"

SECTIONS = {
    "0": "ROLE AND SCOPE", "0.1": "LAW", "0.2": "PROTOCOLS",
    "1": "COGNITIVE", "2": "HALLUCINATION", "3": "DOs", "4": "DON'Ts",
    "5": "LANGUAGE", "6": "OUTPUT", "7": "INPUT", "8": "METRICS",
    "9": "MEMORY", "10": "RED TEAM", "11": "FAIL-CLOSED",
    "12": "TEMPLATES", "13": "INTEGRATION", "14": "ONBOARDING",
    "15": "SELF-IMPROVEMENT", "16": "VERSIONING",
}
MIN_COUNTS = {
    "0.2-killswitch": 5, "3-dos": 15, "4-donts": 15,
    "8-metricas": 8, "10-redteam": 8, "11-failclosed": 6,
}
HEADER_RE = re.compile(r"^##\s+(\d+(?:\.\d+)?)\.?\s")


def _split_sections(lines) -> dict:
    """Mapeia num → corpo (lista de linhas) das seções '## N...' conhecidas."""
    bodies, current = {}, None
    for ln in lines:
        m = HEADER_RE.match(ln)
        if m:
            num = m.group(1)
            current = num if num in SECTIONS else None
            if current:
                bodies[current] = []
            continue
        if current:
            bodies[current].append(ln)
    return bodies


def _count_items(body: list) -> int:
    """Conta itens quantitativos: enumerados, bullets, e linhas de tabela."""
    n = 0
    for ln in body:
        s = ln.strip()
        if re.match(r"^\d+\.\s+\S", s):
            n += 1
        elif s.startswith(("- ", "* ", "• ")):
            n += 1
        elif s.startswith("|") and not re.match(r"^\|[\s\-|]+\|$", s):
            n += 1
    return n


def analyze(path: Path, strict: bool = False) -> dict:
    rep = {"file": str(path), "ok": True, "status": "aceito",
           "score": 0, "errors": [], "warnings": []}
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    bodies = _split_sections(lines)
    lower = text.lower()

    # (1) Orçamento: 5 pts do score + warning
    est_tokens = max(1, len(text) // 4)
    rep["est_tokens"] = est_tokens
    over = est_tokens > TOKEN_BUDGET

    # (2) Seções: 15 pts, penalidade 2/caixa ausente
    missing = [n for n, kw in SECTIONS.items() if n not in bodies]
    score = 15 if not missing else max(0, 15 - 2 * len(missing))

    # (3) Counts quantitativos
    counts = {}
    for key in MIN_COUNTS:
        sec = key.split("-", 1)[0]
        counts[key] = _count_items(bodies.get(sec, []))

    thresholds = {
        "0.2-killswitch": (5, 10), "10-redteam": (8, 10), "8-metricas": (8, 10),
        "11-failclosed": (6, 8), "3-dos": (15, 10), "4-donts": (15, 10),
    }
    for key, (abe, pts) in thresholds.items():
        score += pts if counts[key] >= abe else (counts[key] * pts) // abe

    # (4) Proxies declarados (heurísticos, teto 100 somando exatamente §0.9):
    score += 10 if "bypass" in lower else 0                    # Bypass Protocol
    score += 10 if ("lgpd" in lower or "marco civil" in lower) else 0  # ideology
    score += 7 if all(w in lower for w in ("8700g", "cpu")) else \
        (4 if any(w in lower for w in ("8700g", "llama.cpp", "cpu-only")) else 0)
    # language: fingerprints EN dos headers canônicos
    score += 5 if not missing else 0
    score += 5 if "foss" in lower else 0
    score += 5 if not over else max(0, 5 - (est_tokens - TOKEN_BUDGET) // 800)
    score += 5 if (text.startswith("---") and "\nagent-" in text) else \
        (3 if "agent-" in text else 0)

    rep["counts"] = counts
    rep["score"] = min(100, score)

    # FAIL-CLOSED estrutural: seção ausente = BLOCK independente do score (§0.9)
    if missing:
        rep["errors"].append("secções ausentes: " + ", ".join(missing[:8]))
        rep["ok"] = False
        rep["status"] = "rejeitado"
    for key, abe in MIN_COUNTS.items():
        if counts[key] < abe:
            rep["errors"].append(f"{key}: {counts[key]} < mínimo {abe}")
            rep["ok"] = False
            rep["status"] = "rejeitado"
    if over:
        rep["warnings"].append(f"orçamento estourado: ~{est_tokens} > {TOKEN_BUDGET}")
    if rep["score"] < CUT_SCORE and rep["ok"]:
        rep["errors"].append(f"score {rep['score']} < corte {CUT_SCORE}")
        rep["status"] = "rejeitado"
        rep["ok"] = False
    elif rep["ok"] and rep["score"] < 95:
        rep["status"] = "condicional"

    rep["ok"] = not rep["errors"]
    return rep


def main() -> int:
    parser = argparse.ArgumentParser(description="Gate de qualidade §0.9 — forjas AFA")
    parser.add_argument("targets", nargs="*", help="arquivos .md de agentes")
    parser.add_argument("--strict-all", action="store_true",
                        help="cobre frontmatter de todos, inclusive o forjador")
    parser.add_argument("--report", default=None)
    args = parser.parse_args()

    files = [Path(t) for t in args.targets] if args.targets else sorted(AGENTS_DIR.glob("*.md"))
    if not files:
        print("[!] Nenhum agente para validar", file=sys.stderr)
        return 1

    results = []
    for f in files:
        if f.name.startswith(LEGACY_PREFIX) and not args.strict_all:
            results.append({"file": str(f), "ok": True, "status": "legacy-forge",
                            "score": None, "errors": [], "warnings": [],
                            "note": "forjador — fora do escopo do gate"})
        else:
            results.append(analyze(f, args.strict_all))

    summary = {
        "total": len(results),
        "aceitos": sum(1 for r in results if r["ok"]),
        "rejeitados": sum(1 for r in results if not r["ok"]),
        "reports": results,
    }
    out = json.dumps(summary, indent=2, ensure_ascii=False)
    print(out)
    if args.report:
        Path(args.report).write_text(out, encoding="utf-8")
    return 1 if summary["rejeitados"] else 0


if __name__ == "__main__":
    sys.exit(main())
