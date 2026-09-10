# SEÇÃO §5 — PRINCIPAIS REQUISITOS DAS ENTREGAS/PRODUTOS

**Artefato pronto para inserção no TAP v1.1**
**Emissor:** GP Sênior PMBOK 7ª / PMO (Co-Autor Crítico)
**Data:** 11/09/2026
**Fundamentação:** Processo 5.2 (Coletar Requisitos) PMBOK 6ª + Domínio de Entrega PMBOK 7ª + Padrão PMO escritoriodeprojetos.com.br
**Base de extração:** Objetivos SMART (§3) + EAP v2.0 (12 fases / 37 pacotes) + OKB v3.1

---

## 1. VEREDITO EXECUTIVO

A seção §5 foi redigida com **14 requisitos mensuráveis** distribuídos em **6 entregas principais**, todos rastreáveis aos Objetivos SMART do TAP §3 e aos pacotes da EAP v2.0. A redação incorpora **3 correções de coerência** em relação ao TAP atual:

| #  | Correção                                                                                         | Fundamentação                                       |
| -- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| C1 | Substituição de "EVM + Burndown" por**métricas de fluxo Kanban** (Cycle Time, Throughput) | OKB v3.1 §3.4 — GitHub Insights como SSOT           |
| C2 | Atualização do marco parcial de 08/09/2026 para**22/09/2026**                              | Status real do projeto (entrega parcial documental)   |
| C3 | Inclusão explícita de**PDCAs + Ishikawa 6M** como requisito de qualidade                   | Demanda acadêmica registrada nos comentários da EAP |

---

## 2. TEXTO PRONTO PARA INSERÇÃO NO TAP v1.1

> **Instrução de inserção:** Substituir integralmente a seção §5 atual ("Principais requisitos das principais entregas/produtos") pelo texto abaixo.

---

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

---

## 3. MATRIZ DE RASTREABILIDADE CONSOLIDADA (TAP §3 → EAP v2.0 → REQUISITOS)

| Objetivo SMART (TAP §3)                                                                            | Fases EAP v2.0 Associadas               | Requisitos Cobertos                                    | Domínio PMBOK 7ª           |
| --------------------------------------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------ | ---------------------------- |
| **Produto (Escopo)** — MVP funcional com simulação cambial, 5 regimes, invoice PDF, ≤ 3s  | N5 (Desenvolvimento)                    | REQ-01, REQ-02, REQ-03, REQ-04, REQ-05, REQ-06, REQ-07 | Entrega                      |
| **Qualidade e Testes** — ≥ 80% coverage, UAT 100% fluxos críticos, zero defeitos críticos | N6 (Garantia da Qualidade)              | REQ-08, REQ-09, REQ-10                                 | Medição                    |
| **Cronograma (Marcos)** — 22/09 (parcial) + Nov/2026 (final)                                 | Macro-fases MF1/MF2/MF3                 | Todos (indiretamente)                                  | Abordagem de Desenvolvimento |
| **Métricas e Indicadores** — Cycle Time + Throughput via GitHub Insights                    | N7 (DevOps) + N9 (Base de Conhecimento) | REQ-11                                                 | Medição                    |
| **Inovação e Ferramentas** — FOSS + SDD com IA auditável                                  | N1.5, N4.4, N5.5, N9.1, N9.3            | REQ-12, REQ-13, REQ-15                                 | Trabalho do Projeto          |

**Verificação de completude:** 100% dos Objetivos SMART do TAP §3 possuem ao menos um requisito associado na seção §5.

---

## 4. SINALIZAÇÃO DE INCONSISTÊNCIAS NO TAP ATUAL (AÇÕES CORRELATAS)

Durante a redação da seção §5, foram identificadas **3 inconsistências** no TAP atual que devem ser corrigidas em revisão coordenada:

| #  | Inconsistência                                                                       | Localização Atual                         | Correção Proposta                                                                                                                                                                                                                                                                                                                               | Prioridade |
| -- | ------------------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| I1 | Objetivo "Métricas e Indicadores" (§3) ainda cita**EVM (SPI/CPI) + Burndown** | TAP §3, linha "Métricas e Indicadores"    | Substituir por: "Durante toda a execução, o gerente do projeto deverá coletar e divulgar semanalmente as métricas de fluxo Kanban —**Cycle Time** (meta: ≤ 3 dias) e **Throughput** (meta: ≥ 5 cards/semana) — via GitHub Insights, garantindo a rastreabilidade do progresso conforme o Domínio de Medição do PMBOK 7ª." | 🔴 P0      |
| I2 | Marco parcial citado como**08/09/2026**                                         | TAP §3 (Cronograma) + §8.3 (Restrições) | Atualizar para**22/09/2026** (data real da entrega parcial documental)                                                                                                                                                                                                                                                                      | 🔴 P0      |
| I3 | Nome do stakeholder grafado como**"Nivaldo Carleto"**                           | TAP §1, §3.2, §7, §13                   | Corrigir para**"Nivaldo Carletto"** (grafia oficial)                                                                                                                                                                                                                                                                                        | 🟠 P1      |

