---
id: OKB-001
title: "Base de Conhecimento Operacional do COGME — corpus único (v5.0.0)"
version: 5.0.0
class: okb
status: draft
owner: agent-architect
derived-from:
  - constitution.md v1.2.0 (Arts. 2, 4, 5, 6, 9, 10; P-01..P-13)
  - docs/planos/plano-integral-tap-1-2-3-4-5.md v1.0.0 (TAP v3 integral: §3, §4, §6, §8, §9, §11)
  - docs/decisoes/ADR-001-stack.md v1.0.0
  - docs/decisoes/ADR-002-kanban.md v1.0.0
  - docs/decisoes/ADR-003-metricas.md v1.0.0
  - docs/decisoes/ADR-004-tasklists.md v1.0.0
  - docs/decisoes/ADR-005-freeze.md v1.0.0
  - docs/decisoes/ADR-006-inteligencia-sdd.md v2.0.0
  - docs/decisoes/ADR-007-redes-de-projeto.md v1.1.0
  - docs/decisoes/ADR-008.md v1.1.0
  - docs/decisoes/ADR-009.md v1.0.0
  - docs/decisoes/ADR-010-Stack-Infraestrutura.md v1.0.0
  - docs/decisoes/ADR-011-Ecossistema-SDDAI.md v1.0.0
  - docs/decisoes/ADR-012-constituicao-como-artefato-de-governanca.md v1.0.1
  - docs/planos/plano-integracao.md v2.0.0 / plano-escopo.md v1.1.0 / plano-cronograma.md v1.2.0 / plano-custos.md v1.2.0 / plano-qualidade.md v1.1.0 / plano-recursos.md v1.0.0 / plano-comunicacoes.md v1.0.0 / plano-riscos.md v1.0.0
  - docs/conhecimento/glossario.md v3.1 (declarado; divergência com KB-INDEX — §9 OKB-C-07)
  - .ai/specs/kb-taxonomy.md v1.1.0 (KB-TAX-001)
  - docs/conhecimento/KB-INDEX.md v1.1.0
  - docs/auditorias/AUD-2610-02.md, AUD-2610-03.md, AUD-2610-04.md; docs/auditorias/vio-register.md v1.1.0
  - docs/change-requests/CR-001-m2-replanejamento.md (sem versão declarada)
  - docs/archive/legacy-md-artifact/OKB_COGME_v3.1-draft-aplicado-em-v4.md (v3.1; imutável, proveniência)
last-revised: 2026-10-30
lgpd-class: n/a
caveats:
  - "UNKNOWN-GAP: OKB v4.0.0 (23/10/2026, 594 linhas, corpus único) perdida no evento destrutivo VIO-006 (24/10 02:53:32); reemissão parte do corpo v3.0 sobrevivente + fontes citadas, nunca do texto perdido (KG-01/KG-04)."
  - "UNKNOWN-GAP: owner — KB-INDEX.md:48 registra divergência CCB (agent-docker-specialist) fundada em 'OKB §10.2 C-10', seção inexistente no corpus sobrevivente; adotado o default da taxonomia (agent-architect) até confirmação do CCB."
  - "UNKNOWN-GAP: frontend canônico — ADR-001 v1.0.0 fixa HTML5/CSS3/JS vanilla; registry.yaml (agent frontend) e VIO-001 registram Jinja/HTMX/Tailwind; sem ADR de emenda (§9 OKB-C-10)."
  - "UNKNOWN-GAP: fechamento de M2 sem evidência em FS (MF2-licoes 0 B; baseline 0 B); CR-001 repactua M2 para 15/11/2026 sem ADR e colide com M3 (§9 OKB-C-06)."
  - "UNKNOWN-GAP: glossário — cabeçalho v3.1 (20/09) contra 3.2.0 declarado no KB-INDEX; corpo ainda afirma 13 fases/48 pacotes, Qwen 32B e SQLite (§9 OKB-C-07)."
  - "UNKNOWN-GAP: baseline de métricas 0 B — metas da ADR-003 permanecem provisórias (não calibradas) até popular docs/metricas/baseline.md."
  - "DEFEITO CRÍTICO (OKB-C-21): constitution.md v1.2.0 apresenta os Arts. 5–10 em duplicidade (duas redações no mesmo arquivo); consolidação é ato exclusivo do Humano (Art. 5.2) e não foi executada por agente."
  - "UNKNOWN-GAP: docs/tap/TAP.md, docs/requisitos/requisitos.md e .ai/specs/{tap,eap,requisitos}.md em 0 B; TAP canônico vive no plano-integral (docx = export derivado)."
  - "Documento CANDIDATO: somente substitui o corpus vivo após ratificação CCB (Art. 5.1). Não altera ADRs, o TAP congelado (ADR-005) nem a Constituição."
---

# OKB v5.0.0 — Base de Conhecimento Operacional (corpus único)

| Campo | Valor |
|---|---|
| Versão | 5.0.0 |
| Status | draft — candidato canônico; ratificação CCB pendente |
| Data-base (as-of) | 30/10/2026 |
| Decisor da ratificação | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Substitui | OKB v3.0 (20/09/2026, corpus vivo) e a linhagem v3.1 (22/09) / v4.0.0 (23/10, perdida em VIO-006) |
| Hierarquia vigente | `constitution.md` v1.2.0 > TAP v3 congelado (ADR-005) > ADRs 001–012 > **OKB** > Planos > Glossário > Specs > Código |
| Custódia | agent-architect (default KB-TAX-001) — divergência anterior em aberto (ver caveats) |
| LGPD | n/a (sem PII — P-04) |

---

## 0. LEITURA E REGRAS DE USO

### 0.1 O que este documento é

O OKB é a **base de conhecimento técnico-aplicada** do COGME (classe `okb`, KB-TAX-001 §2): consolida stack, hardware, método, configuração do SSOT e o estado canônico dos artefatos. Ele **não cria norma autônoma**: operacionaliza a Constituição, o TAP congelado e as ADRs (Art. 2.3).

### 0.2 Regras de leitura

1. **Toda afirmação normativa cita fonte e versão pinada** — `ADR-NNN vX.Y.Z`, `plano-X vX.Y`, `TAP §N`. Alegação sem fonte é `UNKNOWN-GAP` (P-08).
2. **Metadado honesto:** a seção §4 registra a versão *real* encontrada no arquivo, não a versão *declarada* pelo índice. Divergência é defeito rastreado (§9), nunca silenciada.
3. **Hierarquia absoluta:** em conflito, vale o Art. 2 da Constituição v1.2.0, não a ordem interna de versões anteriores do OKB (§1.1 corrige a ordem praticada até 20/09).
4. **Congelamento:** este documento não edita o TAP (ADR-005). Divergências do TAP são lidas via Notas de Contexto do Plano de Cronograma §3.8, nunca "corrigidas".

