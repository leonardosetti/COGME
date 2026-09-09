# Relatório Canônico: Stack SDD Local — Arquitetura Convergente

**Documento:** `specs/stack-sdd-canonical.md`
**Versão:** 1.0
**Data:** 2026-09-10
**Status:** Aprovado — base de conhecimento para projetos SDD
**Escopo:** COGME, COBECO e projetos greenfield futuros
**Natureza:** Documento convergente. Consolida e resolve tensões entre quatro análises prévias (stack inicial, crítica do Obsidian, validação de modelos, análise de personas).

---

## 1. Propósito e Princípios Guia

### 1.1. Propósito

Este documento estabelece a **arquitetura canônica** para ambientes SDD (Spec-Driven Development) locais, FOSS, de custo zero, executados em hardware APU AMD (Ryzen 7 8700G + Radeon 780M + 58GB RAM unificada). Serve como:

- **Input único** para onboarding de novos projetos
- **Contrato** entre camadas de infraestrutura, personas e metodologia
- **Base de conhecimento** para o segundo cérebro (Obsidian)
- **Referência de validação** para decisões futuras

### 1.2. Princípios First-Principles (Imutáveis)

| # | Princípio | Implicação Prática |
|---|-----------|---------------------|
| P1 | **Separação ortogonal de camadas** | L1 (infra), L2 (personas), L3 (metodologia) evoluem independentemente |
| P2 | **Simplicidade por padrão** | Adicionar complexidade só quando a dor for mensurável |
| P3 | **Single source of truth** | Todo contexto da IA vive no Git do projeto; Obsidian é interface, não repositório |
| P4 | **Parsing determinístico** | Convenção de nomes > frameworks mágicos |
| P5 | **Custo zero** | 100% FOSS; cloud free-tier apenas como acelerador estratégico |
| P6 | **Especialização via prompt, não via modelo** | Um modelo base + N prompts = N especialistas |
| P7 | **Hardware-realismo** | Decisões baseadas em medições reais, não em specs nominais |

---

## 2. Hardware de Referência (Validado Empiricamente)

### 2.1. Inventário Real (2026-09-07)

| Componente | Especificação | Observação |
|------------|---------------|------------|
| CPU | AMD Ryzen 7 8700G (Zen 4, 8C/16T, AVX-512) | Boost até 5.17 GHz |
| GPU | Radeon 780M (RDNA 3, 12 CUs) | APU — VRAM compartilhada |
| RAM total | **58.0 GB** (não 64GB nominais) | Delta de 6GB vs. premissa inicial |
| RAM disponível (ociosa) | 49.0 GB | OS + GNOME consomem ~9 GB |
| Swap | 16 GB (`/extra/swap/swapfile`) | Adequado para LTO builds |
| `/var` livre | **420 GB** de 458 GB | Suficiente para todos os modelos |
| `/home` livre | 129 GB | Projetos e vaults Obsidian |
| Kernel | Linux 7.1.9-zen1-2-zen | Zen kernel, governor `performance` |
| Mesa | 26.2.1 (radv) | Vulkan 1.4.357 |
| Toolchain | GCC 16.2.1, CMake 4.4.3, Ninja 1.13.2 | AVX-512 via `-march=znver4` |

### 2.2. Implicações Arquiteturais do Hardware Real

- **Margem de RAM apertada para 72B:** 58GB total − 8GB OS = 50GB. Modelo 72B Q4_K_M consome ~42GB → restam 8GB. Qualquer pico do GNOME empurra para swap.
- **32B é o sweet spot real:** 20GB modelo + 8GB OS = 28GB. Margem de 30GB para KV cache (16k ctx) e headroom.
- **Vulkan é o backend primário:** radv está maduro para RDNA 3 em Mesa 26.2. Fallback CPU AVX-512 é viável, não emergencial.

---

## 3. Stack de Software — Três Camadas Ortogonais

### 3.1. Camada L1: Infraestrutura de Inferência