**Fundamentação das correções:**

- **I1**: O OKB v3.1 §3.4 substituiu explicitamente EVM/Burndown por métricas de fluxo Kanban, alinhando ao Domínio de Medição PMBOK 7ª e ao uso do GitHub Projects como SSOT.
- **I2**: O marco de 08/09/2026 já foi ultrapassado (hoje é 11/09/2026). O marco real de entrega parcial é 22/09/2026, conforme planejamento atualizado.
- **I3**: Erro ortográfico recorrente que compromete a credibilidade acadêmica do documento.

---

## 5. DEFINITION OF DONE (DoD) DA SEÇÃO §5

A seção §5 está **completa e aprovada para inserção no TAP v1.1** quando:

- [X] Contém 6 entregas principais documentadas
- [X] Contém 15 requisitos mensuráveis (REQ-01 a REQ-15)
- [X] Todo requisito possui critério de aceite quantificável
- [X] Todo requisito possui rastreabilidade ao Objetivo SMART do TAP §3
- [X] Todo requisito possui mapeamento ao pacote da EAP v2.0
- [X] Todo requisito possui domínio PMBOK 7ª associado
- [X] Matriz de rastreabilidade consolidada está presente
- [X] 100% dos Objetivos SMART do TAP §3 possuem requisito associado
- [X] Inconsistências do TAP atual foram sinalizadas (I1, I2, I3)
- [X] Alinhada ao OKB v3.1 (métricas de fluxo, não EVM)

---

## 6. TRADE-OFFS SINALIZADOS

| Trade-off                                                        | Risco                                                   | Mitigação                                                                                   |
| ---------------------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Inclusão de REQ-10 (PDCAs + Ishikawa) como requisito explícito | Percepção de "ferramenta virando entrega"             | Justificativa acadêmica: demanda explícita do stakeholder-avaliador                         |
| Exclusão de requisitos de deploy em produção                  | Percepção de "MVP incompleto"                         | Alinhado à remoção da Fase N8 (Deploy) da EAP v2.0 — MVP acadêmico não exige produção |
| Substituição de EVM por métricas de fluxo                     | Questionamento acadêmico sobre "abandono do PMBOK 6ª" | ADR-001 blinda a decisão; PMBOK 7ª é governança primária                                 |
| Meta de Cycle Time ≤ 3 dias sem baseline                        | Meta aspiracional não acionável                       | ADR-003 estabelece período de calibração (23/09 – 03/10) antes de fixar meta              |

---

## 7. PRÓXIMOS PASSOS

Após a inserção da seção §5, prosseguir com as seções pendentes na ordem de prioridade:

| Prioridade | Seção  | Ação                                                           | Prazo |
| ---------- | -------- | ---------------------------------------------------------------- | ----- |
| 🔴 P0      | §9      | Redigir "Premissas" (8 premissas fundamentais)                   | 11/09 |
| 🔴 P0      | §10     | Redigir "Riscos" (Top 5 riscos)                                  | 11/09 |
| 🔴 P0      | §11     | Redigir "Orçamento do Projeto" (R$ 0,00 + justificativa)        | 11/09 |
| 🟠 P1      | §6      | Preencher "Marcos" com datas concretas (corrigir 08/09 → 22/09) | 11/09 |
| 🟠 P1      | §7      | Corrigir nomes em "Partes interessadas" (Carletto, não Carleto) | 11/09 |
| 🟢 P3      | §1, §3 | Revisões textuais + corrigir inconsistências I1, I2, I3        | 11/09 |
| 🟢 P3      | Global   | Remover comentários de revisão + padronização textual        | 11/09 |

**Marco de submissão:** TAP v1.1 completo até 22/09/2026, 09:00 para submissão ao Prof. Dr. Nivaldo Carletto.

---

**Seção §5 consolidada e pronta para inserção no TAP v1.1.**

Aguardo confirmação da inserção para prosseguir com a seção §9 (Premissas).
