---
id: ai-handoffs-hf-0610-spec-009-uat-produto-v1
title: Emissao spec-009-uat-produto-v1 (B.5/REQ-09) — insumo TA-0047
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0610-spec-009-uat-produto-v1.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---

# HF-0610 — Emissao spec-009-uat-produto-v1 (B.5/REQ-09) — insumo TA-0047

## Tarefa
Emitir .ai/specs/spec-009-uat-produto-v1.spec.md (plano e roteiro de UAT de produto, fase N6.2 — item B.5 da LISTA): 100% fluxos criticos cobertos, passagem binaria zero defeitos criticos/bloqueantes (REQ-09 spec-002:70; US-009 :165); a proposta spec-005 SS12 (315-344) cobre so camadas de containers. PROPOSTA DE DESTINO das evidencias conforme parcela TA-0047 (fecha C.5 — spec-005:342 UNKNOWN - verify). INCORPORE a parcela TA-0047 (agent-qa-sdet).

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1, SS2.1, SS2.2)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:37 (B.5), :52 (C.5)
- .ai/specs/spec-005-container-layers-v1.spec.md:315-344, :342
- Parcela de consulta: .ai/handoffs/HF-0603

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0054","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}


## Critérios de Aceite
- [ ] Spec emitida conforme template MANIFEST SS1 (camadas a-h)
- [ ] Todas as fontes obrigatórias citadas com arquivo:linha
- [ ] Insumo da parcela TA-0047 incorporado por referência
