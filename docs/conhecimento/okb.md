---
id: OKB-001
title: OKB v5.3.0 | Operational Knowledge Base — Base de Conhecimento Operacional do Projeto COGME
version: 5.3.0
class: conhecimento
status: obsoleto
owner: agent-architect
derived-from:
- docs/conhecimento/okb.md (normalizado em 2026-11-05)
last-revised: '2026-11-02'
lgpd-class: n/a
tags:
- conhecimento
- docs
- normalizado
---

# OKB v5.3.0 | Operational Knowledge Base — Base de Conhecimento Operacional do Projeto COGME

**Identidade do template:** este artefato materializa o template **OKB-TEMPLATE-CANON v1.0** (arsenal de seções, ordem e blocos de assinatura). Este template é **CANÔNICO para o OKB até decisão posterior do CCB**; seções são agrupadas em categorias fechadas (I–IV) e todo registro de mudança usa o formato VER-NNN (§12).

| Campo | Valor |
|---|---|
| ID | OKB-001 |
| Nomenclatura canônica | **OKB \| Operational Knowledge Base — Base de Conhecimento Operacional** |
| Versão | **5.3.0** |
| Status | **ratified** — promulgada por CCB-003 (GP) em 30/10/2026; **normalização + ratificação extraordinária em 31/10/2026 (CCB-LOG RAT-2026-10-31-A11, aprovação indireta via agente, autorização expressa do GP); consolidação ADRs 013–016 em 02/11/2026** |
| Data da última atualização | **2026-11-02** |
| Decisor | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Custódia | agent-architect (default KB-TAX-001; KB-INDEX:48 ajustado) |
| Substitui | OKB v5.1.0 (30/10/2026) — **normalização estrutural, corpo normativo preservado**; linhagem v3.0 / v3.1 / v4.0.0 (perdida em VIO-006) |
| Auditoria desta rodada | **AUD-2610-09 — Auditoria Extraordinária dedicada ao OKB** (docs/auditorias/aud-2610-09-okb-normalizacao.md) |
| Hierarquia vigente | `constitution.md` (VIGENTE-PLENA) > TAP v3 (baseline viva sob ADR-013-a) > ADRs 001–016 > **OKB** > Planos > Glossário > Specs > Código |
| LGPD | n/a (sem PII — C-P-04) |
| Passível de auditoria | **SIM — o OKB é parte constitutiva do SSOT e encontra-se sujeito a checagem de congruência contínua contra o SSOT (KB-INDEX, ledger, ccb-log, FS)** |

---

## ÍNDICE NORMATIVO

**Parte I — Metadados e Assinaturas**
- §0 Introdução, escopo e regras de leitura
- §13 Bloco de ratificação e co-assinatura (não integra o hash normativo)

**Parte II — Normatividade (Governança e Decisões)**
- §1 Declaração de governança (hierarquia, CCB, freeze, entrega faseada, CI/CD)
- §2 Regime de decisões (catálogo ADR-001…013, supersede, gatilhos, tipos de mudança, GMV)

**Parte II/III — Conhecimento Operacional de Estado**
- §3 Estado canônico do projeto (as-of 31/10/2026)
- §4 Inventário de artefatos e metadados
- §5 Premissas e restrições vigentes
- §6 Métricas e fluxo

**Parte III — Operações (SSOT e Integração)**
- §7 SSOT operacional (GitHub Projects)
- §8 Integração documental e padrão de citação
- §9 Cobertura metodológica — PMBOK 7ª · TOGAF ADM · ITIL 4

**Parte IV — Qualidade, Auditoria e Histórico**
- §10 Inconsistências, lacunas e pendências (registro OKB-C)
- §11 Proveniência e limites
- §12 Changelog normativo (VER-NNN)

---

## 0. INTRODUÇÃO, ESCOPO E REGRAS DE LEITURA

### 0.1 O que este documento é

O OKB é a **base de conhecimento técnico-aplicada** do COGME (classe `okb`, KB-TAX-001 §2): consolida stack, hardware, método, configuração do SSOT e o estado canônico dos artefatos. Ele **não cria norma autônoma**: operacionaliza a Constituição, o TAP congelado e as ADRs (Art. 2.3). É **passível de auditoria e checagem de congruência ao SSOT** e, sendo parte constitutiva do SSOT, qualquer incongruência sua com o FS/ledger/ccb-log é defeito rastreado (§10), jamais silenciado (C-P-08).

### 0.2 Regras de leitura

1. **Toda afirmação normativa cita fonte e versão pinada** — `ADR-NNN vX.Y.Z`, `plano-X vX.Y`, `TAP §N`. Alegação sem fonte é `UNKNOWN-GAP` (C-P-08).
2. **Metadado honesto:** a seção §4 registra a versão *real* encontrada no arquivo, não a versão *declarada* pelo índice. Divergência é defeito rastreado (§10), nunca silenciada.
3. **Hierarquia absoluta:** em conflito, vale o Art. 2 da Constituição VIGENTE-PLENA, não a ordem interna de versões anteriores do OKB (§1.1).
4. **Regime do TAP:** desde a ADR-013-a, o TAP é **baseline viva com núcleo blindado** (emendável apenas pelo regime de emenda controlada). Divergências intra-TAP materiais (§6 Marcos) permanecem canônicas para matéria temporal.
5. **Confluência de versão:** alegações sobre o OKB citam sempre `OKB v5.2.0` (versão pinada). Referências a "OKB v3.1" no repo vivo são vestígio (normalizadas nesta rodada — patch list §8.4).

### 0.3 O que mudou nesta versão (v5.1.0 → v5.2.0) — registros em §12 (VER-007)

| # | Change | Tipo |
|---|---|---|
| 1 | Template canônico **OKB-TEMPLATE-CANON v1.0** adotado (nomenclatura, índice normativo, blocos de categoria, changelog VER-NNN, bloco de co-assinatura) | normalização |
| 2 | Estado canônico as-of **31/10/2026**: Constituição VIGENTE-PLENA co-assinada; ADR-013 (2 artefatos —⚠️ colisão C-26); regimes CI/CD (CI-CD-GOV-001) e DevSecOps (DEVSECOPS-001); 46 agentes promulgados; VIO-013..025 | persistência |
| 3 | Sanitize decidido: glossário sanitizado com bump v3.1 → **3.2.0** (hierarquia, EAP 12/37, SQLite→PostgreSQL, Qwen MoE, refs OKB v5.2.0) — OKB-C-07 ✅ | sanitize |
| 4 | Patch list §8.4 **aplicada** (personas ×2, plano-integral ×6, ADR-012 ×1 + glossário) — propagação completa | normalização |
| 5 | Tipos de mudança (change enablement) formalizados em §2.6 — OKB-C-23 encerrado | normatize |
| 6 | Namespace de premissas declarado: `TAP-P#` × `C-P-##` — OKB-C-19 encerrado para o corpus (efeito prospectivo) | normatize |
| 7 | Achados novos registrados: **OKB-C-26** (colisão ADR-013), **OKB-C-27** (bump Constituição v1.2.1), **OKB-C-28** (inconsistência temporal) | auditoria |
| 8 | Auditoria extraordinária dedicada materializada: **AUD-2610-09** (documentada em docs/auditorias/) | auditoria |
| 9 | CCB-LOG recebe entrada RAT-2026-10-31-A11; ledger append; KB-INDEX bump 1.2.0 → 1.3.0 | governança |

### 0.4 Emendas aplicadas historicamente (5.0.0-draft → 5.1.0) — preservado

| # | Emenda | Lente | Efeito |
|---|---|---|---|
| 1 | §9 — cobertura metodológica (PMBOK 7ª, TOGAF ADM, ITIL 4) com estado por domínio/fase/prática | cobertura integral | 8 domínios, 10 fases ADM + requisitos e 11 práticas deixam de ser implícitos |
| 2 | Achados novos: OKB-C-22 (ADR-010 não propagada), C-23 (tipos de mudança), C-24 (partes interessadas) | crítica | lacunas materiais passam a ter dono e evidência |
| 3 | Árvore de diretórios comprimida; §4.2 reduzida ao essencial | YAGNI | KB-INDEX e CSV passam a ser a fonte do inventário |
| 4 | Hierarquia declarada uma única vez (§1.1); §0.2 e §8.1 passam a referenciar | YAGNI | "1 fato = 1 local" aplicado ao próprio OKB |
| 5 | Bloco de ratificação com SHA-256 (Art. 5.4), hash excluindo o próprio bloco | rastreabilidade | verificável por `sha256sum` |
| 6 | Promoção executada: v3.0 arquivado, KB-INDEX atualizado, ledger registrado | governança | uma única corpora viva |

---

## 1. DECLARAÇÃO DE GOVERNANÇA

### 1.1 Hierarquia normativa (constitution.md, Art. 2)

**Ramo de projeto (escopo/negócio):**

1. `constitution.md` (lei suprema — ADR-012; VIGENTE-PLENA com co-assinatura, 30/10/2026)
2. TAP v3 — **baseline viva com núcleo blindado** (ADR-013-a) — emenda via CR + ADR de emenda + CCB
3. ADRs aprovadas (`docs/decisoes/`) — podem sobrepor-se parcialmente entre si, nunca à Constituição nem ao núcleo blindado do TAP
4. **OKB** (este documento) — conhecimento operacional, sem autonomia normativa
5. Planos de gerenciamento (`docs/planos/`) e normas técnicas ratificadas (`docs/governanca/`: CI-CD-GOV-001, DEVSECOPS-001)
6. Glossário (`docs/conhecimento/glossario.md` v3.2.0)
7. Especificações SDD e inputs canônicos (`.ai/specs/`)
8. Código-fonte e testes (`src/`, `tests/`)

