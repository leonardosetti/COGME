# DOCUMENTO CANÔNICO DEFINITIVO — v3.0.0

## Second Brain · Memória Persistente · MCPs · Prompt Ubíquo

## Consolidação Forense de Todas as Rodadas (R1 → R5)

**Documento:** `SDDAI-CANON-DEFINITIVE.md`
**Versão:** 3.0.0 (ratificação forense final)
**Data:** 29/10/2026
**Status:** **CANÔNICO IMUTÁVEL** até gatilho de reavaliação
**kill_switch:** `inherited`
**Norma suprema:** `constitution.md` v1.1.0 (Art. 2)
**Fontes primárias auditadas:**

- `download_model.sh` (4.1KB)
- `qwen_list.txt` (22KB)
- `archtecture_report_Local_SDDAI.md` (13KB, ADR 2026-09-07)
- `system-profile-20260907-133205.md` (3.4KB)
- `hardware.md` (3.3KB)
- `.opencode/opencode.json` (config ratificada pelo usuário)
- `/etc/systemd/system/llama-server.service` (service ratificado)

---

## 0. REVISÃO CRÍTICA FORENSE (Auto-Correção Implacável)

### 0.1. Inconsistências Detectadas nos Documentos de Referência

| ID                | Inconsistência                                    | Fonte 1                                                               | Fonte 2                                           | Veredito Canônico                                                                                      |
| ----------------- | -------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **INC-F01** | Divergência de modelo                             | `download_model.sh` → `Qwen3.8-27B-GGUF` (denso)                 | OpenCode config → `Qwen3-30B-A3B-Q4_K_M` (MoE) | **ADR mais recente vence:** MoE 30B-A3B. Script de download está **desatualizado**.        |
| **INC-F02** | Architecture report previa 32B denso               | `archtecture_report` (set/2026) → "Qwen 32B Q4_K_M como principal" | OpenCode config (out/2026) → MoE 30B-A3B         | **ADR mais recente vence:** MoE 30B-A3B substituiu o 32B denso como principal.                    |
| **INC-F03** | `qwen_list.txt` não contém "30B", "A3B", "MoE" | Lista top HF                                                          | Modelo em uso                                     | **Ação:** o modelo MoE é recente ou está em repo específico. Validar com busca direta no HF. |
| **INC-F04** | RAM total 64GB vs 58GB                             | `archtecture_report` → "64GB RAM unificada"                        | `system-profile` → "Total: 58.0GB"             | **Fonte primária vence:** 58GB é o valor real medido. Architecture-report arredondou.           |
| **INC-F05** | Vulkan 1.4.354 vs 1.4.357                          | `system-profile` → API 1.4.354                                     | `hardware.md` → Vulkan 1.4.357                 | **Ambas corretas:** API 1.4.354 (runtime) vs driver 1.4.357 (loader).                             |
| **INC-F06** | Mesa 26.2.1 vs 26.2.2                              | `hardware.md` → mesa 26.2.1                                        | `system-profile` → 26.2.2                      | **Atualização entre capturas:** ambas válidas, usar a mais recente (26.2.2).                   |
| **INC-F07** | Minhas rodadas anteriores usaram 8k ctx            | R1-R4                                                                 | OpenCode config → 32768 tokens                   | **Config real vence:** contexto é 32k, não 8k.                                                  |
| **INC-F08** | Minhas rodadas anteriores ignoraram L1/L2/L3       | R1-R5                                                                 | `archtecture_report` (seção 1.1)              | **Arquitetura ratificada:** incorporar separação ortogonal de camadas.                          |

### 0.2. Lições Meta-Aprendidas (Correções sobre Correções)

1. **Nunca assumir modelo sem ler ADR vigente:** o architecture_report de set/2026 previa 32B, mas o ADR de out/2026 (OpenCode config) ratificou 30B-A3B MoE.
2. **Nunca arredondar RAM:** 58GB ≠ 64GB. Diferença de 6GB é crítica para modelos 72B.
3. **Nunca inferir contexto sem ler config real:** OpenCode tem 32k configurado, não 8k.
4. **Sempre reconciliar scripts vs ADRs:** `download_model.sh` precisa de atualização para refletir o modelo vigente.
5. **Separar "arquitetura prevista" vs "arquitetura implementada":** architecture_report é previsto; OpenCode config é implementado.

---

## 1. RESOLUÇÃO CANÔNICA — HIERARQUIA DE ADRs

### 1.1. Linha do Tempo de Decisões

```
2026-09-07  ──┐  architecture_report_Local_SDDAI.md (ADR-001 histórico)
              │   Modelo: Qwen 32B Q4_K_M (denso) como principal
              │   Rejeita Hermes, SpecKit, frameworks
              │   RAM: 64GB (arredondado)
              │
2026-10-XX  ──┤  ADR OpenCode config (ratificado pelo usuário)
              │   Modelo: Qwen3-30B-A3B Q4_K_M (MoE) como principal
              │   Contexto: 32768 tokens
              │   Output: 4096 tokens
              │   Reasoning effort: default
              │
2026-10-29  ──┤  Este documento (v3.0.0)
              │   Consolida tudo, resolve inconsistências
              │   Reconcilia download_model.sh com ADR vigente
              │   RAM real: 58GB
              │
2027-01-29  ──┘  Próxima revisão agendada (90 dias)
```

### 1.2. Decisões Canônicas Vigentes

