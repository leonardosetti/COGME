---
id: docs-decisoes-ratificacao-ccb-invoices-2026-11-14
title: Ratificação CCB/GP — Persistência de Invoices + LGPD (DEC-04 a DEC-07)
type: adr
version: 1.0.0
status: ratificado
owner: agent-project-analyst
derived-from:
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-04 a DEC-07)
- docs/analise/RELATORIO-PERSISTENCIA-RECUPERACAO-INVOICES-2026-11-14.md
- constitution.md (Art. 5.1, 5.4, 9.3)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- ccb
- lgpd
- invoices
- persistência
- erase
- bilíngue
- numeração
---

# Ratificação CCB/GP — Persistência de Invoices + LGPD (DEC-04 a DEC-07)

**Data da sessão:** 2026-11-14  
**Participantes:** Gerente de Projeto — CCB de membro único  
**Instrumento:** Prompt expresso CCB — ratificação única consolidada  
**Base:** DEC-04 a DEC-07 ratificados em `docs/decisoes/ccb-lgpd-decisoes.md` (continuação RAT-2026-11-14-E20)  
**Referência técnica:** Opção A (Snapshot Completo) do `RELATORIO-PERSISTENCIA-RECUPERACAO-INVOICES-2026-11-14.md` §4

---

## Decisões Consolidadas (4 Ratificações → 1 Instrumento)

| DEC | Decisão | Fundamento Resumido | Status |
|-----|---------|---------------------|--------|
| **DEC-04** | Retenção **5a + 6m** + **DELETE hard** `/v1/invoices/{id}` + backup 30d | Art. 206 §5º CC + LGPD art. 18, VI | **RATIFICADA** |
| **DEC-05** | Ciclo **draft/finalized** + **clone** (`supersedes_invoice_id`) — CR6-D01 | Fluxo real rascunho→emissão; imutabilidade fiscal | **RATIFICADA** |
| **DEC-06** | Numeração **`INV-{YYYYMM}-{SEQ:04d}`** por emissor/mês (tabela `invoice_sequences`) | Legível, auditável, sem gap, atende C-04 | **RATIFICADA** |
| **DEC-07** | Bilíngue **país→locale** (`BR`→pt-BR, demais→en) + templates separados + snapshot `locale` | Determinístico, auditável, isola traduções | **RATIFICADA** |

> **Nota:** DEC-01/02 (base legal art. 7º V) e DEC-03 (inventário mínimo: endereço/bancários NULLable) já ratificados em `ccb-lgpd-decisoes.md` v1.0.0. Esta ratificação incorpora-os por referência para a migration Alembic.

---

## Especificação Técnica Consolidada (Para Implementação Paralela)

### 1. Migration Alembic — `invoices` + `invoice_sequences` (F1)
**Arquivo:** `migrations/versions/XXXX_create_invoices_and_sequences.py`

