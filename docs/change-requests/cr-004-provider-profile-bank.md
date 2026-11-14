---
id: docs-change-requests-cr-004-provider-profile-bank
title: CR-004 — Perfil da prestadora e contas bancárias de depósito
type: change-request
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md (CR-002, SPEC-018)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md (PROP-017, §12.2 tabelas provider_profiles, provider_bank_accounts)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9.1-9.3)
- .ai/specs/spec-007-invoice-data-model-v1.spec.md (dados bancários snapshot)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (LGPD condicional)
- .ai/specs/spec-023-ui-spec-v1.spec.md (formulários de perfil/banco)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- change-request
- perfil
- prestadora
- contas-bancarias
- lgpd
cr-number: CR-004
impacto: alto
prazo-analise-gp: '2026-11-16'
decisao-ccb: pendente
instrumento: pendente
github-issue: '#37'
parent-cr: CR-002
---

# CR-004 — Perfil da prestadora e contas bancárias de depósito

## 1. Origem e relação com CR-002

Esta CR deriva da **CR-002** (§5, §12, §13) e corresponde à **SPEC-018** da proposta **PROP-017**. Isola o cadastro da empresa prestadora (MEI/PJ), CNPJ, endereço e contas bancárias para wire transfer, pois são dados sensíveis financeiros que exigem parecer LGPD e validação de `agent-dba` antes da implementação.

## 2. Escopo desta CR

### 2.1 Funcionalidades

- Perfil da prestadora vinculado 1:1 ao `users.id`:
  - Razão social / nome fantasia
  - Categoria: `mei` ou `legal_entity`
  - CNPJ (obrigatório apenas para `legal_entity`; validação dígito verificador)
  - Endereço completo (logradouro, número, complemento, bairro, cidade, UF, CEP, país)
- Contas bancárias de depósito (1:N por usuário):
  - Tipo: `checking`, `savings`, `payment`, `wire`
  - Banco (código COMPE, nome)
  - Agência, conta, dígito
  - SWIFT/BIC (para wire internacional)
  - IBAN (para SEPA/internacional)
  - Titular da conta
  - Moeda padrão da conta
  - Flag `is_primary` (uma conta primária por usuário)
- Snapshot dos dados da prestadora e da conta bancária primária na invoice finalizada
- Dados bancários sensíveis: armazenamento com controles de acesso restritos, nunca em logs

### 2.2 Modelo de dados (tabelas novas)

| Tabela | Campos essenciais | Constraints |
|--------|-------------------|-------------|
| `provider_profiles` | `user_id UUID PK/FK`, `legal_name`, `category`, `cnpj`, `address_line1`, `address_line2`, `neighborhood`, `city`, `state`, `postal_code`, `country_code`, `created_at`, `updated_at` | `category ∈ {mei,legal_entity}`; CNPJ obrigatório se `legal_entity`; `country_code` ISO 3166-1 |
| `provider_bank_accounts` | `id UUID PK`, `user_id FK`, `account_type`, `bank_code`, `bank_name`, `branch`, `account_number`, `account_digit`, `swift_bic`, `iban`, `account_holder`, `currency`, `is_primary`, `created_at`, `updated_at` | `account_type ∈ {checking,savings,payment,wire}`; uma conta primária por usuário (`UNIQUE(user_id) WHERE is_primary`); FK explícita `ON DELETE CASCADE` |

### 2.3 Regras de integridade

- `provider_profiles` tem PK/FK compartilhada com `users.id` (one-to-one).
- CNPJ válido apenas dígitos; dígito verificador validado application-side.
- Snapshot na invoice: ao finalizar, copiar prestadora + conta primária para `invoices` (imutável).
- Alteração posterior do perfil/banco **não** altera invoices já finalizadas.
- Dados bancários nunca em logs, seeds, fixtures ou exemplos técnicos.
- LGPD: base legal para dados bancários — decisão CR2-D02/D03.

## 3. Decisões requeridas do CCB/PO

| ID | Decisão | Responsável |
|----|---------|-------------|
| CR4-D01 | Conjunto mínimo de campos bancários por tipo de transferência (wire vs. nacional) | `agent-dba` + `agent-business-analysis-specialist` + CCB |
| CR4-D02 | Criptografia em repouso para campos sensíveis (conta, SWIFT, IBAN) | `agent-digital-security` + CCB |
| CR4-D03 | Validação de CNPJ: apenas dígito verificador ou consulta ReceitaWS? | `agent-dba` + CCB |
| CR4-D04 | Snapshot: copiar todos os campos ou apenas primários na invoice? | `agent-sdd-specialist` + CCB |

## 4. Artefatos afetados

| Artefato | Ação |
|----------|------|
| `constitution.md` | emenda para admitir dados de prestadora/banco (Art. 1.2) |
| `spec-007` | adicionar colunas de snapshot de prestadora/banco em `invoices` |
| `spec-004` | rotas CRUD `/provider/*`, `/bank/*` |
| `spec-023` | telas de perfil da prestadora e contas bancárias |
| `spec-015` | LGPD: minimização, base legal, retenção de dados bancários |
| Banco/Alembic | 2 migrations `upgrade`/`downgrade` com FKs e constraints |
| Segurança | criptografia em repouso, acesso restrito, auditoria de acesso |

## 5. Spec proposta

**SPEC-018 — `provider-profile-bank-account-v1`** (em `docs/especificacoes/spec-prop-019-provider-profile-bank.md`)

- Status: **draft** (em avaliação)
- Agente avaliador primário: `agent-dba`
- Consultados: `agent-business-analysis-specialist`, `agent-digital-security`, `agent-compliance-governance`, `agent-sdd-specialist`, `agent-frontend-dev`, `agent-qa-sdet`

## 6. Critérios para encerrar a CR

- [ ] Issue publicada com label `change-request` e link para esta CR e PROP-019.
- [ ] Parecer de modelagem de dados emitido por `agent-dba`.
- [ ] Parecer LGPD emitido por `agent-compliance-governance`.
- [ ] Parecer de segurança emitido por `agent-digital-security`.
- [ ] Decisões CR4-D01..D04 deliberadas e registradas.
- [ ] SPEC-018 promovida a spec oficial ou explicitamente recusada.
- [ ] Emenda constitucional ratificada se alterar Art. 1.2.

## 7. Rollback

Até a ratificação, nenhuma migration, rota ou código de prestadora/banco é autorizado. Se recusada, a proposta associada será marcada `obsoleto`/`arquivado`.

## CHANGELOG

- 1.0.0 — 2026-11-14: CR derivada da CR-002 para isolar domínio de prestadora/banco; modelo de 2 tabelas, snapshot em invoice, criptografia em repouso, 4 decisões bloqueadoras, spec proposta SPEC-018. Status ativo, aguardando pareceres e decisão CCB.