### 0.3 O que mudou nesta versão (v3.0 → v5.0.0)

| # | Mudança | Motivo |
|---|---|---|
| 1 | Frontmatter de 10 campos (KB-TAX-001 §1) | v3.0 não tinha metadados; classe `okb` exige DoR |
| 2 | Hierarquia corrigida (Constituição no topo; ADRs acima do OKB) | v3.0:5 dizia "TAP > OKB > Glossário > ADRs" — conflito com Art. 2.1 |
| 3 | Catálogo de ADRs 001–012 (era 001–004) | 8 ADRs emitidas/ratificadas em 28–29/10 |
| 4 | Estado canônico as-of 30/10 (stack ADR-010, LLM ADR-006, agentes ADR-011) | v3.0 refletia 20/09 |
| 5 | Inventário de artefatos com versão real vs declarada | consolidação realista de metadados |
| 6 | 27 labels (corrige "23" interno) | §2 de v3.0:51 contradizia §9.1:466 |
| 7 | Registro de inconsistências e pendências (§9) | auditorias AUD-2610-02/03/04 + VIO-006 |
| 8 | Padrão de citação com versão + lista de patch | versionamento das menções internas |
| 9 | P9 incluída nas premissas (era P1–P8) | TAP §9 tem 9 premissas |
| 10 | "Próximos passos pré-M1" substituído por estado as-of | cronograma de 21/09 estava obsoleto |

---

## 1. DECLARAÇÃO DE GOVERNANÇA

### 1.1 Hierarquia normativa (constitution.md v1.2.0, Art. 2)

**Ramo de projeto (escopo/negócio):**

1. `constitution.md` (lei suprema — ADR-012)
2. TAP v3, congelado pela ADR-005 (18/09/2026)
3. ADRs aprovadas (`docs/decisoes/`) — podem sobrepor-se parcialmente entre si, nunca à Constituição nem ao TAP
4. **OKB** (este documento) — conhecimento operacional, sem autonomia normativa
5. Planos de gerenciamento (`docs/planos/`)
6. Glossário (`docs/conhecimento/glossario.md`)
7. Especificações SDD e inputs canônicos (`.ai/specs/`)
8. Código-fonte e testes (`src/`, `tests/`)

**Ramo de forja (agentes/SDD):**

1. `constitution.md`
2. Diretiva AFA-ULTIMATE
3. ADRs de governança de agentes + roster (`.ai/agents/registry.yaml`)
4. Personas, specs, handoffs, ledger e MCPs
5. Scripts e código de agentes

> **Nota de correção:** a ordem praticada até o OKB v3.0 ("TAP > OKB > Glossário > ADRs") está **revogada**. ADRs são camada 3 e o Glossário é camada 6 (achado F-04 de AUD-2610-03; ver OKB-C-01).

### 1.2 Autoridade de mudança (CCB)

| Item | Definição | Fonte |
|---|---|---|
| CCB | GP Leonardo (membro único) | TAP v3 §1.c; Premissa P7 |
| Stakeholder-avaliador | **Prof. Dr. Nivaldo Carleto** (grafia imutável) | ADR-008 v1.1.0 |
| Instrumentos de ratificação | CCB-001 (ADRs 006–011 + 007/008/009/010) e CCB-002 (ADR-012), 29/10/2026 | cabeçalhos das ADRs |
| Emenda constitucional | proposta → parecer de auditoria → CCB → bump + changelog + co-assinatura | Art. 9.1; Art. 5.4 |
| Emenda de ADR | CR + CCB + ADR (MAJOR se alterar marco oficial) | OKB §2.4; plano-custos §4.5/§4.6 |

### 1.3 Obsolescência declarada do PMBOK 6ª

PMBOK® 7ª é a governança primária (princípios + domínios). PMBOK® 6ª é **dicionário de processos**, citado apenas para rastreabilidade acadêmica. EVM/SPI/CPI são **LEGADO — NÃO APLICÁVEIS** (ADR-003 v1.0.0): orçamento zero inviabiliza CPI (AC = 0) e o fluxo contínuo inviabiliza PV.

### 1.4 Regime de freeze do TAP (ADR-005 v1.0.0)

1. O TAP **não é revisado** ao longo do ciclo (última versão 18/09/2026).
2. Em divergência intra-TAP, a **seção §6 (Marcos)** é canônica para matéria temporal.
3. As **Notas de Contexto (NC)** do Plano de Cronograma §3.8 são o locus de leitura operacional — nunca "correção" do TAP.
4. ADR-005 está em **regularização tardia**: decisão efetiva 21/09/2026 (NC-00), formalização 28/10/2026, **ratificação CCB pendente** (OKB-C-12).

### 1.5 Estratégia de entrega faseada dos planos

| Marco | Plano original | Planos entregues | Observação as-of 30/10 |
|---|---|---|---|
| M1 (22/09/2026) | 5 planos | Integração, Escopo, Cronograma, Custos, Qualidade | ✅ corpos em FS (v1.1–v2.0) |
| M2 (30/09/2026) | 3 planos | Recursos, Comunicações, Riscos | ⚠️ corpos em FS (v1.0), mas **fechamento de M2 sem registro** e data repactuada por CR-001 (OKB-C-06) |

Trade-off declarado: redução de ~30% da carga documental do M1 em favor da qualidade dos 5 planos-base e da configuração do SSOT (tailoring — PMBOK 7ª, Domínio de Abordagem de Desenvolvimento).

---

## 2. REGIME DE DECISÕES (ADRs)

### 2.1 Catálogo canônico ADR-001 … ADR-012 (as-of 30/10/2026)

