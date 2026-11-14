---
id: ai-specs-spec-017-identity-access-session-v1
title: 'SPEC spec-017 — identity-access-session-v1 — Identidade, aliases, senha, sessões e recuperação'
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-003-identity-access-session.md
- docs/especificacoes/spec-prop-018-identity-access-session.md
- docs/decisoes/ccb-003-multiusuario-lgpd.md (CR-008 liberado)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04, P-07, P-14, P-15)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.md (dependência)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.md (D1-D7)
- .ai/specs/spec-004-backend-mvp-v1.md (rotas auth)
- .ai/specs/spec-023-ui-spec-v1.md (telas login/recovery)
last-revised: '2026-11-14'
lgpd-class: sensível
tags:
- specs
- docs
- identidade
- autenticacao
- sessao
- seguranca
spec-id: spec-017
specname: identity-access-session-v1
version: 1.0.0
status: ratificado
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: docs/change-requests/cr-003-identity-access-session.md (CR-003, SPEC-017)
task: "TA-0065 | sender: agent-nexus-prime-ultimate"
kill_switch: inherited
lgpd-class: sensível
trace:
  - docs/change-requests/cr-003-identity-access-session.md
  - docs/especificacoes/spec-prop-018-identity-access-session.md
  - docs/decisoes/ccb-003-multiusuario-lgpd.md (CR-008 liberado)
  - constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04, P-07, P-14, P-15)
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.md
  - .ai/specs/spec-015-lgpd-produto-proposta-v1.md
  - .ai/specs/spec-004-backend-mvp-v1.md
  - .ai/specs/spec-023-ui-spec-v1.md
---

# SPEC spec-017 — identity-access-session-v1 — Identidade, aliases, senha, sessões e recuperação

**Status:** **RATIFICADA** — Liberada após CCB-003 (CR-008 resolvido). Implementa CR-003. Dependência: SPEC-022 (lifecycle/privacidade).

---

## 1. Contexto e Origem

Emitida por TA-0065 / CR-003 (agent-nexus-prime-ultimate → agent-sdd-specialist, action: spec, 2026-11-14) para implementar o domínio de identidade e acesso: cadastro, login (email/CPF/CNPJ), aliases HMAC, senha Argon2id, sessão opaca, recuperação por email, CSRF, rate limit. Condicionada à SPEC-022 (lifecycle/privacidade) via CCB-003.

---

## 2. Modelo de Dados

### 2.1 Tabela `users`

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|-----------|
| `id` | UUID | PK | Identificador único |
| `internal_username_hash` | BYTEA | NOT NULL, UNIQUE | HMAC-SHA-256(pepper, identificador_aleatorio) |
| `name` | VARCHAR(120) | NOT NULL | Nome completo |
| `email` | VARCHAR(255) | NOT NULL, UNIQUE, IMMUTABLE | Email (lowercase, trim) |
| `phone` | VARCHAR(30) | NULLABLE | Telefone (opcional) |
| `cpf` | CHAR(11) | NOT NULL, UNIQUE, IMMUTABLE | CPF apenas dígitos |
| `password_hash` | VARCHAR(255) | NOT NULL | Argon2id hash |
| `status` | VARCHAR | NOT NULL, DEFAULT `active`, CHECK IN (`active`, `dormant`, `deleted`) | Estado da conta |
| `dormant_since` | TIMESTAMPTZ | NULLABLE | Timestamp dormência |
| `last_login_at` | TIMESTAMPTZ | NULLABLE | Último login |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Criação |
| `updated_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Atualização |

**Regras:**
- `email` e `cpf` são **imutáveis** após cadastro (não há endpoint de alteração).
- `internal_username_hash` = HMAC-SHA-256(pepper, uuid_aleatorio) — identificador opaco para logs/auditoria.
- `status` transições: `active ↔ dormant`, `active → deleted`, `dormant → deleted`. `deleted` terminal.

### 2.2 Tabela `user_login_identifiers`

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|-----------|
| `id` | UUID | PK | Identificador único |
| `user_id` | UUID | FK → `users.id`, ON DELETE CASCADE | Proprietário |
| `kind` | VARCHAR | NOT NULL, CHECK IN (`email`, `cpf`, `cnpj`) | Tipo de identificador |
| `lookup_hmac` | BYTEA | NOT NULL | HMAC-SHA-256(pepper, identificador_normalizado) |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Criação |
| `retired_at` | TIMESTAMPTZ | NULLABLE | Rotacionado (CNPJ) |

**Constraints:**
- `UNIQUE (kind, lookup_hmac)` — impede colisão e enumeração.
- `UNIQUE (user_id, kind) WHERE retired_at IS NULL` — um identificador ativo por tipo por usuário.
- CNPJ pode ser alterado: antiga entrada `retired_at = now()`, nova entrada com novo HMAC.

### 2.3 Tabela `user_sessions`

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|-----------|
| `id` | UUID | PK | Identificador único |
| `user_id` | UUID | FK → `users.id`, ON DELETE CASCADE | Proprietário |
| `token_hash` | BYTEA | NOT NULL, UNIQUE | SHA-256(token_aleatorio_256bit) |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Criação |
| `last_seen_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Último uso |
| `expires_at` | TIMESTAMPTZ | NOT NULL | Expiração (24h sliding) |
| `revoked_at` | TIMESTAMPTZ | NULLABLE | Revogação |

