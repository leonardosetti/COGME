---
id: docs-qualidade-01-piramide-testes
title: Pirâmide de Testes — COGME
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/planos/plano-granular/plano-qualidade.md (§5.2, §5.3, §5.4)
- docs/qualidade/00-contexto-disciplina-qualidade.md (§3.1)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- piramide-de-testes
- estrategia-de-teste
- camadas
---

# Pirâmide de Testes — COGME

A pirâmide organiza os testes em três camadas por custo de execução, velocidade de feedback e volume de casos. Quanto mais baixa a camada, mais casos e feedback mais rápido. Quanto mais alta a camada, menos casos e feedback mais caro.

```
        /\
       /  \  Funcional / E2E   (Playwright + Screenplay)
      /____\  Poucos casos, fluxos críticos pela UI
     /      \
    /   Integração   \  (pytest + TestClient)
   /_________________\  Contratos /v1, persistência, PDF, erros
  /                   \
 /      Unidade       \  (pytest)
/_______________________\  Muitos casos, regras de negócio, schemas, cálculo
```

## Camada 1 — Unidade (base, maior volume)

**Objetivo:** validar unidades isoladas de código (funções, classes, serviços, regras de negócio, schemas, cálculo decimal, circuit breaker).

- Ferramenta: `pytest` (Python).
- Local: `tests/unit`.
- Dublês: repositórios, provedores de cotação, relógios — todos em memória e determinísticos (conftest da camada).
- Sem rede, sem banco, sem sistema de arquivos real.
- Execução: rápida; roda a cada commit local e no CI (`test-suite`).

Exemplos cobertos no projeto: `test_rate_service.py` (cache/TTL, fallback, circuit breaker), `test_schemas.py` (validação decimal), `test_invoice_number.py` (numeração), `test_calculator.py`, `test_circuit_breaker.py`.

**Critério da camada:** ≥ 80% dos casos de teste do projeto residem aqui.

## Camada 2 — Integração (meio, volume médio)

**Objetivo:** validar a cooperação entre camadas e contratos expostos.

- Ferramenta: `pytest` + `fastapi.testclient.TestClient` (Python).
- Local: `tests/integration`.
- Dublês: `RateService` com `ScriptedProvider`/`failing_provider`, `MemoryRepository`, relógios fixos. A dependência é injetada via `app.dependency_overrides`.
- Sem rede real; o `lifespan` não roda (sem banco nem HTTP real).
- Execução: rápida-média; roda no CI (`test-suite`) com PostgreSQL efêmero para testes de persistência (`postgres` marker).

Exemplos cobertos: `test_api_contract.py` (contrato exato §2, regimes, erros canônicos, cache), `test_invoice.py` (invoice PDF, recálculo server-side, LGPD no log, XSS escapado), `test_api_validation.py`, `test_invoices_persistence.py`.

**Critério da camada:** 100% dos requisitos REQ-01 a REQ-07 cobertos por testes de integração ou unidade (plano-qualidade §5.4.2).

## Camada 3 — Funcional / E2E (topo, menor volume)

**Objetivo:** validar fluxos críticos de ponta a ponta pela interface do usuário.

- Ferramenta: Playwright (Python), padrão Screenplay Pattern.
- Local: `tests/e2e_playwright`.
- Alvo: stack rodando (front + back + db), navegador headless.
- Casos: simulação pelos 5 regimes, emissão de invoice PDF, download do PDF, erro de cotação indisponível.

Exemplos: `test_simulacao_funcional.py`, `test_emissao_invoice_funcional.py`.

**Critério da camada:** apenas fluxos críticos (UAT-01..UAT-07); casos de exceção e borda ficam nas camadas abaixo.

## Regras de composição

1. **Defeito baixo o máximo possível:** se um defeito pode ser capturado em unidade, não escreve o caso em integração; se pode ser em integração, não escreve em funcional.
2. **Um nível, uma responsabilidade:** unidade não acessa rede; integração não testa UI; funcional não valida regra de negócio detalhada (já coberta abaixo).
3. **Volume:** unidade ≫ integração ≫ funcional.

## Rastreabilidade

| Camada | REQ cobertos | Critério de qualidade (plano-qualidade) |
|---|---|---|
| Unidade | REQ-01, REQ-02, REQ-03, REQ-04, REQ-07 | Testes críticos 100% REQ-01..REQ-07 (§5.4.2) |
| Integração | REQ-01 a REQ-07 | Cobertura ≥ 80% sobre `src/` (§5.4.2) |
| Funcional | REQ-01 (cotação), REQ-04 (invoice PDF), REQ-06 (UI) | UAT sem defeitos críticos/bloqueantes |
