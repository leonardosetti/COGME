---
id: ai-handoffs-hf-0404-sddai-cli
title: 'Handoff: SDDAI CLI Orchestrator — Pipeline Unificado'
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0404-sddai-cli.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
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
- CPU-only, sem CUDA/cloud