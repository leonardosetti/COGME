---
id: ai-specs-spec-021-invoice-bilingual-v1-spec
title: SPEC spec-021 — invoice-bilingual-v1 — Invoice bilíngue PT-BR/EN (regra país→locale, templates separados)
type: spec
version: 1.0.0
status: ativo
owner: agent-frontend-dev
derived-from:
- docs/decisoes/ccb-CR-002.md (Gate D liberado, CR2-D05 ratificada)
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-07 bilíngue aprovado)
- .ai/specs/spec-019-client-directory-v1.spec.md (Gate D, client_country_code canônico)
- .ai/specs/spec-020-simulation-invoice-history-v1.spec.md (Gate D, locale + client_country_code snapshoteados)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (Gate B, P-15 LGPD/GDPR por design)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.4 idioma, §13.1 Gate D SPEC-021)
- constitution.md v1.3.0 (Art. 1.2 escopo bilíngue, P-15 LGPD/GDPR, P-10 linguagem)
- LGPD Lei 13.709/2018 (art. 7º V, 9º - informação clara e acessível)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- specs
- docs
- adequado-a-norma
- bilíngue
- invoice
- i18n
- template
---
---
spec_id: spec-021
specname: invoice-bilingual-v1
version: 1.0.0
status: ratificada
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: CR-002 Gate D (docs/decisoes/ccb-CR-002.md, CR2-D05) + SPEC-019 + SPEC-020 + SPEC-022
task: CR-002 | sender: agent-project-analyst | kill_switch: inherited
trace:
  - docs/decisoes/ccb-CR-002.md (Gate D liberado; CR2-D05: regra país→idioma)
  - docs/decisoes/ccb-lgpd-decisoes.md (DEC-07: bilíngue aprovado, país→locale, templates separados)
  - .ai/specs/spec-019-client-directory-v1.spec.md (client_country_code canônico, fictício exige país)
  - .ai/specs/spec-020-simulation-invoice-history-v1.spec.md (locale + client_country_code snapshoteados)
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (P-15 LGPD/GDPR por design)
  - docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.4, §13.1 Gate D SPEC-021)
  - constitution.md v1.3.0 (Art. 1.2, P-15, P-10)
  - LGPD art. 7º V, 9º (informação clara)
lgpd-class: n/a
---

# SPEC spec-021 — invoice-bilingual-v1 — Invoice bilíngue PT-BR/EN (regra país→locale, templates separados)

**Status: RATIFICADA** — Emissão autorizada por CCB/GP via CR-002 Gate D (2026-11-14). Paralela às SPEC-018, 019, 020. Dependências: SPEC-019 (cliente/country_code), SPEC-020 (invoice/locale snapshot), SPEC-022 (P-15).

---

## 1. Contexto e origem

Esta spec implementa a **emissão de invoice em dois idiomas**: **Português (pt-BR)** para clientes brasileiros e **Inglês (en)** para clientes estrangeiros. A regra é **determinística e auditável**:

> **`client_country_code` (ISO 3166-1) → `locale`**
> - `BR` → `pt-BR`
> - Qualquer outro código → `en`

**Princípios (DEC-07, CR2-D05):**
- Fonte canônica: `client_country_code` do cliente (cadastrado ou fictício)
- Cliente fictício **exige `country_code` explícito** (400 validation_error se ausente)
- Templates **separados**: `invoice_pt_br.html` e `invoice_en.html`
- Macros compartilhadas: `_invoice_macros.html` (formatação moeda, datas, números)
- `locale` + `client_country_code` **snapshoteados** na invoice finalizada (imutáveis)
- Erros da API e interface do produto permanecem **PT-BR** (i18n integral fora de escopo)

---

## 2. Arquitetura de Templates

### 2.1 Estrutura de arquivos

```
templates/
├── invoice_pt_br.html      # Template PT-BR (padrão)
├── invoice_en.html         # Template EN
├── _invoice_macros.html    # Macros Jinja2 compartilhadas
└── _invoice_notice_pt_br.html  # Notice legal PT-BR
    _invoice_notice_en.html     # Notice legal EN
```

### 2.2 Macros compartilhadas (`_invoice_macros.html`)

