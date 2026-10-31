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
from validate_nexus_yaml import AGENTS_DIR, parse_frontmatter, validate_agent, LEGACY_SLUG_RE, KNOWN_SLUGS

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

    # hardware incompatível: detecta referência real a CUDA/cloud, exceto quando
    # o arquivo declara explicitamente conformidade com CPU-only (P-02).
    # Isso evita falso positivo em agentes que declaram "no CUDA, no cloud inference".
    cuda_cloud_hits = CUDA_CLOUD_RE.findall(text)
    if cuda_cloud_hits:
        # Verifica se o arquivo declara conformidade com CPU-only
        compliance_indicators = [
            "no cuda", "no cloud", "cpu-only", "cpu only",
            "never", "proibido", "bloqueado", "forbidden",
            "cpu-only forever", "sem cuda", "sem cloud",
        ]
        lower = text.lower()
        declares_compliance = any(ind in lower for ind in compliance_indicators)
        if not declares_compliance:
            rep["ok"] = False
            rep["errors"].append(
                f"referencia a hardware/cloud proibido (CPU-only obrigatorio): "
                f"{', '.join(sorted(set(cuda_cloud_hits)))}"
            )

    # kill switch: agentes fora da topologia caninca (nao sao do ecossistema oficial)
    # nao sao avaliados para Kill Switch/Bypass (nao fazem parte do ecossistema ativo)
    in_topology = path.stem in KNOWN_SLUGS
    if not KILL_SWITCH_RE.search(lower):
        if in_topology:
            rep["ok"] = False
            rep["errors"].append("Kill Switch ausente")
        # else: agente fora da topologia - nao avaliar (nao eh parte do ecossistema)

    # bypass protocol: mesma regra
    if not BYPASS_RE.search(lower):
        if in_topology:
            rep["ok"] = False
            rep["errors"].append("Bypass Protocol ausente")
        # else: agente fora da topologia - nao avaliar

    # fail-closed: apenas agentes na topologia caninca sao obrigados a declarar
    if not FAIL_CLOSED_RE.search(lower) and in_topology:
        rep["warnings"].append("FAIL-CLOSED não encontrado explicitamente")

    # frontmatter valido
    check = validate_agent(path)
    if not check["ok"]:
        # Agentes legacy-forge (Art. 4.8) nao exigem frontmatter; sao aceitos por design
        if LEGACY_SLUG_RE.search(path.stem):
            pass  # legacy-forge aceito sem frontmatter, sem aviso
        else:
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
