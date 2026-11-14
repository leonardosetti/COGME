---
id: ai-specs-spec-018-provider-profile-bank-account-v1-spec
title: SPEC spec-018 — provider-profile-bank-account-v1 — Perfil da prestadora e contas bancárias de depósito
type: spec
version: 1.0.0
status: ativo
owner: agent-dba
derived-from:
- docs/decisoes/ccb-CR-002.md (Gate D liberado)
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-03 inventário, DEC-06 numeração, DEC-07 bilíngue)
- .ai/specs/spec-017-identity-access-session-v1.spec.md (Gate C, require_owner, P-14)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (Gate B, retenção, CP-1..CP-5)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.2 tabelas provider_profiles, provider_bank_accounts, §13.1 Gate D)
- constitution.md v1.3.0 (P-14 isolamento, P-15 LGPD/GDPR, P-03 soberania)
- LGPD Lei 13.709/2018 (art. 7º V, 11 - dados bancários = comuns, não sensíveis)
last-revised: '2026-11-14'
lgpd-class: dados-pessoais
tags:
- specs
- docs
- adequado-a-norma
- prestadora
- banco
- dados-bancarios
---
---
spec_id: spec-018
specname: provider-profile-bank-account-v1
version: 1.0.0
status: ratificada
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: CR-002 Gate D (docs/decisoes/ccb-CR-002.md) + SPEC-017 + SPEC-022
task: CR-002 | sender: agent-project-analyst | kill_switch: inherited
trace:
  - docs/decisoes/ccb-CR-002.md (Gate D liberado)
  - docs/decisoes/ccb-lgpd-decisoes.md (DEC-03: endereço/bancários NULLable; DEC-06: numeração; DEC-07: bilíngue)
  - .ai/specs/spec-017-identity-access-session-v1.spec.md (require_owner, P-14, Argon2id)
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (retenção 5a+6m, anonimização, CP-1..CP-5)
  - docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.2 tabelas, §13.1 Gate D SPEC-018)
  - constitution.md v1.3.0 (P-14, P-15, P-03, Art. 7)
  - LGPD art. 7º V, 11 (dados bancários = comuns)
lgpd-class: dados-pessoais
---

# SPEC spec-018 — provider-profile-bank-account-v1 — Perfil da prestadora e contas bancárias de depósito

**Status: RATIFICADA** — Emissão autorizada por CCB/GP via CR-002 Gate D (2026-11-14). Paralela às SPEC-019, 020, 021. Dependências: SPEC-017 (identidade/autorização), SPEC-022 (privacidade/lifecycle).

---

## 1. Contexto e origem

Esta spec define o cadastro da **empresa prestadora** (MEI ou Pessoa Jurídica) e suas **contas bancárias de depósito**, com snapshot na invoice finalizada. Dados bancários são criptografados em repouso (P-03, ADR-019). Endereço e dados bancários são **NULLable** (DEC-03, minimização art. 6º III LGPD).

**Regras de negócio:**
- Um perfil prestadora por usuário (`provider_profiles.user_id` PK/FK)
- Uma ou mais contas bancárias; **exatamente uma primária** (`is_primary`)
- Snapshot dos dados na invoice finalizada (imutável)
- CNPJ obrigatório apenas para `category = 'legal_entity'`; MEI usa CPF do titular
- Rotação de alias CNPJ na mesma transação do update de `provider_profiles.cnpj` (SPEC-017 §3.2)

---

## 2. Modelo de dados

### 2.1 `provider_profiles` — Perfil da prestadora

