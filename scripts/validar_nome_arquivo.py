#!/usr/bin/env python3
"""validar_nome_arquivo.py — Valida nomes de *.md contra a Norma de Nomenclatura.

Regra: {prefixo}-{slug}.md, kebab-case, prefixo coerente com o diretório.

Uso:
  python3 scripts/validar_nome_arquivo.py [caminho_arquivo ...]
  (sem argumentos: valida todos os *.md do escopo)
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(".")
EXCLUDED_DIR_NAMES = {
    ".git", "node_modules", ".venv", "venv", ".pytest_cache", "graphify-out",
    ".planning", "__pycache__",
}
EXCLUDED_PATH_PARTS = (".opencode/skills", ".agents/skills")

NOME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")

# diretório → prefixo esperado
PREFIXO_BY_DIR = {
    "docs/decisoes": "adr",
    "docs/change-requests": "cr",
    "docs/auditorias": "aud",
    "docs/especificacoes": "spec",
    "docs/planos": "plan",
    "docs/operacao": "proc",
    "docs/relatorios": "rel",
    "docs/evidencias": "evid",
    "docs/metricas": "met",
    "docs/requisitos": "req",
    "docs/governanca": "gov",
    "docs/conhecimento": "kb",
    "docs/archive": "arc",
    "docs/analise": "ana",
    "docs/uat": "uat",
    "docs/tap": "tap",
    "docs/verification": "ver",
    ".ai/handoffs": "hf",
    ".ai/specs": "spec",
    ".ai/personas": "pers",
}

# Artefatos canônicos preservados por decisão de governança (CCB/OKB) —
# renomeá-los quebraria referências em README, specs e planos (Norma §8).
NOME_CANONICO = {"constitution.md", "README.md", "AGENTS.md", "okb.md", "ccb-log.md"}


def coletar_arquivos(alvos):
    if alvos:
        return [
            Path(a) for a in alvos
            if not any(part in EXCLUDED_DIR_NAMES for part in Path(a).parts)
            and not any(part in EXCLUDED_PATH_PARTS for part in Path(a).parts)
        ]
    files = []
    for p in ROOT.rglob("*.md"):
        parts = p.parts
        if any(part in EXCLUDED_DIR_NAMES for part in parts):
            continue
        if any(part in EXCLUDED_PATH_PARTS for part in parts):
            continue
        files.append(p)
    files.sort()
    return files


def prefixo_esperado(caminho: Path) -> str | None:
    partes = caminho.parts
    for i, part in enumerate(partes):
        chave = "/".join(partes[: i + 1])
        if chave in PREFIXO_BY_DIR:
            return PREFIXO_BY_DIR[chave]
    if caminho.name in NOME_CANONICO:
        return None
    return None


def validar(args) -> int:
    alvos = coletar_arquivos(args.alvos) if args.alvos else coletar_arquivos(None)
    erros = []
    for caminho in alvos:
        nome = caminho.name
        if nome in NOME_CANONICO:
            continue
        if not NOME_RE.match(nome):
            erros.append(f"{caminho}: nome fora de kebab-case '{nome}'")
            continue
        esperado = prefixo_esperado(caminho)
        if esperado is None:
            continue  # diretório sem regra de prefixo
        prefixo_atual = nome.split("-")[0]
        if prefixo_atual != esperado:
            erros.append(
                f"{caminho}: prefixo '{prefixo_atual}' incoerente com diretório "
                f"(esperado '{esperado}')"
            )
    if erros:
        print(f"[FAIL] {len(erros)} problema(s) de nomeclatura:")
        for e in erros:
            print(f"  - {e}")
        return 1
    print("[OK] Nomes de arquivo válidos.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida nomes de *.md contra a Norma de Nomenclatura")
    parser.add_argument("alvos", nargs="*", help="arquivos .md para validar")
    args = parser.parse_args()
    return validar(args)


if __name__ == "__main__":
    sys.exit(main())