```jinja2
{% macro format_currency(value, currency='BRL', locale='pt_BR') %}
    {# value: NUMERIC(18,2) #}
    {% if locale == 'pt_BR' %}
        R$ {{ (value / 100) | format_number(locale='pt_BR') }}
    {% else %}
        {{ currency }} {{ (value / 100) | format_number(locale='en_US') }}
    {% endif %}
{% endmacro %}

{% macro format_date(date, locale='pt_BR') %}
    {% if locale == 'pt_BR' %}
        {{ date.strftime('%d/%m/%Y') }}
    {% else %}
        {{ date.strftime('%m/%d/%Y') }}
    {% endif %}
{% endmacro %}

{% macro format_datetime(datetime, locale='pt_BR') %}
    {% if locale == 'pt_BR' %}
        {{ datetime.strftime('%d/%m/%Y %H:%M') }}
    {% else %}
        {{ datetime.strftime('%m/%d/%Y %H:%M') }}
    {% endif %}
{% endmacro %}

{% macro format_number(value, locale='pt_BR') %}
    {% if locale == 'pt_BR' %}
        {{ '{:,.2f}'.format(value).replace(',', 'X').replace('.', ',').replace('X', '.') }}
    {% else %}
        {{ '{:,.2f}'.format(value) }}
    {% endif %}
{% endmacro %}
```

### 2.3 Template PT-BR (`invoice_pt_br.html`)

```jinja2
{% extends "base.html" %}
{% from "_invoice_macros.html" import format_currency, format_date, format_datetime, format_number %}
{% include "_invoice_notice_pt_br.html" %}

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Invoice {{ invoice.number }} - {{ invoice.issuer_snapshot.legal_name }}</title>
    <style>/* CSS otimizado para PDF (WeasyPrint) */</style>
</head>
<body>
    <header>
        <h1>INVOICE</h1>
        <div class="invoice-number">{{ invoice.number }}</div>
    </header>
    
    <section class="parties">
        <div class="issuer">
            <h2>Prestadora</h2>
            <p>{{ invoice.issuer_snapshot.legal_name }}</p>
            <p>{{ invoice.issuer_snapshot.cnpj | format_cnpj }}</p>
            {% if invoice.issuer_snapshot.address %}
            <p>{{ invoice.issuer_snapshot.address }}, {{ invoice.issuer_snapshot.city }}/{{ invoice.issuer_snapshot.state }}</p>
            {% endif %}
        </div>
        
        <div class="client">
            <h2>Cliente</h2>
            <p>{{ invoice.client_snapshot.name }}</p>
            <p>{{ invoice.client_snapshot.tax_id | format_cpf_cnpj }}</p>
            {% if invoice.client_snapshot.address %}
            <p>{{ invoice.client_snapshot.address }}</p>
            {% endif %}
            <p>País: {{ invoice.client_country_code }}</p>
        </div>
    </section>
    
    <section class="details">
        <table>
            <thead>
                <tr><th>Descrição</th><th>Regime</th><th>Quantidade</th><th>Valor ({{ invoice.currency }})</th></tr>
            </thead>
            <tbody>
                <tr>
                    <td>{{ invoice.simulation_snapshot.description }}</td>
                    <td>{{ invoice.simulation_snapshot.regime }}</td>
                    <td>{{ format_number(invoice.simulation_snapshot.quantity) }}</td>
                    <td>{{ format_currency(invoice.amounts_snapshot.gross_foreign, invoice.currency, 'pt_BR') }}</td>
                </tr>
            </tbody>
        </table>
        
        <div class="totals">
            <div class="row"><span>Bruto ({{ invoice.currency }})</span><span>{{ format_currency(invoice.amounts_snapshot.gross_foreign, invoice.currency, 'pt_BR') }}</span></div>
            <div class="row"><span>Bruto (BRL)</span><span>{{ format_currency(invoice.amounts_snapshot.gross_brl, 'BRL', 'pt_BR') }}</span></div>
            <div class="row"><span>Spread</span><span>{{ format_currency(invoice.amounts_snapshot.spread_brl, 'BRL', 'pt_BR') }}</span></div>
            <div class="row"><span>IOF</span><span>{{ format_currency(invoice.amounts_snapshot.iof_brl, 'BRL', 'pt_BR') }}</span></div>
            <div class="row total"><span>Líquido (BRL)</span><span>{{ format_currency(invoice.amounts_snapshot.net_brl, 'BRL', 'pt_BR') }}</span></div>
        </div>
        
        <div class="rate-info">
            <p>Taxa: {{ format_number(invoice.quote_snapshot.rate, 'pt_BR') }} {{ invoice.currency }}/BRL</p>
            <p>Fonte: {{ invoice.quote_snapshot.rate_source }} ({{ format_date(invoice.quote_snapshot.quoted_at, 'pt_BR') }})</p>
            <p>Boletim: {{ invoice.quote_snapshot.bulletin }}</p>
            {% if invoice.quote_snapshot.stale %}
            <p class="stale-warning">⚠ Cotação com mais de 24h</p>
            {% endif %}
        </div>
    </section>
    
    <footer>
        <div class="bank-details">
            <h3>Dados Bancários</h3>
            <p>Banco: {{ invoice.bank_snapshot.bank_name }} ({{ invoice.bank_snapshot.bank_code }})</p>
            <p>Agência: {{ invoice.bank_snapshot.branch }} | Conta: {{ invoice.bank_snapshot.account_number }}-{{ invoice.bank_snapshot.account_digit }}</p>
            <p>Titular: {{ invoice.bank_snapshot.account_holder }}</p>
            {% if invoice.bank_snapshot.swift_bic %}
            <p>SWIFT/BIC: {{ invoice.bank_snapshot.swift_bic }}</p>
            {% endif %}
        </div>
        
        <div class="notice">
            {{ notice_pt_br | safe }}
        </div>
        
        <div class="audit-trail">
            <p>Emitida em: {{ format_datetime(invoice.finalized_at, 'pt_BR') }}</p>
            <p>Locale: {{ invoice.locale }} | País cliente: {{ invoice.client_country_code }}</p>
        </div>
    </footer>
</body>
</html>
```

