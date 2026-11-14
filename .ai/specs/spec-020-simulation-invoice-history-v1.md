---
id: ai-specs-spec-020-simulation-invoice-history-v1
title: 'SPEC spec-020 — simulation-invoice-history-v1 — Simulações salvas, histórico e ciclo de vida das invoices'
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-006-simulation-invoice-history.md
- docs/especificacoes/spec-prop-021-simulation-invoice-history.md
- docs/decisoes/ccb-003-multiusuario-lgpd.md (CR-008 liberado)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04, P-14, P-15)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.md (dependência)
- .ai/specs/spec-017-identity-access-session-v1.md (dependência)
- .ai/specs/spec-018-provider-profile-bank-account-v1.md (dependência)
- .ai/specs/spec-019-client-directory-v1.md (dependência)
- .ai/specs/spec-004-backend-mvp-v1.md (contrato invoice, recálculo)
- .ai/specs/spec-007-invoice-data-model-v1.md (modelo canônico)
- .ai/specs/spec-023-ui-spec-v1.md (telas histórico, rascunho/finalizada, clone)
last-revised: '2026-11-14'
lgpd-class: sensível
tags:
- specs
- docs
- simulacao
- historico
- invoice
- lifecycle
spec-id: spec-020
specname: simulation-invoice-history-v1
version: 1.0.0
status: ratificado
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: docs/change-requests/cr-006-simulation-invoice-history.md (CR-006, SPEC-020)
task: "TA-0068 | sender: agent-nexus-prime-ultimate"
kill_switch: inherited
lgpd-class: sensível
trace:
  - docs/change-requests/cr-006-simulation-invoice-history.md
  - docs/especificacoes/spec-prop-021-simulation-invoice-history.md
  - docs/decisoes/ccb-003-multiusuario-lgpd.md
  - constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04, P-14, P-15)
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.md
  - .ai/specs/spec-017-identity-access-session-v1.md
  - .ai/specs/spec-018-provider-profile-bank-account-v1.md
  - .ai/specs/spec-019-client-directory-v1.md
  - .ai/specs/spec-004-backend-mvp-v1.md
  - .ai/specs/spec-007-invoice-data-model-v1.md
  - .ai/specs/spec-023-ui-spec-v1.md
---

# SPEC spec-020 — simulation-invoice-history-v1 — Simulações salvas, histórico e ciclo de vida das invoices

**Status:** **RATIFICADA** — Liberada após CCB-003 (CR-008 resolvido). Implementa CR-006. Dependências: SPEC-017, 018, 019, 022. Ratificação US-016/US-017 (CCB-003).

---

## 1. Contexto e Origem

Emitida por TA-0068 / CR-006 (agent-nexus-prime-ultimate → agent-sdd-specialist, action: spec, 2026-11-14) para implementar: simulações salvas (opt-in), histórico unificado, ciclo de vida da invoice (rascunho/finalizada), clonagem, numeração sem PostgreSQL Sequence. Condicionada à SPEC-017/018/019/022. US-016/US-017 ratificadas no CCB-003.

---

## 2. Modelo de Dados