**Ramo de forja (agentes/SDD):**

1. `constitution.md`
2. Diretiva AFA-ULTIMATE
3. ADRs de governança de agentes + roster (`.ai/agents/registry.yaml`) — 46 agentes promulgados (CCB-LOG A09)
4. Personas, specs, handoffs, ledger e MCPs
5. Scripts e código de agentes

> **Nota de correção (F-04 de AUD-2610-03):** a ordem praticada até o OKB v3.0 ("TAP > OKB > Glossário > ADRs") está **revogada**. ADRs são camada 3 e o Glossário é camada 6 (OKB-C-01; sanado).

### 1.2 Autoridade de mudança (CCB)

| Item | Definição | Fonte |
|---|---|---|
| CCB | GP Leonardo (membro único) | TAP v3 §1.c; TAP-P7 |
| Stakeholder-avaliador | **Prof. Dr. Nivaldo Carleto** (grafia imutável) | ADR-008 v1.1.0 |
| Instrumentos de ratificação | CCB-001 (ADRs 006–011), CCB-002 (ADR-012), 29/10; CCB-003 (Constituição PLENA + OKB), 30/10; RAT-2026-10-31-A01 … A11 (rodadas de ratificação/promulgação), 30–31/10 | cabeçalhos das ADRs; `docs/governanca/ccb-log.md` |
| Registro vivo de decisões | CCB-LOG-NNN (`ccb-log.md`, append-only) — modelo CAB, gates PMBOK/TOGAF/ITIL por entrada. Tipos de mudança normalizados em §2.6 (OKB-C-23 encerrado) | ccb-log.md |
| Emenda constitucional | proposta → parecer de auditoria → CCB → bump + changelog + co-assinatura | Art. 9.1; Art. 5.4 |
| Emenda de ADR | CR + CCB + ADR (MAJOR se alterar marco oficial) | §2.4; plano-custos §4.5/§4.6 |
| Emenda do TAP | **Regime de Emenda Controlada (ADR-013-a)**: núcleo blindado imutável; capítulos dinâmicos emendáveis com CR + ADR de emenda + ratificação; cresce por anexo histórico (nunca reescreve o corpo ratificado) | ADR-013-a v1.0.0 |

### 1.3 Obsolescência declarada do PMBOK 6ª

PMBOK® 7ª é a governança primária (princípios + domínios). PMBOK® 6ª é **dicionário de processos**, citado apenas para rastreabilidade acadêmica. EVM/SPI/CPI são **LEGADO — NÃO APLICÁVEIS** (ADR-003 v1.0.0): orçamento zero inviabiliza CPI (AC = 0) e o fluxo contínuo inviabiliza PV.

### 1.4 Regime do TAP — de freeze a baseline viva (ADR-005 → ADR-013-a)

| Aspecto | Regime original (ADR-005 v1.0.0) | Regime vigente (ADR-013-a v1.0.0) |
|---|---|---|
| Natureza | freeze absoluto — não revisado | **baseline viva com núcleo blindado** |
| Emenda | proibida | controlada: CR + ADR de emenda + CCB; corpo ratificado jamais reescrito (anexo histórico) |
| §6 Marcos | canônico para matéria temporal | mantido como núcleo blindado |
| Notas de Contexto (NCs) | locus de leitura operacional | mantido (plano-cronograma §3.8) |
| Ratificação da ADR-005 | pendente (OKB-C-12) | superseded **parcialmente**: o regime de emenda da ADR-013-a substitui o freeze; a precedência intra-TAP (§6; NCs) permanece medida pela ADR-005 |

**Efeito sobre o CR-001 (repactuação M2 → 15/11/2026):** agora habilitado a tramitar no regime da ADR-013-a (CR + ADR de emenda + CCB). Prevalece a data do TAP §6 até a ratificação formal (OKB-C-06 em regularização).

### 1.5 Estratégia de entrega faseada dos planos

| Marco | Plano original | Planos entregues | Observação as-of 31/10 |
|---|---|---|---|
| M1 (22/09/2026) | 5 planos | Integração, Escopo, Cronograma, Custos, Qualidade | ✅ corpos em FS (v1.1–v2.0) |
| M2 (30/09/2026) | 3 planos | Recursos, Comunicações, Riscos | ⚠️ corpos em FS (v1.0), fechamento de M2 sem registro; CR-001 repactua data (OKB-C-06, via ADR-013-a) |

Trade-off declarado: redução de ~30% da carga documental do M1 em favor da qualidade dos 5 planos-base e da configuração do SSOT (tailoring — PMBOK 7ª, Domínio de Abordagem de Desenvolvimento).

### 1.6 Normas técnicas ratificadas (rodada 31/10/2026 — CCB-LOG A10)

| Norma | Conteúdo | Gates |
|---|---|---|
| **CI-CD-GOV-001** (`docs/governanca/ci-cd-governance.md` v1.0.0) | Política de Governança CI/CD: pipelines COGME CI/CD (Kill Switch, FOSS, SDD/DAG, Agent Health, Testes, Status) e SDDAI Verify (7 passos, fail-closed, strict) refatorados | DevOps/DevSecOps; Integração (PMBOK); Qualidade (C-P-06) |
| **DEVSECOPS-001** (`docs/governanca/devsecops-policy.md` v1.0.0) | Política DevSecOps: segurança integrada ao pipeline, princípios first-principles + YAGNI | DevSecOps; Segurança (C-P-07); Qualidade (C-P-06); Governança (Art. 4) |

Ambas promulgadas em RAT-2026-10-31-A10 com todos os pipelines **green sem bypassing**. Vinculam-se à ADR-010 (infra), C-P-01 (FOSS) e C-P-07 (segurança).

---

## 2. REGIME DE DECISÕES (ADRs)

### 2.1 Catálogo canônico ADR-001 … ADR-016 (as-of 02/11/2026)

| ADR | Título | Versão | Status | Decisão | Formalização | Custódia |
|---|---|---|---|---|---|---|
| ADR-001 | Stack Tecnológica FOSS | 1.1.0 | Finalizado | 19/09/2026 | 28/10/2026 | agent-architect |
| ADR-002 | Kanban como Método de Execução | 1.0.0 | Finalizado | 19/09/2026 | 28/10/2026 | agent-pm (operação) + agent-architect |
| ADR-003 | Métricas de Fluxo (substituição de EVM) | 1.0.0 | Finalizado | 19/09/2026 | 28/10/2026 | agent-pm (coleta) + agent-architect (definição) |
| ADR-004 | Tasklists Markdown (rejeição de subissues) | 1.0.0 | Finalizado | 20/09/2026 | 28/10/2026 | não declarada (autor 1.0.0: agent-architect) |
| ADR-005 | Freeze do TAP e precedência intra-TAP | 1.1.0 | Regularização tardia — ratificação pendente (C-12); **parcialmente sobreposta por ADR-013-a** | 21/09/2026 (NC-00) | 28/10/2026 | agent-architect + agent-pm (NCs) |
| ADR-006 | Módulo de Inteligência SDD (modelo, fallback, cloud FREE) | 2.1.0 | Finalizado (CCB-001) | 26/10/2026 | 29/10/2026 | agent-nexus-prime-ultimate |
| ADR-007 | Redes de Projeto (dualidade CPM × Kanban) | 1.1.0 | Aprovado (CCB-001) | 29/10/2026 | 29/10/2026 | agent-scheduler |
| ADR-008 | Grafia canônica do stakeholder-avaliador | 1.1.0 | Aprovado (CCB-001) | 29/10/2026 | 29/10/2026 | agent-comms + project-auditor |
| ADR-009 | Contagem canônica da EAP (12 fases + 37 pacotes) | 1.0.0 | Aprovado (CCB-001) | 29/10/2026 | 29/10/2026 | agent-scope-manager + project-auditor |
| ADR-010 | Stack de Infraestrutura (PostgreSQL/Docker/Nginx/APIs) | 1.0.0 | Supersedida por ADR-001 v1.1.0 | 29/10/2026 | 29/10/2026 | agent-backend-dev + agent-devops |
| ADR-011 | Ecossistema SDD (MCPs, memória, L1/L2/L3) | 1.0.0 | Aprovado (CCB-001) | 29/10/2026 | 29/10/2026 | agent-nexus-prime-ultimate + agent-architect |
| ADR-012 | Constituição como artefato normativo supremo | 1.0.1 | Aprovado (CCB-002) | 29/10/2026 | 29/10/2026 | GP Leonardo (guardião) |
| **ADR-013-a** | Regime de Emenda Controlada do TAP (Baseline Vivo) | 1.0.0 | **Ratificado** (CCB-LOG A08; promulgado A09-A-002) | 01/11/2026 ⚠️ C-28 | 31/10/2026 | — (não declarada) |
| **ADR-014** (ex-013-b) ⚠️ | Promulgação dos Agentes SDDAI e Resolução de Gaps de Compliance | 1.0.1 | **Ratificado** (CCB 31/10; A09-A-003); Supersedida por ADR-006 v2.1.0 | 31/10/2026 | 31/10/2026 | NEXUS-PRIME ULTIMATE (L0) |
| **ADR-015** | Emenda de Marco — Repactuação Temporal do M2 | 1.0.0 | **Ratificado** (CCB-LOG RAT-2026-10-31-A12) | 31/10/2026 | 31/10/2026 | agent-scheduler |
| **ADR-016** | Backend do MVP — cálculo, cotações, persistência e contrato de erro | 1.0.0 | **Proposta** (pendente CCB) | 31/10/2026 | 02/11/2026 | agent-architect (T10) |

