---
id: docs-analise-threat-model-multiusuario
title: Threat Model — Expansão Multiusuário COGME (CR-008 / SPEC-022)
type: relatorio
version: 1.0.0
status: ativo
owner: agent-digital-security
derived-from:
- docs/change-requests/cr-008-account-lifecycle-privacy.md
- docs/analise/parecer-juridico-lgpd-gdpr-cogme.md
- constitution.md (P-02, P-03, P-04, P-07)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md
- OWASP Top 10 2021
- STRIDE
last-revised: '2026-11-14'
lgpd-class: sensível
tags:
- threat-model
- seguranca
- stride
- owasp
- cr-008
---

# Threat Model — Expansão Multiusuário COGME

## 1. Visão Geral do Sistema

### 1.1 Contexto

Expansão do COGME (Conversor de Ganhos em Moeda Estrangeira) de aplicação single-user/local para **multiusuário com isolamento por conta**, incluindo:
- Identidade: cadastro, login (email/CPF/CNPJ), recovery, sessão
- Prestadora: perfil MEI/PJ, CNPJ, contas bancárias (wire/SWIFT/IBAN)
- Clientes: carteira ativo/inativo, snapshot em invoice
- Simulações: opt-in, histórico, cotações
- Invoices: draft/finalized/clone, bilíngue PT-BR/EN, anonimização pós-exclusão
- Lifecycle: active/dormant/deleted, job dormência, erase route

### 1.2 Premissas de Segurança

- **Stack:** FastAPI + PostgreSQL + SQLAlchemy async + Jinja2 + Vanilla JS
- **Infra:** 100% local/on-premise, Docker Compose, PostgreSQL local, SMTP autohospedado
- **Soberania:** P-02/P-03 — zero PII em nuvem, zero telemetria, zero suboperadores
- **LGPD/GDPR:** Privacy by design, minimização, erase local, logs sem PII

### 1.3 Ativos de Alto Valor

| Ativo | Classificação | Impacto Vazamento |
|-------|---------------|-------------------|
| Hash de senha (Argon2id) | Crítico | Comprometimento de contas |
| Pepper HMAC aliases | Crítico | Enumeração de CPF/email/CNPJ |
| Dados bancários (SWIFT/IBAN/conta) | Crítico | Fraude financeira, wire transfer |
| Dados de clientes (terceiros) | Alto | Violação LGPD Art. 7º V, GDPR Art. 28 |
| Invoices finalizadas (valores + partes) | Alto | Vazamento financeiro, obrigação fiscal |
| Tokens de sessão/recovery | Alto | Hijacking de conta |
| Chaves criptográficas (pgcrypto) | Crítico | Descriptografia dados bancários |

---

## 2. Modelo STRIDE

### 2.1 Spoofing (Falsificação de Identidade)

| Ameaça | Vetor | Controle | Residual |
|--------|-------|----------|----------|
| Login com credenciais roubadas | Credential stuffing, phishing | Rate limit/IP + por identificador; Argon2id; MFA futuro | **Médio** |
| Session hijacking | Token roubado (XSS, MITM) | HttpOnly, Secure, SameSite=Lax; TLS local; rotação pós-login; revogação | **Baixo** |
| Recovery token abuse | Token interceptado | Single-use, TTL 1h, hash no banco, email local | **Baixo** |
| Alias enumeration | Força bruta em CPF/email/CNPJ | HMAC-SHA-256 com pepper rotativo; rate limit por identificador | **Baixo** |

### 2.2 Tampering (Adulteração)

| Ameaça | Vetor | Controle | Residual |
|--------|-------|----------|----------|
| Alteração de invoice finalizada | API direta, SQL injection | Status `finalized` imutável (CHECK + middleware); FK RESTRICT; row-level security | **Baixo** |
| Alteração de snapshot bancário/prestadora | SQL injection, API | Snapshot na finalização; criptografia em repouso (pgcrypto); validação Pydantic | **Baixo** |
| Injeção em template Jinja2 | SSTI via campos de invoice | Autoescape ativo; `_RefusingUrlFetcher`; campos validados; sandbox | **Baixo** |
| Modificação de pepper HMAC | Acesso ao servidor | Pepper em variável de ambiente; rotação anual; logs de rotação | **Médio** |
| CSRF em operações mutáveis | Formulário malicioso externo | Double-submit cookie + header `X-CSRF-Token`; SameSite=Lax | **Baixo** |

### 2.3 Repudiation (Repúdio)

