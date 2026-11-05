---
id: docs-archive-tap-sections-review-tap
title: RELATÓRIO DE AJUSTES DO TAP — TRANSIÇÃO PARA VERSÃO 1.2
type: archive
version: '1.2'
status: ativo
owner: agent-project-analyst
derived-from:
- docs/archive/tap-sections/review-tap.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- tap-sections
- docs
- normalizado
---


# RELATÓRIO DE AJUSTES DO TAP — TRANSIÇÃO PARA VERSÃO 1.2

**Emissor:** GP Sênior PMBOK 7ª / PMO (Co-Autor Crítico)
**Data:** 18/09/2026
**Base de Análise:** `review_TAP.md` (Parecer de Revisão — Rodada 1 / Plano de Integração v1.1)
**Documento Alvo:** `Termo-de-Abertura-do-Projeto.docx`

---

## 1. VEREDITO EXECUTIVO

A análise do `review_TAP.md` identificou **conflitos ontológicos e de governança** entre o TAP atual (v1.1) e as decisões consolidadas para o Plano de Gerenciamento da Integração (v1.1).

O conflito central reside no **papel do Prof. Dr. Nivaldo Carleto** e na **autoridade de aprovação de mudanças**. O TAP atual declara o Professor como "cliente com poder de aprovação", enquanto o Plano de Integração redefine que ele é **avaliador acadêmico nos marcos**, sem ingerência operacional, sendo o **Gerente de Projeto (Leonardo)** o CCB (Change Control Board) de membro único.

Para manter a **coerência documental cruzada** (regra de ouro do Plano de Integração §4), o TAP deve ser atualizado para a **versão 1.2**, absorvendo essa reinterpretação na fonte.

---

## 2. MATRIZ DE AJUSTES NECESSÁRIOS (TAP v1.1 → v1.2)

| #           | Seção do TAP                        | Conflito Identificado no Review                                                 | Ação Corretiva                                                                          |
| ----------- | ------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **1** | §0 Controle de Versões              | —                                                                              | Adicionar registro da Versão 3 (TAP v1.2)                                                |
| **2** | §3.2 Critérios de Sucesso (Item a)  | "aprovado pelo cliente (Prof. Dr. Nivaldo Carleto)"                             | Substituir por "validado academicamente pelo Prof. Dr. Nivaldo Carleto"                   |
| **3** | §3.2 Critérios de Sucesso (Item g)  | "Termo de Aceite assinado pelo Prof. Dr. Nivaldo Carleto"                       | Substituir por "Validação acadêmica formal pelo Prof. Dr. Nivaldo Carleto"             |
| **4** | §6 Marcos (M4 - Critério de Aceite) | "Termo de Aceite assinado pelo Prof. Dr. Nivaldo Carleto"                       | Substituir por "Validação acadêmica pelo Prof. Dr. Nivaldo Carleto"                    |
| **5** | §7 Partes Interessadas               | Função "Cliente"                                                              | Substituir por "Avaliador Acadêmico (Cliente simulado)"                                  |
| **6** | §9 Premissas (P7)                    | "único stakeholder formal com poder de aprovação (Patrocinador e Avaliador)" | Reinterpretar como "stakeholder-avaliador único nos marcos, sem ingerência operacional" |

---

## 3. TEXTOS PRONTOS PARA SUBSTITUIÇÃO (COPY & PASTE)

Abaixo estão os blocos de texto exatos para substituir no documento Word.

### A. §0 Controle de Versões (Adicionar nova linha)

*Adicione a seguinte linha à tabela de Controle de Versões:*

| Versão     | Data                 | Autores                                                                         | Notas da Revisão                                                                                                                                                                                                                                                                                                        |
| ----------- | -------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **3** | **18/09/2026** | **Leonardo David Silva Setti, Fabricio de Lima Cabral, Edson Luis Silva** | **Reinterpretação de governança: Prof. Dr. Nivaldo Carleto redefinido como avaliador acadêmico nos marcos (sem ingerência operacional); GP consolidado como CCB de membro único; remoção de "Termo de Aceite assinado" em favor de "validação acadêmica". Alinhamento com Plano de Integração v1.1.** |

---

### B. §3.2 Critérios de Sucesso do Projeto (Itens a e g)

*Substitua os itens **a)** e **g)** pelos textos abaixo:*

> **a) Critério de Aceitação Final:** O MVP entregue for **validado academicamente pelo Prof. Dr. Nivaldo Carleto** e pelos stakeholders representativos (usuários-piloto*) em uma sessão de validação prática, demonstrando que a ferramenta resolve a dor da falta de integração nas simulações cambiais.

> **g) Critério de Cronograma (NOVO):** O marco M1 (Entrega Parcial Documental em 22/09/2026) for cumprido integralmente, e o marco M4 (Encerramento e Aceite Final em 15/12/2026) for atingido com a **validação acadêmica formal pelo Prof. Dr. Nivaldo Carleto** e o repositório com tag de release final.

---

### C. §6 Marcos (Tabela de Marcos Principais — Linha M4)

*Na tabela de Marcos, localize a linha do **M4** e substitua a coluna "Critério de Aceite":*

| ID           | Macro-Fase (EAP)    | Descrição do Marco (Entrega de Valor)                                                                                                                                                     | Data Alvo  | **Critério de Aceite**                                                                                        |
| ------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------- |
| **M4** | MF3: Consolidação | **Encerramento e Validação Final:** Documentação técnica consolidada, lições aprendidas, verificação dos critérios SMART e apresentação final com validação acadêmica. | 15/12/2026 | **Validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4 e repositório com tag de release final.** |

---

### D. §7 Partes Interessadas do Projeto

*Substitua a tabela de Partes Interessadas pela versão abaixo, ajustando a função do Prof. Nivaldo:*

| Empresa | Participante                                                          | Função                                          |
| ------- | --------------------------------------------------------------------- | ------------------------------------------------- |
| FATEC   | **Nivaldo Carleto**                                             | **Avaliador Acadêmico (Cliente simulado)** |
| COGME   | Leonardo David Silva Setti, Fabricio de Lima Cabral, Edson Luis Silva | Desenvolvedores do projeto                        |

---

### E. §9 Premissas (Tabela de Premissas — Linha P7)

*Na tabela de Premissas Estratégicas e Operacionais Fundamentais, localize a linha **P7** e substitua integralmente:*

