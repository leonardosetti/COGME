# OKB v3.1 — Operational Knowledge Base (Consolidada Pós-M1)

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Data de Emissão:** 22/09/2026 (data do Marco M1 — Entrega Parcial Documental)
**Versão anterior:** OKB v3.0 (20/09/2026)
**Emissor:** GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carleto
**Hierarquia de autoridade:** TAP v3 > OKB v3.1 > Glossário v3.1 > ADRs 001–004 > Notas Adjacentes
**Regime do TAP:** Congelado (freeze) desde 18/09/2026 — não é objeto de revisão
**Status:** ✅ Convergente à Redação M1 v0.2 + TAP v3 + ADRs 001–004

---

## 1. VEREDITO SUMÁRIO

O OKB v3.1 consolida o estado do projeto no **Marco M1 (22/09/2026)**, incorporando as decisões estruturais tomadas entre 19/09 e 22/09/2026: entrega faseada dos planos (5 no M1, 3 no M2), regime de freeze do TAP, ADR-004 (tasklists Markdown), sistema de 27 labels, 5 milestones, padrão de cards ubíquos A/B, prioridade temporal P0–P3, e a política formal de ADRs. A Redação M1 Consolidada v0.2 é o artefato canônico de submissão ao Prof. Dr. Nivaldo Carleto; este OKB é o **instrumento de governança operacional** que sustenta a transição para o M2 (30/09/2026) e o período de calibração (23/09–03/10/2026).

**Mudanças críticas v3.0 → v3.1:**
- Contagem canônica da EAP fixada em **12 fases + 37 pacotes** (TAP §4) — divergências do Glossário (13/48) tratadas como artefato volátil
- Stack SDD local canônica nomeada: **llama.cpp + Qwen 32B + OpenCode**
- Regime de freeze do TAP formalizado (NC-00)
- Aditivo da Política de ADRs incorporado como seção formal (§6)
- Backlog M1 consolidado com status real de submissão
- Incidente LA-001 registrado como lição aprendida estrutural
- Saneamento de pendências externas (grafias, numerações, Cycle Time)

---

## 2. DECLARAÇÃO DE GOVERNANÇA (Convergente ao TAP §1.c)

### 2.1 Modelo Híbrido Declarado

| Camada | Fonte Normativa | Função no COGME |
|---|---|---|
| Governança primária | PMBOK® 7ª edição — 12 princípios + 8 domínios de desempenho | Define **por que** e **para quê**; orienta decisões por valor |
| Dicionário complementar | PMBOK® 6ª edição — processos citados apenas para rastreabilidade acadêmica | Fornece vocabulário estrutural; **obsolescência assumida para métricas preditivas (EVM)** |
| Método de execução | Manifesto Ágil + Kanban via GitHub Projects (SSOT) | Define **como** o trabalho é executado diariamente |
| Abordagem de desenvolvimento | Specification-Driven Development (SDD) com IA generativa auditável (stack local) | Geração de código e artefatos com revisão humana obrigatória |

### 2.2 Autoridade de Mudança (CCB)

**CCB = GP Leonardo David Silva Setti** — membro único, conforme TAP v3 §1.c e Premissa P7.
**Prof. Dr. Nivaldo Carleto:** stakeholder-avaliador nos marcos M1–M4, **sem ingerência operacional**.
**Trade-off declarado:** Velocidade decisória > colegialidade (simplificação pedagógica do TAP §9 P7).

### 2.3 Obsolescência Formalmente Declarada

O PMBOK® 6ª (2017) é tratado **exclusivamente como dicionário de processos**. Processos preditivos (4.1, 5.2, 6.5, 11.1) são citados apenas para rastreabilidade acadêmica. **Métricas EVM (SPI/CPI/VAC) são LEGADO e NÃO APLICÁVEIS** — substituídas por métricas de fluxo Kanban (Cycle Time, Throughput, CFD), conforme TAP §3 "Métricas e Indicadores" e Domínio de Medição PMBOK 7ª (ADR-003).

### 2.4 Estratégia de Entrega Faseada dos Planos

Conforme princípio de Elaboração Progressiva (PMBOK 6ª) e Personalização/Tailoring (PMBOK 7ª):

| Marco | Planos Entregues | Justificativa |
|---|---|---|
| **M1 (22/09/2026)** | Integração, Escopo, Cronograma, Custos, Qualidade (Áreas 1–5) | Fundação documental mínima viável; atendimento integral ao TAP §6 |
| **M2 (30/09/2026)** | Recursos, Comunicações, Riscos (Áreas 6–8) | Redigidos após calibração do fluxo Kanban (23/09–03/10) com dados empíricos |

**Trade-off:** Redução de ~30% da carga documental do M1, permitindo foco na qualidade dos 5 planos fundamentais e na configuração do SSOT.

### 2.5 Regime de Freeze do TAP (NC-00)

O TAP encontra-se **congelado desde 18/09/2026** (última versão anterior a todos os planos de gerenciamento). Duas regras derivam:
1. **Precedência intra-TAP:** em divergência entre seções do TAP, a seção §6 (Marcos) é canônica para matéria temporal.
2. **Locus de contexto:** os Planos de Gerenciamento detêm as Notas de Contexto (NC-00 a NC-06, NC-C1 a NC-C4, NC-Q1 a NC-Q5) que registram a leitura operacional vigente do TAP congelado. Divergências **jamais** são tratadas como correções do TAP.

**Trade-off declarado:** aceita-se divergência textual entre o termo autorizativo imutável e a leitura operacional, em favor da imutabilidade da referência de autorização e da trilha auditável de interpretações.

---

## 3. CORREÇÕES CRÍTICAS APLICADAS (v3.0 → v3.1)

| Item | v3.0 (Anterior) | v3.1 (Corrigido) | Domínio PMBOK 7ª |
|---|---|---|---|
| Contagem EAP | Ambiguidade (13/48 vs 12/37) | **12 fases + 37 pacotes** canônicos (TAP §4); Glossário tratado como volátil | Planejamento |
| Stack SDD | "QwenStudio" (genérico) | **llama.cpp + Qwen 32B + OpenCode** (stack local canônica) | Trabalho do Projeto |
| Regime do TAP | Não declarado | **Freeze formal** desde 18/09/2026; NC-00 como mecanismo | Abordagem de Desenvolvimento |
| Cycle Time | "To Do → Done" (coluna inexistente) | **"In Progress → Done"** (ADR-003 canônica) | Medição |
| Grafia stakeholder | "Carletto" / "Carleto" inconsistente | **"Prof. Dr. Nivaldo Carleto"** (TAP v3 canônico) | Stakeholders |
| ADR-005 | Não emitida | **Encaminhada** para emissão antes do M2 (regime de freeze) | Incerteza |
| Fronteira M1 | Ambiguidade 5 vs 8 planos | **5 planos no M1** (Áreas 1–5); 3 diferidos para M2 | Abordagem de Desenvolvimento |
| Tasklists | ADR-004 emitida, DoD não atualizado | **DoD item 8** incorpora tasklist (Plano de Escopo §2.6) | Trabalho do Projeto |
| Sistema de tags | 23 labels | **27 labels em 5 categorias** (inclusão P0–P3) | Trabalho do Projeto |

---

## 4. ESTRUTURA DO OKB v3.1 — ARTEFATOS OBRIGATÓRIOS

### 4.1 Status dos Artefatos no Marco M1 (22/09/2026)

