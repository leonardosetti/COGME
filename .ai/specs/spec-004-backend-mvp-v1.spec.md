---
id: ai-specs-spec-004-backend-mvp-v1-spec
title: SPEC spec-004 — backend-mvp-v1 — Backend do MVP COGME (REQ-01 a REQ-05, REQ-07, REQ-14, REQ-16, REQ-17)
type: spec
version: 2.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- constitution.md v1.3.0 (Art. 1.2, P-14, P-15, Art. 7, Art. 9.3.v)
- docs/decisoes/ccb-CR-002.md (CR2-D01..D09 ratificadas)
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-01..07)
- docs/decisoes/adr-017-dependencia-argon2id.md
- docs/decisoes/adr-018-tap-replanejamento-m4.md
- docs/decisoes/adr-019-seguranca-multiusuario.md
- .ai/specs/spec-002-requisitos-review-round-1.spec.md v2.0.0 (REQ-16, REQ-17, REQ-18)
- .ai/specs/spec-017-identity-access-session-v1.spec.md
- .ai/specs/spec-018-provider-profile-bank-account-v1.spec.md
- .ai/specs/spec-019-client-directory-v1.spec.md
- .ai/specs/spec-020-simulation-invoice-history-v1.spec.md
- .ai/specs/spec-021-invoice-bilingual-v1.spec.md
- .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md
last-revised: '2026-11-15'
lgpd-class: dados-pessoais
tags:
- specs
- docs
- adequado-a-norma
- backend
- mvp
- autenticacao
- multiusuario
---
---
spec_id: spec-004
specname: backend-mvp-v1
version: 2.0.0
status: ratificada
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-10-23
updated: 2026-11-15
origin: CR-002 Onda 1 (Emenda E-20 + ADR-017/018/019) — Emenda contratual para multiusuário, auth, persistência, autorização
task: TA-0031 | sender: agent-project-analyst | kill_switch: inherited
trace:
  - constitution.md v1.3.0 (E-20: Art. 1.2 escopo multiusuário, P-14 isolamento, P-15 LGPD/GDPR)
  - docs/decisoes/ccb-CR-002.md (CR2-D01..D09)
  - docs/decisoes/ccb-lgpd-decisoes.md (DEC-01..07)
  - docs/decisoes/adr-017-dependencia-argon2id.md
  - docs/decisoes/adr-018-tap-replanejamento-m4.md
  - docs/decisoes/adr-019-seguranca-multiusuario.md
  - .ai/specs/spec-002-requisitos-review-round-1.spec.md v2.0.0 (REQ-16, REQ-17, REQ-18)
  - .ai/specs/spec-017-identity-access-session-v1.spec.md
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md
lgpd-class: dados-pessoais
---

# SPEC spec-004 — backend-mvp-v1 — Backend do MVP COGME (REQ-01 a REQ-05, REQ-07, REQ-14, REQ-16, REQ-17)

**Status: RATIFICADA v2.0.0** — Emenda contratual para multiusuário (CR-002): autenticação, autorização, persistência, novos endpoints, contratos de erro atualizados.

---

## 1. Contexto e origem

Esta spec v2.0.0 emenda a spec-004 original (v1.1.0, 2026-11-05) para incorporar:
- **Emenda Constitucional E-20** (constitution.md v1.3.0): escopo expandido para identidade, contas multiusuário, prestadora/banco, clientes, histórico, invoice bilíngue, lifecycle conta
- **CR-002 Gates A/B/C/D ratificados**: autenticação (SPEC-017), autorização por proprietário (P-14), persistência de invoices/simulações (REQ-17), lifecycle (SPEC-022)
- **ADR-017**: Dependência `argon2-cffi` (Argon2id) para hash de senhas
- **ADR-018**: Replanejamento TAP/M4 → 30/12/2026, cenário A completo
- **ADR-019**: Threat model STRIDE + 10 testes ST-01..ST-10
- **SPEC-017, 022 ratificadas**: Contratos de identidade, sessão, lifecycle

**Mudança principal:** **Autenticação, cadastro, histórico de simulações e autorização SAEM de "fora de escopo" para DENTRO DO ESCOPO** (REQ-16, REQ-17). Contrato HTTP `POST /v1/simulate` mantido; novos endpoints para auth, recursos, invoices.

---

## 2. Resolução de conflitos

