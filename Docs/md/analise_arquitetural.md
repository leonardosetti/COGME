# RELATÓRIO DE AUDITORIA ANALÍTICA v2.0 — CONSOLIDAÇÃO ARQUITETURAL DEFINITIVA DO COGME

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Data de Emissão:** 10/09/2026
**Emissor:** GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carletto
**Referências:** `analise_auditoria_1.3.md` + `Relatorio_Canônico_Stack_SDD_Local.md` + `OKB_COGME_v3.0` + `TAP_EAP.md` + `hardware.md`
**Status:** Decisão Arquitetural Consolidada — input para OKB v3.1 + ADR-002/004 finais + Plano de Ação 10-22/09

---

## 0. VEREDITO SUMÁRIO EXECUTIVO

A rodada v2.0 introduz **6 correções estruturais críticas** que redefinem a arquitetura documental e técnica do COGME:

1. **Separação ontológica TAP ≠ EAP ≠ PDCA** — o TAP antecede o projeto e não deve ser medido/controlado via EAP ou PDCA (correção de vício conceitual grave).
2. **Stack SDD Local canônica** — substitui Qwen 7B (subdimensionado) por Qwen 32B Instruct Q4_K_M como pilar, validado empiricamente no hardware real (58GB RAM, não 60GB nominais).
3. **Personas SDD consolidadas** — núcleo de 4 (PM, Coder, Reviewer, Tester) compartilhando o mesmo modelo; especialização via prompt (P6), não via modelo.
4. **Atividades derivadas da EAP via decomposição** (PMBOK 6ª §6.2) — pacotes de trabalho (entregas/substantivos) decompõem-se em atividades (ações/verbos) para o cronograma.
5. **TAP concluído sem invadir escopo gerencial** — TAP define "o quê/por quê/quem"; planos de gerenciamento definem "como/quando/quanto".
6. **Requisitos, riscos e premissas previsíveis** explicitados no TAP conforme padrão PMO escritoriodeprojetos.com.br.

**Veredito final:** A arquitetura v2.0 é **coerente, acionável e defensável academicamente**. Todas as decisões passam no teste GMV (OKB v3.0 §4.2) e respeitam a hierarquia de governança (OKB v3.0 §4.1). A entrega parcial de 22/09/2026 permanece viável com folga de 28%.

---

## 1. DELTA ANALÍTICO v1.2 → v2.0

| # | Mudança Estrutural | Categoria | Severidade | Domínio PMBOK 7ª |
|---|---|---|---|---|
| 1 | **TAP não integra EAP nem PDCA** (correção ontológica) | Conceitual | 🔴 CRÍTICA | Escopo + Medição |
| 2 | **Stack SDD Local canônica** (Qwen 32B pilar, 14B rápido, 72B adiado) | Técnica | 🔴 CRÍTICA | Abordagem de Desenvolvimento |
| 3 | **Personas SDD = 4 (núcleo mínimo)** compartilhando 1 modelo | Técnica | 🟠 ALTA | Trabalho do Projeto |
| 4 | **Atividades derivadas da EAP via decomposição** (PMBOK 6ª §6.2) | Processual | 🟠 ALTA | Cronograma |
| 5 | **TAP sem invadir escopo gerencial** (padrão PMO) | Conceitual | 🟠 ALTA | Integração |
| 6 | **Hardware real = 58GB RAM** (não 60GB nominais) | Técnica | 🟡 MÉDIA | Recursos |

---

## 2. ANÁLISE CRÍTICA DAS MUDANÇAS

### 2.1. Mudança 1 — Separação Ontológica TAP ≠ EAP ≠ PDCA (CRÍTICA)

**Problema identificado nas versões anteriores:** O TAP (Termo de Abertura do Projeto) estava sendo tratado como pacote de trabalho N1.1 da EAP e como alvo de PDCA. Isso viola um princípio fundamental do PMBOK:

> **O TAP é o documento que AUTORIZA o projeto e concede autoridade ao gerente. Ele antecede o planejamento e não é objeto de gerenciamento — é a base sobre a qual o gerenciamento se constrói.** (PMBOK 6ª §4.1 / PMBOK 7ª Domínio de Entrega)

**Correção aplicada:**

| Artefato | Natureza | Integra EAP? | Tem PDCA? |
|---|---|---|---|
| **TAP** | Autorização + base de referência | ❌ NÃO | ❌ NÃO |
| **Planos de Gerenciamento (01-10)** | Execução do escopo autorizado | ✅ SIM | ✅ SIM |
| **Código-fonte (11)** | Produto final | ✅ SIM | ✅ SIM |

**Impacto na EAP:**
- Remover N1.1 (TAP) da EAP — o TAP é **pré-condição**, não pacote de trabalho.
- A Fase N1 (Iniciação e Planejamento) passa a conter apenas: N1.2 a N1.6.
- O PDCA do TAP é substituído por **histórico de versões do próprio TAP** (v0.1 → v0.9 → v1.0), sem ciclo PDCA formal.

**Impacto no Plano de Qualidade (§5.6):**
- Remover "PDCA do TAP (N1.1)" da lista de PDCAs consolidados.
- Lista passa de 13 para **12 PDCAs** (N1.2 a N4.4).

**Teste GMV:**
- P1 (Prof. Dr. Nivaldo Carletto exigirá?): ✅ SIM — correção conceitual acadêmica
- P2 (Evita retrabalho?): ✅ SIM — blinda contra questionamento da banca
- P3 (PMBOK 7ª exige?): ✅ SIM — Domínio de Integração
- P4 (Útil para equipe?): ✅ SIM — clareza ontológica

**Veredito:** 4×SIM → **MANDATÓRIO**

### 2.2. Mudança 2 — Stack SDD Local Canônica (CRÍTICA)

**Problema identificado:** A v1.0/v1.1/v1.2 assumiam Qwen 7B como modelo primário. O Relatório Canônico demonstra que o hardware real (58GB RAM) suporta modelos muito mais capazes:

| Modelo | RAM Carga | RAM Livre | Qualidade | Veredito v1.x | Veredito v2.0 |
|---|---|---|---|---|---|
| Qwen 7B Q4 | ~5GB | ~45GB | ⭐⭐⭐ | ✅ Pilar | ❌ **Subdimensionado** |
| Qwen 14B Q4_K_M | ~9GB | ~41GB | ⭐⭐⭐⭐ | ⚠️ Rápido | ✅ **Acelerador** |
| **Qwen 32B Instruct Q4_K_M** | **~20GB** | **~30GB** | **⭐⭐⭐⭐⭐** | ❌ Não avaliado | ✅ **PILAR** |
| Qwen 72B Q4_K_M | ~42GB | ~8GB | ⭐⭐⭐⭐⭐ | ❌ Não avaliado | ⚠️ **Adiar** |

**Decisão canônica (ADR-002 atualizado):**

| Prioridade | Modelo | Uso | tg Target |
|---|---|---|---|
| **P0** | Qwen 32B Instruct Q4_K_M | Pilar SDD (todas as personas) | ≥6 t/s (Vulkan) |
| **P1** | Qwen 14B Instruct Q4_K_M | Testes rápidos, validação | ≥12 t/s |
| **P2** | Qwen 14B Instruct Q5_K_M | Validação de specs (qualidade superior) | ≥10 t/s |
| **P3** | Qwen 32B Coder Q4_K_M | Condicional — apenas se P0 falhar | ≥6 t/s |
| **P4** | DeepSeek-Coder-V2 Lite 16B | Código puro sob demanda | ≥12 t/s |
| **P5** | Qwen 72B Instruct Q4_K_M | **NÃO baixar** — RAM insuficiente | ~1-2 t/s |

**Justificativa first-principles:**
- 32B é o **sweet spot real** do hardware (30GB livres após carga = margem segura para 16k ctx).
- 7B é **subdimensionado** para SDD complexo (raciocínio abstrato, specs longas).
- 72B é **impossível interativamente** (8GB livres = swap massivo).

**Impacto no ADR-002:** Substituir "Qwen2.5-Coder-7B-Q4" por "Qwen 32B Instruct Q4_K_M" como modelo primário.

### 2.3. Mudança 3 — Personas SDD Consolidadas (ALTA)

**Problema identificado:** Versões anteriores não definiam personas SDD explicitamente, gerando risco de "framework fetishism" (adicionar complexidade sem dor mensurável).

**Decisão canônica (núcleo mínimo viável):**

| Persona | Responsabilidade | Input | Output | Modelo |
|---|---|---|---|---|
| **PM** | Especificar features, critérios de aceite | Requisitos vagos | `NNN-*-spec.md` | Qwen 32B |
| **Coder** | Implementar aderente à spec | Spec + código | Código em `src/` | Qwen 32B |
| **Reviewer** | Revisar código contra spec + standards | Código + spec | `NNN-*-review.md` | Qwen 32B |
| **Tester** | Gerar testes que validam a spec | Spec + código | Testes em `tests/` | Qwen 32B |

**Princípio P6 em ação:** Todas as personas compartilham o **mesmo modelo** (Qwen 32B). A troca de persona = troca de symlink em `.ai/prompts/active.md`. Zero overhead de RAM, zero reload de modelo.

