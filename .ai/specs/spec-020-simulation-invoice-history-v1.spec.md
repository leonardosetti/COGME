---
id: ai-specs-spec-020-simulation-invoice-history-v1-spec
title: SPEC spec-020 — simulation-invoice-history-v1 — Simulações salvas, histórico e ciclo de vida das invoices
type: spec
version: 1.0.0
status: ativo
owner: agent-sdd-specialist
derived-from:
- docs/decisoes/ccb-CR-002.md (Gate D liberado, CR2-D08 ratificada)
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-03 inventário, DEC-05 draft/finalized/clone, DEC-06 numeração)
- .ai/specs/spec-017-identity-access-session-v1.spec.md (Gate C, require_owner, P-14)
- .ai/specs/spec-018-provider-profile-bank-account-v1.spec.md (Gate D, snapshot prestadora/banco)
- .ai/specs/spec-019-client-directory-v1.spec.md (Gate D, snapshot cliente, country_code)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (Gate B, retenção 5a+6m, erase, CP-1..CP-5)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.2 tabelas simulations/invoices, §12.3 integridade, §12.5 lifecycle, §13.1 Gate D)
- .ai/specs/spec-007-invoice-data-model-v1.spec.md (modelo canônico invoice, §3.4 snapshot, §3.7.3 cotação gap)
- constitution.md v1.3.0 (P-14 isolamento, P-15 LGPD/GDPR, Art. 7)
last-revised: '2026-11-14'
lgpd-class: dados-pessoais
tags:
- specs
- docs
- adequado-a-norma
- simulacao
- historico
- invoice
- draft
- finalized
- clone
---
---
spec_id: spec-020
specname: simulation-invoice-history-v1
version: 1.0.0
status: ratificada
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: CR-002 Gate D (docs/decisoes/ccb-CR-002.md, CR2-D08) + SPEC-017/018/019/022
task: CR-002 | sender: agent-project-analyst | kill_switch: inherited
trace:
  - docs/decisoes/ccb-CR-002.md (Gate D liberado; CR2-D08: draft/finalized/clone)
  - docs/decisoes/ccb-lgpd-decisoes.md (DEC-03: inventário; DEC-05: draft/finalized/clone; DEC-06: numeração INV-{YYYYMM}-{SEQ})
  - .ai/specs/spec-017-identity-access-session-v1.spec.md (require_owner, P-14)
  - .ai/specs/spec-018-provider-profile-bank-account-v1.spec.md (snapshot prestadora/banco)
  - .ai/specs/spec-019-client-directory-v1.spec.md (snapshot cliente, country_code)
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (retenção 5a+6m, erase, CP-3)
  - docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.2/§12.3/§12.5, §13.1 Gate D SPEC-020)
  - .ai/specs/spec-007-invoice-data-model-v1.spec.md (§3.4 snapshot, §3.7.3 cotação gap)
  - constitution.md v1.3.0 (P-14, P-15, Art. 7)
lgpd-class: dados-pessoais
---

# SPEC spec-020 — simulation-invoice-history-v1 — Simulações salvas, histórico e ciclo de vida das invoices

**Status: RATIFICADA** — Emissão autorizada por CCB/GP via CR-002 Gate D (2026-11-14). Paralela às SPEC-018, 019, 021. Dependências: SPEC-017, 018, 019, 022.

---

## 1. Contexto e origem

Esta spec implementa:
- **Simulações salvas por opt-in** (US-016): usuário escolhe salvar resultado da simulação
- **Histórico de simulações e invoices** (US-017): listagem paginada, filtros, download
- **Ciclo de vida da invoice**: `draft` (rascunho, editável) ↔ `finalized` (emitida, imutável) + **clone** (novo rascunho baseado em invoice existente)
- **Numeração canônica**: `INV-{YYYYMM}-{SEQ:04d}` por emissor/mês (DEC-06, tabela `invoice_sequences`)

**Princípios:**
- Isolamento por proprietário (P-14, `require_owner` em tudo)
- Simulação salva guarda **snapshot da cotação** (resolve gap spec-007 §3.7.3)
- Invoice `draft` editável; `finalized` imutável (fail-closed)
- Clone = novo rascunho com novo número + `supersedes_invoice_id` para rastreabilidade

---

## 2. Modelo de dados

### 2.1 `simulations` — Simulações salvas (opt-in)