### 2.1 Tabela `simulations` (Nova)

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|-----------|
| `id` | UUID | PK | Identificador único |
| `owner_user_id` | UUID | FK → `users.id`, ON DELETE CASCADE | Proprietário |
| `currency` | CHAR(3) | NOT NULL, CHECK IN (`USD`, `EUR`) | Moeda |
| `regime` | VARCHAR | NOT NULL, CHECK IN (`hourly`,`daily`,`weekly`,`monthly`,`fixed`) | Regime |
| `amount` | NUMERIC(18,2) | NOT NULL, CHECK `> 0` | Valor por unidade |
| `quantity` | NUMERIC(12,2) | NULLABLE, CHECK `> 0` (se regime ≠ fixed) | Quantidade |
| `spread_pct` | NUMERIC(6,4) | NOT NULL, CHECK `0-100` | Spread % |
| `iof_pct` | NUMERIC(6,4) | NOT NULL, CHECK `0-100` | IOF % |
| `gross_foreign` | NUMERIC(18,2) | NOT NULL | Bruto moeda estrangeira |
| `gross_brl` | NUMERIC(18,2) | NOT NULL | Bruto BRL |
| `spread_brl` | NUMERIC(18,2) | NOT NULL | Spread BRL |
| `iof_brl` | NUMERIC(18,2) | NOT NULL | IOF BRL |
| `net_brl` | NUMERIC(18,2) | NOT NULL | Líquido BRL |
| `effective_rate` | NUMERIC(18,6) | NOT NULL | Câmbio efetivo |
| `rate` | NUMERIC(18,6) | NOT NULL | Cotação usada |
| `rate_source` | VARCHAR | NOT NULL, CHECK IN (`frankfurter`, `ptax`) | Fonte |
| `quoted_at` | TIMESTAMPTZ | NOT NULL | Timestamp cotação |
| `bulletin` | VARCHAR(40) | NULLABLE | Boletim PTAX |
| `stale` | BOOLEAN | NOT NULL | Flag cotação velha |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Criação |

**Regras:**
- `owner_user_id` obrigatório; FK `ON DELETE CASCADE`.
- Snapshot tipado: entrada + resultado + cotação — **não recalcula** ao listar histórico.
- Opt-in explícito: usuário clica "Salvar simulação" após cálculo.

### 2.2 Emenda `invoices` (SPEC-007)

| Campo | Tipo | Constraint | Descrição |
|-------|------|------------|-----------|
| `owner_user_id` | UUID | FK → `users.id`, ON DELETE RESTRICT, NOT NULL | Proprietário |
| `client_id` | UUID | FK → `clients.id`, ON DELETE RESTRICT, NULLABLE | Cliente (se cadastrado) |
| `simulation_id` | UUID | FK → `simulations.id`, ON DELETE RESTRICT, NULLABLE | Simulação salva (se opt-in) |
| `status` | VARCHAR | NOT NULL, DEFAULT `draft`, CHECK IN (`draft`, `finalized`) | Estado |
| `locale` | VARCHAR | NOT NULL, CHECK IN (`pt-BR`, `en`) | Idioma da invoice |
| `client_country_code` | CHAR(2) | NOT NULL | ISO 3166-1 do cliente |
| `finalized_at` | TIMESTAMPTZ | NULLABLE, NOT NULL WHEN `status=finalized` | Finalização |
| `supersedes_invoice_id` | UUID | FK → `invoices.id`, ON DELETE SET NULL, NULLABLE | Invoice original (clone) |

**Constraints adicionais:**
- `CHECK (status = 'finalized' AND finalized_at IS NOT NULL) OR (status = 'draft' AND finalized_at IS NULL)`
- `FK owner_user_id ON DELETE RESTRICT` (não cascade — invoices anonimizadas, não removidas)
- `FK client_id/simulation_id ON DELETE RESTRICT` (preservam integridade referencial)
- `FK supersedes_invoice_id ON DELETE SET NULL` (auto-referência)

---

## 3. Regras de Negócio

### 3.1 Simulação Salva (Opt-in)

- **Gatilho:** Usuário clica "Salvar simulação" **após** cálculo (botão dedicado, não automático).
- **Persiste:** Entrada validada + resultado recalculado + cotação snapshot (rate, source, quoted_at, bulletin, stale).
- **Não recalcula** ao listar histórico — mostra valores da época.
- **Listagem:** `GET /simulations?page=1&size=20` ordenado por `created_at DESC`.
- **Acesso:** Apenas próprias simulações (`owner_user_id` da sessão).

### 3.2 Ciclo de Vida da Invoice (US-016/US-017 Ratificados)

