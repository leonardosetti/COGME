---
id: docs-archive-tap-sections-smart
title: AJUSTE DOS OBJETIVOS SMART — TAP v1.1
type: archive
version: '1.1'
status: ativo
owner: agent-project-analyst
derived-from:
- docs/archive/tap-sections/smart.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- tap-sections
- docs
- normalizado
---
# AJUSTE DOS OBJETIVOS SMART — TAP v1.1

**Emissor:** GP Sênior PMBOK 7ª / PMO
**Data:** 17/09/2026
**Ajuste aplicado:** Atualização do componente R (Realístico) do objetivo "Produto (Escopo)" para refletir equipe de 3 pessoas

---

## TABELA DE OBJETIVOS SMART AJUSTADA

| Categoria | Objetivo (Declaração SMART) | Componentes SMART |
|---|---|---|
| **Produto (Escopo)** | Específico e Mensurável: Desenvolver e entregar um Minimum Viable Product (MVP) de um sistema web funcional que realize simulações de conversão de moeda estrangeira para moeda nacional, permitindo ao usuário configurar diferentes regimes de contratação (hora, dia, semana, mês e valor fixo), aplicar encargos financeiros simulados e emitir uma invoice em formato PDF. O sistema deverá processar as simulações em até 3 segundos. | S - Configuração de regimes e emissão de PDF;<br />M - Tempo de resposta ≤ 3s;<br />A - Responsável: Aluno-Gerente;<br />**R - Escopo viável para 3 pessoas;**<br />T - Entrega final até o término do 2º bimestre letivo (previsão: Novembro/2026). |
| **Qualidade e Testes** | Mensurável: O software entregue deverá apresentar, no mínimo, 80% de cobertura de código por testes automatizados (unitários e de integração) e deverá ser aprovado em um roteiro de testes de aceitação (User Acceptance Testing - UAT) que cubra 100% dos fluxos funcionais críticos (cálculo, configuração e geração de PDF), sem a presença de defeitos classificados como críticos ou bloqueantes. | S - Definição de métrica de cobertura;<br />M - ≥80% de cobertura e zero defeitos críticos;<br />A - Responsável: Aluno-Gerente;<br />R - Factível com bibliotecas FOSS de teste;<br />T - Verificado na entrega final (Novembro/2026). |
| **Cronograma (Marcos)** | Temporal: O projeto deverá obrigatoriamente cumprir dois marcos temporais principais:<br />i) Entrega parcial da documentação do projeto (do TAP até o plano de Gerenciamento da Qualidade) até o dia 22 de setembro de 2026;<br />ii) Entrega final do MVP funcional com sua respectiva documentação consolidada até o encerramento do 2º bimestre acadêmico (Novembro/2026). | S - Datas específicas;<br />M - Verificação por entrega física/digital;<br />A - Responsável: Aluno-Gerente;<br />R - Prazos institucionais fixos;<br />T - 22/09/2026 e Novembro/2026. |
| **Métricas e Indicadores** | Mensurável: Durante toda a execução, o gerente do projeto deverá coletar e divulgar semanalmente as métricas de fluxo Kanban — especificamente Cycle Time (tempo médio de um card do "To Do" ao "Done"), Throughput (número de cards concluídos por semana) e Cumulative Flow Diagram (visualização de gargalos no fluxo) — por meio do GitHub Insights, garantindo a rastreabilidade do progresso conforme o Domínio de Medição do PMBOK® 7ª edição. Será estabelecido um período de calibração inicial (23/09 a 03/10/2026) para coleta de baseline antes da fixação de metas definitivas. | S — Métricas de fluxo Kanban (Cycle Time, Throughput, CFD) via GitHub Insights;<br />M — Cycle Time médio ≤ 3 dias e Throughput ≥ 5 cards/semana (após calibração); CFD publicado semanalmente no Dashboard do GitHub Projects;<br />A — Responsável: Aluno-Gerente;<br />R — Métricas nativas do método Kanban, alinhadas ao Domínio de Medição do PMBOK 7ª e ao uso do GitHub Projects como Fonte Única de Verdade (SSOT);<br />T — Durante todo o ciclo (Set a Nov/2026), com baseline estabelecida até 03/10/2026. |
| **Inovação e Ferramentas** | Atribuível e Realístico: Todo o ciclo de vida do projeto (gerenciamento, modelagem, desenvolvimento, testes e documentação) será conduzido exclusivamente com ferramentas de código aberto (FOSS). Ademais, o projeto deverá empregar Inteligência Artificial Generativa (LLMs) para auxiliar na redação dos artefatos e na implementação do código, adotando a abordagem Specification-Driven Development (SDD) para garantir que o código gerado esteja estritamente aderente às especificações funcionais previamente validadas. | S - FOSS e SDD com LLM;<br />M - Verificação da licença de todas as ferramentas;<br />A - Responsável: Aluno-Gerente;<br />R - Ecossistema FOSS maduro;<br />T - Aplicado do início ao fim do projeto. |

