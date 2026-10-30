# 2.5 Gerenciamento de Qualidade

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** O TAP e REQ-08 estabelecem cobertura mínima de 80% do código. O painel da monografia apresenta 70% das regras de negócio, com limiar e base diferentes. Nesta versão, o painel foi alinhado a 80% do código para manter o critério do TAP; essa correção editorial não comprova cobertura alcançada. As evidências de execução dos ciclos PDCA e do diagrama de Ishikawa não acompanham estas seções.

O critério de qualidade do projeto exige que o código-fonte entregue atinja o índice mínimo de 80% de cobertura de testes automatizados — unitários e de integração, executados com pytest e coverage.py — e não apresente defeitos de severidade crítica ou alta no ambiente de homologação, sendo aprovado em roteiro de testes de aceitação que cubra 100% dos fluxos funcionais críticos (cálculo cambial, configuração de regimes e geração de PDF). Os critérios de qualidade foram consolidados em duas dimensões obrigatórias, em substituição ao modelo anterior de quatro dimensões simultâneas, considerado excessivo para uma equipe de duas pessoas: a dimensão de conformidade acadêmica (rastreabilidade ao TAP, aderência ao PMBOK® 7ª edição, consistência cruzada entre planos e linguagem técnica impessoal) e a dimensão de valor funcional (critérios de prontidão e de conclusão claros, código testado e implantação funcional em homologação). Uma terceira dimensão, opcional mas recomendada, trata da auditoria do processo SDD, por meio do registro dos prompts de geração, de commits com assinatura de coautoria de IA e de registros de decisão arquitetural.

## Temas relacionados

- [2.5.1 PDCA](02_05_01_pdca.md)
- [2.5.2 Diagrama de causa e efeito](02_05_02_diagrama_de_causa_e_efeito.md)

## 2.5.3 Painel de Medição

O Domínio de Medição do PMBOK® 7ª edição estabelece que a avaliação do desempenho deve produzir informação acionável, e não apenas registro histórico. Como o projeto não possui remuneração nem orçamento de aquisições, os indicadores clássicos de valor agregado perdem poder informativo, razão pela qual a medição se apoia em métricas de fluxo extraídas diretamente do quadro Kanban, complementadas por indicadores de qualidade do produto. Cada indicador possui meta, fonte de dado e gatilho de ação previamente definidos, de modo que a superação de um limite dispare resposta imediata, e não discussão posterior. As metas serão calibradas ao término do período de estabilização, entre 23 de setembro e 3 de outubro de 2026, quando houver massa de dados suficiente. O Quadro 12 apresenta o painel de medição do projeto.

**Quadro 12 — Painel de medição do projeto**

| Indicador | Meta de referência | Fonte do dado | Gatilho de ação |
| --- | --- | --- | --- |
| Tempo de ciclo por cartão | Até 5 dias corridos | Painel do GitHub Projects | Dois cartões consecutivos acima da meta exigem revisão da decomposição |
| Vazão semanal | Mínimo de 3 cartões concluídos | Painel do GitHub Projects | Duas semanas seguidas abaixo da meta exigem replanejamento do escopo do período |
| Trabalho em progresso | Máximo de 2 cartões por integrante | Quadro Kanban | Bloqueio de novas entradas até a conclusão de um cartão em andamento |
| Idade do trabalho em andamento | Nenhum cartão parado por mais de 7 dias | Quadro Kanban | Escalonamento imediato ao orientador quando houver impedimento externo |
| Taxa de retrabalho | Até 15% dos cartões concluídos reabertos | Histórico de issues | Acima da meta, abre-se investigação de causa-raiz pelo diagrama de Ishikawa |
| Cobertura de testes automatizados | Mínimo de 80% do código (testes unitários e de integração) | Relatório do pipeline de integração contínua | Abaixo da meta, bloqueia-se a publicação em produção |
| Aderência aos critérios de aceite | 100% dos requisitos com critério verificado | Testes de aceitação | Requisito sem verificação não é considerado entregue |
| Sobrecarga da equipe | Até 20 horas semanais por integrante | Autodeclaração semanal | Excesso em duas semanas exige redução de escopo do período |

Fonte: elaborado pelos autores (2026).

## Fontes documentais

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.5 e respectivos quadros.
- [Termo de Abertura do Projeto v1_opngoing.docx](../../docx/Termo%20de%20Abertura%20do%20Projeto%20v1_opngoing.docx), objetivos, EAP, requisitos e restrições.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

A qualidade combina prevenção de falhas no processo e verificação do produto. No COGME, a cobertura de código precisa ser acompanhada de testes que realmente verifiquem cálculos, cotações, encargos e documentos.

- [ ] Criar matriz requisito × verificação × ambiente × dados de teste × resultado esperado × evidência × responsável.
- [ ] Especificar medição de cobertura de 80%, latência, fluxo crítico, severidade de defeitos e critérios de liberação; conciliar a divergência de 70% no painel original.
- [ ] Definir critérios para iniciar uma atividade e considerá-la concluída: requisito claro, revisão, testes aplicáveis, documentação e ausência de defeitos impeditivos.

**Entrega esperada:** Plano de qualidade com indicadores mensuráveis, método de coleta e ação quando a meta não for atingida.
