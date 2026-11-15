---
id: docs-decisoes-adr-019-seguranca-multiusuario
title: ADR-019 — Threat Model e Controles de Segurança — Contas Multiusuário (CR-002)
type: adr
version: 1.0.0
status: ratificado
owner: agent-digital-security
derived-from:
- constitution.md (P-07, Art. 7, Art. 9.3.ii)
- docs/decisoes/ccb-CR-002.md (Gate C, CR2-D06)
- docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md (§3, §12.1, §12.2)
- docs/decisoes/adr-017-dependencia-argon2id.md
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- adr
- seguranca
- threat-model
- multiusuario
- autenticacao
- sessao
- csrf
- rate-limit
adr-number: 019
impacto: alto
---

# ADR-019 — Threat Model e Controles de Segurança — Contas Multiusuário (CR-002)

## 1. Contexto

A CR-002 introduz identidade, autenticação, sessão, recuperação de senha e isolamento por proprietário (`owner_user_id`). Isso expande a superfície de ataque significativamente. Este ADR define o threat model e os controles obrigatórios **antes** da implementação (Gate C → SPEC-017).

## 2. Ativos e Superfície de Ataque

| Ativo | Classificação | Ameaças Principais |
|-------|---------------|-------------------|
| `users.password_hash` | Crítico (segredo) | Brute force, rainbow table, side-channel, vazamento em log |
| `user_sessions.token_hash` | Crítico (credencial) | Session fixation, hijacking, replay, enumeration |
| `user_login_identifiers.lookup_hmac` | Alto (PII derivado) | Enumeração de CPF/email/CNPJ via timing attack |
| `password_reset_tokens.token_hash` | Crítico (credencial temporária) | Reset abuse, token prediction, replay |
| `provider_bank_accounts` | Crítico (dados financeiros) | Acesso não autorizado, vazamento em invoice/snapshot |
| `invoices` (com `owner_user_id`) | Alto (dados pessoais + financeiros) | IDOR, vazamento cross-user, snapshot mutável |

## 3. Threat Model (STRIDE)

| Ameaça | Vetor | Controle Obrigatório | Spec/Teste |
|--------|-------|---------------------|------------|
| **Spoofing** | Login com credenciais roubadas | Argon2id (m=19456, t=2, p=1); rate limit login (5/min/IP, 10/min/user) | SPEC-017 AC-03, AC-04 |
| **Tampering** | Alteração de `owner_user_id` no request | Autorização server-side **sempre** da sessão; nunca aceitar `user_id` do cliente | SPEC-017 AC-07 |
| **Repudiation** | Usuário nega ação | Audit log imutável (`account_lifecycle_events`) com hash encadeado | SPEC-022 AC-02 |
| **Information Disclosure** | Vazamento cross-user (IDOR) | Testes de autorização em **todas** rotas (`GET /api/simulations/{id}`, `GET /api/invoices/{id}`) | SPEC-017 AC-08 |
| **Information Disclosure** | PII em logs/erros | Logs sem PII/valores/corpo (spec-004:126, spec-015 CP-2); error handler sanitiza | SPEC-015 CP-2 |
| **Information Disclosure** | Enumeração CPF/email via timing | `lookup_hmac` (HMAC-SHA256 com pepper rotacionado 90d); tempo constante | SPEC-017 AC-05 |
| **DoS** | Brute force login/reset | Rate limit + exponential backoff + CAPTCHA após 5 falhas (opcional) | SPEC-017 AC-04 |
| **Elevation of Privilege** | Session fixation | Regenerar session ID após login; `HttpOnly`, `Secure`, `SameSite=Lax` | SPEC-017 AC-06 |
| **Elevation of Privilege** | CSRF em mutações | Double-submit cookie + header `X-CSRF-Token` em todas rotas `POST/PUT/DELETE/PATCH` | SPEC-017 AC-09 |
| **Elevation of Privilege** | Alias rotation race | Rotacionar CNPJ alias na **mesma transação** do update de `provider_profiles.cnpj` | SPEC-018 AC-03 |

## 4. Controles de Implementação (Checklist SPEC-017)

### 4.1 Hash de Senha (ADR-017)
- [ ] `argon2-cffi` com parâmetros OWASP mínimos
- [ ] Funções `hash_password()`, `verify_password()` em `src/backend/security/password.py`
- [ ] Testes: hash único por chamada, tempo constante, verificação correta

### 4.2 Sessão
- [ ] Token: 32 bytes aleatórios (`secrets.token_urlsafe(32)`)
- [ ] Armazenar apenas `token_hash = SHA256(token + pepper)` em `user_sessions`
- [ ] Cookie: `Set-Cookie: session=<token>; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=86400`
- [ ] Regenerar session ID no login (revogar sessão anterior)
- [ ] Expiração: 24h sliding (`last_seen_at` atualizado a cada request)
- [ ] Revogação: `revoked_at` preenchido no logout + cleanup job diário