| Ameaça | Vetor | Controle | Residual |
|--------|-------|----------|----------|
| Usuário nega ação (login, invoice, exclusão) | Falta de auditoria | `account_lifecycle_events` (CREATE, LOGIN, FINALIZE, DELETE, ANONYMIZE); logs de acesso sem PII | **Baixo** |
| Admin nega ação de anonimização | Falta de log imutável | Evento `ANONYMIZED` com hash da invoice; log de rotação pepper | **Baixo** |

### 2.4 Information Disclosure (Vazamento de Informação)

| Ameaça | Vetor | Controle | Residual |
|--------|-------|----------|----------|
| Vazamento de hash senha | Backup, logs, debug | Argon2id (não reversível); logs sem PII/valores; backups cifrados | **Baixo** |
| Enumeração de usuários via CPF/email | Resposta diferenciada 404/400 | Resposta uniforme "credenciais inválidas"; rate limit | **Baixo** |
| Dados bancários em logs/debug | Log acidental | Logs sem PII/valores/corpo (spec-004:126); middleware sanitizador | **Baixo** |
| Invoices de outro usuário | IDOR (Insecure Direct Object Reference) | Middleware `owner_user_id` em TODAS as rotas; row-level security PostgreSQL | **Baixo** |
| Pepper HMAC em logs/variável exposta | Configuração incorreta | Pepper apenas em env var; nunca em código/logs; rotação anual | **Médio** |
| Dados de clientes (terceiros) | Acesso indevido, backup | Isolamento por `owner_user_id`; anonimização pós-exclusão | **Baixo** |

### 2.5 Denial of Service (Negação de Serviço)

| Ameaça | Vetor | Controle | Residual |
|--------|-------|----------|----------|
| Exaustão de conexões DB | Login/recovery em massa | Rate limit por IP + identificador; pool conexões limitado; circuit breaker repo | **Médio** |
| Exaustão de SMTP | Recovery em massa | Rate limit recovery (ex.: 3/hora por email); queue local | **Médio** |
| Preenchimento de disco | Simulações/invoices ilimitadas | Limite por usuário (ex.: 10k simulações, 5k invoices); monitoramento | **Baixo** |
| CPU Argon2id | Login paralelo | Parâmetros Argon2id balanceados (memória/iterations); concorrência limitada | **Médio** |

### 2.6 Elevation of Privilege (Elevação de Privilégio)

| Ameaça | Vetor | Controle | Residual |
|--------|-------|----------|----------|
| Acesso a rotas admin/debug | Rota exposta | **Nenhuma rota admin** — single-user por conta; no multi-tenant | **Baixo** |
| Manipulação de `owner_user_id` | Request forjado | `owner_user_id` **nunca** aceito do cliente; derivado da sessão validada | **Baixo** |
| Elevação via SQL injection | Input não sanitizado | SQLAlchemy ORM + parâmetros vinculados; Pydantic `extra="forbid"` | **Baixo** |
| Acesso a dados de outra conta | Session fixation, prediction | Rotação de sessão pós-login; token aleatório 256-bit; HttpOnly/Secure | **Baixo** |

---

## 3. Análise OWASP Top 10 2021

| Categoria | Risco | Mitigação COGME |
|-----------|-------|-----------------|
| **A01: Broken Access Control** | IDOR, bypass autorização | Middleware `owner_user_id` em todas rotas; row-level security; `finalized` imutável |
| **A02: Cryptographic Failures** | Hash fraco, chaves expostas | Argon2id, HMAC-SHA-256 pepper, pgcrypto, TLS 1.3 local, rotação pepper |
| **A03: Injection** | SQL, SSTI, command | SQLAlchemy ORM, Pydantic `forbid`, Jinja2 autoescape, `_RefusingUrlFetcher` |
| **A04: Insecure Design** | Falta threat model, privacy by design | **Este documento**; privacy by design (minimização, anonimização, erase local) |
| **A05: Security Misconfiguration** | Debug exposto, defaults inseguros | Config via env var; `extra="forbid"`; sem CORS; proxy Nginx; headers seguros |
| **A06: Vulnerable Components** | Dependências desatualizadas | `pip-audit` no CI; dependências FOSS pinned; `cryptography`, `argon2-cffi` atuais |
| **A07: Identification & Authentication Failures** | Brute force, session fixation | Rate limit, Argon2id, rotação sessão pós-login, TTL recovery, HMAC aliases |
| **A08: Software & Data Integrity Failures** | CI/CD não verificado, updates inseguros | CI com `pip-audit`, `mypy`, `pytest-cov ≥80%`; imagens base por digest |
| **A09: Security Logging & Monitoring Failures** | Logs sem auditoria, PII em log | `account_lifecycle_events`, logs sem PII/valores, alertas em falhas críticas |
| **A10: Server-Side Request Forgery (SSRF)** | Invoice busca recursos externos | `_RefusingUrlFetcher` recusa **todas** URLs; WeasyPrint sem fetcher externo |

