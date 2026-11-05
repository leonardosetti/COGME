---
id: decisoes-consolidado-adrs-tmp
title: Consolidado temporário — ADRs 001 a 012 (COGME)
version: '2.1'
class: decisao-adr
status: obsoleto
owner: agent-project-analyst
derived-from:
- docs/decisoes/consolidado-adrs-tmp.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- normalizado
---
<!-- PROVENIÊNCIA: arquivo temporário de análise (consolidado ADR-001..012), mantido a pedido do GP.
     Reconstruído em 30/10/2026 após remoção acidental na onda de higiene (CCB-LOG A01/A02).
     Conteúdo = concatenação verbatim das 12 ADRs canônicas (sem edição). Não é fonte normativa:
     a fonte de cada ADR é o arquivo individual em docs/decisoes/. -->

# Consolidado temporário — ADRs 001 a 012 (COGME)

> **Natureza:** artefato de análise, não canônico. Cada seção abaixo reproduz integralmente uma ADR.
> **Regerado em:** 30/10/2026 | **Fontes:** `docs/decisoes/ADR-00*.md` (12 arquivos, versões vigentes).

---


<!-- ===== docs/decisoes/adr-001-stack.md ===== -->

# ADR-001 — Stack Tecnológica FOSS

| Campo | Valor |
|---|---|
| Versão | 1.0.0 |
| Status | Finalizado |
| Data da decisão | 19/09/2026 |
| Data de formalização do documento | 28/10/2026 |
| Decisor | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Gatilhos G1–G4 | G1 (impacto transversal — todas as fases N4–N12), G2 (irreversibilidade prática — troca de stack reescreve backend), G4 (trade-off FOSS × conveniência proprietária) |
| Rastreabilidade | TAP §3 (Inovação) + §8 (Restrições FOSS/§8.4 orçamento zero) + §11; EAP N1.4, N4.1, N5.1–N5.4 (fila N9.1); REQ-12 (ADRs); ADRs correlatas: ADR-005 (freeze), ADR-006 (LLM local, Draft — Pending CCB Human Verification) |
| Domínio PMBOK 7ª | Trabalho do Projeto + Abordagem de Desenvolvimento |

## Contexto

O projeto exige stack 100% FOSS (restrição TAP §8.4, orçamento zero — TAP §11), com capacidade de: backend assíncrono para simulação cambial (REQ-01, latência ≤ 2s); geração de PDF (REQ-04, ≤ 3s); cache local (REQ-07); testes automatizados (REQ-08, coverage ≥ 80%). A seleção é executada na fase EAP N4.1 (Seleção e Validação da Stack FOSS), com validação por protótipo (TAP §10, R2; Plano de Cronograma NC-04).

Fonte autorizativa do corpo: resumo aprovado em `git dd3b087` (21/09/2026) + OKB §4 (ADR-001). O commit dd3b087 persistiu emissões 001–005 com 0 byte; a formalização em corpo íntegra ocorre em 28/10/2026 (ver ADR-005 para a política de regularização).

## Decisão

Adoção da seguinte stack (todas as licenças OSI-approved):

| Camada | Tecnologia | Licença | Justificativa |
|---|---|---|---|
| Backend | Python 3.11 + FastAPI | PSF / MIT | Assíncrono nativo, ecossistema maduro |
| Banco | SQLite | Public Domain | Zero-config, ACID, adequado ao MVP |
| Geração PDF | WeasyPrint | BSD-3-Clause | HTML/CSS → PDF, FOSS |
| Testes | pytest + coverage.py | MIT | Padrão Python, integração CI |
| CI/CD | GitHub Actions (Free Tier) | Proprietário gratuito | Nativo ao SSOT |
| Frontend | HTML5 + CSS3 + JS vanilla | — | KISS, sem framework pesado |
| LLM (SDD) | QwenStudio | Licença autorizada | TAP §3 (Inovação); inferência local via llama.cpp/Qwen 30B no hardware 8700G/60GB — ver ADR-006 (Draft — Pending CCB Human Verification) |

## Alternativas Consideradas

- Flask (MIT) — fallback registrado, acionável se a curva de aprendizado do FastAPI for excessiva.
- PostgreSQL — descartado: complexidade operacional desnecessária para MVP acadêmico.
- Ferramentas proprietárias de PDF/CI — descartadas: violam a restrição FOSS absoluta (P2) e orçamento zero.

## Consequências e Trade-offs

- ✅ Positivas: zero custo, auditabilidade total, comunidade ativa, compatibilidade com hardware local (P6 revisada).
- ⚠️ Riscos: SQLite limita concorrência (aceitável para o MVP acadêmico); WeasyPrint exige dependências nativas (glibc, Pango).
- 🔄 Fallback: FastAPI com curva excessiva → Flask (MIT).
- Trade-offs aceitos: Simplicidade (KISS) > Performance extrema; FOSS absoluto > conveniência proprietária; SQLite > PostgreSQL.
- Stack sob regime de freeze (ADR-005): mudança de componente exige ADR de emenda (KYB: MAJOR), nunca bypass (contratos: Plano de Custos §4.5/§4.6, gates de registro em ADR-001 ou ADR específica).

## Governança

- Custódia: agent-architect (R-01 stack-drift watch, CVE half co-ownership com digital-security).
- Emenda: somente via change-request + CCB humano (GP Leonardo) + ADR MAJOR (Integração §1.7; Plano de Custos §4.6).
- kill_switch: screened (sem vigilância por design; sem kernel proprietário sem Pilares de Bypass).

## Histórico

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 28/10/2026 | agent-architect | Formalização do corpo (decisão CCB de 19/09/2026; emissão original comprometida em commit de 0 byte — 21/09/2026; stubs contraditórios detectados 26/10) |


---


<!-- ===== docs/decisoes/adr-002-kanban.md ===== -->

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


---


<!-- ===== docs/decisoes/adr-003-metricas.md ===== -->

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


---


<!-- ===== docs/decisoes/adr-004-tasklists.md ===== -->

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


---


<!-- ===== docs/decisoes/adr-005-freeze.md ===== -->

# ADR-005 — Regime de Freeze do TAP e Precedência Intra-TAP

| Campo | Valor |
|---|---|
| Versão | 1.0.0 |
| Status | Regularização Tardia — ratificação CCB pendente da verificação da data 25/09 informada na memória do GP |
| Data da decisão efetiva | 21/09/2026 (NC-00, Plano de Cronograma §3.8) |
| Data de formalização do documento | 28/10/2026 |
| Decisor | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Gatilhos G1–G4 | G1 (impacto transversal — todos os 8 planos), G3 (questionabilidade acadêmica), G4 (trade-off não óbvio — imutabilidade × leitura operacional) |
| Rastreabilidade | TAP §6 (precedência intra-TAP) + §3/§9 P9 (status ontológico do TAP); EAP N9.1; REQ-12; NC-00 (Plano de Cronograma §3.8 — locus canônico da decisão); Glossário §11; ADRs correlatas: ADR-001–004 (todas sob o regime de freeze); Integração §1.4 |
| Domínio PMBOK 7ª | Trabalho do Projeto + Incerteza |
| Processo PMBOK 6ª (dicionário) | 4.6 |

**Tipo:** Regularização tardia
**Data da decisão efetiva:** 21/09/2026
**Data da formalização:** 28/10/2026
**Motivo da tardança:** emissões 001–004 comprometidas em commit 0 byte (dd3b087, 21/09/2026); stubs contraditórios detectados 26/10; a emissão prometida da ADR-005 "antes do M2" (≤ 30/09/2026, Plano de Cronograma §3.9/Tabela 3) não se consumou.
**Lição aprendida:** decisões do GP com ≥ 2 gatilhos devem ser formalizadas em arquivo canônico com corpo no mesmo ciclo do commit de emissão; não deixar a formalização última da fila (política OKB Aditivo §2.3). Auditoria de stubs 0B na lista de verificação de cada marco.

## Contexto

O TAP encontra-se congelado desde o início do planejamento (última versão 18/09/2026, anterior aos planos): não é revisado, reversionado ou corrigido ao longo do ciclo, em conformidade com seu status ontológico (Premissa P9; Glossário §11; PMBOK 6ª §4.1 como dicionário). Divergências entre seções do TAP precisavam de locus formal de resolução sem tocar o termo autorizativo. Fonte integral da decisão (texto canônico): Plano de Cronograma §3.8 NC-00 (docs/planos/plano-cronograma.md).

## Decisão

1. **Freeze:** o TAP não é revisado ao longo do ciclo — nenhuma nota de contexto o corrige.
2. **Precedência intra-TAP:** em divergência entre seções do TAP, a seção §6 Marcos é canônica para matéria temporal e de marcos.
3. **Locus de contexto:** o Plano de Cronograma (§3.8) detém, com precedência, as Notas de Contexto (NCs) que registram a leitura operacional vigente do TAP congelado; divergências jamais são tratadas como correções do TAP.
4. **Trade-off declarado:** aceita-se divergência textual entre o termo autorizativo imutável e a leitura operacional, em favor da imutabilidade da referência de autorização e da trilha auditável de interpretações.

## Alternativas Consideradas

- Revertionar/corrigir o TAP (novas versões) — rejeitado: viola P9, status ontológico e auditabilidade do termo autorizativo.
- Deixar cada plano resolver divergências de forma independente — rejeitado: incoerência entre as 8 áreas e perda de trilha única.
- Corrigir apenas os artefatos vivos (Glossário, ADRs, baseline) por saneamento — adotado parcialmente: registro de saneamento do Plano de Cronograma §3.8 (tabela de pendências por artefato vivo).

## Consequências e Trade-offs

- ✅ Positivas: imutabilidade da referência de autorização; trilha auditável de interpretações; blindagem acadêmica (Prof. Dr. Nivaldo Carleto vê coerência ontológica).
- ⚠️ Riscos: custo de manutenção das NCs; risco de leitura divergente em planos que não adotarem o locus.
- 🔄 Fallback: divergência não coberta por NC → change-request + decisão do GP + registro em NC subsequente.
- **Registro de mudança de compromisso:** a formalização migrou do compromisso de "emissão antes do M2 (≤ 30/09)" para formalização em 28/10/2026 — consequência direta da tardança dos termos acima.

## Governança

- Custódia: agent-architect (ADRs) + agent-pm (Notas de Contexto).
- Emenda: qualquer mudança de marco oficial exige change-request + aprovação do CCB + ADR + comunicação ao Prof. Dr. Nivaldo Carleto no marco subsequente (Integração §1.7.3).
- Incorporação da cláusula na próxima revisão do Plano de Integração §1.4 (Plano de Cronograma Tabela 3).
- kill_switch: screened.

## Histórico

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 28/10/2026 | agent-architect | Regularização tardia: formalização do corpo (decisão efetiva 21/09/2026, NC-00); status reflete pendência de ratificação CCB da data 25/09 alegada em memória do GP |


---


<!-- ===== docs/decisoes/adr-006-inteligencia-sdd.md ===== -->


# ADR-006 — Módulo de Inteligência SDD: Modelo Primário, Fallback e Flexibilização Cloud/FREE

| Campo                                         | Valor                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Versão**                             | 2.0.0                                                                                                                                                                                                                                                                                                                                                         |
| **Status**                              | Finalizado (ratificado pelo CCB-001 em 29/10/2026)                                                                                                                                                                                                                                                                                                            |
| **Data da decisão**                    | 26/10/2026                                                                                                                                                                                                                                                                                                                                                    |
| **Data de formalização do documento** | 29/10/2026                                                                                                                                                                                                                                                                                                                                                    |
| **Decisor**                             | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7)                                                                                                                                                                                                                                                                                                         |
| **Gatilhos G1–G4**                     | G1 (impacto transversal — todas as fases de execução SDD), G2 (irreversibilidade prática — troca de modelo GGUF implica recompilação e revalidação de throughput), G3 (questionabilidade acadêmica — "por que MoE e não denso?"), G4 (trade-off não óbvio — eficiência computacional × complexidade operacional de dois modos de execução) |
| **Rastreabilidade**                     | TAP §3 (Inovação) + §8 (Restrições FOSS/orçamento zero) + §9 (Premissa P3 — stack local); EAP N1.4, N4.4; REQ-12 (ADRs), REQ-13 (prompts catalogados); ADRs correlatas: ADR-001 (stack FOSS, sobreposta parcialmente), ADR-005 (freeze), ADR-011 (MCPs e memória persistente, sobreposta parcialmente por esta em relação ao roteamento)          |
| **Domínio PMBOK 7ª**                  | Abordagem de Desenvolvimento + Trabalho do Projeto + Incerteza                                                                                                                                                                                                                                                                                                |
| **Processo PMBOK 6ª (dicionário)**    | 4.3 Orientar e Gerenciar o Trabalho do Projeto; 8.2 Realizar Garantia da Qualidade                                                                                                                                                                                                                                                                            |

## Contexto

O ecossistema SDD do COGME opera exclusivamente em hardware local (AMD Ryzen 7 8700G, Radeon 780M, 58GB RAM reais, Arch Linux). O motor de inferência é o `llama.cpp` compilado com Vulkan, LTO e AVX-512. A interface é o OpenCode.

Na versão 1.0 desta ADR, o modelo primário era Qwen 32B Instruct (denso, ~20GB RAM ativa). Após materialização do risco RE-08 (*overengineering* de governança consumindo capacidade de desenvolvimento), constatou-se que o modelo denso limitava fluxos paralelos de agentes, degradando throughput abaixo de 6 t/s em cenários de múltiplas personas ativas simultaneamente.

Adicionalmente, a Constituição v1.1.0 proibia qualquer tráfego de dados do projeto para nuvem (P-02 absolutista). Essa restrição, embora defensável academicamente, impedia resiliência operacional em picos de carga sem comprometer orçamento zero.

