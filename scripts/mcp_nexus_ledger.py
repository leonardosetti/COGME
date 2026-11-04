#!/usr/bin/env python3
"""MCP stdio JSON-RPC — nexus-ledger. Local-only, sem rede, sem PII."""
import json
import sys
import yaml
from datetime import datetime, timezone

LEDGER = ".ai/agents/ledger.yaml"


def load_ledger():
    with open(LEDGER, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_ledger(data):
    with open(LEDGER, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)


def handle(req):
    method = req.get("method")
    params = req.get("params") or {}
    rid = req.get("id")
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": rid, "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "mcp-nexus-ledger", "version": "0.1.0"},
        }}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"tools": [
            {"name": "ledger_read", "description": "Lê .ai/agents/ledger.yaml", "inputSchema": {"type": "object", "properties": {}}},
            {"name": "ledger_append", "description": "Anexa linha de auditoria ao ledger", "inputSchema": {"type": "object", "properties": {"line": {"type": "string"}}, "required": ["line"]}},
        ]}}
    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments") or {}
        try:
            if name == "ledger_read":
                text = yaml.safe_dump(load_ledger(), allow_unicode=True, sort_keys=False)
            elif name == "ledger_append":
                line = args.get("line", "")
                data = load_ledger()
                if not isinstance(data, list):
                    data = []
                data.append({
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "line": line,
                })
                save_ledger(data)
                text = "ok"
            else:
                return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "tool desconhecida"}}
            return {"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": text}]}}
        except Exception as exc:  # noqa: BLE001
            return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32603, "message": str(exc)}}
    return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "método desconhecido"}}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue
        resp = handle(req)
        if resp is not None and req.get("id") is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