| Campo | Tipo | Constraints | Observações |
|-------|------|-------------|-------------|
| `id` | UUID | PK | |
| `owner_user_id` | UUID | FK → `users.id`, NOT NULL | ON DELETE CASCADE; P-14 |
| `currency` | CHAR(3) | NOT NULL | Moeda base (USD, EUR, etc.) |
| `regime` | VARCHAR(20) | NOT NULL, CHECK `IN ('hourly','daily','weekly','monthly','fixed')` | Regime de contratação |
| `amount` | NUMERIC(18,2) | NOT NULL | Valor na moeda estrangeira |
| `quantity` | NUMERIC(10,2) | NOT NULL | Quantidade (horas, dias, semanas, meses) |
| `spread_pct` | NUMERIC(5,2) | NOT NULL | Spread % informado pelo usuário |
| `iof_pct` | NUMERIC(5,2) | NOT NULL | IOF % informado pelo usuário |
| `gross_foreign` | NUMERIC(18,2) | NOT NULL | Valor bruto moeda estrangeira |
| `gross_brl` | NUMERIC(18,2) | NOT NULL | Valor bruto BRL |
| `spread_brl` | NUMERIC(18,2) | NOT NULL | Spread em BRL |
| `iof_brl` | NUMERIC(18,2) | NOT NULL | IOF em BRL |
| `net_brl` | NUMERIC(18,2) | NOT NULL | Líquido BRL |
| `effective_rate` | NUMERIC(18,6) | NOT NULL | Taxa efetiva BRL/foreign |
| `rate` | NUMERIC(18,6) | NOT NULL | Taxa de câmbio (PTAX/Frankfurter) |
| `rate_source` | VARCHAR(50) | NOT NULL | Fonte da cotação (PTAX, Frankfurter) |
| `quoted_at` | TIMESTAMPTZ | NOT NULL | Timestamp da cotação |
| `bulletin` | VARCHAR(50) | NOT NULL | Boletim/fechamento (ex.: PTAX 2026-11-14) |
| `stale` | BOOLEAN | NOT NULL, DEFAULT false | `true` se cotação > 24h |
| `fx_quote_id` | UUID | FK → `fx_quotes.id`, NULLABLE | **Snapshot da cotação** (resolve gap spec-007 §3.7.3) |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT now() | |

**Regra:** Simulação **só persiste se usuário clicar "Salvar"** (opt-in). Não salvo = não persiste.

### 2.2 `invoices` — Emenda ao modelo canônico (spec-007)

Adiciona à tabela `invoices` (migração preserva `upgrade`/`downgrade`):

| Campo | Tipo | Constraints | Observações |
|-------|------|-------------|-------------|
| `owner_user_id` | UUID | FK → `users.id`, NOT NULL | ON DELETE RESTRICT (retenção 5a+6m); P-14 |
| `client_id` | UUID | FK → `clients.id`, NULLABLE | NULL = cliente fictício |
| `simulation_id` | UUID | FK → `simulations.id`, NULLABLE | NULL se invoice criada sem simulação salva |
| `status` | VARCHAR(20) | NOT NULL, DEFAULT 'draft', CHECK `IN ('draft','finalized')` | **Draft editável; Finalized imutável** |
| `locale` | VARCHAR(10) | NOT NULL, CHECK `IN ('pt-BR','en')` | `pt-BR` ou `en` (DEC-07) |
| `client_country_code` | CHAR(2) | NOT NULL | Fonte canônica locale (DEC-07) |
| `finalized_at` | TIMESTAMPTZ | NULL | Preenchido na finalização |
| `supersedes_invoice_id` | UUID | FK → `invoices.id`, NULLABLE | Clone: aponta para invoice original |
| `number` | VARCHAR(30) | NOT NULL, UNIQUE | Formato `INV-{YYYYMM}-{SEQ:04d}` (DEC-06) |
| `issuer_snapshot` | JSONB | NOT NULL | Dados da prestadora no momento |
| `client_snapshot` | JSONB | NOT NULL | Dados do cliente (cadastrado ou fictício) |
| `bank_snapshot` | JSONB | NOT NULL | Dados bancários descriptografados |
| `simulation_snapshot` | JSONB | NULLABLE | Parâmetros + resultado da simulação |
| `quote_snapshot` | JSONB | NOT NULL | Cotação completa (rate, source, quoted_at, bulletin, stale) |
| `amounts_snapshot` | JSONB | NOT NULL | `gross_foreign`, `gross_brl`, `spread_brl`, `iof_brl`, `net_brl`, `effective_rate` |
| `notice_snapshot` | TEXT | NOT NULL | Texto legal (notice) no locale da invoice |

**Constraints adicionais:**
- `CHECK (status = 'finalized' AND finalized_at IS NOT NULL) OR (status = 'draft' AND finalized_at IS NULL)`
- `UNIQUE (owner_user_id, number)` — numeração única por emissor (complementa `invoice_sequences`)

---

## 3. Numeração Canônica — `INV-{YYYYMM}-{SEQ:04d}` (DEC-06)

