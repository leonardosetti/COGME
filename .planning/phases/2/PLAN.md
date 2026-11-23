---
id: cogme-plan-2
title: COGME — PLAN Fase 2
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .planning/phases/2/PLAN.md
last-revised: '2026-11-22'
lgpd-class: n/a
tags:
- planejamento
- fase-2
- planejamento
---

# PLAN — Fase 2: Pré-produção CR-009 (ENCERRADA)

## Fase
Número: 2 | Slug: `pre-producao-cr-009` | Status: **ENCERRADA**

## Goal (entregue)
Deixar a implementação liberada para produção (pré-produção CR-009): fechar **15 BLOQ** (B-01 a B-15; B-16 e B-17 já em main) e os **12 ALTO** (H-01 a H-12), de acordo com a auditoria `docs/auditorias/aud-cr-009-2026-11-17-pre-producao.md` v1.1.1 (veredito REPROVADO → APROVADO).

## Entregas realizadas

| Item | Status | Commit |
|------|--------|--------|
| B-01 PII em log cadastro | ✅ | 3309349 |
| B-02 HMAC identidade | ✅ | 3309349 |
| B-03 Argon2id ativo | ✅ | 3309349 |
| B-04 Invoice unique composto | ✅ | f382332 |
| B-05 Cross-owner client/simulação | ✅ | 3309349 |
| B-06 CSRF cookie/logout | ✅ | 3309349 |
| B-07 Reset senha entrega token | ✅ | código já existia, testado |
| B-08 Exclusão conta unicidade | ✅ | 029aba8 |
| B-09 Reativação dormente | ✅ | 029aba8 |
| B-10 Sessão revalida status | ✅ | 693946e |
| B-11 Alembic ≤32 chars | ✅ | b160ef7 |
| B-12 Cookie Secure só produção | ✅ | 693946e |
| B-13 Clientes internacionais | ✅ | f382332 |
| B-14 Rate limits não-auth | ✅ | 535bd6d |
| B-15 Rate limit IP proxy | ✅ | 33e2ce0 |
| H-01 Sliding expiration | ✅ | 1d86b4a |
| H-02 IntegrityError → 409 | ✅ | 60a02c3 |
| H-03 CNPJ único + checksum | ✅ | 273aa67 |
| H-04 Dados bancários criptografados | ✅ | 0a5e31a |
| H-05 CSP/HSTS/Permissions-Policy | ✅ | e2d02bb |
| H-06 Google Fonts removido | ✅ | 063d85e |
| H-07 Navbar/dashboard/perfil/clientes/sobre | ✅ | 60d6a0e |
| H-08 #sobre HTML válido | ✅ | 08abb64 |
| H-09 Snapshot do banco no PDF | ✅ | a933616 |
| H-10 Aliases reais mascarados | ✅ | e30e304 |
| H-11 /auth/me email e telefone | ✅ | 693946e |
| H-12 Scripts inline → arquivo externo | ✅ | ff4e62e |

## Métricas finais
- Suíte de testes: **1294 passed, 0 failed, 6 skipped**
- Cobertura: **72%** (hook pre-push: 70%)
- Pipeline Auditoria de Compliance: **VERDE**
- `sync_agent_registry.py --check`: exit 0
- `nexus_dispatcher.py --report`: JSON válido, sem camada UNKNOWN

## Decisão CCB
`docs/decisoes/ccb-aprovacao-fase-2-pre-producao.md` — APROVADO e RATIFICADO (2026-11-22)

## Auditoria
`docs/auditorias/aud-cr-009-2026-11-22-aprovacao-producao.md` — veredito **APROVADO para pré-produção**

## Completude
`docs/auditorias/relatorio-completude-sistema.md` — **86.2%** (100% nos itens que bloqueiam produção)

## Próxima fase
**Fase 1.5 — Especs/integridade (TA-061 a TA-065):**
- TA-061: emendas spec-004/005 (HF-0617)
- TA-062: auditoria integridade specs 017–022 (HF-0618)
- TA-063: repovoar tap.md (HF-0619)
- TA-064: repovoar eap.md (HF-0620)
- TA-065: repovoar requisitos.md (HF-0621)

## Arquivos-chave modificados nesta fase
- `src/backend/routers/auth.py` — B-02, B-03, B-07, B-10, B-11, H-04, H-10, H-11
- `src/backend/routers/account.py` — B-08, B-09, B-14 (rate limit)
- `src/backend/routers/clients.py` — B-02, B-13, H-02
- `src/backend/routers/invoices.py` — B-04, B-05, B-09, B-14
- `src/backend/routers/provider.py` — B-14 (contas bancárias)
- `src/backend/routers/simulations.py` — B-14
- `src/backend/routers/rates.py` — B-14
- `src/backend/middleware/session.py` — B-10, H-01
- `src/backend/middleware/csrf.py` — B-06
- `src/backend/models/provider.py` — H-03, H-04
- `src/backend/models/client.py` — B-13 (já existia)
- `src/backend/models/invoice.py` — B-04 (já existia)
- `src/backend/models/user.py` — H-11 (já existia)
- `src/backend/schemas/auth.py` — H-11 (campo phone)
- `src/backend/models/database.py` — migrações 0009–0016 já existentes
- `infra/nginx/default.conf` — H-05
- `src/frontend/templates/` — H-06, H-07, H-08
- `src/frontend/static/js/app.js` — H-12 (novo)
- `Dockerfile` — B-15 (já existia)
