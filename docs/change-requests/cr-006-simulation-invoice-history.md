---
id: docs-change-requests-cr-006-simulation-invoice-history
title: CR-006 — Simulações salvas, histórico e ciclo de vida das invoices
type: change-request
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md (CR-002, SPEC-020)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md (PROP-017, §12.2 tabelas simulations, emenda invoices)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9.1-9.3)
- .ai/specs/spec-004-backend-mvp-v1.spec.md (contrato invoice, recálculo server-side)
- .ai/specs/spec-007-invoice-data-model-v1.spec.md (modelo canônico invoice)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (LGPD condicional)
- .ai/specs/spec-023-ui-spec-v1.spec.md (telas de histórico, rascunho/finalizada)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- change-request
- simulacao
- historico
- invoice
- lifecycle
cr-number: CR-006
impacto: alto
prazo-analise-gp: '2026-11-16'
decisao-ccb: pendente
instrumento: pendente
github-issue: '#39'
parent-cr: CR-002
---

# CR-006 — Simulações salvas, histórico e ciclo de vida das invoices

## 1. Origem e relação com CR-002

Esta CR deriva da **CR-002** (§5, §12, §13) e corresponde à **SPEC-020** da proposta **PROP-017**. Isola o histórico de simulações (opt-in), o ciclo de vida da invoice (rascunho/finalizada), a clonagem e a numeração, pois altera o modelo canônico de `invoices` (SPEC-007) e exige decisão do CCB sobre US-016/US-017.

## 2. Escopo desta CR

### 2.1 Funcionalidades

- **Simulação salva (opt-in):**
  - Usuário escolhe explicitamente salvar a simulação após o cálculo
  - Persiste entrada validada + resultado recalculado + cotação usada (rate, source, quoted_at, bulletin, stale)
  - Não recalcula com taxa vigente ao listar histórico; mostra snapshot da época
  - Listagem paginada ordenada por data decrescente

- **Ciclo de vida da invoice (condicionado à ratificação CCB — US-016/US-017):**
  - `status ∈ {draft, finalized}`
  - Rascunho: editável, pode ser salvo múltiplas vezes
  - Finalizada: **imutável**; nenhuma alteração permitida
  - Finalização copia snapshots completos: prestadora, banco, cliente, simulação/cotação, valores, locale
  - `finalized_at` timestamp obrigatório na transição draft → finalized

- **Numeração e clonagem (condicionado à ratificação CCB — US-017):**
  - Numeração: solução sem PostgreSQL Sequence (C-04, GAP-06) — a ratificar
  - Clonagem: invoice finalizada → novo rascunho com novo número único, `supersedes_invoice_id`, data de emissão atual

- **Histórico unificado:**
  - Listagem combinada de simulações salvas e invoices (rascunho + finalizadas)
  - Filtros: tipo, status, período, cliente
  - Acesso apenas aos próprios recursos (`owner_user_id` da sessão)

### 2.2 Modelo de dados

| Tabela | Alteração | Campos adicionais |
|--------|-----------|-------------------|
| `simulations` | **nova** | `id UUID PK`, `owner_user_id FK`, `currency`, `regime`, `amount`, `quantity`, `spread_pct`, `iof_pct`, `gross_foreign`, `gross_brl`, `spread_brl`, `iof_brl`, `net_brl`, `effective_rate`, `rate`, `rate_source`, `quoted_at`, `bulletin`, `stale`, `created_at` |
| `invoices` | **emenda** (SPEC-007) | `owner_user_id FK`, `client_id FK`, `simulation_id FK`, `status`, `locale`, `client_country_code`, `finalized_at`, `supersedes_invoice_id` |

Constraints em `invoices`:
- `owner_user_id NOT NULL`
- `status ∈ {draft,finalized}` (CHECK)
- `locale ∈ {pt-BR,en}` (CHECK)
- `finalized_at` NOT NULL quando `status = finalized`
- `supersedes_invoice_id` FK auto-referenciada, NULL permitido
- FKs explícitas com `ON DELETE RESTRICT` para `client_id`, `simulation_id`, `owner_user_id`

