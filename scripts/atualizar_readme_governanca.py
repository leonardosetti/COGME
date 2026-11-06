#!/usr/bin/env python3
"""atualizar_readme_governanca.py — Reescreve README.md com versão e governança.

Bump de versão (patch) no frontmatter, atualiza last-revised e injeta/limpa a
seção de falha de pipeline. Stdlib only. Sem dependências novas.

Uso:
  python scripts/atualizar_readme_governanca.py [--falha-pipeline "<msg>"]
  python scripts/atualizar_readme_governanca.py --limpar-falha-pipeline
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
FALHA_MARKER = "<!-- FALHA_PIPELINE -->"


def ler() -> str:
    return README.read_text(encoding="utf-8")


def escrever(conteudo: str) -> None:
    README.write_text(conteudo, encoding="utf-8")


def bump_versao(conteudo: str) -> str:
    """Bump patch da versão no frontmatter (ex.: 1.0.0 -> 1.0.1)."""
    m = re.search(r"^version: (\d+)\.(\d+)\.(\d+)$", conteudo, re.MULTILINE)
    if not m:
        raise SystemExit("versão não encontrada no frontmatter")
    major, minor, patch = int(m.group(1)), int(m.group(2)), int(m.group(3))
    nova = f"{major}.{minor}.{patch + 1}"
    return re.sub(r"^version: \d+\.\d+\.\d+$", f"version: {nova}", conteudo, count=1, flags=re.MULTILINE)


def atualizar_data(conteudo: str) -> str:
    hoje = date.today().isoformat()
    if re.search(r"^last-revised:", conteudo, re.MULTILINE):
        return re.sub(r"^last-revised: .*$", f"last-revised: '{hoje}'", conteudo, count=1, flags=re.MULTILINE)
    return conteudo


def secao_falha(mensagem: str | None) -> str:
    linha_data = date.today().isoformat()
    if mensagem:
        return (
            f"\n{FALHA_MARKER}\n"
            f"## Falha de pipeline (último push)\n\n"
            f"- Data: {linha_data}\n"
            f"- Motivo: {mensagem}\n"
            f"- Ação: sane e republique via `scripts/publicar_pos_push.sh`.\n"
        )
    return ""


def injetar_ou_limpar_falha(conteudo: str, mensagem: str | None, limpar: bool) -> str:
    if limpar:
        # Remove bloco inteiro da seção de falha, se existir.
        padrao = re.compile(
            rf"{re.escape(FALHA_MARKER)}\n## Falha de pipeline \(último push\]\n.*?(?=\n## |\Z)", re.DOTALL
        )
        return padrao.sub("", conteudo).rstrip() + "\n"
    if mensagem is None:
        return conteudo
    # Remove seção antiga, se houver, e insere nova antes do rodapé final.
    conteudo = re.compile(
        rf"{re.escape(FALHA_MARKER)}\n## Falha de pipeline \(último push\].*?(?=\n## |\Z)", re.DOTALL
    ).sub("", conteudo)
    # Remove rodapé final (*...) para inserir seção antes.
    rodape_match = re.search(r"\n---\n\*Documento de caracterização.*\*$", conteudo, re.DOTALL)
    if rodape_match:
        pos = rodape_match.start()
        return conteudo[:pos] + secao_falha(mensagem) + conteudo[pos:]
    return conteudo.rstrip() + secao_falha(mensagem) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Atualiza README com versão e governança.")
    parser.add_argument("--falha-pipeline", metavar="MSG", help="Registra falha de pipeline no README.")
    parser.add_argument("--limpar-falha-pipeline", action="store_true", help="Remove seção de falha do README.")
    args = parser.parse_args()

    conteudo = ler()
    conteudo = bump_versao(conteudo)
    conteudo = atualizar_data(conteudo)
    conteudo = injetar_ou_limpar_falha(conteudo, args.falha_pipeline, args.limpar_falha_pipeline)
    escrever(conteudo)
    print(f"README atualizado (version bump + last-revised).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
