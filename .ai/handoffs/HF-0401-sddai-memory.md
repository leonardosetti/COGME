---
id: ai-handoffs-hf-0401-sddai-memory
title: 'Handoff: SDDAI Memory Optimizer — Otimização de Memória'
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0401-sddai-memory.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
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