> ⚠️ **OKB-C-26 (colisão de ID):** `ADR-013-regime-emenda-tap.md` e `ADR-013-SDDAI-Promulgacao.md` usam o mesmo identificador `ADR-013`. A designação a/b é a convenção **deste** OKB para desambiguar; a renumeração para **ADR-014** foi decidida pelo CCB em 31/10/2026 (RAT-2026-10-31-A12). Catálogo registra ADRs **001–016 com 16 artefatos** (ADR-010 supersedida, ADR-014 supersedida por ADR-006 v2.1.0).

### 2.2 Cadeia de sobreposição (supersede)

| Decisão | Sobreposta por | Natureza | Efeito prático no OKB |
|---|---|---|---|
| ADR-001 (SQLite; LLM "QwenStudio") | ADR-010 v1.0.0 (parcial) | banco canônico → PostgreSQL 15+ | §3.3 adota PostgreSQL; SQLite só em testes isolados |
| ADR-001 (LLM) | ADR-006 v2.0.0 (parcial) | modelo primário → Qwen3-30B-A3B | §3.4 adota MoE + fallback 14B |
| ADR-003 (EVM legado; redes "obsoletas") | ADR-007 v1.1.0 (parcial) | CPM autorizado no nível macro/acadêmico | §3.7 registra dualidade "a rede valida o marco; o Kanban executa a tarefa" |
| ADR-008 v1.0.0 (grafia viciada, duplo "t") | ADR-008 v1.1.0 (total) | grafia canônica "Carleto" | §1.2 e todo o corpus |
| **ADR-005 (freeze absoluto)** | **ADR-013-a v1.0.0 (parcial)** | **TAP: freeze → baseline viva com núcleo blindado** | §1.4; CR-001 tramita no novo regime |
| ADR-002 (WIP) | Constitution Art. 6.2 | compatível: "WIP ≤ 3 **por pessoa**" | §7.1 |
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

Campos obrigatórios da ADR tardia: `Tipo`, `Data da decisão efetiva`, `Data da formalização`, `Motivo da tardança`, `Lição aprendida`. Casos vigentes: **ADR-005** autodeclarada tardia (efetiva 21/09 → formalizada 28/10); **ADR-006** com hiato de 3 dias, sem autodeclaração. Proporção declarada: 1/12 ≈ 8%; ampliada: 2/12 ≈ 17% — abaixo do limiar de 30%. **ADR-013-a** soma hiato declarado em A08 (decisão efetiva frente ao custo de retrabalho de 8h documentado) — incluir na próxima verificação GMV.

### 2.5 Tipos de mudança (change enablement) — formalizado nesta versão

**Base:** prática ITIL 4 "Habilitação de Mudança" já operada pelo CCB-LOG na prática (linhas A01–A10); formalização encerra OKB-C-23. É operacionalização, não norma autônoma (Art. 2.3).

| Classe | Definição | Portão | Exemplo COGME |
|---|---|---|---|
| **standard** | mudança pré-autorizada, repetitiva, sem julgamento adicional | sem CCB; registro no artefato alvo | bump de patch em documento; aplicação de patch list; lint |
| **normal** | mudança não pré-autorizada de menor/maior risco | CR → ADR (se ≥2 gatilhos §2.3) → CCB → bump + changelog | normalização do OKB; emenda de ADR |
| **SEV** | emergência/incidente que ameaça o circuito ou a lei | autorização expressa do CCB + registro retroativo ≤ 24h + AUD | rollout fora de janela; evento VIO com kill switch |

Regra adicional: **qualquer mudança em lei suprema (Constituição) é sempre `normal` com co-assinatura humana** (Art. 5.4) — jamais `standard`. O CCB-LOG deve sinalizar `change-class:` na entrada (efeito prospectivo).

### 2.6 Limite de ADRs por marco (GMV)

| Marco | Limite declarado (v3.1 §6.4) | Emitidas | Situação |
|---|---|---|---|
| M1 | 4 (001–004) | 4 | ✅ |
| M2 | ≤ 2 | 9–10 (005–013) | ⚠️ excede o marco individual, coberto pelo teto global revisado |
| M3 | ≤ 3 | 0 | — |
| M4 | ≤ 1 | 0 | — |
| **Total** | **≤ 20** | **13 IDs (14 artefatos)** | ✅ dentro do teto GMV revisado — **OKB-C-05 encerrado** |

**Decisão do CCB:** teto global de ADRs revisado de ≤ 10 para **≤ 20** (decisão 3 da inspeção Constitution/OKB). O excedente decorre da onda de consolidação constitucional (28–31/10). O marco M2 excede seu limite individual (≤ 2) por força da mesma onda, mas permanece coberto pelo teto global. OKB-C-05 encerrado.

---

## 3. ESTADO CANÔNICO DO PROJETO (as-of 31/10/2026)

### 3.1 Escopo e EAP

| Item | Valor canônico | Fonte |
|---|---|---|
| EAP | **12 fases (N1–N12) + 37 pacotes de nível 2** | ADR-009 v1.0.0; TAP §4 |
| Macro-fases | MF1 Fundação (N1–N4, N8, N9, N10 parcial); MF2 Construção (N5–N7, N10); MF3 Consolidação (N11, N12) | §7.2 (labels); plano-integral:337. **Distribuição de pacotes por MF = `UNKNOWN-GAP`** (Figuras 7–9 placeholders) |
| Escopo do produto | simulação cambial, 5 regimes de contratação, spread/IOF, invoice PDF | TAP §2; Art. 1.2 |
| "13 fases / 48 pacotes" | **não canônico** — sanado no Glossário v3.2.0 nesta rodada | ADR-009; NC-Q4 |
| 13ª fase "Encerramento Administrativo" | subsumida em N12 | ADR-009 §Decisão 2 |

### 3.2 Marcos (TAP §6, núcleo blindado ADR-013-a) e situação real

| Marco | Data canônica | Critério de aceite | Situação as-of 31/10 |
|---|---|---|---|
| M1 — Entrega Parcial Documental | 22/09/2026 | 5 planos + 12 PDCAs + Ishikawa, sem achados críticos | Documentos em FS; aceite acadêmico não registrado em FS |
| Calibração (auxiliar) | 03/10/2026 | Baseline de métricas | ⚠️ baseline seed **SIMULADO** promulgada (A09-A-006); medição real pendente (C-16) |
| M2 — Ambiente e Modelagem | 30/09/2026 (TAP) | CI verde + DER + UX/UI versionados | ⚠️ vencido sem fechamento; CR-001 propõe 15/11/2026 via ADR-013-a (C-06) |
| M3 — MVP Funcional (Beta) | 15/11/2026 | coverage ≥ 80%, UAT sem defeitos críticos | Risco ativo: nenhum card de construção no quadro (plano-riscos Q-02:117) |
| M4 — Encerramento | 15/12/2026 | documentação consolidada + aceite formal | — |

> **Conflito declarado:** CR-001 (M2 → 15/11/2026) colide com M3 (15/11/2026) e não foi formalizado em ADR de emenda. Prevalece a data do TAP §6 (núcleo blindado) até decisão do CCB.

### 3.3 Stack efetiva (ADR-001 v1.0.0 + ADR-010 v1.0.0)

| Camada | Componente canônico | Licença | Observação |
|---|---|---|---|
| Linguagem/Backend | Python 3.11 + FastAPI (async) | PSF/MIT | Uvicorn por container |
| Banco | **PostgreSQL 15+** (asyncpg + SQLAlchemy async + Alembic) | PostgreSQL License | SQLite **revogado** como banco canônico (ADR-010); uso só em teste isolado |
| Orquestração | Docker + Docker Compose (`db`, `web`, `proxy`) | Apache-2.0 | paridade dev/test/prod |
| Proxy | Nginx (latente, perfil opcional) | BSD-2 | pronto para TLS futuro |
| PDF | WeasyPrint | BSD-3 | deps nativas glibc/Pango |
| Testes | pytest + coverage.py (≥ 80%) | MIT | CI por push |
| CI/CD | GitHub Actions Free Tier + pipelines ratificados (CI-CD-GOV-001) | proprietário gratuito | **Bypass registrado** (C-P-01) |
| Frontend | ⚠️ **conflito aberto**: ADR-001 = HTML5/CSS3/JS vanilla; registry = Jinja + HTMX + Tailwind | — | OKB-C-10 |
| APIs de câmbio | Circuit Breaker: Frankfurter (primária) → fallbacks → **PTAX/BCB obrigatório** | MIT/CC0 | ADR-010 §4 |
| LLM | ver §3.4 | Apache-2.0 | ADR-006 |

**Regra de mudança de stack:** CR + ADR específica + CCB + ADR MAJOR; nenhum componente trocado por conveniência (ADR-001 §Governança; plano-custos §4.5/§4.6). Drift silencioso = incidente.

