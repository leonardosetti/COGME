---
id: docs-qualidade-09-relatorio-resumo-de-teste
title: Relatório Resumo de Teste — ISTQB CTFL (Test Summary Report)
type: relatorio
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/07-registro-de-teste.md (execuções E-001, E-002, E-003)
- docs/qualidade/08-relatorio-incidente-de-teste.md (incidentes)
- docs/uat/rodada-001/relatorio-analitico.md (veredito UAT)
- docs/planos/plano-granular/plano-qualidade.md (§5.3 métricas)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- istqb
- relatorio-resumo-de-teste
- test-summary-report
- qualidade
---

# Relatório Resumo de Teste — COGME (ISTQB CTFL Test Summary Report)

## 1. Identificação

| Campo | Valor |
|---|---|
| Projeto | COGME — Conversor de Ganhos em Moeda Estrangeira |
| Artefato | Test Summary Report |
| Versão | 1.0.0 |
| Período coberto | Execuções E-001 (13/11/2026), E-002 (31/10/2026), E-003 (planejada, 14/11/2026) |
| Base | Registro de Teste (docs/qualidade/07-registro-de-teste.md); Relatório de Incidente (docs/qualidade/08-relatorio-incidente-de-teste.md) |
| Rastreabilidade | RTM em docs/qualidade/10-rtm-qualidade.md |

## 2. Resumo executivo

A suíde de testes automatizados do COGME (unidade + integração, pytest) está verde: **1392 casos executados, 0 falhas, 0 defeitos críticos/bloqueantes**. A UAT rodada 001 foi executada em 13/11/2026 com **14/14 casos PASS** e veredito **APROVADA** (15/11/2026 01:39). Três incidentes de falso positivo no CI/CD (segurança, health check, credenciais) foram investigados e resolvidos por auditorias extraordinárias. Três incidentes pendentes estão abertos (testes pulados, drift de cobertura, evidências PDCA) com ações corretivas definidas.

Uma nova camada de teste funcional/E2E (Playwright + Screenplay Pattern) foi instituída nesta disciplina (docs/qualidade/00-contexto-disciplina-qualidade.md) e aguarda primeira execução (E-003).

## 3. Resultados por execução

| Execução | Data | Suíte | Casos | PASS | FAIL | Skip | Cobertura src/ | Veredito |
|---|---|---|---|---|---|---|---|---|
| E-001 | 13/11/2026 | pytest (unit + integration) | 1405 | 1392 | 0 | 13 | ≥ 80% (meta); CI gate 95% | APROVADO |
| E-002 | 31/10/2026 | security_scan + agent_health + pytest | 181 | 181 | 0 | 1 | — | APROVADO |
| E-003 | 14/11/2026 (planejada) | Playwright (funcional/E2E) | 5 | 0 | 0 | 5 | — | Pendente |

## 4. Cobertura de teste

| Métrica | Valor | Meta | Status |
|---|---|---|---|
| Cobertura de linhas sobre `src/` | ≥ 80% (plano-qualidade §5.3) | ≥ 80% | Atende (documento) |
| Gate de cobertura CI (`--cov-fail-under`) | 95% (ci.yml:213) | 95% | Atende (CI) |
| Requisitos REQ-01 a REQ-07 cobertos por teste | 100% | 100% | Atende (RTM) |
| Casos de teste com rastreabilidade na RTM | 100% | 100% | Atende (RTM preenchida) |
| Testes pulados | 13 | 0 (regra CI zero-skipping) | Não atende — INC-004 |

**Nota sobre drift:** o documento `plano-qualidade.md` declara 80% enquanto o CI exige 95%. Incidente INC-005 aberto para alinhamento.

## 5. Defeitos e incidentes

| Status | Quantidade | IDs |
|---|---|---|
| Resolvidos | 4 | INC-001, INC-002, INC-003, INC-007 |
| Pendentes/Abertos | 3 | INC-004, INC-005, INC-006 |
| Defeitos críticos/bloqueantes em UAT | 0 | — |

Todos os incidentes têm RCA, prioridade, impacto e severidade definidos em `docs/qualidade/08-relatorio-incidente-de-teste.md` e no board de resultados (`docs/qualidade/11-board-resultados-qualidade.md`).

## 6. Avaliação de risco e confiança

| Risco | Nível | Mitigação |
|---|---|---|
| Regressão sem detecção (coverage abaixo do real) | Médio | Gate CI 95% + zero-skipping + revisão de PR |
| Falso positivo de CI bloqueia entrega | Baixo | Detecção com contexto (INC-001/003 resolvidos); legacy-forge aceito (INC-002) |
| E2E não executado (nova camada) | Médio | Playwright instituído; primeira execução E-003 agendada |

## 7. Conclusão e recomendação

O nível de qualidade do COGME está adequado para a entrega do MVP: suíte automatizada verde, UAT aprovada sem defeitos críticos, cobertura acima da meta do termo autorizativo, e processo de detecção precoce (Shift-Left) operando no CI. Recomenda-se:

1. Executar a camada funcional Playwright (E-003) e fechar INC-004 (alinhar skip condicional ao CI).
2. Alinhar plano-qualidade.md ao gate de 95% (fechar INC-005).
3. Registrar lições por PDCA MF2/MF3 (fechar INC-006).
4. Manter a RTM atualizada a cada novo requisito/caso de teste.

## 8. Aprovação

| Papel | Nome/Função | Data | Assinatura |
|---|---|---|---|
| Autor | qa-sdet (agent-qa-sdet) | 14/11/2026 | |
| Revisor | reviewer (agent-reviewer) | | |
| Gatekeeper | gatekeeper (agent-gatekeeper) | | |
| Auditor | auditor (agent-project-auditor) | | |

## 9. Anexos

- docs/qualidade/07-registro-de-teste.md (Test Log)
- docs/qualidade/08-relatorio-incidente-de-teste.md (Test Incident Report)
- docs/qualidade/10-rtm-qualidade.md (RTM)
- docs/qualidade/11-board-resultados-qualidade.md (Board de Análise + RCA)
- docs/uat/rodada-001/relatorio-analitico.md (UAT rodada 001)
