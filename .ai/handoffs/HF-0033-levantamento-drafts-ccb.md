---
id: ai-handoffs-hf-0033-levantamento-drafts-ccb
title: 'Handoff: Levantamento de artefatos com status draft para aprovação CCB (TA-0033)'
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
agent: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0033-levantamento-drafts-ccb.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
created: 2026-11-05
updated: 2026-11-06
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---
# Handoff: Levantamento de artefatos com status draft para aprovação CCB (TA-0033)

## Contexto

Rodada garantidora do GP/Humano (2026-11-02, Art. 5.1): levantar TODOS os artefatos do
projeto com status `draft` (ou equivalente de pendência de aprovação) para submissão à CCB
(Humano, Art. 5.1 — você recomenda, o Humano decide; nenhuma decisão sua é veredicto).

## Tarefa

1. **Varredura exaustiva** (grep + leitura de frontmatter/Status) por status draft/pending em:
   `.ai/specs/*.md` (frontmatter `status` e linha `Status:` — ex.: "PENDENTE DE REVISÃO"),
   `.ai/handoffs/*.md` (enum do `handoff_parser.py`: draft|ready|dispatched|in_progress|done|blocked),
   `.ai/agents/*.yaml|yml` (ex.: `universal-adjustment-session.yaml`), `docs/decisoes/*`
   (status de ADRs: proposta/emenda pendente), `docs/planos/**` (rascunhos/ONGOING),
   `.ai/workflows/`, raiz (`PLANEJAMENTO.md`, `task-*.json`). Use caminhos VIVOS (a árvore
   tem realocação humana não-commitada em `docs/planos/` → `legacy/` + `plano-granular/`).
2. **Para cada item**: caminho, tipo, status exato + linha, origem (task/HF/ADR que o gerou),
   o que pendência (revisão? CCB? implementação?), ação CCB recomendada
   (`aprovar|ratificar|rejeitar|remendar`) com justificativa — SEM decidir.
3. **Seção secundária — pendências CCB já conhecidas** (cross-referência, sem duplicar
   inventário): emendas E-01..E-08 (spec-001:193-334), proposta ADR-016 (ADR-016:5), emenda
   ADR-010 (spec-005:349), gate humano G-1..G-7 (docs/analise/REV-PLANO-GERENCIAMENTO-COGME-v2.1.0-rodada2.md),
   GAPs de spec pendentes (docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md).
4. **Consolidação**: tabela única ordenada por ação CCB recomendada + contagem por status;
   no topo, os 3 itens mais bloqueantes com justificativa.

## Critérios de Aceite

- [ ] Relatório emitido em `docs/analise/LEVANTAMENTO-DRAFTS-CCB-2026-11-02.md` com frontmatter (padrão do projeto)
- [ ] Varredura cobre .ai/specs, .ai/handoffs, .ai/agents, docs/decisoes, docs/planos, raiz — com método declarado (comandos grep usados)
- [ ] Cada item com caminho+linha do status, origem, pendência e ação CCB recomendada (recomendação, não veredicto)
- [ ] Seção de pendências CCB já conhecidas (E-01..E-08, ADR-016, ADR-010, G-1..G-7, lista de specs pendentes) cross-referenciada
- [ ] Tabela consolidada + contagens por status + top-3 bloqueantes
- [ ] Nenhum arquivo fora do relatório alterado; imutáveis intocados
- [ ] Cada classificação com evidência `arquivo:linha`; incerteza `UNKNOWN - verify`

## Restrições

- Edite EXCLUSIVELY `docs/analise/LEVANTAMENTO-DRAFTS-CCB-2026-11-02.md`.
- NUNCA alterar: `constitution.md`, registry (header/version enum), `.opencode/agents/*`,
  handoffs, ledger, ADRs, specs — levantamento é somente leitura.
- Sem decisão de aprovação (Art. 5.1 — CCB é o Humano); sem invenção de status/datas.
- Narrativa PT-BR; identificadores/caminhos EN; evidência `arquivo:linha`.
- Retorno: parcel half-duplex schema 6 (enum correto, `route` objeto), `dod` com todos os
  AC, `notes` ≤5 linhas com contagens (nº de drafts por status) + top-3 bloqueantes.
  Resposta final ≤1200 tokens (relatório vai ao ARQUIVO).
- kill_switch: inherited
- CPU-only, sem CUDA/cloud; FOSS-only; LGPD primária (zero PII em relatórios e volumes).
