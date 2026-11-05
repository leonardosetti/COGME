#!/usr/bin/env python3
"""normalizar_artefatos_docs.py — Normaliza frontmatter de artefatos .md em ./docs/*/*.

Aplica frontmatter YAML canônico a todos os artefatos Markdown sob ./docs/*/*,
preservando o corpo existente. Gera relatório de auditoria em
./docs/conhecimento/compliance/AUDITORIA-NORMALIZACAO-ARTIFACTOS.md.

Não renomeia arquivos (evita quebrar referências cruzadas). Reporta o estado
antes/depois por arquivo para rastreabilidade.

Uso:
  python3 scripts/normalizar_artefatos_docs.py          # aplica normalização
  python3 scripts/normalizar_artefatos_docs.py --check  # apenas reporta drift
"""

import argparse
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("docs")
REPORT_DIR = Path("docs/conhecimento/compliance")
REPORT_PATH = REPORT_DIR / "AUDITORIA-NORMALIZACAO-ARTIFACTOS.md"

# Classe canônica por subpasta de docs/
CLASS_BY_DIR = {
    "analise": "relatorio-levantamento",
    "archive": "artefato-arquivo",
    "auditorias": "relatorio-auditoria",
    "change-requests": "change-request",
    "compliance": "relatorio-compliance",
    "conhecimento": "conhecimento",
    "decisoes": "decisao-adr",
    "dependencias": "registro-dependencias",
    "especificacoes": "especificacao",
    "evidencias": "relatorio-evidencia",
    "governanca": "relatorio-governanca",
    "metricas": "metrica",
    "operacao": "procedimento-operacao",
    "planos": "plano-gerenciamento",
    "relatorios": "relatorio",
    "requisitos": "requisito",
    "slides_apresentacao": "apresentacao",
    "stakeholder": "resumo-stakeholder",
    "tap": "termo-abertura",
    "verification": "registro-verificacao",
}

VALID_CLASSES = set(CLASS_BY_DIR.values()) | {
    "spec", "relatorio", "plano", "decisao", "auditoria", "glossario",
    "especificacao", "procedimento", "registro", "apresentacao",
}
VALID_STATUSES = {"active", "draft", "ratificado", "obsoleto", "arquivado", "blocked", "ready"}

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
ID_RE = re.compile(r"^id:\s*(\S+)", re.MULTILINE)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def slugify(name: str) -> str:
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    return re.sub(r"-+", "-", name).strip("-")


def extract_title(text: str, fallback: str) -> str:
    m = H1_RE.search(text)
    if m:
        return m.group(1).strip()
    return fallback


def extract_version(text: str) -> str:
    m = re.search(r"v(?:ersão)?\.?\s*(\d+\.\d+(?:\.\d+)?)", text, re.IGNORECASE)
    if m:
        return m.group(1)
    m = re.search(r"version:\s*(\S+)", text)
    if m:
        return m.group(1)
    return "1.0.0"


def parse_frontmatter(text: str):
    m = FM_RE.match(text)
    if not m:
        return None, text
    try:
        import yaml
        data = yaml.safe_load(m.group(1)) or {}
    except Exception:
        return None, text
    body = text[m.end():]
    return data, body


def canonical_id(fm: dict, rel_path: Path) -> str:
    if fm and fm.get("id"):
        return str(fm["id"])
    stem = rel_path.stem
    parent = rel_path.parent.name
    return f"{parent}-{slugify(stem)}"


def canonical_class(fm: dict, rel_path: Path) -> str:
    if fm and fm.get("class") in VALID_CLASSES:
        return str(fm["class"])
    parent = rel_path.parent.name
    return CLASS_BY_DIR.get(parent, "conhecimento")


def canonical_status(fm: dict, text: str, rel: Path) -> str:
    if fm and fm.get("status") in VALID_STATUSES:
        return str(fm["status"])
    low = text.lower()
    if "obsoleto" in low or "deprecated" in low or "[legacy]" in rel.name.lower():
        return "obsoleto"
    if "draft" in low or "rascunho" in low:
        return "draft"
    if "ratificado" in low or "promulgado" in low:
        return "ratificado"
    if "arquivado" in low or "archive" in low:
        return "arquivado"
    return "active"


def build_frontmatter(fm: dict, rel_path: Path, text: str, today: str) -> dict:
    _id = canonical_id(fm, rel_path)
    _title = extract_title(text, rel_path.stem.replace("-", " ").title())
    _version = str(fm.get("version") or extract_version(text))
    _class = canonical_class(fm, rel_path)
    _status = canonical_status(fm, text, rel_path)
    _owner = str(fm.get("owner") or "agent-project-analyst")
    _last = str(fm.get("last-revised") or today)
    _lgpd = str(fm.get("lgpd-class") or "n/a")
    _tags = fm.get("tags") or [rel_path.parent.name, "docs", "normalizado"]
    if isinstance(_tags, str):
        _tags = [_tags]

    return {
        "id": _id,
        "title": _title,
        "version": _version,
        "class": _class,
        "status": _status,
        "owner": _owner,
        "derived-from": [f"docs/{rel_path} (normalizado em {today})"],
        "last-revised": _last,
        "lgpd-class": _lgpd,
        "tags": _tags,
    }