| ADR | Título | Versão | Status | Decisão | Formalização | Custódia |
|---|---|---|---|---|---|---|
| ADR-001 | Stack Tecnológica FOSS | 1.0.0 | Finalizado | 19/09/2026 | 28/10/2026 | agent-architect |
| ADR-002 | Kanban como Método de Execução | 1.0.0 | Finalizado | 19/09/2026 | 28/10/2026 | agent-pm (operação) + agent-architect |
| ADR-003 | Métricas de Fluxo (substituição de EVM) | 1.0.0 | Finalizado | 19/09/2026 | 28/10/2026 | agent-pm (coleta) + agent-architect (definição) |
| ADR-004 | Tasklists Markdown (rejeição de subissues) | 1.0.0 | Finalizado | 20/09/2026 | 28/10/2026 | não declarada (autor 1.0.0: agent-architect) |
| ADR-005 | Freeze do TAP e precedência intra-TAP | 1.0.0 | Regularização tardia — ratificação pendente | 21/09/2026 (NC-00) | 28/10/2026 | agent-architect + agent-pm (NCs) |
| ADR-006 | Módulo de Inteligência SDD (modelo, fallback, cloud FREE) | 2.0.0 | Finalizado (CCB-001) | 26/10/2026 | 29/10/2026 | agent-nexus-prime-ultimate |
| ADR-007 | Redes de Projeto (dualidade CPM × Kanban) | 1.1.0 | Aprovado (CCB-001) | 29/10/2026 | 29/10/2026 | agent-scheduler |
| ADR-008 | Grafia canônica do stakeholder-avaliador | 1.1.0 | Aprovado (CCB-001) | 29/10/2026 | 29/10/2026 | agent-comms + project-auditor |
| ADR-009 | Contagem canônica da EAP (12 fases + 37 pacotes) | 1.0.0 | Aprovado (CCB-001) | 29/10/2026 | 29/10/2026 | agent-scope-manager + project-auditor |
| ADR-010 | Stack de Infraestrutura (PostgreSQL/Docker/Nginx/APIs) | 1.0.0 | Aprovado (CCB-001) | 29/10/2026 | 29/10/2026 | agent-backend-dev + agent-devops |
| ADR-011 | Ecossistema SDD (MCPs, memória, L1/L2/L3) | 1.0.0 | Aprovado (CCB-001) | 29/10/2026 | 29/10/2026 | agent-nexus-prime-ultimate + agent-architect |
| ADR-012 | Constituição como artefato normativo supremo | 1.0.1 | Aprovado (CCB-002) | 29/10/2026 | 29/10/2026 | GP Leonardo (guardião) |

### 2.2 Cadeia de sobreposição (supersede)

| Decisão | Sobreposta por | Natureza | Efeito prático no OKB |
|---|---|---|---|
| ADR-001 (SQLite; LLM "QwenStudio") | ADR-010 v1.0.0 (parcial) | banco canônico → PostgreSQL 15+ | §3.3 adota PostgreSQL; SQLite só em testes isolados |
| ADR-001 (LLM) | ADR-006 v2.0.0 (parcial) | modelo primário → Qwen3-30B-A3B | §3.4 adota MoE + fallback 14B |
| ADR-003 (EVM legado; redes "obsoletas") | ADR-007 v1.1.0 (parcial) | CPM autorizado no nível macro/acadêmico | §3.7 registra dualidade "a rede valida o marco; o Kanban executa a tarefa" |
| ADR-008 v1.0.0 (grafia viciada, duplo "t") | ADR-008 v1.1.0 (total) | grafia canônica "Carleto" | §1.2 e todo o corpus |
| ADR-002 (WIP) | Constitution v1.2.0 Art. 6.2 | compatível: "WIP ≤ 3 **por pessoa**" | §6.2 |
| Todas as ADRs | ADR-012 v1.0.1 | subordinação à Constituição | §1.1 |

### 2.3 Gatilhos para nova ADR (teste de 4 perguntas)

Uma decisão exige ADR se atender **≥ 2** critérios; 1 critério → commit `decision:`; 0 → não registrar.

| # | Critério | Teste |
|---|---|---|
| G1 | Impacto transversal | Afeta ≥ 2 fases da EAP ou ≥ 2 planos? |
| G2 | Irreversibilidade prática | Reverter custa > 8h de retrabalho? |
| G3 | Questionabilidade acadêmica | O Prof. Dr. Nivaldo Carleto pode questionar no marco? |
| G4 | Trade-off não óbvio | Abre mão de alternativa viável com justificativa não trivial? |

**Gatilhos negativos:** lint/formatação (`.editorconfig`), nome de variável, ajuste textual sem mudança de escopo, decisão já coberta por ADR, operação diária (Daily).

### 2.4 ADR tardia — política de regularização

| Condição | Ação | Prazo |
|---|---|---|
| Implementada há ≤ 48h e ≥ 2 gatilhos | ADR tardia com nota "Regularização: aplicada em [data], formalizada em [data]" | ≤ 24h |
| Implementada há > 48h e ≥ 2 gatilhos | ADR tardia + lição aprendida | ≤ 72h |
| Apenas 1 gatilho | commit `decision:` | imediato |
| 0 gatilhos | não registrar | — |

Campos obrigatórios da ADR tardia: `Tipo`, `Data da decisão efetiva`, `Data da formalização`, `Motivo da tardança`, `Lição aprendida`. Casos vigentes: **ADR-005** é a única autodeclarada tardia (efetiva 21/09 → formalizada 28/10); **ADR-006** tem hiato de 3 dias entre decisão (26/10) e formalização (29/10), sem autodeclaração. Proporção declarada: 1/12 ≈ 8%; proporção ampliada (incluindo hiatos > 48h): 2/12 ≈ 17% — ambas abaixo do limiar de alerta de 30%.

### 2.5 Limite de ADRs por marco (GMV) — **em violação declarada**

| Marco | Limite declarado (v3.1 §6.4) | Emitidas | Situação |
|---|---|---|---|
| M1 | 4 (001–004) | 4 | ✅ |
| M2 | ≤ 2 | 8 (005–012) | ❌ excedido |
| M3 | ≤ 3 | 0 (até 30/10) | — |
| M4 | ≤ 1 | 0 | — |
| **Total** | **≤ 10** | **12** | ❌ **OKB-C-05** |

**Leitura registrada (não decisão):** o excedente decorre da onda de consolidação constitucional de 28–29/10 (reemissão das ADRs perdidas + 7 ADRs novas). Duas saídas legítimas, ambas exigindo CCB: (a) revisar o teto para ≤ 14 por emenda à política; ou (b) classificar 006–012 como "emendas constitucionais derivadas" (ADR-012), fora da contagem GMV. **Nenhuma das duas foi decidida** — pendência em §9.

---

## 3. ESTADO CANÔNICO DO PROJETO (as-of 30/10/2026)

### 3.1 Escopo e EAP

| Item | Valor canônico | Fonte |
|---|---|---|
| EAP | **12 fases (N1–N12) + 37 pacotes de nível 2** | ADR-009 v1.0.0; TAP §4 |
| Macro-fases | MF1 Fundação (N1–N4, N8, N9, N10 parcial); MF2 Construção (N5–N7, N10); MF3 Consolidação (N11, N12) | OKB §7.2 (labels de macro-fase); plano-integral:337. **Distribuição de pacotes por MF = `UNKNOWN-GAP`** (Figuras 7–9 são placeholders) |
| Escopo do produto | simulação cambial, 5 regimes de contratação, spread/IOF, invoice PDF | TAP §2; Art. 1.2 |
| "13 fases / 48 pacotes" | **não canônico** — resíduo volátil do Glossário v3.1:18 | ADR-009; NC-Q4 (plano-qualidade §5.9) |
| 13ª fase "Encerramento Administrativo" | subsumida em N12 | ADR-009 §Decisão 2 |

