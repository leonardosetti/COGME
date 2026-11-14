---
id: ai-specs-spec-007-invoice-data-model-v1-spec
title: SPEC spec-007 — invoice-data-model-v1 — Modelo canônico de dados da invoice (GAP-04 + CR-002)
type: spec
version: 2.0.0
status: ativo
owner: agent-dba
derived-from:
- constitution.md v1.3.0 (Art. 1.2, P-14, P-15, Art. 7)
- docs/decisoes/ccb-CR-002.md (CR2-D01..D09 ratificadas)
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-01..07 ratificadas)
- docs/decisoes/adr-016-backend-mvp.md (D4 = persistir com erase)
- docs/decisoes/adr-018-tap-replanejamento-m4.md
- .ai/specs/spec-002-requisitos-review-round-1.spec.md v2.0.0 (REQ-16, REQ-17, REQ-18)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md v0.3.0 (D1-D7 ratificadas, CP-1..CP-5)
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
- invoice
- modelo-dados
- multiusuario
- lgpd
---
---
spec_id: spec-007
specname: invoice-data-model-v1
version: 2.0.0
status: ratificada
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-10-23
updated: 2026-11-15
origin: CR-002 Onda 1 (Emenda E-20 + ADR-016 D4 + DEC-01..07) — Emenda modelo canônico: owner, status, locale, FKs, snapshots, numeração, bilíngue, LGPD
task: TA-0031 | sender: agent-project-analyst | kill_switch: inherited
trace:
  - constitution.md v1.3.0 (E-20: Art. 1.2 escopo multiusuário, P-14 isolamento, P-15 LGPD/GDPR)
  - docs/decisoes/ccb-CR-002.md (CR2-D01..D09)
  - docs/decisoes/ccb-lgpd-decisoes.md (DEC-01..07)
  - docs/decisoes/adr-016-backend-mvp.md (D4 = persistir com erase, RAT-2026-11-05-A16-D4)
  - docs/decisoes/adr-018-tap-replanejamento-m4.md
  - .ai/specs/spec-002-requisitos-review-round-1.spec.md v2.0.0 (REQ-16, REQ-17, REQ-18)
  - .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md v0.3.0 (CP-1..CP-5 executáveis)
  - .ai/specs/spec-017-identity-access-session-v1.spec.md
  - .ai/specs/spec-018-provider-profile-bank-account-v1.spec.md
  - .ai/specs/spec-019-client-directory-v1.spec.md
  - .ai/specs/spec-020-simulation-invoice-history-v1.spec.md
  - .ai/specs/spec-021-invoice-bilingual-v1.spec.md
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md
lgpd-class: dados-pessoais
---

# SPEC spec-007 — invoice-data-model-v1 — Modelo canônico de dados da invoice (GAP-04 + CR-002)

**Status: RATIFICADA v2.0.0** — Emenda canônica para multiusuário (CR-002): `owner_user_id`, `status`, `locale`, `client_country_code`, FKs, snapshots completos, numeração `INV-{YYYYMM}-{SEQ:04d}`, bilíngue, LGPD/GDPR por design.

---

## 1. Contexto e origem

Esta spec v2.0.0 emenda a spec-007 original (v1.0.0, 2026-10-23) para incorporar:
- **Emenda Constitucional E-20** (constitution.md v1.3.0): escopo multiusuário, lifecycle conta, bilíngue
- **ADR-016 D4 ratificada** (RAT-2026-11-05-A16-D4): **Persistência de invoice** com rota erase obrigatória
- **CR-002 DEC-01..07 ratificadas** (ccb-lgpd-decisoes.md): base legal art. 7º V, minimização, retenção 5a+6m, draft/finalized/clone, numeração, bilíngue
- **SPEC-015 v0.3.0 ratificada**: CP-1..CP-5 executáveis (minimização, logs sem PII, erase, lgpd-class, limpeza E.1)
- **Specs derivadas ratificadas**: SPEC-017 (identidade), SPEC-018 (prestadora/banco), SPEC-019 (clientes), SPEC-020 (simulações/invoices), SPEC-021 (bilíngue), SPEC-022 (lifecycle/privacy)

