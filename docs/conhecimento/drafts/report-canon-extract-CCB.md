# [Context]

**Objeto:** Relatório Guia de Retificação Modular do `Plano-de-Projeto-COGME_v2.0.1-ONGOING.docx` (167 páginas, emitido 25/10/2026).
**Natureza:** Consolidação brutal das Rodadas 1 e 2 de análise, com extração canônica de dados e validação cruzada de referências.
**Fontes autorizadas:** `constitution.md` v1.2.0 · `TAP.docx` v3 (18/09/2026) · ADRs 001–012 · `OKB_v5.0.0-candidate.md` · `OKB_COGME_v3.1.md` · `Glossario.md` v3.1 · `notas_adjacentes.md` v2.0 · `Monografia-COGME.pdf` · `artefatos-metadados.csv`.
**Hierarquia aplicada:** Constitution v1.2.0 > TAP v3 (ADR-005) > ADRs 001–012 > OKB v5.0.0-candidate > Planos > Glossário > Specs > Código.
**Data-base:** 31/10/2026.
**Obsolescência declarada:** PMBOK 6ª = dicionário terminológico. Governança primária = PMBOK 7ª (12 princípios + 8 domínios de desempenho).

---

# [Artifact/Decision] — Relatório Guia de Retificação Modular

## 1. Veredito Executivo Unificado

O artefato `Plano-de-Projeto-COGME_v2.0.1-ONGOING.docx` **não é um Plano de Projeto profissional** — é uma **monografia acadêmica com planos de área embutidos**, contendo:

- **7 defeitos críticos** de forma (monografia vs. plano);
- **14 violações diretas** de ADRs vigentes (001, 005, 006, 007, 008, 009, 010, 011, 012);
- **6 marcadores `[A CONFIRMAR]`** em pontos críticos (Tabelas 88, 127, 128; Seções 4.4, 4.7; Referências);
- **Stack drift silencioso** (SQLite, Qwen 32B, HTMX/Tailwind/Jinja2) em relação às ADRs 006 e 010;
- **Constituição v1.2.0 totalmente ausente** do corpo do documento;
- **Glossário v3.1 com 7 violações** que contaminam o plano por cross-reference;
- **CR-001 (M2 → 15/11)** não formalizado, colidindo com M3.

**Veredito:** o documento exige **bifurcação imediata** em dois artefatos distintos e **retificação modular** em 9 blocos acionáveis, com validação rigorosa de cross-references e gate de qualidade por bloco.

---

## 2. Matriz Consolidada de Defeitos (P0/P1/P2)

### 2.1 Defeitos P0 — Críticos (bloqueiam a retificação)

| ID | Defeito | Evidência | ADR violada | Impacto |
|---|---|---|---|---|
| **D-C01** | Artefato é monografia, não plano | Capa Fatec, resumo, palavras-chave, listas ABNT, considerações finais, referências | GMV + ADR-012 | Inviabiliza uso como plano profissional |
| **D-C02** | TAP integral como capítulo 1 | "1 TERMO DE ABERTURA DO PROJETO" (32 páginas) | ADR-005 §Decisão (separação ontológica) | TAP não é plano; não pode ser revisado dentro do plano |
| **D-C03** | Constituição v1.2.0 ausente | Zero menções em 167 páginas | ADR-012 (artefato normativo supremo) | Plano opera sem âncora constitucional |
| **D-C04** | Grafia inconsistente do stakeholder | Capa: "DR. NIVALDO CARLETO" (correto); corpo: "Prof. Ms. Nivaldo Carleto" (Tabelas 1, 10, 27) | ADR-008 v1.1.0 ("Prof. Dr. Nivaldo Carleto") | Ofensa institucional; inconsistência interna |
| **D-C05** | Stack desatualizada (SQLite/Qwen 32B) | Tabela 88 (SQLite); Tabela 119 (SQLite + QwenStudio); REQ-07 (cache SQLite) | ADR-006 (Qwen3-30B-A3B MoE) + ADR-010 (PostgreSQL 15+) | Stack drift silencioso; violação de freeze |
| **D-C06** | Frontend desatualizado | Tabela 119: "HTMX + Tailwind + Jinja2" | ADR-001 v1.0.0 (HTML5/CSS3/JS vanilla) | Conflito aberto com OKB-C-10 |
| **D-C07** | 6 marcadores `[A CONFIRMAR]` | Tabelas 88, 127, 128; Seções 4.4, 4.7; Referências (Decreto IOF) | P-08 (honestidade) + OKB §0.2 | Plano publicado com lacunas assumidas |

