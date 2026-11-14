---
id: docs-especificacoes-spec-prop-021-simulation-invoice-history
title: Proposta de Spec — Simulações salvas, histórico e ciclo de vida das invoices
type: spec
version: 0.1.0
status: draft
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-006-simulation-invoice-history.md
- docs/conhecimento/templates/proposta-spec-template.md
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9)
- .ai/specs/spec-004-backend-mvp-v1.spec.md
- .ai/specs/spec-007-invoice-data-model-v1.spec.md
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md
- .ai/specs/spec-023-ui-spec-v1.spec.md
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- proposta
- spec
- simulacao
- historico
- invoice
- lifecycle
spec-id: PROP-021
camada: produto
estado-implementacao: nao-iniciada
rastreia-req:
- CR-006
testes-vinculados: []
---

# Proposta de Spec — Simulações salvas, histórico e ciclo de vida das invoices

## 1. Ideia / Draft

**Título da proposta:** Simulações salvas (opt-in), histórico unificado e ciclo de vida das invoices (rascunho/finalizada, clonagem)

**Autor:** PO/GP — derivação da CR-006 (2026-11-14)

**Data:** 2026-11-14

**Contexto / problema que resolve:**

O MVP atual gera invoice PDF sem persistência (`spec-004:126`) e sem histórico de simulações (`spec-004:31` fora de escopo). US-016/US-017 (rascunho/finalizada, clonagem) são candidatas condicionais (`spec-002:178-179`). A CR-006 isola este domínio para ratificação do CCB e emenda do modelo canônico `invoices` (SPEC-007).

**Descrição breve da solução proposta:**

- Simulação salva por opt-in explícito (botão "Salvar simulação"): persiste entrada + resultado + cotação snapshot
- Invoice com `status ∈ {draft,finalized}`: rascunho editável, finalizada imutável
- Finalização atômica: copia snapshots completos (prestadora, banco, cliente, simulação/cotação, valores, locale)
- Clonagem: finalizada → novo rascunho com novo número, `supersedes_invoice_id`, data atual
- Histórico unificado: listagem paginada de simulações salvas + invoices (filtrável por tipo, status, período, cliente)
- Numeração: solução sem PostgreSQL Sequence (C-04, GAP-06) — a ratificar

**Escopo inicial (DENTRO):**

- Tabela `simulations` nova com snapshot tipado
- Emenda `invoices`: `owner_user_id`, `client_id`, `simulation_id`, `status`, `locale`, `client_country_code`, `finalized_at`, `supersedes_invoice_id`
- Opt-in de simulação (não automático)
- Status draft/finalized com transição irreversível
- Clonagem condicionada a US-017 ratificada
- Numeração sem Sequence — a ratificar
- Acesso apenas aos próprios recursos (`owner_user_id` da sessão)

**Fora de escopo (NÃO está):**

- Versionamento de rascunho (histórico de edições)
- Workflow de aprovação de invoice
- Envio automático de invoice por email
- Integração com contabilidade/ERP
- Dashboard analítico de simulações/invoices

## 2. Análise de Derivação Multi-Spec

**Resultado:** **Uma spec única** — domínio coeso de histórico/ciclo invoice com tabelas, status, snapshots e numeração próprios.

| Critério de Divisão | Aplica-se? | Justificativa |
|---|---:|---|
| Domínios técnicos disjuntos | Sim | Simulações, invoices, status, snapshots, numeração, clonagem |
| Ciclos de vida independentes | Parcial | Simulação salva é snapshot; invoice tem ciclo draft→finalized→clone |
| Requisitos regulatórios separados | Sim | LGPD em simulações/invoices; retenção/erase condicionada a CR-008 |
| Dependências com desenvolvimento paralelo | Sim | Depende de SPEC-017/018/019 e CR-008; pode especificar em paralelo |

**Spec derivada:** SPEC-020 — `simulation-invoice-history-v1` | Agente dono: `agent-sdd-specialist` + `agent-dba`

## 3. Viabilidade Técnica

| Critério | Avaliação | Observações |
|---|---|---|
| Tecnologias no stack? | Sim | PostgreSQL, SQLAlchemy, Alembic, transações atômicas |
| Nova dependência? | Não | Stack atual suficiente |
| Impacta arquitetura/contratos? | Sim, alto | Nova tabela, emenda `invoices` (SPEC-007), rotas, status, clonagem |
| Complexidade | Alta | Transações atômicas, imutabilidade, snapshots, numeração, LGPD |
| Riscos técnicos | Elevados | Inconsistência de snapshot, numeração duplicada, finalizada mutável, vazamento cross-user |

## 4. Viabilidade Negocial

| Critério | Avaliação | Observações |
|---|---|---|
| Alinhado com produto/roadmap? | Condicional | Requer ratificação US-016/017, emenda constitucional, CR-008 |
| Valor mensurável? | Sim | Histórico confiável, rascunho/editável, clone para correção |
| ROI | Positivo | Elimina re-emissão manual; base para relatórios futuros |
| Dependências externas | Sim | CCB (US-016/017), `agent-dba` (numeração), CR-008 (LGPD) |
| Urgência | Alta | Blocker para invoice usável em produção; após CR-008 |

