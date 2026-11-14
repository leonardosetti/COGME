---
id: ai-specs-spec-017-identity-access-session-v1-spec
title: SPEC spec-017 — identity-access-session-v1 — Identidade, aliases, senha, sessões, recuperação e autorização por proprietário
type: spec
version: 1.0.0
status: ativo
owner: agent-digital-security
derived-from:
- docs/decisoes/ccb-CR-002.md (Gate C liberado, CR2-D06 ratificada)
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-01..07)
- docs/decisoes/adr-017-dependencia-argon2id.md (Argon2id m=19456, t=2, p=1)
- docs/decisoes/adr-019-seguranca-multiusuario.md (Threat model STRIDE, ST-01..ST-10)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (Gate B, P-14, P-15, CP-1..CP-5)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.1, §12.2 tabelas identidade, §13.1 Gate C)
- constitution.md v1.3.0 (Art. 1.2, P-14 isolamento, P-15 LGPD/GDPR, Art. 7)
- LGPD Lei 13.709/2018 (art. 7º V, 16, 18)
last-revised: '2026-11-14'
lgpd-class: dados-pessoais
tags:
- specs
- docs
- adequado-a-norma
- identidade
- autenticacao
- sessao
- seguranca
---
---
spec_id: spec-017
specname: identity-access-session-v1
version: 1.0.0
status: ratificada
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: CR-002 Gate C (docs/decisoes/ccb-CR-002.md, CR2-D06) + ADR-017 + ADR-019 + SPEC-022
task: CR-002 | sender: agent-project-analyst | kill_switch: inherited
trace:
  - docs/decisoes/ccb-CR-002.md (Gate C liberado; CR2-D06: SMTP local, TTL 1h, pepper 90d)
  - docs/decisoes/adr-017-dependencia-argon2id.md (Argon2id OWASP/RFC 9106; m=19456, t=2, p=1)
  - docs/decisoes/adr-019-seguranca-multiusuario.md (Threat model STRIDE; ST-01..ST-10 obrigatórios)
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (P-14 isolamento, P-15 LGPD/GDPR, CP-1..CP-5)
  - docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.1 identidade/login, §12.2 tabelas users/login_identifiers/sessions/reset_tokens, §13.1 Gate C SPEC-017)
  - constitution.md v1.3.0 (Art. 1.2 escopo, P-14 isolamento proprietário, P-15 LGPD/GDPR, Art. 7)
  - LGPD art. 7º V, 16, 18
lgpd-class: dados-pessoais
---

# SPEC spec-017 — identity-access-session-v1 — Identidade, aliases, senha, sessões, recuperação e autorização por proprietário

**Status: RATIFICADA** — Emissão autorizada por CCB/GP via CR-002 Gate C (2026-11-14). Dependências: SPEC-022 (Gate B), ADR-017 (Argon2id), ADR-019 (Threat model). Precede SPEC-018, 019, 020, 021 (Gate D).

---

## 1. Contexto e origem

Esta spec implementa a camada de **identidade e acesso** para contas multiusuário (CR-002), derivando de:
- **SPEC-022** (Gate B): ciclo de vida, base legal art. 7º V, isolamento por proprietário (P-14)
- **ADR-017**: dependência `argon2-cffi` (Argon2id) para hash de senhas — parâmetros OWASP mínimos
- **ADR-019**: threat model STRIDE + 10 testes de segurança obrigatórios (ST-01..ST-10)
- **spec-prop-017** §12.1/§12.2: regras de identidade, aliases, tabelas `users`, `user_login_identifiers`, `user_sessions`, `password_reset_tokens`

**Objetivo:** Definir contratos, validações e APIs para:
- Cadastro, login, logout, recuperação de senha
- Aliases de login (email, CPF, CNPJ) com HMAC anti-enumeração
- Sessões seguras (regeneração, HttpOnly, SameSite, expiração sliding)
- Recuperação de senha (token TTL 1h, single-use, SMTP local)
- Middleware de autorização `require_owner` (P-14)

---

## 2. Resolução de conflitos