| Tema | Decisão v2.0.0 | Fonte vencedora | Texto superado |
|------|----------------|-----------------|----------------|
| **Autenticação/Cadastro** | **DENTRO DO ESCOPO** — REQ-16 (SPEC-017): register, login, logout, reset senha, sessão | Constitution v1.3.0 Art. 1.2 (E-20) + CR2-D01 | spec-004 v1.1 §1.3: "Autenticação, cadastro e histórico de simulações FORA DO ESCOPO" |
| **Persistência Invoices** | **PERSISTIDA** — REQ-17 (SPEC-020): invoices finalizadas salvas com snapshots, numeração, retenção 5a+6m | ADR-016 D4 (RAT-2026-11-05-A16-D4) + CR2-D03 | spec-004 v1.1 §6: "Invoice nunca é persistida" |
| **Persistência Simulações** | **OPT-IN** — REQ-17 (SPEC-020): simulações salvas apenas se usuário clicar "Salvar" | SPEC-020 §2.1 | spec-004 v1.1: "Histórico de simulações FORA DO ESCOPO" |
| **Autorização** | **P-14 ISOLAMENTO POR PROPRIETÁRIO** — `owner_user_id` obrigatório em TODOS recursos; middleware `require_owner` em 100% rotas; 404 cross-user | Constitution v1.3.0 P-14 + SPEC-017 §5 + SPEC-022 | Não existia (single-user local) |
| **Contrato Erro** | Atualizado para incluir códigos auth/autorização/validação multiusuário | SPEC-017 §4 + ADR-019 | Códigos originais apenas simulação/cotação |
| **Rate Limiting** | Obrigatório em auth (login/reset) e API geral | ADR-019 §7 + SPEC-017 §7 | Não definido |
| **CSRF Protection** | Double-submit cookie + header `X-CSRF-Token` em todas rotas mutáveis | ADR-019 §4.6 + SPEC-017 §6 | Não existia |

---

## 3. Arquitetura e Stack (Mantida + Extensões)

### 3.1 Stack Tecnológica

| Camada | Tecnologia | Versão | Observação |
|--------|------------|--------|------------|
| **API Framework** | FastAPI | 0.109+ | Async, OpenAPI automático |
| **ORM** | SQLAlchemy | 2.0+ | Async + PostgreSQL |
| **Banco** | PostgreSQL | 15+ | Via Docker Compose |
| **Migrações** | Alembic | 1.13+ | `upgrade`/`downgrade` testados |
| **Validação** | Pydantic | 2.5+ | v2, schemas por endpoint |
| **Auth/Hash** | `argon2-cffi` | 23.1+ | **NOVO** (ADR-017) Argon2id m=19456,t=2,p=1 |
| **Criptografia Banco** | `pgcrypto` (AES-256-GCM) | PostgreSQL ext | Dados bancários (SPEC-018) |
| **Cache** | In-memory (TTL) | Python stdlib | Cotações FX (REQ-07) |
| **PDF** | WeasyPrint | 60+ | HTML→PDF invoices |
| **Email** | `aiosmtplib` + Postfix/Dovecot local | 3.0+ | Reset senha SMTP local (CR2-D06) |
| **Rate Limit** | `slowapi` / custom middleware | 0.1.9+ | ADR-019 §7 |
| **CSRF** | Custom double-submit | Python stdlib | ADR-019 §4.6 |
| **Testes** | pytest + pytest-asyncio | 7.4+ | Coverage ≥ 80% (REQ-08) |

### 3.2 Containerização (ADR-010, Art. 10.1)

```yaml
# docker-compose.yml (resumo)
services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: cogme
      POSTGRES_USER: cogme
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./migrations:/migrations
    secrets:
      - db_password

  api:
    build: .
    depends_on: [postgres]
    environment:
      DATABASE_URL: postgresql+asyncpg://cogme:@postgres:5432/cogme
      LOGIN_PEPPER_FILE: /run/secrets/login_pepper
      SMTP_HOST: postfix
      SMTP_PORT: 25
      SMTP_USER_FILE: /run/secrets/smtp_user
      SMTP_PASS_FILE: /run/secrets/smtp_pass
    secrets:
      - db_password
      - login_pepper
      - smtp_user
      - smtp_pass

  postfix:
    image: boky/postfix:latest
    environment:
      SMTP_USER: ${SMTP_USER}
      SMTP_PASSWORD: ${SMTP_PASSWORD}
    secrets:
      - smtp_user
      - smtp_pass

secrets:
  db_password:
    file: ./secrets/db_password.txt
  login_pepper:
    file: ./secrets/login_pepper.txt
  smtp_user:
    file: ./secrets/smtp_user.txt
  smtp_pass:
    file: ./secrets/smtp_pass.txt

volumes:
  pgdata:
```