### 2.2 Defeitos P1 — Altos (distorcem o conteúdo)

| ID | Defeito | Evidência | ADR violada |
|---|---|---|---|
| **D-A01** | ADRs 006–012 não referenciadas | Catálogo para em 001–004 | ADR-012 §2 (hierarquia trifásica) |
| **D-A02** | ADR-007 sem frase canônica | Redes CPM incluídas (Figuras 16–21) sem "a rede valida o marco; o Kanban executa a tarefa" | ADR-007 v1.1.0 §Decisão |
| **D-A03** | ADR-011 ignorada | Zero menções a MCPs, ledger.yaml, L1/L2/L3 | ADR-011 v1.0.0 |
| **D-A04** | CR-001 não formalizado | M2 repactuado para 15/11/2026 colide com M3; sem ADR | OKB-C-06 |
| **D-A05** | Seção 3 é spec técnica, não plano | 13 páginas de arquitetura, código, APIs | GMV + separação ontológica |
| **D-A06** | Seção 4 é monográfica | "Síntese do Projeto", "Trabalhos Futuros" | GMV |
| **D-A07** | Planos 6–8 sem carimbo de versão | Recursos (Edson), Comunicações (Fabricio), Riscos (Leonardo) | OKB §4.1 |
| **D-A08** | Contagem EAP divergente no Glossário | Glossário v3.1 afirma "13 fases + 48 pacotes" | ADR-009 v1.0.0 (12/37 canônicos) |
| **D-A09** | Cycle Time com definição errada | Glossário v3.1: "To Do → Done" | ADR-003 v1.0.0 (In Progress → Done) |

### 2.3 Defeitos P2 — Médios (cosméticos, acumulativos)

| ID | Defeito |
|---|---|
| D-M01 | Numeração de seções inconsistente (1, 1., 2.1, 2.6.1.1) |
| D-M02 | Figuras numeradas de 1 a 33, mas referenciadas como "FIG-1" em alguns pontos |
| D-M03 | Tabela 119 mistura versões "(projeto)" e "(estável)" sem critério claro |
| D-M04 | Tabela 122 (Wise API) em seção de Desenvolvimento — deveria estar em spec técnica |
| D-M05 | Referências ABNT completas em plano profissional (YAGNI) |
| D-M06 | Tabela 129 (controle de versões) cita v2.0 em 25/10, divergindo do CSV (v1.0.0) |

---

## 3. Blocos Modulares de Retificação

Cada bloco possui: **escopo**, **cross-references obrigatórias**, **gate de validação**, **responsável** e **estimativa**.

### Bloco B1 — Bifurcação Monografia × Plano (P0 · 8h)

**Escopo:** Separar o artefato em dois:
1. **Monografia acadêmica** (`Monografia-COGME-v2.0.docx`): mantém capa Fatec, resumo, listas, considerações finais, referências ABNT.
2. **Plano de Projeto profissional** (`Plano-de-Projeto-COGME_v2.0.md`): frontmatter YAML, seções objetivas, cross-references.

**Estrutura canônica do Plano profissional:**
```yaml
---
id: PLANO-PROJETO
version: 2.0.0
status: draft
owner: agent-pm
derived-from:
  - constitution.md v1.2.0
  - TAP v3 (18/09/2026)
  - ADRs 001-012
  - OKB v5.0.0-candidate
---
```

