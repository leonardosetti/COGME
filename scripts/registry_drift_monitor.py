#!/usr/bin/env python3
"""registry_drift_monitor.py — Detecta drift entre disco, registry e topologia (ONDA 8).

Compara:
  - .opencode/agents/*.md (arquivos presentes)
  - .ai/agents/registry.yaml (roster SSOT)
  - AGENT_TOPOLOGY (validate_nexus_yaml.py — fonte unica)

Reporta:
  - slugs no disco mas nao na topologia (orfãos)
  - slugs na topologia mas ausentes do disco (não forjados)
  - slugs no registry mas ausentes do disco (fantasmas)
  - slugs no disco mas ausentes do registry (não sincronizados)

Exit 1 se drift detectado (modo CI via --strict).
FOSS/stdlib apenas.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_nexus_yaml import AGENTS_DIR, KNOWN_SLUGS
from sync_agent_registry import REGISTRY

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


def disco_slugs() -> set:
    return {f.stem for f in AGENTS_DIR.glob("*.md") if not f.name.startswith(".")}


def registry_slugs() -> set:
    if yaml is None or not REGISTRY.exists():
        return set()
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    return {a.get("name") for a in data.get("agents", []) if a.get("name")}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Monitor de drift do registry COGME")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 se drift detectado (CI)")
    parser.add_argument("--report", default=None, help="salva JSON do report")
    args = parser.parse_args()

    disco = disco_slugs()
    topo = KNOWN_SLUGS
    reg = registry_slugs()

    report = {
        "disco": sorted(disco),
        "topologia": sorted(topo),
        "registry": sorted(reg),
        "drift": {
            "orfao_no_disco_nao_na_topologia": sorted(disco - topo),
            "nao_forjado_na_topologia": sorted(topo - disco),
            "fantasma_no_registry_nao_no_disco": sorted(reg - disco),
            "nao_sincronizado_no_disco_nao_no_registry": sorted(disco - reg),
        },
        "drift_detectado": False,
    }
    d = report["drift"]
    report["drift_detectado"] = any(bool(v) for v in d.values())

    out = json.dumps(report, indent=2, ensure_ascii=False)
    print(out)
    if args.report:
        Path(args.report).write_text(out, encoding="utf-8")

    if report["drift_detectado"]:
        print(f"[DRIFT] drift detectado (ver relatorio)", file=sys.stderr)
        return 1 if args.strict else 0
    print("[DRIFT] sem drift: disco == topologia == registry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
