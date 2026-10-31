<!-- PROVENIÊNCIA: OKB v3.0 (20/09/2026) — corpus vivo até 30/10/2026; substituído pelo OKB v5.1.0 ratificado (CCB-003, 30/10/2026). Arquivado em 30/10/2026. Artefato imutável: não editar, não citar como fonte viva. -->

# OKB v3.0 — Operational Knowledge Base (Consolidada)

**Data:** 20/09/2026
**Status:** Ativa — convergente ao TAP v3 (18/09/2026)
**Hierarquia de autoridade:** TAP > OKB > Glossário > ADRs
**Referência matriz:** TAP v3 (18/09/2026) — Leonardo David Silva Setti
**Substitui:** OKB v2.2 (19/09/2026)

---

## 1. DECLARAÇÃO DE GOVERNANÇA (Convergente ao TAP §1.c)

### 1.1 Modelo Híbrido Declarado

| Camada                       | Fonte Normativa                                                                  | Função no COGME                                                                    |
| ---------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Governança primária        | PMBOK® 7ª edição — 12 princípios e 8 domínios de desempenho               | Define*por que* e *para quê*; orienta decisões por valor                       |
| Dicionário complementar     | PMBOK® 6ª edição — processos citados apenas para rastreabilidade acadêmica | Fornece vocabulário estrutural quando necessário;**obsolescência assumida** |
| Método de execução        | Kanban via GitHub Projects (SSOT — Single Source of Truth)                      | Define*como* o trabalho é executado diariamente                                   |
| Abordagem de desenvolvimento | Specification-Driven Development (SDD) com IA generativa auditável              | Geração de código e artefatos com revisão humana obrigatória                    |

### 1.2 Autoridade de Mudança (CCB)

- **CCB = GP (Leonardo David Silva Setti)** — membro único, conforme TAP v3 §1.c
- **Prof. Dr. Nivaldo Carleto:** stakeholder-avaliador nos marcos M1–M4, sem ingerência operacional
- **Trade-off aceito:** Velocidade decisória > colegialidade (justificável academicamente pela simplificação pedagógica do TAP §9 P7)

### 1.3 Obsolescência Formalmente Declarada

> **Declaração de obsolescência assumida:** O PMBOK® 6ª (2017) é tratado como dicionário de processos. Processos preditivos (ex: 4.1, 5.2, 6.5, 11.1) são citados apenas para rastreabilidade acadêmica. Métricas EVM (SPI/CPI) são **LEGADO e NÃO APLICÁVEIS** — substituídas por métricas de fluxo Kanban (Cycle Time, Throughput, CFD), conforme TAP §3 "Métricas e Indicadores" e Domínio de Medição PMBOK 7ª.

### 1.4 Estratégia de Entrega Faseada dos Planos de Gerenciamento

Conforme princípio de **Elaboração Progressiva** (PMBOK® 6ª) e **Personalização (Tailoring)** da Abordagem de Desenvolvimento (PMBOK® 7ª), a entrega dos planos de gerenciamento é faseada:

| Marco                     | Planos Entregues                                                  | Justificativa                                                                 |
| ------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **M1** (22/09/2026) | Integração, Escopo, Cronograma, Custos, Qualidade (Áreas 1–5) | Fundação documental mínima viável; foco no critério de aceite do TAP §6 |
| **M2** (30/09/2026) | Recursos, Comunicações, Riscos (Áreas 6–8)                    | Entregues após calibração do fluxo Kanban (23/09–03/10)                   |

**Trade-off declarado:** Redução de 30% da carga documental do M1, permitindo foco na qualidade dos 5 planos fundamentais e na configuração do ambiente Kanban (SSOT). Decisão alinhada ao Domínio de Abordagem de Desenvolvimento e Ciclo de Vida (PMBOK 7ª) e ao princípio GMV.

---

## 2. CORREÇÕES CRÍTICAS APLICADAS (v2.2 → v3.0)

| Item                          | v2.2 (Anterior)                | v3.0 (Corrigido — TAP v3)                                                                 | Domínio PMBOK 7ª           |
| ----------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------ | ---------------------------- |
| Fronteira M1                  | Ambiguidade entre 5 e 8 planos | **5 planos no M1** (Áreas 1–5); 3 planos diferidos para M2                         | Abordagem de Desenvolvimento |
| ADR-004                       | Inexistente                    | **Emitida** — Tasklists Markdown (rejeição de subissues)                          | Trabalho do Projeto          |
| Sistema de Tags               | Não formalizado               | **23 labels** em 5 categorias (Tipo, Macro-Fase, Área, Status, Prioridade)          | Trabalho do Projeto          |
| Milestones GitHub             | Não formalizadas              | **5 milestones** (M1–M4 + Calibração auxiliar)                                    | Medição                    |
| Prioridade Temporal           | Apenas MoSCoW                  | **P0–P3** complementar ao MoSCoW                                                    | Planejamento                 |
| Padrão de Redação de Cards | Não definido                  | **Padrão A** (documental) + **Padrão B** (User Story GWT, projetivo para M2) | Entrega                      |

---

## 3. ESTRUTURA DO OKB v3.0

### 3.1 Artefatos Obrigatórios (Rastreabilidade TAP → EAP)

| Artefato                 | Fase EAP | Status                       | Responsável |
| ------------------------ | -------- | ---------------------------- | ------------ |
| TAP v3                   | N1.2     | ✅ Aprovado (18/09/2026)     | Leonardo     |
| EAP                      | N1.2     | ✅ Aprovado                  | Leonardo     |
| Plano de Integração    | N1.2     | ✅ v1.0 (19/09/2026)         | Leonardo     |
| Plano de Escopo          | N1.2     | 🔄 v0.2 em revisão de pares | Fabricio     |
| Plano de Cronograma      | N1.2     | ⏳ Até 21/09                | Fabricio     |
| Plano de Custos          | N1.2     | ⏳ Até 21/09                | Fabricio     |
| Plano de Qualidade       | N1.3     | ⏳ Até 21/09                | Edson        |
| Plano de Recursos        | N1.2     | ⏳ Até 30/09 (M2)           | Leonardo     |
| Plano de Comunicações  | N1.2     | ⏳ Até 30/09 (M2)           | Leonardo     |
| Plano de Riscos          | N1.2     | ⏳ Até 30/09 (M2)           | Leonardo     |
| ADR-001 (Stack)          | N9.1     | ✅ Emitida (19/09)           | Leonardo     |
| ADR-002 (Kanban)         | N9.1     | ✅ Emitida (19/09)           | Leonardo     |
| ADR-003 (Métricas)      | N9.1     | ✅ Emitida (19/09)           | Leonardo     |
| ADR-004 (Tasklists)      | N9.1     | ✅ Emitida (20/09)           | Leonardo     |
| Catálogo de Prompts SDD | N9.3     | ⏳ Até 03/10                | Leonardo     |

### 3.2 Premissas Vigentes (TAP §9)

| ID | Premissa                                                         | Status                             |
| -- | ---------------------------------------------------------------- | ---------------------------------- |
| P1 | Governança híbrida (PMBOK 7ª + 6ª dicionário + Kanban)      | ✅ Vigente                         |
| P2 | FOSS absoluto                                                    | ✅ Vigente                         |
| P3 | SDD com IA auditável                                            | ✅ Vigente                         |
| P4 | Código-fonte é deliverable formal                              | ✅ Vigente                         |
| P5 | 20h/semana por membro                                            | ✅ Vigente                         |
| P6 | Hardware adequado e suficiente                                   | ✅ Revisada (hardware.md comprova) |
| P7 | GP = CCB único; Prof. Dr. Nivaldo Carleto = avaliador de marcos | ✅ Vigente                         |
| P8 | Aquisições e Partes Interessadas simplificadas                 | ✅ Vigente                         |

### 3.3 Restrições Vigentes (TAP §8)

- Escopo restrito ao MVP acadêmico
- Prazo letivo inegociável (M1: 22/09/2026)
- Orçamento zero (proibição de aquisições pagas)
- Equipe de 3 pessoas (múltiplos papéis)
- Stack 100% FOSS
- Licenciamento final open source (MIT/GPL)

---

## 4. ADRs EMITIDAS

### ADR-001: Stack Tecnológica FOSS

**Status:** Aprovada
**Data:** 19/09/2026
**Decisor:** GP Leonardo (CCB)
**Rastreabilidade:** TAP §3 (Inovação) + §8 (FOSS) + EAP N4.1, N5.1–N5.4

#### Contexto

O projeto exige stack 100% FOSS (restrição TAP §8.4), com capacidade de:

- Backend assíncrono para simulação cambial (REQ-01, latência ≤ 2s)
- Geração de PDF (REQ-04, ≤ 3s)
- Cache local (REQ-07)
- Testes automatizados (REQ-08, coverage ≥ 80%)

#### Decisão

Adoção da seguinte stack (todas licenças OSI-approved):

| Camada        | Tecnologia                 | Licença               | Justificativa                          |
| ------------- | -------------------------- | ---------------------- | -------------------------------------- |
| Backend       | Python 3.11 + FastAPI      | PSF / MIT              | Assíncrono nativo, ecossistema maduro |
| Banco         | SQLite                     | Public Domain          | Zero-config, ACID, adequado ao MVP     |
| Geração PDF | WeasyPrint                 | BSD-3-Clause           | HTML/CSS → PDF, FOSS                  |
| Testes        | pytest + coverage.py       | MIT                    | Padrão Python, integração CI        |
| CI/CD         | GitHub Actions (Free Tier) | Proprietário gratuito | Nativo ao SSOT                         |
| Frontend      | HTML5 + CSS3 + JS vanilla  | —                     | KISS, sem framework pesado             |
| LLM (SDD)     | QwenStudio                 | Licença autorizada    | TAP §3 (Inovação)                   |

