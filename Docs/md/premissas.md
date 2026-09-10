# RELATÓRIO DE CRÍTICA E REESTRUTURAÇÃO — SEÇÃO "PREMISSAS" DO TAP

**Eissore:** GP Sênior PMBOK 7ª / PMO (Co-Autor Crítico)  
**Data:** 11/09/2026  
**Documento Avaliado:** Seção "Premissas" (versão anterior) vs. Restrições de Governança e PMO  

---

## 1. VEREDITO EXECUTIVO SOBRE A REDAÇÃO ANTERIOR

A redação anterior das premissas, embora tecnicamente precisa, **cometeu dois desvios em relação aos padrões PMO e à sua nova diretriz**:

1. **Dependência Circular / Citação Excessiva do OKB**: Citar explicitamente "OKB v3.1 §X" ou "hardware.md" no TAP é inadequado. O TAP é o documento que *autoriza* o projeto e, por extensão, autoriza a criação e o uso da Base de Conhecimento (OKB). Citar um documento adjacente em evolução como fundamento de uma premissa do TAP cria uma dependência circular. O TAP deve ser autossuficiente em suas premissas de alto nível.
2. **Invasão de Escopo (Scope Creep no TAP)**: Incluir detalhes técnicos específicos (ex: "58GB RAM", "Qwen 32B Instruct Q4_K_M", "label `change-request`") na seção de premissas do TAP viola o princípio de que o TAP define o **"O Quê" e o "Por Quê"** em alto nível, não o **"Como"** (que pertence aos Planos de Gerenciamento e ADRs). Premissas no TAP devem ser estratégicas, não especificações técnicas.

**Decisão:** A seção "Premissas" foi totalmente reescrita para elevar o nível de abstração, remover citações diretas a documentos adjacentes em evolução (OKB/hardware.md) e eliminar detalhes técnicos que configuram invasão de escopo, mantendo apenas os fatores críticos que, se invalidados, paralisariam o projeto.

---

## 2. TEXTO REESTRUTURADO — SEÇÃO §9: PREMISSAS (Pronto para o TAP)

> **Instrução de inserção:** Substituir integralmente a seção §9 atual pelo texto abaixo.

---

### 9. Premissas do Projeto

Esta seção documenta os fatores considerados verdadeiros, reais ou certos para fins de planejamento do projeto COGME, conforme o Processo 4.1 (Desenvolver o Termo de Abertura do Projeto) do PMBOK®. Premissas são declarações de alto nível que, caso se provem falsas durante a execução, exigirão reavaliação imediata do escopo, cronograma ou custos do projeto, podendo acionar o processo formal de gestão de mudanças.

#### 9.1. Premissas Estratégicas e Operacionais Fundamentais

| # | Premissa | Justificativa de Alto Nível | Impacto se Invalidada |
|---|---|---|---|
| **P1** | **A governança do projeto seguirá o modelo híbrido: PMBOK 7ª como base de princípios e domínios, com PMBOK 6ª atuando como dicionário de processos complementares, e Kanban como método de execução.** | Alinhamento com as diretrizes acadêmicas da disciplina e necessidade de adaptação a equipes enxutas. | Exigência de retrabalho massivo na documentação para adequação a um modelo puramente preditivo (cascata), inviabilizando o prazo. |
| **P2** | **O projeto será desenvolvido e entregue utilizando exclusivamente tecnologias de Software Livre e Código Aberto (FOSS).** | Premissa pedagógica e de valor social, garantindo auditabilidade, gratuidade e sustentabilidade do artefato final. | Necessidade de aquisição de licenças, violando a restrição de orçamento zero e inviabilizando a entrega. |
| **P3** | **O uso de Inteligência Artificial Generativa (LLMs) como ferramenta de apoio ao desenvolvimento (SDD) é autorizado e esperado, desde que com rastreabilidade e revisão humana.** | Reconhecimento das diretrizes acadêmicas atuais que permitem o uso ético e auditável de IA para potencializar a produtividade. | Perda de produtividade da equipe e necessidade de reescrita manual de artefatos e código, comprometendo o cronograma. |
| **P4** | **O código-fonte funcional (MVP full-stack) constitui um deliverable formal e parte integrante da documentação de sucesso do projeto, não apenas os artefatos textuais.** | Alinhamento com a natureza prática do curso de Análise e Desenvolvimento de Sistemas. | O projeto seria considerado incompleto academicamente, mesmo com toda a documentação de gerenciamento perfeita. |
| **P5** | **A equipe do projeto (2 membros) manterá uma disponibilidade média de até 20 horas semanais dedicadas ao projeto, conciliando com as demais atividades acadêmicas.** | Capacidade realística de alocação de recursos humanos para um projeto acadêmico noturno. | Atraso crônico nas entregas, burnout da equipe e necessidade de redução drástica do escopo do MVP. |
| **P6** | **O hardware local disponível para a equipe é adequado e suficiente para as tarefas de desenvolvimento, modelagem, testes e execução do MVP em ambiente local.** | Condição base para que o desenvolvimento ocorra sem dependência de infraestrutura de nuvem paga. | Necessidade de migrar para ambientes de desenvolvimento em nuvem, gerando custos não previstos ou inviabilizando o trabalho. |
| **P7** | **O Professor Orientador atua como o único stakeholder formal com poder de aprovação (Patrocinador e Avaliador), simplificando os processos de comunicação e gestão de mudanças.** | Premissa de simplificação pedagógica, focando o esforço de gerenciamento no valor entregue e não em burocracia de múltiplos aprovadores. | Aumento exponencial da complexidade de comunicação e do tempo de ciclo para aprovações de mudanças. |
| **P8** | **As áreas de conhecimento de "Aquisições" e "Gerenciamento das Partes Interessadas" serão tratadas com simplificação pedagógica, conforme permitido pelo escopo acadêmico.** | Foco do projeto nas 8 áreas de conhecimento restantes, otimizando o tempo da equipe para o desenvolvimento do produto. | Exigência de planos de aquisição complexos para um projeto de orçamento zero, desviando o foco do produto. |