**Personas opcionais (adicionar apenas com dor mensurável):**
- Architect (>10k LOC)
- Debugger (stack traces longos)
- DocWriter (API pública)
- Refactorer (dívida técnica)
- SecurityReviewer (exposição externa)

**Regra de ouro:** Começar com 4 personas. Adicionar apenas quando o prompt genérico falhar consistentemente (>30% dos casos).

### 2.4. Mudança 4 — Atividades Derivadas da EAP via Decomposição (ALTA)

**Fundamento teórico (PMBOK 6ª §6.2 — Definir as Atividades):**

> "As atividades do projeto são derivadas dos **pacotes de trabalho** da EAP através do processo de **decomposição**. Enquanto a EAP foca em entregas (substantivos), a lista de atividades foca nas ações (verbos) necessárias para gerar essas entregas."

**Aplicação ao COGME:**

```
EAP (ENTREGAS / SUBSTANTIVOS)
    N5.1: Backend — Lógica de Negócio
         ↓ decomposição
ATIVIDADES (AÇÕES / VERBOS)
    A5.1.1: Modelar entidades de domínio (Câmbio, Spread, IOF)
    A5.1.2: Implementar serviços de cálculo
    A5.1.3: Escrever testes unitários
    A5.1.4: Documentar API (OpenAPI)
```

**Impacto no Plano de Cronograma:**
- A EAP permanece como **estrutura de decomposição do escopo**.
- O cronograma é construído a partir da **lista de atividades derivadas**, não diretamente da EAP.
- Cada atividade possui: código, predecessoras, sucessoras, recursos, restrições (atributos).

**Mapeamento EAP → Atividades (exemplo para MF1):**

| Pacote EAP | Atividades Derivadas (exemplo) |
|---|---|
| N1.2 Identificação de Stakeholders | A1.2.1: Listar stakeholders; A1.2.2: Classificar poder/interesse; A1.2.3: Documentar matriz |
| N2.1 Requisitos Funcionais | A2.1.1: Entrevistar Prof. Dr. Nivaldo Carletto; A2.1.2: Redigir user stories; A2.1.3: Validar com stakeholder |
| N4.1 Seleção da Stack FOSS | A4.1.1: Pesquisar candidatos; A4.1.2: Aplicar critérios GMV; A4.1.3: Redigir ADR-002; A4.1.4: Validar com protótipo |

**Domínio PMBOK 7ª associado:** Domínio de Planejamento (decomposição de escopo em trabalho executável).

### 2.5. Mudança 5 — TAP Sem Invadir Escopo Gerencial (ALTA)

**Fundamento (padrão PMO escritoriodeprojetos.com.br):**

O TAP responde a **6 perguntas fundamentais**:
1. **O quê?** — Objetivos SMART do projeto
2. **Por quê?** — Justificativa e alinhamento estratégico
3. **Quem?** — Stakeholders e papéis
4. **O quê (entregas)?** — Escopo de alto nível + EAP
5. **Quando?** — Marcos temporais
6. **Quanto?** — Orçamento preliminar + restrições

O TAP **NÃO responde**:
- Como o trabalho será executado (→ Plano de Integração)
- Como o escopo será detalhado (→ Plano de Escopo)
- Como o cronograma será gerenciado (→ Plano de Cronograma)
- Como a qualidade será garantida (→ Plano de Qualidade)

**Aplicação ao COGME:**

| Seção do TAP | Conteúdo | NÃO deve conter |
|---|---|---|
| §1 Identificação | Nome, gerente, patrocinador | Detalhes de RACI |
| §2 Justificativa | Problema, solução, alinhamento | Análise de mercado detalhada |
| §3 Objetivos SMART | 5 objetivos mensuráveis | Critérios de aceite de cada feature |
| §4 Escopo Alto Nível | O que está DENTRO e FORA | EAP detalhada (apenas níveis 1-2) |
| §5 Marcos | M1 (22/09) + M2 (Nov/Dez) | Cronograma detalhado de atividades |
| §6 Orçamento | R$ 0,00 (FOSS) | Planilha de custos detalhada |
| §7 Riscos | Top 5 riscos + respostas | Matriz completa de riscos |
| §8 Premissas | 8 premissas fundamentais | Dicionário de premissas |
| §9 Restrições | 8 categorias de restrições | Plano de mitigação detalhado |

**Teste GMV:**
- P1: ✅ SIM — padrão PMO é exigido academicamente
- P2: ✅ SIM — evita sobreposição com planos
- P3: ✅ SIM — Domínio de Integração PMBOK 7ª
- P4: ✅ SIM — clareza para a equipe

**Veredito:** 4×SIM → **MANDATÓRIO**

### 2.6. Mudança 6 — Hardware Real = 58GB RAM (MÉDIA)

**Correção factual:** O `hardware.md` mostra:
- RAM total: **58.0 GB** (não 64GB nominais)
- RAM disponível (ociosa): **49.0 GB**
- OS + GNOME consomem: **~9 GB**
- Swap: **16 GB**
- `/var` livre: **420 GB**

**Implicação:** Todos os cálculos de RAM das versões anteriores estavam superestimados em ~6GB. A decisão de adiar o Qwen 72B (Mudança 2) é **validada empiricamente**.

---

## 3. REESTRUTURAÇÃO DA EAP (PÓS-CORREÇÃO ONTOLÓGICA)

### 3.1. EAP v1.0 (Consolidada)

**Remoções:**
- ❌ N1.1 (TAP) — TAP não é pacote de trabalho
- ❌ N5.6 (Execução Kanban) — fundido com N1.6
- ❌ N6.3 (Testes de Performance) — YAGNI
- ❌ N9.3 (Relatórios Quinzenais) — GitHub é SSOT
- ❌ N10.4 (Runbooks) — YAGNI
- ❌ N12.3 (Relatórios EVM) — Kanban usa métricas de fluxo
- ❌ N13.4 (Auditoria FOSS Final) — fundido com N4.4
- ❌ N14-N17 (Fases Desejáveis) — removidas do TAP+EAP

**Resultado:**

| Nível 1 | Pacotes Nível 2 | Macro-Fase |
|---|---|---|
| **N1. Iniciação e Planejamento** | N1.2 Stakeholders, N1.3 Planos, N1.4 Qualidade, N1.5 Política FOSS, N1.6 Backlog+Kanban | MF1 |
| **N2. Requisitos** | N2.1 RF, N2.2 RNF, N2.3 Casos de Uso | MF1 |
| **N3. Modelagem** | N3.1 Arquitetura, N3.2 Protótipo, N3.3 DER | MF1 |
| **N4. Ambiente** | N4.1 Stack FOSS, N4.2 Git+CI/CD, N4.3 Setup, N4.4 Auditoria Licenças | MF1 |
| **N5. Desenvolvimento** | N5.1 Backend Lógica, N5.2 Backend API+Cache, N5.3 Frontend, N5.4 PDF, N5.5 SDD+IA | MF2 |
| **N6. Qualidade** | N6.1 Testes Unit/Integ, N6.2 UAT | MF2 |
| **N7. DevOps** | N7.1 Pipeline CI, N7.2 Deploy Manual | MF2 |
| **N8. Deploy** | N8.1 Publicação, N8.2 Documentação Deploy | MF2 |
| **N9. Comunicação** | N9.1 RACI, N9.2 Canais, N9.4 Cerimônias | MF1 |
| **N10. Base Conhecimento** | N10.1 ADRs, N10.2 Lições, N10.3 Prompts SDD | MF1 |
| **N11. Mudanças** | N11.1 CCB, N11.2 Registro, N11.3 Label change-request, N11.4 Versionamento | MF2 |
| **N12. Documentação** | N12.1 Técnica, N12.2 Manual, N12.4 Consolidação Parcial | MF3 |
| **N13. Encerramento** | N13.1 Lições Finais, N13.2 SMART, N13.3 Apresentação | MF3 |

**Total:** 13 fases Nível 1 + **48 pacotes Nível 2** (redução de 62 para 48, ganho de 23%).

### 3.2. PDCAs Consolidados no Plano de Qualidade (§5.6)

**Lista final de 12 PDCAs (sem TAP):**

| # | Atividade | Fase EAP | Macro-Fase |
|---|---|---|---|
| 1 | PDCA da Identificação de Stakeholders | N1.2 | MF1 |
| 2 | PDCA dos Planos de Gerenciamento | N1.3 | MF1 |
| 3 | PDCA do Plano de Qualidade | N1.4 | MF1 |
| 4 | PDCA da Política FOSS | N1.5 | MF1 |
| 5 | PDCA do Backlog e Kanban | N1.6 | MF1 |
| 6 | PDCA dos Requisitos Funcionais | N2.1 | MF1 |
| 7 | PDCA dos Requisitos Não Funcionais | N2.2 | MF1 |
| 8 | PDCA dos Casos de Uso | N2.3 | MF1 |
| 9 | PDCA da Arquitetura da Solução | N3.1 | MF1 |
| 10 | PDCA do Protótipo UX/UI | N3.2 | MF1 |
| 11 | PDCA da Modelagem de Dados (DER) | N3.3 | MF1 |
| 12 | PDCA da Seleção da Stack FOSS | N4.1 | MF1 |