| #            | Premissa                                                                                                                                                                                                                                       | Justificativa de Alto Nível                                                                                                                                                                      | Impacto se Invalidada                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **P7** | **O Professor Orientador atua como stakeholder-avaliador único nos marcos de entrega (M1 a M4), sem ingerência em decisões operacionais diárias. A autoridade de aprovação de mudanças (CCB) é delegada ao Gerente de Projeto.** | **Premissa de simplificação pedagógica e autonomia do GP, focando o esforço de gerenciamento no valor entregue e evitando gargalos de decisão incompatíveis com o prazo acadêmico.** | **Necessidade de envolver o avaliador em decisões operacionais, gerando gargalo e comprometendo a autonomia do GP declarada no §1.b.** |

---

### F. §9 Premissas (Declaração de Rastreabilidade — Linha P7)

*Na tabela de Rastreabilidade das Premissas, localize a linha **P7** e ajuste:*

| Premissa             | Domínio de Desempenho (PMBOK 7ª)                    | Artefato de Detalhamento (Pós-TAP)                                                                                         |
| -------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **P1, P7, P8** | **Abordagem de Desenvolvimento / Stakeholders** | **Plano de Integração (§1.2.2 Papéis de Governança e §1.7.1 Autoridade de Mudança) / Plano de Comunicações** |

---

## 4. DECLARAÇÃO DE COERÊNCIA PÓS-AJUSTE

Após a aplicação destes ajustes, o TAP v1.2 estará **100% alinhado** com o Plano de Gerenciamento da Integração v1.1 nos seguintes pontos críticos:

1. **Autoridade de Mudança:** O TAP (§9 P7) agora delega explicitamente a autoridade de aprovação ao GP, sustentando o §1.7.1 do Plano de Integração (CCB de membro único).
2. **Papel do Stakeholder:** O TAP (§7 e §9 P7) agora reflete que o Prof. Dr. Nivaldo Carleto é **avaliador nos marcos**, sustentando o §1.2.2 do Plano de Integração.
3. **Critério de Encerramento:** O TAP (§3.2.g e §6 M4) agora utiliza "validação acadêmica" em vez de "Termo de Aceite assinado", sustentando o §1.8.2 do Plano de Integração.

**Regra de ouro respeitada:** O TAP foi ajustado na fonte. Não há mais necessidade de "notas de reinterpretação" no Plano de Integração. Ambos os documentos agora declaram a mesma governança.

---

## 5. PRÓXIMOS PASSOS

1. **Aplicar** os 6 ajustes acima no documento Word.
2. **Salvar** o arquivo como `Termo-de-Abertura-do-Projeto_v1.2.docx` (ou manter o nome original com a versão atualizada internamente).
3. **Atualizar o Plano de Integração v1.1:** Remover as "Notas de reinterpretação" e o parecer de revisão do início do documento, deixando apenas o plano limpo e assertivo (conforme indicado na "ANÁLISE — RODADA 3" do review).
4. **Atualizar o Glossário v2.1 → v2.2:** Alterar a definição de CCB de "Comitê de controle de mudanças (Prof. Nivaldo)" para "Gerente de Projeto (CCB de membro único)".

---

**Fim das correções.**

---

###### Histórico b ase para review e  correções acima


# PARECER DE REVISÃO — RODADA 1 (GP Leonardo)

**Revisor:** GP Sênior PMBOK 7ª / PMO (Co-Autor Crítico)
**Data:** 18/09/2026
**Objeto:** Plano de Integração v1.0 → v1.1
**Postura:** Implacável. Sem condescendência com inconsistência ontológica.

---

## 1. VEREDITO DA RODADA

As seis notas de revisão são **aplicáveis**, mas três delas (4, 5 e 6) introduzem **contradição estrutural com o TAP v1.1** que precisa ser resolvida *antes* do merge, sob pena de o avaliador identificar falha de rastreabilidade na Entrega Parcial (22/09).

Não é cosmético. É ontológico.

---

## 2. ANÁLISE CRÍTICA NOTA A NOTA

### Nota 1 — Padronização "Prof. Dr. Nivaldo Carleto"

**Aplicável.** Correção cosmética, sem impacto conceitual. Todas as ocorrências serão normalizadas.

### Nota 2 — Remoção da menção Gantt no §3

**Aplicável.** A frase é redundante: a decisão já está formalizada em ADR-001 e declarada no §2.1 (hierarquia). Remover não gera lacuna.

### Nota 3 — Adoção da nomenclatura "ADR"

**Aplicável, com ressalva.** A instrução original desta seção determinava que ADRs *não fossem mencionados explicitamente*. A nota de revisão sobrepõe essa diretriz. Como revisor, **acato a nota mais recente**, mas registro que houve mudança de posição do GP. Impacto: zero negativo — ADR é nomenclatura padrão de mercado e o glossário v2.1 já a define.

### Nota 4 — Prof. Dr. Nivaldo Carleto como avaliador por marco (não participante ativo)

**Aplicável, com IMPACTO ALTO.** Esta nota altera a governança declarada no TAP v1.1:

| Referência no TAP v1.1      | Declaração Atual                                                                    | Conflito com Nota 4         |
| ---------------------------- | ------------------------------------------------------------------------------------- | --------------------------- |
| Premissa P7 (§9)            | "Professor Orientador atua como o único stakeholder formal com poder de aprovação" | ❌ Contradiz                |
| Critério de Sucesso §3.2.a | "MVP aprovado pelo cliente (Prof. Dr. Nivaldo Carleto)"                               | ⚠️ Contradiz parcialmente |
| Glossário v2.1              | "CCB — Comitê de controle de mudanças (Prof. Nivaldo)"                             | ❌ Contradiz                |
| Marco M4 (§6)               | "Termo de Aceite assinado pelo Prof. Dr. Nivaldo Carleto"                             | ❌ Contradiz                |

**Resolução:** O GP possui autoridade formal (TAP §1.b) para reinterpretar o papel do stakeholder no contexto acadêmico prático. O Plano de Integração v1.1 **declarará explicitamente** essa reinterpretação com justificativa, e sinalizará que o TAP v1.2 (próxima versão) deve absorver a mudança para manter coerência documental.

### Nota 5 — Aprovação de mudanças é responsabilidade exclusiva do GP

**Aplicável, com IMPACTO ALTO.** Decorre logicamente da Nota 4. Se o Prof. Dr. Nivaldo Carleto não tem ingerência operacional, o CCB é o próprio GP (Leonardo). O glossário v2.1 precisa ser atualizado na próxima versão.

### Nota 6 — Remoção do "Termo de Aceite assinado" no §8.2

