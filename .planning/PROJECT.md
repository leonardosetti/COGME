---
id: cogme-project
title: COGME — Projeto
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .planning/PROJECT.md
last-revised: '2026-11-22'
lgpd-class: n/a
tags:
- planejamento
- projeto
---

# COGME

## What This Is

Sistema entregável v1 — plataforma multiempresa com ciclo de vida do usuário, dashboard, fluxo anônimo, faturamento (invoices), simulações, provedores e taxas. Interface ifit.com (templates Jinja2 + CSS design system + JS consolidado). Backend em Python (FastAPI/Flask-like rotas `/v1/*`), frontend estático, banco com migrações Alembic.

## Core Value

Entregar o sistema completo v1 com specs/integridade (SSOT camada 5) ratificadas via Gate G2, mantendo 100% dos itens que bloqueiam produção e sem alterar imutáveis (constitution, ADRs, ledger, .opencode).

## Business Context

- **Customer**: multiempresa (clientes internacionais e locais)
- **Revenue model**: simulações, faturamento, taxas e provedores
- **Success metric**: suíte verde (1294 testes), pipeline de compliance verde, sync_agent_registry exit 0, nexus_dispatcher JSON válido

## Requirements

### Validated

- ✓ Fase 1: saneamento de compliance (VIO-019..032 fechados, exceto VIO-026 por decisão CCB)
- ✓ Fase 2: pré-produção CR-009 (15 BLOQ + 12 ALTO, aprovado por CCB 2026-11-22)

### Active

- [ ] TA-061: Emendas spec-004/005 (SS11, SS13, job contract-network, destino evidências UAT, bump + CHANGELOG)
- [ ] TA-062: Auditoria integridade specs 017–022
- [ ] TA-063: Repovoar tap.md (TAP v3, rastreabilidade arquivo:linha)
- [ ] TA-064: Repovoar eap.md (fases N1..N11)
- [ ] TA-065: Repovoar requisitos.md (RF/RNF/US REQ-01..15, rastreabilidade 15/15)

### Out of Scope

- VIO-026 (auto-delegação TA-0028) — decisão Humana/CCB, não reabrir
- Reescrever arquivos imutáveis (constitution, ADRs, ledger pré-existente, .opencode)
- Promover requisitos a "aprovado" nesta fase
- Gate G2 (ratificação specs 024/025/026) — depende desta fase, entra na próxima

## Context

- Branch `main`, working tree limpo, todos commits pushados para origin/main
- Suíte: 1294 passed / 0 failed / 6 skipped; cobertura 72% (hook pré-push 70%)
- Pipeline Auditoria de Compliance: verde
- `sync_agent_registry.py --check`: exit 0; `nexus_dispatcher.py --report`: JSON válido
- Completude sistema: 86.2% (100% nos itens que bloqueiam produção)
- Especs 017–022 já implementadas; falta camada canônica + rastreabilidade SDD
- Referências: `.ai/specs/MANIFEST.md`, `constitution.md` (Art. 2, 4, 6), `docs/planos/plano-integral-tap-1-2-3-4-5.md`, ADR-005/ADR-013

## Constraints

- **Imutáveis**: não alterar constitution, ADRs, ledger pré-existente, .opencode
- **Versão**: bump spec-004 1.0.0→1.1.0, spec-005 0.2.0→0.3.0 + CHANGELOG
- **Kill switch**: `kill_switch: inherited` em frontmatter de tap.md/eap.md/requisitos.md
- **Status**: docs em `status: draft`, não promover a "aprovado"

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Fase 1.5 = specs/integridade (TA-061 a TA-065) | Handoff da Fase 2 (CCB aprovado 2026-11-22) | — |
| Não rodar `gsd-new-milestone` (fases.clear) | Evitar arquivar/destruir phases 1, 2, 1_5 existentes | PLANs preservados |

---
*Last updated: 2026-11-22 after creating phase 1.5 plan*
