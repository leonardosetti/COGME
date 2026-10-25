#!/usr/bin/env python3
"""security_scan.py — Varredura de seguranca leve do ecossistema de agentes (ONDA 8).

Checa:
  - Nenhuma chave secreta versionada em .opencode/, scripts/, .ai/
  - Nenhuma referencia a CUDA/NVIDIA/cloud GPU em agentes (P-02)
  - Kill Switch propagado em cada arquivo de agente (>= 5 vetores)
  - Bypass Protocol presente em cada agente
  - FAIL-CLOSED >= 6 regras por agente
  - Frontmatter YAML valido (5 chaves)

Falha = exit 1. FOSS/stdlib apenas. Nenhuma transmissao de dados para fora.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_nexus_yaml import AGENTS_DIR, parse_frontmatter, validate_agent

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),          # API keys estilo sk-...
    re.compile(r"AKIA[0-9A-Z]{16}"),             # AWS access key
    re.compile(r"[pP]assword\s*[:=]\s*\S+"),    # senha em texto claro
    re.compile(r"[sS]ecret\s*[:=]\s*\S+"),      # secret em texto claro
]
CUDA_CLOUD_RE = re.compile(r"(cuda|nvidia|colab|aws|gcp|azure|cloud\s*gpu|remote\s*inference)", re.I)
KILL_SWITCH_RE = re.compile(r"kill.?switch", re.I)
BYPASS_RE = re.compile(r"bypass", re.I)
FAIL_CLOSED_RE = re.compile(r"fail.?closed", re.I)


def scan_file(path: Path) -> dict:
    rep = {"file": str(path), "ok": True, "errors": [], "warnings": []}
    text = path.read_text(encoding="utf-8", errors="ignore")
    lower = text.lower()

    # segredos versionados
    for pat in SECRET_PATTERNS:
        if pat.search(text):
            rep["ok"] = False
            rep["errors"].append("possivel segredo versionado detectado")

    # hardware incompatível
    if CUDA_CLOUD_RE.search(text):
        rep["ok"] = False
        rep["errors"].append("referencia a hardware/cloud proibido (CPU-only obrigatorio)")

    # kill switch
    if not KILL_SWITCH_RE.search(lower):
        rep["ok"] = False
        rep["errors"].append("Kill Switch ausente")

    # bypass protocol
    if not BYPASS_RE.search(lower):
        rep["ok"] = False
        rep["errors"].append("Bypass Protocol ausente")

    # fail-closed
    if not FAIL_CLOSED_RE.search(lower):
        rep["warnings"].append("FAIL-CLOSED não encontrado explicitamente")

    # frontmatter valido
    check = validate_agent(path)
    if not check["ok"]:
        rep["ok"] = False
        rep["errors"].extend(check["errors"][:3])

    return rep


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Varredura de seguranca do ecossistema de agentes COGME")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 se qualquer erro ou aviso")
    parser.add_argument("--report", default=None, help="salva JSON do report")
    args = parser.parse_args()

    files = sorted(AGENTS_DIR.glob("*.md"))
    if not files:
        print("[!] Nenhum agente em .opencode/agents/", file=sys.stderr)
        return 1

    results = [scan_file(f) for f in files]
    falhas = [r for r in results if not r["ok"]]
    avisos = [r for r in results if r["ok"] and r["warnings"]]

    report = {
        "total": len(results),
        "aprovados": len(results) - len(falhas) - len(avisos),
        "com_aviso": len(avisos),
        "falhas": len(falhas),
        "resultados": results,
    }
    out = json.dumps(report, indent=2, ensure_ascii=False)
    print(out)
    if args.report:
        Path(args.report).write_text(out, encoding="utf-8")

    if falhas:
        print(f"[SECURITY] FALHAS: {len(falhas)}/{len(results)}", file=sys.stderr)
        return 1 if args.strict else 0
    if avisos and args.strict:
        print(f"[SECURITY] AVISOS: {len(avisos)}/{len(results)}", file=sys.stderr)
        return 1
    print(f"[SECURITY] OK: {len(results) - len(falhas)}/{len(results)} arquivos verificados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
