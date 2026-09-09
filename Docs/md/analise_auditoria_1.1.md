# RELATÓRIO ANALÍTICO v1.1 — CONSOLIDAÇÃO PÓS-REVISÃO E PLANO DE ENTREGA PARCIAL (19/09/2026)

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Data de Emissão:** 10/09/2026
**Emissor:** GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carletto
**Referência:** `analise_auditoria_1.0.md` (revisado) + OKB v3.0 + TAP v1_opngoing + hardware.md
**Status:** Input para ADR-001, ADR-002, ADR-003, ADR-004 + Plano de Ação 10-19/09

**Notas**:

1. Data de entrega parcial alterada (extendida): 22/09/2026 às 9:00AM impreterivelmente - Aplicar esta mudança em todo o contexto deste relatório atualizando todas as referências à data 19/09/2026 para a nova data 22/09/2026 9:00AM
2. Todas as menções ao Prof Nivaldo devem ter sua nomenclatura alterada para Profº Dr. Nivaldo Carletto em forma de prestar respeito e formalidade

---

## 0. DELTA ANALÍTICO v1.0 → v1.1

A revisão do relatório v1.0 introduziu **7 notas de ajuste** que alteram significativamente o plano de execução. Abaixo, o delta consolidado:

| # | Nota de Revisão                                                                                                                                                                                                                                                                                         | Impacto no Projeto                                                    | Severidade |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------- |
| 1 | Entrega parcial em**19/09/2026** (documentação até Área 5 — Qualidade) <br />Nota de revisão: Data alterada (extendida): 22/09/2026 às 9:00AM impreterivelmente - Entrega inclui a Documentação em formato Docx ou PDF uma sumarização exuta (4-5 slides max) em PPTx ou export to PDF | **CRÍTICO** — redefine cronograma; 7 dias úteis até entrega | 🔴         |
| 2 | PDCA obrigatório por atividade (último PDCA de cada atividade, com breve comentário sobre mudanças)                                                                                                                                                                                                  | **ALTO** — exige reestruturação da base documental           | 🟠         |
| 3 | Documentação formal é viva até entrega do MVP funcional                                                                                                                                                                                                                                              | **MÉDIO** — valida iterações contínuas                     | 🟡         |
| 4 | Entrega parcial**não exige código/implementação prévia**                                                                                                                                                                                                                                      | **ALTO** — alivia pressão sobre Fase 5                        | 🟢         |
| 5 | Remover seção "Fases Desejáveis" (14-17) do escopo estrito                                                                                                                                                                                                                                            | **BAIXO** — já estava como pós-entrega                       | 🟢         |
| 6 | Redesenhar roadmap para**dois marcos** (Parcial + Final) em vez de trimestres                                                                                                                                                                                                                      | **ALTO** — muda comunicação com stakeholder                  | 🟠         |
| 7 | Considerar ADRs adicionais:**ADR-001, ADR-003**                                                                                                                                                                                                                                                    | **MÉDIO** — exige conformidade com projeto                    | 🟡         |
| 8 | Verificar Seção 9 (Stack SDD Local) como referência para LLM                                                                                                                                                                                                                                          | **MÉDIO** — consolida ADR-004                                 | 🟡         |

**Veredito sumário:** A revisão **aprova 85% das recomendações v1.0** e introduz **restrição temporal bloqueante** (entrega parcial 19/09) que exige replanejamento imediato do plano de ação. O relatório v1.1 foca em: (a) consolidar as aprovações, (b) redesenhar o roadmap para dois marcos, (c) validar a aderência das ADRs propostas, (d) definir o plano de ação 10-19/09.

---

## 1. ANÁLISE CRÍTICA DAS NOTAS DE REVISÃO

### 1.1. Nota 1 — Entrega Parcial em 19/09/2026 (CRÍTICA)

**Contexto:** O TAP v1_opngoing (§3.1 — Cronograma) já previa entrega parcial em **08/09/2026** (TAP até Plano de Qualidade). A revisão posterga para **19/09/2026 (alterado para 22/09/2026)**, concedendo **9 dias corridos adicionais** (~7 dias úteis).

**Análise de viabilidade: -> Recalcule**

- **Capacidade disponível:** 2 pessoas × 20h/semana × 1,4 semanas = **56h úteis** até 19/09
- **Escopo da entrega parcial:** TAP + Planos de Integração, Escopo, Cronograma, Custos, Qualidade + PDCA de cada atividade
- **Estimativa de esforço:** ~40h (TAP 8h + 5 planos × 6h = 38h + PDCA 4h = 42h)
- **Folga:** 14h (~25%) — **viável com margem**