| Tema | Decisão desta spec | Fonte vencedora | Texto superado |
|------|-------------------|-----------------|----------------|
| Hash de senha | **Argon2id** (`argon2-cffi` m=19456, t=2, p=1) | ADR-017 (OWASP/RFC 9106) | Nenhum (nova dependência) |
| Aliases login | **HMAC-SHA256 com pepper rotacionado 90d** — anti-enumeração | ADR-019; spec-prop-017 §12.1 | Hash simples de CPF/email (permitia enumeração) |
| Sessão | **Regeneração no login**; token 32 bytes; armazenar só hash | ADR-019 (ST-02 session fixation) | Session fixation vulnerável |
| Recuperação senha | **TTL 1h**; single-use; rate limit 3/h; SMTP local | CR2-D06; ADR-019 (ST-06/ST-07) | TTL não definido; reset abuse |
| Autorização | **Middleware `require_owner`** em 100% rotas recurso; 404 se não owner | SPEC-022 P-14; ADR-019 (ST-03 IDOR) | IDs do cliente como autorização (vazamento cross-user) |
| CSRF | **Double-submit cookie** + header `X-CSRF-Token` em todas rotas mutáveis | ADR-019 (ST-04/ST-05) | Sem proteção CSRF |
| Rate limiting | Login 5/min/IP, 10/min/user; Reset 3/h; API 100/min/user | ADR-019 (ST-01 DoS) | Sem rate limit |
| Dados bancários | **Criptografia em repouso** (AES-256-GCM / pgcrypto) | ADR-019 §4.8; P-03 soberania | Texto plano |

---

## 3. Modelo de dados (tabelas de identidade)

### 3.1 `users` — Conta principal

| Campo | Tipo | Constraints | Observações |
|-------|------|-------------|-------------|
| `id` | UUID | PK | `gen_random_uuid()` |
| `internal_username_hash` | BYTEA | UNIQUE, NOT NULL | HMAC-SHA256(pepper, random_id) — opaco, não derivado de PII |
| `name` | VARCHAR(255) | NOT NULL | Nome completo do usuário |
| `email` | VARCHAR(255) | UNIQUE, NOT NULL, IMMUTABLE | Normalizado: trim + casefold |
| `phone` | VARCHAR(20) | NULL | Opcional |
| `cpf` | CHAR(11) | UNIQUE, NOT NULL, IMMUTABLE | Apenas dígitos; validação dígito verificador |
| `password_hash` | TEXT | NOT NULL | Argon2id (ver §3.5) |
| `status` | VARCHAR(20) | NOT NULL, DEFAULT 'active' | `active` \| `dormant` (CHECK) |
| `dormant_since` | TIMESTAMPTZ | NULL | Preenchido na transição `active` → `dormant` |
| `last_login_at` | TIMESTAMPTZ | NULL | Atualizado a cada login bem-sucedido |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | |
| `updated_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | Trigger `updated_at` auto |

**Índices:** `ix_users_email`, `ix_users_cpf`, `ix_users_status`, `ix_users_last_login_at`

### 3.2 `user_login_identifiers` — Aliases de login (anti-enumeração)

| Campo | Tipo | Constraints | Observações |
|-------|------|-------------|-------------|
| `id` | UUID | PK | |
| `user_id` | UUID | FK → `users.id`, NOT NULL | ON DELETE CASCADE |
| `kind` | VARCHAR(10) | NOT NULL, CHECK `kind IN ('email','cpf','cnpj')` | |
| `lookup_hmac` | BYTEA | NOT NULL | HMAC-SHA256(pepper, normalized_identifier) |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | |
| `retired_at` | TIMESTAMPTZ | NULL | Preenchido na rotação (ex.: CNPJ change) |

**Constraints:**
- `UNIQUE (kind, lookup_hmac)` — impede colisão de aliases
- `UNIQUE (user_id, kind) WHERE retired_at IS NULL` — um alias ativo por tipo por usuário

**Pepper:** 32 bytes aleatórios, armazenado em variável de ambiente (`LOGIN_PEPPER`), rotacionado a cada 90 dias (CR2-D06). Rotação: novo pepper → recalcula todos `lookup_hmac` em batch → swap atômico.

### 3.3 `user_sessions` — Sessões individuais

| Campo | Tipo | Constraints | Observações |
|-------|------|-------------|-------------|
| `id` | UUID | PK | |
| `user_id` | UUID | FK → `users.id`, NOT NULL | ON DELETE CASCADE |
| `token_hash` | BYTEA | NOT NULL, UNIQUE | SHA256(token + pepper) — **nunca** token em claro |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | |
| `last_seen_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | Atualizado a cada request autenticado |
| `expires_at` | TIMESTAMPTZ | NOT NULL | `created_at + 24h` (sliding: renova em `last_seen_at`) |
| `revoked_at` | TIMESTAMPTZ | NULL | Preenchido no logout / expiração / revogação admin |

