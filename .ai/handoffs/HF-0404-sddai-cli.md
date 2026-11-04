---
id: HF-0404
agent: agent-sddai-cli
status: ready
created: 2026-10-31
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