---
id: HF-0618
title: "Auditoria de integridade da rodada de specs (fechamento)"
task: TA-0062
sender: agent-nexus-prime-ultimate
target: agent-project-auditor
action: audit
created: 2026-11-03
kill_switch: inherited
status: emitted
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0618 — Auditoria de integridade da rodada de specs (fechamento)

## Tarefa (executar APENAS apos conclusao de TA-0051..TA-0064)
Auditar a rodada: (1) existencia e nao-vaziedade de spec-006..spec-015 em .ai/specs/; (2) conformidade de template (frontmatter SS1.1, H1, secoes, MAPA TA-0031) por arquivo; (3) nomenclatura spec-NNN-specname.spec.md; (4) uso correto de `UNKNOWN - verify` (sem invencao P-08); (5) emendas spec-004 1.1.0 e spec-005 0.3.0 com CHANGELOG e decisoes preservadas; (6) tap.md/eap.md nao vazios com rastreabilidade; (7) pytest tests/agents/ = baseline 4F/149P/1S sem NOVAS falhas; (8) sync_agent_registry.py --check exit 0; (9) nenhum imutavel (constitution, ADRs, ledger pre-existente, .opencode) alterado (git status); (10) handoffs HF-0601..0620 e task JSONs presentes. Emitir relatorio de auditoria em docs/auditorias/ e parcela final com dod por item.

## Fontes
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (itens A-C)
- .ai/specs/MANIFEST.md (criterios de aceite SS6)
- .ai/handoffs/HF-0618 (este handoff)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0062","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}