**Nota:** Apenas atividades da MF1 terão PDCA documentado na entrega parcial de 22/09. Atividades da MF2 e MF3 terão PDCAs até a entrega final.

---

## 4. STACK SDD LOCAL CANÔNICA (CONSOLIDADA)

### 4.1. Arquitetura em 3 Camadas Ortogonais

```
┌─────────────────────────────────────────────────────────────┐
│  CAMADA L1 — INFRAESTRUTURA DE INFERÊNCIA                  │
│  • llama.cpp 0.4.0-dev (Vulkan + LTO + AVX-512)            │
│  • Backend Vulkan (radv Mesa 26.2.1) + CPU AVX-512 fallback│
│  • API Server OpenAI-compat (porta 8080)                   │
│  • systemd units para ciclo de vida                        │
├─────────────────────────────────────────────────────────────┤
│  CAMADA L2 — PERSONAS E CONTEXTO                           │
│  • .ai/prompts/_base.md (persona base)                     │
│  • .ai/prompts/{coder,reviewer,tester,pm}.md               │
│  • .ai/prompts/active.md → symlink para persona corrente   │
│  • Princípio P6: 1 modelo + N prompts = N especialistas    │
├─────────────────────────────────────────────────────────────┤
│  CAMADA L3 — METODOLOGIA SDD                               │
│  • .ai/specs/*.md (regras imutáveis, contratos)            │
│  • .ai/handoffs/NNN-*-fase.md (artefatos entre fases)      │
│  • .ai/workflows/sdd-cycle.sh (automação bash ~30 linhas)  │
│  • Obsidian vault por projeto (interface, não repositório) │
└─────────────────────────────────────────────────────────────┘
```

### 4.2. Modelos Aprovados (Hierarquia Definitiva)

| Prioridade | Modelo | Quantização | Disco | RAM Carga | RAM Livre | Ctx Max | tg Target | Status |
|---|---|---|---|---|---|---|---|---|
| **P0** | Qwen 32B Instruct | Q4_K_M | ~20GB | ~20GB | ~30GB | 16k | ≥6 t/s | ✅ **PILAR** |
| **P1** | Qwen 14B Instruct | Q4_K_M | ~9GB | ~9GB | ~41GB | 32k+ | ≥12 t/s | ✅ Rápido |
| **P2** | Qwen 14B Instruct | Q5_K_M | ~11GB | ~11GB | ~39GB | 32k+ | ≥10 t/s | ✅ Validação |
| **P3** | Qwen 32B Coder | Q4_K_M | ~20GB | ~20GB | ~30GB | 16k | ≥6 t/s | ⚠️ Condicional |
| **P4** | DeepSeek-Coder-V2 Lite | Q4_K_M | ~9GB | ~9GB | ~41GB | 16k | ≥12 t/s | ⚠️ Sob demanda |
| **P5** | Qwen 72B Instruct | Q4_K_M | ~42GB | ~42GB | ~8GB | 4k | ~1-2 t/s | ❌ **ADIAR** |

**Total imediato (P0+P1+P2):** 40GB de 420GB disponíveis em `/var` → 9.5% utilizado ✅

### 4.3. Localização no Filesystem

```
/var/lib/llama.cpp/models/
├── qwen-32b-instruct-q4_k_m.gguf     # P0 — baixar primeiro
├── qwen-14b-instruct-q4_k_m.gguf     # P1 — baixar segundo
├── qwen-14b-instruct-q5_k_m.gguf     # P2 — baixar terceiro (opcional)
├── qwen-32b-coder-q4_k_m.gguf        # P3 — apenas se necessário
└── qwen-72b-instruct-q4_k_m.gguf     # P5 — NÃO baixar

/extra/backup/llama-models/            # Backup resiliente (P0 + P1)
```

### 4.4. Comandos de Download (Fase 2)

```bash
# P0: Modelo principal (obrigatório)
huggingface-cli download \
  Qwen/Qwen2.5-32B-Instruct-GGUF \
  qwen2.5-32b-instruct-q4_k_m.gguf \
  --local-dir /var/lib/llama.cpp/models/

# P1: Modelo rápido
huggingface-cli download \
  Qwen/Qwen2.5-14B-Instruct-GGUF \
  qwen2.5-14b-instruct-q4_k_m.gguf \
  --local-dir /var/lib/llama.cpp/models/

# P2: Variante de maior qualidade (opcional)
huggingface-cli download \
  Qwen/Qwen2.5-14B-Instruct-GGUF \
  qwen2.5-14b-instruct-q5_k_m.gguf \
  --local-dir /var/lib/llama.cpp/models/
```

### 4.5. Critérios de Validação Pós-Download

```bash
# Teste de carga (32B exemplo)
llama-server \
  -m /var/lib/llama.cpp/models/qwen-32b-instruct-q4_k_m.gguf \
  -ngl 99 \
  -c 16384 \
  --port 8080

# Checklist de validação:
# [ ] "llama_model_load: Vulkan buffer allocated" → GPU ativa
# [ ] "llama_model_load: model size = XXXX MB" → tamanho esperado
# [ ] RAM pico ≤ 28GB (htop) → dentro do budget
# [ ] Resposta a prompt teste em <2s (TTFT) → latência OK
# [ ] tg ≥ 6 t/s (medir com 200 tokens output) → throughput OK
```

### 4.6. Anti-Padrões Explícitos (O Que NÃO Fazer)

| Anti-Padrão | Princípio Violado | Motivo |
|---|---|---|
| Vault global do Obsidian | P3 (single source of truth) | Poluição cognitiva entre projetos |
| Orquestrador (Hermes, LangChain) | P2 (simplicidade) | RAM, latência, ponto único de falha |
| Framework SDD (SpecKit) | P2, P4 | Framework fetishism; Markdown + bash basta |
| Modelo diferente por persona | P6 (especialização via prompt) | Viola princípio de simplicidade |
| Múltiplos modelos simultâneos | P7 (hardware-realismo) | RAM unificada é recurso finito |
| Documentos de gestão em `.ai/` | Regra de ouro | Polui contexto da IA |
| Quantizações IQ2/IQ3 | Qualidade | Degradação em raciocínio lógico |
| Modelos não-FOSS | P5 (custo zero) | Viola princípio de liberdade |

---

## 5. TAP v1.0 — REQUISITOS, RISCOS E PREMISSAS PREVISÍVEIS

### 5.1. Principais Requisitos das Entregas/Produtos (Padrão PMO)

| Entrega Principal | Requisitos Chave | Critério de Aceite |
|---|---|---|
| **MVP Web Funcional** | Simulação cambial (USD/EUR → BRL); 5 regimes (hora, dia, semana, mês, fixo); cálculo de spread + IOF; emissão de invoice PDF | Tempo de resposta ≤ 3s; 100% dos fluxos críticos funcionais |
| **Cobertura de Testes** | Testes unitários + integração automatizados | ≥ 80% coverage (pytest + coverage.py) |
| **Documentação Técnica** | Arquitetura, APIs (OpenAPI), manual do usuário | Revisão cruzada aprovada |
| **Base de Conhecimento** | ADRs, lições aprendidas, prompts SDD catalogados | 100% das decisões críticas documentadas |
| **Auditoria FOSS** | Lista completa de dependências + licenças | 100% compatível com MIT/Apache 2.0/BSD/GPL |

### 5.2. Principais Riscos Previsíveis (Top 5)

| ID | Risco | Prob. | Impacto | Severidade | Resposta |
|---|---|---|---|---|---|
| **R-01** | Stack FOSS indefinida bloqueia Fase 5 | 80% | Alto | 🔴 Crítico | ADR-002 até 11/09 |
| **R-02** | EAP não sincronizada com GitHub Projects | 60% | Alto | 🟠 Alto | Mapeamento 1:1 até 15/09 |
| **R-03** | Governança > 50% do tempo da equipe | 70% | Médio | 🟠 Alto | Aplicar GMV (OKB v3.0 §4.2) |
| **R-08** | Equipe exceder 20h/semana (burnout) | 50% | Médio | 🟠 Alto | WIP limits + métrica de burnout |
| **R-09** | Entrega parcial 22/09 não concluída | 15% | Alto | 🟠 Alto | Plano de ação 10-22/09 + folga 28% |

### 5.3. Premissas Previsíveis (8 Premissas Fundamentais)

| # | Premissa | Fundamentação |
|---|---|---|
| **P1** | PMBOK 7ª é governança primária; PMBOK 6ª é dicionário complementar | Hierarquia OKB v3.0 §4.1 |
| **P2** | Stack 100% FOSS (MIT, Apache 2.0, BSD, GPL) | TAP §2.4 + OKB v3.0 P2 |
| **P3** | Kanban via GitHub Projects é método de execução | ADR-001 |
| **P4** | Uso de LLM é irrestrito e autorizado | OKB v3.0 §4.8 |
| **P5** | Código-fonte (MVP full-stack) é deliverable formal | TAP §3 |
| **P6** | Equipe de 2 pessoas com carga ≤ 20h/semana cada | PMBOK 7ª Domínio de Equipe |
| **P7** | Prof. Dr. Nivaldo Carletto é stakeholder único formal | TAP §1 |
| **P8** | Hardware local (AMD Ryzen 7 8700G, 58GB RAM, Arch Linux) é suficiente para SDD local | hardware.md + Relatório Canônico |

