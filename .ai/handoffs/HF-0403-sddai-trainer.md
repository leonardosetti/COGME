---
id: HF-0403
title: 'Handoff: SDDAI Model Trainer — Treinamento de Modelo'
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
agent: agent-sddai-trainer
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