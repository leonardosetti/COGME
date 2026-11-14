---
id: ai-specs-spec-018-provider-profile-bank-account-v1
title: 'SPEC spec-018 — provider-profile-bank-account-v1 — Perfil da prestadora e contas bancárias de depósito'
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-004-provider-profile-bank.md
- docs/especificacoes/spec-prop-019-provider-profile-bank.md
- docs/decisoes/ccb-003-multiusuario-lgpd.md (CR-008 liberado)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04, P-14, P-15)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.md (dependência)
- .ai/specs/spec-017-identity-access-session-v1.md (dependência: identidade, RLS, pepper)
- .ai/specs/spec-007-invoice-data-model-v1.md (snapshot invoice)
- .ai/specs/spec-023-ui-spec-v1.md (telas perfil/banco)
last-revised: '2026-11-14'
lgpd-class: sensível
tags:
- specs
- docs
- prestadora
- contas-bancarias
- lgpd
spec-id: spec-018
specname: provider-profile-bank-account-v1
version: 1.0.0
status: ratificado
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: docs/change-requests/cr-004-provider-profile-bank.md (CR-004, SPEC-018)
task: "TA-0066 | sender: agent-nexus-prime-ultimate"
kill_switch: inherited
lgpd-class: sensível
trace:
  - docs/change-requests/cr-004-provider-profile-bank.md
  - docs/especificacoes/spec-prop-019-provider-profile-bank.md
  - docs/decisoes/ccb-003-multiusuario-lgpd.md
  - constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04, P-14, P-15)
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.md
  - .ai/specs/spec-017-identity-access-session-v1.md
  - .ai/specs/spec-007-invoice-data-model-v1.md
  - .ai/specs/spec-023-ui-spec-v1.md
---

# SPEC spec-018 — provider-profile-bank-account-v1 — Perfil da prestadora e contas bancárias de depósito

**Status:** **RATIFICADA** — Liberada após CCB-003 (CR-008 resolvido). Implementa CR-004. Dependências: SPEC-017 (identidade), SPEC-022 (lifecycle/criptografia/SMTP).

---

## 1. Contexto e Origem

Emitida por TA-0066 / CR-004 (agent-nexus-prime-ultimate → agent-sdd-specialist, action: spec, 2026-11-14) para implementar o cadastro da empresa prestadora (MEI/PJ), CNPJ, endereço e contas bancárias de depósito (wire transfer, SWIFT/BIC, IBAN). Snapshot na invoice finalizada para imutabilidade histórica. Criptografia em repouso para dados bancários sensíveis. Condicionada à SPEC-017 (identidade/RLS/pepper) e SPEC-022 (criptografia pgcrypto/SMTP/lifecycle).

---

## 2. Modelo de Dados