| Estado | Descrição | Permissões |
|--------|-----------|------------|
| `draft` | Rascunho editável | CREATE, READ, UPDATE, DELETE (próprio) |
| `finalized` | Finalizada imutável | READ only (próprio); CLONE (US-017) |

**Transição `draft → finalized`:**
1. Validação: invoice completa (partes, simulação, número, data, descrição).
2. **Transação atômica:**
   - Copia snapshots: prestadora (SPEC-018), banco (SPEC-018), cliente (SPEC-019), simulação/cotação, valores, `locale` (SPEC-021), `client_country_code`.
   - `status = 'finalized'`, `finalized_at = now()`.
   - `locale` derivado automaticamente: `client_country_code = 'BR' → 'pt-BR'`, senão `'en'`.
3. **Imutabilidade:** `finalized` → READ only; qualquer UPDATE/DELETE → 403 Forbidden.

### 3.3 Clonagem (US-017)

- **Pré-requisito:** Invoice `finalized`.
- **Ação:** `POST /invoices/{id}/clone` → cria novo `draft`:
  - Copia todos os campos do `draft` original.
  - Novo `invoice_number` (gerado: solução sem Sequence, ver §3.4).
  - `issue_date = today()`.
  - `status = 'draft'`, `finalized_at = NULL`.
  - `supersedes_invoice_id = id_original`.
  - Novo `id` UUID.
- **Acesso:** Apenas próprio usuário (`owner_user_id`).

### 3.4 Numeração de Invoice (Sem Sequence — C-04, GAP-06)

- **Formato:** `INV-{YYYY}{MM}-{SEQ:04d}` (ex.: `INV-202611-0001`).
- **Geração:** `SEQ` = `COUNT(*) + 1` onde `invoice_number LIKE 'INV-{YYYY}{MM}%'` e `owner_user_id = current_user`.
- **Concorrência:** `SELECT ... FOR UPDATE` na tabela `invoices` filtrando por prefixo do mês/ano + usuário.
- **Unicidade:** Garantida por `UNIQUE (owner_user_id, invoice_number)` + transação `FOR UPDATE`.

### 3.5 Histórico Unificado

- **Endpoint:** `GET /history?type=simulation|invoice|all&status=draft|finalized|all&from=...&to=...&page=1&size=20`
- **Resultado:** Lista combinada paginada (simulações salvas + invoices) ordenada por data decrescente.
- **Filtros:** `type`, `status`, período (`from`/`to`), `client_id` (para invoices).
- **Acesso:** Apenas próprios recursos (`owner_user_id` da sessão).

---

## 4. Contrato HTTP

### 4.1 Simulações

| Verbo | Rota | Entrada | Saída | Erros |
|-------|------|---------|-------|-------|
| POST | `/simulations/save` | `SimulationSaveRequest` | 201 `Simulation` | 400, 401, 422 |
| GET | `/simulations` | `?page=1&size=20` | 200 `Paginated[Simulation]` | 401 |
| DELETE | `/simulations/{id}` | — | 204 | 401, 404 |

### 4.2 Invoices (Estende `/v1/invoice`)

| Verbo | Rota | Entrada | Saída | Erros |
|-------|------|---------|-------|-------|
| POST | `/v1/invoice` | `InvoiceRequest` + `save_draft: true` | 201 `InvoiceDraft` | 400, 401, 422 |
| POST | `/v1/invoice` | `InvoiceRequest` + `finalize: true` | 200 `application/pdf` | 400, 401, 422, 503 |
| GET | `/invoices` | `?status=draft|finalized|all&page=1&size=20` | 200 `Paginated[Invoice]` | 401 |
| GET | `/invoices/{id}` | — | 200 `InvoiceDetail` | 401, 404 |
| POST | `/invoices/{id}/finalize` | — | 200 `application/pdf` | 400, 401, 404, 409, 503 |
| POST | `/invoices/{id}/clone` | — | 201 `InvoiceDraft` | 401, 404, 409 |
| DELETE | `/invoices/{id}` | — | 204 | 401, 404, 409 |

