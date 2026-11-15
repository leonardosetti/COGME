---
id: docs-decisoes-ccb-lgpd-decisoes
title: Registro de Decisões LGPD — CR-002 (DEC-01 a DEC-07)
type: adr
version: 1.0.0
status: ratificado
owner: agent-compliance-governance
derived-from:
- docs/decisoes/ccb-CR-002.md (CR2-D02, CR2-D03, CR2-D04, CR2-D05, CR2-D08)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (v0.3.0, D2-D7 ratificadas)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md (v0.2.0, §15 vereditos)
- LGPD Lei 13.709/2018 (art. 4º I, 6º III, 7º V, 16, 18, 206 §5º CC)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- ccb
- lgpd
- gdpr
- decisao
- cr-002
- spec-015
- spec-022
---

# Registro de Decisões LGPD — CR-002 (DEC-01 a DEC-07)

**Data da sessão:** 2026-11-14  
**Participantes:** Gerente de Projeto (CCB de membro único) + `agent-compliance-governance` (parecer)  
**Instrumento:** Prompt expresso CCB — ratificação única (continuação RAT-2026-11-14-E20)  
**Base:** Decisões CR2-D02, D03, D04, D05, D08 ratificadas em `docs/decisoes/ccb-CR-002.md`

---

## DEC-01 + DEC-02: Base Legal Unificada — **APROVADA**

| Item | Decisão | Fundamento |
|------|---------|------------|
| **DEC-01** (art. 4º I — "exclusivamente particular") | **NÃO APLICÁVEL** | Emissão de invoice para **terceiro (cliente)** = finalidade econômica (prestação de serviço, cobrança, comprovação fiscal). Art. 4º I exige *ausência* de finalidade econômica. |
| **DEC-02** (art. 7º V — execução de contrato) | **APLICAR art. 7º V** | Invoice decorre de **contrato/prestação de serviço** com o cliente. Dados do cliente (nome, CPF/CNPJ, endereço) são necessários para execução contratual. Base legal sólida, não requer consentimento. |

**Decisão única:** **Base legal = art. 7º V (execução de contrato)** para todos os dados da invoice (emitente + cliente). Registrar no `ROPA` simplificado.

**Impacto em specs:**
- `spec-015` §3.4.1: Cenário A ratificado (art. 7º V); Cenário B (art. 4º I) descartado
- `spec-022`: ROPA simplificado inclui `base_legal: "art_7_v_lgpd"` para `invoices`

---

## DEC-03: Inventário Mínimo de Campos (Obrigatórios vs NULLable) — **APROVADA**

| Campo | Nullability | Justificativa |
|-------|-------------|---------------|
| `issuer_name`, `issuer_tax_id_digits`, `client_name`, `client_tax_id_digits` | **NOT NULL** | Identificação das partes — indispensável para validade da invoice (art. 7º V) |
| `periodo_inicio`, `periodo_fim` | **NOT NULL** | Período de prestação — essencial para vincular serviço ao valor |
| `description` | **NOT NULL** | Descrição do serviço — requisito fiscal mínimo |
| `issuer_address`, `client_address` | **NULL** (opcional) | LGPD art. 6º III: coletar **só se necessário**. Endereço não é obrigatório para invoice de serviço digital; template condicional (`{% if address %}`) |
| `banco`, `agencia`, `conta_com_digito`, `pix_key` | **NULL** (opcional) | Dados bancários sensíveis — só coletar se template US-004 exigir (P-04 minimização). Cliente pode pagar via PIX sem conta tradicional. |
| `regime`, `currency`, `amount`, `quantity`, `spread_pct`, `iof_pct` | **NOT NULL** | Parâmetros de cálculo — já validados no request |
| `gross_foreign`, `gross_brl`, `spread_brl`, `iof_brl`, `net_brl`, `effective_rate` | **NOT NULL** | Valores calculados — snapshot para reprodutibilidade (spec-007 §3.4) |
| `quote.rate`, `quote.source`, `quoted_at`, `bulletin`, `stale` | **NOT NULL** | Cotação usada — **crítico para reprodutibilidade** (gap declarado em spec-007 §3.7.3) |

**Decisão:** **Aprovar inventário acima**. Endereço e bancários = NULLable (coleta condicional no frontend).

