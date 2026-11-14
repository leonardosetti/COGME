---
id: ai-specs-spec-019-client-directory-v1-spec
title: SPEC spec-019 — client-directory-v1 — Carteira de clientes, ativo/inativo, cliente fictício
type: spec
version: 1.0.0
status: ativo
owner: agent-business-analysis-specialist
derived-from:
- docs/decisoes/ccb-CR-002.md (Gate D liberado)
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-03 inventário, DEC-07 bilíngue country_code)
- .ai/specs/spec-017-identity-access-session-v1.spec.md (Gate C, require_owner, P-14)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (Gate B, retenção, CP-1..CP-5)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.2 tabela clients, §12.3 integridade, §13.1 Gate D)
- constitution.md v1.3.0 (P-14 isolamento, P-15 LGPD/GDPR, Art. 7)
- LGPD Lei 13.709/2018 (art. 7º V, 6º III minimização)
last-revised: '2026-11-14'
lgpd-class: dados-pessoais
tags:
- specs
- docs
- adequado-a-norma
- clientes
- carteira
- ficticio
---
---
spec_id: spec-019
specname: client-directory-v1
version: 1.0.0
status: ratificada
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: CR-002 Gate D (docs/decisoes/ccb-CR-002.md) + SPEC-017 + SPEC-022
task: CR-002 | sender: agent-project-analyst | kill_switch: inherited
trace:
  - docs/decisoes/ccb-CR-002.md (Gate D liberado)
  - docs/decisoes/ccb-lgpd-decisoes.md (DEC-03: address NULLable; DEC-07: country_code canônico para locale)
  - .ai/specs/spec-017-identity-access-session-v1.spec.md (require_owner, P-14)
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (retenção 5a+6m, anonimização)
  - docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.2 clients, §12.3 integridade, §13.1 Gate D SPEC-019)
  - constitution.md v1.3.0 (P-14, P-15, Art. 7)
  - LGPD art. 7º V, 6º III
lgpd-class: dados-pessoais
---

# SPEC spec-019 — client-directory-v1 — Carteira de clientes, ativo/inativo, cliente fictício

**Status: RATIFICADA** — Emissão autorizada por CCB/GP via CR-002 Gate D (2026-11-14). Paralela às SPEC-018, 020, 021. Dependências: SPEC-017 (identidade/autorização), SPEC-022 (privacidade/lifecycle).

---

## 1. Contexto e origem

Esta spec define a **carteira de clientes** do usuário: cadastro opcional, estado ativo/inativo, e suporte a **cliente fictício** (dummy) para invoices ocasionais sem cadastro prévio. O `country_code` do cliente é a **fonte canônica para locale da invoice** (DEC-07: `BR`→pt-BR, demais→en). Endereço é **NULLable** (DEC-03 minimização).

**Regras de negócio:**
- Cliente pertence a um `owner_user_id` (isolamento P-14)
- `is_active` obrigatório; inativação por contrato suspenso/encerrado (`deactivated_at`)
- **Cliente fictício**: não salvo na tabela `clients`; dados informados *ad hoc* na criação da invoice; **exige `country_code` explícito** (validação 400 se ausente)
- Snapshot do cliente na invoice finalizada (imutável) — alterações posteriores não afetam histórico

---

## 2. Modelo de dados

### 2.1 `clients` — Carteira de clientes cadastrados

