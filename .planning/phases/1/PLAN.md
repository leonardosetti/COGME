---
id: cogme-plan-1
title: COGME — PLAN Fase 1
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .planning/phases/1/PLAN.md
last-revised: '2026-11-22'
lgpd-class: n/a
tags:
- planejamento
- fase-1
- planejamento
---

# PLAN — Fase 1: Saneamento de compliance (P0–P3)

## Fase
Número: 1 | Slug: `saneamento-compliance` | Status: planejado

## Goal
Deixar a Auditoria de Compliance verde no CI (fechar VIO-030/031/032) e sanar incidentes críticos de integridade dos agentes/ledger/registry (VIO-019, VIO-020..029), exceto VIO-026 que exige decisão Humana/CCB (Art. 5.1) — fica de fora desta fase.

## Contexto (do discuss-phase)
- Repositório COGME, branch `main`, release v1.0.0 (commit 26819ab). Working tree sujo: 43 arquivos modificados (implementação CR-002, specs 017–022) + não-rastreados (specs 024–026, migrations 0009–0016, `src/backend/utils/`, templates auth reset/verify_email).
- Sem ROADMAP.md; esta é a primeira fase planejada.
- 4 workflows ativos no GitHub (leonardosetti/COGME): `Auditoria de Compliance` (schedule 90min, falha desde 16/11), `COGME CI/CD Pipeline` (push, falha em 16/11), `cr-spec-approval` (push, falha em 16/11), `SDDAI Verify Pipeline` (push, sucesso consistente).
- Causa raiz confirmada no log do job 136346714553: passo 7 de `sddai_verify_pipeline.py` roda `python3 -m pytest`, mas o workflow `auditoria-compliance.yml` instala apenas `requirements.txt`, que não tinha pytest → `No module named pytest` → rc=1 → fail-closed.
- Fix já commitado localmente (a1e7196): `pytest>=9.2,<10` adicionado a `requirements.txt`. Push bloqueado por hook de pré-push (cobertura 66,50% < 80% e `COGME_TEST_DATABASE_URL` não definido).
- VIO-register aberto: VIO-019 (AFA < 85 SDDAI), VIO-020/021/022 (contratos sem dod:true), VIO-024 (45/45 frontmatter incompleto), VIO-026 (auto-delegação TA-0028, decisão Humana/CCB), VIO-027 (ledger fora do contrato), VIO-028 (drift registry↔DAG), VIO-029 (3 gates L3 sem downstream), VIO-030/031/032 (scheduler auditoria).
- Auditorias CR-009 pré-produção (VIO-033/034, 17 BLOQ) são bloqueadores de release, não desta fase.

## Escopo (P0–P3)

### P0 — Desbloquear CI / auditoria compliance (fecha VIO-030/031/032; apoia TA-0068/HF-0500)
| ID | Task | Dependências |
|---|---|---|
| T1 | Confirmar `requirements.txt` com `pytest>=9.2,<10` (commit a1e7196 já feito, pendente push) | — |
| T2 | Normalizar handoff TA-0068/HF-0500: agent `nexus-prime-ultimate` → `agent-devops`; status `blocked` → `ready`; scheduler 90min 24/7; canais GitHub Actions cron + timer systemd/cron local; orquestrar `security_scan.py`, `registry_drift_monitor.py --check`, `sync_agent_registry.py --check`, `nexus_dispatcher.py --report`, `sddai_verify_pipeline.py --strict`; relatório em `docs/auditorias/` + `vio-register.md`; fail-closed exit 1; sem PII; CPU-only; FOSS-only; Critérios de Aceite checkáveis; `kill_switch: inherited` | T1 |

### P1 — Integridade dos agentes SDDAI (fecha VIO-024; apoia TA-0061/0062/0063/0064/0065)
| ID | Task | Dependências |
|---|---|---|
| T3 | Preencher frontmatter em 45/45 agentes (chaves `name`, `layer`, `role`, `description`, Art. 4.3) | — |
| T4 | Repopular `tap.md`, `eap.md`, `requisitos.md` (TA-0063/0064/0065) | — |
| T5 | Auditoria de integridade das specs 017–022 (TA-0062) e emendas spec-004/005 (TA-0061) | T4 |

