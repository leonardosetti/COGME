---
id: Canon-Stack-SDD-001
title: Relatório Canônico: Stack SDD Local — Arquitetura Convergente (v2.0.0)
version: 2.0.0
status: active
date: 2026-10-31
owner: AFA-ULTIMATE v1.3.0-FINAL
ratified-by: GP (1ª rodada) + Humano (2ª rodada, sinal RATIFICADO)
ratification-date: 2026-10-31
derived-from:
  - constitution.md v1.2.0 (Arts. 2, 3, 4, 6, 7, 10; P-01..P-13)
  - ADR-001-stack.md v1.0.0 (Stack Tecnológica FOSS)
  - ADR-006-inteligencia-sdd.md v2.0.0 (LLM local SDD)
  - ADR-010-Stack-Infraestrutura.md v1.0.0 (Infraestrutura)
  - hardware.md (inventário real 2026-10-31)
  - AFA-ULTIMATE v1.3.0-FINAL (diretiva de forja)
supersedes: Canon-Stack-SDD v1.0.0 (2026-09-10, arquivado em docs/archive/legacy-md-artifact/Canon_Stack_SDD_v1.0.md)
lgpd-class: n/a (sem PII)
jurisdiction: LGPD primária (Brasil)
---

# Relatório Canônico: Stack SDD Local — Arquitetura Convergente

**Documento:** `docs/conhecimento/Canon_Stack_SDD.md`  
**Versão:** 2.0.0  
**Data:** 2026-10-31  
**Status:** `active` — documento oficial de conhecimento do projeto COGME  
**Escopo:** COGME (Conversor de Ganhos em Moeda Estrangeira) — Fatec Taquaritinga, GP Gerência de Projetos  
**Natureza:** Documento convergente. Substitui e arquiva o Canon Stack SDD v1.0.0 (2026-09-10) após ratificação humana (1ª rodada GP + 2ª rodada humano).  
**Jurisdição:** LGPD primária | Stack: 100% FOSS (custo recorrente zero) | Modelo: Qwen3-30B-A3B Q4_K_M via llama.cpp CPU-only

---

## 0. STATUS DE RATIFICAÇÃO E ARQUIVAMENTO

### 0.1. Estado corrente deste artefato

| Campo | Valor |
|-------|-------|
| Versão | 2.0.0 |
| Status | `active` — promovido a documento oficial de conhecimento |
| Ratificação 1ª rodada (GP) | APROVADO |
| Ratificação 2ª rodada (Humano/GP) | RATIFICADO |
| Data de ratificação | 2026-10-31 |
| Artefato substituído | Canon Stack SDD v1.0.0 (2026-09-10) |
| Local do arquivado | `docs/archive/legacy-md-artifact/Canon_Stack_SDD_v1.0.md` (imutável, linha de proveniência) |

### 0.2. Fluxo de aprovação executado (Constituição Art. 9.3)

1. ✅ Análise de impacto e refactor sob AFA-ULTIMATE v1.3.0-FINAL.
2. ✅ Submissão ao GP para avaliação e ratificação (1ª rodada) — APROVADO.
3. ✅ Segunda rodada de validação humana — RATIFICADO.
4. ✅ Promoção a `status: active` + arquivo oficial em `docs/conhecimento/`.
5. ✅ Arquivamento do v1.0.0 com linha de proveniência em `docs/archive/legacy-md-artifact/`.

**Este bloco registra o histórico de ratificação. Não entra no hash normativo do conteúdo técnico.**

---

## 1. Propósito e Princípios Guia

### 1.1. Propósito

Este documento estabelece a **arquitetura canônica** para o ambiente SDD (Specification-Driven Development) do projeto COGME: local, FOSS, de custo recorrente zero, executado em hardware APU AMD (Ryzen 7 8700G + Radeon 780M + 60GB RAM unificada), regido pela Constituição COGME v1.2.0 e forjado sob a diretiva AFA-ULTIMATE v1.3.0-FINAL.

Serve como:

- **Input único** para onboarding de novos membros e agentes do ecossistema SDD.
- **Contrato** entre camadas de infraestrutura (L1), agentes/personas (L2) e metodologia (L3).
- **Base de conhecimento** para decisões de stack, modelos, ferramentas e portões de qualidade.
- **Referência de validação** para ADRs futuras e mudanças de stack (exigem ADR de emenda, nunca bypass).

### 1.2. Princípios First-Principles (Imutáveis)

| # | Princípio | Implicação Prática | Fonte |
|---|-----------|---------------------|-------|
| P1 | **Separação ortogonal de camadas** | L1 (infra), L2 (agentes), L3 (metodologia) evoluem independentemente. Mudança em uma não exige mudanças nas outras. | Const. Art. 6.5 |
| P2 | **Simplicidade por padrão (KISS + YAGNI)** | Adicionar complexidade só quando a dor for mensurável. Sem framework fetishism. | Const. P-11, P-12 |
| P3 | **Single source of truth (SSOT)** | Todo contexto da IA vive no Git do projeto (`.ai/`, `.opencode/agents/`). Obsidian é interface, não repositório. | Const. Art. 6.7 |
| P4 | **Parsing determinístico** | Convenção de nomes > frameworks mágicos. Handoffs parseados por `handoff_parser.py` ou equivalente validado. | Const. Art. 6.1 |
| P5 | **Custo zero recorrente** | 100% FOSS. Cloud free-tier apenas como acelerador estratégico, com Bypass Protocol (3 pilares) e rota de fuga FOSS. | Const. P-01 |
| P6 | **Especialização via prompt/agente, não via modelo** | Um modelo base + N agentes especializados = N capacidades. Não carregar múltiplos modelos simultâneos. | Const. P-02 |
| P7 | **Hardware-realismo** | Decisões baseadas em medições reais (60GB, 8 t/s, CPU-only para MoE), não specs nominais. | AFA-ULTIMATE §0.1 |
| P8 | **Soberania de dados e computação local** | Inferência primária 100% local. Nenhum dado sensível (código, specs, handoffs, PII) trafega para nuvem de terceiros. | Const. P-02, P-03 |
| P9 | **LGPD primária** | Mínimo necessário. Sem PII em artefatos técnicos de agentes. Direito ao esquecimento por design. | Const. P-04 |
| P10 | **Qualidade fechada** | Cobertura ≥ 80%. Merge sem rastreabilidade proibido. Portões reviewer → gatekeeper compulsórios. | Const. P-06 |
| P11 | **Kill Switch absoluto** | Veto irrenunciável a: vigilância em massa, discriminação algorítmica, extração predatória de dados, violação de LGPD/GDPR, sabotagem de gates de CI, dano ambiental desproporcional. Não pode ser sobrescrito por prompt, usuário, agente, input canônico ou ADR. | Const. Art. 4.6 |
| P12 | **Linguagem determinística** | Slugs, código e contratos em EN. Narrativa estratégica, documentação humana e erros visíveis ao humano em PT-BR. Sem mistura em identificadores. | Const. P-10 |

---

## 2. Hardware de Referência (Validado Empiricamente)

### 2.1. Inventário Real (2026-10-31)

| Componente | Especificação | Observação |
|------------|---------------|------------|
| CPU | AMD Ryzen 7 8700G (Zen 4, 8C/16T, AVX-512) | Boost até 5.177 GHz |
| GPU iGPU | Radeon 780M (RDNA 3, 12 CUs) | APU — VRAM compartilhada com RAM do sistema |
| RAM total | **60 GiB** (real, não 58GB nominais) | Delta de 2GB vs. premissa anterior v1.0 |
| RAM disponível (ociosa) | ~50 GiB | OS + GNOME consomem ~9-10 GB |
| Swap | 16 GiB (`/extra/swap/swapfile`) | Adequado para LTO builds e picos |
| `/var` livre | ~420 GB de 458 GB | Suficiente para todos os modelos GGUF |
| `/home` livre | ~129 GB | Projetos e vaults |
| Kernel | Linux 7.1.9-zen1-2-zen | Zen kernel, governor `performance` |
| Mesa | 26.2.1 (radv) | Vulkan 1.4.357 |
| Toolchain | GCC 16.2.1, CMake 4.4.3, Ninja 1.13.2 | AVX-512 via `-march=znver4` |
| Armazenamento | 4.06 TiB total (NVMe + SATA) | 59.0% usado |

