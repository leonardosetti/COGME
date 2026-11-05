---
id: ai-handoffs-hf-0617-c-1-c-2-em-spec-004-e-c-4-c-5-em-spec-005
title: Emendas C.1+C.2 em spec-004 e C.4+C.5 em spec-005 (lacunas de conteudo)
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0617-c-1-c-2-em-spec-004-e-c-4-c-5-em-spec-005.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---

# HF-0617 — Emendas C.1+C.2 em spec-004 e C.4+C.5 em spec-005 (lacunas de conteudo)

## Tarefa
Fechar as lacunas de conteudo C.1-C.5 da LISTA (item 44-52) EMENDANDO as specs existentes (nunca reescrever decisoes; apenas preencher secoes declaradas `UNKNOWN - verify`):
- spec-004-backend-mvp-v1.spec.md: (C.1) preencher SS11 com criterios de aceite proprios (:228-230); (C.2) preencher SS13 fora de escopo adicional (:243-245). Bump 1.0.0 -> 1.1.0 + entrada CHANGELOG.
- spec-005-container-layers-v1.spec.md: (C.4) resolver nome do job contract-network com o estado REAL auditado na parcela TA-0048 (:210); (C.5) resolver destino das evidencias UAT conforme parcela TA-0047 (:342). Bump 0.2.0 -> 0.3.0 + entrada CHANGELOG (preservando a amenda TA-0030).
- C.3 (handoff/task de criacao das specs 003/004) NAO e emendavel: resolvida por esta rodada — os envelopes task-ta-*.json desta rodada seguem o padrao; registrar em CHANGELOG a nota de resolucao de C.3 por processo (sem editar spec-003/004 frontmatter historico).
INCORPORE as parcelas TA-0047 e TA-0048.

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1, SS2.2 — regras de bump e CHANGELOG)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:48-52 (C.1-C.5)
- .ai/specs/spec-004-backend-mvp-v1.spec.md:228-230, :243-245
- .ai/specs/spec-005-container-layers-v1.spec.md:210, :342
- Parcelas: .ai/handoffs/HF-0603 (qa-sdet), .ai/handoffs/HF-0604 (devops)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0061","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}


## Critérios de Aceite
- [ ] Emendas C.1 e C.2 aplicadas em spec-004 e spec-005 sem reescrever decisões
- [ ] Bump de versão registrado no CHANGELOG de cada spec
- [ ] C.3 resolvida por processo (não editar specs 003/004)
