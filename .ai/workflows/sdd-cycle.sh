#!/bin/bash
# sdd-cycle.sh — Ciclo SDD canônico (Revisado com base em opencode --help)
# Fundamentação: Glossário §5 + ADR-006 + Runbook SDD v1.1

set -euo pipefail

PERSONA=${1:-"coder"}
HANDOFF=${2:-"000-smoke-test.md"}
HANDOFF_PATH=".ai/handoffs/${HANDOFF}"

# 1. Validar pré-requisitos
if [ ! -f "$HANDOFF_PATH" ]; then
  echo "Erro: Handoff ${HANDOFF_PATH} não encontrado."
  exit 1
fi

if ! curl -s http://127.0.0.1:8080/health | grep -q "ok"; then
  echo "Erro: llama-server inativo na porta 8080."
  echo "Ação: sudo systemctl start llama-server"
  exit 1
fi

# 2. Trocar persona ativa (symlink runtime)
ln -sf "${PERSONA}.md" .ai/personas/active.md
echo "✓ Persona ativa: ${PERSONA}"

# 3. Extrair payload do handoff (lê o conteúdo markdown)
PAYLOAD=$(cat "$HANDOFF_PATH")

# 4. Executar OpenCode via CLI não-interativa (run)
# O OpenCode lerá .ai/personas/active.md e .ai/specs/ automaticamente via config.json
echo "✓ Executando handoff ${HANDOFF}..."
opencode run "${PAYLOAD}" --agent "${PERSONA}"

echo "✓ Ciclo SDD concluído. Lembre-se de commitar os artefatos gerados com co-autoria."