### 3.2 Marcos (TAP §6, congelado) e situação real

| Marco | Data canônica | Critério de aceite | Situação as-of 30/10 |
|---|---|---|---|
| M1 — Entrega Parcial Documental | 22/09/2026 | 5 planos + 12 PDCAs + Ishikawa, sem achados críticos | Documentos em FS; aceite acadêmico não registrado em FS |
| Calibração (auxiliar) | 03/10/2026 | Baseline de métricas | ❌ `docs/metricas/baseline.md` = 0 B (OKB-C-08) |
| M2 — Ambiente e Modelagem | 30/09/2026 (TAP) | CI verde + DER + UX/UI versionados | ⚠️ vencido sem registro de fechamento; CR-001 propõe 15/11/2026 (OKB-C-06) |
| M3 — MVP Funcional (Beta) | 15/11/2026 | coverage ≥ 80%, UAT sem defeitos críticos | Risco ativo: nenhum card de construção no quadro (plano-riscos Q-02:117) |
| M4 — Encerramento | 15/12/2026 | documentação consolidada + aceite formal | — |

> **Conflito declarado:** CR-001 (M2 → 15/11/2026) colide com M3 (15/11/2026) e não foi refletido nos planos nem formalizado em ADR. Prevalece a data do TAP §6 (ADR-005) até decisão do CCB.

### 3.3 Stack efetiva (ADR-001 v1.0.0 + ADR-010 v1.0.0)

| Camada | Componente canônico | Licença | Observação |
|---|---|---|---|
| Linguagem/Backend | Python 3.11 + FastAPI (async) | PSF/MIT | Uvicorn por container |
| Banco | **PostgreSQL 15+** (asyncpg + SQLAlchemy async + Alembic) | PostgreSQL License | SQLite **revogado** como banco canônico (ADR-010); uso só em teste isolado |
| Orquestração | Docker + Docker Compose (`db`, `web`, `proxy`) | Apache-2.0 | paridade dev/test/prod |
| Proxy | Nginx (latente, perfil opcional) | BSD-2 | pronto para TLS futuro |
| PDF | WeasyPrint | BSD-3 | deps nativas glibc/Pango |
| Testes | pytest + coverage.py (≥ 80%) | MIT | CI por push |
| CI/CD | GitHub Actions Free Tier | proprietário gratuito | **Bypass registrado** (P-01) |
| Frontend | ⚠️ **conflito aberto**: ADR-001 = HTML5/CSS3/JS vanilla; registry = Jinja + HTMX + Tailwind | — | OKB-C-10 |
| APIs de câmbio | Circuit Breaker: Frankfurter (primária) → fallbacks → **PTAX/BCB obrigatório** | MIT/CC0 | ADR-010 §4 |
| LLM | ver §3.4 | Apache-2.0 | ADR-006 |

**Regra de mudança de stack:** CR + ADR específica + CCB + ADR MAJOR; nenhum componente trocado por conveniência (ADR-001 §Governança; plano-custos §4.5/§4.6). Drift silencioso = incidente.

### 3.4 SDD, LLM e hardware (ADR-006 v2.0.0 + ADR-011 v1.0.0 + P-02)

| Item | Valor canônico |
|---|---|
| Hardware | AMD Ryzen 7 8700G (Zen 4, 8C/16T, AVX-512); Radeon 780M (RDNA 3); **58 GB RAM reais**; limite de inferência 32 GB via systemd; Arch Linux; Vulkan 1.4.354 / Mesa 26.2.2 |
| Motor | `llama.cpp` compilado com Vulkan + LTO + AVX-512 |
| Modelo primário | **Qwen3-30B-A3B Q4_K_M** (MoE: 30B totais, ~3B ativos, ~18 GB disco, ~4 GB RAM ativa) — Apache-2.0 |
| Fallback local | Qwen 14B Q4_K_M (denso, ~9 GB) via symlink `.ai/personas/active.md` |
| Deferred | Qwen 72B Q4_K_M (não baixar sem necessidade comprovada) |
| Deprecated | Qwen3.8-27B Q4_K_M — backup forense, proibido em uso ativo (INC-F01) |
| Contexto | 32.768 tokens configurados; **orçamento efetivo 24.000** (75%); output máx. 4.096 |
| Performance alvo | ≥ 12 t/s geração; ≥ 25 t/s prompt; TTFT < 2 s |
| Cloud | free tier **apenas dados não sensíveis**, whitelist (HF, OpenRouter, Groq, GitHub Models) — P-02 revisado, Art. 7.4 |
| Camadas | L1 infraestrutura (imutável por agentes) · L2 personas · L3 metodologia (única mutável diariamente) |
| Memória | `ledger.yaml` (schema v2.0) + handoffs JSON + specs imutáveis + lições por MF |
| MCPs | `nexus-ledger`, `nexus-dispatch`, `nexus-validate`, `nexus-kb` (Python stdlib + PyYAML) |

### 3.5 Agentes e forja

| Item | Regra |
|---|---|
| Roster SSOT | `.ai/agents/registry.yaml` (validado por `scripts/sync_agent_registry.py --check`) |
| Topologia | `scripts/validate_nexus_yaml.py` (camadas L1–L3, half-duplex) |
| Forja | exclusiva AFA-ULTIMATE (Art. 4.1) — agentes não forjam agentes |
| Auto-delegação | proibida (sender ≠ target) |
| Kill switch | herdado por todo envelope; 15 vetores (Art. 4.6) |
| Custo-benefício | P-09: nenhum papel opera abaixo do custo-benefício |

---

## 4. INVENTÁRIO DE ARTEFATOS E METADADOS

### 4.1 Artefatos vivos (versão real × versão declarada)

Legenda: **real** = extraído do cabeçalho/frontmatter do arquivo em 30/10/2026; **índice** = `KB-INDEX.md` v1.1.0.

