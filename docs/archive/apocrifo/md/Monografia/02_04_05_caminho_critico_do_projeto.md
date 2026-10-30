# 2.4.5 Caminho crítico do projeto

[Planejamento e índice](../../../PLANEJAMENTO.md)

O caminho crítico ainda não pode ser determinado com os dados disponíveis. Seu cálculo requer uma rede completa de atividades, durações estimadas, calendário de trabalho e vínculos de precedência consistentes. A monografia apresenta uma cadeia candidata, mas também informa que o cálculo de folgas por atividade permanece pendente.

A cadeia narrada na fonte coloca frontend e PDF em sequência após o motor de comparação. Entretanto, a tabela de precedência permite que frontend e PDF sejam desenvolvidos em paralelo após a lógica de negócio. Portanto, essa cadeia não deve ser apresentada como caminho crítico comprovado.

## Procedimento para consolidação

1. Resolver os identificadores duplicados da EAP e decompor os pacotes em atividades.
2. Estimar as durações, registrando esforço, disponibilidade dos integrantes e calendário.
3. Completar a rede, incluindo integração PTAX, comparação de provedores, testes, documentação e aceite.
4. Calcular início e término mais cedo por avanço na rede e início e término mais tarde por retrocesso.
5. Calcular a folga total: início mais tarde menos início mais cedo, ou término mais tarde menos término mais cedo.
6. Identificar os caminhos de maior duração e as atividades com folga total zero na rede sem restrições adicionais; avaliar conflitos de recursos e recalcular o cronograma após o nivelamento.

## Capacidade do marco parcial

A monografia informa 64 horas-equipe de capacidade e 46 horas de esforço no plano de ação do marco parcial. A diferença é de 18 horas-equipe, equivalente a 28,125% da capacidade (aproximadamente 28%). Esse saldo de capacidade não é a folga total de uma atividade e não comprova o caminho crítico.

## Marcos de referência e pendências

A monografia prevê entrega parcial em 22/09/2026 e final em 30/11/2026. O TAP também contém 08/09/2026 para a parcial, exigindo conciliação documental. Permanecem pendentes a duração total calculada, as folgas individuais, o caminho crítico e a comprovação da aprovação dos marcos.

Consultar a [Tabela de Precedência](02_04_04_tabela_de_precedencia.md) e a [Rede de projeto](02_04_03_rede_de_projeto.md) para as dependências preliminares.

## Fontes documentais

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.4.5 e respectivos quadros.
- [Termo de Abertura do Projeto v1_opngoing.docx](../../docx/Termo%20de%20Abertura%20do%20Projeto%20v1_opngoing.docx), objetivos, EAP, requisitos e restrições.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

O caminho crítico depende da rede e das durações, e pode mudar quando as estimativas ou os recursos mudam. A sequência narrada na monografia e o saldo de 18 horas-equipe não substituem esse cálculo.

- [ ] Preencher uma tabela com duração, início e término mais cedo, início e término mais tarde e folga total por atividade.
- [ ] Calcular a rede e identificar o caminho de maior duração; registrar calendário, restrições e possíveis caminhos críticos simultâneos.
- [ ] Rever a viabilidade com os recursos disponíveis e atualizar o cálculo após mudanças; separar folga calculada, saldo de capacidade e reserva planejada.

**Entrega esperada:** Memória de cálculo reproduzível, duração prevista do projeto e identificação fundamentada das atividades críticas.

**Apoio metodológico:** [Da EAP ao cronograma de caminho crítico](https://www.pmi.org/learning/library/moving-work-breakdown-structure-critical-path-6978).