**Schemas (Pydantic `extra="forbid"`):**
- `SimulationSaveRequest`: `simulation` (SimulationRequest), `result` (SimulationResponse), `quote` (RateQuote)
- `InvoiceDraft`: `id`, `status='draft'`, campos de invoice (sem PDF)
- `InvoiceDetail`: `InvoiceDraft` + `pdf_url?` (se finalized) + snapshots

---

## 5. Segurança — Controles Obrigatórios

| Controle | Implementação |
|----------|---------------|
| **RLS** | `CREATE POLICY` em `simulations`, `invoices` (`owner_user_id = current_user_id()`) |
| **Autorização** | Middleware `owner_user_id` da sessão; nunca do request |
| **Imutabilidade** | `finalized` → UPDATE/DELETE → 403; middleware valida `status` |
| **Numeração** | Transação `SELECT ... FOR UPDATE` por prefixo mensal + usuário |
| **Snapshots** | Transação atômica copia prestadora, banco, cliente, simulação, valores, locale |
| **Logs** | Zero PII/valores em logs; `account_lifecycle_events` para finalização/clone |

---

## 6. Critérios de Aceite e Testes

| ID | Critério | Método |
|----|----------|--------|
| AC-01 | Simulação opt-in: botão "Salvar" persiste snapshot; listagem mostra valores da época | Teste integração |
| AC-02 | Invoice draft: CRUD completo; finalize transação atômica copia snapshots + status + finalized_at | Teste integração (transação) |
| AC-03 | Invoice finalized: imutável (403 em UPDATE/DELETE); apenas READ | Teste integração |
| AC-04 | Clone: finalized → novo draft com novo número, `supersedes_invoice_id`, data hoje | Teste integração |
| AC-04 | Numeração: `INV-YYYYMM-SEQ`; concorrência `FOR UPDATE`; unicidade por owner+mês | Teste concorrência (carga) |
| AC-05 | Histórico unificado: paginado, filtrável por tipo/status/período/cliente | Teste integração |
| AC-06 | RLS: usuário A não acessa simulações/invoices de usuário B | Teste integração (multi-user) |
| AC-07 | Imutabilidade: finalized + UPDATE → 403; clone cria novo draft | Teste integração |
| AC-08 | Snapshots: prestadora, banco, cliente, simulação, valores, locale copiados na finalização | Teste integração (transação) |
| AC-09 | Logs zero PII/valores | Teste automatizado (grep) |

---

## 7. Rastreabilidade

| Fonte | Seção |
|-------|-------|
| CR-006 (issue #39) | Todas |
| CR-008 / SPEC-022 | LGPD, lifecycle, anonimização, RLS |
| CR-003/004/005 / SPEC-017/018/019 | Identidade, prestadora, clientes, RLS |
| CCB-003 | CR6-D01..D04, US-016/017 ratificadas, CR8-D01..D06 |
| Constitution | P-02, P-03, P-04, P-14, P-15 |
| SPEC-022 | Lifecycle, anonimização, RLS |
| SPEC-017/018/019 | Identidade, prestadora, clientes |
| SPEC-004/007 | Contrato invoice, modelo canônico |
| SPEC-023 | Telas histórico, rascunho/finalizada, clone |

---

## 8. Fora de Escopo (YAGNI)

- Versionamento de rascunho (histórico de edições).
- Workflow de aprovação de invoice.
- Envio automático de invoice por email.
- Integração com contabilidade/ERP.
- Dashboard analítico de simulações/invoices.

---

## CHANGELOG

- 1.0.0 — 2026-11-14: SPEC-020 ratificada (CCB-003); implementa CR-006; tabela `simulations` opt-in, emenda `invoices` com status/locale/snapshots/clone, numeração sem Sequence, histórico unificado. US-016/017 ratificadas. Dependências SPEC-017/018/019/022.