## Opções Consideradas

| #  | Opção                                       | Prós                                                                                     | Contras                                                                                                       |
| -- | --------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| O1 | Manter Qwen 32B Instruct denoso               | Simplicidade; um único modo de execução                                                | Throughput insuficiente para fluxos paralelos; RAM pico elevado; sem resiliência                             |
| O2 | Migrar para Qwen3-30B-A3B MoE (Q4_K_M)        | ~3B parâmetros ativos por token vs. 30B; ~4GB RAM ativa; ≥ 12 t/s esperados; Apache-2.0 | Complexidade adicional (dois modos: local + cloud fallback); necessidade de reconciliar `download_model.sh` |
| O3 | Adicionar modelos cloud free tier (whitelist) | Resiliência em sobrecarga local; custo zero; Hugging Face/OpenRouter/Groq/GitHub Models  | Risco de soberania de dados; violação potencial da Constituição v1.1.0 se não emendada                   |
| O4 | Combinar O2 + O3 com restrições             | Melhor equilíbrio entre eficiência, resiliência e soberania                            | Maior superfície de configuração; exige kill switch claro                                                  |

## Decisão

**Aprovar a opção O4.**

1. **Modelo primário:** substituir Qwen 32B Instruct por **Qwen3-30B-A3B Q4_K_M** (MoE: 30B totais, ~3B ativos por token, ~18 GB em disco, ~4 GB RAM ativa). Licença: Apache-2.0.
2. **Modelo fallback local:** manter **Qwen 14B Q4_K_M** (denso, ~9 GB, ~10 GB RAM, ≥ 12 t/s) como reversão imediata via symlink `active.md`.
3. **Modelo batch (deferred):** registrar **Qwen 72B Q4_K_M** no catálogo, mas NÃO baixar até necessidade real comprovada (~42 GB, contexto limitado a 4k).
4. **Modelo deprecated:** registrar **Qwen3.8-27B Q4_K_M** como mantido em disco para backup forense, mas PROIBIDO para uso ativo (INC-F01).
5. **Flexibilização cloud:** autorizar provedores em free tier da whitelist constitucional (Hugging Face Inference API, OpenRouter, Groq, GitHub Models), **exclusivamente para tarefas não sensíveis**, nos termos da emenda constitucional v1.2.0 (Art. 3, P-02 revisado e Art. 7.4).
6. **Contexto configurado:** 32.768 tokens. Orçamento efetivo de execução: 24.000 tokens (75%, margem de segurança). Output máximo: 4.096 tokens.
7. **Performance alvo:** ≥ 12 t/s (geração), ≥ 25 t/s (processamento de prompt). TTFT < 2 s.

## Consequências

- Positivas: aumento significativo de throughput em fluxos paralelos; redução de consumo de RAM ativa; resiliência operacional via fallback cloud condicionado; alinhamento com ADR-011 (MCPs e separação L1/L2/L3).
- Negativas: complexidade de gestão de dois modos de execução (local + cloud); necessidade de auditoria contínua de soberania de dados; overhead de reconciliação do `download_model.sh`.
- Neutras: o modelo denso Qwen 32B permanece disponível como fallback secundário, mas não é mais o primário.

## Trade-offs Declarados

| Aspecto                  | Ganho                           | Perda/Risco                                                    | Mitigação                                                                                         |
| ------------------------ | ------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| MoE vs. Denso            | Eficiência (3B ativos vs. 30B) | Menor profundidade de raciocínio em tarefas complexas únicas | Fallback para Qwen 72B deferred se necessário; revisão humana obrigatória                        |
| Cloud free tier          | Resiliência em sobrecarga      | Risco de soberania de dados                                    | Proibição absoluta de dados sensíveis; whitelist auditável; kill switch imediato                |
| Dois modos de execução | Flexibilidade                   | Complexidade operacional                                       | Symlink `active.md` como mecanismo canônico de troca; MCP `nexus-dispatch` gerencia roteamento |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo                                                                                               | Domínio PMBOK 7ª           | Data       |
| -------------- | -------- | ---------------------------------------------------------------------------------------------------- | ---------------------------- | ---------- |
| ADR-001        | Parcial  | Substituição do modelo LLM primário (Qwen 32B → Qwen3-30B-A3B MoE) + flexibilização Cloud/FREE | Abordagem de Desenvolvimento | 29/10/2026 |

## kill_switch

Reversão automática para Qwen 14B via alteração do symlink `.ai/personas/active.md` se:

- throughput < 12 t/s por 5 minutos consecutivos;
- detecção de envio de dados sensíveis para cloud não autorizada;
- corrupção do ledger de sessão impedindo roteamento determinístico.

## Governança

- **Custódia:** `agent-nexus-prime-ultimate` (L0 orquestrador).
- **Emenda:** somente via change-request + CCB humano (GP Leonardo) + ADR MAJOR.
- **Auditoria:** `project-auditor` verifica conformidade com P-02/P-03 em cada milestone.
- **Registro de handoffs:** todos os prompts enviados ao modelo primário ou fallback devem ser catalogados em `.ai/handoffs/task-ta-*.json` (REQ-13).


---


<!-- ===== docs/decisoes/adr-007-redes-de-projeto.md ===== -->


# ADR-007 — Redes de Projeto como Artefato Acadêmico Macro (Dualidade CPM × Kanban)

| Campo                                         | Valor                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Versão**                             | 1.1.0                                                                                                                                                                                                                                                                                                      |
| **Status**                              | Aprovado (ratificado pelo CCB-001 em 29/10/2026)                                                                                                                                                                                                                                                           |
| **Data da decisão**                    | 29/10/2026                                                                                                                                                                                                                                                                                                 |
| **Data de formalização do documento** | 29/10/2026                                                                                                                                                                                                                                                                                                 |
| **Decisor**                             | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7)                                                                                                                                                                                                                                                      |
| **Gatilhos G1–G4**                     | G1 (impacto transversal — Cronograma + Integração + Escopo), G3 (questionabilidade acadêmica — imposição do stakeholder-avaliador Prof. Dr. Nivaldo Carleto quanto à presença de redes CPM), G4 (trade-off não óbvio — dualidade de modelos preditivo macro × ágil micro)                    |
| **Rastreabilidade**                     | TAP §3 (Métricas) + §6 (Marcos M1–M4); EAP N3.1–N3.6; REQ-12; ADRs correlatas: ADR-002 (Kanban como método de execução), ADR-003 (métricas de fluxo, sobreposta parcialmente), ADR-005 (freeze do TAP); NC-01 e NC-04 do Plano de Cronograma §3.6; Figuras 16–21 e Tabelas 53–58 do Plano v2.0 |
| **Domínio PMBOK 7ª**                  | Planejamento + Medição + Entrega                                                                                                                                                                                                                                                                         |
| **Processo PMBOK 6ª (dicionário)**    | 6.3 Sequenciar Atividades; 6.5 Desenvolver Cronograma                                                                                                                                                                                                                                                      |

## Contexto

O Plano de Cronograma v2.0 (§3.4) apresentava redes CPM (Critical Path Method) com caminho crítico, folgas e sequenciamento preditivo. A ADR-003 havia declarado métricas EVM (SPI/CPI/VAC) como LEGADO — NÃO APLICÁVEIS, substituindo-as por métricas de fluxo Kanban (Cycle Time, Throughput, CFD, WIP, Coverage).

Essa tensão gerou contradição interna no documento: se EVM é inaplicável, por que manter redes CPM? Além disso, o Prof. Dr. Nivaldo Carleto, como stakeholder-avaliador, exigiu expressamente a presença de redes de projeto como artefato de validação acadêmica de viabilidade macro.

A questão central não era técnica, mas epistemológica: como conciliar um modelo preditivo (CPM/Gantt) com um modelo adaptativo (Kanban/fluxo contínuo) sem quebrar o SSOT operacional?

## Opções Consideradas

| #  | Opção                                                                     | Prós                                                           | Contras                                                                                               |
| -- | --------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| O1 | Eliminar completamente as redes CPM                                         | Pureza metodológica ágil; elimina contradição               | Viola imposição direta do stakeholder-avaliador; perde evidência acadêmica de viabilidade macro   |
| O2 | Manter redes CPM como linha de base operacional                             | Atende requisito acadêmico                                     | Contradiz ADR-003; reintroduz EVM implicitamente; confunde equipe sobre qual modelo executar          |
| O3 | Dualidade documentada: CPM macro (acadêmico) × Kanban micro (operacional) | Atende stakeholder sem quebrar SSOT; transparência pedagógica | Exige comunicação clara para evitar confusão operacional; overhead de manutenção de dois modelos |

## Decisão

**Aprovar a opção O3.**

1. As redes de projeto (Figuras 16–21, Tabelas 53–58 do Plano v2.0) são mantidas **exclusivamente como artefatos de validação acadêmica de viabilidade macro**, atendendo à imposição do Prof. Dr. Nivaldo Carleto.
2. O nível operacional permanece regido pelo fluxo Kanban (ADR-002) e métricas de fluxo (ADR-003). Nenhuma atividade diária, card ou sprint é planejada com base em datas preditivas derivadas das redes CPM.
3. A dualidade deve ser explicitada textualmente no Plano de Cronograma §2.4.4 com a frase canônica: *"A rede valida o marco; o Kanban executa a tarefa."*
4. As redes CPM devem ser refatoradas de PNG para SVG editável (ação P2.3 do input canônico), com caminho crítico destacado em `#C0392B`.
5. Métricas EVM continuam declaradas como LEGADO — NÃO APLICÁVEIS (ADR-003). As redes servem apenas para demonstrar coerência temporal macro entre marcos M1–M4, não para controle diário.

## Consequências

- Positivas: atende requisito acadêmico mandatório sem contaminar execução operacional; preserva integridade da ADR-002 e ADR-003; demonstra maturidade metodológica da equipe ao lidar com dualidade.
- Negativas: risco de confusão se a comunicação não for clara; overhead de manter dois modelos sincronizados nos marcos.
- Neutras: as redes não geram alertas automáticos nem gates operacionais; sua função é estritamente expositiva-acadêmica.

## Trade-offs Declarados

| Aspecto                       | Ganho                                         | Perda/Risco                              | Mitigação                                                                        |
| ----------------------------- | --------------------------------------------- | ---------------------------------------- | ---------------------------------------------------------------------------------- |
| CPM macro + Kanban micro      | Compliance acadêmico + agilidade operacional | Dualidade cognitiva para a equipe        | Comunicação explícita no Refinement semanal; blindagem textual no Plano §2.4.4 |
| Redes como artefato estático | Simplicidade de manutenção                  | Obsolescência rápida se marcos mudarem | Atualização obrigatória nas mudanças de marco via CR + ADR                     |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo                                                                                            | Domínio PMBOK 7ª       | Data       |
| -------------- | -------- | ------------------------------------------------------------------------------------------------- | ------------------------ | ---------- |
| ADR-003        | Parcial  | Autoriza redes CPM no nível macro/acadêmico, sem reintroduzir EVM/SPI/CPI no nível operacional | Planejamento + Medição | 29/10/2026 |

## kill_switch

Não aplicável diretamente. Contudo, se uma rede CPM for utilizada indevidamente como gate operacional (ex.: bloquear card por divergência de data preditiva), isso constitui violação da ADR-002 e ADR-003, acionando abortamento da operação e escalonamento ao CCB.

## Governança

- **Custódia:** `agent-scheduler` (área de Cronograma).
- **Validação:** cada mudança de marco (M1–M4) exige atualização das redes CPM correspondentes antes do fechamento do marco.
- **Comunicação:** o GP deve reiterar a dualidade em toda retrospectiva onde houver dúvida sobre precedência entre CPM e Kanban.


---


<!-- ===== docs/decisoes/adr-008.md ===== -->

# ADR-008 — Grafia Canônica do Stakeholder-Avaliador

| Campo | Valor |
|---|---|
| **Versão** | 1.1.0 |
| **Status** | Aprovado (ratificado pelo CCB-001 em 29/10/2026) |
| **Data da decisão** | 29/10/2026 |
| **Data de formalização do documento** | 29/10/2026 |
| **Decisor** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| **Gatilhos G1–G4** | G3 (questionabilidade acadêmica — risco de ofensa por grafia incorreta do nome do avaliador), G4 (trade-off não óbvio — consistência documental × overhead de saneamento global) |
| **Rastreabilidade** | TAP v3 (capa, sumário, agradecimentos, listas); Monografia-COGME.pdf; Plano de Recursos v2.0 §2.6; Plano de Comunicações v2.0 §2.7; Glossário v3.1; ADRs correlatas: nenhuma sobreposta; princípio constitucional P-10 (linguagem) e P-13 (precisão linguística, proposto na emenda v1.2.0) |
| **Domínio PMBOK 7ª** | Stakeholders + Qualidade |
| **Processo PMBOK 6ª (dicionário)** | 13.1 Identificar Partes Interessadas; 8.3 Controlar Qualidade |

## Contexto

Durante a revisão dos artefatos documentais do COGME, identificaram-se quatro variantes de grafia do nome do stakeholder-avaliador ao longo do histórico do projeto:

1. "Prof. Dr. Nivaldo Carletto" (duplo "t");
2. "Prof. Dr. Nivaldo Carleto" (único "t");
3. "Prof. Ms. Nivaldo Carleto";
4. "Nivaldo Carleto" (sem título).

A variante predominante em documentos recentes era "Carletto" (duplo "t"), introduzida erroneamente pela ADR-008 v1.0, que inferiu a grafia a partir de documentos históricos sem validação direta junto ao próprio stakeholder ou ao GP.

Trata-se de dado sensível: erro de grafia em nome de avaliador acadêmico configura falta grave de respeito institucional e pode comprometer avaliação nos marcos M1–M4.