**Aplicável, com IMPACTO MÉDIO.** Contradiz o critério de aceite do Marco M4 no TAP v1.1. A resolução é substituir por "validação acadêmica no marco M4", que preserva a função de avaliação sem implicar assinatura formal de cliente externo.

---

## 3. SINALIZAÇÃO DE IMPACTOS E PROVIDÊNCIAS

| # | Impacto                                                                            | Severidade       | Providência                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | TAP v1.1 declara Prof. Dr. Nivaldo Carleto como "cliente com poder de aprovação" | **ALTA**   | TAP v1.2 deve ser atualizado antes da Entrega Final (Nov/2026). Para a Entrega Parcial (22/09), o Plano de Integração v1.1 declara a reinterpretação com justificativa. |
| 2 | Glossário v2.1 define CCB = Prof. Nivaldo                                         | **MÉDIA** | Glossário v2.2 deve redefinir CCB = GP (Leonardo). Atualizar na próxima revisão.                                                                                         |
| 3 | Critério de sucesso §3.2.a menciona "aprovação pelo cliente"                   | **MÉDIA** | Reinterpretar como "validação acadêmica pelo Prof. Dr. Nivaldo Carleto nos marcos".                                                                                      |
| 4 | Nota 3 contradiz instrução anterior sobre ADRs                                   | **BAIXA**  | Registrado neste parecer. Nota mais recente prevalece.                                                                                                                      |

**Regra de ouro aplicada:** O Plano de Integração *coordena*, não contradiz. Se a governança mudou, o plano declara a mudança e sinaliza a atualização do TAP. Nunca omite a divergência.

---

## 4. PLANO DE INTEGRAÇÃO v1.1 (REVISADO)

---

# 01. PLANO DE GERENCIAMENTO DA INTEGRAÇÃO

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Versão:** 1.1
**Data:** 18/09/2026
**Autores:** Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

---

> *Este plano deriva diretamente das Premissas P1 (governança híbrida), P3 (SDD com LLM), P4 (código como deliverable) e P7 (stakeholder-avaliador), e das Restrições de Cronograma e Custo estabelecidas no TAP v1.1, respeitando o Domínio de Abordagem de Desenvolvimento e o Domínio de Trabalho do Projeto do PMBOK® 7ª edição.*

---

## 1. IDENTIFICAÇÃO E PROPÓSITO

Este Plano de Gerenciamento da Integração coordena a execução integrada do projeto COGME, garantindo que os sete planos de área subsequentes (Escopo, Cronograma, Custos, Qualidade, Recursos, Comunicações e Riscos), o código-fonte e os artefatos de governança permaneçam coerentes com os Objetivos SMART aprovados no Termo de Abertura do Projeto (TAP v1.1).

**Função ontológica:** O TAP *autoriza*; este plano *coordena*. Ele não duplica conteúdo do TAP — define os mecanismos de coerência entre todos os artefatos do ciclo de vida.

**Domínio PMBOK 7ª atendido:** Abordagem de Desenvolvimento.
**Processo PMBOK 6ª de referência:** 4.2 — Desenvolver o Plano de Gerenciamento do Projeto.

---

## 2. MODELO DE GOVERNANÇA HÍBRIDA

O projeto COGME adota um modelo trifásico de governança, declarado no TAP v1.1 (§1.c) e operacionalizado neste plano:

| Camada                             | Fonte Normativa                                                    | Função no COGME                                                               |
| ---------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| **Governança primária**    | PMBOK® 7ª edição — 12 Princípios + 8 Domínios de Desempenho | Define*por que* e *para quê* o projeto existe; orienta decisões por valor |
| **Dicionário complementar** | PMBOK® 6ª edição — Processos 4.1 a 4.7                        | Fornece vocabulário e estrutura processual quando necessário                  |
| **Método de execução**    | Manifesto Ágil (4 valores) + Kanban (fluxo contínuo)             | Define*como* o trabalho é executado diariamente                              |

### 2.1. Hierarquia de Resolução de Conflitos

Em caso de conflito entre fontes normativas, aplica-se a seguinte ordem de precedência:

1. Valor entregue ao usuário final (Domínio de Entrega — PMBOK 7ª)
2. Ementa da disciplina + orientação do Prof. Dr. Nivaldo Carleto
3. PMBOK® 7ª edição (princípios e domínios)
4. Manifesto Ágil + Kanban (método de execução)
5. PMBOK® 6ª edição (dicionário de processos)

**Trade-off declarado:** Esta hierarquia favorece velocidade de entrega sobre completude documental. A decisão é intencional e alinhada ao Princípio "Foco em Valor" (PMBOK 7ª) e ao Valor Ágil "Software funcionando sobre documentação abrangente".

### 2.2. Papéis de Governança

| Papel                   | Titular                                   | Responsabilidade                                                                                   |
| ----------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Gerente de Projeto (GP) | Leonardo David Silva Setti                | Decisor operacional único, CCB de facto, responsável por aprovações e rejeições de mudanças |
| Desenvolvedores         | Fabricio de Lima Cabral, Edson Luis Silva | Execução técnica, revisão em pares, self-report de carga horária                              |
| Stakeholder-Avaliador   | Prof. Dr. Nivaldo Carleto                 | Avaliação acadêmica nos marcos M1–M4; sem ingerência direta em decisões operacionais         |

**Justificativa:** O projeto é trabalho prático acadêmico de gerência de projetos, não processo formal profissional. O Prof. Dr. Nivaldo Carleto atua como avaliador nos marcos, sem participação ativa no fluxo diário de decisões. Esta reinterpretação da Premissa P7 do TAP v1.1 será absorvida na próxima versão do TAP (v1.2) para manter coerência documental.

### 2.3. Princípio de Governança Mínima Viável (GMV)

Todo artefato de governança produzido no âmbito deste projeto deve justificar sua existência pelo teste GMV:

- O Prof. Dr. Nivaldo Carleto exigirá este artefato na avaliação?
- Este artefato evita retrabalho futuro?
- Este artefato é útil para a equipe (não apenas para avaliação)?

Se duas ou mais respostas forem negativas, o artefato é candidato a simplificação ou eliminação. Este princípio evita burocracia incompatível com uma equipe de 3 pessoas e orçamento zero (Restrição §8.4 do TAP v1.1).

---

## 3. GITHUB PROJECTS COMO FONTE ÚNICA DE VERDADE (SSOT)

O repositório GitHub do projeto e seu módulo GitHub Projects constituem o artefato primário de integração, cronograma e monitoramento. Esta decisão substitui o uso de Gantt tradicional como ferramenta ativa de planejamento e está formalizada em ADR-001.