---

## 4. Contrato HTTP — Endpoints (Atualizado)

### 4.1 Simulação (Existente — Mantido)

| Endpoint | Método | Descrição | Auth | Rate Limit |
|----------|--------|-----------|------|------------|
| `/v1/simulate` | POST | Simulação cambial tempo real | Opcional (session se salvo) | 100/min/user |
| `/v1/fx/quote` | GET | Cotação atual (cache) | Pública | 100/min/IP |

### 4.2 Identidade e Autenticação (NOVO — SPEC-017)

| Endpoint | Método | Descrição | Auth | Rate Limit | Spec |
|----------|--------|-----------|------|------------|------|
| `/v1/auth/register` | POST | Cadastro (email, CPF/CNPJ, senha, nome) | Pública | 5/min/IP | SPEC-017 |
| `/v1/auth/login` | POST | Login (identificador + senha) | Pública | 5/min/IP, 10/min/user | SPEC-017 |
| `/v1/auth/logout` | POST | Logout (revoga sessão atual) | Cookie session | - | SPEC-017 |
| `/v1/auth/password/reset-request` | POST | Solicita reset (email/CPF/CNPJ) | Pública | 3/h/identificador | SPEC-017 |
| `/v1/auth/password/reset-confirm` | POST | Confirma reset (token + nova senha) | Pública | 5/h/token | SPEC-017 |
| `/v1/auth/me` | GET | Perfil usuário logado | Session | 100/min/user | SPEC-017 |
| `/v1/auth/aliases` | GET | Lista aliases ativos (tipo + mascarado) | Session | 100/min/user | SPEC-017 |
| `/v1/auth/aliases/cnpj` | PUT | Rotaciona alias CNPJ (mesma transação) | Session | 10/min/user | SPEC-017 |

### 4.3 Prestadora e Contas Bancárias (NOVO — SPEC-018)

| Endpoint | Método | Descrição | Auth | Rate Limit | Spec |
|----------|--------|-----------|------|------------|------|
| `/v1/provider/profile` | GET | Retorna perfil prestadora | `require_owner` | 100/min/user | SPEC-018 |
| `/v1/provider/profile` | PUT | Atualiza perfil (exceto category PJ) | `require_owner` | 10/min/user | SPEC-018 |
| `/v1/provider/bank-accounts` | GET | Lista contas (descriptografadas) | `require_owner` | 100/min/user | SPEC-018 |
| `/v1/provider/bank-accounts` | POST | Cria conta (criptografa sensíveis) | `require_owner` | 10/min/user | SPEC-018 |
| `/v1/provider/bank-accounts/{id}` | PUT | Atualiza conta | `require_owner` | 10/min/user | SPEC-018 |
| `/v1/provider/bank-accounts/{id}` | DELETE | Remove conta (não primária única) | `require_owner` | 10/min/user | SPEC-018 |

### 4.4 Clientes (NOVO — SPEC-019)

| Endpoint | Método | Descrição | Auth | Rate Limit | Spec |
|----------|--------|-----------|------|------------|------|
| `/v1/clients` | GET | Lista clientes (paginado, filtros) | `require_owner` | 100/min/user | SPEC-019 |
| `/v1/clients` | POST | Cadastra cliente | `require_owner` | 10/min/user | SPEC-019 |
| `/v1/clients/{id}` | GET | Detalha cliente | `require_owner` | 100/min/user | SPEC-019 |
| `/v1/clients/{id}` | PUT | Atualiza (exceto tax_id, owner) | `require_owner` | 10/min/user | SPEC-019 |
| `/v1/clients/{id}/deactivate` | POST | Inativa cliente | `require_owner` | 10/min/user | SPEC-019 |
| `/v1/clients/{id}/activate` | POST | Reativa cliente | `require_owner` | 10/min/user | SPEC-019 |

### 4.5 Simulações Salvas (NOVO — SPEC-020)

| Endpoint | Método | Descrição | Auth | Rate Limit | Spec |
|----------|--------|-----------|------|------------|------|
| `/v1/simulations` | GET | Lista simulações salvas (paginado) | `require_owner` | 100/min/user | SPEC-020 |
| `/v1/simulations` | POST | Salva simulação (opt-in) | `require_owner` | 10/min/user | SPEC-020 |
| `/v1/simulations/{id}` | GET | Detalha simulação + cotação snapshot | `require_owner` | 100/min/user | SPEC-020 |