## Opções Consideradas

| # | Opção | Prós | Contras |
|---|---|---|---|
| O1 | Manter "Carletto" como estava | Zero esforço de correção | Ofensa potencial ao avaliador; inconsistência com TAP v3 original |
| O2 | Validar grafia diretamente com o GP/CCB e fixar como canônica | Elimina ambiguidade; respeita hierarquia decisória | Overhead de saneamento global em ~15 documentos |
| O3 | Usar apenas "Nivaldo" informalmente | Simplicidade | Viola formalidade acadêmica exigida pelo contexto Fatec |

## Decisão

**Aprovar a opção O2.**

1. A grafia canônica, oficial e imutável é: **"Prof. Dr. Nivaldo Carleto"** (título "Dr." + sobrenome com um único "t").
2. Qualquer variação ("Carletto", "Ms.", ausência de título) constitui erro crítico e viola o princípio de precisão linguística (P-13 proposto na emenda constitucional v1.2.0).
3. Deve ser executado saneamento global (find & replace) em todos os arquivos Markdown, YAML, JSON, TXT e código comentado do repositório, excluindo backups forenses em `docs/archive/corrupted/`.
4. A ADR-008 v1.0 é revogada e substituída por esta v1.1.0.
5. Lição aprendida LA-003 registrada: decisões de grafia/nomes devem ser validadas diretamente com o stakeholder ou CCB, nunca inferidas de documentos históricos.

## Consequências

- Positivas: consistência documental total; respeito acadêmico blindado; eliminação de risco de ofensa.
- Negativas: overhead de atualização em aproximadamente 15 documentos; necessidade de verificação pós-saneamento para garantir zero ocorrências residuais.
- Neutras: monografias e PDFs já publicados podem conter a grafia antiga; esses artefatos são tratados como legado histórico, não como fonte viva de verdade.

## Trade-offs Declarados

| Aspecto | Ganho | Perda/Risco | Mitigação |
|---|---|---|---|
| Saneamento global | Consistência absoluta | Tempo de execução (~1h estimado) | Comando automatizado `rg + sed`; verificação pós-execução com grep negativo |
| Fixação em ADR | Imutabilidade normativa | Rigidez se o stakeholder mudar legalmente o nome | Emenda futura via CCB se necessário; registro de data-base 29/10/2026 |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo | Domínio PMBOK 7ª | Data |
|---|---|---|---|---|
| ADR-008 v1.0 | Total | Correção de inferência anterior não validada; fixação da grafia canônica definitiva | Stakeholders + Qualidade | 29/10/2026 |

## kill_switch

Qualquer geração de texto em PT-BR que contenha "Carletto" (duplo "t") após esta ADR entra em vigor constitui violação do mandamento linguístico absoluto (§0.2 do input canônico) e aciona abortamento imediato da operação, com retorno de Parcel contendo `kill_switch_invoked: true` e `ccb_action_required: true`.

## Governança

- **Custódia:** `agent-comms` (área de Comunicações) e `project-auditor`.
- **Verificação:** checklist de marco inclui busca por "Carletto" em todo o repositório.
- **Prevenção futura:** novos artefatos devem herdar a grafia canônica automaticamente via `_base.md` e templates de issue.


---


<!-- ===== docs/decisoes/adr-009.md ===== -->

# ADR-009 — Contagem Canônica da EAP (12 Fases + 37 Pacotes de Trabalho)

| Campo | Valor |
|---|---|
| **Versão** | 1.0.0 |
| **Status** | Aprovado (ratificado pelo CCB-001 em 29/10/2026) |
| **Data da decisão** | 29/10/2026 |
| **Data de formalização do documento** | 29/10/2026 |
| **Decisor** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| **Gatilhos G1–G4** | G1 (impacto transversal — Escopo, Cronograma, Custos, Qualidade, Riscos, Recursos, Comunicações, Integração), G2 (irreversibilidade prática — alterar contagem da EAP implica reestruturação completa do backlog Kanban e dos planos), G3 (questionabilidade acadêmica — divergência entre TAP §4 e Glossário v3.1), G4 (trade-off não óbvio — compliance com freeze × atualização de artefatos vivos) |
| **Rastreabilidade** | TAP v3 §4 (Tabela 4 — EAP canônica congelada desde 18/09/2026); EAP N1.1–N12.2; REQ-12; ADRs correlatas: ADR-005 (freeze do TAP, fundamento principal), ADR-002 (cards Kanban mapeados aos pacotes), ADR-004 (tasklists vinculadas aos pacotes); Glossário v3.1 (divergência detectada: 13 fases + 48 pacotes); Plano de Escopo v2.0 §2.5 |
| **Domínio PMBOK 7ª** | Planejamento + Entrega + Trabalho do Projeto |
| **Processo PMBOK 6ª (dicionário)** | 5.4 Criar EAP; 5.5 Validar Escopo |

## Contexto

O TAP v3, congelado pela ADR-005 desde 18/09/2026, define no §4 (Tabela 4) uma EAP composta por **12 fases macro e 37 pacotes de trabalho**. Essa é a estrutura autorizativa canônica do projeto.

Contudo, durante a revisão do Glossário v3.1 e de notas adjacentes, detectou-se uma divergência: algumas referências mencionavam **13 fases e 48 pacotes**. Essa discrepância surgiu provavelmente de:

1. Uma proposta inicial de decomposição mais granular que não foi incorporada ao TAP final;
2. Erro de contagem manual em rascunhos intermediários;
3. Inclusão implícita de uma 13ª fase de "Encerramento Administrativo" que, na verdade, está subsumida na Fase 12 (N12 — Encerramento).

A divergência cria risco operacional: se a equipe trabalhar com 48 pacotes enquanto o TAP autoriza apenas 37, haverá scope creep invisível, inflação de estimativas e perda de rastreabilidade TAP → EAP → Cards.

## Opções Consideradas

| # | Opção | Prós | Contras |
|---|---|---|---|
| O1 | Adotar 13 fases + 48 pacotes como canônico | Maior granularidade teórica | Viola TAP congelado (ADR-005); requer emenda constitucional prévia; rompe rastreabilidade |
| O2 | Manter 12 fases + 37 pacotes conforme TAP §4 | Compliance com freeze; SSOT preservado; auditabilidade acadêmica | Glossário e alguns planos precisam ser atualizados; risco de resistência da equipe acostumada à contagem maior |
| O3 | Ignorar a divergência e deixar ambos coexistirem | Zero esforço imediato | Insegurança operacional; impossibilidade de validar DoD contra baseline correta |

## Decisão

**Aprovar a opção O2.**

1. A contagem canônica da EAP é **12 fases + 37 pacotes de trabalho**, conforme TAP v3 §4, Tabela 4.
2. A 13ª fase eventualmente referenciada em artefatos vivos está implicitamente incluída na Fase 12 (N12 — Encerramento), não constituindo entidade autônoma.
3. O Glossário deve ser atualizado para v3.2 refletindo 12/37.
4. O OKB deve ser atualizado para v3.3 incorporando esta decisão.
5. Todos os cards Kanban existentes devem ser auditados contra a lista de 37 pacotes; cards órfãos (não mapeados a nenhum pacote) devem ser extintos ou remapeados.
6. Esta decisão está fundamentada na ADR-005 (freeze do TAP): o TAP é o artefato autorizativo supremo em matéria de escopo, e sua contagem não pode ser alterada por artefatos subordinados.

## Consequências

- Positivas: eliminação de ambiguidade escopística; compliance integral com regime de freeze; rastreabilidade TAP → EAP → Cards restaurada; base sólida para cálculo de throughput e cycle time.
- Negativas: overhead de atualização do Glossário e OKB (~2h estimado); necessidade de auditoria de todos os cards existentes contra a lista de 37 pacotes.
- Neutras: a diferença numérica (37 vs. 48) representa principalmente granularidade excessiva em propostas não adotadas; o conteúdo funcional dos pacotes permaneceu essencialmente o mesmo.

## Trade-offs Declarados

| Aspecto | Ganho | Perda/Risco | Mitigação |
|---|---|---|---|
| Compliance com TAP congelado | Auditabilidade acadêmica máxima | Rigidez se surgir necessidade real de novo pacote | Nova fase/pacote exige emenda constitucional + CR + ADR MAJOR |
| Atualização de artefatos vivos | Consistência documental | Esforço temporário de saneamento | Execução via script automatizado + verificação manual |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo | Domínio PMBOK 7ª | Data |
|---|---|---|---|---|
| — | — | Nenhuma ADR anterior tratava da contagem da EAP de forma explícita | — | — |

> **Nota:** Esta ADR reforça e operacionaliza a ADR-005 (freeze do TAP) no aspecto específico da contagem da EAP. Não há sobreposição direta, mas sim aplicação concreta de princípio já estabelecido.

## kill_switch

Se qualquer artefato vivo (Glossário, OKB, plano, spec, README) voltar a mencionar "13 fases" ou "48 pacotes" como contagem canônica após esta ADR entrar em vigor, isso constitui violação de SSOT e da ADR-005, acionando abortamento da operação e escalonamento ao CCB.

## Governança

- **Custódia:** `agent-scope-manager` (área de Escopo) e `project-auditor`.
- **Verificação:** checklist de marco inclui conferência cruzada TAP §4 ↔ Glossário ↔ OKB ↔ cards Kanban.
- **Prevenção futura:** templates de nova EAP devem importar diretamente da Tabela 4 do TAP.docx, evitando digitação manual sujeita a erro.


---


<!-- ===== docs/decisoes/adr-010-stack-infraestrutura.md ===== -->

# ADR-010 — Stack de Infraestrutura: PostgreSQL, Docker Compose, Nginx Latente e Hierarquia de APIs de Câmbio

| Campo | Valor |
|---|---|
| **Versão** | 1.0.0 |
| **Status** | Aprovado (ratificado pelo CCB-001 em 29/10/2026) |
| **Data da decisão** | 29/10/2026 |
| **Data de formalização do documento** | 29/10/2026 |
| **Decisor** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| **Gatilhos G1–G4** | G1 (impacto transversal — Backend, Dados, CI/CD, Frontend, Testes), G2 (irreversibilidade prática — migração SQLite → PostgreSQL exige schema, migrations e adaptação de ORM), G3 (questionabilidade acadêmica — "por que não manter SQLite mais simples?"), G4 (trade-off não óbvio — realismo de produção × overhead de infraestrutura) |
| **Rastreabilidade** | TAP §8 (Restrições FOSS) + §11 (Orçamento Zero); EAP N5.1–N5.4, N7.1; REQ-07 (persistência de cotações/cache), REQ-14 (OpenAPI automático); ADRs correlatas: ADR-001 (stack FOSS original, sobreposta parcialmente), ADR-005 (freeze — esta ADR emenda a stack dentro dos limites permitidos), ADR-011 (integração com MCPs e separação L1/L2/L3); Plano de Custos §4.5/§4.6 (gates de registro) |
| **Domínio PMBOK 7ª** | Abordagem de Desenvolvimento + Trabalho do Projeto + Qualidade |
| **Processo PMBOK 6ª (dicionário)** | 4.3 Orientar e Gerenciar o Trabalho; 8.2 Realizar Garantia da Qualidade |

## Contexto

A ADR-001 estabeleceu inicialmente SQLite como banco de dados canônico do produto, justificando-o por simplicidade e adequação ao MVP. Contudo, ao longo das rodadas de planejamento técnico, identificaram-se limitações estruturais:

1. **Tipagem fraca:** SQLite não impõe constraints rigorosas de tipo, aumentando risco de bugs silenciosos em cálculos cambiais (REQ-03 exige precisão de 2 casas decimais).
2. **Concorrência:** apesar de o MVP ser single-user, a arquitetura prevê endpoints assíncronos FastAPI que podem acessar o banco simultaneamente; SQLite locks tornam-se gargalo.
3. **Realismo de produção:** para fins acadêmicos e de portfólio, demonstrar domínio de PostgreSQL agrega valor significativamente superior a SQLite.
4. **Paridade de ambientes:** a ausência de containerização gerava o problema clássico "works on my machine".

Simultaneamente, definiu-se a necessidade de uma hierarquia robusta de fontes de cotação cambial (REQ-01, REQ-07), com fallback mandatório para dados oficiais brasileiros (PTAX/BCB), garantindo conformidade fiscal e soberania de dados.

## Opções Consideradas

### Banco de Dados

| # | Opção | Prós | Contras |
|---|---|---|---|
| DB1 | Manter SQLite | Simplicidade; zero setup | Tipagem fraca; lock em concorrência; menos realismo acadêmico |
| DB2 | Migrar para PostgreSQL 15+ | Tipagem estrita; concorrência MVCC; ecossistema maduro; valor acadêmico | Overhead de instalação/container; curva de aprendizado marginal |
| DB3 | MySQL/MariaDB | Alternativa válida | Menor aderência ao ecossistema Python async (asyncpg > aiomysql em maturidade) |

### Orquestração

| # | Opção | Prós | Contras |
|---|---|---|---|
| ORCH1 | Sem containerização | Simplicidade máxima | "Works on my machine"; dificuldade de replicar ambiente em CI |
| ORCH2 | Docker + Docker Compose | Paridade dev/test/prod; isolamento limpo; portabilidade | Consumo adicional de RAM (mitigado por 58GB disponíveis) |
| ORCH3 | Kubernetes | Escalabilidade extrema | Absolutamente desnecessário para MVP; overengineering flagrante |

### Servidor Web

| # | Opção | Prós | Contras |
|---|---|---|---|
| WEB1 | Apenas Uvicorn expondo porta | Simples | Sem TLS termination nativo; sem serving de estáticos otimizado |
| WEB2 | Nginx como reverse proxy latente | Profissional; pronto para HTTPS futuro; serve estáticos eficientemente | Um serviço extra no compose (opcional/desativável) |