#### Consequências

✅ **Positivas:** Zero custo, auditabilidade total, comunidade ativa, compatível com hardware local (TAP P6 revisada)
⚠️ **Riscos:** SQLite limita concorrência (aceitável para MVP acadêmico); WeasyPrint exige dependências nativas (glibc, Pango)
🔄 **Fallback:** Se FastAPI apresentar curva de aprendizado excessiva → Flask (MIT) como alternativa

#### Trade-offs Aceitos

- Simplicidade (KISS) > Performance extrema
- FOSS absoluto > Conveniência de soluções proprietárias
- SQLite > PostgreSQL (complexidade operacional desnecessária para MVP)

---

### ADR-002: Kanban como Método de Execução

**Status:** Aprovada
**Data:** 19/09/2026
**Decisor:** GP Leonardo (CCB)
**Rastreabilidade:** TAP §1.c + §3 (Métricas) + EAP N1.5, N7

#### Contexto

O TAP declara Kanban como método de execução (P1), mas o glossário v2.1 mencionava "Sprint" e "Sprint Planning" (incompatível com fluxo contínuo). É necessário operacionalizar o método de forma consistente.

#### Decisão

- **Ferramenta:** GitHub Projects (SSOT)
- **Colunas do fluxo:** `Backlog` → `Ready (DoR)` → `In Progress` → `Code Review` → `Done (DoD)`
- **WIP Limits:** 3 cards em `In Progress` por pessoa (Domínio de Equipe PMBOK 7ª — prevenção de burnout, TAP §10 R3)
- **Pull system:** Trabalho puxado por capacidade, não empurrado por cronograma rígido
- **Rituais:**
  - Daily assíncrona: GitHub Issues (15min/dia)
  - Refinement semanal: Product Backlog (30min)
  - Retrospectiva quinzenal: Risk backlog + lições aprendidas
- **Sprints:** NÃO utilizadas — fluxo contínuo (TAP §3 "Métricas")

#### Consequências

✅ **Positivas:** Flexibilidade, visibilidade total, métricas de fluxo nativas (GitHub Insights)
⚠️ **Riscos:** Requer disciplina de WIP limits; risco de cards parados em `Code Review`
🔄 **Fallback:** Se throughput cair abaixo de 3 cards/semana por 2 semanas consecutivas → revisar WIP limits

#### Mapeamento Domínios PMBOK 7ª → Rituais Kanban

| Domínio PMBOK 7ª           | Ritual Kanban                  | Artefato              |
| ---------------------------- | ------------------------------ | --------------------- |
| Stakeholders                 | Refinement semanal             | Backlog refinado      |
| Equipe                       | Daily assíncrona + WIP limits | GitHub Projects       |
| Abordagem de Desenvolvimento | Fluxo contínuo (sem sprints)  | CFD                   |
| Planejamento                 | Refinement + Priorização     | Backlog ordenado      |
| Trabalho do Projeto          | Pull system                    | Cards em fluxo        |
| Entrega                      | DoD + Code Review              | Incrementos validados |
| Medição                    | Cycle Time + Throughput        | GitHub Insights       |
| Incerteza                    | Retrospectiva + Risk backlog   | Lições aprendidas   |

#### Trade-offs Aceitos

- Fluxo contínuo > Iterações time-boxed (adequado à equipe de 3 pessoas)
- GitHub Projects > Jira/Trello (integração nativa ao SSOT, zero custo)

---

### ADR-003: Métricas de Fluxo (Substituição de EVM)

**Status:** Aprovada
**Data:** 19/09/2026
**Decisor:** GP Leonardo (CCB)
**Rastreabilidade:** TAP §3 (Métricas) + §11.3 (implícito) + Domínio de Medição PMBOK 7ª

#### Contexto

O glossário v2.1 listava SPI/CPI (EVM — PMBOK 6ª) como métricas ativas. O TAP §3 declara explicitamente uso de métricas de fluxo Kanban. Há conflito que deve ser resolvido.

#### Análise Técnica

**EVM (SPI/CPI):** Projetado para ambientes preditivos com linha de base de custos. Inaplicável ao COGME porque:

- Orçamento zero (TAP §11) → AC (Actual Cost) = 0 → CPI indeterminado
- Escopo emergente (Kanban) → PV (Planned Value) não faz sentido em fluxo contínuo

**Métricas de fluxo Kanban:** Alinhadas ao Domínio de Medição PMBOK 7ª e à realidade ágil do projeto.

#### Decisão

**Métricas oficiais do COGME (exclusivas):**

| Métrica                      | Fórmula                     | Meta                  | Frequência   |
| ----------------------------- | ---------------------------- | --------------------- | ------------- |
| Cycle Time                    | Média (Done − In Progress) | ≤ 3 dias             | Semanal       |
| Throughput                    | Cards concluídos / semana   | ≥ 5 cards            | Semanal       |
| CFD (Cumulative Flow Diagram) | Visualização de gargalos   | Sem bandas largas     | Semanal       |
| WIP em fluxo                  | Cards em In Progress         | ≤ 9 (3 × 3 pessoas) | Contínuo     |
| Coverage                      | Linhas testadas / totais     | ≥ 80%                | Por push (CI) |

**Métricas LEGADO (NÃO APLICÁVEIS):**

- ❌ SPI (Schedule Performance Index)
- ❌ CPI (Cost Performance Index)
- ❌ EVM (Earned Value Management)

**Declaração formal:** SPI/CPI são removidos do glossário v2.2 e marcados como "LEGADO — NÃO APLICÁVEL — Substituído por métricas de fluxo Kanban (ADR-003)".

#### Consequências

✅ **Positivas:** Alinhamento ao Manifesto Ágil, métricas nativas do GitHub, foco em valor entregue
⚠️ **Riscos:** Exige calibração inicial (23/09 a 03/10) para estabelecer baseline realista
🔄 **Fallback:** Se baseline indicar throughput < 3 cards/semana após 03/10 → revisar escopo do MVP (gestão de mudanças)

#### Período de Calibração

- **Início:** 23/09/2026
- **Fim:** 03/10/2026
- **Objetivo:** Coletar dados reais para estabelecer metas factíveis (TAP §3 "Métricas e Indicadores")
- **Saída:** Baseline documentada + metas ajustadas (se necessário via change-request)

#### Trade-offs Aceitos

- Métricas de fluxo > EVM (adequação ao contexto ágil)
- Baseline empírica > Metas arbitrárias (Domínio de Medição PMBOK 7ª)

---

### ADR-004: Controle de Progresso via Tasklists Markdown (Rejeição de Subissues)

**Status:** Aprovada
**Data:** 20/09/2026
**Decisor:** GP Leonardo (CCB — membro único)
**Rastreabilidade:** TAP §1.c (Governança Híbrida) + REQ-12 (ADRs) + ADR-002 (Kanban) + ADR-003 (Métricas)
**Domínio PMBOK 7ª:** Abordagem de Desenvolvimento + Medição + Trabalho do Projeto
**Processo PMBOK 6ª (dicionário):** 4.3 — Orientar e Gerenciar o Trabalho do Projeto

#### Contexto

Cards complexos (estimativa ≥ 6h ou com múltiplos entregáveis, como o Plano de Qualidade ou a Configuração do Repositório) exigem decomposição visual do progresso interno para evitar a opacidade de cards estagnados na coluna `In Progress` por múltiplos dias. A equipe avaliou mecanismos para prover esta granularidade sem violar o fluxo Kanban.

#### Opções Avaliadas

1. **Sem decomposição:** Card único, sem visibilidade de progresso interno.
2. **Tasklists Markdown nativas (`- [ ]`):** Checklists no corpo da Issue.
3. **Subissues reais (Issues filhas):** Issues vinculadas via `#`, com status independente.

#### Decisão

Adotar a **Opção 2 (Tasklists Markdown condicionais)** e **rejeitar formalmente a Opção 3 (Subissues reais)**.

**Regras de aplicação:**

- **Obrigatórias** para cards com estimativa ≥ 6h ou múltiplos entregáveis.
- **Proibidas** para cards atômicos (≤ 4h) ou em status `Code Review`/`Done`.
- **Formato canônico:** Mínimo 3 itens, máximo 7 itens; último item obrigatoriamente "Validação final".
- **Natureza binária:** Itens são "feito/não feito", sem status intermediário.

#### Consequências

✅ **Positivas:** Zero overhead de gestão; visibilidade nativa no GitHub (barra de progresso da tasklist); não fragmenta o backlog no GitHub Projects.
⚠️ **Riscos:** Requer disciplina do responsável para manter a tasklist atualizada durante a execução.
🔄 **Fallback:** Se a tasklist se mostrar insuficiente para cards de código (M2/M3), reavaliar na Retrospectiva da MF2.

#### Impacto nas Métricas (ADR-003)

- **Cycle Time e Throughput:** Medem exclusivamente o **card pai**. Sub-tarefas da tasklist não são unidades de entrega.
- **WIP Limit:** Conta o **card pai** na coluna `In Progress` (respeitando o limite de 3 cards/pessoa da ADR-002).
- **CFD:** Ignora o progresso interno da tasklist, evitando distorção das bandas largas.

