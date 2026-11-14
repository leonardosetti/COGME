---
id: docs-change-requests-cr-007-invoice-bilingual
title: CR-007 — Invoice bilíngue PT-BR / EN
type: change-request
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md (CR-002, SPEC-021)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md (PROP-017, §12.4)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 9.1-9.3)
- .ai/specs/spec-007-invoice-data-model-v1.spec.md (locale em invoice)
- .ai/specs/spec-008-frontend-web-responsive-v1.spec.md (i18n fora de escopo do MVP)
- .ai/specs/spec-023-ui-spec-v1.spec.md (PDF template)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- change-request
- invoice
- i18n
- bilingual
cr-number: CR-007
impacto: medio
prazo-analise-gp: '2026-11-16'
decisao-ccb: pendente
instrumento: pendente
github-issue: '#40'
parent-cr: CR-002
---

# CR-007 — Invoice bilíngue PT-BR / EN

## 1. Origem e relação com CR-002

Esta CR deriva da **CR-002** (§5, §12, §13) e corresponde à **SPEC-021** da proposta **PROP-017**. Isola a regra de idioma da invoice (PT-BR para cliente BR, EN para estrangeiro) e os templates bilíngues, pois o MVP atual declara i18n multi-idioma como fora de escopo (OS-09, `spec-008:242`).

## 2. Escopo desta CR

### 2.1 Funcionalidades

- **Regra canônica de idioma:** derivada do país do cliente (`client.country_code`):
  - `BR` → `pt-BR`
  - Qualquer outro código ISO 3166-1 → `en`
- **Cliente fictício (dummy):** exige país explícito no request; sem país = request inválido (400).
- **Templates separados:**
  - `invoice_pt_br.html` — labels, moeda, datas, notice em português
  - `invoice_en.html` — labels, currency, dates, notice em inglês
- **Snapshot na invoice:** `locale` e `client_country_code` gravados na invoice finalizada para auditoria histórica.
- **Erros da API e interface do produto:** permanecem em PT-BR; apenas o PDF da invoice é bilíngue.

### 2.2 Modelo de dados

Emenda de `invoices` (já prevista na CR-006):
- `locale` — `CHECK (locale IN ('pt-BR','en'))`
- `client_country_code` — `CHAR(2)` ISO 3166-1

### 2.3 Regras de integridade

- `locale` é derivado automaticamente no backend a partir de `client.country_code`; **não aceito do cliente**.
- Invoice finalizada registra o `locale` usado; alteração posterior de país do cliente não afeta invoice já emitida.
- Cliente fictício: request sem `country_code` é rejeitado (400 validation_error).
- Templates Jinja2 separados; compartilham lógica de formatação (valores, datas) via macros.
- Notice legal traduzida e mantida integral em ambos os idiomas.
- LGPD: idioma não é dado pessoal; decisão CR2-D05.

## 3. Decisões requeridas do CCB/PO

| ID | Decisão | Responsável |
|----|---------|-------------|
| CR7-D01 | Regra definitiva: país do cliente como fonte canônica (confirmada?) | CCB/PO |
| CR7-D02 | Tradução do notice legal validada por revisão jurídica? | `agent-compliance-governance` + jurídico |
| CR7-D03 | Suporte a outros idiomas no futuro (ES, FR, etc.) — YAGNI ou planejado? | CCB/PO |

## 4. Artefatos afetados

| Artefato | Ação |
|----------|------|
| `constitution.md` | emenda para admitir invoice bilíngue (Art. 1.2) |
| `spec-007` | adicionar `locale` e `client_country_code` em `invoices` |
| `spec-004` | derivar `locale` no backend; templates separados |
| `spec-008` | i18n integral permanece FORA; apenas PDF bilíngue |
| `spec-023` | templates `invoice_pt_br.html` e `invoice_en.html` |
| `spec-015` | LGPD: idioma não é PII; sem impacto em retenção/erase |
| Banco/Alembic | emenda `invoices` (já na CR-006) adiciona `locale`, `client_country_code` |
| Frontend | validação de país obrigatório para cliente fictício |

## 5. Spec proposta

**SPEC-021 — `invoice-bilingual-v1`** (em `docs/especificacoes/spec-prop-022-invoice-bilingual.md`)

- Status: **draft** (em avaliação)
- Agente avaliador primário: `agent-frontend-dev`
- Consultados: `agent-sdd-specialist`, `agent-compliance-governance`, `agent-dba`, `agent-business-analysis-specialist`, `agent-qa-sdet`

## 6. Critérios para encerrar a CR

- [ ] Issue publicada com label `change-request` e link para esta CR e PROP-022.
- [ ] Tradução do notice legal validada.
- [ ] Decisões CR7-D01..D03 deliberadas e registradas.
- [ ] SPEC-021 promovida a spec oficial ou explicitamente recusada.
- [ ] Emenda constitucional ratificada se alterar Art. 1.2.

## 7. Rollback

Até a ratificação, nenhum template bilíngue ou lógica de locale é autorizado. Se recusada, a proposta associada será marcada `obsoleto`/`arquivado`.

## CHANGELOG

- 1.0.0 — 2026-11-14: CR derivada da CR-002 para isolar domínio de invoice bilíngue; regra país→locale, templates separados, snapshot em invoice, 3 decisões bloqueadoras, spec proposta SPEC-021. Status ativo, aguardando pareceres e decisão CCB.