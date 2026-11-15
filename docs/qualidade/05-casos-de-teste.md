---
id: docs-qualidade-05-casos-de-teste
title: Especificação de Caso de Teste — ISTQB CTFL (Test Case Specification)
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/04-especificacao-projeto-teste.md
- docs/planos/plano-granular/plano-qualidade.md (§5.4.2)
- docs/uat/rodada-001/relatorio-analitico.md (trace ids)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- istqb
- caso-de-teste
- test-case-specification
- rastreabilidade
---

# Especificação de Caso de Teste — COGME (ISTQB CTFL)

## 1. Identificação

| Campo | Valor |
|---|---|
| Projeto | COGME |
| Artefato | Test Case Specification |
| Versão | 1.0.0 |
| Base | Test Design Specification (docs/qualidade/04-especificacao-projeto-teste.md) |
| Rastreabilidade | RTM em docs/qualidade/10-rtm-qualidade.md |

## 2. Convenção de ID de caso de teste

`CT-<camada>-<NNN>` onde `<camada>` ∈ {UN, INT, FUNC}:

- `CT-UN-*` — unidade (pytest, `tests/unit`)
- `CT-INT-*` — integração (pytest + TestClient, `tests/integration`)
- `CT-FUNC-*` — funcional/E2E (Playwright + Screenplay, `tests/e2e_playwright`)

Cada caso carrega: ID, título, requisito (REQ), user story (US), trace id, camada, pré-condição, entrada, resultado esperado, pós-condição, status.

## 3. Catálogo de casos de teste (unidade e integração — implementados)

### Camada Unidade (pytest)