#### Trade-offs Aceitos

- Simplicidade (GMV) > Granularidade de status de sub-tarefas.
- Unidade atômica de métrica (card pai) > Rastreabilidade fina de sub-passos.
- Valor Ágil aplicado: *"Indivíduos e interações sobre processos e ferramentas."*

#### Adendo Normativo: Atualização do Plano de Escopo (§2.6)

A seção 2.6 (Definition of Ready e Definition of Done) do Plano de Escopo deve ser atualizada para incorporar a tasklist como gate de qualidade.

**Ação:** Adicionar o item 8 ao DoD na próxima revisão do plano:

> **8.** se o card possuir tasklist Markdown no corpo da Issue (conforme ADR-004), 100% dos itens estejam marcados como concluídos.

---

## 5. GLOSSÁRIO v3.0 — CORREÇÕES APLICADAS

### 5.1 Termos Corrigidos (v2.2 → v3.0)

| Termo         | v2.2                                                                            | v3.0 (Corrigido)                                                                      |
| ------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| CCB           | "Comitê de controle de mudanças (GP Leonardo — membro único, TAP v3 §1.c)" | Mantido — sem alteração                                                            |
| SPI           | "LEGADO — NÃO APLICÁVEL — Substituído por Cycle Time (ADR-003)"            | Mantido — sem alteração                                                            |
| CPI           | "LEGADO — NÃO APLICÁVEL — Substituído por Throughput (ADR-003)"            | Mantido — sem alteração                                                            |
| EVM           | "LEGADO — NÃO APLICÁVEL — Orçamento zero inviabiliza EVM (ADR-003)"        | Mantido — sem alteração                                                            |
| Sprint        | "NÃO UTILIZADO — Fluxo contínuo Kanban (ADR-002)"                            | Mantido — sem alteração                                                            |
| Hardware (P6) | "Adequado e suficiente" (premissa revisada — hardware.md comprova)             | Mantido — sem alteração                                                            |
| Fronteira M1  | Ambiguidade (5 ou 8 planos)                                                     | **Corrigido:** M1 entrega 5 planos (Áreas 1–5); Áreas 6–8 diferidas para M2 |

### 5.2 Termos Adicionados (v3.0)

| Termo             | Definição                                                                                                                | Contexto                                                    |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Tasklist Markdown | Checklist nativo do GitHub (`- [ ]`) no corpo da Issue                                                                   | ADR-004 — controle de progresso interno de cards complexos |
| Subissue          | Issue filha vinculada a uma Issue pai                                                                                      | **REJEITADO** formalmente pela ADR-004                |
| Card Ubíquo      | Card autossuficiente que declara o quê, por quê, como será aceito e a quem pertence sem dependência de leitura externa | Padrão de redação definido no OKB §9.3                  |
| P0–P3            | Escala de prioridade temporal complementar ao MoSCoW                                                                       | P0 = caminho crítico; P3 = postergável                    |
| pair-review       | Status de artefato redigido aguardando validação de um par                                                               | Aplica-se a planos, requisitos, matrizes                    |
| in-review         | Status de artefato aprovado pelo CCB aguardando consolidação/versionamento final                                         | Aplica-se a ADRs, decisões formais                         |

---

## 6. RASTREABILIDADE CONSOLIDADA (TAP → OKB → ADRs)

| TAP §                         | OKB v3.0                | ADR                    | Domínio PMBOK 7ª           |
| ------------------------------ | ----------------------- | ---------------------- | ---------------------------- |
| §1.c (Governança)            | §1.1, §1.2            | ADR-002                | Abordagem de Desenvolvimento |
| §3 (Métricas)                | §3.2 (P1–P8)          | ADR-003                | Medição                    |
| §3 (Inovação)               | §4 (ADRs)              | ADR-001                | Trabalho do Projeto          |
| §6 (M1 — fronteira 5 planos) | §1.4 (Entrega Faseada) | —                     | Abordagem de Desenvolvimento |
| §8 (Restrições FOSS)        | §3.3                   | ADR-001                | Abordagem de Desenvolvimento |
| §9 (Premissas)                | §3.2 (P6 revisada)     | —                     | Recursos                     |
| §10 (Riscos)                  | §3.2 (P5 — burnout)   | ADR-002 (WIP limits)   | Equipe                       |
| REQ-12 (ADRs)                  | §4 (4 ADRs emitidas)   | ADR-001, 002, 003, 004 | Trabalho do Projeto          |

---

## 7. PRÓXIMOS PASSOS (Pré-M1: 22/09/2026)

| Ação                                            | Responsável | Prazo                 | Prioridade |
| ------------------------------------------------- | ------------ | --------------------- | ---------- |
| Consolidar OKB v3.0 no repositório               | Leonardo     | 20/09                 | CRÍTICA   |
| Atualizar glossário para v3.0                    | Leonardo     | 20/09                 | ALTA       |
| Configurar GitHub Projects (colunas + WIP)        | Leonardo     | 20/09                 | CRÍTICA   |
| Criar 27 labels no repositório (sistema de tags) | Leonardo     | 20/09                 | CRÍTICA   |
| Criar 5 milestones no GitHub                      | Leonardo     | 20/09                 | CRÍTICA   |
| Redigir Plano de Integração (GMV)               | Leonardo     | ✅ Concluído (19/09) | —         |
| Redigir Plano de Escopo                           | Fabricio     | 21/09                 | ALTA       |
| Redigir Plano de Cronograma                       | Fabricio     | 21/09                 | ALTA       |
| Redigir Plano de Custos                           | Fabricio     | 21/09                 | ALTA       |
| Redigir Plano de Qualidade (12 PDCAs + Ishikawa)  | Edson        | 21/09                 | ALTA       |
| Aplicar tasklists nos cards ≥ 6h (ADR-004)       | Equipe       | 21/09                 | ALTA       |
| Submeter M1 via GitHub                            | Leonardo     | 22/09                 | CRÍTICA   |

---

## 8. LITERATURA DE APOIO — QUESTÕES ADJACENTES

Esta seção documenta decisões técnicas fundamentadas em literatura PMBOK® e boas práticas de gerenciamento de projetos, utilizadas como apoio às decisões de configuração do GitHub e governança do COGME.

### 8.1 Área de Conhecimento para Rede de Projeto e Caminho Crítico

**Questão:** Segundo PMI PMBOK ed 7 e 6, qual área de conhecimento deve conter a rede de projeto contendo a sequência de tarefas do projeto conforme progressão e tempo para cálculo das tabelas de precedência e caminhos críticos?

**Resposta técnica:**

| Edição                            | Resposta                                                                                                                                                                      |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PMBOK® 6ª (Dicionário)           | **Gerenciamento do Cronograma do Projeto** — Processos 6.4 (Sequenciar as Atividades) e 6.6 (Desenvolver o Cronograma)                                                 |
| PMBOK® 7ª (Governança Primária) | **Domínio de Desempenho de Planejamento** (evolução progressiva do cronograma) + **Domínio de Desempenho de Medição** (monitoramento do progresso temporal) |

**Aplicação no COGME:**

Conforme ADR-003 e Plano de Integração §1.6.2, o projeto declara formalmente a **obsolescência operacional** do uso de redes de projeto detalhadas (CPM/Gantt) para o gerenciamento do fluxo de trabalho diário.

| Nível                       | Abordagem                                                                                                                                                         |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Macro (Marcos M1–M4)        | Sequenciamento temporal fixo; lógica de precedência do PMBOK 6ª (Processo 6.5) usada apenas para validar viabilidade acadêmica                                |
| Operacional (Tarefas da EAP) | Sequenciamento gerenciado pelo Pull System no GitHub Projects (ADR-002); "caminho crítico" identificado empiricamente por gargalos no CFD e Cycle Time (ADR-003) |

**Trade-off declarado:** Abre-se mão da formalidade preditiva (CPM/EVM) em favor de métricas de fluxo ágil nativas, conforme o Domínio de Medição do PMBOK 7ª e o método Kanban.

---

### 8.2 Estruturação do Cumulative Flow Diagram (CFD) para Demonstração Formal

**Questão:** Como estruturar no documento o Cumulative Flow Diagram (CFD) para demonstração formal ao orientador?

**Resposta técnica:**

O CFD deve aparecer em três artefatos, com funções distintas:

| Artefato                | Seção                        | Função                       |
| ----------------------- | ------------------------------ | ------------------------------ |
| Plano de Integração   | §1.6.1 (Métricas de Fluxo)   | Definição formal + cadência |
| Plano de Cronograma     | §2.3 (Monitoramento Temporal) | Substituto do Gantt/EVM        |
| Plano de Comunicações | §3.2 (Relatórios Semanais)   | Evidência visual de progresso |

**Regra GMV:** Não criar artefato separado. O CFD é métrica nativa do GitHub Insights — qualquer documentação adicional seria burocracia.

**Definição formal (para inclusão nos planos):**

> O Cumulative Flow Diagram (CFD) é a visualização gráfica do fluxo de trabalho acumulado ao longo do tempo, onde cada banda horizontal representa uma coluna do quadro Kanban (Backlog, Ready, In Progress, Code Review, Done). A largura de cada banda em um determinado instante indica a quantidade de cards naquela etapa.

**Fonte de dados:** GitHub Projects → GitHub Insights → Aba "Charts" → "Cumulative Flow Diagram"
**Frequência:** Semanal (toda segunda-feira, 09:00)
**Responsável:** GP Leonardo David Silva Setti