```sql
-- Tabela principal: invoices (snapshot completo, Opção A)
CREATE TABLE invoices (
    id                      BIGSERIAL PRIMARY KEY,
    owner_user_id           BIGINT NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    client_id               BIGINT REFERENCES clients(id) ON DELETE RESTRICT,
    simulation_id           BIGINT REFERENCES simulations(id) ON DELETE RESTRICT,
    invoice_number          VARCHAR(32) NOT NULL UNIQUE,
    status                  VARCHAR(16) NOT NULL DEFAULT 'finalized'
        CHECK (status IN ('draft','finalized')),
    locale                  VARCHAR(8) NOT NULL DEFAULT 'pt-BR'
        CHECK (locale IN ('pt-BR','en')),
    client_country_code     CHAR(2) NOT NULL,
    -- Partes (DEC-03: endereço/bancários NULLable)
    issuer_name             VARCHAR(120) NOT NULL,
    issuer_tax_id_digits    CHAR(14) NOT NULL,
    issuer_address          VARCHAR(240),
    client_name             VARCHAR(120) NOT NULL,
    client_tax_id_digits    CHAR(14) NOT NULL,
    client_address          VARCHAR(240),
    -- Bancários opcionais (DEC-03)
    banco                   VARCHAR(80),
    agencia                 VARCHAR(20),
    conta_com_digito        VARCHAR(30),
    pix_key                 VARCHAR(80),
    -- Período e descrição
    periodo_inicio          DATE NOT NULL,
    periodo_fim             DATE NOT NULL,
    description             VARCHAR(500) NOT NULL,
    -- Parâmetros de cálculo
    regime                  VARCHAR(16) NOT NULL
        CHECK (regime IN ('hourly','daily','weekly','monthly','fixed')),
    currency                CHAR(3) NOT NULL
        CHECK (currency IN ('USD','EUR')),
    amount                  NUMERIC(18,2) NOT NULL,
    quantity                NUMERIC(10,2),
    spread_pct              NUMERIC(6,4) NOT NULL,
    iof_pct                 NUMERIC(6,4) NOT NULL,
    -- Valores calculados (snapshot para reprodutibilidade)
    gross_foreign           NUMERIC(18,2) NOT NULL,
    gross_brl               NUMERIC(18,2) NOT NULL,
    spread_brl              NUMERIC(18,2) NOT NULL,
    iof_brl                 NUMERIC(18,2) NOT NULL,
    net_brl                 NUMERIC(18,2) NOT NULL,
    effective_rate          NUMERIC(18,6) NOT NULL,
    -- Cotação usada (crítico para reprodutibilidade)
    quote_rate              NUMERIC(18,6) NOT NULL,
    quote_source            VARCHAR(20) NOT NULL,
    quote_bulletin          VARCHAR(40),
    quoted_at               TIMESTAMPTZ NOT NULL,
    stale                   BOOLEAN NOT NULL DEFAULT FALSE,
    -- Lifecycle
    finalized_at            TIMESTAMPTZ,
    supersedes_invoice_id   BIGINT REFERENCES invoices(id) ON DELETE SET NULL,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at              TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    -- Constraint: identity check (reprodutibilidade)
    CONSTRAINT chk_invoice_identity CHECK (
        gross_brl - spread_brl - iof_brl = net_brl
    )
);

-- Índices para listagem e erase
CREATE INDEX ix_invoices_owner_created ON invoices (owner_user_id, created_at DESC);
CREATE INDEX ix_invoices_status ON invoices (status);
CREATE INDEX ix_invoices_client ON invoices (client_id);
CREATE INDEX ix_invoices_invoice_number ON invoices (invoice_number);
CREATE INDEX ix_invoices_finalized_at ON invoices (finalized_at);

-- Tabela de sequências (DEC-06: numeração sem SEQUENCE)
CREATE TABLE invoice_sequences (
    issuer_tax_id_digits    CHAR(14) NOT NULL,
    year_month              CHAR(7) NOT NULL,  -- '2026-11'
    last_number             INT NOT NULL DEFAULT 0,
    PRIMARY KEY (issuer_tax_id_digits, year_month)
);

-- Function atômica: next_invoice_number(issuer_tax_id_digits) → 'INV-202611-0001'
CREATE OR REPLACE FUNCTION next_invoice_number(p_issuer_tax_id_digits CHAR(14))
RETURNS TEXT LANGUAGE plpgsql AS $$
DECLARE
    v_ym        CHAR(7) := to_char(NOW(), 'YYYY-MM');
    v_next      INT;
    v_number    TEXT;
BEGIN
    LOOP
        UPDATE invoice_sequences
           SET last_number = last_number + 1
         WHERE issuer_tax_id_digits = p_issuer_tax_id_digits
           AND year_month = v_ym
        RETURNING last_number INTO v_next;
        IF FOUND THEN
            v_number := 'INV-' || replace(v_ym, '-', '') || '-' || lpad(v_next::TEXT, 4, '0');
            RETURN v_number;
        END IF;
        -- Race condition: tenta inserir nova linha
        BEGIN
            INSERT INTO invoice_sequences (issuer_tax_id_digits, year_month, last_number)
            VALUES (p_issuer_tax_id_digits, v_ym, 1)
            ON CONFLICT (issuer_tax_id_digits, year_month) DO NOTHING;
        EXCEPTION WHEN unique_violation THEN
            -- Outra transação inseriu; loop continua
        END;
    END LOOP;
END;
$$;
```

### 2. Rota Erase — `DELETE /v1/invoices/{id}` (DEC-04)
**Arquivo:** `src/backend/routers/invoices.py`