| ID | Título | REQ | US | Trace id | Resultado |
|---|---|---|---|---|---|
| CT-UN-001 | Cache fresco devolve sem chamar rede (REQ-07) | REQ-07 | US-006 | REQ-07::UAT-06::product::cache-reduction | PASS |
| CT-UN-002 | Idade do cache é inclusiva no limite do TTL (REQ-07) | REQ-07 | US-006 | REQ-07::UAT-06::product::cache-reduction | PASS |
| CT-UN-003 | Cache expirado busca e grava com fetched_at atual (REQ-07) | REQ-07 | US-006 | REQ-07::UAT-06::product::cache-reduction | PASS |
| CT-UN-004 | Fallback Frankfurter→PTAX, só PTAX gravada (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-UN-005 | Primeira fonte para, PTAX não chamada (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-UN-006 | Circuito aberto pula provedor sem chamá-lo (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-UN-007 | 3 falhas abrem circuito; quarta pula (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-UN-008 | Todas fontes falham → cache stale (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-UN-009 | Sem cache e sem fonte → RatesUnavailableError 503 (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-UN-010 | Cotação rejeitada no aceite não é gravada (REQ-01, §8.1) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-UN-011 | 10 req com cache reduzem chamadas de rede ≥ 50% (REQ-07) | REQ-07 | US-006 | REQ-07::UAT-06::product::cache-reduction | PASS |
| CT-UN-012 | Validação decimal: limites, casas, não-echo de valor | REQ-02, REQ-03 | US-002, US-003 | REQ-02::UAT-02::product::regimes-5 | PASS |
| CT-UN-013 | Schemas rejeitam valores desconhecidos/campos extras | REQ-02 | US-002 | REQ-02::UAT-02::product::regimes-5 | PASS |
| CT-UN-014 | Numeração de invoice única (DEC-06) | REQ-17 | US-017 | — | PASS |
| CT-UN-015 | Circuit breaker: parâmetros padrão, reset, bloqueio | REQ-01 | US-001 | — | PASS |

### Camada Integração (pytest + TestClient)

| ID | Título | REQ | US | Trace id | Resultado |
|---|---|---|---|---|---|
| CT-INT-001 | Health responde 200 ok (§3) | REQ-08 | US-008 | REQ-08::UAT-07::product::coverage-gate | PASS |
| CT-INT-002 | Rates/USD devolve cotação exata, decimal como string (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-INT-003 | Simulate exemplo §2 exato (USD hourly 30×160) (REQ-02) | REQ-02 | US-002 | REQ-02::UAT-02::product::regimes-5 | PASS |
| CT-INT-004 | Cinco regimes produzem bruto/spread/IOF/líquido da §2 (REQ-02/03) | REQ-02, REQ-03 | US-002, US-003 | REQ-03::UAT-03::product::spread-iof-audit | PASS |
| CT-INT-005 | Regime fixed aceito sem quantidade (REQ-02) | REQ-02 | US-002 | REQ-02::UAT-02::product::regimes-5 | PASS |
| CT-INT-006 | Rota inexistente → 404 not_found, sem eco do caminho (§3) | REQ-08 | US-008 | — | PASS |
| CT-INT-007 | Método errado → 405 com Allow, chave not_found (§3) | REQ-08 | US-008 | — | PASS |
| CT-INT-008 | Sem fonte e sem cache → 503 rates_unavailable (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-INT-009 | Simulate sem cotação → 503 rates_unavailable (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-INT-010 | Erro inesperado → 500 internal_error, sem traceback/vazamento (§3) | REQ-08 | US-008 | — | PASS |
| CT-INT-011 | Segunda requisição no TTL usa cache (REQ-07) | REQ-07 | US-006 | REQ-07::UAT-06::product::cache-reduction | PASS |
| CT-INT-012 | Invoice PDF: 200, application/pdf, anexo, no-store (REQ-04) | REQ-04 | US-004 | REQ-04::UAT-04::product::invoice-pdf | PASS |
| CT-INT-013 | Servidor recalcula simulação; contexto com valores §2 (REQ-04) | REQ-04 | US-004 | REQ-04::UAT-04::product::invoice-pdf | PASS |
| CT-INT-014 | Cliente não envia valores pré-calculados → 400 (REQ-04, §8.1) | REQ-04 | US-004 | REQ-04::UAT-04::product::invoice-pdf | PASS |
| CT-INT-015 | Cotação indisponível bloqueia invoice → 503 (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-INT-016 | WeasyPrint ausente → 503 pdf_unavailable; LGPD no log (REQ-04) | REQ-04 | US-004 | REQ-04::UAT-04::product::invoice-pdf | PASS |
| CT-INT-017 | `<script>` no nome é escapado (XSS) (REQ-04) | REQ-04 | US-004 | REQ-04::UAT-04::product::invoice-pdf | PASS |
| CT-INT-018 | Cotação stale mostra aviso; fresca não (REQ-01) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | PASS |
| CT-INT-019 | Fonte PTAX mostra boletim; Frankfurter não (REQ-04) | REQ-04 | US-004 | REQ-04::UAT-04::product::invoice-pdf | PASS |
| CT-INT-020 | Valores formatados pt-BR (R$ 23.430,62; data dd/mm/aaaa) (REQ-04) | REQ-04 | US-004 | REQ-04::UAT-04::product::invoice-pdf | PASS |
| CT-INT-021 | Aviso constante (NOTICE) no rodapé (REQ-04) | REQ-04 | US-004 | REQ-04::UAT-04::product::invoice-pdf | PASS |
| CT-INT-022 | PDF real com WeasyPrint (CI com Pango) (REQ-04) | REQ-04 | US-004 | REQ-04::UAT-04::product::invoice-pdf | PASS (skip se sem Pango) |
| CT-INT-023 | Persistência de invoice (crud, clone, erase LGPD) | REQ-17 | US-017, US-004 | — | PASS |
| CT-INT-024 | OpenAPI sem 422; contrato de erro canônico | REQ-08 | US-008 | — | PASS |

### Camada Funcional/E2E (Playwright + Screenplay Pattern)

| ID | Título | REQ | US | Trace id | Status |
|---|---|---|---|---|---|
| CT-FUNC-001 | Simulação pelo front: 5 regimes exibem resultado correto | REQ-02 | US-002 | REQ-02::UAT-02::product::regimes-5 | Planejado |
| CT-FUNC-002 | Simulação USD/EUR → BRL em tempo real (cotação 5.000000) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | Planejado |
| CT-FUNC-003 | Emissão de invoice PDF e download (REQ-04) | REQ-04 | US-004 | REQ-04::UAT-04::product::invoice-pdf | Planejado |
| CT-FUNC-004 | Erro de cotação indisponível exibido na UI (503) | REQ-01 | US-001 | REQ-01::UAT-01::product::sim-realtime | Planejado |
| CT-FUNC-005 | Interface responsiva nos navegadores alvo | REQ-06 | US-005 | REQ-06::UAT-05::product::ui-browsers | Planejado |

## 4. Rastreabilidade caso ↔ teste automatizado

Todo caso acima tem implementação correspondente:

- Casos CT-UN-* → `tests/unit/test_*.py` (ex: CT-UN-004 → `tests/unit/test_rate_service.py::test_falls_back_from_frankfurter_to_ptax_req01`).
- Casos CT-INT-* → `tests/integration/test_*.py` (ex: CT-INT-003 → `tests/integration/test_api_contract.py::test_simulate_spec_section2_example_gives_exact_strings_req02`; CT-INT-012 → `tests/integration/test_invoice.py::test_invoice_pdf_has_attachment_and_no_store_headers_req04`).
- Casos CT-FUNC-* → `tests/e2e_playwright/tests/test_*.py` (Screenplay Pattern).

## 5. Status agregado (baseline UAT rodada 001, 13/11/2026)

| Camada | Casos planejados | Executados | PASS | FAIL | Skip | Taxa |
|---|---|---|---|---|---|---|
| Unidade + Integração (pytest) | ~1400 | 1392 | 1392 | 0 | 13 | 100% executados |
| Funcional (Playwright) | 5 | 0 | 0 | 0 | 5 | 0% (nova camada) |
| UAT produto + camada | 14 | 14 | 14 | 0 | 0 | 100% |

**Nota:** os 13 testes pulados (skip) são o PDF real sem WeasyPrint nativo (ambientes locais sem Pango); no CI com Pango executam de verdade. A regra CI proíbe testes pulados no gate `test-suite` — incidente INC-004 registrado no board de resultados.