**Meta de desempenho:**

- **CFD saudável:** Bandas paralelas e de largura constante (fluxo estável)
- **CFD com gargalo:** Bandas que se alargam progressivamente (acúmulo em uma etapa)
- **Ação corretiva:** Se uma banda ultrapassar 2× a largura média das demais por 2 semanas consecutivas, acionar Retrospectiva extraordinária (ADR-002)

**Blindagem acadêmica:** Se o Prof. Dr. Nivaldo Carleto questionar a ausência de Gantt, a defesa técnica é a ADR-003, fundamentada em três pilares:

1. Domínio de Medição do PMBOK 7ª: Prioriza métricas de fluxo sobre métricas preditivas
2. Restrição de Orçamento Zero (TAP §11): Inviabiliza EVM (AC = 0 → CPI indeterminado)
3. Natureza do Fluxo Contínuo (ADR-002): CFD fornece visibilidade em tempo real sem overhead

---

### 8.3 Resolução da Inconsistência de Fronteira do M1

**Questão:** O TAP §6 M1 declara 5 planos, mas o OKB v2.2 lista 8 planos. Esta informação sana a inconsistência TAP?

**Resposta técnica:**

**Sim, esta informação sana totalmente a inconsistência** e valida a governança híbrida sob a ótica do PMBOK®.

| Artefato              | Leitura Anterior (Incorreta)              | Leitura Corrigida (Governança Híbrida)                                                               |
| --------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| TAP §6               | "Incompleto" por citar apenas 5 áreas    | **Correto:** Define a linha de base faseada do Marco M1 (Fundação)                             |
| OKB v2.2 §3.1        | "Contraditório" por listar 8 planos      | **Correto:** Define o inventário total de artefatos do projeto ao longo de todo o ciclo de vida |
| Plano de Integração | Ambiguidade sobre "7 planos subsequentes" | Atualizado para explicitar a estratégia de entrega faseada                                            |

**Princípio PMBOK 7ª Aplicado:** Personalização (Tailoring) da Abordagem de Desenvolvimento. Entregar todos os 8 planos no M1 geraria overhead burocrático inicial desnecessário (anti-ágil). Deferir Recursos, Comunicações e Riscos para quando o fluxo de trabalho estiver mais maduro é uma decisão de tailoring legítima e defensável academicamente.

---

## 9. CONFIGURAÇÃO OPERACIONAL DO GITHUB

Esta seção formaliza as decisões de configuração do GitHub como SSOT do COGME, conforme ADR-002.

### 9.1 Sistema de Tags (Labels) — 27 Labels em 5 Categorias

**Fundamentação:** As tags abaixo foram desenhadas para operar no GitHub Issues + GitHub Projects (SSOT, ADR-002), com três objetivos:

1. Rastreabilidade TAP → EAP → Card (cada card vincula-se a fase, área e requisito)
2. Métricas de fluxo (Throughput e Cycle Time por tipo/área, ADR-003)
3. Controle de mudanças e riscos (labels operacionais do Plano de Integração §1.7 e §1.9)

**Princípio aplicado:** GMV — cada tag existe apenas se for útil para filtragem, métrica ou governança.

#### Categoria 1 — Tipo de Trabalho (6 tags)

| Tag       | Descrição                                                           | Cor sugerida                   |
| --------- | --------------------------------------------------------------------- | ------------------------------ |
| `feat`  | Nova funcionalidade do MVP                                            | `#0E8A16` (verde)            |
| `bug`   | Defeito em funcionalidade existente                                   | `#D73A4A` (vermelho)         |
| `docs`  | Artefatos textuais: planos, TAP, OKB, Glossário, lições aprendidas | `#0075CA` (azul)             |
| `test`  | Testes unitários, de integração e UAT                              | `#BFD4F2` (azul claro)       |
| `ci`    | Configuração e manutenção do pipeline GitHub Actions              | `#FBCA04` (amarelo)          |
| `chore` | Tarefas operacionais que não alteram código nem docs                | `#E4E669` (cinza-esverdeado) |

#### Categoria 2 — Macro-Fase EAP (3 tags)

| Tag                  | Descrição                          | Cor sugerida             |
| -------------------- | ------------------------------------ | ------------------------ |
| `MF1-fundacao`     | Fases N1 a N4, N8, N9, N10 (parcial) | `#D4C5F9` (roxo claro) |
| `MF2-construcao`   | Fases N5 a N7, N10                   | `#C5DEF5` (azul claro) |
| `MF3-consolidacao` | Fases N11 e N12                      | `#BFDADC` (rosa claro) |

#### Categoria 3 — Área de Conhecimento (8 tags)

| Tag                   | Descrição                                             | Cor sugerida                  |
| --------------------- | ------------------------------------------------------- | ----------------------------- |
| `area:integracao`   | Coordenação entre planos, controle de mudanças, SSOT | `#1D76DB` (azul)            |
| `area:escopo`       | Requisitos, EAP, DoR/DoD, fronteira IN/OUT, YAGNI       | `#006B75` (teal)            |
| `area:cronograma`   | Marcos M1–M4, fluxo contínuo, baseline de métricas   | `#5319E7` (roxo)            |
| `area:custos`       | Orçamento zero, conformidade FOSS                      | `#B60205` (vermelho escuro) |
| `area:qualidade`    | Coverage ≥ 80%, UAT, 12 PDCAs, Ishikawa 6M             | `#008672` (verde-azulado)   |
| `area:recursos`     | Equipe de 3, hardware, prevenção de burnout           | `#D93F0B` (laranja)         |
| `area:comunicacoes` | Daily assíncrona, Refinement, Retrospectiva            | `#F9D0C4` (salmão)         |
| `area:riscos`       | R1–R5, risk backlog, gatilhos de escalation            | `#B60205` (vermelho escuro) |

#### Categoria 4 — Status Operacional (4 tags)

| Tag                | Descrição                                                  | Cor sugerida                  |
| ------------------ | ------------------------------------------------------------ | ----------------------------- |
| `change-request` | Solicitação formal de mudança. Aciona fluxo CCB em ≤ 48h | `#FF0000` (vermelho)        |
| `risk`           | Risco identificado ou materializado (R1–R5)                 | `#FFFF00` (amarelo)         |
| `blocked`        | Card bloqueado por dependência externa ou interna           | `#B60205` (vermelho escuro) |
| `sdd-ia`         | Artefato ou código gerado com apoio de IA generativa (SDD)  | `#A2EEEF` (ciano)           |

#### Categoria 5 — Prioridade (6 tags: MoSCoW + P0–P3)

| Tag        | Descrição                              | Cor sugerida                  |
| ---------- | ---------------------------------------- | ----------------------------- |
| `must`   | Requisito indispensável ao MVP          | `#B60205` (vermelho escuro) |
| `should` | Requisito importante mas não bloqueante | `#FBCA04` (amarelo)         |
| `P0`     | Crítico / Caminho crítico              | `#B60205` (vermelho escuro) |
| `P1`     | Alto                                     | `#D93F0B` (laranja)         |
| `P2`     | Médio                                   | `#FBCA04` (amarelo)         |
| `P3`     | Baixo                                    | `#0E8A16` (verde)           |

#### Regras de Aplicação

1. Todo card deve ter no mínimo 3 tags: 1 tipo + 1 macro-fase + 1 área.
2. Cards de código devem ter obrigatoriamente `feat` ou `bug` + tag de macro-fase.
3. Cards de documentação devem ter `docs` + `area:X` correspondente.
4. Cards com `sdd-ia` exigem que o commit vinculado declare co-autoria (DoD, Plano de Escopo §2.6).
5. Cards com `change-request` não migram para `In Progress` até aprovação do GP.
6. Cards com `blocked` devem registrar a dependência no corpo da Issue.

#### Tags Explicitamente Excluídas (decisão GMV)

| Tag rejeitada                         | Motivo da exclusão                                         |
| ------------------------------------- | ----------------------------------------------------------- |
| `N1` … `N12` (fases individuais) | 12 tags redundantes; fase já consta no título padronizado |
| `REQ-01` … `REQ-15`              | Rastreabilidade via corpo do card, não via tag             |
| `could`, `wont`                   | Classes vazias no escopo atual                              |
| `epic`                              | MVP é único; não há múltiplos épicos                  |
| `spike`                             | Não há pesquisa exploratória formal no escopo            |
| `good first issue`                  | Equipe de 3 pessoas; onboarding não se aplica              |
| `help wanted`                       | Mesmo motivo                                                |

---

### 9.2 Milestones do Projeto — 5 Milestones

**Decisão GMV:** 5 milestones no total. O GitHub não suporta hierarquia nativa de milestones, portanto as subfases da EAP são rastreadas via labels de macro-fase dentro de cada milestone.

| # | Milestone                                       | Due Date   | Abertura   | Macro-Fase               | Tipo          | Cards Associados        |
| - | ----------------------------------------------- | ---------- | ---------- | ------------------------ | ------------- | ----------------------- |
| 1 | `M1 — Entrega Parcial Documental`            | 22/09/2026 | 01/09/2026 | MF1                      | Marco oficial | M1-01 a M1-21           |
| 2 | `M2 — Ambiente e Modelagem Concluídos`      | 30/09/2026 | 23/09/2026 | MF1 (encerramento)       | Marco oficial | N3.x, N4.x, N2.3        |
| 3 | `Calibração — Baseline de Métricas`       | 03/10/2026 | 23/09/2026 | MF1 → MF2 (transição) | Auxiliar      | Baseline + ADR de metas |
| 4 | `M3 — MVP Funcional (Beta)`                  | 15/11/2026 | 04/10/2026 | MF2                      | Marco oficial | N5.x, N6.x, N7.1, N10.x |
| 5 | `M4 — Encerramento e Validação Acadêmica` | 15/12/2026 | 16/11/2026 | MF3                      | Marco oficial | N11.x, N12.x            |

