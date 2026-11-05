---
id: HF-0613
title: "Emissao spec-012-rastreabilidade-prompts-sdd-v1 (B.8/REQ-13)"
task: TA-0057
sender: agent-nexus-prime-ultimate
agent: agent-sdd-specialist
action: spec
created: 2026-11-03
kill_switch: inherited
status: dispatched
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0613 — Emissao spec-012-rastreabilidade-prompts-sdd-v1 (B.8/REQ-13)

## Tarefa
Emitir .ai/specs/spec-012-rastreabilidade-prompts-sdd-v1.spec.md (rastreabilidade de prompts SDD — item B.8 da LISTA): 100% dos prompts catalogados em .ai/handoffs/ (REQ-13, fase N9.3, spec-002:74) para auditoria de co-autoria. Definir criterio de cobertura total (o que constitui "prompt catalogado"), formato do catalogo (INDEX.md existente), verificacao por grep/auditoria, e lacunas `UNKNOWN - verify`.

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1, SS2.1, SS2.2)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:40 (B.8), :61 (D.4 onda 7)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md:74 (REQ-13)
- .ai/handoffs/INDEX.md (catalogo vivo)
- .ai/handoffs/HF-0500-backend-mvp.md (precedente REQ-13)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0057","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}


## Critérios de Aceite
- [ ] Spec emitida conforme template MANIFEST SS1 (camadas a-h)
- [ ] Todas as fontes obrigatórias citadas com arquivo:linha
- [ ] Critério de cobertura 100% definido (C-01 a C-04)