### 4.6 Invoices (EMENDADO — SPEC-007 + SPEC-020)

| Endpoint | Método | Descrição | Auth | Rate Limit | Spec |
|----------|--------|-----------|------|------------|------|
| `/v1/invoices` | GET | Lista invoices (paginado, filtros) | `require_owner` | 100/min/user | SPEC-020 |
| `/v1/invoices` | POST | Cria invoice `draft` | `require_owner` | 10/min/user | SPEC-020 |
| `/v1/invoices/{id}` | GET | Detalha invoice (todos snapshots) | `require_owner` | 100/min/user | SPEC-020 |
| `/v1/invoices/{id}` | PUT | Atualiza invoice `draft` | `require_owner` | 10/min/user | SPEC-020 |
| `/v1/invoices/{id}/finalize` | POST | Finaliza invoice (draft→finalized) | `require_owner` | 10/min/user | SPEC-020 |
| `/v1/invoices/{id}/clone` | POST | Clona invoice (novo draft) | `require_owner` | 10/min/user | SPEC-020 |
| `/v1/invoices/{id}/download` | GET | Download PDF (locale snapshoteado) | `require_owner` | 20/min/user | SPEC-021 |

### 4.7 Lifecycle Conta (NOVO — SPEC-022)

| Endpoint | Método | Descrição | Auth | Rate Limit | Spec |
|----------|--------|-----------|------|------------|------|
| `/v1/account` | DELETE | Exclusão definitiva (agenda erase) | `require_owner` | 1/h/user | SPEC-022 |
| `/v1/account/reactivate` | POST | Reativação dormente (reset+verificação) | Session | 5/h/user | SPEC-022 |

---

## 5. Schemas de Request/Response (Pydantic v2)

### 5.1 Auth Schemas (`src/backend/schemas/auth.py`)

```python
# Register
class RegisterRequest(BaseModel):
    identifier: str  # email, CPF (11 dígitos) ou CNPJ (14 dígitos)
    password: str = Field(min_length=8, max_length=128)
    name: str = Field(min_length=1, max_length=255)

class RegisterResponse(BaseModel):
    user_id: UUID
    message: str = "Conta criada. Faça login."

# Login
class LoginRequest(BaseModel):
    identifier: str  # email, CPF ou CNPJ normalizado
    password: str

class LoginResponse(BaseModel):
    message: str = "Login realizado"
    # Token retornado via cookie HttpOnly

# Reset Request
class ResetRequestRequest(BaseModel):
    identifier: str  # email, CPF ou CNPJ

class ResetConfirmRequest(BaseModel):
    token: str
    new_password: str = Field(min_length=8, max_length=128)

# Aliases
class AliasResponse(BaseModel):
    kind: Literal["email", "cpf", "cnpj"]
    masked: str  # ex.: "jo***@example.com", "***.***.123-45", "**.***.***/0001-99"
```

### 5.2 Provider Schemas (`src/backend/schemas/provider.py`)

```python
class ProviderProfileRequest(BaseModel):
    legal_name: str = Field(min_length=1, max_length=255)
    category: Literal["mei", "legal_entity"]
    cnpj: str | None = Field(default=None, pattern=r"^\d{14}$")  # Obrigatório se PJ
    address: str | None = Field(default=None, max_length=500)
    city: str | None = Field(default=None, max_length=100)
    state: str | None = Field(default=None, pattern=r"^[A-Z]{2}$")
    postal_code: str | None = Field(default=None, pattern=r"^\d{8}$")
    country_code: str = Field(default="BR", pattern=r"^[A-Z]{2}$")

class BankAccountRequest(BaseModel):
    account_type: Literal["checking", "savings", "payment"]
    bank_code: str = Field(pattern=r"^\d{3}$")  # COMPE
    bank_name: str = Field(min_length=1, max_length=100)
    branch: str = Field(min_length=1, max_length=10)
    account_number: str = Field(min_length=1, max_length=20)
    account_digit: str = Field(min_length=1, max_length=2)
    swift_bic: str | None = Field(default=None, pattern=r"^[A-Z]{6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3})?$")
    iban: str | None = Field(default=None, max_length=34)
    account_holder: str = Field(min_length=1, max_length=255)
    currency: Literal["BRL", "USD", "EUR"] = "BRL"
    is_primary: bool = False
```