| ID / classe | Caminho | Versão real | Status real | Índice declara | Divergência |
|---|---|---|---|---|---|
| Lei | `constitution.md` | 1.2.0 | VIGENTE-INTERINA | não indexada | co-assinatura pendente (OKB-C-15) + **Arts. 5–10 duplicados** (OKB-C-21) |
| TAP (export) | `docs/tap/TAP.docx` | 18/09/2026 | congelado | — | `TAP.md` = 0 B e declarado "não-0B" no índice (OKB-C-09) |
| plano-integral | `docs/planos/plano-integral-tap-1-2-3-4-5.md` | 1.0.0¹ | ativo | 1.0.0 active | sem carimbo de versão no corpo |
| Plano de Projeto | `docs/planos/Plano-de-Projeto-COGME_v1.0.md` | 1.0.0¹ | ativo | 1.0.0 active | docx v1.1 concorrente — decisão CCB pendente |
| Integração | `docs/planos/plano-integracao.md` | 2.0 | ativo | 2.0.0 active | normalizar 2.0 → 2.0.0 |
| Escopo | `docs/planos/plano-escopo.md` | 1.1 | ativo | 1.1.0 active | normalizar |
| Cronograma | `docs/planos/plano-cronograma.md` | 1.2 | ativo | 1.2.0 active | normalizar |
| Custos | `docs/planos/plano-custos.md` | 1.2 | ativo | 1.2.0 active | normalizar |
| Qualidade | `docs/planos/plano-qualidade.md` | 1.1 | ativo | 1.1.0 active | normalizar |
| Recursos | `docs/planos/plano-recursos.md` | 1.0¹ | ativo | 1.0.0 active | sem carimbo |
| Comunicações | `docs/planos/plano-comunicacoes.md` | 1.0¹ | ativo | 1.0.0 active | sem carimbo |
| Riscos | `docs/planos/plano-riscos.md` | 1.0¹ | ativo | 1.0.0 active | sem carimbo |
| ADR-001..004 | `docs/decisoes/ADR-00{1..4}-*.md` | **1.0.0** | Finalizado | **1.1.0 ratified** | índice desatualizado (OKB-C-02) |
| ADR-005 | `docs/decisoes/ADR-005-freeze.md` | 1.0.0 | ratificação **pendente** | 1.0.0 ratified | índice desatualizado (OKB-C-12) |
| ADR-006 | `docs/decisoes/ADR-006-inteligencia-sdd.md` | 2.0.0 | Finalizado (CCB-001) | **ausente** | + 2 cópias idênticas (OKB-C-04) |
| ADR-007 | `docs/decisoes/ADR-007-redes-de-projeto.md` | 1.1.0 | Aprovado (CCB-001) | ausente | — |
| ADR-008 | `docs/decisoes/ADR-008.md` | 1.1.0 | Aprovado (CCB-001) | ausente | — |
| ADR-009 | `docs/decisoes/ADR-009.md` | 1.0.0 | Aprovado (CCB-001) | ausente | — |
| ADR-010 | `docs/decisoes/ADR-010-Stack-Infraestrutura.md` | 1.0.0 | Aprovado (CCB-001) | ausente | — |
| ADR-011 | `docs/decisoes/ADR-011-Ecossistema-SDDAI.md` | 1.0.0 | Aprovado (CCB-001) | ausente | — |
| ADR-012 | `docs/decisoes/ADR-012-constituicao-...md` | 1.0.1 | Aprovado (CCB-002) | ausente | — |
| OKB | `docs/conhecimento/OKB.md` | **3.0** | Ativa (20/09) | **4.0.0 active** | OKB-C-02 (este candidato = 5.0.0) |
| Glossário | `docs/conhecimento/glossario.md` | **3.1** | Atualizado (20/09) | **3.2.0 active** | OKB-C-07/OKB-C-17 |
| KB-INDEX | `docs/conhecimento/KB-INDEX.md` | 1.1.0 | active | 1.1.0 | coerente, porém desatualizado em 9 linhas |
| Taxonomia | `.ai/specs/kb-taxonomy.md` | 1.1.0 | ratified | 1.1.0 | coerente |
| Requisitos | `docs/requisitos/requisitos.md` | 0 B | — | 1.0.0 draft (ponteiro) | 0 B (OKB-C-08) |
| Baseline | `docs/metricas/baseline.md` | 0 B | — | 1.0.0 draft | 0 B (OKB-C-08) |
| Dependências | `docs/dependencias/registro.md` | 0 B | — | 1.0.0 draft | 0 B (OKB-C-08) |
| Specs SDD | `.ai/specs/{tap,eap,requisitos}.md` | **0 B** | — | 1.0.0 draft "preenchidas" | drift grave (OKB-C-08) |
| Lições MF1/MF2/MF3 | `docs/conhecimento/licoes-aprendidas/` | 1,9 KB / 0 / 0 | sem frontmatter | licoes (não indexadas) | MF2/MF3 0 B |
| CR-001 | `docs/change-requests/CR-001-m2-replanejamento.md` | sem versão | aprovado "neste prompt" | não indexado | sem registro formal (OKB-C-06) |
| VIO register | `docs/auditorias/vio-register.md` | 1.1.0 | active | não indexado | — |
| Auditorias | `docs/auditorias/AUD-2610-0{2,3,4}.md` | 1.0.0 | active | não indexado | classe `relatorio-auditoria` fora do enum KB-TAX (OKB-C-13) |

¹ versão inferida do índice porque o corpo não carrega campo de versão.

### 4.2 Artefatos anômalos (apenas registro)

| Caminho | Anomalia | Ação |
|---|---|---|
| `docs/decisoes/ADR-006-chunk-1.md` e `ADR-006-chunk-aa` (sem extensão) | byte-idênticos a ADR-006 v2.0.0 (md5 `91e91ef1…`) | arquivar/excluir na rodada de normalização |
| `docs/decisoes/_consolidado-adrs.tmp.md` | artefato temporário de análise (ADR-001..012) | descartar após uso (autorizado) |
| `docs/planos/.~ano-de-Projeto-COGME_v2.0.1-ONGOING.docx` | lock temporário de editor | remover |
| `docs/planos/Plano-de-Projeto-COGME_v2.0{,.1}-ONGOING.docx` | export/docx concorrente sem `.md` canônico | decisão CCB (R-03) |
| `argparse` (raiz, 16 MB) | binário de 30/10 sem relação com o escopo | avaliar remoção (drift) |

### 4.3 Classes sem artefato vivo completo

| Classe | Estado | Gap |
|---|---|---|
| `requisito` | ponteiro 0 B | popular em `.ai/specs/requisitos.md` e espelhar |
| `log-baseline` | 2 stubs 0 B | popular baseline e registro de dependências |
| `licoes` | 1 de 3 arquivos | MF2/MF3 0 B |
| `diagrama` | PNG+SVG por área | EAP com placeholders; fonte SVG/Mermaid exigida |

---

## 5. PREMISSAS E RESTRIÇÕES VIGENTES

### 5.1 Premissas do TAP v3 §9 (P1–P9)

