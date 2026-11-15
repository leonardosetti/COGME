---
id: docs-qualidade-13-ciclo-incidentes-bugs
title: Ciclo de Incidentes e Gerenciamento de Bugs — COGME
type: procedimento
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/08-relatorio-incidente-de-teste.md
- docs/qualidade/11-board-resultados-qualidade.md
- docs/qualidade/14-regras-resolucao-incidentes.md
- docs/qualidade/15-regras-reporting-registro-logging-incidentes.md
last-revised: '2026-11-15'
lgpd-class: n/a
tags:
- ciclo-de-incidentes
- gerenciamento-de-bugs
- incidente
- defeito
- rca
- rastreabilidade
---

# Ciclo de Incidentes e Gerenciamento de Bugs — COGME

Define o ciclo de vida de um defeito/incidente desde a detecção até o encerramento. Aplica a testes unitários, integração, E2E (Playwright), exploratórios, UAT e homologação/produção.

## 1. Estados do ciclo (board de qualidade)

```
  NOVO ──► TRIAGEM ──► EM RESOLUÇÃO ──► EM VERIFICAÇÃO ──► FECHADO
    │            │              │               │              ▲
    │            │              │               │              │
    ▼            ▼              ▼               ▼              │
  DESCARTADO ◄───┴─────────────┴─── REABERTO ──────────────────┘
        (não é defeito)           (reapareceu ou não resolvido)
```

| Estado | Significado | Quem move | Critério de transição |
|---|---|---|---|
| NOVO | Incidente aberto, sem análise | qa-sdet / qualquer membro | ID INC-NNN criado, campos obrigatórios preenchidos |
| TRIAGEM | Severidade/prioridade definidas, dono atribuído | GP + qa-sdet | P1-P4 atribuído, responsável nomeado |
| EM RESOLUÇÃO | Correção em desenvolvimento | desenvolvedor | branch aberta, commit em andamento |
| EM VERIFICAÇÃO | Correção validada (reprodução + regressão) | qa-sdet | testes afetados PASS, CI verde |
| FECHADO | Incidente resolvido e evidenciado | auditor | RCA registrado, ação corretiva no board |
| DESCARTADO | Não é defeito (regras de negócio/uso esperado) | GP | justificativa documentada |
| REABERTO | Defeito reapareceu após fechamento | qa-sdet | regressão confirmada, volta a EM RESOLUÇÃO |

## 2. Entrada no ciclo (detecção)

Um incidente entra no ciclo quando detectado em:

- **Testes automatizados** (unit/integração): falha no CI `test-suite` ou local.
- **E2E Playwright**: falha no job `playwright-e2e` (CT-FUNC-*).
- **Exploratórios**: defeito encontrado em sessão de teste ad-hoc.
- **UAT**: falha em fluxo crítico (veredito REPROVADO).
- **Homologação/produção**: regressão ou defeito em ambiente real.

Cada incidente recebe ID `INC-NNN` sequencial e é registrado no board (doc 11) e no relatório de incidente ISTQB (doc 08).

## 3. Saída do ciclo (encerramento)

O incidente só fecha quando:

1. Correção aplicada e mergeada (ou descartado com justificativa).
2. Testes afetados executados com PASS (incluindo regressão da suíte relacionada).
3. CI verde no PR da correção.
4. RCA preenchido (causa-raiz, ação corretiva, 6M se aplicável — spec-010 §3.2).
5. RTM atualizada se o defeito revelou gap de cobertura (doc 10).

Se reaparecer após fechamento, volta a `REABERTO` e reentra em `EM RESOLUÇÃO`.

## 4. Exemplo de percorrimento (INC-004 — testes pulados)

NOVO (detecção no CI/test-suite) → TRIAGEM (P3, médio, dono qa-sdet) → EM RESOLUÇÃO (marcador `weasyprint` ou instalar Pango) → EM VERIFICAÇÃO (suíte passa sem skips) → FECHADO (RCA: expectativa de execução invariante entre ambientes).

## 5. Ligação com outros documentos

| Documento | Relação |
|---|---|
| doc 11 — board | Estado atual de cada incidente, prioridade/impacto/severidade |
| doc 14 — regras de resolução | SLA, escala P/I/S, regras E2E/exploratórios/hotfix |
| doc 15 — reporting/registro/logging | Campos obrigatórios, template, log de auditoria |
| doc 08 — relatório de incidente ISTQB | Detalhe do RCA e evidência |