### 3.4 SDD, LLM e hardware (ADR-006 v2.0.0 + ADR-011 v1.0.0 + C-P-02)

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
| Cloud | free tier **apenas dados não sensíveis**, whitelist (HF, OpenRouter, Groq, GitHub Models) — C-P-02 revisado, Art. 7.4 |
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
| Custo-benefício | C-P-09: nenhum papel opera abaixo do custo-benefício |
| Onda SDDAI (novidade 31/10) | 5 agentes forjados e promulgados (sddai-loader/engineer/trainer/memory/cli — ADR-013-b); verify pipeline `sddai_verify_pipeline.py` + workflow `sddai-verify.yml` (fail-closed, strict) — A10; **ecossistema: 46 agentes promulgados** (A09) |

### 3.6 Eventos de governança (25/10 → 31/10)

| Data | Evento | Fonte |
|---|---|---|
| 29/10 | CCB-001 ratifica ADRs 006–011; CCB-002 ratifica ADR-012 | ADRs; ccb-log |
| 30/10 | A01 — Constituição co-assinada, VIGENTE-PLENA (commit `7cff886`; hash `b3f296c6…`) | ccb-log; Art. 5.4 |
| 30/10 | A08 — ADR-013-a (Regime de Emenda do TAP) ratificada; autorização de consolidação v1.2.1 | ccb-log |
| 30–31/10 | AUD-2610-05/06 (SDDAI compliance), AUD-2610-07 (rodada de ratificação — TA-900), AUD-2610-08 (CI/CD extraordinária) | docs/auditorias/ |
| 31/10 | A09 — promulgação de 16 artefatos (inclui constitution "v1.2.1" ⚠️ C-27, baseline seed, Canon_Stack_SDD v2.0.0, ledger, SDDAI) | ccb-log |
| 31/10 | A10 — CI-CD-GOV-001 + DEVSECOPS-001 + workflows ratificados (todos green) | ccb-log |
| 31/10 | VIO-013..VIO-025 registrados (contratos JSON half-duplex, gates Art. 4.7) | vio-register |
| 31/10 | A11 — **esta rodada**: normalização do OKB v5.2.0 (template canônico, sanitize, patch list, auditoria AUD-2610-09) | ccb-log; §12 |
| 02/11 | A12 — consolidação _consolidado-adrs.tmp.md com ADRs 013–016; bump OKB para v5.3.0; atualização catálogo ADR e inventário | ccb-log; §12 |

---

## 4. INVENTÁRIO DE ARTEFATOS E METADADOS

### 4.1 Artefatos vivos (versão real × versão declarada)

Legenda: **real** = extraído do cabeçalho/frontmatter do arquivo em 31/10/2026; **índice** = `KB-INDEX.md` v1.3.0.

| ID / classe | Caminho | Versão real | Status real | Índice declara | Divergência |
|---|---|---|---|---|---|
| Lei | `constitution.md` | 1.2.0 | **VIGENTE-PLENA** | não indexada | **A-09 declara v1.2.1** (sanitizada, ratificada); header do arquivo não atualizado — **OKB-C-27** |
| CCB-LOG | `docs/governanca/ccb-log.md` | 0.1.0 | active | não indexado | classe `register-decision` fora do enum KB-TAX (C-13); cita plano inexistente (C-25) |
| Normas técnicas | `docs/governanca/ci-cd-governance.md`; `devsecops-policy.md` | 1.0.0 / 1.0.0 | ratified (A10) | não indexado | registrar no KB-INDEX |
| TAP (export) | `docs/tap/TAP.docx` | 18/09/2026 | congelado/blindado | — | `TAP.md` = 0 B e declarado "não-0B" no índice (OKB-C-09) |
| ADR-013-a | `docs/decisoes/adr-013-regime-emenda-tap.md` | 1.0.0 | ratified | não indexado | frontmatter date 01/11 vs instrumento 31/10 (C-28) |
| ADR-013-b ⚠️ | `docs/decisoes/ADR-013-SDDAI-Promulgacao.md` | 1.0.0 | ratified; supersedida por ADR-006 v2.1.0 | não indexado | **colisão de ID com ADR-013-a (C-26)** |
| ADR-014 | `docs/decisoes/adr-014-sddai-promulgacao.md` | 1.0.1 | ratified; supersedida por ADR-006 v2.1.0 | não indexado | renumeração de ADR-013-b (OKB-C-26) |
| ADR-015 | `docs/decisoes/adr-015-emenda-marco-m2.md` | 1.0.0 | ratified | não indexado | — |
| ADR-016 | `docs/decisoes/adr-016-backend-mvp.md` | 1.0.0 | proposta | não indexado | pendente CCB |
| plano-integral | `docs/planos/plano-integral-tap-1-2-3-4-5.md` | 1.0.0¹ | ativo | 1.0.0 active | sem carimbo de versão no corpo; refs atualizadas nesta rodada |
| Plano de Projeto | `docs/planos/Plano-de-Projeto-COGME_v1.0.md` | 1.0.0¹ | ativo | 1.0.0 active | docx v1.1/v2.0 ONGOING concorrentes — decisão CCB pendente (R-03) |
| Integração | `docs/planos/plano-integracao.md` | 2.0 | ativo | 2.0.0 active | normalizar 2.0 → 2.0.0 |
| Escopo | `docs/planos/plano-escopo.md` | 1.1 | ativo | 1.1.0 active | normalizar |
| Cronograma | `docs/planos/plano-cronograma.md` | 1.2 | ativo | 1.2.0 active | normalizar |
| Custos | `docs/planos/plano-custos.md` | 1.2 | ativo | 1.2.0 active | normalizar |
| Qualidade | `docs/planos/plano-qualidade.md` | 1.1 | ativo | 1.1.0 active | normalizar |
| Recursos | `docs/planos/plano-recursos.md` | 1.0¹ | ativo | 1.0.0 active | sem carimbo |
| Comunicações | `docs/planos/plano-comunicacoes.md` | 1.0¹ | ativo | 1.0.0 active | sem carimbo |
| Riscos | `docs/planos/plano-riscos.md` | 1.0¹ | ativo | 1.0.0 active | sem carimbo |
| ADR-001..004 | `docs/decisoes/ADR-00{1..4}-*.md` | **1.1.0 (001) / 1.0.0 (002–004)** | Finalizado | **1.1.0 ratified** | índice ainda desatualizado (OKB-C-02) |
| ADR-005 | `docs/decisoes/adr-005-freeze.md` | 1.0.0 / 1.1.0 (regime-tap) | ratificação formal pendente; parcialmente sobreposta | 1.0.0 ratified | OKB-C-12 |
| ADR-006 | `docs/decisoes/adr-006-inteligencia-sdd.md` | 2.1.0 | Finalizado (CCB-001) | **ausente** | duplicatas eliminadas (C-04 ✅); absorveu ADR-014 |
| ADR-007..012 | `docs/decisoes/ADR-00{7..12}*.md` | 1.1.0 ✓ / 1.0.0 / 1.1.0 / 1.0.0 / 1.0.0 / 1.0.1 | Aprovados (CCB-001/002) | ausentes | índice a registrar (`KB-INDEX v1.3.0` desta rodada) |
| OKB | `docs/conhecimento/okb.md` | **5.3.0** | ratified | 5.2.0 | ✅ sanado (este documento); bump v5.3.0 em 02/11 |
| Glossário | `docs/conhecimento/glossario.md` | **3.2.0** | Sanitizado (31/10) | 3.2.0 active | ✅ coerente — saneado nesta rodada (C-07) |
| KB-INDEX | `docs/conhecimento/kb-index.md` | 1.3.0 | active | 1.3.0 | ✅ bump nesta rodada |
| Taxonomia | `.ai/specs/kb-taxonomy.md` | 1.1.0 | ratified | 1.1.0 | coerente |
| Requisitos | `docs/requisitos/requisitos.md` | 0 B | — | 1.0.0 draft (ponteiro) | 0 B (OKB-C-08) |
| Baseline | `docs/metricas/baseline.md` | seed | promulgado como **SIMULADO** (A09-A-006) | 1.0.0 draft | seed não-verídico — medir em M3 (C-16) |
| Dependências | `docs/dependencias/registro.md` | 0 B | — | 1.0.0 draft | 0 B (OKB-C-08) |
| Specs SDD | `.ai/specs/{tap,eap,requisitos}.md` | **0 B** | — | 1.0.0 draft "preenchidas" | drift grave (OKB-C-08) |
| Canon SDD | `docs/conhecimento/canon-stack-sdd.md` | 2.0.0 | promulgado (A09-A-007) | não indexado | registrar |
| Registro de ratificação | `docs/governanca/ratificacao-promulgacao.md` | 1.0.0 | promulgado (A09-A-005) | não indexado | registrar |
| Relatórios SDD | `docs/analise/relatorio-memoria-persistente-sddai.md`; `docs/evidencias/relatorio-testes-sddai.md`; `docs/operacao/sddai-verify-pipeline.md` | — | promulgados (A09) | não indexado | registrar |
| Lições MF1/MF2/MF3 | `docs/conhecimento/licoes-aprendidas/` | MF1 1,9 KB / MF2 0 / MF3 0 | — | não indexadas | C-48 (classes sem artefato) |
| CR-001 | `docs/change-requests/cr-001-m2-replanejamento.md` | sem versão | aprovado "neste prompt" (31/10) | não indexado | tramitação agora via ADR-013-a (C-06) |
| VIO register | `docs/auditorias/vio-register.md` | 1.1.0 | active | não indexado | VIO-001..025; 13 abertos |
| Auditorias | `docs/auditorias/AUD-2610-0{2..9}*.md` | 1.0.0 | active | não indexado (exceto 09 nesta rodada) | classe `relatorio-auditoria` fora do enum KB-TAX (C-13) |