**Risco identificado:** A nota diz "não é mandatório entrega de código ou implementação prévia". Isso **libera a Fase 5 (Desenvolvimento)** da entrega parcial, mas exige que os **Planos de Qualidade (Área 5)** estejam 100% concluídos e com PDCA documentado.

**Decisão:** A entrega parcial deve conter **artefatos das Áreas 1-5 do PMBOK 6ª** (Integração, Escopo, Cronograma, Custos, Qualidade) com PDCA de cada atividade, conforme exigência do Prof. Nivaldo.

### 1.2. Nota 2 — PDCA Obrigatório por Atividade (ALTA)

**Contexto:** O Prof. Nivaldo exige **pelo menos um PDCA por atividade do projeto**. A nota operacionaliza: "adotaremos sempre o último PDCA de cada atividade caso mais de 1 PDCA tenha sido executado, comentando brevemente as mudanças resultantes".

**Análise crítica:**

- **OKB v3.0 §4.4** já havia absorvido a dimensão PDCA nas Dimensões 1 e 2 (Compliance + Valor Funcional). A nota **reintroduz PDCA explícito** como artefato obrigatório.
- **Trade-off:** Aumenta volume documental, mas atende a exigência acadêmica explícita. -> Tradeoff aceito - Este é um artefato inegociável
- **Mitigação KISS:** PDCA não precisa ser documento separado — pode ser **seção dentro de cada plano** (ex: "§X.X PDCA do Plano de Escopo"). - O artefato não deve ser separado, mas deve estar reunido sob o tópico/item/plano de projeto (área de conhecimento) 5 Gerenciamento da Qualidade, e não em cada plano. (Devo confirmar se a sugestão é cabível e aceita pelo Profº Dr. Nivaldo Carletto conforme formalização documental) -> Em análise (Componha doi blocos para cada modelo (A sugestão KISS e a que estou assumindo temporáriamente como correta - a confirmar - assim manteremos o tracking de decisões.))

**Modelo de PDCA recomendado (KISS):**

```markdown
## §X.X PDCA do [Nome do Plano]

| Fase | Ação | Evidência |
|------|------|-----------|
| **Plan** | Definição do escopo do plano | TAP §X + OKB v3.0 §4.7 |
| **Do** | Redação do plano v0.1 | Arquivo `/docs/planos/XX-escopo.md` |
| **Check** | Revisão cruzada (persona revisora) | Checklist v2.1 (7 critérios) |
| **Act** | Ajustes → v0.2/v1.0 | Commit `docs(plano-escopo): v1.0` |

**Mudanças relevantes vs. PDCAs anteriores:**
- v0.1 → v0.2: Adição de dicionário EAP (crítica da revisão anterior)
- v0.2 → v1.0: Alinhamento com macro-fases MF1/MF2/MF3 (OKB v3.0 §4.6)
```

**Domínio PMBOK 7ª associado:** Domínio de Medição (Check/Act) + Domínio de Entrega (Plan/Do).

### 1.3. Nota 3 — Documentação Formal Viva (MÉDIA)

**Contexto:** A documentação pode sofrer ajustes integrais até a entrega do MVP funcional (Nov/Dez 2026).

**Análise:** Esta nota **valida o princípio P6 do OKB** (entrega incremental via fluxo contínuo) e **reforça a hierarquia de governança** (OKB v3.0 §4.1). Não exige ação imediata, mas **blinda academicamente** iterações nos planos após 19/09.

**Implicação operacional:** Os planos entregues em 19/09 serão **v1.0 (baseline)**, mas podem evoluir para v1.1, v1.2 etc. até a entrega final, desde que cada mudança tenha:

1. ADR associado (se afetar ≥ 2 fases da EAP)
2. PDCA documentando a mudança
3. Commit com mensagem convencional (`docs(plano-X): descrição`)

### 1.4. Nota 4 — Código Não Obrigatório na Entrega Parcial (ALTA)

**Contexto:** A entrega parcial de 19/09 **não exige código ou implementação prévia**.

**Análise:** Esta é a **notícia mais relevante** da revisão. Significa que:

- ✅ **Fase 5 (Desenvolvimento) sai do escopo da entrega parcial**
- ✅ **Fase 4 (Configuração de Ambiente) pode ser parcial** (apenas documentação da stack, não setup completo)
- ✅ **Foco total em documentação das Áreas 1-5**

**Impacto no plano de ação:** Reduz escopo da entrega parcial em ~40%, aumentando a folga de 25% para ~45%.

### 1.5. Nota 5 — Remoção de Fases Desejáveis (BAIXA)

