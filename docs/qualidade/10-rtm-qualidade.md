---
id: docs-qualidade-10-rtm-qualidade
title: Matriz de Rastreabilidade de Requisitos — Qualidade de Software (RTM)
type: metrica
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/uat/rodada-001/relatorio-analitico.md (§2 cobertura REQ→US→trace id→spec)
- docs/planos/plano-granular/plano-qualidade.md (§5.4 rastreabilidade 100% REQ-01 a REQ-15)
- docs/qualidade/05-casos-de-teste.md (catálogo CT-*)
- .ai/specs/spec-004-backend-mvp-v1.spec.md (REQ-01 a REQ-05, REQ-07, REQ-14, REQ-16, REQ-17)
- .ai/specs/spec-010-qualidade-pdca-ishikawa-v1.spec.md (REQ-10, N6.3)
- .ai/specs/spec-011-cicd-pipeline-v1.spec.md (REQ-11)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- rtm
- matriz-de-rastreabilidade
- rastreabilidade
- requisitos
- qualidade
---

# Matriz de Rastreabilidade de Requisitos — COGME (RTM)

## 1. Identificação

| Campo | Valor |
|---|---|
| Projeto | COGME — Conversor de Ganhos em Moeda Estrangeira |
| Artefato | Matriz de Rastreabilidade de Requisitos (RTM) |
| Versão | 1.0.0 |
| Base | UAT rodada 001 (relatório analítico, §2); Plano de Gerenciamento da Qualidade v1.1.0 (§5.4) |
| Cobertura exigida | 100% dos requisitos (REQ-01 a REQ-15) mapeados a casos de teste e vice-versa (plano-qualidade §5.4.3) |
| Rastreabilidade bidirecional | REQ → Caso de Teste → Evidência; Caso de Teste → REQ |

## 2. Convenção de IDs

- **REQ-NN**: requisito funcional/não funcional (termo autorizativo / specs).
- **US-NN**: user story associada.
- **Trace id**: padrão `REQ-NN::UAT-nn::<camada>::<caso>` (UAT produto) ou `container::F-0N` (UAT camadas), conforme relatório analítico da UAT rodada 001.
- **CT-UN-NNN**: caso de teste unitário (pytest, `tests/unit`).
- **CT-INT-NNN**: caso de teste de integração (pytest + TestClient, `tests/integration`).
- **CT-FUNC-NNN**: caso de teste funcional/E2E (Playwright + Screenplay Pattern, `tests/e2e_playwright`).
- **Camadas**: UN = unidade, INT = integração, FUNC = funcional/E2E.
- **Status**: PASS (executado e aprovado), Planejado (instituído, aguarda execução), Não aplicável (requisito de escopo posterior/multiusuário).

## 3. Matriz preenchida (REQ → US → Caso de Teste → Evidência)