## 5. Custo Técnico Estimado

| Item | Estimativa | Notas |
|---|---:|---|
| Desenvolvimento | 48–72 h | Tabela simulations, emenda invoices, status, snapshots, clone, numeração |
| Design/UX | 16–24 h | Telas histórico, rascunho, finalizada, clone, numeração |
| QA/testes | 24–36 h | Unit, integração, imutabilidade, autorização, snapshots, numeração |
| Parecer LGPD/numeração | 8–12 h | Retenção simulações, numeração sem Sequence |
| **Total** | **96–144 h** | |

## 6. Aderência ao Projeto / Produto

- **Constituição:** condicional — emenda Art. 1.2; ratificação US-016/017; Art. 7/9 (LGPD)
- **AGENT_TOPOLOGY:** `agent-sdd-specialist` (primário), `agent-dba`, `agent-compliance-governance`, `agent-digital-security`, `agent-business-analysis-specialist`, `agent-frontend-dev`, `agent-qa-sdet`
- **LGPD/GDPR:** não aderente até CR6-D01..D04 e CR8-D01..D06. Propõe minimização, retenção, erase.
- **FOSS/soberania:** compatível — stack local
- **YAGNI:** Opt-in, status binário, clone, numeração simples; versionamento/aprovação/email fora.

## 7. Critérios de Aceite para Promoção à Spec

- [x] Viabilidade técnica: **Sim**, com riscos declarados
- [x] Viabilidade negocial: **Parcial**, condicionada a ratificação US-016/017 e CR-008
- [ ] Custo aprovado pelo PO/PM
- [ ] Aderência constitucional: emenda ratificada
- [x] Riscos mapeados com mitigação
- [x] Done definido

**Resultado:** proposta em **draft**, em avaliação. Promoção depende de CR-006 e CR-008.

## 8. Agentes Responsáveis

**Avaliador primário:** `agent-sdd-specialist`
**Consultados:** `agent-dba`, `agent-compliance-governance`, `agent-digital-security`, `agent-business-analysis-specialist`, `agent-frontend-dev`, `agent-qa-sdet`
**Decisor:** CCB/GP

## 9. Modelo de Dados e Regras (Resumo)

### Tabela nova

| Tabela | PK | Campos-chave |
|---|---|---|
| `simulations` | `id UUID` | `owner_user_id FK`, `currency`, `regime`, `amount`, `quantity`, `spread_pct`, `iof_pct`, `gross_foreign`, `gross_brl`, `spread_brl`, `iof_brl`, `net_brl`, `effective_rate`, `rate`, `rate_source`, `quoted_at`, `bulletin`, `stale`, `created_at` |

### Emenda `invoices` (SPEC-007)

| Campo | Tipo | Constraint |
|---|---|---|
| `owner_user_id` | UUID FK | NOT NULL |
| `client_id` | UUID FK | `ON DELETE RESTRICT` |
| `simulation_id` | UUID FK | `ON DELETE RESTRICT` |
| `status` | VARCHAR | `CHECK IN ('draft','finalized')` |
| `locale` | VARCHAR | `CHECK IN ('pt-BR','en')` |
| `client_country_code` | CHAR(2) | ISO 3166-1 |
| `finalized_at` | TIMESTAMPTZ | NOT NULL quando `status='finalized'` |
| `supersedes_invoice_id` | UUID FK | Auto-ref, NULL permitido |

### Regras de integridade

- Simulação só persiste com opt-in explícito ("Salvar simulação")
- Invoice draft editável; finalized imutável (fail-closed na API)
- Finalização: transação atômica copia snapshots + `finalized_at`
- Clonagem: novo draft com `supersedes_invoice_id`, novo número, data atual
- Listagens filtram por `owner_user_id` da sessão
- LGPD: decisões CR2-D02/D03/D06 via CR-008

## 10. Decisões Bloqueadoras (CR-006)

| ID | Decisão | Responsável |
|---|---|---|
| CR6-D01 | Ratificar US-016 (Rascunho/Finalizada) e US-017 (Clonagem) | CCB/PO |
| CR6-D02 | Solução de numeração sem Sequence | `agent-dba` + CCB |
| CR6-D03 | Opt-in: botão dedicado ou checkbox? | `agent-frontend-dev` + `agent-business-analysis-specialist` |
| CR6-D04 | Retenção de simulações salvas | `agent-compliance-governance` + CCB |

## 11. Próximos Passos

| Ação | Responsável | Condição |
|---|---|---|
| Ratificar US-016/017 | CCB/GP | Antes de implementação |
| Emitir solução de numeração | `agent-dba` | Antes do CCB |
| Emitir parecer LGPD | `agent-compliance-governance` | Antes do CCB (via CR-008) |
| Deliberar CR6-D01..D04 | CCB/GP | Após pareceres |
| Emitir SPEC-020 oficial | `agent-sdd-specialist` | Após ratificação |

## CHANGELOG

- 0.1.0 — 2026-11-14: Proposta derivada da CR-006; tabela simulations, emenda invoices com status/locale/snapshots/clone, 4 decisões bloqueadoras, spec SPEC-020. Status draft.