**Mudança principal:** Modelo `invoices` **persistido** (não mais "nunca persistida" — supera spec-004:126), com isolamento por proprietário (P-14), snapshots imutáveis, numeração sequencial por emissor/mês, suporte a bilíngue e conformidade LGPD/GDPR.

---

## 2. Resolução de conflitos

| Tema | Decisão v2.0.0 | Fonte vencedora | Texto superado |
|------|----------------|-----------------|----------------|
| **Persistência invoice** | **PERSISTIDA** — tabela `invoices` com snapshots, numeração, retenção 5a+6m | ADR-016 D4 + CR2-D01/D03 | spec-004 v1.1 §6: "Invoice nunca é persistida" |
| **Isolamento por proprietário** | **OBRIGATÓRIO** — `owner_user_id` FK NOT NULL em `invoices`; P-14 | Constitution v1.3.0 P-14 + SPEC-017 | Single-user local (sem owner) |
| **Status invoice** | **draft / finalized** — draft editável, finalized imutável (fail-closed) | DEC-05 + SPEC-020 | Não existia (invoice única) |
| **Numeração** | **INV-{YYYYMM}-{SEQ:04d}** por emissor/mês (tabela `invoice_sequences`) | DEC-06 + SPEC-020 | Não definida |
| **Bilíngue** | **locale + client_country_code** snapshoteados; `BR`→pt-BR, demais→en | DEC-07 + SPEC-021 | Não existia |
| **Cliente** | `client_id` FK NULLABLE (NULL = fictício) + `client_snapshot` JSONB | SPEC-019 + SPEC-020 | Cliente apenas no template |
| **Prestadora/Banco** | `issuer_snapshot` + `bank_snapshot` JSONB (descriptografado no snapshot) | SPEC-018 | Apenas no template |
| **Simulação** | `simulation_id` FK NULLABLE + `simulation_snapshot` + `quote_snapshot` | SPEC-020 (resolve gap §3.7.3) | Não persistida |
| **Cotação snapshot** | `quote_snapshot` JSONB completo (rate, source, quoted_at, bulletin, stale) | SPEC-020 §2.1 (gap spec-007 §3.7.3) | Gap declarado: "cotação não snapshoteada" |
| **Valores snapshot** | `amounts_snapshot` JSONB (gross_foreign, gross_brl, spread_brl, iof_brl, net_brl, effective_rate) | SPEC-020 | Não persistidos |
| **Notice legal** | `notice_snapshot` TEXT (locale da invoice) | SPEC-021 | Hardcoded no template |
| **Retenção/Erase** | 5 anos + 6 meses → anonimização irreversível → hard delete; backup cleanup 30d | DEC-04 + SPEC-022 | Não definida |
| **LGPD Minimização** | Endereço/bancários **NULLable** (DEC-03); `lgpd-class: dados-pessoais` | DEC-03 + SPEC-015 CP-1/CP-4 | Campos obrigatórios |
| **Base legal** | **art. 7º V LGPD** (execução contrato) — invoice carrega dados de terceiros/cliente | DEC-01/02 | Não definida |

---

## 3. Modelo de Dados — Tabela `invoices` (v2.0.0)

### 3.1 Schema Completo (PostgreSQL)

