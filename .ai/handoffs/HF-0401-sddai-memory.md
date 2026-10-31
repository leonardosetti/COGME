---
id: HF-0401
agent: agent-sddai-memory
status: ready
created: 2026-10-31
---
# Handoff: SDDAI Memory Optimizer — Otimização de Memória
## Contexto
O pipeline SDDAI requer otimização de memória antes da engenharia de features. Threshold padrão de 10GB.
## Tarefa
Executar `cogme-sddai-memory.cli --threshold 10.0 --output <json>` e retornar parcel com status de memória e otimizações aplicadas.
## Critérios de Aceite
- [ ] /proc/meminfo lido (ou fallback para ambiente não-Linux)
- [ ] garbage collection executado
- [ ] Resultado contém total/available/used memory em GB
- [ ] within_threshold avaliado corretamente
- [ ] Parcel JSON retornado com dod=true
## Restrições
- Zero dependências externas (stdlib Python apenas)
- Não exceder envelope de hardware (8700G / 58GB RAM)
- kill_switch: inherited
- CPU-only, sem CUDA/cloud