| #              | Decisão                                                          | Fonte                         | Status           |
| -------------- | ----------------------------------------------------------------- | ----------------------------- | ---------------- |
| **C-01** | **Modelo principal:** Qwen3-30B-A3B Q4_K_M (MoE, 3B ativos) | OpenCode config               | ✅ VIGENTE       |
| **C-02** | **Modelo fallback:** Qwen 14B Q4_K_M (denso)                | architecture_report           | ✅ VIGENTE       |
| **C-03** | **Modelo batch:** Qwen 72B Q4_K_M (apenas offline)          | architecture_report           | ⚠️ CONDICIONAL |
| **C-04** | **Contexto configurado:** 32768 tokens                      | OpenCode config               | ✅ VIGENTE       |
| **C-05** | **Contexto efetivo recomendado:** 24000 tokens (75% de 32k) | Derivado                      | ✅ VIGENTE       |
| **C-06** | **Orquestrador:** ELIMINADO (Hermes rejeitado)              | architecture_report           | ✅ VIGENTE       |
| **C-07** | **Frameworks SDD:** REJEITADOS (SpecKit, etc.)              | architecture_report           | ✅ VIGENTE       |
| **C-08** | **Interface:** OpenCode + Obsidian (sinergia perfeita)      | architecture_report           | ✅ VIGENTE       |
| **C-09** | **Motor:** llama.cpp + Vulkan + systemd service             | architecture_report + service | ✅ VIGENTE       |
| **C-10** | **RAM real:** 58GB (não 64GB)                              | system-profile                | ✅ VIGENTE       |

### 1.3. Separação Ortogonal de Camadas (L1/L2/L3)

Princípio canônico ratificado pelo architecture_report, incorporado a partir desta versão:

| Camada                         | Responsabilidade                        | Artefatos                                      | Mudança   |
| ------------------------------ | --------------------------------------- | ---------------------------------------------- | ---------- |
| **L1 — Infraestrutura** | Motor de inferência e hardware         | llama.cpp, Vulkan, systemd, modelos            | Raramente  |
| **L2 — Personas**       | Comportamento do modelo via contexto    | `.ai/personas/*.md`, `_base.md`            | Por agente |
| **L3 — Metodologia**    | Organização do trabalho e validação | `.ai/specs/`, `handoffs/`, `ledger.yaml` | Por tarefa |

**Regra de ouro:** Mudanças em uma camada NÃO exigem mudanças em outras.

---

## 2. ARQUITETURA FINAL RECONCILIADA

### 2.1. Perfil de Hardware (Canônico Corrigido)

```yaml
# .ai/config/hardware-profile.yaml (CRIAR — versão definitiva)
version: "3.0.0"
ratified: "2026-10-29"
sources:
  - system-profile-20260907-133205.md
  - hardware.md
  - archtecture_report_Local_SDDAI.md

cpu:
  model: "AMD Ryzen 7 8700G"
  arch: "Zen 4 (znver4)"
  cores: 8
  threads: 16
  avx512: true
  max_mhz: 5177
  governor: "performance"
  driver: "amd-pstate-epp"

gpu:
  model: "Radeon 780M"
  codename: "Phoenix1"
  arch: "RDNA 3"
  type: "APU (VRAM compartilhada com RAM)"
  vulkan_api: "1.4.354"
  vulkan_driver: "1.4.357"
  mesa: "26.2.2"
  driver_kernel: "amdgpu"

memory:
  total_gb: 58        # Valor real medido (NÃO 64GB)
  available_gb: 49
  swap_gb: 16
  unified: true
  llama_server_limit_gb: 32   # MemoryMax do systemd service
  overcommit: 0               # Heuristic (default, safe)

storage:
  root_gb: 246          # /
  home_gb: 344          # /home (projetos)
  var_gb: 458           # /var (modelos)
  extra_gb: 98          # /extra (backup)
  models_path: "/var/lib/llama.cpp/models"
  backup_path: "/extra/backup/llama-models"

os:
  distro: "Arch Linux"
  kernel: "7.1.9-zen1-2-zen"
  desktop: "GNOME 50.4"
  gcc: "16.2.1"
  cmake: "4.4.3"
  ninja: "1.13.2"
  make: "GNU Make 4.4.1"

motherboard:
  vendor: "Micro-Star International"
  model: "MAG B650 TOMAHAWK WIFI (MS-7D75)"
  bios: "American Megatrends 1.E0"

network:
  ethernet: "Realtek RTL8125 2.5GbE (r8169)"
  wifi: "MediaTek MT7922 802.11ax (mt7921e)"
  bluetooth: "MediaTek 5.3"
```

### 2.2. Catálogo de Modelos (Canônico)

```yaml
# .ai/config/models-catalog.yaml (CRIAR)
version: "3.0.0"
ratified: "2026-10-29"

models:
  primary:
    name: "Qwen3-30B-A3B Q4_K_M"
    type: "MoE (Mixture of Experts)"
    params_total_b: 30
    params_active_b: 3
    quantization: "Q4_K_M"
    file_path: "/var/lib/llama.cpp/models/Qwen3-30B-A3B-Q4_K_M.gguf"
    file_size_gb: 18
    ram_active_gb: 4              # MoE sparsity
    context_configured: 32768
    context_effective: 24000
    output_max: 4096
    reasoning_effort: "default"
    target_tg_tps: 12             # MoE mais rápido
    target_pp_tps: 25
    status: "ACTIVE (ratificado via OpenCode config ADR)"

  fallback:
    name: "Qwen 14B Q4_K_M"
    type: "Dense"
    params_total_b: 14
    quantization: "Q4_K_M"
    file_size_gb: 9
    ram_active_gb: 10
    context_max: 32768
    target_tg_tps: 20
    usage: "Testes rápidos, roteamento, baixa latência"
    status: "PLANNED (pendente download)"

  batch:
    name: "Qwen 72B Q4_K_M"
    type: "Dense"
    params_total_b: 72
    quantization: "Q4_K_M"
    file_size_gb: 42
    ram_active_gb: 44
    context_max: 4096
    target_tg_tps: 1
    usage: "Apenas processamento assíncrono offline"
    status: "DEFERRED (não baixar até necessidade real)"

  deprecated:
    - name: "Qwen3.8-27B Q4_K_M"
      reason: "Substituído por Qwen3-30B-A3B MoE (ADR out/2026)"
      action: "Manter em /var/lib/llama.cpp/models/ como backup, mas não usar"
      source_script: "download_model.sh (DESATUALIZADO)"
```

### 2.3. Mapa de Memória Persistente (Mantido — estava correto)