**Contexto:** As fases 14-17 (Segurança, Acessibilidade, Observabilidade, i18n) já estavam marcadas como "Pós-Entrega" no TAP v1_opngoing (§5.3).

**Análise:** A nota apenas **formaliza** o que já estava documentado. Nenhuma ação necessária — apenas **reforço da rastreabilidade** no TAP.

### 1.6. Nota 6 — Redesenho do Roadmap para Dois Marcos (ALTA)

**Contexto:** O OKB v2.1 §8.2.1 usava roadmap trimestral (Q3/Q4/Q1). A revisão exige **dois marcos**: Entrega Parcial (19/09) e Entrega Final (MVP funcional).

**Análise:** Esta mudança **alinhada ao YAGNI** — roadmap trimestral era burocracia para projeto de 3 meses. Dois marcos são suficientes e mais claros.

**Novo roadmap proposto (ADR-003):**

| Marco                           | Data                   | Escopo                                                      | Critério de Aceite                            |
| ------------------------------- | ---------------------- | ----------------------------------------------------------- | ---------------------------------------------- |
| **M1 — Entrega Parcial** | 19/09/2026 *Alterado* | TAP + Planos Áreas 1-5 + PDCA de cada atividade            | Prof. Nivaldo valida completude documental     |
| **M2 — Entrega Final**   | Nov/Dez 2026           | MVP funcional + documentação consolidada + apresentação | ≥ 80% coverage + UAT aprovado + FOSS auditado |

**Macro-fases ajustadas:**

| Macro-Fase                    | Período            | Foco                                  |
| ----------------------------- | ------------------- | ------------------------------------- |
| **MF1: Fundação**     | 01/09 – 19/09/2026 | Documentação Áreas 1-5 + PDCA      |
| **MF2: Construção**   | 20/09 – 15/11/2026 | Desenvolvimento + Testes + Deploy     |
| **MF3: Consolidação** | 16/11 – Dez/2026   | Documentação final + Apresentação |

### 1.7. Nota 7 — ADRs ADicionais: ADER-001 e ADR-003 (MÉDIA)

**Contexto:** A revisão solicita avaliação de aderência de **ADER-001** e **ADR-003** ao projeto.

**Análise de aderência:**

#### ADER-001 — "Architecture Decision Enhancement Record" -> Descartar: Isso foi typo - Considere ADR-001 

~~**Hipótese:** A sigla "ADER" sugere um ADR expandido, possivelmente com seção de "Enhancement" (melhoria contínua).~~

**~~Aderência ao COGME:~~**

- ~~✅ Alinha ao P1 (valor sobre documentação) se o "Enhancement" for acionável~~
- ~~⚠️ Risco de burocratização se exigir seções extras não previstas no OKB v3.0 §4.5~~
- ~~**Decisão:** **NÃO ADERENTE** no formato atual. O COGME já possui critério claro de ADR (OKB v3.0 §4.5). Criar "ADER" duplica nomenclatura sem valor adicional.~~
- ~~**Recomendação:** Manter ADR padrão (Contexto → Decisão → Consequências). Se houver necessidade de registrar "enhancements", usar **label `enhancement` no GitHub Issues** + link no ADR original.~~

#### ADR-003 — "Métricas de Fluxo com Baseline"

**Hipótese:** ADR-003 formaliza a calibração de métricas (Cycle Time, Throughput) conforme OKB v3.0 Crítica 4.

**Aderência ao COGME:**

- ✅ Alinha ao Domínio de Medição PMBOK 7ª
- ✅ Resolve Crítica 4 do OKB v3.0 (métricas sem baseline)
- ✅ Necessário para MF2 (Construção) quando o Kanban entrar em operação plena
- **Decisão:** **ADERENTE** — deve ser formalizado até 30/09/2026 (fim da MF1).

### 1.8. Nota 8 — Seção 9 (Stack SDD Local) como Referência (MÉDIA)

**Contexto:** A revisão aponta para a Seção 9 do relatório v1.0 como referência para a stack SDD local (llama.cpp + Qwen + OpenCode). -> Completar com Obsidian para controle de artefatos e second-brain do LLM

**Análise:** A Seção 9 já está aprovada e detalhada no relatório v1.0. A nota apenas **confirma** que esta seção deve ser a base do **ADR-004** (SDD Local).

**Ação:** Consolidar Seção 9 como anexo do ADR-004.

---

## 2. REDESENHO DO ROADMAP (DOIS MARCOS)

### 2.1. Roadmap Consolidado (ADR-003 draft)

