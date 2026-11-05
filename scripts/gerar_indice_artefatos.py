#!/usr/bin/env python3
"""gerar_indice_artefatos.py — Gera índice de artefatos *.md a partir do frontmatter.

Lê todo .md do escopo com frontmatter válido e gera docs/normas/INDICE-ARTEFATOS.md
mapeando id → caminho → tipo → status. Usado para rastreamento e tracking.

Uso:
  python3 scripts/gerar_indice_artefatos.py
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(".")
EXCLUDED_DIR_NAMES = {
    ".git", "node_modules", ".venv", "venv", ".pytest_cache", "graphify-out",
    "__pycache__",
}
EXCLUDED_PATH_PARTS = (".opencode/skills", ".agents/skills")

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def coletar_arquivos():
    files = []
    for p in ROOT.rglob("*.md"):
        parts = p.parts
        if any(part in EXCLUDED_DIR_NAMES for part in parts):
            continue
        if any(part in EXCLUDED_PATH_PARTS for part in parts):
            continue
        if p.is_symlink():
            continue
        files.append(p)
    files.sort()
    return files


def ler_frontmatter(caminho: Path):
    texto = caminho.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(texto)
    if not m or yaml is None:
        return None
    try:
        dados = yaml.safe_load(m.group(1)) or {}
    except Exception:
        return None
    if not isinstance(dados, dict):
        return None
    return dados


def gerar():
    arquivos = coletar_arquivos()
    entradas = []
    for caminho in arquivos:
        fm = ler_frontmatter(caminho)
        if fm is None:
            continue
        ident = fm.get("id")
        if not ident:
            continue
        entradas.append({
            "id": str(ident),
            "caminho": str(caminho),
            "tipo": fm.get("type", "-"),
            "status": fm.get("status", "-"),
            "titulo": str(fm.get("title", "-")),
        })
    entradas.sort(key=lambda e: e["id"])

    linhas = []
    linhas.append("# Índice de Artefatos Markdown")
    linhas.append("")
    linhas.append(f"Total de artefatos indexados: {len(entradas)}")
    linhas.append("")
    linhas.append("| id | caminho | tipo | status | título |")
    linhas.append("|---|---|---|---|---|")
    for e in entradas:
        linhas.append(
            f"| `{e['id']}` | `{e['caminho']}` | `{e['tipo']}` | `{e['status']}` | {e['titulo']} |"
        )
    linhas.append("")
    linhas.append("---")
    linhas.append("*Índice gerado automaticamente a partir do frontmatter `id` de cada `.md`.*")

    saida = Path("docs/normas/INDICE-ARTEFATOS.md")
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"[OK] Índice gerado em {saida} ({len(entradas)} entradas).")
    return 0


if __name__ == "__main__":
    sys.exit(gerar())
