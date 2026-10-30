# ADR-003 — Métricas de Fluxo (Substituição de EVM)

| Campo | Valor |
|---|---|
| Versão | 1.0.0 |
| Status | Finalizado |
| Data da decisão | 19/09/2026 |
| Data de formalização do documento | 28/10/2026 |
| Decisor | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Gatilhos G1–G4 | G1 (impacto transversal — Cronograma + Integração + Qualidade), G3 (questionabilidade acadêmica — ausência de Gantt/EVM), G4 (trade-off não óbvio — abandono de métricas preditivas) |
| Rastreabilidade | TAP §3 (Métricas e Indicadores) + §11 (orçamento zero) + §11.3 (implícito); EAP N9.1; REQ-12; ADRs correlatas: ADR-002 (fluxo), ADR-004 (unidade de métrica), ADR-005 (freeze); NC-03 do Plano de Cronograma (definição operacional de Cycle Time) |
| Domínio PMBOK 7ª | Medição |

## Contexto

O glossário v2.1 listava SPI/CPI (EVM — PMBOK 6ª) como métricas ativas; o TAP §3 declara o uso de métricas de fluxo Kanban. Análise registrada no OKB §4: EVM é inaplicável ao COGME porque (i) orçamento zero (TAP §11) → AC = 0 → CPI indeterminado; (ii) escopo emergente (Kanban) → PV não faz sentido em fluxo contínuo. Métricas de fluxo são alinhadas ao Domínio de Medição PMBOK 7ª.

## Decisão

**Métricas oficiais do COGME (exclusivas):**

| Métrica | Fórmula | Meta | Frequência |
|---|---|---|---|
| Cycle Time | Média (Done − In Progress) | ≤ 3 dias | Semanal |
| Throughput | Cards concluídos / semana | ≥ 5 cards | Semanal |
| CFD (Cumulative Flow Diagram) | Visualização de gargalos | Sem bandas largas | Semanal |
| WIP em fluxo | Cards em In Progress | ≤ 9 (3 × 3 pessoas) | Contínuo |
| Coverage | Linhas testadas / totais | ≥ 80% | Por push (CI) |

**Métricas LEGADO (NÃO APLICÁVEIS):** SPI, CPI, EVM — removidas do glossário v2.2+ e marcadas "LEGADO — NÃO APLICÁVEL — Substituído por métricas de fluxo Kanban (ADR-003)".

**Instrumentação:** as métricas são nativas do GitHub Insights/fluxo Kanban (SSOT, ADR-002) — não há stack de observabilidade dedicada (Prometheus/Grafana rejeitados). Definição operacional de Cycle Time vigente: `In Progress` → `Done` (Plano de Cronograma NC-03). Período de calibração: 23/09–03/10/2026; metas ajustadas pós-calibração via ADR da baseline (Integração §1.6.3) — ver INDEX.md, ADR-proposta-007 (não emitida).

## Alternativas Consideradas

- EVM (SPI/CPI) — descartado: matematicamente indeterminado com AC = 0 e escopo emergente.
- Prometheus + Grafana — descartado: overhead operacional sem justificativa para MVP acadêmico (métricas nativas do GitHub Insights bastam).
- Datadog/ELK — descartados: serviços pagos/proprietários (violam P2 FOSS e TAP §11).

## Consequências e Trade-offs

- ✅ Positivas: alinhamento ao Manifesto Ágil, métricas nativas do GitHub, foco em valor entregue.
- ⚠️ Riscos: exige calibração inicial (23/09–03/10) para estabelecer baseline realista.
- 🔄 Fallback: baseline indicando throughput < 3 cards/semana após 03/10 → revisar escopo do MVP (gestão de mudanças).
- Trade-offs aceitos: métricas de fluxo > EVM (contexto ágil); baseline empírica > metas arbitrárias (Domínio de Medição PMBOK 7ª).

## Governança

- Custódia: agent-pm (coleta semanal); definição formal deste documento (custódia architect).
- Emenda: ajuste de metas pós-calibração → ADR específica (Integração §1.6.3); divergências com dados empíricos → `docs/metricas/baseline.md` (standalone, GMV).
- NÃO duplicar o texto desta ADR nos planos — cross-reference (OKB §3.4 anti-padrões).
- kill_switch: screened.

## Histórico

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 28/10/2026 | agent-architect | Formalização do corpo (decisão CCB de 19/09/2026; emissão original comprometida em commit de 0 byte — 21/09/2026; stub antigo dizia "Prometheus + Grafana" — substituído pela decisão aprovada de fluxo Kanban/GitHub Insights) |