```sql
-- Tabela principal invoices (emenda v2.0.0)
CREATE TABLE invoices (
    -- Identidade
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    owner_user_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,  -- P-14, retenção 5a+6m
    number VARCHAR(30) NOT NULL,  -- INV-{YYYYMM}-{SEQ:04d}
    
    -- Relacionamentos (FKs)
    client_id UUID REFERENCES clients(id) ON DELETE SET NULL,  -- NULL = cliente fictício
    simulation_id UUID REFERENCES simulations(id) ON DELETE SET NULL,
    
    -- Estado
    status VARCHAR(20) NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'finalized')),
    locale VARCHAR(10) NOT NULL CHECK (locale IN ('pt-BR', 'en')),
    client_country_code CHAR(2) NOT NULL,  -- Fonte canônica locale (DEC-07)
    finalized_at TIMESTAMPTZ,  -- NOT NULL se status = 'finalized'
    supersedes_invoice_id UUID REFERENCES invoices(id) ON DELETE SET NULL,  -- Clone
    
    -- Snapshots imutáveis (JSONB)
    issuer_snapshot JSONB NOT NULL,      -- Prestadora no momento
    client_snapshot JSONB NOT NULL,      -- Cliente (cadastrado ou fictício)
    bank_snapshot JSONB NOT NULL,        -- Dados bancários descriptografados
    simulation_snapshot JSONB,           -- Parâmetros + resultado simulação (opcional)
    quote_snapshot JSONB NOT NULL,       -- Cotação completa (resolve gap §3.7.3)
    amounts_snapshot JSONB NOT NULL,     -- Valores calculados
    notice_snapshot TEXT NOT NULL,       -- Notice legal no locale da invoice
    
    -- Auditoria
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    
    -- Constraints
    CONSTRAINT uq_owner_number UNIQUE (owner_user_id, number),
    CONSTRAINT chk_finalized CHECK (
        (status = 'finalized' AND finalized_at IS NOT NULL) OR
        (status = 'draft' AND finalized_at IS NULL)
    )
);

-- Índices
CREATE INDEX ix_invoices_owner_user_id ON invoices(owner_user_id);
CREATE INDEX ix_invoices_status ON invoices(status);
CREATE INDEX ix_invoices_client_id ON invoices(client_id);
CREATE INDEX ix_invoices_simulation_id ON invoices(simulation_id);
CREATE INDEX ix_invoices_finalized_at ON invoices(finalized_at) WHERE finalized_at IS NOT NULL;
CREATE INDEX ix_invoices_client_country_code ON invoices(client_country_code);
CREATE INDEX ix_invoices_supersedes ON invoices(supersedes_invoice_id);

-- Trigger updated_at
CREATE TRIGGER trg_invoices_updated_at
    BEFORE UPDATE ON invoices
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

### 3.2 Tabela `invoice_sequences` (Numeração DEC-06)

```sql
CREATE TABLE invoice_sequences (
    issuer_tax_id_digits CHAR(14) NOT NULL,  -- CNPJ da prestadora (14 dígitos)
    year_month CHAR(7) NOT NULL,             -- '2026-11'
    last_number INT NOT NULL DEFAULT 0,
    PRIMARY KEY (issuer_tax_id_digits, year_month)
);

-- Function atômica para próxima numeração
CREATE OR REPLACE FUNCTION next_invoice_number(p_issuer_tax_id CHAR(14))
RETURNS TEXT AS $$
DECLARE
    v_ym CHAR(7) := to_char(now(), 'YYYY-MM');
    v_seq INT;
BEGIN
    LOOP
        UPDATE invoice_sequences
        SET last_number = last_number + 1
        WHERE issuer_tax_id_digits = p_issuer_tax_id AND year_month = v_ym
        RETURNING last_number INTO v_seq;
        
        IF FOUND THEN
            RETURN 'INV-' || replace(v_ym, '-', '') || '-' || lpad(v_seq::text, 4, '0');
        END IF;
        
        -- Primeira invoice do emissor/mês
        INSERT INTO invoice_sequences (issuer_tax_id_digits, year_month, last_number)
        VALUES (p_issuer_tax_id, v_ym, 1)
        ON CONFLICT DO NOTHING;
    END LOOP;