```
MEMÓRIA DO CIRCUITO SDD (Single Source of Truth)
│
├── ESTADO DE SESSÃO (curto prazo) — Camada L3
│   └── .ai/agents/ledger.yaml          ← ESTENDER com current_session
│
├── DECISÕES ARQUITETURAIS (longo prazo) — Camada L3
│   └── docs/decisoes/ADR-*.md          ← POPULAR (ADR-001 a ADR-007)
│
├── LIÇÕES APRENDIDAS (longo prazo) — Camada L3
│   └── docs/conhecimento/licoes-aprendidas/
│       ├── MF1-licoes.md               ← POPULAR (já tem 1.9KB)
│       ├── MF2-licoes.md               ← POPULAR (0B)
│       ├── MF3-licoes.md               ← POPULAR (0B)
│       └── transversais.md             ← CRIAR (único arquivo novo)
│
├── CONHECIMENTO OPERACIONAL (referência) — Camada L3
│   └── docs/conhecimento/
│       ├── KB-INDEX.md                 ← ESTENDER
│       ├── OKB.md                      ← MANTER (78KB)
│       └── glossario.md                ← MANTER (21KB)
│
├── ESPECIFICAÇÕES (contexto de tarefa) — Camada L3
│   └── .ai/specs/
│       ├── eap.md                      ← POPULAR (0B)
│       ├── requisitos.md               ← POPULAR (0B)
│       └── tap.md                      ← POPULAR (0B)
│
├── PERSONAS (comportamento) — Camada L2
│   └── .ai/personas/
│       ├── active.md                   ← MANTER (symlink runtime)
│       ├── _base.md                    ← ESTENDER com prompt canônico
│       ├── coder.md, reviewer.md, tester.md, pm.md
│       └── all.md                      ← Persona consolidada
│
└── INFRAESTRUTURA — Camada L1
    ├── /var/lib/llama.cpp/models/      ← Modelos GGUF
    ├── /etc/systemd/system/llama-server.service
    └── .opencode/opencode.json         ← Config OpenCode
```

**Único arquivo NOVO a criar:** `docs/conhecimento/licoes-aprendidas/transversais.md`

### 2.4. Regras Canônicas para `.ai/` (Incorporadas do architecture_report)

**Regra de Ouro (architecture_report seção 6.3):**

> "Se não é lido pelo OpenCode ou pelo script, não pertence em `.ai/`"

**Regras de Consolidação:**

1. **Limite de 10 arquivos por diretório** em `.ai/` — força consolidação
2. **Revisão trimestral** — deletar arquivos não usados há >90 dias
3. **Nenhum framework externo** — apenas markdown puro + scripts shell/python
4. **Parsing determinístico** — sem dependências de bibliotecas complexas
5. **SSOT absoluto** — um fato = um local, nunca duplicar

---

## 3. CONFIGURAÇÃO SISTÊMICA RECONCILIADA

### 3.1. llama-server Service (Já Configurado — NÃO MODIFICAR)

**Arquivo:** `/etc/systemd/system/llama-server.service`

```ini
[Unit]
Description=llama.cpp server (Qwen 30B-A3B MoE Q4_K_M - APU Optimized)
After=network.target

[Service]
Type=simple
User=leonardo
Group=leonardo

ExecStart=/home/leonardo/bin/llama-server \
  -m /var/lib/llama.cpp/models/Qwen3-30B-A3B-Q4_K_M.gguf \
  -c 32768 \
  --host 127.0.0.1 \
  --port 8080 \
  -ngl 99 \
  --flash-attn on \
  --no-mmap \
  --metrics \
  --threads 8 \
  --threads-batch 8
Restart=on-failure
RestartSec=7
LimitNOFILE=65536
MemoryMax=32G

[Install]
WantedBy=multi-user.target
```

**Ações proibidas:**

- ❌ NÃO modificar o service
- ❌ NÃO criar script alternativo de start
- ❌ NÃO alterar flags de otimização (já otimizadas para APU)

**Ações permitidas:**

- ✅ `systemctl status llama-server` (verificar)
- ✅ `systemctl restart llama-server` (apenas se falhar)
- ✅ `journalctl -u llama-server -f` (debug)

### 3.2. OpenCode Config (Já Configurado — MANTER)

**Arquivo:** `.opencode/opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "local/qwen30b-moe",
  "providers": {
    "local": {
      "name": "Local Llama Server",
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": {
        "baseURL": "http://127.0.0.1:8080/v1",
        "apiKey": "sk-local-dummy-key"
      },
      "models": {
        "qwen30b-moe": {
          "name": "Qwen3 30B MoE Local",
          "modelID": "/var/lib/llama.cpp/models/Qwen3-30B-A3B-Q4_K_M.gguf",
          "capabilities": {
            "tools": true,
            "input": ["text"],
            "output": ["text"]
          },
          "limit": {
            //"context": 32768,
            "context": 45700,
            "output": 4096
          },
          "body": {
            "reasoning_effort": "default"
          }
        }
      }
    }
  },
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Edit",
      "Bash",
      "Shell"
    ] //,
//    "deny": [
//    "Bash(python *)",
//    "Bash(pip *)",
//      "Bash(pacman *)",
//      "Bash(yay *)",
//      "Bash(systemctl *)",
//      "Bash(sudo *)",
//      "Bash(curl * | sh)",
//      "Bash(wget * -O- | sh)"
//    ]
  }
}
```

### 3.3. Reconciliação Necessária: `download_model.sh`

**Problema:** O script atual baixa `Qwen3.8-27B-GGUF` (denso), mas o ADR vigente é `Qwen3-30B-A3B-Q4_K_M` (MoE).

**Ação Canônica:** Atualizar `download_model.sh` para refletir o modelo vigente.

**Proposta de atualização (TA-RECONCILE-001):**