**Justificativa:** Para uma equipe de 3 pessoas com fluxo contínuo (sem sprints time-boxed), o Gantt impõe overhead de manutenção desproporcional ao valor gerado. O Kanban via GitHub Projects fornece visibilidade em tempo real, métricas nativas de fluxo e rastreabilidade automática via commits.

**Domínio PMBOK 7ª:** Medição + Trabalho do Projeto.
**Valor Ágil aplicado:** "Indivíduos e interações sobre processos e ferramentas."

### 3.1. Mapeamento Kanban ↔ Processos PMBOK 6ª

| Coluna Kanban         | Processo PMBOK 6ª Associado         | Domínio PMBOK 7ª | Regra Operacional                   |
| --------------------- | ------------------------------------ | ------------------ | ----------------------------------- |
| **Backlog**     | 5.2 Coletar Requisitos               | Planejamento       | Card criado com DoR pendente        |
| **To Do**       | 4.3 Orientar Trabalho (preparação) | Trabalho           | DoR atendido; aguardando capacidade |
| **In Progress** | 4.3 Orientar e Gerenciar Trabalho    | Trabalho           | WIP limit: máx. 3 cards/pessoa     |
| **Review**      | 4.5 Monitorar e Controlar Trabalho   | Medição          | Revisão em pares obrigatória      |
| **Done**        | 5.4 Criar EAP (aceite do pacote)     | Entrega            | DoD atendido; commit mergeado       |

### 3.2. Regras de Fluxo

- **Pull system:** Cards só migram para "In Progress" quando há capacidade disponível (WIP limit respeitado).
- **Daily assíncrona:** Realizada via GitHub Discussions, respeitando a disponibilidade de curso noturno e carga ≤ 20h/semana por membro (Premissa P5).
- **SDD com LLM:** Código gerado com apoio de IA passa por revisão humana obrigatória antes do merge. Commits declaram co-autoria.

---

## 4. DESENVOLVIMENTO E MANUTENÇÃO DO PLANO DE GERENCIAMENTO

**Processo PMBOK 6ª:** 4.2 — Desenvolver o Plano de Gerenciamento do Projeto.

Os oito planos de área (Integração, Escopo, Cronograma, Custos, Qualidade, Recursos, Comunicações, Riscos) são versionados no repositório GitHub sob `/docs/`. Cada plano:

- Inicia com frase de rastreabilidade ao TAP v1.1 (Premissa + Restrição + Domínio PMBOK 7ª).
- Possui extensão máxima de 4 páginas (princípio GMV).
- É versionado via Conventional Commits: `docs(plano-integracao): atualização §X`.
- Passa por revisão em pares antes de ser considerado "Done".

**Regra de coerência cruzada:** Nenhum plano pode contradizer datas de marcos (M1–M4), premissas (P1–P8) ou restrições (§8) do TAP v1.1. Inconsistências detectadas em revisão acionam correção imediata antes do merge.

---

## 5. ORIENTAÇÃO E GESTÃO DO TRABALHO DO PROJETO

**Processo PMBOK 6ª:** 4.3 — Orientar e Gerenciar o Trabalho do Projeto.
**Domínio PMBOK 7ª:** Trabalho do Projeto.

### 5.1. Execução Diária

- Trabalho é puxado do backlog conforme capacidade (pull system).
- Cada card no GitHub Projects possui: título padronizado (ex: `N5.1 — Backend: Lógica de Negócio`), label de fase, responsável e critério de aceite.
- Commits seguem Conventional Commits (`feat`, `fix`, `docs`, `test`, `ci`, `chore`).

### 5.2. Gestão do Conhecimento

**Processo PMBOK 6ª:** 4.4 — Gerenciar o Conhecimento do Projeto.

- Estrutura de conhecimento: `/docs/` no repositório (planos, diagramas, lições aprendidas, catálogo de prompts SDD).
- Lições aprendidas registradas ao final de cada macro-fase (MF1, MF2, MF3), não apenas no encerramento.
- Decisões técnicas que afetam ≥ 2 fases da EAP, envolvem troca de tecnologia ou seriam questionadas pelo Prof. Dr. Nivaldo Carleto em avaliação são formalmente registradas via **ADR** (Architecture Decision Record) no repositório. Decisões menores ficam registradas em commit messages.

---

## 6. MONITORAMENTO E CONTROLE INTEGRADO

**Processo PMBOK 6ª:** 4.5 — Monitorar e Controlar o Trabalho do Projeto.
**Domínio PMBOK 7ª:** Medição.

### 6.1. Métricas de Fluxo Kanban (Substituição do EVM Tradicional)

Dada a restrição de orçamento zero (TAP §11), o Earned Value Management (EVM) tradicional é inaplicável. As métricas de desempenho são baseadas no fluxo Kanban, nativas do método e mensuráveis via GitHub Insights:

| Métrica                | Definição                                  | Meta (pós-calibração) | Frequência |
| ----------------------- | -------------------------------------------- | ------------------------ | ----------- |
| Cycle Time              | Tempo médio de um card do "To Do" ao "Done" | ≤ 3 dias                | Semanal     |
| Throughput              | Cards concluídos por semana                 | ≥ 5 cards/semana        | Semanal     |
| Cumulative Flow Diagram | Visualização de gargalos no fluxo          | Publicado no Dashboard   | Semanal     |
| WIP em progresso        | Cards ativos por pessoa                      | ≤ 3                     | Contínuo   |
| Burnout (self-report)   | Carga horária semanal declarada             | ≤ 20h/pessoa            | Semanal     |

### 6.2. Período de Calibração

De 23/09/2026 a 03/10/2026, as métricas são coletadas sem meta fixa, estabelecendo a baseline de desempenho real da equipe. Após calibração, metas são ajustadas com base na média observada ± 20% e formalizadas via ADR.

### 6.3. Trade-off Declarado

Abre-se mão da formalidade EVM (SPI/CPI) em favor de métricas acionáveis e nativas do método. Caso o Prof. Dr. Nivaldo Carleto solicite SPI/CPI em avaliação, serão calculados *post-hoc* utilizando os marcos M1–M4 como pontos de medição de valor agregado.

---

## 7. CONTROLE INTEGRADO DE MUDANÇAS

**Processo PMBOK 6ª:** 4.6 — Realizar o Controle Integrado de Mudanças.
**Domínio PMBOK 7ª:** Incerteza.

### 7.1. Autoridade de Mudança

O Gerente de Projeto (Leonardo David Silva Setti) atua como Change Control Board (CCB) de membro único. O Prof. Dr. Nivaldo Carleto não participa do fluxo de aprovação de mudanças; sua atuação restringe-se à avaliação acadêmica nos marcos M1–M4.