**Cross-references obrigatórias:**
- Constitution v1.2.0 (ADR-012)
- TAP v3 §3, §4, §6, §8, §9, §11
- ADRs 001–012 (catálogo completo)
- OKB v5.0.0-candidate §1.1 (hierarquia)

**Gate de validação:**
- [ ] Monografia preservada como artefato separado
- [ ] Plano profissional com frontmatter YAML
- [ ] Zero elementos monográficos no plano (resumo, palavras-chave, listas ABNT)
- [ ] Cross-references validadas contra fontes canônicas

**Responsável:** GP Leonardo · **Estimativa:** 8h

---

### Bloco B2 — Saneamento de ADRs Violadas (P0 · 6h)

**Escopo:** Find & replace global + inserções obrigatórias.

| ADR | Ação | Localização |
|---|---|---|
| ADR-008 | Substituir "Prof. Ms. Nivaldo Carleto" → "Prof. Dr. Nivaldo Carleto" | Tabelas 1, 10, 27, 39, 55, 61, 70, 82, 105, 128 |
| ADR-006 | Substituir "Qwen 32B Instruct" → "Qwen3-30B-A3B Q4_K_M (MoE)" | Tabelas 88, 119, 120 |
| ADR-010 | Substituir "SQLite" → "PostgreSQL 15+" (exceto em testes isolados) | Tabelas 88, 119; REQ-07; Tabela 40 (fronteira OUT) |
| ADR-001 | Corrigir frontend: "HTMX + Tailwind + Jinja2" → "HTML5/CSS3/JS vanilla" | Tabela 119 |
| ADR-007 | Inserir frase canônica: "A rede valida o marco; o Kanban executa a tarefa" | §2.4.4 (após Figura 15) |
| ADR-011 | Adicionar seção referenciando MCPs (nexus-ledger, nexus-dispatch, nexus-validate, nexus-kb) e separação L1/L2/L3 | Nova seção §2.9 |
| ADR-012 | Adicionar §2 declarando subordinação à Constituição v1.2.0 | Início do plano |

**Cross-references obrigatórias:**
- ADR-008 v1.1.0 (grafia canônica)
- ADR-006 v2.0.0 (modelo primário MoE)
- ADR-010 v1.0.0 (PostgreSQL 15+)
- ADR-001 v1.0.0 (frontend vanilla)
- ADR-007 v1.1.0 (dualidade CPM × Kanban)
- ADR-011 v1.0.0 (MCPs e L1/L2/L3)
- ADR-012 v1.0.1 (Constituição como artefato supremo)

**Gate de validação:**
- [ ] Zero ocorrências de "Ms. Nivaldo" ou "Carletto" (duplo t)
- [ ] Zero ocorrências de "Qwen 32B" ou "QwenStudio"
- [ ] SQLite apenas em testes isolados (explicitado)
- [ ] Frontend vanilla (HTMX/Tailwind/Jinja2 removidos)
- [ ] Frase canônica da ADR-007 presente
- [ ] Seção ADR-011 (MCPs) inserida
- [ ] Subordinação à Constituição declarada

**Responsável:** Fabricio (find & replace) + Leonardo (review) · **Estimativa:** 6h

---

### Bloco B3 — Remoção do TAP Embutido (P0 · 2h)

**Escopo:** Remover integralmente a Seção 1 (TAP) do Plano de Projeto. Substituir por cross-reference:

> "O Termo de Abertura do Projeto (TAP v3, congelado em 18/09/2026 conforme ADR-005) é o artefato autorizativo canônico e não integra este plano. Ver `docs/tap/TAP.docx`."

**Cross-references obrigatórias:**
- ADR-005 v1.0.0 (freeze do TAP)
- TAP v3 (18/09/2026)

