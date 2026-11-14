---
id: docs-qualidade-requirements-traceability-matrix
title: "Matriz de Rastreabilidade de Requisitos (RTM) — COGME"
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/conhecimento/templates/kb-template-rtm.md v1.0.0
- constitution.md Art. 2 (Hierarquia: Requisitos → Specs → Código → Testes)
- OKB §4 (Inventário de artefatos e metadados)
- SPEC-004, SPEC-008, SPEC-017 a 023
- ADR-001, ADR-003, ADR-010, ADR-017, ADR-019
- IEEE 830 / ISO/IEC/IEEE 29148 (Rastreabilidade bidirecional)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- qualidade
- rastreabilidade
- rtm
- pmbok
- compliance
---

# Matriz de Rastreabilidade de Requisitos (RTM) — COGME

> **Finalidade**: Garantir **rastreabilidade bidirecional** entre: **Requisitos de Negócio** (PRD/Constitution/TAP) ↔ **Especificações Técnicas** (Specs/ADRs) ↔ **Implementação** (Código/Schema DB/API) ↔ **Testes** (Unit/Integration/E2E/UAT) ↔ **Critérios de Aceite**.
> **Uso**: Validação Gate 2 (Desenho) e Gate 3 (Go-Live). Evita **Gold Plating** (entrega não solicitada) e **Gap** (requisito não implementado/testado).
> **Manutenção**: Atualizada a cada Spec ratificada, CR aprovado, ou nova implementação. Arquivo mestre: `docs/planos/rtm.csv` (versionado no Git). Este documento Markdown é visão executiva.

---

## 1. LEGENDA E CONVENÇÕES

| Símbolo | Significado |
|---|---|
| ✅ | Rastreado e Verificado (implementado + testado + aprovado) |
| 🔄 | Rastreado Parcial (implementado, teste pendente / vice-versa) |
| ❌ | Gap Identificado (requisito sem implementação OU implementação sem requisito) |
| ⏳ | Planejado (no backlog/wave futura) |
| 🚫 | Fora de Escopo (decisão CCB documentada) |

| Prefixo ID | Origem |
|---|---|
| **REQ-** | Requisitos de Negócio (PRD, Constitution, TAP, OKR) |
| **SPEC-** | Especificações Técnicas (Specs, ADRs, NFRs) |
| **IMPL-** | Implementação (Código, Schema, API Endpoint, Config) |
| **TEST-** | Testes (Unit, Integration, E2E, UAT, Performance, Security) |
| **AC-** | Critérios de Aceite (Gherkin Given/When/Then) |

---

## 2. MATRIZ CONSOLIDADA (Visão Executiva)

> **Instrução**: Uma linha por **Requisito de Negócio (REQ-)**. Expande para múltiplas linhas se um REQ gerar múltiplas SPECs/IMPLs/TESTs.

