---
id: HF-0609
title: "Emissao spec-008-frontend-web-responsive-v1 (B.1/REQ-06) — insumo TA-0046"
task: TA-0053
sender: agent-nexus-prime-ultimate
target: agent-sdd-specialist
action: spec
created: 2026-11-03
kill_switch: inherited
status: emitted
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0609 — Emissao spec-008-frontend-web-responsive-v1 (B.1/REQ-06) — insumo TA-0046

## Tarefa
Emitir .ai/specs/spec-008-frontend-web-responsive-v1.spec.md (interface web responsiva 100% FOSS do MVP — item B.1 da LISTA): REQ-06 browsers ultimas 2 versoes, templates, UX, integracao browser; camada `front` da spec-005; estado vazio atual (index.html 0 B, static/ vazio, spec-005:30); escopo derivado da onda 4 (A.11 ui-ux-advisor -> A.12 frontend-dev, plano-producao-agentes.md:129-131). INCORPORE a parcela TA-0046 (agent-ui-ux-advisor).

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1, SS2.1, SS2.2)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:33 (B.1), :58 (D.1)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md:67 (REQ-06)
- .ai/specs/spec-005-container-layers-v1.spec.md:30 (front vazia), camada front
- Parcela de consulta: .ai/handoffs/HF-0602

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0053","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}
