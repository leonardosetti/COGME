#!/usr/bin/env python3
"""validar_frontmatter_md.py — Valida frontmatter de TODOS os *.md do projeto COGME.

Aplica a Norma Global de Templates para Artefatos (docs/normas/NORMA-TEMPLATES-ARTEFATOS.md):
  - frontmatter YAML na linha 1
  - 10 campos comuns obrigatórios: id, title, type, version, status, owner,
    derived-from, last-revised, lgpd-class, tags
  - type coerente com o diretório (mapeamento diretório → type)
  - status e lgpd-class nos valores fechados
  - id único no repositório

Uso:
  python3 scripts/validar_frontmatter_md.py          # valida, exit 1 se drift
  python3 scripts/validar_frontmatter_md.py --check  # idem (sinônimo, clareza)
"""

import argparse
import re
import sys
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

# Mapeamento diretório → type (Seção 5 da norma)
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

# Raiz: arquivos específicos
TYPE_BY_FILE = {
    "constitution.md": "constituicao",
    "README.md": "readme",
    "AGENTS.md": "readme",
}

VALID_TYPES = set(TYPE_BY_DIR.values()) | set(TYPE_BY_FILE.values())
VALID_STATUSES = {"ativo", "draft", "ratificado", "obsoleto", "arquivado"}
VALID_LGPD = {"n/a", "interno", "sensível"}

COMMON_FIELDS = (
    "id", "title", "type", "version", "status", "owner",
    "derived-from", "last-revised", "lgpd-class", "tags",
)

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def now_iso() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def expected_type(rel_path: Path) -> str | None:
    """Devolve o type esperado para o caminho, ou None se não há regra."""
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
        # Pular symlinks (alias de outro arquivo, não artefato independente)
        if p.is_symlink():
            continue
        # pule pastas excluídas
        parts = p.parts
        if any(part in EXCLUDED_DIR_NAMES for part in parts):
            continue
        # Excluir skills instaladas do OpenCode (mantidas externamente)
        if ".opencode" in parts and "skills" in parts:
            continue
        if ".agents" in parts and "skills" in parts:
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


def validate() -> int:
    errors: list[str] = []
    seen_ids: dict[str, str] = {}
    files = collect_md_files()

    for path in files:
        rel = str(path)
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, _body = parse_frontmatter(text)

        if fm is None:
            errors.append(f"{rel}: frontmatter YAML ausente na linha 1")
            continue

        # Campos comuns obrigatórios
        missing = [f for f in COMMON_FIELDS if f not in fm or fm[f] in (None, "")]
        if missing:
            errors.append(f"{rel}: campos obrigatórios ausentes: {', '.join(missing)}")

        # id único
        fid = fm.get("id")
        if fid:
            if fid in seen_ids:
                errors.append(f"{rel}: id duplicado '{fid}' (já em {seen_ids[fid]})")
            else:
                seen_ids[fid] = rel

        # type válido e coerente com diretório
        ftype = fm.get("type")
        if ftype not in VALID_TYPES:
            errors.append(f"{rel}: type inválido '{ftype}' (válidos: {sorted(VALID_TYPES)})")
        else:
            expected = expected_type(path)
            if expected is not None and ftype != expected:
                errors.append(
                    f"{rel}: type '{ftype}' incoerente com o diretório (esperado '{expected}')"
                )

        # status fechado
        if fm.get("status") not in VALID_STATUSES:
            errors.append(
                f"{rel}: status inválido '{fm.get('status')}' (válidos: {sorted(VALID_STATUSES)})"
            )

        # lgpd-class fechado
        if fm.get("lgpd-class") not in VALID_LGPD:
            errors.append(
                f"{rel}: lgpd-class inválido '{fm.get('lgpd-class')}' "
                f"(válidos: {sorted(VALID_LGPD)})"
            )

        # derived-from deve ser lista
        if not isinstance(fm.get("derived-from"), list):
            errors.append(f"{rel}: derived-from deve ser uma lista")

        # tags deve ser lista
        if not isinstance(fm.get("tags"), list):
            errors.append(f"{rel}: tags deve ser uma lista")

    if errors:
        print(f"[FAIL] {len(errors)} problema(s) de frontmatter em {len(files)} arquivo(s):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"[OK] {len(files)} arquivo(s) .md com frontmatter válido.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida frontmatter de todos os *.md do projeto COGME")
    parser.add_argument("--check", action="store_true",
                        help="apenas reporta drift, não grava (mesmo comportamento padrão)")
    args = parser.parse_args()
    return validate()


if __name__ == "__main__":
    sys.exit(main())
