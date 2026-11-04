# 2.3.1 Planilha de Custos (em tabela)

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** Valores reproduzidos da monografia como estimativa, sem comprovação de desembolso. A assinatura paga de IA depende de conciliação com a proibição do TAP (§8.4). O uso de 8 horas por dia durante 30 dias corresponde a 240 horas/mês; os consumos de 36 kWh e 240 kWh pressupõem potências médias de 0,15 kW e 1 kW, respectivamente, inferidas da fonte e ainda a confirmar. Validar também o rateio da internet compartilhada e as horas de uso. O total com assinatura é R$ 1.186,40; sem essa despesa, o cenário seria R$ 962,40, mantendo as demais premissas.

A apuração dos custos adota as seguintes premissas declaradas: (i) horizonte de execução de 3 meses (01/09/2026 a 30/11/2026), com base de 30 dias por mês; (ii) não há remuneração financeira efetiva no âmbito acadêmico, razão pela qual o esforço da equipe não é convertido em custo monetário nesta planilha; (iii) tarifa de energia elétrica de R$ 0,80/kWh; (iv) consumo de 8 horas diárias dos equipamentos, em razão da execução local de inferência de modelos de linguagem (llama.cpp) durante as atividades de SDD; (v) uma assinatura individual de Inteligência Artificial a R$ 112,00 mensais, contratada apenas durante os dois meses de maior intensidade de desenvolvimento; e (vi) custo de conectividade estimado em R$ 100,00 mensais, valor a ser confirmado pela equipe. O Quadro 8 apresenta a planilha de custos consolidada.

**Quadro 8 — Planilha de custos do projeto**

| Categoria de Custo | Base de Cálculo | Custo Mensal | Custo Total (3 meses) |
| --- | --- | --- | --- |
| Assinatura de IA (1 licença individual) | 1 × R$ 112,00 por mês, incidente em 2 dos 3 meses | R$ 112,00 | R$ 224,00 |
| Energia elétrica — notebook | 8 h/dia × 30 dias = 36 kWh × R$ 0,80/kWh | R$ 28,80 | R$ 86,40 |
| Energia elétrica — ar-condicionado | 8 h/dia × 30 dias = 240 kWh × R$ 0,80/kWh | R$ 192,00 | R$ 576,00 |
| Internet (banda larga) — estimado | Plano residencial compartilhado | R$ 100,00 | R$ 300,00 |
| Licenciamento de software (FOSS) | 100% de licenças OSI (MIT, Apache 2.0, BSD, GPL) | R$ 0,00 | R$ 0,00 |
| Hospedagem e CI/CD | Planos gratuitos (GitHub Actions/Projects) e API de câmbio em free tier | R$ 0,00 | R$ 0,00 |
| Hardware | Equipamentos próprios da equipe (sem aquisição) | R$ 0,00 | R$ 0,00 |
| CUSTO TOTAL DO PROJETO | Assinaturas de IA + energia elétrica + internet | R$ 432,80 (meses 1–2) / R$ 320,80 (mês 3) | R$ 1.186,40 |

Fonte: elaborado pelos autores (2026).

Observa-se que o desembolso financeiro estimado na monografia é de R$ 1.186,40 para todo o ciclo de três meses, valor previsto para ser absorvido integralmente pela equipe e composto pelo consumo de energia elétrica (R$ 662,40, ou 55,8% do total, dos quais R$ 576,00 referentes à climatização do ambiente de trabalho), pela conectividade (R$ 300,00) e pela assinatura de Inteligência Artificial (R$ 224,00), esta última incidente em apenas dois dos três meses. Por não haver remuneração da equipe, o orçamento do projeto resume-se a despesas recorrentes de baixo valor, o que reforça a adoção do princípio de Governança Mínima Viável (GMV) e a decisão de limitar a produção de artefatos àqueles que efetivamente agregam valor ou são exigidos academicamente.

## Fontes documentais

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.3.1 e respectivos quadros.
- [Termo de Abertura do Projeto v1_opngoing.docx](../../docx/Termo%20de%20Abertura%20do%20Projeto%20v1_opngoing.docx), objetivos, EAP, requisitos e restrições.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

A planilha deve permitir reproduzir os cálculos e distinguir previsão de gasto comprovado. A potência dos equipamentos e o rateio da internet são premissas que precisam de confirmação.

- [ ] Acrescentar item, categoria, quantidade, unidade, valor unitário, período, percentual atribuído ao COGME, total estimado, realizado, fonte e situação da estimativa.
- [ ] Usar energia = potência média em kW × horas de uso × tarifa por kWh; validar notebook/estação e climatização separadamente.
- [ ] Distribuir as despesas mês a mês e conferir totais, meses da assinatura e rateio; identificar custos existentes e custos adicionais sem somá-los duas vezes.

**Entrega esperada:** Planilha rastreável, com fórmulas, premissas e campos de realizado inicialmente sem preenchimento quando não houver comprovantes.