| ID | Premissa | Status |
|---|---|---|
| P1 | Governança híbrida (PMBOK 7ª + 6ª dicionário + Kanban) | vigente |
| P2 | FOSS absoluto (com Bypass registrado — P-01) | vigente |
| P3 | SDD com IA auditável | vigente |
| P4 | Código-fonte é deliverable formal | vigente |
| P5 | 20 h/semana por membro | vigente |
| P6 | Hardware adequado e suficiente | revisada (58 GB reais) |
| P7 | GP = CCB único; Prof. Dr. Nivaldo Carleto = avaliador de marcos | vigente |
| P8 | Aquisições e partes interessadas simplificadas | vigente |
| P9 | Separação ontológica TAP ≠ EAP ≠ PDCA | vigente |

> **Correção:** o OKB v3.0 listava apenas P1–P8; P9 (base da ADR-005) faltava.

### 5.2 Princípios constitucionais (P-01…P-13, constitution.md v1.2.0)

| ID | Princípio | Efeito operacional |
|---|---|---|
| P-01 | FOSS zero-cost | dependência proprietária só com Bypass (3 pilares) |
| P-02 | Soberania local com flexibilização controlada | inferência local primária; cloud free tier só dados não sensíveis |
| P-03 | Soberania de dados | zero telemetria, zero lock-in |
| P-04 | LGPD primária | mínimo necessário; sem PII em artefatos |
| P-05 | Traces | toda decisão não trivial gera ADR/registro; silêncio = defeito |
| P-06 | Qualidade fechada | coverage ≥ 80%; gates reviewer → gatekeeper |
| P-07 | Segurança | OWASP baseline; fail-closed |
| P-08 | Honestidade | alegação sem fonte = KNOWLEDGE GAP |
| P-09 | Anti-subutilização | papéis com custo-benefício comprovado |
| P-10 | Linguagem | EN para código/contratos; PT-BR para humano |
| P-11 | YAGNI | nada sem demanda do ciclo atual |
| P-12 | Primeiros princípios | pressuposto não fundamentado = gap declarado |
| P-13 | Precisão linguística | sem ambiguidade normativa |

> **Alerta de namespace (OKB-C-19):** as premissas do TAP (P1–P9) e os princípios constitucionais (P-01…P-13) usam a **mesma letra com semânticas distintas** (ex.: TAP P6 = hardware; P-06 = qualidade; TAP P3 = SDD; P-03 = soberania de dados). Recomendação para a rodada de normalização: prefixar `TAP-P#` e `C-P-##` em todo o corpus.

### 5.3 Restrições (TAP §8 e §11)

Escopo restrito ao MVP acadêmico; prazo letivo inegociável; **orçamento R$ 0,00**; equipe de 3 pessoas com múltiplos papéis; stack 100% FOSS (com Bypass registrado); licenciamento final open source (MIT/GPL).

---

## 6. MÉTRICAS E FLUXO

### 6.1 Métricas oficiais (ADR-003 v1.0.0)

| Métrica | Definição | Meta | Frequência | Estado |
|---|---|---|---|---|
| Cycle Time | Done − In Progress (NC-Q3) | ≤ 3 dias | semanal | ⚠️ provisória (sem baseline) |
| Throughput | cards concluídos/semana | ≥ 5 | semanal | ⚠️ provisória |
| CFD | bandas do fluxo acumulado | sem bandas largas | semanal | ✅ nativo (GitHub Insights) |
| WIP | cards em In Progress | ≤ 3 **por pessoa** (≤ 9 total) | contínuo | ✅ Art. 6.2 |
| Coverage | linhas testadas/totais | ≥ 80% | por push (CI) | ✅ P-06 |

**Métricas LEGADO:** SPI, CPI, EVM — não aplicáveis.

### 6.2 Calibração e baseline

Período 23/09–03/10/2026 encerrado **sem baseline registrada** (`docs/metricas/baseline.md` = 0 B). Consequência: as metas acima são **aspiracionais**, não calibradas; qualquer comparação de desempenho é `UNKNOWN-GAP` até a baseline existir (OKB-C-16).

---

## 7. SSOT OPERACIONAL (GitHub Projects)

### 7.1 Fluxo e WIP

Colunas `Backlog → Ready (DoR) → In Progress → Code Review → Done (DoD)`; pull system; WIP ≤ 3 por pessoa (Art. 6.2); sem sprints (ADR-002).

**Rituais:** Daily assíncrona (Issues, 15 min/dia); Refinement semanal (30 min); Retrospectiva quinzenal (risk backlog + lições).

### 7.2 Labels — 27 em 5 categorias

| Categoria | Qtd | Labels |
|---|---|---|
| Tipo de trabalho | 6 | `feat` `bug` `docs` `test` `ci` `chore` |
| Macro-fase EAP | 3 | `MF1-fundacao` `MF2-construcao` `MF3-consolidacao` |
| Área de conhecimento | 8 | `area:integracao` `area:escopo` `area:cronograma` `area:custos` `area:qualidade` `area:recursos` `area:comunicacoes` `area:riscos` |
| Status operacional | 4 | `change-request` `risk` `blocked` `sdd-ia` |
| Prioridade | 6 | `must` `should` `P0` `P1` `P2` `P3` |

**Regras:** mínimo 3 labels por card (1 tipo + 1 macro-fase + 1 área); `sdd-ia` exige co-autoria no commit; `change-request` não entra em `In Progress` sem aprovação do GP.

**Excluídas (GMV):** `N1..N12`, `REQ-01..REQ-15`, `could`, `wont`, `epic`, `spike`, `good first issue`, `help wanted`.

### 7.3 Milestones

5 milestones: M1 (22/09), M2 (30/09), Calibração (03/10, auxiliar), M3 (15/11), M4 (15/12). Regra: 1 Issue = 1 milestone; milestone não fecha com `blocked`/`change-request` abertos. **Ressalva:** CR-001 propõe mover M2 para 15/11 (OKB-C-06).

### 7.4 Padrão de card ubíquo

| Padrão | Aplica-se | Campos |
|---|---|---|
| A — Documental/governança/infra | `docs`, `ci`, `chore` | Título `N{X}.{Y} — Descrição`; contexto ubíquo; entrega; ≥ 3 critérios binários; rastreabilidade (TAP + EAP + REQ + domínio); dependências; atribuição ≤ 8h; tags + milestone + status |
| B — User Story (GWT) | `feat`, `bug`, `test` | Título `N{X}.{Y} — US-NN`; "Como/quero/para"; contexto; ≥ 2 cenários Dado/Quando/Então; regras de negócio; rastreabilidade; dependências; atribuição; status |

### 7.5 Tasklists Markdown (ADR-004 v1.0.0)

