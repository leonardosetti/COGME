#!/usr/bin/env python3
"""atualizar_referencias_cruzadas.py — Atualiza links markdown e caminhos docs/

dado um mapeamento antigo->novo extraído do relatório de renomeação.

Uso:
  python3 scripts/atualizar_referencias_cruzadas.py --map /tmp/mapeamento.json
  python3 scripts/atualizar_referencias_cruzadas.py --map /tmp/mapeamento.json --check
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path("docs")
LINK_MD_RE = re.compile(r"(\]\(\.?\/)?([^)\s]+\.md)(\"?)")
DOCS_PATH_RE = re.compile(r"(docs\/[^)\s\"'<>]+\.md)")


def carregar_mapa(caminho: Path) -> dict[str, str]:
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def build_stem_index(mapa: dict[str, str]) -> dict[str, str]:
    """stem antigo (sem extensão) -> novo caminho completo (docs/...)."""
    idx = {}
    for antigo, novo in mapa.items():
        idx[Path(antigo).stem] = novo
    return idx


def atualizar_arquivo(p: Path, mapa: dict[str, str], stem_idx: dict[str, str]) -> tuple[str, int]:
    """Retorna (texto_novo, num_substituicoes)."""
    texto = p.read_text(encoding="utf-8", errors="replace")
    original = texto
    base = p.parent.resolve()

    def repl_docs(m):
        c = m.group(1)
        return mapa.get(c, c)

    texto = DOCS_PATH_RE.sub(repl_docs, texto)

    def repl_link(m):
        prefixo = m.group(1) or ""
        c = m.group(2)
        sufixo = m.group(3) or ""
        if c in mapa:
            return prefixo + mapa[c] + sufixo
        try:
            cand = (base / c).resolve()
        except Exception:
            cand = None
        if cand:
            for antigo, novo in mapa.items():
                if (base / antigo).resolve() == cand:
                    return prefixo + novo + sufixo
        if "/" not in c and "\\" not in c:
            stem = Path(c).stem
            if stem in stem_idx:
                return prefixo + stem_idx[stem] + sufixo
        return prefixo + c + sufixo

    texto = LINK_MD_RE.sub(repl_link, texto)
    n = sum(1 for a, b in zip(original, texto) if a != b) + abs(len(original) - len(texto))
    return texto, n if texto != original else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Atualiza referências cruzadas após renomeação kebab-case")
    parser.add_argument("--map", required=True, help="arquivo JSON com mapeamento antigo->novo")
    parser.add_argument("--check", action="store_true", help="apenas reporta, não grava")
    args = parser.parse_args()

    mapa = carregar_mapa(Path(args.map))
    stem_idx = build_stem_index(mapa)

    total = 0
    alterados = 0
    total_subs = 0

    for dirpath, dirs, files in __import__("os").walk(ROOT):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = Path(dirpath) / fn
            total += 1
            texto, _ = atualizar_arquivo(p, mapa, stem_idx)
            # conta substituicoes aproximadas: comparar ocorrencias de caminhos antigos
            subs = 0
            for antigo in mapa:
                subs += texto.count(antigo)  # após substituição, antigos não devem mais aparecer
            # na verdade, contar antes vs depois é mais confiável
            original = p.read_text(encoding="utf-8", errors="replace")
            antes = sum(original.count(a) for a in mapa)
            depois = sum(texto.count(a) for a in mapa)
            nsubs = antes - depois
            if nsubs > 0:
                alterados += 1
                total_subs += nsubs
                if not args.check:
                    p.write_text(texto, encoding="utf-8")

    print(f"[OK] {total} arquivos varridos, {alterados} com referências atualizadas, {total_subs} substituições.")
    if args.check:
        print("[check] Nenhuma gravação realizada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
