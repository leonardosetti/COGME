# 2.2 Gerenciamento de Escopo

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** A monografia inclui comparação de provedores e encaminhamento externo. O TAP lista múltiplas plataformas de transferência entre funcionalidades futuras. É necessário distinguir comparação informativa de execução de transferências e registrar a aprovação do escopo adicional; esta organização documental não constitui aprovação.

O escopo do projeto COGME está restrito à entrega de um Produto Mínimo Viável (MVP) em regime acadêmico, compreendendo a simulação cambial a partir de cotação oficial do Banco Central do Brasil (PTAX), a consulta e a comparação de custo efetivo entre provedores de pagamento internacional e a emissão do documento de cobrança correspondente. O COGME atua exclusivamente como ferramenta de consulta e apoio à decisão: o sistema reúne cotações e tarifas públicas, apresenta o comparativo e encaminha o usuário ao provedor de sua escolha, sem executar, intermediar ou processar qualquer operação de pagamento. Funcionalidades não essenciais — como a execução de transferências, a integração transacional com as plataformas de pagamento, o cadastro de múltiplos usuários ou relatórios gerenciais avançados — ficam reservadas a versões futuras, salvo aprovação formal de mudança de escopo. Registre-se que o comparativo de provedores é informativo e baseado em tarifas públicas parametrizadas, não constituindo recomendação financeira nem intermediação de operação cambial. O desenvolvimento ocorre integralmente do zero, sem reaproveitamento de código ou sistemas legados, demandando esforço completo de modelagem, codificação e testes dentro do período letivo.

## Temas relacionados

- [2.2.1 Levantamento de requisitos](02_02_01_levantamento_de_requisitos.md)
- [2.2.2 E.A.P](02_02_02_eap.md)

## Fontes documentais

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.2 e respectivos quadros.
- [Termo de Abertura do Projeto v1_opngoing.docx](../../docx/Termo%20de%20Abertura%20do%20Projeto%20v1_opngoing.docx), objetivos, EAP, requisitos e restrições.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

O escopo do produto define o que o COGME faz; o escopo do projeto inclui também requisitos, modelagem, testes, implantação e documentação. Uma nova função só pode ser assumida após considerar o trabalho necessário para entregá-la.

- [ ] Consolidar uma declaração de escopo com objetivo, entregas, inclusões, exclusões, premissas, restrições e critérios de aceite.
- [ ] Separar comparação informativa e encaminhamento externo de execução de pagamentos; conciliar REQ-16 a REQ-19 com o TAP.
- [ ] Registrar como o orientador validará as entregas e como pedidos de novas moedas, provedores ou relatórios serão avaliados.

**Entrega esperada:** Quadro de escopo incluído/excluído e critérios verificáveis para aceitar cada entrega do MVP.