**Justificativa:** O projeto é trabalho prático acadêmico de gerência de projetos, não processo formal profissional. Atribuir poder de aprovação operacional ao avaliador externo comprometeria a autonomia do GP declarada no TAP v1.1 §1.b e geraria gargalo de decisão incompatível com o prazo de 13 semanas.

### 7.2. Fluxo de Solicitação de Mudança

| Etapa | Ação                                               | Responsável              | Prazo                    |
| ----- | ---------------------------------------------------- | ------------------------- | ------------------------ |
| 1     | Abertura de GitHub Issue com label`change-request` | Qualquer membro da equipe | Imediato                 |
| 2     | Análise de impacto (escopo, prazo, qualidade)       | GP (Leonardo)             | ≤ 48h                   |
| 3     | Aprovação ou rejeição via comentário na Issue   | GP (Leonardo)             | ≤ 24h após análise    |
| 4     | Atualização do backlog + planos afetados + commit  | Equipe                    | ≤ 24h após aprovação |

### 7.3. Limiar de Formalidade

- **Mudanças que NÃO alteram marcos (M1–M4) nem escopo do MVP:** Aprovadas pelo GP com registro em commit e comentário na Issue.
- **Mudanças que ALTERAM marcos ou escopo do MVP:** Aprovadas pelo GP com registro formal via ADR e comunicação ao Prof. Dr. Nivaldo Carleto no marco de avaliação subsequente.

**Valor Ágil aplicado:** "Responder a mudanças sobre seguir um plano." O processo é leve, mas auditável.

---

## 8. ENCERRAMENTO DO PROJETO OU FASE

**Processo PMBOK 6ª:** 4.7 — Encerrar o Projeto ou Fase.
**Domínio PMBOK 7ª:** Entrega.

### 8.1. Critérios de Encerramento por Macro-Fase

| Macro-Fase          | Período            | Critério de Encerramento                                                                               |
| ------------------- | ------------------- | ------------------------------------------------------------------------------------------------------- |
| MF1: Fundação     | 01/09 – 30/09/2026 | TAP aprovado + 8 planos v0.1 + EAP sincronizada + Stack definida + Ambiente configurado                 |
| MF2: Construção   | 01/10 – 15/11/2026 | MVP funcional + ≥ 80% coverage + UAT aprovado + Pipeline CI verde                                      |
| MF3: Consolidação | 16/11 – 15/12/2026 | Documentação consolidada + Apresentação final + Validação acadêmica no marco M4 + Tag de release |

### 8.2. Encerramento Formal do Projeto

- Tag de release final no repositório GitHub.
- Lições aprendidas finais consolidadas.
- Verificação dos cinco Objetivos SMART do TAP §3.
- Validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4.

---

## 9. CONDIÇÕES DE FRACASSO E ESCALATION

Derivado do TAP v1.1 §3.3 (Condições de Fracasso), os seguintes gatilhos acionam ação corretiva imediata pelo GP:

| Gatilho                                           | Ação                                                                    |
| ------------------------------------------------- | ------------------------------------------------------------------------- |
| Desvio > 3 dias úteis em qualquer marco (M1–M4) | Issue`change-request` + proposta de replanejamento + ADR                |
| Coverage < 70% por 2 semanas consecutivas         | Revisão de prioridade de testes + ajuste de escopo                       |
| Burnout detectado (> 20h/semana por 2 semanas)    | Redução de WIP + redistribuição de cards                              |
| Scope creep > 15% do backlog original             | Congelamento de novas features + CCB (GP)                                 |
| MVP não funcional em homologação até M3       | Acionamento de contingência técnica (redução de escopo não-crítico) |

**Nota:** Escalation ao Prof. Dr. Nivaldo Carleto ocorre apenas nos marcos de avaliação ou quando o GP identificar risco de não cumprimento dos critérios SMART do TAP §3.

---

## 10. DECLARAÇÃO DE RASTREABILIDADE

| Seção deste Plano            | Origem no TAP v1.1                              | Domínio PMBOK 7ª           | Processo PMBOK 6ª |
| ------------------------------ | ----------------------------------------------- | ---------------------------- | ------------------ |
| §2 (Governança Híbrida)     | §1.c + Premissa P1                             | Abordagem de Desenvolvimento | 4.1, 4.2           |
| §3 (GitHub como SSOT)         | Premissa P1 + §3 (Métricas)                   | Medição + Trabalho         | 4.3, 4.5           |
| §5 (Orientação do Trabalho) | Premissas P3, P4, P5                            | Trabalho do Projeto          | 4.3, 4.4           |
| §6 (Monitoramento)            | §3 (Métricas e Indicadores)                   | Medição                    | 4.5                |
| §7 (Controle de Mudanças)    | §3.3 (Fracasso) + Premissa P7 (reinterpretada) | Incerteza                    | 4.6                |
| §8 (Encerramento)             | §6 (Marcos M1–M4)                             | Entrega                      | 4.7                |
| §9 (Escalation)               | §3.3 (Fracasso) + §10 (Riscos)                | Incerteza                    | 4.5, 4.6           |

**Verificação de completude:** 100% das seções deste plano possuem rastreabilidade a ao menos uma premissa, restrição ou objetivo SMART do TAP v1.1.

**Nota de reinterpretação:** A Premissa P7 do TAP v1.1 ("Professor Orientador atua como único stakeholder formal com poder de aprovação") é reinterpretada neste plano como "Professor Orientador atua como stakeholder-avaliador nos marcos, sem ingerência operacional". Esta reinterpretação será absorvida no TAP v1.2.

---

## 11. PREMISSAS E RESTRIÇÕES APLICÁVEIS A ESTE PLANO

| Tipo              | Referência TAP           | Impacto neste Plano                       |
| ----------------- | ------------------------- | ----------------------------------------- |
| Premissa P1       | Governança híbrida      | Fundamenta §2                            |
| Premissa P3       | SDD com LLM autorizado    | Fundamenta §5.2                          |
| Premissa P5       | ≤ 20h/semana por membro  | Fundamenta §3.2 e §9                    |
| Premissa P7       | Stakeholder-avaliador     | Fundamenta §2.2 e §7.1 (reinterpretada) |
| Restrição §8.4 | Orçamento zero           | Fundamenta §6.3 (inaplicabilidade EVM)   |
| Restrição §8.2 | Prazo letivo inegociável | Fundamenta §9 (gatilhos de escalation)   |

---

## CONTROLE DE VERSÕES