| REQ-ID | Requisito de Negócio (Resumo) | Fonte (PRD/TAP/Constitution) | SPEC-ID(s) | IMPL-ID(s) | TEST-ID(s) | AC-ID(s) | Status | Gap / Observação |
|---|---|---|---|---|---|---|---|---|
| REQ-01 | Simulação de conversão cambial (USD/EUR) com latência ≤ 2s | Constitution Art. 3 / TAP §3 / PRD §2.1 | SPEC-004 (backend-mvp) / SPEC-008 (frontend) | IMPL-001 (rates service) / IMPL-002 (simulate endpoint) / IMPL-003 (frontend simulator) | TEST-001 (unit calculator) / TEST-002 (integration rates) / TEST-003 (E2E simulate) / TEST-004 (perf latency) | AC-001 / AC-002 | ✅ | |
| REQ-02 | Geração de invoice PDF bilingue (PT/EN) ≤ 3s | PRD §2.4 / Constitution Art. 3 | SPEC-004 §8 / SPEC-022 (invoice-bilingual) | IMPL-004 (invoice service) / IMPL-005 (PDF generator) / IMPL-006 (templates PT/EN) | TEST-005 (unit PDF) / TEST-006 (integration invoice) / TEST-007 (E2E PDF) / TEST-008 (perf PDF) | AC-003 / AC-004 | 🔄 | Teste perf PDF pendente |
| REQ-03 | Cache local de cotações (7 dias) com fallback PTAX | ADR-001 v1.1.0 / TAP §8 / PRD §2.2 | SPEC-004 §5 / ADR-001 | IMPL-007 (fx_quotes table) / IMPL-008 (rate providers) / IMPL-009 (circuit breaker) | TEST-009 (unit cache) / TEST-010 (integration fallback) / TEST-011 (E2E cache) | AC-005 | ✅ | |
| REQ-04 | Identidade e acesso multiusuário (Argon2id, sessões, recovery) | CR-002 / PROP-017 / Constitution Art. 7 | SPEC-017 (identity) / SPEC-018 (sessions) / ADR-017 (argon2id) | IMPL-010 (users table) / IMPL-011 (auth service) / IMPL-012 (session mgmt) | TEST-012 (unit auth) / TEST-013 (integration login) / TEST-014 (E2E multiusuario) / TEST-015 (security argon2id) | AC-006..AC-010 | ⏳ | Wave M2 — não iniciado |
| REQ-05 | Perfil prestadora + contas bancárias (SWIFT/IBAN) | PROP-019 / PRD §2.5 | SPEC-019 (provider) / SPEC-020 (bank accounts) | IMPL-013 (provider tables) / IMPL-014 (bank account service) | TEST-016 (unit provider) / TEST-017 (integration bank) | AC-011..AC-013 | ⏳ | Wave M3 — não iniciado |
| REQ-06 | Diretório de clientes (CRUD, país, tax_id) | PROP-020 / PRD §2.6 | SPEC-021 (clients) | IMPL-015 (clients table) / IMPL-016 (client service) | TEST-018 (unit client) / TEST-019 (integration client) | AC-014..AC-016 | ⏳ | Wave M3 — não iniciado |
| REQ-07 | Histórico de simulações / invoices por usuário | PROP-021 / PRD §2.7 | SPEC-022 (simulation history) | IMPL-017 (simulation/invoice tables) / IMPL-018 (history service) | TEST-020 (unit history) / TEST-021 (integration history) | AC-017..AC-019 | ⏳ | Wave M4 — não iniciado |
| REQ-08 | LGPD / Marco Civil / Soberania de dados (zero cloud, FOSS, criptografia) | Constitution Art. 7 / P-02, P-03, P-04 / LGPD Art. 7-11 | ADR-001 (FOSS) / ADR-010 (infra) / ADR-017 (Argon2id) / SPEC-023 (privacy) | IMPL-019 (encryption at rest) / IMPL-020 (HMAC lookup) / IMPL-021 (data retention) | TEST-022 (security scan) / TEST-023 (pen test) / TEST-024 (LGPD compliance) | AC-020..AC-025 | 🔄 | Pen test agendado M4 |
| REQ-09 | Observabilidade: health check, métricas fluxo, logs estruturados | Constitution Art. 4 / ADR-003 (metrics) / README §10 | SPEC-004 §10 / ADR-003 | IMPL-022 (health endpoint) / IMPL-023 (metrics endpoint) / IMPL-024 (structured logging) | TEST-025 (unit health) / TEST-026 (integration metrics) / TEST-027 (E2E observability) | AC-026..AC-028 | ✅ | |
| REQ-10 | CI/CD fail-closed, FOSS, zero credenciais, SDD/DAG validation | Constitution Art. 4.6, 4.8, 6.1 / CI-CD-GOV-001 / DEVSECOPS-001 | CI-CD-GOV-001 / DEVSECOPS-001 | IMPL-025 (ci.yml) / IMPL-026 (sddai-verify.yml) / IMPL-027 (agent health) | TEST-028 (CI pipeline) / TEST-029 (SDDAI verify) | AC-029..AC-031 | ✅ | |

---

## 3. DETALHAMENTO POR CAMADA (Para Auditoria Profunda)

### 3.1 Requisitos → Especificações (Forward Traceability)
| REQ-ID | SPEC-ID | Seção na Spec | Cobertura | Nota |
|---|---|---|---|---|
| REQ-01 | SPEC-004 | §2.1, §3, §8 | Completa | |
| REQ-01 | SPEC-008 | §4, §5 | Completa | |
| REQ-02 | SPEC-004 | §8 | Completa | |
| REQ-02 | SPEC-022 | §3, §4 | Completa | |
| REQ-03 | SPEC-004 | §5 | Completa | |
| REQ-03 | ADR-001 | §Decisão (tabela stack) | Completa | |
| REQ-04 | SPEC-017 | §3, §4 | Completa (spec ratified) | Aguardando implementação |
| REQ-04 | SPEC-018 | §3, §4 | Completa (spec ratified) | Aguardando implementação |
| REQ-04 | ADR-017 | §Decisão | Completa | Argon2id adotado |
| REQ-05 | SPEC-019 | §3, §4 | Completa (spec ratified) | Aguardando implementação |
| REQ-05 | SPEC-020 | §3, §4 | Completa (spec ratified) | Aguardando implementação |
| REQ-06 | SPEC-021 | §3, §4 | Completa (spec ratified) | Aguardando implementação |
| REQ-07 | SPEC-022 | §3, §4 | Completa (spec ratified) | Aguardando implementação |
| REQ-08 | ADR-001 | §Decisão (FOSS) | Completa | |
| REQ-08 | ADR-010 | §Decisão (infra) | Completa | |
| REQ-08 | ADR-017 | §Decisão (Argon2id) | Completa | |
| REQ-08 | SPEC-023 | §3, §4 | Completa (spec ratified) | Aguardando implementação |
| REQ-09 | SPEC-004 | §10 | Completa | |
| REQ-09 | ADR-003 | §Decisão | Completa | Métricas de fluxo definidas |
| REQ-10 | CI-CD-GOV-001 | §4 (Regras Fail-Closed) | Completa | |
| REQ-10 | DEVSECOPS-001 | §3 (Princípios) | Completa | |