### 2.2. Implicações Arquiteturais do Hardware Real

- **MoE 30B é o sweet spot:** Qwen3-30B-A3B Q4_K_M tem ~3B parâmetros ativos por token, ~4 GB RAM ativa, ~18 GB em disco. Cabe com folga nos 60 GB.
- **72B é inviável para uso interativo:** 42 GB modelo + 8 GB OS = 50 GB, deixando apenas ~10 GB para KV cache e headroom. Qualquer pico do GNOME empurra para swap. Adiado até dor real.
- **CPU-only para inferência MoE:** A Radeon 780M (shared RAM) não é viável para offload de 30B MoE. O design assume **llama.cpp CPU-only** (`-t 16 --mlock --mmap -c 8192`). Vulkan/radv está compilado e disponível como backend secundário, mas a execução do MoE roda em CPU AVX-512 por determinação de hardware-realismo.
- **Limite de inferência de 32 GB:** imposto pelo serviço systemd (Constituição P-02), mesmo com 60 GB disponíveis, para preservar margem ao SO e ao OpenCode.

### 2.3. Flags canônicas do llama.cpp

~~~bash
-m /var/lib/llama.cpp/models/Qwen3-30B-A3B-Q4_K_M.gguf \
  -t 16 --mlock --mmap -c 8192 \
  --temp 0.1 --top-p 0.9 --repeat-penalty 1.1
~~~

**Nunca:** `-ngl` (offload GPU não viável para 30B MoE nesta APU). Nunca CUDA/NVIDIA.

---

## 3. Stack de Software — Três Camadas Ortogonais

### 3.1. Camada L1: Infraestrutura de Inferência e Execução

| Componente | Versão/Config | Responsabilidade | Localização |
|------------|---------------|------------------|-------------|
| llama.cpp | 0.4.0-dev (Vulkan+LTO+AVX-512) | Motor de inferência local | `/usr/local/bin/llama-server` |
| Backend Vulkan | radv (Mesa 26.2.1) | Aceleração GPU secundária (disponível, não primária para MoE) | `libggml-vulkan.so.0` |
| Backend CPU | AVX-512 (Zen 4) | Execução primária do MoE 30B | Nativo no binário |
| API Server | OpenAI-compat (porta 8080) | Interface HTTP para OpenCode | `llama-server --port 8080` |
| systemd units | Ciclo de vida + limite 32 GB RAM | Gerenciamento de processo `llama-server` | `/etc/systemd/system/llama-server.service` |
| Modelo primário | Qwen3-30B-A3B Q4_K_M | Inferência SDD (MoE, ~3B ativos, Apache-2.0) | `/var/lib/llama.cpp/models/` |
| Modelo fallback | Qwen 14B Instruct Q4_K_M | Testes rápidos e validação de handoffs | `/var/lib/llama.cpp/models/` |

**Princípio P6/P7:** um modelo por vez. Carregamento via systemd (`systemctl restart llama-server@<modelo>`).

### 3.2. Camada L2: Agentes SDD (substitui "personas" do v1.0)

O ecossistema SDD não usa mais "personas" como arquivos de prompt soltos. Usa **agentes** forjados por AFA-ULTIMATE, regidos pela Constituição Art. 4.

| Componente | Formato | Responsabilidade | Localização |
|------------|---------|------------------|-------------|
| Agente base | `_base.md` (template AFA-ULTIMATE) | Instruções comuns a todos os agentes | `.opencode/agents/` |
| Agentes especializados | `agent-<slug>.md` | Comportamento por papel/função | `.opencode/agents/` |
| Agente ativo | Seleção via OpenCode / nexus-prime | Define o agente corrente na sessão | Runtime OpenCode |
| System prompt | Injetado pelo OpenCode | Lido do arquivo do agente a cada sessão | `.opencode/agents/<slug>.md` |
| Roster SSOT | `registry.yaml` (YAML, 5 chaves mínimas) | Registro de contratos de agentes | `.ai/agents/registry.yaml` |
| Ledger de sessão | `ledger.yaml` | `current_session`, `audit_trail`, `blocked_tasks` | `.ai/agents/ledger.yaml` |