### 3.1 Tabela `invoice_sequences`

```sql
CREATE TABLE invoice_sequences (
    issuer_tax_id_digits CHAR(14) NOT NULL,  -- CNPJ da prestadora (14 dígitos)
    year_month CHAR(7) NOT NULL,             -- '2026-11'
    last_number INT NOT NULL DEFAULT 0,
    PRIMARY KEY (issuer_tax_id_digits, year_month)
);

-- Function atômica
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
$$ LANGUAGE plpgsql;
```

### 3.2 Uso na criação de invoice finalized

```python
# Em src/backend/services/invoice.py
async def create_finalized_invoice(..., db: AsyncSession):
    issuer_tax_id = await get_issuer_tax_id(user_id, db)  # de provider_profiles.cnpj ou users.cpf
    number = await db.execute(select(next_invoice_number(issuer_tax_id)))
    # ... cria invoice com number
```

---

## 4. Ciclo de Vida da Invoice (DEC-05, CR2-D08)

| Estado | Transição | Gatilho | Regras |
|--------|-----------|---------|--------|
| `draft` | → `finalized` | `POST /v1/invoices/{id}/finalize` | Valida snapshots completos; preenche `finalized_at = now()`; gera `number` via `next_invoice_number()`; **imutável após** |
| `draft` | → `draft` (clone) | `POST /v1/invoices/{id}/clone` | Cria nova invoice `draft` com snapshots copiados; `supersedes_invoice_id = id_original`; novo `number` na finalização |
| `finalized` | — | **Nenhuma** | **Imutável** (fail-closed na API: 409 em PUT/PATCH/DELETE) |

**Clone (recorrência mensal):**
- Copia todos snapshots (`issuer`, `client`, `bank`, `simulation`, `quote`, `amounts`, `notice`)
- `status = 'draft'`, `finalized_at = NULL`, `number = NULL`
- `supersedes_invoice_id = id_original`
- Usuário edita o que quiser (datas, valores, regime) → finaliza → novo número único

---

## 5. APIs

| Endpoint | Método | Descrição | Autenticação | Regras |
|----------|--------|-----------|--------------|--------|
| `/v1/simulations` | GET | Lista simulações salvas (paginado, `created_at` DESC) | `require_owner("simulation")` | Filtros: `currency`, `regime`, `stale`, `date_from`, `date_to` |
| `/v1/simulations` | POST | Salva simulação (opt-in) | `require_owner("simulation")` | Body: parâmetros simulação + `fx_quote_id`; retorna `simulation_id` |
| `/v1/simulations/{id}` | GET | Detalha simulação | `require_owner("simulation")` | Inclui cotação snapshot |
| `/v1/invoices` | GET | Lista invoices (paginado, `created_at` DESC) | `require_owner("invoice")` | Filtros: `status`, `locale`, `client_country_code`, `date_from`, `date_to` |
| `/v1/invoices` | POST | Cria invoice `draft` | `require_owner("invoice")` | Body: snapshots parciais; `status = 'draft'` |
| `/v1/invoices/{id}` | GET | Detalha invoice | `require_owner("invoice")` | Inclui todos snapshots |
| `/v1/invoices/{id}` | PUT | Atualiza invoice `draft` | `require_owner("invoice")` | **409 se `status = 'finalized'`** |
| `/v1/invoices/{id}/finalize` | POST | Finaliza invoice (draft → finalized) | `require_owner("invoice")` | Valida snapshots completos; gera `number`; `status = 'finalized'` |
| `/v1/invoices/{id}/clone` | POST | Clona invoice (nova draft) | `require_owner("invoice")` | Copia snapshots; `supersedes_invoice_id = id`; `status = 'draft'` |
| `/v1/invoices/{id}/download` | GET | Download PDF da invoice | `require_owner("invoice")` | Gera PDF no locale da invoice (`locale` snapshoteado) |

---

## 6. Histórico e Reprodutibilidade

- **Listar histórico não recalcula** com taxa vigente — usa `amounts_snapshot` + `quote_snapshot`
- **Cotação snapshot:** `fx_quote_id` em `simulations` + `quote_snapshot` em `invoices` (resolve gap spec-007 §3.7.3)
- **Valores reproduzíveis:** Todos campos numéricos armazenados com precisão fixa (NUMERIC)
- **PDF download:** Usa template no `locale` snapshoteado (`pt-BR` ou `en`); notice legal no mesmo idioma

---

## 7. Retenção e Eliminação (SPEC-022, DEC-04)

