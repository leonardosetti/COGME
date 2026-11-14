---
id: ai-specs-spec-019-client-directory-v1
title: 'SPEC spec-019 — client-directory-v1 — Carteira de clientes e estado ativo/inativo'
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-005-client-directory.md
- docs/especificacoes/spec-prop-020-client-directory.md
- docs/decisoes/ccb-003-multiusuario-lgpd.md (CR-008 liberado)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04, P-14, P-15)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.md (dependência)
- .ai/specs/spec-017-identity-access-session-v1.md (dependência: identidade, RLS)
- .ai/specs/spec-007-invoice-data-model-v1.md (snapshot invoice)
- .ai/specs/spec-023-ui-spec-v1.md (telas carteira, autocomplete)
last-revised: '2026-11-14'
lgpd-class: sensível
tags:
- specs
- docs
- cliente
- carteira
- lgpd
spec-id: spec-019
specname: client-directory-v1
version: 1.0.0
status: ratificado
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: docs/change-requests/cr-005-client-directory.md (CR-005, SPEC-019)
task: "TA-0067 | sender: agent-nexus-prime-ultimate"
kill_switch: inherited
lgpd-class: sensível
trace:
  - docs/change-requests/cr-005-client-directory.md
  - docs/especificacoes/spec-prop-020-client-directory.md
  - docs/decisoes/ccb-003-multiusuario-lgpd.md
  - constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04, P-14, P-15)
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.md
  - .ai/specs/spec-017-identity-access-session-v1.md
  - .ai/specs/spec-007-invoice-data-model-v1.md
  - .ai/specs/spec-023-ui-spec-v1.md
---

# SPEC spec-019 — client-directory-v1 — Carteira de clientes e estado ativo/inativo

**Status:** **RATIFICADA** — Liberada após CCB-003 (CR-008 resolvido). Implementa CR-005. Dependências: SPEC-017 (identidade/RLS), SPEC-022 (lifecycle/LGPD).

---

## 1. Contexto e Origem

Emitida por TA-0067 / CR-005 (agent-nexus-prime-ultimate → agent-sdd-specialist, action: spec, 2026-11-14) para implementar a carteira de clientes: cadastro opcional, estado ativo/inativo, cliente fictício (dummy) sem persistência, snapshot na invoice finalizada. Base legal LGPD Art. 7º V (execução de contrato) para dados de terceiros. Condicionada à SPEC-017 (identidade/RLS) e SPEC-022 (lifecycle/LGPD).

---

## 2. Modelo de Dados