### 5.3 Client Schemas (`src/backend/schemas/client.py`)

```python
class ClientRequest(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    tax_id: str = Field(pattern=r"^\d{11}$|^\d{14}$")  # CPF ou CNPJ
    address: str | None = Field(default=None, max_length=500)
    country_code: str = Field(pattern=r"^[A-Z]{2}$")  # ISO 3166-1

class ClientFictitiousRequest(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    tax_id: str = Field(pattern=r"^\d{11}$|^\d{14}$")
    address: str | None = Field(default=None, max_length=500)
    country_code: str = Field(pattern=r"^[A-Z]{2}$")  # OBRIGATÓRIO (DEC-07)
```

### 5.4 Simulation Schemas (`src/backend/schemas/simulation.py`)

```python
class SimulationSaveRequest(BaseModel):
    currency: Literal["USD", "EUR", "GBP", "JPY", "CHF"]
    regime: Literal["hourly", "daily", "weekly", "monthly", "fixed"]
    amount: Decimal = Field(gt=0, max_digits=18, decimal_places=2)
    quantity: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    spread_pct: Decimal = Field(ge=0, le=100, max_digits=5, decimal_places=2)
    iof_pct: Decimal = Field(ge=0, le=100, max_digits=5, decimal_places=2)
    fx_quote_id: UUID  # Snapshot cotação (SPEC-020 resolve gap spec-007 §3.7.3)

class SimulationResponse(BaseModel):
    id: UUID
    currency: str
    regime: str
    amount: Decimal
    quantity: Decimal
    spread_pct: Decimal
    iof_pct: Decimal
    gross_foreign: Decimal
    gross_brl: Decimal
    spread_brl: Decimal
    iof_brl: Decimal
    net_brl: Decimal
    effective_rate: Decimal
    rate: Decimal
    rate_source: str
    quoted_at: datetime
    bulletin: str
    stale: bool
    created_at: datetime
```

### 5.5 Invoice Schemas (`src/backend/schemas/invoice.py`)

```python
class InvoiceCreateDraft(BaseModel):
    client_id: UUID | None = None  # None = cliente fictício
    client_fictitious: ClientFictitiousRequest | None = None  # Obrigatório se client_id=None
    simulation_id: UUID | None = None
    # Snapshots parciais aceitos no draft

class InvoiceFinalizeRequest(BaseModel):
    # Valida se todos snapshots completos

class InvoiceResponse(BaseModel):
    id: UUID
    owner_user_id: UUID
    client_id: UUID | None
    simulation_id: UUID | None
    status: Literal["draft", "finalized"]
    locale: Literal["pt-BR", "en"]
    client_country_code: str
    finalized_at: datetime | None
    supersedes_invoice_id: UUID | None
    number: str  # INV-{YYYYMM}-{SEQ:04d}
    issuer_snapshot: dict
    client_snapshot: dict
    bank_snapshot: dict
    simulation_snapshot: dict | None
    quote_snapshot: dict
    amounts_snapshot: dict
    notice_snapshot: str
    created_at: datetime
```

### 5.6 Error Schema Unificado (Atualizado)

```python
class ErrorResponse(BaseModel):
    error: str
    code: str  # Código estável para frontend
    details: dict | None = None
    trace_id: str  # Para correlação logs

# Códigos de erro NOVOS (multiusuário):
# AUTH_INVALID_CREDENTIALS, AUTH_SESSION_EXPIRED, AUTH_SESSION_REVOKED
# AUTH_RATE_LIMIT_LOGIN, AUTH_RATE_LIMIT_RESET
# AUTH_RESET_TOKEN_INVALID, AUTH_RESET_TOKEN_EXPIRED, AUTH_RESET_TOKEN_USED
# AUTH_CSRF_MISSING, AUTH_CSRF_INVALID
# AUTH_ALIAS_ROTATION_FAILED
# AUTHZ_RESOURCE_NOT_FOUND (404 cross-user)
# VALIDATION_COUNTRY_CODE_REQUIRED (cliente fictício)
# INVOICE_STATUS_IMMUTABLE (finalized não editável)
# INVOICE_NUMBER_CONFLICT
# ACCOUNT_DORMANT, ACCOUNT_DELETED
# PROVIDER_CNPJ_REQUIRED_FOR_PJ
```

---

## 6. Middleware de Autorização — `require_owner` (P-14)