```
┌─────────────────────────────────────────────────────────────────┐
│  MARCO 1 — ENTREGA PARCIAL (19/09/2026)                       │
│  Escopo: Documentação Áreas 1-5 do PMBOK 6ª                   │
│  ├─ TAP v1.0 (com EAP 13 fases + 8 premissas)                 │
│  ├─ Plano de Integração v1.0                                   │
│  ├─ Plano de Escopo v1.0 (+ EAP + Dicionário)                 │
│  ├─ Plano de Cronograma v1.0 (+ Roadmap 2 marcos)             │
│  ├─ Plano de Custos v1.0 (simplificado)                        │
│  ├─ Plano de Qualidade v1.0 (+ DoD/DoR + PDCA)                │
│  └─ PDCA de cada atividade (último PDCA + mudanças relevantes)│
│  Critério de aceite: Prof. Nivaldo valida completude           │
├─────────────────────────────────────────────────────────────────┤
│  MARCO 2 — ENTREGA FINAL (Nov/Dez 2026)                       │
│  Escopo: MVP funcional + documentação consolidada              │
│  ├─ Código-fonte (Backend + Frontend + PDF)                    │
│  ├─ ≥ 80% coverage de testes                                   │
│  ├─ UAT aprovado                                               │
│  ├─ Documentação técnica + manual do usuário                   │
│  ├─ Apresentação final + aceite                                │
│  └─ Auditoria FOSS final                                       │
│  Critério de aceite: MVP funcional + ≥ 80% coverage + UAT      │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2. Macro-Fases Ajustadas

| Macro-Fase                    | Período            | Fases da EAP                 | Entregáveis-Chave                    |
| ----------------------------- | ------------------- | ---------------------------- | ------------------------------------- |
| **MF1: Fundação**     | 01/09 – 19/09/2026 | 1, 2, 3, 4 (parcial), 9, 10  | TAP + Planos Áreas 1-5 + PDCA        |
| **MF2: Construção**   | 20/09 – 15/11/2026 | 4 (completo), 5, 6, 7, 8, 11 | MVP funcional + ≥ 80% coverage       |
| **MF3: Consolidação** | 16/11 – Dez/2026   | 12, 13                       | Documentação final + Apresentação |

**Trade-off declarado:** A MF1 foi **comprimida de 30 dias para 19 dias** (01/09 → 19/09). Isso exige **foco absoluto em documentação** e **adiamento da Fase 4 completa** para a MF2.

---

## 3. PLANO DE AÇÃO 10-19/09/2026 (ENTREGA PARCIAL)

### 3.1. Capacidade Disponível

| Recurso         | Disponibilidade                          |
| --------------- | ---------------------------------------- |
| Dias úteis     | 7 (10, 11, 12, 15, 16, 17, 18/09)        |
| Horas por dia   | 4h/pessoa (20h/semana ÷ 5 dias)         |
| Total de horas  | 2 pessoas × 4h × 7 dias =**56h** |
| Escopo estimado | 42h (TAP 8h + 5 planos × 6h + PDCA 4h)  |
| **Folga** | **14h (25%)**                      |

### 3.2. Cronograma Detalhado

| Data                   | Ação                                                   | Responsável | Artefato                                | DoD                                                      |
| ---------------------- | -------------------------------------------------------- | ------------ | --------------------------------------- | -------------------------------------------------------- |
| **10/09 (qui)**  | Finalizar TAP v1.0 (EAP + premissas)                     | GP           | `TAP_EAP.md` v1.0                     | TAP com 13 fases + 8 premissas                           |
| **11/09 (sex)**  | Redigir ADR-001 (GitHub Projects) + ADR-002 (Stack FOSS) | GP + Dev     | `docs/adr/ADR-001.md`, `ADR-002.md` | ADRs formatados (Contexto → Decisão → Consequências) |
| **12/09 (sáb)** | Plano de Integração v1.0                               | GP           | `docs/planos/01-integracao.md`        | Contém links GitHub + SSOT                              |
| **15/09 (seg)**  | Plano de Escopo v1.0 (+ EAP + Dicionário)               | GP           | `docs/planos/02-escopo.md`            | EAP sincronizada com GitHub Projects                     |
| **16/09 (ter)**  | Plano de Cronograma v1.0 (+ Roadmap 2 marcos)            | GP           | `docs/planos/03-cronograma.md`        | Roadmap M1 (19/09) + M2 (Nov/Dez)                        |
| **17/09 (qua)**  | Plano de Custos v1.0 (simplificado)                      | GP           | `docs/planos/04-custos.md`            | 1-2 páginas, foco em premissas                          |
| **18/09 (qui)**  | Plano de Qualidade v1.0 (+ DoD/DoR + PDCA)               | GP           | `docs/planos/05-qualidade.md`         | DoD/DoR claros + PDCA de cada atividade                  |
| **19/09 (sex)**  | Revisão final + submissão ao Prof. Nivaldo             | GP           | Issue no GitHub                         | Zero achados CRÍTICOS no checklist                      |

### 3.3. PDCA Consolidado (Entrega Parcial)

Para cada plano, incluir seção PDCA conforme modelo da Seção 1.2. Exemplo para o **Plano de Escopo**:

```markdown
## §6.6 PDCA do Plano de Escopo