| Artefato | Fase EAP | Status | Localização Canônica |
|---|---|---|---|
| TAP v3 | N1.2 | ✅ Aprovado (18/09/2026, freeze) | `/docs/tap/TAP.docx` |
| EAP (12 fases + 37 pacotes) | N1.2 | ✅ Canônica | TAP §4 + Plano de Escopo §2.5 |
| Plano de Integração v2.0 | N1.2 | ✅ Submetido M1 | `/docs/planos/plano-integracao.md` |
| Plano de Escopo v1.1 | N1.2 | ✅ Submetido M1 | `/docs/planos/plano-escopo.md` |
| Plano de Cronograma v1.2 | N1.2 | ✅ Submetido M1 | `/docs/planos/plano-cronograma.md` |
| Plano de Custos v1.2 | N1.2 | ✅ Submetido M1 | `/docs/planos/plano-custos.md` |
| Plano de Qualidade v1.1 | N1.3 | ✅ Submetido M1 | `/docs/planos/plano-qualidade.md` |
| Plano de Recursos | N1.2 | ⏳ Até M2 (30/09) | `/docs/planos/plano-recursos.md` |
| Plano de Comunicações | N1.2 | ⏳ Até M2 (30/09) | `/docs/planos/plano-comunicacoes.md` |
| Plano de Riscos | N1.2 | ⏳ Até M2 (30/09) | `/docs/planos/plano-riscos.md` |
| ADR-001 (Stack) | N9.1 | ✅ Emitida | `/docs/decisoes/ADR-001-stack.md` |
| ADR-002 (Kanban) | N9.1 | ✅ Emitida | `/docs/decisoes/ADR-002-kanban.md` |
| ADR-003 (Métricas) | N9.1 | ✅ Emitida | `/docs/decisoes/ADR-003-metricas.md` |
| ADR-004 (Tasklists) | N9.1 | ✅ Emitida (20/09) | `/docs/decisoes/ADR-004-tasklists.md` |
| ADR-005 (Freeze) | N9.1 | ⏳ Antes do M2 | `/docs/decisoes/ADR-005-freeze.md` |
| OKB v3.1 | N9.1 | ✅ Emitido (22/09) | `/docs/conhecimento/OKB.md` |
| Glossário v3.1 | N9.1 | 🔄 Saneamento pendente | `/docs/conhecimento/glossario.md` |
| Catálogo de Prompts SDD | N9.3 | ⏳ Até 03/10 | `/.ai/handoffs/` |
| Baseline de Métricas | — | ⏳ Pós-calibração (03/10) | `/docs/metricas/baseline.md` |
| Lições Aprendidas MF1 | N9.2 | ⏳ Até 30/09 | `/docs/conhecimento/licoes-aprendidas/MF1-licoes.md` |
| Redação M1 Consolidada v0.2 | — | ✅ Submetida M1 | Artefato de submissão |

### 4.2 Premissas Vigentes (TAP §9)

| ID | Premissa | Status |
|---|---|---|
| P1 | Governança híbrida (PMBOK 7ª + 6ª dicionário + Kanban) | ✅ Vigente |
| P2 | FOSS absoluto | ✅ Vigente |
| P3 | SDD com IA auditável (stack local canônica) | ✅ Vigente |
| P4 | Código-fonte é deliverable formal | ✅ Vigente |
| P5 | 20h/semana por membro | ✅ Vigente |
| P6 | Hardware adequado e suficiente | ✅ Vigente |
| P7 | GP = CCB único; Prof. Dr. Nivaldo Carleto = avaliador de marcos | ✅ Vigente |
| P8 | Aquisições e Partes Interessadas simplificadas | ✅ Vigente |
| P9 | Separação ontológica TAP ≠ EAP ≠ PDCA | ✅ Vigente |

### 4.3 Restrições Vigentes (TAP §8 + §11)

- Escopo restrito ao MVP acadêmico
- Prazo letivo inegociável (M1: 22/09/2026; M2: 30/09/2026; M3: 15/11/2026; M4: 15/12/2026)
- Orçamento zero (proibição de aquisições pagas)
- Equipe de 3 pessoas (múltiplos papéis)
- Stack 100% FOSS (OSI-approved)
- Licenciamento final open source (MIT/GPL)

---

## 5. ADRs EMITIDAS

### ADR-001: Stack Tecnológica FOSS
**Status:** Aprovada | **Data:** 19/09/2026 | **Decisor:** GP Leonardo (CCB)
**Rastreabilidade:** TAP §3 (Inovação) + §8 (FOSS) + EAP N4.1, N5.1–N5.4

| Camada | Tecnologia | Licença | Justificativa |
|---|---|---|---|
| Backend | Python 3.11 + FastAPI | PSF / MIT | Assíncrono nativo, ecossistema maduro |
| Banco | SQLite | Public Domain | Zero-config, ACID, adequado ao MVP |
| Geração PDF | WeasyPrint | BSD-3-Clause | HTML/CSS → PDF, FOSS |
| Testes | pytest + coverage.py | MIT | Padrão Python, integração CI |
| CI/CD | GitHub Actions (Free Tier) | Proprietário gratuito | Nativo ao SSOT |
| Frontend | HTML5 + CSS3 + HTMX + Tailwind | — | KISS, interatividade sem JS pesado |
| LLM (SDD) | llama.cpp + Qwen 32B Instruct + OpenCode | MIT / Autorizada | Stack local canônica, zero custo |
| Cache | SQLite (mesmo banco) | Public Domain | Simplicidade > Redis para MVP |

**Fallback:** Se FastAPI apresentar curva excessiva → Flask (MIT). Se Qwen 32B exceder RAM → Qwen 14B (P1).

### ADR-002: Kanban como Método de Execução
**Status:** Aprovada | **Data:** 19/09/2026 | **Decisor:** GP Leonardo (CCB)
**Rastreabilidade:** TAP §1.c + §3 (Métricas) + EAP N1.5, N7

- **Ferramenta:** GitHub Projects (SSOT)
- **Colunas:** `Backlog` → `Ready (DoR)` → `In Progress` → `Code Review` → `Done (DoD)`
- **WIP Limits:** 3 cards em `In Progress` por pessoa (Domínio de Equipe PMBOK 7ª)
- **Pull system:** trabalho puxado por capacidade
- **Rituais:** Daily assíncrona (15min), Refinement semanal (30min), Retrospectiva quinzenal (30min)
- **Sprints:** NÃO utilizadas — fluxo contínuo

### ADR-003: Métricas de Fluxo (Substituição de EVM)
**Status:** Aprovada | **Data:** 19/09/2026 | **Decisor:** GP Leonardo (CCB)
**Rastreabilidade:** TAP §3 (Métricas) + Domínio de Medição PMBOK 7ª

**Métricas oficiais (exclusivas):**

| Métrica | Fórmula | Meta (pós-calibração) | Frequência |
|---|---|---|---|
| Cycle Time | Média (Done − In Progress) | ≤ 3 dias | Semanal |
| Throughput | Cards concluídos / semana | ≥ 5 cards | Semanal |
| CFD | Visualização de gargalos | Sem bandas largas | Semanal |
| WIP em fluxo | Cards em In Progress | ≤ 9 (3 × 3 pessoas) | Contínuo |
| Coverage | Linhas testadas / totais | ≥ 80% | Por push (CI) |
| Burnout | Carga horária semanal | ≤ 20h/pessoa | Semanal |

**Métricas LEGADO (NÃO APLICÁVEIS):** ❌ SPI | ❌ CPI | ❌ EVM

**Período de Calibração:** 23/09/2026 a 03/10/2026 — coleta sem meta fixa para estabelecer baseline empírica.

### ADR-004: Tasklists Markdown (Rejeição de Subissues)
**Status:** Aprovada | **Data:** 20/09/2026 | **Decisor:** GP Leonardo (CCB)
**Rastreabilidade:** TAP §1.c + REQ-12 + ADR-002 + ADR-003