**Localização:** `src/backend/middleware/authorization.py`

```python
from fastapi import Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

async def get_current_session(request: Request, db: AsyncSession = Depends(get_db)) -> SessionData | None:
    """Extrai e valida sessão do cookie; retorna SessionData ou None."""
    token = request.cookies.get("session")
    if not token:
        return None
    token_hash = hashlib.sha256((token + get_pepper()).encode()).digest()
    session = await db.fetchrow(
        "SELECT * FROM user_sessions WHERE token_hash = $1 AND revoked_at IS NULL AND expires_at > now()",
        token_hash
    )
    if not session:
        return None
    # Sliding expiration
    await db.execute(
        "UPDATE user_sessions SET last_seen_at = now() WHERE id = $1",
        session["id"]
    )
    return SessionData(user_id=session["user_id"], session_id=session["id"])

def require_owner(resource_type: str, resource_id_param: str = "id"):
    """Dependency FastAPI: valida owner_user_id do recurso."""
    resource_map = {
        "simulation": ("simulations", "owner_user_id"),
        "invoice": ("invoices", "owner_user_id"),
        "client": ("clients", "owner_user_id"),
        "provider_profile": ("provider_profiles", "user_id"),
        "provider_bank_account": ("provider_bank_accounts", "user_id"),
    }
    table, owner_col = resource_map[resource_type]
    
    async def _check(
        request: Request,
        resource_id: UUID = Path(..., alias=resource_id_param),
        db: AsyncSession = Depends(get_db),
        session: SessionData = Depends(get_current_session)
    ):
        if not session:
            raise HTTPException(401, "Não autenticado", headers={"WWW-Authenticate": "Cookie"})
        
        query = f"SELECT * FROM {table} WHERE id = $1 AND {owner_col} = $2"
        resource = await db.fetchrow(query, resource_id, session.user_id)
        
        if not resource:
            raise HTTPException(404, "Recurso não encontrado")  # 404, não 403
        return resource
    return _check
```

**Aplicação em TODAS rotas de recurso (SPEC-017 AC-07, ADR-019 ST-03):**
```python
# Exemplo uso:
@router.get("/v1/simulations/{simulation_id}")
async def get_simulation(simulation = Depends(require_owner("simulation"))):
    return SimulationResponse(**simulation)

@router.put("/v1/invoices/{invoice_id}")
async def update_invoice(
    data: InvoiceUpdate,
    invoice = Depends(require_owner("invoice", "invoice_id"))
):
    if invoice["status"] == "finalized":
        raise HTTPException(409, "Invoice finalizada é imutável", code="INVOICE_STATUS_IMMUTABLE")
    # ... update
```

---

## 7. Proteção CSRF (ADR-019 §4.6)

**Middleware:** `src/backend/middleware/csrf.py`

```python
CSRF_EXEMPT_PATHS = {"/v1/auth/register", "/v1/auth/login", "/v1/auth/logout",
                     "/v1/auth/password/reset-request", "/v1/auth/password/reset-confirm"}

async def csrf_protect(request: Request, call_next):
    if request.method in ("POST", "PUT", "PATCH", "DELETE"):
        if request.url.path not in CSRF_EXEMPT_PATHS:
            cookie_token = request.cookies.get("csrf_token")
            header_token = request.headers.get("X-CSRF-Token")
            if not cookie_token or not header_token:
                raise HTTPException(403, "CSRF token ausente", code="AUTH_CSRF_MISSING")
            if not hmac.compare_digest(cookie_token, header_token):
                raise HTTPException(403, "CSRF token inválido", code="AUTH_CSRF_INVALID")
    response = await call_next(request)
    # Seta cookie CSRF se não existe (login gera)
    if "csrf_token" not in request.cookies:
        response.set_cookie("csrf_token", generate_csrf_token(), httponly=True, secure=True, samesite="lax")
    return response
```

---

## 8. Rate Limiting (ADR-019 §7)

**Implementação:** `slowapi` com Redis/in-memory + custom keys

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address, default_limits=["100/minute"])

# Overrides por endpoint:
@router.post("/v1/auth/login")
@limiter.limit("5/minute", key_func=lambda r: get_remote_address(r))  # por IP
@limiter.limit("10/minute", key_func=lambda r: get_user_id_from_identifier(r))  # por user
async def login(...)

