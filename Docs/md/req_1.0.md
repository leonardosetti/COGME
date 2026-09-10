### 5. Principais Requisitos das Principais Entregas/Produtos

Esta seção documenta os requisitos fundamentais dos produtos e entregas identificados na Estrutura Analítica do Projeto (EAP), conforme o Processo 5.2 (Coletar Requisitos) do PMBOK® 6ª edição e o Domínio de Entrega do PMBOK® 7ª edição. Cada requisito é mensurável, rastreável aos Objetivos SMART (§3) e vinculado a um pacote de trabalho específico da EAP.

**Regra de consistência:** Todo requisito deve possuir (a) critério de aceite quantificável, (b) rastreabilidade ao Objetivo SMART do TAP §3, (c) mapeamento ao pacote da EAP v2.0, e (d) domínio PMBOK 7ª associado.

#### 5.1. Entrega Principal 1 — MVP Web Funcional (Fase N5)

| ID     | Requisito                                                                  | Critério de Aceite                                       | Rastreabilidade               |
| ------ | -------------------------------------------------------------------------- | --------------------------------------------------------- | ----------------------------- |
| REQ-01 | Simulação de conversão cambial em tempo real (USD/EUR → BRL)           | Cotação obtida via API externa com latência ≤ 2s      | TAP §3 (Produto) + N5.2      |
| REQ-02 | Suporte a 5 regimes de contratação (hora, dia, semana, mês, valor fixo) | 100% dos regimes operacionais em UAT                      | TAP §3 (Produto) + N5.1      |
| REQ-03 | Aplicação de encargos financeiros simulados (spread + IOF)               | Cálculo auditável com precisão de 2 casas decimais     | TAP §3 (Produto) + N5.1      |
| REQ-04 | Emissão de invoice em formato PDF                                         | Geração via WeasyPrint em ≤ 3s por documento           | TAP §3 (Produto) + N5.4      |
| REQ-05 | Tempo de resposta da aplicação                                           | ≤ 3s em 95% das requisições (ambiente homologação)   | TAP §3 (Produto — M) + N5.1 |
| REQ-06 | Interface web responsiva (FOSS)                                            | Compatível com Chrome/Firefox/Edge (últimas 2 versões) | TAP §3 (Inovação) + N5.3   |
| REQ-07 | Cache de cotações (SQLite)                                               | Redução de ≥ 50% das chamadas à API externa           | OKB v3.1 §4.2 + N5.2         |

#### 5.2. Entrega Principal 2 — Garantia da Qualidade (Fase N6)

| ID     | Requisito                                                    | Critério de Aceite                                                                  | Rastreabilidade            |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------------------------------ | -------------------------- |
| REQ-08 | Cobertura de testes automatizados                            | ≥ 80% do código (unitários + integração via pytest + coverage.py)               | TAP §3 (Qualidade) + N6.1 |
| REQ-09 | Testes de aceitação (UAT)                                  | 100% dos fluxos críticos passing, zero defeitos críticos/bloqueantes               | TAP §3 (Qualidade) + N6.2 |
| REQ-10 | Aplicação de ferramentas da qualidade (PDCA + Ishikawa 6M) | 12 PDCAs consolidados + diagrama de causa e efeito documentado no Plano de Qualidade | TAP §3 (Qualidade) + N6.3 |

#### 5.3. Entrega Principal 3 — DevOps e CI/CD (Fase N7)

| ID     | Requisito             | Critério de Aceite                        | Rastreabilidade       |
| ------ | --------------------- | ------------------------------------------ | --------------------- |
| REQ-11 | Pipeline CI funcional | Lint + testes rodando em ≤ 5 min por push | OKB v3.1 §4.1 + N7.1 |

#### 5.4. Entrega Principal 4 — Base de Conhecimento (Fase N9)

| ID     | Requisito                                   | Critério de Aceite                                   | Rastreabilidade       |
| ------ | ------------------------------------------- | ----------------------------------------------------- | --------------------- |
| REQ-12 | ADRs para decisões arquiteturais críticas | Mínimo 3 ADRs registrados (stack, Kanban, métricas) | OKB v3.1 §4.5 + N9.1 |
| REQ-13 | Rastreabilidade de prompts SDD              | 100% dos prompts catalogados em`.ai/handoffs/`      | OKB v3.1 §4.4 + N9.3 |

#### 5.5. Entrega Principal 5 — Documentação Técnica (Fase N11)

| ID     | Requisito                           | Critério de Aceite                                | Rastreabilidade           |
| ------ | ----------------------------------- | -------------------------------------------------- | ------------------------- |
| REQ-14 | Documentação técnica consolidada | Arquitetura + APIs (OpenAPI) revisadas e aprovadas | TAP §3 (Produto) + N11.1 |

#### 5.6. Entrega Principal 6 — Conformidade FOSS (Fases N1, N4)

| ID     | Requisito               | Critério de Aceite                                                        | Rastreabilidade                    |
| ------ | ----------------------- | -------------------------------------------------------------------------- | ---------------------------------- |
| REQ-15 | Licenciamento 100% FOSS | Todas dependências com licenças OSI-approved (MIT, Apache 2.0, BSD, GPL) | TAP §3 (Inovação) + N1.5 + N4.4 |

#### 5.7 MATRIZ DE RASTREABILIDADE CONSOLIDADA (TAP §3 → EAP → REQUISITOS)

| Objetivo SMART (TAP §3)                                                                            | Fases EAP v2.0 Associadas               | Requisitos Cobertos                                    | Domínio PMBOK 7ª           |
| --------------------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------ | ---------------------------- |
| **Produto (Escopo)** — MVP funcional com simulação cambial, 5 regimes, invoice PDF, ≤ 3s  | N5 (Desenvolvimento)                    | REQ-01, REQ-02, REQ-03, REQ-04, REQ-05, REQ-06, REQ-07 | Entrega                      |
| **Qualidade e Testes** — ≥ 80% coverage, UAT 100% fluxos críticos, zero defeitos críticos | N6 (Garantia da Qualidade)              | REQ-08, REQ-09, REQ-10                                 | Medição                    |
| **Cronograma (Marcos)** — 22/09 (parcial) + Nov/2026 (final)                                 | Macro-fases MF1/MF2/MF3                 | Todos (indiretamente)                                  | Abordagem de Desenvolvimento |
| **Métricas e Indicadores** — Cycle Time + Throughput via GitHub Insights                    | N7 (DevOps) + N9 (Base de Conhecimento) | REQ-11                                                 | Medição                    |
| **Inovação e Ferramentas** — FOSS + SDD com IA auditável                                  | N1.5, N4.4, N5.5, N9.1, N9.3            | REQ-12, REQ-13, REQ-15                                 | Trabalho do Projeto          |

**Verificação de completude:** 100% dos Objetivos SMART do TAP §3 possuem ao menos um requisito associado na seção §5.