#### Regras de Aplicação no GitHub

1. Cada Issue deve estar associada a exatamente uma milestone. Cards sem milestone são tratados como `Backlog` não planejado.
2. A milestone não pode ser fechada enquanto houver Issues abertas com label `blocked` ou `change-request`.
3. O fechamento da milestone exige: (i) todos os critérios de fechamento atendidos, (ii) registro de lições aprendidas da fase, (iii) comunicação ao Prof. Dr. Nivaldo Carleto quando aplicável (M1, M3, M4).
4. Alteração de data de milestone exige `change-request` + aprovação do CCB (GP Leonardo) + ADR se alterar marco oficial.
5. A milestone auxiliar (Calibração) não substitui M2 — são complementares. M2 encerra MF1; Calibração estabelece baseline para MF2.

---

### 9.3 Padrão de Redação de Cards Ubíquos

**Princípio do Card Ubíquo:** Um card ubíquo é autossuficiente: qualquer membro da equipe (ou o Prof. Dr. Nivaldo Carleto, em avaliação) deve conseguir compreender o quê, por quê, como será aceito e a quem pertence sem abrir nenhum outro artefato.

**Três propriedades obrigatórias:**

1. **Autocontextualização** — o card declara sua finalidade em linguagem própria
2. **Critério de aceite mensurável** — checklist binário (atingido/não atingido)
3. **Rastreabilidade dupla** — vínculo vertical (TAP → EAP → REQ) e horizontal (área + macro-fase + milestone)

#### Padrão A — Card Documental / Governança / Infraestrutura

**Aplica-se a:** `docs`, `ci`, `chore`.

| Campo                     | Função                    | Regra de preenchimento                           |
| ------------------------- | --------------------------- | ------------------------------------------------ |
| 1. Título                | Identificação padronizada | Formato`N{X}.{Y} — Descrição curta`         |
| 2. Contexto Ubíquo       | Por que este card existe    | 2 a 3 frases autocontidas                        |
| 3. Descrição da Entrega | O que será produzido       | Verbo no infinitivo + artefato + localização   |
| 4. Critérios de Aceite   | Checklist binário          | Mínimo 3 itens mensuráveis                     |
| 5. Rastreabilidade        | Elo de auditoria            | TAP §X + EAP NX.Y + REQ-XX + Domínio PMBOK 7ª |
| 6. Dependências          | Pré-requisitos explícitos | Listar cards ou artefatos bloqueantes            |
| 7. Atribuição           | Responsável + esforço     | Nome completo + estimativa ≤ 8h                 |
| 8. Estado                 | Tags + milestone + status   | Mínimo 3 tags + milestone + status operacional  |

#### Padrão B — Card User Story (GWT) — padrão projetivo para M2

**Aplica-se a:** `feat`, `bug`, `test`.
**Status normativo:** Padrão definido nesta data, com aplicação efetiva a partir do marco M2 (30/09/2026).

| Campo                         | Função                    | Regra de preenchimento                                          |
| ----------------------------- | --------------------------- | --------------------------------------------------------------- |
| 1. Título                    | Identificação padronizada | Formato`N{X}.{Y} — US-{NN}: Descrição`                     |
| 2. User Story                 | Narrativa de valor          | `Como [papel], quero [ação], para [benefício mensurável]` |
| 3. Contexto Ubíquo           | Dor de negócio endereçada | 1 a 2 frases ligando a história ao público-alvo               |
| 4. Critérios de Aceite (GWT) | Comportamento verificável  | Blocos`Dado / Quando / Então`; mínimo 2 cenários           |
| 5. Regras de Negócio         | Restrições de domínio    | Spread, IOF, precisão decimal, regimes                         |
| 6. Rastreabilidade            | Elo de auditoria            | REQ-XX + EAP NX.Y + Domínio PMBOK 7ª                          |
| 7. Dependências              | Pré-requisitos técnicos   | Cards de arquitetura, DER ou API bloqueantes                    |
| 8. Atribuição               | Responsável + esforço     | Nome completo + estimativa ≤ 8h                                |
| 9. Estado                     | Tags + milestone + status   | Mínimo 3 tags + milestone + status operacional                 |

---

### 9.4 Sistema de Prioridade P0–P3

**Definição:** Escala complementar ao MoSCoW (que classifica valor de escopo) e foca em urgência temporal e criticidade de bloqueio.

| Peso | Definição                 | Critério objetivo                                                        | Ação no Kanban                                       |
| ---- | --------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------ |
| P0   | Crítico / Caminho crítico | Sem este card, o marco não é atingido ou ele bloqueia ≥ 2 outros cards | Execução imediata; WIP reservado; Daily obrigatória |
| P1   | Alto                        | Essencial para o marco, mas não bloqueia outros cards diretamente        | Execução na janela do marco                          |
| P2   | Médio                      | Importante, mas pode deslizar para o marco seguinte                       | Execução pós-marco atual                            |
| P3   | Baixo                       | Desejável; postergável sem impacto formal                               | Backlog priorizado; puxar apenas se capacidade sobrar  |

**Regra de desempate:** Se dois cards têm o mesmo peso, prioriza-se aquele que desbloqueia mais cards subsequentes.

**Trade-off declarado:** Um card `must` (MoSCoW) pode ser P2 se sua entrega puder deslizar para M2 sem violar o critério de aceite do M1.

---

## 10. BACKLOG DO MARCO M1 — CONSOLIDADO

### 10.1 Resumo dos 21 Cards

| #     | Card                               | Tipo  | Macro-Fase | Área             | Prioridade MoSCoW | Prioridade Temporal | Milestone | Status         |
| ----- | ---------------------------------- | ----- | ---------- | ----------------- | ----------------- | ------------------- | --------- | -------------- |
| M1-01 | Plano de Integração              | docs  | MF1        | area:integracao   | must              | P0                  | M1        | 🔄 pair-review |
| M1-02 | Plano de Escopo                    | docs  | MF1        | area:escopo       | must              | P0                  | M1        | 🔄 pair-review |
| M1-03 | Plano de Cronograma                | docs  | MF1        | area:cronograma   | must              | P0                  | M1        | ⏳ 21/09       |
| M1-04 | Plano de Custos                    | docs  | MF1        | area:custos       | must              | P0                  | M1        | ⏳ 21/09       |
| M1-05 | Plano Qualidade + PDCAs + Ishikawa | docs  | MF1        | area:qualidade    | must              | P0                  | M1        | ⏳ 21/09       |
| M1-06 | Requisitos Funcionais              | docs  | MF1        | area:escopo       | must              | P1                  | M1        | 🔄 pair-review |
| M1-07 | Requisitos Não Funcionais         | docs  | MF1        | area:qualidade    | must              | P1                  | M1        | 🔄 pair-review |
| M1-08 | Arquitetura da Solução           | docs  | MF1        | area:escopo       | must              | P2                  | M2        | ⏳ 30/09       |
| M1-09 | Protótipo UX/UI                   | docs  | MF1        | area:escopo       | should            | P3                  | M2        | ⏳ 30/09       |
| M1-10 | Modelagem de Dados (DER)           | docs  | MF1        | area:escopo       | must              | P2                  | M2        | ⏳ 30/09       |
| M1-11 | Seleção Stack FOSS (ADR-001)     | docs  | MF1        | area:recursos     | must              | P1                  | M1        | 🔄 in-review   |
| M1-12 | Repositório Git + CI/CD           | ci    | MF1        | area:integracao   | must              | P0                  | M1        | ⏳ 22/09       |
| M1-13 | Setup Local e Homologação        | chore | MF1        | area:recursos     | must              | P1                  | M1        | ⏳ 22/09       |
| M1-14 | Auditoria de Licenças FOSS        | docs  | MF1        | area:qualidade    | must              | P2                  | M2        | ⏳ 30/09       |
| M1-15 | ADR-001 Stack                      | docs  | MF1        | area:integracao   | must              | P1                  | M1        | 🔄 in-review   |
| M1-16 | ADR-002 Kanban                     | docs  | MF1        | area:integracao   | must              | P1                  | M1        | 🔄 in-review   |
| M1-17 | ADR-003 Métricas                  | docs  | MF1        | area:cronograma   | must              | P1                  | M1        | 🔄 in-review   |
| M1-18 | Lições Aprendidas MF1            | docs  | MF1        | area:integracao   | should            | P3                  | M2        | ⏳ 30/09       |
| M1-19 | Matriz RACI                        | docs  | MF1        | area:comunicacoes | should            | P2                  | M1        | ⏳ 22/09       |
| M1-20 | Canais Oficiais                    | docs  | MF1        | area:comunicacoes | should            | P2                  | M1        | ⏳ 22/09       |
| M1-21 | Labels + change-request            | chore | MF1        | area:integracao   | must              | P1                  | M1        | ⏳ 22/09       |

**Total:** 21 cards · 15 `must` · 6 `should` · 6 P0 · 8 P1 · 5 P2 · 2 P3