**Decisão:** Tasklists Markdown nativas (`- [ ]` / `- [x]`) no corpo da Issue; **subissues reais formalmente rejeitadas**.

**Regras:**
- Obrigatórias para cards com estimativa ≥ 6h ou múltiplos entregáveis
- Formato canônico: mínimo 3, máximo 7 itens; último item obrigatoriamente "Validação final"
- Natureza binária: feito/não feito
- Card só migra para `Code Review` com 100% dos itens concluídos (DoD item 8)

**Impacto nas métricas:** Cycle Time, Throughput e CFD medem **exclusivamente o card pai**.

### ADR-005: Regime de Freeze do TAP (ENCAMINHADA)
**Status:** ⏳ A emitir antes do M2 | **Decisor:** GP Leonardo (CCB)
**Rastreabilidade:** NC-00 (Cronograma §3.8) + Premissa P9
**Objeto:** Formalizar o regime de freeze do TAP, a precedência intra-TAP da seção §6 Marcos, e o mecanismo de Notas de Contexto como locus de leitura operacional.

---

## 6. POLÍTICA DE ADRs E INTEGRAÇÃO DOCUMENTAL

### 6.1 Gatilhos para Criação de ADRs (Teste de 4 Perguntas)

Uma decisão exige ADR se atender a **pelo menos 2 dos 4 critérios**:

| # | Critério | Exemplo no COGME | Domínio PMBOK 7ª |
|---|---|---|---|
| G1 | Impacto transversal: afeta ≥ 2 fases da EAP ou ≥ 2 planos | ADR-003 (métricas) impacta Cronograma + Integração + Qualidade | Planejamento + Medição |
| G2 | Irreversibilidade prática: reverter custaria > 8h | ADR-001 (stack) — trocar FastAPI reescreve backend | Abordagem de Desenvolvimento |
| G3 | Questionabilidade acadêmica: Prof. Dr. Nivaldo Carleto poderia questionar | ADR-004 (tasklists vs subissues) | Stakeholders |
| G4 | Trade-off não óbvio: abre mão de alternativa viável | ADR-002 (Kanban sem sprints) | Abordagem de Desenvolvimento |

**Regra GMV:** 1 critério → commit com prefixo `decision:`. 0 critérios → não registra.

### 6.2 Gatilhos Negativos (Quando NÃO Criar ADR)

| Situação | Ação Correta |
|---|---|
| Decisão de formatação de código (lint, indentação) | `.editorconfig` + commit |
| Escolha de nome de variável/função | Commit message |
| Ajuste de texto em plano (sem mudança de escopo) | `docs(plano-X): ajuste §Y` |
| Decisão já coberta por ADR existente | Referência à ADR no commit |
| Decisão operacional do dia a dia | Daily assíncrona |

### 6.3 Política de ADR Tardia

| Condição | Ação | Prazo |
|---|---|---|
| Implementada há ≤ 48h, ≥ 2 gatilhos | ADR tardia com nota de regularização | ≤ 24h |
| Implementada há > 48h, ≥ 2 gatilhos | ADR tardia + lição aprendida | ≤ 72h |
| Implementada, apenas 1 gatilho | NÃO emitir ADR; commit `decision:` | Imediato |
| Implementada, 0 gatilhos | Não registrar | — |

**Estrutura obrigatória da ADR tardia:** Tipo (Regularização tardia), Data da decisão efetiva, Data da formalização, Motivo da tardança, Lição aprendida.

### 6.4 Limite de ADRs por Marco (GMV)

| Marco | Máximo de ADRs novas | Justificativa |
|---|---|---|
| M1 (22/09) | 4 (001–004 emitidas) | Fundação completa |
| M2 (30/09) | ≤ 2 | Baseline + eventual ajuste de stack |
| M3 (15/11) | ≤ 3 | Padrão de API, estratégia de teste, fallback |
| M4 (15/12) | ≤ 1 | Licenciamento final |

**Total projetado:** ≤ 10 ADRs ao longo do ciclo de vida.

### 6.5 Arquitetura de Integração Documental

**Princípio diretor:** Documentos de governança são *standalone*; planos de área são coordenados; **cross-references substituem duplicação**.

```
/docs/
 ├── planos/                    ← 8 planos de área (M1: 5 | M2: 3)
 ├── decisoes/                  ← ADRs 001–005
 ├── conhecimento/              ← OKB, Glossário, lições aprendidas
 ├── metricas/                  ← baseline (pós 03/10)
 ├── requisitos/                ← REQ-01 a REQ-15
 ├── diagramas/                 ← SVGs canônicos por área
 ├── dependencias/              ← registro.md (auditoria FOSS)
 ├── tap/                       ← TAP.md + TAP.docx
 └── archive/                   ← drafts, legados, deprecados
```

**Anti-padrões proibidos:**
- ❌ Copiar texto integral de ADR dentro de plano
- ❌ Criar "Anexos" com documentos externos no final de cada plano
- ❌ Embutir Glossário como seção do Plano de Integração
- ❌ Criar "Super-Documento" com TAP + planos + ADRs

**Padrão canônico de cross-reference:**
```
Conforme [ADR-003 — Métricas de Fluxo](/docs/decisoes/ADR-003-metricas.md),
as métricas EVM são declaradas LEGADO.
```

---

## 7. CONFIGURAÇÃO OPERACIONAL DO GITHUB (SSOT)

### 7.1 Sistema de Tags — 27 Labels em 5 Categorias

**Categoria 1 — Tipo de Trabalho (6):** `feat` `bug` `docs` `test` `ci` `chore`
**Categoria 2 — Macro-Fase EAP (3):** `MF1-fundacao` `MF2-construcao` `MF3-consolidacao`
**Categoria 3 — Área de Conhecimento (8):** `area:integracao` `area:escopo` `area:cronograma` `area:custos` `area:qualidade` `area:recursos` `area:comunicacoes` `area:riscos`
**Categoria 4 — Status Operacional (4):** `change-request` `risk` `blocked` `sdd-ia`
**Categoria 5 — Prioridade (6):** `must` `should` `P0` `P1` `P2` `P3`

**Regras:**
- Todo card: mínimo 3 tags (1 tipo + 1 macro-fase + 1 área)
- Cards `sdd-ia` exigem co-autoria no commit (DoD)
- Cards `change-request` não migram para `In Progress` até aprovação do GP
- Cards `blocked` devem registrar dependência no corpo da Issue

### 7.2 Milestones — 5 Milestones

| # | Milestone | Due Date | Abertura | Tipo |
|---|---|---|---|---|
| 1 | M1 — Entrega Parcial Documental | 22/09/2026 | 01/09/2026 | Marco oficial |
| 2 | M2 — Ambiente e Modelagem | 30/09/2026 | 23/09/2026 | Marco oficial |
| 3 | Calibração — Baseline de Métricas | 03/10/2026 | 23/09/2026 | Auxiliar |
| 4 | M3 — MVP Funcional (Beta) | 15/11/2026 | 04/10/2026 | Marco oficial |
| 5 | M4 — Encerramento e Validação | 15/12/2026 | 16/11/2026 | Marco oficial |

**Regras:**
- Cada Issue vinculada a exatamente 1 milestone
- Milestone não fecha com Issues `blocked` ou `change-request` abertas
- Alteração de data exige `change-request` + CCB + ADR (se marco oficial)

### 7.3 Padrão de Redação de Cards Ubíquos

**Padrão A — Card Documental** (`docs`, `ci`, `chore`):
Título `N{X}.{Y} — Descrição` | Contexto ubíquo | Entrega | Critérios binários | Rastreabilidade | Dependências | Atribuição | Estado

