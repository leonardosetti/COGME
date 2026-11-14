---
id: docs-change-requests-cr-003-identity-access-session
title: CR-003 — Identidade, aliases de login, senha, sessões e recuperação
type: change-request
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md (CR-002, SPEC-017)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md (PROP-017, §12.1, §12.2 tabelas users, user_login_identifiers, user_sessions, password_reset_tokens)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9.1-9.3)
- .ai/specs/spec-004-backend-mvp-v1.spec.md (fora de escopo autenticação)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (LGPD condicional)
- .ai/specs/spec-023-ui-spec-v1.spec.md (login, recovery, accessibility)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- change-request
- identidade
- autenticacao
- sessao
- seguranca
- lgpd
cr-number: CR-003
impacto: alto
prazo-analise-gp: '2026-11-16'
decisao-ccb: pendente
instrumento: pendente
github-issue: '#36'
parent-cr: CR-002
---

# CR-003 — Identidade, aliases de login, senha, sessões e recuperação

## 1. Origem e relação com CR-002

Esta CR deriva da **CR-002** (§5, §12, §13) e corresponde à **SPEC-017** da proposta **PROP-017**. Isola o domínio de identidade e acesso para tramitação, avaliação de segurança e decisão independentes, pois introduz superfície de ataque nova (login, recovery, session, CSRF, rate limit) e exige parecer de `agent-digital-security` antes da implementação.

## 2. Escopo desta CR

### 2.1 Funcionalidades

- Cadastro de conta com validação de unicidade por email, CPF e CNPJ
- Login aceitando qualquer dos três identificadores (email, CPF, CNPJ)
- Identificador interno opaco (`internal_username_hash`) derivado por HMAC-SHA-256 com chave secreta do servidor
- Armazenamento de senha com **Argon2id** (parâmetros a ratificar)
- Recuperação de senha por email com token single-use, TTL e hash no banco
- Sessão opaca com token aleatório, armazenado apenas como hash, expiração e revogação
- Cookies `HttpOnly`, `Secure` (em HTTPS), `SameSite=Lax`
- Proteção CSRF em operações mutáveis (double-submit cookie ou header)
- Rate limit em endpoints de login e recuperação
- Rotação de sessão após login bem-sucedido
- Logout e revogação de sessão individual e global

### 2.2 Modelo de dados (tabelas novas)

| Tabela | Campos essenciais | Constraints |
|--------|-------------------|-------------|
| `users` | `id UUID PK`, `internal_username_hash BYTEA`, `name`, `email`, `phone`, `cpf`, `password_hash`, `status`, `dormant_since`, `last_login_at`, `created_at`, `updated_at` | `status ∈ {active,dormant}`; email/CPF únicos e imutáveis; `internal_username_hash` único |
| `user_login_identifiers` | `id UUID PK`, `user_id FK`, `kind`, `lookup_hmac BYTEA`, `created_at`, `retired_at` | `UNIQUE(kind, lookup_hmac)`; `UNIQUE(user_id, kind)` enquanto ativo |
| `user_sessions` | `id UUID PK`, `user_id FK`, `token_hash BYTEA`, `created_at`, `last_seen_at`, `expires_at`, `revoked_at` | token único; revogação e expiração fail-closed |
| `password_reset_tokens` | `id UUID PK`, `user_id FK`, `token_hash BYTEA`, `created_at`, `expires_at`, `used_at` | single-use; TTL a ratificar |

### 2.3 Regras de integridade

- `users.email` e `users.cpf` **não possuem endpoint de alteração**; são imutáveis após cadastro.
- CNPJ pode ser alterado, mas o alias de login CNPJ deve ser rotacionado na mesma transação.
- Toda consulta de recurso filtra por `owner_user_id` derivado da sessão; IDs enviados pelo cliente **não são autorização**.
- Aliases de login usam HMAC com pepper rotativo; enumeração por força bruta de CPF/email é impedida.
- Senha nunca logada; tokens de sessão/reset nunca aparecem em log.

## 3. Decisões requeridas do CCB/PO

| ID | Decisão | Responsável |
|----|---------|-------------|
| CR3-D01 | Parâmetros Argon2id (memory, iterations, parallelism) | `agent-digital-security` + CCB |
| CR3-D02 | TTL de sessão, TTL de reset, rotação do pepper HMAC | `agent-digital-security` + CCB |
| CR3-D03 | Canal de email (SMTP local/autohospedado) dentro da soberania de dados | Arquitetura + CCB |
| CR3-D04 | Rate limit: janela, burst, resposta 429 | `agent-digital-security` + CCB |
| CR3-D05 | CSRF: double-submit cookie vs. header customizado | `agent-digital-security` + CCB |
| CR3-D06 | Expiração de sessão ociosa vs. absoluta | `agent-digital-security` + CCB |

## 4. Artefatos afetados

| Artefato | Ação |
|----------|------|
| `constitution.md` | emenda para admitir identidade/sessão (Art. 1.2) |
| `spec-004` | adicionar rotas `/auth/*`, middleware de sessão, autorização por owner |
| `spec-023` | telas de login, cadastro, recuperação, perfil |
| `spec-015` | LGPD: minimização em formulários de auth, logs sem PII |
| Banco/Alembic | 4 migrations `upgrade`/`downgrade` com FKs explícitas |
| Segurança | threat model, testes negativos de IDOR, enumeração, fixation, CSRF |

## 5. Spec proposta

**SPEC-017 — `identity-access-session-v1`** (em `docs/especificacoes/spec-prop-018-identity-access-session.md`)

- Status: **draft** (em avaliação)
- Agente avaliador primário: `agent-digital-security`
- Consultados: `agent-backend-dev`, `agent-compliance-governance`, `agent-sdd-specialist`, `agent-frontend-dev`, `agent-qa-sdet`

## 6. Critérios para encerrar a CR

- [ ] Issue publicada com label `change-request` e link para esta CR e PROP-018.
- [ ] Threat model emitido por `agent-digital-security`.
- [ ] Parecer LGPD emitido por `agent-compliance-governance`.
- [ ] Decisões CR3-D01..D06 deliberadas e registradas.
- [ ] SPEC-017 promovida a spec oficial ou explicitamente recusada.
- [ ] Emenda constitucional ratificada se alterar Art. 1.2.

## 7. Rollback

Até a ratificação, nenhuma migration, rota ou código de auth é autorizado. Se recusada, a proposta associada será marcada `obsoleto`/`arquivado`.

## CHANGELOG

- 1.0.0 — 2026-11-14: CR derivada da CR-002 para isolar domínio de identidade/acesso; modelo de 4 tabelas, regras de HMAC/Argon2id/CSRF/rate-limit, 6 decisões bloqueadoras, spec proposta SPEC-017. Status ativo, aguardando pareceres e decisão CCB.