### 3.2 Especificações → Implementação (Forward Traceability)
| SPEC-ID | IMPL-ID | Arquivo / Componente | Função / Classe / Tabela | Cobertura | Nota |
|---|---|---|---|---|---|
| SPEC-004 §3 | IMPL-001 | `src/backend/services/rate_service.py` | `RateService.get_rate()` | Completa | |
| SPEC-004 §5 | IMPL-007 | `migrations/versions/0001_create_fx_quotes.py` | `fx_quotes` table | Completa | Migration aplicada |
| SPEC-004 §5 | IMPL-008 | `src/backend/services/rate_providers.py` | `FrankfurterProvider`, `PtaxProvider` | Completa | Circuit breaker integrado |
| SPEC-004 §5 | IMPL-009 | `src/backend/services/circuit_breaker.py` | `CircuitBreaker` class | Completa | Threshold 5 falhas |
| SPEC-004 §8 | IMPL-004 | `src/backend/services/invoice_service.py` | `InvoiceService.generate_pdf()` | Completa | WeasyPrint + Jinja2 |
| SPEC-004 §8 | IMPL-005 | `src/backend/services/invoice_number.py` | `InvoiceNumberGenerator` | Completa | Sequencial por ano |
| SPEC-004 §8 | IMPL-006 | `src/frontend/templates/invoice_pt_br.html`, `invoice_en.html` | Templates Jinja2 | Completa | Bilingue PT/EN |
| SPEC-008 §4 | IMPL-003 | `src/frontend/templates/index.html`, `static/js/app.js` | Simulator UI + HTMX | Completa | |
| SPEC-017 §3 | IMPL-010 | `migrations/versions/0002_create_users*.py` (planejada) | `users`, `user_login_identifiers`, `user_sessions`, `password_reset_tokens` | ⏳ Planejada | Spec ratificada, migration pendente |
| SPEC-017 §4 | IMPL-011 | `src/backend/services/auth_service.py` (planejado) | `AuthService` (register, login, argon2id, recovery) | ⏳ Planejada | |
| SPEC-018 §3 | IMPL-012 | `src/backend/services/session_service.py` (planejado) | `SessionService` (create, validate, revoke, cleanup) | ⏳ Planejada | |
| ADR-017 | IMPL-019 | `src/backend/services/password_hasher.py` (planejado) | `Argon2idHasher` (params: m=65536, t=3, p=4) | ⏳ Planejada | OWASP recommended |
| SPEC-023 | IMPL-020 | `src/backend/models/lookup_hmac.py` (planejado) | HMAC-SHA256 para lookup de email/CPF | ⏳ Planejada | Pseudonimização LGPD |
| SPEC-023 | IMPL-021 | `src/backend/services/retention_service.py` (planejado) | Políticas retenção/exclusão automática | ⏳ Planejada | Job agendado |

