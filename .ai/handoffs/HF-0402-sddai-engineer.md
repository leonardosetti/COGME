---
id: HF-0402
agent: agent-sddai-engineer
status: ready
created: 2026-10-31
---
# Handoff: SDDAI Feature Engineer — Engenharia de Features
## Contexto
O pipeline SDDAI requer transformação de dados ingeridos em features estruturadas antes do treinamento.
## Tarefa
Executar `cogme-sddai-engineer.cli --input <json_loader> --output <json>` e retornar parcel com features extraídas.
## Critérios de Aceite
- [ ] Entrada é JSON válido com resultado do loader
- [ ] word_count, char_count, unique_words computados
- [ ] feature_checksum SHA-256 presente
- [ ] features.lexical_diversity e features.avg_words_per_line calculados
- [ ] Parcel JSON retornado com dod=true
## Restrições
- Zero dependências externas (stdlib Python apenas)
- Métricas determinísticas (não inventadas)
- kill_switch: inherited
- CPU-only, sem CUDA/cloud