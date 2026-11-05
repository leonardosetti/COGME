---
id: ai-handoffs-hf-0612-spec-011-cicd-pipeline-v1
title: Emissao spec-011-cicd-pipeline-v1 (B.7/REQ-11) — insumo TA-0048
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0612-spec-011-cicd-pipeline-v1.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---

# HF-0612 — Emissao spec-011-cicd-pipeline-v1 (B.7/REQ-11) — insumo TA-0048

## Tarefa
Emitir .ai/specs/spec-011-cicd-pipeline-v1.spec.md (pipeline CI/CD — item B.7 da LISTA): lint+testes <=5 min por push, falha bloqueando merge (REQ-11 spec-002:72; US-011 :167); delta sobre spec-005 SS8 (198-210, fase unica); auditoria do drift G-05 (plano:33 x ledger:24) com estado REAL do ci.yml registrado; nome exato do job contract-network (fecha C.4, spec-005:210). INCORPORE a parcela TA-0048 (agent-devops).

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1, SS2.1, SS2.2)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:39 (B.7), :51 (C.4), :59 (D.2)
- .ai/specs/spec-005-container-layers-v1.spec.md:198-210, :352
- .ai/agents/ledger.yaml:24 (drift G-05 — historico, nao editar)
- Parcela de consulta: .ai/handoffs/HF-0604

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0056","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}


## Critérios de Aceite
- [ ] Spec emitida conforme template MANIFEST SS1 (camadas a-h)
- [ ] Todas as fontes obrigatórias citadas com arquivo:linha
- [ ] Insumo da parcela TA-0048 incorporado por referência
