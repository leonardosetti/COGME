---
id: ai-specs-spec-021-invoice-bilingual-v1
title: 'SPEC spec-021 — invoice-bilingual-v1 — Invoice bilíngue PT-BR / EN'
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-007-invoice-bilingual.md
- docs/especificacoes/spec-prop-022-invoice-bilingual.md
- docs/decisoes/ccb-003-multiusuario-lgpd.md (CR-008 liberado)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 9; P-02, P-03, P-04)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.md (dependência)
- .ai/specs/spec-020-simulation-invoice-history-v1.md (dependência: emenda invoices)
- .ai/specs/spec-007-invoice-data-model-v1.md (modelo canônico)
- .ai/specs/spec-008-frontend-web-responsive-v1.md (frontend MVP)
- .ai/specs/spec-023-ui-spec-v1.md (templates PDF)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- specs
- docs
- invoice
- i18n
- bilingual
spec-id: spec-021
specname: invoice-bilingual-v1
version: 1.0.0
status: ratificado
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: docs/change-requests/cr-007-invoice-bilingual.md (CR-007, SPEC-021)
task: "TA-0069 | sender: agent-nexus-prime-ultimate"
kill_switch: inherited
lgpd-class: n/a
trace:
  - docs/change-requests/cr-007-invoice-bilingual.md
  - docs/especificacoes/spec-prop-022-invoice-bilingual.md
  - docs/decisoes/ccb-003-multiusuario-lgpd.md
  - constitution.md (Arts. 1.2, 1.3, 3, 5.1, 9; P-02, P-03, P-04)
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.md
  - .ai/specs/spec-020-simulation-invoice-history-v1.md
  - .ai/specs/spec-007-invoice-data-model-v1.md
  - .ai/specs/spec-008-frontend-web-responsive-v1.md
  - .ai/specs/spec-023-ui-spec-v1.md
---

# SPEC spec-021 — invoice-bilingual-v1 — Invoice bilíngue PT-BR / EN

**Status:** **RATIFICADA** — Liberada após CCB-003 (CR-008 resolvido). Implementa CR-007. Dependências: SPEC-020 (emenda invoices), SPEC-022 (lifecycle). OS-09 parcialmente revertido (apenas PDF bilíngue).

---

## 1. Contexto e Origem

Emitida por TA-0069 / CR-007 (agent-nexus-prime-ultimate → agent-sdd-specialist, action: spec, 2026-11-14) para implementar a regra de idioma da invoice: PT-BR para cliente nacional (`BR`), EN para cliente estrangeiro. Dois templates Jinja2 separados com macros compartilhadas. Snapshot `locale` + `client_country_code` na invoice finalizada. Erros da API e interface permanecem PT-BR. Condicionada à SPEC-020 (emenda `invoices` com `locale`/`client_country_code`) e SPEC-022 (lifecycle).

---

## 2. Regra de Idioma (CR7-D01)

### 2.1 Fonte Canônica

- **Origem:** `client_country_code` (ISO 3166-1) do cliente na invoice.
- **Derivação automática no backend:** 
  - `client_country_code = 'BR'` → `locale = 'pt-BR'`
  - Qualquer outro código → `locale = 'en'`
- **Não aceito do request:** `locale` derivado server-side; validação rejeita `locale` no payload.

### 2.2 Cliente Fictício (Dummy)

- **Requisito:** `client_country_code` **obrigatório** no request de invoice.
- **Sem país:** 400 `validation_error` ("country_code é obrigatório para cliente fictício").
- **Nenhuma inferência silenciosa** — país deve ser informado explicitamente.

### 2.3 Snapshot na Invoice Finalizada

- **Campos gravados (emenda SPEC-020):**
  - `locale` — `pt-BR` ou `en`
  - `client_country_code` — ISO 3166-1 do cliente
- **Finalidade:** Auditoria histórica — invoice emitida registra idioma usado.

---

## 3. Templates Jinja2

### 3.1 Arquivos