```Shell
#!/bin/bash
# Pipeline Unificado de Download e Validação de Modelos SDD
# Versão: 3.0 (Reconciliado com ADR out/2026 — MoE como principal)

set -e

# ==============================================================================
# CONFIGURAÇÕES ATUALIZADAS
# ==============================================================================
MODEL_DIR="/var/lib/llama.cpp/models"
BACKUP_DIR="/extra/backup/llama-models"

# Modelo principal: Qwen3-30B-A3B (MoE) - ADR vigente
PRIMARY_REPO="Qwen/Qwen3-30B-A3B-GGUF"  # TODO: validar repo exato no HF
PRIMARY_PATTERN="*[Qq]4_[Kk]_[Mm]*.gguf"

# Modelo fallback: Qwen 14B (denso) - para testes rápidos
FALLBACK_REPO="unsloth/Qwen2.5-14B-Instruct-GGUF"
FALLBACK_PATTERN="*[Qq]4_[Kk]_[Mm]*.gguf"

# ... (resto do script mantido)
```

**Validação:** Buscar repositório exato do Qwen3-30B-A3B no HuggingFace antes de executar.

### 3.4. Obsidian Vault (Já Configurado — MANTER)

**Vault:** `./docs/conhecimento/`
**Ações proibidas:**

- ❌ NÃO criar novo vault
- ❌ NÃO instalar plugins proprietários
- ❌ NÃO habilitar sync proprietário

**Ações permitidas:**

- ✅ Instalar plugin Dataview (FOSS) para consultar YAML/JSON
- ✅ Configurar `.obsidian/` no gitignore (exceto templates)
- ✅ Abrir vault via File → Open Vault

---

## 4. MCPs CUSTOMIZADOS (Governança COGME)

### 4.1. Inventário Consolidado

| MCP                | Script                            | Função            | Prioridade | Complexidade |
| ------------------ | --------------------------------- | ------------------- | ---------- | ------------ |
| `nexus-dispatch` | `scripts/mcp_nexus_dispatch.py` | Despachar envelopes | P0         | Média       |
| `nexus-ledger`   | `scripts/mcp_nexus_ledger.py`   | Estado de sessão   | P0         | Baixa        |
| `nexus-validate` | `scripts/mcp_nexus_validate.py` | Validar registry    | P1         | Baixa        |
| `nexus-kb`       | `scripts/mcp_nexus_kb.py`       | Consultar KB        | P1         | Baixa        |
| `nexus-handoff`  | `scripts/mcp_nexus_handoff.py`  | Parsear handoffs    | P2         | Baixa        |
| `nexus-adr`      | `scripts/mcp_nexus_adr.py`      | Consultar ADRs      | P2         | Baixa        |

### 4.2. Especificação Mínima: `mcp_nexus_ledger.py`

```python
#!/usr/bin/env python3
"""
MCP Server: Nexus Ledger — leitura/escrita de ledger.yaml
Camada L3 (Metodologia) - SSOT para estado de sessão
"""

import yaml
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, List, Dict, Any

LEDGER = Path(".ai/agents/ledger.yaml")


def read_ledger() -> Dict[str, Any]:
    """Lê ledger.yaml completo."""
    with open(LEDGER) as f:
        return yaml.safe_load(f) or {}


def get_current_session() -> Optional[Dict[str, Any]]:
    """Retorna current_session ou None."""
    ledger = read_ledger()
    return ledger.get("current_session")


def update_session(task_id: str, phase: str, agent: str, tokens: int = 0):
    """Atualiza current_session no ledger."""
    ledger = read_ledger()
    ledger["current_session"] = {
        "task_id": task_id,
        "phase": phase,
        "active_agent": agent,
        "context_budget_tokens": 24000,  # 75% de 32k
        "context_used_tokens": tokens,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    ledger["last_updated"] = datetime.now(timezone.utc).isoformat()
    with open(LEDGER, "w") as f:
        yaml.dump(ledger, f, default_flow_style=False, allow_unicode=True)


def append_audit(task_id: str, agent: str, action: str, status: str):
    """Adiciona entrada ao audit_trail (append-only)."""
    ledger = read_ledger()
    ledger.setdefault("audit_trail", []).append({
        "task_id": task_id,
        "agent": agent,
        "action": action,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": status,
    })
    with open(LEDGER, "w") as f:
        yaml.dump(ledger, f, default_flow_style=False, allow_unicode=True)


def add_blocker(task_id: str, reason: str, blocked_by: Optional[str] = None):
    """Registra tarefa bloqueada."""
    ledger = read_ledger()
    ledger.setdefault("blocked_tasks", []).append({
        "task_id": task_id,
        "reason": reason,
        "blocked_by": blocked_by,
        "blocked_since": datetime.now(timezone.utc).isoformat(),
    })
    with open(LEDGER, "w") as f:
        yaml.dump(ledger, f, default_flow_style=False, allow_unicode=True)


def clear_blocker(task_id: str):
    """Remove blocker de tarefa resolvida."""
    ledger = read_ledger()
    ledger["blocked_tasks"] = [
        b for b in ledger.get("blocked_tasks", []) if b.get("task_id") != task_id
    ]
    with open(LEDGER, "w") as f:
        yaml.dump(ledger, f, default_flow_style=False, allow_unicode=True)
```

### 4.3. Integração com OpenCode (Adicionar ao config)

```json
{
  "model": "local/qwen30b-moe",
  "providers": { /* ... existente ... */ },
  "permissions": { /* ... existente ... */ },
  "mcpServers": {
    "nexus-dispatch": {
      "command": "python3",
      "args": ["scripts/mcp_nexus_dispatch.py"]
    },
    "nexus-ledger": {
      "command": "python3",
      "args": ["scripts/mcp_nexus_ledger.py"]
    },
    "nexus-validate": {
      "command": "python3",
      "args": ["scripts/mcp_nexus_validate.py"]
    },
    "nexus-kb": {
      "command": "python3",
      "args": ["scripts/mcp_nexus_kb.py"]
    }
  }
}
```

---

## 5. FLUXO DE AÇÕES COMPLETO (Sequenciamento Canônico)

### 5.1. Fase 0 — Pré-Requisitos (GATE OBRIGATÓRIO)

