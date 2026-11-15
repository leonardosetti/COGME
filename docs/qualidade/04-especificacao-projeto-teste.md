---
id: docs-qualidade-04-especificacao-projeto-teste
title: Especificação de Projeto de Teste — ISTQB CTFL (Test Design Specification)
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/03-plano-testes-istqb.md
- docs/planos/plano-granular/plano-qualidade.md (§5.4.2)
- .ai/specs/spec-004-backend-mvp-v1.spec.md (REQ-01 a REQ-05, REQ-07)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- istqb
- especificacao-de-projeto-de-teste
- test-design-specification
- tecnica-de-teste
---

# Especificação de Projeto de Teste — COGME (ISTQB CTFL)

## 1. Identificação

| Campo | Valor |
|---|---|
| Projeto | COGME |
| Artefato | Test Design Specification |
| Versão | 1.0.0 |
| Base | Plano de Testes (docs/qualidade/03-plano-testes-istqb.md) |
| Rastreabilidade | REQ-01 a REQ-08; UAT-01 a UAT-07; F-01 a F-07 |

## 2. Objetivo

Definir a abordagem de projeto dos casos de teste: técnicas de projeto de teste, itens de teste, entradas, saídas esperadas, ambiente e critéries de passagem/falha por camada da pirâmide.

## 3. Itens de teste

| Item | Descrição | Localização |
|---|---|---|
| Contrato `/v1/simulate` | Simulação de recebimento em BRL, 5 regimes | `src/backend/routers/simulations.py` |
| Contrato `/v1/rates/{currency}` | Cotação vigente USD/EUR em BRL | `src/backend/routers/rates.py` |
| Contrato `/v1/invoice` | Geração de invoice PDF com recálculo server-side | `src/backend/routers/invoices.py` |
| Rotas expandidas de invoice | Listagem, recuperação PDF, finalize, clone, erase | `src/backend/routers/invoices.py` |
| Contrato `/v1/health` | Health da API | `src/backend/routers/common.py` |
| Serviço de cotação (RateService) | Cache TTL, fallback Frankfurter→PTAX, circuit breaker, RatesUnavailable | `src/backend/services/rate_service.py` |
| Serviço de simulação | Cálculo bruto, spread, IOF, líquido, taxa efetiva (invariant) | `src/backend/services/simulation_service.py` |
| Serviço de invoice | Render PDF, formatação pt-BR, LGPD (sem PII em log) | `src/backend/services/invoice_service.py` |
| Schemas (contrato de entrada/saída) | Validação decimal, enums, erro canônico sem eco | `src/shared/schemas.py` |
| Frontend (Jinja2) | Tela de simulação e emissão de invoice | `src/frontend/app.py`, templates |

## 4. Técnicas de projeto de teste aplicadas

| Técnica | Onde é aplicada | Justificativa |
|---|---|---|
| Particionamento de equivalência | Campos numéricos (amount, quantity, spread_pct, iof_pct) | Reduz casos cobrindo classes válidas/inválidas |
| Análise de valores-limite | Limites de decimal (0 exclusivo, máximos, casas decimais) | Erros de arredondamento e escala são defeitos críticos financeiros |
| Teste de decisão/tabela de decisão | 5 regimes de contratação (hourly/daily/weekly/monthly/fixed) | Regras de negócio distintas por regime |
| Teste de transição de estado | Status da invoice (draft → finalized; draft → erase) | Ciclo de vida da invoice (DEC-05, DEC-06) |
| Teste de erro (negativo) | Campos extras, valores pré-calculados, cotação indisponível | Segurança e integridade (sem eco de entrada, 503) |
| Teste exploratório direcionado | Fluxos E2E pela UI (Playwright) | Fluxos críticos cobertos pela UAT |

## 5. Cobertura de teste por requisito

Cobertura analítica mapeada na RTM (`docs/qualidade/10-rtm-qualidade.md`). Resumo:

| Requisito | Técnica principal | Camadas |
|---|---|---|
| REQ-01 (cotação/fallback) | Particionamento + decisão | Unidade, Integração, Funcional |
| REQ-02 (5 regimes) | Tabela de decisão | Unidade, Integração, Funcional |
| REQ-03 (spread/IOF 2 casas) | Valores-limite | Unidade, Integração |
| REQ-04 (invoice PDF) | Estado + negativo | Integração, Funcional |
| REQ-06 (UI responsiva) | Exploratório direcionado | Funcional |
| REQ-07 (cache reduz chamadas) | Particionamento | Unidade, Integração |
| REQ-08 (coverage gate) | Métrica | CI (`test-suite`) |

## 6. Ambiente de teste

- Unitário: Python 3.11, pytest, fixtures determinísticos (relógios, repositórios, provedores falsos). Sem rede.
- Integração: TestClient FastAPI, `RateService` com dublês, relógios fixos; testes com marcador `postgres` usam PostgreSQL efêmero no CI.
- Funcional/E2E: Playwright (Python) + Screenplay Pattern contra stack rodando (front na porta 8000, back proxied). Navegador headless (Chromium).

## 7. Critérios de passagem e falha

- **Pass:** resposta HTTP/status esperado, corpo JSON conforme contrato, decimais como strings exatas, cabeçalhos canônicos (Cache-Control no-store, Content-Disposition), sem PII em logs, PDF começa com `%PDF-`, resultado de simulação confere com os valores da spec-004 §2.
- **Fail:** status inesperado, corpo não confere com o contrato, vazamento de dado do usuário em erro/log, PII no log, PDF ausente ou inválido, coverage < 95%, teste pulado.

## 8. Rastreabilidade

Todo caso de teste especificado aqui é detalhado em `docs/qualidade/05-casos-de-teste.md` (Test Case Specification) e executado conforme `docs/qualidade/06-procedimento-de-teste.md` (Test Procedure Specification), com rastreabilidade 1:1 na RTM.