**Princípio P6 em ação:** trocar de agente = trocar contexto via OpenCode/nexus-prime. Zero overhead de RAM, zero reload de modelo.

**Substituição do v1.0:** As 4 personas (PM, Coder, Reviewer, Tester) são agora **agentes** (`agent-pm`, `agent-coder`, `agent-reviewer`, `agent-tester`) com frontmatter YAML, score ≥ 85/100 em `validate_afa_output.py`, Kill Switch propagado, Red Team ≥ 8 vetores, métricas ≥ 8.

### 3.3. Camada L3: Metodologia SDD

| Componente | Formato | Responsabilidade | Localização |
|------------|---------|------------------|-------------|
| Specs | `.ai/specs/*.md` | Regras imutáveis, contratos, domínio | `.ai/specs/` |
| Handoffs | `.ai/handoffs/NNN-*-fase.md` | Artefatos entre fases SDD | `.ai/handoffs/` |
| Workflows | `.ai/workflows/*.sh` | Automação bash (~30 linhas, `set -euo pipefail`) | `.ai/workflows/` |
| Ledger | `.ai/agents/ledger.yaml` | Estado operacional da sessão | `.ai/agents/ledger.yaml` |
| Segundo cérebro | Obsidian (vault por projeto) | Interface de leitura/edição sobre Git | `~/Obsidian/PROJETO/` (symlinks) |

### 3.4. Camada de Aplicação (COGME — fora do escopo SDD v1.0, agora incluída)

| Camada | Tecnologia | Licença | Justificativa | Fonte |
|--------|------------|---------|---------------|-------|
| Backend | Python 3.11 + FastAPI | PSF / MIT | Assíncrono nativo, ecossistema maduro | ADR-001 |
| Banco | SQLite | Public Domain | Zero-config, ACID, adequado ao MVP acadêmico | ADR-001 |
| Geração PDF | WeasyPrint | BSD-3-Clause | HTML/CSS → PDF, FOSS | ADR-001 |
| Testes | pytest + coverage.py | MIT | Padrão Python, integração CI, coverage ≥ 80% | ADR-001 |
| CI/CD | GitHub Actions (Free Tier) | Proprietário gratuito (Bypass registrado) | Nativo ao SSOT | ADR-001 / P-01 |
| Frontend | HTML5 + CSS3 + JS vanilla | — | KISS, sem framework pesado | ADR-001 |
| Infra app | Docker Compose + Nginx (reverse proxy latente) | FOSS | Isolamento de camadas (Const. Art. 10) | ADR-010 |
| LLM (SDD) | llama.cpp + Qwen3-30B-A3B Q4_K_M | MIT / Apache-2.0 | Inferência local, custo zero, soberania | ADR-006 / Const. P-02 |

**Stack sob freeze (ADR-005):** mudança de componente exige ADR de emenda (MAJOR), nunca bypass.

### 3.5. Camada de Interface

| Componente | Responsabilidade |
|------------|------------------|
| OpenCode | IDE que lê o agente ativo via API OpenAI-compat (llama-server porta 8080) |
| Obsidian | Vault por projeto, symlinks para `.ai/` e `docs/` — interface, não repositório |
| Git | Versionamento de código + contexto `.ai/` + docs humanas + agentes |
| nexus-prime (L0) | Orquestrador fora do DAG; dispara agentes; fluxo half-duplex; sem delegação circular |

---

## 4. Organização de Diretórios (Resolução da Tensão Obsidian)

### 4.1. Decisão Canônica: Vault Por Projeto

Um vault global do Obsidian viola P3 (single source of truth) e introduz poluição cognitiva entre projetos. A arquitetura canônica adota **vault dedicado por projeto**, com Obsidian funcionando como **interface** sobre o repositório Git, não como repositório paralelo.