| Fase | Ação | Evidência |
|------|------|-----------|
| **Plan** | Definição do escopo com base no TAP §2 | TAP v1.0 §2 + OKB v3.0 §4.7 |
| **Do** | Redação do plano v0.1 com EAP 13 fases | Commit `docs(plano-escopo): v0.1` (15/09) |
| **Check** | Revisão cruzada (persona revisora) | Checklist v2.1 — 7 critérios |
| **Act** | Ajustes → v1.0 (adição de dicionário EAP) | Commit `docs(plano-escopo): v1.0` (18/09) |

**Mudanças relevantes vs. PDCAs anteriores:**
- v0.1 → v1.0: Adição de dicionário EAP (crítica da revisão do relatório v1.0)
- v0.1 → v1.0: Alinhamento com macro-fases MF1/MF2/MF3 ajustadas (M1 = 19/09)
```

---

## 4. ADRs A FORMALIZAR (10-30/09/2026)

### 4.1. ADR-001 — GitHub Projects como SSOT (11/09)

**Contexto:** O TAP v1_opngoing (§3.1) menciona EVM e relatórios quinzenais, mas o OKB v3.0 §8.2 substitui Gantt por Kanban/GitHub Projects.

**Decisão:** GitHub Projects é a **fonte única de verdade** para cronograma, monitoramento e medição. Gantt (se exigido) é derivado do Kanban, não o contrário.

**Consequências:**

- ✅ Alinha ao Domínio de Medição PMBOK 7ª (GitHub Insights)
- ✅ Reduz burocracia (sem relatórios estáticos duplicados)
- ⚠️ Risco: Prof. Nivaldo pode exigir Gantt tradicional → mitigação: gerar Gantt a posteriori a partir do Kanban - Isto já é ponto Pacificado, o Prof Dr. Nivaldo Carletto declarou preferência por não Gannt, apesar de não restringir seu uso. Esqueça Gantt e adote a opção mais moderna e apenas isso.

### 4.2. ADR-002 — Stack FOSS (11/09)

**Contexto:** OKB v3.0 Crítica 3 identifica stack indefinida como risco crítico (R-01).

**Decisão:** Stack recomendada (conforme relatório v1.0 §3.2):

- Backend: Python 3.12 + FastAPI
- Banco: SQLite 3
- Frontend: HTML + HTMX + Tailwind CSS
- PDF: WeasyPrint
- LLM: llama.cpp + Qwen2.5-Coder-7B-Q4 (via OpenCode TUI)

**Consequências:**

- ✅ 100% FOSS (alinha P2)
- ✅ Rodável no hardware local (hardware.md)
- ✅ Curva de aprendizado ≤ 2 semanas

### 4.3. ADR-003 — Métricas de Fluxo com Baseline (30/09)

**Contexto:** OKB v3.0 Crítica 4 identifica métricas sem baseline.

**Decisão:** Estabelecer período de calibração (20/09 – 03/10) para coletar Cycle Time e Throughput sem meta fixa. Após calibração, definir metas realistas (média ± 20%).

**Consequências:**

- ✅ Alinha ao Domínio de Medição PMBOK 7ª
- ✅ Evita metas aspiracionais não acionáveis

### 4.4. ADR-004 — SDD Local via llama.cpp (30/09)

**Contexto:** Relatório v1.0 §5 + Seção 9 (Stack SDD Local).

**Decisão:** Adotar SDD local com llama.cpp + Qwen2.5-Coder-7B-Q4 + OpenCode TUI, conforme arquitetura da Seção 9.

**Consequências:**

- ✅ Zero custo operacional (alinha P2)
- ✅ Auditabilidade total (prompts versionáveis)
- ⚠️ Trade-off: qualidade inferior a GPT-4 → mitigação: revisão humana + testes automatizados -> TradeOff =irrelevante no momento, o uso de GPT-4 ou Claude implica no uso pago das ferramentas, Qwen Code (entre outras opções gratuitas) via Ollama é viável e configurável para uso local do SDD.

---

## 5. TRADE-OFFS E RISCOS ATUALIZADOS

### 5.1. Trade-offs Declarados

| Trade-off                                    | Risco                                      | Mitigação                                                                                       |
| -------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| MF1 comprimida (30 → 19 dias)               | Qualidade documental reduzida              | Folga de 25% (14h) + foco absoluto em Áreas 1-5                                                  |
| PDCA obrigatório por atividade              | Aumento de volume documental               | PDCA como seção dentro de cada plano (não documento separado)                                  |
| Código não obrigatório na entrega parcial | Percepção de "atraso" pelo Prof. Nivaldo | Comunicar explicitamente que MF2 (20/09 em diante) é dedicada ao código                         |
| ADR-003 com período de calibração         | Métricas sem meta por 2 semanas           | Comunicar ao Prof. Nivaldo que calibração é prática padrão (Domínio de Medição PMBOK 7ª) |

### 5.2. Riscos Atualizados

| ID   | Risco                                           | Prob. | Impacto | Severidade | Resposta                                | Status          |
| ---- | ----------------------------------------------- | ----- | ------- | ---------- | --------------------------------------- | --------------- |
| R-01 | Stack FOSS indefinida - Assumir stack sugerida  | 80%   | Alto    | Crítico   | ADR-002 até 11/09                      | 🟠 Aberto       |
| R-02 | EAP não sincronizada com GitHub                | 60%   | Alto    | Alto       | Mapeamento 1:1 até 15/09               | 🟡 Em andamento |
| R-03 | Governança > 50% do tempo                      | 70%   | Médio  | Alto       | Aplicar GMV                             | 🟡 Aberto       |
| R-04 | Prof. exigir Gantt tradicional                  | 30%   | Médio  | Médio     | ADR-001 + Gantt derivado                | 🟢 Mitigado     |
| R-05 | Scope creep                                     | 50%   | Alto    | Alto       | CCB + DoR rigoroso                      | 🟡 Monitorando  |
| R-09 | **Entrega parcial 19/09 não concluída** | 30%   | Alto    | Alto       | Plano de ação 10-19/09 + folga 25%    | 🟠 Novo         |
| R-10 | **PDCA não documentado por atividade**   | 40%   | Médio  | Médio     | Template PDCA padronizado (Seção 1.2) | 🟠 Novo         |

---

## 6. AÇÕES BLOQUEANTES (10-19/09/2026)

| #  | Ação                                                                         | Responsável | Prazo | Artefato                         |
| -- | ------------------------------------------------------------------------------ | ------------ | ----- | -------------------------------- |
| 1  | Finalizar TAP v1.0 (EAP + premissas) - Ongoing                                 | GP           | 10/09 | `TAP_EAP.md` v1.0              |
| 2  | Redigir ADR-001 (GitHub Projects) - Ongoing                                    | GP           | 11/09 | `docs/adr/ADR-001.md`          |
| 3  | Redigir ADR-002 (Stack FOSS)                                                   | GP + Dev     | 11/09 | `docs/adr/ADR-002.md`          |
| 4  | Plano de Integração v1.0 - Iniciar                                           | GP           | 12/09 | `docs/planos/01-integracao.md` |
| 5  | Plano de Escopo v1.0 (+ EAP + Dicionário) - Iniciar                          | GP           | 15/09 | `docs/planos/02-escopo.md`     |
| 6  | Plano de Cronograma v1.0 (+ Roadmap 2 marcos) - Iniciar                        | GP           | 16/09 | `docs/planos/03-cronograma.md` |
| 7  | Plano de Custos v1.0 (simplificado) - Verificar e Iniciar                      | GP           | 17/09 | `docs/planos/04-custos.md`     |
| 8  | Plano de Qualidade v1.0 (+ DoD/DoR + PDCA) - Iniciar                          | GP           | 18/09 | `docs/planos/05-qualidade.md`  |
| 9  | PDCA de cada atividade (último PDCA + mudanças) - Iniciar                    | GP           | 18/09 | Seção em cada plano            |
| 10 | Revisão final + submissão ao Prof. Nivaldo - não mandatório até dia 22/09 | GP           | 19/09 | Issue no GitHub                  |

---

## 7. DECLARAÇÃO DE CONFORMIDADE

Este relatório v1.1:

- ✅ Deriva 100% das notas de revisão do relatório v1.0
- ✅ Cita domínios e princípios PMBOK 7ª explicitamente
- ✅ Aplica teste GMV (OKB v3.0 §4.2) para cada recomendação
- ✅ Declara trade-offs e riscos (Domínio de Incerteza PMBOK 7ª)
- ✅ Respeita hierarquia de governança (OKB v3.0 §4.1)
- ✅ É acionável (plano de ação 10-19/09 com datas e responsáveis)
- ✅ Integra PDCA como mecanismo de qualidade (nota de revisão 2)
- ✅ Redesenha roadmap para dois marcos (nota de revisão 6)
- ✅ Avalia aderência de ADER-001 (não aderente) e ADR-003 (aderente)

---

## 8.  Crítica Propositiva: Obsidian Global vs. Por Projeto

## 8.1. Análise First-Principles do Questionamento

Você identificou uma **contradição arquitetural** no relatório original. Vamos decompor:

### 8.1.1. O Que o Relatório Diz (e Onde Falha)

O relatório propõe:

```
.ai/ (no Git, por projeto) + Obsidian (vault global)
```

**Problema:** Isso cria uma **separação artificial** entre:

- Contexto versionado (`.ai/`)
- Contexto não-versionado (Obsidian)

Se o Obsidian é "segundo cérebro", ele deveria conter **todo** o contexto necessário para a IA, não apenas um subconjunto.

### 8.1.2. Princípio Violado

> "Separação clara: código do projeto (Git) vs. contexto da IA (`.ai/` no Git + Vault global no Obsidian)"

Isso viola o princípio de **single source of truth**. Se a IA precisa de contexto, ele deve estar em **um lugar só**, versionado e determinístico.

---

## 8.2. Trade-Offs: Vault Global vs. Por Projeto

### 8.2.1. Argumentos a Favor de Vault Global

| Vantagem                                          | Análise Crítica                                          |
| ------------------------------------------------- | ---------------------------------------------------------- |
| **Hardware profile compartilhado**          | ✅ Válido, mas pode ser um arquivo único em cada projeto |
| **Specs reutilizáveis** (coding-standards) | ⚠️ Falso positivo: cada projeto tem regras específicas  |
| **Menos complexidade de sync**              | ✅ Válido, mas Obsidian sync é trivial (Git/Syncthing)   |
| **Cérebro é um só**                      | ❌ Metáfora enganosa: projetos são contextos distintos   |

### 8.2.2. Argumentos a Favor de Vault Por Projeto

| Vantagem                             | Análise Crítica                                      |
| ------------------------------------ | ------------------------------------------------------ |
| **Isolamento de contexto**     | ✅ Crítico: evita poluição cognitiva entre projetos |
| **Customização por projeto** | ✅ Essencial: COGME ≠ COBECO em regras de domínio    |
| **Versionamento independente** | ✅ Cada projeto evolui em ritmo próprio               |
| **Onboarding facilitado**      | ✅ Novo colaborador vê apenas o projeto relevante     |
| **Backup granular**            | ✅ Posso backup apenas projetos ativos                 |

### 8.2.3. O Custo Real de Vault Global

```
Vault Global/
├── COGME/
│   ├── specs/
│   └── handoffs/
├── COBECO/
│   ├── specs/
│   └── handoffs/
├── hardware-profile.md  ← compartilhado
└── preferences.md       ← compartilhado
```

**Problemas:**

1. **Poluição de busca:** Buscar "spec" retorna resultados de todos projetos
2. **Graph view inútil:** Mistura relações de projetos distintos
3. **Backup monolítico:** Não posso backup apenas COGME
4. **Conflitos de merge:** Se dois projetos evoluem specs compartilhadas

---

## 8.3. Arquitetura Ótima Proposta (Refinamento)

### 3.1. Princípio Guia

> **"Contexto da IA deve estar 100% versionado no Git do projeto. Obsidian é apenas uma interface de leitura/edição."**

### 8.3.2. Estrutura por Projeto (Vault Dedicado)

```
COGME/                          # Repositório Git
├── .git/
├── src/
├── docs/                       # Documentação HUMANA (não lida pela IA)
│   ├── project-plan.md
│   ├── meeting-notes/
│   └── roadmap.md
│
├── .ai/                        # CONTEXTO DA IA (lido pelo OpenCode)
│   ├── prompts/
│   ├── specs/
│   ├── handoffs/
│   └── workflows/
│
└── .obsidian/                  # Configuração do vault (opcional)
    └── workspace.json