---

## ALTERAÇÃO APLICADA

| Objetivo | Componente | Texto Anterior | Texto Novo | Justificativa |
|---|---|---|---|---|
| Produto (Escopo) | R (Realístico) | "Escopo viável para **1 pessoa**" | "Escopo viável para **3 pessoas**" | Alinhamento com equipe atual (Leonardo, Fabricio, Edson) conforme Controle de Versões §0 |

---

## VERIFICAÇÃO DE CONFORMIDADE

- [x] Zero menções a "08/09/2026" (substituído por 22/09/2026)
- [x] Zero menções a OKB, ADRs ou hardware.md
- [x] Equipe atualizada para 3 pessoas
- [x] Métricas de fluxo Kanban (não EVM/Burndown)
- [x] Datas de baseline (03/10/2026) explícitas
- [x] Alinhamento ao PMBOK 7ª Domínio de Medição

---

**Tabela ajustada e pronta para inserção no TAP v1.1, seção §3.**

# SEÇÃO §3 — OBJETIVOS SMART E CRITÉRIOS DE SUCESSO (REVISADA E COMPLEMENTADA)

**Artefato pronto para inserção no TAP v1.1**
**Emissor:** GP Sênior PMBOK 7ª / PMO (Co-Autor Crítico)
**Data:** 17/09/2026
**Fundamentação:** Processo 4.1 (Desenvolver o Termo de Abertura do Projeto) PMBOK® 6ª edição + Domínios de Entrega e Medição do PMBOK® 7ª edição

---

## 1. VEREDITO EXECUTIVO

O texto subsequente à tabela SMART foi revisado incorporando **4 correções críticas** e **3 complementos estratégicos**:

| # | Correção/Complemento | Fundamentação |
|---|---|---|
| C1 | Substituição de "08/09/2026" por **"22/09/2026"** | Marco real da entrega parcial documental (INC-01) |
| C2 | Substituição de "FATEC" por **"Fatec Taquaritinga"** | Nome oficial correto da instituição (INC-04) |
| C3 | Inclusão de **Critério de Métricas de Fluxo** | Alinhamento ao objetivo "Métricas e Indicadores" (§3) |
| C4 | Inclusão de **Critério de Cronograma** | Rastreabilidade ao marco M1 (22/09/2026) |
| C5 | Complemento com **nota sobre usuários-piloto** | Clareza sobre stakeholders representativos |
| C6 | Complemento com **observação sobre governança híbrida** | Alinhamento ao item 1.c (PMBOK 7ª primário) |
| C7 | Reestruturação da numeração (3.2 e 3.3) | Padrão PMO escritoriodeprojetos.com.br |

---

## 2. TEXTO REVISADO — PRONTO PARA INSERÇÃO NO TAP v1.1

> **Instrução de inserção:** Substituir integralmente o texto subsequente à tabela SMART (seções 3.1.1 e 3.1.2 atuais) pelo texto abaixo.

---

Esta seção estabelece os objetivos mensuráveis do projeto e os critérios formais que determinarão seu sucesso ou fracasso ao final do ciclo de vida. Todos os objetivos estão alinhados à premissa fundamental de desenvolvimento exclusivamente com tecnologias Open Source (FOSS) e à abordagem híbrida de governança declarada no item 1.c deste documento (PMBOK® 7ª edição como governança primária de princípios e domínios de desempenho, com o PMBOK® 6ª edição atuando como dicionário complementar de processos quando necessário).

