---
id: docs-analise-backlog-req-us-m3-m4
title: Backlog Kanban COGME — conversão REQ → User Story (Gap E.4)
type: relatorio
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/analise/BACKLOG-REQ-US-M3-M4.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- analise
- docs
- adequado-a-norma
---
# Backlog Kanban COGME — conversão REQ → User Story (Gap E.4)

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira  
**Fonte:** spec-002-requisitos-review-round-1.spec.md (US-001..017, REQ-01..15)  
**Marco alvo:** M3 fechado em 03/11/2026 (TA-0039) → backlog publicado a partir de 05/11/2026, direcionado a M4 (17/11/2026)  
**Estado:** backlog publicado como artefato; **não importado como Issues no GitHub** (token PAT sem permissão de escrita — `createIssue` 403).  
**Importação:** o PO (agent-po) ou humano cria as Issues no GitHub web a partir desta lista, aplicando os labels existentes (`feat`, `must`/`should`/`blocked`, `MF2-construcao`/`MF3-consolidacao`, `area:escopo`/`area:qualidade`/`area:integracao`).

---

## Tabela do backlog (cards)

| Card (US) | Slug | REQ | Prioridade | Macro-fase | Status | Trace id | Spec |
|-----------|------|-----|------------|------------|--------|----------|------|
| US-001 | realtime-currency-simulation | REQ-01, REQ-05 | must | MF2-construcao | pronto | REQ-01::US-001 | spec-004 |
| US-002 | five-engagement-regimes | REQ-02 | must | MF2-construcao | pronto | REQ-02::US-002 | spec-004 |
| US-003 | spread-iof-net-calculation | REQ-03 | must | MF2-construcao | pronto | REQ-03::US-003 | spec-004 |
| US-004 | invoice-pdf-generation | REQ-04 | must | MF2-construcao | pronto | REQ-04::US-004 | spec-004, spec-007 |
| US-005 | responsive-foss-web-ui | REQ-06 | must | MF2-construcao | pronto | REQ-06::US-005 | spec-008 |
| US-006 | sqlite-quote-cache | REQ-07 | must | MF2-construcao | pronto | REQ-07::US-006 | spec-004 |
| US-008 | test-coverage-gate | REQ-08 | must | MF2-construcao | pronto | REQ-08::US-008 | spec-011 |
| US-009 | uat-critical-flows | REQ-09 | must | MF2-construcao | pronto | REQ-09::US-009 | spec-009 |
| US-011 | ci-pipeline | REQ-11 | must | MF2-construcao | pronto | REQ-11::US-011 | spec-011 |
| US-015 | foss-license-compliance | REQ-15 | must | MF3-consolidacao | pronto | REQ-15::US-015 | spec-006, spec-011 |
| US-010 | quality-tools-pdca-ishikawa | REQ-10 | should | MF3-consolidacao | pronto | REQ-10::US-010 | spec-010 |
| US-012 | adr-records | REQ-12 | should → blocked | MF3-consolidacao | **blocked** (gate E) | REQ-12::US-012 | — |
| US-013 | sdd-prompt-traceability | REQ-13 | should | MF3-consolidacao | pronto | REQ-13::US-013 | spec-012 |
| US-014 | tech-docs-openapi | REQ-14 | should | MF3-consolidacao | pronto | REQ-14::US-014 | spec-013 |
| US-007 | api-failure-fallback | REQ-07 (corrobora) | conditional | MF2-construcao | conditional (KG-R-02) | — | spec-004 |
| US-016 | invoice-lifecycle-draft-finalize | — (RF-08) | conditional | MF2-construcao | conditional (KG-R-03) | — | spec-007 |
| US-017 | invoice-clone-new-number | — (RF-09) | conditional | MF2-construcao | conditional (depende US-016) | — | spec-007 |

**Totais:** 17 cards | 10 must | 4 should | 3 conditional | 1 blocked

---

## Critério de entrada no Ready (DoR)

Um card entra na coluna `Ready` do Kanban somente quando:
1. Está listado nesta tabela com prioridade e rastreabilidade preenchidas;
2. Não está `blocked` nem `conditional` sem ratificação CCB/PO;
3. Tem critério de aceitação (GWT) definido nesta tabela ou na spec de origem.

---

## Rastreabilidade REQ → US (completa, spec-002 §C.1)

| REQ | US | REQ | US | REQ | US |
|-----|----|-----|----|-----|----|
| REQ-01 | US-001 | REQ-06 | US-005 | REQ-11 | US-011 |
| REQ-02 | US-002 | REQ-07 | US-006, US-007 | REQ-12 | US-012 |
| REQ-03 | US-003 | REQ-08 | US-008 | REQ-13 | US-013 |
| REQ-04 | US-004 | REQ-09 | US-009 | REQ-14 | US-014 |
| REQ-05 | US-001 | REQ-10 | US-010 | REQ-15 | US-015 |

---

## Limitações e riscos

- **Sem write no GitHub:** o PAT não permite criar Issues nem labels. Este documento é o backlog oficial até que o write-token esteja disponível ou a importação seja feita manualmente via GitHub web.
- **M3 já encerrado (03/11/2026):** o backlog não pôde ser publicado "dentro do M3" conforme solicitado; está alinhado a M4 (17/11/2026).
- **Condicionais (US-007, US-016, US-017):** dependem de ratificação CCB/PO (KG-R-02/KG-R-03). Não entram no Ready até decisão humana.
- **Bloqueada (US-012):** depende de re-emissão ADR-001..006 (gate E).

---

## Como usar (PO / agent-po)

1. Abrir o GitHub web do repo `leonardosetti/COGME`, aba Issues.
2. Criar uma Issue por card acima, com título `US-NNN — <slug>` e corpo copiado da respectiva linha/trace.
3. Aplicar labels existentes: `feat`, prioridade (`must`/`should`/`blocked`), macro-fase (`MF2-construcao`/`MF3-consolidacao`), `area:*` quando couber.
4. Colocar na coluna `Backlog` do Kanban (GitHub Projects) — mover para `Ready` após DoR.