| Componente | Versão/Config | Responsabilidade | Localização |
|------------|---------------|------------------|-------------|
| llama.cpp | 0.4.0-dev (Vulkan+LTO+AVX-512) | Motor de inferência | `/usr/local/bin/llama-server` |
| Backend Vulkan | radv (Mesa 26.2.1) | Aceleração GPU | `libggml-vulkan.so.0` |
| Backend CPU | AVX-512 (Zen 4) | Fallback | Nativo no binário |
| API Server | OpenAI-compat (porta 8080) | Interface HTTP | `llama-server --port 8080` |
| systemd units | Ciclo de vida | Gerenciamento de processo | `/etc/systemd/system/llama-server.service` |

### 3.2. Camada L2: Personas e Contexto

| Componente | Formato | Responsabilidade |
|------------|---------|------------------|
| Persona base | `_base.md` | Instruções comuns |
| Especialistas | `{coder,reviewer,tester,pm}.md` | Comportamento por papel |
| Persona ativa | `active.md → *.md` | Symlink que define o especialista corrente |
| System prompt | Injetado pelo OpenCode | Lido de `active.md` a cada sessão |

**Princípio P6 em ação:** trocar de persona = trocar symlink. Zero overhead de RAM, zero reload de modelo.

### 3.3. Camada L3: Metodologia SDD

| Componente | Formato | Responsabilidade |
|------------|---------|------------------|
| Specs | `.ai/specs/*.md` | Regras imutáveis, contratos, domínio |
| Handoffs | `.ai/handoffs/NNN-*-fase.md` | Artefatos entre fases |
| Workflows | `.ai/workflows/*.sh` | Automação bash (~30 linhas) |
| Segundo cérebro | Obsidian (vault por projeto) | Interface de leitura/edição |

### 3.4. Camada de Interface

| Componente | Responsabilidade |
|------------|------------------|
| OpenCode | IDE que lê persona ativa via API OpenAI-compat |
| Obsidian | Vault por projeto, symlinks para `.ai/` e `docs/` |
| Git | Versionamento de código + contexto `.ai/` + docs humanas |

---

## 4. Organização de Diretórios (Resolução da Tensão Obsidian)

### 4.1. Decisão Canônica: Vault Por Projeto

A análise crítica identificou que um vault global do Obsidian viola o princípio P3 (single source of truth) e introduz poluição cognitiva entre projetos. A arquitetura canônica adota **vault dedicado por projeto**, com Obsidian funcionando como **interface** sobre o repositório Git, não como repositório paralelo.

### 4.2. Estrutura no Repositório Git

```
PROJETO/                          # Repositório Git (single source of truth)
├── .git/
├── .gitignore
├── README.md
│
├── src/                          # Código-fonte
├── tests/                        # Testes automatizados
│
├── docs/                         # Documentação HUMANA (não lida pela IA)
│   ├── project-plan.md
│   ├── roadmap.md
│   ├── meeting-notes/
│   └── decisions/                # ADRs humanos
│
├── .ai/                          # CONTEXTO DA IA (versionado, lido pelo OpenCode)
│   ├── prompts/
│   │   ├── _base.md
│   │   ├── coder.md
│   │   ├── reviewer.md
│   │   ├── tester.md
│   │   ├── pm.md
│   │   └── active.md → coder.md
│   │
│   ├── specs/
│   │   ├── coding-standards.md
│   │   ├── api-contracts.md
│   │   ├── domain-rules.md
│   │   └── architecture.md       # ADRs que afetam código
│   │
│   ├── handoffs/
│   │   ├── 001-feature-x-spec.md
│   │   ├── 001-feature-x-code.md
│   │   ├── 001-feature-x-review.md
│   │   └── 001-feature-x-test.md
│   │
│   └── workflows/
│       └── sdd-cycle.sh
│
└── .obsidian/                    # Configuração do vault (opcional)
    └── workspace.json
```

### 4.3. Estrutura do Vault Obsidian (Interface)

