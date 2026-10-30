# ADR-002 — Kanban como Método de Execução

| Campo | Valor |
|---|---|
| Versão | 1.0.0 |
| Status | Finalizado |
| Data da decisão | 19/09/2026 |
| Data de formalização do documento | 28/10/2026 |
| Decisor | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Gatilhos G1–G4 | G1 (impacto transversal — todos os planos e o SSOT), G3 (questionabilidade acadêmica — "por que sem sprints?"), G4 (trade-off não óbvio — abre mão de iterações time-boxed) |
| Rastreabilidade | TAP §1.c (Governança Híbrida) + §3 (Métricas) + §10 (R3 burnout); EAP N1.5, N7 (fila N9.1); REQ-12; ADRs correlatas: ADR-003 (métricas), ADR-004 (tasklists), ADR-005 (freeze) |
| Domínio PMBOK 7ª | Abordagem de Desenvolvimento + Equipe + Trabalho do Projeto |

## Contexto

O TAP declara Kanban como método de execução (Premissa P1), mas o glossário v2.1 mencionava "Sprint" e "Sprint Planning", incompatível com fluxo contínuo. É necessário operacionalizar o método de forma consistente com o SSOT (GitHub Projects) e a equipe de 3 pessoas.

## Decisão

- **Ferramenta:** GitHub Projects (SSOT).
- **Colunas do fluxo:** `Backlog` → `Ready (DoR)` → `In Progress` → `Code Review` → `Done (DoD)`.
- **WIP Limits:** 3 cards em `In Progress` por pessoa (Domínio de Equipe PMBOK 7ª — prevenção de burnout, TAP §10 R3).
- **Pull system:** trabalho puxado por capacidade, não empurrado por cronograma rígido.
- **Rituais:** Daily assíncrona (GitHub Issues, 15min/dia); Refinement semanal (30min); Retrospectiva quinzenal (risk backlog + lições aprendidas).
- **Sprints:** NÃO utilizadas — fluxo contínuo (TAP §3 "Métricas").

Mapeamento Domínios PMBOK 7ª → rituais: Stakeholders → Refinement semanal; Equipe → Daily + WIP limits; Abordagem de Desenvolvimento → fluxo contínuo (CFD); Trabalho do Projeto → pull system; Entrega → DoD + Code Review; Medição → Cycle Time + Throughput (GitHub Insights); Incerteza → Retrospectiva + risk backlog.

## Alternativas Consideradas

- Jira — descartado: integração nativa ausente ao SSOT GitHub (GitHub Projects vence por integração nativa e custo zero).
- Trello — descartado: mesmo motivo (integração ao repositório e metrics nativas inferiores).
- Sprints/time-boxing — descartado: inadequado à equipe de 3 pessoas e ao fluxo contínuo declarado no TAP.

## Consequências e Trade-offs

- ✅ Positivas: flexibilidade, visibilidade total, métricas de fluxo nativas (GitHub Insights).
- ⚠️ Riscos: exige disciplina de WIP limits; risco de cards parados em `Code Review`.
- 🔄 Fallback: throughput < 3 cards/semana por 2 semanas consecutivas → revisar WIP limits.
- Trade-offs aceitos: fluxo contínuo > iterações time-boxed; GitHub Projects > Jira/Trello (integração nativa ao SSOT, custo zero).

## Governança

- Custódia: agent-pm (operação) + agent-architect (o fluxo é referência para métricas ADR-003 e tasklists ADR-004).
- Emenda: mudança de colunas/limites do fluxo afeta ≥ 2 planos (G1) → change-request + CCB + ADR de emenda.
- kill_switch: screened.

## Histórico

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 28/10/2026 | agent-architect | Formalização do corpo (decisão CCB de 19/09/2026; emissão original comprometida em commit de 0 byte — 21/09/2026; stub antigo dizia "Custom workflow engine" — substituído pela decisão aprovada) |
