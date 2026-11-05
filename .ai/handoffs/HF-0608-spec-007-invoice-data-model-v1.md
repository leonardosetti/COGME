---
id: HF-0608
title: "Emissao spec-007-invoice-data-model-v1 (B.4/GAP-04) — insumo TA-0045"
task: TA-0052
sender: agent-nexus-prime-ultimate
agent: agent-sdd-specialist
action: spec
created: 2026-11-03
kill_switch: inherited
status: dispatched
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0608 — Emissao spec-007-invoice-data-model-v1 (B.4/GAP-04) — insumo TA-0045

## Tarefa
Emitir .ai/specs/spec-007-invoice-data-model-v1.spec.md (modelo canonico de dados da invoice — item B.4 da LISTA): campos bancarios, CPF/CNPJ, periodo; complementa spec-004 (que cobre so o contrato POST /v1/invoice); alimenta US-004 (spec-002:161, "modelo de dados pendente — GAP-04"). INCORPORE as recomendacoes da parcela de consulta TA-0045 (agent-dba) reproduzida no payload.

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1, SS2.1, SS2.2)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:36 (B.4)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md:103,161
- .ai/specs/spec-004-backend-mvp-v1.spec.md (contrato POST /v1/invoice)
- Parcela de consulta: .ai/handoffs/HF-0601 (consulta agent-dba)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0052","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}


## Critérios de Aceite
- [ ] Spec emitida conforme template MANIFEST SS1 (camadas a-h)
- [ ] Todas as fontes obrigatórias citadas com arquivo:linha
- [ ] Insumo da parcela TA-0045 incorporado por referência
