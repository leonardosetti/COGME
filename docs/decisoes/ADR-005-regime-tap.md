# ADR-005 — Regime do TAP: Freeze e Emenda Controlada (Baseline Vivo)

| Campo | Valor |
|---|---|
| Versão | 1.1.0 |
| Status | Ratificado |
| Data da decisão | 18/09/2026 (decisão original) / 31/10/2026 (emenda ADR-LOG-002) |
| Data de formalização do documento | 28/10/2026 (v1.0.0) / 31/10/2026 (v1.1.0 — emenda ADR-LOG-002) |
| Decisor | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Gatilhos G1–G4 | G1 (impacto transversal — todos os 8 planos), G3 (questionabilidade acadêmica), G4 (trade-off não óbvio — imutabilidade × leitura operacional) |
| Rastreabilidade | TAP §6 (precedência intra-TAP) + §3/§9 P9 (status ontológico do TAP); EAP N9.1; REQ-12; NC-00 (Plano de Cronograma §3.8 — locus canônico da decisão); Glossário §11; ADRs correlatas: ADR-001–004 (todas sob o regime de freeze); Integração §1.4 |
| Domínio PMBOK 7ª | Trabalho do Projeto + Incerteza |
| Processo PMBOK 6ª (dicionário) | 4.6 |

## Contexto

O TAP encontra-se congelado desde o início do planejamento (última versão 18/09/2026, anterior aos planos): não é revisado, reversionado ou corrigido ao longo do ciclo, em conformidade com seu status ontológico (Premissa P9; Glossário §11; PMBOK 6ª §4.1 como dicionário). Divergências entre seções do TAP precisavam de locus formal de resolução sem tocar o termo autorizativo. Fonte integral da decisão (texto canônico): Plano de Cronograma §3.8 NC-00 (docs/planos/plano-cronograma.md).

## Decisão

O TAP v3 entra em **Regime de Emenda Controlada**.

1. **Mantido da ADR-005:** Precedência intra-TAP (§6 Marcos é canônico para matéria temporal) e locus de contexto (Notas de Contexto nos planos).

2. **Revogado da ADR-005:** A proibição absoluta de revisão/reversão textual do TAP.

3. **Blindado (Intocável sem Emenda MAJOR):** Objeto, objetivos SMART, justificativa, orçamento-teto (R$ 0,00) e a estrutura macro da EAP (12 fases / 37 pacotes).

## Mecanismo de Emenda (Delta Log)

Qualquer ajuste pontual no TAP deve ser registrado em `docs/tap/delta-v3.1.md` com a seguinte estrutura:

| Campo Alterado | Valor Anterior | Valor Novo | Justificativa (ADR/CR) | Data |
|----------------|----------------|------------|------------------------|------|
| REQ-07 (Cache) | SQLite | PostgreSQL 15+ | Alinhamento à ADR-010 (Stack Infra) | 2026-11-01 |
| Marco M2 (data-alvo) | 30/09/2026 | 15/11/2026 | CR-001 (atraso ~25 dias, risco crítico ao M3) | 2026-10-31 |

## Consequências

- **Ganho:** Flexibilidade documental para corrigir drifts de stack e requisitos sem violar a ontologia do projeto.
- **Risco:** Perda da imutabilidade absoluta do termo autorizativo.
- **Mitigação:** O núcleo do TAP permanece blindado; alterações são auditáveis via Delta Log e exigem aprovação do CCB (GP).

## Ratificação

Ratificado via CCB-LOG-2026-10-31-A08 (Regime de Emenda Controlada) e ratificado via CCB-LOG-2026-10-31-A12 (Emenda de Marco M2). A ADR-005 permanece vigente para todos os aspectos não explicitamente revogados por esta ADR-005 v1.1.0.

---

# Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo | Domínio PMBOK 7ª | Data |
|----------------|----------|--------|------------------|------|
| ADR-013 | Parcial | Regime de Emenda Controlada do TAP — mesclada nesta ADR-005 v1.1.0 | Integração + Incerteza | 01/11/2026 |
| ADR-015 | Parcial | Emenda de Marco M2 (30/09/2026 → 15/11/2026) — emenda de linha de base do TAP registrada no Delta Log | Integração | 31/10/2026 |

## Kill Switch

Se qualquer tentativa de alterar o núcleo blindado do TAP (objeto, objetivos SMART, justificativa, orçamento-teto R$ 0,00, EAP 12/37 pacotes) for feita sem ADR MAJOR e aprovação explícita do CCB (GP), acionar abortamento imediato das operações e escalonamento ao CCB humano.

## Governança

- **Custódia:** agent-architect (ADRs) + agent-pm (Notas de Contexto).
- **Emenda:** qualquer mudança de marco oficial exige change-request + aprovação do CCB + ADR + comunicação ao Prof. Dr. Nivaldo Carleto no marco subsequente (Integração §1.7.3).
- **Auditoria:** project-auditor verifica integridade do TAP congelado a cada milestone.
- **Sucessão:** constituição.md + ADR-005 v1.1.0 + ADR-LOG.md bastam para reconstruir contexto.

---

## Histórico

| Versão | Data | Autor | Mudança |
|--------|------|-------|-----------|
| 1.0.0 | 28/10/2026 | agent-architect | Regularização tardia: formalização do corpo (decisão efetiva 21/09/2026, NC-00); status reflete pendência de ratificação CCB da data 25/09 alegada em memória do GP |
| 1.1.0 | 31/10/2026 | GP Leonardo (CCB) | Emenda ADR-LOG-002: incorpora Regime de Emenda Controlada do TAP (ADR-013) — núcleo blindado, tabela delta em docs/tap/delta-v3.1.md, ADR-013 permanece como artefato histórico |

---

\*Promulgado sob AFA-ULTIMATE v1.3.0-FINAL. A Constituição é lei marcial: aplica-se, não se debate.*