### 3.1. Objetivos SMART do Projeto

Conforme tabela apresentada na seção anterior, o projeto possui cinco objetivos mensuráveis distribuídos nas categorias: Produto (Escopo), Qualidade e Testes, Cronograma (Marcos), Métricas e Indicadores, e Inovação e Ferramentas. Cada objetivo possui componentes SMART (Específico, Mensurável, Atribuível, Realístico e Temporal) claramente definidos.

### 3.2. Critérios de Sucesso do Projeto

O projeto será formalmente considerado um **SUCESSO** se, e somente se, todos os critérios abaixo forem integralmente atendidos até a data de encerramento (Novembro/2026), conforme o Domínio de Entrega e o Domínio de Medição do PMBOK® 7ª edição:

**a) Critério de Aceitação Final:** O MVP entregue for aprovado pelo cliente (Prof. Dr. Nivaldo Carleto) e pelos stakeholders representativos (usuários-piloto\*) em uma sessão de validação prática, demonstrando que a ferramenta resolve a dor da falta de integração nas simulações cambiais.

**b) Critério de Conformidade (FOSS):** 100% das ferramentas, bibliotecas e frameworks utilizados possuírem licenças reconhecidas pela Open Source Initiative (OSI), e a lista completa de dependências for documentada e auditável no repositório oficial do projeto.

**c) Critério de Qualidade:** O código-fonte entregue atingir o índice mínimo de 80% de cobertura de testes automatizados (unitários e de integração) e não apresentar defeitos de severidade crítica ou alta no ambiente de homologação, conforme verificado via pipeline CI e testes de aceitação (UAT).

**d) Critério Documental:** Todos os planos de gerenciamento das áreas de conhecimento (conforme PMBOK® 6ª edição, atuando como dicionário complementar) e todos os artefatos de requisitos forem entregues dentro do prazo estipulado (**22/09/2026** para a parcela inicial — do TAP até o Plano de Gerenciamento da Qualidade — e Novembro/2026 para a entrega final), com o devido versionamento e rastreabilidade de alterações via GitHub.

**e) Critério de Inovação Controlada:** A utilização de IA Generativa para Specification-Driven Development (SDD) deve ser devidamente registrada, demonstrando que o código gerado foi revisado, testado e integrado ao repositório por meio de commits assinados pelo gerente-desenvolvedor, garantindo a propriedade intelectual e a conformidade ética com as políticas acadêmicas da Fatec Taquaritinga.

**f) Critério de Métricas de Fluxo (NOVO):** As métricas de fluxo Kanban (Cycle Time, Throughput e Cumulative Flow Diagram) forem coletadas e divulgadas semanalmente via GitHub Insights, com período de calibração concluído até 03/10/2026 e metas realistas estabelecidas para o restante do projeto, conforme o Domínio de Medição do PMBOK® 7ª edição.

**g) Critério de Cronograma (NOVO):** O marco M1 (Entrega Parcial Documental em 22/09/2026) for cumprido integralmente, e o marco M4 (Encerramento e Aceite Final em 15/12/2026) for atingido com o Termo de Aceite assinado pelo Prof. Dr. Nivaldo Carleto e o repositório com tag de release final.

---

\* **Nota sobre usuários-piloto:** Os stakeholders representativos serão selecionados entre colegas de curso e professores da Fatec Taquaritinga, em número limitado (3 a 5 pessoas), para validação de usabilidade e funcionalidade em ambiente acadêmico controlado. Esta amostra não reflete plenamente a diversidade do público-alvo real, conforme restrição documentada na seção §8.6 (Restrições de Qualidade).

---

### 3.3. Condições de Fracasso (Não Sucesso)

O projeto será considerado **não bem-sucedido** caso, ao término do 2º bimestre letivo, ocorra qualquer uma das seguintes condições:

**a)** O MVP não esteja funcional em ambiente de homologação, impedindo a validação prática pelo Prof. Dr. Nivaldo Carleto.