### 2.3 Regras de integridade

- Simulação só persiste quando usuário clica "Salvar simulação" (opt-in explícito).
- Invoice rascunho pode ser editada; finalizada é somente leitura (fail-closed na API).
- Finalização é transação atômica: cria/atualiza invoice + snapshots + `finalized_at`.
- Clonagem cria novo rascunho com `supersedes_invoice_id` apontando para a original.
- Listagens filtram por `owner_user_id` da sessão; nenhum recurso de outro usuário acessível.
- LGPD: simulações e invoices contêm dados pessoais — decisões CR2-D02/D03/D06.

## 3. Decisões requeridas do CCB/PO

| ID | Decisão | Responsável |
|----|---------|-------------|
| CR6-D01 | Ratificar US-016 (Rascunho/Finalizada) e US-017 (Clonagem) | CCB/PO |
| CR6-D02 | Solução de numeração de invoice (sem Sequence) | `agent-dba` + CCB |
| CR6-D03 | Opt-in de simulação: botão dedicado ou checkbox no formulário? | `agent-frontend-dev` + `agent-business-analysis-specialist` |
| CR6-D04 | Retenção de simulações salvas vs. exclusão | `agent-compliance-governance` + CCB |

## 4. Artefatos afetados

| Artefato | Ação |
|----------|------|
| `constitution.md` | emenda para admitir histórico de simulações e ciclo invoice (Art. 1.2) |
| `spec-004` | rotas `/simulations/*`, emenda `/invoice` com status, clone, listagem |
| `spec-007` | adicionar owner, status, locale, client_id, simulation_id, finalized_at, supersedes_invoice_id |
| `spec-008` | telas de histórico, rascunho, finalizada, clone, numeração |
| `spec-015` | LGPD: retenção, minimização, rota de erase |
| `spec-023` | UI de histórico unificado, toggle rascunho/finalizada |
| Banco/Alembic | 1 migration nova (`simulations`) + 1 emenda (`invoices`) com `upgrade`/`downgrade` |
| Segurança | autorização por owner, imutabilidade de finalizada testada |

## 5. Spec proposta

**SPEC-020 — `simulation-invoice-history-v1`** (em `docs/especificacoes/spec-prop-021-simulation-invoice-history.md`)

- Status: **draft** (em avaliação)
- Agente avaliador primário: `agent-sdd-specialist`
- Consultados: `agent-dba`, `agent-compliance-governance`, `agent-digital-security`, `agent-business-analysis-specialist`, `agent-frontend-dev`, `agent-qa-sdet`

## 6. Critérios para encerrar a CR

- [ ] Issue publicada com label `change-request` e link para esta CR e PROP-021.
- [ ] Ratificação de US-016/US-017 pelo CCB.
- [ ] Parecer de numeração emitido por `agent-dba`.
- [ ] Parecer LGPD emitido por `agent-compliance-governance`.
- [ ] Decisões CR6-D01..D04 deliberadas e registradas.
- [ ] SPEC-020 promovida a spec oficial ou explicitamente recusada.
- [ ] Emenda constitucional ratificada se alterar Art. 1.2.

## 7. Rollback

Até a ratificação, nenhuma migration, rota ou código de histórico/ciclo invoice é autorizado. Se recusada, a proposta associada será marcada `obsoleto`/`arquivado`.

## CHANGELOG

- 1.0.0 — 2026-11-14: CR derivada da CR-002 para isolar domínio de simulações/histórico/ciclo invoice; tabela simulations nova, emenda invoices, status draft/finalized, clone, numeração, 4 decisões bloqueadoras, spec proposta SPEC-020. Status ativo, aguardando pareceres e decisão CCB.