### APIs de Câmbio

| # | Estratégia | Prós | Contras |
|---|---|---|---|
| API1 | Apenas Frankfurter | Gratuita; MIT; ECB confiável | Sem validação cruzada com dados BR |
| API2 | Apenas PTAX/BCB | Oficial brasileira; soberania | Latência variável; sem cobertura EUR/múltiplas moedas em tempo real |
| API3 | Circuit Breaker: Frankfurter → Fallbacks → PTAX/BCB obrigatório | Resiliência; conformidade fiscal; multi-fonte | Complexidade de implementação; necessidade de adapter pattern |

## Decisão

**Aprovar combinações: DB2 + ORCH2 + WEB2 + API3.**

1. **SGBD:** substituir SQLite por **PostgreSQL 15+** como banco canônico de persistência de cotações, cache e dados transacionais (REQ-07). Acesso via SQLAlchemy async + asyncpg. Migrações gerenciadas por Alembic.
2. **Orquestração:** adotar **Docker + Docker Compose** para paridade de ambientes dev/test/prod. Serviços mínimos: `db` (postgres:15-alpine), `web` (FastAPI/Uvicorn custom image), `proxy` (nginx:alpine, opcional/latente).
3. **Servidor Web:** prever **Nginx** como reverse proxy no `docker-compose.yml`, inicialmente desabilitado ou em perfil opcional, pronto para ativação quando houver necessidade de TLS ou serving intensivo de estáticos.
4. **Hierarquia de APIs de câmbio:** implementar padrão **Circuit Breaker** com a seguinte cadeia:
   - **Primária:** Frankfurter (`https://frankfurter.dev/`, REST, MIT, dados ECB).
   - **Fallbacks candidatos:** `fawazahmed0 currency-api` (JSON estático, CC0), `CurrencyConverter` (Python offline, Apache-2.0), `AllRatesToday` starters (MIT), datasets de bancos centrais via jsDelivr, ECB Data Portal (SDMX).
   - **Fallback mandatório:** API PTAX do Banco Central do Brasil (`https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/`). Acionada obrigatoriamente para validação cruzada ou em caso de falha das fontes globais, garantindo conformidade com a realidade fiscal brasileira.
5. **Padrões de código:** Adapter Pattern na integração com APIs; cache com TTL no PostgreSQL para reduzir ≥ 50% das chamadas externas; type hints obrigatórios; docstrings padrão Google; coverage ≥ 80%.
6. **Flexibilidade FOSS controlada:** autorizada adoção de bibliotecas adicionais desde que: (a) licença OSI-approved; (b) auditáveis; (c) provenham de PyPI oficial/Docker Hub Official; (d) não violem orçamento zero; (e) sejam registradas em `docs/dependencias/registro.md`.

## Consequências

- Positivas: realismo de produção; tipagem estrita eliminando bugs siliciosos; paridade ambiental via containers; resiliência cambial multi-fonte com âncora brasileira; valor acadêmico acrescido.
- Negativas: overhead inicial de setup (Dockerfile, docker-compose.yml, alembic init); consumo adicional de RAM (~2–3GB para PostgreSQL containerizado, mitigado por 58GB totais); complexidade ligeiramente maior no CI (container efêmero PostgreSQL).
- Neutras: SQLite permanece como dependência transitiva possível (testes unitários isolados podem usar sqlite:///memory:), mas não é mais o banco canônico de persistência.

## Trade-offs Declarados

| Aspecto | Ganho | Perda/Risco | Mitigação |
|---|---|---|---|
| PostgreSQL > SQLite | Robustez, tipagem, concorrência | Overhead de infra | 58GB RAM comportam containers sem impacto perceptível |
| Docker Compose | Paridade ambiental | Complexidade de build | Makefile/scripts helper; documentação clara no README |
| Nginx latente | Pronto para produção futura | Serviço extra no compose | Perfil opcional no docker-compose; desativável por default |
| Circuit Breaker multi-API | Resiliência + conformidade BR | Complexidade de teste | Mocks determinísticos em testes; integration tests com fixtures locais |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo | Domínio PMBOK 7ª | Data |
|---|---|---|---|---|
| ADR-001 | Parcial | Substituição de SQLite por PostgreSQL; adição de Docker/Nginx; definição de hierarquia de APIs de câmbio | Abordagem de Desenvolvimento | 29/10/2026 |

## kill_switch

Se a migração para PostgreSQL causar regressão funcional não corrigível em ≤ 48h, ou se o consumo de recursos do Docker comprometer seriamente a inferência local (< 12 t/s sustentados), acionar rollback parcial: manter lógica de negócio desacoplada via Repository Pattern, permitindo troca transparente entre PostgreSQL e SQLite (esta última apenas como emergência temporária, nunca como estado final).

## Governança

- **Custódia:** `agent-backend-dev` (Fabricio) + `agent-devops` (Leonardo).
- **Emenda:** mudança de componente de infra exige ADR específica + CCB humano.
- **Auditoria:** `docs/dependencias/registro.md` deve listar todas as imagens Docker, versões exatas, licenças e URLs de origem.
- **CI:** pipeline GitHub Actions roda em container PostgreSQL efêmero (`services: postgres`) para garantir reprodutibilidade.


---


<!-- ===== docs/decisoes/adr-011-ecossistema-sddai.md ===== -->

# ADR-011 — Ecossistema de Inteligência SDD: MCPs, Memória Persistente e Separação Ortogonal L1/L2/L3

| Campo | Valor |
|---|---|
| **Versão** | 1.0.0 |
| **Status** | Aprovado (ratificado pelo CCB-001 em 29/10/2026) |
| **Data da decisão** | 29/10/2026 |
| **Data de formalização do documento** | 29/10/2026 |
| **Decisor** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| **Gatilhos G1–G4** | G1 (impacto transversal — todos os agentes SDD, workflow de handoffs, specs, personas e roteamento), G2 (irreversibilidade prática — implementação de MCPs e ledger redefine arquitetura de memória do circuito), G3 (questionabilidade acadêmica — "por que não usar LangChain/AutoGen?"), G4 (trade-off não óbvio — determinismo e auditabilidade × velocidade de prototipagem com frameworks prontos) |
| **Rastreabilidade** | TAP §3 (Inovação) + §9 (Premissa P3 — stack local auditável); EAP N1.4, N4.4, N9.1; REQ-13 (prompts catalogados); ADRs correlatas: ADR-001 (stack FOSS), ADR-006 (modelo primário/fallback, sobreposta parcialmente), ADR-010 (infraestrutura, complementar); archtecture_report_Local_SDDAI.md; constitution.md v1.2.0 Art. 4.9, 4.10, 6.5, 6.6, 6.7 |
| **Domínio PMBOK 7ª** | Trabalho do Projeto + Abordagem de Desenvolvimento + Incerteza |
| **Processo PMBOK 6ª (dicionário)** | 4.3 Orientar e Gerenciar o Trabalho do Projeto; 4.6 Integrar Mudanças |

## Contexto

O ecossistema SDD do COGME utiliza Qwen3-30B-A3B MoE via llama.cpp e OpenCode como interface. Na configuração inicial, o circuito operava de forma stateless: cada interação começava do zero, sem memória persistente entre sessões, sem protocolo formal de handoffs estruturados além de arquivos JSON soltos, e sem separação clara entre camadas de responsabilidade.

Isso gerou problemas concretos:

1. **Perda de contexto:** informações cruciais (decisões anteriores, blockers, lições aprendidas) eram perdidas entre sessões, forçando reprocessamento redundante.
2. **Falta de auditabilidade:** não havia registro sistemático de quem fez o quê, quando e por quê, dificultando rastreamento de defeitos até prompts específicos.
3. **Acoplamento indevido:** modificações em infraestrutura (troca de modelo) impactavam diretamente metodologia (specs, handoffs), violando princípio de separação de responsabilidades.
4. **Ausência de guardrails:** sem validação automática de schemas e estados, erros humanos ou alucinações do modelo passavam despercebidos até fases tardias.

Frameworks existentes (LangChain, AutoGen, CrewAI) ofereceriam soluções rápidas, mas introduziriam dependências pesadas, black boxes opacas e potencial violação de soberania de dados (telemetria embutida, calls para serviços externos não autorizados).

## Opções Consideradas

| # | Opção | Prós | Contras |
|---|---|---|---|
| O1 | Manter estadoless puro | Simplicidade máxima; zero overhead | Perda constante de contexto; baixa auditabilidade; retrabalho elevado |
| O2 | Adotar framework externo (LangChain/AutoGen) | Rapidez de implementação; comunidade ativa | Dependências pesadas; opacidade; risco de telemetria/lock-in; viola P-02/P-03 absolutistas |
| O3 | Construir camada própria de memória persistente + MCPs customizados + separação L1/L2/L3 | Determinismo total; auditabilidade completa; soberania preservada; leveza (Python stdlib + PyYAML) | Esforço inicial de implementação; necessidade de disciplina de manutenção |

## Decisão

**Aprovar a opção O3.**

### 3.1. Separação Ortogonal de Camadas (L1 / L2 / L3)

| Camada | Responsabilidade | Artefatos | Frequência de Mudança | Autoridade do Agente |
|---|---|---|---|---|
| **L1 — Infraestrutura** | Motor de inferência e hardware | `llama.cpp`, Vulkan/radv, systemd service, modelos GGUF, `opencode.json`, imagens Docker base | Raramente (semestral/anual) | ❌ Não modifica. Reporta blocker. |
| **L2 — Personas** | Comportamento do modelo via contexto | `.ai/personas/*.md` (`_base.md`, `pm.md`, `coder.md`, `reviewer.md`, `tester.md`, `all.md`), symlink `active.md` | Por agente ou papel | ✅ Lê e segue a persona ativa. Pode propor updates via PR. |
| **L3 — Metodologia** | Organização do trabalho e validação | `.ai/specs/*`, `.ai/handoffs/task-ta-*.json`, `.ai/agents/ledger.yaml`, ADRs, planos, lições aprendidas | Por tarefa/ciclo | ✅ Interage, lê e atualiza. Única camada mutável diariamente. |

**Regra de ouro:** mudanças em uma camada **NÃO** exigem mudanças em outras. Violação desta regra aciona kill switch operacional.

### 3.2. Protocolo de Memória Persistente

O estado do sistema é gerido exclusivamente via:

- **`ledger.yaml`** (`.ai/agents/ledger.yaml`): SSOT para `current_session`, `audit_trail`, `blocked_tasks`, `last_updated`, `context_budget_tokens` (24.000), `context_used_tokens`. Schema v2.0 obrigatório. Modificação somente por script ou MCP validado.
- **Handoffs estruturados** (`.ai/handoffs/task-ta-*.json`): envelope JSON contendo `task_id`, `from_agent`, `to_agent`, `payload`, `timestamp`, `parent_task_id`. Parseados por `handoff_parser.py` ou MCP equivalente.
- **Specs imutáveis** (`.ai/specs/*.md`): `tap.md`, `eap.md`, `requisitos.md`, `input-canonico-v4.1.1.md`. Once written, never modified without new version file.
- **Lições aprendidas acumulativas**: `MF1-licoes.md`, `MF2-licoes.md`, `MF3-licoes.md`, `transversais.md`. Formato markdown padronizado.

### 3.3. MCPs Customizados (Model Context Protocol)

Quatro servidores MCP implementados em Python puro (stdlib + PyYAML como única dependência externa permitida):

| MCP | Script | Função |
|---|---|---|
| `nexus-ledger` | `scripts/mcp_nexus_ledger.py` | Leitura/escrita estruturada do `ledger.yaml` com validação de schema e operações idempotentes |
| `nexus-dispatch` | `scripts/mcp_nexus_dispatch.py` | Despacho de envelopes de tarefa entre personas, respeitando topologia AGENT_TOPOLOGY e proibindo auto-delegação |
| `nexus-validate` | `scripts/mcp_nexus_validate.py` | Validação de schemas (frontmatter YAML de agentes, handoffs JSON, specs markdown) e registros de conformidade |
| `nexus-kb` | `scripts/mcp_nexus_kb.py` | Consulta indexada à OKB, Glossário e lições aprendidas via grep estruturado ou índice invertido leve |

**Requisitos técnicos dos MCPs:**
- Python preferencialmente com biblioteca padrão;
- Se usar YAML, empregar PyYAML (MIT) registrado em `requirements.txt` como dependência de desenvolvimento;
- Sem framework de orquestração externa obrigatório;
- Parsing determinístico;
- Operações idempotentes;
- Registro de auditoria em `audit_trail` do ledger;
- Bloqueio fail-closed em estado inconsistente.

### 3.4. Regras Operacionais da Camada `.ai/`

- **Regra de Ouro:** "Se não é lido pelo OpenCode, por MCP ou por script canônico, não pertence ao diretório `.ai/`."
- **Limite máximo:** 10 arquivos por diretório em `.ai/` (exceto `.ai/handoffs/`, que é append-only e deve ter índice `INDEX.md` e arquivamento trimestral de handoffs > 90 dias).
- **Revisão trimestral:** deletar ou arquivar arquivos não usados há > 90 dias.
- **Nenhum framework externo pesado:** apenas Markdown puro + scripts Shell/Python leves.
- **SSOT absoluto:** um fato = um local, nunca duplicar.

### 3.5. Integração com OpenCode

Atualizar `.opencode/opencode.json` para registrar `mcpServers`, apontando para os quatro scripts acima. Não alterar modelo, contexto ou permissões além do necessário.

## Consequências

- Positivas: determinismo total; auditabilidade ponta a ponta (cada ação registrada no ledger); soberania preservada (zero telemetria externa); leveza (sem frameworks pesados); separação clara de responsabilidades facilitando manutenção e sucessão.
- Negativas: esforço inicial de implementação (~8–12h estimadas para MCPs básicos + ledger + specs); necessidade de disciplina rígida de manutenção (revisão trimestral, limite de arquivos); curva de aprendizado para novos membros da equipe entenderem o protocolo.
- Neutras: compatibilidade retroativa limitada — handoffs antigos (22 arquivos JSON já existentes) precisam ser migrados para o novo schema ou arquivados como legado.

## Trade-offs Declarados

| Aspecto | Ganho | Perda/Risco | Mitigação |
|---|---|---|---|
| MCPs próprios vs. frameworks | Controle total; soberania; leveza | Velocidade de entrega inicial menor | Foco em MVP funcional dos 4 MCPs essenciais; expandir gradualmente |
| Ledger como SSOT de estado | Auditabilidade perfeita | Ponto único de falha se corrompido | Backups periódicos do ledger; validação schema em cada escrita; fail-closed |
| Limite de 10 arquivos/diretório | Força consolidação; evita dispersão | Pode exigir arquivamento frequente em `.ai/handoffs/` | Índices automáticos (`INDEX.md`); política de rolagem trimestral clara |
| Separação L1/L2/L3 | Modularidade; independência de evolução | Rigidez percebida inicialmente | Documentação clara; exemplos práticos de como cada camada evolui isoladamente |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo | Domínio PMBOK 7ª | Data |
|---|---|---|---|---|
| ADR-006 | Parcial | Adição de MCPs, memória persistente, separação L1/L2/L3 e refinamento do roteamento de agentes | Trabalho do Projeto | 29/10/2026 |
| ADR-001 | Parcial | Especificação de contexto (32k configurado, 24k efetivo), reconciliação de scripts, perfis de hardware/modelo via YAML | Abordagem de Desenvolvimento | 29/10/2026 |

## kill_switch

Abortar imediatamente e retornar Parcel com `kill_switch_invoked: true` se:
1. Detecção de corrupção ou inconsistência do `ledger.yaml` (schema inválido, campos obrigatórios faltantes, conflito com handoffs processados);
2. Tentativa de um agente da camada L3 modificar arquivos da camada L1 sem passar pelo protocolo MCP adequado;
3. Tentativa de auto-delegação (agente despachando tarefa para si mesmo, violando princípio half-duplex);
4. Criação de arquivo órfão em `.ai/` que não seja lido por OpenCode, MCP ou script canônico;
5. Exceder limite de 10 arquivos por diretório em `.ai/` sem índice ou arquivamento canônico;
6. Envio de dados sensíveis para cloud não autorizada durante operação de MCP.

Ao abortar: registrar em `audit_trail` do ledger e marcar `ccb_action_required: true`.

## Governança

- **Custódia:** `agent-nexus-prime-ultimate` (L0 orquestrador) + `agent-architect` (guardião da separação L1/L2/L3).
- **Emenda:** mudança na arquitetura de memória ou adicion/remoção de MCP exige ADR específica + CCB humano.
- **Auditoria:** `project-auditor` verifica integridade do ledger, conformidade dos handoffs e ausência de arquivos órfãos em `.ai/` a cada semana.
- **Sucessão:** `.ai/agents/registry.yaml` + `constitution.md` + ADRs bastam para reconstruir contexto completo do circuito SDD.


---


<!-- ===== docs/decisoes/adr-012-constituicao-como-artefato-de-governanca.md ===== -->

# ADR-012 — Constituição como Artefato Normativo Supremo e Mecanismo de Restauração Constitucional

| Campo                                         | Valor                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Versão**                             | 1.0.1                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Status**                              | Aprovado (ratificado pelo CCB-002 em 29/10/2026)                                                                                                                                                                                                                                                                                                                                                                         |
| **Data da decisão**                    | 29/10/2026                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Data de formalização do documento** | 29/10/2026                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Decisor**                             | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7)                                                                                                                                                                                                                                                                                                                                                                    |
| **Gatilhos G1–G4**                     | G1 (impacto transversal — define a validade de TODOS os outros artefatos), G2 (irreversibilidade prática — corrupção ou perda da Constituição invalida o ecossistema inteiro), G3 (questionabilidade acadêmica — "por que uma Constituição separada do Plano de Gerenciamento?"), G4 (trade-off não óbvio — rigidez normativa × segurança contra deriva algorítmica)                                    |
| **Rastreabilidade**                     | TAP §1 (Identidade) + §2 (Restrições Éticas/Legais); EAP N1.1 (Definição do Projeto); REQ-12 (ADRs); ADRs correlatas: ADR-005 (fundamenta o freeze do TAP, mas a Constituição está ACIMA dele), ADR-008 (grafia canônica blindada constitucionalmente), ADR-011 (MCPs e L1/L2/L3 subordinados à Constituição); CCB-001 e CCB-002 (instrumentos de ratificação); Monografia Cap. 3 (Governança Híbrida) |
| **Domínio PMBOK 7ª**                  | Integração + Trabalho do Projeto + Incerteza                                                                                                                                                                                                                                                                                                                                                                           |
| **Processo PMBOK 6ª (dicionário)**    | 4.1 Desenvolver Plano de Gerenciamento do Projeto; 4.6 Realizar Mudanças Integradas; 13.2 Gerenciar Engajamento das Partes Interessadas                                                                                                                                                                                                                                                                                 |

