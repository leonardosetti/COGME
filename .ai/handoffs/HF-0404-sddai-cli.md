---
id: HF-0404
title: 'Handoff: SDDAI CLI Orchestrator — Pipeline Unificado'
type: handoff
version: 1.0.0
status: draft
owner: agent-project-analyst
derived-from:
  - constitution.md (Art. 6.1)
last-revised: '2026-10-31'
lgpd-class: n/a
tags:
  - handoff
  - sddai
agent: agent-sddai-cli
created: 2026-10-31
updated: 2026-11-06
---
# Handoff: SDDAI CLI Orchestrator — Pipeline Unificado
## Contexto
O pipeline SDDAI `data_optimization` requer orquestração unificada de loader → memory → engineer → trainer via CLI `sddai`.
## Tarefa
Executar `sddai run data_optimization --source <arquivo> --epochs 3 --memory-threshold 10.0` e retornar parcel consolidado com status de todos os 4 componentes.
## Critérios de Aceite
- [ ] Pipeline executado em ordem: loader → memory → engineer → trainer
- [ ] Cada componente retorna ok=true
- [ ] Resultado consolidado com pipeline_id, status, summary
- [ ] Parcel JSON retornado com dod=true
## Restrições
- Zero dependências externas (stdlib Python apenas)
- Orquestração via subprocess (isolamento de componentes)
- kill_switch: inherited
- CPU-only, sem CUDA/cloud; FOSS-only; LGPD primária (zero PII em resultados).