| Campo | Tipo | Constraints | Observações |
|-------|------|-------------|-------------|
| `id` | UUID | PK | |
| `owner_user_id` | UUID | FK → `users.id`, NOT NULL | ON DELETE CASCADE; isolamento P-14 |
| `name` | VARCHAR(255) | NOT NULL | Nome/razão social do cliente |
| `tax_id` | VARCHAR(20) | NOT NULL | CPF (11 dígitos) ou CNPJ (14 dígitos) — apenas dígitos |
| `address` | TEXT | NULL | **NULLable** (DEC-03 minimização) |
| `country_code` | CHAR(2) | NOT NULL, DEFAULT 'BR' | ISO 3166-1; **fonte canônica para locale** (DEC-07) |
| `is_active` | BOOLEAN | NOT NULL, DEFAULT true | Ativo/inativo |
| `deactivated_at` | TIMESTAMPTZ | NULL | Preenchido na inativação |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | |
| `updated_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | Trigger auto |

**Índices:** `ix_clients_owner_user_id`, `ix_clients_tax_id`, `ix_clients_is_active`, `ix_clients_country_code`

**Validações:**
- `tax_id`: apenas dígitos; validação DV para CPF (11) ou CNPJ (14)
- `country_code`: ISO 3166-1 válido (tabela de referência ou validação regex)
- Inativação: `is_active = false`, `deactivated_at = now()`; não deleta (histórico)

---

## 3. Cliente Fictício (Dummy) — Não Persistido

**Caso de uso:** Invoice eventual para cliente que não merece cadastro na carteira.

**Fluxo:**
1. Frontend: opção "Cliente não cadastrado" → campos: `name`, `tax_id`, `address` (opcional), **`country_code` OBRIGATÓRIO**
2. Backend: valida `country_code` (ISO 3166-1); se ausente → **400 validation_error** (DEC-07)
3. Cria invoice com `client_id = NULL` + `client_snapshot` JSONB contendo os dados informados
4. `client_country_code` = `country_code` informado → determina `locale` (`BR`→pt-BR, demais→en)
5. **Não** cria registro em `clients`; `client_id` permanece NULL

**Snapshot do cliente fictício na invoice:**
```json
{
  "name": "Cliente Eventual Ltda",
  "tax_id": "12345678000199",
  "address": "Av. Exemplo, 123 - São Paulo/SP",
  "country_code": "BR"
}
```

---

## 4. APIs

| Endpoint | Método | Descrição | Autenticação | Validações |
|----------|--------|-----------|--------------|------------|
| `/v1/clients` | GET | Lista clientes (paginado, ordenado por `created_at` DESC) | `require_owner("client")` | Filtra `owner_user_id`; query params: `is_active`, `country_code`, `search` |
| `/v1/clients` | POST | Cadastra cliente | `require_owner("client")` | `tax_id` único por owner; `country_code` ISO 3166-1 |
| `/v1/clients/{id}` | GET | Detalha cliente | `require_owner("client")` | 404 se não owner |
| `/v1/clients/{id}` | PUT | Atualiza cliente (exceto `owner_user_id`, `tax_id`) | `require_owner("client")` | `tax_id` imutável; `country_code` válido |
| `/v1/clients/{id}/deactivate` | POST | Inativa cliente | `require_owner("client")` | `is_active = false`, `deactivated_at = now()` |
| `/v1/clients/{id}/activate` | POST | Reativa cliente | `require_owner("client")` | `is_active = true`, `deactivated_at = NULL` |

**Schemas:** `src/backend/schemas/client.py`. `tax_id` imutável após criação (sem endpoint de alteração).

---

## 5. Snapshot na Invoice Finalizada

Tanto para cliente cadastrado (`client_id` preenchido) quanto fictício (`client_id = NULL`):

```python
client_snapshot = {
    "name": client.name,
    "tax_id": client.tax_id,
    "address": client.address,  # pode ser NULL
    "country_code": client.country_code,  # SEMPRE presente (NOT NULL)
}
# Armazenado em invoices.client_snapshot (JSONB)
```

**Regra:** Snapshot é **imutável** — alterações posteriores no cadastro do cliente não afetam invoices já finalizadas.

---

## 6. Retenção e Eliminação (SPEC-022, DEC-04)

| Dado | Retenção | Eliminação |
|------|----------|------------|
| `clients` (cadastrados) | Enquanto conta ativa | Hard delete na exclusão conta (cascade) |
| `invoices.client_snapshot` | 5 anos + 6 meses (segue invoice) | Anonimização: `name`→`ANONIMIZADO`, `tax_id`→`HASH`, `address`→`NULL`; mantém `country_code` |

---

## 7. Critérios de aceite e testes

- [ ] **AC-01:** CRUD clientes com `require_owner`; `tax_id` único por owner; `address` NULLable
- [ ] **AC-02:** Inativação/reativação: `is_active` toggle + `deactivated_at`; não deleta
- [ ] **AC-03:** Cliente fictício: `country_code` **obrigatório** (400 se ausente); não cria registro em `clients`
- [ ] **AC-04:** `client_country_code` na invoice = `country_code` do cliente (cadastrado ou fictício)
- [ ] **AC-05:** Snapshot imutável na invoice finalizada; alterações no cadastro não propagam
- [ ] **AC-06:** Retenção: hard delete `clients` na exclusão conta; snapshot invoice anonimiza 5a+6m
- [ ] **AC-07:** `country_code` ISO 3166-1 validado na criação/atualização
- [ ] **AC-08:** Testes: owner check cross-user (404); fictício sem country_code → 400; snapshot imutável

---

## 8. Rastreabilidade

| Referência | Fonte |
|------------|-------|
| CR-002 Gate D | `docs/decisoes/ccb-CR-002.md` |
| DEC-03, DEC-07 | `docs/decisoes/ccb-lgpd-decisoes.md` |
| SPEC-017, SPEC-022 | `.ai/specs/spec-017-*.spec.md`, `.ai/specs/spec-022-*.spec.md` |
| spec-prop-017 §12.2/§12.3 | `docs/especificacoes/spec-prop-017-conta-multiusuario.md` |
| Constitution v1.3.0 | `constitution.md` (P-14, P-15, Art. 7) |
| LGPD art. 7º V, 6º III | Minimização, base legal |

---

## 9. Fora de escopo (YAGNI)

- Importação em lote de clientes (CSV/Excel) — futuro
- Portal do cliente / área do cliente — fora single-user
- Enriquecimento automático de dados (ReceitaWS, CNPJ.io) — fora MVP
- Histórico de alterações de cliente (auditoria) — futuro
- Múltiplos endereços por cliente (cobrança, entrega) — futuro

---

## 10. Metadados de emissão

- **Avaliador primário:** `agent-business-analysis-specialist` + `agent-dba`
- **Ratificação:** CCB/GP via CR-002 Gate D (2026-11-14)
- **Dependências:** SPEC-017, SPEC-022
- **parcel.dod:** true
- **Data da emissão:** 2026-11-14
- **Status da spec:** ativa / ratificada

---

## CHANGELOG

| Versão | Data | Task/Handoff | Mudança |
|--------|------|--------------|---------|
| 1.0.0 | 2026-11-14 | CR-002 Gate D / agent-business-analysis-specialist + agent-dba | Emissão inicial, ratificada. Carteira clientes ativo/inativo, fictício exige country_code, snapshot imutável, NULLable address, retenção 5a+6m. |

---

## CAMADAS FUNDAMENTAIS — MAPA (TA-0031)

| Camada | Seção nesta spec | Estado |
|--------|------------------|--------|
| (a) cabeçalho | frontmatter (`spec_id: spec-019`, `version: 1.0.0`, `status: ratificada`) | aplicada |
| (b) Contexto/origem | §1 + frontmatter `origin`/`task` | aplicada |
| (c) Resolução de conflitos | §1 (regras cliente fictício, country_code canônico) | aplicada |
| (d) Corpo de decisões/requisitos/contratos | §2 (modelo), §3 (fictício), §4 (APIs), §5 (snapshot), §6 (retenção) | aplicada |
| (e) Critérios de aceite/testes | §7 (AC-01..AC-08) | aplicada |
| (f) Rastreabilidade | §8 + frontmatter `trace` | aplicada |
| (g) Fora de escopo (YAGNI) | §9 | aplicada |
| (h) Changelog | CHANGELOG | aplicada |