¹ versão inferida do índice porque o corpo não carrega campo de versão.

### 4.2 Artefatos anômalos (apenas registro)

| Caminho | Anomalia | Ação |
|---|---|---|
| `docs/decisoes/adr-013-regime-emenda-tap.md` × `ADR-013-SDDAI-Promulgacao.md` | **colisão de id ADR-013** + frontmatter datado 01/11 | **RESOLVIDA**: ADR-013-b renumerada para ADR-014 por decisão CCB (RAT-2026-10-31-A12); OKB-C-26/C-28 encerrados |
| `docs/decisoes/consolidado-adrs-tmp.md` | artefato temporário de análise | descartar após uso (autorizado) |
| `docs/planos/.~ano-de-Projeto-COGME_v2.0.1-ONGOING.docx` | lock temporário de editor | remover |
| `docs/planos/Plano-de-Projeto-COGME_v2.0{,.1}-ONGOING.docx` | export/docx concorrente sem `.md` canônico | decisão CCB (R-03) |

> Demais anomalias de higiene do repositório não são registradas aqui por YAGNI: inventário vivo e coluna `divergencia` em `docs/conhecimento/drafts/artefatos-metadados.csv`.

### 4.3 Classes sem artefato vivo completo

| Classe | Estado | Gap |
|---|---|---|
| `requisito` | ponteiro 0 B | popular em `.ai/specs/requisitos.md` e espelhar |
| `log-baseline` | baseline seed (simulado) + registro 0 B | popular registro de dependências; medir baseline real |
| `licoes` | 1 de 3 arquivos | MF2/MF3 0 B |
| `diagrama` | PNG+SVG por área | EAP com placeholders; fonte SVG/Mermaid exigida |

---

## 5. PREMISSAS E RESTRIÇÕES VIGENTES

### 5.1 Premissas do TAP v3 §9 (TAP-P1…TAP-P9)

> **Namespace normalizado nesta versão:** as premissas passam a ser grafadas `TAP-P#`; os princípios constitucionais `C-P-##` (OKB-C-19 encerrado — efeito prospectivo; demais artefatos renomeam na próxima edição do próprio artefato).

| ID | Premissa | Status |
|---|---|---|
| TAP-P1 | Governança híbrida (PMBOK 7ª + 6ª dicionário + Kanban) | vigente |
| TAP-P2 | FOSS absoluto (com Bypass registrado — C-P-01) | vigente |
| TAP-P3 | SDD com IA auditável | vigente |
| TAP-P4 | Código-fonte é deliverable formal | vigente |
| TAP-P5 | 20 h/semana por membro | vigente |
| TAP-P6 | Hardware adequado e suficiente | revisada (58 GB reais) |
| TAP-P7 | GP = CCB único; Prof. Dr. Nivaldo Carleto = avaliador de marcos | vigente |
| TAP-P8 | Aquisições e partes interessadas simplificadas | vigente |
| TAP-P9 | Separação ontológica TAP ≠ EAP ≠ PDCA | vigente |

> **Correção histórica:** o OKB v3.0 listava apenas P1–P8; TAP-P9 (base da ADR-005) faltava.

### 5.2 Princípios constitucionais (C-P-01…C-P-13, constitution.md)

| ID | Princípio | Efeito operacional |
|---|---|---|
| C-P-01 | FOSS zero-cost | dependência proprietária só com Bypass (3 pilares) |
| C-P-02 | Soberania local com flexibilização controlada | inferência local primária; cloud free tier só dados não sensíveis |
| C-P-03 | Soberania de dados | zero telemetria, zero lock-in |
| C-P-04 | LGPD primária | mínimo necessário; sem PII em artefatos |
| C-P-05 | Traces | toda decisão não trivial gera ADR/registro; silêncio = defeito |
| C-P-06 | Qualidade fechada | coverage ≥ 80%; gates reviewer → gatekeeper |
| C-P-07 | Segurança | OWASP baseline; fail-closed |
| C-P-08 | Honestidade | alegação sem fonte = KNOWLEDGE GAP |
| C-P-09 | Anti-subutilização | papéis com custo-benefício comprovado |
| C-P-10 | Linguagem | EN para código/contratos; PT-BR para humano |
| C-P-11 | YAGNI | nada sem demanda do ciclo atual |
| C-P-12 | Primeiros princípios | pressuposto não fundamentado = gap declarado |
| C-P-13 | Precisão linguística | sem ambiguidade normativa |

### 5.3 Restrições (TAP §8 e §11)

Escopo restrito ao MVP acadêmico; prazo letivo inegociável; **orçamento R$ 0,00**; equipe de 3 pessoas com múltiplos papéis; stack 100% FOSS (com Bypass registrado); licenciamento final open source (MIT/GPL).

---

## 6. MÉTRICAS E FLUXO

### 6.1 Métricas oficiais (ADR-003 v1.0.0)

| Métrica | Definição | Meta | Frequência | Estado |
|---|---|---|---|---|
| Cycle Time | Done − In Progress (NC-Q3) | ≤ 3 dias | semanal | ⚠️ aspiracional (baseline seed simulado) |
| Throughput | cards concluídos/semana | ≥ 5 | semanal | ⚠️ aspiracional |
| CFD | bandas do fluxo acumulado | sem bandas largas | semanal | ✅ nativo (GitHub Insights) |
| WIP | cards em In Progress | ≤ 3 **por pessoa** (≤ 9 total) | contínuo | ✅ Art. 6.2 |
| Coverage | linhas testadas/totais | ≥ 80% | por push (CI) | ✅ C-P-06 |

**Métricas LEGADO:** SPI, CPI, EVM — não aplicáveis.

### 6.2 Calibração e baseline

Período 23/09–03/10/2026 encerrado sem medição registrada. Em 31/10/2026, `docs/metricas/baseline.md` foi **promulgada como baseline seed SIMULADO** (CCB-LOG A09-A-006, declarado no registro) — servindo de chassi auxiliar, **não como evidência de desempenho**. Metas acima seguem **aspiracionais** até baseline real em M3 (OKB-C-16).

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

## 8. INTEGRAÇÃO DOCUMENTAL E PADRÃO DE CITAÇÃO

### 8.1 Princípio diretor

Documentos de governança são **standalone**; planos de área são **coordenados**; **cross-reference substitui duplicação**. Um fato = um local (SSOT informacional, C-P-05/G2).

### 8.2 Estrutura real do repositório (as-of 02/11)

```text
docs/
├── tap/ planos/            TAP.docx (export; TAP.md = stub 0 B) + plano-integral + 8 planos + Plano de Projeto
├── decisoes/               ADR-001..ADR-016 (16 artefatos; ADR-010 supersedida, ADR-014 supersedida por ADR-006 v2.1.0); _consolidado-adrs.tmp.md
├── conhecimento/           docs/conhecimento/okb.md (v5.3.0), glossario.md (v3.2.0), docs/conhecimento/kb-index.md (v1.3.0), docs/conhecimento/canon-stack-sdd.md, licoes-aprendidas/, drafts/
├── governanca/             ccb-log.md, ci-cd-governance.md, devsecops-policy.md, ratificacao-promulgacao.md, ci-cd-devsecops relatório
├── governance/             council-notification.md (promulgado A09-A-011)
├── auditorias/             AUD-2610-02..09; vio-register.md (VIO-001..025)
├── change-requests/        CR-001
├── requisitos|metricas|dependencias/   requisitos 0 B; baseline.md (seed simulado); registro 0 B
├── analise|evidencias|operacao|verification|stakeholder/   relatórios SDDAI e ciclo de verificação (promulgados A09)
├── especificacoes|diagramas|slides_apresentacao/           diagramas PNG+SVG por área
└── archive/                legado imutável — nunca fonte viva
```

### 8.3 Formato canônico de citação (obrigatório)

```text
[ADR-010 v1.0.0](docs/decisoes/adr-010-stack-infraestrutura.md)
[plano-cronograma v1.2](docs/planos/plano-cronograma.md) §3.8 (NC-00)
TAP v3 §6 (docs/planos/plano-integral-tap-1-2-3-4-5.md, bloco Marcos)
[OKB v5.2.0](docs/conhecimento/okb.md) §2.5
```

Regras: (i) sempre pinar `vX.Y.Z` (ADR/norma) ou `vX.Y` (plano); (ii) citar seção/NC; (iii) nunca citar `docs/archive/` como fonte viva; (iv) versão desconhecida → `UNKNOWN-GAP`, não omitir.

### 8.4 Patch list de menções ao OKB — **INSUMO EXECUTADO nesta rodada (31/10/2026, RAT-2026-10-31-A11)**