```
~/Obsidian/PROJETO/               # Vault dedicado
├── .ai → /path/to/PROJETO/.ai    # Symlink (single source of truth)
├── docs → /path/to/PROJETO/docs  # Symlink
└── .obsidian/                    # Configuração do vault
```

### 4.4. Regras de Separação de Escopo

| Diretório | Consumidor | Conteúdo típico | Versionado? |
|-----------|------------|-----------------|-------------|
| `src/`, `tests/` | Compilador/runtime | Código | ✅ |
| `.ai/prompts/` | OpenCode (system prompt) | Personas | ✅ |
| `.ai/specs/` | OpenCode (contexto) | Regras, contratos | ✅ |
| `.ai/handoffs/` | OpenCode + scripts | Artefatos SDD | ✅ |
| `.ai/workflows/` | Shell | Automação | ✅ |
| `docs/` | Humanos | Planos, roadmaps, atas | ✅ |
| `~/Obsidian/PROJETO/` | Obsidian | Symlinks + config | ❌ (local) |

**Regra de ouro:** Se não é lido pelo OpenCode nem pelo script SDD, não pertence em `.ai/`.

---

## 5. Modelos Quantizados Aprovados

### 5.1. Matriz de Decisão (Hardware-Real)

| Prioridade | Modelo | Quantização | Disco | RAM Carga | RAM Livre | Ctx Max | tg Target | Status |
|------------|--------|-------------|-------|-----------|-----------|---------|-----------|--------|
| **P0** | Qwen 32B Instruct | Q4_K_M | ~20 GB | ~20 GB | ~30 GB | 16k | ≥6 t/s | ✅ Pilar |
| **P1** | Qwen 14B Instruct | Q4_K_M | ~9 GB | ~9 GB | ~41 GB | 32k+ | ≥12 t/s | ✅ Rápido |
| **P2** | Qwen 14B Instruct | Q5_K_M | ~11 GB | ~11 GB | ~39 GB | 32k+ | ≥10 t/s | ✅ Validação |
| **P3** | Qwen 32B Coder | Q4_K_M | ~20 GB | ~20 GB | ~30 GB | 16k | ≥6 t/s | ⚠️ Experimental |
| **P4** | DeepSeek-Coder-V2 Lite | Q4_K_M | ~9 GB | ~9 GB | ~41 GB | 16k | ≥12 t/s | ⚠️ Sob demanda |
| **P5** | Qwen 72B Instruct | Q4_K_M | ~42 GB | ~42 GB | ~8 GB | 4k | ~1-2 t/s | ❌ Adiar |

### 5.2. Regras de Uso

- **Um modelo por vez.** Carregamento via systemd (`systemctl restart llama-server@<modelo>`).
- **P0 é o padrão.** Todas as personas SDD rodam sobre o 32B Instruct.
- **P1/P2 para testes rápidos** e validação de handoffs (parsing determinístico).
- **P3/P4 apenas se P0 falhar consistentemente** em tarefas específicas (>30% de falha mensurável).
- **P5 adiado** até dor real. O budget de RAM (8GB livres) é insuficiente para uso interativo.

### 5.3. Localização

```
/var/lib/llama.cpp/models/
├── qwen-32b-instruct-q4_k_m.gguf     # P0
├── qwen-14b-instruct-q4_k_m.gguf     # P1
├── qwen-14b-instruct-q5_k_m.gguf     # P2
├── qwen-32b-coder-q4_k_m.gguf        # P3 (baixar apenas se necessário)
└── qwen-72b-instruct-q4_k_m.gguf     # P5 (NÃO baixar)

/extra/backup/llama-models/            # Backup resiliente (P0 + P1)
```

**Total imediato (P0+P1+P2):** 40 GB de 420 GB disponíveis → 9.5% do `/var`.

---

## 6. Personas SDD e Associação Modelo-Prompt

### 6.1. Núcleo Mínimo Viável (4 personas)

