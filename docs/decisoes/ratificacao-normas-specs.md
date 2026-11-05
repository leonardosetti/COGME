---
id: decisoes-ratificacao-normas-specs
title: 'Ratificação e Promulgação de Normas de Especificação — Template, Nomenclatura e Campo Wave'
version: 1.0.0
status: ratificada
date: 2026-11-05
decisor: GP Leonardo (CCB de membro único). Decisão: ratificada e promulgada definitivamente em 05/11/2026.
regime: Norma de governança de artefatos; não emenda o TAP nem o núcleo blindado
domain: Governança de especificações e artefatos (PMBOK 7ª: Abordagem de Desenvolvimento; Qualidade)
instrumento-ccb: RAT-2026-11-05-A16 / RAT-2026-11-05-A16-D4 / RAT-2026-11-05-A18
---

# Ratificação e Promulgação de Normas de Especificação

## Normas ratificadas

| Norma | Fonte | Instrumento CCB | Status |
|-------|-------|-----------------|--------|
| Template canônico de specs (frontmatter camada a, camadas b–h) | `.ai/specs/MANIFEST.md` §1.1–1.2 | RAT-2026-11-05-A16 (ADR-016) | Ratificada |
| Norma de nomenclatura de arquivos | `docs/decisoes/adr-018-nomeclatura-arquivos.md` (ADR-018) | RAT-2026-11-05-A18 | Ratificada |
| Campo `wave` opcional no frontmatter | `.ai/specs/MANIFEST.md` §1.1 | RAT-2026-11-05-A16 | Ratificada |

## Detalhe por norma

### 1. Template canônico de specs (MANIFEST.md §1.1–1.2)

O frontmatter canônico (camada a) exige os campos: `spec_id`, `specname`, `version`, `status`, `custody`, `created`/`updated`, `origin`, `task`/`sender`, `kill_switch`, `trace`, `lgpd-class` (opcional) e `wave` (opcional). O corpo segue as camadas (b)–(h): contexto/origem, resolução de conflitos, corpo de decisões/requisitos/contratos, critérios de aceite/testes, rastreabilidade, fora de escopo (YAGNI), changelog. Todas as 16 specs existentes em `.ai/specs/` foram verificadas; as specs 001–003 foram ajustadas para aderência (commit `a3094dc`).

### 2. Norma de nomenclatura de arquivos (ADR-018)

Padrão: `tipo_artefato-id_artefato-nome_artefato.{spec,test,audit,rule,change,note,etc,{open,ready,deprecated}}.md`. As specs existentes já seguem o caso particular `spec-NNN-specname.spec.md`. Nenhuma renomeação é necessária.

### 3. Campo `wave` opcional (MANIFEST.md §1.1)

Campo `wave` adicionado como opcional no frontmatter (ex.: `WS-1`, `WS-3`), útil para rastreabilidade de rodadas de emissão. Já usado em spec-001 e spec-002.

## Validade

A partir de 05/11/2026, estas normas são vigentes para todo novo artefato de especificação e arquivo do projeto COGME. Nada aqui contraria a Constituição nem o TAP congelado (Art. 2.1, hierarquia de cima para baixo).

## Assinatura

| Versão | SHA-256 do conteúdo normativo | Commit Git | Data | Papel do ratificador humano | Instrumento |
|--------|------------------------------|------------|------|----------------------------|-------------|
| 1.0.0 | pendente | pendente | 05/11/2026 | Gerente de Projeto — CCB de membro único | RAT-2026-11-05-A16 / A18 |

*Promulgado sob AFA-ULTIMATE v1.3.0-FINAL. Constituição é lei marcial: aplica-se, não se debate.*
