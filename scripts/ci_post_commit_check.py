#!/usr/bin/env python3
"""ci_post_commit_check.py — Verifica quebras de CI locais após commit.

Executa as mesmas validações do .github/workflows/ci.yml e
.sddai-verify.yml no escopo local. Não bloqueia o commit (post-commit não
pode vetar); apenas avisa quando algo falhou para saneamento antes do push.

Uso: .git/hooks/post-commit chama este script automaticamente.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable

def md_alterados() -> list[str]:
    """Nomes de .md alterados no último commit (espelha o CI)."""
    r = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD", "--", "*.md"],
        cwd=ROOT, text=True, capture_output=True,
    )
    if r.returncode != 0:
        return []
    return [l for l in r.stdout.splitlines() if l]


STEPS_RAW = [
    ("flake8", [PY, "-m", "flake8", "src", "migrations", "tests/unit", "tests/integration"]),
    ("pytest + coverage >=95", [PY, "-m", "pytest", "tests/", "-q", "--tb=short",
                                "--cov=src", "--cov-report=term-missing",
                                "--cov-fail-under=95", "-p", "no:cacheprovider"]),
    ("frontmatter", [PY, "scripts/validar_frontmatter_md.py"]),
    ("nomes de arquivo (.md alterados)", [PY, "scripts/validar_nome_arquivo.py", *md_alterados()] if md_alterados() else None),
    ("SDDAI verify", [PY, "scripts/sddai_verify_pipeline.py", "--strict"]),
    ("security scan", [PY, "scripts/security_scan.py"]),
]

STEPS = [(nome, cmd) for nome, cmd in STEPS_RAW if cmd is not None]


def run(nome: str, cmd: list[str]) -> bool:
    print(f"\n==> {nome}")
    r = subprocess.run(cmd, cwd=ROOT, text=True)
    ok = r.returncode == 0
    print(f"==> {nome}: {'OK' if ok else 'FALHA (rc=' + str(r.returncode) + ')'}")
    return ok


def main() -> int:
    resultados = [run(nome, cmd) for nome, cmd in STEPS]
    print("\n=== RESUMO ===")
    for (nome, _), ok in zip(STEPS, resultados):
        print(f"  {'OK ' if ok else 'FALHA'} {nome}")
    if all(resultados):
        print("Todas as verificações passaram.")
        return 0
    print("Uma ou mais verificações falharam. Sanear antes de pushar para origin/main.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