END;
$$ LANGUAGE plpgsql VOLATILE;
```

---

## 4. Estrutura dos Snapshots (JSONB)

### 4.1 `issuer_snapshot` (Prestadora)

```json
{
  "legal_name": "Empresa Exemplo Ltda",
  "category": "legal_entity",
  "cnpj": "12345678000199",
  "address": "Av. Principal, 100 - Centro",
  "city": "São Paulo",
  "state": "SP",
  "postal_code": "01000000",
  "country_code": "BR"
}
```

### 4.2 `client_snapshot` (Cliente — cadastrado ou fictício)

```json
{
  "name": "Cliente Exemplo S.A.",
  "tax_id": "98765432000199",
  "address": "Rua das Flores, 50 - Jardins",
  "country_code": "BR"
}
```
> **Nota:** `address` pode ser `null` (DEC-03 minimização). `country_code` **SEMPRE presente** (NOT NULL, fonte canônica locale).

### 4.3 `bank_snapshot` (Dados Bancários — descriptografados para snapshot)

```json
{
  "bank_code": "001",
  "bank_name": "Banco do Brasil S.A.",
  "branch": "1234-5",
  "account_number": "123456",
  "account_digit": "7",
  "account_holder": "Empresa Exemplo Ltda",
  "currency": "BRL",
  "swift_bic": "BRASBRRJ",
  "iban": null
}
```
> **Origem:** Descriptografado de `provider_bank_accounts` (pgcrypto) no momento da finalização.

### 4.4 `simulation_snapshot` (Parâmetros + Resultado)

```json
{
  "currency": "USD",
  "regime": "hourly",
  "amount": "1000.00",
  "quantity": "160.00",
  "spread_pct": "2.50",
  "iof_pct": "1.10",
  "gross_foreign": "1000.00",
  "gross_brl": "5200.00",
  "spread_brl": "130.00",
  "iof_brl": "57.20",
  "net_brl": "5012.80",
  "effective_rate": "5.0128",
  "rate": "5.0000",
  "rate_source": "PTAX",
  "quoted_at": "2026-11-15T10:30:00Z",
  "bulletin": "PTAX 2026-11-15",
  "stale": false
}
```

### 4.5 `quote_snapshot` (Cotação Completa — resolve gap §3.7.3)

```json
{
  "rate": "5.0000",
  "rate_source": "PTAX",
  "quoted_at": "2026-11-15T10:30:00Z",
  "bulletin": "PTAX 2026-11-15",
  "stale": false,
  "fx_quote_id": "uuid-da-fx_quotes"
}
```

### 4.6 `amounts_snapshot` (Valores Calculados)

```json
{
  "gross_foreign": "1000.00",
  "gross_brl": "5200.00",
  "spread_brl": "130.00",
  "iof_brl": "57.20",
  "net_brl": "5012.80",
  "effective_rate": "5.0128"
}
```

### 4.7 `notice_snapshot` (Notice Legal por Locale)

**PT-BR:**
```
Este documento é uma invoice de prestação de serviços, emitida conforme legislação brasileira vigente. Os valores apresentados incluem spread cambial e IOF conforme informados pelo usuário. A taxa de câmbio refere-se à cotação PTAX de 15/11/2026 (boletim PTAX 2026-11-15). Este documento não substitui nota fiscal eletrônica (NF-e/NFS-e) quando exigida por lei.
```

**EN:**
```
This document is a service invoice issued under applicable Brazilian legislation. Amounts include foreign exchange spread and IOF as informed by the user. The exchange rate refers to PTAX quotation dated 11/15/2026 (bulletin PTAX 2026-11-15). This document does not replace electronic fiscal invoice (NF-e/NFS-e) when required by law.
```

---

## 5. Tabelas Relacionadas (Referência)

### 5.1 `users` (SPEC-017)

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    internal_username_hash BYTEA NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20),
    cpf CHAR(11) NOT NULL UNIQUE,  -- IMMUTABLE
    password_hash TEXT NOT NULL,    -- Argon2id
    status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (status IN ('active','dormant')),
    dormant_since TIMESTAMPTZ,
    last_login_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

### 5.2 `clients` (SPEC-019)

```sql
CREATE TABLE clients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    owner_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    tax_id VARCHAR(20) NOT NULL,  -- CPF 11 dígitos ou CNPJ 14 dígitos
    address TEXT,  -- NULLable (DEC-03)
    country_code CHAR(2) NOT NULL DEFAULT 'BR',  -- ISO 3166-1
    is_active BOOLEAN NOT NULL DEFAULT true,
    deactivated_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (owner_user_id, tax_id)
);
```

### 5.3 `simulations` (SPEC-020)

```sql
CREATE TABLE simulations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    owner_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    currency CHAR(3) NOT NULL,
    regime VARCHAR(20) NOT NULL CHECK (regime IN ('hourly','daily','weekly','monthly','fixed')),
    amount NUMERIC(18,2) NOT NULL,
    quantity NUMERIC(10,2) NOT NULL,
    spread_pct NUMERIC(5,2) NOT NULL,
    iof_pct NUMERIC(5,2) NOT NULL,
    gross_foreign NUMERIC(18,2) NOT NULL,
    gross_brl NUMERIC(18,2) NOT NULL,
    spread_brl NUMERIC(18,2) NOT NULL,
    iof_brl NUMERIC(18,2) NOT NULL,
    net_brl NUMERIC(18,2) NOT NULL,
    effective_rate NUMERIC(18,6) NOT NULL,
    rate NUMERIC(18,6) NOT NULL,
    rate_source VARCHAR(50) NOT NULL,
    quoted_at TIMESTAMPTZ NOT NULL,
    bulletin VARCHAR(50) NOT NULL,
    stale BOOLEAN NOT NULL DEFAULT false,
    fx_quote_id UUID REFERENCES fx_quotes(id) ON DELETE SET NULL,  -- Snapshot cotação
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