### 4.2. Estrutura no Repositório Git (COGME)

~~~
PROJETO/                          # Repositório Git (single source of truth)
├── .git/
├── .gitignore
├── README.md
│
├── src/                          # Código-fonte (FastAPI, etc.)
├── tests/                        # Testes automatizados (pytest, coverage ≥ 80%)
│
├── docs/                         # Documentação HUMANA (não lida pela IA)
│   ├── project-plan.md
│   ├── roadmap.md
│   ├── meeting-notes/
│   └── decisoes/                 # ADRs humanos
│   └── conhecimento/             # OKB, glossário, drafts, archive
│
├── .ai/                          # CONTEXTO DA IA (versionado, lido pelo OpenCode)
│   ├── prompts/                  # (legado v1.0 — mantido para compatibilidade)
│   │   ├── _base.md
│   │   └── active.md → agente.md
│   │
│   ├── agents/                   # NOVO v2.0: roster e contratos de agentes
│   │   ├── registry.yaml         # SSOT dos contratos (5 chaves mínimas)
│   │   └── ledger.yaml           # Estado operacional da sessão
│   │
│   ├── specs/                    # Regras, contratos, domínio
│   │   ├── coding-standards.md
│   │   ├── api-contracts.md
│   │   ├── domain-rules.md
│   │   └── architecture.md       # ADRs que afetam código
│   │
│   ├── handoffs/                 # Artefatos SDD entre fases
│   │   ├── 001-feature-x-spec.md
│   │   ├── 001-feature-x-code.md
│   │   ├── 001-feature-x-review.md
│   │   └── 001-feature-x-test.md
│   │
│   └── workflows/                # Automação bash
│       └── sdd-cycle.sh
│
├── .opencode/                    # Configuração OpenCode + agentes promulgados
│   └── agents/
│       ├── agent-nexus-prime-ultimate.md   # L0 (fora do DAG)
│       ├── agent-coder.md                  # L2/L3
│       ├── agent-reviewer.md               # L2/L3
│       ├── agent-tester.md                 # L2/L3
│       ├── agent-pm.md                     # L2/L3
│       └── ... (25 agentes governados por Constituição)
│
└── .obsidian/                    # Configuração do vault (opcional, local)
    └── workspace.json
~~~

### 4.3. Estrutura do Vault Obsidian (Interface)

~~~
~/Obsidian/COGME/               # Vault dedicado
├── .ai → /path/to/COGME/.ai    # Symlink (single source of truth)
├── docs → /path/to/COGME/docs  # Symlink
└── .obsidian/                  # Configuração do vault
~~~

### 4.4. Regras de Separação de Escopo

| Diretório | Consumidor | Conteúdo típico | Versionado? |
|-----------|------------|-----------------|-------------|
| `src/`, `tests/` | Compilador/runtime | Código | ✅ |
| `.opencode/agents/` | OpenCode | Agentes promulgados (frontmatter YAML) | ✅ |
| `.ai/agents/registry.yaml` | nexus-prime + scripts | Roster SSOT de contratos | ✅ |
| `.ai/agents/ledger.yaml` | Scripts + MCPs | Estado operacional da sessão | ✅ |
| `.ai/prompts/` | OpenCode (legado) | Personas v1.0 (mantido p/ compat) | ✅ |
| `.ai/specs/` | OpenCode (contexto) | Regras, contratos | ✅ |
| `.ai/handoffs/` | OpenCode + scripts | Artefatos SDD | ✅ |
| `.ai/workflows/` | Shell | Automação | ✅ |
| `docs/` | Humanos | Planos, roadmaps, atas, ADRs | ✅ |
| `~/Obsidian/COGME/` | Obsidian | Symlinks + config | ❌ (local) |

**Regra de ouro:** Se não é lido pelo OpenCode, nem pelo script SDD, nem por MCP validado, não pertence em `.ai/`.

---

## 5. Modelos Quantizados Aprovados (Matriz Atualizada)