**Gate de validação:**
- [ ] Zero páginas de TAP no corpo do plano
- [ ] Cross-reference ao TAP.docx canônico inserida

**Responsável:** Leonardo · **Estimativa:** 2h

---

### Bloco B4 — Eliminação de `[A CONFIRMAR]` (P0 · 4h)

**Escopo:** Preencher ou declarar `INSUFFICIENT DATA` com assunção documentada.

| Marcador | Ação | Fonte canônica |
|---|---|---|
| Tabela 88 (baseline calibração) | Declarar `INSUFFICIENT DATA` (OKB-C-08, OKB-C-16) | OKB v5.0.0 §6.2 |
| Tabela 127 (responsável Seção 3) | Preencher: "Fabricio de Lima Cabral" | Tabela 129 (controle de versões) |
| Tabela 128 (atendimento SMART) | Preencher status real (M1 ✅; M2 ⚠️; M3 ⏳; M4 ⏳) | OKB v5.0.0 §3.2 |
| Seção 4.4 (lições aprendidas) | Transpor LA-001 + I1–I8 de `notas_adjacentes.md` §6 e §8 | `notas_adjacentes.md` |
| Seção 4.7 (conclusão) | Remover marcador; manter parágrafo como provisório | — |
| Decreto IOF (referências) | Confirmar Decreto 6.306/2007 (já consta); remover marcador | Monografia Referências |

**Cross-references obrigatórias:**
- OKB v5.0.0 §6.2 (baseline)
- `notas_adjacentes.md` §6 (LA-001) e §8 (I1–I8)
- Tabela 129 (controle de versões)

**Gate de validação:**
- [ ] Zero ocorrências de `[A CONFIRMAR]`
- [ ] Todos os `INSUFFICIENT DATA` com referência OKB-C
- [ ] Lições aprendidas transpostas para `MF2-licoes.md`

**Responsável:** Edson (lições) + Leonardo (demais) · **Estimativa:** 4h

---

### Bloco B5 — Saneamento do Glossário v3.2 (P0 · 3h)

**Escopo:** Corrigir 7 violações no `Glossario.md` v3.1 antes do bump para v3.2.0.

| # | Violação | Correção canônica |
|---|---|---|
| V-01 | "Prof. Dr. Nivaldo Carletto" | → "Prof. Dr. Nivaldo Carleto" |
| V-02 | "13 fases + 48 pacotes" | → "12 fases + 37 pacotes" |
| V-03 | "Qwen 32B Instruct" | → "Qwen3-30B-A3B Q4_K_M (MoE)" |
| V-04 | "SQLite" como banco principal | → "PostgreSQL 15+" |
| V-05 | "HTMX + Tailwind" | → "HTML5 + CSS3 + JS vanilla" |
| V-06 | Hierarquia "TAP > OKB > Glossário > ADRs" | → "Constitution > TAP > ADRs > OKB > Planos > Glossário" |
| V-07 | Cycle Time "To Do → Done" | → "In Progress → Done" |

**Cross-references obrigatórias:**
- ADR-008 v1.1.0 (grafia)
- ADR-009 v1.0.0 (EAP 12/37)
- ADR-006 v2.0.0 (modelo MoE)
- ADR-010 v1.0.0 (PostgreSQL)
- ADR-001 v1.0.0 (frontend)
- ADR-012 v1.0.1 (hierarquia)
- ADR-003 v1.0.0 (Cycle Time)

**Gate de validação:**
- [ ] `grep` negativo para "Carletto", "13 fases", "48 pacotes", "Qwen 32B", "To Do → Done"
- [ ] Bump para v3.2.0 com changelog
- [ ] Cross-references validadas

**Responsável:** Edson + Leonardo (review) · **Estimativa:** 3h

---

### Bloco B6 — Formalização de CR-001 (P0 · 2h)

**Escopo:** Emitir ADR de marco formalizando a repactuação do M2 para 15/11/2026, resolvendo a colisão com M3.