**Comportamento:**
- Login: gera token 32 bytes (`secrets.token_urlsafe(32)`), calcula `token_hash`, cria registro, retorna token no cookie
- Request autenticado: extrai token do cookie → SHA256(token + pepper) → busca em `user_sessions` onde `revoked_at IS NULL` e `expires_at > now()` → atualiza `last_seen_at = now()`
- Logout: `revoked_at = now()`
- Expiração: job diário limpa sessões com `expires_at < now()` ou `revoked_at IS NOT NULL`
- **Regeneração no login:** novo login → revoga sessões anteriores do usuário (`revoked_at = now()`) → cria nova

### 3.4 `password_reset_tokens` — Recuperação de senha

| Campo | Tipo | Constraints | Observações |
|-------|------|-------------|-------------|
| `id` | UUID | PK | |
| `user_id` | UUID | FK → `users.id`, NOT NULL | ON DELETE CASCADE |
| `token_hash` | BYTEA | NOT NULL, UNIQUE | SHA256(token + pepper) |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | |
| `expires_at` | TIMESTAMPTZ | NOT NULL | `created_at + 1 hora` (CR2-D06 TTL) |
| `used_at` | TIMESTAMPTZ | NULL | Preenchido na validação bem-sucedida (single-use) |

**Fluxo:**
1. `POST /v1/auth/password/reset-request` — recebe email/CPF/CNPJ → normaliza → busca `user_login_identifiers` → se encontrado, gera token 32 bytes, cria registro, envia email (SMTP local)
2. Email: template PT-BR, link `https://app/reset?token={token}`, expiração clara (1h)
3. `POST /v1/auth/password/reset-confirm` — recebe token + nova senha → SHA256(token + pepper) → busca registro válido (`used_at IS NULL`, `expires_at > now()`) → valida → `used_at = now()` → `password_hash = argon2id.hash(nova_senha)` → revoga todas sessões do usuário

**Rate limits:** 3 requests/hora por identificador (reset-request); 5 requests/hora por token (reset-confirm)

### 3.5 Hash de senha — Argon2id (ADR-017)

**Módulo:** `src/backend/security/password.py`

```python
from argon2 import PasswordHasher, Type

ph = PasswordHasher(
    memory_cost=19456,    # 19 MiB (OWASP mínimo)
    time_cost=2,          # 2 passadas (OWASP mínimo)
    parallelism=1,        # 1 thread (OWASP mínimo)
    hash_len=32,
    salt_len=16,
    type=Type.ID          # Argon2id
)

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    try:
        ph.verify(password_hash, password)
        return True
    except Exception:
        return False

def needs_rehash(password_hash: str) -> bool:
    return ph.check_needs_rehash(password_hash)
```

**Testes obrigatórios:**
- Hash único por chamada (salt aleatório)
- Verificação correta (hash/verify roundtrip)
- Tempo constante (timing attack resistance)
- `needs_rehash` detecta parâmetros desatualizados

---

## 4. APIs de Identidade e Acesso

| Endpoint | Método | Descrição | Autenticação | Rate Limit |
|----------|--------|-----------|--------------|------------|
| `/v1/auth/register` | POST | Cadastro (email, CPF/CNPJ, senha, nome) | Pública | 5/min/IP |
| `/v1/auth/login` | POST | Login (identificador + senha) | Pública | 5/min/IP, 10/min/user |
| `/v1/auth/logout` | POST | Logout (revoga sessão atual) | Cookie session | - |
| `/v1/auth/password/reset-request` | POST | Solicita reset (email/CPF/CNPJ) | Pública | 3/h/identificador |
| `/v1/auth/password/reset-confirm` | POST | Confirma reset (token + nova senha) | Pública | 5/h/token |
| `/v1/auth/me` | GET | Perfil do usuário logado | Session | 100/min/user |
| `/v1/auth/aliases` | GET | Lista aliases ativos (tipo + mascarado) | Session | 100/min/user |
| `/v1/auth/aliases/cnpj` | PUT | Rotaciona alias CNPJ (mesma transação update perfil) | Session | 10/min/user |

