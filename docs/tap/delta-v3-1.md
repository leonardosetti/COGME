---
id: tap-delta-v3-1
title: TAP v3.1 — Delta Log (Regime de Emenda Controlada ADR-013-a)
version: '3.1'
class: termo-abertura
status: active
owner: agent-project-analyst
derived-from:
- docs/tap/delta-v3-1.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- tap
- docs
- normalizado
---
# TAP v3.1 — Delta Log (Regime de Emenda Controlada ADR-013-a)

> **Regra:** append-only. Toda emenda pontual do TAP v3 (baseline congelado 18/09/2026) registra-se aqui. Núcleo blindado (objeto, objetivos SMART, orçamento-teto R$0,00, EAP 12/37, §6 Marcos como texto) não é alterado textualmente — leitura operacional vive nas Notas de Contexto (NC-XX) dos planos.

## Emendas Registradas

| Campo Alterado | Valor Anterior | Valor Novo | Justificativa (ADR/CR) | Data |
|---|---|---|---|---|
| REQ-07 — Cache de cotações | SQLite | PostgreSQL 15+ | ADR-010 (Stack Infra) | 2026-11-01 |
| Marco M2 — data-alvo (TAP §6, leitura operacional) | 30/09/2026 | 15/11/2026 | CR-001 + ADR-015 (repactuação ~25 dias; risco crítico ao M3) | 2026-10-31 |

---

**Histórico de versões deste Delta Log:**
- v1.0 — 31/10/2026 — criação inicial (ADR-015); inclui emenda REQ-07 de 29/10 (ADR-010) retroativamente para trilha auditável completa.

*Governado por ADR-013 (Regime de Emenda Controlada) + NC-00/NC-07 do Plano de Cronograma. CCB: GP Leonardo (único).*