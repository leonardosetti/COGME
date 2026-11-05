---
id: docs-decisoes-adr-018-nomeclatura-arquivos
title: ADR-018 — Norma de nomenclatura de arquivos de artefato do projeto COGME
type: adr
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-018-nomeclatura-arquivos.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- adequado-a-norma
---
---
id: decisoes-adr-018-nomeclatura-arquivos
title: 'ADR-018 — Norma de nomenclatura de arquivos de artefato do projeto COGME'
version: 1.0.0
status: ratificada
date: 2026-11-05
decisor: GP Leonardo (CCB de membro único). Decisão: ratificada definitivamente em 05/11/2026.
regime: Norma de governança de artefatos; não emenda o TAP nem o núcleo blindado
domain: Governança de artefatos e especificações (PMBOK 7ª: Abordagem de Desenvolvimento; Qualidade)
instrumento-ccb: RAT-2026-11-05-A18
---

# ADR-018 — Norma de nomenclatura de arquivos de artefato do projeto COGME

## Contexto

O projeto COGME produz múltiplos tipos de artefato (specs, testes, auditorias, regras, change-requests, notas, entre outros) em pastas distintas (`.ai/specs/`, `tests/`, `docs/auditorias/`, `docs/decisoes/`, etc.). Cada tipo de artefato usava padrões de nomeação dispersos, sem um padrão único e rastreável. É necessário um padrão de nomenclatura único, aderente ao kebab-case já vigente (Constituição Art. 4.2) e aos prefixos existentes do repo (`HF-NNNN`, `TA-NNNN`, `ADR-NNN`, `VIO-NNN`, `spec-NNN`).

## Decisão

**D1. Padrão de nome de arquivo.** Todo artefato versionado do projeto segue o padrão:

```
tipo_artefato-id_artefato-nome_artefato.{spec,test,audit,rule,change,note,etc,{open,ready,deprecated}}.md
```

Campos:
- `tipo_artefato`: slug em EN, kebab-case, curta (ex.: `spec`, `test`, `audit`, `rule`, `change`, `note`, `etc`). Define a categoria do artefato.
- `id_artefato`: numeral sequencial (ex.: `001`, `004`, `016`). Único dentro do tipo de artefato.
- `nome_artefato`: slug em EN, kebab-case, descritivo do domínio (ex.: `backend-mvp-v1`, `lgpd-produto-proposta`).
- Extensão: `.md` obrigatório. O sufixo entre chaves indica o subtipo quando relevante (ex.: `.spec.md` para specs, `.test.md` para testes, `.audit.md` para auditorias).

**D2. Aplicação às specs existentes.** As specs em `.ai/specs/` já seguem o padrão `spec-NNN-specname.spec.md` (caso particular de D1 com `tipo_artefato=spec`, extensão `.spec.md`). Esse padrão fica ratificado como norma vigente; nenhuma renomeação é necessária.

**D3. Novos artefatos.** Qualquer novo artefato criado no projeto deve seguir D1. A exceção são arquivos imutáveis já referenciados por outros artefatos (ledger, handoffs, ADRs, constituição), que mantêm seus nomes atuais para não quebrar rastreabilidade.

## Alternativas consideradas

| Decisão | Alternativas | Escolha e motivo |
|---------|--------------|------------------|
| Padrão de nome | `id-nome.md`; `nome-id.md`; `tipo-id-nome.md` (D1) | `tipo-id-nome.md` agrupa por tipo no filesystem, facilita `ls` e `grep`, e é coerente com os prefixos existentes do repo. |

## Consequências

Positivas:
- Ordem alfabética agrupa artefatos do mesmo tipo.
- `grep` e `ls` filtram por tipo facilmente.
- Coerente com slugs e identificadores em EN (Constituição P-10).
- Não exige mudança nas specs existentes (D2).

Negativas e riscos:
- Artefatos legados fora do padrão precisam de decisão caso a caso (não são renomeados automaticamente para não quebrar referências `arquivo:linha` em imutáveis).

## Ratificação

Ratificada definitivamente em 05/11/2026 pelo GP Leonardo (CCB de membro único), instrumento RAT-2026-11-05-A18, conforme Constituição Art. 5. As decisões D1–D3 são norma vigente para nomeação de arquivos do projeto.

## Referências

- `constitution.md` (Art. 4.2 — prefixo e slug; P-10 — linguagem)
- `.ai/specs/MANIFEST.md` §2.1 — slug e `spec_id` das specs
