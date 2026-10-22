#!/usr/bin/env python3
"""sync_agent_registry.py — Sincroniza o SSOT de roster (FASE S.5).

Lê frontmatter dos .md em .opencode/agents/ (reutilizando o parser de
validate_nexus_yaml — SSOT única, eliminação de redundância) e regenera
a lista `agents` de .ai/agents/registry.yaml, preservando os blocos
`registry`, `deprecated` e `interim_fallback` existentes.

Modos:
  sync       (default) reescreve agents no registry
  --check    valida drift entre disco e registry; exit 1 se divergir (cível para CI)
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_nexus_yaml import AGENTS_DIR, parse_frontmatter, validate_agent, LEGACY_SLUG_RE

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

REGISTRY = Path(".ai/agents/registry.yaml")


def scan_agents() -> list:
    """Extrai entries de .opencode/agents/*.md (não-archive)."""
    entries = []
    for f in sorted(AGENTS_DIR.glob("*.md")):
        contract, _fm_err = parse_frontmatter(f)
        check = validate_agent(f)  # fail-closed: rejeitado nunca entra no roster
        if not check["ok"]:
            entries.append({
                "file": f".opencode/agents/{f.name}", "name": None,
                "status": "rejeitado", "errors": check["errors"],
            })
            continue
        if contract is None and LEGACY_SLUG_RE.search(f.name):
            entry = {
                "file": f".opencode/agents/{f.name}",
                "name": f.stem if f.stem.startswith("agent-") else f"agent-{f.stem}",
                "version": None, "layer": "META",
                "role": "forge", "description": None,
                "status": "legacy-forge",
                "upstream": [], "downstream": [],
            }
        else:
            entry = {
                "file": f".opencode/agents/{f.name}",
                "name": contract.get("name") or check["slug"],
                "version": str(contract.get("version") or ""),
                "layer": contract.get("layer"),
                "role": contract.get("role"),
                "description": contract.get("description"),
                "status": "promulgado",
                "upstream": list(contract.get("upstream") or []),
                "downstream": list(contract.get("downstream") or []),
            }
        entries.append(entry)
    return entries


def build_model() -> dict:
    model = {"registry": {"version": "1.0", "project": "COGME",
                          "slug_rule": "kebab-case com prefixo agent- (constitution.md Art. 4)"},
            "agents": scan_agents()}
    if REGISTRY.exists():
        existing = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
        for key in ("registry", "deprecated", "interim_fallback"):
            if key in existing:
                model.setdefault(key, existing[key])
    return model


def canonicalize(entries: list) -> list:
    clean = []
    for e in entries:
        if e.get("errors"):
            e = {k: e[k] for k in ("file", "name", "status", "errors") if k in e}
        clean.append(e)
    return sorted(clean, key=lambda x: str(x.get("name") or x.get("file")))


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync/verificação do roster SSOT")
    parser.add_argument("--check", action="store_true",
                        help="exit 1 se registry divergir do disco")
    args = parser.parse_args()

    model = build_model()
    model["agents"] = canonicalize(model["agents"])

    if args.check:
        if not REGISTRY.exists():
            print("[DRIFT] registry ausente", file=sys.stderr)
            return 1
        current = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
        if current.get("agents") != model["agents"]:
            disk = {a.get("name") or a.get("file") for a in current.get("agents", [])}
            live = {a.get("name") or a.get("file") for a in model["agents"]}
            print(json.dumps({
                "drift": True,
                "apenas_no_registry": sorted(disk - live),
                "apenas_no_disco": sorted(live - disk),
            }, indent=2, ensure_ascii=False))
            return 1
        print('[OK] registry em sincronia com o disco')
        return 0

    out = "# SSOT DO ROSTER COGME — NÃO EDITAR MANUALMENTE\n" \
          "# Sincronizado por: python3 scripts/sync_agent_registry.py\n" \
          "# Validação de contratos: scripts/validate_nexus_yaml.py\n" \
          "# Governa: constitution.md Art. 4\n\n" + \
        yaml.safe_dump(model, sort_keys=False, allow_unicode=True, width=100)
    REGISTRY.write_text(out, encoding="utf-8")

    summary = {
        "registry": str(REGISTRY),
        "agentes": len([a for a in model["agents"] if not a.get("errors")]),
        "rejeitados": len([a for a in model["agents"] if a.get("errors")]),
        "legacy_forge": len([a for a in model["agents"]
                             if a.get("status") == "legacy-forge"]),
    }
    print(f"[SYNC] {summary}")
    return 1 if summary["rejeitados"] else 0


if __name__ == "__main__":
    sys.exit(main())