```python
@router.delete("/{invoice_id}", status_code=204)
async def erase_invoice(
    invoice_id: int,
    rate_service: RateService = Depends(get_rate_service),  # para owner check
    current_user: User = Depends(get_current_user),
) -> None:
    """LGPD art. 18: eliminação hard + cascade órfãs + log auditoria (sem PII)."""
    async with get_session() as session:
        invoice = await session.get(Invoice, invoice_id)
        if not invoice:
            raise NotFoundError("Invoice não encontrada")
        if invoice.owner_user_id != current_user.id:
            raise ForbiddenError("Não autorizado")

        # Hard delete (cascade em simulations se órfã via FK ON DELETE SET NULL)
        await session.delete(invoice)
        await session.commit()

    # Log auditoria (sem PII)
    logger.info("invoice_erased invoice_id=%d owner_user_id=%d", invoice_id, current_user.id)

    # Backup cleanup job (script separado, roda diário): apaga de backups > 30 dias
```

### 3. Sequenciador — `next_invoice_number()` (DEC-06)
**Arquivo:** `src/backend/services/invoice_number.py`

```python
async def generate_invoice_number(
    session: AsyncSession,
    issuer_tax_id_digits: str,
) -> str:
    """Chama function PL/pgSQL atômica; retorna 'INV-202611-0001'."""
    result = await session.execute(
        text("SELECT next_invoice_number(:issuer)"),
        {"issuer": issuer_tax_id_digits},
    )
    return result.scalar_one()
```

### 4. Templates Bilíngues (DEC-07)
**Arquivos:**
- `src/frontend/templates/invoice_pt_br.html` (pt-BR: labels, notice legal, moeda BRL, datas dd/mm/aaaa)
- `src/frontend/templates/invoice_en.html` (en: labels, notice legal, moeda USD/EUR, datas mm/dd/yyyy)
- `src/frontend/templates/_invoice_macros.html` (macros compartilhadas: formatação numérica, tabelas)

**Seleção no backend:**
```python
template_name = "invoice_pt_br.html" if invoice.locale == "pt-BR" else "invoice_en.html"
```

---

## Plano de Implementação Paralela (4 Workstreams Independentes)

| Workstream | Responsável | Entregável | Critério de Pronto |
|------------|-------------|------------|-------------------|
| **WS-1: Migration + Repository** | `agent-dba` | `migrations/versions/XXXX_create_invoices_and_sequences.py` + `SqlAlchemyInvoiceRepository` | Upgrade/downgrade OK em CI; tabelas criadas; FKs/CHECKs/UNIQUEs ativos |
| **WS-2: Rota Erase + API CRUD** | `agent-backend-dev` | `DELETE /v1/invoices/{id}` + `GET/LIST/FINALIZE/CLONE` | Property test `test_persistence_roundtrip` + `test_lgpd_erase` passam |
| **WS-3: Sequenciador** | `agent-dba` | `invoice_sequences` + `next_invoice_number()` function + service wrapper | Numeração sequencial por emissor/mês sem gaps; concorrência testada |
| **WS-4: Templates Bilíngues** | `agent-frontend-dev` | `invoice_pt_br.html`, `invoice_en.html`, `_invoice_macros.html` | PDF renderiza corretamente em ambos locales; notice legal traduzido |

**Sincronização:** WS-1 desbloqueia WS-2/WS-3. WS-4 independe (templates). Integração final em `F3` do relatório.

---

## Validação Obrigatória (Gate 1 — Pós-Implementação)

1. **Property test** `tests/unit/test_property_persistence_reprocess.py`:
   - `test_save_then_get_latest_round_trips` (persistência = reprocesso)
   - `test_calculate_identity_gross_brl_minus_deductions_equals_net`
2. **LGPD erase test** `tests/unit/test_property_lgpd_erase.py`:
   - `test_render_invoice_logs_no_personal_data`
   - `test_simulation_response_no_personal_data`
3. **Integração**: `tests/integration/test_invoice.py` — CRUD completo + erase + clone
4. **Migração**: `alembic upgrade head` + `alembic downgrade base` sem erros

---

## Assinatura CCB/GP

| Versão | SHA-256 do conteúdo normativo | Commit Git | Data | Papel do ratificador humano | Instrumento |
|--------|------------------------------|------------|------|----------------------------|-------------|
| 1.0.0 | `pending` | `pending` | 2026-11-14 | Gerente de Projeto — CCB de membro único | RAT-2026-11-14-INVOICES (consolida DEC-04..07) |

---

*Promulgado sob AFA-ULTIMATE v1.3.0-FINAL. Constituição é lei marcial: aplica-se, não se debate.*