### 10.2 Cards que Receberão Tasklist (ADR-004)

| Card                                       | Estimativa | Justificativa                                         |
| ------------------------------------------ | ---------- | ----------------------------------------------------- |
| M1-01 (Plano de Integração)              | 6h         | Múltiplas seções; requer validação cruzada       |
| M1-02 (Plano de Escopo)                    | 6h         | Múltiplas seções; requer validação cruzada       |
| M1-05 (Plano Qualidade + PDCAs + Ishikawa) | 8h         | Múltiplos entregáveis (plano + 12 PDCAs + diagrama) |
| M1-08 (Arquitetura da Solução)           | 6h         | Diagrama + validação de componentes                 |
| M1-09 (Protótipo UX/UI)                   | 8h         | Wireframes + validação de usabilidade               |
| M1-10 (Modelagem de Dados DER)             | 6h         | Entidades + cardinalidades + validação SQLite       |
| M1-12 (Repositório Git + CI/CD)           | 6h         | Repositório + pipeline + Projects + labels           |

### 10.3 Distribuição de Trabalho por Membro

| Membro   | Cards P0            | Cards P1                   | Cards P2/P3 | Carga Total Estimada |
| -------- | ------------------- | -------------------------- | ----------- | -------------------- |
| Leonardo | M1-01, M1-12        | M1-15, M1-16, M1-17, M1-21 | M1-20       | ~14h                 |
| Fabricio | M1-02, M1-03, M1-04 | M1-06, M1-13               | M1-10       | ~13h                 |
| Edson    | M1-05               | M1-07                      | M1-19       | ~11h                 |

**Verificação:** Todos os membros estão dentro do limite de 20h/semana (Premissa P5) e do WIP limit de 3 cards/pessoa em `In Progress` (ADR-002).

# Análise Crítica — Sub-seção 10.2 e ADR-004

## Diagnóstico da Ambiguidade

A sub-seção 10.2 ("Cards que Receberão Tasklist") está **tecnicamente correta**, mas a redação atual pode gerar uma leitura equivocada:

| Leitura Possível                                     | Problema                                                               |
| ----------------------------------------------------- | ---------------------------------------------------------------------- |
| "Tasklist = subissue disfarçada"                     | ❌ Falso — tasklist é checklist**dentro** do corpo da Issue    |
| "Se subissue é vetada, como decompor cards grandes?" | ✅ Pergunta legítima — a resposta é:**via tasklist Markdown** |
| "Tasklist fragmenta o backlog como subissue faria?"   | ❌ Não — a tasklist não cria Issues filhas no GitHub Projects       |

**Raiz da ambiguidade:** A sub-seção 10.2 lista *quais* cards recebem tasklist, mas não explica *como* a tasklist contorna a ausência de subissues. O leitor (especialmente o Prof. Dr. Nivaldo Carleto em avaliação) pode questionar: "Se vocês vetaram subissues, como acompanham o progresso interno de um card de 8h?"

**Solução:** Adicionar uma sub-seção **10.2.1 — Mecanismo de Contorno: Tasklist como Substituto de Subissue** que explica explicitamente a relação.

---

## Sub-seção 10.2 Revisada (para OKB v3.0)

### 10.2 Cards que Receberão Tasklist (ADR-004)

**Regra de aplicação (ADR-004):**

- **Obrigatória** para cards com estimativa ≥ 6h ou múltiplos entregáveis.
- **Proibida** para cards atômicos (≤ 4h) ou em status `Code Review`/`Done`.
- **Formato canônico:** Mínimo 3 itens, máximo 7 itens; último item obrigatoriamente "Validação final".
- **Natureza binária:** Itens são "feito/não feito" (`- [ ]` / `- [x]`), sem status intermediário.

**Cards do M1 que receberão tasklist:**

| Card                                       | Estimativa | Justificativa                                         | Nº de Itens |
| ------------------------------------------ | ---------- | ----------------------------------------------------- | ------------ |
| M1-01 (Plano de Integração)              | 6h         | Múltiplas seções; requer validação cruzada       | 5            |
| M1-02 (Plano de Escopo)                    | 6h         | Múltiplas seções; requer validação cruzada       | 5            |
| M1-05 (Plano Qualidade + PDCAs + Ishikawa) | 8h         | Múltiplos entregáveis (plano + 12 PDCAs + diagrama) | 6            |
| M1-08 (Arquitetura da Solução)           | 6h         | Diagrama + validação de componentes                 | 4            |
| M1-09 (Protótipo UX/UI)                   | 8h         | Wireframes + validação de usabilidade               | 5            |
| M1-10 (Modelagem de Dados DER)             | 6h         | Entidades + cardinalidades + validação SQLite       | 4            |
| M1-12 (Repositório Git + CI/CD)           | 6h         | Repositório + pipeline + Projects + labels           | 6            |

**Total:** 7 cards com tasklist · 35 itens de checklist · 0 subissues criadas.

---

### 10.2.1 Mecanismo de Contorno: Tasklist como Substituto de Subissue

**Problema:** Cards complexos (≥ 6h) exigem visibilidade de progresso interno. A solução tradicional seria criar subissues (Issues filhas), mas isso foi **formalmente rejeitado** pela ADR-004 porque:

- Fragmenta o backlog no GitHub Projects (cada subissue vira um card independente)
- Distorce métricas de fluxo (Throughput e Cycle Time contariam sub-tarefas, não o entregável real)
- Viola o princípio GMV (overhead de gestão de múltiplas Issues para um único entregável)

**Contorno adotado:** Tasklist Markdown nativa do GitHub (`- [ ]` / `- [x]`) **dentro do corpo da Issue**. Este mecanismo:

| Propriedade                                  | Subissue (VETADA)  | Tasklist Markdown (ADOTADA)        |
| -------------------------------------------- | ------------------ | ---------------------------------- |
| Cria nova Issue no repositório?             | ✅ Sim             | ❌ Não                            |
| Aparece como card no GitHub Projects?        | ✅ Sim (fragmenta) | ❌ Não (permanece no card pai)    |
| Afeta métricas de fluxo (ADR-003)?          | ✅ Sim (distorce)  | ❌ Não (card pai é a unidade)    |
| Fornece visibilidade de progresso?           | ✅ Sim             | ✅ Sim (barra de progresso nativa) |
| Exige gestão de dependências entre Issues? | ✅ Sim (overhead)  | ❌ Não                            |
| Overhead de gestão                          | Alto               | Zero                               |

**Exemplo prático (Card M1-05 — Plano de Qualidade):**

~~~markdown
## Tasklist (ADR-004)

- [ ] Estrutura do Plano de Qualidade redigida (seções 1-8)
- [ ] 12 ciclos PDCA consolidados (um por fase da EAP)
- [ ] Diagrama de Ishikawa 6M desenhado e versionado
- [ ] Critérios de aceite vinculados a REQ-08, REQ-09, REQ-10
- [ ] Revisão em pares solicitada (Fabricio ou Leonardo)
- [ ] Validação final
~~~

**Regras operacionais:**

1. A tasklist é criada **no momento da abertura do card** (antes de migrar para `In Progress`).
2. Cada item é marcado como concluído (`- [x]`) **somente quando o critério daquele passo for objetivamente atendido**.
3. O card só migra para `Code Review` quando **100% dos itens estiverem marcados** (DoD, Plano de Escopo §2.6 item 8).
4. O GitHub exibe automaticamente uma **barra de progresso** no card (ex: "4 of 6 tasks complete"), fornecendo visibilidade sem fragmentação.

**Fundamentação PMBOK 7ª:** Domínio de Trabalho do Projeto — "O trabalho do projeto é executado por meio de atividades que produzem entregas. A decomposição do trabalho deve ser suficiente para permitir o controle, sem gerar overhead desnecessário."

**Trade-off aceito (ADR-004):** Simplicidade (GMV) > Granularidade de status de sub-tarefas. A unidade atômica de métrica permanece sendo o **card pai**, não os itens da tasklist.

---

## OKB v3.0 — Seção 10 Atualizada (Trecho Revisado)

Substituir a seção 10.2 anterior pela versão acima. As demais seções do OKB v3.0 permanecem inalteradas.

**Resumo da alteração:**

| Item                                    | Versão Anterior               | Versão Revisada                              |
| --------------------------------------- | ------------------------------ | --------------------------------------------- |
| Sub-seção 10.2                        | Lista de cards + justificativa | Lista + regras de aplicação + nº de itens  |
| Sub-seção 10.2.1                      | ❌ Inexistente                 | ✅ Mecanismo de contorno explicado            |
| Tabela comparativa Subissue vs Tasklist | ❌ Inexistente                 | ✅ 6 propriedades comparadas                  |
| Exemplo prático de tasklist            | ❌ Inexistente                 | ✅ Card M1-05 com 6 itens                     |
| Regras operacionais (4 regras)          | ❌ Inexistente                 | ✅ Quando criar, quando marcar, quando migrar |
| Fundamentação PMBOK 7ª               | ❌ Inexistente                 | ✅ Domínio de Trabalho do Projeto            |
| Trade-off explícito                    | Implícito                     | ✅ Declarado formalmente                      |

**Verificação de congruência:**