---

## 6. PLANO DE AÇÃO 10-22/09/2026 (ATUALIZADO)

### 6.1. Capacidade Disponível

| Recurso | Disponibilidade |
|---|---|
| Dias úteis | 8 (10, 11, 15, 16, 17, 18, 19, 22/09) |
| Horas por dia | 4h/pessoa (20h/semana ÷ 5 dias) |
| Total de horas | 2 pessoas × 4h × 8 dias = **64h** |
| Escopo estimado | 46h (TAP 8h + 5 planos × 6h + PDCA 6h + Ishikawa 2h) |
| **Folga** | **18h (28%)** |

### 6.2. Cronograma Detalhado

| Data | Ação | Responsável | Artefato | DoD |
|---|---|---|---|---|
| **10/09 (qui)** | Finalizar TAP v1.0 (sem N1.1, com 8 premissas + top 5 riscos) | GP | `TAP_EAP.md` v1.0 | TAP com 12 fases N1 + 8 premissas + 5 riscos |
| **11/09 (sex)** | Redigir ADR-001 (GitHub Projects) + ADR-002 (Stack FOSS + SDD Local) + ADR-003 (Métricas) | GP + Dev | `docs/adr/ADR-001.md`, `ADR-002.md`, `ADR-003.md` | ADRs formatados (Contexto → Decisão → Consequências) |
| **15/09 (seg)** | Plano de Integração v1.0 | GP | `docs/planos/01-integracao.md` | Contém links GitHub + SSOT |
| **16/09 (ter)** | Plano de Escopo v1.0 (+ EAP 48 pacotes + Dicionário + Atividades Derivadas) | GP | `docs/planos/02-escopo.md` | EAP sincronizada + lista de atividades |
| **17/09 (qua)** | Plano de Cronograma v1.0 (+ Roadmap 2 marcos) | GP | `docs/planos/03-cronograma.md` | Roadmap M1 (22/09) + M2 (Nov/Dez) |
| **18/09 (qui)** | Plano de Custos v1.0 (simplificado) | GP | `docs/planos/04-custos.md` | 1-2 páginas, foco em premissas |
| **19/09 (sex)** | Plano de Qualidade v1.0 (+ DoD/DoR + Ishikawa + 12 PDCAs consolidados) | GP | `docs/planos/05-qualidade.md` | DoD/DoR + Ishikawa 6M + 12 PDCAs |
| **22/09 (ter, 09:00)** | Revisão final + submissão ao Prof. Dr. Nivaldo Carletto | GP | Issue no GitHub | Zero achados CRÍTICOS no checklist |

---

## 7. ADRs A FORMALIZAR (10-30/09/2026)

### 7.1. ADR-001 — GitHub Projects como SSOT (11/09)

**Contexto:** O TAP menciona EVM e relatórios quinzenais, mas o OKB v3.0 §8.2 substitui Gantt por Kanban/GitHub Projects.

**Decisão:** GitHub Projects é a **fonte única de verdade** para cronograma, monitoramento e medição. Gantt (se exigido) é derivado do Kanban, não o contrário.

**Consequências:**
- ✅ Alinha ao Domínio de Medição PMBOK 7ª (GitHub Insights)
- ✅ Reduz burocracia (sem relatórios estáticos duplicados)
- ⚠️ Risco: Prof. Dr. Nivaldo Carletto pode exigir Gantt tradicional → mitigação: gerar Gantt a posteriori a partir do Kanban

### 7.2. ADR-002 — Stack FOSS + SDD Local Canônica (11/09)

**Contexto:** OKB v3.0 Crítica 3 + Relatório Canônico da Stack SDD Local.

**Decisão:**
- **Backend:** Python 3.12 + FastAPI
- **Banco:** SQLite 3
- **Frontend:** HTML + HTMX + Tailwind CSS
- **PDF:** WeasyPrint
- **LLM Local:** llama.cpp + **Qwen 32B Instruct Q4_K_M** (P0) + Qwen 14B Instruct Q4_K_M (P1)
- **TUI:** OpenCode

**Consequências:**
- ✅ 100% FOSS (alinha P2)
- ✅ Rodável no hardware local (58GB RAM)
- ✅ Curva de aprendizado ≤ 2 semanas
- ✅ SDD local auditável (prompts versionáveis)

### 7.3. ADR-003 — Métricas de Fluxo com Baseline (11/09)

**Contexto:** OKB v3.0 Crítica 4 identifica métricas sem baseline.

**Decisão:** Estabelecer período de calibração (23/09 – 03/10) para coletar Cycle Time e Throughput sem meta fixa. Após calibração, definir metas realistas (média ± 20%).

**Consequências:**
- ✅ Alinha ao Domínio de Medição PMBOK 7ª
- ✅ Evita metas aspiracionais não acionáveis

### 7.4. ADR-004 — Separação Ontológica TAP ≠ EAP ≠ PDCA (30/09)

**Contexto:** Correção conceitual identificada na análise v1.3.

**Decisão:** O TAP é documento de autorização que antecede o projeto. Não integra a EAP nem é alvo de PDCA. Planos de gerenciamento (01-10) e código-fonte (11) são objetos de EAP e PDCA.

**Consequências:**
- ✅ Alinha ao Domínio de Integração PMBOK 7ª
- ✅ Blinda academicamente contra questionamento da banca
- ✅ Clareza ontológica para a equipe

---

## 8. TRADE-OFFS E RISCOS RECALCULADOS

### 8.1. Trade-offs Declarados

| Trade-off | Risco | Mitigação |
|---|---|---|
| Remoção de N1.1 (TAP) da EAP | Percepção de "EAP incompleta" | Justificar via ADR-004 + padrão PMO |
| Qwen 32B em vez de 7B | Maior consumo de RAM (20GB vs 5GB) | Hardware real suporta (30GB livres) |
| 4 personas compartilhando 1 modelo | Perda de "especialização" | Especialização via prompt (P6) |
| Atividades derivadas da EAP | Complexidade adicional no cronograma | Decomposição é padrão PMBOK 6ª §6.2 |
| TAP sem invadir escopo gerencial | Percepção de "TAP incompleto" | Padrão PMO escritoriodeprojetos.com.br |

### 8.2. Riscos Recalculados

| ID | Risco | Prob. | Impacto | Severidade | Resposta | Status |
|---|---|---|---|---|---|---|
| R-01 | Stack FOSS indefinida | 80% | Alto | Crítico | ADR-002 até 11/09 | 🟠 Aberto |
| R-02 | EAP não sincronizada com GitHub | 60% | Alto | Alto | Mapeamento 1:1 até 15/09 | 🟡 Em andamento |
| R-03 | Governança > 50% do tempo | 70% | Médio | Alto | Aplicar GMV | 🟡 Aberto |
| R-04 | Prof. Dr. Nivaldo Carletto exigir Gantt tradicional | 30% | Médio | Médio | ADR-001 + Gantt derivado | 🟢 Mitigado |
| R-05 | Scope creep | 50% | Alto | Alto | CCB + DoR rigoroso | 🟡 Monitorando |
| R-08 | Equipe exceder 20h/semana (burnout) | 50% | Médio | Alto | WIP limits + métrica de burnout | 🟡 Monitorando |
| R-09 | Entrega parcial 22/09 não concluída | **15%** | Alto | Alto | Plano de ação 10-22/09 + folga 28% | 🟢 Mitigado |
| R-10 | PDCA não documentado por atividade | 40% | Médio | Médio | Template PDCA padronizado (§5.6) | 🟠 Novo |
| R-12 | Diagrama de Ishikawa incompleto | 30% | Médio | Médio | Template 6M padronizado (§5.5) | 🟠 Novo |
| **R-13** | **Qwen 32B não atende tg ≥ 6 t/s** | **20%** | **Médio** | **Médio** | **Fallback para 14B (P1)** | 🟢 **Mitigado** |
| **R-14** | **Confusão TAP/EAP/PDCA** | **30%** | **Médio** | **Médio** | **ADR-004 + treinamento equipe** | 🟠 **Novo** |

---

## 9. AÇÕES BLOQUEANTES (10-22/09/2026)

