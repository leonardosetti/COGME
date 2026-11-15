---
id: docs-qualidade-06-procedimento-de-teste
title: Especificação de Procedimento de Teste — ISTQB CTFL (Test Procedure Specification)
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/05-casos-de-teste.md
- docs/planos/plano-granular/plano-qualidade.md (§5.4.2, §5.5.1)
- .github/workflows/ci.yml (jobs de teste)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- istqb
- procedimento-de-teste
- test-procedure-specification
- test-item-transmittal-report
- execucao-de-teste
---

# Especificação de Procedimento de Teste — COGME (ISTQB CTFL)

## 1. Identificação

| Campo | Valor |
|---|---|
| Projeto | COGME |
| Artefato | Test Procedure Specification (+ Test Item Transmittal Report) |
| Versão | 1.0.0 |
| Base | Test Case Specification (docs/qualidade/05-casos-de-teste.md); CI pipeline (.github/workflows/ci.yml) |
| Rastreabilidade | RTM em docs/qualidade/10-rtm-qualidade.md |

## 2. Procedimentos de execução por camada

### 2.1 Camada Unidade — pytest

**Procedimento:** `UN-P-01`

1. Garantir Python 3.11 e dependências de dev instaladas (`pip install -r requirements-dev.txt`).
2. Executar: `python -m pytest tests/unit -q`.
3. Verificar: todos PASS; 0 FAIL.
4. Opcional (cobertura): `python -m pytest tests/unit tests/integration --cov=src --cov-report=term-missing`.

**Critério de passagem:** 0 falhas. Qualquer falha bloqueia o commit local.

### 2.2 Camada Integração — pytest + TestClient

**Procedimento:** `INT-P-01`

1. Executar suíte completa: `python -m pytest tests/unit tests/integration tests/agents -q --tb=short`.
2. Para testes de persistência com marcador `postgres`: requer `COGME_TEST_DATABASE_URL` (PostgreSQL efêmero no CI).
3. Verificar: 0 falhas, 0 pulados (regra CI zero-skipping).

**Critério de passagem:** 0 falhas, 0 skips.

### 2.3 Camada Funcional/E2E — Playwright + Screenplay Pattern

**Procedimento:** `FUNC-P-01`

1. Subir stack de teste (front + back + db): `docker compose up --build -d db migrate back front` com `.env` de teste (credenciais dummy, válidas somente no job).
2. Aguardar health do front (`GET /` → 200).
3. Definir `COGME_BASE_URL=http://localhost:8001` (front publicada na porta 8000 do container, mapeada 8001 no host).
4. Instalar navegadores Playwright (primeira execução): `playwright install chromium`.
5. Executar: `python -m pytest tests/e2e_playwright -q`.
6. Verificar: 0 falhas.
7. Derrubar stack: `docker compose down -v --remove-orphans`.

**Critério de passagem:** 0 falhas nos 5 casos CT-FUNC-*.

## 3. Execução no CI (gate constitucional)

Conforme `.github/workflows/ci.yml`, job `test-suite`:

- Timeout: 5 min (REQ-11).
- PostgreSQL efêmero (digest-pinada `postgres:15-alpine@sha256:...`).
- Rodada de migração Alembic: `upgrade head` → `check` → `downgrade base`.
- Instala bibliotecas nativas WeasyPrint (Pango etc.).
- Executa: `python -m pytest tests/unit tests/integration tests/agents -q --tb=short --cov=src --cov-report=xml:coverage.xml --cov-report=term-missing --cov-fail-under=95 --junitxml=junit.xml -p no:cacheprovider`.
- Gate adicional: `grep` por `, N skipped` no relatório; qualquer teste pulado → exit 1 (zero-skipping).
- Artefatos publicados (sempre): `coverage.xml`, `junit.xml` (nomes LGPD-safe, sem PII).

## 4. Test Item Transmittal Report (ISTQB)

Registro de transmissão dos itens de teste entre as etapas de teste. Preenchido a cada execução da suíte.

| Item de teste | Identificador | Versão | Local | Transmitido de | Transmitido para | Data | Transmitido por | Recebido por | Status |
|---|---|---|---|---|---|---|---|---|---|
| Contrato /v1/simulate | CT-INT-003..005 | 1.0.0 | src/backend/routers/simulations.py | Desenvolvimento | Integração | 13/11/2026 | agent-project-analyst | qa-sdet | Aprovado |
| Contrato /v1/rates/{currency} | CT-INT-002, CT-INT-008..009 | 1.0.0 | src/backend/routers/rates.py | Desenvolvimento | Integração | 13/11/2026 | agent-project-analyst | qa-sdet | Aprovado |
| Contrato /v1/invoice | CT-INT-012..022 | 1.0.0 | src/backend/routers/invoices.py | Desenvolvimento | Integração | 13/11/2026 | agent-project-analyst | qa-sdet | Aprovado |
| RateService (cache/fallback/breaker) | CT-UN-001..011 | 1.0.0 | src/backend/services/rate_service.py | Desenvolvimento | Unidade | 13/11/2026 | agent-project-analyst | qa-sdet | Aprovado |
| Schemas (contrato de erro) | CT-UN-012..013, CT-INT-024 | 1.0.0 | src/shared/schemas.py | Desenvolvimento | Unidade + Integração | 13/11/2026 | agent-project-analyst | qa-sdet | Aprovado |
| Frontend simulação + invoice | CT-FUNC-001..005 | 1.0.0 | src/frontend/app.py + templates | Desenvolvimento | Funcional (Playwright) | 14/11/2026 | agent-project-analyst | qa-sdet | Pendente execução |

**Observação:** itens de frontend transmitidos à camada funcional aguardam execução dos casos CT-FUNC-* (nova camada Playwright instituída nesta disciplina).

## 5. Ambiente e dados de teste

- Todos os dados são sintéticos (P-04, constitution.md:90): nomes, CPFs, endereços, valores são fictícios (`Pessoa Fictícia da Silva`, `INV-0001`, `15/01/2026`).
- Nenhum dado de terceiros é usado.
- Relógios fixos (`2026-10-30 16:00 UTC`) para determinismo.
- Nenhum teste acessa rede real nem sistema de arquivos de produção.

## 6. Rastreabilidade do procedimento

Cada procedimento `*-P-01` executa os casos de `docs/qualidade/05-casos-de-teste.md` mapeados na RTM (`docs/qualidade/10-rtm-qualidade.md`). O resultado de execução é registrado no Registro de Teste (`docs/qualidade/07-registro-de-teste.md`) e consolidado no Relatório Resumo de Teste (`docs/qualidade/09-relatorio-resumo-de-teste.md`).