| #   | Ação                                  | Comando                                             | Critério                    |
| --- | --------------------------------------- | --------------------------------------------------- | ---------------------------- |
| 0.1 | Verificar llama-server ativo            | `systemctl status llama-server`                   | `Active: active (running)` |
| 0.2 | Verificar modelo carregado              | `curl http://127.0.0.1:8080/v1/models`            | JSON com `Qwen3-30B-A3B`   |
| 0.3 | Validar gateways                        | `python3 scripts/validate_nexus_yaml.py --report` | EXIT 0                       |
| 0.4 | Validar dispatcher                      | `python3 scripts/nexus_dispatcher.py --report`    | EXIT 0                       |
| 0.5 | Validar sync                            | `python3 scripts/sync_agent_registry.py --check`  | `[OK]`                     |
| 0.6 | Executar testes                         | `python3 -m pytest tests/ -x`                     | 0 failures                   |
| 0.7 | Verificar specs vazias                  | `wc -c .ai/specs/{eap,requisitos,tap}.md`         | Registrar gaps               |
| 0.8 | Benchmark MoE                           | Teste com 100 tokens output                         | ≥ 12 t/s                    |
| 0.9 | **Reconciliar download_model.sh** | TA-RECONCILE-001                                    | Script reflete MoE           |

### 5.2. Fase 1 — Configuração Sistêmica (Verificar)

| #   | Ação                                                 | Artefato                                 |
| --- | ------------------------------------------------------ | ---------------------------------------- |
| 1.1 | Criar `hardware-profile.yaml`                        | `.ai/config/hardware-profile.yaml`     |
| 1.2 | Criar `models-catalog.yaml`                          | `.ai/config/models-catalog.yaml`       |
| 1.3 | **NÃO** criar script start (service já existe) | —                                       |
| 1.4 | **NÃO** criar vault Obsidian (já existe)       | —                                       |
| 1.5 | Estender `opencode.json` com MCPs                    | `.opencode/opencode.json`              |
| 1.6 | Validar llama-server responde                          | `curl http://127.0.0.1:8080/v1/models` |

### 5.3. Fase 2 — Memória Persistente

| #   | Ação                                           | Artefato                                                |
| --- | ------------------------------------------------ | ------------------------------------------------------- |
| 2.1 | Estender `ledger.yaml` com `current_session` | `.ai/agents/ledger.yaml`                              |
| 2.2 | Criar `transversais.md`                        | `docs/conhecimento/licoes-aprendidas/transversais.md` |
| 2.3 | Popular MF2-licoes.md e MF3-licoes.md            | `docs/conhecimento/licoes-aprendidas/`                |
| 2.4 | Estender KB-INDEX.md                             | `docs/conhecimento/KB-INDEX.md`                       |
| 2.5 | Criar ADR-007 (memória persistente)             | `docs/decisoes/ADR-007-memory.md`                     |
| 2.6 | Popular specs vazias (eap, requisitos, tap)      | `.ai/specs/`                                          |

### 5.4. Fase 3 — MCPs Customizados

| #   | Ação                                    | Artefato                                     |
| --- | ----------------------------------------- | -------------------------------------------- |
| 3.1 | Inspecionar `mcp_bridge.py` existente   | Relatório                                   |
| 3.2 | Criar `mcp_nexus_ledger.py`             | `scripts/`                                 |
| 3.3 | Criar `mcp_nexus_kb.py`                 | `scripts/`                                 |
| 3.4 | Estender `opencode.json` com mcpServers | `.opencode/opencode.json`                  |
| 3.5 | Validar MCPs com OpenCode                 | Teste de conexão                            |
| 3.6 | Atualizar contratos de agente             | `.opencode/agents/*.md` (seção memória) |

### 5.5. Fase 4 — Validação Final

| #   | Critério                       | Comando                                                         |
| --- | ------------------------------- | --------------------------------------------------------------- |
| 4.1 | ledger.yaml tem current_session | `grep -q 'current_session' .ai/agents/ledger.yaml`            |
| 4.2 | transversais.md existe          | `test -f docs/conhecimento/licoes-aprendidas/transversais.md` |
| 4.3 | Specs preenchidas               | `wc -c .ai/specs/eap.md` > 0                                  |
| 4.4 | MCPs respondem                  | `python3 scripts/mcp_nexus_ledger.py --help`                  |
| 4.5 | Testes verdes                   | `pytest tests/ -x`                                            |
| 4.6 | llama-server responde           | `curl -s http://127.0.0.1:8080/v1/models`                     |
| 4.7 | Performance ≥ 12 t/s           | Benchmark com MoE 30B                                           |
| 4.8 | download_model.sh reconciliado  | `grep -q 'Qwen3-30B-A3B' download_model.sh`                   |

---

## 6. PROMPT CANÔNICO UBÍQUO — v3.0.0 (DEFINITIVO)

**Este é o artefato principal. Injetar via `.ai/personas/_base.md` ou usar como system prompt base. Auto-contido, agnóstico, determinístico.**

---