| Template | Idioma | Descrição |
|----------|--------|-----------|
| `invoice_pt_br.html` | PT-BR | Labels, moeda (R$), datas (dd/mm/aaaa), notice em português |
| `invoice_en.html` | EN | Labels, currency (USD/EUR), dates (mm/dd/yyyy), notice in English |

### 3.2 Macros Compartilhadas (`macros.html`)

```jinja2
{% macro format_money(value, currency, locale) %}
  {% if locale == 'pt-BR' %}
    R$ {{ value | format_number(locale='pt_BR') }}
  {% else %}
    {{ currency }} {{ value | format_number(locale='en_US') }}
  {% endif %}
{% endmacro %}

{% macro format_date(value, locale) %}
  {% if locale == 'pt-BR' %}
    {{ value | format_datetime(format='dd/MM/yyyy', locale='pt_BR') }}
  {% else %}
    {{ value | format_datetime(format='MM/dd/yyyy', locale='en_US') }}
  {% endif %}
{% endmacro %}

{% macro format_datetime(value, locale) %}
  {% if locale == 'pt-BR' %}
    {{ value | format_datetime(format='dd/MM/yyyy HH:mm', locale='pt_BR') }}
  {% else %}
    {{ value | format_datetime(format='MM/dd/yyyy HH:mm', locale='en_US') }}
  {% endif %}
{% endmacro %}

{% macro format_rate(value, locale) %}
  {% if locale == 'pt-BR' %}
    {{ value | format_number(locale='pt_BR', decimal_places=6) }}
  {% else %}
    {{ value | format_number(locale='en_US', decimal_places=6) }}
  {% endif %}
{% endmacro %}
```

### 3.3 Labels por Locale

| Chave | PT-BR | EN |
|-------|-------|-----|
| `invoice_number` | Número da Invoice | Invoice Number |
| `issue_date` | Data de Emissão | Issue Date |
| `description` | Descrição | Description |
| `issuer` | Emitente | Issuer |
| `client` | Cliente | Client |
| `name` | Nome | Name |
| `tax_id` | Documento | Tax ID |
| `address` | Endereço | Address |
| `regime` | Regime | Regime |
| `quantity` | Quantidade | Quantity |
| `unit_amount` | Valor Unitário | Unit Amount |
| `currency` | Moeda | Currency |
| `rate` | Cotação | Rate |
| `rate_source` | Fonte | Source |
| `bulletin` | Boletim | Bulletin |
| `gross_foreign` | Bruto (Moeda Estrangeira) | Gross (Foreign Currency) |
| `gross_brl` | Bruto (BRL) | Gross (BRL) |
| `spread_pct` | Spread (%) | Spread (%) |
| `spread_brl` | Spread (BRL) | Spread (BRL) |
| `iof_pct` | IOF (%) | IOF (%) |
| `iof_brl` | IOF (BRL) | IOF (BRL) |
| `net_brl` | Líquido (BRL) | Net (BRL) |
| `effective_rate` | Câmbio Efetivo | Effective Rate |
| `stale_warning` | ⚠ Cotação com defasagem | ⚠ Stale Rate |
| `notice` | (texto legal PT-BR) | (legal text EN) |

### 3.4 Notice Legal (CR7-D02)

- **PT-BR:** Texto original da `spec-004` ("Simulação de caráter informativo; spread e IOF foram informados pelo usuário e não substituem a orientação de um profissional habilitado.")
- **EN:** Tradução validada juridicamente ("This simulation is for informational purposes only; spread and IOF were provided by the user and do not substitute the advice of a qualified professional.")
- **Validação:** Parecer jurídico (CR7-D02) — tradução fiel, sem alteração de sentido.

---

## 4. Implementação Backend

### 4.1 Derivação de Locale (SPEC-020 `render_invoice`)