**Regras:**
- Token gerado: 256-bit aleatório (secrets.token_bytes(32)).
- Armazenado apenas `token_hash = SHA-256(token)`.
- TTL: 24h sliding (atualiza `last_seen_at` e `expires_at` a cada request autenticado).
- Rotação pós-login: nova sessão, antiga revogada.
- Revogação: logout, exclusão conta, dormência, reativação, admin.

### 2.4 Tabela `password_reset_tokens`

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|-----------|
| `id` | UUID | PK | Identificador único |
| `user_id` | UUID | FK → `users.id`, ON DELETE CASCADE | Proprietário |
| `token_hash` | BYTEA | NOT NULL, UNIQUE | SHA-256(token_aleatorio_256bit) |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Criação |
| `expires_at` | TIMESTAMPTZ | NOT NULL | TTL 1h |
| `used_at` | TIMESTAMPTZ | NULLABLE | Single-use |

**Regras:**
- Token: 256-bit aleatório.
- TTL: 1 hora.
- Single-use: `used_at` preenchido no uso; token invalidado após uso.
- Email local (SMTP autohospedado SPEC-022).

---

## 3. Regras de Negócio

### 3.1 Cadastro

- **Campos obrigatórios:** `name`, `email`, `cpf`, `password`.
- **Opcional:** `phone`, `cnpj` (se categoria PJ).
- **Validações:**
  - Email: lowercase, trim, formato RFC 5322, UNIQUE.
  - CPF: 11 dígitos, dígito verificador válido, UNIQUE.
  - CNPJ (se informado): 14 dígitos, dígito verificador válido, UNIQUE (enquanto ativo).
  - Senha: mínimo 12 chars, Argon2id hash.
- **Cria aliases:** `email` + `cpf` (+ `cnpj` se informado) em `user_login_identifiers`.
- **Status inicial:** `active`.

### 3.2 Login

- **Identificadores aceitos:** `email`, `cpf`, `cnpj` (qualquer um).
- **Normalização:** email → lowercase/trim; CPF/CNPJ → apenas dígitos.
- **Lookup:** HMAC-SHA-256(pepper, identificador_normalizado) → `user_login_identifiers.lookup_hmac` → `user_id`.
- **Verificação senha:** Argon2id `verify(password_hash, password)`.
- **Sucesso:** Cria nova sessão (token 256-bit, hash SHA-256, TTL 24h sliding), revoga sessão anterior se mesma UA/IP, atualiza `last_login_at`.
- **Falha:** Resposta uniforme "Credenciais inválidas" (não distingue usuário inexistente vs senha errada).

### 3.3 Recuperação de Senha (CR3-D03/D04)

- **Fluxo:** Usuário informa email/CPF/CNPJ → sistema normaliza → lookup HMAC → se encontrado, gera token recovery (256-bit, hash SHA-256, TTL 1h, single-use) → envia email local (SMTP SPEC-022) com link `POST /auth/reset?token=...` → usuário define nova senha (Argon2id) → token marcado `used_at` → senha atualizada → sessões revogadas → nova sessão criada.
- **Rate Limit:** 3 requests/hora por email/CPF/CNPJ.
- **Token:** 256-bit aleatório, hash SHA-256, TTL 1h, single-use (`used_at`).