| Arquivo | Menção atualizada | Status |
|---|---|---|
| `.ai/personas/pm.md` | `OKB v3.1` → `OKB v5.2.0` | ✅ aplicado |
| `.ai/personas/all.md` (2 loci) | `OKB v3.1` / `OKB v3.1 §10` → `OKB v5.2.0` | ✅ aplicado |
| `docs/decisoes/ADR-012..md:84` | `OKB v3.3+` → `OKB v5.2.0` | ✅ aplicado |
| `plano-integral:207` | `OKB v3.1; Glossário v3.1; ADRs 001–004` → `OKB v5.2.0; Glossário v3.2.0; ADRs 001–013` | ✅ aplicado |
| `plano-integral:660` | `OKB v3.1 §2.4` → `OKB v5.2.0 §1.5` | ✅ aplicado |
| `plano-integral:668` | `OKB v3.1 §7.2` → `OKB v5.2.0 §3.2` | ✅ aplicado |
| `plano-integral:681` | `OKB v3.1 §8.1` → `OKB v5.2.0 §12` | ✅ aplicado |
| `plano-integral:685` | `OKB v3.1 §5` → `OKB v5.2.0 §2` | ✅ aplicado |
| `plano-integral:707` | `OKB v3.1… Glossário v3.1 (saneamento pendente)` → `OKB v5.2.0… Glossário v3.2.0 (saneado)` | ✅ aplicado |
| `glossario.md` | cabeçalho v3.1 → **v3.2.0** sanitizado + refs | ✅ aplicado |
| `docs/archive/**` | referências históricas | 🔒 **imutável — não alterar** |

**Remap de seções aplicado (VER-007):** §1.5 entrega faseada · §3.2 marcos · §12 changelog. Referências a seções históricas do OKB v3.1 foram remapeadas para as seções canônicas de v5.2.0 conforme tabela acima.

---

## 9. COBERTURA METODOLÓGICA — PMBOK 7ª · TOGAF ADM · ITIL 4

**Por que esta seção existe.** O COGME é *gerido* por PMBOK 7ª, *arquitetado* com a lógica TOGAF (adaptada a produto único) e *operado* com disciplina de serviços ITIL 4 — sendo o "serviço" o circuito documental e o próprio produto. Esta seção é um **mapa de aderência**: cada linha nomeia o artefato que já descarrega a obrigação metodológica. `GAP` = nenhum artefato a descarrega (registrado em §10). `✅` = coberto · `⚠️` = parcial · `❌` = lacuna · `⛔` = fora de escopo.

**Regra anti-cerimônia (YAGNI, C-P-11).** Nenhuma prática é "adotada" por constar aqui. Constar significa apenas que o projeto já a exerce por outro meio; o que não se aplica está declarado em §9.4 e **não gera artefato**.

### 9.1 PMBOK 7ª — 8 domínios de desempenho

| Domínio | Como o COGME exerce | Evidência | Estado |
|---|---|---|---|
| Partes interessadas | Stakeholder-avaliador único, CCB de membro único, equipe de 3 | ADR-008 v1.1.0; TAP §1.c e TAP-P7 | ⚠️ sem registro/matriz de partes interessadas (OKB-C-24) |
| Equipe | Plano de recursos; WIP ≤ 3 por pessoa; 20 h/semana por membro | plano-recursos v1.0; Art. 6.2; TAP-P5 | ✅ |
| Abordagem de desenvolvimento e ciclo de vida | Híbrido: entrega documental faseada (M1/M2) + fluxo contínuo Kanban; SDD com LLM local | ADR-001, ADR-002, ADR-006, ADR-007 | ✅ |
| Planejamento | TAP baseline viva (ADR-013-a) + 8 planos de área + marcos; trabalho puxado por capacidade | ADR-005→013-a; plano-integral; plano-cronograma | ✅ (CR-001 via ADR-013-a — C-06) |
| Trabalho do projeto | GitHub Projects como SSOT; tasklists; handoffs SDD | ADR-002, ADR-004; §7 | ✅ |
| Entrega | EAP 12 fases/37 pacotes; marcos M1–M4; MVP full-stack | ADR-009; §3.1–3.2 | ⚠️ M2 vencido sem fechamento; 0 cards de construção |
| Medição | Cycle Time, Throughput, CFD, WIP, coverage ≥ 80% | ADR-003; §6 | ⚠️ baseline seed simulado; metas não calibradas (C-16) |
| Incerteza | plano-riscos (R1–R5, Q-01..Q-0n); ADR tardia; kill switch; auditorias; VIO register 25 registros | plano-riscos v1.0; vio-register v1.1 | ⚠️ VIO-013..025 abertos (contratos half-duplex) |

**9.1.1 Matriz de partes interessadas (aceite M4) — encerra OKB-C-24**

| Parte interessada | Papel | Interesse no COGME | Influência |
|---|---|---|---|
| Prof. Dr. Nivaldo Carleto | Stakeholder-avaliador / banca | Aceite de marcos M1–M4 e entrega final (15/12/2026) | Decisor de aceite acadêmico (ADR-008 v1.1.0) |
| GP Leonardo | CCB de membro único / Gerente de Projeto | Entrega dentro do prazo letivo e orçamento R$ 0,00 | Decisor único via CCB (Constitution Art. 5.1) |
| Equipe (3 membros, múltiplos papéis) | Execução | Escopo EAP 12 fases / 37 pacotes; MVP funcional | Execução técnica; WIP ≤ 3 por pessoa (Art. 6.2) |

**Tailoring declarado (domínio Abordagem de Desenvolvimento).** Três adaptações, todas com ADR ou registro formal: (i) EVM/SPI/CPI abandonados em favor de métricas de fluxo (ADR-003); (ii) 3 dos 8 planos de área diferidos de M1 para M2, −30% de carga documental (§1.5); (iii) subissues rejeitadas em favor de tasklists Markdown, com o card pai como unidade atômica de métrica (ADR-004).

**Princípios × Constituição.** Os 12 princípios do PMBOK 7ª não são replicados: a Constituição já os converte em deveres executáveis (*stewardship* → C-P-05; *quality* → C-P-06; *tailoring* → C-P-11; *risk* → C-P-07; *change* → Art. 9).

### 9.2 TOGAF ADM — fases aplicáveis

| Fase ADM | Tradução no COGME | Artefato | Estado |
|---|---|---|---|
| Preliminar | Lei, taxonomia, roster e princípios de arquitetura | constitution.md; KB-TAX-001; registry.yaml | ✅ |
| A — Visão de arquitetura | Por que o sistema existe, escopo, restrições, avaliador | TAP v3 (núcleo blindado); §1 e §3 deste OKB | ✅ |
| B — Arquitetura de negócio | Processos (simulação, 5 regimes, invoice), RF/RNF | plano-escopo v1.1; REQ-01..REQ-15 | ⚠️ repositório de requisitos 0 B (C-08) |
| C1 — Arquitetura de dados | Modelo de dados, entidades, ciclo de vida da cotação | **DER — entregável de M2** | ❌ DER não existe em FS |
| C2 — Arquitetura de aplicação | Backend, frontend, integrações, catálogo de aplicações | §3.3; ADR-010 | ⚠️ conflito de frontend (C-10) |
| D — Arquitetura de tecnologia | Runtime, banco, containers, hardware, LLM | ADR-010 v1.0.0; ADR-006 v2.0.0; CI/CD ratificado | ✅ |
| E — Oportunidades e soluções | Backlog, work packages, build vs. reuse | GitHub Projects (§7); ADRs | ⚠️ sem gap analysis formal |
| F — Planejamento de migração | Arquitetura de transição (SQLite → PostgreSQL) | **nenhum** | ❌ ADR-010 sem reflexo em cronograma/custos/recursos; REQ-07 ainda pede SQLite (OKB-C-22) |
| G — Governança de implementação | CCB, gates reviewer → gatekeeper, auditorias, CI/CD ratificado | Art. 4/5; CI-CD-GOV-001; VIO | ✅ (VIO de contrato abertos) |
| H — Gestão de mudança de arquitetura | ADR, CR, VIO, emenda (ADR-013-a) | §2.3–2.5; Art. 9 | ✅ (regime formalizado) |
| Requisitos (função central) | REQ-01..15 rastreados a TAP/EAP/cards | plano-integral (34 referências) | ⚠️ parcial (C-08) |

**Peças de governança TOGAF já existentes:** repositório de arquitetura = `KB-INDEX` + `docs/archive/`; conselho de arquitetura = CCB (GP único); princípios = Art. 3 (C-P-01..13); conformidade = AUD-2610-0x + VIO register; contratos = ADRs. **Fora de escopo (YAGNI):** modelo de maturidade de arquitetura e roadmap plurianual de portfolio.

### 9.3 ITIL 4 — cadeia de valor e práticas

**Cadeia de valor (6 atividades):** *Plan* → §1/§3 · *Improve* → retrospectivas, lições por MF, SIR, §10 · *Engage* → CCB, marcos, plano de comunicações · *Design & Transition* → ADRs, specs SDD, handoffs, CI · *Obtain/Build* → código, testes, coverage · *Deliver & Support* → MVP, invoice, API de câmbio.