#### 9.2. Declaração de Rastreabilidade das Premissas

| Premissa | Domínio de Desempenho (PMBOK 7ª) | Artefato de Detalhamento (Pós-TAP) |
|---|---|---|
| P1, P7, P8 | Abordagem de Desenvolvimento / Stakeholders | Plano de Integração / Plano de Comunicações |
| P2, P6 | Abordagem de Desenvolvimento / Recursos | ADR de Stack Tecnológica / Plano de Recursos |
| P3, P4 | Trabalho do Projeto / Entrega | Base de Conhecimento (ADRs e Prompts) |
| P5 | Equipe | Plano de Recursos (RACI simplificado) |

---

## 3. ANÁLISE DE INVASÃO DE ESCOPO (O que foi removido e por quê)

| O que estava na versão anterior | Por que configura Invasão de Escopo no TAP | Onde isso deve estar (Correção) |
|---|---|---|
| "Hardware local (AMD Ryzen 7 8700G, 58GB RAM...)" | O TAP não é um inventário de TI. Especificar modelo e RAM é detalhe técnico. | **Plano de Recursos** ou **ADR-002** (Stack Tecnológica). O TAP apenas assume que o hardware é "adequado" (P6). |
| "Qwen 32B Instruct Q4_K_M como pilar" | Nomear modelos específicos é uma decisão de arquitetura, não uma premissa de planejamento. | **ADR-002** (Decisão Arquitetural). |
| "Label `change-request` no GitHub" | Detalhe operacional de configuração de ferramenta. | **Plano de Gestão de Mudanças** ou **Plano de Comunicações**. |
| Citações explícitas como "OKB v3.1 §3.1" | Cria dependência circular. O TAP autoriza o projeto; o OKB é um artefato *do* projeto. | Substituído por "Diretrizes acadêmicas" ou "Modelo híbrido" (conforme reescrita acima). |

---

## 4. CONTINUIDADE DO MONITORAMENTO DE INCONSISTÊNCIAS NO TAP

Conforme solicitado, sigo sinalizando as inconsistências críticas que **ainda persistem** no documento `Termo de Abertura do Projeto v1_opngoing.docx` e que devem ser corrigidas antes da submissão ao Prof. Dr. Nivaldo Carletto:

| ID | Inconsistência | Localização Atual no TAP | Ação Corretiva Obrigatória | Severidade |
|---|---|---|---|---|
| **INC-01** | Data de marco ultrapassada | §3 (Cronograma) e §8.3: menciona "08/09/2026" | Alterar para **22/09/2026** (Entrega Parcial Documental). | 🔴 Crítica |
| **INC-02** | Grafia incorreta do Stakeholder | §1, §3.2, §7, §13: "Nivaldo Carleto" | Corrigir para **Nivaldo Carletto** (com dois 't'). | 🔴 Crítica |
| **INC-03** | Grafia incorreta do Gerente | §13 (Aprovações): "Leonardo David Siva Setti" | Corrigir para **Leonardo David Silva Setti** (com 'l' no Silva). | 🔴 Crítica |
| **INC-04** | Nome da Instituição desatualizado/incorreto | §1, §2.3, §13: "FATEC Marlene Maria Miletta Servidoni" | Padronizar para **Fatec Taquaritinga** (nome oficial e atual). | 🟠 Alta |
| **INC-05** | Menção a EVM e Burndown | §3 (Métricas e Indicadores): cita SPI, CPI e Burndown Chart. | Substituir por: **"Métricas de fluxo Kanban (Cycle Time e Throughput) via GitHub Insights"**. | 🟠 Alta |
| **INC-06** | Comentário de revisão visível | §8.9 (Síntese): `Comment by leonardo: Verificar com o Profº...` | **Excluir** o comentário do Word antes da geração do PDF final. | 🟠 Alta |
| **INC-07** | Menção a "Cache Redis" na EAP | EAP (versão antiga ainda presente em algumas partes): N5.2 | Garantir que esteja apenas como "Cache" (genérico), conforme decisão de usar SQLite. | 🟡 Média |

---

## 5. PRÓXIMOS PASSOS IMEDIATOS

1. **Inserir a Seção §9 reestruturada** (acima) no TAP, garantindo que não haja invasão de escopo ou dependência circular do OKB.
2. **Aplicar as correções das inconsistências INC-01 a INC-07** no documento Word.
3. **Prosseguir para a Seção §10 (Riscos)**: Redigir os 5 riscos principais de alto nível, mantendo o foco estratégico (sem invadir o Plano de Riscos detalhado).

**Aguardo sua confirmação para prosseguir com a redação da Seção §10 (Riscos) ou para ajustes nesta seção de Premissas.**