| Persona | Responsabilidade | Input | Output | Modelo |
|---------|------------------|-------|--------|--------|
| **PM** | Especificar features, critérios de aceite | Requisitos vagos | `NNN-*-spec.md` | Qwen 32B Instruct |
| **Coder** | Implementar aderente à spec | Spec + código | Código em `src/` | Qwen 32B Instruct |
| **Reviewer** | Revisar código contra spec + standards | Código + spec | `NNN-*-review.md` | Qwen 32B Instruct |
| **Tester** | Gerar testes que validam a spec | Spec + código | Testes em `tests/` | Qwen 32B Instruct |

**Todas compartilham o mesmo modelo (P0).** Especialização via prompt, não via modelo.

### 6.2. Personas Opcionais (Adicionar Apenas Com Dor Mensurável)

| Persona | Gatilho de Adição | Alternativa Simples |
|---------|-------------------|---------------------|
| Architect | >10k LOC ou múltiplos módulos | PM com prompt específico |
| Debugger | Bugs com stack traces longos | Coder com prompt de diagnóstico |
| DocWriter | API pública | Coder com prompt de documentação |
| Refactorer | Dívida técnica mensurável | Reviewer com prompt de refatoração |
| SecurityReviewer | Exposição externa | Reviewer com checklist de segurança |

### 6.3. Candidatos Alternativos (Rejeitados ou Condicionais)

| Modelo | Veredito | Justificativa |
|--------|----------|---------------|
| Qwen 32B Coder | Condicional (P3) | Ganho marginal em código; perda em PT-BR |
| DeepSeek-Coder-V2 Lite | Condicional (P4) | Forte em código puro, fraco em PT-BR |
| Llama 3.3 70B | Rejeitado | Apertado em RAM, inferior ao Qwen 32B |
| Mistral Small 24B | Rejeitado | Sem ganho mensurável sobre Qwen |
| Gemma 2 27B | Rejeitado | Inferior em código e PT-BR |
| Phi-3.5/4 Mini | Rejeitado | Limitado para SDD |
| Command R | Rejeitado | Licença não-comercial |

**Critério eliminatório:** modelos que falham em português são rejeitados, independente da qualidade em código.

---

## 7. Fluxo SDD Padrão

### 7.1. Ciclo de uma Feature

```bash
# 1. PM escreve especificação
vim .ai/handoffs/001-feature-x-spec.md

# 2. Coder implementa
ln -sf coder.md .ai/prompts/active.md
./.ai/workflows/sdd-cycle.sh code 001

# 3. Reviewer revisa
ln -sf reviewer.md .ai/prompts/active.md
./.ai/workflows/sdd-cycle.sh review 001

# 4. Tester gera testes
ln -sf tester.md .ai/prompts/active.md
./.ai/workflows/sdd-cycle.sh test 001

# 5. Commit atômico por fase
git add .ai/handoffs/001-feature-x-* src/ tests/
git commit -m "SDD: feature-x (spec→code→review→test)"
```

### 7.2. Troca de Modelo (Quando Necessário)

```bash
# Trocar para 14B (testes rápidos)
systemctl restart llama-server@14b

# Trocar para 32B (produção)
systemctl restart llama-server@32b
```

---

## 8. Métricas de Sucesso e Gatilhos de Reavaliação

### 8.1. Targets de Performance

| Métrica | Target | Método de Validação |
|---------|--------|---------------------|
| tg 32B-Vulkan | ≥6 t/s | Output do `llama-server` |
| tg 14B-Vulkan | ≥12 t/s | Output do `llama-server` |
| RAM pico (32B) | ≤30 GB | `htop` durante inferência |
| Contexto 16k | Sem OOM | `-c 16384` com prompt longo |
| TTFT (32B) | <2s | Medição manual |
| Parsing handoff | 100% determinístico | Script de validação |
| Custo financeiro | R$ 0,00 | Stack 100% FOSS |

### 8.2. Gatilhos de Fallback

| Condição | Ação |
|----------|------|
| tg < 4 t/s no 32B | Reduzir ctx para 8k ou migrar para 14B |
| OOM no 32B | Reduzir ctx ou migrar para 14B |
| Vulkan crash >2x/dia | Migrar para CPU AVX-512 |
| 72B necessário | Aumentar swap para 32GB + fechar GNOME |