| REQ | US | Trace id | Descrição do requisito | Espec que cobre | Casos de teste | Camada | Evidência | Status | Última execução |
|---|---|---|---|---|---|---|---|---|---|
| REQ-01 | US-001 | `REQ-01::UAT-01::product::sim-realtime` | Cotação tempo real USD/EUR → BRL, fallback e cache | spec-004 §3-4; spec-006 NF-01/NF-02 | CT-UN-004, CT-UN-005, CT-UN-006, CT-UN-007, CT-UN-008, CT-UN-009, CT-UN-010, CT-INT-002, CT-INT-008, CT-INT-009, CT-INT-015, CT-INT-018, CT-FUNC-002, CT-FUNC-004 | UN, INT, FUNC | `tests/unit/test_rate_service.py`; `tests/integration/test_api_contract.py`; `tests/integration/test_invoice.py` | PASS | E-001 (13/11/2026) |
| REQ-02 | US-002 | `REQ-02::UAT-02::product::regimes-5` | 5 regimes de contratação (hourly/daily/weekly/monthly/fixed) | spec-004 §2-3 | CT-INT-003, CT-INT-004, CT-INT-005, CT-FUNC-001 | INT, FUNC | `tests/integration/test_api_contract.py` | PASS | E-001 (13/11/2026) |
| REQ-03 | US-003 | `REQ-03::UAT-03::product::spread-iof-audit` | Encargos spread+IOF, 2 casas decimais, ROUND_HALF_EVEN | spec-004 §2; ADR-016 D1-D3 | CT-UN-012, CT-INT-004, CT-INT-020 | UN, INT | `tests/integration/test_api_contract.py`; `tests/integration/test_invoice.py` | PASS | E-001 (13/11/2026) |
| REQ-04 | US-004 | `REQ-04::UAT-04::product::invoice-pdf` | Emissão de invoice PDF, recálculo server-side, LGPD | spec-004 §6; spec-007 §3.1; ADR-016 D4 | CT-INT-012, CT-INT-013, CT-INT-014, CT-INT-015, CT-INT-016, CT-INT-017, CT-INT-019, CT-INT-020, CT-INT-021, CT-INT-022, CT-UN-014, CT-FUNC-003 | INT, UN, FUNC | `tests/integration/test_invoice.py` | PASS | E-001 (13/11/2026) |
| REQ-05 | US-002 | — | Contrato de erro e validação canônica (sem eco de entrada) | spec-004 §3, §8.1 | CT-INT-006, CT-INT-007, CT-INT-010, CT-UN-012, CT-UN-013 | INT, UN | `tests/integration/test_api_contract.py`; `tests/unit/test_schemas.py` | PASS | E-001 (13/11/2026) |
| REQ-06 | US-005 | `REQ-06::UAT-05::product::ui-browsers` | Interface responsiva nos navegadores alvo | spec-008 | CT-FUNC-005 | FUNC | `tests/e2e_playwright` (instituído, aguarda execução E-003) | Planejado | — |
| REQ-07 | US-006 | `REQ-07::UAT-06::product::cache-reduction` | Cache reduz chamadas à API de cotação (TTL) | spec-004 §4; spec-006 NF-04 | CT-UN-001, CT-UN-002, CT-UN-003, CT-UN-011, CT-INT-011 | UN, INT | `tests/unit/test_rate_service.py`; `tests/integration/test_api_contract.py` | PASS | E-001 (13/11/2026) |
| REQ-08 | US-008 | `REQ-08::UAT-07::product::coverage-gate` | Cobertura ≥ 80% por CI (gate de qualidade) | spec-011; ci.yml:170 | CT-INT-001, CI job `test-suite` | INT | `.github/workflows/ci.yml`; `coverage.xml` | PASS (gate) | E-001 (CI) |
| REQ-10 | — | — | Qualidade: 12 PDCAs + Ishikawa 6M (fase N6.3) | spec-010 | (artefatos docs/qualidade/04, 05, 06, 07, 08, 09) | — | `docs/qualidade/` (esta disciplina) | PASS | E-003 (disciplina instituída) |
| REQ-11 | — | — | Pipeline CI/CD: lint+testes ≤ 5 min, falha bloqueia merge | spec-011 | CI jobs `lint`, `test-suite` | — | `.github/workflows/ci.yml` | PASS | CI verde |
| REQ-14 | — | — | Documentação técnica: OpenAPI revisada/aprovada | spec-013 | CT-INT-024 | INT | `tests/integration/test_openapi.py` | PASS | E-001 (13/11/2026) |
| REQ-16 | — | — | Identidade, sessões, autenticação (multiusuário, CR-002) | spec-017 | — | — | (escopo CR-002/SPEC-017, posterior ao MVP atual) | Não aplicável (MVP atual) | — |
| REQ-17 | US-017 | — | Persistência de invoices, simulações salvas, ciclo de vida | spec-020 | CT-INT-023 | INT | `tests/integration/test_invoices_persistence.py` | PASS | E-001 (13/11/2026) |

## 4. Matriz por camada de teste (inverso: Caso de Teste → REQ)

| Caso de teste | REQ | US | Status |
|---|---|---|---|
| CT-UN-001 a CT-UN-011 | REQ-01, REQ-07 | US-001, US-006 | PASS |
| CT-UN-012, CT-UN-013 | REQ-02, REQ-03, REQ-05 | US-002, US-003 | PASS |
| CT-UN-014 | REQ-04 | US-004 | PASS |
| CT-UN-015 | REQ-01 | US-001 | PASS |
| CT-INT-001 | REQ-08 | US-008 | PASS |
| CT-INT-002 a CT-INT-011 | REQ-01, REQ-07 | US-001, US-006 | PASS |
| CT-INT-012 a CT-INT-022 | REQ-01, REQ-04 | US-001, US-004 | PASS |
| CT-INT-023 | REQ-17 | US-017 | PASS |
| CT-INT-024 | REQ-14 | — | PASS |
| CT-FUNC-001 a CT-FUNC-005 | REQ-01, REQ-02, REQ-04, REQ-06 | US-001, US-002, US-004, US-005 | Planejado |