| Prática ITIL 4 | Mecanismo no COGME | Evidência | Estado |
|---|---|---|---|
| Gestão do conhecimento | OKB + KB-INDEX + glossário + lições + Canon_Stack_SDD | este documento; KB-TAX-001 | ✅ |
| Habilitação de mudança | CR → ADR → CCB → bump + changelog; **tipos standard/normal/SEV formalizados (§2.5)** | §2.5; ccb-log | ✅ (encerra C-23) |
| Gestão de incidentes | Falha operacional que para o circuito (VIO-013..018: saída JSON dos scripts; registry corrompido 30/10; ledger truncado 25/10) | vio-register v1.1 | ⚠️ incidente e violação usam o mesmo registro (VIO) |
| Gestão de problemas | Auditoria de causa-raiz + lições aprendidas | AUD-2610-02..09; licoes-aprendidas/ | ⚠️ MF2/MF3 em 0 B |
| Gestão de configuração (CMDB) | Roster de agentes + inventário de artefatos | §4.1; KB-INDEX v1.3.0; `drafts/artefatos-metadados.csv` | ⚠️ sem CMDB canônico completo |
| Gestão de nível de serviço | Marcos M1–M4 como SLA acadêmico; coverage ≥ 80% | TAP §6; ADR-003 | ✅ (informal, sem OLA) |
| Gestão de fornecedores | Whitelist FOSS; APIs de câmbio com fallback; cloud free tier restrito | ADR-010; C-P-01/02 | ⚠️ registro de dependências vazio (C-08) |
| Segurança da informação | LGPD primária, OWASP baseline, fail-closed, DEVSECOPS-001 | Art. 7; DEVSECOPS-001 | ✅ |
| Melhoria contínua (CSI) | Retrospectiva quinzenal; lições por macro-fase; SIR | §7.1; plano-qualidade | ✅ |
| Implantação e liberação | GitHub Actions ratificados (CI-CD-GOV-001); gate de coverage | ADR-010; §1.6 | ✅ (runbook de release pendente) |
| Catálogo de serviços | **nenhum** | — | ❌ o "serviço" (conversor + API + documentação) não está catalogado |
| Service desk 24×7 | — | — | ⛔ não aplicável (acadêmico, sem operação contínua) |

### 9.4 Síntese, exclusões declaradas e leitura crítica

| Lente | ✅ | ⚠️ | ❌ | ⛔ excluído por YAGNI |
|---|---|---|---|---|
| PMBOK 7ª (8 domínios) | 4 | 4 | 0 | — |
| TOGAF ADM (10 fases + requisitos) | 5 | 4 | 2 | maturidade de arquitetura; roadmap plurianual |
| ITIL 4 (11 práticas) | 6 | 3 | 1 | service desk 24×7; OLA formal |

**Leitura crítica.** A cobertura é adequada a um projeto de um semestre com equipe de 3 pessoas, mas três lacunas são materiais: (i) **arquitetura de dados inexistente** (DER é entregável de M2, marco vencido); (ii) **arquitetura de transição ausente** (ADR-010 trocou SQLite por PostgreSQL sem uma linha de cronograma/custo/recurso correspondente, e o REQ-07 ainda especifica SQLite); (iii) **medição sem baseline real** — as metas de fluxo são aspiracionais, o que impede afirmação de desempenho verificável em M3/M4.

**Contrapeso de honestidade.** As três lacunas acima **não** foram convertidas em novos artefatos nesta normalização: criar DER, plano de migração e baseline real é trabalho de M2/M3 sob custódia própria (`agent-backend-dev`, `agent-pm`), não de um documento de conhecimento. Registrá-las é o máximo que este OKB pode fazer sem violar YAGNI nem a separação de custódias.

---

## 10. INCONSISTÊNCIAS, LACUNAS E PENDÊNCIAS

### 10.1 Registro de consistência (OKB-C)

| ID | Sev. | Achado | Evidência | Status / ação |
|---|---|---|---|---|
| OKB-C-01 | Alta | Hierarquia praticada ("TAP > OKB > Glossário > ADRs") contradizia a Constituição | OKB v3.0; Art. 2.1 | ✅ corrigido em v5.0.0 §1.1 |
| OKB-C-02 | Alta | Índice declara ADR-001..004 `1.1.0 ratified`; arquivos reais são `1.0.0` | KB-INDEX:41-44 vs frontmatter | ❌ aberto (KB-INDEX a harmonizar ou ADRs a bumpar — decisão CCB) |
| OKB-C-03 | Crítica | VIO-006: evento destrutivo 24/10 reverteu leis sem trilha git; conteúdo v4.0.0 irrecuperável | vio-register; AUD-2610-04:48 | ✅ encerrado por decisão Humana/CCB (2026-11-05, kill switch Art. 5.1); conteúdo pré-evento irrecuperável — registrado como evidência histórica, nunca apagado |
| OKB-C-04 | Baixa | ADR-006 triplicada | md5 idêntico `91e91ef1…` | ✅ resolvido — apenas a canônica restou |
| OKB-C-05 | Alta | Teto GMV de ADRs (≤ 10) excedido: 13 IDs (14 artefatos) | §2.6 | ✅ encerrado — teto revisado para ≤ 20 (decisão CCB); 13 IDs (14 artefatos) dentro do novo teto |
| OKB-C-06 | Crítica | CR-001 repactua M2 → 15/11/2026, colide com M3; ADR de emenda emitida (ADR-015) e ratificada (RAT-2026-10-31-A12); Delta Log criado | CR-001; ADR-015; plano-cronograma:80; docs/tap/delta-v3-1.md | ✅ resolvido (C-06 principal) — ADR-015 emitida e ratificada 31/10/2026; CR-001 formalizado. Ressalva C-06b (colisao M2=M3 em 15/11) segue aberta para deliberacao futura do CCB (fusao M2+M3, deslocamento M3 ate M4, ou manutencao) |
| OKB-C-07 | Alta | Glossário contradiz canon (13/48, Qwen 32B, SQLite, hierarquia invertida) | glossario:8,18,23,161 | ✅ **resolvido nesta rodada** — sanitize + bump v3.2.0 (31/10; RAT-2026-10-31-A11); re-verificar na próxima auditoria |
| OKB-C-08 | Alta | Artefatos 0 B: `TAP.md`, `registro.md`, `requisitos.md`, `.ai/specs/{tap,eap,requisitos}.md` | `wc -c` = 0 | ❌ aberto (baseline.md recebeu seed simulado — ressalva C-16) |
| OKB-C-09 | Alta | TAP canônico só como `.docx` + bloco integral no plano-integral; `.md` é stub declarado "não-0B" no índice | KB-INDEX:29; plano-integral:49 | ❌ aberto |
| OKB-C-10 | Alta | Frontend: ADR-001 fixa vanilla JS; roster/infra assumem Jinja+HTMX+Tailwind | ADR-001:31; VIO-001 | ❌ aberto — ADR de emenda |
| OKB-C-11 | Baixa | Custódia do OKB divergia sem registro recuperável | KB-INDEX:48 | ✅ resolvido — CCB-003 ratificou owner `agent-architect` |
| OKB-C-12 | Média | ADR-005 em regularização tardia com ratificação formal pendente | ADR-005:6,56 | ✅ encerrada — ADR-005 v1.1.0 status `ratificado`, instrumentos CCB-LOG A08 + A12, incorpora Regime de Emenda Controlada (ADR-013) e Emenda M2 (ADR-015); `adr-005-freeze.md` marcada SUPERSSEDIDA (superseded-by: ADR-005 v1.1.0) |
| OKB-C-13 | Baixa | Classes `relatorio-auditoria`, `register-vio`, `register-decision` fora do enum de 10 classes | kb-taxonomy §2; audits | ⏳ próxima rodada |
| OKB-C-14 | Baixa | Colisão de ID `CR-001` | CR-001; plano-escopo:178 | ⏳ renumerar CRs |
| OKB-C-15 | Baixa | Constituição em VIGENTE-INTERINA | constitution.md:3 | ✅ resolvido — VIGENTE-PLENA, commit `7cff886` (30/10) |
| OKB-C-16 | Baixa | Metas de fluxo sem baseline real | baseline.md seed SIMULADO (A09-A-006) | ⚠️ seed promulgada; medição real em M3 |
| OKB-C-17 | Média | Glossário: cabeçalho 3.1 × índice 3.2.0 | glossario:1; KB-INDEX:51 | ✅ resolvido — arquivo sanitizado para v3.2.0 real (31/10) |
| OKB-C-18 | Baixa | ADR-001 cita ADR-005/006 como "Draft" e mantém "QwenStudio" | ADR-001:11,32 | ⏳ emenda editorial ADR-001 |
| OKB-C-19 | Média | Colisão de rótulos P# (TAP × Constituição) | §5.1/§5.2 | ✅ resolvido (~ namespace `TAP-P#` / `C-P-##` declarado — efeito prospectivo, §5.1) |
| OKB-C-20 | Baixa | Sem índice de ADRs em `docs/decisoes/` | ls docs/decisoes | ⏳ criar README/INDEX |
| OKB-C-21 | Crítica | Constituição continha Arts. 5–10 duplicados (duas redações no mesmo arquivo) | constitution.md | ✅ **resolvido** — corpo consolidado (11 cabeçalhos ART., Art. 6 único); co-assinatura humana registrada 30/10 (A01). Ressalva de bump em C-27 |
| OKB-C-22 | Alta | ADR-010 não propagada: REQ-07 ainda pede SQLite; sem Docker/PostgreSQL em cronograma/custos/recursos | plano-integral:77; buscas = 0 | ❌ aberto — plano de transição + estimativa |
| OKB-C-23 | Média | Tipos de mudança não definidos normativamente | ccb-log (A01–A10) | ✅ **resolvido** — formalizado em §2.5 (31/10); sinalização `change-class:` efeito prospectivo |
| OKB-C-24 | Média | Sem registro/matriz de partes interessadas | TAP §1.c/TAP-P7; ADR-008 | ✅ encerrado — matriz inserida em §9.1.1 (avaliador, GP/CCB, equipe de 3) |
| OKB-C-25 | Média | CCB-LOG cita `docs/governanca/plano-consolidacao-estrutural.md` inexistente | ccb-log:6; A02 | ✅ encerrado — plano criado em `docs/governanca/plano-consolidacao-estrutural.md` (v1.0.0, ativo) |
| **OKB-C-26** | **Crítica** | **Colisão de ID: dois artefatos diferentes usavam `ADR-013`** (`adr-013-regime-emenda-tap.md` e `ADR-013-SDDAI-Promulgacao.md`); resolvida por renumeração para ADR-014 | ls docs/decisoes; adr-014-sddai-promulgacao.md:144 (nota de renumeração); RAT-2026-10-31-A12 | ✅ resolvido — ADR-013-b renumerada para ADR-014 por decisão CCB (RAT-2026-10-31-A12); catálogo OKB §2.1 e KB-INDEX atualizados nesta rodada |
| **OKB-C-27** | **Média** | **Bump da Constituição não aplicado:** A09-A-001 ratifica "constitution.md v1.2.1 (sanitizada)", mas o header do arquivo continuam v1.2.0 e o hash co-assinado `b3f296c6…` não foi re-gerado após consolidação | head constitution.md; ccb-log A09 | ❌ aberto — bump editorial + hash dedicado (Art. 5.4) |
| **OKB-C-28** | **Baixa** | **Inconsistência temporal:** ADR-013-a frontmatter `date: 2026-11-01` e entrada RAT-2026-11-01-A08, enquanto o instrumento e demais artefatos da rodada são de 30–31/10 | frontmatter; ccb-log; `date` do FS (31/10) | ⏳ ajuste editorial no próximo saneamento incluindo provas de data |