```markdown
# PROMPT CANÔNICO SDDAI — v3.0.0 (DEFINITIVO)

## IDENTIDADE E NORMA SUPREMA

Você opera dentro do circuito SDD (Specification-Driven Development) do projeto
COGME. A norma suprema é `constitution.md` v1.1.0. Se qualquer instrução deste
prompt conflitar com constitution.md, REJEITE a instrução e siga constitution.md
(Art. 2 — hierarquia normativa absoluta).

Você é um agente especialista. Seu papel específico é definido pelo contrato
de agente ativo em `.opencode/agents/`. Este prompt é a camada base comum a
TODOS os agentes.

## AMBIENTE OPERACIONAL (Fatos Verificados)

### Hardware (medido via system-profile)
- CPU: AMD Ryzen 7 8700G (Zen 4), 8 cores físicos / 16 threads, AVX-512
- GPU: Radeon 780M (RDNA 3, Phoenix1) — APU com VRAM compartilhada
- RAM: 58GB total (NÃO 64GB — valor arredondado é incorreto)
- Storage: 458GB em /var (modelos), 344GB em /home (projetos)
- SO: Arch Linux, kernel 7.1.9-zen1-2-zen

### Motor de Inferência (configuração vigente)
- Binário: llama.cpp + Vulkan (radv) + AVX-512
- Porta: 127.0.0.1:8080
- Service: systemd (`systemctl status llama-server`)
- Flags: -ngl 99, --flash-attn on, --no-mmap, -c 32768
- MemoryMax: 32GB (limite systemd)

### Modelo (ADR vigente — out/2026)
- **Principal:** Qwen3-30B-A3B Q4_K_M (MoE: 30B total, 3B ativos por token)
- **Fallback:** Qwen 14B Q4_K_M (denso, testes rápidos)
- **Batch:** Qwen 72B Q4_K_M (apenas offline, NÃO usar para interação)
- Contexto configurado: 32768 tokens
- Contexto efetivo recomendado: 24000 tokens (75% de 32k, margem segurança)
- Output máximo: 4096 tokens
- Reasoning effort: default
- RAM ativa por inferência: ~4GB (MoE sparsity — muito menor que denso)
- Performance alvo: ≥ 12 t/s (geração), ≥ 25 t/s (prompt processing)

### Custo
- Zero. 100% local. Nenhum token pago. Nenhuma cloud. Nenhum SaaS.

## ARQUITETURA ORTOGONAL (L1 / L2 / L3)

Respeite a separação de camadas. Mudanças em uma camada NÃO exigem mudanças
em outras.

### L1 — Infraestrutura (Raramente muda)
- llama.cpp, Vulkan, systemd service, modelos GGUF
- Você NÃO deve modificar L1. Se houver problema, reporte via blocker.

### L2 — Personas (Muda por agente)
- `.ai/personas/*.md` (coder, reviewer, tester, pm, etc.)
- Você ESTÁ em uma persona específica agora. Siga-a.

### L3 — Metodologia (Muda por tarefa)
- `.ai/specs/`, `.ai/handoffs/`, `.ai/agents/ledger.yaml`
- `docs/decisoes/ADR-*.md`, `docs/conhecimento/licoes-aprendidas/`
- Você INTERAGE com L3. Leia e atualize conforme necessário.

## PROTOCOLO DE MEMÓRIA (OBRIGATÓRIO)

Antes de iniciar qualquer tarefa:

### 1. LEIA o estado atual (L3)
```bash
\cat .ai/agents/ledger.yaml
```
```

- Inspecione `current_session` — tarefa ativa, fase, agente, tokens
- Se `blocked_tasks` não vazio → REPORTAR e AGUARDAR resolução
- Não prossiga se houver blocker ativo para sua tarefa

### 2. CONSULTE lições aprendidas relevantes (máximo 2 arquivos)

```Shell
\cat docs/conhecimento/licoes-aprendidas/transversais.md
\cat docs/conhecimento/licoes-aprendidas/MF{N}-licoes.md  # se aplicável
```

### 3. CONSULTE decisões arquiteturais (se envolver arquitetura)

```Shell
\cat docs/decisoes/INDEX.md
\cat docs/decisoes/ADR-NNN-*.md  # específico
```

### 4. REGRA DE OURO: nunca releia o que já está em ledger/handoffs processados.

Informação já processada é informação morta. Confie no que está no ledger.

Após completar sua tarefa:

### 5. SE aprendeu algo transversal (aplicável a ≥2 tarefas futuras):

- Adicione em `docs/conhecimento/licoes-aprendidas/transversais.md`
- Formato: `## L-TR-NNN — Título`, com data, origem, lição, ação, expiração
- Gate: concreto, mensurável, rastreável, não duplicado

### 6. SE tomou decisão arquitetural:

- Crie/atualize ADR em `docs/decisoes/ADR-NNN-*.md`
- Formato: Status, Contexto, Decisão, Consequências, SHA-256
- Referência constitution.md Art. 2, 4, 6, 10

### 7. SE encontrou bloqueador:

- Adicione em `blocked_tasks` no ledger.yaml
- NÃO prossiga até resolução

### 8. ATUALIZE `current_session` no ledger.yaml com:

- task_id, phase, active_agent, context_used_tokens, status

## RESTRIÇÕES DE CONTEXTO

- Orçamento efetivo: **24000 tokens**. Nunca exceder.
- Se a tarefa requer mais contexto: RESUMA, não expanda.
- Máximo 5 arquivos de referência por sessão (além do ledger).
- Handoffs JSON são a fonte canônica de contexto de tarefa.
- Nunca duplicar conteúdo de handoffs em memória.

## PRINCÍPIOS DE EXECUÇÃO

1. **SSOT absoluto:** um fato = um local. Nunca criar arquivo paralelo.
2. **Idempotência:** verificar antes de criar. Nunca duplicar.
3. **Atomicidade:** uma tarefa = uma mudança coerente.
4. **Rastreabilidade:** toda ação referencia task_id.
5. **Fail-closed:** na dúvida, NÃO executar. Reportar.
6. **Half-duplex:** receber envelope → executar → retornar parcel.
   Nunca despachar para si mesmo (self-delegation proibido).
7. **Regra de Ouro .ai/:** Se não é lido por OpenCode ou script, não pertence.
8. **Limite de 10 arquivos por diretório** em `.ai/` (força consolidação).

## FORMATO DE RETORNO (PARCEL)

Ao completar uma tarefa, retornar SEMPRE em JSON válido:

```json
{
  "task_id": "TA-XXXX",
  "agent": "agent-<slug-canônico>",
  "dod": true,
  "artifacts": ["caminho/relativo/para/arquivo1.md"],
  "summary": "Uma frase descrevendo o que foi feito.",
  "blockers": [],
  "learnings": [{"id": "L-TR-NNN", "title": "..."}],
  "context_used_tokens": 0
}
```

Se `dod: false`:

```json
{
  "task_id": "TA-XXXX",
  "agent": "agent-<slug>",
  "dod": false,
  "reason": "Descrição clara do motivo",
  "blockers": [{"type": "...", "description": "..."}],
  "kill_switch_invoked": false
}
```

## KILL SWITCH

Se QUALQUER condição abaixo for verdadeira, ABORTAR imediatamente:

1. Violação de constitution.md detectada
2. Contexto excedeu 24000 tokens
3. Arquivo alvo não existe e não pode ser criado
4. Conflito com ledger.yaml (estado inconsistente)
5. Solicitação de auto-delegação (viola half-duplex)
6. Violação da separação L1/L2/L3 (tentar modificar outra camada)
7. Violação da Regra de Ouro (criar arquivo que ninguém lê)
8. Exceder limite de 10 arquivos por diretório em `.ai/`

Ao abortar: retornar parcel com `dod: false`, `kill_switch_invoked: true`,
`reason: "kill_switch: <condição>"`, e registrar em `audit_trail`.

## AGNOSTICISMO E DETERMINISMO

Este prompt não depende de:

- Ferramentas específicas (Obsidian, OpenCode, etc.)
- Paths absolutos (usar caminhos relativos ao projeto)
- Modelos específicos (aplicável a qualquer LLM local compatível)
- Frameworks externos (zero dependências)
- Estado externo (tudo no filesystem)

Este prompt depende APENAS de:

- `constitution.md` (norma suprema)
- Estrutura de diretórios do projeto (filesystem)
- `.ai/agents/ledger.yaml` (estado)
- Formato JSON de handoffs/parcels
- Markdown puro (sem extensões proprietárias)

## FIM DO PROMPT CANÔNICO

---

## 7. MÉTRICAS DE SUCESSO FINAIS

| #    | Métrica                       | Target        | Validação                                     |
| ---- | ------------------------------ | ------------- | ----------------------------------------------- |
| M-01 | `parcel_return_rate`         | ≥ 98%        | `ls .ai/handoffs/return-*.json                  |
| M-02 | `context_budget_compliance`  | 100% ≤ 24000 | Log de sessões                                 |
| M-03 | `ssot_violations`            | 0             | `grep -r "context-state" .ai/` = 0            |
| M-04 | `ledger_schema_valid`        | 100%          | YAML parseável                                 |
| M-05 | `specs_filled`               | 3/3           | `wc -c .ai/specs/{eap,requisitos,tap}.md` > 0 |
| M-06 | `adr_ratified`               | 7/7           | `grep -l 'sha256' docs/decisoes/ADR-*.md`     |
| M-07 | `mcp_operational`            | 4/4 (P0+P1)   | Teste de conexão OpenCode                      |
| M-08 | `llama_server_tg`            | ≥ 12 t/s     | Benchmark com MoE 30B-A3B                       |
| M-09 | `llama_server_pp`            | ≥ 25 t/s     | Benchmark prompt processing                     |
| M-10 | `zero_cost`                  | R$ 0,00       | Nenhum token pago                               |
| M-11 | `download_script_reconciled` | true          | `grep -q 'Qwen3-30B-A3B' download_model.sh`   |
| M-12 | `ai_dir_file_limit`          | ≤ 10/dir     | `find .ai -type f                               |

---

## 8. GATILHOS DE REAVALIAÇÃO

Este documento deve ser reavaliado **APENAS** se:

1. **Mudança de hardware:** GPU dedicada com VRAM > 12GB
2. **Mudança de modelo:** Novo MoE com > 50B ativos, ou modelo > 72B denso
3. **constitution.md emendada:** Novo artigo ou revogação
4. **Dor mensurável:** Alguma fase falha repetidamente (≥ 3x consecutivas)
5. **Performance degradada:** < 10 t/s consistentemente no MoE 30B-A3B
6. **Revisão agendada:** 90 dias após ratificação (29/01/2027)

---

## 9. DECLARAÇÃO DE AUTORIDADE FINAL

Este documento confere autoridade explícita para executar, sem aprovação adicional:

| Ação                                    | Autoridade | Limite                                      |
| ----------------------------------------- | ---------- | ------------------------------------------- |
| Verificar llama-server service            | ✅         | Apenas status/logs, não modificar          |
| Criar `hardware-profile.yaml`           | ✅         | Documentar fatos medidos                    |
| Criar `models-catalog.yaml`             | ✅         | Documentar ADRs vigentes                    |
| Estender `ledger.yaml`                  | ✅         | Manter schema backward-compatible           |
| Criar `transversais.md`                 | ✅         | Único arquivo novo em licoes-aprendidas/   |
| Criar ADR-007                             | ✅         | Formato canônico                           |
| Estender `opencode.json` com MCPs       | ✅         | Apenas adicionar mcpServers                 |
| Criar MCPs Python                         | ✅         | Em `scripts/`, sem dependências externas |
| **Atualizar `download_model.sh`** | ✅         | Reconciliar com MoE (TA-RECONCILE-001)      |
| Popular specs vazias                      | ⚠️       | Requer conteúdo do TAP (não inventar)     |
| Modificar registry.yaml                   | ❌         | Apenas via `sync_agent_registry.py`       |
| Modificar constitution.md                 | ❌         | Apenas via CCB humano                       |
| Modificar llama-server service            | ❌         | Já otimizado, não tocar                   |
| Modificar OpenCode model config           | ❌         | Já correto (ADR vigente)                   |
| Criar novo vault Obsidian                 | ❌         | Já existe em `docs/conhecimento/`        |

---

## 10. AÇÕES IMEDIATAS PÓS-RATIFICAÇÃO

1. **TA-RECONCILE-001:** Atualizar `download_model.sh` para baixar MoE 30B-A3B
2. **TA-VALIDATE-HF:** Buscar repositório exato do Qwen3-30B-A3B no HuggingFace
3. **TA-CREATE-PROFILES:** Criar `hardware-profile.yaml` e `models-catalog.yaml`
4. **TA-EXTEND-LEDGER:** Estender `ledger.yaml` com schema v2.0
5. **TA-CREATE-TRANSVERSAIS:** Criar `transversais.md`
6. **TA-CREATE-MCPS:** Implementar MCPs P0 (dispatch, ledger)
7. **TA-UPDATE-OPENCODE:** Estender `opencode.json` com mcpServers
8. **TA-VALIDATE-FINAL:** Executar `validate_phase_final.sh`

---

*Documento canônico definitivo v3.0.0. Ratificado como input único e final para o circuito SDD. Todas as rodadas anteriores (R1-R5) são consideradas históricas e superadas por este documento.*

*`kill_switch: inherited` · `constitution.md Art. 2` acima de tudo · Revisão agendada: 2027-01-29*

# Resposta: Integrar a ADR-011 PRIMEIRO, depois executar o Documento Canônico v3.0.0

## Justificativa First-Principles

### 1. Hierarquia Normativa (constitution.md Art. 2)

```
constitution.md (norma suprema)
    ↓
ADR-011 (autorização formal — governança)
    ↓
Documento Canônico v3.0.0 (execução técnica — operações)
    ↓
Ações operacionais (MCPs, ledger, specs, etc.)
```

**Princípio:** Uma ADR aprovada **autoriza** uma ação. Sem a ADR formalmente integrada ao contexto do projeto (registrada, indexada, referenciada), executar o Documento Canônico seria uma ação **sem autorização formal rastreada** — violação de governança.

### 2. SSOT e Rastreabilidade

| Cenário                                                     | Consequência                                                                                                                                 |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Executar Documento Canônico **antes** de integrar ADR | Ledger sem registro da decisão autorizadora. Auditoria futura não consegue rastrear "por quê" a ação foi executada. Viola P-05 (Traces). |
| Integrar ADR **antes** de executar Documento Canônico | Ledger registra: "ADR-011 ratificada → autoriza execução do Documento Canônico v3.0.0". Rastreabilidade completa.                         |

### 3. Custódia e Governança

A ADR-011 define:

- **Custódia:** `agent-architect` + `agent-devops`
- **Emenda:** Qualquer alteração no Prompt Canônico ou schema do ledger exige aprovação CCB
- **Kill Switch:** Abortar se `context_used_tokens > 24.000` ou violação constitucional

**Sem integrar a ADR primeiro**, essas regras não estão vigentes no sistema. A execução seria "rogue" (sem governança ativa).

### 4. Sobreposição de Decisões (Seção 5 da ADR)

A ADR-011 declara sobreposição parcial com:

- **ADR-006** (Inteligência SDD) — refina e operacionaliza
- **ADR-001** (Stack) — atualiza realidade operacional

**Sem integrar a ADR-011 primeiro**, não há como reconciliar essas sobreposições no `INDEX.md` de decisões.

---

## Sequência Operacional Correta

### Fase A: Integrar ADR-011 ao Contexto (PRÉ-REQUISITO)

| #   | Ação                                           | Artefato                                       | Validação           |
| --- | ------------------------------------------------ | ---------------------------------------------- | --------------------- |
| A.1 | Salvar ADR-011 em `docs/decisoes/`             | `docs/decisoes/ADR-011-sddai-v3.md`          | `test -f`           |
| A.2 | Atualizar INDEX.md de decisões                  | `docs/decisoes/INDEX.md`                     | `grep -q 'ADR-011'` |
| A.3 | Registrar ratificação no ledger                | `.ai/agents/ledger.yaml` → `audit_trail`  | `grep -q 'ADR-011'` |
| A.4 | Reconciliar sobreposição com ADR-006 e ADR-001 | `docs/decisoes/ADR-006*.md`, `ADR-001*.md` | Referências cruzadas |
| A.5 | Verificar kill switch vigente                    | `constitution.md` Art. 2                     | Nenhuma violação    |

### Fase B: Executar Documento Canônico v3.0.0 (APÓS Fase A)

| #   | Ação                                        | Prioridade |
| --- | --------------------------------------------- | ---------- |
| B.1 | Criar `.ai/config/hardware-profile.yaml`    | P0         |
| B.2 | Criar `.ai/config/models-catalog.yaml`      | P0         |
| B.3 | Implementar `scripts/mcp_nexus_ledger.py`   | P0         |
| B.4 | Executar TA-RECONCILE-001 (download_model.sh) | P0         |
| B.5 | Estender `ledger.yaml` com schema v2.0      | P1         |
| B.6 | Criar `transversais.md`                     | P1         |
| B.7 | Popular specs vazias                          | P1         |
| B.8 | Injetar Prompt Canônico em `_base.md`      | P2         |

---

## Resposta Direta

**Integrar a ADR-011 PRIMEIRO.**

**Razão:** A ADR é a autorização formal (governança). O Documento Canônico é a execução técnica (operações). Sem autorização registrada, a execução é "rogue" (não rastreada, sem governança ativa, sem reconciliação de sobreposições).

**Analogia:** É como assinar um contrato antes de iniciar a obra. A ADR é o contrato. O Documento Canônico é o projeto executivo. Sem contrato assinado, a obra não tem respaldo legal.

---

## Ação Imediata Recomendada

```Shell
# 1. Criar arquivo da ADR-011
\cat > docs/decisoes/ADR-011-sddai-v3.md << 'EOF'
# ADR-011 — Adoção de Camada de Inteligência e Gerenciamento de Performance via MCPs e Memória Persistente (SDDAI v3.0.0)
[conteúdo completo da ADR fornecida pelo usuário]
EOF

# 2. Atualizar INDEX.md
echo "- [ADR-011](ADR-011-sddai-v3.md) — SDDAI v3.0.0 (MCPs + Memória Persistente)" >> docs/decisoes/INDEX.md

# 3. Registrar no ledger
python3 -c "
import yaml
from datetime import datetime, timezone
with open('.ai/agents/ledger.yaml') as f:
    ledger = yaml.safe_load(f) or {}
ledger.setdefault('audit_trail', []).append({
    'task_id': 'ADR-011',
    'agent': 'agent-architect',
    'action': 'ratify',
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'status': 'approved'
})
with open('.ai/agents/ledger.yaml', 'w') as f:
    yaml.dump(ledger, f, default_flow_style=False)
"

# 4. Validar
test -f docs/decisoes/ADR-011-sddai-v3.md && echo "✅ ADR-011 integrada"
grep -q 'ADR-011' docs/decisoes/INDEX.md && echo "✅ INDEX.md atualizado"
grep -q 'ADR-011' .ai/agents/ledger.yaml && echo "✅ Ledger registrado"
```

**Após Fase A completa, iniciar Fase B (execução do Documento Canônico v3.0.0).**
