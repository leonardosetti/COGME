---
id: docs-conhecimento-vet-calculo-cambio
title: Conhecimento — Valor Efetivo Total (VET) de câmbio com spread e IOF
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- conversa do usuário 2026-11-13 (raciocínio de spread e IOF)
- https://www.mercadopago.com.br/blog/cartao-exterior-iof-taxas-fatura
- https://www.traderbrasil.com/blog/calculadora-cambio-remessa-iof-vet.php
- https://skycambio.com.br/blog/iof-2026-cambio-cartao-conta-internacional-dinheiro/
- https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12499.htm
last-revised: '2026-11-13'
lgpd-class: n/a
tags:
- conhecimento
- calculo
- cambio
- spread
- iof
- vet
- simulacao
---

# Conhecimento — Valor Efetivo Total (VET) de câmbio com spread e IOF

## Propósito

Fonte de conhecimento para a simulação de câmbio do COGME. Define o cálculo realista do custo de uma operação de câmbio aplicando spread sobre a cotação comercial e, em seguida, incidindo o IOF sobre o montante já convertido em reais — nunca a soma simples dos dois percentuais.

Este documento é insumo para validação/testes da regra de negócio em `src/backend/services/calculator.py`. Não altera o contrato `spec-004` §3, que já expõe `spread_pct` e `iof_pct` como entrada do usuário, nem embute alíquotas no código (princípio do README: alíquota informada pelo usuário, nenhuma alíquota embutida).

## 1. Passo a passo do cálculo realista

### 1.1 Cotação comercial de referência

Use a cotação interbancária do momento (PTAX do Banco Central do Brasil) para compra ou venda de moeda estrangeira.

### 1.2 Spread cambial

Margem cobrada pela instituição acima do câmbio comercial.

- Descoberta do spread cobrado:
  `Spread (%) = ((Cotação Cobrada − Cotação Comercial) / Cotação Comercial) × 100`
- Projeção da cotação final com spread:
  `Cotação Cobrada = Cotação Comercial × (1 + Spread)`

### 1.3 IOF sobre o valor em reais

O imposto incide sobre o total em reais **após** a aplicação do spread.

- `Valor Base (R$) = Valor em Moeda Estrangeira × Cotação Cobrada`
- `IOF (R$) = Valor Base (R$) × Alíquota do IOF`

### 1.4 Valor Efetivo Total (VET)

- `VET = (Valor Base (R$) + IOF (R$) + Tarifas Fixas) / Valor em Moeda Estrangeira`

Resulta em quanto custa cada unidade de moeda estrangeira, consolidando spread, IOF e tarifas fixas.

## 2. Alíquotas vigentes do IOF (2026)

Conforme o Decreto nº 12.499/2025 (restabelecido pelo STF):

| Tipo de Operação | Alíquota de IOF | Base de Incidência |
|------------------|-----------------|--------------------|
| Cartão de crédito, débito ou pré-pago | 3,50% | Valor da compra convertido em R$ na liquidação |
| Compra de moeda em espécie | 3,50% | Valor total da compra em R$ |
| Remessa para conta própria (gastos/viagem) | 3,50% | Valor enviado em R$ |
| Remessa para investimentos no exterior | 1,10% | Valor enviado em R$ (exige finalidade declarada) |
| Recebimento de recursos do exterior | 0,38% | Valor ingressado em R$ (salvo isenções específicas) |

## 3. Exemplo prático (Compra de US$ 1.000)

Remessa para conta global/gasto internacional de US$ 1.000,00, dólar comercial R$ 5,50, spread 2,0%, IOF 3,5%, sem tarifas fixas:

| Passo | Cálculo | Resultado |
|-------|---------|-----------|
| Cotação com spread | 5,50 × 1,02 | R$ 5,61 |
| Subtotal em reais | 1.000 × 5,61 | R$ 5.610,00 |
| IOF (3,5%) | 5.610 × 0,035 | R$ 196,35 |
| Total desembolsado | 5.610 + 196,35 | R$ 5.806,35 |
| VET final | 5.806,35 / 1.000 | R$ 5,8064 por dólar |

Acréscimo real de 5,57% sobre o dólar comercial (5,50), e não 5,50%.

## 4. Cuidados para uma simulação fiel

- **Data de liquidação:** cartão de crédito costuma converter usando a cotação PTAX do dia do fechamento/processamento da fatura, não do dia da compra — expõe o cálculo à oscilação cambial.
- **Dupla conversão:** compras em moedas diferentes do dólar (pesos, ienes) no cartão costumam passar por conversão prévia da bandeira para USD antes da conversão para BRL, embutindo spread extra.
- **Comparação pelo VET:** para comparar instituições, peça sempre o VET, pois consolida spread, IOF e tarifas.

## 5. Nota de implementação (não produção)

O trecho Python abaixo é protótipo de validação, não código para produção:

- Usa `float` para dinheiro → risco de arredondamento. Produção financeira exige `decimal.Decimal`.
- Sem validação de ranges (spread/IOF 0–100), sem arredondamento (2 casas BRL, 4 casas taxas), sem tarifas fixas.

```python
usd = 1000
cotacao_comercial = 5.50
spread_pct = 0.02
iof_pct = 0.035
tarifa = 0

cotacao_cobrada = cotacao_comercial * (1 + spread_pct)
reais_sem_iof = usd * cotacao_cobrada
custo_spread = usd * (cotacao_cobrada - cotacao_comercial)
iof_valor = reais_sem_iof * iof_pct
total_pago = reais_sem_iof + iof_valor + tarifa
vet = total_pago / usd

print(f"Cotacao cobrada: {cotacao_cobrada:.4f}")
print(f"Custo spread: {custo_spread:.2f}")
print(f"Reais sem IOF: {reais_sem_iof:.2f}")
print(f"IOF: {iof_valor:.2f}")
print(f"Total pago: {total_pago:.2f}")
print(f"VET: {vet:.4f}")
```

## 6. Metadados de ratificação

- **Avaliador:** agent-project-analyst
- **Ratificação:** usuário (CCB), 2026-11-13
- **Status:** publicado como conhecimento do projeto
- **Aplicação:** fonte de conhecimento e oráculo para testes da regra de câmbio; não é regra embutida no código
