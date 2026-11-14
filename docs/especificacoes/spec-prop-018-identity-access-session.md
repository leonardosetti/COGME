---
id: docs-especificacoes-spec-prop-018-identity-access-session
title: Proposta de Spec — Identidade, aliases, senha, sessões e recuperação
type: spec
version: 0.1.0
status: draft
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-003-identity-access-session.md
- docs/templates/proposta-spec-template.md
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9)
- .ai/specs/spec-004-backend-mvp-v1.spec.md
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md
- .ai/specs/spec-023-ui-spec-v1.spec.md
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- proposta
- spec
- identidade
- autenticacao
- sessao
- seguranca
spec-id: PROP-018
camada: produto
estado-implementacao: nao-iniciada
rastreia-req:
- CR-003
testes-vinculados: []
---

# Proposta de Spec — Identidade, aliases, senha, sessões e recuperação

## 1. Ideia / Draft

**Título da proposta:** Identidade, aliases de login, senha, sessões e recuperação

**Autor:** PO/GP — derivação da CR-003 (2026-11-14)

**Data:** 2026-11-14

**Contexto / problema que resolve:**

A CR-002 introduz contas multiusuário, mas o domínio de identidade/acesso tem superfície de ataque própria e decisões de segurança (Argon2id, HMAC, CSRF, rate limit) que devem ser avaliadas por `agent-digital-security` antes de qualquer implementação. Isolar em CR-003 e SPEC-017 permite tramitação paralela dos demais domínios condicionada a esta.

**Descrição breve da solução proposta:**

Implementar cadastro/login/recuperação com identificadores email/CPF/CNPJ normalizados, aliases protegidos por HMAC com pepper rotativo, senha Argon2id, sessão opaca com hash, cookies seguros, CSRF double-submit, rate limit e revogação de sessão. Toda autorização deriva da sessão (owner_user_id), nunca de ID enviado pelo cliente.

**Escopo inicial (DENTRO):**

- Cadastro com validação de unicidade por email, CPF, CNPJ
- Login aceitando qualquer dos três identificadores
- `internal_username_hash` = HMAC-SHA-256(pepper, identificador_aleatorio)
- Senha: Argon2id (parâmetros a ratificar CR3-D01)
- Recuperação: token single-use, TTL, hash no banco, email
- Sessão: token aleatório, armazenado como hash, expiração, revogação
- Cookies: `HttpOnly`, `Secure` (HTTPS), `SameSite=Lax`
- CSRF: double-submit cookie em operações mutáveis
- Rate limit: login e recovery (janela, burst, 429)
- Rotação de sessão após login
- Logout individual e global (revogação de todas as sessões)

**Fora de escopo (NÃO está):**

- OAuth, SSO, MFA, federação de identidade, recuperação por SMS
- Equipes, organizações, papéis administrativos, painel admin
- Integração com provedores de identidade externos
- Auditoria de acesso (pode ser adicionada depois)

## 2. Análise de Derivação Multi-Spec

**Resultado:** **Uma spec única** — domínio coeso de identidade/acesso com contratos, tabelas e superfície de ataque próprios.

| Critério de Divisão | Aplica-se? | Justificativa |
|---|---:|---|
| Domínios técnicos disjuntos | Sim | Auth/session é fronteira de segurança distinta de prestadora, clientes, histórico |
| Ciclos de vida independentes | Parcial | Sessão/token tem ciclo curto; usuário tem ciclo longo |
| Requisitos regulatórios separados | Sim | LGPD/GDPR em credenciais e logs de auth exigem contrato próprio |
| Dependências com desenvolvimento paralelo | Sim | Prerequisite para SPEC-018..021; pode ser especificada em paralelo |

**Spec derivada:** SPEC-017 — `identity-access-session-v1` | Agente dono: `agent-digital-security` + `agent-backend-dev`

## 3. Viabilidade Técnica

| Critério | Avaliação | Observações |
|---|---|---|
| Tecnologias no stack? | Sim | FastAPI, SQLAlchemy, PostgreSQL, `argon2-cffi` (FOSS) |
| Nova dependência? | Sim | `argon2-cffi` — FOSS, sem custo recorrente |
| Impacta arquitetura/contratos? | Sim, alto | Nova fronteira de autenticação, middleware, rotas `/auth/*` |
| Complexidade | Alta | HMAC/pepper, Argon2id, CSRF, rate limit, revogação, testes negativos |
| Riscos técnicos | Elevados | Enumeração de identifiers, session fixation, CSRF, reset abuse, vazamento entre owners |

## 4. Viabilidade Negocial

| Critério | Avaliação | Observações |
|---|---|---|
| Alinhado com produto/roadmap? | Condicional | Requer emenda constitucional (OS-01 revertido) e decisão CCB |
| Valor mensurável? | Sim | Titular real, isolamento de dados, base para histórico e invoice |
| ROI | Positivo, condicionado | Habilita todo o multiusuário; risco de segurança se mal implementado |
| Dependências externas | Sim | CCB, threat model, parecer LGPD, decisão de canal de email |
| Urgência | Alta | Blocker para SPEC-018..021; CR-008 deve ser resolvida antes |

