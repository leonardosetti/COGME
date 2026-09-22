# 2.6.2 Matriz de responsabilidade

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** Papéis: Leonardo David Silva Setti é o gerente e também desenvolvedor; Fabricio de Lima Cabral é desenvolvedor; Nivaldo Carleto é orientador e cliente. A matriz de origem foi preservada, mas as linhas de ADR, backend, frontend e pipeline não indicam A (aprovador). Definir a autoridade de aceite dessas entregas antes de considerar a RACI completa. A atribuição de patrocinador ao orientador na monografia também difere do campo Patrocinador: N/A no TAP.

A matriz de responsabilidades do projeto adota o formato RACI simplificado, coerente com a dimensão da equipe e com a premissa P7, segundo a qual o professor orientador é o único stakeholder formal com poder de aprovação, acumulando os papéis de patrocinador, avaliador e presidente do comitê de controle de mudanças. O Quadro 14 apresenta a matriz aplicada às principais entregas do projeto, na qual se adota a convenção R para responsável pela execução, A para aprovador, C para consultado e I para informado.

**Quadro 14 — Matriz de responsabilidade (RACI)**

| Entrega / Decisão | Gerente do Projeto | Desenvolvedor | Orientador (Cliente/CCB) |
| --- | --- | --- | --- |
| Termo de Abertura do Projeto (TAP) | R | C | A |
| Planos de Gerenciamento | R | C | A |
| Levantamento de Requisitos | R | C | A |
| Registros de Decisão Arquitetural (ADR) | R | C | I |
| Desenvolvimento do Backend | C | R | I |
| Desenvolvimento do Frontend | C | R | I |
| Testes Automatizados e UAT | C | R | A |
| Pipeline de CI e Implantação | C | R | I |
| Solicitações de Mudança | R | C | A |
| Documentação Técnica e Manual | R | C | A |
| Apresentação Final e Aceite | R | C | A |

Fonte: elaborado pelos autores (2026).

## Fonte documental

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.6.2.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

A RACI deve esclarecer execução, responsabilidade final, consulta e informação. Na adaptação do COGME, aprovação técnica e aceite acadêmico podem ser decisões diferentes e precisam ser explicitadas.

- [ ] Mapear os papéis aos nomes e revisar cada linha para indicar responsável pela execução e um responsável final claramente definido.
- [ ] Preencher as lacunas das linhas de ADR, backend, frontend e pipeline; registrar quem revisa tecnicamente e quando o orientador participa.
- [ ] Conferir a atribuição de patrocinador no TAP e na monografia e obter validação da matriz, sem presumir que já foi aprovada.

**Entrega esperada:** Matriz RACI completa, com legenda e limites de autoridade por tipo de decisão.

**Apoio metodológico:** [PMI — Papéis, responsabilidades e recursos](https://www.pmi.org/learning/library/best-practices-managing-people-quality-management-7012).
