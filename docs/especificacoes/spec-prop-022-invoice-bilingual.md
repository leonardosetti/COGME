---
id: docs-especificacoes-spec-prop-022-invoice-bilingual
title: Proposta de Spec — Invoice bilíngue PT-BR / EN
type: spec
version: 0.1.0
status: draft
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-007-invoice-bilingual.md
- docs/templates/proposta-spec-template.md
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 9)
- .ai/specs/spec-007-invoice-data-model-v1.spec.md
- .ai/specs/spec-008-frontend-web-responsive-v1.spec.md
- .ai/specs/spec-023-ui-spec-v1.spec.md
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- proposta
- spec
- invoice
- i18n
- bilingual
spec-id: PROP-022
camada: produto
estado-implementacao: nao-iniciada
rastreia-req:
- CR-007
testes-vinculados: []
---

# Proposta de Spec — Invoice bilíngue PT-BR / EN

## 1. Ideia / Draft

**Título da proposta:** Invoice bilíngue (PT-BR para cliente nacional, EN para estrangeiro)

**Autor:** PO/GP — derivação da CR-007 (2026-11-14)

**Data:** 2026-11-14

**Contexto / problema que resolve:**

O MVP atual emite invoice apenas em português (`spec-008:242` i18n multi-idioma fora de escopo). Clientes estrangeiros exigem invoice em inglês. A CR-007 isola a regra de idioma (país do cliente → locale) e os templates bilíngues para avaliação independente.

**Descrição breve da solução proposta:**

- Regra canônica: `client.country_code = BR` → `locale = pt-BR`; demais → `locale = en`
- Cliente fictício (dummy): exige `country_code` explícito; sem país = 400
- Dois templates Jinja2: `invoice_pt_br.html` e `invoice_en.html`
- `locale` e `client_country_code` gravados na invoice finalizada (snapshot)
- Erros da API e interface do produto permanecem em PT-BR; apenas PDF é bilíngue
- Notice legal traduzida e validada juridicamente

**Escopo inicial (DENTRO):**

- Derivação automática de `locale` no backend (não aceito do cliente)
- Templates separados com macros compartilhadas para formatação
- Snapshot `locale` + `client_country_code` na invoice finalizada
- Cliente fictício: `country_code` obrigatório
- Tradução do notice legal (validação jurídica CR7-D02)

**Fora de escopo (NÃO está):**

- i18n integral da interface e dos erros (OS-09, permanece FORA)
- Outros idiomas (ES, FR, etc.) — YAGNI (CR7-D03)
- Tradução dinâmica via gettext/i18n libraries
- Portal do cliente com invoice no idioma preferido

## 2. Análise de Derivação Multi-Spec

**Resultado:** **Uma spec única** — domínio coeso de locale/PDF com regra, templates e snapshot próprios.

| Critério de Divisão | Aplica-se? | Justificativa |
|---|---:|---|
| Domínios técnicos disjuntos | Sim | Templates PDF, macros Jinja2, regra de derivção, snapshot |
| Ciclos de vida independentes | Sim | Templates mudam independentemente do modelo de dados |
| Requisitos regulatórios separados | Não | Idioma não é PII; LGPD sem impacto direto |
| Dependências com desenvolvimento paralelo | Sim | Depende de CR-006 (emenda invoices) e CR-008; pode especificar em paralelo |

**Spec derivada:** SPEC-021 — `invoice-bilingual-v1` | Agente dono: `agent-frontend-dev` + `agent-sdd-specialist`

## 3. Viabilidade Técnica

| Critério | Avaliação | Observações |
|---|---|---|
| Tecnologias no stack? | Sim | Jinja2, WeasyPrint, DejaVu Sans (já no Docker) |
| Nova dependência? | Não | Stack atual suficiente |
| Impacta arquitetura/contratos? | Baixo-Médio | Dois templates, regra no backend, campos em invoice (já na CR-006) |
| Complexidade | Baixa-Média | Dois templates, macros compartilhadas, validação país |
| Riscos técnicos | Baixos | Tradução inconsistente, locale incorreto, notice legal não validado |

## 4. Viabilidade Negocial

