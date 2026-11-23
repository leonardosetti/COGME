#!/usr/bin/env python3
"""
pip_audit_baseline_check.py — Garante que pip-audit NÃO introduza novas vulnerabilidades.

Executa `pip-audit --format json` e compara o conjunto de (pacote, id) encontrado
com a linha de base documentada em docs/seguranca/pip-audit-baseline.json
(vulnerabilidades pre-existentes em dependências transitórias/dev).

Saída 0  : apenas vulnerabilidades da linha de base (ou nenhuma).
Saída 1  : apareceu (pacote, id) fora da linha de base → vulnerabilidade NOVA.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "docs" / "seguranca" / "pip-audit-baseline.json"


def main() -> int:
    if not BASELINE.exists():
        print(f"ERRO: linha de base não encontrada: {BASELINE}", file=sys.stderr)
        return 2

    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    base_pairs = {(e["package"], e["vuln_id"]) for e in base.get("baseline", [])}

    with tempfile.NamedTemporaryFile("w+", suffix=".json", delete=False) as tf:
        report_path = tf.name

    try:
        # pip-audit sai 0 mesmo achando vulnerabilidades; a decisão é nossa.
        subprocess.run(
            ["pip-audit", "--format", "json", "-o", report_path],
            capture_output=True,
            text=True,
        )
        try:
            data = json.loads(Path(report_path).read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"ERRO ao ler relatório pip-audit: {exc}", file=sys.stderr)
            return 2

        ci_pairs = set()
        for dep in data.get("dependencies", []):
            for v in dep.get("vulns", []):
                ci_pairs.add((dep.get("name"), v.get("id")))

        new_pairs = sorted(ci_pairs - base_pairs)
        if new_pairs:
            print("🚨 pip-audit: vulnerabilidades NOVAS detectadas (fora da linha de base):")
            for pkg, vid in new_pairs:
                print(f"  - {pkg} {vid}")
            print(f"\nLinha de base: {len(base_pairs)} pares.")
            print(f"CI encontrou: {len(ci_pairs)} pares.")
            print("Atualize docs/seguranca/pip-audit-baseline.json apenas se a nova")
            print("vulnerabilidade for intencional e aceita.")
            return 1

        print(f"✅ pip-audit: sem vulnerabilidades novas ({len(ci_pairs)} pares na linha de base).")
        return 0
    finally:
        try:
            Path(report_path).unlink(missing_ok=True)
        except Exception:
            pass


if __name__ == "__main__":
    sys.exit(main())