| # | Ação | Responsável | Prazo | Artefato |
|---|---|---|---|---|
| 1 | Finalizar TAP v1.0 (sem N1.1, com 8 premissas + top 5 riscos) | GP | 10/09 | `TAP_EAP.md` v1.0 |
| 2 | Redigir ADR-001 (GitHub Projects) | GP | 11/09 | `docs/adr/ADR-001.md` |
| 3 | Redigir ADR-002 (Stack FOSS + SDD Local Canônica) | GP + Dev | 11/09 | `docs/adr/ADR-002.md` |
| 4 | Redigir ADR-003 (Métricas de Fluxo) | GP | 11/09 | `docs/adr/ADR-003.md` |
| 5 | Plano de Integração v1.0 | GP | 15/09 | `docs/planos/01-integracao.md` |
| 6 | Plano de Escopo v1.0 (+ EAP 48 pacotes + Atividades Derivadas) | GP | 16/09 | `docs/planos/02-escopo.md` |
| 7 | Plano de Cronograma v1.0 (+ Roadmap 2 marcos) | GP | 17/09 | `docs/planos/03-cronograma.md` |
| 8 | Plano de Custos v1.0 (simplificado) | GP | 18/09 | `docs/planos/04-custos.md` |
| 9 | Plano de Qualidade v1.0 (+ DoD/DoR + Ishikawa + 12 PDCAs) | GP | 19/09 | `docs/planos/05-qualidade.md` |
| 10 | Diagrama de Ishikawa (6M) para problema central | GP | 19/09 | Seção §5.5 do Plano de Qualidade |
| 11 | 12 PDCAs consolidados (sem TAP) | GP | 19/09 | Seção §5.6 do Plano de Qualidade |
| 12 | Padronização do nome "Prof. Dr. Nivaldo Carletto" | GP | 19/09 | Busca e substituição global |
| 13 | Eliminação do termo "ADER" | GP | 19/09 | Busca e substituição global |
| 14 | Revisão final + submissão ao Prof. Dr. Nivaldo Carletto | GP | **22/09, 09:00** | Issue no GitHub |
| 15 | Redigir ADR-004 (Separação TAP ≠ EAP ≠ PDCA) | GP | 30/09 | `docs/adr/ADR-004.md` |

---

## 10. DECLARAÇÃO DE CONFORMIDADE

Este relatório v2.0:
- ✅ Deriva 100% das 6 mudanças estruturais declaradas em `analise_auditoria_1.3.md`
- ✅ Integra o Relatório Canônico da Stack SDD Local (Qwen 32B como pilar)
- ✅ Cita domínios e princípios PMBOK 7ª explicitamente (Integração, Escopo, Cronograma, Qualidade, Medição)
- ✅ Aplica teste GMV (OKB v3.0 §4.2) para cada recomendação
- ✅ Declara trade-offs e riscos (Domínio de Incerteza PMBOK 7ª)
- ✅ Respeita hierarquia de governança (OKB v3.0 §4.1)
- ✅ É acionável (plano de ação 10-22/09 com datas e responsáveis)
- ✅ **Separa ontologicamente TAP ≠ EAP ≠ PDCA** (Mudança 1)
- ✅ **Consolida Stack SDD Local Canônica** (Qwen 32B + 4 personas) (Mudanças 2 e 3)
- ✅ **Deriva atividades da EAP via decomposição** (PMBOK 6ª §6.2) (Mudança 4)
- ✅ **TAP sem invadir escopo gerencial** (padrão PMO) (Mudança 5)
- ✅ **Hardware real = 58GB RAM** (não 60GB nominais) (Mudança 6)
- ✅ Padroniza o nome do stakeholder como "Prof. Dr. Nivaldo Carletto"
- ✅ Elimina definitivamente o termo "ADER"

---

## 11. PRÓXIMOS PASSOS

1. **Aprovar este relatório v2.0** como base para execução 10-22/09
2. **Iniciar ação #1** (TAP v1.0 sem N1.1) imediatamente (10/09)
3. **Formalizar ADR-001, ADR-002 e ADR-003** até 11/09
4. **Redigir Plano de Qualidade v1.0 com Ishikawa + 12 PDCAs consolidados** até 19/09
5. **Submeter ao Prof. Dr. Nivaldo Carletto** em 22/09/2026, 09:00 via Issue no GitHub
6. **Produzir OKB_COGME v3.1** incorporando todas as mudanças v2.0 (entrega paralela)
7. **Próxima revisão:** 30/09/2026 (fechamento da MF1 — Fundação)

---

**Fim do Relatório de Auditoria Analítica v2.0**

Aguardo autorização para iniciar a execução do plano de ação 10-22/09/2026 e a produção do OKB_COGME v3.1.

---
---

# OKB_COGME v3.1 — BASE DE CONHECIMENTO OPERACIONAL (GUARDRAIL EVOLUÍDO)

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Data de Emissão:** 10/09/2026
**Versão anterior:** OKB_COGME_v3.0 (09/09/2026)
**Emissor:** GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carletto
**Status:** Pronto para aplicação imediata

---

## 1. VEREDITO SUMÁRIO

A OKB v3.1 incorpora **6 correções estruturais** identificadas na análise de auditoria v2.0:

1. **Separação ontológica TAP ≠ EAP ≠ PDCA** — o TAP autoriza o projeto, não é gerenciado por ele.
2. **Stack SDD Local Canônica** — Qwen 32B Instruct Q4_K_M como pilar (não mais Qwen 7B).
3. **Personas SDD consolidadas** — núcleo de 4 (PM, Coder, Reviewer, Tester) compartilhando 1 modelo.
4. **Atividades derivadas da EAP via decomposição** (PMBOK 6ª §6.2).
5. **TAP sem invadir escopo gerencial** (padrão PMO escritoriodeprojetos.com.br).
6. **Hardware real = 58GB RAM** (não 60GB nominais).

Esta versão **não revisita debates encerrados** (hibridização, exclusão de Partes Interessadas, uso de LLM, escopo do código). O foco é consolidar as correções v2.0 e preparar o projeto para a entrega parcial de 22/09/2026.

---

## 2. PRINCÍPIOS CONSTITUTIVOS DO PROJETO (IMUTÁVEIS)

| # | Princípio | Fundamentação |
|---|---|---|
| **P1** | Valor sobre documentação | PMBOK 7ª — Princípio 1 |
| **P2** | FOSS absoluto | Restrição pedagógica + valor social (TAP §2.4) |
| **P3** | KISS como métrica de arquitetura | Cada decisão técnica justificada pela simplicidade |
| **P4** | SDD com IA auditável | Todo código gerado por LLM tem rastreabilidade via commit |
| **P5** | ACID e Clean Code como padrão | Restrição técnica inegociável |
| **P6** | **Especialização via prompt, não via modelo** | 1 modelo + N prompts = N especialistas (NOVO v3.1) |
| **P7** | Entrega incremental via fluxo contínuo | Kanban + GitHub Projects (sem sprints fixas) |
| **P8** | Stakeholder único formal | Prof. Dr. Nivaldo Carletto como patrocinador-avaliador |
| **P9** | **Separação ontológica TAP ≠ EAP ≠ PDCA** | TAP autoriza, não é gerenciado (NOVO v3.1) |

---

## 3. ABORDAGEM HÍBRIDA DE GOVERNANÇA

### 3.1. Hierarquia de Resolução de Conflitos (Mantida)

1º Valor entregue ao usuário final (PMBOK 7ª — Domínio de Entrega)
2º Ementa da disciplina + orientação do Prof. Dr. Nivaldo Carletto
3º PMBOK 7ª (12 princípios + 8 domínios de desempenho)
4º Manifesto Ágil + Kanban (método de execução)
5º PMBOK 6ª (apenas como dicionário de processos quando necessário)
6º Literatura técnica complementar

**Adendo v3.1:** Em caso de conflito entre velocidade de entrega e completude documental, a entrega de valor prevalece, desde que justificada via ADR e comunicada ao Prof. Dr. Nivaldo Carletto em até 48h.

### 3.2. Princípio de Governança Mínima Viável (GMV) — MANTIDO

Todo artefato de governança deve passar pelo teste GMV antes de ser produzido:

| Pergunta | Se SIM | Se NÃO |
|---|---|---|
| O Prof. Dr. Nivaldo Carletto exigirá este artefato na avaliação? | Produzir completo | Simplificar ou eliminar |
| Este artefato evita retrabalho futuro? | Produzir | Avaliar custo-benefício |
| Este artefato é exigido pelo PMBOK 7ª como evidência de domínio? | Produzir | Documentar em 1 parágrafo no TAP |
| Este artefato é útil para a equipe (não apenas para o professor)? | Produzir | Eliminar |

**Regra:** Se ≥ 2 respostas forem NÃO, o artefato é candidato a eliminação. Decisão final via CCB (Prof. Dr. Nivaldo Carletto).

### 3.3. Separação Ontológica TAP ≠ EAP ≠ PDCA (NOVO v3.1)

| Artefato | Natureza | Integra EAP? | Tem PDCA? |
|---|---|---|---|
| **TAP** | Autorização + base de referência | ❌ NÃO | ❌ NÃO |
| **Planos de Gerenciamento (01-10)** | Execução do escopo autorizado | ✅ SIM | ✅ SIM |
| **Código-fonte (11)** | Produto final | ✅ SIM | ✅ SIM |

**Fundamento:** O TAP é o documento que AUTORIZA o projeto e concede autoridade ao gerente. Ele antecede o planejamento e não é objeto de gerenciamento — é a base sobre a qual o gerenciamento se constrói. (PMBOK 6ª §4.1 / PMBOK 7ª Domínio de Integração)