| Campo | Tipo | Constraints | Observações |
|-------|------|-------------|-------------|
| `user_id` | UUID | PK, FK → `users.id` | ON DELETE CASCADE; um por usuário |
| `legal_name` | VARCHAR(255) | NOT NULL | Razão social / nome fantasia |
| `category` | VARCHAR(20) | NOT NULL, CHECK `IN ('mei','legal_entity')` | MEI ou Pessoa Jurídica |
| `cnpj` | CHAR(14) | NULL, UNIQUE | Obrigatório se `category = 'legal_entity'`; apenas dígitos; validação DV |
| `address` | TEXT | NULL | **NULLable** (DEC-03 minimização) |
| `city` | VARCHAR(100) | NULL | |
| `state` | CHAR(2) | NULL | UF (SP, RJ, etc.) |
| `postal_code` | CHAR(8) | NULL | CEP apenas dígitos |
| `country_code` | CHAR(2) | NOT NULL, DEFAULT 'BR' | ISO 3166-1 |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | |
| `updated_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | Trigger auto |

**Validações:**
- Se `category = 'legal_entity'` → `cnpj` NOT NULL + válido (DV)
- Se `category = 'mei'` → `cnpj` NULL (usa CPF do titular via `users.cpf`)
- `country_code` = 'BR' fixo no MVP (expansão internacional futura)

### 2.2 `provider_bank_accounts` — Contas bancárias de depósito

| Campo | Tipo | Constraints | Observações |
|-------|------|-------------|-------------|
| `id` | UUID | PK | |
| `user_id` | UUID | FK → `users.id`, NOT NULL | ON DELETE CASCADE |
| `account_type` | VARCHAR(20) | NOT NULL, CHECK `IN ('checking','savings','payment')` | Corrente, poupança, pagamento |
| `bank_code` | VARCHAR(10) | NOT NULL | Código COMPE (ex.: 001, 237, 341) |
| `bank_name` | VARCHAR(100) | NOT NULL | Nome do banco |
| `branch` | VARCHAR(10) | NOT NULL | Agência (com dígito se houver) |
| `account_number` | VARCHAR(20) | NOT NULL | Número da conta |
| `account_digit` | VARCHAR(2) | NOT NULL | Dígito verificador da conta |
| `swift_bic` | VARCHAR(11) | NULL | SWIFT/BIC para wire internacional |
| `iban` | VARCHAR(34) | NULL | IBAN (futuro uso internacional) |
| `account_holder` | VARCHAR(255) | NOT NULL | Titular da conta (deve bater com `legal_name` ou `users.name`) |
| `currency` | CHAR(3) | NOT NULL, DEFAULT 'BRL' | ISO 4217 |
| `is_primary` | BOOLEAN | NOT NULL, DEFAULT false | **Exatamente uma por usuário** (partial unique index) |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | |
| `updated_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | Trigger auto |

**Constraints:**
- `UNIQUE (user_id, is_primary) WHERE is_primary = true` — uma conta primária por usuário
- `CHECK (currency IN ('BRL','USD','EUR'))` — moedas suportadas

**Criptografia em repouso (P-03, ADR-019):**
- Campos sensíveis: `account_number`, `account_digit`, `swift_bic`, `iban`
- Implementação: `pgcrypto` (AES-256-GCM) com DEK por usuário (derivada de `user_id` + master key em env var)
- Funções: `encrypt_bank_field(plaintext, user_id)`, `decrypt_bank_field(ciphertext, user_id)`
- **Snapshot em invoice:** descriptografa no momento da finalização → armazena em `invoices.bank_snapshot` (JSONB, texto plano) — invoice finalizada é imutável e auditorável

---

## 3. APIs

| Endpoint | Método | Descrição | Autenticação | Validações |
|----------|--------|-----------|--------------|------------|
| `/v1/provider/profile` | GET | Retorna perfil da prestadora | `require_owner("provider_profile")` | - |
| `/v1/provider/profile` | PUT | Atualiza perfil (exceto `user_id`, `category` se PJ) | `require_owner("provider_profile")` | Se `category = legal_entity` → `cnpj` obrigatório + válido; rotação alias CNPJ atômica |
| `/v1/provider/bank-accounts` | GET | Lista contas bancárias (descriptografadas) | `require_owner("provider_bank_account")` | Owner check |
| `/v1/provider/bank-accounts` | POST | Cria conta bancária | `require_owner("provider_bank_account")` | Se `is_primary=true` → desmarca anterior; criptografa campos sensíveis |
| `/v1/provider/bank-accounts/{id}` | PUT | Atualiza conta | `require_owner("provider_bank_account")` | Mesma lógica primária; criptografa |
| `/v1/provider/bank-accounts/{id}` | DELETE | Remove conta (não permite remover primária se for única) | `require_owner("provider_bank_account")` | Validação integridade |

**Schemas:** `src/backend/schemas/provider.py` (Pydantic). Campos sensíveis marcados `exclude=True` em response models (nunca retornados em listagem — apenas no GET individual com owner check).

---

## 4. Snapshot na Invoice Finalizada

Na finalização da invoice (`POST /v1/invoices/{id}/finalize` ou criação direta finalized):

```python
bank_snapshot = {
    "bank_code": decrypt(bank.bank_code),
    "bank_name": bank.bank_name,
    "branch": bank.branch,
    "account_number": decrypt(bank.account_number),  # descriptografado para snapshot
    "account_digit": decrypt(bank.account_digit),
    "account_holder": bank.account_holder,
    "currency": bank.currency,
    "swift_bic": decrypt(bank.swift_bic) if bank.swift_bic else None,
    "iban": decrypt(bank.iban) if bank.iban else None,
}
# Armazenado em invoices.bank_snapshot (JSONB)
```