def dump_frontmatter(data: dict) -> str:
    import yaml
    lines = ["---"]
    lines.append(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120).rstrip())
    lines.append("---")
    return "\n".join(lines) + "\n"


def normalize_file(path: Path, today: str, check_only: bool) -> dict:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(text)
    had_fm = fm is not None

    if had_fm and fm:
        # Já tem frontmatter: apenas normaliza campos ausentes/ínvalidos
        new = build_frontmatter(fm, rel, text, today)
        changed = new != fm
    else:
        new = build_frontmatter({}, rel, text, today)
        changed = True

    report = {
        "file": str(rel),
        "had_frontmatter": had_fm,
        "id": new["id"],
        "title": new["title"],
        "version": new["version"],
        "class": new["class"],
        "status": new["status"],
        "changed": changed,
        "error": None,
    }

    if not check_only and changed:
        out = dump_frontmatter(new) + body
        path.write_text(out, encoding="utf-8")

    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Normaliza frontmatter de artefatos docs/*/*")
    parser.add_argument("--check", action="store_true", help="apenas reporta drift, não grava")
    args = parser.parse_args()

    today = now_iso()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    files = []
    for dirpath, dirs, fnames in os.walk(ROOT):
        for fn in fnames:
            if not fn.endswith(".md"):
                continue
            p = Path(dirpath) / fn
            parts = p.relative_to(ROOT).parts
            if len(parts) < 2:
                continue  # só ./docs/*/* (mínimo duas níveis)
            files.append(p)
    files.sort()

    reports = []
    for p in files:
        reports.append(normalize_file(p, today, args.check))

    changed = sum(1 for r in reports if r["changed"])
    total = len(reports)
    had = sum(1 for r in reports if r["had_frontmatter"])

    # Relatório de auditoria
    lines = []
    lines.append("# Relatório de Auditoria — Normalização de Artefatos docs/*/*")
    lines.append("")
    lines.append(f"**Gerado em:** {today}")
    lines.append(f"**Total de artefatos .md:** {total}")
    lines.append(f"**Com frontmatter antes:** {had}")
    lines.append(f"**Sem frontmatter antes:** {total - had}")
    lines.append(f"**Artefatos alterados:** {changed}")
    lines.append(f"**Artefatos inalterados:** {total - changed}")
    lines.append("")
    lines.append("## Padrão aplicado (frontmatter canônico)")
    lines.append("```yaml")
    lines.append("---")
    lines.append("id: <identificador>")
    lines.append("title: <título>")
    lines.append("version: <versão>")
    lines.append("class: <classe>")
    lines.append("status: <status>")
    lines.append("owner: <responsável>")
    lines.append("derived-from:")
    lines.append("  - <fonte>")
    lines.append("last-revised: <YYYY-MM-DD>")
    lines.append("lgpd-class: <classe LGPD>")
    lines.append("tags:")
    lines.append("  - <tag>")
    lines.append("---")
    lines.append("```")
    lines.append("")
    lines.append("## Classes por diretório")
    for d, c in sorted(CLASS_BY_DIR.items()):
        lines.append(f"- `docs/{d}/` → `{c}`")
    lines.append("")
    lines.append("## Status de validação")
    statuses = {}
    for r in reports:
        statuses[r["status"]] = statuses.get(r["status"], 0) + 1
    for s, n in sorted(statuses.items()):
        lines.append(f"- `{s}`: {n}")
    lines.append("")
    lines.append("## Detalhe por arquivo")
    lines.append("")
    lines.append("| Arquivo | Antes FM | ID | Título | Versão | Classe | Status | Alterado |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for r in reports:
        lines.append(
            f"| {r['file']} | {'sim' if r['had_frontmatter'] else 'não'} | "
            f"`{r['id']}` | {r['title']} | {r['version']} | {r['class']} | "
            f"{r['status']} | {'sim' if r['changed'] else 'não'} |"
        )
    lines.append("")
    lines.append("## Escopo não coberto")
    lines.append("- Renomeação de arquivos: não realizada (evita quebrar referências cruzadas).")
    lines.append("- Atualização automática de referências cruzadas internas: não realizada;")
    lines.append("  verificar manualmente links que apontam para IDs de artefato.")
    lines.append("- Arquivos não-Markdown (.docx, .pdf, .png, .svg, .drawio): fora de escopo de frontmatter.")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[OK] {total} artefatos varridos, {changed} alterados.")
    print(f"[OK] Relatório gravado em {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