**Padrão B — User Story (GWT)** (`feat`, `bug`, `test`) — aplicação efetiva a partir do M2:
Título `N{X}.{Y} — US-{NN}: Descrição` | User Story | Contexto | Critérios GWT (Dado/Quando/Então) | Regras de Negócio | Rastreabilidade | Dependências | Atribuição | Estado

### 7.4 Sistema de Prioridade P0–P3

| Peso | Definição | Ação no Kanban |
|---|---|---|
| **P0** | Crítico / Caminho crítico — sem ele, marco não é atingido | Execução imediata; WIP reservado |
| **P1** | Alto — essencial ao marco | Execução na janela do marco |
| **P2** | Médio — pode deslizar para marco seguinte | Execução pós-marco atual |
| **P3** | Baixo — postergável sem impacto | Puxar apenas se capacidade sobrar |

---

## 8. BACKLOG DO MARCO M1 — STATUS REAL (22/09/2026)

### 8.1 Resumo dos 21 Cards

| # | Card | Tipo | Prioridade | Status (22/09) |
|---|---|---|---|---|
| M1-01 | Plano de Integração | docs | P0 must | ✅ Submetido |
| M1-02 | Plano de Escopo | docs | P0 must | ✅ Submetido |
| M1-03 | Plano de Cronograma | docs | P0 must | ✅ Submetido |
| M1-04 | Plano de Custos | docs | P0 must | ✅ Submetido |
| M1-05 | Plano Qualidade + PDCAs + Ishikawa | docs | P0 must | ✅ Submetido |
| M1-06 | Requisitos Funcionais | docs | P1 must | ✅ Consolidado no TAP §5 |
| M1-07 | Requisitos Não Funcionais | docs | P1 must | ✅ Consolidado no TAP §5 |
| M1-08 | Arquitetura da Solução | docs | P2 must | ⏳ M2 |
| M1-09 | Protótipo UX/UI | docs | P3 should | ⏳ M2 |
| M1-10 | Modelagem de Dados (DER) | docs | P2 must | ⏳ M2 |
| M1-11 | Seleção Stack FOSS (ADR-001) | docs | P1 must | ✅ ADR-001 emitida |
| M1-12 | Repositório Git + CI/CD | ci | P0 must | ✅ Configurado |
| M1-13 | Setup Local e Homologação | chore | P1 must | ✅ Concluído |
| M1-14 | Auditoria de Licenças FOSS | docs | P2 must | ⏳ M2 |
| M1-15 | ADR-001 Stack | docs | P1 must | ✅ Emitida |
| M1-16 | ADR-002 Kanban | docs | P1 must | ✅ Emitida |
| M1-17 | ADR-003 Métricas | docs | P1 must | ✅ Emitida |
| M1-18 | Lições Aprendidas MF1 | docs | P3 should | ⏳ 30/09 |
| M1-19 | Matriz RACI | docs | P2 should | ⏳ M2 (Plano Comunicações) |
| M1-20 | Canais Oficiais | docs | P2 should | ⏳ M2 (Plano Comunicações) |
| M1-21 | Labels + change-request | chore | P1 must | ✅ 27 labels configuradas |

**Totais:** 21 cards · 15 `must` · 6 `should` · 6 P0 · 8 P1 · 5 P2 · 2 P3

### 8.2 Distribuição de Carga Real

| Membro | Carga Estimada | Limite P5 | Status |
|---|---|---|---|
| Leonardo | ~14h | 20h/semana | ✅ Dentro do limite |
| Fabricio | ~13h | 20h/semana | ✅ Dentro do limite |
| Edson | ~11h | 20h/semana | ✅ Dentro do limite |

---

## 9. LITERATURA DE APOIO — QUESTÕES ADJACENTES

### 9.1 Área de Conhecimento para Rede de Projeto e Caminho Crítico

| Edição | Resposta |
|---|---|
| PMBOK 6ª (Dicionário) | Gerenciamento do Cronograma — Processos 6.4 (Sequenciar) e 6.6 (Desenvolver) |
| PMBOK 7ª (Governança) | Domínio de Planejamento + Domínio de Medição |

**Aplicação no COGME:** CPM/Gantt declarados LEGADO (ADR-003). Caminho crítico identificado empiricamente via CFD, Cycle Time, cards P0 e label `blocked`.

### 9.2 Estruturação do CFD para Demonstração Formal

O CFD aparece em três artefatos com funções distintas:
- **Integração §1.6.1:** definição formal + cadência
- **Cronograma §3.7:** substituto do Gantt/EVM
- **Comunicações §3.2 (M2):** evidência visual de progresso

**Definição canônica:** visualização gráfica do fluxo acumulado no tempo, com bandas horizontais representando colunas Kanban.

**Ação corretiva:** banda com largura > 2× a média das demais por 2 semanas consecutivas → Retrospectiva extraordinária (ADR-002).

### 9.3 Separação Ontológica (TAP ≠ EAP ≠ PDCA)

| Artefato | Natureza | Integra EAP? | Tem PDCA? |
|---|---|---|---|
| TAP | Autorização + base de referência | ❌ NÃO | ❌ NÃO |
| Planos de Gerenciamento (01–08) | Execução do escopo autorizado | ✅ SIM | ✅ SIM |
| Código-fonte (MVP) | Produto final | ✅ SIM | ✅ SIM |

**Fundamento:** O TAP AUTORIZA o projeto e antecede o planejamento. Não é objeto de gerenciamento (PMBOK 6ª §4.1 / PMBOK 7ª Domínio de Integração).

---

## 10. REGISTRO DE INCIDENTES

### LA-001: Incidente de Reestruturação Paralela
**Data:** 22/09/2026 | **Macro-Fase:** MF1 | **Domínio PMBOK 7ª:** Trabalho do Projeto + Entrega
**Localização canônica:** `/docs/conhecimento/licoes-aprendidas/MF1-licoes.md`

**O que aconteceu:** Reestruturação formal do repositório executada em paralelo com produção ativa de diagramas e textos. Alguns artefatos recentes foram perdidos ou deslocados.

**Causa raiz:**
- Ausência de branch dedicada para reestruturação (operação em `main` direta)
- Uso de `mv` do sistema em vez de `git mv` (perda de rastreabilidade de rename)
- Execução de `git add -A` sem verificação prévia da árvore de destino
- Produção ativa de artefatos durante a janela de reestruturação

**Impacto:** Perda de 1–2 diagramas recentes; deslocamento temporário de diagramas canônicos para archive; retrabalho estimado em 2–3h.

**Ações preventivas (regras permanentes):**
1. Reestruturações SEMPRE em branch dedicada (`chore/restructure-*`)
2. Usar `git mv` em vez de `mv` para qualquer movimentação versionada
3. Congelar produção durante reestruturação (janela de manutenção)
4. Verificar `tree` da estrutura de destino ANTES de `git add -A`
5. Commit único de reestruturação com mensagem descritiva + tag de rollback

---

## 11. NOTAS DE CONTEXTO E SANEAMENTO DE ARTEFATOS VIVOS

### 11.1 Notas de Contexto Consolidadas (Transversais)