```

**Vault do Obsidian:**

```
~/Obsidian/COGME/              # Vault dedicado ao projeto
├── .ai/ → /path/to/COGME/.ai/  # Symlink para o repositório Git
├── docs/ → /path/to/COGME/docs/ # Symlink para documentação humana
└── .obsidian/                  # Configuração do vault
```

### 8.3.3. Benefícios Desta Abordagem

| Benefício                       | Explicação                                                |
| -------------------------------- | ----------------------------------------------------------- |
| **Single source of truth** | Tudo está no Git, Obsidian é apenas interface             |
| **Isolamento de contexto** | Cada projeto tem seu vault, sem poluição                  |
| **Versionamento total**    | Código + contexto IA + docs humanas no mesmo Git           |
| **Flexibilidade de docs**  | `docs/` pode conter planos, roadmaps, sem poluir `.ai/` |
| **Zero overhead**          | Symlinks são gratuitos, sem duplicação                   |

### 8.3.4. Onde Ficam os Documentos de Gerenciamento?

**Resposta:** Em `docs/`, **fora** do contexto da IA.

```
docs/
├── project-plan.md          # Plano do projeto (humano)
├── roadmap.md               # Roadmap (humano)
├── meeting-notes/           # Atas de reunião (humano)
└── decisions/               # ADRs (Architecture Decision Records)
```

**Por que não em `.ai/`?**

- A IA não precisa de contexto de gerenciamento para codar
- `.ai/` deve conter apenas o **mínimo necessário** para a IA trabalhar
- Princípio: "Se não é lido pelo OpenCode, não pertence em `.ai/`"

**Exceção:** Se um ADR (Architecture Decision Record) afeta diretamente o código, ele deve estar em `.ai/specs/architecture.md`.

---

## 8.4. Crítica ao Relatório Original

### 4.1. O Que Estava Errado

1. **Separação artificial:** `.ai/` no Git + Obsidian global cria dualidade desnecessária
2. **Subutilização do Obsidian:** Tratado como "segundo cérebro" mas limitado a hardware profile
3. **Falta de clareza sobre `docs/`:** Não especificou onde ficam planos, roadmaps, etc.

### 8.4.2. O Que Estava Certo

1. **`.ai/` versionado no Git:** Correto, contexto da IA deve ser versionado
2. **Separação L1/L2/L3:** Correto, camadas ortogonais
3. **Simplicidade first:** Correto, evitar frameworks desnecessários

---

## 8.5. Recomendação Final

### 5.1. Adotar Vault Por Projeto

```bash
# Criar vault dedicado para cada projeto
mkdir -p ~/Obsidian/COGME
cd ~/Obsidian/COGME

