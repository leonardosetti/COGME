---
id: decisoes-adr-017-mcp-nexus-servidores-stdio
title: ADR-017 — Servidores MCP nexus-* (stdio, local-only)
version: 1.0.0
class: decisao-adr
status: ratificado
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-017-mcp-nexus-servidores-stdio.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- normalizado
---
# ADR-017 — Servidores MCP nexus-* (stdio, local-only)

| Campo | Valor |
|---|---|
| ID | ADR-017 |
| Título | Conversão dos 4 stubs `nexus-*` em servidores MCP stdio JSON-RPC reais |
| Versão | 1.0.0 |
| Status | Ratificado |
| Data da decisão | 2026-11-04 |
| Decisor | GP Leonardo (CCB membro único) — autorização expressa TA-MCP-001 |
| Custódia | agent-ai-llm-rag-dag-mcp-roster-master-specialist |

## Contexto
Os 4 servidores `nexus-ledger`, `nexus-dispatch`, `nexus-kb`, `nexus-validate` estavam declarados no OKB §3.4 mas existiam apenas como stubs (funções auxiliares, sem protocolo MCP). TA-MCP-001 exige expô-los como servidores MCP registrados.

## Decisão
Reescrever os 4 stubs como servidores MCP stdio JSON-RPC 2.0 reais, cada um independente, expor `initialize`, `tools/list` e `tools/call`, transport stdio apenas, local-only (sem rede), FOSS (Python stdlib + PyYAML), zero custo, sem PII, sem dados sensíveis nos caminhos. Registrar em `.mcp-servers.json` e `.opencode/opencode.jsonc` com `command: python3` e `args: scripts/mcp_nexus_*.py`.

## Conformidade
- Kill Switch: `inherited` (nenhum dado de código/specs/handoffs/PII sai do localhost).
- P-01 / C-P-01: FOSS zero custo, sem custo recorrente, sem proprietário.
- P-02 / C-P-02: inferência e MCP locais; cloud não envolvida.
- P-03 / C-P-03: soberania de dados, zero telemetria.
- P-04 / C-P-04: LGPD, sem PII em caminhos MCP (`allowedPaths` do filesystem já restrito a pastas não sensíveis).
- Art. 4.5: agente não se auto-delega (sender `nexus-prime-ultimate` ≠ target `agent-ai-llm-rag-dag-mcp-roster-master-specialist`).
- Art. 4.6: Kill Switch propagado em todo envelope/parcela.

## Efeito
`docs/conhecimento/okb.md` §3.4 já lista os 4 MCPs como "Python stdlib + PyYAML"; esta ADR torna a implementação condizente com o OKB. Não altera o hash ratificado do OKB (nenhuma edição em OKB.md).