**Schemas de request/response:** Definidos em `src/backend/schemas/auth.py` (Pydantic).

---

## 5. Middleware de Autorização — `require_owner` (P-14)

**Localização:** `src/backend/middleware/authorization.py`

```python
async def require_owner(resource_type: str, resource_id_param: str = "id"):
    """
    Dependency FastAPI que valida owner_user_id do recurso.
    Uso: `resource = await require_owner("simulation", "simulation_id")`
    Retorna o recurso se owner = sessão atual; senão 404.
    """
    async def _check(request: Request, resource_id: str = Path(...), db: AsyncSession = Depends(get_db)):
        session = await get_current_session(request, db)
        if not session:
            raise HTTPException(401, "Não autenticado")
        
        # Mapeia resource_type → tabela + coluna owner
        table_map = {
            "simulation": ("simulations", "owner_user_id"),
            "invoice": ("invoices", "owner_user_id"),
            "client": ("clients", "owner_user_id"),
            "provider_profile": ("provider_profiles", "user_id"),
            "provider_bank_account": ("provider_bank_accounts", "user_id"),
        }
        table, owner_col = table_map[resource_type]
        
        query = f"SELECT * FROM {table} WHERE id = $1 AND {owner_col} = $2"
        resource = await db.fetchrow(query, resource_id, session.user_id)
        
        if not resource:
            raise HTTPException(404, "Recurso não encontrado")  # 404, não 403 (não vazar existência)
        return resource
    return _check
```

**Aplicação obrigatória em TODAS rotas de recurso:**
- `GET/PUT/DELETE /v1/simulations/{id}`
- `GET/POST/PUT/DELETE /v1/invoices/{id}`
- `GET/POST/PUT/DELETE /v1/clients/{id}`
- `GET/PUT /v1/provider/profile`
- `GET/POST/PUT/DELETE /v1/provider/bank-accounts/{id}`

---

## 6. Proteção CSRF (ADR-019 ST-04/ST-05)

**Implementação:** Double-submit cookie

```python
# Middleware (src/backend/middleware/csrf.py)
async def csrf_protect(request: Request):
    if request.method in ("POST", "PUT", "PATCH", "DELETE"):
        # Exceções: rotas stateless de auth
        if request.url.path.startswith("/v1/auth/"):
            return
        
        cookie_token = request.cookies.get("csrf_token")
        header_token = request.headers.get("X-CSRF-Token")
        
        if not cookie_token or not header_token:
            raise HTTPException(403, "CSRF token ausente")
        if not hmac.compare_digest(cookie_token, header_token):
            raise HTTPException(403, "CSRF token inválido")

# Login/set-cookie: gera csrf_token aleatório, seta cookie HttpOnly SameSite=Lax
# Frontend: lê cookie e envia header X-CSRF-Token em todas mutações
```

---

## 7. Rate Limiting (ADR-019 ST-01)

**Implementação:** `slowapi` ou middleware customizado com Redis/in-memory

| Escopo | Limite | Janela | Chave |
|--------|--------|--------|-------|
| Login | 5 req | 1 min | IP |
| Login | 10 req | 1 min | `user_id` (após resolução identificador) |
| Reset request | 3 req | 1 hora | identificador normalizado |
| Reset confirm | 5 req | 1 hora | token |
| API geral | 100 req | 1 min | `user_id` (sessão) |
| API geral | 20 burst | - | `user_id` |

---

## 8. SMTP Local / Autohospedado (CR2-D06)

- **Postfix + Dovecot** em container Docker (mesmo docker-compose da aplicação)
- **Apenas saída** (envio de reset de senha); sem entrada de email
- **Credenciais:** variáveis de ambiente (`SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`)
- **Template:** `templates/emails/password_reset_pt_br.html` (PT-BR apenas; erros API PT-BR)
- **From:** `noreply@cogme.local` (domínio local)
- **TLS:** STARTTLS obrigatório (certificado auto-assinado local)

---

## 9. Critérios de aceite e testes

