---
id: docs-metricas-baseline
title: Baseline de Métricas de Fluxo (Calibração)
type: metrica
version: 1.1.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/metricas/baseline.md (normalizado em 2026-11-05)
- docs/auditorias/aud-2026-11-03-rodada-specs.md (dados observáveis de execução)
- docs/auditorias/aud-2611-01-auditoria-registry-ledger.md (dados observáveis de execução)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- metricas
- docs
- normalizado
---

# Baseline de Métricas de Fluxo (Calibração)

## 1. Baseline observado (dados reais de auditoria)

Os valores abaixo foram extraídos das auditorias realizadas e refletem o estado real do repositório na data da calibração.

| Métrica | Valor observado | Fonte | Data |
|---|---|---|---|
| Testes de agentes — aprovados | 149 passed / 149 total (excluindo 4 falhas pré-existentes de wiring/topologia) | aud-2026-11-03-rodada-specs.md; aud-2611-01 | 03/11/2026 |
| Testes de agentes — falhas pré-existentes | 4 failed (test_dispatcher_and_sync topology_report; test_onda1 gate_promulgation[nexus]; test_onda6 chain_wiring; test_onda7 no_loose_ends) | aud-2026-11-03-rodada-specs.md | 03/11/2026 |
| Agentes L2 no AGENT_TOPOLOGY | 30 | aud-2611-01-auditoria-registry-ledger.md (F-02) | 02/11/2026 |
| Specs repovoadas na rodada | 10 novas + 2 emendas + 3 pinned | aud-2026-11-03-rodada-specs.md | 03/11/2026 |
| Agents promulgados (ecossistema) | 46 | ccb-log A09 | 31/10/2026 |

## 2. Baseline simulado (pendente de medição real — OKB-C-16)

O período de calibração (23/09–03/10) encerrou-se sem registro de dados reais de Cycle Time e Throughput no repositório. Os valores abaixo permanecem **seeds simulados** e serão substituídos por medição real a partir da execução de M2+M3 (checkpoint único 15/11/2026) via GitHub Insights.

> ⚠️ **AVISO:** valores simulados, não empíricos. Não constituem evidência de desempenho.

| Métrica | Valor Seed (SIMULADO) | Meta Calibrada | Fonte Real Futura |
|---|---|---|---|
| Cycle Time | 3 dias | ≤ 3 dias | GitHub Insights (In Progress → Done) |
| Throughput | 5 cards/semana | ≥ 5 cards/semana | GitHub Insights |
| WIP em Fluxo | 3 cards/pessoa | ≤ 3 cards/pessoa | GitHub Projects (Coluna In Progress) |
| Coverage | 80% | ≥ 80% | GitHub Actions (pytest + coverage.py) |

**Owner:** GP Leonardo (Recalibração) · **Prazo de Substituição:** 08/11/2026 · **Status OKB-C-16:** extração de auditorias concluída; medição real de Cycle Time/Throughput pendente em M3.