| Critério | Avaliação | Observações |
|---|---|---|
| Alinhado com produto/roadmap? | Condicional | Requer emenda constitucional (OS-09 revertido parcialmente) |
| Valor mensurável? | Sim | Invoice profissional para cliente estrangeiro |
| ROI | Positivo | Habilita mercado internacional; baixo esforço |
| Dependências externas | Sim | CCB, validação jurídica notice EN, CR-006/CR-008 |
| Urgência | Média | Após CR-006 (emenda invoices) e CR-008 |

## 5. Custo Técnico Estimado

| Item | Estimativa | Notas |
|---|---:|---|
| Desenvolvimento | 16–24 h | Dois templates, macros, regra locale, validação país |
| Design/UX | 8–12 h | Layout EN, notice legal, testes visuais PDF |
| QA/testes | 8–12 h | PDF pt-BR/en, cliente BR/estrangeiro, fictício, snapshot |
| Validação jurídica | 4–8 h | Tradução notice legal |
| **Total** | **36–56 h** | |

## 6. Aderência ao Projeto / Produto

- **Constituição:** condicional — emenda Art. 1.2 (OS-09 parcialmente revertido)
- **AGENT_TOPOLOGY:** `agent-frontend-dev` (primário), `agent-sdd-specialist`, `agent-compliance-governance`, `agent-dba`, `agent-business-analysis-specialist`, `agent-qa-sdet`
- **LGPD/GDPR:** aderente — idioma não é PII; CR-008 decisions não afetam
- **FOSS/soberania:** compatível — Jinja2/WeasyPrint FOSS, fontes locais
- **YAGNI:** Apenas pt-BR/en; pt-BR para BR, en para demais; outros idiomas fora

## 7. Critérios de Aceite para Promoção à Spec

- [x] Viabilidade técnica: **Sim**
- [x] Viabilidade negocial: **Sim**, condicionada a emenda e validação jurídica
- [ ] Custo aprovado pelo PO/PM
- [ ] Aderência constitucional: emenda ratificada
- [x] Riscos mapeados com mitigação
- [x] Done definido

**Resultado:** proposta em **draft**, em avaliação. Promoção depende de CR-007, CR-006, CR-008.

## 8. Agentes Responsáveis

**Avaliador primário:** `agent-frontend-dev`
**Consultados:** `agent-sdd-specialist`, `agent-compliance-governance`, `agent-dba`, `agent-business-analysis-specialist`, `agent-qa-sdet`
**Decisor:** CCB/GP

## 9. Modelo de Dados e Regras (Resumo)

### Emenda `invoices` (já na CR-006)

| Campo | Tipo | Constraint |
|---|---|---|
| `locale` | VARCHAR | `CHECK IN ('pt-BR','en')` |
| `client_country_code` | CHAR(2) | ISO 3166-1 |

### Regras

- `locale` derivado automaticamente: `client.country_code = 'BR' → 'pt-BR'`; senão `'en'`
- Não aceito do request; validação no backend
- Cliente fictício: `country_code` obrigatório; sem país = 400
- Snapshot: `locale` + `client_country_code` gravados na invoice finalizada
- Templates: `invoice_pt_br.html` e `invoice_en.html` com macros compartilhadas
- Notice legal traduzida (validação CR7-D02)
- Erros API e UI: permanecem PT-BR

## 10. Decisões Bloqueadoras (CR-007)

| ID | Decisão | Responsável |
|---|---|---|
| CR7-D01 | Regra país→locale confirmada? | CCB/PO |
| CR7-D02 | Tradução notice legal validada juridicamente? | `agent-compliance-governance` + jurídico |
| CR7-D03 | Outros idiomas (ES, FR) — YAGNI ou planejado? | CCB/PO |

## 11. Próximos Passos

| Ação | Responsável | Condição |
|---|---|---|
| Validar tradução notice legal | `agent-compliance-governance` + jurídico | Antes do CCB |
| Deliberar CR7-D01..D03 | CCB/GP | Após validação |
| Emitir SPEC-021 oficial | `agent-sdd-specialist` | Após ratificação |

## CHANGELOG

- 0.1.0 — 2026-11-14: Proposta derivada da CR-007; regra país→locale, dois templates Jinja2, snapshot em invoice, 3 decisões bloqueadoras, spec SPEC-021. Status draft.