| Item                                              | Status                             |
| ------------------------------------------------- | ---------------------------------- |
| ADR-004 coerente com sub-seção 10.2             | ✅ OK                              |
| Subissues explicitamente vetadas                  | ✅ OK                              |
| Tasklists explicitamente adotadas como contorno   | ✅ OK                              |
| Métricas de fluxo (ADR-003) não afetadas        | ✅ OK                              |
| WIP limits (ADR-002) não afetados                | ✅ OK                              |
| DoD do Plano de Escopo §2.6 item 8 referenciado  | ✅ OK                              |
| Prof. Dr. Nivaldo Carleto por extenso (se citado) | ✅ N/A (não citado nesta seção) |
| Princípio GMV respeitado                         | ✅ OK                              |

**Status:** Sub-seção 10.2 revisada — pronta para incorporação ao OKB v3.0. Nenhuma contradição residual com ADR-004.

---

## 11. VERIFICAÇÃO DE CONGRUÊNCIA

| Item                                                              | Status |
| ----------------------------------------------------------------- | ------ |
| OKB v3.0 substitui formalmente OKB v2.2                           | ✅ OK  |
| ADR-004 incorporada na seção 4 (ADRs Emitidas)                  | ✅ OK  |
| Seção de Literatura de Apoio (Questões Adjacentes) criada      | ✅ OK  |
| Configuração do GitHub formalizada (tags, milestones, backlog)  | ✅ OK  |
| Fronteira M1 corrigida (5 planos, não 8)                         | ✅ OK  |
| Estratégia de Entrega Faseada documentada (§1.4)                | ✅ OK  |
| Sistema de tags expandido de 23 para 27 labels (inclusão P0–P3) | ✅ OK  |
| Padrão de redação de cards definido (Padrão A + Padrão B)    | ✅ OK  |
| Sistema de prioridade P0–P3 formalizado                          | ✅ OK  |
| Tasklists Markdown (ADR-004) integradas ao DoD                    | ✅ OK  |
| Prof. Dr. Nivaldo Carleto sempre por extenso                      | ✅ OK  |
| EVM declarado LEGADO — NÃO APLICÁVEL                           | ✅ OK  |
| Obsolescência PMBOK 6ª declarada formalmente                    | ✅ OK  |
| Rastreabilidade TAP → OKB → ADRs preservada                     | ✅ OK  |
| Princípio GMV respeitado em todas as seções                    | ✅ OK  |

---

**OKB v3.0 emitido por:** GP Leonardo David Silva Setti
**Aprovação:** CCB (GP — membro único, TAP v3 §1.c)
**Data:** 20/09/2026
**Status:** ✅ Convergente ao TAP v3 + ADRs 001–004 — pronto para M1
**Substitui:** OKB v2.2 (19/09/2026)

---

*Fim do documento — OKB v3.0 | COGME | Fatec Taquaritinga | 20/09/2026

# Aditivo:

# Política de ADRs e Integração Documental — COGME

**Domínio PMBOK 7ª:** Trabalho do Projeto + Incerteza + Abordagem de Desenvolvimento
**Processo PMBOK 6ª (dicionário):** 4.4 — Gerenciar o Conhecimento do Projeto
**Rastreabilidade:** TAP §3 (Inovação) + REQ-12 + Plano de Integração §1.5.2 + ADR-002
**Princípio norteador:** GMV (Governança Mínima Viável)

---

## 1. Gatilhos para Criação de Novas ADRs

### 1.1 Critério Formal Vigente (Plano de Integração §1.5.2)

O gatilho atual declara:

> *"Decisões que afetam ≥ 2 fases da EAP, envolvem troca de tecnologia ou seriam questionadas pelo Prof. Dr. Nivaldo Carleto em avaliação são formalmente registradas via ADR."*

Este critério é necessário mas **insuficiente** para operacionalização diária. Abaixo, formalizo uma matriz de gatilhos completa, alinhada ao GMV.

### 1.2 Matriz de Gatilhos (Teste de 4 Perguntas)

Uma decisão **exige** ADR se atender a **pelo menos 2** dos 4 critérios abaixo. Se atender a apenas 1, registra-se em commit message. Se não atender a nenhum, não se registra formalmente.

| #  | Critério                                                                                                                             | Exemplo no COGME                                                     | Domínio PMBOK 7ª           |
| -- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------- |
| G1 | **Impacto transversal:** Afeta ≥ 2 fases da EAP ou ≥ 2 planos de área                                                        | ADR-003 (métricas) impacta Cronograma + Integração + Qualidade    | Planejamento + Medição     |
| G2 | **Irreversibilidade prática:** Reverter a decisão custaria > 8h de retrabalho                                                 | ADR-001 (stack) — trocar FastAPI por Flask reescreve backend        | Abordagem de Desenvolvimento |
| G3 | **Questionabilidade acadêmica:** O Prof. Dr. Nivaldo Carleto poderia questionar a decisão na avaliação de um marco          | ADR-004 (tasklists vs subissues) — "por que não usaram subissues?" | Stakeholders                 |
| G4 | **Trade-off não óbvio:** A decisão abre mão de uma alternativa viável em favor de outra, e a justificativa não é trivial | ADR-002 (Kanban sem sprints) — abre mão de iterações time-boxed  | Abordagem de Desenvolvimento |

**Regra GMV:** Se a decisão atende a apenas 1 critério → commit message com prefixo `decision:`. Se atende a 0 → não se registra.

### 1.3 Gatilhos Específicos por Fase do Ciclo de Vida

| Fase                 | Gatilho Provável                                                                        | Exemplo                                                   |
| -------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| MF1 (Fundação)     | Seleção de stack, método de execução, métricas, configuração SSOT                | ADRs 001–004 (já emitidas)                              |
| MF2 (Construção)   | Troca de biblioteca, padrão arquitetural, estratégia de teste, decisão de API externa | Ex: "Adotar httpx vs requests para chamadas assíncronas" |
| MF3 (Consolidação) | Estratégia de release, formato de documentação final, decisão de licenciamento       | Ex: "MIT vs GPLv3 para release final"                     |
| Transversal          | Mudança de marco, alteração de escopo do MVP, contingência de risco materializado    | Ex: "Reduzir REQ-06 para MVP se M3 estiver em risco"      |

### 1.4 Gatilhos Negativos (Quando NÃO Criar ADR)

| Situação                                                        | Ação Correta                              | Justificativa GMV             |
| ----------------------------------------------------------------- | ------------------------------------------- | ----------------------------- |
| Decisão de formatação de código (lint, indentação)          | Configuração no`.editorconfig` + commit | Não afeta ≥ 2 fases         |
| Escolha de nome de variável ou função                          | Commit message                              | Reversível em < 5min         |
| Ajuste de texto em plano (sem mudança de escopo)                 | Commit`docs(plano-X): ajuste §Y`         | Não é decisão arquitetural |
| Decisão já coberta por ADR existente                            | Referência à ADR no commit                | Evita proliferação          |
| Decisão operacional do dia a dia (ex: "hoje trabalho no card X") | Daily assíncrona                           | Não é decisão de projeto   |

---

## 2. ADR Tardia — Trade-offs e Política de Regularização

### 2.1 Definição

Uma **ADR tardia** é aquela emitida **após** a decisão já ter sido implementada ou operacionalizada. No COGME, a ADR-004 (Tasklists Markdown, 20/09/2026) é o exemplo: a decisão já estava sendo aplicada quando foi formalizada.

### 2.2 Matriz de Trade-offs

| Dimensão                            | ADR Tempestiva (antes da execução)                           | ADR Tardia (após a execução)                        |
| ------------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------ |
| **Rastreabilidade**            | ✅ Plena — decisão precede ação                            | ⚠️ Parcial — ação precede registro                |
| **Custo de produção**        | Baixo (contexto fresco)                                        | Médio (requer reconstrução do raciocínio)          |
| **Risco de perda de contexto** | Baixo                                                          | Alto (detalhes da deliberação se perdem)             |
| **Blindagem acadêmica**       | ✅ Máxima (Prof. Dr. Nivaldo Carleto vê coerência temporal) | ⚠️ Reduzida (pode parecer racionalização post hoc) |
| **Overhead burocrático**      | Baixo (integra-se ao fluxo natural)                            | Médio (exige parada para documentar)                  |
| **Valor para a equipe**        | Alto (guia a execução)                                       | Médio (documenta o que já foi feito)                 |

### 2.3 Política de Regularização (Regra GMV)

| Condição                                              | Ação                                                                                              | Prazo                        |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------- |
| Decisão implementada há ≤ 48h e atende ≥ 2 gatilhos | Emitir ADR tardia com nota`"Regularização: decisão aplicada em [data], formalizada em [data]"` | ≤ 24h após identificação |
| Decisão implementada há > 48h e atende ≥ 2 gatilhos  | Emitir ADR tardia + registrar lição aprendida ("decisão não formalizada tempestivamente")       | ≤ 72h                       |
| Decisão implementada e atende apenas 1 gatilho         | NÃO emitir ADR; registrar em commit com prefixo`decision:`                                       | Imediato                     |
| Decisão implementada e atende 0 gatilhos               | Não registrar formalmente                                                                          | —                           |

### 2.4 Estrutura Obrigatória da ADR Tardia

Além dos campos padrão (Contexto, Opções, Decisão, Consequências, Trade-offs), a ADR tardia **deve** incluir:

~~~markdown
**Tipo:** Regularização tardia
**Data da decisão efetiva:** [data em que foi aplicada]
**Data da formalização:** [data de emissão da ADR]
**Motivo da tardança:** [ex: "priorização de entrega do M1 sobre documentação"]
**Lição aprendida:** [ação preventiva para evitar recorrência]
~~~