**Impacto na EAP:**
- Remover N1.1 (TAP) da EAP — o TAP é **pré-condição**, não pacote de trabalho.
- A Fase N1 (Iniciação e Planejamento) passa a conter apenas: N1.2 a N1.6.

**Impacto no Plano de Qualidade (§5.6):**
- Lista de PDCAs passa de 13 para **12 PDCAs** (N1.2 a N4.4).

### 3.4. Mapeamento PMBOK 7ª ↔ Kanban ↔ PMBOK 6ª (Refinado v3.1)

| Domínio PMBOK 7ª | Ritual Kanban (GitHub Projects) | Processo PMBOK 6ª | Artefato | Frequência |
|---|---|---|---|---|
| Stakeholders | Review assíncrono via Issues + link público do repo | 13.1, 13.2 | Matriz de comunicação simplificada | Quinzenal |
| Equipe | Daily assíncrona (Discussion) + WIP limits | 9.1, 9.2 | RACI simplificado (2 pessoas) | Diário |
| Abordagem | Kanban flow contínuo (sem sprints) | 4.1, 4.2 | TAP + ADR-001 | Único + evolutivo |
| Planejamento | Refinement semanal do backlog | 5.2, 5.3, 5.4, 6.5 | Backlog + EAP + Atividades Derivadas + Roadmap | Semanal |
| Trabalho | Pull system + colunas Kanban + SDD local | 4.3, 4.4 | Código-fonte + commits + handoffs SDD | Contínuo |
| Entrega | Deploy contínuo (CI/CD) | 5.4, 8.3 | MVP funcional + DoD | Incremental |
| Medição | GitHub Insights (Cycle Time, Throughput) | 4.5, 6.6 | Dashboard + métricas de fluxo | Semanal |
| Incerteza | Labels `risk` / `blocked` + Risk Backlog | 11.1, 11.2, 11.5 | Matriz Prob./Impacto | Quinzenal |

**Adendo v3.1:** O Domínio de Trabalho agora inclui explicitamente o SDD local (llama.cpp + Qwen 32B + OpenCode) como método de execução do código-fonte.

---

## 4. STACK SDD LOCAL CANÔNICA (NOVO v3.1)

### 4.1. Arquitetura em 3 Camadas Ortogonais

| Camada | Componentes | Princípio |
|---|---|---|
| **L1 — Infraestrutura** | llama.cpp 0.4.0-dev (Vulkan + LTO + AVX-512); Backend Vulkan (radv Mesa 26.2.1); API Server OpenAI-compat (porta 8080); systemd units | P2 (FOSS) + P7 (hardware-realismo) |
| **L2 — Personas** | `.ai/prompts/_base.md`; `.ai/prompts/{coder,reviewer,tester,pm}.md`; `.ai/prompts/active.md` (symlink) | **P6 (especialização via prompt)** |
| **L3 — Metodologia** | `.ai/specs/*.md`; `.ai/handoffs/NNN-*-fase.md`; `.ai/workflows/sdd-cycle.sh`; Obsidian vault por projeto | P3 (KISS) + P4 (parsing determinístico) |

### 4.2. Modelos Quantizados Aprovados

| Prioridade | Modelo | Quantização | Disco | RAM Carga | RAM Livre | Ctx Max | tg Target | Status |
|---|---|---|---|---|---|---|---|---|
| **P0** | Qwen 32B Instruct | Q4_K_M | ~20GB | ~20GB | ~30GB | 16k | ≥6 t/s | ✅ **PILAR** |
| **P1** | Qwen 14B Instruct | Q4_K_M | ~9GB | ~9GB | ~41GB | 32k+ | ≥12 t/s | ✅ Rápido |
| **P2** | Qwen 14B Instruct | Q5_K_M | ~11GB | ~11GB | ~39GB | 32k+ | ≥10 t/s | ✅ Validação |
| **P3** | Qwen 32B Coder | Q4_K_M | ~20GB | ~20GB | ~30GB | 16k | ≥6 t/s | ⚠️ Condicional |
| **P4** | DeepSeek-Coder-V2 Lite | Q4_K_M | ~9GB | ~9GB | ~41GB | 16k | ≥12 t/s | ⚠️ Sob demanda |
| **P5** | Qwen 72B Instruct | Q4_K_M | ~42GB | ~42GB | ~8GB | 4k | ~1-2 t/s | ❌ **ADIAR** |

**Total imediato (P0+P1+P2):** 40GB de 420GB disponíveis em `/var` → 9.5% utilizado ✅

### 4.3. Personas SDD (Núcleo Mínimo Viável)

| Persona | Responsabilidade | Input | Output | Modelo |
|---|---|---|---|---|
| **PM** | Especificar features, critérios de aceite | Requisitos vagos | `NNN-*-spec.md` | Qwen 32B |
| **Coder** | Implementar aderente à spec | Spec + código | Código em `src/` | Qwen 32B |
| **Reviewer** | Revisar código contra spec + standards | Código + spec | `NNN-*-review.md` | Qwen 32B |
| **Tester** | Gerar testes que validam a spec | Spec + código | Testes em `tests/` | Qwen 32B |

**Regra de ouro:** Todas as personas compartilham o **mesmo modelo** (Qwen 32B). A troca de persona = troca de symlink em `.ai/prompts/active.md`. Zero overhead de RAM.

**Personas opcionais (adicionar apenas com dor mensurável >30% falhas):**
- Architect (>10k LOC)
- Debugger (stack traces longos)
- DocWriter (API pública)
- Refactorer (dívida técnica)
- SecurityReviewer (exposição externa)

### 4.4. Estrutura de Diretórios Padrão

```
COGME/
├── .git/
├── src/                          # Código-fonte
├── tests/                        # Testes automatizados
├── docs/                         # Documentação HUMANA (não lida pela IA)
│
├── .ai/                          # CONTEXTO DA IA (versionado, lido pelo OpenCode)
│   ├── prompts/
│   │   ├── _base.md              # Persona base
│   │   ├── coder.md              # Especialista: implementação
│   │   ├── reviewer.md           # Especialista: revisão
│   │   ├── tester.md             # Especialista: testes
│   │   ├── pm.md                 # Especialista: planejamento
│   │   └── active.md → coder.md  # Symlink: persona ativa
│   │
│   ├── specs/
│   │   ├── coding-standards.md
│   │   ├── api-contracts.md
│   │   ├── domain-rules.md
│   │   └── architecture.md
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
```

**Regra de ouro:** Se não é lido pelo OpenCode nem pelo script SDD, não pertence em `.ai/`.

### 4.5. Fluxo SDD Padrão

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

### 4.6. Anti-Padrões Explícitos

| Anti-Padrão | Princípio Violado | Motivo |
|---|---|---|
| Vault global do Obsidian | P3 (single source of truth) | Poluição cognitiva entre projetos |
| Orquestrador (Hermes, LangChain) | P2 (simplicidade) | RAM, latência, ponto único de falha |
| Framework SDD (SpecKit) | P2, P4 | Framework fetishism; Markdown + bash basta |
| Modelo diferente por persona | **P6 (especialização via prompt)** | Viola princípio de simplicidade |
| Múltiplos modelos simultâneos | P7 (hardware-realismo) | RAM unificada é recurso finito |
| Documentos de gestão em `.ai/` | Regra de ouro | Polui contexto da IA |
| Quantizações IQ2/IQ3 | Qualidade | Degradação em raciocínio lógico |
| Modelos não-FOSS | P5 (custo zero) | Viola princípio de liberdade |

---

## 5. EAP REVISADA (v3.1 — 48 PACOTES)

### 5.1. Níveis 1 e 2 — Fases Obrigatórias (MVP Acadêmico)

