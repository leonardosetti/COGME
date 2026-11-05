---
id: norma-nomeclarte-artefatos
title: Norma de Nomenclatura para Artefatos Markdown
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
  - constitution.md (Art. 2, Art. 3 P-05, Art. 9)
  - docs/normas/NORMA-TEMPLATES-ARTEFATOS.md
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
  - norma
  - nomeclatura
  - arquivo
  - governanca
---

# Norma de Nomenclatura para Artefatos *.md

## 1. Objetivo

Padronizar nomes de arquivos `*.md` para rastreamento, índice, controle de storage, governança e compliance. Todo novo artefato `.md` deve seguir este padrão. O estoque existente não é renomeado automaticamente (risco de quebrar links internos e scripts); novos arquivos são barrados pelo CI se estiverem fora do padrão.

## 2. Padrão de nomeação

Formato: `{prefixo}-{slug}.md`

- `prefixo`: minúsculo, coerente com o diretório (Tabela 1).
- `slug`: `kebab-case` (letras minúsculas, dígitos, hífens), descritivo do conteúdo.
- Extensão: `.md` (minúscula).
- Não usar espaços, maiúsculas, caracteres especiais ou underscores no nome do arquivo.

Exemplos válidos:
- `docs/decisoes/adr-013-regime-emenda-tap.md`
- `docs/change-requests/cr-001-m2-replanejamento.md`
- `docs/auditorias/aud-2610-03.md`
- `.ai/handoffs/hf-0010-consulta-dominio.md`
- `.ai/specs/spec-004-backend-mvp-v1.md`

## 3. Tabela 1 — prefixo por diretório

| Diretório | Prefixo | Tipo de artefato |
|-----------|---------|------------------|
| `docs/decisoes/` | `adr` | ADR |
| `docs/change-requests/` | `cr` | Change-Request |
| `docs/auditorias/` | `aud` | Audit |
| `docs/especificacoes/` | `spec` | Spec |
| `docs/planos/` | `plan` | Plano |
| `docs/operacao/` | `proc` | Procedimento |
| `docs/relatorios/` | `rel` | Relatório |
| `docs/evidencias/` | `evid` | Evidência |
| `docs/metricas/` | `met` | Métrica |
| `docs/requisitos/` | `req` | Requisito |
| `docs/governanca/` | `gov` | Governança |
| `docs/conhecimento/` | `kb` | Conhecimento |
| `docs/archive/` | `arc` | Arquivo |
| `docs/analise/` | `ana` | Análise |
| `docs/uat/` | `uat` | UAT/Teste |
| `docs/tap/` | `tap` | TAP |
| `docs/verification/` | `ver` | Verificação |
| `.ai/handoffs/` | `hf` | Handoff |
| `.ai/specs/` | `spec` | Spec |
| `.ai/personas/` | `pers` | Persona |
| raiz (`constitution.md`) | `const` | Constituição (mantém `constitution.md`) |
| raiz (`README.md`, `AGENTS.md`) | — | README (mantém nome canônico) |

## 4. Estoque existente

Arquivos já versionados não são renomeados por esta norma (evita quebrar links internos e scripts com caminhos fixos). Novos arquivos devem seguir o padrão. Para renomear estoque futuro, usar script de renomeação com symlink de redirect do nome antigo para o novo.

## 5. Gate de validação

O script `scripts/validar_nome_arquivo.py` verifica:
- Nome em `kebab-case` (regex `^[a-z0-9]+(-[a-z0-9]+)*\.md$`).
- Prefixo coerente com o diretório (Tabela 1).
- Não há espaços, maiúsculas, underscores ou caracteres especiais.

O CI roda o script no job `lint`. Novo `.md` fora do padrão bloqueia o pipeline.

## 6. Índice de artefatos

O índice é derivado do frontmatter `id` de cada `.md` (norma de templates). Não depende do nome do arquivo. O frontmatter `id` é o identificador estável para rastreamento; o nome do arquivo é apenas convenção legível por humanos.

---