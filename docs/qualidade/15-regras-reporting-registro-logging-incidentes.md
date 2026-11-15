---
id: docs-qualidade-15-regras-reporting-registro-logging-incidentes
title: Regras de Reporting, Registro e Logging de Incidentes — COGME
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/07-registro-de-teste.md (Test Log)
- docs/qualidade/08-relatorio-incidente-de-teste.md (Test Incident Report)
- docs/qualidade/11-board-resultados-qualidade.md (board)
- constitution.md (P-04 LGPD, P-08 fatos citáveis)
last-revised: '2026-11-15'
lgpd-class: n/a
tags:
- reporting
- registro-de-incidente
- logging
- auditoria
- lgpd
- rastreabilidade
---

# Regras de Reporting, Registro e Logging de Incidentes — COGME

Define como incidentes são reportados, registrados e logados, garantindo rastreabilidade, conformidade LGPD (sem PII) e evidência auditável (P-08, fatos citáveis).

## 1. Canal de reporte

Todos os incidentes são reportados por um único canal: **issue no GitHub Projects/Backlog do COGME** com label `bug-critical`, `bug-major`, `bug-minor` ou `bug-trivial`, conforme prioridade P1-P4.

O issue deve conter:
- Título: `[INC-NNN] <resumo curto>`.
- Corpo: modelo obrigatório (seção 2).
- Link para o board de qualidade (doc 11) e para o relatório de incidente ISTQB (doc 08).

## 2. Modelo obrigatório de registro (campos)

Todo incidente deve conter, no mínimo:

| Campo | Obrigatório? | Descrição |
|---|---|---|
| ID | Sim | `INC-NNN` sequencial |
| Título | Sim | Resumo curto do defeito |
| Data/hora abertura | Sim | ISO 8601 |
| Detetado em | Sim | CI `test-suite` / `playwright-e2e` / exploratório / UAT / produção |
| Escopo de teste | Sim | unit / integração / E2E / exploratório / UAT / hotfix |
| REQ / US / trace id | Sim (quando aplicável) | mapeamento na RTM (doc 10) |
| Caso de teste | Sim (quando aplicável) | CT-UN / CT-INT / CT-FUNC que falhou |
| Severidade (S) | Sim | P1-P4 (doc 14 §1) |
| Impacto (I) | Sim | P1-P4 (doc 14 §1) |
| Prioridade (P) | Sim | máximo(S, I) (doc 14 §1) |
| Status | Sim | NOVO/TRIAGEM/EM RESOLUÇÃO/EM VERIFICAÇÃO/FECHADO/DESCARTADO/REABERTO |
| Responsável | Sim | desenvolvedor ou qa-sdet nomeado na triagem |
| RCA | Sim (P1/P2; recomendado P3/P4) | causa-raiz, classificação 6M se aplicável |
| Ação corretiva | Sim | o que foi feito para corrigir e prevenir recorrência |
| Evidência | Sim | log, screenshot, cobertura, link do CI/run |
| Data fechamento | Não | preenchida ao transitar para FECHADO |

## 3. Logging e rastreabilidade

| Log | Onde | Conteúdo |
|---|---|---|
| Registro de Teste (Test Log) | doc 07 | execuções E-001/E-002/E-003, casos executados, resultado, skip/fail |
| Relatório de Incidente (Test Incident Report) | doc 08 | cada INC-NNN com RCA, prioridade, impacto, severidade, ação corretiva |
| Board de Qualidade | doc 11 | estado atual de todos os incidentes, colunas do Kanban, métricas agregadas |
| CI artifacts | `.github/workflows/ci.yml` | `coverage.xml`, `junit.xml`, `GITHUB_STEP_SUMMARY` por run |
| GitHub Issues | repositório | issue `INC-NNN` com histórico de comentários e alterações de estado |

**Regra de logging:** toda transição de estado do incidente deve ser registrada com data, autor e motivo no issue do GitHub e refletida no board (doc 11). Não há logging paralelo fora desses canais.

## 4. Conformidade LGPD (P-04)

- **Nunca registrar PII** em logs de incidente, issues, CI artifacts ou relatórios: nomes, CPF/CNPJ, endereços, tax IDs de partes reais são proibidos.
- Usar apenas dados sintéticos (`Pessoa Fictícia da Silva`, `INV-0001`, `15/01/2026`, valores de exemplo da spec-004 §2).
- Se um incidente envolver vazamento acidental de PII em log, classificar como P1 e remover o log imediatamente (erase LGPD art. 18 / rotatividade de segredos).

## 5. Reporting (consolidação)

| Relatório | Frequência | Conteúdo | Destinatário |
|---|---|---|---|
| Resumo de execução | por run de CI | casos PASS/FAIL/skip, cobertura, gates | GP + qa-sdet |
| Relatório Resumo de Teste | por marco/UAT | consolidado de execuções, defeitos, risco | GP + auditor |
| Board de Qualidade | contínuo (atualizado a cada transição) | estado de incidentes, métricas, plano de ação | toda a equipe |
| Relatório de Incidente ISTQB | por incidente | RCA detalhado, evidência, ação corretiva | auditor + gatekeeper |

## 6. Exemplo de entrada (INC-004, resumido)

```
ID: INC-004
Título: 13 testes pulados (skip) violam regra zero-skipping do CI
Detetado em: CI test-suite / local
Escopo: integração
REQ: REQ-04, REQ-08
Caso: PDF real sem WeasyPrint nativo (ambientes sem Pango)
S: Média | I: Médio | P: P3
Status: Pendente (aberto)
Responsável: qa-sdet
RCA: expectativa de execução invariante entre ambientes (CI com Pango vs local sem Pango)
Ação corretiva: marcador `weasyprint` + execução separada no CI, ou instalar Pango local
Evidência: docs/qualidade/05-casos-de-teste.md §5; docs/qualidade/11-board-resultados-qualidade.md
```

## 7. Rastreabilidade

| Artefato | Onde registra |
|---|---|
| Abertura de incidente | issue GitHub + doc 11 (coluna NOVO/TRIAGEM) |
| Execução e resultado | doc 07 (Test Log) |
| RCA e ação corretiva | doc 08 (Test Incident Report) + doc 14 §3 |
| Estado corrente | doc 11 (board Kanban) |
| Cobertura/gap de RTM | doc 10 (matriz de rastreabilidade) |