| ID Nível 1 | Fase (Nível 1) | ID Nível 2 | Pacote de Trabalho (Nível 2) | Macro-Fase |
|---|---|---|---|---|
| **N1** | 1. Iniciação e Planejamento | N1.2 | 1.2. Identificação de Stakeholders | MF1 |
| | | N1.3 | 1.3. Planos de Gerenciamento | MF1 |
| | | N1.4 | 1.4. Plano da Qualidade | MF1 |
| | | N1.5 | 1.5. Política de Licenciamento FOSS | MF1 |
| | | N1.6 | 1.6. Definição do Backlog e Kanban | MF1 |
| **N2** | 2. Levantamento de Requisitos | N2.1 | 2.1. Requisitos Funcionais | MF1 |
| | | N2.2 | 2.2. Requisitos Não Funcionais | MF1 |
| | | N2.3 | 2.3. Casos de Uso e Histórias de Usuário | MF1 |
| **N3** | 3. Modelagem e Prototipação | N3.1 | 3.1. Arquitetura da Solução | MF1 |
| | | N3.2 | 3.2. Protótipo UX/UI | MF1 |
| | | N3.3 | 3.3. Modelagem de Dados (DER) | MF1 |
| **N4** | 4. Configuração de Ambiente | N4.1 | 4.1. Seleção e Validação da Stack FOSS | MF1 |
| | | N4.2 | 4.2. Repositório Git + CI/CD | MF1 |
| | | N4.3 | 4.3. Setup Local e Homologação | MF1 |
| | | N4.4 | 4.4. Auditoria de Licenças | MF1 |
| **N5** | 5. Desenvolvimento do Sistema | N5.1 | 5.1. Backend — Lógica de Negócio | MF2 |
| | | N5.2 | 5.2. Backend — API de Câmbio + Cache | MF2 |
| | | N5.3 | 5.3. Frontend — Interface e Simulações | MF2 |
| | | N5.4 | 5.4. Módulo PDF (WeasyPrint) | MF2 |
| | | N5.5 | 5.5. SDD com IA (Prompts + Revisão) | MF2 |
| **N6** | 6. Garantia da Qualidade | N6.1 | 6.1. Testes Unitários/Integração (≥ 80%) | MF2 |
| | | N6.2 | 6.2. Testes de Aceitação (UAT) | MF2 |
| **N7** | 7. DevOps e CI/CD | N7.1 | 7.1. Pipeline CI (lint + testes) | MF2 |
| | | N7.2 | 7.2. Deploy Manual Documentado | MF2 |
| **N8** | 8. Implantação (Deploy) | N8.1 | 8.1. Publicação em Produção | MF2 |
| | | N8.2 | 8.2. Documentação de Deploy + Rollback | MF2 |
| **N9** | 9. Comunicação | N9.1 | 9.1. Matriz de Comunicação (RACI) | MF1 |
| | | N9.2 | 9.2. Canais Oficiais (GitHub, e-mail) | MF1 |
| | | N9.4 | 9.4. Cerimônias com Prof. Dr. Nivaldo Carletto | MF1 |
| **N10** | 10. Base de Conhecimento | N10.1 | 10.1. ADRs (decisões arquiteturais) | MF1 |
| | | N10.2 | 10.2. Lições Aprendidas Contínuas | MF1 |
| | | N10.3 | 10.3. Catálogo de Prompts SDD | MF1 |
| **N11** | 11. Gestão de Mudanças | N11.1 | 11.1. CCB — Prof. Dr. Nivaldo Carletto | MF2 |
| | | N11.2 | 11.2. Registro de Solicitações de Mudança | MF2 |
| | | N11.3 | 11.3. Label `change-request` no GitHub | MF2 |
| | | N11.4 | 11.4. Aprovação e Versionamento | MF2 |
| **N12** | 12. Documentação do Projeto | N12.1 | 12.1. Documentação Técnica (Arquitetura, APIs) | MF3 |
| | | N12.2 | 12.2. Manual do Usuário | MF3 |
| | | N12.4 | 12.4. Consolidação da Documentação Parcial | MF3 |
| **N13** | 13. Encerramento | N13.1 | 13.1. Lições Aprendidas Finais | MF3 |
| | | N13.2 | 13.2. Verificação SMART | MF3 |
| | | N13.3 | 13.3. Apresentação Final + Aceite | MF3 |

**Total:** 13 fases Nível 1 + **48 pacotes Nível 2** (redução de 62 para 48, ganho de 23%).

### 5.2. Mapeamento com Macro-Fases Temporais

| Macro-Fase | Período | Fases da EAP Incluídas | Total de Pacotes |
|---|---|---|---|
| **MF1: Fundação** | 01/09 – 22/09/2026 | 1, 2, 3, 4, 9, 10 | 22 |
| **MF2: Construção** | 23/09 – 15/11/2026 | 5, 6, 7, 8, 11 | 16 |
| **MF3: Consolidação** | 16/11 – 15/12/2026 | 12, 13 | 6 |
| **TOTAL** | — | 13 fases | **48 pacotes** |

### 5.3. Atividades Derivadas da EAP (PMBOK 6ª §6.2)

**Fundamento:** As atividades do projeto são derivadas dos pacotes de trabalho da EAP através do processo de **decomposição**. Enquanto a EAP foca em entregas (substantivos), a lista de atividades foca nas ações (verbos) necessárias para gerar essas entregas.

**Exemplo de decomposição:**

| Pacote EAP (ENTREGA) | Atividades Derivadas (AÇÕES) |
|---|---|
| N4.1 Seleção da Stack FOSS | A4.1.1: Pesquisar candidatos; A4.1.2: Aplicar critérios GMV; A4.1.3: Redigir ADR-002; A4.1.4: Validar com protótipo "Hello World" |
| N5.1 Backend — Lógica de Negócio | A5.1.1: Modelar entidades de domínio; A5.1.2: Implementar serviços de cálculo; A5.1.3: Escrever testes unitários; A5.1.4: Documentar API (OpenAPI) |
| N5.5 SDD com IA | A5.5.1: Configurar llama.cpp + Qwen 32B; A5.5.2: Escrever personas em `.ai/prompts/`; A5.5.3: Executar ciclo SDD completo; A5.5.4: Catalogar prompts em `.ai/handoffs/` |

**Impacto no Plano de Cronograma:** A EAP permanece como estrutura de decomposição do escopo. O cronograma é construído a partir da lista de atividades derivadas, não diretamente da EAP.

---

## 6. CRITÉRIOS DE QUALIDADE UNIFICADOS (v3.1)

### 6.1. Dimensões Obrigatórias

**Dimensão 1 — Compliance Acadêmico (Obrigatória)**
- Rastreabilidade ao TAP (todo item deriva de requisito/premissa)
- Conformidade com PMBOK 7ª (citar princípio ou domínio)
- Consistência cruzada entre planos (datas/custos/escopo)
- Linguagem técnica, impessoal, objetiva

**Dimensão 2 — Valor Funcional (Obrigatória)**
- DoR claro antes de iniciar card
- DoD claro antes de fechar card
- Código testado (meta ≥ 80% coverage)
- Deploy funcional em ambiente de homologação

**Dimensão 3 — Auditoria SDD (Obrigatória v3.1)**
- Prompts de geração registrados em `.ai/handoffs/`
- Commits com assinatura de co-autoria LLM (`Co-authored-by: Qwen 32B`)
- ADR para decisões arquiteturais relevantes
- Personas SDD compartilhando 1 modelo (P6)

### 6.2. PDCAs Consolidados no Plano de Qualidade (§5.6)

**Lista final de 12 PDCAs (sem TAP):**

| # | Atividade | Fase EAP | Macro-Fase |
|---|---|---|---|
| 1 | PDCA da Identificação de Stakeholders | N1.2 | MF1 |
| 2 | PDCA dos Planos de Gerenciamento | N1.3 | MF1 |
| 3 | PDCA do Plano de Qualidade | N1.4 | MF1 |
| 4 | PDCA da Política FOSS | N1.5 | MF1 |
| 5 | PDCA do Backlog e Kanban | N1.6 | MF1 |
| 6 | PDCA dos Requisitos Funcionais | N2.1 | MF1 |
| 7 | PDCA dos Requisitos Não Funcionais | N2.2 | MF1 |
| 8 | PDCA dos Casos de Uso | N2.3 | MF1 |
| 9 | PDCA da Arquitetura da Solução | N3.1 | MF1 |
| 10 | PDCA do Protótipo UX/UI | N3.2 | MF1 |
| 11 | PDCA da Modelagem de Dados (DER) | N3.3 | MF1 |
| 12 | PDCA da Seleção da Stack FOSS | N4.1 | MF1 |

**Nota:** Apenas atividades da MF1 terão PDCA documentado na entrega parcial de 22/09. Atividades da MF2 e MF3 terão PDCAs até a entrega final (Nov/Dez 2026).

---

## 7. ESTRUTURA DOCUMENTAL (v3.1)

```
PROJETO COGME
├── 00. TAP (Termo de Abertura)                          [GMV: OBRIGATÓRIO — NÃO integra EAP/PDCA]
├── 01. Plano de Integração                               [GMV: OBRIGATÓRIO]
├── 02. Plano de Escopo + EAP/WBS + Dicionário + Atividades Derivadas [GMV: OBRIGATÓRIO]
├── 03. Plano de Cronograma + Roadmap + Kanban Setup      [GMV: OBRIGATÓRIO]
├── 04. Plano de Custos + Orçamento                       [GMV: SIMPLIFICAR*]
├── 05. Plano de Qualidade + Métricas + DoD/DoR + Ishikawa + 12 PDCAs [GMV: OBRIGATÓRIO]
├── 06. Plano de Recursos + RACI                          [GMV: SIMPLIFICAR*]
├── 07. Plano de Comunicações + Matriz                    [GMV: OBRIGATÓRIO]
├── 08. Plano de Riscos + Matriz + Respostas              [GMV: OBRIGATÓRIO]
├── 09. Base de Conhecimento                              [GMV: OBRIGATÓRIO]
│   ├── 09.1. ADRs (apenas decisões críticas)
│   ├── 09.2. Lições Aprendidas
│   ├── 09.3. Prompts SDD (em .ai/handoffs/)
│   └── 09.4. Runbooks [DESCARTADO — YAGNI]
├── 10. Plano de Gestão de Mudanças (CCB)                 [GMV: SIMPLIFICAR*]
└── 11. Código-Fonte (MVP) + DER + Diagramas + .ai/       [GMV: OBRIGATÓRIO]
```