**Regra:** Snapshot é **imutável** — alterações posteriores no perfil/banco não afetam invoices já finalizadas.

---

## 5. Retenção e Eliminação (SPEC-022, DEC-04)

| Dado | Retenção | Eliminação |
|------|----------|------------|
| `provider_profiles` | Enquanto conta ativa | Hard delete imediato na exclusão conta |
| `provider_bank_accounts` | Enquanto conta ativa | Hard delete imediato (dados criptografados) |
| `invoices.bank_snapshot` | 5 anos + 6 meses (segue invoice) | Anonimização: campos bancários → `NULL`; mantém `bank_name`, `currency` |

---

## 6. Critérios de aceite e testes

- [ ] **AC-01:** Perfil prestadora: MEI (sem CNPJ) ou PJ (CNPJ obrigatório + validação DV); `address`/`city`/etc. NULLable
- [ ] **AC-02:** Contas bancárias: criptografia `pgcrypto` AES-256-GCM em `account_number`, `account_digit`, `swift_bic`, `iban`; DEK por usuário
- [ ] **AC-03:** Exatamente uma conta primária por usuário (partial unique index); toggle `is_primary` atômico
- [ ] **AC-04:** Snapshot na invoice finalizada descriptografa dados bancários; armazena em `bank_snapshot` JSONB
- [ ] **AC-05:** `require_owner` em todas rotas; 404 se não owner; CNPJ rotation atômica com alias (SPEC-017)
- [ ] **AC-06:** Retenção/eliminação: hard delete perfil/banco na exclusão conta; snapshot invoice segue retenção 5a+6m
- [ ] **AC-07:** Logs nunca contêm dados bancários descriptografados (spec-015 CP-2, ADR-019 ST-09)
- [ ] **AC-08:** Testes: criptografia/descriptografia roundtrip; partial unique index; snapshot imutável; owner check

---

## 7. Rastreabilidade

| Referência | Fonte |
|------------|-------|
| CR-002 Gate D | `docs/decisoes/ccb-CR-002.md` |
| DEC-03, DEC-06, DEC-07 | `docs/decisoes/ccb-lgpd-decisoes.md` |
| SPEC-017 (identidade) | `.ai/specs/spec-017-identity-access-session-v1.spec.md` |
| SPEC-022 (privacidade) | `.ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md` |
| spec-prop-017 §12.2 | `docs/especificacoes/spec-prop-017-conta-multiusuario.md` |
| Constitution v1.3.0 | `constitution.md` (P-14, P-15, P-03) |
| LGPD art. 7º V, 11 | Dados bancários = comuns |

---

## 8. Fora de escopo (YAGNI)

- Múltiplos perfis prestadora por usuário
- Contas bancárias em moedas além de BRL/USD/EUR (futuro)
- Integração com APIs bancárias (Open Banking, Pix automático)
- Validação de titularidade da conta (microdepósitos)
- Histórico de alterações de perfil/banco (auditoria) — futuro

---

## 9. Metadados de emissão

- **Avaliador primário:** `agent-dba` + `agent-business-analysis-specialist`
- **Ratificação:** CCB/GP via CR-002 Gate D (2026-11-14)
- **Dependências:** SPEC-017, SPEC-022
- **parcel.dod:** true
- **Data da emissão:** 2026-11-14
- **Status da spec:** ativa / ratificada

---

## CHANGELOG

| Versão | Data | Task/Handoff | Mudança |
|--------|------|--------------|---------|
| 1.0.0 | 2026-11-14 | CR-002 Gate D / agent-dba + agent-business-analysis-specialist | Emissão inicial, ratificada. Perfil MEI/PJ, contas bancárias criptografadas, snapshot invoice, NULLable endereço/bancários, uma primária por usuário. |

---

## CAMADAS FUNDAMENTAIS — MAPA (TA-0031)

| Camada | Seção nesta spec | Estado |
|--------|------------------|--------|
| (a) cabeçalho | frontmatter (`spec_id: spec-018`, `version: 1.0.0`, `status: ratificada`) | aplicada |
| (b) Contexto/origem | §1 + frontmatter `origin`/`task` | aplicada |
| (c) Resolução de conflitos | §1 (regras de negócio) | aplicada |
| (d) Corpo de decisões/requisitos/contratos | §2 (modelo dados), §3 (APIs), §4 (snapshot), §5 (retenção) | aplicada |
| (e) Critérios de aceite/testes | §6 (AC-01..AC-08) | aplicada |
| (f) Rastreabilidade | §7 + frontmatter `trace` | aplicada |
| (g) Fora de escopo (YAGNI) | §8 | aplicada |
| (h) Changelog | CHANGELOG | aplicada |