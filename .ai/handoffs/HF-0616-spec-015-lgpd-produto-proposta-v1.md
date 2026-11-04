---
id: HF-0616
title: "Emissao spec-015-lgpd-produto-proposta-v1 (B.3/GAP-08) — PROPOSTA draft condicionada a CCB"
task: TA-0060
sender: agent-nexus-prime-ultimate
target: agent-sdd-specialist
action: spec
created: 2026-11-03
kill_switch: inherited
status: emitted
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0616 — Emissao spec-015-lgpd-produto-proposta-v1 (B.3/GAP-08) — PROPOSTA draft condicionada a CCB

## Tarefa
Emitir .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (item B.3 da LISTA) como **PROPOSTA (status: draft)** sujeita a ratificacao CCB/PO: criterios LGPD de produto — minimizacao e tratamento de dados pessoais/financeiros na invoice e nos logs (GAP-08, spec-002:107) sob P-04 (constitution.md:36). A LISTA condiciona a emissao a decisao previa de CCB/PO — portanto: status NUNCA aprovado; incluir secao "Condicionantes de ratificacao" listando as decisoes CCB pendentes (fundamentos da parcela TA-0050). INCORPORE a parcela TA-0050 (agent-compliance-governance).

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1, SS2.1, SS2.2)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:35 (B.3), :67 (E.1)
- constitution.md:36 (P-04), Art. 3, Art. 5.1
- Parcela de consulta: .ai/handoffs/HF-0606

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0060","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}