**Cross-references obrigatórias:**
- OKB-C-06 (CR-001 não formalizado)
- TAP §6 (marcos canônicos)
- ADR-005 (freeze do TAP)

**Gate de validação:**
- [ ] CR-001 formalizado em `docs/change-requests/CR-001-m2-replanejamento.md`
- [ ] ADR de marco emitida (ADR-013?)
- [ ] Colisão M2 × M3 resolvida

**Responsável:** Leonardo (CCB) · **Estimativa:** 2h

---

### Bloco B7 — Reestruturação de Seções Técnicas (P1 · 4h)

**Escopo:** Mover Seção 3 (Desenvolvimento) para artefato separado: `docs/especificacoes/arquitetura-COGME.md`. O Plano de Projeto deve apenas **referenciar** a arquitetura, não detalhá-la.

**Cross-references obrigatórias:**
- GMV (princípio de governança mínima viável)
- OKB v5.0.0 §8.1 (cross-reference substitui duplicação)

**Gate de validação:**
- [ ] Seção 3 movida para spec técnica
- [ ] Plano referencia spec via cross-reference
- [ ] Zero detalhe técnico no plano

**Responsável:** Fabricio · **Estimativa:** 4h

---

### Bloco B8 — Normalização de Metadados (P1 · 1h)

**Escopo:** Alinhar versionamento.

**Cross-references obrigatórias:**
- KB-TAX-001 §4.5 (versionamento)
- `artefatos-metadados.csv`

**Gate de validação:**
- [ ] CSV atualizado (PLANO-PROJETO → v2.0.0)
- [ ] OKB v5.0.0 atualizado (após ratificação)
- [ ] Frontmatter YAML com `version: 2.0.0`

**Responsável:** Leonardo · **Estimativa:** 1h

---

### Bloco B9 — Ratificação do OKB v5.0.0 (P0 · 1h)

**Escopo:** CCB ratifica OKB v5.0.0-candidate como corpus canônico.

**Cross-references obrigatórias:**
- Constitution v1.2.0 Art. 5.1 (ratificação)
- OKB-C-02 (OKB v4.0.0 perdida em VIO-006)

**Gate de validação:**
- [ ] OKB v5.0.0 promovido de `draft` para `active`
- [ ] `docs/conhecimento/OKB.md` atualizado
- [ ] KB-INDEX.md atualizado

**Responsável:** Leonardo (CCB) · **Estimativa:** 1h

---

## 4. Decisões CCB Pendentes (não executáveis por agente)

| ID | Decisão | Urgência | Fundamentação |
|---|---|---|---|
| **D-C1** | Ratificar OKB v5.0.0 como corpus canônico | 🔴 P0 | Substitui OKB v3.0 + v4.0.0 perdida (VIO-006) |
| **D-C2** | Formalizar CR-001 (M2 → 15/11) com ADR de marco | 🔴 P0 | Colide com M3; sem ADR = OKB-C-06 |
| **D-C3** | Consolidar Constitution v1.2.0 (Arts. 5–10 duplicados) | 🔴 P0 | OKB-C-21 — ambiguidade normativa |
| **D-C4** | Ratificar ADR-005 (ratificação pendente desde 28/10) | 🟠 P1 | OKB-C-12 |
| **D-C5** | Resolver teto de ADRs (12 emitidas vs limite GMV de 10) | 🟠 P1 | OKB-C-05 — opções: (a) elevar teto para 14; (b) classificar 006–012 como "emendas constitucionais derivadas" |
| **D-C6** | Confirmar custódia do OKB (`agent-architect` vs `agent-docker-specialist`) | 🟡 P2 | OKB-C-11 |
| **D-C7** | Resolver conflito de frontend (ADR-001 vanilla vs registry Jinja/HTMX) | 🟡 P2 | OKB-C-10 — exige ADR de emenda |
| **D-C8** | Encerrar VIO-006 (kill switch) | 🟡 P2 | OKB-C-03 — só humano encerra |