```python
def derive_locale(client_country_code: str) -> str:
    """Deriva locale do país do cliente."""
    return 'pt-BR' if client_country_code == 'BR' else 'en'

async def render_invoice(request: InvoiceRequest, rate_service: RateService) -> bytes:
    # ... existing code ...
    locale = derive_locale(request.client.country_code)
    # client_country_code já validado no schema (obrigatório para dummy)
    template_name = f'invoice_{locale.replace("-", "_")}.html'  # invoice_pt_br.html ou invoice_en.html
    # ... render com macros compartilhadas ...
```

### 4.2 Schema `InvoiceRequest` (SPEC-020)

- `client.country_code`: **Obrigatório** (CHAR(2) ISO 3166-1).
- Validação: `country_code` presente → 200; ausente → 400.

---

## 5. Frontend (SPEC-023)

### 5.1 Formulário de Invoice

- **Campo País do Cliente:** Select com países (ISO 3166-1), padrão `BR`.
- **Cliente Fictício:** País obrigatório (validação client-side + server-side).
- **Cliente Cadastrado:** País pré-preenchido do cadastro (editável).
- **Preview:** Não necessário — PDF baixado diretamente.

### 5.2 Erros e Interface

- **Erros da API:** Permanecem PT-BR (conforme `spec-004`/`spec-008`).
- **Interface:** Permanece PT-BR (i18n integral fora de escopo — OS-09).

---

## 6. Segurança e LGPD

- **Idioma não é PII** — sem impacto em LGPD/GDPR (CR8-D02).
- **Snapshot:** `locale` + `client_country_code` gravados na invoice finalizada para auditoria.
- **Templates:** Apenas labels/formatos; nenhum dado sensível nos templates.
- **WeasyPrint:** `_RefusingUrlFetcher` recusa tudo; fontes locais (DejaVu Sans).

---

## 6. Critérios de Aceite e Testes

| ID | Critério | Método |
|----|----------|--------|
| AC-01 | Cliente BR → invoice PT-BR (labels, moeda R$, datas dd/mm/aaaa, notice PT) | Teste integração (PDF) |
| AC-02 | Cliente US/DE/FR → invoice EN (labels, moeda USD/EUR, datas mm/dd/yyyy, notice EN) | Teste integração (PDF) |
| AC-03 | Cliente fictício sem `country_code` → 400 validation_error | Teste integração |
| AC-04 | Snapshot: `locale` + `client_country_code` gravados na invoice finalizada | Teste integração (transação) |
| AC-05 | Templates: macros compartilhadas; labels corretos por locale | Teste unitário (render) |
| AC-06 | Notice legal: PT-BR original + EN traduzido validado juridicamente | Revisão jurídica (CR7-D02) |
| AC-07 | Erros API/UI: permanecem PT-BR | Teste integração |
| AC-08 | WeasyPrint: `_RefusingUrlFetcher` ativo; fontes locais | Teste integração |

---

## 7. Rastreabilidade

| Fonte | Seção |
|-------|-------|
| CR-007 (issue #40) | Todas |
| CR-008 / SPEC-022 | Lifecycle, LGPD (idioma não é PII) |
| CR-006 / SPEC-020 | Emenda `invoices` (`locale`, `client_country_code`) |
| CCB-003 | CR7-D01..D03, CR8-D02 |
| Constitution | P-02, P-03, P-04 |
| SPEC-022 | Lifecycle, LGPD |
| SPEC-020 | Emenda `invoices` |
| SPEC-007/008 | Modelo canônico, frontend MVP |
| SPEC-023 | Templates PDF, macros |

---

## 8. Fora de Escopo (YAGNI)

- i18n integral da interface e dos erros (OS-09 permanece FORA).
- Outros idiomas (ES, FR, etc.) — YAGNI (CR7-D03).
- Tradução dinâmica via gettext/i18n libraries.
- Portal do cliente com invoice no idioma preferido.

---

## CHANGELOG

- 1.0.0 — 2026-11-14: SPEC-021 ratificada (CCB-003); implementa CR-007; regra país→locale, dois templates Jinja2 com macros compartilhadas, snapshot `locale`+`client_country_code`, notice legal traduzido validado. Dependências SPEC-020, SPEC-022.