| Versão | Data       | Alteração                                                                                                                                                              | Responsável         |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| 1.0     | 18/09/2026 | Emissão inicial                                                                                                                                                         | Leonardo D. S. Setti |
| 1.1     | 18/09/2026 | Revisão GP: padronização de nomenclatura, remoção de menção Gantt, adoção de ADR, redefinição de autoridade de mudanças, remoção de termo de aceite formal | Leonardo D. S. Setti |

---

*Fim do Plano de Gerenciamento da Integração — COGME v1.1*

---

## CHECKLIST DE VALIDAÇÃO PÓS-REVISÃO

- [X] Todas as menções normalizadas para "Prof. Dr. Nivaldo Carleto"
- [X] Menção Gantt removida do §3
- [X] Nomenclatura ADR adotada para decisões arquiteturais
- [X] §7.1: CCB = GP Leonardo; Prof. Dr. Nivaldo Carleto como avaliador por marco
- [X] §7.2: Aprovação/rejeição é responsabilidade exclusiva do GP
- [X] §7.3: Removida exigência de aprovação do Prof. Dr. Nivaldo Carleto
- [X] §8.2: Removido "Termo de Aceite assinado"
- [X] Nota de reinterpretação da Premissa P7 declarada explicitamente
- [X] Sinalização de atualização pendente no TAP v1.2 e Glossário v2.2

---

*GP Sênior PMBOK 7ª / PMO — Co-Autor Crítico*
*Projeto COGME | Fatec Taquaritinga | 18/09/2026*
*Faltam 4 dias úteis para o Marco M1 (22/09/2026).*

# ANÁLISE — RODADA 3 (GP Leonardo)

## Veredito da Rodada

A supressão das notas de reinterpretação está correta. Se o TAP será ajustado na fonte, o Plano de Integração não deve carregar meta-comentários sobre divergências que deixarão de existir. O documento deve ser **autossuficiente, limpo e assertivo** — como se o TAP já refletisse a governança operacional real.

**Decisões consolidadas para esta versão:**

| Ponto                      | Decisão Final                            |
| -------------------------- | ----------------------------------------- |
| Autoridade de mudanças    | GP Leonardo (CCB de membro único)        |
| Prof. Dr. Nivaldo Carleto  | Avaliador acadêmico nos marcos M1–M4    |
| Nomenclatura de decisões  | ADR (Architecture Decision Record)        |
| Menção Gantt             | Suprimida                                 |
| Termo de Aceite            | Substituído por "validação acadêmica" |
| Notas de reinterpretação | Suprimidas (ajuste na fonte: TAP)         |
| Numeração                | Hierárquica: 1, 1.1, 1.2, 1.2.1...       |

**Nenhum conflito residual.** Procedo à redação integral.

---

# 1 INTEGRAÇÃO

**Plano de Gerenciamento da Integração**
**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Versão:** 1.1
**Data:** 18/09/2026
**Autores:** Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

> *Este plano deriva diretamente das Premissas P1 (governança híbrida), P3 (SDD com LLM), P4 (código como deliverable) e P7 (stakeholder-avaliador único), e das Restrições de Cronograma e Custo do TAP, respeitando o Domínio de Abordagem de Desenvolvimento e o Domínio de Trabalho do Projeto do PMBOK® 7ª edição.*

---

## 1.1 Identificação e Propósito

Este Plano de Gerenciamento da Integração coordena a execução integrada do projeto COGME, garantindo que os sete planos de área subsequentes (Escopo, Cronograma, Custos, Qualidade, Recursos, Comunicações e Riscos), o código-fonte e os artefatos de governança permaneçam coerentes com os Objetivos SMART aprovados no Termo de Abertura do Projeto.

**Função ontológica:** O TAP *autoriza*; este plano *coordena*. Ele não duplica conteúdo do TAP — define os mecanismos de coerência entre todos os artefatos do ciclo de vida.

- **Domínio PMBOK 7ª:** Abordagem de Desenvolvimento.
- **Processo PMBOK 6ª (dicionário):** 4.2 — Desenvolver o Plano de Gerenciamento do Projeto.

---

## 1.2 Modelo de Governança Híbrida

O projeto adota um modelo trifásico de governança, operacionalizado neste plano:

| Camada                   | Fonte Normativa                                        | Função no COGME                                              |
| ------------------------ | ------------------------------------------------------ | -------------------------------------------------------------- |
| Governança primária    | PMBOK® 7ª edição — 12 Princípios + 8 Domínios   | Define*por que* e *para quê*; orienta decisões por valor |
| Dicionário complementar | PMBOK® 6ª edição — Processos 4.1 a 4.7            | Fornece vocabulário e estrutura processual quando necessário |
| Método de execução    | Manifesto Ágil (4 valores) + Kanban (fluxo contínuo) | Define*como* o trabalho é executado diariamente             |

### 1.2.1 Hierarquia de Resolução de Conflitos

Em caso de conflito entre fontes normativas:

1. Valor entregue ao usuário final (Domínio de Entrega — PMBOK 7ª)
2. Ementa da disciplina + orientação do Prof. Dr. Nivaldo Carleto
3. PMBOK® 7ª edição (princípios e domínios)
4. Manifesto Ágil + Kanban (método de execução)
5. PMBOK® 6ª edição (dicionário de processos)

**Trade-off declarado:** Esta hierarquia favorece velocidade de entrega sobre completude documental, alinhada ao Princípio "Foco em Valor" (PMBOK 7ª) e ao Valor Ágil "Software funcionando sobre documentação abrangente".

### 1.2.2 Papéis de Governança

| Papel                   | Titular                                   | Responsabilidade                                                                              |
| ----------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------- |
| Gerente de Projeto (GP) | Leonardo David Silva Setti                | Decisor operacional único; autoridade para aprovações, rejeições e controle de mudanças |
| Desenvolvedores         | Fabricio de Lima Cabral, Edson Luis Silva | Execução técnica; revisão em pares; self-report de carga horária                         |
| Stakeholder-Avaliador   | Prof. Dr. Nivaldo Carleto                 | Avaliação acadêmica nos marcos M1–M4; sem ingerência em decisões operacionais           |

### 1.2.3 Governança Mínima Viável (GMV)

Todo artefato de governança deve justificar sua existência pelo teste GMV:

| Pergunta                                                             | Se SIM            | Se NÃO                  |
| -------------------------------------------------------------------- | ----------------- | ------------------------ |
| O Prof. Dr. Nivaldo Carleto exigirá este artefato na avaliação?   | Produzir completo | Simplificar ou eliminar  |
| Este artefato evita retrabalho futuro?                               | Produzir          | Avaliar custo-benefício |
| Este artefato é útil para a equipe (não apenas para avaliação)? | Produzir          | Eliminar                 |