## Contexto

O projeto COGME opera sob uma dualidade complexa: é simultaneamente um produto de software (conversor cambial FOSS) e um laboratório experimental de engenharia assistida por IA (SDD com agentes autônomos locais). Nessa configuração, surgiram riscos críticos de **deriva normativa**:

1. **Fragmentação de Autoridade:** Inicialmente, tentou-se gerir a governança exclusivamente via TAP e Planos. Contudo, a chegada de modelos generativos exigiu regras mais estritas sobre soberania de dados, precisão linguística e limites éticos que transcendem o escopo técnico tradicional.
2. **Corrupção Institucional Detectada:** Em rodadas anteriores, identificou-se que a `constitution.md` v1.1.0 sofreu degradação semântica e estrutural (contradições internas, referências obsoletas, ausência de reconhecimento de MCPs/Docker), tornando-a inviável como fonte única de verdade. Isso evidenciou a fragilidade de confiar a integridade sistêmica a um arquivo passível de edição acidental ou maliciosa sem salvaguardas robustas.
3. **Subordinação de Inputs Canônicos:** Modelos locais tendem a tratar prompts extensos ("inputs canônicos") como normas supremas se não houver uma barreira clara estabelecendo que tais prompts são meramente derivativos. Sem essa distinção constitucional explícita, há risco de alucinação normativa onde o agente inventa regras baseadas em contexto temporário.

A situação exigia a elevação da `constitution.md` ao patamar de **Lei Suprema Imutável Exceto Por Emenda Formal**, dotada de mecanismos próprios de detecção de corrupção e restauração integral, distinta dos planos executáveis e das especificações técnicas.

## Opções Consideradas

| #  | Opção                                                                                | Prós                                                                                                                                                                  | Contras                                                                                                                                                                                             |
| -- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| O1 | Manter governança integrada no TAP e Planos                                           | Simplicidade aparente; menos arquivos                                                                                                                                  | Mistura matéria autorizativa (TAP) com operacional (Planos) e ética/normativa (Constituição); difícil de auditar separadamente; vulnerável a edições indevidas de escopo durante execução |
| O2 | Criar uma "Cartilha de Agentes" separada da Constituição                             | Foca na interação humana-agente                                                                                                                                      | Deixa lacuna jurídica para o produto em si; cria duas fontes de verdade concorrentes; ignora requisitos legais (LGPD) e éticos universais                                                         |
| O3 | Elevar `constitution.md` a Artefato Normativo Supremo com protocolo de restauração | Clareza hierárquica absoluta; proteção contra deriva; mecanismo robusto de recuperação de desastres normativos; subordinação clara de todos os demais artefatos | Rigidez inicial; exige disciplina rigorosa de versionamento e hashing; overhead de manutenção da integridade textual                                                                              |

## Decisão

**Aprovar a opção O3.**

Fica instituída a **ADR-012**, declarando a `constitution.md` como o ápice incontestável da hierarquia normativa do COGME, regida pelos seguintes princípios fundamentais:

### 1. Supremacia e Imutabilidade Condicional

A Constituição prevalece sobre qualquer outro artefato (TAP, ADRs, OKB, Planos, Specs, Código). Nenhuma ADR, CR ou Input Canônico pode contradizê-la. Alterações somente ocorrem via **Emenda Constitucional** aprovada pelo CCB humano (GP Leonardo), seguida de bump de versão (`MAJOR.MINOR.PATCH`) e registro de co-assinatura com hash SHA-256 do conteúdo normativo (excluindo o bloco de assinatura para evitar autorreferência).

### 2. Hierarquia Trifásica Explícita

Para eliminar ambiguidades, a Constituição estabelece duas vertentes de autoridade distintas, porém complementares:

* **Hierarquia de Projeto (Matéria de Negócio/Escopo):**
  `Constitution` > `TAP v3 (Congelado)` > `ADRs Técnicas` > `OKB` > `Planos` > `Glossário` > `Inputs Canônicos` > `Código`.
* **Hierarquia de Forja (Matéria de Agentes/SDD):**
  `Constitution` > `Diretiva AFA-ULTIMATE` > `Roster de Agentes` > `Personas/MCPs` > `Scripts`.

Esta separação garante que decisões de escopo (ex.: adicionar feature X) sigam o fluxo TAP→EAP→Card, enquanto decisões de comportamento do modelo (ex.: alterar persona Y) sigam o fluxo AFA→Registry→Persona, ambas ancoradas na mesma lei suprema.

### 3. Subordinação Rígida de Inputs Canônicos e Prompts

Qualquer prompt de sistema, input consolidado, memória ubíqua ou handoff JSON é classificado como **artefato derivativo**. Ele operacionaliza a vontade expressa na Constituição, mas não cria norma autônoma. Em caso de conflito interpretativo entre um input longo e um artigo constitucional curto, prevalece sempre o artigo constitucional. Os agentes devem ser programados para rejeitar instruções implícitas em contextos que violem artigos explícitos da Constituição (ex.: envio de dados sensíveis para cloud não whitelistada).

### 4. Protocolo de Detecção e Restauração de Corrupção

Diante do histórico de degradação do arquivo, institui-se o **Protocolo de Integridade Constitucional**:

* **Hash de Referência:** Cada versão promulgada possui um hash SHA-256 calculado sobre o corpo normativo (sem metadados variáveis como timestamps de edição recentes).
* **Backup Forense Automático:** Antes de qualquer modificação proposta pelo circuito SDD, a versão vigente deve ser copiada para `docs/archive/corrupted/` ou `docs/archive/history/`, garantindo rastreabilidade reversa.
* **Restauração Integral:** Se for detectada inconsistência lógica, truncamento ou violação de hierarquia na `constitution.md` ativa, o processo de correção não é via "patch", mas via **restauração completa** a partir da última versão validada e assinada pelo CCB. Isso elimina o risco de fusões semânticas errôneas.
* **Kill Switch Constitucional:** Qualquer tentativa de modificar a Constituição fora do fluxo de Emenda Formal (Art. 9 da própria Constituição) dispara abortamento imediato das operações do circuito SDD e escalonamento obrigatório ao CCB humano.

### 5. Relação com AFA-ULTIMATE e CCB

* **AFA-ULTIMATE:** Atua como executor técnico da governança, validando contratos de agentes e roteamento, mas está estritamente subordinado à Constituição. Não tem poder legislativo próprio.
* **CCB (Comitê de Controle de Mudanças):** Representado exclusivamente pelo GP Leonardo, detém o monopólio da interpretação final e da aprovação de emendas. Agentes podem sugerir emendas, mas jamais aprová-las autonomamente.

## Consequências

- Positivas: Eliminação definitiva de dúvidas sobre qual artefato manda em caso de conflito; proteção robusta contra alucinações normativas dos LLMs; capacidade de recuperação rápida após incidentes de corrupção documental; alinhamento perfeito entre exigências acadêmicas (formalidade) e necessidades práticas (agilidade controlada).
- Negativas: Aumento da burocracia para mudanças radicais (embora necessário); necessidade de ferramentas auxiliares (scripts de hash/validation) para manter a integridade; curva de aprendizado para novos membros entenderem a diferença entre "alterar plano" e "emendar constituição".
- Neutras: A Constituição torna-se o ponto focal de auditorias externas e avaliações do Prof. Dr. Nivaldo Carleto, simplificando a demonstração de maturidade de gestão.

## Trade-offs Declarados

| Aspecto                              | Ganho                                   | Perda/Risco                                   | Mitigação                                                                    |
| ------------------------------------ | --------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------ |
| Supremacia Absoluta                  | Segurança jurídica e técnica máxima | Rigidez percebida                             | Cláusulas de exceção claras (Bypass Protocol) já previstas nos Arts. 3 e 7 |
| Restauração Integral vs. Patch     | Coerência total pós-recuperação     | Perda de nuances de edições intermediárias | Backups forenses detalhados preservam histórico completo                      |
| Separação Hierarquia Projeto/Forja | Clareza epistemológica                 | Complexidade cognitiva inicial                | Diagramas de fluxo e exemplos práticos no OKB v3.3+                           |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo                                                                                                                                                                                                                                                   | Domínio PMBOK 7ª | Data       |
| -------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------- |
| —             | —       | Esta ADR não sobrepõe outra diretamente; ela **consolida e institucionaliza** os princípios dispersos nas ADRs 001, 005, 008 e 011, elevando-os a status constitucional. Reforça a ADR-005 ao colocar a Constituição acima do TAP congelado. | Integração       | 29/10/2026 |

