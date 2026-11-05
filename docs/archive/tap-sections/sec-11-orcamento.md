---
id: docs-archive-tap-sections-sec-11-orcamento
title: Sec_11_Orcamento
type: archive
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/archive/tap-sections/sec-11-orcamento.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- tap-sections
- docs
- normalizado
---
Esta seção estabelece a estimativa preliminar de custos para o projeto COGME, conforme o Processo 4.1 (Desenvolver o Termo de Abertura do Projeto) do PMBOK® 6ª edição e o Domínio de Planejamento do PMBOK® 7ª edição.

Dada a natureza acadêmica e simulada do projeto, aliada ao compromisso institucional com o Software Livre, o orçamento aprovado para a linha de base de custos é **nulo**.

#### 11.1. Linha de Base de Custos (Preliminar)

| Categoria de Custo                    | Estimativa Preliminar | Justificativa e Premissa Associada                                                                                                                                       |
| ------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Recursos Humanos**            | R$ 0,00               | Esforço acadêmico dos membros da equipe (2 pessoas). Não há folha de pagamento, terceirização ou horas extras remuneradas.                                         |
| **Software e Ferramentas**      | R$ 0,00               | Adoção estrita de tecnologias 100% FOSS (Free and Open Source Software). Ex: Python, FastAPI, SQLite, WeasyPrint, GitHub (Free Tier).                                  |
| **Infraestrutura e Hospedagem** | R$ 0,00               | O MVP será desenvolvido, testado e validado em ambiente local (homologação). Não há contratação de serviços de cloud paga ou domínios comerciais.               |
| **Reserva de Contingência**    | R$ 0,00               | Não há verba financeira para absorver imprevistos. A mitigação de riscos dependerá exclusivamente de flexibilidade de escopo, alternativas FOSS e gestão de tempo. |
| **Reserva de Gerenciamento**    | R$ 0,00               | Inaplicável em projetos sem patrocínio financeiro ou margem de lucro.                                                                                                  |
| **TOTAL DO ORÇAMENTO**         | **R$ 0,00**     | **Linha de base de custos aprovada para o ciclo de vida do projeto.**                                                                                              |

#### 11.2. Implicações Estratégicas do Orçamento Zero

A ausência de recursos financeiros impõe condições específicas à gestão do projeto, que devem ser rigorosamente observadas:

1. **Mitigação de Riscos sem Custo:** Qualquer risco materializado (ex: instabilidade de uma API gratuita de câmbio) deve ser resolvido com alternativas técnicas gratuitas (ex: *adapter pattern* para outra API FOSS) ou ajuste de escopo, nunca com a aquisição de serviços pagos.
2. **Validação da Stack Tecnológica:** A seleção de todas as ferramentas (Fase N4.1 da EAP) está condicionada à existência de licenças compatíveis (MIT, Apache 2.0, GPL) e planos gratuitos que suportem a carga do MVP acadêmico.
3. **Foco em Valor, não em Despesa:** Conforme o Domínio de Medição do PMBOK 7ª, o sucesso do projeto será mensurado pela entrega de funcionalidades (Throughput, Cycle Time, cobertura de testes), e não por métricas financeiras tradicionais (como CPI ou SPI, que são inaplicáveis neste contexto).

#### 11.3. Rastreabilidade

| Origem no TAP                            | Vínculo com o Orçamento                                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| §3 (Objetivo: Inovação e Ferramentas) | Exige que 100% do ciclo de vida utilize ferramentas FOSS, sustentando o custo zero.                           |
| §8.4 (Restrições de Custo)            | Estabelece a proibição formal de aquisições pagas e a inexistência de verba institucional.               |
| §9 (Premissas)                          | Assume que o hardware local da equipe é suficiente e que serviços externos gratuitos estarão disponíveis. |

*Nota: O detalhamento de qualquer eventual custo indireto (ex: consumo marginal de energia elétrica ou internet) é considerado absorvido pelos recursos pessoais da equipe e não compõe a linha de base formal do projeto.*