**Regra:** Se ≥ 2 respostas forem NÃO, o artefato é candidato a simplificação ou eliminação. Decisão final do GP.

---

## 1.3 GitHub Projects como Fonte Única de Verdade (SSOT)

O repositório GitHub e seu módulo GitHub Projects constituem o artefato primário de integração, cronograma e monitoramento. Esta decisão substitui o uso de Gantt tradicional como ferramenta ativa de planejamento e está formalizada em ADR-001.

**Justificativa:** Para uma equipe de 3 pessoas com fluxo contínuo, o Gantt impõe overhead de manutenção desproporcional ao valor gerado. O Kanban via GitHub Projects fornece visibilidade em tempo real, métricas nativas de fluxo e rastreabilidade automática via commits.

- **Domínio PMBOK 7ª:** Medição + Trabalho do Projeto.
- **Valor Ágil:** "Indivíduos e interações sobre processos e ferramentas."

### 1.3.1 Mapeamento Kanban ↔ Processos PMBOK 6ª

| Coluna Kanban | Processo PMBOK 6ª                   | Domínio PMBOK 7ª | Regra Operacional                   |
| ------------- | ------------------------------------ | ------------------ | ----------------------------------- |
| Backlog       | 5.2 Coletar Requisitos               | Planejamento       | Card criado com DoR pendente        |
| To Do         | 4.3 Orientar Trabalho (preparação) | Trabalho           | DoR atendido; aguardando capacidade |
| In Progress   | 4.3 Orientar e Gerenciar Trabalho    | Trabalho           | WIP limit: máx. 3 cards/pessoa     |
| Review        | 4.5 Monitorar e Controlar            | Medição          | Revisão em pares obrigatória      |
| Done          | 5.4 Criar EAP (aceite do pacote)     | Entrega            | DoD atendido; commit mergeado       |

### 1.3.2 Regras de Fluxo

- **Pull system:** Cards migram para "In Progress" somente quando há capacidade disponível (WIP limit respeitado).
- **Daily assíncrona:** Via GitHub Discussions, respeitando curso noturno e carga ≤ 20h/semana por membro (Premissa P5).
- **SDD com LLM:** Código gerado com apoio de IA passa por revisão humana obrigatória antes do merge. Commits declaram co-autoria.

---

## 1.4 Desenvolvimento e Manutenção do Plano de Gerenciamento

**Processo PMBOK 6ª:** 4.2 — Desenvolver o Plano de Gerenciamento do Projeto.

Os oito planos de área são versionados no repositório GitHub sob `/docs/`. Cada plano:

- Inicia com frase de rastreabilidade ao TAP (Premissa + Restrição + Domínio PMBOK 7ª).
- Possui extensão máxima de 4 páginas (princípio GMV).
- É versionado via Conventional Commits: `docs(plano-integracao): atualização §X`.
- Passa por revisão em pares antes de ser considerado "Done".

**Regra de coerência cruzada:** Nenhum plano pode contradizer datas de marcos (M1–M4), premissas (P1–P8) ou restrições (§8) do TAP. Inconsistências detectadas em revisão acionam correção imediata antes do merge.

---

## 1.5 Orientação e Gestão do Trabalho do Projeto

**Processo PMBOK 6ª:** 4.3 — Orientar e Gerenciar o Trabalho do Projeto.
**Domínio PMBOK 7ª:** Trabalho do Projeto.

### 1.5.1 Execução Diária

- Trabalho puxado do backlog conforme capacidade (pull system).
- Cada card no GitHub Projects possui: título padronizado (ex: `N5.1 — Backend: Lógica de Negócio`), label de fase, responsável e critério de aceite.
- Commits seguem Conventional Commits (`feat`, `fix`, `docs`, `test`, `ci`, `chore`).

### 1.5.2 Gestão do Conhecimento

**Processo PMBOK 6ª:** 4.4 — Gerenciar o Conhecimento do Projeto.

- Estrutura de conhecimento: `/docs/` no repositório (planos, diagramas, lições aprendidas, catálogo de prompts SDD).
- Lições aprendidas registradas ao final de cada macro-fase (MF1, MF2, MF3).
- Decisões que afetam ≥ 2 fases da EAP, envolvem troca de tecnologia ou seriam questionadas pelo Prof. Dr. Nivaldo Carleto em avaliação são formalmente registradas via **ADR** (Architecture Decision Record). Decisões menores ficam em commit messages.

---

## 1.6 Monitoramento e Controle Integrado

**Processo PMBOK 6ª:** 4.5 — Monitorar e Controlar o Trabalho do Projeto.
**Domínio PMBOK 7ª:** Medição.

### 1.6.1 Métricas de Fluxo Kanban

Dada a restrição de orçamento zero, o Earned Value Management (EVM) tradicional é inaplicável. As métricas de desempenho baseiam-se no fluxo Kanban:

| Métrica                | Definição                                  | Meta (pós-calibração) | Frequência |
| ----------------------- | -------------------------------------------- | ------------------------ | ----------- |
| Cycle Time              | Tempo médio de um card do "To Do" ao "Done" | ≤ 3 dias                | Semanal     |
| Throughput              | Cards concluídos por semana                 | ≥ 5 cards/semana        | Semanal     |
| Cumulative Flow Diagram | Visualização de gargalos no fluxo          | Publicado no Dashboard   | Semanal     |
| WIP em progresso        | Cards ativos por pessoa                      | ≤ 3                     | Contínuo   |
| Burnout (self-report)   | Carga horária semanal declarada             | ≤ 20h/pessoa            | Semanal     |

### 1.6.2 Período de Calibração

De 23/09/2026 a 03/10/2026, as métricas são coletadas sem meta fixa, estabelecendo a baseline de desempenho real da equipe. Após calibração, metas são ajustadas com base na média observada ± 20% e formalizadas via ADR.

### 1.6.3 Trade-off Declarado

Abre-se mão da formalidade EVM (SPI/CPI) em favor de métricas acionáveis e nativas do método. Caso o Prof. Dr. Nivaldo Carleto solicite SPI/CPI em avaliação, serão calculados *post-hoc* utilizando os marcos M1–M4 como pontos de medição de valor agregado.

---

## 1.7 Controle Integrado de Mudanças

**Processo PMBOK 6ª:** 4.6 — Realizar o Controle Integrado de Mudanças.
**Domínio PMBOK 7ª:** Incerteza.