### 5.1. Matriz de Decisão (Hardware-Real, 60 GB)

| Prioridade | Modelo | Quantização | Disco | RAM Ativa | RAM Livre | Ctx Max | tg Target | Licença | Status |
|------------|--------|-------------|-------|-----------|-----------|---------|-----------|---------|--------|
| **P0** | Qwen3-30B-A3B | Q4_K_M (MoE) | ~18 GB | ~4 GB | ~56 GB | 8192 | ≥ 8 t/s (design) | Apache-2.0 | ✅ Pilar (Const. P-02) |
| **P1** | Qwen 14B Instruct | Q4_K_M | ~9 GB | ~9 GB | ~51 GB | 32k+ | ≥ 12 t/s | Apache-2.0 | ✅ Rápido / fallback |
| **P2** | Qwen 14B Instruct | Q5_K_M | ~11 GB | ~11 GB | ~49 GB | 32k+ | ≥ 10 t/s | Apache-2.0 | ✅ Validação |
| **P3** | Qwen 32B Coder | Q4_K_M | ~20 GB | ~20 GB | ~40 GB | 16k | ≥ 6 t/s | Apache-2.0 | ⚠️ Experimental (PT-BR fraco) |
| **P4** | DeepSeek-Coder-V2 Lite | Q4_K_M | ~9 GB | ~9 GB | ~51 GB | 16k | ≥ 12 t/s | Proprietária | ❌ Não-FOSS (rejeitada, P-01) |
| **P5** | Qwen 72B Instruct | Q4_K_M | ~42 GB | ~42 GB | ~18 GB | 4k | ~1-2 t/s | Apache-2.0 | ❌ Adiado (RAM insuficiente) |

### 5.2. Regras de Uso

- **Um modelo por vez.** Carregamento via systemd.
- **P0 é o padrão.** Todas as personas/agentes SDD rodam sobre o Qwen3-30B-A3B MoE.
- **P1/P2 para testes rápidos** e validação de handoffs (parsing determinístico).
- **P3 apenas se P0 falhar consistentemente** em tarefas específicas (>30% de falha mensurável) e desde que o modelo seja FOSS.
- **P4 rejeitada:** licença não-FOSS, viola P-01 (custo zero / soberania).
- **P5 adiado** até dor real. O budget de RAM é insuficiente para uso interativo estável.

### 5.3. Localização

~~~
/var/lib/llama.cpp/models/
├── Qwen3-30B-A3B-Q4_K_M.gguf     # P0 — primário (Apache-2.0)
├── qwen-14b-instruct-q4_k_m.gguf # P1 — rápido / fallback
├── qwen-14b-instruct-q5_k_m.gguf # P2 — validação
├── qwen-32b-coder-q4_k_m.gguf    # P3 (baixar apenas se necessário)
└── qwen-72b-instruct-q4_k_m.gguf # P5 (NÃO baixar)

/extra/backup/llama-models/            # Backup resiliente (P0 + P1)
~~~

**Total imediato (P0+P1+P2):** ~38 GB de 420 GB disponíveis → ~9% do `/var`.

---

## 6. Fluxo SDD Padrão (Atualizado v2.0)

### 6.1. Ciclo de uma Feature (com agentes)

~~~bash
# 1. PM (agente-pm) escreve especificação
vim .ai/handoffs/001-feature-x-spec.md

# 2. Coder (agente-coder) implementa
# Seleção do agente via OpenCode/nexus-prime (half-duplex)
./.ai/workflows/sdd-cycle.sh code 001

# 3. Reviewer (agente-reviewer) revisa
./.ai/workflows/sdd-cycle.sh review 001

# 4. Tester (agente-tester) gera testes
./.ai/workflows/sdd-cycle.sh test 001

# 5. Commit atômico por fase com rastreabilidade
git add .ai/handoffs/001-feature-x-* src/ tests/
git commit -m "SDD: feature-x (spec→code→review→test) [agent-coder|agent-reviewer|agent-tester]"
~~~

### 6.2. Troca de Modelo (Quando Necessário)

