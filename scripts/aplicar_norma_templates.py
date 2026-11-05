#!/usr/bin/env python3
"""aplicar_norma_templates.py — Converte *.md para o padrão da Norma Global de Templates.

Converte o frontmatter gerado pela auditoria de 2026-11-05 (chave ``class``,
status ``active``, lgpd-class ``n/a (sem PII)``) para o novo padrão comum
(chave ``type``, status ``ativo``, lgpd-class ``n/a``) e preenche campos
faltantes. Arquivos sem frontmatter recebem um frontmatter inicial derivado do
nome/caminho.

A norma completa está em docs/normas/NORMA-TEMPLATES-ARTEFATOS.md.

Uso:
  python3 scripts/aplicar_norma_templates.py --check   # mostra o que mudaria
  python3 scripts/aplicar_norma_templates.py --apply   # grava as mudanças
"""

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(".")
# Pastas excluídas por nome (em qualquer nível)
EXCLUDED_DIR_NAMES = {
    ".git", "node_modules", ".venv", "venv", ".pytest_cache", "graphify-out",
    "__pycache__",
}
# Caminhos prefixo excluídos (skills instaladas do OpenCode, mantidas externamente)
EXCLUDED_PREFIXES = (".opencode/skills/",)

# class (antigo) → type (novo)
CLASS_TO_TYPE = {
    "relatorio-levantamento": "relatorio",
    "artefato-arquivo": "archive",
    "relatorio-auditoria": "audit",
    "change-request": "change-request",
    "relatorio-compliance": "governanca",
    "conhecimento": "conhecimento",
    "decisao-adr": "adr",
    "registro-dependencias": "conhecimento",
    "especificacao": "spec",
    "relatorio-evidencia": "evidencia",
    "relatorio-governanca": "governanca",
    "metrica": "metrica",
    "procedimento-operacao": "procedimento",
    "plano-gerenciamento": "plano",
    "relatorio": "relatorio",
    "requisito": "requisito",
    "apresentacao": "conhecimento",
    "resumo-stakeholder": "conhecimento",
    "termo-abertura": "spec",
    "registro-verificacao": "audit",
}

# Mapeamento diretório → type (para arquivos sem frontmatter ou sem class reconhecido)
TYPE_BY_DIR = {
    "docs/decisoes": "adr",
    "docs/change-requests": "change-request",
    "docs/auditorias": "audit",
    "docs/especificacoes": "spec",
    "docs/planos": "plano",
    "docs/operacao": "procedimento",
    "docs/relatorios": "relatorio",
    "docs/evidencias": "evidencia",
    "docs/metricas": "metrica",
    "docs/requisitos": "requisito",
    "docs/governanca": "governanca",
    "docs/conhecimento": "conhecimento",
    "docs/archive": "archive",
    "docs/analise": "relatorio",
    "docs/uat": "test",
    "docs/tap": "spec",
    "docs/verification": "audit",
    ".ai/specs": "spec",
    ".ai/handoffs": "handoff",
    ".ai/personas": "persona",
}
TYPE_BY_FILE = {
    "constitution.md": "constituicao",
    "README.md": "readme",
    "AGENTS.md": "readme",
}

VALID_STATUSES = {"ativo", "draft", "ratificado", "obsoleto", "arquivado"}
VALID_LGPD = {"n/a", "interno", "sensível"}

COMMON_FIELDS = (
    "id", "title", "type", "version", "status", "owner",
    "derived-from", "last-revised", "lgpd-class", "tags",
)

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


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


def expected_type(rel_path: Path) -> str | None:
    name = rel_path.name
    if name in TYPE_BY_FILE:
        return TYPE_BY_FILE[name]
    for dir_prefix, t in TYPE_BY_DIR.items():
        if str(rel_path).startswith(dir_prefix + "/") or str(rel_path) == dir_prefix:
            return t
    return None


def parse_frontmatter(text: str):
    m = FM_RE.match(text)
    if not m:
        return None, text
    if yaml is None:
        return None, text
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except Exception:
        return None, text
    if not isinstance(data, dict):
        return None, text
    body = text[m.end():]
    return data, body


