---
id: ai-handoffs-hf-0403-sddai-trainer
title: 'Handoff: SDDAI Model Trainer — Treinamento de Modelo'
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0403-sddai-trainer.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---
# Handoff: SDDAI Model Trainer — Treinamento de Modelo
## Contexto
O pipeline SDDAI requer treinamento determinístico sobre features engenheiradas para produzir artefato de modelo.
## Tarefa
Executar `cogme-sddai-trainer.cli --input <json_engineer> --epochs 3 --output <json>` e retornar parcel com modelo treinado.
## Critérios de Aceite
- [ ] Entrada é JSON válido com resultado do engineer
- [ ] model_id gerado deterministicamente
- [ ] final_loss e accuracy computados
- [ ] training_checksum SHA-256 presente
- [ ] Parcel JSON retornado com dod=true
## Restrições
- Zero dependências externas (stdlib Python apenas)
- Treinamento determinístico (sem CUDA/cloud inference)
- kill_switch: inherited
- CPU-only