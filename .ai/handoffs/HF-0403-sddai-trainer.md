---
id: HF-0403
agent: agent-sddai-trainer
status: ready
created: 2026-10-31
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