### 3.4 Sessão

- **Token:** 256-bit aleatório (`secrets.token_bytes(32)`).
- **Armazenamento:** `token_hash = SHA-256(token)` em `user_sessions`.
- **Cookie:** `__Host-session=<token>; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=86400`.
- **TTL:** 24h sliding (atualiza `expires_at` a cada request autenticado).
- **Rotação pós-login:** Nova sessão, anterior revogada (`revoked_at = now()`).
- **Revogação:** Logout, exclusão conta, dormência (todas), reativação (todas), admin.

### 3.5 Recuperação de Senha (CR3-D03)

- **Email:** SMTP local/autohospedado (SPEC-022).
- **Link:** `https://host/auth/reset?token=<token_aleatorio>` (token no query param, não no path).
- **TTL:** 1 hora.
- **Single-use:** `used_at` preenchido ao resetar.

### 3.6 CSRF (CR3-D05)

- **Double-submit cookie:** Cookie `csrf_token` (256-bit, `HttpOnly`, `Secure`, `SameSite=Lax`) + Header `X-CSRF-Token` em todas requests mutáveis (POST, PUT, PATCH, DELETE).
- **Validação:** Middleware compara cookie vs header; 403 se ausentes ou diferentes.
- **Exceções:** GET, HEAD, OPTIONS; rotas de login/recovery (stateless).

### 3.7 Rate Limit (CR3-D04)

| Endpoint | Limite | Janela | Chave |
|----------|--------|--------|-------|
| `POST /auth/login` | 10 req | 1 min | IP + identificador (email/CPF/CNPJ) |
| `POST /auth/register` | 5 req | 1 hora | IP |
| `POST /auth/recovery` | 3 req | 1 hora | IP + identificador |
| `POST /auth/reset` | 10 req | 1 hora | IP |

**Resposta 429:** `{"error": {"key": "rate_limited", "message": "Muitas tentativas. Tente novamente mais tarde."}}`

### 3.7 Aliases e Pepper HMAC

- **Pepper:** Variável `COGME_HMAC_PEPPER` (256-bit, env var).
- **Alias HMAC:** `HMAC-SHA-256(pepper, identificador_normalizado)`.
- **Rotação:** Anual (job manual). Pepper antigo mantido para verificação; novo pepper para novos hashes.
- **Rotação CNPJ:** Alteração de CNPJ → aposenta alias antigo (`retired_at = now()`) + cria novo alias com novo HMAC na mesma transação.

---

## 4. Autorização (P-14)

- **Princípio:** Todo recurso persistido carrega `owner_user_id` obrigatório.
- **Mecanismo:** Middleware extrai `user_id` da sessão validada → injeta `owner_user_id` nas dependências → **nunca** aceita `owner_user_id` do request.
- **Row-Level Security:** PostgreSQL `CREATE POLICY` em todas tabelas com `owner_user_id`:
  ```sql
  CREATE POLICY owner_isolation ON users USING (id = current_setting('app.current_user_id')::uuid);
  CREATE POLICY owner_isolation ON simulations USING (owner_user_id = current_setting('app.current_user_id')::uuid);
  -- ... demais tabelas
  ```
- **Violação:** 403 Forbidden; log de auditoria.

---

## 5. Contrato HTTP `/auth`

| Verbo | Rota | Entrada | Saída | Erros |
|-------|------|---------|-------|-------|
| POST | `/auth/register` | `RegisterRequest` | 201 `{"user_id": "uuid"}` | 400, 409, 429 |
| POST | `/auth/login` | `LoginRequest` | 200 `{"session_token": "..."}` + cookie | 400, 401, 429 |
| POST | `/auth/logout` | — | 204 | 401 |
| POST | `/auth/recovery` | `RecoveryRequest` | 202 `{"message": "Se o email/CPF/CNPJ existir, enviaremos instruções."}` | 400, 429 |
| POST | `/auth/reset` | `ResetRequest` | 200 `{"session_token": "..."}` + cookie | 400, 401, 410, 429 |
| GET | `/auth/me` | — | 200 `UserProfile` | 401 |
| POST | `/auth/sessions/revoke` | `{"all": true}` | 204 | 401 |