- [ ] **AC-01:** Cadastro cria `users` + `user_login_identifiers` (email, CPF ou CNPJ) + `provider_profiles` (vazio) — transação atômica
- [ ] **AC-02:** Login aceita email, CPF ou CNPJ normalizados; resolve para mesmo `users.id`; regenera sessão; revoga anteriores
- [ ] **AC-03:** Senha hasheada com Argon2id (m=19456, t=2, p=1); `verify_password` funciona; tempo constante
- [ ] **AC-04:** Aliases `lookup_hmac` = HMAC-SHA256(pepper, normalized); pepper rotacionado 90d recalcula todos
- [ ] **AC-05:** Sessão: token 32 bytes; cookie `HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=86400`; sliding 24h
- [ ] **AC-06:** Reset senha: token TTL 1h; single-use (`used_at`); rate limit 3/h request, 5/h confirm; SMTP local envia email
- [ ] **AC-07:** Middleware `require_owner` em 100% rotas recurso; retorna 404 se não owner (não 403)
- [ ] **AC-08:** CSRF double-submit: cookie + header `X-CSRF-Token`; 403 se ausente/inválido; exceção rotas `/v1/auth/`
- [ ] **AC-09:** Rate limits aplicados conforme tabela §7; logs de segurança em tentativas bloqueadas
- [ ] **AC-10:** Dados bancários criptografados em repouso (`pgcrypto` AES-256-GCM); snapshot em invoice descriptografa
- [ ] **AC-11:** Testes de segurança ST-01..ST-10 (ADR-019) passam: brute force, session fixation, IDOR, CSRF, reset reuse/expiry, timing attack, log sanitization, alias rotation atomic

---

## 10. Rastreabilidade

| Referência | Fonte |
|------------|-------|
| CR-002 Gate C | `docs/decisoes/ccb-CR-002.md` (CR2-D06) |
| ADR-017 Argon2id | `docs/decisoes/adr-017-dependencia-argon2id.md` |
| ADR-019 Threat Model | `docs/decisoes/adr-019-seguranca-multiusuario.md` (ST-01..ST-10) |
| SPEC-022 (P-14, P-15, CP-1..CP-5) | `.ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md` |
| spec-prop-017 §12.1/§12.2 | `docs/especificacoes/spec-prop-017-conta-multiusuario.md` |
| Constitution v1.3.0 | `constitution.md` (Art. 1.2, P-14, P-15, Art. 7) |
| LGPD | art. 7º V, 16, 18 |

---

## 11. Fora de escopo (YAGNI)

- OAuth, SSO, MFA, federação de identidade, recuperação por SMS
- Equipes, organizações, papéis administrativos, painel admin
- Integração com provedores de identidade externos (Google, GitHub, etc.)
- Logs de auditoria detalhados além do `account_lifecycle_events` (futuro)
- Múltiplas sessões simultâneas por usuário (single-session por design)
- Expiração de senha forçada / rotação periódica (fora do MVP)

---

## 12. Metadados de emissão

- **Avaliador primário:** `agent-digital-security` + `agent-backend-dev`
- **Ratificação:** CCB/GP via CR-002 Gate C (2026-11-14)
- **Dependências:** SPEC-022 (Gate B), ADR-017, ADR-019
- **parcel.dod:** true
- **Data da emissão:** 2026-11-14
- **Status da spec:** ativa / ratificada

---

## CHANGELOG

| Versão | Data | Task/Handoff | Mudança |
|--------|------|--------------|---------|
| 1.0.0 | 2026-11-14 | CR-002 Gate C / agent-digital-security + agent-backend-dev | Emissão inicial, ratificada. Argon2id, HMAC aliases, sessão regenerada, reset 1h TTL, require_owner, CSRF, rate limit, SMTP local. |

---

## CAMADAS FUNDAMENTAIS — MAPA (TA-0031)

| Camada | Seção nesta spec | Estado |
|--------|------------------|--------|
| (a) cabeçalho | frontmatter (`spec_id: spec-017`, `version: 1.0.0`, `status: ratificada`) | aplicada |
| (b) Contexto/origem | §1 + frontmatter `origin`/`task` | aplicada |
| (c) Resolução de conflitos | §2 (8 conflitos resolvidos) | aplicada |
| (d) Corpo de decisões/requisitos/contratos | §3 (modelo dados), §4 (APIs), §5 (require_owner), §6 (CSRF), §7 (rate limit), §8 (SMTP) | aplicada |
| (e) Critérios de aceite/testes | §9 (AC-01..AC-11 + ST-01..ST-10) | aplicada |
| (f) Rastreabilidade | §10 + frontmatter `trace` | aplicada |
| (g) Fora de escopo (YAGNI) | §11 | aplicada |
| (h) Changelog | CHANGELOG | aplicada |