### P2 — Conformidade de contratos e ledger (fecha VIO-020/021/022, VIO-027, VIO-028, VIO-029)
| ID | Task | Dependências |
|---|---|---|
| T6 | Contratos half-duplex L2/L3: adicionar `dod:true` (VIO-020/021/022) | — |
| T7 | Ledger Art. 4.10: restringir ações a `VALID_ACTIONS`; prefixo `agent-` no `sender`; schema completo (`version`, `current_session`, `audit_trail`, `last_updated`); parar `safe_dump` de reescrever arquivo (VIO-027) | — |
| T8 | Drift registry↔DAG: remover `agent-factory-architect-ultimate` do registry ou adicionar ao `AGENT_TOPOLOGY` com camada definida (VIO-028) | T3 |
| T9 | 3 gates L3 com `downstream: []`: preencher `downstream` em `agent-reviewer`, `agent-gatekeeper`, `agent-clean-code-evaluator` (VIO-029) | T3 |

### P3 — AFA dos 5 agentes SDDAI (fecha VIO-019)
| ID | Task | Dependências |
|---|---|---|
| T10 | Re-forjar 5 agentes SDDAI com 16 seções canônicas (ADR-014 §3.2); score AFA ≥ 85/100 via `validate_afa_output.py` | T3 |

## Fora de escopo (explicitamente excluídos)
- VIO-026 (auto-delegação TA-0028, sender==receiver `nexus-prime-ultimate`): requer decisão Humana/CCB Art. 5.1 — não fecha nesta fase.
- VIO-033 + VIO-034 (CR-009 pré-produção, 17 BLOQ + 12 ALTO + ...): bloqueadores de release, fase separada (pré-produção CR-009).
- Working tree sujo da CR-002 (43 arquivos, specs 017–022, migrations 0001–0008, frontend ifit.com): não entra; fase 1 é saneamento de compliance.
- Specs 024–026, migrations 0009–0016, `src/backend/utils/`, templates auth `reset.html`/`verify_email.html` (não-rastreados): fora.

## Critérios de aceite (checkáveis)

**P0:**
- [ ] Pipeline `Auditoria de Compliance` verde no `main` (passos 1–7 de `auditoria_compliance.py` passam no CI).
- [ ] `pytest` instalável via `requirements.txt` no runner do CI (Python 3.12).
- [ ] Handoff TA-0068/HF-0500: status `ready`, agent `agent-devops`, scheduler 90min 24/7 documentado.

**P1:**
- [ ] 45/45 agentes com frontmatter completo (`name`, `layer`, `role`, `description`).
- [ ] `tap.md`, `eap.md`, `requisitos.md` repovoados com conteúdo não-vazio e rastreabilidade arquivo:linha.
- [ ] Specs 017–022 integridade OK; spec-004/005 emendadas (bump + CHANGELOG).

**P2:**
- [ ] `dod:true` presente nos contratos half-duplex L2/L3.
- [ ] Ledger aceita apenas ações de `VALID_ACTIONS`; `sender` com prefixo `agent-`; schema completo; gravação append-only (sem `safe_dump` reescrevendo).
- [ ] `registry` == `AGENT_TOPOLOGY`; nenhuma camada `UNKNOWN` em `nexus_dispatcher.py --report`.
- [ ] 3 gates L3 com `downstream` preenchido (`agent-reviewer`, `agent-gatekeeper`, `agent-clean-code-evaluator`).

**P3:**
- [ ] 5 agentes SDDAI com 16 seções canônicas (ADR-014 §3.2).
- [ ] `validate_afa_output.py` score ≥ 85/100.

## Riscos
- Working tree sujo: commitar `requirements.txt` pode entrar em conflito com mudanças não commitadas. Verificar `git status` antes de commitar.
- VIO-026 bloqueado por decisão Humana/CCB; não forçar fechamento.
- CR-009 bloqueadores (PII, Argon2id inativo, CSRF, exclusão de conta, etc.) não entram na fase 1; se o CI for exigido para validá-los, adiar CR-009 para após P0.
- Mudanças em `ledger.yaml`/`registry.yaml` podem quebrar agentes existentes; testar `sync_agent_registry.py --check` e `nexus_dispatcher.py --report` antes de fecar VIO-027/028.

## Próximo comando
`/gsd-execute-phase` (fase 1) após revisão deste PLAN.md.