### 2.4 Template EN (`invoice_en.html`)

Estrutura idêntica, mas:
- Labels em inglês: "Provider", "Client", "Description", "Regime", "Quantity", "Amount", "Gross", "Spread", "IOF", "Net", "Rate", "Source", "Bulletin", "Bank Details", "Branch", "Account", "Holder", "Issued on", "Locale", "Client country"
- Formatação US: moeda `$ 1,234.56`, data `MM/DD/YYYY`, números `1,234.56`
- Notice legal em inglês (`_invoice_notice_en.html`)

### 2.5 Notice Legal (separado por idioma)

**`_invoice_notice_pt_br.html`:**
```jinja2
{% set notice_pt_br %}
<p><strong>Aviso Legal:</strong> Este documento é uma invoice de prestação de serviços, emitida conforme legislação brasileira vigente. Os valores apresentados incluem spread cambial e IOF conforme informados pelo usuário. A taxa de câmbio refere-se à cotação {{ invoice.quote_snapshot.rate_source }} de {{ format_date(invoice.quote_snapshot.quoted_at, 'pt_BR') }} (boletim {{ invoice.quote_snapshot.bulletin }}). {% if invoice.quote_snapshot.stale %}Atenção: cotação com mais de 24 horas.{% endif %} Este documento não substitui nota fiscal eletrônica (NF-e/NFS-e) quando exigida por lei.</p>
{% endset %}
```

**`_invoice_notice_en.html`:**
```jinja2
{% set notice_en %}
<p><strong>Legal Notice:</strong> This document is a service invoice issued under applicable Brazilian legislation. Amounts include foreign exchange spread and IOF as informed by the user. The exchange rate refers to {{ invoice.quote_snapshot.rate_source }} quotation dated {{ format_date(invoice.quote_snapshot.quoted_at, 'en_US') }} (bulletin {{ invoice.quote_snapshot.bulletin }}). {% if invoice.quote_snapshot.stale %}Warning: quotation older than 24 hours.{% endif %} This document does not replace electronic fiscal invoice (NF-e/NFS-e) when required by law.</p>
{% endset %}
```

---

## 3. Lógica de Seleção de Template (Backend)

**Localização:** `src/backend/services/invoice_pdf.py`

```python
def select_invoice_template(locale: str) -> str:
    """
    Seleciona template baseado no locale snapshoteado na invoice.
    locale ∈ {'pt-BR', 'en'} — válido por construção (SPEC-020 finalização).
    """
    if locale == "pt-BR":
        return "invoice_pt_br.html"
    return "invoice_en.html"  # en ou qualquer outro → en

async def generate_invoice_pdf(invoice_id: UUID, db: AsyncSession) -> bytes:
    invoice = await get_invoice_with_snapshots(invoice_id, db)
    template_name = select_invoice_template(invoice.locale)
    
    # Renderiza com macros + notice do idioma correto
    template = env.get_template(template_name)
    html = template.render(invoice=invoice)
    
    # WeasyPrint para PDF
    pdf = weasyprint.HTML(string=html).write_pdf()
    return pdf
```

---

## 4. Validação de `country_code` (Frontend + Backend)

### 4.1 Cliente Cadastrado (`clients.country_code`)
- `NOT NULL`, DEFAULT 'BR', ISO 3166-1 válido
- Frontend: select com busca (typeahead) de países
- Backend: validação regex `^[A-Z]{2}$` + checagem contra tabela `countries` (ou lista estática)

### 4.2 Cliente Fictício (Dummy)
- **Obrigatório** no formulário de criação de invoice
- Se ausente → **400 validation_error**: `"client_country_code é obrigatório para cliente não cadastrado"`
- Não há default oculto (DEC-07)

---

## 5. Snapshot na Invoice Finalizada (SPEC-020)

Na finalização, a invoice recebe:

