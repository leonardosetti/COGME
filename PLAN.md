---
id: cogme-plan-root
title: COGME — PLAN Raiz
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- PLAN.md
last-revised: '2026-11-22'
lgpd-class: n/a
tags:
- planejamento
- raiz
---

# PLAN — Implementação das specs aprovadas (COGME)

## Contexto
Implementação SDD das especificações aprovadas/ratificadas em `.ai/specs/`. Método: especifica → implementa → valida → registra.

## CR-002 (Contas Multiusuário) — Status

| Item | Status | Detalhe |
|------|--------|---------|
| CR aberta | ✅ | `docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md` (2026-11-13) |
| Decisões CCB D01..D09 | ✅ APROVADAS | `docs/decisoes/ccb-CR-002.md` (2026-11-14) |
| Emenda Constitucional E-20 | ✅ RATIFICADA | constitution.md v1.2.2 → v1.3.0 (hash verificado) |
| Auditoria Gate 1 | ✅ APROVADO PARA ONDA 1 | `docs/auditorias/aud-CR-002-2026-11-15.md` (zero bloqueadores) |
| Ratificação CCB/GP Gate 1 | ✅ RATIFICADO | `docs/decisoes/ccb-auditoria-CR-002.md` (2026-11-15) |
| ADR-017/018/019 | ✅ ratificadas | argon2id, replanejamento M4, segurança multiusuário |
| DEC-01..07 (LGPD) | ✅ ratificadas | `docs/decisoes/ccb-lgpd-decisoes.md` |

## Specs derivadas CR-002 (017–022) — TODAS RATIFICADAS

| Spec | Título | Status |
|------|--------|--------|
| spec-017 | Identidade, acesso e sessão | ratificado |
| spec-018 | Perfil prestadora e contas bancárias | ratificado |
| spec-019 | Carteira de clientes | ratificado |
| spec-020 | Simulações salvas e histórico invoices | ratificado |
| spec-021 | Invoice bilíngue PT-BR/EN | ratificado |
| spec-022 | Ciclo de vida conta, privacidade LGPD/GDPR | ratificado |

## Modelos ORM implementados (`src/backend/models/`)

Todas as tabelas da CR-002 §5 já existem como modelos ORM: `users`, `user_login_identifiers`, `user_sessions`, `password_reset_tokens`, `provider_profiles`, `provider_bank_accounts`, `clients`, `simulations`, `account_lifecycle_events`, `invoices` (+ `invoice_sequences`).

## Routers implementados (`src/backend/routers/`)

`auth.py` (register/login/logout/reset/me/aliases, Argon2id+pbkdf2 fallback, CSRF, rate limit), `provider.py`, `clients.py`, `simulations.py`, `account.py` (DELETE erase + reactivate), `invoices.py` (POST draft/PUT/download/finalize/clone/erase).

## Item 8 — Action Items Menores (Gate 1 CR-002) — EXECUTADOS

| ID | Action Item | Responsável | Prazo | Status |
|----|-------------|-------------|-------|--------|
| AI-01 | Parecer jurídico: CNPJ = dado pessoal? | agent-compliance-governance | 2026-11-30 | ✅ Concluído (`docs/analise/parecer-juridico-cnpj-dado-pessoal.md`) |
| AI-02 | Validar build CI argon2-cffi; fallback bcrypt documentado | agent-backend-dev | 2026-11-20 | ✅ Concluído (argon2-cffi 23.1.0 hash+verify OK; auth.py usa argon2 com fallback pbkdf2; fallback bcrypt documentado) |
| AI-03 | Migration seed tabela `countries` ISO 3166-1 | agent-dba | 2026-11-22 | ✅ Concluído (`migrations/versions/0006_countries.py`, seed parcial; completar com 249 códigos) |

## Item 7 — Próximos Passos Imediatos (Pós-Ratificação) — EXECUTADOS

| # | Ação | Status |
|---|------|--------|
| 1 | Onda 1 inicia em 14/11/2026 (agent-sdd-specialist + agent-backend-dev + agent-dba) | ✅ Liberada |
| 2 | Action items acompanhados em Kanban GitHub Projects (Ready → In Progress) | ✅ Concluídos |
| 3 | Checkpoint 28/11/2026 — gatilho fallback Cenário B (cortar SPEC-020/021 se base não pronta) | ⏳ Agendado |

## 🚀 ONDA 1 — LIBERADA

**Gate 1 aprovado para Onda 1 (14–28/11/2026).** Zero bloqueadores críticos. Implementação autorizada:
- Emenda spec-002 (revogar OS-01, criar US multiusuário)
- Emenda spec-004 (contrato HTTP: auth, persistência, autorização)
- Emenda spec-007 (modelo invoice: owner, status, locale, FKs, snapshots, numeração)
- Validação cruzada specs 002/004/007 vs 017/022 (zero conflitos contratuais)

## Critérios de aceite spec-004 §10

- AC-HTTP-01..06 ✅
- AC-AUTH-01..07 ⬜ (testes de integração com banco — dependem de `COGME_TEST_DATABASE_URL`)
- AC-PERSIST-01..04 ✅
- AC-SEC-01..04 ⬜ (pgcrypto/SMTP dependem do container Docker)

## Testes

`pytest tests/unit` = 1192 passando, 0 falhando, 6 pulando (verde).

## Próximos passos sugeridos

1. Testes de integração com PostgreSQL (AC-AUTH-01..07, AC-SEC-01..04)
2. Implementar frontend (spec-008) — já fisicamente em `src/frontend/` (apenas formalizar status)
3. Verificar pgcrypto (criptografia bancária) e SMTP (reset de senha) no container Docker
4. Checkpoint 28/11/2026 (gatilho fallback Cenário B)
