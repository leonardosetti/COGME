---
id: docs-qualidade-12-workflow-qa-otimizado
title: Workflow de QA Otimizado — COGME
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/00-contexto-disciplina-qualidade.md
- docs/qualidade/02-shift-left.md
- docs/qualidade/03-plano-testes-istqb.md
- .github/workflows/ci.yml (gates existentes)
- .ai/specs/spec-011-cicd-pipeline-v1.spec.md (REQ-11)
last-revised: '2026-11-15'
lgpd-class: n/a
tags:
- workflow-qa
- processo-de-qualidade
- ci-cd
- e2e
- exploratorio
- hotfix
---

# Workflow de QA Otimizado — COGME

Workflow de ponta a ponta: **Shift-Left no commit → gates no CI → merge controlado → UAT por marco → incidentes/hotfix → fechamento**. Cobre E2E (Playwright Screenplay), testes exploratórios e hotfixes.

## 1. Visão geral do fluxo (estágios)

```
Desenvolvimento (local)
      │
      ▼
 Pré-commit (lint + pytest unit+integration + coverage)
      │
      ▼
 Pull Request (CI paralelo: gates + playwright-e2e + code review)
      │
      ▼
 Gatekeeper aprova merge (regra de ouro: CI verde + coverage ≥95% + review + tasklist)
      │
      ▼
 main / stage — CI completo + deploy homologação (stack efêmero)
      │
      ├─ UAT rodada (por marco) ──► aprovada → próximo marco
      │                                   │
      │                                   ▼
      │                          Exploratórios (ad-hoc, pós-UAT)
      │                                   │
      └─ Defeito encontrado ─────────────► Ciclo de Incidentes (doc 13)
                                            │
                                            ├─ P1/P2 → Hotfix (doc 14/15)
                                            └─ P3/P4 → Backlog de qualidade
```

## 2. Estágio A — Desenvolvimento local (Shift-Left)

Responsável: desenvolvedor. Antes de abrir o PR:

| Ação | Ferramenta | Comando | Bloqueia commit? |
|---|---|---|---|
| Análise estática | flake8, mypy, validação frontmatter/nomes | `flake8 src migrations tests` | Sim (CI lint) |
| Testes unit + integração | pytest | `pytest tests/unit tests/integration -q` | Sim |
| Cobertura local | coverage.py | `--cov=src --cov-fail-under=80` | Recomendado |
| Revisão própria | diff + RTM | conferir REQ → caso de teste | Sim (DoR/DoD) |

Regra: todo PR novo traz teste para o código que adiciona/altera (Shift-Left).

## 3. Estágio B — Pull Request (CI paralelo)

Responsável: CI + reviewer + gatekeeper. Jobs executam em paralelo:

- `foss-compliance`, `sdd-validation`, `agent-health` (segurança e governança SDD)
- `lint` (flake8, mypy, frontmatter, nomes de arquivo)
- `test-suite` (pytest unit + integration, coverage ≥95%, zero skips)
- `build-layers` (imagens Docker por digest)
- `contract-network` (stack efêmero, saúde do back)
- `playwright-e2e` (CT-FUNC-*, stack efêmero, Chromium headless)

Critério de aprovação do PR: todos os jobs verdes, cobertura ≥95%, zero testes pulados, code review aprovado, tasklist 100% (ADR-004).

## 4. Estágio C — Merge e homologação

Responsável: gatekeeper. O merge só ocorre com CI verde. O stack de homologação é efêmero (docker compose), sem porta publicada no host, acesso apenas pela rede interna do compose.

## 5. Estágio D — UAT por marco

Responsável: qa-sdet + GP. Executada em rodadas (ex.: rodada 001, 14/14 PASS, aprovada 15/11/2026). Critério binário: 100% fluxos críticos PASS e zero defeitos críticos/bloqueantes abertos. Qualquer falha = rodada REPROVADA e abre incidente.

## 6. Estágio E — Testes exploratórios (escopo específico)

Quando executar: após cada rodada de UAT e antes de fechar o marco. Objetivo: encontrar defeitos que os testes roteirizados (E2E/unit/integração) não cobrem.

| Item | Regras |
|---|---|
| Alvo | Fluxos críticos pela UI (simulação, emissão de invoice PDF), navegação entre telas, comportamento com dados inválidos no formulário |
| Técnica | Teste exploratório direcionado (charter de 45-60 min, sessão única, sem roteiro fixo) |
| Registro | Todo defeito encontrado vira incidente no ciclo (doc 13) com ID INC-NNN |
| Rastreabilidade | Mapear o defeito ao REQ/US na RTM (doc 10) |
| Saída | Relatório exploratório anexado ao board de qualidade (doc 11) |

## 7. Estágio F — Hotfixes (escopo específico)

Quando executar: defeito P1 (crítico) ou P2 (alto) detectado em homologação/produção ou que bloqueie o merge/release.

| Item | Regras |
|---|---|
| Gatilho | Defeito bloqueante (veredito UAT reprovado, CI travado, regressão crítica) |
| Fluxo | branch `hotfix/inc-NNN` a partir de `main`, correção mínima, CI completo obrigatório (não bypassar), code review + gatekeeper, merge direto com mensagem de hotfix |
| Pós-mortem | RCA registrado no relatório de incidente (doc 08) e ação corretiva no board (doc 11) |
| Exceção | Hotfix P1 pode pular a rodada de UAT completa, mas deve validar o fluxo afetado por E2E + regressão dos testes afetados |

## 8. Cadência e responsáveis (RACI)

| Atividade | GP | qa-sdet | reviewer | gatekeeper | auditor |
|---|---|---|---|---|---|
| Pré-commit local | I | C | R | I | I |
| CI gates (PR) | I | R | C | C | I |
| Code review | C | C | R | A | I |
| UAT rodada | A | R | C | C | I |
| Exploratórios | C | R | I | I | C |
| Hotfix | A | C | R | R | C |
| Encerramento incidente | C | R | C | C | R/A |

## 9. Rastreabilidade

| Fonte | Onde |
|---|---|
| plano-qualidade.md (regra de ouro, gatilhos) | §2, §3, §7 |
| spec-011 (REQ-11, CI ≤ 5 min) | §3 |
| spec-010 (REQ-10, N6.3, RACI onda 6) | §8 |
| Constitution (gates de qualidade, P-06) | §3 |
