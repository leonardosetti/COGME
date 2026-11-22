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
