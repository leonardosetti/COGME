---
id: docs-change-requests-cr-005-client-directory
title: CR-005 — Carteira de clientes e estado ativo/inativo
type: change-request
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md (CR-002, SPEC-019)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md (PROP-017, §12.2 tabela clients)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9.1-9.3)
- .ai/specs/spec-007-invoice-data-model-v1.spec.md (client snapshot em invoice)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (LGPD condicional)
- .ai/specs/spec-023-ui-spec-v1.spec.md (formulário de cliente)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- change-request
- cliente
- carteira
- lgpd
cr-number: CR-005
impacto: medio
prazo-analise-gp: '2026-11-16'
decisao-ccb: pendente
instrumento: pendente
github-issue: '#38'
parent-cr: CR-002
---

# CR-005 — Carteira de clientes e estado ativo/inativo

## 1. Origem e relação com CR-002

Esta CR deriva da **CR-002** (§5, §12, §13) e corresponde à **SPEC-019** da proposta **PROP-017**. Isola a carteira de clientes (cadastro opcional, estado ativo/inativo, snapshot em invoice) para tramitação independente, pois envolve dados de terceiros e decisões LGPD sobre base legal art. 7º V.

## 2. Escopo desta CR

### 2.1 Funcionalidades

- Cadastro opcional de cliente (não obrigatório para emitir invoice):
  - Nome*, documento (CPF/CNPJ), endereço, país (ISO 3166-1)
  - Estado: `is_active` (boolean, default true), `deactivated_at` (timestamp)
  - Inativação por contrato suspenso ou encerrado; reativação permitida
- Cliente fictício (dummy) admitido sem criar registro na carteira:
  - Exige país explícito no request (sem inferência silenciosa)
  - Não persiste em `clients`; usado apenas para a invoice pontual
- Snapshot do cliente na invoice finalizada:
  - Copia nome, documento, endereço, país para `invoices` (imutável)
  - Alteração posterior do cadastro **não** afeta invoices finalizadas
- Listagem paginada, filtro por estado ativo/inativo, busca por nome/documento

### 2.2 Modelo de dados (tabela nova)

| Tabela | Campos essenciais | Constraints |
|--------|-------------------|-------------|
| `clients` | `id UUID PK`, `owner_user_id FK`, `name`, `tax_id`, `address_line1`, `address_line2`, `neighborhood`, `city`, `state`, `postal_code`, `country_code`, `is_active`, `deactivated_at`, `created_at`, `updated_at` | `is_active NOT NULL DEFAULT true`; `country_code` ISO 3166-1; FK `owner_user_id` explícita `ON DELETE CASCADE`; índice em `(owner_user_id, is_active)` |

### 2.3 Regras de integridade

- `owner_user_id` obrigatório; usuário só acessa próprios clientes (autorização por sessão).
- Cliente inativo não aparece em autocomplete/sugestão, mas permanece consultável para histórico.
- Snapshot na invoice: ao finalizar, copiar cliente para `invoices.client_snapshot` (imutável).
- Cliente fictício: não cria registro em `clients`; país é campo obrigatório no request de invoice.
- LGPD: dados de terceiros (cliente) — base legal art. 7º V (execução de contrato) — decisão CR2-D02/D03.

## 3. Decisões requeridas do CCB/PO

| ID | Decisão | Responsável |
|----|---------|-------------|
| CR5-D01 | Base legal LGPD para dados de cliente (art. 7º V confirmada?) | `agent-compliance-governance` + CCB |
| CR5-D02 | Retenção de clientes inativos vs. exclusão | `agent-compliance-governance` + CCB |
| CR5-D03 | Autocomplete/sugestão: incluir apenas ativos? | `agent-frontend-dev` + `agent-business-analysis-specialist` |

## 4. Artefatos afetados

| Artefato | Ação |
|----------|------|
| `constitution.md` | emenda para admitir carteira de clientes (Art. 1.2) |
| `spec-007` | adicionar `client_id` e `client_snapshot` em `invoices` |
| `spec-004` | rotas CRUD `/clients/*` |
| `spec-023` | tela de carteira de clientes, autocomplete no formulário de invoice |
| `spec-015` | LGPD: minimização, base legal art. 7º V, retenção |
| Banco/Alembic | 1 migration `upgrade`/`downgrade` com FK e índices |
| Segurança | autorização por owner, nenhum dado de terceiro em log |

## 5. Spec proposta

**SPEC-019 — `client-directory-v1`** (em `docs/especificacoes/spec-prop-020-client-directory.md`)

- Status: **draft** (em avaliação)
- Agente avaliador primário: `agent-business-analysis-specialist`
- Consultados: `agent-dba`, `agent-compliance-governance`, `agent-digital-security`, `agent-sdd-specialist`, `agent-frontend-dev`, `agent-qa-sdet`

## 6. Critérios para encerrar a CR

- [ ] Issue publicada com label `change-request` e link para esta CR e PROP-020.
- [ ] Parecer LGPD emitido por `agent-compliance-governance`.
- [ ] Decisões CR5-D01..D03 deliberadas e registradas.
- [ ] SPEC-019 promovida a spec oficial ou explicitamente recusada.
- [ ] Emenda constitucional ratificada se alterar Art. 1.2.

## 7. Rollback

Até a ratificação, nenhuma migration, rota ou código de clientes é autorizado. Se recusada, a proposta associada será marcada `obsoleto`/`arquivado`.

## CHANGELOG

- 1.0.0 — 2026-11-14: CR derivada da CR-002 para isolar domínio de carteira de clientes; modelo de 1 tabela, snapshot em invoice, cliente fictício, LGPD art. 7º V, 3 decisões bloqueadoras, spec proposta SPEC-019. Status ativo, aguardando pareceres e decisão CCB.