# Criar symlinks para o repositório Git
ln -s /path/to/COGME/.ai .ai
ln -s /path/to/COGME/docs docs

# Abrir no Obsidian
obsidian .
```

### 8.5.2. Estrutura de Diretórios Refinada

```
PROJETO/
├── .git/
├── src/                          # Código-fonte
├── tests/                        # Testes
│
├── docs/                         # Documentação HUMANA
│   ├── project-plan.md
│   ├── roadmap.md
│   ├── meeting-notes/
│   └── decisions/                # ADRs (se afetam código, mover para .ai/specs/)
│
├── .ai/                          # CONTEXTO DA IA (lido pelo OpenCode)
│   ├── prompts/
│   │   ├── _base.md
│   │   ├── coder.md
│   │   ├── reviewer.md
│   │   ├── tester.md
│   │   ├── pm.md
│   │   └── active.md → coder.md
│   │
│   ├── specs/
│   │   ├── coding-standards.md   # Regras específicas do projeto
│   │   ├── api-contracts.md
│   │   ├── domain-rules.md
│   │   └── architecture.md       # ADRs que afetam código
│   │
│   ├── handoffs/
│   │   ├── 001-feature-x-spec.md
│   │   ├── 001-feature-x-code.md
│   │   └── 001-feature-x-review.md
│   │
│   └── workflows/
│       └── sdd-cycle.sh
│
└── .obsidian/                    # Configuração do vault (opcional)
    └── workspace.json
```

### 8.5.3. Regras de Ouro

1. **`.ai/` é sagrado:** Apenas o que a IA lê para trabalhar
2. **`docs/` é humano:** Planos, roadmaps, atas de reunião
3. **Obsidian é interface:** Não é repositório, é visualizador/editor
4. **Tudo no Git:** Código + `.ai/` + `docs/` no mesmo repositório
5. **Vault por projeto:** Isolamento de contexto, zero poluição

---

## 8.6. Conclusão

A solução ótima é:

- **Vault por projeto** (não global)
- **`.ai/` versionado no Git** (single source of truth)
- **`docs/` separado** (documentação humana fora do contexto da IA)
- **Obsidian como interface** (symlinks para o repositório Git)

Isso mantém a simplicidade first-principles, mas resolve o problema de isolamento de contexto e clareza sobre onde ficam documentos de gerenciamento.