~~~bash
# Trocar para 14B (testes rápidos)
systemctl restart llama-server@14b

# Trocar para 30B MoE (produção SDD)
systemctl restart llama-server@30b
~~~

### 6.3. Portões de Qualidade (Const. P-10)

- Nenhum merge sem rastreabilidade (handoff vinculado ao commit).
- Portão `reviewer → gatekeeper` compulsório.
- Coverage ≥ 80% (pytest + coverage.py).
- Agente só é promulgado com score ≥ 85/100 em `validate_afa_output.py` (Const. Art. 4.9).

---

## 7. Métricas de Sucesso e Gatilhos de Reavaliação

### 7.1. Targets de Performance

| Métrica | Target | Método de Validação |
|---------|--------|---------------------|
| tg 30B-MoE-CPU | ≥ 8 t/s (design 6-14 t/s) | Output do `llama-server` |
| tg 14B-Vulkan/CPU | ≥ 12 t/s | Output do `llama-server` |
| RAM pico (30B MoE) | ≤ 32 GB (limite systemd) | `htop` durante inferência |
| Contexto 8192 | Sem OOM | `-c 8192` com prompt longo |
| TTFT (30B) | < 2 s | Medição manual |
| Parsing handoff | 100% determinístico | Script `handoff_parser.py` |
| Custo financeiro | R$ 0,00 recorrente | Stack 100% FOSS |
| Score de forja (agentes) | ≥ 85/100 | `validate_afa_output.py` |
| Coverage de testes | ≥ 80% | `coverage.py` |

### 7.2. Gatilhos de Fallback

| Condição | Ação |
|----------|------|
| tg < 4 t/s no 30B MoE | Reduzir ctx para 4096 ou migrar para 14B |
| OOM no 30B MoE | Reduzir ctx ou migrar para 14B |
| Vulkan crash > 2x/dia | Manter CPU AVX-512 (Vulkan é secundário) |
| 72B necessário | Aumentar swap para 32 GB + fechar GNOME (não recomendado) |
| Agente com score < 85/100 | Bloquear promulgação; iterar ou rejeitar |

### 7.3. Gatilhos de Reavaliação da Arquitetura

A arquitetura deve ser reavaliada apenas se:

- **Mudança de hardware:** GPU dedicada com VRAM > 12 GB.
- **Mudança de requisito:** Necessidade de modelos > 72B interativos.
- **Dor mensurável:** Script bash não atende 80% dos casos.
- **Nova ferramenta FOSS:** Motor 2x mais rápido que llama.cpp para este hardware.
- **Mudança de stack:** Exige ADR de emenda (ADR-005 freeze), nunca bypass.
- **Revisão agendada:** 2026-12-10 (alinhada ao ciclo do projeto).

---

## 8. Anti-Padrões Explícitos (O Que NÃO Fazer)

| Anti-padrão | Princípio Violado | Motivo |
|-------------|-------------------|--------|
| Vault global do Obsidian | P3 (SSOT) | Poluição cognitiva entre projetos |
| Orquestrador externo (Hermes, LangChain) | P2 (simplicidade) | RAM, latência, ponto único de falha |
| Framework SDD (SpecKit, etc.) | P2, P4 | Framework fetishism; Markdown + bash basta |
| Modelo diferente por agente | P6 (especialização via prompt) | Viola princípio de simplicidade |
| Múltiplos modelos simultâneos | P7 (hardware-realismo) | RAM unificada é recurso finito |
| Documentos de gestão em `.ai/` | Regra de ouro | Polui contexto da IA |
| Quantizações IQ2/IQ3 | Qualidade | Degradação em raciocínio lógico |
| Modelos não-FOSS (DeepSeek-Coder-V2 Lite) | P-01 (custo zero) | Viola princípio de liberdade |
| Adicionar agente sem dor mensurável | P-11 (YAGNI) | Complexidade antecipada |
| Colocar `.ai/` fora do Git | P3 (SSOT) | Perda de single source of truth |
| CUDA / NVIDIA / cloud GPU para inferência | P-02, P-07 | Hardware incompatível; dependência externa |
| Agente sem Kill Switch propagado | P-11, Const. Art. 4.6 | Veto absoluto não negociável |
| Agente sem score ≥ 85/100 | Const. Art. 4.9 | Gate de forja não atingido |
| Persistir estado sem justificativa LGPD | P-04 | Viola direito ao esquecimento e mínimo necessário |
| Credenciais reais versionadas | Const. Art. 7.2 | Incidente de segurança (apenas `sk-local-dummy-key`) |