---

## 4. Controles por Camada

### 4.1 Aplicação (FastAPI)

| Controle | Implementação |
|----------|---------------|
| Autenticação | Middleware extrai `owner_user_id` da sessão validada; 401 se inválida |
| Autorização | `owner_user_id` injetado em dependências; nunca do request |
| Validação | Pydantic v2 `extra="forbid"` em todos schemas; `Decimal` para dinheiro |
| Rate Limit | `slowapi` ou middleware custom: login/recovery por IP + identificador |
| CSRF | Double-submit cookie (`csrf_token` cookie + header `X-CSRF-Token`) |
| Headers Seguros | `Content-Security-Policy`, `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin` |
| Logs | Structlog; zero PII/valores/corpo; `account_lifecycle_events` para auditoria |

### 4.2 Banco de Dados (PostgreSQL)

| Controle | Implementação |
|----------|---------------|
| Row-Level Security | `CREATE POLICY` em todas tabelas `owner_user_id = current_setting('app.current_user_id')::uuid` |
| Cifragem em Repouso | `pgcrypto` para `account_number`, `swift_bic`, `iban`; chaves derivadas de pepper |
| Constraints | `CHECK` enums, `FK ON DELETE RESTRICT/CASCADE`, `UNIQUE` aliases, `NOT NULL` |
| Auditoria | `account_lifecycle_events` (append-only, sem PII) |
| Backup | `pg_dump` cifrado; retenção 30 dias; teste de restore mensal |

### 4.3 Sessão e Credenciais

| Controle | Implementação |
|----------|---------------|
| Senha | Argon2id (memory=64MB, iterations=3, parallelism=4) — parâmetros ratificados CR3-D01 |
| Aliases Login | HMAC-SHA-256(pepper, identificador_normalizado); pepper rotativo anual |
| Sessão | Token aleatório 256-bit; armazenado hash SHA-256; TTL 24h sliding; rotação pós-login |
| Recovery | Token aleatório 256-bit; hash SHA-256; TTL 1h; single-use; email local |
| Cookies | `HttpOnly`, `Secure` (HTTPS), `SameSite=Lax`, `__Host-` prefix |
| Revogação | Imediata (logout, exclusão, dormência, reativação); `revoked_at` indexado |

### 4.4 Email (SMTP Local)

| Controle | Implementação |
|----------|---------------|
| Servidor | Postfix/Exim em container dedicado; DKIM/SPF/DMARC |
| Conteúdo | Apenas metadata em logs (hash destinatário, timestamp, status); **nunca corpo** |
| Rate Limit | 3 recovery/hora por email; queue local com backoff |
| TLS | STARTTLS obrigatório; certificado local |

### 4.5 Frontend (Jinja2 + Vanilla JS)

| Controle | Implementação |
|----------|---------------|
| Autoescape | Jinja2 `autoescape=True` global; `_RefusingUrlFetcher` no WeasyPrint |
| CSP | `default-src 'self'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; connect-src 'self'` |
| Formulários | `autocomplete="off"` em sensíveis; `novalidate` + validação JS + server-side |
| PDF | WeasyPrint com `url_fetcher` que recusa tudo; fontes locais (DejaVu Sans) |

---

## 5. Cenários de Ataque Prioritários (Attack Trees)

### 5.1 Comprometimento de Conta via Recovery

```
Objetivo: Acessar conta de outro usuário
├── Interceptar token recovery
│   ├── MITM email → Bloqueado: TLS local, SMTP autohospedado
│   ├── Acesso ao servidor → Bloqueado: single-use, TTL 1h, hash no banco
│   └── Enumeração email → Bloqueado: resposta uniforme, rate limit
├── Força bruta token → Bloqueado: 256-bit aleatório, single-use
└── Reutilização token → Bloqueado: `used_at` + single-use
```

### 5.2 Vazamento de Dados Bancários

```
Objetivo: Obter SWIFT/IBAN/conta de usuários
├── SQL Injection → Bloqueado: SQLAlchemy ORM, parâmetros vinculados
├── Backup não cifrado → Bloqueado: pg_dump cifrado, chaves separadas
├── Logs com dados → Bloqueado: middleware sanitizador, zero PII em logs
├── Acesso direto DB → Bloqueado: RLS, apenas app user conecta
└── Chave pgcrypto exposta → Mitigado: pepper em env var, rotação anual
```

