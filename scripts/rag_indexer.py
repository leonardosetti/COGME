#!/usr/bin/env python3
"""rag_indexer.py — Indexador preparatorio para futuro pipeline RAG (ONDA 8, stub).

Prepara metadados e chunks de documentos do projeto (.ai/specs/, constitution.md,
ADRs, planos) para indexacao futura em um indexador RAG local (ex.: llama.cpp +
embeddings CPU). Nao executa embeddings nem rede; apenas estrutura o corpus.

Princípios SDD: especificacao antes de implementacao. Este script define o
contrato de indexacao (fonte -> chunk -> metadados) para implementacao posterior.
FOSS/stdlib apenas. Zero custo recorrente. Dados permanecem locais (LGPD P-03).
"""
import argparse
import json
import sys
from pathlib import Path

CORPUS_DIRS = [Path("docs"), Path(".ai/specs"), Path("constitution.md"),
               Path("docs/decisoes"), Path("docs/planos")]


def list_corpus() -> list:
    entries = []
    for base in CORPUS_DIRS:
        if base.is_file():
            entries.append({"source": str(base), "type": "file"})
        elif base.is_dir():
            for f in sorted(base.rglob("*")):
                if f.is_file() and f.suffix in {".md", ".yaml", ".yml", ".json", ".py", ".txt"}:
                    entries.append({"source": str(f), "type": "file"})
    return entries


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Indexador preparatorio RAG COGME (stub)")
    parser.add_argument("--list-corpus", action="store_true",
                        help="lista arquivos do corpus candidatos a indexacao")
    parser.add_argument("--report", default=None, help="salva JSON do report")
    args = parser.parse_args()

    corpus = list_corpus()
    report = {
        "rag_indexer_version": "0.1.0-stub",
        "corpus_count": len(corpus),
        "corpus_dirs": [str(d) for d in CORPUS_DIRS],
        "note": "stub: estrutura apenas; indexacao/embeddings a implementar localmente",
        "entries": corpus,
    }
    out = json.dumps(report, indent=2, ensure_ascii=False)
    print(out)
    if args.report:
        Path(args.report).write_text(out, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