| NC | Matéria | Entendimento Adotado |
|---|---|---|
| NC-00 | Regime de freeze + precedência intra-TAP | TAP congelado; §6 Marcos canônico para matéria temporal |
| NC-01 | SMART Cronograma × §6 | §6 prevalece: MVP funcional no M3, consolidação no M4 |
| NC-02 | Numeração de processos | Canônica PMBOK 6ª (6.1–6.6, 7.1–7.4, 8.1–8.3) |
| NC-03 | Convenção dupla de dias | Fluxo em dias corridos; marcos/capacidade em dias úteis |
| NC-04 | Critério M2 (stack) | "Definida e validada por protótipo" (ADR-001 em avaliação) |
| NC-05 | Base temporal do gatilho P0 | 48h em horas corridas (evento de fluxo) |
| NC-06 | Verificação de capacidade M1 | Todos os membros dentro do limite de 20h/semana |
| NC-C1 a NC-C4 | Custos | Inaplicabilidade 7.2–7.4; delimitação com Qualidade |
| NC-Q1 a NC-Q5 | Qualidade | Freeze; EAP 12 fases; grafia Carleto |

### 11.2 Registro de Saneamento — Artefatos Vivos (não bloqueante)

| Pendência | Artefato Vivo | Momento Previsto |
|---|---|---|
| Numeração 6.3/6.5 no §8.1 | OKB §8.1 | Próxima revisão |
| "Processo 6.4 Estimar Custos" → 7.2 | Glossário §3 | Próxima revisão |
| Grafia "Carletto" → "Carleto" | Glossário | Próxima revisão |
| Cycle Time "To Do → Done" → "In Progress → Done" | Glossário | Próxima revisão |
| Contagem EAP "13/48" → 12/37 | Glossário §1 | Próxima revisão |
| Convenção dupla de dias | ADR-003 / Glossário / baseline | Após 03/10 |
| Cláusula NC-00 + ADR-005 | Integração §1.4 / ADR-005 | Antes do M2 |
| Micro-ajuste Integração §1.3.2 | Integração | Aguardando GP |

---

## 12. PRÓXIMOS PASSOS (PÓS-M1: 23/09 – 30/09/2026)

### 12.1 Prioridades da Semana (23–27/09)

| Prioridade | Ação | DoD |
|---|---|---|
| 🔴 P0 | Submeter M1 ao Prof. Dr. Nivaldo Carleto | Validação sem achados críticos |
| 🔴 P0 | Emitir ADR-005 (regime de freeze) | ADR registrada em `/docs/decisoes/` |
| 🟠 P1 | Iniciar período de calibração de métricas | Baseline coletada até 03/10 |
| 🟠 P1 | Saneamento do Glossário v3.2 | Contagem, grafias, Cycle Time corrigidos |
| 🟡 P2 | Redigir Plano de Recursos (Área 6) | v0.1 até 30/09 |
| 🟡 P2 | Redigir Plano de Comunicações (Área 7) | v0.1 até 30/09 |
| 🟡 P2 | Redigir Plano de Riscos (Área 8) | v0.1 até 30/09 |
| 🟢 P3 | Gerar SVGs pendentes (Ishikawa, Roadmap, Fluxo Qualidade) | 4 SVGs incorporados |

### 12.2 Marco de Fechamento de Setembro (30/09/2026 — M2)

**Entrega:** MF1 (Fundação) 100% concluída.

**Critérios de aceite:**
- ✅ TAP v3 aprovado (freeze)
- ✅ 5 planos (Áreas 1–5) submetidos no M1
- ✅ 3 planos (Áreas 6–8) submetidos no M2
- ✅ EAP sincronizada (12 fases + 37 pacotes)
- ✅ Stack FOSS definida e validada por protótipo
- ✅ Ambiente local + CI configurados
- ✅ DER e Protótipo UX/UI versionados
- ✅ ADR-005 emitida
- ✅ Pipeline CI "verde"
- ✅ Baseline de métricas em coleta (até 03/10)

---

## 13. CONDIÇÕES DE VALIDADE E GATILHOS

**Válido enquanto:**
- Ementa da disciplina mantiver PMBOK como base
- Prof. Dr. Nivaldo Carleto mantiver papel de stakeholder-avaliador único
- Equipe mantiver 3 pessoas com ≤ 20h/semana cada
- Prazo final mantiver em 15/12/2026
- TAP permanecer em regime de freeze

**Invalida se:**
- Professor exigir PMBOK 6ª como base exclusiva (regressão de governança)
- Ementa migrar para framework ágil puro sem PMBOK
- Código deixar de ser deliverable formal
- Equipe expandir para > 3 pessoas ou reduzir para < 2
- Prazo final antecipar para antes de Nov/2026

**Gatilhos de reavaliação:**
- Novo artefato solicitado fora da árvore (seções 00–11)
- Mudança no critério de avaliação da disciplina
- Scope creep > 15% do backlog original
- Orientação verbal do Prof. Dr. Nivaldo Carleto divergente deste guardrail
- Falha crítica na API de câmbio externa
- Burnout detectado (> 20h/semana por 2 semanas consecutivas)
- Throughput < 3 cards/semana por 2 semanas consecutivas

---

## 14. INSTRUÇÃO DE USO DESTE GUARDRAIL v3.1

| Situação | Consulte |
|---|---|
| Durante redação de artefatos | Seções 4, 6, 7 |
| Durante revisão de artefatos | Seção 6.1 (gatilhos de ADR) |
| Durante conflito entre fontes | Seção 2.1 (hierarquia) + 2.5 (freeze) |
| Durante dúvida sobre escopo | EAP canônica (TAP §4) + Plano de Escopo §2.5 |
| Durante decisão técnica | Seção 6.1 (matriz de gatilhos) |
| Durante dúvida sobre burocracia | Teste GMV (Seção 6.1) |
| Durante planejamento semanal | Seção 12 (próximos passos) |
| Durante gestão do trabalho | Kanban no GitHub Projects (SSOT) |
| Durante conflito de governança | Macro-fases (TAP §6) + NC-00 |
| Durante análise de métricas | ADR-003 + Seção 9.2 (CFD) |

---

## 15. VERIFICAÇÃO DE CONGRUÊNCIA

| Item | Status |
|---|---|
| OKB v3.1 substitui formalmente OKB v3.0 | ✅ OK |
| Contagem EAP canônica (12/37) fixada | ✅ OK |
| Stack SDD local canônica nomeada | ✅ OK |
| Regime de freeze do TAP declarado | ✅ OK |
| ADR-004 incorporada + DoD item 8 | ✅ OK |
| Sistema de 27 labels formalizado | ✅ OK |
| 5 milestones configuradas | ✅ OK |
| Padrões A/B de cards definidos | ✅ OK |
| Política de ADRs incorporada (aditivo) | ✅ OK |
| Backlog M1 com status real (22/09) | ✅ OK |
| Incidente LA-001 registrado | ✅ OK |
| Saneamento de pendências externas mapeado | ✅ OK |
| Prof. Dr. Nivaldo Carleto sempre por extenso | ✅ OK |
| EVM declarado LEGADO — NÃO APLICÁVEL | ✅ OK |
| Obsolescência PMBOK 6ª declarada | ✅ OK |
| Rastreabilidade TAP → OKB → ADRs preservada | ✅ OK |
| Princípio GMV respeitado em todas as seções | ✅ OK |
| Separação ontológica TAP ≠ EAP ≠ PDCA | ✅ OK |

---

**OKB v3.1 emitido por:** GP Leonardo David Silva Setti
**Aprovação:** CCB (GP — membro único, TAP v3 §1.c)
**Data:** 22/09/2026
**Status:** ✅ Convergente à Redação M1 v0.2 + TAP v3 (freeze) + ADRs 001–004 — pronto para transição M2
**Substitui:** OKB v3.0 (20/09/2026)
**Próxima revisão:** 30/09/2026 (fechamento da MF1 — Fundação / M2)

*Fim do documento — OKB v3.1 | COGME | Fatec Taquaritinga | 22/09/2026*


-----

# HISTÓRICO


