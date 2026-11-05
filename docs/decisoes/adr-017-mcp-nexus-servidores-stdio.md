---
id: docs-decisoes-adr-017-mcp-nexus-servidores-stdio
title: ADR-017 — Servidores MCP nexus-* (stdio, local-only)
type: adr
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-017-mcp-nexus-servidores-stdio.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- deprecated
---
# ADR-017 — Servidores MCP nexus-* (stdio, local-only) — DESCONTINUADO

| Campo | Valor |
|---|---|
| ID | ADR-017 |
| Título | Servidores MCP `nexus-*` (stdio, local-only) — descontinuados |
| Versão | 1.0.0 |
| Status | Deprecated |
| Data da decisão | 2026-11-04 |
| Decisor | GP Leonardo (CCB membro único) — autorização expressa TA-MCP-001 |
| Custódia | agent-ai-llm-rag-dag-mcp-roster-master-specialist |

## Contexto
Os 4 servidores `nexus-ledger`, `nexus-dispatch`, `nexus-kb`, `nexus-validate` foram implementados como servidores MCP stdio JSON-RPC 2.0 reais sob TA-MCP-001. Análise posterior mostrou **zero calls reais nos agentes** (apenas `initialize`/`tools/list` no log de uso) e duplicação de ~240 linhas entre os 4 servidores, cada um espelhando leitura/gravação de um único YAML local substituível por chamada direta de stdlib. Classificado como bloat.

## Decisão
Descontinuar os 4 servidores MCP `nexus-*` e o utilitário `mcp_usage_log.py`. Os arquivos são movidos para `.ai/deprecated/mcp-nexus/` (não publicáveis em repositório ativo) e removidos do registro em `.opencode/opencode.jsonc`. A leitura/gravação de `.ai/agents/ledger.yaml`, `.ai/agents/registry.yaml`, `.ai/knowledge_base.yaml` e validação de `scripts/mcp_*.py` volta a ser feita por chamada direta de stdlib nos scripts orquestradores (`nexus_dispatcher.py`, `validate_nexus_yaml.py`, etc.).

A ADR-017 será reativada somente quando provar-se necessário o desenvolvimento de MCP nexus (refact/consolidação).

## Conformidade
- Kill Switch: `inherited` (nenhum dado sai do localhost; arquivos mantidos localmente).
- P-01 / C-P-01: FOSS zero custo, sem custo recorrente, sem proprietário.
- P-02 / C-P-02: inferência e MCP locais; cloud não envolvida.
- P-03 / C-P-03: soberania de dados, zero telemetria.
- P-04 / C-P-04: LGPD, sem PII nos caminhos.
- Art. 4.5 / 4.6: inalterados (nenhum agente dependia dos MCPs).

## Efeito
Registros `nexus-*` removidos de `.opencode/opencode.jsonc` (8 blocos). Arquivos movidos para `.ai/deprecated/mcp-nexus/`. Nenhum agente chama os MCPs, logo não há impacto no flow de dispatch/agentes. Testes ajustados para importar do diretório deprecated.