Obrigatórias para cards ≥ 6h ou com múltiplos entregáveis; proibidas para cards atômicos (≤ 4h) ou em `Code Review`/`Done`; 3 a 7 itens; último item "Validação final"; binárias. **Subissues rejeitadas** (fragmentam o backlog e distorcem throughput/cycle time). A unidade atômica de métrica é sempre o **card pai**.

### 7.6 Prioridade P0–P3

P0 crítico/caminho crítico (bloqueia ≥ 2 cards) · P1 alto (essencial ao marco) · P2 médio (pode deslizar) · P3 baixo (postergável). Desempate: quem desbloqueia mais cards. `must` pode ser P2 se puder deslizar sem violar o marco.

### 7.7 DoR/DoD

Fonte única: `plano-escopo v1.1` §2.6 (inclui item 8 — tasklist 100% concluída no DoD). O OKB não replica.

---

## 8. INTEGRAÇÃO DOCUMENTAL E PADRÃO DE CITAÇÃO (v5)

### 8.1 Princípio diretor

Documentos de governança são **standalone**; planos de área são **coordenados**; **cross-reference substitui duplicação**. Um fato = um local (SSOT informacional, P-05/G2).

### 8.2 Estrutura real do repositório (as-of 30/10)

```text
docs/
├── tap/               TAP.docx (export; TAP.md = stub 0 B)
├── planos/            plano-integral (TAP+áreas 1-5), 8 planos de área, Plano de Projeto v1.0
├── decisoes/          ADR-001..ADR-012 (+2 duplicatas de ADR-006; consolidado temporário)
├── conhecimento/      OKB.md, glossario.md, KB-INDEX.md, licoes-aprendidas/, drafts/
├── auditorias/        AUD-2610-02/03/04, vio-register.md
├── change-requests/   CR-001
├── diagramas/         eap/, escopo/, cronograma/, custos/, qualidade/, integracao/, comunicacoes/
├── especificacoes/    analise-viabilidade-onda-8.md
├── metricas/          baseline.md (0 B)
├── dependencias/      registro.md (0 B)
├── requisitos/        requisitos.md (0 B — ponteiro)
├── slides_apresentacao/
└── archive/           legado imutável (não é fonte viva)
```

> **Correção:** a árvore do OKB v3.0 (Aditivo §3.2) listava apenas `planos/ decisoes/ conhecimento/ metricas/ requisitos/` e ADR-001..005 — desatualizada.

### 8.3 Formato canônico de citação (obrigatório a partir de v5.0.0)

```text
[ADR-010 v1.0.0](docs/decisoes/ADR-010-Stack-Infraestrutura.md)
[plano-cronograma v1.2](docs/planos/plano-cronograma.md) §3.8 (NC-00)
TAP v3 §6 (docs/planos/plano-integral-tap-1-2-3-4-5.md, bloco Marcos)
```

Regras: (i) sempre pinar `vX.Y.Z` (ADR) ou `vX.Y` (plano); (ii) citar seção/NC; (iii) nunca citar `docs/archive/` como fonte viva; (iv) versão desconhecida → `UNKNOWN-GAP`, não omitir.

### 8.4 Versionamento das menções — patch list (execução na próxima rodada)

| Arquivo:linha | Menção atual | Substituir por |
|---|---|---|
| `.ai/personas/pm.md:22` | `OKB v3.1` | `OKB v5.0.0` (após ratificação) |
| `.ai/personas/all.md:149` | `OKB v3.1` | `OKB v5.0.0` (após ratificação) |
| `.ai/personas/all.md:365` | `OKB v3.1 §10` | `OKB v5.0.0 §9/§10` |
| `docs/planos/plano-integral-tap-1-2-3-4-5.md:207` | `OKB v3.1; Glossário v3.1; ADRs 001–004` | `OKB v5.0.0; Glossário v3.2.0; ADRs 001–012` |
| `plano-integral:660,668,681,685,707` | `OKB v3.1 §X` | `OKB v5.0.0 §X` (remapear seção) |
| `docs/decisoes/ADR-012-...md:84` | `OKB v3.3+` | `OKB v5.0.0` |
| `docs/conhecimento/glossario.md:1,5,7,27,…` | `OKB v3.1` / `OKB_COGME_v3.1.md` | `OKB v5.0.0` / `docs/conhecimento/OKB.md` |
| `docs/conhecimento/KB-INDEX.md:48` | `4.0.0`, owner `agent-docker-specialist` | `5.0.0`, owner a confirmar |
| `docs/conhecimento/KB-INDEX.md:39-43` | ADR-001..004 `1.1.0 ratified` | versões reais (§4.1) |
| `docs/conhecimento/KB-INDEX.md:49` | Glossário `3.2.0` | `3.1` até saneamento, ou 3.2.0 após |
| `docs/archive/**` | referências históricas | **não alterar** (imutável) |

> **Decisão de escopo desta rodada:** o patch acima **não foi aplicado** porque cada arquivo-alvo exige bump de versão + changelog próprios (KB-TAX-001 §4.5) e entraria em conflito com a padronização global da próxima rodada. Fica registrado como insumo do board de metadados.

---

## 9. INCONSISTÊNCIAS, LACUNAS E PENDÊNCIAS

### 9.1 Registro de consistência (OKB-C)