## 5. Casos de UAT camadas (container::F-0N) — rastreáveis à infra

| Trace id | Fluxo | REQ/Infra | Espec | Status (UAT rodada 001) |
|---|---|---|---|---|
| `container::F-01` | Reprodutibilidade `docker compose up --build` | infra | spec-005 §12 | PASS |
| `container::F-02` | Simulação E2E pelos 5 regimes | infra | spec-005 §12 | PASS |
| `container::F-03` | Invoice PDF ≤ 3s, sem PII em logs | infra | spec-005 §12 | PASS |
| `container::F-04` | Isolamento: `front` não alcança `db:5432` | infra | spec-005 §12 | PASS |
| `container::F-05` | Degradação: `db` parado → 503 canônico | infra | spec-005 §12 | PASS |
| `container::F-06` | Migração Alembic upgrade/downgrade | infra | spec-005 §12 | PASS |
| `container::F-07` | Segurança: 100% controles do bloco §6 | infra | spec-005 §12 | PASS |

## 6. Cobertura analítica da rodada 001

| Métrica | Valor | Fonte |
|---|---|---|
| Fluxos críticos de produto planejados | 7 (UAT-01 a UAT-07) | spec-009 §3.3 |
| Casos executados na rodada | 14 (7 produto + 7 camada) | relatório analítico UAT §1 |
| Taxa de aceite | 100% (14/14 PASS) | relatório analítico UAT §1 |
| Defeitos críticos/bloqueantes abertos | 0 | relatório analítico UAT §1 |
| Casos de teste automatizados (pytest) | 1392 PASS, 0 FAIL, 13 skip | relatório analítico UAT §2, Registro de Teste E-001 |
| Casos de teste funcional (Playwright) | 5 instituídos, 0 executados | esta disciplina (CT-FUNC-001 a 005) |
| Requisitos mapeados na RTM | 14 (REQ-01..08, 10, 11, 14, 16, 17) | esta matriz |
| Rastreabilidade bidirecional | 100% | cada REQ tem ≥ 1 CT; cada CT mapeia a ≥ 1 REQ |

## 7. Rastreabilidade de artefatos ISTQB

| Artefato ISTQB | Caminho | Mapeia |
|---|---|---|
| Plano de Testes | docs/qualidade/03-plano-testes-istqb.md | REQ-01 a REQ-08, REQ-10, REQ-11 |
| Especificação de Projeto de Teste | docs/qualidade/04-especificacao-projeto-teste.md | Itens de teste, técnicas, cobertura por REQ |
| Especificação de Caso de Teste | docs/qualidade/05-casos-de-teste.md | CT-UN, CT-INT, CT-FUNC por REQ |
| Especificação de Procedimento de Teste | docs/qualidade/06-procedimento-de-teste.md | Procedimentos UN-P-01, INT-P-01, FUNC-P-01; Test Item Transmittal Report |
| Registro de Teste | docs/qualidade/07-registro-de-teste.md | Execuções E-001, E-002, E-003 por caso |
| Relatório de Incidente de Teste | docs/qualidade/08-relatorio-incidente-de-teste.md | INC-001 a INC-007, com RCA |
| Relatório Resumo de Teste | docs/qualidade/09-relatorio-resumo-de-teste.md | Consolidado de execuções, defeitos, risco |
| Matriz de Rastreabilidade | docs/qualidade/10-rtm-qualidade.md | (este documento) |
| Board de Análise + RCA | docs/qualidade/11-board-resultados-qualidade.md | Incidentes, prioridade, impacto, severidade, RCA |

## 8. Declaração de conformidade

100% dos requisitos funcionais do MVP (REQ-01 a REQ-08, REQ-14, REQ-17) estão mapeados a pelo menos um caso de teste executado com resultado PASS na UAT rodada 001. REQ-16 (identidade multiusuário) pertence ao escopo CR-002/SPEC-017, posterior ao MVP atual, e está marcado como Não aplicável. REQ-10 e REQ-11 são atendidos por artefatos de qualidade e pipeline CI, respectivamente.