### 10.2 Decisões humanas requeridas (não executadas por agente)

1. **OKB-C-26** — renumerar ADR-013-dupla e padronizar o catálogo — **bloqueia cross-references nuevos**.
2. **OKB-C-21/C-27** — validar consolidação da Constituição e aplicar bump v1.2.1 + re-hash.
3. **OKB-C-06** — ratificar/ajustar CR-001 e emitir ADR de emenda do marco (M2 × M3) via regime ADR-013-a.
4. **OKB-C-22** — decidir a arquitetura de transição SQLite → PostgreSQL (ADR-010): plano, estimativa e reflexo no cronograma/custos antes de qualquer card de dados.
5. **OKB-C-05** — ✅ encerrado: teto de ADRs revisado para ≤ 20 (decisão CCB). 13 IDs (14 artefatos) dentro do novo teto.
6. **OKB-C-03** — encerrar VIO-006 (kill switch: só o Humano encerra).
7. **OKB-C-12** — ✅ encerrada: ADR-005 v1.1.0 ratificada (CCB-LOG A08 + A12); `adr-005-freeze.md` SUPERSSEDIDA.
8. **OKB-C-24** — ✅ encerrado: matriz de partes interessadas inserida em §9.1.1.
9. **OKB-C-25** — ✅ encerrado: `docs/governanca/plano-consolidacao-estrutural.md` criado (v1.0.0).
10. **Ratificação deste OKB v5.2.0** — ✅ **CUMPRIDA** nesta emissão (CCB-LOG RAT-2026-10-31-A11, 31/10/2026; bloco §13).

---

## 11. PROVENIÊNCIA E LIMITES

Esta versão é uma **normalização**, não uma reescrita: corpo normativo de v5.1.0 preservado íntegro; divergências de estado atualizadas com fonte. Tudo o que existia apenas na v4.0.0 (perdida em VIO-006) permanece `UNKNOWN-GAP`. Fontes usadas estão em `derived-from`; cada afirmação normativa cita a fonte no corpo. O OKB é **parte constitutiva do SSOT** e sujeito a auditoria extraordinária dedicada: a desta rodada é **AUD-2610-09** (docs/auditorias/aud-2610-09-okb-normalizacao.md).

---

## 12. CHANGELOG NORMATIVO (VER-NNN — formato canônico)

| ID | Versão | Data | Base | Registro de mudança | Instrumento de ratificação |
|---|---|---|---|---|---|
| VER-001 | v2.1 | ~09/2026 | — | guardrail original | — |
| VER-002 | v3.0 | 20/09/2026 | TAP v3 | consolidação pré-M1; 4 ADRs; 27 labels; backlog M1 | implícita (fluxo de forja) |
| VER-003 | v3.1 | 22/09/2026 | v3.0 | pós-M1; freeze; política de ADRs | implícita (pre-COB) |
| VER-004 | v4.0.0 | 23/10/2026 | v3.1 + dedupe | corpus único (594 l) — **perdido em VIO-006** | — |
| VER-005 | v5.0.0 | 30/10/2026 | v3.0 + ADRs 001–012 + Constitution 1.2.0 | reemissão: frontmatter, hierarquia corrigida, catálogo ADR, estado as-of, inventário, achados, padrão de citação | — (draft absorvido por VER-006) |
| VER-006 | v5.1.0 | 30/10/2026 | v5.0.0-draft + PMBOK/TOGAF/ITIL | primeira versão ratificada: §9 cobertura metodológica; C-22..C-24; poda YAGNI; promoção a corpus canônico único; SHA `ac27f0c1…9547` (bloco ratificado antes da promulgação) | CCB-003 (30/10) |
| **VER-007** | **v5.2.0** | **31/10/2026** | v5.1.0 + rodada de estado 31/10 (A08–A10, VIO-013..025) | **(a) Template canônico OKB-TEMPLATE-CANON v1.0 adotado** (nomenclatura OKB \| Operational Knowledge Base; índice normativo; blocos I–IV; changelog VER-NNN; bloco de co-assinatura §13). **(b) Sanitize:** glossário v3.1 → v3.2.0 (hierarquia, EAP 12/37, PostgreSQL, Qwen MoE, refs); patch list §8.4 executada (personas ×2, ADR-012, plano-integral ×6) — cada alvo com bump/changelog próprio ou ressalva complementar. **(c) Normatize:** §2.5 tipos de mudança (encerra C-23); §5.1 namespace TAP-P#/C-P-## (encerra C-19 para o corpus); §1.4/§1.6 regimes ADR-013-a, CI-CD-GOV-001 e DEVSECOPS-001. **(d) Persistência:** estado as-of 31/10 (§3.6); inventário atualizado (baseline seed, ADR-013-a/b, normas técnicas, artefatos promulgados). **(e) Auditoria:** AUD-2610-09 extraordinária dedicada; achados novos C-26/C-27/C-28. **(f) Governança:** CCB-LOG A11 (aprovação indireta via agente, autorização expressa e deliberativa do GP); ledger append; KB-INDEX bump 1.2.0→1.3.0 | **CCB-LOG RAT-2026-10-31-A11** — CCB único (GP Leonardo), aprovação indireta via agente com gatilho de permissão prévia deliberativo executado |

---

## 13. BLOCO DE RATIFICAÇÃO E CO-ASSINATURA (Art. 5.4 da Constituição)

Este bloco não integra o hash normativo.

| Campo | Valor |
|---|---|
| Documento | OKB-001 — OKB \| Operational Knowledge Base — Base de Conhecimento Operacional do Projeto COGME |
| Versão ratificada | 5.2.0 |
| Status | ratified |
| Template | OKB-TEMPLATE-CANON v1.0 (canônico até decisão posterior do CCB) |
| Instrumento | **CCB-LOG RAT-2026-10-31-A11** (registro vivo append-only) + prompt deliberativo de permissão prévia do GP (31/10/2026) |
| Ratificador | Gerente de Projeto — CCB de membro único (Art. 5.4: papel, sem nome civil) |
| Aprovação indireta via agente | SIM — autoridade plena delegada ao agente executor e à cadeia subordinada, com CCB encerrando a auditoria após o fato (gatilho de permissão prévia executado e registrado) |
| Data da ratificação | 2026-10-31 |
| Assinatura | `/s/ CCB de membro único` — co-assinada: `/s/ agent-architect` (custódia OKB) e `/s/ AUD-2610-09` (parecer de auditoria extraordinária) |
| SHA-256 do conteúdo normativo | `9ebe406629e7f71a0bc127a8b7692a395d82171b097ebc8b9c3ea2f73b3330e5` |
| Método de verificação | `sha256sum` sobre os bytes do início do arquivo até a linha imediatamente anterior a `## 13. BLOCO DE RATIFICAÇÃO` |
| Cross-reference com o Plano de Projeto | plano-integral-tap-1-2-3-4-5.md (TAP v3 integral + Plano de Projeto híbrido, ADR-013-a) — refs atualizadas (§8.4); KB-INDEX v1.3.0; ccb-log A11; ledger append |
| Escopo | ratifica + promulga o OKB v5.2.0 como documento de conhecimento canônico único sob o template OKB-TEMPLATE-CANON v1.0; aplica sanitize + propagação + auditoria extraordinária |
| Efeito | substitui o OKB v5.1.0 como corpus vivo; não altera Constituição, TAP (núcleo blindado) nem ADRs |
| Ressalvas | OKB-C-03, C-05, C-06, C-08, C-09, C-10, C-12, C-22, C-24, C-25, **C-26, C-27, C-28** seguem **abertos**; a ratificação não os sana |
| Revogação | apenas por CCB com emenda registrada e novo bump de versão |

*Fim do documento — OKB v5.2.0 (ratificado) | template OKB-TEMPLATE-CANON v1.0 | COGME | Fatec Taquaritinga | 31/10/2026*
