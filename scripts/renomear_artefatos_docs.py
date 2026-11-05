#!/usr/bin/env python3
"""renomear_artefatos_docs.py — Renomeia .md de ./docs/*/* para kebab-case e atualiza referências cruzadas.

Etapa 1: renomeia arquivos (slug do stem em kebab-case), mantendo diretório e extensão.
Etapa 2: atualiza links markdown [texto](caminho.md) e frontmatter derived-from
         que apontem para caminhos antigos.
Etapa 3: gera relatório de auditoria em ./docs/conhecimento/compliance/.

Não altera conteúdo além de caminhos de referência. IDs de artefato (frontmatter id)
não são afetados pela renomeação de arquivo.
"""

import argparse
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("docs")
REPORT_DIR = Path("docs/conhecimento/compliance")
REPORT_PATH = REPORT_DIR / "AUDITORIA-RENOMEACAO-ARTEFACTOS.md"

LINK_RE = re.compile(r"(\]\(?)(\.\/)?([^)\s]+\.md)(\"?\s*\))")
MD_PATH_RE = re.compile(r"docs\/[^)\s\"'<>]+\.md")


def slugify_stem(stem: str) -> str:
    s = stem.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def plan_renames() -> dict[Path, Path]:
    """Retorna {caminho_antigo: caminho_novo} para arquivos que precisam renomear."""
    plano = {}
    for dirpath, dirs, files in os.walk(ROOT):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = Path(dirpath) / fn
            new_stem = slugify_stem(p.stem)
            if new_stem == p.stem:
                continue
            novo = p.with_name(new_stem + ".md")
            plano[p] = novo
    return plano


def aplicar_renomeacao(plano: dict[Path, Path], check_only: bool) -> list[dict]:
    """Renomeia arquivos físicos. Retorna lista de {antigo, novo, ok, erro}."""
    resultados = []
    # Ordena por profundidade decrescente para evitar colisão de diretório pai
    for antigo in sorted(plano, key=lambda p: len(p.parts), reverse=True):
        novo = plano[antigo]
        rel_antigo = str(antigo)
        rel_novo = str(novo)
        entry = {"antigo": rel_antigo, "novo": rel_novo, "ok": False, "erro": None}
        if novo.exists():
            entry["erro"] = "destino ja existe"
            resultados.append(entry)
            continue
        if check_only:
            entry["ok"] = True
            resultados.append(entry)
            continue
        try:
            antigo.rename(novo)
            entry["ok"] = True
        except OSError as exc:
            entry["erro"] = str(exc)
        resultados.append(entry)
    return resultados


def construir_map_caminhos(plano: dict[Path, Path]) -> dict[str, str]:
    """Mapeia caminho relativo antigo (docs/...) -> novo (docs/...)."""
    m = {}
    for antigo, novo in plano.items():
        m[str(antigo)] = str(novo)
    return m


def atualizar_referencias(plano: dict[Path, Path], map_caminhos: dict[str, str], check_only: bool) -> list[dict]:
    """Varre todos os .md (já renomeados) e substitui caminhos antigos por novos."""
    alterados = []
    # Índice por stem antigo -> novo caminho completo (docs/...)
    stem_para_novo = {}
    for antigo, novo in map_caminhos.items():
        stem_para_novo[antigo.stem] = novo

    # Regex para links markdown: [texto](caminho.md) ou [texto](./caminho.md)
    link_md_re = re.compile(r"(\]\(\.?\/)?([^)\s]+\.md)(\"?)")
    # Caminho docs/... em frontmatter derived-from ou texto livre
    docs_path_re = re.compile(r"(docs\/[^)\s\"'<>]+\.md)")

    for dirpath, dirs, files in os.walk(ROOT):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = Path(dirpath) / fn
            texto = p.read_text(encoding="utf-8", errors="replace")
            original = texto

            # Substitui caminhos docs/antigo.md -> docs/novo.md
            def repl_docs(m):
                caminho = m.group(1)
                if caminho in map_caminhos:
                    return map_caminhos[caminho]
                return caminho

            texto = docs_path_re.sub(repl_docs, texto)

            # Substitui links relativos que correspondam a um arquivo renomeado
            def repl_link(m):
                prefixo = m.group(1) or ""
                caminho = m.group(2)
                sufixo = m.group(3) or ""
                # 1) Caminho docs/antigo.md ou relativo que bate direto no mapeamento
                if caminho in map_caminhos:
                    return prefixo + map_caminhos[caminho] + sufixo
                # 2) Resolve relativo ao diretório do arquivo corrente
                base = p.parent.resolve()
                try:
                    candidato = (base / caminho).resolve()
                except Exception:
                    candidato = None
                if candidato:
                    for antigo, novo in map_caminhos.items():
                        if (base / antigo).resolve() == candidato:
                            return prefixo + str(novo) + sufixo
                # 3) Nome puro de arquivo (sem barras) que bate pelo stem antigo
                if "/" not in caminho and "\\" not in caminho:
                    stem = Path(caminho).stem
                    if stem in stem_para_novo:
                        novo = stem_para_novo[stem]
                        return prefixo + str(novo) + sufixo
                return prefixo + caminho + sufixo

            texto = link_md_re.sub(repl_link, texto)

            if texto != original:
                if not check_only:
                    p.write_text(texto, encoding="utf-8")
                alterados.append({"arquivo": str(p), "referencias_atualizadas": True})

    return alterados


