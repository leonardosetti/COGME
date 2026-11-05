# MCP `nexus-*` — DESCONTINUADO / DEPRECATED

## Arquivos movidos para cá
- `mcp_nexus_ledger.py`
- `mcp_nexus_dispatch.py`
- `mcp_nexus_kb.py`
- `mcp_nexus_validate.py`
- `mcp_usage_log.py`

## Motivo
Zero calls reais nos agentes (apenas `initialize`/`tools/list` no log de uso). Cada um espelhava leitura/gravação de um único YAML local, substituível por chamada direta de stdlib. Classificado como bloat (ver análise prévia). Removidos do registro ativo em `.opencode/opencode.jsonc`.

## ADR-017
Status alterado de `ratificado` para `deprecated`. Reativado somente quando provar-se necessário desenvolvimento de MCP nexus (refact/consolidação).

## Reativação
Mover os arquivos de volta para `scripts/` e re-registrar em `.opencode/opencode.jsonc` (blocos `nexus-*` sob `mcpServers` e `mcp.servers`).