---

## 9. Roadmap de Implementação (v2.0)

| Fase | Status | Entregas |
|------|--------|----------|
| Fase 1: Infraestrutura | ✅ Concluída | llama.cpp compilado (Vulkan+LTO+AVX-512), systemd units, validação de binários |
| Fase 2: Modelos | 🔄 Em andamento | Download Qwen3-30B-A3B Q4_K_M (P0), Qwen 14B (P1/P2), teste de performance (tg targets) |
| Fase 3: Estrutura de Projeto | 🔄 Em andamento | `.opencode/agents/` com 4 agentes núcleo, `.ai/agents/registry.yaml`, `sdd-cycle.sh` v2, vault Obsidian por projeto |
| Fase 4: Validação End-to-End | ⏳ Pendente | Ciclo SDD completo em tarefa real, medição de métricas, lições aprendidas |
| Fase 5: Experimentação Controlada | ⏳ Opcional | Qwen 32B Coder (P3) em tarefas de código puro; decisão com base em métricas (>50 tarefas) |

---

## 10. Referências Normativas e Rastreabilidade

| Artefato | Versão | Papel |
|----------|--------|-------|
| `constitution.md` | v1.2.0 (VIGENTE-PLENA) | Lei suprema do projeto |
| `ADR-001-stack.md` | v1.0.0 | Stack tecnológica FOSS (congelada, ADR-005) |
| `ADR-006-inteligencia-sdd.md` | v2.0.0 | LLM local SDD (Qwen3-30B-A3B MoE) |
| `ADR-010-Stack-Infraestrutura.md` | v1.0.0 | Infraestrutura e isolamento (Docker+Nginx) |
| `hardware.md` | — | Inventário real de hardware (2026-10-31) |
| `AFA-ULTIMATE` | v1.3.0-FINAL | Diretiva de forja de agentes |
| `validate_afa_output.py` | — | Gate de qualidade de forja (≥ 85/100) |
| `validate_nexus_yaml.py` | — | Validação de contratos YAML de agentes |
| `handoff_parser.py` | — | Parsing determinístico de handoffs SDD |

---

## 11. Conclusão

A arquitetura canônica v2.0.0 resolve as tensões identificadas nas análises prévias e incorpora todas as mudanças ratificadas desde setembro/2026:

1. **Modelo:** Qwen3-30B-A3B Q4_K_M (MoE) como pilar, substituindo Qwen 32B Instruct. 14B como acelerador/fallback. 72B adiado.
2. **RAM real:** 60 GB (não 58 GB). Limite de inferência de 32 GB imposto pelo systemd.
3. **Inferência:** llama.cpp CPU-only para MoE (Vulkan secundário, nunca CUDA/NVIDIA).
4. **Agentes:** Substituem as "personas" do v1.0. Forjados por AFA-ULTIMATE, com frontmatter YAML, roster SSOT, Kill Switch, score ≥ 85/100.
5. **Stack de aplicação:** FastAPI + SQLite + WeasyPrint + pytest + GitHub Actions Free Tier + Docker+Nginx (ADR-001, ADR-010).
6. **Governação:** Constituição v1.2.0 como lei suprema; LGPD primária; FOSS-first com Bypass Protocol (3 pilares).

**Princípio guia consolidado:** *"Comece com a solução mais simples possível. Só adicione complexidade quando a dor for real, mensurável e persistente."*

Este documento é a **fonte canônica da stack SDD**. Qualquer divergência entre projetos deve ser justificada por dor mensurável e registrada como ADR em `.ai/specs/architecture.md` do projeto respectivo.