### 1.7.1 Autoridade de Mudança

O Gerente de Projeto (Leonardo David Silva Setti) atua como Change Control Board (CCB) de membro único, com autoridade formal delegada pelo TAP para aprovar, rejeitar e versionar mudanças.

### 1.7.2 Fluxo de Solicitação de Mudança

| Etapa | Ação                                               | Responsável              | Prazo                    |
| ----- | ---------------------------------------------------- | ------------------------- | ------------------------ |
| 1     | Abertura de GitHub Issue com label`change-request` | Qualquer membro da equipe | Imediato                 |
| 2     | Análise de impacto (escopo, prazo, qualidade)       | GP (Leonardo)             | ≤ 48h                   |
| 3     | Aprovação ou rejeição via comentário na Issue   | GP (Leonardo)             | ≤ 24h após análise    |
| 4     | Atualização do backlog + planos afetados + commit  | Equipe                    | ≤ 24h após aprovação |

### 1.7.3 Limiar de Formalidade

- **Mudanças que NÃO alteram marcos (M1–M4) nem escopo do MVP:** Aprovadas pelo GP com registro em commit e comentário na Issue.
- **Mudanças que ALTERAM marcos ou escopo do MVP:** Aprovadas pelo GP com registro formal via ADR e comunicação ao Prof. Dr. Nivaldo Carleto no marco de avaliação subsequente.

**Valor Ágil aplicado:** "Responder a mudanças sobre seguir um plano." O processo é leve, mas auditável.

---

## 1.8 Encerramento do Projeto ou Fase

**Processo PMBOK 6ª:** 4.7 — Encerrar o Projeto ou Fase.
**Domínio PMBOK 7ª:** Entrega.

### 1.8.1 Critérios de Encerramento por Macro-Fase

| Macro-Fase          | Período            | Critério de Encerramento                                                                               |
| ------------------- | ------------------- | ------------------------------------------------------------------------------------------------------- |
| MF1: Fundação     | 01/09 – 30/09/2026 | TAP aprovado + 8 planos v0.1 + EAP sincronizada + Stack definida + Ambiente configurado                 |
| MF2: Construção   | 01/10 – 15/11/2026 | MVP funcional + ≥ 80% coverage + UAT aprovado + Pipeline CI verde                                      |
| MF3: Consolidação | 16/11 – 15/12/2026 | Documentação consolidada + Apresentação final + Validação acadêmica no marco M4 + Tag de release |

### 1.8.2 Encerramento Formal do Projeto

- Tag de release final no repositório GitHub.
- Lições aprendidas finais consolidadas.
- Verificação dos cinco Objetivos SMART do TAP §3.
- Validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4.

---

## 1.9 Condições de Fracasso e Escalation

Derivado do TAP §3.3 (Condições de Fracasso), os seguintes gatilhos acionam ação corretiva imediata pelo GP:

| Gatilho                                           | Ação                                                     |
| ------------------------------------------------- | ---------------------------------------------------------- |
| Desvio > 3 dias úteis em qualquer marco (M1–M4) | Issue`change-request` + proposta de replanejamento + ADR |
| Coverage < 70% por 2 semanas consecutivas         | Revisão de prioridade de testes + ajuste de escopo        |
| Burnout detectado (> 20h/semana por 2 semanas)    | Redução de WIP + redistribuição de cards               |
| Scope creep > 15% do backlog original             | Congelamento de novas features + CCB (GP)                  |
| MVP não funcional em homologação até M3       | Contingência técnica: redução de escopo não-crítico  |

**Nota:** Escalation ao Prof. Dr. Nivaldo Carleto ocorre apenas nos marcos de avaliação ou quando o GP identificar risco de não cumprimento dos critérios SMART do TAP §3.

---

## 1.10 Declaração de Rastreabilidade

| Seção             | Origem no TAP                    | Domínio PMBOK 7ª           | Processo PMBOK 6ª |
| ------------------- | -------------------------------- | ---------------------------- | ------------------ |
| 1.2 (Governança)   | §1.c + Premissa P1              | Abordagem de Desenvolvimento | 4.1, 4.2           |
| 1.3 (GitHub SSOT)   | Premissa P1 + §3 (Métricas)    | Medição + Trabalho         | 4.3, 4.5           |
| 1.5 (Orientação)  | Premissas P3, P4, P5             | Trabalho do Projeto          | 4.3, 4.4           |
| 1.6 (Monitoramento) | §3 (Métricas e Indicadores)    | Medição                    | 4.5                |
| 1.7 (Mudanças)     | §3.3 (Fracasso) + Premissa P7   | Incerteza                    | 4.6                |
| 1.8 (Encerramento)  | §6 (Marcos M1–M4)              | Entrega                      | 4.7                |
| 1.9 (Escalation)    | §3.3 (Fracasso) + §10 (Riscos) | Incerteza                    | 4.5, 4.6           |

**Verificação:** 100% das seções possuem rastreabilidade a ao menos uma premissa, restrição ou objetivo SMART do TAP.

---

## 1.11 Premissas e Restrições Aplicáveis

| Tipo              | Referência TAP              | Impacto neste Plano      |
| ----------------- | ---------------------------- | ------------------------ |
| Premissa P1       | Governança híbrida         | Fundamenta 1.2           |
| Premissa P3       | SDD com LLM autorizado       | Fundamenta 1.5.2         |
| Premissa P5       | ≤ 20h/semana por membro     | Fundamenta 1.3.2 e 1.9   |
| Premissa P7       | Stakeholder-avaliador único | Fundamenta 1.2.2 e 1.7.1 |
| Restrição §8.4 | Orçamento zero              | Fundamenta 1.6.3         |
| Restrição §8.2 | Prazo letivo inegociável    | Fundamenta 1.9           |

---

## Controle de Versões

| Versão | Data       | Alteração                                                                         | Responsável         |
| ------- | ---------- | ----------------------------------------------------------------------------------- | -------------------- |
| 1.0     | 18/09/2026 | Emissão inicial                                                                    | Leonardo D. S. Setti |
| 1.1     | 18/09/2026 | Revisão GP: padronização, ADR, autoridade de mudanças, numeração hierárquica | Leonardo D. S. Setti |

---

*Fim da Seção 1 — Integração | COGME v1.1*

---

*GP Sênior PMBOK 7ª / PMO — Co-Autor Crítico*
*Projeto COGME | Fatec Taquaritinga | 18/09/2026*
*Faltam 4 dias úteis para o Marco M1 (22/09/2026).*