### 2.1 Tabela `provider_profiles` (1:1 com `users`)

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|-----------|
| `user_id` | UUID | PK, FK → `users.id`, ON DELETE CASCADE | Proprietário (compartilha PK) |
| `legal_name` | VARCHAR(120) | NOT NULL | Razão social / nome fantasia |
| `category` | VARCHAR | NOT NULL, CHECK IN (`mei`, `legal_entity`) | Categoria jurídica |
| `cnpj` | CHAR(14) | NULLABLE, UNIQUE (WHERE NOT NULL) | CNPJ apenas dígitos (obrigatório se `legal_entity`) |
| `address_line1` | VARCHAR(200) | NOT NULL | Logradouro + número |
| `address_line2` | VARCHAR(100) | NULLABLE | Complemento |
| `neighborhood` | VARCHAR(100) | NOT NULL | Bairro |
| `city` | VARCHAR(100) | NOT NULL | Cidade |
| `state` | CHAR(2) | NOT NULL | UF (código IBGE) |
| `postal_code` | CHAR(8) | NOT NULL | CEP apenas dígitos |
| `country_code` | CHAR(2) | NOT NULL, DEFAULT `BR` | ISO 3166-1 |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Criação |
| `updated_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Atualização |

**Regras:**
- PK/FK compartilhada com `users.id` (one-to-one).
- `category = 'legal_entity'` → `cnpj` **obrigatório** (14 dígitos, dígito verificador válido).
- `category = 'mei'` → `cnpj` opcional (MEI pode usar CPF).
- `cnpj` válido apenas dígitos; dígito verificador validado application-side.
- Alteração de `cnpj` → rotação alias HMAC em `user_login_identifiers` (mesma transação, SPEC-017).
- `country_code` ISO 3166-1 (padrão `BR`).

### 2.2 Tabela `provider_bank_accounts` (1:N por usuário)

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|-----------|
| `id` | UUID | PK | Identificador único |
| `user_id` | UUID | FK → `users.id`, ON DELETE CASCADE | Proprietário |
| `account_type` | VARCHAR | NOT NULL, CHECK IN (`checking`, `savings`, `payment`, `wire`) | Tipo de conta |
| `bank_code` | CHAR(3) | NOT NULL | Código COMPE do banco (ex.: `001`, `237`, `341`) |
| `bank_name` | VARCHAR(100) | NOT NULL | Nome do banco |
| `branch` | VARCHAR(10) | NOT NULL | Agência |
| `account_number` | BYTEA | NOT NULL | **Cifrado** (`pgcrypto` + pepper) |
| `account_digit` | VARCHAR(2) | NOT NULL | Dígito da conta |
| `swift_bic` | BYTEA | NULLABLE | **Cifrado** (SWIFT/BIC para wire internacional) |
| `iban` | BYTEA | NULLABLE | **Cifrado** (IBAN para SEPA/internacional) |
| `account_holder` | VARCHAR(120) | NOT NULL | Titular da conta |
| `currency` | CHAR(3) | NOT NULL, CHECK IN (`BRL`, `USD`, `EUR`) | Moeda da conta |
| `is_primary` | BOOLEAN | NOT NULL, DEFAULT `false` | Conta primária (uma por usuário) |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Criação |
| `updated_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Atualização |

**Constraints:**
- `UNIQUE (user_id) WHERE is_primary` — uma conta primária por usuário.
- `account_type = 'wire'` → `swift_bic` **obrigatório**; `iban` opcional.
- `account_type IN ('checking','savings','payment')` → `swift_bic`/`iban` opcionais.
- FK `ON DELETE CASCADE` com `users`.

### 2.3 Cifragem em Repouso (CR4-D02, SPEC-022)

- **Biblioteca:** `pgcrypto` (PostgreSQL nativo) ou `cryptography` (Python) — preferência `pgcrypto` para transparência SQL.
- **Chave:** Derivada de `COGME_ENCRYPTION_PEPPER` (env var, 256-bit) via HKDF.
- **Campos cifrados:** `account_number`, `swift_bic`, `iban` (tipo `BYTEA`).
- **Funções SQL:**
  ```sql
  -- Cifrar
  INSERT ... pgp_sym_encrypt(account_number::text, current_setting('app.encryption_key')) ...
  -- Decifrar (apenas em transação de snapshot invoice)
  SELECT pgp_sym_decrypt(account_number, current_setting('app.encryption_key')) ...
  ```
- **Chave de cifragem:** Derivada de `COGME_ENCRYPTION_PEPPER` via `current_setting('app.encryption_key')` (definida no middleware de request).
- **Rotação:** Anual (job manual). Re-cifra dados existentes com nova chave.

---

## 3. Snapshot na Invoice Finalizada (CR4-D04, SPEC-007)

- **Momento:** Transição `draft → finalized` (SPEC-020).
- **Dados copiados (imutáveis):**
  - `provider_profiles`: `legal_name`, `category`, `cnpj`, endereço completo, `country_code`.
  - `provider_bank_accounts` (primária): `bank_code`, `bank_name`, `branch`, `account_number` (decifrado), `account_digit`, `swift_bic` (decifrado), `iban` (decifrado), `account_holder`, `currency`.
