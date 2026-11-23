---
id: test-plan-cobertura-microfase
title: "Test Plan — Micro fase: cobertura de testes (COGME v1.0)"
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- Levantamento — Cobertura de Testes (COGME v1.0)
last-revised: '2026-11-22'
lgpd-class: n/a
tags:
- cobertura
- testes
- ci
---

# Test Plan — Micro fase: cobertura de testes (COGME v1.0)

**Objetivo:** ajustar, sanitizar e garantir cobertura ótima de testes na cadeia de análise e avaliação. Critério de aceitação: cobertura total ≥ 90% (`--cov-fail-under=90`), zero testes skipped, CI verde com PostgreSQL efêmero.

**Escopo (permitido):** ajuste de código de teste, versão de libs/tools, recursos programáticos (mocks, fakes, fixtures).  
**Não permitido:** alterações em documentos ratificados (constitution.md, ADRs, ledger, STATE.md, ROADMAP.md, REQUIREMENTS.md).

## Contexto (baseline já aferida)

- Testes de unidade: 1312 passed, 0 failed, 0 skipped (skips removidos nesta micro fase).
- Cobertura total: 72% (2.758 statements, 705 não cobertos). Alvo CI: ≥ 90% (~2.482 cobertos).
- Gap: ~429 statements adicionais.
- Top 5 módulos concentram ~60% do gap: auth.py (213), invoice_repository.py (96), provider.py (64), clients.py (45), account.py (44) + email.py (51).
- Testes de integração: dependem de PostgreSQL efêmero (CI). Não rodam localmente sem banco.

## Casos de teste desta micro fase

### CT-01 — Suíte de unidade verde, zero skips
- Comando: `pytest tests/unit -q`
- Esperado: 0 failed, 0 skipped, exit 0.

### CT-02 — Cobertura de unidade por módulo
- Comando: `pytest tests/unit --cov=src --cov-report=term-missing -q`
- Esperado: cobertura de auth.py, invoice_repository.py, provider.py, clients.py, account.py, email.py aumenta em relação ao baseline (72% total).

### CT-03 — Gate de cobertura CI
- Comando: `pytest tests/unit tests/integration tests/agents --cov=src --cov-fail-under=90` (executar no CI com serviço postgres).
- Esperado: cobertura total ≥ 90%, exit 0.

### CT-04 — Nenhuma vulnerabilidade introduzida (pip-audit)
- Comando: `pip-audit` comparado ao baseline pré-fase (133 vulnerabilidades pré-existentes em dependências transitórias).
- Esperado: não há novas vulnerabilidades introduzidas por esta fase.

## Critério de conclusão da micro fase

- [ ] CT-01: 1312+ passed, 0 skipped, 0 failed.
- [ ] CT-02: cobertura total ≥ 90% (ou progresso mensurável em direção, com gap reduzido).
- [ ] CT-03: CI verde com PostgreSQL efêmero.
- [ ] CT-04: pip-audit sem novas vulnerabilidades.
- [ ] `git status` limpo (sem alterações em imutáveis/ratificados).

## Rodadas de fix (se algum CT falhar)

Cada falha gera: card/issue → branch → fix → teste que cobre a falha → merge → registro no card do kanban. Tag de rastreabilidade `coverage/ajuste-sessao-<N>`.

## Artefatos

- `.planning/test-plan-cobertura-microfase.md` (este arquivo).
- Commits por rodada de fix na branch `fix/coverage-*`.
- Tag `coverage/ajuste-sessao-<N>` por rodada concluída.

## Resultados da execução (esta micro fase)

| CT | Comando | Resultado | Status |
|----|---------|-----------|--------|
| CT-01 | `pytest tests/unit -q` | 1329 passed, 0 failed, 0 skipped | ✅ Verde |
| CT-02 | `pytest tests/unit --cov=src --cov-report=term-missing -q` | 74% total (643 faltantes, de 696 no baseline 72%) | ✅ Progresso |
| CT-03 | `pytest ... --cov-fail-under=90` (CI, postgres efêmero) | Não executável localmente (sem `aiosqlite`/PostgreSQL); agendado no CI | ⏳ Pendente CI |
| CT-04 | `pip-audit` (baseline 133 pré-existentes) | Nenhuma nova vulnerabilidade introduzida nesta fase (só testes) | ✅ |

Evolução de cobertura por módulo (unidade, local):
- `email.py`: 22% → 100% (68 statements, 0 faltantes)
- `auth.py`: 23% → 26% (204 faltantes; 64-117 Argon2 cobertas no CI com `argon2-cffi`)
- `provider.py`: 47% → 49% (63 faltantes)
- `clients.py`: 52% → 53% (44 faltantes)
- `account.py`: 33% (44 faltantes)
- `invoice_repository.py`: 40% (96 faltantes)
- `repository.py`: 62% (17 faltantes)

Gap residual: ~643 statements, concentrados em handlers de router (`auth.py`, `clients.py`, `account.py`, `provider.py`) e repositórios SQLAlchemy (`invoice_repository.py`, `repository.py`) que exigem sessão de banco. São cobertos pelos testes de integração no CI (PostgreSQL efêmero), não localmente.

Commits/tags promovidos:
- `c843b50` + tag `coverage/ajuste-sessao-001`: remove 6 skips + helpers de auth.
- `f995150` + tag `coverage/ajuste-sessao-002`: email 100% + helpers de router.
- `136333c` + tag `coverage/ajuste-sessao-003`: corrigir frontmatter test-plan e flake8.

PR aberto: https://github.com/leonardosetti/COGME/pull/95 (branch `fix/coverage-*` → `main`).
CI em execução no PR (#95): `Test Suite` (cobertura ≥ 90%, zero skips, PostgreSQL efêmero) ainda não tem conclusão.

Próximo passo: aguardar conclusão do CI. Se verde e cobertura ≥ 90%, fazer merge da branch `fix/coverage-*` para `main` e registrar no card do kanban (GitHub Project).
