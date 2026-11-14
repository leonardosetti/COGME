---
id: docs-change-requests-cr-008-account-lifecycle-privacy
title: CR-008 — Ciclo de vida da conta, dormência, exclusão e privacidade LGPD/GDPR
type: change-request
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md (CR-002, SPEC-022)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md (PROP-017, §12.5, §13 ordem de emissão)
- constitution.md (Arts. 1.1, 1.2, 1.3, 3, 5.1, 7, 9.1-9.3; P-02, P-03, P-04)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (D1-D7 condicionais)
- .ai/specs/spec-004-backend-mvp-v1.spec.md (LGPD logs, invoice nunca persistida)
- LGPD Lei 13.709/2018 (art. 4º I, 5º II, 6º I/III, 7º V, 11, 18)
- GDPR Regulamento (UE) 2016/679 (art. 3, 17, 25, 32, 44-50)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- change-request
- lifecycle
- privacidade
- lgpd
- gdpr
- dormencia
- exclusao
cr-number: CR-008
impacto: critico
prazo-analise-gp: '2026-11-15'
decisao-ccb: pendente
instrumento: pendente
github-issue: '#41'
parent-cr: CR-002
---

# CR-008 — Ciclo de vida da conta, dormência, exclusão e privacidade LGPD/GDPR

## 1. Origem e relação com CR-002

Esta CR deriva da **CR-002** (§5, §12, §13) e corresponde à **SPEC-022** da proposta **PROP-017**. **Deve ser resolvida primeiro** (ordem 1 em §13 da PROP-017), pois suas decisões de retenção, dormência, exclusão e bases legais LGPD/GDPR condicionam a implementação de todos os demais domínios (identidade, prestadora, clientes, histórico, invoice).

## 2. Escopo desta CR

### 2.1 Funcionalidades

- **Estados da conta:**
  - `active` — padrão; criação, login, uso normal
  - `dormant` — inativação por prazo ou solicitação; revoga sessões, bloqueia criação/alteração; dados permanecem conforme retenção ratificada
  - `deleted` — exclusão definitiva; remove usuário, aliases, sessões, tokens, perfil, banco, clientes, simulações, eventos de lifecycle

- **Dormência:**
  - Critério automático: inatividade por prazo a ratificar (ex.: 365 dias)
  - Critério manual: solicitação do titular
  - Efeito: revogação de todas as sessões; bloqueio de login, criação/alteração de recursos; leitura de histórico permitida
  - Reativação: exige reset de senha + verificação de identidade (email/CPF/CNPJ)

- **Exclusão definitiva:**
  - Revoga sessões e tokens
  - Remove: usuário, aliases, sessões, tokens de reset, perfil prestadora, contas bancárias, clientes, simulações, eventos de lifecycle
  - **Invoices finalizadas:** decisão CR2-D03 / CR8-D01 — retenção legal, anonimização ou eliminação
  - Log de evento `account_lifecycle_events` registra `DELETED` sem PII

- **Privacidade por design (LGPD art. 6º, 7º, 18; GDPR art. 17, 25):**
  - Minimização: coletar apenas o necessário (perfil, banco, cliente, simulação opt-in)
  - Logs sem PII, sem valores, sem corpo de requisição (herda `spec-004:126`)
  - Direito ao esquecimento: operação local, sem propagação remota (single-user/local)
  - Base legal: art. 7º V (execução de contrato) para dados de terceiros/cliente; art. 4º I (fins exclusivamente particulares) para dados do próprio usuário — decisões CR2-D02/D03
  - GDPR: acionado se houver oferta de serviço ou monitoramento de pessoas no EEE/Reino Unido — decisão CR2-D02

### 2.2 Modelo de dados (tabela nova)

| Tabela | Campos essenciais | Constraints |
|--------|-------------------|-------------|
| `account_lifecycle_events` | `id UUID PK`, `user_id FK`, `event_type`, `from_status`, `to_status`, `created_at` | `event_type ∈ {CREATED, ACTIVATED, DORMANT_AUTO, DORMANT_MANUAL, REACTIVATED, DELETED}`; `ON DELETE CASCADE` com `users`; sem PII no evento |

### 2.3 Regras de integridade