---

## 5. Matriz de Validação de Cross-References

| Origem | Destino | Validação |
|---|---|---|
| Plano §2 (Hierarquia) | Constitution v1.2.0 | ✅ ADR-012 |
| Plano §3 (TAP) | TAP.docx v3 | ✅ ADR-005 |
| Plano §4 (ADRs) | ADRs 001–012 | ✅ OKB v5.0.0 §2.1 |
| Plano §5 (OKB) | OKB v5.0.0 | ✅ Ratificação pendente (D-C1) |
| Plano §6 (Glossário) | Glossário v3.2.0 | ⏳ Saneamento pendente (B5) |
| Plano §7 (Specs) | `docs/especificacoes/arquitetura-COGME.md` | ⏳ Criação pendente (B7) |
| Tabela 88 (baseline) | `docs/metricas/baseline.md` | ❌ 0 B (OKB-C-08) |
| Tabela 119 (stack) | ADR-001 + ADR-006 + ADR-010 | ❌ Desatualizada (B2) |
| Tabela 127 (responsável) | Tabela 129 (controle de versões) | ✅ Fabricio (B4) |
| Tabela 128 (SMART) | OKB v5.0.0 §3.2 | ✅ Status real (B4) |

---

## 6. Cronograma de Retificação (alinhado ao M3)

| Bloco | Prioridade | Estimativa | Responsável | Prazo |
|---|---|---|---|---|
| B1 (Bifurcação) | 🔴 P0 | 8h | Leonardo | 03/11/2026 |
| B2 (ADRs) | 🔴 P0 | 6h | Fabricio + Leonardo | 04/11/2026 |
| B3 (TAP) | 🔴 P0 | 2h | Leonardo | 04/11/2026 |
| B4 (`[A CONFIRMAR]`) | 🔴 P0 | 4h | Edson + Leonardo | 05/11/2026 |
| B5 (Glossário) | 🔴 P0 | 3h | Edson + Leonardo | 05/11/2026 |
| B6 (CR-001) | 🔴 P0 | 2h | Leonardo (CCB) | 06/11/2026 |
| B7 (Seção 3) | 🟠 P1 | 4h | Fabricio | 07/11/2026 |
| B8 (Metadados) | 🟠 P1 | 1h | Leonardo | 07/11/2026 |
| B9 (OKB) | 🔴 P0 | 1h | Leonardo (CCB) | 07/11/2026 |
| **Total** | — | **31h** | — | **07/11/2026** |

**Marco intermediário:** 07/11/2026 (8 dias antes do M3 em 15/11/2026).

---

# [PMBOK Traceability]

| Domínio PMBOK 7ª | Aplicação nesta retificação |
|---|---|
| **Integração** | Hierarquia de autoridade (ADR-012) — Constituição no topo |
| **Escopo** | Fronteira entre artefatos canônicos e voláteis (Glossário) |
| **Cronograma** | CR-001 e colisão M2 × M3 (OKB-C-06) |
| **Qualidade** | 7 violações no Glossário — gate de saneamento |
| **Recursos** | Atribuição de responsáveis por bloco (Edson/Fabricio/Leonardo) |
| **Comunicações** | Cross-references canônicos (OKB §8.3) |
| **Riscos** | 8 decisões humanas requeridas (OKB-C-03/05/06/11/12/15/21) |
| **Medição** | Baseline 0 B = métrica aspiracional (OKB-C-16) |
| **Incerteza** | VIO-006 e OKB v4.0.0 perdida — kill switch (OKB-C-03) |

**Processos PMBOK 6ª (dicionário):** 4.6 (Controle Integrado de Mudanças), 8.3 (Controlar Qualidade), 10.3 (Monitorar Comunicações). Obsolescência procedural declarada.

---

# [Trade-offs]

