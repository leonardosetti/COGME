# PLAN — Implementação spec-004 (backend-mvp-v1, ratificada v2.0.0)

## Contexto
Spec-004 ratificada (2026-11-15, CR-002 Onda 1 + Emenda E-20). Expande o backend MVP para:
- Autenticação/cadastro (SPEC-017), autorização por proprietário P-14 (require_owner, 404 cross-user)
- Persistência de invoices e simulações (REQ-17), novos endpoints auth/recursos
- CSRF double-submit, rate limiting, contrato de erro atualizado

Baseline: 1181 testes unitários passam, 0 falham. Código já tem modelos ORM (users, sessions, clients, simulations, invoices), repositórios (quotes, invoices), serviços (calculator, rate_service, simulation_service, invoice_service) e routers (health, rates, simulate, invoice, invoices CRUD com `owner_user_id` via Query hardcoded = 1).

## O que falta (comparado ao spec-004 §4)

### Onda A — Auth + autorização (bloqueante, muda todos os routers)
1. Middleware de sessão (`get_current_session`, cookie `session`, sliding 24h)
2. Middleware `require_owner` (P-14: `owner_user_id` em todas rotas recurso, 404 cross-user)
3. Middleware CSRF (double-submit cookie + `X-CSRF-Token`; isenta `/v1/auth/*`)
4. Rate limiting (slowapi): auth 5/min IP, reset 3/h identificador, API 100/min
5. Router `auth.py`: register, login, logout, reset-request, reset-confirm, me, aliases
6. Atualizar routers existentes (invoices, simulations) para `require_owner` + sessão (remover `owner_user_id=1` hardcoded)
7. Error schema: novos códigos AUTH_*, AUTHZ_*, etc.

### Onda B — Novos recursos (SPEC-018/019/020/021/022)
8. Modelos provider_profile + provider_bank_accounts (SPEC-018)
9. Router provider: profile (GET/PUT), bank-accounts (GET/POST/PUT/DELETE)
10. Router clients: list/get/create/update/deactivate/activate (modelo Client existe)
11. Router simulations salvos: list/get (modelo Simulation existe)
12. Invoices POST (draft), PUT, download PDF (SPEC-021); account DELETE/reactivate (SPEC-022)

### Onda C — Verificação
13. Testes para auth, require_owner, CSRF, rate limit
14. `pytest tests/unit` verde; cobertura ≥ 80%

## Ordem de execução
Onda A → Onda B → Onda C. Cada onda commitada separadamente.

## Critérios de aceite (do spec-004 §10)
- AC-HTTP-01..06, AC-AUTH-01..07, AC-PERSIST-01..04, AC-SEC-01..04
- `require_owner` em 100% rotas recurso; teste IDOR cross-user (ST-03)
