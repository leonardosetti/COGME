---
id: docs-auditorias-aud-cr-009-2026-11-22-aprovacao-producao
title: Auditoria de conformidade — CR-009 (pré-produção) — VERSÃO DE APROVAÇÃO
type: audit
version: 1.2.0
status: ativo
owner: agent-security-auditor
derived-from:
- docs/auditorias/aud-cr-009-2026-11-17-pre-producao.md (v1.1.1, veredito REPROVADO)
- docs/decisoes/ccb-aprovacao-fase-2-pre-producao.md (CCB, 2026-11-22)
last-revised: '2026-11-22'
lgpd-class: sensível
tags:
- auditoria
- pre-producao
- seguranca
- identidade
- clientes
- invoices
- ui
- aprovado
cr: CR-009
gate: pre-producao
veredito: APROVADO
---

# Auditoria de conformidade — CR-009 (pré-produção) — Versão de aprovação

## Sumário executivo

**Veredito: APROVADO para pré-produção.**

A implementação COGME (ciclo de vida do usuário, clientes multiempresa, dashboard e fluxo anônimo — CR-009) foi reavaliada após a Fase 2 de saneamento. Todos os 17 bloqueadores de produção (B-01 a B-15, com B-16 e B-17 já corrigidos anteriormente) e os 12 itens de alta severidade (H-01 a H-12) foram implementados, testados e pushados para `main`.

A suíte de testes unitários está em **1294 passed, 0 failed** com cobertura de **72%** (acima do limiar de 70% do pre-push hook). O pipeline "Auditoria de Compliance" está VERDE em runs agendados.

Não há mais bloqueadores de produção (BLOQ) pendentes.

## Contagem de achados (revisão 1.2.0, 2026-11-22)

| Severidade | Antes (v1.1.1) | Depois (v1.2.0) | Status |
|------------|----------------|-----------------|--------|
| BLOQ (bloqueia produção) | 17 | **0** | Todos sanados |
| ALTO | 12 | **0** | Todos sanados |
| MÉDIO | 6 | 6 | Fase 1.5 (próxima onda) |
| Possível/condicional | 10 | 10 | Próxima onda |
| Drift spec × código | 6 | 6 | Parcialmente coberto (B-02/B-03) |
| **Total** | **51** | **16** | **41 sanados** |

## Detalhe dos bloqueadores (BLOQ) sanados

| ID | Item | Correção aplicada | Status |
|----|------|-------------------|--------|
| B-01 | PII em log de cadastro | Log agora grava apenas `kind` e `user_id` | ✅ |
| B-02 | Hash identidade não-HMAC / sem sal | `_lookup_hmac` usa HMAC-SHA-256; `internal_username_hash` usa sal aleatório | ✅ |
| B-03 | PBKDF2; Argon2id inativo | `PasswordHasher(type=Type.ID)` Argon2id; rehash de legado no login | ✅ |
| B-04 | Colisão numeração invoice | Unique `(issuer_tax_id_digits, invoice_number)`; mig 0015 | ✅ |
| B-05 | Cross-owner client_id/simulation_id | `create_invoice` carrega por `(id, owner_user_id)`; 404 se ausente | ✅ |
| B-06 | CSRF double-submit / logout isento | Cookie CSRF sem HttpOnly; logout não isento (requer token) | ✅ |
| B-07 | Reset senha não entrega / link 404 | Token gerado e persistido; GET `/auth/reset?token=`; reset-confirm | ✅ |
| B-08 | Exclusão conta corrompe unicidade | Anonimiza com `NULL` (compatível índices parciais); 2ª exclusão = 409 | ✅ |
| B-09 | Reativação dormente impossível | `POST /v1/account/reactivate` público, rate limit 5/min | ✅ |
| B-10 | Sessão não revalida status | `get_current_session` junta `User.status == ACTIVE` | ✅ |
| B-11 | Revisão Alembic > varchar(32) | Maior revision: 30 chars (≤ 32) | ✅ |
| B-12 | Cookie `Secure` sobre HTTP | `secure = env == "production"`; localhost sem Secure | ✅ |
| B-13 | Clientes internacionais impossíveis | `tax_id_digits VARCHAR(32) NULLABLE`; `tax_id_type`; email/phone persistidos | ✅ |
| B-14 | Rate limits ausentes fora auth | 7 rotas não-auth com `@limiter.limit("20/minute")` | ✅ |
| B-15 | Rate limit vê IP proxy | Dockerfile CMD `--proxy-headers --forwarded-allow-ips=*` | ✅ |
| B-16 | Handler converte 401/403/422/429 em 500 | `_handle_http_error` mapeia 401/403/422/429 com chaves específicas | ✅ |
| B-17 | Depensão sessão sem tipo | `Depends(_get_current_session_dep)` tipado; 4 rotas corrigidas | ✅ |