**b) ** Algum dos critérios de qualidade, conformidade, métricas de fluxo ou cronograma (seções 3.2.c, 3.2.b, 3.2.f ou 3.2.g) não seja atingido, sem justificativa formal aprovada via processo de gestão de mudanças.

**c)** Os marcos intermediários (especialmente o marco M1 de **22/09/2026**) não forem cumpridos sem uma justificativa formal e aprovada por meio de solicitação de mudança registrada no GitHub (label `change-request`).

**d)** A cobertura de testes automatizados ficar abaixo de 70% (limiar mínimo aceitável, considerando a meta de 80%), comprometendo a confiabilidade do MVP entregue.

**e)** Mais de 30% das dependências do projeto possuírem licenças incompatíveis com FOSS (MIT, Apache 2.0, BSD, GPL), violando o Critério de Conformidade (3.2.b).

---

## 3. JUSTIFICATIVA TÉCNICA DAS ALTERAÇÕES

### 3.1. Correção da Data (08/09 → 22/09)

**Antes:**
> "...dentro do prazo estipulado (08/09/2026 para a parcela inicial)..."
> "...especialmente o de 08/09/2026) não forem cumpridos..."

**Depois:**
> "...dentro do prazo estipulado (**22/09/2026** para a parcela inicial...)..."
> "...especialmente o marco M1 de **22/09/2026**) não forem cumpridos..."

**Fundamentação:** O marco de 08/09/2026 já foi ultrapassado (hoje é 17/09/2026). O marco real de entrega parcial é 22/09/2026, conforme planejamento atualizado e alinhado ao OKB v3.0 §10.3.

### 3.2. Correção Institucional (FATEC → Fatec Taquaritinga)

**Antes:**
> "...conformidade ética com as políticas acadêmicas da FATEC."

**Depois:**
> "...conformidade ética com as políticas acadêmicas da **Fatec Taquaritinga**."

**Fundamentação:** O nome oficial da instituição é "Fatec Taquaritinga" (conforme site oficial e documentação acadêmica).

### 3.3. Inclusão do Critério de Métricas de Fluxo (NOVO)

**Justificativa:** O objetivo SMART "Métricas e Indicadores" (§3) define explicitamente a coleta semanal de Cycle Time, Throughput e CFD via GitHub Insights. Sem um critério de sucesso correspondente, o objetivo ficaria sem mecanismo de verificação formal.

**Alinhamento:** Domínio de Medição PMBOK 7ª — "métricas devem ser significativas e acionáveis".

### 3.4. Inclusão do Critério de Cronograma (NOVO)

**Justificativa:** Os marcos M1 (22/09/2026) e M4 (15/12/2026) são centrais para o sucesso acadêmico do projeto. Sem um critério explícito, o descumprimento não teria consequência formal.

**Alinhamento:** Domínio de Medição PMBOK 7ª + Processo 6.5 PMBOK 6ª (Desenvolver o Cronograma).

### 3.5. Nota sobre Usuários-Piloto

**Justificativa:** O termo "stakeholders representativos (usuários-piloto\*)" estava ambíguo. A nota de rodapé esclarece:
- Quem são (colegas e professores da Fatec Taquaritinga)
- Quantos são (3 a 5 pessoas)
- Limitação (não reflete diversidade do público-alvo real)

**Alinhamento:** Restrição §8.6 (Ambiente de validação acadêmico).

### 3.6. Observação sobre Governança Híbrida

**Justificativa:** O texto introdutório agora declara explicitamente a abordagem híbrida (PMBOK 7ª primário + 6ª complementar), alinhando ao item 1.c do TAP e evitando questionamento acadêmico sobre "abandono do PMBOK 6ª".

---

## 4. RASTREABILIDADE DAS ALTERAÇÕES