### 8.3. Gatilhos de Reavaliação da Arquitetura

A arquitetura deve ser reavaliada apenas se:

- **Mudança de hardware:** GPU dedicada com VRAM >12GB
- **Mudança de requisito:** Necessidade de modelos >72B interativos
- **Dor mensurável:** Script bash não atende 80% dos casos
- **Nova ferramenta FOSS:** Motor 2x mais rápido que llama.cpp para este hardware
- **Revisão agendada:** 2026-12-10 (3 meses)

---

## 9. Anti-Padrões Explícitos (O Que NÃO Fazer)

| Anti-padrão | Princípio Violado | Motivo |
|-------------|-------------------|--------|
| Vault global do Obsidian | P3 (single source of truth) | Poluição cognitiva entre projetos |
| Orquestrador (Hermes, LangChain) | P2 (simplicidade) | RAM, latência, ponto único de falha |
| Framework SDD (SpecKit) | P2, P4 | Framework fetishism; Markdown + bash basta |
| Modelo diferente por persona | P6 (especialização via prompt) | Viola princípio de simplicidade |
| Múltiplos modelos simultâneos | P7 (hardware-realismo) | RAM unificada é recurso finito |
| Documentos de gestão em `.ai/` | Regra de ouro | Polui contexto da IA |
| Quantizações IQ2/IQ3 | Qualidade | Degradação em raciocínio lógico |
| Modelos não-FOSS | P5 (custo zero) | Viola princípio de liberdade |
| Adicionar persona sem dor | P2 | Complexidade antecipada |
| Colocar `.ai/` fora do Git | P3 | Perda de single source of truth |

---

## 10. Roadmap de Implementação

### Fase 1: Infraestrutura ✅ (Concluída)
- [x] Compilar llama.cpp com Vulkan + LTO + AVX-512
- [x] Validar binários e symlinks
- [x] Documentar build em Obsidian

### Fase 2: Modelos (Próxima)
- [ ] Download Qwen 32B Instruct Q4_K_M (P0)
- [ ] Download Qwen 14B Instruct Q4_K_M (P1)
- [ ] Download Qwen 14B Instruct Q5_K_M (P2)
- [ ] Teste de performance (validar tg targets)

### Fase 3: Estrutura de Projeto
- [ ] Criar `.ai/{prompts,specs,handoffs,workflows}/` em COGME/COBECO
- [ ] Escrever `_base.md` e as 4 personas do núcleo
- [ ] Escrever `sdd-cycle.sh`
- [ ] Configurar vault Obsidian por projeto com symlinks

### Fase 4: Validação End-to-End
- [ ] Executar ciclo SDD completo em tarefa real
- [ ] Medir métricas de performance
- [ ] Documentar lições aprendidas

### Fase 5: Experimentação Controlada (Opcional)
- [ ] Testar Qwen 32B Coder (P3) em tarefas de código puro
- [ ] Testar DeepSeek-Coder-V2 Lite (P4) comparativamente
- [ ] Decidir adoção com base em métricas (>50 tarefas)

---

## 11. Conclusão

A arquitetura canônica resolve as tensões identificadas nas análises prévias:

1. **Obsidian:** vault por projeto, como interface sobre o Git, não como repositório paralelo.
2. **Modelos:** 32B Instruct como pilar, 14B como acelerador, 72B adiado. Candidatos alternativos condicionais a dor mensurável.
3. **Personas:** núcleo de 4, especialização via prompt, modelo único.
4. **Organização:** `.ai/` versionado no Git, `docs/` separado para humanos, symlinks no vault Obsidian.

**Princípio guia consolidado:** *"Comece com a solução mais simples possível. Só adicione complexidade quando a dor for real, mensurável e persistente."*

Este documento é a **fonte canônica**. Qualquer divergência entre projetos deve ser justificada por dor mensurável e registrada como ADR em `.ai/specs/architecture.md` do projeto respectivo.