def collect_md_files() -> list[Path]:
    files: list[Path] = []
    for p in ROOT.rglob("*.md"):
        parts = p.parts

        # Pular symlinks (alias de outro arquivo, não artefato independente)
        if p.is_symlink():
            continue

        # Excluir pastas por nome (em qualquer nível)
        if any(part in EXCLUDED_DIR_NAMES for part in parts):
            continue

        # Excluir skills instaladas do OpenCode (mantidas externamente)
        if (".opencode" in parts and "skills" in parts) or (".agents" in parts and "skills" in parts):
            continue

        # Em .opencode/, só agentes COGME nativos (.opencode/agents/agent-*.md)
        if ".opencode" in parts:
            idx = parts.index(".opencode")
            resto = parts[idx + 1:]
            if not (len(resto) >= 2 and resto[0] == "agents" and resto[1].startswith("agent-")):
                continue

        files.append(p)
    files.sort()
    return files


def build_frontmatter(fm: dict | None, rel_path: Path, text: str, today: str) -> dict:
    """Monta o frontmatter canônico a partir do existente (ou vazio)."""
    fm = fm or {}

    # id: único no repositório, derivado do caminho relativo (não preserva id existente que pode colidir)
    _id = str(rel_path).replace("/", "-").replace(".md", "")
    _id = slugify(_id)

    # title
    _title = str(fm.get("title") or extract_title(text, rel_path.stem.replace("-", " ").title()))

    # version
    _version = str(fm.get("version") or "1.0.0")

    # type: diretório tem prioridade; depois converte class antiga; fallback conhecimento
    _type = expected_type(rel_path)
    if _type is None:
        _class = fm.get("class")
        if _class in CLASS_TO_TYPE:
            _type = CLASS_TO_TYPE[_class]
        else:
            _type = fm.get("type")
            if _type not in set(list(TYPE_BY_DIR.values()) + list(TYPE_BY_FILE.values())):
                _type = "conhecimento"

    # status: converter 'active' → 'ativo'
    _status = fm.get("status")
    if _status == "active":
        _status = "ativo"
    if _status not in VALID_STATUSES:
        _status = "ativo"

    # owner
    _owner = str(fm.get("owner") or "agent-project-analyst")

    # derived-from
    _derived = fm.get("derived-from")
    if not isinstance(_derived, list) or not _derived:
        _derived = [f"{rel_path} (adequado à norma em {today})"]

    # last-revised
    _last = str(fm.get("last-revised") or today)

    # lgpd-class: converter 'n/a (sem PII)' → 'n/a'
    _lgpd = fm.get("lgpd-class")
    if _lgpd == "n/a (sem PII)":
        _lgpd = "n/a"
    if _lgpd not in VALID_LGPD:
        _lgpd = "n/a"

    # tags
    _tags = fm.get("tags")
    if not isinstance(_tags, list) or not _tags:
        _tags = [rel_path.parent.name, "docs", "adequado-a-norma"]
    if isinstance(_tags, str):
        _tags = [_tags]

    return {
        "id": _id,
        "title": _title,
        "type": _type,
        "version": _version,
        "status": _status,
        "owner": _owner,
        "derived-from": _derived,
        "last-revised": _last,
        "lgpd-class": _lgpd,
        "tags": _tags,
    }


def dump_frontmatter(data: dict) -> str:
    lines = ["---"]
    lines.append(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120).rstrip())
    lines.append("---")
    return "\n".join(lines) + "\n"


def process_file(path: Path, today: str, apply: bool) -> dict:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = parse_frontmatter(text)
    had_fm = fm is not None

    new = build_frontmatter(fm, rel, text, today)

    changed = (
        not had_fm
        or new != fm
        or "class" in (fm or {})
    )

    report = {
        "file": str(rel),
        "had_frontmatter": had_fm,
        "id": new["id"],
        "type": new["type"],
        "status": new["status"],
        "changed": changed,
    }

    if apply and changed:
        out = dump_frontmatter(new) + body
        path.write_text(out, encoding="utf-8")

    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Aplica a Norma Global de Templates aos *.md do projeto COGME")
    parser.add_argument("--check", action="store_true",
                        help="mostra o que mudaria, não grava")
    parser.add_argument("--apply", action="store_true",
                        help="grava as mudanças nos arquivos")
    args = parser.parse_args()

    if not args.check and not args.apply:
        parser.error("use --check ou --apply")

    today = now_iso()
    files = collect_md_files()
    reports = [process_file(p, today, args.apply) for p in files]

    changed = sum(1 for r in reports if r["changed"])
    total = len(reports)
    verb = "seriam alterados" if args.check else "alterados"
    print(f"[INFO] {total} arquivo(s) varrido(s), {changed} {verb}.")
    if args.check and changed:
        print("[INFO] Rode com --apply para gravar.")
    elif args.apply:
        print("[OK] Mudanças gravadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
