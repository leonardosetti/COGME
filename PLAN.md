# PLAN — Implementação das specs aprovadas (COGME)

## Contexto
Implementação SDD das especificações aprovadas/ratificadas em `.ai/specs/`. Método: especifica → implementa → valida → registra.

## Spec-004 (backend-mvp-v1, ratificada v2.0.0) ✅ 100% CONCLUÍDA

### Onda A — Auth + autorização ✅
- Sessão (cookie HttpOnly, sliding 24h), CSRF double-submit, rate limiting (slowapi)
- Router /v1/auth: register, login, logout, reset-request/reset-confirm, me, aliases
- P-14 isolamento por proprietário em todas rotas recurso (404 cross-user)
- Modelos ProviderProfile, ProviderBankAccount

### Onda B — Novos recursos ✅
- /v1/provider: profile, bank-accounts (CRUD)
- /v1/clients: list/create/get/update/activate/deactivate
- /v1/simulations: list/save(opt-in)/get
- /v1/account: DELETE (erase LGPD), POST /reactivate
- Auditoria AccountLifecycleEvent (sem PII)

### Onda C — Verificação ✅
- POST /v1/invoices (criar draft, número sequencial DEC-06)
- PUT /v1/invoices/{id} (atualizar draft, finalized imutável)
- GET /v1/invoices/{id}/download (PDF, SPEC-021)
- Testes: test_invoice_draft.py (6), test_auth_csrf_rate.py (5)
- 1192 testes passando, 0 falhando

## Outras specs aprovadas — avaliar implementação
- spec-007 (invoice-data-model, ratificada v2.0.0): modelos ORM já implementados (invoice.py, client.py, simulation.py, user.py, provider.py)
- spec-008 (frontend-web-responsive): frontend ainda não implementado (index.html 0 B, static/ vazio)
- spec-015 (lgpd-produto-proposta): proposta, não ratificada
- spec-001/002/003/005/006/009/010/011/012/013/014/016: specs de processo/documentação

## Critérios de aceite spec-004 §10
- AC-HTTP-01..06 ✅ (06: novos códigos como strings literais)
- AC-AUTH-01..07 ⬜ (testes de integração com banco — dependem de COGME_TEST_DATABASE_URL)
- AC-PERSIST-01..04 ✅
- AC-SEC-01..04 ⬜ (pgcrypto/SMTP dependem do container Docker)

## Próximos passos sugeridos
1. Testes de integração com PostgreSQL (AC-AUTH-01..07, AC-SEC)
2. Implementar frontend (spec-008) — index.html e static/ estão vazios
3. Verificar pgcrypto (criptografia bancária) e SMTP (reset de senha) no container