| ID | Sev. | Achado | Evidência | Status / ação |
|---|---|---|---|---|
| OKB-C-01 | Alta | Hierarquia praticada ("TAP > OKB > Glossário > ADRs") contradizia a Constituição | OKB v3.0:5; constitution.md Art. 2.1 | ✅ **corrigido em v5.0.0 §1.1** (F-04) |
| OKB-C-02 | Alta | Metadado divergente: índice declara OKB 4.0.0/594 l; arquivo vivo é v3.0 (1.080 l) | KB-INDEX:48; OKB.md:1-2; AUD-2610-04:30 | ⏳ resolvido por este candidato; índice a atualizar |
| OKB-C-03 | Crítica | VIO-006: evento destrutivo 24/10 02:53:32 reverteu leis sem trilha git; conteúdo v4.0.0 irrecuperável | vio-register:29; AUD-2610-04:48 | ❌ aberto — só o Humano encerra (KS) |
| OKB-C-04 | Média | ADR-006 triplicada (`-chunk-1.md`, `-chunk-aa` sem extensão, canônica) | md5 idêntico `91e91ef1…` | ⏳ remover duplicatas na normalização |
| OKB-C-05 | Alta | Teto GMV de ADRs (≤ 10) excedido: 12 emitidas | Aditivo §4.2; §2.1 | ❌ aberto — decisão CCB |
| OKB-C-06 | Crítica | CR-001 repactua M2 → 15/11/2026, colide com M3, sem ADR e sem reflexo nos planos; aprovação "neste prompt" não registrada formalmente | CR-001; plano-cronograma:80; plano-integracao:131 | ❌ aberto — CR + ADR + CCB |
| OKB-C-07 | Alta | Glossário v3.1 contradiz canon: 13 fases/48 pacotes, Qwen 32B, SQLite, hierarquia invertida | glossario:8,18,23,161 | ❌ aberto — saneamento (próxima rodada) |
| OKB-C-08 | Alta | Artefatos 0 B: `TAP.md`, `requisitos.md`, `baseline.md`, `registro.md`, `.ai/specs/{tap,eap,requisitos}.md` | `wc -c` = 0 | ❌ aberto (P-05/P-08) |
| OKB-C-09 | Alta | TAP canônico só existe como `.docx` + bloco integral no plano-integral; `.md` é stub — e o índice o declara "não-0B" | docs/tap/TAP.md 0 B; KB-INDEX:27 (`não-0B`); plano-integral:49 | ❌ aberto |
| OKB-C-10 | Alta | Frontend: ADR-001 fixa vanilla JS; roster/infra assumem Jinja+HTMX+Tailwind | ADR-001:31; registry frontend; VIO-001 | ❌ aberto — ADR de emenda |
| OKB-C-11 | Média | Custódia do OKB diverge (architect × docker-specialist) sem registro recuperável | KB-INDEX:48 (`§10.2 C-10` inexistente) | ❌ aberto — CCB |
| OKB-C-12 | Média | ADR-005 em "regularização tardia" com ratificação pendente desde 28/10 | ADR-005:6,56 | ❌ aberto |
| OKB-C-13 | Baixa | Classes `relatorio-auditoria`/`register-vio` fora do enum de 10 classes | kb-taxonomy §2; AUD-2610-03:5; vio-register:5 | ⏳ próxima rodada |
| OKB-C-14 | Baixa | Colisão de ID `CR-001` (replanejamento M2 × CR de EAP removida) | CR-001; plano-escopo:178 | ⏳ renumerar CRs |
| OKB-C-15 | Média | Constituição v1.2.0 em `VIGENTE-INTERINA` (co-assinatura pendente) | constitution.md:3 | ❌ aberto |
| OKB-C-16 | Baixa | Metas de fluxo sem baseline; período de calibração encerrado sem registro | baseline.md 0 B; ADR-003 | ❌ aberto |
| OKB-C-17 | Média | Glossário: cabeçalho 3.1 × índice 3.2.0; saneamento "pendente" citado em planos | glossario:1; KB-INDEX:49 | ❌ aberto |
| OKB-C-18 | Baixa | ADR-001 cita ADR-005/006 como "Draft" e mantém "QwenStudio" | ADR-001:11,32 | ⏳ emenda editorial ADR-001 |
| OKB-C-19 | Média | Colisão de rótulos P# (TAP P1–P9 × C-P-01..13) | §5.1/§5.2 | ⏳ namespace na normalização |
| OKB-C-20 | Baixa | Sem índice de ADRs nem cadeia de supersede em `docs/decisoes/` | `ls docs/decisoes` | ⏳ criar README/INDEX |
| OKB-C-21 | **Crítica** | Constituição v1.2.0 contém **Arts. 5–10 duplicados**: duas redações coexistem no mesmo arquivo (1ª sem bloco de co-assinatura; 2ª com bloco e pequenas divergências de pontuação). O corpo normativo tem dois textos válidos da mesma matéria — ambiguidade direta contra P-13 | `constitution.md:131-221` (cópia 1) × `:222-331` (cópia 2); Arts. 1–4 aparecem uma única vez (`:14-130`) | ❌ aberto — **só o Humano consolida** (lei suprema; Art. 5.2). Ação: escolher o texto definitivo, remover a cópia e re-hashear |

### 9.2 Decisões humanas requeridas (não executadas por agente)

1. **OKB-C-05** — rever teto de ADRs ou reclassificar 006–012.
2. **OKB-C-06** — ratificar/ajustar CR-001 e emitir ADR de marco (M2 × M3).
3. **OKB-C-11** — confirmar custódia do OKB.
4. **OKB-C-12** — ratificar ADR-005 (ou manter pendência declarada).
5. **OKB-C-15** — fechar co-assinatura da Constituição v1.2.0.
6. **OKB-C-03** — encerrar VIO-006 (kill switch só o Humano encerra).
7. **OKB-C-21** — consolidar a Constituição v1.2.0 (remover a cópia duplicada dos Arts. 5–10 e re-hashear) antes de qualquer emenda.
8. **Ratificação deste OKB v5.0.0** (Art. 5.1).

---

## 10. HISTÓRICO E PROVENIÊNCIA

| Versão | Data | Base | Mudança |
|---|---|---|---|
| v2.1 | ~09/2026 | — | guardrail original (arquivado, imutável) |
| v3.0 | 20/09/2026 | TAP v3 | consolidação pré-M1; 4 ADRs; 27 labels; backlog M1 |
| v3.1 | 22/09/2026 | v3.0 | pós-M1; freeze; ADR-005 "encaminhada"; política de ADRs (arquivado) |
| v4.0.0 | 23/10/2026 | v3.1 + dedupe | corpus único (594 l) — **perdido em VIO-006** (nunca commitado) |
| **v5.0.0** | **30/10/2026** | v3.0 sobrevivente + ADRs 001–012 + Constitution 1.2.0 | reemissão canônica: frontmatter, hierarquia corrigida, catálogo ADR 001–012, estado as-of, inventário de metadados, registro de inconsistências, padrão de citação |

**Proveniência e limites:** esta versão é uma **reemissão**, não uma recuperação. Tudo o que existia apenas na v4.0.0 (ex.: seção §10.2 C-10 citada pelo KB-INDEX) permanece `UNKNOWN-GAP`. Fontes usadas estão listadas em `derived-from` e cada afirmação normativa cita a fonte no corpo.

**Procedimento de promoção (quando o CCB ratificar):**

1. CCB aprecia este candidato e registra a decisão no ledger.
2. `docs/conhecimento/OKB.md` v3.0 → `docs/archive/legacy-md-artifact/OKB_COGME_v3.0.md` (imutável, com linha de proveniência).
3. Candidato promovido a `docs/conhecimento/OKB.md`, `status: active`, bump para `5.0.0`.
4. `KB-INDEX.md:48` atualizado (versão, owner, caveats); auditoria registra addendum em `vio-register` (nunca reescrita).
5. Patch list §8.4 aplicado junto ao bump de cada artefato-alvo (rodada de normalização/board).

---

*Fim do documento — OKB v5.0.0 (candidato canônico) | COGME | Fatec Taquaritinga | 30/10/2026*
