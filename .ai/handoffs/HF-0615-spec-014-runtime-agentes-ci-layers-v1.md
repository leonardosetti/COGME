---
id: ai-handoffs-hf-0615-spec-014-runtime-agentes-ci-layers-v1
title: Emissao spec-014-runtime-agentes-ci-layers-v1 (B.10) — escopo CONFIRMADO pelo orquestrador
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0615-spec-014-runtime-agentes-ci-layers-v1.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---

# HF-0615 — Emissao spec-014-runtime-agentes-ci-layers-v1 (B.10) — escopo CONFIRMADO pelo orquestrador

## Tarefa
Emitir .ai/specs/spec-014-runtime-agentes-ci-layers-v1.spec.md (item B.10 da LISTA). **CONFIRMACAO DO ORQUESTRADOR (nexus-prime-ultimate, 2026-11-03): escopo CONFIRMADO.** Fundamento: spec-005:81 declara `UNKNOWN - verify` quanto a spec propria das camadas L1/L3 (runtime de agentes SDD, Art. 6.5) e camada de CI (GitHub Actions Free Tier sob Bypass registrado, P-01); follow-up em spec-005:352. Nenhuma spec propria existe (verificado por auditoria TA-0031). Cobrir: definicao dessas camadas segundo Art. 10.1, limites com spec-005, e o regime de Bypass registrado para CI free-tier. INCORPORE a parcela TA-0048 (agent-devops, camada CI).

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1, SS2.1, SS2.2)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:42 (B.10)
- .ai/specs/spec-005-container-layers-v1.spec.md:81 (UNKNOWN - verify), :352 (follow-up)
- constitution.md Art. 6.5, Art. 10.1, P-01, SS0.2 BYPASS_PROTOCOL
- Parcela de consulta: .ai/handoffs/HF-0604

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0059","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}


## Critérios de Aceite
- [ ] Spec emitida conforme template MANIFEST SS1 (camadas a-h)
- [ ] Todas as fontes obrigatórias citadas com arquivo:linha
- [ ] Confirmação do orquestrador incorporada no frontmatter
