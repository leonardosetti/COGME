---
id: HF-0603
title: "Consulta de dominio: UAT de produto e destino de evidencias (B.5/C.5)"
task: TA-0047
sender: agent-nexus-prime-ultimate
agent: agent-qa-sdet
action: consult
created: 2026-11-03
kill_switch: inherited
status: dispatched
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0603 — Consulta de dominio: UAT de produto e destino de evidencias (B.5/C.5)

## Tarefa (meio-duplex — sem escrita de arquivos)
1. Leia seu contrato: .opencode/agents/agent-qa-sdet.md
2. Leia as fontes citadas abaixo.
3. Produza PARCELA DE CONSULTA (JSON) com recomendacoes para a futura spec-009 (plano e roteiro de UAT de produto, fase N6.2): criterio REQ-09 (100% fluxos criticos, zero defeitos criticos/bloqueantes, passagem binaria), roteiro por US (US-009), proposta de DESTINO das evidencias (fecha C.5: spec-005:342 `UNKNOWN - verify`) — onde armazenar, nomenclatura, retencacao — e o que DEVE ficar `UNKNOWN - verify`.
NAO crie arquivos. NAO edite nada. Responda apenas a parcela.

## Fontes
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:37 (item B.5), :52 (C.5)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md:70 (REQ-09), :165 (US-009)
- .ai/specs/spec-005-container-layers-v1.spec.md:315-344 (SS12 UAT de camadas), :342 (evidencias UNKNOWN - verify)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0047","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}

## RESPOSTA — PARCELA DE CONSULTA (TA-0047 / agent-qa-sdet, 2026-11-03)

```json
{
  "task_id": "TA-0047",
  "status": "accepted",
  "parcel": {
    "dod": true,
    "artifacts": [],
    "notes": "(1) CRITERIO BINARIO fail-closed (precedente spec-005:331): cada fluxo critico pass/fail; UAT aprovada somente 100% PASS e zero defeitos criticos/bloqueantes abertos; qualquer reprovado = UAT reprovada; menores/medios ao backlog com severidade e decisao PO; evidencia com run id, exit code, timestamp, comando de repro; proibido fake green; fixtures 100% sinteticas (P-04).\n(2) ROTEIRO: matriz fluxo x US x REQ com trace REQ-x::UAT-nn::layer::case; reaproveitar F-01..F-07 spec-005 SS12 POR REFERENCIA (sem duplicar); fluxos produto: US-001 (simulacao USD/EUR->BRL, latencia <=2s/3s — C-07), US-002 (5 regimes), US-003 (spread/IOF 2 casas), US-004 (PDF <=3s, sem PII logs), US-005 (browsers ult. 2 versoes), US-006 (cache >=50%), US-008 (>=80% via run CI). US-007/016/017 so se ratificadas (KG-R-02/03). Papeis: executor qa-sdet, revisor security+reviewer, aprovador Humano CCB (Art. 5.3).\n(3) DESTINO EVIDENCIAS (C.5, spec-005:342): proposta QA-executavel — docs/uat/N6.2/ com relatorio-UAT-<yyyymmdd>-run<nn>.md (tabela pass/fail + defeitos com severidade) e docs/uat/N6.2/evidencias/ com F-<id>__US-<slug>__<yyyymmdd>__run<nn>.log|.png; retencao PERMANENTE versionada em git (trilha auditoria, sem exclusao); sintetico-only. RATIFICACAO CCB/PO NECESSARIA: destino final reservado ao GP em spec-005:342 — ratificar docs/uat/ (alternativa docs/auditorias/), retencao e carater bloqueante do relatorio. Formato/nomenclatura/captura = decisao QA-executavel.\n(4) UNKNOWN - verify: destino/retencao ratificados; versoes exatas browsers na data; valores spread/IOF (GAP-03); campos invoice (GAP-04); TTL cache (GAP-06); run id CI citavel enquanto G-05 nao auditado (B.7); inclusao US-016/017."
  },
  "kill_switch": "inherited"
}
```


## Critérios de Aceite
- [ ] Parcelo de consulta entregue com roteiro de UAT de produto
- [ ] Critério binário fail-closed definido (100% fluxos críticos, zero defeitos críticos)
- [ ] Destino de evidências proposto (condicionante CCB — não decisão final)
