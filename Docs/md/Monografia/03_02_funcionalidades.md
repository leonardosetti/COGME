# 3.2 Funcionalidades

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** As funcionalidades e metas são as descritas na monografia, não resultados de validação do software. REQ-16 a REQ-19 precisam ser conciliados com o escopo do TAP. As metas de latência, redução de chamadas e cobertura funcional exigem evidências de testes antes de serem declaradas alcançadas.

O MVP descrito na monografia contempla as seguintes funcionalidades principais, rastreáveis aos requisitos levantados na seção 2.2.1: simulação de conversão cambial em tempo real entre USD/EUR e BRL, com tempo de resposta de até 3 segundos (REQ-01, REQ-05); suporte a cinco regimes de contratação — hora, dia, semana, mês e valor fixo (REQ-02); aplicação de encargos financeiros simulados, incluindo spread e Imposto sobre Operações Financeiras (IOF), com precisão de duas casas decimais (REQ-03); emissão de invoice em formato PDF, gerada em até 3 segundos por documento (REQ-04); interface web responsiva, compatível com os principais navegadores (REQ-06); cache de cotações cambiais, reduzindo em ao menos 50% as chamadas à API externa (REQ-07); obtenção da cotação oficial de referência junto à API do Banco Central do Brasil (PTAX), com registro de data, moeda e tipo de cotação (REQ-16); comparativo de custo efetivo entre, no mínimo, quatro provedores de pagamento internacional, considerando spread, tarifa fixa e valor líquido estimado por operação (REQ-17); ranqueamento automático dos provedores pelo maior valor líquido a receber, com detalhamento da composição do custo (REQ-18); e encaminhamento do usuário ao site oficial do provedor selecionado, com aviso de que a operação ocorre fora do COGME (REQ-19).

## Fonte documental

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 3.2.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

Cada funcionalidade deve ser demonstrada em um cenário do usuário, com entradas e resultados esperados. Uma tela existente não comprova o atendimento integral ao requisito.

- [ ] Montar matriz requisito × funcionalidade × cenário × evidência × resultado × situação de aceite.
- [ ] Demonstrar conversão, cinco regimes, encargos, PDF, cotação de referência e comparativo conforme aprovação do escopo; incluir entradas inválidas e indisponibilidade externa.
- [ ] Medir metas de desempenho no ambiente declarado e registrar limitações; manter simulação e comparação separadas de operações de pagamento.

**Entrega esperada:** Roteiro de demonstração e matriz de evidências funcionais, sem marcar como entregue o que ainda não foi verificado.
