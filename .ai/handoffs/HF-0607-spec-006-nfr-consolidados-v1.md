---
id: ai-handoffs-hf-0607-spec-006-nfr-consolidados-v1
title: Emissao spec-006-nfr-consolidados-v1 (B.2/GAP-02)
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0607-spec-006-nfr-consolidados-v1.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---

# HF-0607 — Emissao spec-006-nfr-consolidados-v1 (B.2/GAP-02)

## Tarefa
Emitir .ai/specs/spec-006-nfr-consolidados-v1.spec.md (registro canonico de NFR — item B.2 da LISTA): cobrir a fase N2.2 "Requisitos Nao Funcionais" prevista na EAP (PDF:645) sem artefato (GAP-02, spec-002:101) e mapear P-06/P-07/P-04 a criterios de produto. Fonte unica de verificacao nao funcional.

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1, SS2.1, SS2.2)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:34 (B.2, com citacoes)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md:101 (GAP-02), tabela A.1 REQ/P
- docs/planos/plano-integral-tap-1-2-3-4-5.md (fase N2.2, PDF:645)
- constitution.md:36 (P-04), P-06, P-07

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0051","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}


## Critérios de Aceite
- [ ] Spec emitida conforme template MANIFEST SS1 (camadas a-h)
- [ ] Todas as fontes obrigatórias citadas com arquivo:linha
- [ ] Zero decisões novas promovidas — apenas especificação de NFR existentes