### 4.3 Recuperação de Senha
- [ ] Token: 32 bytes aleatórios, hash armazenado (`SHA256(token + pepper)`)
- [ ] TTL: **1 hora** (CR2-D06)
- [ ] Single-use: `used_at` preenchido na validação; token invalidado após uso
- [ ] Rate limit: 3 requests/hora por email/CPF
- [ ] Email: template PT-BR, link com token na URL, expiração clara

### 4.4 Aliases de Login (`user_login_identifiers`)
- [ ] `kind ∈ {email, cpf, cnpj}`
- [ ] `lookup_hmac = HMAC-SHA256(pepper, normalized_identifier)`
- [ ] Pepper: 32 bytes aleatórios, rotacionado a cada 90 dias (CR2-D06)
- [ ] Unicidade: `UNIQUE(kind, lookup_hmac)` + `UNIQUE(user_id, kind)` ativo
- [ ] Email/CPF imutáveis; CNPJ rotaciona alias na mesma transação

### 4.5 Autorização por Recurso (Owner Check)
- [ ] Middleware `require_owner(resource_type, resource_id)` em **todas** rotas de recurso
- [ ] Extrai `owner_user_id` da sessão validada
- [ ] Query: `SELECT 1 FROM {table} WHERE id = ? AND owner_user_id = ?`
- [ ] Retorna 404 (não 403) para não vazar existência

### 4.6 CSRF Protection
- [ ] Double-submit cookie: `csrf_token` cookie (HttpOnly, SameSite=Lax) + header `X-CSRF-Token`
- [ ] Validar em **todas** rotas mutáveis (`POST`, `PUT`, `PATCH`, `DELETE`)
- [ ] Exceção: rotas de login/logout/reset (stateless)

### 4.7 Rate Limiting
- [ ] Login: 5 req/min/IP, 10 req/min/user (baseado em `user_login_identifiers`)
- [ ] Reset request: 3 req/hora/identificador
- [ ] Reset confirm: 5 req/hora/token
- [ ] API geral: 100 req/min/user (burst 20)

### 4.8 Dados Bancários (`provider_bank_accounts`)
- [ ] Criptografia em repouso: `pgcrypto` ou aplicação (AES-256-GCM com DEK por usuário)
- [ ] Snapshot em invoice: copiar dados descriptografados para `invoices.bank_snapshot` (JSONB)
- [ ] Logs: **nunca** logar campos bancários (spec-015 CP-2)

## 5. Testes de Segurança Obrigatórios

| Teste | Descrição | Critério de Aceite |
|-------|-----------|-------------------|
| **ST-01** | Brute force login | 6ª tentativa bloqueia por 15 min; log de segurança |
| **ST-02** | Session fixation | Login regenera session ID; sessão anterior inválida |
| **ST-03** | IDOR cross-user | User A não acessa simulation/invoice/client de User B (404) |
| **ST-04** | CSRF token missing | POST mutável sem header `X-CSRF-Token` → 403 |
| **ST-05** | CSRF token invalid | Header com token errado → 403 |
| **ST-06** | Reset token reuse | Token usado uma vez; segunda tentativa → 400 |
| **ST-07** | Reset token expiry | Token > 1h → 400 |
| **ST-08** | Enumeração timing | `lookup_hmac` tempo constante (±5ms) para hit/miss |
| **ST-09** | Log sanitization | Logs de erro/request não contêm PII, valores, corpo (spec-015 CP-2) |
| **ST-10** | Alias rotation atomic | Update CNPJ + rotate alias em transação única; rollback se falhar |

## 6. Conformidade

- **Constitution P-07:** Baseline OWASP atendido (ASVS L1/L2)
- **Constitution Art. 7:** Zero Trust, menor privilégio, fail-closed
- **Spec-015 CP-2:** Logs sem PII/valores/corpo
- **Spec-015 CP-3:** Rota erase operante + retenção 5 anos + anonimização
- **LGPD Art. 46-48:** Medidas técnicas/organizacionais de segurança

## 7. Rastreabilidade

- CR-002: `docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md`
- CCB Decision: `docs/decisoes/ccb-CR-002.md` (Gate C, CR2-D06)
- ADR-017: `docs/decisoes/adr-017-dependencia-argon2id.md` (hash senha)
- SPEC-017: `docs/especificacoes/spec-prop-017-conta-multiusuario.md` (deriva SPEC-017)
- SPEC-022: `docs/especificacoes/spec-prop-017-conta-multiusuario.md` (deriva SPEC-022)

---

## CHANGELOG

- **1.0.0 — 2026-11-14:** Emissão inicial, aprovada por CCB/GP via CR-002 Gate C. Responsável: `agent-digital-security`.