---
id: HF-0400
agent: agent-sddai-loader
status: ready
created: 2026-10-31
---
# Handoff: SDDAI Data Loader — Ingestão de Dados
## Contexto
O pipeline SDDAI `data_optimization` requer ingestão de arquivo de entrada com validação de integridade (sha256). Este é o primeiro estágio do fluxo de 4 etapas.
## Tarefa
Executar `cogme-sddai-loader.cli --source <arquivo> --output <json>` e retornar parcel com metadados do arquivo ingerido.
## Critérios de Aceite
- [ ] Arquivo de origem existe e é legível
- [ ] Checksum SHA-256 computado e presente no resultado
- [ ] Resultado contém path, size_bytes, lines, checksum_sha256, content
- [ ] Parcel JSON retornado com dod=true
## Restrições
- Zero dependências externas (stdlib Python apenas)
- Não modificar arquivo de origem
- kill_switch: inherited
- CPU-only, sem CUDA/cloud