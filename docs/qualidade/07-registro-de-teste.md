---
id: docs-qualidade-07-registro-de-teste
title: Registro de Teste — ISTQB CTFL (Test Log)
type: test
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/06-procedimento-de-teste.md
- docs/uat/rodada-001/relatorio-analitico.md (§1, §2, §5)
- docs/auditorias/ (incidentes AUD-2610-09/10/11)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- istqb
- registro-de-teste
- test-log
- execucao-de-teste
---

# Registro de Teste — COGME (ISTQB CTFL Test Log)

## 1. Identificação

| Campo | Valor |
|---|---|
| Projeto | COGME |
| Artefato | Test Log |
| Versão | 1.0.0 |
| Base | Execução da suíte pytest + UAT rodada 001 + auditorias extraordinárias |
| Rastreabilidade | RTM em docs/qualidade/10-rtm-qualidade.md; Board de resultados em docs/qualidade/11-board-resultados-qualidade.md |

## 2. Execuções registradas

### Execução E-001 — Suíte pytest (baseline UAT rodada 001)

| Campo | Valor |
|---|---|
| ID da execução | E-001 |
| Data | 13/11/2026 |
| Ambiente | Stack separado (docker compose up --build: db, migrate, back, front, proxy) + CI local |
| Suíte | `tests/unit tests/integration` |
| Comandos | `python -m pytest tests/ -q` |
| Total de casos | 1405 (1392 executados + 13 skip) |
| PASS | 1392 |
| FAIL | 0 |
| Skip | 13 (PDF real sem WeasyPrint nativo; executam no CI com Pango) |
| Taxa de execução | 100% dos não-skippáveis |
| Cobertura sobre src/ | ≥ 80% (plano-qualidade); gate CI 95% |
| Resultado | APROVADO (veredito binário UAT: APROVADA, 15/11/2026 01:39) |
| Evidências | `docs/uat/rodada-001/evidencias/` (14 arquivos) |

### Execução E-002 — Auditorias extraordinárias de CI/CD (falsos positivos)

| Campo | Valor |
|---|---|
| ID da execução | E-002 |
| Data | 31/10/2026 |
| Suítes | `security_scan.py`, `agent_health_check.py --strict`, suíte pytest completa |
| Resultado | 181 testes passam, 1 skipped; Security Scan 46 aprovados/0 falhas; Agent Health Check 45/45 saudáveis; SDDAI Verify 7/7 aprovados |
| Incidentes relacionados | INC-001, INC-002, INC-003 (falsos positivos, resolvidos) |

### Execução E-003 — Funcional/E2E Playwright (nova camada, planejada)

| Campo | Valor |
|---|---|
| ID da execução | E-003 |
| Data | 14/11/2026 (instituição da disciplina) |
| Suíte | `tests/e2e_playwright` (Screenplay Pattern) |
| Casos | CT-FUNC-001 a CT-FUNC-005 |
| Resultado | Pendente execução (camada instituída nesta disciplina; alvo: stack rodando, base URL http://localhost:8001) |

## 3. Detalhe por caso de teste (resumo dos casos CT-UN / CT-INT)

Os casos CT-UN-001 a CT-UN-015 e CT-INT-001 a CT-INT-024 estão implementados em `tests/unit/` e `tests/integration/` com resultado PASS na execução E-001 (ver `docs/qualidade/05-casos-de-teste.md`, coluna Resultado). Nenhuma falha registrada.

## 4. Incidentes registrados no log

| Incidente | ID | Status | Referência |
|---|---|---|---|
| Falso positivo CI/CD — segurança (CUDA/cloud) | INC-001 | Resolvido | AUD-2610-09 |
| Falso positivo CI/CD — health check agentes | INC-002 | Resolvido | AUD-2610-10 |
| Falso positivo CI/CD — credenciais | INC-003 | Resolvido | AUD-2610-11 |
| Testes pulados (13) violam regra zero-skipping do CI | INC-004 | Aberto/Pendente | Board §2 |
| Drift cobertura: plano 80% vs CI 95% | INC-005 | Aberto/Pendente | Board §2 |
| Ausência evidências execução PDCA MF2/MF3 | INC-006 | Aberto/Pendente | Board §2 |
| Drift gráfico FIG-5 = FIG-3; diretório diagrams/ inexistente | INC-007 | Resolvido (forma mermaid, spec-010) | spec-010 §2, AC-07 |

## 5. Assinatura do registro

| Papel | Nome/Função | Data |
|---|---|---|
| Executante dos testes | qa-sdet (agent-qa-sdet, onda 6) | 14/11/2026 |
| Revisor do registro | reviewer (agent-reviewer) | |
| Auditor | auditor (agent-project-auditor) | |