### 5.4 `provider_profiles` + `provider_bank_accounts` (SPEC-018)

Ver SPEC-018 §2.1/§2.2 — `provider_bank_accounts` usa `pgcrypto` AES-256-GCM para campos sensíveis.

### 5.5 `fx_quotes` (Existente — Inalterada)

```sql
CREATE TABLE fx_quotes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    currency CHAR(3) NOT NULL,
    rate NUMERIC(18,6) NOT NULL,
    source VARCHAR(50) NOT NULL,
    quoted_at TIMESTAMPTZ NOT NULL,
    bulletin VARCHAR(50) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (currency, source, quoted_at)
);
```

---

## 6. Migração (Alembic) — `upgrade`/`downgrade`

### 6.1 `upgrade()` — Adiciona colunas e tabelas novas

```python
def upgrade():
    # 1. Tabela invoice_sequences
    op.create_table(
        'invoice_sequences',
        sa.Column('issuer_tax_id_digits', sa.CHAR(14), nullable=False),
        sa.Column('year_month', sa.CHAR(7), nullable=False),
        sa.Column('last_number', sa.Integer(), nullable=False, server_default='0'),
        sa.PrimaryKeyConstraint('issuer_tax_id_digits', 'year_month')
    )
    
    # 2. Function next_invoice_number (raw SQL)
    op.execute("""
        CREATE OR REPLACE FUNCTION next_invoice_number(p_issuer_tax_id CHAR(14))
        RETURNS TEXT AS $$ ... $$ LANGUAGE plpgsql VOLATILE;
    """)
    
    # 3. Adiciona colunas em invoices
    with op.batch_alter_table('invoices') as batch:
        batch.add_column(sa.Column('owner_user_id', sa.UUID(), nullable=False))
        batch.add_column(sa.Column('client_id', sa.UUID(), nullable=True))
        batch.add_column(sa.Column('simulation_id', sa.UUID(), nullable=True))
        batch.add_column(sa.Column('status', sa.String(20), nullable=False, server_default='draft'))
        batch.add_column(sa.Column('locale', sa.String(10), nullable=False))
        batch.add_column(sa.Column('client_country_code', sa.CHAR(2), nullable=False))
        batch.add_column(sa.Column('finalized_at', sa.DateTime(timezone=True), nullable=True))
        batch.add_column(sa.Column('supersedes_invoice_id', sa.UUID(), nullable=True))
        batch.add_column(sa.Column('number', sa.String(30), nullable=False))
        batch.add_column(sa.Column('issuer_snapshot', sa.JSONB(), nullable=False))
        batch.add_column(sa.Column('client_snapshot', sa.JSONB(), nullable=False))
        batch.add_column(sa.Column('bank_snapshot', sa.JSONB(), nullable=False))
        batch.add_column(sa.Column('simulation_snapshot', sa.JSONB(), nullable=True))
        batch.add_column(sa.Column('quote_snapshot', sa.JSONB(), nullable=False))
        batch.add_column(sa.Column('amounts_snapshot', sa.JSONB(), nullable=False))
        batch.add_column(sa.Column('notice_snapshot', sa.Text(), nullable=False))
    
    # 4. FKs e constraints
    op.create_foreign_key('fk_invoices_owner_user_id', 'invoices', 'users', ['owner_user_id'], ['id'], ondelete='RESTRICT')
    op.create_foreign_key('fk_invoices_client_id', 'invoices', 'clients', ['client_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('fk_invoices_simulation_id', 'invoices', 'simulations', ['simulation_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('fk_invoices_supersedes', 'invoices', 'invoices', ['supersedes_invoice_id'], ['id'], ondelete='SET NULL')
    op.create_unique_constraint('uq_owner_number', 'invoices', ['owner_user_id', 'number'])
    op.create_check_constraint('chk_invoice_finalized', 'invoices', 
        "(status = 'finalized' AND finalized_at IS NOT NULL) OR (status = 'draft' AND finalized_at IS NULL)")
    op.create_check_constraint('chk_invoice_status', 'invoices', "status IN ('draft', 'finalized')")
    op.create_check_constraint('chk_invoice_locale', 'invoices', "locale IN ('pt-BR', 'en')")
    
    # 5. Índices
    op.create_index('ix_invoices_owner_user_id', 'invoices', ['owner_user_id'])
    op.create_index('ix_invoices_status', 'invoices', ['status'])
    op.create_index('ix_invoices_client_id', 'invoices', ['client_id'])
    op.create_index('ix_invoices_simulation_id', 'invoices', ['simulation_id'])
    op.create_index('ix_invoices_finalized_at', 'invoices', ['finalized_at'], postgresql_where=sa.text("finalized_at IS NOT NULL"))
    op.create_index('ix_invoices_client_country_code', 'invoices', ['client_country_code'])
    op.create_index('ix_invoices_supersedes', 'invoices', ['supersedes_invoice_id'])
```