### 2.1 Tabela `clients`

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|-----------|
| `id` | UUID | PK | Identificador único |
| `owner_user_id` | UUID | FK → `users.id`, ON DELETE CASCADE | Proprietário |
| `name` | VARCHAR(120) | NOT NULL | Nome do cliente |
| `tax_id` | VARCHAR(40) | NULLABLE | CPF/CNPJ (apenas dígitos ou com máscara) |
| `address_line1` | VARCHAR(200) | NULLABLE | Logradouro + número |
| `address_line2` | VARCHAR(100) | NULLABLE | Complemento |
| `neighborhood` | VARCHAR(100) | NULLABLE | Bairro |
| `city` | VARCHAR(100) | NULLABLE | Cidade |
| `state` | CHAR(2) | NULLABLE | UF (código IBGE) |
| `postal_code` | CHAR(8) | NULLABLE | CEP apenas dígitos |
| `country_code` | CHAR(2) | NOT NULL, DEFAULT `BR` | ISO 3166-1 |
| `is_active` | BOOLEAN | NOT NULL, DEFAULT `true` | Estado ativo/inativo |
| `deactivated_at` | TIMESTAMPTZ | NULLABLE | Timestamp inativação |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Criação |
| `updated_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Atualização |

**Constraints:**
- `owner_user_id` obrigatório; FK `ON DELETE CASCADE`.
- Índice composto: `CREATE INDEX idx_clients_owner_active ON clients (owner_user_id, is_active)`.
- `country_code` ISO 3166-1 (padrão `BR`).
- `tax_id`: apenas dígitos (validação application-side para CPF/CNPJ).
- Cliente inativo (`is_active = false`) → `deactivated_at` preenchido; reativação permitida (limpa `deactivated_at`).

---

## 3. Regras de Negócio

### 3.1 Cadastro (Opcional)

- **Não obrigatório** para emitir invoice — cliente fictício permitido (ver §3.3).
- **Campos:** `name` (obrigatório), `tax_id`, endereço, `country_code` (padrão `BR`).
- **Validações:** `name` 1-120; `tax_id` dígitos (validação CPF/CNPJ se informado); `country_code` ISO 3166-1.
- **Estado inicial:** `is_active = true`, `deactivated_at = NULL`.

### 3.2 Estado Ativo/Inativo

- **Inativação manual:** Usuário marca cliente como inativo → `is_active = false`, `deactivated_at = now()`.
- **Reativação:** Usuário reativa → `is_active = true`, `deactivated_at = NULL`.
- **Efeito do inativo:**
  - ❌ Não aparece em autocomplete/sugestão no formulário de invoice.
  - ✅ Permanece consultável para histórico (listagem com filtro).
  - ✅ Snapshots em invoices finalizadas **não afetados** (imutáveis).

### 3.3 Cliente Fictício (Dummy)

- **Permitido** sem criar registro em `clients`.
- **Requisito:** `country_code` **obrigatório** no request de invoice (sem inferência silenciosa).
- **Uso:** Apenas para a invoice pontual; não persiste em `clients`.
- **Validação:** Request sem `client.country_code` → 400 `validation_error`.

### 3.4 Snapshot na Invoice Finalizada (SPEC-020)

- **Momento:** Transição `draft → finalized`.
- **Dados copiados (imutáveis):** `name`, `tax_id`, endereço completo, `country_code`.
- **Armazenamento:** Colunas `client_snapshot` em `invoices` (emenda SPEC-007).
- **Imutabilidade:** Alteração posterior do cadastro **não** afeta invoices finalizadas.

---

## 4. Contrato HTTP `/clients`

| Verbo | Rota | Entrada | Saída | Erros |
|-------|------|---------|-------|-------|
| GET | `/clients` | `?active=true&search=&page=1&size=20` | 200 `Paginated[Client]` | 401 |
| POST | `/clients` | `ClientCreate` | 201 `Client` | 400, 401, 409 |
| GET | `/clients/{id}` | — | 200 `Client` | 401, 404 |
| PUT | `/clients/{id}` | `ClientUpdate` | 200 `Client` | 400, 401, 404 |
| PATCH | `/clients/{id}/deactivate` | — | 200 `Client` | 401, 404 |
| PATCH | `/clients/{id}/reactivate` | — | 200 `Client` | 401, 404 |
| DELETE | `/clients/{id}` | — | 204 | 401, 404 |

**Query Parameters (Listagem):**
- `active`: `true` | `false` | omitido (todos)
- `search`: busca por `name` ou `tax_id` (ILIKE)
- `page`, `size`: paginação (padrão 20, máx 100)

**Schemas (Pydantic `extra="forbid"`):**
- `ClientCreate`: `name`, `tax_id?`, `address_line1?`, `address_line2?`, `neighborhood?`, `city?`, `state?`, `postal_code?`, `country_code?`
- `ClientUpdate`: campos opcionais de `Create` (exceto `owner_user_id`)
- `Client`: todos campos + `is_active`, `deactivated_at`, `created_at`, `updated_at`

---

## 5. Autocomplete no Formulário de Invoice (SPEC-023)

- **Fonte:** `GET /clients?active=true&search={termo}` (apenas ativos).
- **Exibição:** `name` + `tax_id` (mascarado) + `country_code`.
- **Seleção:** Preenche campos hidden `client_id` + `client_country_code` no request de invoice.
- **Cliente fictício:** Usuário não seleciona da lista; preenche campos manualmente + `country_code` obrigatório.

---

## 5. Segurança — Controles Obrigatórios

| Controle | Implementação |
|----------|---------------|
| **RLS** | `CREATE POLICY` em `clients` (`owner_user_id = current_user_id()`) |
| **Autorização** | Middleware `owner_user_id` da sessão; nunca do request |
| **LGPD Art. 7º V** | Base legal: execução de contrato (invoice) — usuário garante base contratual com cliente |
| **Logs** | Zero dados de clientes em logs; apenas metadata de acesso |
| **Autorização** | Middleware `owner_user_id` da sessão; nunca do request |

---

## 6. Critérios de Aceite e Testes

| ID | Critério | Método |
|----|----------|--------|
| AC-01 | Cadastro cliente: cria com `is_active=true`; valida country_code ISO 3166-1 | Teste integração |
| AC-02 | Inativação: `is_active=false`, `deactivated_at` preenchido; não aparece em autocomplete | Teste integração |
| AC-03 | Reativação: `is_active=true`, `deactivated_at=NULL`; volta ao autocomplete | Teste integração |
| AC-04 | Cliente fictício: request sem `client_id` mas com `country_code` → 200; sem país → 400 | Teste integração |
| AC-05 | Snapshot invoice: copia cliente na finalização; alteração posterior não afeta | Teste integração (transação) |
| AC-05 | RLS: usuário A não acessa clientes de usuário B | Teste integração (multi-user) |
| AC-06 | Autocomplete: apenas ativos; busca por name/tax_id; retorna id + country_code | Teste integração |
| AC-07 | LGPD: base legal Art. 7º V documentada; usuário garante contrato com cliente | Documentação + termo de uso |
| AC-08 | Logs zero dados de clientes | Teste automatizado (grep) |

---

## 7. Rastreabilidade

| Fonte | Seção |
|-------|-------|
| CR-005 (issue #38) | Todas |
| CR-008 / SPEC-022 | LGPD Art. 7º V, lifecycle, RLS |
| CR-003 / SPEC-017 | Identidade, RLS, autorização P-14 |
| CCB-003 | CR5-D01..D03, CR8-D02, CR8-D06 |
| Constitution | P-02, P-03, P-04, P-14, P-15 |
| SPEC-022 | LGPD executivo, lifecycle |
| SPEC-017 | Identidade, RLS, autorização P-14 |
| SPEC-007 | Modelo canônico invoice (snapshot) |
| SPEC-023 | Tela carteira, autocomplete invoice |

---

## 8. Fora de Escopo (YAGNI)

- Hierarquia de clientes (empresa/filial).
- Portal do cliente, notificações automáticas.
- Integração com CRM externo.
- Importação em lote (CSV/Excel).
- Auditoria de alterações (pode ser adicionada depois).

---

## CHANGELOG

- 1.0.0 — 2026-11-14: SPEC-019 ratificada (CCB-003); implementa CR-005; tabela `clients` com estado ativo/inativo, cliente fictício, snapshot invoice, autocomplete, LGPD Art. 7º V. Dependências SPEC-017, SPEC-022.