# RELATÓRIO ANALÍTICO — BASE DE CONHECIMENTO COMPLEMENTAR v3.0 (GUARDRAIL EVOLUÍDO)

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Data de Emissão:** 09/09/2026
**Versão anterior:** OKB_COGME_v2.1 (07/09/2026)
**Emissor:** GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)
**Stakeholder:** Prof. Dr. Nivaldo Carleto

---

## 1. VEREDITO SUMÁRIO

A base de conhecimento operacional do COGME (OKB v2.1) atingiu maturidade estrutural suficiente para sustentar a fase de consolidação documental e transição para execução de código. As críticas das rodadas anteriores foram devidamente absorvidas e refutadas pelo aluno, resultando em um modelo híbrido coerente: **PMBOK 7ª como governança primária, Kanban/GitHub Projects como execução, PMBOK 6ª como dicionário complementar, e código MVP como marco de sucesso**.

Esta nova rodada não revisita debates encerrados (hibridização, exclusão de Partes Interessadas, uso de LLM, escopo do código). O foco agora é **identificar lacunas operacionais remanescentes** que ameaçam a execução nos próximos 60 dias úteis até a entrega final (Nov/Dez 2026).

---

## 2. NOVA RODADA DE CRÍTICAS (LACUNAS REMANESCENTES)

### Crítica 1 — Sobrecarga de Governança para Equipe de 2 Pessoas (Severidade: ALTA)

**Problema:** O OKB v2.1 prescreve 14 seções de governança, 7 princípios constitutivos, 8 domínios de desempenho com metas mensuráveis, 13 fases obrigatórias na EAP, 4 dimensões de qualidade simultâneas (PMBOK 7ª + Ágil + SDD + PDCA), e 7 critérios de revisão por artefato. Para uma equipe de 2 pessoas com carga máxima de 20h/semana cada (Princípio de Equipe do PMBOK 7ª), isso representa **~40h/semana de governança pura**, antes de qualquer linha de código.

**Evidência:** O plano de ação imediato (status report 07/09) já comprimiu 5 ações críticas em 4 dias úteis. Isso é insustentável por mais de 2 semanas consecutivas sem comprometer a qualidade ou a saúde da equipe.

**Recomendação:** Introduzir **princípio de governança mínima viável (GMV)**: cada artefato de governança deve justificar sua existência com a pergunta *"Se eu remover este artefato, o Prof. Nivaldo perceberá e penalizará?"*. Se a resposta for não, o artefato é candidato a simplificação ou eliminação.

### Crítica 2 — EAP com 13 Fases Obrigatórias é Ambiciosa para o Prazo (Severidade: MÉDIA-ALTA)

**Problema:** 13 fases obrigatórias em ~12 semanas úteis (setembro a dezembro) com 2 pessoas = menos de 1 semana por fase em média. Algumas fases (ex: 5. Desenvolvimento do Sistema com 6 subfases, 6. Garantia da Qualidade com 3 subfases) demandam sozinhas 3-4 semanas.

**Evidência:** A Fase 5 (Desenvolvimento) contém Backend, API de Câmbio, Frontend, Módulo PDF, SDD com IA e Execução Kanban — isso é um projeto inteiro, não uma fase.

**Recomendação:** Reorganizar a EAP em **3 macro-fases temporais** (Fundação → Construção → Consolidação) com as 13 fases como pacotes de trabalho distribuídos, não como etapas sequenciais. O Kanban já permite paralelismo; a EAP deve refletir isso.

### Crítica 3 — Stack Tecnológica FOSS Indefinida (Severidade: ALTA)

**Problema:** O OKB v2.1 menciona "stack FOSS" e "MVP full-stack" mas **não especifica linguagens, frameworks ou banco de dados**. A Fase 4 (Configuração de Ambiente) tem subfase 4.1 "Seleção e Validação da Stack FOSS", mas sem decisão tomada, não é possível estimar custos, cronograma ou recursos com precisão.

**Evidência:** O glossário menciona Redis (cache), WeasyPrint (PDF), mas omite linguagem principal (Python? JavaScript? Go?), framework web (Django? FastAPI? Next.js?), e banco de dados relacional (PostgreSQL? SQLite?).

**Recomendação:** Criar **ADR-002: Seleção da Stack Tecnológica FOSS** como ação bloqueante antes do início da Fase 5. A decisão deve considerar: (a) curva de aprendizado da equipe, (b) compatibilidade com WeasyPrint e Redis, (c) suporte a testes automatizados (meta ≥ 80% coverage), (d) deploy em ambiente gratuito (Railway? Render? Fly.io?).

### Crítica 4 — Métricas de Fluxo sem Baseline (Severidade: MÉDIA)

**Problema:** As metas de Cycle Time ≤ 3 dias e Throughput ≥ 5 cards/semana são **arbitrárias** — não há histórico de desempenho da equipe para calibrá-las. O Domínio de Medição do PMBOK 7ª exige que métricas sejam "significativas e acionáveis", não aspiracionais.

**Recomendação:** Estabelecer **período de calibração de 2 semanas** (15-29/09/2026) onde as métricas são coletadas sem meta fixa. Após calibração, definir metas realistas baseadas na média observada ± 20%. Registrar no ADR-003.

### Crítica 5 — ADR como Burocracia Potencial (Severidade: BAIXA-MÉDIA)

**Problema:** A regra "toda decisão técnica relevante deve ter ADR" é vaga. O que é "relevante"? Escolher nome de variável? Escolher biblioteca de testes? Sem critério claro, a equipe gastará tempo documentando trivialidades ou omitindo decisões críticas.

**Recomendação:** Definir **critério de obrigatoriedade de ADR**: (a) decisão que afeta ≥ 2 fases da EAP, (b) decisão que envolve troca de tecnologia, (c) decisão que o Prof. Nivaldo questionaria em apresentação. Decisões menores ficam registradas apenas em commit messages convencionais (Conventional Commits).

### Crítica 6 — Gap Temporal no Plano de Ação (Severidade: MÉDIA)

**Problema:** O status report de 07/09 definiu plano até 11/09. Hoje é 09/09 — estamos no dia 3 de 5. Não há plano de ação para a semana seguinte (14-18/09), que é quando a Fase 4 (Configuração de Ambiente) deveria iniciar.

**Recomendação:** Este relatório deve incluir **plano de ação estendido até 30/09/2026** (fim do período de calibração), cobrindo a transição da consolidação documental para a execução de código.

---

## 3. ANÁLISE DE RISCO ATUALIZADA (Setembro 2026)

### Riscos Ativos

| ID | Risco | Prob. | Impacto | Severidade | Resposta | Status |
|----|-------|-------|---------|------------|----------|--------|
| R-01 | Stack FOSS indefinida bloqueia Fase 5 | 80% | Alto | **Crítico** | ADR-002 até 15/09 | Aberto |
| R-02 | EAP não sincronizada com GitHub Projects | 60% | Alto | **Alto** | Mapeamento 1:1 até 11/09 | Em andamento |
| R-03 | Governança consome >50% do tempo da equipe | 70% | Médio | **Alto** | Aplicar GMV (governança mínima viável) | Aberto |
| R-04 | Professor exigir Gantt tradicional | 30% | Médio | **Médio** | ADR-001 + Gantt derivado do Kanban | Mitigado |
| R-05 | Scope creep nas fases de desenvolvimento | 50% | Alto | **Alto** | CCB (Prof. Nivaldo) + DoR rigoroso | Monitorando |
| R-06 | API de câmbio externa indisponível | 20% | Alto | **Médio** | Adapter pattern + fallback BCB | Pós-entrega |
| R-07 | Ambiente de deploy gratuito instável | 40% | Médio | **Médio** | Docker local como fallback | Monitorando |
| R-08 | Equipe exceder 20h/semana (burnout) | 50% | Médio | **Alto** | WIP limits + métrica de burnout | Monitorando |

