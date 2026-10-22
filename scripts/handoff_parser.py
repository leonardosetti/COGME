#!/usr/bin/env python3
"""handoff_parser.py — Extrai handoffs SDD estruturados (FASE S.2).

Contrato canônico de handoff (constituição.md Art. 6.1; consumido por agent-sdd-specialist):

    ---
    id: HF-001
    agent: agent-backend-dev
    status: ready            # draft|ready|dispatched|in_progress|done|blocked
    created: 2026-10-22
    ---
    # Handoff: <título>
    ## Contexto
    ...
    ## Tarefa
    ...
    ## Critérios de Aceite
    - [ ] critério 1
    - [x] critério 2
    ## Restrições
    ...

Saída: JSON estruturado (payload dispatchable). Fail-closed → exit 1.
FOSS/stdlib: argparse + yaml + re.

Uso:
  python3 scripts/handoff_parser.py .ai/handoffs/HF-001.md
  python3 scripts/handoff_parser.py --dir .ai/handoffs
  python3 scripts/handoff_parser.py arquivo.md --output /tmp/payload.json
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

HANDOFFS_DIR = Path(".ai/handoffs")
VALID_STATUSES = {"draft", "ready", "dispatched", "in_progress", "done", "blocked"}
ID_RE = re.compile(r"^HF-\d{3,4}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
CHECKBOX_RE = re.compile(r"^[-*]\s\[( |x|X)\]\s(.+)$")
HEADER_RE = re.compile(r"^(#{1,3})\s+(.*)$")


def _parse_frontmatter(lines):
    if lines[0].strip() != "---":
        return None, "handoff sem frontmatter YAML (Art. 6.1)"
    if len(lines) < 3 or lines[1].strip() == "---":
        return None, "frontmatter degenerado"
    try:
        end = next(i for i, ln in enumerate(lines) if i > 0 and ln.strip() == "---")
    except StopIteration:
        return None, "frontmatter aberto: fechamento ausente"
    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        return None, f"YAML inválido: {str(exc)[:120]}"
    if not isinstance(data, dict):
        return None, "frontmatter não é mapping YAML"
    return data, end


def _normalize_meta(meta: dict) -> dict:
    """Coerção defensiva: PyYAML converte datas ISO em objetos date — normaliza para str."""
    out = {}
    for k, v in meta.items():
        if hasattr(v, "isoformat"):
            out[k] = v.isoformat()
        elif isinstance(v, str) and str(v)[:10].isdigit():
            out[k] = v
        else:
            out[k] = v
    return out


def parse_handoff(path: Path) -> dict:
    """Parseia UM handoff. Nunca lança: retorna report fail-closed."""
    rep = {"file": str(path), "ok": True, "errors": [], "warnings": []}
    if not path.exists():
        rep["ok"], rep["errors"] = False, [f"arquivo inexistente: {path}"]
        return rep
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    meta, end = _parse_frontmatter(lines)
    if meta is None:
        rep["ok"] = False
        rep["errors"].append(end)
        return rep
    meta = _normalize_meta(meta)
    rep["meta"] = meta

    # --- Metadata: chaves e enums -----------------------------------------
    hid = str(meta.get("id") or "")
    if not ID_RE.match(hid):
        rep["errors"].append(f"id fora do padrão HF-NNN: {hid!r}")
    agent = str(meta.get("agent") or "")
    if not agent.startswith("agent-"):
        rep["errors"].append(f"alvo fora do roster: {agent!r}")
    status = str(meta.get("status") or "")
    if status not in VALID_STATUSES:
        rep["errors"].append(f"status fora do enum: {status!r}")
    created = str(meta.get("created") or "")
    if not DATE_RE.match(created):
        rep["errors"].append(f"created fora do padrão ISO: {created!r}")
    if not DATE_RE.match(created):
        rep["errors"].append(f"created fora do padrão ISO: {created!r}")
    elif date.fromisoformat(created) > date.today():
        rep["warnings"].append("created no futuro")

    # --- Corpo: secções numeradas + critérios ------------------------------
    body = lines[end + 1:]
    sections, current = {}, None
    acceptance = []
    for ln in body:
        m = HEADER_RE.match(ln)
        if m:
            current = m.group(2).strip()
            sections[current] = []
        elif current is not None:
            cm = CHECKBOX_RE.match(ln.strip())
            if cm:
                acceptance.append({"criterion": cm.group(2).strip(),
                                   "done": cm.group(1).lower() == "x"})
            elif ln.strip():
                sections[current].append(ln.rstrip())
    rep["title"] = next((k.lstrip("# ").replace("Handoff:", "").strip()
                         for k, v in sections.items() if k.startswith("#")), "")
    rep["sections"] = {k: v for k, v in sections.items()}
    rep["acceptance"] = acceptance

    if not sections:
        rep["errors"].append("corpo sem secções de contrato")
    if not any("Critérios" in k for k in sections):
        rep["errors"].append("secção 'Critérios de Aceite' ausente")
    if not acceptance:
        rep["errors"].append("nenhum critério de aceite parseado")
    if rep.get("meta", {}).get("status") in ("ready", "dispatched") and \
            all(a["done"] for a in acceptance):
        rep["warnings"].append("handoff ready/dispated com todos critérios já done")

    rep["ok"] = not rep["errors"]
    return rep


def main() -> int:
    parser = argparse.ArgumentParser(description="Parseia handoffs SDD para payloads dispatchable")
    parser.add_argument("targets", nargs="*", help="arquivos .md do handoff")
    parser.add_argument("--dir", default=None, help="processa todo diretório de handoffs")
    parser.add_argument("--output", default=None, help="salva payload JSON")
    args = parser.parse_args()

    files = []
    if args.dir:
        files = sorted(Path(args.dir).glob("*.md"))
    files += [Path(t) for t in args.targets]
    if not files:
        print("[!] Nenhum handoff informado (targets ou --dir)", file=sys.stderr)
        return 1

    results = [parse_handoff(f) for f in files]
    bad = [r for r in results if not r["ok"]]
    summary = {
        "total": len(results),
        "parsed": len(results) - len(bad),
        "rejeitados": len(bad),
        "handoffs": results,
    }
    out = json.dumps(summary, indent=2, ensure_ascii=False)
    print(out)
    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