**Schemas (Pydantic `extra="forbid"`):**
- `RegisterRequest`: `name`, `email`, `phone?`, `cpf`, `cnpj?`, `password`
- `LoginRequest`: `identifier` (email/CPF/CNPJ), `password`
- `RecoveryRequest`: `identifier` (email/CPF/CNPJ)
- `ResetRequest`: `token`, `password`
- `UserProfile`: `id`, `name`, `email`, `phone?`, `cpf`, `status`, `created_at`

---

## 6. Segurança — Controles Obrigatórios

| Controle | Implementação | Parâmetros |
|----------|---------------|------------|
| **Senha** | Argon2id | memory=64MB, iterations=3, parallelism=4 (CR3-D01) |
| **Aliases** | HMAC-SHA-256(pepper, identificador_normalizado) | Pepper rotativo anual |
| **Sessão** | Token 256-bit; hash SHA-256; TTL 24h sliding; rotação pós-login | — |
| **Recovery** | Token 256-bit; hash SHA-256; TTL 1h; single-use | — |
| **CSRF** | Double-submit cookie + header `X-CSRF-Token` | SameSite=Lax |
| **Rate Limit** | Por IP + identificador | `slowapi` ou middleware custom |
| **RLS** | PostgreSQL `CREATE POLICY` em todas tabelas `owner_user_id` | — |
| **Logs** | Zero PII/valores/corpo; `account_lifecycle_events` auditoria | SPEC-022 |

---

## 7. Critérios de Aceite e Testes

| ID | Critério | Método |
|----|----------|--------|
| AC-01 | Cadastro cria usuário + aliases email/CPF (+CNPJ); status `active` | Teste integração |
| AC-02 | Login aceita email, CPF ou CNPJ; resposta uniforme em falha | Teste integração |
| AC-03 | Senha Argon2id (memory=64MB, iter=3, parallel=4); vetores conhecidos | Teste unitário |
| AC-04 | Sessão: token 256-bit, hash SHA-256, cookie `__Host-session`, TTL 24h sliding, rotação pós-login | Teste integração |
| AC-05 | Recovery: email local enviado, token TTL 1h, single-use, nova senha Argon2id | Teste integração (SMTP local) |
| AC-06 | CSRF: request mutável sem token → 403; com token → 200 | Teste integração |
| AC-06 | Rate limit: login 10/min por IP+identificador → 429 | Teste carga |
| AC-07 | RLS: usuário A não lê/escrita recursos de usuário B | Teste integração (multi-user) |
| AC-08 | Alias HMAC: pepper rotativo anual; rotação CNPJ atômica | Teste unitário (vetores) |
| AC-09 | Logs zero PII: nenhum log contém email, CPF, senha, token | Teste automatizado (grep) |
| AC-10 | Revogação: logout, dormência, exclusão, reativação revogam sessões | Teste integração |

---

## 8. Rastreabilidade

| Fonte | Seção |
|-------|-------|
| CR-003 (issue #36) | Todas |
| CR-008 / SPEC-022 | Dependência (lifecycle, pepper, RLS, SMTP) |
| CCB-003 | CR8-D01..D06 (pepper, RLS, SMTP local, anonimização) |
| Constitution | P-02, P-03, P-04, P-07, P-14, P-15 |
| SPEC-022 | Lifecycle, pepper, RLS, SMTP local |
| SPEC-004 | Rotas `/auth/*`, middleware auth |
| SPEC-023 | Telas login, cadastro, recovery, perfil |

---

## 9. Fora de Escopo (YAGNI)

- OAuth, SSO, MFA, federação de identidade.
- Equipes, organizações, papéis admin.
- Auditoria de acesso detalhada (pode ser adicionada depois).
- Login por Magic Link, WebAuthn, TOTP.

---

## CHANGELOG

- 1.0.0 — 2026-11-14: SPEC-017 ratificada (CCB-003); implementa CR-003; 4 tabelas, Argon2id, HMAC pepper, sessão opaca, recovery email local, CSRF double-submit, rate limit, RLS, autorização P-14. Dependência SPEC-022.