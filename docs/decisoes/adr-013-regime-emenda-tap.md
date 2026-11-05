---
id: docs-decisoes-adr-013-regime-emenda-tap
title: ADR-013 — Regime de Emenda Controlada do TAP (Baseline Vivo) — SUPERSSEDIDA
type: adr
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-013-regime-emenda-tap.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- normalizado
- self-updated
- supersedida
---
**Esta ADR está SUPERSSEDIDA.** Foi incorporada integralmente na **ADR-005 v1.1.0** (Regime do TAP: Freeze + Emenda Controlada) conforme decisão do GP em 31/10/2026 (RAT-2026-10-31-A12). Não deve ser usada como referência normativa vigente. Consulte `docs/decisoes/adr-005-regime-tap.md` (versão 1.1.0) para o conteúdo vigente.

---

## Contexto

A ADR-005 estabeleceu o freeze absoluto do TAP v3 (18/09/2026). Contudo, a natureza viva do projeto e a necessidade de alinhar requisitos (ex.: REQ-07 de SQLite para PostgreSQL, conforme ADR-010) exigem um mecanismo de ajuste pontual sem descaracterizar o núcleo autorizativo do projeto.

## Decisão

O TAP v3 entra em **Regime de Emenda Controlada**.

1. **Mantido da ADR-005:** Precedência intra-TAP (§6 Marcos é canônico para matéria temporal) e locus de contexto (Notas de Contexto nos planos).
2. **Revogado da ADR-005:** A proibição absoluta de revisão/reversão textual do TAP.
3. **Blindado (Intocável sem Emenda MAJOR):** Objeto, objetivos SMART, justificativa, orçamento-teto (R$ 0,00) e a estrutura macro da EAP (12 fases / 37 pacotes).

## Mecanismo de Emenda (Delta Log)

Qualquer ajuste pontual no TAP deve ser registrado em `docs/tap/delta-v3-1.md` com a seguinte estrutura:

| Campo Alterado | Valor Anterior | Valor Novo | Justificativa (ADR/CR) | Data |
|---|---|---|---|---|
| REQ-07 (Cache) | SQLite | PostgreSQL 15+ | Alinhamento à ADR-010 (Stack Infra) | 2026-11-01 |

## Consequências

- **Ganho:** Flexibilidade documental para corrigir drifts de stack e requisitos sem violar a ontologia do projeto.
- **Risco:** Perda da imutabilidade absoluta do termo autorizativo.
- **Mitigação:** O núcleo do TAP permanece blindado; alterações são auditáveis via Delta Log e exigem aprovação do CCB (GP).

## Ratificação

Ratificado via CCB-LOG-2026-11-01-A08. A ADR-005 permanece vigente para todos os aspectos não explicitamente revogados por esta ADR-013.