@router.post("/v1/auth/password/reset-request")
@limiter.limit("3/hour", key_func=lambda r: normalize_identifier(r.json().get("identifier")))
async def reset_request(...)
```

---

## 9. Contrato de Erro Atualizado

| Código HTTP | Code (estável) | Quando |
|-------------|----------------|--------|
| 400 | `VALIDATION_ERROR` | Pydantic validation fail |
| 400 | `VALIDATION_COUNTRY_CODE_REQUIRED` | Cliente fictício sem `country_code` |
| 401 | `AUTH_INVALID_CREDENTIALS` | Login/senha inválidos |
| 401 | `AUTH_SESSION_EXPIRED` | Sessão expirada |
| 401 | `AUTH_SESSION_REVOKED` | Sessão revogada (logout/outro login) |
| 403 | `AUTH_CSRF_MISSING` | Header `X-CSRF-Token` ausente |
| 403 | `AUTH_CSRF_INVALID` | Token CSRF inválido |
| 403 | `AUTH_RATE_LIMIT_LOGIN` | Rate limit login excedido |
| 403 | `AUTH_RATE_LIMIT_RESET` | Rate limit reset excedido |
| 403 | `AUTH_RESET_TOKEN_INVALID` | Token reset inválido |
| 403 | `AUTH_RESET_TOKEN_EXPIRED` | Token reset > 1h |
| 403 | `AUTH_RESET_TOKEN_USED` | Token reset já usado |
| 403 | `AUTH_ALIAS_ROTATION_FAILED` | Falha rotação CNPJ (transação) |
| 404 | `AUTHZ_RESOURCE_NOT_FOUND` | Owner check fail (cross-user) |
| 409 | `INVOICE_STATUS_IMMUTABLE` | PUT/PATCH/DELETE em invoice finalized |
| 409 | `INVOICE_NUMBER_CONFLICT` | Concorrência numeração (raro) |
| 409 | `PROVIDER_CNPJ_REQUIRED_FOR_PJ` | category=legal_entity sem CNPJ |
| 422 | `ACCOUNT_DORMANT` | Operação em conta dormente |
| 422 | `ACCOUNT_DELETED` | Operação em conta excluída |

---

## 10. Critérios de Aceite e Testes (v2.0.0)

### 10.1 Contrato HTTP

- [ ] **AC-HTTP-01:** `POST /v1/simulate` mantido compatível (não quebrado)
- [ ] **AC-HTTP-02:** Todos endpoints auth (register, login, logout, reset) funcionais
- [ ] **AC-HTTP-03:** Todos endpoints recurso usam `require_owner`; 404 cross-user
- [ ] **AC-HTTP-04:** Rate limits aplicados conforme tabela §4
- [ ] **AC-HTTP-05:** CSRF double-submit em todas rotas mutáveis (exceto `/v1/auth/`)
- [ ] **AC-HTTP-06:** Códigos de erro novos retornados corretamente

### 10.2 Autenticação e Sessão (SPEC-017)

- [ ] **AC-AUTH-01:** Cadastro cria `users` + `user_login_identifiers` + `provider_profiles` (transação)
- [ ] **AC-AUTH-02:** Login aceita email/CPF/CNPJ; regenera sessão; revoga anteriores
- [ ] **AC-AUTH-03:** Argon2id (m=19456,t=2,p=1); `verify_password` roundtrip; tempo constante
- [ ] **AC-AUTH-04:** Aliases HMAC-SHA256(pepper); pepper rotacionado 90d recalcula todos
- [ ] **AC-AUTH-05:** Sessão: token 32 bytes; cookie HttpOnly/Secure/SameSite=Lax; sliding 24h
- [ ] **AC-AUTH-06:** Reset senha: TTL 1h; single-use; rate limit 3/h request, 5/h confirm; SMTP local
- [ ] **AC-AUTH-07:** Testes ST-01..ST-10 (ADR-019) passam

### 10.3 Persistência e Autorização

- [ ] **AC-PERSIST-01:** Invoices finalizadas persistidas com snapshots completos + numeração
- [ ] **AC-PERSIST-02:** Simulações salvas apenas opt-in; `fx_quote_id` snapshot cotação
- [ ] **AC-PERSIST-03:** `owner_user_id` em TODAS tabelas recurso; FKs + índices
- [ ] **AC-PERSIST-04:** `require_owner` em 100% rotas recurso; teste IDOR cross-user (ST-03)

### 10.3 Segurança (ADR-019)

- [ ] **AC-SEC-01:** `argon2-cffi` build CI passa; fallback `bcrypt` documentado
- [ ] **AC-SEC-02:** Dados bancários `pgcrypto` AES-256-GCM; snapshot descriptografa
- [ ] **AC-SEC-03:** Logs sem PII/valores/corpo (SPEC-015 CP-2, ST-09)
- [ ] **AC-SEC-04:** SMTP local (Postfix/Dovecot container); reset email funcional

---

## 11. Rastreabilidade

| Referência | Fonte |
|------------|-------|
| Constitution v1.3.0 | `constitution.md` (Art. 1.2, P-14, P-15, Art. 7, Art. 9.3v) |
| CR-002 Gates | `docs/decisoes/ccb-CR-002.md` (CR2-D01..D09) |
| DEC-01..07 LGPD | `docs/decisoes/ccb-lgpd-decisoes.md` |
| ADR-017 Argon2id | `docs/decisoes/adr-017-dependencia-argon2id.md` |
| ADR-018 TAP/M4 | `docs/decisoes/adr-018-tap-replanejamento-m4.md` |
| ADR-019 Threat Model | `docs/decisoes/adr-019-seguranca-multiusuario.md` |
| SPEC-002 v2.0.0 | `.ai/specs/spec-002-requisitos-review-round-1.spec.md` (REQ-16/17/18) |
| SPEC-017, 022 | `.ai/specs/spec-017/022-*.spec.md` |
| SPEC-018/019/020/021 | `.ai/specs/spec-018/019/020/021-*.spec.md` |

---

## 12. Fora de Escopo (YAGNI) — Mantido

- OAuth, SSO, MFA, federação, recuperação SMS
- Equipes, orgs, papéis admin, painel admin
- NF-e/NFS-e, numeração fiscal, email automático
- i18n integral interface/erros
- Plataformas pagamento, Pix, escrow, multi-empresa
- Telemetria, cloud não autorizada (P-03)
- Múltiplas sessões simultâneas, expiração forçada senha

---

## 13. Metadados da Emenda

- **Avaliador primário:** `agent-sdd-specialist` + `agent-backend-dev` + `agent-digital-security`
- **Ratificação:** CCB/GP via CR-002 Onda 1 (2026-11-15)
- **Emenda:** v1.1.0 → v2.0.0 (MAJOR por escopo + auth/autorização/persistência)
- **parcel.dod:** true
- **Data da emenda:** 2026-11-15
- **Status da spec:** ativa / ratificada

---

## CHANGELOG

| Versão | Data | Task/Handoff | Mudança |
|--------|------|--------------|---------|
| 1.0.0 | 2026-10-23 | TA-0031 / agent-sdd-specialist | Emissão original: backend MVP, simulação, cotações, invoice PDF, cache |
| 1.1.0 | 2026-11-05 | RAT-2026-11-05-A16 / CCB | Emendas C.1+C.2 (conteúdo); ACs §11 preenchidas; §13 fora escopo; CHANGELOG |
| 2.0.0 | 2026-11-15 | CR-002 Onda 1 / agent-sdd-specialist + agent-backend-dev + agent-digital-security | **Emenda E-20 + CR-002**: Auth/cadastro/histórico SAEM fora escopo → DENTRO (REQ-16/17); P-14 isolamento; P-15 LGPD; Argon2id; require_owner; CSRF; rate limits; invoices persistidas; simulações opt-in; novos endpoints auth/recursos; contrato erro atualizado |

---

## CAMADAS FUNDAMENTAIS — MAPA (TA-0031)

| Camada | Seção nesta spec | Estado |
|--------|------------------|--------|
| (a) cabeçalho | frontmatter (`spec_id: spec-004`, `version: 2.0.0`, `status: ratificada`) | aplicada |
| (b) Contexto/origem | §1 + frontmatter `origin`/`task` | aplicada |
| (c) Resolução de conflitos | §2 (7 conflitos resolvidos) | aplicada |
| (d) Corpo de decisões/requisitos/contratos | §3 (stack), §4 (endpoints), §5 (schemas), §6 (require_owner), §7 (CSRF), §8 (rate limit), §9 (erros) | aplicada |
| (e) Critérios de aceite/testes | §10 (AC-HTTP, AC-AUTH, AC-PERSIST, AC-SEC) | aplicada |
| (f) Rastreabilidade | §11 + frontmatter `trace` | aplicada |
| (g) Fora de escopo (YAGNI) | §12 | aplicada |
| (h) Changelog | CHANGELOG | aplicada |