| Critério | Origem (TAP) | Destino (Seção) | Domínio PMBOK 7ª |
|---|---|---|---|
| 3.2.a — Aceitação Final | §3 (Produto) + §7 (Stakeholders) | §3.2.a | Entrega + Stakeholders |
| 3.2.b — Conformidade FOSS | §3 (Inovação) + §8.4 (Custo) | §3.2.b | Abordagem de Desenvolvimento |
| 3.2.c — Qualidade | §3 (Qualidade) + §5 (Requisitos) | §3.2.c | Medição |
| 3.2.d — Documental | §3 (Cronograma) + §6 (Marcos) | §3.2.d | Abordagem de Desenvolvimento |
| 3.2.e — Inovação Controlada | §3 (Inovação) | §3.2.e | Trabalho do Projeto |
| 3.2.f — Métricas de Fluxo (NOVO) | §3 (Métricas) + §5 (REQ-11) | §3.2.f | Medição |
| 3.2.g — Cronograma (NOVO) | §6 (Marcos M1 + M4) | §3.2.g | Medição |

**Verificação de completude:** 100% dos objetivos SMART do TAP §3 possuem critério de sucesso associado na seção §3.2.

---

## 5. INCONSISTÊNCIAS RESOLVIDAS

| ID | Inconsistência Anterior | Correção Aplicada |
|---|---|---|
| **INC-01** | Data "08/09/2026" em critérios de sucesso | Substituída por **22/09/2026** |
| **INC-04** | "FATEC" genérico | Substituído por **Fatec Taquaritinga** |
| **INC-10** | Ausência de critério para métricas de fluxo | Incluído **Critério 3.2.f** |
| **INC-11** | Ausência de critério para marcos M1/M4 | Incluído **Critério 3.2.g** |
| **INC-12** | Ambiguidade sobre "usuários-piloto" | Nota de rodapé adicionada |
| **INC-13** | Numeração 3.1.1/3.1.2 (não padrão PMO) | Reestruturado para **3.2 e 3.3** |

---

## 6. DEFINITION OF DONE (DoD) DA SEÇÃO §3

A seção §3 está **completa e aprovada para inserção no TAP v1.1** quando:

- [x] Tabela de objetivos SMART presente com 5 objetivos (Produto, Qualidade, Cronograma, Métricas, Inovação)
- [x] Texto introdutório declara abordagem híbrida (PMBOK 7ª primário + 6ª complementar)
- [x] Seção 3.1 (Objetivos SMART) referencia a tabela
- [x] Seção 3.2 contém 7 critérios de sucesso (a-g)
- [x] Data do marco parcial corrigida para **22/09/2026**
- [x] Instituição grafada como **Fatec Taquaritinga**
- [x] Nota sobre usuários-piloto presente
- [x] Seção 3.3 contém 5 condições de fracasso (a-e)
- [x] 100% dos objetivos SMART possuem critério de sucesso associado
- [x] Alinhada ao PMBOK 7ª (Domínios de Entrega e Medição)
- [x] Alinhada ao PMBOK 6ª (Processo 4.1)
- [x] Zero referências a documentação externa (OKB, ADRs)
- [x] Linguagem técnica, impessoal, objetiva

---

## 7. PRÓXIMOS PASSOS

Após a inserção da seção §3 revisada, prosseguir com as demais correções identificadas:

| Prioridade | Seção | Ação | Prazo |
|---|---|---|---|
| 🔴 P0 | §4 | Corrigir lista aninhada (numeração N8-N12) | 17/09 |
| 🔴 P0 | §5 | Remover referências a OKB (REQ-07, 11, 12, 13) | 17/09 |
| 🟠 P1 | §8.5 | Atualizar equipe (2 → 3 pessoas) | 17/09 |
| 🟠 P1 | §8.9 | Remover comentário de revisão visível | 17/09 |
| 🟢 P3 | §13 | Corrigir data (2016 → 2026) | 17/09 |
| 🟢 P3 | §12 (NOVA) | Inserir "Declarações de Governança" (8 declarações) | 17/09 |

**Marco de submissão:** TAP v1.1 completo até 22/09/2026, 09:00 para submissão ao Prof. Dr. Nivaldo Carleto.

---

**Seção §3 revisada e pronta para inserção no TAP v1.1.**

Aguardo confirmação da inserção para prosseguir com as correções das demais seções (§4, §5, §8, §12, §13).