## 5. Custo Técnico Estimado

| Item | Estimativa | Notas |
|---|---:|---|
| Desenvolvimento | 48–72 h | Rotas auth, middleware, HMAC, Argon2id, CSRF, rate limit, testes |
| Design/UX | 16–24 h | Telas login, cadastro, recovery, perfil, sessões ativas |
| QA/testes | 24–36 h | Unit, integração, segurança (IDOR, enumeração, fixation, CSRF) |
| Auditoria/segurança | 8–16 h | Threat model, revisão de código, pentest leve |
| **Total** | **96–148 h** | |

## 6. Aderência ao Projeto / Produto

- **Constituição:** condicional — exige emenda Art. 1.2 (OS-01 revertido) e Art. 7/9 (LGPD/GDPR)
- **AGENT_TOPOLOGY:** compatível — `agent-digital-security` (primário), `agent-backend-dev`, `agent-compliance-governance`, `agent-sdd-specialist`, `agent-frontend-dev`, `agent-qa-sdet`
- **LGPD/GDPR:** não aderente até CR3-D01..D06 e CR8-D01..D06. Propõe minimização, privacy by design, erase/dormência, logs sem PII, soberania.
- **FOSS/soberania:** compatível — `argon2-cffi` FOSS, PostgreSQL local, SMTP local/autohospedado
- **YAGNI:** mantidos apenas identidade individual, senha, sessão, recovery. MFA/SSO/OAuth fora.

## 7. Critérios de Aceite para Promoção à Spec

- [x] Viabilidade técnica: **Sim**, com riscos e controles declarados
- [x] Viabilidade negocial: **Parcial**, condicionada a emenda e decisões CCB
- [ ] Custo aprovado pelo PO/PM
- [ ] Aderência constitucional: emenda ratificada
- [x] Riscos mapeados com mitigação
- [x] Done e specs derivadas definidos

**Resultado:** proposta em **draft**, em avaliação. Promoção depende de CR-003 e CR-008.

## 8. Agentes Responsáveis

**Avaliador primário:** `agent-digital-security`
**Consultados:** `agent-backend-dev`, `agent-compliance-governance`, `agent-sdd-specialist`, `agent-frontend-dev`, `agent-qa-sdet`
**Decisor:** CCB/GP

## 9. Modelo de Dados e Regras (Resumo)

### Tabelas

| Tabela | PK | Campos-chave | Constraints |
|---|---|---|---|
| `users` | `id UUID` | `internal_username_hash BYTEA`, `email`, `cpf`, `password_hash`, `status`, `dormant_since`, `last_login_at` | email/CPF únicos imutáveis; `internal_username_hash` único; `status ∈ {active,dormant}` |
| `user_login_identifiers` | `id UUID` | `user_id FK`, `kind ∈ {email,cpf,cnpj}`, `lookup_hmac BYTEA` | `UNIQUE(kind, lookup_hmac)`; `UNIQUE(user_id, kind)` ativo |
| `user_sessions` | `id UUID` | `user_id FK`, `token_hash BYTEA`, `expires_at`, `revoked_at` | token único; revogação fail-closed |
| `password_reset_tokens` | `id UUID` | `user_id FK`, `token_hash BYTEA`, `expires_at`, `used_at` | single-use; TTL ratificado |

### Regras de autorização

- `owner_user_id` **sempre** derivado da sessão validada; nunca aceito do request.
- Middleware de autenticação em rotas protegidas; 401 se sessão inválida/expirada/revogada.
- Rate limit por IP + por identificador (email/CPF/CNPJ) em `/auth/login` e `/auth/recovery`.

## 10. Decisões Bloqueadoras (CR-003)

| ID | Decisão | Responsável |
|---|---|---|
| CR3-D01 | Parâmetros Argon2id | `agent-digital-security` + CCB |
| CR3-D02 | TTL sessão, TTL reset, rotação pepper HMAC | `agent-digital-security` + CCB |
| CR3-D03 | Canal de email (SMTP local) | Arquitetura + CCB |
| CR3-D04 | Rate limit: janela, burst, 429 | `agent-digital-security` + CCB |
| CR3-D05 | CSRF: double-submit cookie vs header | `agent-digital-security` + CCB |
| CR3-D06 | Expiração ociosa vs. absoluta | `agent-digital-security` + CCB |

## 11. Próximos Passos

| Ação | Responsável | Condição |
|---|---|---|
| Emitir threat model | `agent-digital-security` | Antes do CCB |
| Emitir parecer LGPD | `agent-compliance-governance` | Antes do CCB |
| Deliberar CR3-D01..D06 | CCB/GP | Após pareceres |
| Ratificar emenda constitucional | CCB/GP | Antes de código |
| Emitir SPEC-017 oficial | `agent-sdd-specialist` | Após ratificação |

## CHANGELOG

- 0.1.0 — 2026-11-14: Proposta derivada da CR-003; modelo de 4 tabelas, HMAC/Argon2id/CSRF/rate-limit, 6 decisões bloqueadoras, spec SPEC-017. Status draft.