### 5.3 Acesso a Dados de Terceiros (Clientes)

```
Objetivo: Obter nome/CPF/endereço de clientes de outro usuário
├── IDOR via invoice_id → Bloqueado: middleware owner_user_id, RLS
├── Enumeração invoice_id → Bloqueado: UUID v4 aleatório, não sequencial
├── Snapshot em invoice → Bloqueado: anonimização pós-exclusão
└── Exportação em massa → Bloqueado: limites por usuário, rate limit
```

---

## 6. Testes de Segurança Requeridos

| Teste | Frequência | Ferramenta |
|-------|------------|------------|
| SAST (Static Analysis) | Cada PR | `bandit`, `semgrep`, `mypy` |
| DAST (Dynamic) | Pré-release | `OWASP ZAP` local |
| Dependency Scan | Cada PR + semanal | `pip-audit`, `safety` |
| Pentest Leve | Pré-produção | Manual (OWASP Top 10) |
| Teste Argon2id | Unitário | Vetores de teste conhecidos |
| Teste HMAC Pepper | Unitário | Vetores conhecidos, rotação |
| Teste RLS | Integração | Multi-usuário paralelo |
| Teste Anonimização | Integração | Conta deleted → invoice anonimizada |
| Teste Rate Limit | Integração | Carga simulada |
| Teste CSRF | Integração | Request sem token → 403 |

---

## 7. Resposta a Incidentes

| Fase | Ação | SLA |
|------|------|-----|
| **Detecção** | Alertas: falhas login >10/min, erros 5xx >5%, anomalias DB | Tempo real |
| **Contenção** | Revogação sessões afetadas; bloqueio IP; rotação pepper se comprometido | ≤1h |
| **Erradicação** | Correção da vulnerabilidade; deploy hotfix; rotação chaves se necessário | ≤24h |
| **Recuperação** | Restore backup se necessário; validação integridade; monitoramento reforçado | ≤48h |
| **Pós-incidente** | Relatório (timeline, causa raiz, impacto, lições); atualização threat model | ≤7 dias |

**Notificação ao usuário (controlador):** ≤72h (LGPD Art. 48 / GDPR Art. 33) via email local + log de auditoria.

---

## 8. Residual Risk Acceptance

| Risco Residual | Justificativa de Aceitação | Monitoramento |
|----------------|---------------------------|---------------|
| Pepper HMAC comprometido (acesso servidor) | Requer comprometimento total do host; rotação anual limita janela | Alerta em rotação pepper; logs de acesso ao pepper |
| DoS via Argon2id (CPU) | Parâmetros balanceados; rate limit pré-Argon2id | Métricas CPU/latência login |
| Enumeração offline se DB vazado | Argon2id + HMAC pepper; sem pepper, hashes são inúteis | Monitoramento de vazamento DB (canary) |
| Anonimização incompleta (bug) | Testes automatizados + revisão de código; job de verificação periódica | Job diário verifica contas `deleted` com invoices não anonimizadas |

---

## 9. Aprovação

Este threat model **aprova a arquitetura de segurança** para a expansão multiusuário, condicionado à implementação fiel dos controles listados nas seções 4 e 5.

**Decisões de implementação ratificadas:**

- [x] Argon2id (parâmetros CR3-D01)
- [x] HMAC-SHA-256 com pepper rotativo anual
- [x] Double-submit CSRF + SameSite=Lax
- [x] Rate limit por IP + identificador
- [x] Row-Level Security PostgreSQL em todas tabelas
- [x] `pgcrypto` para dados bancários
- [x] SMTP local/autohospedado (Postfix container)
- [x] Anonimização seletiva invoices (hash + supressão)
- [x] `account_lifecycle_events` append-only auditoria
- [x] Logs zero PII/valores/corpo
- [x] WeasyPrint `_RefusingUrlFetcher` + CSP estrito

---

## 10. Próximos Passos

1. **CCB ratifica** threat model + parecer jurídico
2. **Implementação** dos controles nas specs SPEC-017 (identidade), SPEC-018 (prestadora/banco), SPEC-022 (lifecycle)
3. **Testes de segurança** no pipeline CI (SAST/DAST/Dependency)
4. **Pentest leve** pré-produção
5. **Revisão anual** do threat model (ou após incidente/mudança arquitetural)

---

## CHANGELOG

- 1.0.0 — 2026-11-14: Threat model emitido para CR-008; STRIDE completo, OWASP Top 10 mapeado, controles por camada, attack trees, testes requeridos, response plan. Condiciona SPEC-017, 018, 022.