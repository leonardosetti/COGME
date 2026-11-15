---
id: docs-qualidade-03-plano-testes-istqb
title: Plano de Testes — ISTQB CTFL (Test Plan)
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/planos/plano-granular/plano-qualidade.md (§5, §5.3, §5.4, §5.5)
- .ai/specs/spec-010-qualidade-pdca-ishikawa-v1.spec.md (REQ-10, N6.3)
- docs/qualidade/00-contexto-disciplina-qualidade.md
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- istqb
- plano-de-testes
- test-plan
- qualidade
---

# Plano de Testes — COGME (ISTQB CTFL)

## 1. Identificação

| Campo | Valor |
|---|---|
| Projeto | COGME — Conversor de Ganhos em Moeda Estrangeira |
| Artefato | Plano de Testes (Test Plan, ISTQB CTFL) |
| Versão | 1.0.0 |
| Status | Ativo |
| Base | Plano de Gerenciamento da Qualidade v1.1.0; SPEC spec-004 (backend-mvp-v1); SPEC spec-008 (frontend web responsivo); SPEC spec-009 (UAT produto) |
| Critérios de aceite | Cobertura ≥ 95% sobre `src/`; zero testes pulados; UAT sem defeitos críticos/bloqueantes; CI verde em ≤ 5 min (lint+testes) |
| Rastreabilidade | REQ-01 a REQ-08, REQ-10, REQ-11; UAT-01 a UAT-07; F-01 a F-07 |

## 2. Escopo de teste

### Em escopo

- **Camada Unidade (pytest):** regras de negócio, schemas (validação decimal, enums, campos extras), serviços (taxa, simulação, invoice, número da invoice), circuit breaker, repositórios.
- **Camada Integração (pytest + TestClient):** contratos HTTP `/v1/*` (health, rates, simulate, invoice), persistência de invoice, lifespan, tratamento de erros canônico, PDF render (WeasyPrint real quando disponível), cache de cotação.
- **Camada Funcional/E2E (Playwright + Screenplay Pattern):** fluxos críticos pela UI — simulação pelos 5 regimes, emissão de invoice com download de PDF, erro de cotação indisponível (503).

### Fora de escopo

- Testes de desempenho/carga (não há requisito de performance além do tempo de CI).
- Testes de usabilidade formais (cobertos pela UAT de produto, spec-009).
- Testes contra provedores reais de cotação (Frankfurter/PTAX) — usam dublês; rede real proibida nos testes automatizados.
- Testes de banco de dados produção (usam PostgreSQL efêmero no CI).

## 3. Abordagem de teste (pirâmide + Shift-Left)

Ver `docs/qualidade/01-piramide-testes.md` e `docs/qualidade/02-shift-left.md`.

Resumo: unidade (maior volume, mais rápida) → integração (contratos/persistência) → funcional/E2E (fluxos críticos pela UI, poucos casos). Detecção o mais cedo possível (Shift-Left): requisitos com DoR, testes escritos com o código, análise estática e security scan em cada push.

## 4. Critérios de entrada e saída

### Entrada (DoR)

- Requisito aprovado com critérios de aceite GWT e rastreável na RTM.
- Código + teste no mesmo PR.
- Ambiente de teste disponível (fixtures determinísticos ou stack efêmero).

### Saída (DoD)

- Pipeline CI verde: kill-switch → foss-compliance → sdd-validation → agent-health → lint → test-suite → build-layers → contract-network.
- Cobertura ≥ 95% sobre `src/` (`--cov-fail-under=95`).
- Zero testes pulados.
- Todos os casos de teste associados ao requisito executados com resultado PASS, ou defeito registrado com RCA.
- Code review aprovado + tasklist concluída (ADR-004).

## 5. Estratégia de automação

| Nível | Ferramenta | Linguagem | Padrão | Local |
|---|---|---|---|---|
| Unitário | pytest | Python | Fixtures + dublês determinísticos | `tests/unit` |
| Integração | pytest + FastAPI TestClient | Python | Injeção de `RateService` dublê | `tests/integration` |
| Funcional/E2E | Playwright | Python | Screenplay Pattern | `tests/e2e_playwright` |

## 6. Entregáveis de teste (artefatos ISTQB)

| # | Artefato ISTQB | Caminho | Status |
|---|---|---|---|
| 1 | Plano de Testes (Test Plan) | `docs/qualidade/03-plano-testes-istqb.md` | Ativo |
| 2 | Especificação de Projeto de Teste (Test Design Specification) | `docs/qualidade/04-especificacao-projeto-teste.md` | Ativo |
| 3 | Especificação de Caso de Teste (Test Case Specification) | `docs/qualidade/05-casos-de-teste.md` | Ativo |
| 4 | Especificação de Procedimento de Teste (Test Procedure Specification) | `docs/qualidade/06-procedimento-de-teste.md` | Ativo |
| 5 | Relatório de Item de Teste Transmitido (Test Item Transmittal Report) | `docs/qualidade/06-procedimento-de-teste.md` (§5) | Ativo |
| 6 | Registro de Teste (Test Log) | `docs/qualidade/07-registro-de-teste.md` | Ativo |
| 7 | Relatório de Incidente de Teste (Test Incident Report) | `docs/qualidade/08-relatorio-incidente-de-teste.md` | Ativo |
| 8 | Relatório Resumo de Teste (Test Summary Report) | `docs/qualidade/09-relatorio-resumo-de-teste.md` | Ativo |
| 9 | Matriz de Rastreabilidade de Requisitos (RTM) | `docs/qualidade/10-rtm-qualidade.md` | Preenchida |
| 10 | Board de Análise de Resultados + RCA | `docs/qualidade/11-board-resultados-qualidade.md` | Preenchido |

## 7. Recursos e responsabilidades (RACI, spec-010 §3.4)

| Atividade | GP | qa-sdet | reviewer | gatekeeper | auditor |
|---|---|---|---|---|---|
| Executar suíte de teste | I | R | C | C | I |
| Analisar cobertura e defeitos | A | R | C | C | I |
| Aprovar merge (regra de ouro) | I | C | R | A | I |
| Auditar rastreabilidade fim-a-fim | C | I | I | C | R/A |

## 8. Riscos e mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Cobertura < 95% bloqueia merge | Média | Alta | TDD para REQ-01..07; `--cov-fail-under=95` |
| Teste pulado invalida gate | Baixa | Alta | Regra zero-skipping no CI; revisão de PR |
| Falso positivo de CI (segurança/FOSS) | Média | Média | Auditoria extraordinária; refatorar detecção, não bypass |
| Ambiente de E2E indisponível | Baixa | Média | Stack efêmero no CI (docker compose); dublês onde possível |

## 9. Cronograma e cadência

- Execução da suíte: a cada push/PR (CI) e localmente antes do commit.
- UAT: por marco (M3 = 15/11/2026, rodada 001 executada; M4 = 15/12/2026, rodada 002 planejada).
- Revisão do plano de testes: a cada marco ou em mudança de escopo (CCB).

## 10. Aprovação

| Papel | Nome/Função | Data | Assinatura |
|---|---|---|---|
| Autor | agent-project-analyst | 14/11/2026 | |
| Revisor | agent-reviewer | | |
| Gatekeeper | agent-gatekeeper | | |
| Auditor | agent-project-auditor | | |