> **Nota Crítica:** Embora não haja sobreposição direta de texto, esta ADR resolve implicitamente contradições potenciais entre a liberdade de ação dos agentes (ADR-006/011) e as restrições éticas/legais (TAP/Constituição), deixando claro que a restrição constitucional vence a eficiência agêntica.

## kill_switch

Ativado automaticamente se:

1. For detectada alteração manual ou automática na `constitution.md` sem o devido commit de Emenda aprovado pelo CCB.
2. O hash SHA-256 do conteúdo normativo divergir do valor registrado na última co-assinatura válida, sem justificativa de emenda pendente.
3. Um agente tentar executar uma instrução presente em um Input Canônico que contradiga explicitamente um artigo da Constituição (ex.: pedir para ignorar LGPD).
4. Falha na verificação de integridade durante o boot do circuito SDD.

Ao disparar, o sistema entra em estado `BLOCKED_CONSTITUTIONAL_INTEGRITY`, exigindo intervenção humana imediata para restauração ou validação da emenda.

## Governança

- **Custódia:** GP Leonardo (Guardião da Constituição).
- **Validação Técnica:** Script `validate_constitution_integrity.py` roda em CI e pré-commit.
- **Auditoria:** `project-auditor` gera relatório mensal de conformidade constitucional.
- **Sucessão:** Em caso de indisponibilidade do Guardião, a posse da chave privada de assinatura ou acesso ao repositório protegido determina a legitimidade das emendas futuras. Atualmente, apenas o CCB Único possui essa prerrogativa.



---



<!-- ===== docs/decisoes/adr-013-regime-emenda-tap.md ===== -->



# ADR-013 — Regime de Emenda Controlada do TAP (Baseline Vivo) — SUPERSSEDIDA

**Esta ADR está SUPERSSEDIDA.** Foi incorporada integralmente na **ADR-005 v1.1.0** (Regime do TAP: Freeze + Emenda Controlada) conforme decisão do GP em 31/10/2026 (RAT-2026-10-31-A12). Não deve ser usada como referência normativa vigente. Consulte `docs/decisoes/adr-005-regime-tap.md` (versão 1.1.0) para o conteúdo vigente.

---
id: ADR-013
title: Regime de Emenda Controlada do TAP (Baseline Vivo)
version: 1.0.0
status: superseded by ADR-005 v1.1.0
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

Qualquer ajuste pontual no TAP deve ser registrado em `docs/tap/delta-v3-1.md` com a seguinte estrutura:

| Campo Alterado | Valor Anterior | Valor Novo | Justificativa (ADR/CR) | Data |
|---|---|---|---|---|
| REQ-07 (Cache) | SQLite | PostgreSQL 15+ | Alinhamento à ADR-010 (Stack Infra) | 2026-11-01 |

## Consequências

- **Ganho:** Flexibilidade documental para corrigir drifts de stack e requisitos sem violar a ontologia do projeto.
- **Risco:** Perda da imutabilidade absoluta do termo autorizativo.
- **Mitigação:** O núcleo do TAP permanece blindado; alterações são auditáveis via Delta Log e exigem aprovação do CCB (GP).

## Ratificação

Ratificada via CCB-LOG-2026-11-01-A08. A ADR-005 permanece vigente para todos os aspectos não explicitamente revogados por esta ADR-013.



---



<!-- ===== ADR-013-SDDAI-Promulgacao.md ===== -->



# ADR-014 — Promulgação dos Agentes SDDAI e Resolução de Gaps de Compliance (Art. 4.1, 4.7, P-06) — SUPERSSEDIDA

**Esta ADR está SUPERSSEDIDA.** Foi incorporada integralmente na **ADR-006 v2.1.0** (Ecossistema SDDAI: Modelo, Agentes, MCPs e Separação L1/L2/L3) conforme decisão do GP em 31/10/2026 (RAT-2026-10-31-A12). Não deve ser usada como referência normativa vigente. Consulte `docs/decisoes/adr-006-ecossistema-sddai.md` (versão 2.1.0) para o conteúdo vigente.

---
# ADR-014 — Promulgação dos Agentes SDDAI e Resolução de Gaps de Compliance (Art. 4.1, 4.7, P-06)

| Campo | Valor |
|---|---|
| **Versão** | 1.0.1 |
| **Status** | Supersedida por ADR-006 v2.1.0 |
| **Data da decisão** | 31/10/2026 |
| **Data de formalização do documento** | 31/10/2026 |
| **Decisor** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) + NEXUS-PRIME ULTIMATE (L0 Orquestrador) |
| **Gatilhos G1–G4** | G1 (impacto transversal — todos os agentes SDDAI, pipeline data_optimization, CI workflow), G2 (irreversibilidade prática — agentes promovidos ao roster SSOT alteram topologia de despacho), G3 (questionabilidade acadêmica — "por que forjar agentes SDDAI via L0 ao invés de AFA-ULTIMATE canônico?"), G4 (trade-off não óbvio — autonomia do ecossistema autorizada pelo Humano vs. rigidez do forjador único canônico) |
| **Rastreabilidade** | TAP §3 (Inovação) + §9 (Premissa P3 — stack local auditável); EAP N1.4, N4.4; REQ-13 (prompts catalogados); ADRs correlatas: ADR-001 (stack FOSS), ADR-006 (modelo primário/fallback), ADR-011 (Ecossistema SDD: MCPs, memória persistente, separação L1/L2/L3); constitution.md v1.2.0 Art. 4.1, 4.3, 4.6, 4.7, 4.10, 6.5, 6.7, P-01..P-12 |
| **Domínio PMBOK 7ª** | Trabalho do Projeto + Abordagem de Desenvolvimento + Incerteza |
| **Processo PMBOK 6ª (dicionário)** | 4.3 Orientar e Gerenciar o Trabalho do Projeto; 4.6 Integrar Mudanças |
---
| **Gatilhos G1–G4** | G1 (impacto transversal — 5 novos agentes L2 no roster, pipeline data_optimization, CI workflow), G2 (irreversibilidade prática — agentes promovidos ao roster SSOT alteram topologia de despacho), G3 (questionabilidade acadêmica — "por que forjar agentes SDDAI via L0 ao invés de AFA-ULTIMATE canônico?"), G4 (trade-off não óbvio — autonomia do ecossistema autorizada pelo Humano vs. rigidez do forjador único canônico) |
| **Rastreabilidade** | TAP §3 (Inovação) + §9 (Premissa P3 — stack local auditável); EAP N1.4, N4.4; REQ-13 (prompts catalogados); ADRs correlatas: ADR-001 (stack FOSS), ADR-006 (modelo primário/fallback), ADR-011 (Ecossistema SDD: MCPs, memória persistente, separação L1/L2/L3); constitution.md v1.2.0 Art. 4.1, 4.3, 4.6, 4.7, 4.10, 6.5, 6.7, P-01..P-12 |
| **Domínio PMBOK 7ª** | Trabalho do Projeto + Abordagem de Desenvolvimento + Incerteza |
| **Processo PMBOK 6ª (dicionário)** | 4.3 Orientar e Gerenciar o Trabalho do Projeto; 4.6 Integrar Mudanças |

## Contexto

Na rodada de implementação SDDAI (31/10/2026), foram forjados 5 agentes L2 (`agent-sddai-loader`, `agent-sddai-engineer`, `agent-sddai-trainer`, `agent-sddai-memory`, `agent-sddai-cli`) sob autorização explícita do Humano ("autonomia total de ação"). Esses agentes:

- Residem em `.opencode/agents/` com frontmatter YAML válido (Art. 4.2, 4.3)
- Estão registrados no `registry.yaml` SSOT (Art. 4.4) via `sync_agent_registry.py --check`
- Fazem parte da topologia DAG AGENT_TOPOLOGY (camada L2) sem ciclos
- Declaram `kill_switch: inherited` (Art. 4.6)
- São 100% FOSS/stdlib, CPU-only, sem CUDA/cloud (P-01, P-02)
- Estão integrados ao pipeline `sddai_verify_pipeline.py` (7/7 passos aprovados)

Porém, a auditoria AUD-2610-05 identificou 3 gaps de compliance:

| Gap | Artigo | Descrição | Severidade |
|-----|--------|-----------|------------|
| **G-01** | Art. 4.7 | Gate de forja (`validate_afa_output.py`) não executado; score < 85/100; seções §2-§16 ausentes; contagens quantitativas zeradas | Alta |
| **G-02** | Art. 3 / P-06 | Ausência de testes dedicados para componentes `cogme_sddai-*`; cobertura não mensurada | Média |
| **G-03** | Art. 4.1 | Forjamento executado por L0 (`agent-nexus-prime-ultimate`) ao invés de AFA-ULTIMATE canônico; tensão com forjador único | Média |

## Opções Consideradas

| # | Opção | Prós | Contras |
|---|---|---|---|
| O1 | Manter agentes como estão (sem gate, sem testes, sem ratificação) | Zero esforço adicional | Não conformes com Art. 4.7 e P-06; não podem ser considerados promulgados formalmente; risco de rejeição em auditoria subsequente |
| O2 | Submeter todos os 5 agentes para re-forja por AFA-ULTIMATE canônico | Conformidade estrita com Art. 4.1 | AFA-ULTIMATE não está disponível como executável autônomo neste ecossistema; atrasa a entrega; contradiz autorização do Humano de autonomia total |
| O3 | Criar o ADR (numerado **ADR-014** nesta formalização; lançado como "ADR-013" na redação original de 31/10) ratificando o forjamento L0 sob autorização Humana, reescrever agentes com 16 seções canônicas para passar o gate, criar testes dedicados, executar gate e co-assinar | Resolve os 3 gaps; mantém autonomia autorizada; conformidade total com Constituição; rastreabilidade completa | Esforço de reescrita dos agentes e criação de testes |

## Decisão

**Aprovar a opção O3.**

### 3.1. Resolução do G-03 — Forjador e Ratificação

O Humano (Gerente de Projeto / CCB) autorizou expressamente "autonomia total de ação" neste ecossistema. Conforme Constitution Art. 5.1, o Humano é o decisor único via CCB. Esta ADR registra a ratificação humana do forjamento dos 5 agentes SDDAI por `agent-nexus-prime-ultimate` (L0), reconhecendo que a autonomia do ecossistema autorizada pelo Humano prevalece sobre a rigidez do forjador único em casos de exceção documentada e ratificada.

A partir desta ADR, os 5 agentes SDDAI são considerados **promulgados com co-assinatura humana** (Constitution Art. 5.4).

### 3.2. Resolução do G-01 — Gate de Forja (Art. 4.7)

Todos os 5 agentes SDDAI serão reescritos com a estrutura canônica de 16 seções (§0-§16) do template AFA-ULTIMATE, contendo:
- Kill Switch: ≥5 itens
- DOs: ≥15 itens
- DON'Ts: ≥15 itens
- Métricas: ≥8 itens
- Red Team: ≥8 itens
- FAIL-CLOSED: ≥6 itens
- Todas as seções §0-§16 presentes
- Orçamento de tokens ≤ 4000 (heurística: < 16000 caracteres)

Após a reescrita, `validate_afa_output.py` será executado para confirmar score ≥ 85/100 e status "aceito".

### 3.3. Resolução do G-02 — Testes Dedicados (P-06)

Serão criados testes unitários em `tests/agents/test_sddai_*.py` para cada componente `cogme_sddai-*`, cobrindo:
- Loader: ingestão, checksum, validação de entrada
- Memory: otimização, leitura de /proc/meminfo, garbage collection
- Engineer: transformação, features, checksum
- Trainer: treinamento determinístico, métricas, artifact
- CLI: orquestração do pipeline, falha em estágio, saída consolidada

Os testes serão integrados ao `sddai_verify_pipeline.py` (Passo 7).

## Consequências

- **Positivas:** Conformidade total com Constituição COGME (Art. 4.1, 4.3, 4.6, 4.7, P-01 a P-12); agentes plenamente promulgados; rastreabilidade via ledger e ADR; pipeline de verificação funcional; testes automatizados; co-assinatura humana registrada.
- **Negativas:** Esforço de reescrita dos 5 agentes e criação de testes; necessidade de manutenção dos testes à medida que os componentes evoluem.
- **Neutras:** Nenhuma alteração nas camadas L1 (infraestrutura) ou L2 (personas) — SDDAI opera exclusivamente em L3 (metodologia).

## Trade-offs Declarados

| Aspecto | Ganho | Perda/Risco | Mitigação |
|-------|-------|-------------|-----------|
| ADR-014 + co-assinatura | Conformidade formal com Art. 4.1; ratificação humana | Dependência de decisão Humana | Documentação clara da autorização prévia ("autonomia total de ação") |
| Reescrita dos agentes | Passagem no gate de forja (score ≥ 85) | Esforço de reescrita; risco de erro na reescrita | Execução de `validate_afa_output.py` após cada alteração |
| Testes dedicados | Cobertura mensurada (P-06) | Manutenção contínua de testes | Integração ao pipeline de verificação existente |

## kill_switch

Abortar imediatamente se:
1. Qualquer agente SDDAI falhar no `validate_afa_output.py` (score < 85 ou seção ausente)
2. Qualquer teste SDDAI falhar no pipeline de verificação
3. Tentativa de modificar agentes SDDAI sem atualizar o ledger e re-executar o gate
4. Desvio da separação L1/L2/L3 (tentativa de agente SDDAI tocar arquivos L1)

Ao abortar: registrar em `audit_trail` do ledger e marcar `ccb_action_required: true`.

## Governança

- **Custódia:** `agent-nexus-prime-ultimate` (L0 orquestrador) + `agent-architect` (guardião da separação L1/L2/L3)
- **Emenda:** mudança nos agentes SDDAI exige re-execução do gate de forja + atualização do ADR + CCB humano
- **Auditoria:** `project-auditor` verifica conformidade dos agentes SDDAI a cada milestone
- **Sucessão:** `registry.yaml` + `constitution.md` + ADR-014 bastam para reconstruir contexto