- **Armazenamento:** Colunas de snapshot em `invoices` (emenda SPEC-007, SPEC-020).
- **Imutabilidade:** Alteração posterior de perfil/banco **não** afeta invoices finalizadas.

---

## 4. Regras de Negócio

### 4.1 Perfil da Prestadora

- **Criação:** Ao primeiro acesso à tela de perfil (lazy) ou no cadastro inicial.
- **Validações:**
  - `legal_name`: 1-120 chars.
  - `category`: `mei` ou `legal_entity`.
  - `cnpj`: 14 dígitos, dígito verificador válido (se `legal_entity`); opcional se `mei`.
  - Endereço: todos campos obrigatórios; `state` UF válida; `postal_code` 8 dígitos.
  - `country_code`: ISO 3166-1.
- **Atualização:** Permitida (exceto `user_id`); `updated_at` automático.
- **CNPJ alteração:** Rotação alias HMAC em `user_login_identifiers` (mesma transação, SPEC-017).

### 4.2 Contas Bancárias

- **CRUD:** Create, Read, Update, Delete (soft delete via `is_primary` shift).
- **Primária:** Apenas uma por usuário (`UNIQUE (user_id) WHERE is_primary`).
- **Wire transfer:** `account_type = 'wire'` exige `swift_bic`; `iban` opcional.
- **Validações:**
  - `bank_code`: 3 dígitos (COMPE válido — lista mantida em config).
  - `branch`: alfanumérico, max 10.
  - `account_number` + `account_digit`: cifrados; validação de formato antes de cifrar.
  - `swift_bic`: 8 ou 11 chars alfanuméricos (BIC padrão).
  - `iban`: até 34 chars alfanuméricos (IBAN padrão).
  - `currency`: `BRL`, `USD`, `EUR`.

### 4.3 Snapshot Invoice (Transação Atômica)

```python
async def finalize_invoice(invoice_id: UUID, user_id: UUID) -> None:
    async with session.begin():
        # 1. Lock invoice + valida owner
        invoice = await session.get(Invoice, invoice_id, with_for_update=True)
        if invoice.owner_user_id != user_id: raise Forbidden
        if invoice.status != 'draft': raise Conflict
        
        # 2. Copia snapshots
        provider = await session.get(ProviderProfile, user_id)
        bank = await session.execute(
            select(ProviderBankAccount).where(
                ProviderBankAccount.user_id == user_id,
                ProviderBankAccount.is_primary == True
            )
        ).scalar_one_or_none()
        
        # 3. Decifra dados bancários para snapshot
        bank_snapshot = decrypt_bank_for_snapshot(bank) if bank else None
        
        # 4. Atualiza invoice com snapshots + status + finalized_at
        invoice.provider_snapshot = provider.to_snapshot_dict()
        invoice.bank_snapshot = bank_snapshot.to_snapshot_dict() if bank_snapshot else None
        invoice.status = 'finalized'
        invoice.finalized_at = datetime.now(timezone.utc)
        invoice.locale = derive_locale(invoice.client_country_code)
        invoice.client_country_code = invoice.client_country_code
```

---

## 5. Contrato HTTP `/provider` e `/bank`

| Verbo | Rota | Entrada | Saída | Erros |
|-------|------|---------|-------|-------|
| GET | `/provider` | — | 200 `ProviderProfile` | 401, 404 |
| PUT | `/provider` | `ProviderProfileUpdate` | 200 `ProviderProfile` | 400, 401, 409 |
| GET | `/bank` | — | 200 `List[BankAccount]` | 401 |
| POST | `/bank` | `BankAccountCreate` | 201 `BankAccount` | 400, 401, 409 |
| PUT | `/bank/{id}` | `BankAccountUpdate` | 200 `BankAccount` | 400, 401, 404 |
| DELETE | `/bank/{id}` | — | 204 | 401, 404 |
| POST | `/bank/{id}/primary` | — | 200 `BankAccount` | 401, 404 |