**Trade-off declarado:** Aceita-se a ADR tardia como mal menor em relação à ausência total de registro, mas desincentiva-se sua recorrência. Se > 30% das ADRs do projeto forem tardias, o GP deve revisar o fluxo de trabalho na Retrospectiva.

---

## 3. Arquitetura de Integração Documental

### 3.1 Princípio Diretor

> **Documentos de governança são standalone; planos de área são coordenados; cross-references substituem duplicação.**

Este princípio deriva do GMV e do Domínio de Trabalho do Projeto (PMBOK 7ª): cada artefato tem **uma única localização canônica** (SSOT informacional), e os demais artefatos **referenciam** essa localização sem copiar conteúdo.

### 3.2 Estrutura de Diretórios no Repositório

~~~
/docs/
├── planos/
│   ├── plano-integracao.md        ← Coordenador (referencia todos os demais)
│   ├── plano-escopo.md
│   ├── plano-cronograma.md
│   ├── plano-custos.md
│   ├── plano-qualidade.md
│   ├── plano-recursos.md          ← M2
│   ├── plano-comunicacoes.md      ← M2
│   └── plano-riscos.md            ← M2
├── decisoes/
│   ├── ADR-001-stack.md
│   ├── ADR-002-kanban.md
│   ├── ADR-003-metricas.md
│   ├── ADR-004-tasklists.md
│   └── ADR-005-[futura].md
├── conhecimento/
│   ├── OKB.md                     ← Operational Knowledge Base
│   ├── glossario.md               ← Glossário
│   └── licoes-aprendidas/
│       ├── MF1-licoes.md
│       ├── MF2-licoes.md
│       └── MF3-licoes.md
├── metricas/
│   └── baseline.md                ← Pós-calibração (03/10)
└── requisitos/
    └── requisitos.md              ← REQ-01 a REQ-15 (consolidados)
~~~

### 3.3 Estratégia de Integração: Cross-Reference vs. Anexo vs. Seção

| Documento                       | Estratégia                                                                                              | Justificativa GMV                                                                  |
| ------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **ADRs**                  | **Standalone** em `/docs/decisoes/` + tabela-resumo no Plano de Integração                     | ADRs são autocontidas; duplicá-las nos planos violaria SSOT e inflaria extensão |
| **OKB**                   | **Standalone** em `/docs/conhecimento/OKB.md` + referência no Plano de Integração §1.1       | OKB é documento de governança transversal; não pertence a uma área específica |
| **Glossário**            | **Standalone** em `/docs/conhecimento/glossario.md` + referência no Plano de Integração §1.1 | Mesmo princípio; glossário é infraestrutura linguística do projeto             |
| **Lições Aprendidas**   | **Standalone** em `/docs/conhecimento/licoes-aprendidas/` + resumo no encerramento de cada MF    | Acumulação temporal; não faz sentido embutir em planos                          |
| **Baseline de Métricas** | **Standalone** em `/docs/metricas/baseline.md` + referência no Plano de Cronograma §2.3        | Dado empírico; não é texto normativo                                            |

### 3.4 O que NÃO Fazer (Anti-Padrões)

| Anti-Padrão                                                                       | Por que viola GMV                                                   | Ação Correta                                                          |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Copiar o texto integral da ADR-003 dentro do Plano de Cronograma                   | Duplicação; se a ADR for atualizada, o plano fica desatualizado   | Referenciar:*"Conforme ADR-003 (/docs/decisoes/ADR-003-metricas.md)"* |
| Criar uma seção "Anexos" no final de cada plano com todos os documentos externos | Infla extensão; viola limite de 4 páginas (GMV)                   | Cross-reference inline                                                  |
| Embutir o Glossário como seção do Plano de Integração                         | Glossário é transversal a todos os planos; não pertence a um só | Standalone + referência                                                |
| Criar um "Super-Documento" que contém TAP + todos os planos + ADRs + Glossário   | Viola SSOT; impossibilita versionamento granular                    | Documentos separados, coordenados pelo Plano de Integração            |

### 3.5 Mecanismo de Cross-Reference (Padrão Canônico)

Em qualquer plano de área, quando for necessário referenciar um documento externo, usa-se o seguinte formato:

~~~markdown
Conforme [ADR-003 — Métricas de Fluxo](/docs/decisoes/ADR-003-metricas.md), 
as métricas EVM são declaradas LEGADO.

Conforme [OKB v3.0 §1.4 — Estratégia de Entrega Faseada](/docs/conhecimento/OKB.md#14), 
o M1 contempla 5 planos.

Conforme [Glossário — Termo "CFD"](/docs/conhecimento/glossario.md#4-metodologia-ágil--kanban), 
o Cumulative Flow Diagram é a visualização gráfica do fluxo acumulado.
~~~

### 3.6 Tabela-Resumo no Plano de Integração (Seção 1.1 — Adendo Proposto)

Para que o Prof. Dr. Nivaldo Carleto tenha visibilidade integral sem abrir cada documento, o Plano de Integração deve conter uma **tabela-índice** na seção 1.1 ou como adendo à seção 1.4:

~~~markdown
### 1.4.1 Índice de Documentos de Governança Transversal

| Documento | Localização | Função | Última Versão |
|-----------|-------------|--------|---------------|
| OKB | /docs/conhecimento/OKB.md | Base de conhecimento operacional | v3.0 |
| Glossário | /docs/conhecimento/glossario.md | Vocabulário padronizado | v2.2 |
| ADR-001 | /docs/decisoes/ADR-001-stack.md | Stack tecnológica FOSS | Aprovada |
| ADR-002 | /docs/decisoes/ADR-002-kanban.md | Kanban como método | Aprovada |
| ADR-003 | /docs/decisoes/ADR-003-metricas.md | Métricas de fluxo | Aprovada |
| ADR-004 | /docs/decisoes/ADR-004-tasklists.md | Tasklists Markdown | Aprovada |
| Baseline | /docs/metricas/baseline.md | Dados empíricos de fluxo | ⏳ Pós 03/10 |
| Lições MF1 | /docs/conhecimento/licoes-aprendidas/MF1.md | Aprendizados da Fundação | ⏳ 30/09 |
~~~

---

## 4. Ciclo de Vida da ADR no Fluxo Kanban

### 4.1 Integração com o GitHub Projects

| Evento Kanban                                      | Ação sobre ADR                                                               |
| -------------------------------------------------- | ------------------------------------------------------------------------------ |
| Card com label`change-request` aprovado pelo CCB | Se a mudança atende ≥ 2 gatilhos → criar card de ADR                        |
| Card de ADR criado                                 | Tipo:`docs` · Área: `area:integracao` · Macro-fase: vigente             |
| ADR em`In Progress`                              | GP redige (estimativa ≤ 2h por ADR)                                           |
| ADR em`Code Review`                              | Revisão por 1 par (Fabricio ou Edson)                                         |
| ADR em`Done`                                     | Commit`docs(adr): ADR-0XX — [título]` + atualização da tabela no OKB §4 |

### 4.2 Limite de ADRs por Marco (GMV)

| Marco      | Máximo de ADRs novas      | Justificativa                                                     |
| ---------- | -------------------------- | ----------------------------------------------------------------- |
| M1 (22/09) | 4 (já emitidas: 001–004) | Fundação completa; não adicionar mais                          |
| M2 (30/09) | ≤ 2                       | Ex: ADR de baseline de métricas + eventual ajuste de stack       |
| M3 (15/11) | ≤ 3                       | Ex: padrão de API, estratégia de teste, fallback de API externa |
| M4 (15/12) | ≤ 1                       | Ex: decisão de licenciamento final                               |

**Total projetado:** ≤ 10 ADRs ao longo do ciclo de vida. Acima disso, o GP deve questionar se o projeto está burocratizando decisões menores.

---

## 5. Síntese e Verificação de Congruência

| Item                                                                      | Status |
| ------------------------------------------------------------------------- | ------ |
| Gatilhos de criação definidos (4 critérios, mínimo 2)                 | ✅     |
| Gatilhos negativos definidos (quando NÃO criar)                          | ✅     |
| Política de ADR tardia com trade-offs declarados                         | ✅     |
| Estrutura de ADR tardia com campos obrigatórios                          | ✅     |
| Arquitetura de integração documental definida                           | ✅     |
| Estratégia: standalone + cross-reference (não anexo, não duplicação) | ✅     |
| Tabela-índice no Plano de Integração proposta                          | ✅     |
| Limite de ADRs por marco (GMV) definido                                   | ✅     |
| Integração com fluxo Kanban (GitHub Projects) definida                  | ✅     |
| Domínio PMBOK 7ª citado em cada seção                                 | ✅     |
| Prof. Dr. Nivaldo Carleto por extenso                                     | ✅     |
| Princípio GMV respeitado em todas as decisões                           | ✅     |
| Obsolescência PMBOK 6ª mantida (dicionário apenas)                     | ✅     |

---

**Decisão final do GP:** Esta política entra em vigor imediatamente. A próxima ADR (ADR-005, se necessária) deve seguir integralmente os critérios aqui definidos. A tabela-índice (§1.4.1) será incorporada ao Plano de Integração na próxima revisão (v1.1), antes do M2.

**Ação imediata:** Nenhuma. As 4 ADRs existentes estão conformes. A política documentada nesta resposta será versionada como seção do OKB v3.1 ou como adendo ao Plano de Integração §1.5.2, conforme decisão no Refinement de 23/09.