### Riscos Encerrados

| ID | Risco | Motivo do Encerramento |
|----|-------|----------------------|
| R-00 | Hibridização PMBOK+Ágil incoerente | Refutado pelo aluno; modelo híbrido validado e documentado no OKB v2.1 |
| R-00b | Uso de LLM penalizado | Refutado; uso é irrestrito e autorizado pela disciplina |
| R-00c | Partes Interessadas como lacuna | Refutado; exclusão é premissa pedagógica conhecida |

---

## 4. BASE DE CONHECIMENTO COMPLEMENTAR EVOLUÍDA (GUARDRAIL v3.0)

### 4.1. Hierarquia de Resolução de Conflitos (Mantida do OKB v2.1 §2.1)

```
1º  Valor entregue ao usuário final (PMBOK 7ª — Domínio de Entrega)
2º  Ementa da disciplina + orientação do Prof. Nivaldo
3º  PMBOK 7ª (12 princípios + 8 domínios de desempenho)
4º  Manifesto Ágil + Kanban (método de execução)
5º  PMBOK 6ª (dicionário de processos quando necessário)
6º  Literatura técnica complementar
```

**Adendo v3.0:** Em caso de conflito entre velocidade de entrega e completude documental, **a entrega de valor prevalece**, desde que justificada via ADR e comunicada ao Prof. Nivaldo em até 48h (Domínio de Stakeholders PMBOK 7ª).

### 4.2. Princípio de Governança Mínima Viável (GMV) — NOVO

Todo artefato de governança deve passar pelo teste GMV antes de ser produzido:

| Pergunta | Se SIM | Se NÃO |
|----------|--------|--------|
| O Prof. Nivaldo exigirá este artefato na avaliação? | Produzir completo | Simplificar ou eliminar |
| Este artefato evita retrabalho futuro? | Produzir | Avaliar custo-benefício |
| Este artefato é exigido pelo PMBOK 7ª como evidência de domínio? | Produzir | Documentar em 1 parágrafo no TAP |
| Este artefato é útil para a equipe (não apenas para o professor)? | Produzir | Eliminar |

**Regra:** Se ≥ 2 respostas forem NÃO, o artefato é candidato a eliminação. Decisão final via CCB (Prof. Nivaldo).

### 4.3. Mapeamento PMBOK 7ª ↔ Kanban ↔ PMBOK 6ª (Refinado)

| Domínio PMBOK 7ª | Ritual Kanban (GitHub Projects) | Processo PMBOK 6ª | Artefato | Frequência |
|---|---|---|---|---|
| **Stakeholders** | Review assíncrono via Issues + link público do repo | 13.1, 13.2 | Matriz de comunicação simplificada | Quinzenal |
| **Equipe** | Daily assíncrona (Discussion) + WIP limits | 9.1, 9.2 | RACI simplificado (2 pessoas) | Diário |
| **Abordagem** | Kanban flow contínuo (sem sprints) | 4.1, 4.2 | TAP + ADR-001 | Único + evolutivo |
| **Planejamento** | Refinement semanal do backlog | 5.2, 5.3, 6.5 | Backlog + EAP + Roadmap | Semanal |
| **Trabalho** | Pull system + colunas Kanban | 4.3, 4.4 | Código-fonte + commits | Contínuo |
| **Entrega** | Deploy contínuo (CI/CD) | 5.4, 8.3 | MVP funcional + DoD | Incremental |
| **Medição** | GitHub Insights (Cycle Time, Throughput) | 4.5, 6.6 | Dashboard + métricas de fluxo | Semanal |
| **Incerteza** | Labels `risk`/`blocked` + Risk Backlog | 11.1, 11.2, 11.5 | Matriz Prob./Impacto | Quinzenal |

**Adendo v3.0:** O Domínio de Equipe agora inclui **métrica de burnout explícita** (≤ 20h/semana por membro), monitorada via self-report semanal na Discussion do GitHub.

### 4.4. Critérios de Qualidade Unificados (Simplificados)

A versão anterior (4 dimensões simultâneas) era excessiva para 2 pessoas. A v3.0 consolida em **2 dimensões obrigatórias + 1 opcional**:

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

**Dimensão 3 — Auditoria SDD (Opcional, mas recomendada)**
- Prompts de geração registrados em `/docs/prompts/`
- Commits com assinatura de co-autoria LLM
- ADR para decisões arquiteturais relevantes

**Nota:** A dimensão PDCA foi absorvida pelas duas primeiras (Plan/Do = Dimensão 2; Check/Act = Dimensão 1).

### 4.5. Critério de Obrigatoriedade de ADR — NOVO

| Situação | ADR Obrigatório? | Registro Alternativo |
|----------|-----------------|---------------------|
| Escolha de stack tecnológica | ✅ SIM | — |
| Substituição de ferramenta (ex: Gantt → Kanban) | ✅ SIM | — |
| Mudança de escopo (nova feature) | ✅ SIM | — |
| Escolha de biblioteca/framework menor | ❌ NÃO | Commit message (Conventional Commits) |
| Decisão de UI/UX (cor, layout) | ❌ NÃO | Comentário na Issue |
| Configuração de CI/CD | ❌ NÃO | README + commit message |
| Decisão que afeta ≥ 2 fases da EAP | ✅ SIM | — |

### 4.6. Macro-Fases Temporais (Reorganização da EAP) — NOVO

Para resolver a crítica de sobrecarga, as 13 fases da EAP são redistribuídas em 3 macro-fases:

| Macro-Fase | Período | Fases da EAP Incluídas | Marco de Entrega |
|------------|---------|----------------------|-----------------|
| **MF1: Fundação** | 01/09 – 30/09/2026 | 1 (Iniciação), 2 (Requisitos), 3 (Modelagem), 4 (Ambiente), 9 (Comunicação), 10 (Base de Conhecimento) | TAP 100% + EAP sincronizada + Stack definida + Ambiente configurado |
| **MF2: Construção** | 01/10 – 15/11/2026 | 5 (Desenvolvimento), 6 (Qualidade), 7 (DevOps), 8 (Deploy), 11 (Mudanças) | MVP funcional em produção + ≥ 80% coverage |
| **MF3: Consolidação** | 16/11 – 15/12/2026 | 12 (Documentação), 13 (Encerramento) | Documentação consolidada + Apresentação final + Aceite do Prof. Nivaldo |

**Regra:** As fases não são sequenciais dentro de cada macro-fase. O Kanban permite paralelismo. A EAP original (13 fases) é mantida como estrutura de decomposição; as macro-fases são apenas agrupamentos temporais para gestão.

### 4.7. Estrutura Documental (Mantida do OKB v2.1 §5, com anotações GMV)

```
PROJETO COGME
 ├── 00. TAP (Termo de Abertura)                          [GMV: OBRIGATÓRIO]
 ├── 01. Plano de Integração                               [GMV: OBRIGATÓRIO]
 ├── 02. Plano de Escopo + EAP/WBS + Dicionário            [GMV: OBRIGATÓRIO]
 ├── 03. Plano de Cronograma + Roadmap + Kanban Setup      [GMV: OBRIGATÓRIO]
 ├── 04. Plano de Custos + Orçamento                       [GMV: SIMPLIFICAR*]
 ├── 05. Plano de Qualidade + Métricas + DoD/DoR           [GMV: OBRIGATÓRIO]
 ├── 06. Plano de Recursos + RACI                          [GMV: SIMPLIFICAR*]
 ├── 07. Plano de Comunicações + Matriz                    [GMV: OBRIGATÓRIO]
 ├── 08. Plano de Riscos + Matriz + Respostas              [GMV: OBRIGATÓRIO]
 ├── 09. Base de Conhecimento                              [GMV: OBRIGATÓRIO]
 │   ├── 09.1. ADRs (apenas decisões críticas)
 │   ├── 09.2. Lições Aprendidas
 │   ├── 09.3. Prompts SDD
 │   └── 09.4. Runbooks
 ├── 10. Plano de Gestão de Mudanças (CCB)                 [GMV: SIMPLIFICAR*]
 └── 11. Código-Fonte (MVP) + DER + Diagramas              [GMV: OBRIGATÓRIO]

* SIMPLIFICAR = 1-2 páginas no máximo, foco em premissas e restrições,
  sem planilhas complexas ou simulações de EVM.
```