| Dado | Retenção | Eliminação |
|------|----------|------------|
| `simulations` | Enquanto conta ativa + opt-in | Hard delete na exclusão conta (cascade) |
| `invoices` (draft) | Enquanto conta ativa | Hard delete na exclusão conta |
| `invoices` (finalized) | **5 anos + 6 meses** | Anonimização irreversível → hard delete |
| `invoice_sequences` | Indeterminado (metadado) | Mantido para auditoria numérica |

---

## 8. Critérios de aceite e testes

- [ ] **AC-01:** Simulação salva por opt-in; guarda `fx_quote_id` + todos parâmetros/resultados; não salva se não clicar "Salvar"
- [ ] **AC-02:** Invoice `draft` editável (PUT); `finalized` imutável (409 em PUT/PATCH/DELETE)
- [ ] **AC-03:** Finalização: valida snapshots completos; gera `number` via `next_invoice_number()`; `finalized_at = now()`
- [ ] **AC-04:** Clone: novo `draft` com snapshots copiados; `supersedes_invoice_id`; novo número na finalização
- [ ] **AC-05:** Numeração `INV-{YYYYMM}-{SEQ:04d}` única por emissor/mês; `invoice_sequences` + function atômica
- [ ] **AC-06:** Histórico: listagem paginada ordenada por `created_at` DESC; filtros funcionais; **não recalcula** com taxa vigente
- [ ] **AC-07:** `require_owner` em 100% rotas; 404 cross-user (ST-03 ADR-019)
- [ ] **AC-08:** Retenção: simulações/drafts hard delete na exclusão conta; finalized 5a+6m → anonimização
- [ ] **AC-09:** PDF download usa `locale` + `notice_snapshot` do snapshot (não template atual)
- [ ] **AC-10:** Testes: concorrência numeração (duas finalizações simultâneas → números sequenciais); clone + edição + finalização; owner check

---

## 9. Rastreabilidade

| Referência | Fonte |
|------------|-------|
| CR-002 Gate D, CR2-D08 | `docs/decisoes/ccb-CR-002.md` |
| DEC-03, DEC-05, DEC-06 | `docs/decisoes/ccb-lgpd-decisoes.md` |
| SPEC-017, 018, 019, 022 | `.ai/specs/spec-017/018/019/022-*.spec.md` |
| spec-007 §3.4, §3.7.3 | `.ai/specs/spec-007-invoice-data-model-v1.spec.md` |
| spec-prop-017 §12.2/§12.3/§12.5 | `docs/especificacoes/spec-prop-017-conta-multiusuario.md` |
| Constitution v1.3.0 | `constitution.md` (P-14, P-15, Art. 7) |

---

## 10. Fora de escopo (YAGNI)

- Agendamento automático de invoices recorrentes (cron) — futuro
- Envio automático de invoice por email — fora MVP
- Integração com ERP/contabilidade (exportação XML/JSON) — futuro
- Dashboard analytics de simulações/invoices — futuro
- Versionamento de invoice (múltiplas finalizações) — clone atende recorrência

---

## 11. Metadados de emissão

- **Avaliador primário:** `agent-sdd-specialist` + `agent-dba`
- **Ratificação:** CCB/GP via CR-002 Gate D (2026-11-14)
- **Dependências:** SPEC-017, 018, 019, 022
- **parcel.dod:** true
- **Data da emissão:** 2026-11-14
- **Status da spec:** ativa / ratificada

---

## CHANGELOG

| Versão | Data | Task/Handoff | Mudança |
|--------|------|--------------|---------|
| 1.0.0 | 2026-11-14 | CR-002 Gate D / agent-sdd-specialist + agent-dba | Emissão inicial, ratificada. Simulações opt-in, histórico, draft/finalized/clone, numeração INV-{YYYYMM}-{SEQ}, snapshots cotação/valores, retenção 5a+6m. |

---

## CAMADAS FUNDAMENTAIS — MAPA (TA-0031)

| Camada | Seção nesta spec | Estado |
|--------|------------------|--------|
| (a) cabeçalho | frontmatter (`spec_id: spec-020`, `version: 1.0.0`, `status: ratificada`) | aplicada |
| (b) Contexto/origem | §1 + frontmatter `origin`/`task` | aplicada |
| (c) Resolução de conflitos | §1 (princípios: opt-in, snapshot, imutável, numeração) | aplicada |
| (d) Corpo de decisões/requisitos/contratos | §2 (modelo simulations/invoices), §3 (numeração), §4 (ciclo vida), §5 (APIs), §6 (histórico), §7 (retenção) | aplicada |
| (e) Critérios de aceite/testes | §8 (AC-01..AC-10) | aplicada |
| (f) Rastreabilidade | §9 + frontmatter `trace` | aplicada |
| (g) Fora de escopo (YAGNI) | §10 | aplicada |
| (h) Changelog | CHANGELOG | aplicada |