- `users.status` transições válidas: `active ↔ dormant`, `active → deleted`, `dormant → deleted`. `deleted` é terminal.
- Dormência automática: job periódico (cron) verifica `last_login_at` ou `updated_at` vs. prazo ratificado.
- Exclusão: transação única remove todas as tabelas dependentes (`ON DELETE CASCADE` nas FKs) + insere evento `DELETED`.
- Invoices finalizadas: **não** removidas por `ON DELETE CASCADE`; decisão de retenção/anonimização/eliminação é separada (CR8-D01).
- PII real nunca em logs, seeds, fixtures, handoffs ou exemplos técnicos.
- Soberania de dados: nenhum PII trafega para nuvem de terceiros (P-02/P-03).

## 3. Decisões requeridas do CCB/PO (BLOQUEADORAS PARA TODAS AS DEMAIS CRs)

| ID | Decisão | Responsável |
|----|---------|-------------|
| **CR8-D01** | Retenção de invoices finalizadas após exclusão da conta: retenção legal (prazo), anonimização (campos pessoais) ou eliminação total | CCB + parecer jurídico/compliance |
| **CR8-D02** | Papel controlador/operador, bases legais (art. 7º V vs. art. 4º I), escopo territorial GDPR (art. 3) | CCB + parecer jurídico/compliance |
| **CR8-D03** | Prazo de dormência automática (ex.: 365 dias) e efeito (bloqueio total vs. leitura permitida) | CCB/PO |
| **CR8-D04** | Critérios de reativação: reset de senha + verificação (qual fator?) | `agent-digital-security` + CCB |
| **CR8-D05** | Canal de email para reset/notificações dentro da soberania (SMTP local/autohospedado) | Arquitetura + CCB |
| **CR8-D06** | Anonimização de invoices: quais campos, qual técnica (hash, supressão, generalização) | `agent-dba` + `agent-compliance-governance` + CCB |

## 4. Artefatos afetados

| Artefato | Ação |
|----------|------|
| `constitution.md` | emenda para admitir lifecycle, dormência, exclusão, LGPD/GDPR executivos (Art. 1.1, 1.2, 7, 9) |
| `spec-015` | **promover a spec executiva**: decisões D1-D7 ratificadas, retenção, erase, base legal, logs |
| `spec-004` | logs sem PII/valores/corpo; middleware de autorização por owner; rotas de lifecycle |
| `spec-007` | rota de erase para invoices (se retenção + anonimização) |
| `spec-017..021` | todas condicionadas às decisões desta CR |
| `spec-023` | telas de conta: dormência, exclusão, reativação, configurações de privacidade |
| Banco/Alembic | 1 migration `account_lifecycle_events`; FKs `ON DELETE CASCADE` nas tabelas dependentes |
| Segurança | threat model completo; testes de enumeração, fixation, CSRF, IDOR, rota de erase |
| Infra | SMTP local/autohospedado para email de reset/notificações |

## 5. Spec proposta

**SPEC-022 — `account-lifecycle-privacy-v1`** (em `docs/especificacoes/spec-prop-023-account-lifecycle-privacy.md`)

- Status: **draft** (em avaliação) — **PRIORIDADE MÁXIMA**
- Agente avaliador primário: `agent-compliance-governance`
- Consultados: `agent-digital-security`, `agent-project-analyst`, `agent-dba`, `agent-sdd-specialist`, `agent-business-analysis-specialist`, `agent-frontend-dev`, `agent-qa-sdet`, **parecer jurídico externo**

## 6. Critérios para encerrar a CR

- [ ] Issue publicada com label `change-request` e link para esta CR e PROP-023.
- [ ] **Parecer jurídico/compliance emitido** (LGPD + GDPR).
- [ ] **Threat model emitido** por `agent-digital-security`.
- [ ] Decisões CR8-D01..D06 deliberadas e registradas.
- [ ] SPEC-022 promovida a spec oficial ou explicitamente recusada.
- [ ] Emenda constitucional ratificada (Art. 1.1, 7, 9).
- [ ] SPEC-015 promovida de PROPOSTA para EXECUTIVA.

## 7. Rollback

Até a ratificação, **nenhuma outra CR derivada (003-007) pode ser implementada**. Se esta CR for recusada, toda a expansão multiusuário (CR-002) será arquivada.

## CHANGELOG

- 1.0.0 — 2026-11-14: CR derivada da CR-002 para isolar domínio de lifecycle/privacidade; precedência máxima (ordem 1), decisões LGPD/GDPR bloqueadoras para todas as demais, spec proposta SPEC-022, promoção da SPEC-015. Status ativo, aguardando parecer jurídico/compliance e decisão CCB.