**Impacto em specs:**
- `spec-007` §3.1: Atualizar tabela de campos com nullability
- `spec-007` migration: `ALTER TABLE invoices ALTER COLUMN issuer_address DROP NOT NULL` (etc.)
- `spec-018` (prestadora/banco): Campos bancários NULLable
- `spec-019` (clientes): `address` NULLable

---

## DEC-04: Política de Retenção + Rota Erase — **APROVADA**

| Aspecto | Decisão | Fundamento |
|---------|---------|------------|
| **Retenção primária** | **5 anos** | Art. 206, §5º, I do CC (prescrição cobrança serviços) + prática fiscal (NF-e/NFS-e) |
| **Retenção pós-contrato** | **+ 6 meses** após última invoice do cliente | Margem para contestações, chargebacks, auditoria |
| **Erase (DELETE)** | **Rota obrigatória**: `DELETE /v1/invoices/{id}` → hard delete + cascade em `simulations` se órfã | LGPD art. 18, VI (eliminação); spec-015 CP-3; spec-007 §3.6 |
| **Backup** | Excluir de backups em até 30 dias após erase | LGPD art. 16 (direito à eliminação em backups) |
| **Logs de erase** | Auditoria: `invoice_id`, `owner_user_id`, `timestamp`, `ator` (sem PII) | Accountability (art. 6º, X) |

**Decisão:** **Aprovar 5a + 6m + rota DELETE hard + exclusão backup 30d**.

**Impacto em specs:**
- `spec-022` (lifecycle/privacy): Implementar job de retenção + rota erase
- `spec-004` (backend): Adicionar `DELETE /v1/invoices/{id}` com owner-check
- `spec-007` §3.6: Documentar política de retenção/erase
- Backup job: script `scripts/backup_erase_cleanup.py` (30 dias)

---

## DEC-05: US-016/017 — Ciclo Draft/Finalized + Clone — **APROVADA**

| Item | Decisão | Justificativa |
|------|---------|---------------|
| **Status `draft`/`finalized`** | **APROVAR** | Permite usuário revisar antes de "emitir"; atende fluxo real (rascunho → envio cliente) |
| **Finalized = imutável** | **APROVAR** (fail-closed na API) | Garantia fiscal/jurídica; invoice emitida não muda |
| **Clone (nova invoice rascunho)** | **APROVAR** | Reutilização comum (recorrência mensal); `supersedes_invoice_id` para rastreabilidade |
| **Numeração no clone** | **Novo número único** (não reutiliza) | Evita duplicidade fiscal; rastreia origem via `supersedes_invoice_id` |

**Decisão:** **Ratificar US-016/017** — habilita CR-006.

**Impacto em specs:**
- `spec-007` migration: Adicionar `status`, `finalized_at`, `supersedes_invoice_id`
- `spec-020` (history): Lógica draft/finalized + clone
- `spec-004` API: `POST /v1/invoices/{id}/clone` → novo draft
- `spec-008` (frontend): UI para draft/finalized/clone

---

## DEC-06: Numeração sem PostgreSQL Sequence — **APROVADA (Opção A)**

| Opção | Decisão | Prós/Contras |
|-------|---------|--------------|
| **A: `INV-{YYYY}{MM}-{SEQ:04d}`** (tabela `invoice_sequences` por emissor/ano/mês) | **RECOMENDADA E APROVADA** | Legível, auditável, sem gap visível, atende C-04 (única por emissor/ano) |
| B: UUID v7 | Rejeitar | Não legível, não sequencial, fiscal pode questionar |
| C: `BIGSERIAL` global | Rejeitar | Vaza volume total do negócio; gap visível em rollback |

**Implementação Opção A:**
```sql
CREATE TABLE invoice_sequences (
    issuer_tax_id_digits CHAR(14) NOT NULL,
    year_month CHAR(7) NOT NULL,  -- '2026-11'
    last_number INT NOT NULL DEFAULT 0,
    PRIMARY KEY (issuer_tax_id_digits, year_month)
);
-- Função atômica: next_invoice_number(issuer_tax_id_digits) → 'INV-202611-0001'
```

**Decisão:** **Aprovar Opção A** — `agent-dba` implementa function + tabela de sequência.

