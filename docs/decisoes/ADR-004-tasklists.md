# ADR-004 — Controle de Progresso via Tasklists Markdown (Rejeição de Subissues)

| Campo | Valor |
|---|---|
| Versão | 1.0.0 |
| Status | Finalizado |
| Data da decisão | 20/09/2026 |
| Data de formalização do documento | 28/10/2026 |
| Decisor | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Gatilhos G1–G4 | G3 (questionabilidade acadêmica — "por que não usaram subissues?"), G4 (trade-off não óbvio — granularidade × simplicidade) |
| Rastreabilidade | TAP §1.c (Governança Híbrida); EAP N9.1; REQ-12; ADRs correlatas: ADR-002 (Kanban), ADR-003 (métricas); ADR-005 (freeze); integração normativa: Plano de Escopo §2.6 (DoD item 8), Integração §1.3.2 |
| Domínio PMBOK 7ª | Abordagem de Desenvolvimento + Medição + Trabalho do Projeto |

## Contexto

Cards complexos (estimativa ≥ 6h ou múltiplos entregáveis) exigem decomposição visual do progresso interno para evitar a opacidade de cards estagnados em `In Progress` por múltiplos dias. A equipe avaliou mecanismos para prover granularidade sem violar o fluxo Kanban (ADR-002).

## Decisão

Adotar **Tasklists Markdown condicionais** (`- [ ]` no corpo da Issue) e **rejeitar formalmente subissues reais** (issues filhas).

**Regras de aplicação:**

- **Obrigatórias** para cards com estimativa ≥ 6h ou múltiplos entregáveis.
- **Proibidas** para cards atômicos (≤ 4h) ou em status `Code Review`/`Done`.
- **Formato canônico:** mínimo 3 itens, máximo 7 itens; último item obrigatoriamente "Validação final".
- **Natureza binária:** itens são "feito/não feito", sem status intermediário.

**Impacto nas métricas (ADR-003):** Cycle Time e Throughput medem exclusivamente o **card pai**; WIP Limit conta o card pai (limite 3/pessoa, ADR-002); CFD ignora o progresso interno da tasklist (evita distorção de bandas).

**Adendo normativo:** a seção §2.6 do Plano de Escopo incorporou o item 8 ao DoD — se o card possuir tasklist Markdown, 100% dos itens marcados `- [x]` (gate de qualidade em efeito).

## Alternativas Consideradas

- Sem decomposição — descartado: opacidade de cards estagnados.
- Subissues reais (issues filhas) — **rejeitado formalmente**: fragmenta o backlog no GitHub Projects e distorce a unidade atômica de métrica.
- Grafos de tarefas/status intermediários — descartado: overhead sem valor para MVP (GMV).

## Consequências e Trade-offs

- ✅ Positivas: zero overhead de gestão; visibilidade nativa no GitHub (barra de progresso da tasklist); não fragmenta o backlog.
- ⚠️ Riscos: requer disciplina do responsável para manter a tasklist atualizada durante a execução.
- 🔄 Fallback: se insuficiente para cards de código (M2/M3), reavaliar na Retrospectiva da MF2.
- Trade-offs aceitos: simplicidade (GMV) > granularidade de status de sub-tarefas; unidade atômica de métrica (card pai) > rastreabilidade fina de sub-passos. Valor Ágil: "Indivíduos e interações sobre processos e ferramentas."

## Governança

- Registrou-se como ADR tardia exemplar da política OKB (Aditivo §2): decisão já operacionalizada quando formalizada — casos futuros seguem a matriz §2.3.
- Emenda: mudança nos limites do formato (3–7 itens) pelo GP com registro em commit se afetar apenas 1 plano; ADR se transversal.
- kill_switch: screened.

## Histórico

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 28/10/2026 | agent-architect | Formalização do corpo (decisão CCB de 20/09/2026; emissão original comprometida em commit de 0 byte — 21/09/2026; stub antigo dizia "Hierarchical task lists with priority tags" — substituído pela decisão aprovada de tasklists Markdown nativas) |
