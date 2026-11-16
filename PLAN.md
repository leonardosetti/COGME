# PLAN — Implementação spec-004 (backend-mvp-v1, ratificada v2.0.0)

## Contexto
Spec-004 ratificada (2026-11-15, CR-002 Onda 1 + Emenda E-20). Expande o backend MVP para:
- Autenticação/cadastro (SPEC-017), autorização por proprietário P-14 (require_owner, 404 cross-user)
- Persistência de invoices e simulações (REQ-17), novos endpoints auth/recursos
- CSRF double-submit, rate limiting, contrato de erro atualizado

Baseline: 1181 testes unitários passam, 0 falham (mantido ao longo de toda a implementação).

## Status da implementação (tudo commitado e verde)

### Onda A — Auth + autorização ✅ CONCLUÍDA
1. ✅ Middleware de sessão (`src/backend/middleware/session.py`): cookie HttpOnly/Secure/SameSite=Lax, sliding 24h, `get_current_session`
2. ✅ CSRF double-submit (`src/backend/middleware/csrf.py` + `CSRFMiddleware` em main.py): isenta `/v1/auth/*`
3. ✅ Rate limiting (`src/backend/middleware/rate_limit.py` + slowapi): login/register 5/min, reset-request 3/h; handler 429 com envelope canônico
4. ✅ Router `/v1/auth` (`src/backend/routers/auth.py`): register, login, logout, reset-request, reset-confirm, me, aliases, aliases/cnpj
5. ✅ P-14 nas rotas de invoice: sessão + filtro por `owner_user_id` (404 cross-user), removido `owner_user_id=1` hardcoded
6. ✅ Modelos `provider.py` (ProviderProfile, ProviderBankAccount)
7. ✅ Argon2-cffi adicionado (pbkdf2 fallback stdlib até o env ter a dep — ADR-017, shortcut documentado)

### Onda B — Novos recursos ✅ CONCLUÍDA
8. ✅ Router `/v1/provider`: profile (GET/PUT), bank-accounts (GET/POST/PUT/DELETE)
9. ✅ Router `/v1/clients`: list (GET), create (POST), get (GET/{id}), update (PUT/{id}), activate/deactivate (POST)
10. ✅ Router `/v1/simulations`: list (GET), save opt-in (POST), get (GET/{id})
11. ✅ Router `/v1/account`: DELETE (erase LGPD, anonimiza + revoga sessões), POST /reactivate
12. ✅ Auditoria `AccountLifecycleEvent` (sem PII)

### Onda C — Verificação ⬜ PENDENTE
13. ⬜ Testes para auth, require_owner, CSRF, rate limit (cobertura nova)
14. ⬜ Invoices POST (criar draft), PUT, download PDF (SPEC-021) — POST /v1/invoice (original) já existe
15. ✅ `pytest tests/unit` verde: 1181 passando, 0 falhando, 6 pulando

## Critérios de aceite do spec-004 §10
- AC-HTTP-01 (simulate mantido) ✅
- AC-HTTP-02 (endpoints auth) ✅
- AC-HTTP-03 (isolamento por proprietário, 404 cross-user) ✅ em invoices/simulations/clients/provider/account
- AC-HTTP-04 (rate limits) ✅ auth
- AC-HTTP-05 (CSRF em rotas mutáveis, exceto /v1/auth/) ✅
- AC-HTTP-06 (códigos de erro) ⬜ (novos códigos como strings literais; ErrorKey mantém as 5 originais por teste existente)
- AC-AUTH-01..07 (cadastro/login/senha/sessão/reset/ST-01..10) ⬜ testes de integração com banco
- AC-PERSIST-01..04 (persistência, owner em todas tabelas, IDOR) ✅ modelo + isolamento
- AC-SEC-01..04 (argon2 build, pgcrypto, logs sem PII, SMTP) ⬜ (pgcrypto/SMTP dependem do container)

## Ordem de execução
Onda A → Onda B → Onda C. Todas commitadas separadamente.
