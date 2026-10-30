# 2.6.1 Escritório de projeto

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** A adoção do GitHub Projects e os ADRs são declarações da monografia; este arquivo não comprova a configuração do quadro ou a execução dos controles. A substituição de relatórios estáticos deve ser conciliada com os objetivos SMART do TAP, que ainda exigem relatórios quinzenais de valor agregado.

O projeto não dispõe de escritório de projetos (PMO) físico ou formalmente instituído, dada sua natureza acadêmica e o tamanho da equipe. Suas funções são exercidas de forma distribuída pelo aluno-gerente e operacionalizadas por meio do GitHub Projects, formalmente designado como fonte única de verdade do projeto pelo registro de decisão arquitetural ADR-001. Nessa condição, a plataforma centraliza o backlog, o quadro Kanban, o registro de riscos, o histórico de decisões e as métricas de fluxo obtidas pelos painéis de análise do próprio repositório, cumprindo em escala reduzida o papel de escritório de projetos. Essa decisão substituiu a produção de relatórios estáticos periódicos e de cronogramas de Gantt mantidos manualmente: caso um diagrama de Gantt seja exigido, ele é derivado a posteriori do quadro Kanban, e não o contrário.

A ausência de estrutura dedicada não implica ausência das funções que um escritório de projetos desempenha. O Quadro 13 relaciona as funções típicas de um escritório de projetos de apoio, segundo a literatura de gerenciamento, ao modo como cada uma é exercida no COGME e ao artefato que a materializa, evidenciando que a supressão da estrutura formal decorre de adaptação ao porte do projeto, e não de desconhecimento da prática.

**Quadro 13 — Funções de escritório de projetos no COGME**

| Função de escritório de projetos | Como é exercida no COGME | Artefato ou ferramenta |
| --- | --- | --- |
| Governança e tomada de decisão | Decisões estruturantes registradas, datadas e justificadas antes da execução | Registros de decisão arquitetural (ADR-001 a ADR-004) |
| Padronização de processos | Modelos de issue e de pull request, convenção de commits e critérios de revisão | Repositório do projeto |
| Repositório de conhecimento | Documentação versionada junto ao código, acessível a toda a equipe | Diretório de documentação do repositório |
| Monitoramento de desempenho | Acompanhamento contínuo das métricas de fluxo e dos indicadores de qualidade | Painel do GitHub Projects e painel de medição (Quadro 12) |
| Controle integrado de mudanças | Alterações de escopo submetidas à aprovação do orientador antes da execução | Comitê de controle de mudanças |
| Gestão de riscos | Registro vivo, revisado a cada marco, com resposta planejada por risco | Registro de riscos (Quadro 15) |
| Suporte metodológico | Definição da abordagem, dos limites de trabalho em progresso e da cadência | Estratégia de adaptação (Quadro 2) |
| Gestão de benefícios | Acompanhamento do valor entregue frente aos objetivos declarados no TAP | Critérios de aceite e objetivos SMART do TAP |

Fonte: elaborado pelos autores (2026).

## Fonte documental

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.6.1.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

O escritório de projeto pode ser uma função de apoio exercida pela equipe. Para o COGME, interessa definir quem mantém padrões e informações, sem criar uma estrutura administrativa incompatível com duas pessoas.

- [ ] Especificar como serão mantidos backlog, decisões, riscos, versões documentais e indicadores no repositório.
- [ ] Definir modelos mínimos para demanda, mudança, risco, revisão e aceite, identificando o responsável pela atualização.
- [ ] Estabelecer uma rotina de conferência da consistência entre EAP, atividades e entregas; verificar se o quadro real está configurado conforme o plano.

**Entrega esperada:** Descrição das funções de apoio, responsáveis e localização dos registros do projeto.