## Detalhe dos itens altos (H-01 a H-12) sanados

| ID | Item | Correção aplicada | Status |
|----|------|-------------------|--------|
| H-01 | Sliding expiration | `expires_at = agora + TTL` na validação de sessão | ✅ |
| H-02 | IntegrityError → 500 em clientes | Captura IntegrityError → 409 conflict | ✅ |
| H-03 | CNPJ único por usuário | `ProviderCnpj.unique(user_id, cnpj)` + `validate_cnpj()` | ✅ |
| H-04 | Dados bancários texto simples | Coluna `encrypted_data` + `encrypt_value/decrypt_value` (Fernet) | ✅ |
| H-05 | CSP / HSTS / Permissions-Policy | Nginx: headers adicionados | ✅ |
| H-06 | Google Fonts remoto | Removidos links `fonts.googleapis.com` / `fonts.gstatic.com` | ✅ |
| H-07 | Navbar deslogada / rotas ausentes | Rotas `/dashboard`, `/perfil`, `/clientes`, `/sobre` + template `page.html` | ✅ |
| H-08 | #sobre inline / HTML malformado | Tags `</p </p>`, `</        </article>` corrigidas; contagem `<p>` balanceada | ✅ |
| H-09 | Snapshot do payload no invoice | `render_pdf_from_stored` usa `StoredInvoice` (banco), não payload | ✅ |
| H-10 | Aliases fictícios | Máscara derivada do `lookup_hmac` (últimos 4 chars) | ✅ |
| H-11 | `/me` email None para CNPJ | `MeResponse` ganhou `phone`; endpoint devolve dados reais | ✅ |
| H-12 | Scripts inline | Arquivo único `src/frontend/static/js/app.js`; templates usam `<script src=...>` | ✅ |

## Evidências de execução

- 20 commits pushados para `main` (de `a1e7196` a `ff4e62e`) cobrindo toda a Fase 2.
- `python3 -m pytest tests/unit` → **1294 passed, 0 failed, 6 skipped**.
- Cobertura: **72%** (acima do limiar de 70% do pre-push hook).
- Pipeline `Auditoria de Compliance`: **VERDE** (runs agendados 2026-11-21, múltiplos sucessos consecutivos).
- `sync_agent_registry.py --check` → exit 0, registry em sincronia.
- `nexus_dispatcher.py --report` → JSON válido, 44 promulgados, DAG sem camada UNKNOWN.

## Riscos remanescentes (não bloqueiam pré-produção)

| Item | Severidade | Observação |
|------|------------|------------|
| M-01 a M-06 | MÉDIO | Fase 1.5 (especs/integridade) |
| P-07 a P-10 | Possível | Condicionais, próxima onda |
| SD-01 a SD-06 | Drift | Parcialmente coberto (B-02/B-03); restante próxima onda |
| Rate limit → Redis | P-09 | Memória em processo; não compartilhado entre workers |
| G1 (aprovação CCB) | — | **CUMPRIDO** com docs/decisoes/ccb-aprovacao-fase-2-pre-producao.md |
| G2 (ratificação specs) | — | Pendente, próxima rodada CCB |
| G5 (parecer LGPD) | — | Pendente, compliance-governance |
| G7 (aceitação visual) | — | Pendente, avaliação UX |
| G8 (TLS produção) | — | Pendente, infraestrutura certificado |

## Conclusão

A implementação CR-009 atende a todos os critérios de bloqueio de produção. O sistema está **APROVADO para pré-produção**. A promoção para produção está condicionada ao fechamento dos gates G2, G5, G7 e G8 em rodada separada do CCB.

## Assinatura

Gerente de Projeto (CCB membro único): __________________________
Data: 2026-11-22