**Nota de renumeração (OKB-C-26 — RAT-2026-10-31-A12):** este artefato foi emitido com o identificador "ADR-013" (colisão com a ADR de Regime de Emenda do TAP); renumerado para **ADR-014** por decisão do CCB de 31/10/2026. Versão 1.0.0 preservada como histórico; conteúdo normativo re-hasheado na linha 1.0.1 da tabela de co-assinatura.



---

## CO-ASSINATURA (Constitution Art. 5.4)

| Versão | SHA-256 do conteúdo normativo | Commit Git | Data | Papel do ratificador humano | Instrumento |
|--------|------------------------------|------------|------|----------------------------|-------------|
| 1.0.0 | `48f3968897edd89d7441a200c765c7e3cf1fda6816de3018231b4183bd473e24` | `f6066829fcc3e63803ef5e213d87368c9c40c206` | 31/10/2026 | Gerente de Projeto — CCB de membro único | Promulgação dos agentes SDDAI via ADR-013 + prompt expresso CCB 31/10/2026 |
| 1.0.1 | `ef53e1a6e30a313aba3f441c93181ba1c369acf486aa900e6ad049fc9beddec9` | commit A12 | 31/10/2026 | Gerente de Projeto — CCB de membro único | **Renumeração ADR-013 → ADR-014 (OKB-C-26, RAT-2026-10-31-A12)** — título, Versão 1.0.1, Status, O3, Governança e nota de renumeração atualizados; hash normativo recalculado (método: sha256 dos bytes do início do arquivo até a linha imediatamente anterior a este bloco `## CO-ASSINATURA`; o hash histórico 1.0.0 `48f39688…` foi gerado com fronteira não documentada e não é reproduzível por este método — preservado como registro histórico) |

---




<!-- ===== docs/decisoes/adr-015-emenda-marco-m2.md ===== -->



---
id: ADR-015
title: Emenda de Marco — Repactuação Temporal do M2 (Regime de Emenda Controlada ADR-013-a)
version: 1.0.0
status: ratified
date: 2026-10-31
decisor: GP Leonardo (CCB único)
instrument: RAT-2026-10-31-A12
regime: ADR-013-a (Regime de Emenda Controlada do TAP — Baseline Vivo)
domain: Cronograma + Integração (PMBOK 7ª: Planejamento, Medição; PMBOK 6ª, dicionário: 4.6 Controle Integrado de Mudanças, 6.6 Controle do Cronograma)
---

# ADR-015 — Emenda de Marco: Repactuação Temporal do M2 (Regime ADR-013-a)

## Contexto

1. **Marco afetado:** M2 — data original no TAP §6 (18/09/2026, congelado): **30/09/2026**.
2. **Desvio constatado:** atraso de aproximadamente 25 dias úteis (superior ao gatilho de escalonamento de 3 dias úteis do Plano de Cronograma §1.8), documentado em `docs/change-requests/cr-001-m2-replanejamento.md`.
3. **Causa raiz (CR-001):** overengineering de governança, atraso na materialização técnica, ausência de pipeline e de código de produto.
4. **Impacto:** risco crítico ao marco M3 (15/11/2026) — MVP funcional.
5. **Ação corretiva já aprovada verbalmente pelo CCB (CR-001):** nova data-alvo 15/11/2026; congelamento de novas ondas de agentes até M3; foco de 80% da capacidade em código e infraestrutura — pendente de registro formal em Issue GitHub quando o repositório remoto estiver acessível.
6. **Regime aplicável:** ADR-013-a — Regime de Emenda Controlada do TAP: o núcleo blindado (incluído §6 Marcos como texto autorizativo) permanece intacto; a emenda materializa-se via **Delta Log** (`docs/tap/delta-v3-1.md`) + ADR (presente documento) + Nota de Contexto (NC-07) no plano. *Ratificação retrospectiva:* a ação corretiva verbal do CR-001 é formalizada retroativamente por este ADR, eliminando o desvio de formalidade registral.

## Decisão

1. **Repactuação temporal operacional de M2:** data-alvo 30/09/2026 → **15/11/2026** (data declarada em CR-001), registrada no Delta Log. A **data do núcleo do TAP §6 (30/09/2026) permanece inalterada textualmente** — o desvio é tratado como leitura operacional, jamais como correção do TAP (NC-00; ADR-005 §llocus de contexto mantido).
2. **M3 mantido em 15/11/2026** — nenhuma renumeração de marcos é executada (respeita o mapeamento canônico macro-fase/marco do TAP §6 e a MF2 vigente 01/10–15/11).
3. **Ressalva aberta C-06b (não resolvida por este ADR):** a repactuação de M2 faz **M2 e M3 colidirem na mesma data (15/11/2026)**. O CCB declara-se ciente e **delibera tratar a colisão em decisão futura e específica** — opções em análise: fusão M2+M3 (checkpoint único), deslocamento de M3 restrito ao prazo acadêmico de M4 (15/12/2026), ou manutenção com M2 de natureza documental e M3 de natureza produto. Até deliberação, ambos os marcos subsistem com critérios de aceite próprios e independentes (Tabela 4 do Plano de Cronograma). **A colisão não bloqueia a execução da ação corretiva do CR-001.**
4. **Ação corretiva vinculante (CR-001):** congelamento de novas ondas de agentes até M3; redirecionamento de 80% da capacidade da equipe para código e infraestrutura. Esta ADR **ratifica e vincula** a resolução; o descumprimento é desvio reportável ao auditor (Art. 8 da Constituição).
5. **Delta Log:** é criado `docs/tap/delta-v3-1.md` (mecanismo da ADR-013, até agora ausente no repositório), com a emenda de M2 e a historiada emenda REQ-07 (SQLite → PostgreSQL 15+, ADR-010).
6. **Nota de Contexto:** incorporada **NC-07** ao Plano (Base) de Cronograma no plano-integral, registrando a leitura operacional da repactuação sem tocar a reprodução do TAP.
7. **Obrigações acessórias:** registro da repactuação em Issue GitHub (label `change-request`, milestone M2) quando o repositório remoto estiver acessível; comunicação no fechamento do marco subsequente (exigência já vigente do Plano de Cronograma §5); propagação no OKB (§3.2 marcos, §4 catálogo) no próximo ciclo de versionamento.

## Mecanismo de Emenda (execução)

| Campo Alterado | Valor Anterior | Valor Novo | Justificativa (ADR/CR) | Data |
|---|---|---|---|---|
| Marco M2 — data-alvo (TAP §6) | 30/09/2026 | 15/11/2026 | CR-001 (atraso ~25 dias, risco crítico ao M3) ratificada como ADR-015 | 2026-10-31 |
| REQ-07 — Cache de cotações | SQLite | PostgreSQL 15+ | Alinhamento à ADR-010 (Stack Infra) | 2026-11-01 *(historizado de ADR-010)* |

Registros no `docs/tap/delta-v3-1.md` são append-only; emendas adicionais exigem CR + ADR (rodízio ADR-013-a).

## Consequências

- **Ganho:** realinhamento da baseline temporal ao estado real do projeto; flexibility documental auditável (Delta Log); formalização da ação corretiva que direciona capacidade ao caminho crítico (pipeline + código de produto); encerramento do finding C-06 do parecer AUD-2610-09.
- **Risco:** (i) perda da equivalência numérica entre data do TAP e leitura operacional — mitigada pela NC-00/NC-07 e pelo registro auditável; (ii) colisão M2=M3 em 15/11/2026 pode forçar decisão às cegas na véspera do marco — mitigada pela ressalva C-06b explicitamente agendada para deliberação futura; (iii) desgaste reputacional por reconhecer atraso — mitigado pela causa raiz documentada e ação corretiva vinculante.
- **Não mitigado por este ADR:** M4 (15/12/2026) permanece invariável como limite absoluto do prazo acadêmico; qualquer emenda futura que toque M4 exige contrapartida de compressão de escopo explicitamente deliberada.

## Ratificação

Ratificada em 31/10/2026 via **CCB-LOG RAT-2026-10-31-A12** (gatilho de permissão prévia deliberativo expresso do GP — CCB membro único), em consonância com o parecer AUD-2610-09 (finding C-06, prioridade crítica). Autoridade: TAP §6 irrevogável como fonte autorizativa; Constituição Art. 5 (governança humana), Art. 6 (SSOT), Art. 8 (auditoria).

## Referências

- `docs/change-requests/cr-001-m2-replanejamento.md` (origem da repactuação)
- `docs/decisoes/adr-013-regime-emenda-tap.md` (regime de emenda — instrumento habilitante)
- `docs/planos/plano-integral-tap-1-2-3-4-5.md` §6/Cronograma Tabela 4 + NC-00/NC-07
- `docs/auditorias/aud-2610-09-okb-normalizacao.md` (finding C-06; ressalva C-06b)
- `docs/governanca/ccb-log.md` (RAT-2026-10-31-A12)

## CO-ASSINATURA (Constitution Art. 5.4)

| Versão | SHA-256 do conteúdo normativo | Commit Git | Data | Papel do ratificador humano | Instrumento |
|--------|------------------------------|------------|------|----------------------------|-------------|
| 1.0.0 | `9cc2e3acdaa9ee26aee22a582fab9a2ca7cffa8a4e34d11e4738cbd90e7edc0e` | commit A12 | 31/10/2026 | Gerente de Projeto — CCB de membro único | Emenda M2 30/09 → 15/11/2026 (CR-001 + regime ADR-013-a); RAT-2026-10-31-A12 *(método: sha256 dos bytes do início do arquivo até a linha imediatamente anterior a este bloco `## CO-ASSINATURA`)* |

---




<!-- ===== docs/decisoes/adr-016-backend-mvp.md ===== -->



---
id: ADR-016
title: Backend do MVP — cálculo, cotações, persistência e contrato de erro
version: 1.0.0
status: proposta
date: 2026-10-31
decisor: Redação técnica (agent-architect, T10). Decisão: CCB humano (Constituição, Art. 5), pendente.
regime: Não se aplica (decisão de implementação; não emenda o TAP nem o núcleo blindado)
domain: Desenvolvimento e Qualidade (PMBOK 7ª: Abordagem de Desenvolvimento; Qualidade)
---

# ADR-016 — Backend do MVP: cálculo, cotações, persistência e contrato de erro

> **Status: proposta.** Esta ADR não está ratificada. A aprovação é ato humano do CCB (Constituição, Art. 5). Até lá, as decisões abaixo são a posição técnica proposta, não norma vigente.

## Contexto

O backend do MVP está especificado em `.ai/specs/backend-mvp-v1.spec.md` e implementado na branch `feat/backend-mvp`. Em 02/11/2026, a branch foi rebaseada sobre `d2ca1ff` (`main` com a consolidação de ADRs) e publicada no fork `FabricioLima-C/COGME`, para pull request. Nada foi integrado à `main`.

A spec e a ADR-001 v1.1.0 fixam o essencial: PostgreSQL, Docker Compose e a cadeia de cotações com Frankfurter primária e PTAX de reserva. Restam decisões que nenhum documento anterior registra e que afetam o resultado, os dados guardados e a resposta da API:

1. **Spread e IOF.** O plano de desenvolvimento deixou em aberto se o usuário informa ou se o sistema sugere (`[A CONFIRMAR]` em `docs/planos/desenvolvimento.md` §3.2.3). O Plano de Riscos (RE-04) trata a mudança de alíquota de IOF como risco externo.
2. **Ordem e arredondamento.** A spec define a sequência do cálculo e o arredondamento, mas não os registra como decisão.
3. **Fonte da cotação.** Frankfurter e PTAX não dão o mesmo número. Medição de 30/10/2026 (USD): Frankfurter 5,4325; PTAX (`cotacaoCompra`) 5,4206. A diferença é de cerca de 0,22 % em relação à PTAX. Por isso a resposta precisa informar a fonte usada.
4. **Cotação vencida.** A spec manda usar o último cache quando as fontes falham, mas não define idade máxima.
5. **Erros.** A spec define 400, 404, 503 e 500. Não trata 405 nem diz onde ficam as peças compartilhadas dos routers.

A stack (PostgreSQL 15+, Docker Compose, Nginx latente e hierarquia de fontes de câmbio) está na ADR-001 v1.1.0, que absorveu a ADR-010 pela emenda ADR-LOG-001. A ADR-010 ficou como registro histórico. Esta ADR pressupõe a ADR-001 v1.1.0 e não a reabre. Pela regra do ADR-LOG, nenhuma decisão desta ADR altera regra de ADR vigente; o que divergir fica como pendência para o CCB.

## Decisões

**D1. Spread e IOF são informados pelo usuário.** O código não contém alíquota de IOF, percentual de spread nem tabela de alíquotas. `calculator.calculate` recebe `spread_pct` e `iof_pct` como parâmetros. Toda resposta traz o aviso fixo: "Simulação de caráter informativo; spread e IOF foram informados pelo usuário e não substituem a orientação de um profissional habilitado." Esta decisão resolve o `[A CONFIRMAR]` de `docs/planos/desenvolvimento.md` §3.2.3.

**D2. Ordem do cálculo.** Todas as etapas usam `Decimal`:

1. bruto estrangeiro: `amount × quantity` nos regimes por tempo, ou `amount` no regime fixo; 2 casas;
2. bruto em BRL: bruto estrangeiro × cotação; 2 casas;
3. spread: bruto em BRL × `spread_pct` / 100; 2 casas;
4. IOF: (bruto em BRL − spread) × `iof_pct` / 100; 2 casas. **O IOF incide sobre o valor após o spread.**
5. líquido: bruto em BRL − spread − IOF;
6. taxa efetiva: líquido / bruto estrangeiro; 6 casas.

