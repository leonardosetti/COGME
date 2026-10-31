---
id: ADR-013
title: Regime de Emenda Controlada do TAP (Baseline Vivo)
version: 1.0.0
status: ratified
date: 2026-11-01
decisor: GP Leonardo (CCB único)
supersedes: ADR-005 (parcialmente)
domain: Integração + Incerteza (PMBOK 7ª)
---

## Contexto

A ADR-005 estabeleceu o freeze absoluto do TAP v3 (18/09/2026). Contudo, a natureza viva do projeto e a necessidade de alinhar requisitos (ex.: REQ-07 de SQLite para PostgreSQL, conforme ADR-010) exigem um mecanismo de ajuste pontual sem descaracterizar o núcleo autorizativo do projeto.

## Decisão

O TAP v3 entra em **Regime de Emenda Controlada**.

1. **Mantido da ADR-005:** Precedência intra-TAP (§6 Marcos é canônico para matéria temporal) e locus de contexto (Notas de Contexto nos planos).
2. **Revogado da ADR-005:** A proibição absoluta de revisão/reversão textual do TAP.
3. **Blindado (Intocável sem Emenda MAJOR):** Objeto, objetivos SMART, justificativa, orçamento-teto (R$ 0,00) e a estrutura macro da EAP (12 fases / 37 pacotes).

## Mecanismo de Emenda (Delta Log)

Qualquer ajuste pontual no TAP deve ser registrado em `docs/tap/delta-v3.1.md` com a seguinte estrutura:

| Campo Alterado | Valor Anterior | Valor Novo | Justificativa (ADR/CR) | Data |
|---|---|---|---|---|
| REQ-07 (Cache) | SQLite | PostgreSQL 15+ | Alinhamento à ADR-010 (Stack Infra) | 2026-11-01 |

## Consequências

- **Ganho:** Flexibilidade documental para corrigir drifts de stack e requisitos sem violar a ontologia do projeto.
- **Risco:** Perda da imutabilidade absoluta do termo autorizativo.
- **Mitigação:** O núcleo do TAP permanece blindado; alterações são auditáveis via Delta Log e exigem aprovação do CCB (GP).

## Ratificação

Ratificado via CCB-LOG-2026-11-01-A08. A ADR-005 permanece vigente para todos os aspectos não explicitamente revogados por esta ADR-013.