```python
invoice.locale = "pt-BR" if client_country_code == "BR" else "en"
invoice.client_country_code = client_country_code  # SEMPRE presente
# Ambos imutáveis após finalização
```

**Auditoria histórica:** Invoice emitida em EN não muda se cliente depois cadastra país BR.

---

## 6. Critérios de aceite e testes

- [ ] **AC-01:** Regra `BR`→`pt-BR`, demais→`en` implementada no backend (função `select_invoice_template`)
- [ ] **AC-02:** Templates `invoice_pt_br.html` e `invoice_en.html` separados; macros compartilhadas em `_invoice_macros.html`
- [ ] **AC-03:** Notice legal separado por idioma (`_invoice_notice_pt_br.html`, `_invoice_notice_en.html`)
- [ ] **AC-04:** Cliente fictício **exige** `country_code` (400 se ausente); não há default
- [ ] **AC-05:** `locale` + `client_country_code` snapshoteados na invoice finalizada (imutáveis)
- [ ] **AC-06:** Formatação correta: PT-BR (R$ 1.234,56; DD/MM/YYYY; 1.234,56) vs EN ($ 1,234.56; MM/DD/YYYY; 1,234.56)
- [ ] **AC-07:** Cotação, valores, notice legal renderizados no idioma correto
- [ ] **AC-08:** PDF gerado via WeasyPrint com CSS A4 correto; `tabular-nums` em valores
- [ ] **AC-09:** Erros da API e interface permanecem PT-BR (i18n integral fora de escopo)
- [ ] **AC-10:** Testes: cliente BR → pt-BR; cliente US → en; fictício sem country_code → 400; snapshot imutável

---

## 7. Rastreabilidade

| Referência | Fonte |
|------------|-------|
| CR-002 Gate D, CR2-D05 | `docs/decisoes/ccb-CR-002.md` |
| DEC-07 bilíngue | `docs/decisoes/ccb-lgpd-decisoes.md` |
| SPEC-019 (country_code) | `.ai/specs/spec-019-client-directory-v1.spec.md` |
| SPEC-020 (locale snapshot) | `.ai/specs/spec-020-simulation-invoice-history-v1.spec.md` |
| SPEC-022 (P-15) | `.ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md` |
| spec-prop-017 §12.4 | `docs/especificacoes/spec-prop-017-conta-multiusuario.md` |
| Constitution v1.3.0 | `constitution.md` (Art. 1.2, P-15, P-10) |
| LGPD art. 7º V, 9º | Informação clara e acessível |

---

## 8. Fora de escopo (YAGNI)

- i18n integral da interface/erros (apenas invoice bilíngue)
- Idiomas além de PT-BR/EN (futuro: ES, FR, PT-PT)
- Tradução automática via API (Google Translate, etc.) — soberania P-03
- Locale baseado em Accept-Language header — regra é `country_code` canônico
- Templates para NF-e/NFS-e — fora MVP
- Right-to-left (RTL) para idiomas árabes/hebraicos — futuro

---

## 9. Metadados de emissão

- **Avaliador primário:** `agent-frontend-dev` + `agent-sdd-specialist`
- **Ratificação:** CCB/GP via CR-002 Gate D (2026-11-14)
- **Dependências:** SPEC-019, SPEC-020, SPEC-022
- **parcel.dod:** true
- **Data da emissão:** 2026-11-14
- **Status da spec:** ativa / ratificada

---

## CHANGELOG

| Versão | Data | Task/Handoff | Mudança |
|--------|------|--------------|---------|
| 1.0.0 | 2026-11-14 | CR-002 Gate D / agent-frontend-dev + agent-sdd-specialist | Emissão inicial, ratificada. Regra país→locale (BR→pt-BR, demais→en), templates separados, macros compartilhadas, notice legal por idioma, fictício exige country_code, snapshot imutável. |

---

## CAMADAS FUNDAMENTAIS — MAPA (TA-0031)

| Camada | Seção nesta spec | Estado |
|--------|------------------|--------|
| (a) cabeçalho | frontmatter (`spec_id: spec-021`, `version: 1.0.0`, `status: ratificada`) | aplicada |
| (b) Contexto/origem | §1 + frontmatter `origin`/`task` | aplicada |
| (c) Resolução de conflitos | §1 (regra determinística, templates separados, macros) | aplicada |
| (d) Corpo de decisões/requisitos/contratos | §2 (templates), §3 (seleção backend), §4 (validação), §5 (snapshot) | aplicada |
| (e) Critérios de aceite/testes | §6 (AC-01..AC-10) | aplicada |
| (f) Rastreabilidade | §7 + frontmatter `trace` | aplicada |
| (g) Fora de escopo (YAGNI) | §8 | aplicada |
| (h) Changelog | CHANGELOG | aplicada |