### 6.2 `downgrade()` — Remove colunas e tabelas (reversível)

```python
def downgrade():
    # Drop índices
    op.drop_index('ix_invoices_supersedes', table_name='invoices')
    op.drop_index('ix_invoices_client_country_code', table_name='invoices')
    op.drop_index('ix_invoices_finalized_at', table_name='invoices')
    op.drop_index('ix_invoices_simulation_id', table_name='invoices')
    op.drop_index('ix_invoices_client_id', table_name='invoices')
    op.drop_index('ix_invoices_owner_user_id', table_name='invoices')
    
    # Drop constraints
    op.drop_constraint('chk_invoice_locale', 'invoices', type_='check')
    op.drop_constraint('chk_invoice_status', 'invoices', type_='check')
    op.drop_constraint('chk_invoice_finalized', 'invoices', type_='check')
    op.drop_constraint('uq_owner_number', 'invoices', type_='unique')
    op.drop_constraint('fk_invoices_supersedes', 'invoices', type_='foreignkey')
    op.drop_constraint('fk_invoices_simulation_id', 'invoices', type_='foreignkey')
    op.drop_constraint('fk_invoices_client_id', 'invoices', type_='foreignkey')
    op.drop_constraint('fk_invoices_owner_user_id', 'invoices', type_='foreignkey')
    
    # Drop colunas
    with op.batch_alter_table('invoices') as batch:
        batch.drop_column('notice_snapshot')
        batch.drop_column('amounts_snapshot')
        batch.drop_column('quote_snapshot')
        batch.drop_column('simulation_snapshot')
        batch.drop_column('bank_snapshot')
        batch.drop_column('client_snapshot')
        batch.drop_column('issuer_snapshot')
        batch.drop_column('number')
        batch.drop_column('supersedes_invoice_id')
        batch.drop_column('finalized_at')
        batch.drop_column('client_country_code')
        batch.drop_column('locale')
        batch.drop_column('status')
        batch.drop_column('simulation_id')
        batch.drop_column('client_id')
        batch.drop_column('owner_user_id')
    
    # Drop function e tabela sequences
    op.execute("DROP FUNCTION IF EXISTS next_invoice_number(CHAR(14))")
    op.drop_table('invoice_sequences')
```