**Impacto em specs:**
- `spec-007` §3.5: Documentar formato de numeração
- `spec-020` (history): Migration cria `invoice_sequences` + function `next_invoice_number()`
- `spec-004` API: Usa function na criação de invoice finalized

---

## DEC-07: Bilíngue PT-BR/EN — **APROVADA**

| Item | Decisão | Justificativa |
|------|---------|---------------|
| **Regra canônica: `client_country_code` → locale** | **APROVAR** | Objetivo, determinístico, auditável |
| `BR` → `pt-BR` | **APROVAR** | Cliente brasileiro = invoice em português |
| Qualquer outro ISO 3166-1 → `en` | **APROVAR** | Inglês = língua franca negócios internacionais |
| **Cliente fictício (dummy) exige `country_code`** | **APROVAR** | Sem país = 400 validation_error; evita locale default oculto |
| **Templates separados** (`invoice_pt_br.html`, `invoice_en.html`) | **APROVAR** | Isola traduções (labels, notice legal, moeda, datas); compartilha macros de formatação |
| **Snapshot `locale` + `client_country_code` na invoice finalizada** | **APROVAR** | Auditoria histórica: invoice emitida em EN não muda se cliente depois cadastra BR |

**Decisão:** **Aprovar regra país→locale + templates separados + snapshot**. Jurídico valida tradução do `notice` legal (CR7-D02) — pode ser feito em paralelo.

**Impacto em specs:**
- `spec-021` (bilingual): Regra implementada no backend + frontend
- `spec-007` migration: Adicionar `locale`, `client_country_code` (NOT NULL)
- `spec-008` (frontend): Validação `country_code` obrigatório para cliente fictício
- Templates: `templates/invoice_pt_br.html`, `templates/invoice_en.html` (compartilham `_invoice_macros.html`)

---

## Resumo: 7 Decisões → 5 Aprovações Diretas

| DEC | Decisão | Specs Impactadas | Ação Imediata |
|-----|---------|------------------|---------------|
| **DEC-01/02** | Base legal = **art. 7º V** (execução contrato) | `spec-015`, `spec-022` | Registrar no ROPA simplificado |
| **DEC-03** | Inventário mínimo **aprovado** (endereço/bancários = NULL) | `spec-007`, `spec-018`, `spec-019` | Atualizar §3.1 + migration |
| **DEC-04** | Retenção **5a + 6m** + **DELETE hard** + backup 30d | `spec-022`, `spec-004`, `spec-007` | Implementar rota erase + job limpeza |
| **DEC-05** | **Ratificar US-016/017** (draft/finalized/clone) | `spec-007`, `spec-020`, `spec-004`, `spec-008` | Migration adiciona colunas |
| **DEC-06** | Numeração **`INV-{YYYYMM}-{SEQ:04d}`** por emissor/mês | `spec-007`, `spec-020` | `agent-dba` cria tabela + function |
| **DEC-07** | **Bilíngue aprovado** (país→locale, templates separados) | `spec-021`, `spec-007`, `spec-008` | Frontend valida `country_code`; 2 templates |

---

## Próximos Passos (Pós-Ratificação)

1. **Atualizar `spec-007-invoice-data-model-v1.spec.md`** — incorporar DEC-03, DEC-05, DEC-06, DEC-07 (campos, nullability, numeração, locale)
2. **Emitir `spec-022-account-lifecycle-privacy-v1.spec.md`** — DEC-04 (retenção/erase), DEC-01/02 (ROPA/base legal)
3. **Emitir `spec-017-identity-access-session-v1.spec.md`** — usa ADR-017 (Argon2id), ADR-019 (threat model)
4. **Emitir `spec-018/019/020/021`** — em paralelo (Gate D liberado)
5. **Implementar migrations** — `agent-dba` cria: `invoice_sequences`, colunas `invoices`, tabelas identidade/domínio
6. **Validar templates bilíngues** — `agent-frontend-dev` cria `invoice_pt_br.html`, `invoice_en.html`

---

## CHANGELOG

- **1.0.0 — 2026-11-14:** Emissão inicial, ratificada por CCB/GP como continuação de RAT-2026-11-14-E20. Responsável: `agent-compliance-governance`.