def gerar_relatorio(plano, resultados_renome, alterados_refs, total_varridos, check_only, today):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ok = sum(1 for r in resultados_renome if r["ok"])
    erro = sum(1 for r in resultados_renome if not r["ok"])
    lines = []
    lines.append("# Relatório de Auditoria — Renomeação de Artefatos docs/*/*")
    lines.append("")
    lines.append(f"**Gerado em:** {today}")
    lines.append(f"**Modo:** {'check-only (sem gravação)' if check_only else 'aplicado'}")
    lines.append(f"**Total de artefatos .md varridos:** {total_varridos}")
    lines.append(f"**Artefatos renomeados (kebab-case):** {len(plano)}")
    lines.append(f"**Renomeações com sucesso:** {ok}")
    lines.append(f"**Falhas na renomeação:** {erro}")
    lines.append(f"**Arquivos com referências cruzadas atualizadas:** {len(alterados_refs)}")
    lines.append("")
    lines.append("## Padrão de nomenclatura")
    lines.append("- Stem do arquivo em kebab-case (letras minúsculas, hífens, sem espaços)")
    lines.append("- Diretório e extensão `.md` preservados")
    lines.append("- IDs de frontmatter inalterados (não dependem do nome do arquivo)")
    lines.append("")
    lines.append("## Detalhe das renomeações")
    lines.append("")
    lines.append("| Antigo | Novo | Status |")
    lines.append("|---|---|---|")
    for r in resultados_renome:
        status = "OK" if r["ok"] else f"ERRO: {r['erro']}"
        lines.append(f"| {r['antigo']} | {r['novo']} | {status} |")
    lines.append("")
    lines.append("## Arquivos com referências cruzadas atualizadas")
    if alterados_refs:
        for a in alterados_refs:
            lines.append(f"- {a['arquivo']}")
    else:
        lines.append("- Nenhum arquivo precisou de atualização de referência.")
    lines.append("")
    lines.append("## Escopo não coberto")
    lines.append("- Links para arquivos fora de ./docs/ (fora do escopo de renomeação).")
    lines.append("- Arquivos não-Markdown (.docx, .pdf, imagens).")
    lines.append("- Referências a IDs de artefato (inalteradas pela renomeação).")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] {len(plano)} renomeações planejadas, {ok} aplicadas, {erro} falhas.")
    print(f"[OK] {len(alterados_refs)} arquivos com referências cruzadas atualizadas.")
    print(f"[OK] Relatório gravado em {REPORT_PATH}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Renomeia artefatos docs/*/* para kebab-case e atualiza referências")
    parser.add_argument("--check", action="store_true", help="apenas reporta, não grava")
    args = parser.parse_args()

    today = now_iso()
    plano = plan_renames()

    # Conta total de .md varridos
    total_varridos = 0
    for dirpath, dirs, files in os.walk(ROOT):
        for fn in files:
            if fn.endswith(".md"):
                parts = Path(dirpath).relative_to(ROOT).parts
                if len(parts) >= 1:
                    total_varridos += 1

    resultados_renome = aplicar_renomeacao(plano, args.check)

    # Reconstroi plano após renomeação (para check_only, os arquivos ainda têm nomes antigos)
    if args.check:
        map_caminhos = construir_map_caminhos(plano)
    else:
        # Após renomeação física, o plano já foi aplicado; map_caminhos antigo->novo ainda vale
        map_caminhos = construir_map_caminhos(plano)

    alterados_refs = atualizar_referencias(plano, map_caminhos, args.check)

    gerar_relatorio(plano, resultados_renome, alterados_refs, total_varridos, args.check, today)
    return 0


if __name__ == "__main__":
    sys.exit(main())
