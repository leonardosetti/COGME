# 2.4.1 Atividades

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** A tabela contém exemplos para quatro pacotes, não a decomposição completa da EAP. Permanecem pendentes as demais atividades, suas durações, responsáveis, calendários e dependências. Nenhuma atividade está sendo declarada executada.

As atividades do projeto não coincidem com os pacotes de trabalho da EAP: em linha com o Domínio de Planejamento do PMBOK® 7ª edição, elas são derivadas dos pacotes por decomposição. Enquanto a EAP foca em entregas — expressas por substantivos —, a lista de atividades foca nas ações necessárias para gerá-las, expressas por verbos. Cada atividade derivada recebe código próprio (prefixo A), predecessoras, sucessoras, recursos alocados e restrições, e é a partir dessa lista, e não diretamente da EAP, que o cronograma é construído. A execução é gerida por quadro Kanban no GitHub Projects, com sistema puxado e limites de trabalho em progresso. O Quadro 9 exemplifica a decomposição aplicada a quatro pacotes representativos.

**Quadro 9 — Decomposição de pacotes de trabalho em atividades**

| Pacote da EAP (entrega) | Atividades Derivadas (ações) |
| --- | --- |
| N1.2 Identificação de Stakeholders | A1.2.1 Listar stakeholders; A1.2.2 Classificar poder/interesse; A1.2.3 Documentar matriz |
| N2.1 Requisitos Funcionais | A2.1.1 Entrevistar o orientador; A2.1.2 Redigir histórias de usuário; A2.1.3 Validar com o stakeholder |
| N4.1 Seleção da Stack FOSS | A4.1.1 Pesquisar candidatos; A4.1.2 Aplicar critérios de governança mínima viável; A4.1.3 Redigir o ADR-002; A4.1.4 Validar com protótipo |
| N5.1 Backend — Lógica de Negócio | A5.1.1 Modelar entidades de domínio (câmbio, spread, IOF); A5.1.2 Implementar serviços de cálculo; A5.1.3 Escrever testes unitários; A5.1.4 Documentar a API (OpenAPI) |

Fonte: elaborado pelos autores (2026).

## Fontes documentais

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.4.1 e respectivos quadros.
- [Termo de Abertura do Projeto v1_opngoing.docx](../../docx/Termo%20de%20Abertura%20do%20Projeto%20v1_opngoing.docx), objetivos, EAP, requisitos e restrições.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

A entrega “módulo de simulação” pode exigir especificar regras, implementar o cálculo, integrar a interface e testar cenários. Cada ação precisa ser identificável e produzir um resultado verificável.

- [ ] Decompor todos os pacotes relevantes, incluindo revisão, integração, correções, documentação e aceite.
- [ ] Registrar código, pacote de origem, verbo e objeto, saída, esforço, duração, responsável, predecessoras e critério de conclusão.
- [ ] Indicar a base das estimativas e revisar atividades grandes ou vagas antes de colocá-las em execução.

**Entrega esperada:** Lista completa de atividades, sem confundir quantidade de cartões com percentual de avanço do projeto.