---

## 7. Retenção e Eliminação (DEC-04, SPEC-022)

| Dado | Retenção Primária | Pós-Contrato | Eliminação |
|------|------------------|--------------|------------|
| `invoices` (finalized) | 5 anos (art. 206 §5º CC) | + 6 meses após última invoice do cliente | Job anonimização → hard delete |
| `invoices` (draft) | Enquanto conta ativa | Hard delete na exclusão conta | Cascade ON DELETE |
| `invoice_sequences` | Indeterminado (metadado numérico) | Mantido para auditoria | Não eliminado |
| Snapshots (JSONB) | Mesmo período da invoice | Anonimização: PII → HASH/ANONIMIZADO/NULL | Mantém valores/numeração |

**Job Anonimização Diário (SPEC-022 §3.2):**
```sql
-- Pseudocódigo do job
UPDATE invoices SET
    issuer_snapshot = jsonb_set(issuer_snapshot, '{legal_name}', '"ANONIMIZADO"'),
    issuer_snapshot = jsonb_set(issuer_snapshot, '{cnpj}', '"HASH_' || md5(issuer_snapshot->>'cnpj') || '"'),
    client_snapshot = jsonb_set(client_snapshot, '{name}', '"ANONIMIZADO"'),
    client_snapshot = jsonb_set(client_snapshot, '{tax_id}', '"HASH_' || md5(client_snapshot->>'tax_id') || '"'),
    client_snapshot = jsonb_set(client_snapshot, '{address}', 'null'),
    bank_snapshot = jsonb_set(bank_snapshot, '{account_number}', 'null'),
    bank_snapshot = jsonb_set(bank_snapshot, '{account_digit}', 'null'),
    bank_snapshot = jsonb_set(bank_snapshot, '{swift_bic}', 'null'),
    bank_snapshot = jsonb_set(bank_snapshot, '{iban}', 'null')
WHERE status = 'finalized'
  AND finalized_at < now() - interval '5 years 6 months'
  AND issuer_snapshot->>'legal_name' != 'ANONIMIZADO';  -- Idempotente
```

---

## 8. Critérios de Aceite e Testes (v2.0.0)

- [ ] **AC-MODEL-01:** Tabela `invoices` com todas colunas v2.0.0; FKs, constraints, índices criados
- [ ] **AC-MODEL-02:** `invoice_sequences` + `next_invoice_number()` function atômica; concorrência testada
- [ ] **AC-MODEL-03:** Numeração `INV-{YYYYMM}-{SEQ:04d}` única por `owner_user_id` + mês; teste 2 finalizações simultâneas
- [ ] **AC-MODEL-04:** Snapshots JSONB completos (issuer, client, bank, simulation, quote, amounts, notice) na finalização
- [ ] **AC-MODEL-05:** `quote_snapshot` inclui `fx_quote_id` + cotação completa (resolve gap §3.7.3)
- [ ] **AC-MODEL-06:** `client_country_code` + `locale` snapshoteados; `BR`→pt-BR, demais→en (DEC-07)
- [ ] **AC-MODEL-07:** `status` draft/finalized + `finalized_at` + constraint chk_finalized; finalized imutável (409)
- [ ] **AC-MODEL-08:** Clone: novo draft com `supersedes_invoice_id`; novo número na finalização
- [ ] **AC-MODEL-09:** Endereço/bancários NULLable nas tabelas origem; minimização DEC-03 atendida
- [ ] **AC-MODEL-10:** Migração `upgrade`/`downgrade` testadas; reversíveis sem perda de dados
- [ ] **AC-MODEL-11:** Retenção 5a+6m + job anonimização + backup cleanup 30d (SPEC-022)
- [ ] **AC-MODEL-12:** `lgpd-class: dados-pessoais` no frontmatter desta spec (CP-4)

