---
id: CI-CD-GOV-001
title: Política de Governança CI/CD — COGME
version: 1.0.0
class: relatorio-governanca
status: ratificado
owner: agent-project-analyst
derived-from:
- docs/governanca/ci-cd-governance.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a (sem PII)
tags:
- governanca
- docs
- normalizado
---

# Política de Governança CI/CD — COGME

## 1. Propósito

Estabelecer as regras de governança, validação, ratificação e promulgação dos pipelines de integração contínua e entrega contínua (CI/CD) do projeto COGME, assegurando que todo pipeline:

- Rode **fail-closed** (qualquer falha interrompe o pipeline, sem bypass)
- Seja **100% FOSS** e **CPU-only** (P-01, P-02)
- Seja **LGPD-safe** (sem PII em artefatos técnicos, P-04)
- Esteja alinhado aos **primeiros princípios** (Art. P-12) e **YAGNI** (P-11)
- Respeite o **Kill Switch herdado** (Art. 4.6)
- Não utilize provedores de nuvem para inferência ou dados sensíveis (P-03)

## 2. Escopo

Aplica-se a todos os workflows de CI/CD no repositório:

| Workflow | Caminho | Propósito |
|----------|---------|-----------|
| COGME CI/CD Pipeline | `.github/workflows/ci.yml` | Validação geral: Kill Switch, FOSS, SDD/DAG, saúde de agentes, testes |
| SDDAI Verify Pipeline | `.github/workflows/sddai-verify.yml` | Verificação específica do ecossistema SDDAI (7 passos) |

## 3. Princípios Orientadores

### 3.1. First-Principles (P-12)

Cada etapa de cada pipeline deve derivar de um fundamento verificável:

| Etapa | Fundamento | Artigo/Princípio |
|-------|-----------|------------------|
| Kill Switch check | Veto constitucional absoluto | Art. 4.6 |
| FOSS compliance | Stack FOSS, custo zero recorrente | P-01 |
| No cloud inference | Soberania computacional local | P-02 |
| No real credentials | Segurança, Zero Trust | P-07, Art. 7.2 |
| SDD/DAG validation | Topologia canônica de agentes | Art. 4.5, 6.1 |
| Agent health | Roster SSOT, contratos válidos | Art. 4.4, 4.5 |
| Test suite | Qualidade fechada, cobertura ≥ 80% | P-06 |
| Final status | Traces documentados | P-05 |

### 3.2. YAGNI (P-11)

Nenhuma etapa é adiciona sem demanda do ciclo atual. Os workflows contêm apenas o mínimo necessário para:
- Validar a Constituição
- Validar o roster de agentes
- Validar a topologia DAG
- Validar a qualidade do código (testes)
- Verificar o pipeline SDDAI

Não há etapas de build, deploy, container registry ou notificação externas — estão fora do escopo atual.

### 3.3. DevOps / DevSecOps Fundamentos

| Princípio | Aplicação no COGME |
|-----------|-------------------|
| Shift-left security | Kill Switch, FOSS e credential checks executam primeiro |
| Fail-closed | Qualquer falha interrompe o pipeline (exit 1) |
| Immutability | Workflows versionados, sem alteração retroativa de marcos |
| Traceability | Ledger atualizado a cada execução bem-sucedida |
| Local-first | 100% CPU-local, zero rede para inferência |
| Observability | Relatório JSON estruturado em cada pipeline |

## 4. Regras de Fail-Closed

| Condição | Ação | Fonte |
|----------|------|-------|
| `kill_switch.trigger` existe | Pipeline bloqueado, exit 1 | Art. 4.6 |
| Agente rejeitado (rejeitados > 0) | Pipeline bloqueado | Art. 4.7 |
| DAG com ciclos ou erros | Pipeline bloqueado | Art. 4.5 |
| Agente não-saudável (falha real) | Pipeline bloqueado | Art. 4.5 |
| Test suite vermelho | Pipeline bloqueado | P-06 |
| Referência a CUDA/cloud inference | Pipeline bloqueado | P-02 |
| Credencial real versionada | Pipeline bloqueado | P-07, Art. 7.2 |

## 5. Bypass Protocol

Nenhum bypass é permitido nos pipelines CI/CD. O Bypass Protocol (3 pilares: força maior, rota de fuga FOSS, ratificação CCB) **não se aplica** a pipelines de CI/CD, pois estes são mecanismos de proteção constitucional, não funcionalidades de negócio.

## 6. Ledger e Traces

Cada execução bem-sucedida do pipeline CI/CD deve registrar no `.ai/agents/ledger.yaml`:

- Versão do pipeline
- Hash do commit Git
- Data/hora (UTC)
- Status (passed/failed)
- Papel do ratificador (GP/CCB)

## 7. Ratificação e Promulgação

Esta política é promulgada como parte da rodada de governança de 31/10/2026, sob autoridade do GP Leonardo (CCB de membro único), conforme Constitution Art. 5.1 e 5.2.

## 8. Revisão

Revisão obrigatória a cada milestone (M1-M4) ou quando houver alteração na Constituição, ADRs de governança de agentes ou roster SSOT.

---

**Assinatura de Governança:**

| Campo | Valor |
|-------|-------|
| Decisor | GP Leonardo — CCB de membro único (TAP v3 §1.c, Premissa P7) |
| Data | 31/10/2026 |
| Instrumento | Prompt expresso do CCB + este documento |
| Status | VIGENTE |