Em toda resposta vale `gross_brl − spread_brl − iof_brl == net_brl`. O `SimulationResponse` valida essa identidade.

**D3. Arredondamento `ROUND_HALF_EVEN`.** Valores em moeda com 2 casas; taxas com 6. O cálculo usa contexto decimal próprio, com precisão de 64 dígitos, e não depende do contexto do processo. `float` não entra no cálculo. Os corpos JSON são lidos com `parse_float=Decimal`.

**D4. Somente cotações são persistidas.** A tabela `fx_quotes` guarda cotações públicas. Simulações e invoices não são gravadas. Nomes, documentos e endereços existem só durante a requisição e não vão para log. Os logs trazem o nome da fonte e o tipo da falha, nunca valor, URL ou corpo da requisição (LGPD, P-04).

**D5. Fontes e identificação.** Frankfurter é a fonte primária e PTAX é a reserva obrigatória (ADR-001 v1.1.0).

- Frankfurter devolve a taxa de referência do BCE. `quoted_at` é a meia-noite UTC da data informada, e não há boletim.
- PTAX devolve `cotacaoCompra`, a taxa de compra que o banco paga ao profissional que vende a moeda estrangeira. Traz o tipo do boletim, e `dataHoraCotacao` é convertido de Brasília para UTC.
- Não há média entre fontes: vale a primeira que responder com cotação aceita.
- Cada cotação traz `source` e, na PTAX, `bulletin`. A simulação devolve a cotação usada em `quote`.

**D6. Cache e cotação vencida.** Cotação com idade até `COGME_RATE_TTL_SECONDS` (padrão 3600 s) é devolvida sem chamar a rede. Se todas as fontes falham, a última linha do cache é devolvida com `stale=true`, sem idade máxima. Sem nenhuma linha, a resposta é 503 `rates_unavailable`.

**D7. Resiliência.** Timeout de 0,9 s por provedor (`COGME_PROVIDER_TIMEOUT_SECONDS`), para caber no limite de 2 s de REQ-01. Circuit breaker por provedor, em memória: abre após 3 falhas consecutivas, fica aberto por 60 s e depois admite uma tentativa. O relógio é injetável, para os testes.

**D8. Aceite de cotação.** A taxa precisa ser `Decimal` finito, arredondada a 6 casas, com `0 < taxa < 1000` após o arredondamento. Taxa reprovada é falha da fonte, e nada é gravado.

**D9. Contrato de erro.**

- Erro de validação: 400 `validation_error`, no lugar do 422 do FastAPI. A mensagem é em PT-BR e não repete o valor enviado.
- 404 e 405: `not_found`. O 405 mantém o cabeçalho `Allow`. Não usa `validation_error`, porque a requisição está bem formada e o recurso é que não aceita o método.
- Falha de leitura do corpo (400 do Starlette): `validation_error`.
- Qualquer outro erro: 500 `internal_error`, sem traceback. Um middleware consome a exceção e registra só o tipo e a rota.
- O 422 e os schemas de erro de validação do FastAPI saem do OpenAPI.

**D10. `routers/common.py`.** Concentra as peças usadas por mais de um router: a dependência `RateServiceDep` (o serviço é montado no lifespan e guardado em `app.state`), as respostas de erro para o OpenAPI e `DecimalJsonRoute`. Essa rota lê o corpo com `Decimal`, recusa `NaN` e `Infinity` e limita o corpo a 64 KiB.

**D11. Versões.** `requires-python >= 3.11` no `pyproject.toml`, conforme a ADR-001 v1.1.0 (Python 3.11). Imagem e CI usam Python 3.12; o CI já usava 3.12 antes do backend. Esta ADR não altera a versão definida na ADR-001: a divergência fica como pendência (P8). Dependências de runtime com versões exatas em `requirements.txt`; os limites ficam em `pyproject.toml`. Lock com hashes: pendente (P1).

**D12. Rede e exposição.** O banco fica em rede interna, sem rota para a internet. Só o serviço `web` publica porta, em `127.0.0.1`. Não há CORS: o frontend é servido na mesma origem.

## Alternativas consideradas

| Decisão | Alternativas | Escolha e motivo |
|---|---|---|
| Spread e IOF (D1) | (a) alíquota fixa no código; (b) alíquota configurável com fonte e data de vigência, como prevê o RE-04; (c) o usuário informa | (c). A alíquota de IOF muda por decreto. Manter tabela de vigência exige revisão a cada mudança, fora do escopo do MVP. Com (c), o sistema não afirma uma alíquota vigente. |
| Ordem do IOF (D2) | IOF sobre o bruto em BRL; IOF sobre o valor após o spread | Após o spread, como define a spec §2. É regra de produto; o projeto não a valida juridicamente. |
| Arredondamento (D3) | `ROUND_HALF_UP`; `ROUND_HALF_EVEN` | `ROUND_HALF_EVEN`, por ser determinístico e sem viés. `ROUND_HALF_UP` é o mais difundido em documentos comerciais; um extrato que o use pode diferir em 0,01. |
| Persistência (D4) | Gravar simulações e invoices; gravar só cotações | Só cotações. Simulação e invoice trazem dados de pessoas e de negócio (LGPD). Histórico de simulações está fora do MVP. |
| Fontes (D5) | Só Frankfurter; só PTAX; média entre as duas | Cadeia com reserva (ADR-001 v1.1.0), sem média, com a fonte informada na resposta. |
| Cache vencido (D6) | Idade máxima, com 503 após o limite; sem limite e sempre `stale=true` | Sem limite, com `stale=true`. A API continua respondendo. O custo é informar cotação antiga; `stale` e `quoted_at` expõem isso. |
| Erro 405 (D9) | `validation_error`; `not_found` com `Allow` | `not_found` com `Allow`. A spec não define 405, e `validation_error` descreveria um erro na requisição que não existe. |
| Peças compartilhadas (D10) | Repetir em cada router; módulo comum | Módulo comum (`routers/common.py`), para que as rotas não divirjam em erros e na leitura do corpo. |

## Consequências

Positivas:

- O resultado depende dos dados informados e da cotação. Não há alíquota no código para ficar desatualizada.
- Cotação e simulação informam a fonte, o que torna a diferença entre Frankfurter e PTAX visível.
- Erros seguem um único modelo, sem traceback e sem eco dos dados enviados.
- Persistir só dados públicos reduz a superfície de LGPD.

Negativas e riscos:

- As fontes divergem. O mesmo dia pode gerar valores diferentes conforme a fonte. A resposta informa a fonte, mas não elimina a diferença.
- Cotação vencida sem idade máxima pode ser muito antiga. `stale` e `quoted_at` sinalizam isso; a interface precisa exibi-los (fora desta ADR).
- O cálculo depende do que o usuário digita. Spread ou IOF errados geram valor errado, e o sistema não tem como detectar.
- `ROUND_HALF_EVEN` pode diferir em 0,01 de cálculos feitos com `ROUND_HALF_UP`.
- O RE-04 do Plano de Riscos descreve como mitigação alíquotas configuráveis, com fonte e vigência. Esta ADR adota outra forma (entrada pelo usuário). Atualizar o RE-04 é decisão humana (P7).
- O TAP e o Plano de Gerenciamento v2.1.0 citam PTAX como fonte de REQ-01, e a ADR-001 v1.1.0 põe a Frankfurter como primária. Esta ADR não edita o TAP nem o plano (P7).
- Não há medição formal de desempenho (REQ-05) nem de UAT (REQ-09). A cobertura do produto (REQ-08) também não tem medição registrada no plano.

## Pendências para decisão humana

Nenhuma destas pendências está aceita nem resolvida por esta ADR.

- **P1. Lock de dependências com hashes.** `requirements.txt` fixa versões, mas não hashes. `docs/dependencias/registro.md` já registra que o lock com hashes é decisão futura. Gerá-lo muda o fluxo de atualização e exige aceite humano do risco. **Verificação de 01/11/2026:** risco confirmado. A imagem tem 45 pacotes (sem contar pip), e só os 11 diretos são fixados. A mesma `requirements.txt` já resolve `anyio` 4.16.0, enquanto a imagem do dia anterior tem 4.15.1. O `pip-audit` não achou vulnerabilidade conhecida nos 45 pacotes; o CI não executa essa auditoria.
- **P2. `/docs` e `/redoc`.** Com a configuração atual, o FastAPI serve essas páginas com ativos de `cdn.jsdelivr.net`, carregados pelo navegador de quem as abre. Há tensão com P-03 (soberania de dados). Opções: desativar essas rotas fora de desenvolvimento, servir os ativos localmente ou aceitar o risco com registro. **Verificação de 01/11/2026:** risco confirmado. `/docs` carrega `swagger-ui-dist@5` e `/redoc` carrega `redoc@2`, em versão flutuante e sem SRI, e a resposta não traz CSP. `/redoc` também usa Google Fonts, e as duas páginas usam favicon de `fastapi.tiangolo.com`. O código de terceiros roda na origem da API, onde o "Try it out" recebe dados de invoice. O proxy repassa essas rotas.
- **P3. Limite de concorrência de PDF.** A renderização roda em thread (`asyncio.to_thread`) sem limite de concorrência. Sob carga, pode esgotar CPU e memória do container. O limite depende de medição, que ainda não existe (REQ-05). **Verificação de 01/11/2026, em 16 CPUs, com payload pequeno:** o risco é de latência e de interferência no cache, não de memória. Rajadas de 1, 8, 32, 64, 128 e 256 invoices terminaram com 100 % de HTTP 200, sem OOM e com pico de 230 MiB (limite: 768 MiB). A vazão ficou perto de 4 PDFs/s: 8 levaram 1,9 s, 32 levaram 7,8 s, e 256 levaram 63,8 s, sem limite de fila. A partir de 32 simultâneas, a renderização atrasa o event loop: houve 71 leituras de cache com timeout de 0,3 s, o circuito do repositório abriu e a API buscou fontes externas com cache válido, gravando 3 linhas extras. A cotação sondada durante a carga levou no máximo 1,81 s. Medição indicativa, não substitui REQ-05.
- **P4. Atributo privado do WeasyPrint.** O `url_fetcher` que recusa recursos externos depende de `_fail_on_errors`, atributo não documentado da versão 70.0 (versão fixada). Uma atualização pode mudar esse comportamento sem aviso. Opções: alternativa pública ou teste de regressão dedicado. **Verificação de 01/11/2026:** dependência confirmada em `weasyprint/urls.py:428`, mas o risco é baixo. O template não referencia URL, e dado do usuário escapado gerou 0 chamadas ao fetcher. Sem o atributo, uma busca gera `AttributeError`, que a API converte em 503. A alternativa pública existe e passou no teste: subclasse de `weasyprint.urls.URLFetcher` com `fetch` próprio.
- **P5. Agentes em provedor externo.** Na execução do backend, os agentes de `.opencode/agents/` foram usados como papéis em modelos Claude (Sonnet, Opus e Haiku 5.5), por provedor externo, conforme `.ai/handoffs/HF-0500-backend-mvp.md`. Não foi usada a inferência local Qwen3 do P-02. O P-02 admite provedor cloud apenas para tarefas não sensíveis e veda o envio de código-fonte, especificações e handoffs. O P-03 classifica código e especificações como sensíveis. Esse uso precisa de avaliação do CCB. Esta ADR não o classifica como conforme.
- **P6. Retenção de `fx_quotes`.** A spec prevê manutenção futura, sem prazo definido. **Verificação de 01/11/2026:** risco baixo. Com 175.200 linhas, equivalentes a 10 anos com 2 moedas renovadas a cada hora, a tabela ocupa 23 MB e a consulta da última cotação leva 0,04 ms. Só há dados públicos.
- **P7. Divergências com documentos existentes.** (a) Atualizar o RE-04 do Plano de Riscos para a forma adotada em D1. (b) O TAP e o Plano de Gerenciamento v2.1.0 citam PTAX como fonte de REQ-01. Por orientação da equipe (02/11/2026), essa redação permanece. Alinhá-la à ADR-001 v1.1.0, se o CCB quiser, segue o regime de emenda controlada da ADR-005 v1.1.0 (delta em `docs/tap/delta-v3-1.md`). (c) O `[A CONFIRMAR]` de `desenvolvimento.md` §3.2.3 foi substituído pela referência a esta proposta; a decisão segue sujeita ao CCB.
- **P8. Versão do Python.** A ADR-001 v1.1.0 define Python 3.11; a imagem e o CI usam 3.12 (D11). Pela regra do ADR-LOG, cabe ao CCB escolher entre emendar a ADR-001 (ADR-LOG) ou passar imagem e CI para 3.11.

## Ratificação

Não ratificada. Status `proposta`. A ratificação é ato humano do CCB (Constituição, Art. 5). Esta ADR não registra aprovação, merge nem entrega.

## Referências

- `.ai/specs/backend-mvp-v1.spec.md` (§§1 a 8)
- `docs/decisoes/adr-001-stack.md` (v1.1.0: stack, banco e fontes de câmbio)
- `docs/decisoes/adr-log.md` (ADR-LOG-001; regra de não sobreposição)
- `docs/decisoes/adr-005-regime-tap.md` (v1.1.0: emenda controlada do TAP)
- `docs/decisoes/adr-010-stack-infraestrutura.md` (histórico; supersedida pela ADR-001 v1.1.0)
- `docs/planos/desenvolvimento.md` (§3.2.3)
- `docs/planos/plano-riscos.md` (RE-04)
- `docs/dependencias/registro.md`
- `.ai/handoffs/HF-0500-backend-mvp.md` (registro de execução)
- `constitution.md` (P-02, P-03, P-04; Art. 5)

---