---

## 9. Rastreabilidade

| Referência | Fonte |
|------------|-------|
| Constitution v1.3.0 | `constitution.md` (Art. 1.2, P-14, P-15, Art. 7, Art. 9.3v) |
| CR-002 DEC-01..07 | `docs/decisoes/ccb-lgpd-decisoes.md` |
| ADR-016 D4 | `docs/decisoes/adr-016-backend-mvp.md` (RAT-2026-11-05-A16-D4) |
| ADR-018 | `docs/decisoes/adr-018-tap-replanejamento-m4.md` |
| SPEC-002 v2.0.0 | `.ai/specs/spec-002-requisitos-review-round-1.spec.md` (REQ-16/17/18) |
| SPEC-015 v0.3.0 | `.ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md` (CP-1..CP-5) |
| SPEC-017, 018, 019, 020, 021, 022 | `.ai/specs/spec-017/018/019/020/021/022-*.spec.md` |
| LGPD art. 7º V, 16, 18 | Base legal, minimização, erase |

---

## 10. Fora de Escopo (YAGNI)

- NF-e/NFS-e, numeração fiscal oficial, envio automático email
- Histórico de alterações de invoice (auditoria) — apenas `supersedes_invoice_id` para clone
- Múltiplas moedas na mesma invoice (uma moeda por invoice)
- Versionamento de invoice além de draft/finalized/clone
- Templates de invoice por regime de contratação (um template por locale)

---

## 11. Metadados da Emenda

- **Avaliador primário:** `agent-dba` + `agent-sdd-specialist`
- **Ratificação:** CCB/GP via CR-002 Onda 1 (2026-11-15)
- **Emenda:** v1.0.0 → v2.0.0 (MAJOR por persistência, owner, status, numeração, bilíngue, LGPD)
- **parcel.dod:** true
- **Data da emenda:** 2026-11-15
- **Status da spec:** ativa / ratificada

---

## CHANGELOG

| Versão | Data | Task/Handoff | Mudança |
|--------|------|--------------|---------|
| 1.0.0 | 2026-10-23 | TA-0031 / agent-sdd-specialist | Emissão original: modelo canônico invoice (GAP-04), campos, snapshots parciais, gap cotação §3.7.3 |
| 2.0.0 | 2026-11-15 | CR-002 Onda 1 / agent-dba + agent-sdd-specialist | **Emenda E-20 + CR-002**: Persistência invoice (ADR-016 D4); owner_user_id (P-14); status draft/finalized; locale+client_country_code (bilíngue DEC-07); numeração INV-{YYYYMM}-{SEQ} (DEC-06); FKs client/simulation; snapshots completos (issuer, client, bank, simulation, quote, amounts, notice); quote_snapshot resolve gap §3.7.3; retenção 5a+6m + anonimização (DEC-04); endereço/bancários NULLable (DEC-03); base legal art. 7º V (DEC-01/02); migração upgrade/downgrade; lgpd-class. |

---

## CAMADAS FUNDAMENTAIS — MAPA (TA-0031)

| Camada | Seção nesta spec | Estado |
|--------|------------------|--------|
| (a) cabeçalho | frontmatter (`spec_id: spec-007`, `version: 2.0.0`, `status: ratificada`) | aplicada |
| (b) Contexto/origem | §1 + frontmatter `origin`/`task` | aplicada |
| (c) Resolução de conflitos | §2 (15 conflitos resolvidos) | aplicada |
| (d) Corpo de decisões/requisitos/contratos | §3 (schema SQL), §4 (snapshots JSONB), §5 (tabelas relacionadas), §6 (migração), §7 (retenção/erase) | aplicada |
| (e) Critérios de aceite/testes | §8 (AC-MODEL-01..12) | aplicada |
| (f) Rastreabilidade | §9 + frontmatter `trace` | aplicada |
| (g) Fora de escopo (YAGNI) | §10 | aplicada |
| (h) Changelog | CHANGELOG | aplicada |