### 4.8. Declarações Obrigatórias no TAP (Atualizadas v3.0)

As 6 declarações do OKB v2.1 são mantidas com os seguintes ajustes:

1. **PMBOK 7ª como governança primária** — PMBOK 6ª como dicionário complementar. *(Mantida)*
2. **Kanban via GitHub Projects** como método de execução. *(Mantida)*
3. **Uso de LLM irrestrito e autorizado**, com rastreabilidade via ADRs e prompts catalogados. *(Reforçada: "irrestrito" adicionado)*
4. **Código-fonte (MVP full-stack)** como marco de sucesso e documentação formal. *(Mantida)*
5. **Aquisições e Partes Interessadas** com simplificação pedagógica. *(Mantida)*
6. **Fases de Segurança, Acessibilidade, Observabilidade e i18n** como melhoria contínua pós-entrega. *(Mantida)*
7. **NOVA — Stack 100% FOSS** com licenciamento compatível (MIT, Apache 2.0, GPL). *(Adicionada)*
8. **NOVA — Governança mínima viável** como princípio de eficiência, priorizando valor entregue sobre volume documental. *(Adicionada)*

---

## 5. DIRETRIZES ESTRATÉGICAS PARA FASE ATUAL (09/09 – 30/09/2026)

### 5.1. Prioridades da Semana Atual (09-13/09)

| Prioridade | Ação | DoD |
|-----------|------|-----|
| 🔴 P0 | Completar TAP v0.9 com EAP 13 fases + 8 premissas | TAP aprovado pelo Prof. Nivaldo |
| 🔴 P0 | Criar ADR-001 (GitHub Projects substitui Gantt) | ADR registrado e linkado |
| 🟠 P1 | Definir stack FOSS e criar ADR-002 | Stack validada com protótipo "Hello World" |
| 🟠 P1 | Sincronizar EAP → GitHub Projects (Fases 1-4) | 100% dos pacotes com card no Kanban |

### 5.2. Prioridades da Semana Seguinte (15-19/09)

| Prioridade | Ação | DoD |
|-----------|------|-----|
| 🟠 P1 | Configurar ambiente local (Fase 4) | Docker + CI/CD pipeline verde |
| 🟠 P1 | Iniciar período de calibração de métricas | Baseline de Cycle Time e Throughput |
| 🟡 P2 | Redigir Planos de Escopo e Qualidade | Versão v0.1 de cada |
| 🟡 P2 | Criar DER e diagrama de arquitetura | Diagramas em draw.io/Mermaid |

### 5.3. Prioridades da Terceira Semana (22-26/09)

| Prioridade | Ação | DoD |
|-----------|------|-----|
| 🟡 P2 | Finalizar Planos restantes (Cronograma, Custos, Recursos, Comunicações, Riscos) | Todos em v0.1 |
| 🟡 P2 | Calibrar métricas de fluxo e definir metas realistas | ADR-003 com metas ajustadas |
| 🟢 P3 | Iniciar protótipo UX/UI (Fase 3.2) | Wireframe aprovado |

### 5.4. Marco de Fechamento de Setembro (30/09)

**Entrega:** MF1 (Fundação) 100% concluída.
**Critérios de aceite:**
- TAP v1.0 aprovado
- 8 planos de área em v0.1 mínimo
- EAP sincronizada com GitHub Projects
- Stack FOSS definida e ambiente configurado
- ADR-001, ADR-002, ADR-003 registrados
- Métricas de fluxo com baseline estabelecida

---

## 6. CONDIÇÕES DE VALIDADE E GATILHOS

### Válido enquanto:
- Ementa da disciplina mantiver PMBOK (qualquer edição) como base
- Prof. Nivaldo mantiver papel de stakeholder único formal
- Equipe mantiver 2 pessoas com ≤ 20h/semana cada
- Prazo final mantiver em Nov/Dez 2026

### Invalida se:
- Professor exigir PMBOK 6ª como base **exclusiva** (regressão de governança)
- Ementa migrar para framework ágil puro sem PMBOK
- Código deixar de ser deliverable formal
- Equipe expandir para > 3 pessoas (muda dinâmica de governança)
- Prazo final antecipar para antes de Nov/2026

### Gatilhos de reavaliação:
- Novo artefato solicitado fora da árvore (seções 00-11)
- Mudança no critério de avaliação da disciplina
- Scope creep > 15% do backlog original
- Orientação verbal do Prof. Nivaldo divergente deste guardrail
- Falha crítica na API de câmbio externa (muda arquitetura)
- Burnout detectado (> 20h/semana por 2 semanas consecutivas)

---

## 7. PREMISSAS ASSUMIDAS (v3.0)

1. Projeto é 100% simulado; não há execução empresarial real.
2. PMBOK 7ª é governança primária; PMBOK 6ª é dicionário complementar.
3. Metodologia ágil Kanban via GitHub Projects é o método de execução.
4. Uso de LLM é irrestrito e autorizado pela disciplina.
5. Código-fonte (MVP full-stack) é deliverable formal e marco de sucesso.
6. Stack tecnológica será 100% FOSS (decisão pendente via ADR-002).
7. Equipe de 2 pessoas com carga ≤ 20h/semana cada.
8. Prof. Nivaldo é o único stakeholder formal (avaliador + patrocinador).
9. Áreas de Aquisições e Partes Interessadas são exclusão pedagógica intencional.
10. Fases de Segurança, Acessibilidade, Observabilidade e i18n são pós-entrega.
11. Documentação PMBOK é compliance acadêmico; código é produto.
12. Hardware local (AMD Ryzen 7 8700G, 60GB RAM, Arch Linux) é suficiente para desenvolvimento e testes.
13. Deploy em produção será em plataforma gratuita (a definir).
14. Governança mínima viável (GMV) é princípio operacional para evitar burocracia.

---

## 8. INSTRUÇÃO DE USO DESTE GUARDRAIL v3.0

| Situação | Consulte |
|----------|----------|
| Durante redação de artefatos | Seções 4.3, 4.4, 4.7 |
| Durante revisão de artefatos | Seção 4.4 (2 dimensões obrigatórias) |
| Durante conflito entre fontes | Seção 4.1 (hierarquia) |
| Durante dúvida sobre escopo | Seção 4.7 (árvore de artefatos) |
| Durante decisão técnica | Seção 4.5 (critério de ADR) |
| Durante dúvida sobre burocracia | Seção 4.2 (teste GMV) |
| Durante planejamento semanal | Seção 5 (diretrizes estratégicas) |
| Durante gestão do trabalho | Kanban no GitHub Projects (fonte de verdade) |
| Durante conflito de governança | Seção 4.6 (macro-fases temporais) |

---

**Versão:** 3.0
**Data:** 09/09/2026
**Status:** Pronto para aplicação imediata
**Próxima revisão:** 30/09/2026 (fechamento da MF1: Fundação)