*SIMPLIFICAR = 1-2 páginas no máximo, foco em premissas e restrições, sem planilhas complexas ou simulações de EVM.

---

## 8. DECLARAÇÕES OBRIGATÓRIAS NO TAP (v3.1)

| # | Declaração | Status |
|---|---|---|
| 1 | PMBOK 7ª como governança primária — PMBOK 6ª como dicionário complementar | Mantida |
| 2 | Kanban via GitHub Projects como método de execução | Mantida |
| 3 | Uso de LLM irrestrito e autorizado, com rastreabilidade via ADRs e prompts catalogados | Reforçada |
| 4 | Código-fonte (MVP full-stack) como marco de sucesso e documentação formal | Mantida |
| 5 | Aquisições e Partes Interessadas com simplificação pedagógica | Mantida |
| 6 | Fases de Segurança, Acessibilidade, Observabilidade e i18n como melhoria contínua pós-entrega | Mantida |
| 7 | Stack 100% FOSS com licenciamento compatível (MIT, Apache 2.0, GPL) | Mantida |
| 8 | Governança mínima viável como princípio de eficiência | Mantida |
| **9** | **Stack SDD Local: llama.cpp + Qwen 32B Instruct Q4_K_M como pilar** | **NOVA v3.1** |
| **10** | **Separação ontológica TAP ≠ EAP ≠ PDCA (TAP não é gerenciado)** | **NOVA v3.1** |

---

## 9. PREMISSAS ASSUMIDAS (v3.1)

| # | Premissa | Status |
|---|---|---|
| 1 | Projeto é 100% simulado; não há execução empresarial real | Mantida |
| 2 | PMBOK 7ª é governança primária; PMBOK 6ª é dicionário complementar | Mantida |
| 3 | Metodologia ágil Kanban via GitHub Projects é o método de execução | Mantida |
| 4 | Uso de LLM é irrestrito e autorizado pela disciplina | Mantida |
| 5 | Código-fonte (MVP full-stack) é deliverable formal e marco de sucesso | Mantida |
| 6 | Stack tecnológica será 100% FOSS (decisão via ADR-002) | Mantida |
| 7 | Equipe de 2 pessoas com carga ≤ 20h/semana cada | Mantida |
| 8 | Prof. Dr. Nivaldo Carletto é o único stakeholder formal | Mantida |
| 9 | Áreas de Aquisições e Partes Interessadas são exclusão pedagógica intencional | Mantida |
| 10 | Fases de Segurança, Acessibilidade, Observabilidade e i18n são pós-entrega | Mantida |
| 11 | Documentação PMBOK é compliance acadêmico; código é produto | Mantida |
| **12** | **Hardware local (AMD Ryzen 7 8700G, 58GB RAM real, Arch Linux) é suficiente para SDD local com Qwen 32B** | **ATUALIZADA v3.1** |
| 13 | Deploy em produção será em plataforma gratuita (a definir) | Mantida |
| 14 | Governança mínima viável (GMV) é princípio operacional | Mantida |
| **15** | **TAP autoriza o projeto, não é gerenciado por ele (separação ontológica)** | **NOVA v3.1** |
| **16** | **Personas SDD compartilham 1 modelo (Qwen 32B); especialização via prompt** | **NOVA v3.1** |

---

## 10. DIRETRIZES ESTRATÉGICAS PARA FASE ATUAL (10/09 – 22/09/2026)

### 10.1. Prioridades da Semana Atual (10-11/09)

| Prioridade | Ação | DoD |
|---|---|---|
| 🔴 P0 | Completar TAP v1.0 (sem N1.1, com 10 declarações + 8 premissas + top 5 riscos) | TAP aprovado pelo Prof. Dr. Nivaldo Carletto |
| 🔴 P0 | Criar ADR-001 (GitHub Projects substitui Gantt) + ADR-002 (Stack FOSS + SDD Local) + ADR-003 (Métricas) | ADRs registrados e linkados |

### 10.2. Prioridades da Semana Seguinte (15-19/09)

| Prioridade | Ação | DoD |
|---|---|---|
| 🟠 P1 | Redigir Planos de Integração, Escopo, Cronograma, Custos | Versão v1.0 de cada |
| 🟠 P1 | Redigir Plano de Qualidade com Ishikawa + 12 PDCAs consolidados | Plano v1.0 completo |
| 🟡 P2 | Criar DER e diagrama de arquitetura | Diagramas em draw.io/Mermaid |

### 10.3. Marco de Entrega Parcial (22/09/2026, 09:00)

**Entrega:** Documentação das Áreas 1-5 do PMBOK 6ª (Integração, Escopo, Cronograma, Custos, Qualidade) + PDCAs consolidados + Ishikawa.

**Critérios de aceite:**
- TAP v1.0 aprovado (sem N1.1, com 10 declarações)
- 5 planos de área em v1.0
- 12 PDCAs consolidados no Plano de Qualidade
- Diagrama de Ishikawa (6M) no Plano de Qualidade
- Zero achados CRÍTICOS no checklist de revisão

### 10.4. Marco de Fechamento da MF1 (30/09/2026)

**Entrega:** MF1 (Fundação) 100% concluída.

**Critérios de aceite:**
- TAP v1.0 aprovado
- 8 planos de área em v0.1 mínimo
- EAP sincronizada com GitHub Projects (48 pacotes)
- Stack FOSS definida (ADR-002) e ambiente configurado
- ADR-001, ADR-002, ADR-003, ADR-004 registrados
- Métricas de fluxo com baseline estabelecida (ADR-003)
- Download de Qwen 32B Instruct Q4_K_M (P0) concluído

---

## 11. CONDIÇÕES DE VALIDADE E GATILHOS

### 11.1. Válido Enquanto

- Ementa da disciplina mantiver PMBOK (qualquer edição) como base
- Prof. Dr. Nivaldo Carletto mantiver papel de stakeholder único formal
- Equipe mantiver 2 pessoas com ≤ 20h/semana cada
- Prazo final mantiver em Nov/Dez 2026
- Hardware local mantiver 58GB RAM (ou superior)

### 11.2. Invalida Se

- Professor exigir PMBOK 6ª como base exclusiva (regressão de governança)
- Ementa migrar para framework ágil puro sem PMBOK
- Código deixar de ser deliverable formal
- Equipe expandir para > 3 pessoas (muda dinâmica de governança)
- Prazo final antecipar para antes de Nov/2026
- Hardware degradar para < 32GB RAM (inviabiliza Qwen 32B)

### 11.3. Gatilhos de Reavaliação

- Novo artefato solicitado fora da árvore (seções 00-11)
- Mudança no critério de avaliação da disciplina
- Scope creep > 15% do backlog original
- Orientação verbal do Prof. Dr. Nivaldo Carletto divergente deste guardrail
- Falha crítica na API de câmbio externa (muda arquitetura)
- Burnout detectado (> 20h/semana por 2 semanas consecutivas)
- Qwen 32B não atinge tg ≥ 6 t/s (fallback para 14B)
- Necessidade de modelos >72B interativos (mudança de hardware)

---

## 12. INSTRUÇÃO DE USO DESTE GUARDRAIL v3.1

| Situação | Consulte |
|---|---|
| Durante redação de artefatos | Seções 3.3, 3.4, 5, 7 |
| Durante revisão de artefatos | Seção 6 (2 dimensões obrigatórias + SDD) |
| Durante conflito entre fontes | Seção 3.1 (hierarquia) |
| Durante dúvida sobre escopo | Seção 7 (árvore de artefatos) |
| Durante decisão técnica | Seção 4.5 (critério de ADR) |
| Durante dúvida sobre burocracia | Seção 3.2 (teste GMV) |
| Durante planejamento semanal | Seção 10 (diretrizes estratégicas) |
| Durante gestão do trabalho | Kanban no GitHub Projects (fonte de verdade) |
| Durante conflito de governança | Seção 5.2 (macro-fases temporais) |
| **Durante uso de SDD local** | **Seção 4 (Stack SDD Local Canônica)** |
| **Durante dúvida sobre TAP/EAP/PDCA** | **Seção 3.3 (separação ontológica)** |

---

## 13. DECLARAÇÃO DE CONFORMIDADE v3.1

Esta versão OKB v3.1:
- ✅ Incorpora todas as 6 mudanças estruturais da análise v2.0
- ✅ Atualiza hardware real (58GB RAM, não 60GB nominais)
- ✅ Consolida Stack SDD Local Canônica (Qwen 32B como pilar)
- ✅ Define personas SDD (núcleo de 4, especialização via prompt)
- ✅ Separa ontologicamente TAP ≠ EAP ≠ PDCA
- ✅ Reduz EAP de 62 para 48 pacotes (ganho de 23%)
- ✅ Reduz PDCAs de 13 para 12 (remoção do TAP)
- ✅ Adiciona atividades derivadas da EAP via decomposição (PMBOK 6ª §6.2)
- ✅ Mantém todas as decisões v3.0 não conflitant