**Schemas (Pydantic `extra="forbid"`):**
- `ProviderProfileUpdate`: `legal_name?`, `category?`, `cnpj?`, `address_line1?`, `address_line2?`, `neighborhood?`, `city?`, `state?`, `postal_code?`, `country_code?`
- `BankAccountCreate`: `account_type`, `bank_code`, `bank_name`, `branch`, `account_number`, `account_digit`, `swift_bic?`, `iban?`, `account_holder`, `currency`, `is_primary?`
- `BankAccountUpdate`: campos opcionais de `Create` + `is_primary`

---

## 5. Segurança — Controles Obrigatórios

| Controle | Implementação |
|----------|---------------|
| **Cifragem bancária** | `pgcrypto` (`pgp_sym_encrypt/decrypt`) com chave derivada de `COGME_ENCRYPTION_PEPPER` |
| **RLS** | `CREATE POLICY` em `provider_profiles` e `provider_bank_accounts` (`owner_user_id = current_user_id()`) |
| **Autorização** | Middleware `owner_user_id` da sessão; nunca do request |
| **Cifragem transacional** | Decifração **apenas** na transação de snapshot invoice (SPEC-020) |
| **Rotação chave** | Anual (job manual); re-cifra dados existentes |
| **Logs** | Zero dados bancários em logs; apenas metadata de acesso |
| **Autorização** | Middleware `owner_user_id` da sessão; nunca do request |

---

## 6. Critérios de Aceite e Testes

| ID | Critério | Método |
|----|----------|--------|
| AC-01 | Perfil prestadora: cria/atualiza; valida CNPJ (dígito verificador); category MEI/PJ | Teste integração |
| AC-02 | Conta bancária: CRUD; primária única; wire exige SWIFT/BIC | Teste integração |
| AC-03 | Cifragem: `account_number`, `swift_bic`, `iban` cifrados em repouso (`pgcrypto`); decifra correto | Teste unitário (vetores) |
| AC-04 | Snapshot invoice: copia prestadora + banco primária (decifrado) na finalização; imutável | Teste integração (transação atômica) |
| AC-05 | RLS: usuário A não acessa perfil/banco de usuário B | Teste integração (multi-user) |
| AC-05 | Rotação chave: job anual re-cifra dados com nova chave | Teste unitário (simulação) |
| AC-06 | Logs zero dados bancários | Teste automatizado (grep) |
| AC-07 | CNPJ alteração: rotação alias HMAC atômica (SPEC-017) | Teste integração |
| AC-08 | Wire transfer: exige `swift_bic`; valida formato BIC | Teste unitário |

---

## 7. Rastreabilidade

| Fonte | Seção |
|-------|-------|
| CR-004 (issue #37) | Todas |
| CR-008 / SPEC-022 | Criptografia pgcrypto, RLS, lifecycle |
| CR-003 / SPEC-017 | Identidade, RLS, pepper HMAC, autorização |
| CCB-003 | CR4-D01..D04, CR8-D02, CR8-D05, CR8-D06 |
| Constitution | P-02, P-03, P-04, P-14, P-15 |
| SPEC-022 | Criptografia pgcrypto, lifecycle, SMTP |
| SPEC-017 | Identidade, RLS, pepper, autorização P-14 |
| SPEC-007 | Modelo canônico invoice (snapshot) |
| SPEC-023 | Telas perfil, contas bancárias |

---

## 8. Fora de Escopo (YAGNI)

- Múltiplas prestadoras por usuário.
- Integração com Open Banking / Pix / plataformas de pagamento.
- NF-e/NFS-e, envio automático de email.
- Auditoria de alterações (pode ser adicionada depois).
- Validação bancária via ReceitaWS / Open Banking.

---

## CHANGELOG

- 1.0.0 — 2026-11-14: SPEC-018 ratificada (CCB-003); implementa CR-004; 2 tabelas (provider_profiles 1:1, provider_bank_accounts 1:N), cifragem pgcrypto, snapshot invoice imutável, RLS, autorização P-14. Dependências SPEC-017, SPEC-022.