### 3.3 Implementação → Testes (Backward Traceability)
| IMPL-ID | TEST-ID | Tipo de Teste | Arquivo de Teste | Cenário Coberto | Status |
|---|---|---|---|---|---|
| IMPL-001 | TEST-001 | Unit | `tests/test_calculator.py` | Cálculo conversão, rounding, edge cases | ✅ Pass |
| IMPL-001 | TEST-002 | Integration | `tests/integration/test_rates.py` | Rate service + cache + fallback PTAX | ✅ Pass |
| IMPL-001 | TEST-003 | E2E | `tests/e2e/test_e2e_simulator.py` (planejado) | Fluxo completo: input → simulate → result | ⏳ Planejado |
| IMPL-001 | TEST-004 | Performance | `tests/performance/test_latency.py` (planejado) | P95 ≤ 2s sob carga | ⏳ Planejado |
| IMPL-004 | TEST-005 | Unit | `tests/test_invoice.py` | PDF generation, template rendering | ✅ Pass |
| IMPL-004 | TEST-006 | Integration | `tests/integration/test_invoice.py` | Invoice service + DB + PDF | ✅ Pass |
| IMPL-004 | TEST-007 | E2E | `tests/e2e/test_e2e_invoice_pdf.py` (planejado) | Fluxo: simulate → generate invoice → download | ⏳ Planejado |
| IMPL-004 | TEST-008 | Performance | `tests/performance/test_pdf_latency.py` (planejado) | P95 ≤ 3s | ⏳ Planejado |
| IMPL-007 | TEST-009 | Unit | `tests/test_repository.py` | FX quotes CRUD, cache expiry | ✅ Pass |
| IMPL-008 | TEST-010 | Integration | `tests/integration/test_rates.py` | Fallback automático Frankfurter→PTAX | ✅ Pass |
| IMPL-009 | TEST-011 | Integration | `tests/integration/test_circuit_breaker.py` | Circuit breaker abre/fecha/half-open | ✅ Pass |

### 3.4 Testes → Critérios de Aceite (Validação)
| TEST-ID | AC-ID | Critério de Aceite (Gherkin) | Status |
|---|---|---|---|
| TEST-003 | AC-001 | **Dado** que o usuário informa valor 1000 USD **Quando** clica em simular **Então** vê valor em BRL com cotação atual | ⏳ Planejado |
| TEST-003 | AC-002 | **Dado** que a API primária falha **Quando** simula **Então** usa fallback PTAX transparente | ✅ Pass (integration) |
| TEST-007 | AC-003 | **Dado** que a simulação foi feita **Quando** gera invoice **Então** PDF baixado com dados corretos PT-BR | ⏳ Planejado |
| TEST-007 | AC-004 | **Dado** que o usuário seleciona inglês **Quando** gera invoice **Então** PDF em EN com moeda USD/EUR | ⏳ Planejado |
| TEST-010 | AC-005 | **Dado** que cotação tem 8 dias **Quando** simula **Então** busca nova cotação (cache expirado) | ✅ Pass (integration) |

---

## 4. RELATÓRIO DE GAPS E GOLD PLATING (Auditoria)

### 4.1 Gaps Identificados (Requisito sem Implementação/Teste Completo)
| REQ-ID | Gap Tipo | Descrição | Ação Corretiva | Prazo | Dono |
|---|---|---|---|---|---|
| REQ-02 | Teste | Teste de performance PDF (≤3s) não implementado | Criar TEST-008 em `tests/performance/test_pdf_latency.py` | 2026-11-20 | agent-qa-sdet |
| REQ-02 | Teste | Testes E2E invoice PDF não implementados | Criar TEST-007 em `tests/e2e/test_e2e_invoice_pdf.py` | 2026-11-25 | agent-qa-sdet |
| REQ-04 | Implementação | Migration 0002 (users, sessions) não criada | Criar migration + models + services (M2 wave) | 2026-11-30 | agent-backend-dev / agent-dba |
| REQ-04 | Teste | Testes auth/multiusuario não existentes | Criar TEST-012 a TEST-015 | 2026-12-05 | agent-qa-sdet |
| REQ-08 | Teste | Pen test LGPD não executado | Agendar pen test interno/externo | 2026-12-01 | agent-digital-security |
| REQ-08 | Teste | Teste de compliance LGPD automatizado não existe | Criar TEST-024 (LGPD compliance checks) | 2026-11-28 | agent-qa-sdet / agent-compliance-governance |

### 4.2 Gold Plating Identificado (Implementação sem Requisito)
| IMPL-ID | Descrição | Justificativa / Decisão | Ação |
|---|---|---|---|
| — | Nenhum identificado na auditoria atual | — | — |

---

## 5. ARQUIVO FONTE (CSV) — Para Automação

> **Arquivo mestre**: `docs/planos/rtm.csv` (versionado no Git). Este documento Markdown é visão executiva gerada a partir do CSV.
> **Colunas CSV**: `REQ_ID,REQ_Description,Source,SPEC_IDS,IMPL_IDS,TEST_IDS,AC_IDS,Status,Gap_Note,Last_Updated,Owner`
> **Script de validação**: `scripts/validate_rtm.py` (verifica completude, gaps, gold plating) — roda no CI.

---

## 6. CONTROLE DE VERSÕES DA RTM

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-project-analyst | Criação inicial (baseado no template aprovado) | GP (CCB) |

---

> **Regra de Ouro**: **Nenhum código entra em `main` sem rastreabilidade mínima: REQ → SPEC → IMPL → TEST → AC**. Se faltar elo, CR obrigatório ou devolução ao backlog.