| Decisão | Ganho | Perda/Risco | Mitigação |
|---|---|---|---|
| Bifurcação Monografia × Plano | Plano profissional utilizável | Perda de formato acadêmico no arquivo de governança | Monografia preservada como artefato separado |
| Remoção do TAP embutido | Compliance com ADR-005 | Redução de páginas (32 → 0) | Cross-reference ao TAP.docx canônico |
| Atualização de stack | Compliance com ADRs 006/010 | Retrabalho em Tabelas 88, 119, REQ-07 | Find & replace automatizado |
| Remoção de Seção 3 | Foco em governança | Perda de detalhe técnico | Arquitetura movida para spec separada |
| Saneamento do Glossário | Compliance com ADRs | ~3h de trabalho + revisão | `grep` negativo pós-saneamento |
| Formalização de CR-001 | Compliance com ADR-005 | Adiciona 1 ADR ao teto (OKB-C-05) | Classificar como "emenda constitucional derivada" |

---

# [Next Kanban Steps]

### Epic: `E09-Normalizacao-Documental` (WBS Level 1)

| Issue | Descrição | Estimativa | Responsável | Prioridade | Milestone |
|---|---|---|---|---|---|
| `#901-B1-Bifurcacao` | Separar monografia e plano profissional | 8h | Leonardo | 🔴 P0 | M3 |
| `#902-B2-ADRs` | Saneamento de ADRs violadas (006, 008, 010, 011, 012) | 6h | Fabricio + Leonardo | 🔴 P0 | M3 |
| `#903-B3-TAP` | Remover TAP embutido + cross-reference | 2h | Leonardo | 🔴 P0 | M3 |
| `#904-B4-A-CONFIRMAR` | Eliminar 6 marcadores `[A CONFIRMAR]` | 4h | Edson + Leonardo | 🔴 P0 | M3 |
| `#905-B5-Glossario` | Saneamento do Glossário v3.2.0 (7 violações) | 3h | Edson + Leonardo | 🔴 P0 | M3 |
| `#906-B6-CR-001` | Formalizar CR-001 + ADR de marco | 2h | Leonardo (CCB) | 🔴 P0 | M3 |
| `#907-B7-Secao-3` | Mover Seção 3 para spec técnica | 4h | Fabricio | 🟠 P1 | M3 |
| `#908-B8-Metadados` | Normalização de metadados (CSV + OKB) | 1h | Leonardo | 🟠 P1 | M4 |
| `#909-B9-OKB` | Ratificar OKB v5.0.0 | 1h | Leonardo (CCB) | 🔴 P0 | M3 |

### Gate de Qualidade (DoD) por Bloco

- [ ] Todos os `INSUFFICIENT DATA` resolvidos ou declarados irrecuperáveis com referência OKB-C
- [ ] Zero ocorrências de `[A CONFIRMAR]` no `.docx` (verificação via `grep`)
- [ ] Glossário v3.2.0 com `grep` negativo para "Carletto", "13 fases", "48 pacotes", "Qwen 32B", "To Do → Done"
- [ ] 8 decisões do CCB formalmente registradas em `docs/change-requests/` ou `docs/decisoes/`
- [ ] `artefatos-metadados.csv` atualizado com versões reais
- [ ] OKB v5.0.0 promovido de `draft` para `active` após ratificação
- [ ] Cross-references validadas contra fontes canônicas
- [ ] Revisão em pares (Code Review) em todos os blocos

### Kill Switch

Se a retificação exceder 31h sem progresso até **07/11/2026**, acionar Retrospectiva extraordinária (ADR-002) e reavaliar viabilidade do M3 (15/11/2026).

---

**Status da análise:** ✅ Completa e consolidada.
**Próxima ação:** Aprovação do CCB (GP Leonardo) para criação dos cards `#901`–`#909` no GitHub Projects.
**Prazo sugerido para conclusão:** 07/11/2026 (8 dias antes do M3).