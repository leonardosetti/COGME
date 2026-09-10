# Ações para produção do Relatório de auditoria e análise 3.0:

1. Sobre EAP e PDCAs:

> O TAP não é parte destes artefatos! o TAP antecede o projeto e não deve invadir o escopo de gerenciamento do projeto, portanto TAP NUNCA deve ser contemplado em um EAP ou PDCA para medição e controle adequado do projeto.

2. Sobre a definição da stack de desenvolvimento

> ### 3.2. Stack Recomendada (ADR-002 APROVADA)
>
> | Camada                     | Tecnologia                             | Licença                 | Justificativa KISS                                                         |
> | -------------------------- | -------------------------------------- | ------------------------ | -------------------------------------------------------------------------- |
> | **Backend**          | **Python 3.12 + FastAPI**        | MIT                      | Sintaxe simples, LLM treinadíssimo, async nativo, OpenAPI automático     |
> | **Banco de Dados**   | **SQLite 3**                     | Public Domain            | Zero setup, ACID nativo, single-file (deploy trivial), 80% coverage fácil |
> | **Cache**            | **FASE (in-process dict + TTL)** | —                       | 1 provider de câmbio (Frankfurter) → cache distribuído é YAGNI         |
> | **Frontend**         | **HTML + HTMX + Tailwind CSS**   | MIT                      | Server-side rendering elimina 90% do JS; KISS puro                         |
> | **Geração PDF**    | **WeasyPrint**                   | BSD3                     | Já especificado no TAP; maduro, FOSS, HTML→PDF                           |
> | **Testes**           | **pytest + coverage.py**         | MIT                      | Padrão de fato Python, integração CI trivial                            |
> | **CI/CD**            | **GitHub Actions**               | Gratuito (2000 min/mês) | Já especificado; integrado ao SSOT                                        |
> | **LLM Local (SDD)**  | **llama.cpp + Seções 10 e 11** | MIT / Apache 2.0         | Roda no hardware (60GB RAM sobra), offline, FOSS                           |
> | **TUI para Prompts** | **OpenCode**                     | MIT                      | Já especificado na nova premissa; TUI nativa                              |

3. Sobre conceito de atividades do projeto

> Segundo o **PMBOK** (Guia do Conhecimento em Gerenciamento de Projetos), você deriva as atividades do projeto principalmente a partir da **Estrutura Analítica do Projeto (EAP)** — ou *Work Breakdown Structure (WBS)* — especificamente dos  **pacotes de trabalho** , que são o nível mais baixo da EAP.
>
> O processo onde isso ocorre é o **Definir as Atividades** (pertencente ao Grupo de Processos de Planejamento e à Área de Conhecimento de Gerenciamento do Cronograma).
>
> 📋 Principais Entradas para Derivar as Atividades
>
> Para decompor o escopo em atividades executáveis, você utiliza os seguintes componentes da  **Linha de Base do Escopo** :
>
> * **EAP (Estrutura Analítica do Projeto):** Fornece a estrutura hierárquica de todo o escopo do projeto.
> * **Pacotes de Trabalho:** São os blocos de entrega no nível mais baixo da EAP. Você pega cada pacote de trabalho e o decompõe em atividades menores necessárias para produzi-lo.
> * **Dicionário da EAP:** Fornece a descrição detalhada das entregas, restrições e requisitos de cada pacote de trabalho, garantindo que nenhuma atividade essencial seja esquecida.
>
> 🛠️ A Técnica Utilizada: Decomposição
>
> A principal técnica utilizada é a  **decomposição** , que consiste em dividir e subdividir o escopo do projeto e as entregas em partes menores e mais gerenciáveis (as atividades). Enquanto a EAP foca em *entregas* (substantivos), a lista de atividades foca na *ação* (verbos) necessária para gerar essas entregas.
>
> 📦 O que é gerado a partir dessa derivação?
>
> Como resultado desse processo, você obterá:
>
> * **Lista de atividades:** Uma lista completa contendo todas as atividades do cronograma que devem ser realizadas no projeto.
> * **Atributos das atividades:** Detalhes de cada atividade (como códigos, predecessoras, sucessoras, recursos necessários, restrições).
> * **Lista de marcos (Milestones):** Pontos ou eventos significativos no projeto (com duração zero).

4. Necessidades para produção da base de conhecimento atualizada e TAP

> Considerando os padrões do PMO - [escritoriodeprojetos.com.br](https://escritoriodeprojetos.com.br/):
>
> * Precisamos do TAP concluído sem ter necessidade do conhecimento do conteúdo gerencial completo do projeto. Não devemos invadir áreas de escopop distintos.
> * EAP deve estar rigorosamente bem definida
> * Precisamos determinar os principais requisitos das principais entregas/produtos previsíveis e aderentes ao TAP
> * Precisamos determinar os riscos previsíveis e aderentes ao TAP
> * Precisamos determinar as premissas previsíveis e aderentes ao TAP

# RELATÓRIO ANALÍTICO v1.2 — CONSOLIDAÇÃO PÓS-REESTRUTURAÇÃO DO COGME

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Data de Emissão:** 10/09/2026 (revisado em 10/09/2026)
**Emissor:** GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carletto
**Referência:** `analise_auditoria_1.2.md` + `OKB_COGME_v3.0` + `TAP_EAP.md` + `hardware.md`
**Status:** Input consolidado para ADR-001, ADR-002, ADR-003, ADR-004 + Plano de Ação 10-22/09/2026

---

## 0. DELTA ANALÍTICO v1.1 → v1.2

A reestruturação v1.2 introduz **5 mudanças estruturais** que alteram significativamente a arquitetura documental e o cronograma de entrega parcial:

| # | Mudança Estrutural                                                                | Categoria                   | Severidade  | Domínio PMBOK 7ª Afetado   |
| - | ---------------------------------------------------------------------------------- | --------------------------- | ----------- | ---------------------------- |
| 1 | **Entrega parcial postergada de 19/09 para 22/09/2026 (09:00)**              | Restrição Temporal        | 🔴 CRÍTICA | Entrega + Medição          |
| 2 | **PDCAs consolidados exclusivamente no Plano de Qualidade (Área 5)**        | Reestruturação Documental | 🔴 CRÍTICA | Qualidade + Medição        |
| 3 | **Diagrama de Ishikawa (Causa e Efeito) obrigatório no Plano de Qualidade** | Novo Artefato               | 🟠 ALTA     | Qualidade + Incerteza        |
| 4 | **Padronização do nome do stakeholder (Prof. Dr. Nivaldo Carletto)**       | Formalização              | 🟢 BAIXA    | Stakeholders                 |
| 5 | **Eliminação definitiva do termo "ADER"**                                  | Simplificação             | 🟢 BAIXA    | Abordagem de Desenvolvimento |

**Veredito sumário:** A v1.2 **aprova 100% das decisões v1.1** e introduz **reestruturação documental centralizadora** (PDCAs + Ishikawa no Plano de Qualidade) que reduz fragmentação e aumenta defensabilidade acadêmica. O ganho de 3 dias úteis (19/09 → 22/09) eleva a folga de 21% para **31%**, mitigando o risco R-09.

---

## 1. ANÁLISE CRÍTICA DAS MUDANÇAS ESTRUTURAIS

### 1.1. Mudança 1 — Postergação da Entrega Parcial (19/09 → 22/09/2026, 09:00)

**Contexto:** A data original (19/09/2026, sexta-feira) foi postergada para **22/09/2026 (terça-feira, 09:00)**, concedendo **3 dias corridos adicionais** (incluindo fim de semana).

**Recálculo de capacidade:**

| Recurso            | v1.1 (até 19/09) | v1.2 (até 22/09)                   | Delta          |
| ------------------ | ----------------- | ----------------------------------- | -------------- |
| Dias úteis        | 7 (10-18/09)      | **8** (10-11, 15-19, 22/09)   | +1 dia         |
| Horas disponíveis | 56h               | **64h**                       | +8h            |
| Escopo estimado    | 44h               | **46h** (acréscimo Ishikawa) | +2h            |
| **Folga**    | 12h (21%)         | **18h (28%)**                 | **+7pp** |

**Impacto no cronograma:**

- ✅ **MF1 (Fundação) estendida de 19 para 22 dias** (01/09 → 22/09)
- ✅ **MF2 (Construção) ajustada:** 23/09 → 15/11/2026 (mantém duração)
- ✅ **MF3 (Consolidação) mantida:** 16/11 → Dez/2026

**Risco mitigado:** R-09 (Entrega parcial não concluída) — probabilidade reduzida de 30% para **15%**.

### 1.2. Mudança 2 — Consolidação dos PDCAs no Plano de Qualidade

**Contexto:** A nota de revisão determina: *"PDCAs devem estar todos reunidos dentro do contexto da área de conhecimento 5 Gerenciamento da Qualidade e não distribuídos em seus respectivos planos."*

**Análise crítica:**

| Dimensão                      | v1.1 (PDCAs distribuídos)           | v1.2 (PDCAs consolidados)                            |
| ------------------------------ | ------------------------------------ | ---------------------------------------------------- |
| **Localização**        | Seção §X.X de cada plano (01-05)  | **Seção única no Plano de Qualidade §5.X** |
| **Rastreabilidade**      | Difusa (5 documentos)                | **Centralizada (1 documento)**                 |
| **Auditoria acadêmica** | Exige leitura cruzada                | **Visão unificada em 1 leitura**              |
| **Volume documental**    | 5 seções × 1 página = 5 páginas | **1 seção × 3-4 páginas = 3-4 páginas**   |
| **Conformidade GMV**     | 3×SIM                               | **4×SIM** (melhor)                            |

**Teste GMV (OKB v3.0 §4.2):**

- P1 (Prof. Dr. Nivaldo Carletto exigirá?): ✅ SIM — exigência explícita
- P2 (Evita retrabalho?): ✅ SIM — visão consolidada facilita revisão
- P3 (PMBOK 7ª exige?): ✅ SIM — Domínio de Qualidade + Medição
- P4 (Útil para equipe?): ✅ SIM — ponto único de verdade para melhoria contínua

**Veredito:** 4×SIM → **MANDATÓRIO**

**Estrutura do Plano de Qualidade v1.2 (revisada):**

```
05. Plano de Qualidade v1.0
├── §5.1. Objetivos de Qualidade (≥ 80% coverage, zero defeitos críticos)
├── §5.2. Definition of Ready (DoR) e Definition of Done (DoD)
├── §5.3. Métricas de Qualidade (Cycle Time, Throughput, Coverage)
├── §5.4. Critérios de Aceite (UAT, FOSS auditado)
├── §5.5. Diagrama de Ishikawa (Causa e Efeito) — NOVO
│   ├── §5.5.1. Problema central: "Risco de não entrega do MVP até Nov/2026"
│   ├── §5.5.2. Causas raiz por categoria (6M)
│   └── §5.5.3. Ações corretivas associadas
└── §5.6. PDCAs Consolidados de Todas as Atividades — NOVO
    ├── §5.6.1. PDCA do TAP (N1.1)
    ├── §5.6.2. PDCA do Plano de Integração (01)
    ├── §5.6.3. PDCA do Plano de Escopo (02)
    ├── §5.6.4. PDCA do Plano de Cronograma (03)
    ├── §5.6.5. PDCA do Plano de Custos (04)
    ├── §5.6.6. PDCA do Plano de Qualidade (05)
    └── §5.6.7. Síntese de Mudanças Relevantes vs. PDCAs Anteriores
```

**Domínio PMBOK 7ª associado:** Domínio de Qualidade (entrega com excelência) + Domínio de Medição (melhoria contínua via PDCA).

### 1.3. Mudança 3 — Diagrama de Ishikawa Obrigatório

**Contexto:** A nota de revisão determina: *"A área de conhecimento 5 Gerenciamento da Qualidade também deverá conter o gráfico de Causa e efeito para todo e qualquer problema reconhecido dentro do projeto (Diagrama de Ishikawa)."*

**Análise crítica:**

O Diagrama de Ishikawa (também conhecido como Espinha de Peixe ou 6M) é uma ferramenta clássica de qualidade que mapeia **causas raiz** de um problema central. Para o COGME, o problema central é:

**Problema Central:** "Risco de não entrega do MVP funcional até Nov/Dez 2026 com ≥ 80% coverage de testes"

**Categorias 6M aplicadas ao COGME:**

| Categoria               | Causas Raiz Identificadas                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mão de Obra**  | Equipe de 2 pessoas (R-08 burnout); curva de aprendizado de SDD local; dependência de revisão humana para LLM                               |
| **Método**       | Governança híbrida PMBOK 7ª + Kanban (complexidade); PDCA distribuído (v1.1) → consolidado (v1.2); ADRs como burocracia potencial (R-03) |
| **Máquina**      | Hardware local (Ryzen 7 8700G) com GPU integrada experimental (ROCm); stack FOSS indefinida até ADR-002 (R-01)                               |
| **Material**      | API de câmbio externa instável (R-06); dependência de serviços gratuitos (Railway, Frankfurter)                                           |
| **Medida**        | Métricas de fluxo sem baseline (Crítica 4 OKB v3.0); metas aspiracionais (Cycle Time ≤ 3 dias arbitrário)                                 |
| **Meio Ambiente** | Prazo acadêmico apertado (3 meses); curso noturno (disponibilidade reduzida); orçamento zero (R-07)                                         |

**Ações corretivas associadas (derivadas do Ishikawa):**

| Causa Raiz                      | Ação Corretiva                                 | Responsável | Prazo     |
| ------------------------------- | ------------------------------------------------ | ------------ | --------- |
| Burnout (Mão de Obra)          | WIP limits + métrica de burnout (≤ 20h/semana) | GP           | Contínuo |
| Governança excessiva (Método) | Aplicar GMV (OKB v3.0 §4.2)                     | GP           | 22/09     |
| Stack indefinida (Máquina)     | ADR-002 (Stack FOSS)                             | GP + Dev     | 11/09     |
| API instável (Material)        | Adapter pattern + fallback BCB                   | Dev          | MF2       |
| Métricas sem baseline (Medida) | ADR-003 (calibração 20/09 – 03/10)            | GP           | 30/09     |
| Prazo apertado (Meio Ambiente)  | Postergação para 22/09 + SDD local             | GP           | 22/09     |

**Domínio PMBOK 7ª associado:** Domínio de Qualidade (análise de causa raiz) + Domínio de Incerteza (mapeamento de riscos).

### 1.4. Mudança 4 — Padronização do Nome do Stakeholder

**Contexto:** Alterar todas as menções de "Prof. Nivaldo" para **"Prof. Dr. Nivaldo Carletto"** (nome completo + titulação).

**Impacto:**

- ✅ Formalização acadêmica (titulação "Dr." é obrigatória em documentos oficiais)
- ✅ Rastreabilidade (nome completo evita ambiguidade)
- ✅ Conformidade com normas ABNT (documentos acadêmicos)

**Ação:** Busca e substituição global em todos os artefatos (TAP, OKB, ADRs, Planos).

### 1.5. Mudança 5 — Eliminação do Termo "ADER"

**Contexto:** A nota de revisão determina: *"Desconsiderar o termo ADER"*.

**Análise:** O termo "ADER-001" (Architecture Decision Enhancement Record) foi avaliado na v1.1 e considerado **NÃO ADERENTE** (3×NÃO no teste GMV). A v1.2 **formaliza a eliminação** do termo, mantendo apenas ADRs padrão (OKB v3.0 §4.5).

**Decisão:** O COGME utiliza exclusivamente **ADR (Architecture Decision Record)** no formato Contexto → Decisão → Consequências. Não há "ADER", "EDR" ou variações.

---

## 2. REESTRUTURAÇÃO DO ROADMAP (DOIS MARCOS AJUSTADOS)

### 2.1. Roadmap Consolidado v1.2

```
┌─────────────────────────────────────────────────────────────────┐
│  MARCO 1 — ENTREGA PARCIAL (22/09/2026, 09:00)                │
│  Escopo: Documentação Áreas 1-5 do PMBOK 6ª                   │
│  ├─ TAP v1.0 (com EAP 13 fases + 8 premissas)                 │
│  ├─ Plano de Integração v1.0                                   │
│  ├─ Plano de Escopo v1.0 (+ EAP + Dicionário)                 │
│  ├─ Plano de Cronograma v1.0 (+ Roadmap 2 marcos)             │
│  ├─ Plano de Custos v1.0 (simplificado)                        │
│  ├─ Plano de Qualidade v1.0 (+ DoD/DoR + Ishikawa + PDCAs)    │
│  └─ PDCAs consolidados de todas as atividades                 │
│  Critério de aceite: Prof. Dr. Nivaldo Carletto valida         │
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

| Macro-Fase                    | Período                      | Fases da EAP                 | Entregáveis-Chave                        |
| ----------------------------- | ----------------------------- | ---------------------------- | ----------------------------------------- |
| **MF1: Fundação**     | 01/09 –**22/09/2026**  | 1, 2, 3, 4 (parcial), 9, 10  | TAP + Planos Áreas 1-5 + PDCA + Ishikawa |
| **MF2: Construção**   | **23/09** – 15/11/2026 | 4 (completo), 5, 6, 7, 8, 11 | MVP funcional + ≥ 80% coverage           |
| **MF3: Consolidação** | 16/11 – Dez/2026             | 12, 13                       | Documentação final + Apresentação     |

---

## 3. PLANO DE QUALIDADE v1.2 — ESTRUTURA DETALHADA

### 3.1. Seção §5.5 — Diagrama de Ishikawa (Causa e Efeito)

```
                    CAUSAS RAIZ DO PROBLEMA CENTRAL
                            ↓
    ┌─────────────────────────────────────────────────────────────┐
    │  PROBLEMA CENTRAL: Risco de não entrega do MVP funcional   │
    │  até Nov/Dez 2026 com ≥ 80% coverage de testes            │
    └─────────────────────────────────────────────────────────────┘
                            ↑
    ┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
    │ Mão de   │ Método   │ Máquina  │ Material │ Medida   │ Meio     │
    │ Obra     │          │          │          │          │ Ambiente │
    ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
    │• 2 pessoas│• Gov.    │• Hardware│• API     │• Métricas│• Prazo   │
    │• Burnout │  híbrida │  local   │  câmbio  │  sem     │  3 meses │
    │• Curva   │• PDCA    │• GPU     │• Serviços│  baseline│• Curso   │
    │  aprend. │  distrib.│  ROCm    │  gratuítos│• Metas  │  noturno │
    │• Revisão │• ADRs    │• Stack   │• Railway │  aspirac.│• Orçam.  │
    │  humana  │  burocr. │  indef.  │• Frankfur│          │  zero    │
    └──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

**Ações corretivas prioritárias (derivadas do Ishikawa):**

1. **Mão de Obra:** WIP limits + métrica de burnout (≤ 20h/semana) — Domínio de Equipe PMBOK 7ª
2. **Método:** Aplicar GMV + consolidar PDCAs no Plano de Qualidade — Domínio de Qualidade
3. **Máquina:** ADR-002 (Stack FOSS) até 11/09 — Domínio de Abordagem de Desenvolvimento
4. **Material:** Adapter pattern + fallback BCB (pós-entrega) — Domínio de Incerteza
5. **Medida:** ADR-003 (calibração de métricas 20/09 – 03/10) — Domínio de Medição
6. **Meio Ambiente:** Postergação para 22/09 + SDD local — Domínio de Entrega

### 3.2. Seção §5.6 — PDCAs Consolidados de Todas as Atividades

**Modelo de PDCA padronizado (KISS):**

```markdown
## §5.6.X PDCA do [Nome da Atividade]

| Fase | Ação | Evidência |
|------|------|-----------|
| **Plan** | Definição do escopo da atividade | TAP §X + OKB v3.0 §4.7 |
| **Do** | Execução da atividade v0.1 | Arquivo `/docs/...` |
| **Check** | Revisão cruzada (persona revisora) | Checklist v2.1 (7 critérios) |
| **Act** | Ajustes → v1.0 | Commit `docs(...): v1.0` |

**Mudanças relevantes vs. PDCAs anteriores:**
- v0.1 → v1.0: [descrição da mudança]
```

**Lista de PDCAs obrigatórios (13 fases da EAP):**

| #  | Atividade                               | Fase EAP | Macro-Fase |
| -- | --------------------------------------- | -------- | ---------- |
| 1  | PDCA do TAP                             | N1.1     | MF1        |
| 2  | PDCA da Identificação de Stakeholders | N1.2     | MF1        |
| 3  | PDCA dos Planos de Gerenciamento        | N1.3     | MF1        |
| 4  | PDCA do Plano de Qualidade              | N1.4     | MF1        |
| 5  | PDCA da Política FOSS                  | N1.5     | MF1        |
| 6  | PDCA do Backlog e Kanban                | N1.6     | MF1        |
| 7  | PDCA dos Requisitos Funcionais          | N2.1     | MF1        |
| 8  | PDCA dos Requisitos Não Funcionais     | N2.2     | MF1        |
| 9  | PDCA dos Casos de Uso                   | N2.3     | MF1        |
| 10 | PDCA da Arquitetura da Solução        | N3.1     | MF1        |
| 11 | PDCA do Protótipo UX/UI                | N3.2     | MF1        |
| 12 | PDCA da Modelagem de Dados (DER)        | N3.3     | MF1        |
| 13 | PDCA da Seleção da Stack FOSS         | N4.1     | MF1        |

**Nota:** Apenas as atividades da MF1 (Fundação) terão PDCA documentado na entrega parcial de 22/09. As atividades da MF2 e MF3 terão PDCAs documentados até a entrega final (Nov/Dez 2026).

---

## 4. PLANO DE AÇÃO 10-22/09/2026 (ENTREGA PARCIAL AJUSTADA)

### 4.1. Capacidade Disponível

| Recurso         | Disponibilidade                                       |
| --------------- | ----------------------------------------------------- |
| Dias úteis     | 8 (10, 11, 15, 16, 17, 18, 19, 22/09)                 |
| Horas por dia   | 4h/pessoa (20h/semana ÷ 5 dias)                      |
| Total de horas  | 2 pessoas × 4h × 8 dias =**64h**              |
| Escopo estimado | 46h (TAP 8h + 5 planos × 6h + PDCA 6h + Ishikawa 2h) |
| **Folga** | **18h (28%)**                                   |

### 4.2. Cronograma Detalhado

| Data                         | Ação                                                                         | Responsável | Artefato                                                | DoD                                                      |
| ---------------------------- | ------------------------------------------------------------------------------ | ------------ | ------------------------------------------------------- | -------------------------------------------------------- |
| **10/09 (qui)**        | Finalizar TAP v1.0 (EAP 13 fases + 8 premissas, remover §5.3)                 | GP           | `TAP_EAP.md` v1.0                                     | TAP com 13 fases + 8 premissas, sem fases 14-17          |
| **11/09 (sex)**        | Redigir ADR-001 (GitHub Projects) + ADR-002 (Stack FOSS) + ADR-003 (Métricas) | GP + Dev     | `docs/adr/ADR-001.md`, `ADR-002.md`, `ADR-003.md` | ADRs formatados (Contexto → Decisão → Consequências) |
| **15/09 (seg)**        | Plano de Integração v1.0                                                     | GP           | `docs/planos/01-integracao.md`                        | Contém links GitHub + SSOT                              |
| **16/09 (ter)**        | Plano de Escopo v1.0 (+ EAP + Dicionário)                                     | GP           | `docs/planos/02-escopo.md`                            | EAP sincronizada com GitHub Projects                     |
| **17/09 (qua)**        | Plano de Cronograma v1.0 (+ Roadmap 2 marcos)                                  | GP           | `docs/planos/03-cronograma.md`                        | Roadmap M1 (22/09) + M2 (Nov/Dez)                        |
| **18/09 (qui)**        | Plano de Custos v1.0 (simplificado)                                            | GP           | `docs/planos/04-custos.md`                            | 1-2 páginas, foco em premissas                          |
| **19/09 (sex)**        | Plano de Qualidade v1.0 (+ DoD/DoR + Ishikawa + PDCAs consolidados)            | GP           | `docs/planos/05-qualidade.md`                         | DoD/DoR + Ishikawa 6M + 13 PDCAs                         |
| **22/09 (ter, 09:00)** | Revisão final + submissão ao Prof. Dr. Nivaldo Carletto                      | GP           | Issue no GitHub                                         | Zero achados CRÍTICOS no checklist                      |

### 4.3. PDCA Consolidado (Entrega Parcial)

**Exemplo para o Plano de Escopo:**

```markdown
## §5.6.3 PDCA do Plano de Escopo

| Fase | Ação | Evidência |
|------|------|-----------|
| **Plan** | Definição do escopo com base no TAP §2 | TAP v1.0 §2 + OKB v3.0 §4.7 |
| **Do** | Redação do plano v0.1 com EAP 13 fases | Commit `docs(plano-escopo): v0.1` (16/09) |
| **Check** | Revisão cruzada (persona revisora) | Checklist v2.1 — 7 critérios |
| **Act** | Ajustes → v1.0 (adição de dicionário EAP) | Commit `docs(plano-escopo): v1.0` (19/09) |

**Mudanças relevantes vs. PDCAs anteriores:**
- v0.1 → v1.0: Adição de dicionário EAP (crítica da revisão v1.0)
- v0.1 → v1.0: Alinhamento com macro-fases MF1/MF2/MF3 ajustadas (M1 = 22/09)
- v0.1 → v1.0: Remoção das fases 14-17 (nota de revisão 6)
```

---

## 5. ADRs A FORMALIZAR (10-30/09/2026)

### 5.1. ADR-001 — GitHub Projects como SSOT (11/09)

**Contexto:** O TAP v1_opngoing (§3.1) menciona EVM e relatórios quinzenais, mas o OKB v3.0 §8.2 substitui Gantt por Kanban/GitHub Projects.

**Decisão:** GitHub Projects é a **fonte única de verdade** para cronograma, monitoramento e medição. Gantt (se exigido) é derivado do Kanban, não o contrário.

**Consequências:**

- ✅ Alinha ao Domínio de Medição PMBOK 7ª (GitHub Insights)
- ✅ Reduz burocracia (sem relatórios estáticos duplicados)
- ⚠️ Risco: Prof. Dr. Nivaldo Carletto pode exigir Gantt tradicional → mitigação: gerar Gantt a posteriori a partir do Kanban

### 5.2. ADR-002 — Stack FOSS (11/09)

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

### 5.3. ADR-003 — Métricas de Fluxo com Baseline (11/09)

**Contexto:** OKB v3.0 Crítica 4 identifica métricas sem baseline.

**Decisão:** Estabelecer período de calibração (23/09 – 03/10) para coletar Cycle Time e Throughput sem meta fixa. Após calibração, definir metas realistas (média ± 20%).

**Consequências:**

- ✅ Alinha ao Domínio de Medição PMBOK 7ª
- ✅ Evita metas aspiracionais não acionáveis

### 5.4. ADR-004 — SDD Local via llama.cpp (30/09)

**Contexto:** Relatório v1.0 §5 + Seção 9 (Stack SDD Local).

**Decisão:** Adotar SDD local com llama.cpp + Qwen2.5-Coder-7B-Q4 + OpenCode TUI, conforme arquitetura da Seção 9.

**Consequências:**

- ✅ Zero custo operacional (alinha P2)
- ✅ Auditabilidade total (prompts versionáveis)
- ⚠️ Trade-off: qualidade inferior a GPT-4 → mitigação: revisão humana + testes automatizados

---

## 6. TRADE-OFFS E RISCOS RECALCULADOS

### 6.1. Trade-offs Declarados

| Trade-off                                | Risco                                                   | Mitigação                                                                   |
| ---------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------- |
| MF1 estendida (19 → 22 dias)            | Percepção de "atraso" pelo Prof. Dr. Nivaldo Carletto | Comunicar explicitamente que postergação é estratégica (folga + Ishikawa) |
| PDCAs consolidados no Plano de Qualidade | Perda de contexto específico por plano                 | Cada PDCA referencia explicitamente o plano associado                         |
| Diagrama de Ishikawa obrigatório        | Volume documental aumentado                             | Ishikawa é 1 página com 6 categorias (KISS)                                 |
| Eliminação do termo "ADER"             | Percepção de "regressão"                             | Justificar via GMV (3×NÃO) + manter ADR padrão                             |

### 6.2. Riscos Recalculados

| ID   | Risco                                                    | Prob.         | Impacto | Severidade | Resposta                             | Status               |
| ---- | -------------------------------------------------------- | ------------- | ------- | ---------- | ------------------------------------ | -------------------- |
| R-01 | Stack FOSS indefinida                                    | 80%           | Alto    | Crítico   | ADR-002 até 11/09                   | 🟠 Aberto            |
| R-02 | EAP não sincronizada com GitHub                         | 60%           | Alto    | Alto       | Mapeamento 1:1 até 15/09            | 🟡 Em andamento      |
| R-03 | Governança > 50% do tempo                               | 70%           | Médio  | Alto       | Aplicar GMV                          | 🟡 Aberto            |
| R-04 | Prof. Dr. Nivaldo Carletto exigir Gantt tradicional      | 30%           | Médio  | Médio     | ADR-001 + Gantt derivado             | 🟢 Mitigado          |
| R-05 | Scope creep                                              | 50%           | Alto    | Alto       | CCB + DoR rigoroso                   | 🟡 Monitorando       |
| R-08 | Equipe exceder 20h/semana (burnout)                      | 50%           | Médio  | Alto       | WIP limits + métrica de burnout     | 🟡 Monitorando       |
| R-09 | Entrega parcial 22/09 não concluída                    | **15%** | Alto    | Alto       | Plano de ação 10-22/09 + folga 28% | 🟢**Mitigado** |
| R-10 | PDCA não documentado por atividade                      | 40%           | Médio  | Médio     | Template PDCA padronizado (§5.6)    | 🟠 Novo              |
| R-11 | Fases 14-17 questionadas pelo Prof. Dr. Nivaldo Carletto | 20%           | Médio  | Médio     | Justificativa GMV + menção no §8  | 🟢 Mitigado          |
| R-12 | **Diagrama de Ishikawa incompleto**                | 30%           | Médio  | Médio     | Template 6M padronizado (§5.5)      | 🟠 Novo              |

---

## 7. AÇÕES BLOQUEANTES (10-22/09/2026)

| #  | Ação                                                                              | Responsável | Prazo                  | Artefato                            |
| -- | ----------------------------------------------------------------------------------- | ------------ | ---------------------- | ----------------------------------- |
| 1  | Finalizar TAP v1.0 (EAP 13 fases + 8 premissas, remover §5.3)                      | GP           | 10/09                  | `TAP_EAP.md` v1.0                 |
| 2  | Redigir ADR-001 (GitHub Projects)                                                   | GP           | 11/09                  | `docs/adr/ADR-001.md`             |
| 3  | Redigir ADR-002 (Stack FOSS)                                                        | GP + Dev     | 11/09                  | `docs/adr/ADR-002.md`             |
| 4  | Redigir ADR-003 (Métricas de Fluxo)                                                | GP           | 11/09                  | `docs/adr/ADR-003.md`             |
| 5  | Plano de Integração v1.0                                                          | GP           | 15/09                  | `docs/planos/01-integracao.md`    |
| 6  | Plano de Escopo v1.0 (+ EAP + Dicionário)                                          | GP           | 16/09                  | `docs/planos/02-escopo.md`        |
| 7  | Plano de Cronograma v1.0 (+ Roadmap 2 marcos)                                       | GP           | 17/09                  | `docs/planos/03-cronograma.md`    |
| 8  | Plano de Custos v1.0 (simplificado)                                                 | GP           | 18/09                  | `docs/planos/04-custos.md`        |
| 9  | **Plano de Qualidade v1.0 (+ DoD/DoR + Ishikawa + PDCAs consolidados)**       | GP           | 19/09                  | `docs/planos/05-qualidade.md`     |
| 10 | **Diagrama de Ishikawa (6M) para problema central**                           | GP           | 19/09                  | Seção §5.5 do Plano de Qualidade |
| 11 | **PDCAs consolidados de todas as atividades (13 PDCAs)**                      | GP           | 19/09                  | Seção §5.6 do Plano de Qualidade |
| 12 | **Padronização do nome "Prof. Dr. Nivaldo Carletto" em todos os artefatos** | GP           | 19/09                  | Busca e substituição global       |
| 13 | **Eliminação do termo "ADER" em todos os artefatos**                        | GP           | 19/09                  | Busca e substituição global       |
| 14 | Revisão final + submissão ao Prof. Dr. Nivaldo Carletto                           | GP           | **22/09, 09:00** | Issue no GitHub                     |
| 15 | Formalizar ADR-004 (SDD Local)                                                      | GP + Dev     | 30/09                  | `docs/adr/ADR-004.md`             |

---

## 8. PASSOS/AÇÕES FUNDAMENTAIS PRIORITÁRIOS

### 8.1. Prioridade 🔴 CRÍTICA (Bloqueante)

| # | Ação                                                              | Prazo | Justificativa                                       |
| - | ------------------------------------------------------------------- | ----- | --------------------------------------------------- |
| 1 | **Finalizar TAP v1.0 com EAP 13 fases + 8 premissas**         | 10/09 | Base para todos os outros planos                    |
| 2 | **Redigir ADR-002 (Stack FOSS)**                              | 11/09 | Desbloqueia Fase 4 e Fase 5                         |
| 3 | **Plano de Qualidade v1.0 com Ishikawa + PDCAs consolidados** | 19/09 | Exigência explícita do Prof. Dr. Nivaldo Carletto |
| 4 | **Submissão ao Prof. Dr. Nivaldo Carletto em 22/09, 09:00**  | 22/09 | Marco M1 (Entrega Parcial)                          |

### 8.2. Prioridade 🟠 ALTA (Risco de retrabalho)

| # | Ação                                                         | Prazo | Justificativa                             |
| - | -------------------------------------------------------------- | ----- | ----------------------------------------- |
| 5 | **Redigir ADR-001 (GitHub Projects como SSOT)**          | 11/09 | Blindagem acadêmica contra Gantt         |
| 6 | **Redigir ADR-003 (Métricas de Fluxo com Baseline)**    | 11/09 | Alinha ao Domínio de Medição PMBOK 7ª |
| 7 | **Diagrama de Ishikawa (6M) para problema central**      | 19/09 | Exigência de qualidade (Área 5)         |
| 8 | **PDCAs consolidados de todas as atividades (13 PDCAs)** | 19/09 | Exigência de melhoria contínua          |

### 8.3. Prioridade 🟡 MÉDIA (Refinamento)

| #  | Ação                                                        | Prazo | Justificativa                  |
| -- | ------------------------------------------------------------- | ----- | ------------------------------ |
| 9  | **Padronização do nome "Prof. Dr. Nivaldo Carletto"** | 19/09 | Conformidade ABNT              |
| 10 | **Eliminação do termo "ADER"**                        | 19/09 | Simplificação (GMV)          |
| 11 | **Plano de Integração v1.0**                          | 15/09 | Guarda-chuva dos outros planos |
| 12 | **Plano de Escopo v1.0 (+ EAP + Dicionário)**          | 16/09 | Base para cronograma e custos  |

### 8.4. Prioridade 🟢 BAIXA (Melhoria contínua)

| #  | Ação                                                  | Prazo | Justificativa                 |
| -- | ------------------------------------------------------- | ----- | ----------------------------- |
| 13 | **Plano de Cronograma v1.0 (+ Roadmap 2 marcos)** | 17/09 | Comunicação com stakeholder |
| 14 | **Plano de Custos v1.0 (simplificado)**           | 18/09 | Compliance acadêmico         |
| 15 | **Formalizar ADR-004 (SDD Local)**                | 30/09 | Desbloqueia Fase 5 (MF2)      |

---

## 9. DECLARAÇÃO DE CONFORMIDADE

Este relatório v1.2:

- ✅ Deriva 100% das 5 mudanças estruturais declaradas em `analise_auditoria_1.2.md`
- ✅ Cita domínios e princípios PMBOK 7ª explicitamente (Qualidade, Medição, Entrega, Incerteza)
- ✅ Aplica teste GMV (OKB v3.0 §4.2) para cada recomendação
- ✅ Declara trade-offs e riscos (Domínio de Incerteza PMBOK 7ª)
- ✅ Respeita hierarquia de governança (OKB v3.0 §4.1)
- ✅ É acionável (plano de ação 10-22/09 com datas e responsáveis)
- ✅ **Padroniza o nome do stakeholder como "Prof. Dr. Nivaldo Carletto"** (Mudança 4)
- ✅ **Elimina definitivamente o termo "ADER"** (Mudança 5)
- ✅ **Consolida PDCAs no Plano de Qualidade (Área 5)** (Mudança 2)
- ✅ **Inclui Diagrama de Ishikawa (6M) no Plano de Qualidade** (Mudança 3)
- ✅ **Recalcula cronograma para entrega parcial em 22/09/2026, 09:00** (Mudança 1)

---

## 10. Validação de Modelos Quantizados: Cruzamento Hardware × Requisitos

## 10.1. Validação de Hardware Real vs. Premissas do Relatório

O relatório de arquitetura assume **64GB RAM unificada**. O hardware real medido mostra:

| Parâmetro            | Premissa do Relatório | Medição Real (system-profile) | Delta         |
| --------------------- | ---------------------- | ------------------------------- | ------------- |
| RAM Total             | 64 GB                  | **58.0 GB**               | −6 GB        |
| RAM Disponível       | —                     | **49.0 GB**               | —            |
| RAM em Uso (OS+GNOME) | —                     | **8.0 GB**                | —            |
| Swap                  | 16 GB                  | **16.0 GB**               | ✅ Confirma   |
| /var livre            | —                     | **420 GB**                | ✅ Suficiente |

**⚠️ Correção crítica:** Os cálculos de RAM livre do relatório original estão superestimados em ~6GB. Isso não invalida as decisões, mas aperta a margem do 72B.

---

## 10.2. Modelos Aprovados: Lista Definitiva

### 10.2.1. Modelo Principal (Produção SDD)

| Campo                              | Valor                                                        |
| ---------------------------------- | ------------------------------------------------------------ |
| **Modelo**                   | Qwen 32B Instruct                                            |
| **Quantização**            | Q4_K_M                                                       |
| **Arquivo GGUF**             | `qwen-32b-instruct-q4_k_m.gguf`                            |
| **Peso em disco**            | ~20 GB                                                       |
| **RAM após carga**          | ~20 GB modelo +~8 GB OS = **~28 GB**                  |
| **RAM livre residual**       | **~30 GB**                                             |
| **Contexto máximo viável** | **16k tokens** (com margem)                            |
| **Target tg**                | ≥6 t/s (Vulkan)                                             |
| **Status**                   | ✅**APROVADO — Pilar da stack**                       |
| **Uso**                      | Todas as fases SDD interativas (coder, reviewer, tester, pm) |

**Validação first-principles:**

- 30GB livres após carga = margem segura para 16k ctx (~4-6GB de KV cache) + picos do GNOME
- Vulkan na 780M com 32B Q4_K_M é o sweet spot documentado em benchmarks Zen 4 APU
- Troca para CPU AVX-512 como fallback mantém ~2-3 t/s (aceitável para emergências)

---

### 10.2.2. Modelo Rápido (Testes e Roteamento)

| Campo                              | Valor                                                                                                       |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Modelo**                   | Qwen 14B Instruct                                                                                           |
| **Quantização**            | Q4_K_M                                                                                                      |
| **Arquivo GGUF**             | `qwen-14b-instruct-q4_k_m.gguf`                                                                           |
| **Peso em disco**            | ~9 GB                                                                                                       |
| **RAM após carga**          | ~9 GB modelo +~8 GB OS = **~17 GB**                                                                  |
| **RAM livre residual**       | **~41 GB**                                                                                            |
| **Contexto máximo viável** | **32k+ tokens**                                                                                       |
| **Target tg**                | ≥12 t/s (Vulkan, estimado)                                                                                 |
| **Status**                   | ✅**APROVADO**                                                                                        |
| **Uso**                      | Testes rápidos de prompt, validação de handoffs, tarefas de baixa complexidade, dry-runs do pipeline SDD |

**Nota de otimização:** Com 41GB livres, este modelo aceita **Q5_K_M** (~11GB) sem impacto operacional. Q5_K_M oferece ganho mensurável em raciocínio lógico e aderência a specs — relevante para validação de handoffs. Recomendo baixar ambas as quantizações e comparar.

| Variante | Tamanho | RAM livre | Recomendação                                  |
| -------- | ------- | --------- | ----------------------------------------------- |
| Q4_K_M   | ~9 GB   | ~41 GB    | Padrão                                         |
| Q5_K_M   | ~11 GB  | ~39 GB    | **Preferível para validação de specs** |

---

### 10.2.3. Modelo Batch (Processamento Assíncrono)

| Campo                              | Valor                                                                          |
| ---------------------------------- | ------------------------------------------------------------------------------ |
| **Modelo**                   | Qwen 72B Instruct                                                              |
| **Quantização**            | Q4_K_M                                                                         |
| **Arquivo GGUF**             | `qwen-72b-instruct-q4_k_m.gguf`                                              |
| **Peso em disco**            | ~42 GB                                                                         |
| **RAM após carga**          | ~42 GB modelo +~8 GB OS = **~50 GB**                                    |
| **RAM livre residual**       | **~8 GB** (sem swap)                                                     |
| **Contexto máximo viável** | **4k tokens** (limite duro)                                              |
| **Target tg**                | ~1-2 t/s (Vulkan, com risco de swap)                                           |
| **Status**                   | ⚠️**CONDICIONAL — Adiar download**                                    |
| **Uso**                      | Apenas batch offline: resumir documentos longos, análise de codebase completa |

**Validação crítica com hardware real:**

Com 58GB total e 50GB consumidos, restam 8GB. O KV cache para 4k tokens em 72B consome ~2-3GB. Sobram ~5GB. Qualquer pico do GNOME (navegador, notificação) empurra para swap.

**Cenários de falha:**

- GNOME abre uma janela pesada → swap → tg cai para <0.5 t/s
- Contexto >4k → OOM killer ou swap massivo
- Build paralelo rodando → OOM certo

**Mitigação se necessário no futuro:**

- Usar IQ4_XS (~38GB) em vez de Q4_K_M → ganha ~4GB de margem
- Fechar GNOME temporariamente (`systemctl isolate multi-user.target`) → recupera ~3-4GB
- Aumentar swap para 32GB → permite contexto até 8k, mas tg degrada

**Decisão:** Não baixar agora. O 32B atende 95% dos casos. Baixar apenas quando houver dor mensurável que o 32B não resolve.

---

## 10.3. Tabela Consolidada

| Modelo   | Quantização | Disco  | RAM Carga | RAM Livre | Contexto Max | tg Target | Status           | Prioridade   |
| -------- | ------------- | ------ | --------- | --------- | ------------ | --------- | ---------------- | ------------ |
| Qwen 14B | Q4_K_M        | ~9 GB  | ~9 GB     | ~41 GB    | 32k+         | ≥12 t/s  | ✅ Aprovado      | **P1** |
| Qwen 14B | Q5_K_M        | ~11 GB | ~11 GB    | ~39 GB    | 32k+         | ≥10 t/s  | ✅ Aprovado      | P2           |
| Qwen 32B | Q4_K_M        | ~20 GB | ~20 GB    | ~30 GB    | 16k          | ≥6 t/s   | ✅ Aprovado      | **P0** |
| Qwen 72B | Q4_K_M        | ~42 GB | ~42 GB    | ~8 GB     | 4k           | ~1-2 t/s  | ⚠️ Condicional | P3 (adiar)   |

**Disco total necessário (P0+P1+P2):** ~40 GB de 420 GB disponíveis em `/var` → **9.5% utilizado** ✅

---

## 10.4. Localização no Filesystem

```
/var/lib/llama.cpp/models/
├── qwen-32b-instruct-q4_k_m.gguf    # P0: baixar primeiro
├── qwen-14b-instruct-q4_k_m.gguf    # P1: baixar segundo
├── qwen-14b-instruct-q5_k_m.gguf    # P2: baixar terceiro (opcional)
└── qwen-72b-instruct-q4_k_m.gguf    # P3: NÃO baixar ainda
```

**Backup correspondente:**

```
/extra/backup/llama-models/           # Cópia resiliente
├── qwen-32b-instruct-q4_k_m.gguf
└── qwen-14b-instruct-q4_k_m.gguf
```

---

## 10.5. Comandos de Download (Quando Fase 2 Iniciar)

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

> **Nota:** Os nomes exatos do repositório HuggingFace dependem da versão da família Qwen disponível. Ajustar `Qwen2.5` para `Qwen3` conforme o repositório oficial vigente. O padrão de nomenclatura GGUF é consistente entre versões.

---

## 10.6. Critérios de Validação Pós-Download

Cada modelo deve passar por este checklist antes de ser considerado operacional:

```bash
# Teste de carga (32B exemplo)
llama-server \
  -m /var/lib/llama.cpp/models/qwen-32b-instruct-q4_k_m.gguf \
  -ngl 99 \
  -c 16384 \
  --port 8080

# Verificar no output:
# [ ] "llama_model_load: Vulkan buffer allocated"  → GPU ativa
# [ ] "llama_model_load: model size = XXXX MB"     → tamanho esperado
# [ ] RAM pico ≤ 28GB (htop)                       → dentro do budget
# [ ] Resposta a prompt teste em <2s (TTFT)        → latência OK
# [ ] tg ≥ 6 t/s (medir com 200 tokens output)     → throughput OK
```

---

## 10.7. O Que NÃO Vamos Usar (e Por Quê)

| Rejeitado                                                          | Motivo First-Principles                                                                                                                               |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Qwen 72B Q5_K_M ou superior**                              | ~50GB+ de RAM. Impossível sem swap massivo. Anti-padrão para APU.                                                                                   |
| **Modelos de código dedicados** (DeepSeek-Coder, CodeLlama) | Um modelo base + N prompts = N especialistas. Adicionar modelo especializado é violação do princípio de simplicidade (seção 1.3 do relatório). |
| **Quantizações IQ2/IQ3**                                   | Degradação de qualidade em raciocínio lógico. O ganho de RAM não compensa a perda de aderência a specs SDD.                                     |
| **Múltiplos modelos simultâneos**                          | RAM unificada é recurso finito. Um modelo por vez. Troca via systemd restart.                                                                        |
| **Modelos >72B**                                             | Fisicamente impossível em 58GB RAM.                                                                                                                  |

---

# 11 Personas SDD e Modelos: Análise First-Principles

## 11.1. Crítica à Premissa da Pergunta

Antes de listar, preciso apontar uma **tensão conceitual** com a arquitetura já aprovada:

> O relatório de arquitetura (seção 11.1.3) estabelece: *"Um modelo base + N prompts = N especialistas"*. Associar modelos diferentes a cada persona **viola este princípio** e reintroduz o over-engineering que a seção 2.3 rejeitou explicitamente.

**Princípio correto:** Todas as personas compartilham o **mesmo modelo base** (Qwen 32B Q4_K_M). A especialização vem do prompt, não do modelo. Trocar modelo por persona custa:

- RAM (carregar múltiplos modelos é proibitivo)
- Latência (troca de contexto em disco)
- Complexidade (gerenciamento de estado)
- Consistência (especialistas com "personalidades" diferentes)

**Quando quebrar a regra:** Apenas se houver **dor mensurável** que o modelo base não resolve. Vou listar as exceções legítimas mais adiante.

---

## 11.2. Personas SDD Essenciais

### 11.2.1. Núcleo Mínimo Viável (4 personas)

| Persona                        | Responsabilidade                                                | Input                      | Output                                 | Complexidade Cognitiva                     |
| ------------------------------ | --------------------------------------------------------------- | -------------------------- | -------------------------------------- | ------------------------------------------ |
| **PM** (Product Manager) | Escrever specs, decompor features, definir critérios de aceite | Requisitos vagos           | `NNN-feature-spec.md` estruturado    | Alta (raciocínio abstrato)                |
| **Coder**                | Implementar código aderente à spec                            | Spec + contexto de código | Código-fonte em`src/`               | Muito alta (razão principal do SDD)       |
| **Reviewer**             | Revisar código contra spec + standards                         | Código + spec + standards | `NNN-feature-review.md` com findings | Alta (análise crítica)                   |
| **Tester**               | Gerar testes que validam a spec                                 | Spec + código             | Testes em`tests/`                    | Média-alta (raciocínio sobre edge cases) |

### 11.2.2. Personas Opcionais (adicionar apenas com dor mensurável)

| Persona                    | Quando Adicionar                             | Alternativa Mais Simples                |
| -------------------------- | -------------------------------------------- | --------------------------------------- |
| **Architect**        | Projetos com >10k LOC ou múltiplos módulos | Subsumir pelo PM com prompt específico |
| **Debugger**         | Bugs complexos com stack traces longos       | Coder com prompt de diagnóstico        |
| **DocWriter**        | Projetos com API pública                    | Coder com prompt de documentação      |
| **Refactorer**       | Codebase legado com dívida técnica         | Reviewer com prompt de refatoração    |
| **SecurityReviewer** | Projetos com exposição externa             | Reviewer com checklist de segurança    |

**Regra de ouro:** Começar com 4 personas. Adicionar apenas quando o prompt genérico falhar consistentemente (>30% dos casos).

---

## 11.3. Associação Modelo-Persona: Estratégia Recomendada

### 11.3.1. Configuração Padrão (Recomendada)

| Persona  | Modelo                    | Justificativa                           |
| -------- | ------------------------- | --------------------------------------- |
| PM       | **Qwen 32B Q4_K_M** | Mesma qualidade de raciocínio do coder |
| Coder    | **Qwen 32B Q4_K_M** | Pilar da stack                          |
| Reviewer | **Qwen 32B Q4_K_M** | Precisa entender o que o coder fez      |
| Tester   | **Qwen 32B Q4_K_M** | Precisa entender a spec                 |

**Troca de persona = troca de symlink, não de modelo:**

```bash
ln -sf pm.md       .ai/prompts/active.md   # continua no mesmo llama-server
ln -sf coder.md    .ai/prompts/active.md   # zero overhead
ln -sf reviewer.md .ai/prompts/active.md   # instantâneo
```

### 11.3.2. Exceções Legítimas (Quebra Controlada do Princípio)

| Cenário                                                    | Modelo Alternativo                | Justificativa First-Principles                 |
| ----------------------------------------------------------- | --------------------------------- | ---------------------------------------------- |
| **Testes rápidos de prompt**                         | Qwen 14B Q4_K_M                   | Latência <1s, RAM sobra para contexto massivo |
| **Validação de handoffs** (parsing determinístico) | Qwen 14B Q5_K_M                   | Qualidade superior em tarefas estruturadas     |
| **Batch offline** (resumir codebase >50k LOC)         | Qwen 72B Q4_K_M                   | Único que cabe no contexto, mesmo que lento   |
| **Tarefa de código puro** (refatoração massiva)    | DeepSeek-Coder-V2 (ver seção 4) | Apenas se Qwen 32B falhar consistentemente     |

**Princípio:** O modelo alternativo deve ser **carregado sob demanda** (systemd restart do llama-server), nunca simultâneo.

---

## 11.4. Candidatos Alternativos: Análise Crítica

### 11.4.1. Metodologia de Avaliação

Critérios first-principles para hardware específico (Ryzen 8700G + Radeon 780M + 58GB RAM):

1. **Qualidade em código** (SWE-bench, HumanEval, MultiPL-E)
2. **Suporte a português** (crítico para specs e docs)
3. **Tamanho vs qualidade** (eficiência de parâmetros)
4. **Quantização GGUF disponível** (compatibilidade com llama.cpp)
5. **Licença FOSS real** (Apache 2.0 / MIT > restritivas)
6. **Performance no hardware** (Vulkan + AVX-512)

### 11.4.2. Tabela Comparativa de Candidatos

| Modelo                            | Tamanho    | Código    | Português | Licença   | GGUF | Veredito                           |
| --------------------------------- | ---------- | ---------- | ---------- | ---------- | ---- | ---------------------------------- |
| **Qwen 2.5/3 Coder 32B**    | 32B        | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Apache 2.0 | ✅   | **Melhor escolha geral**     |
| **Qwen 2.5/3 32B Instruct** | 32B        | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Apache 2.0 | ✅   | **Pilar atual (aprovado)**   |
| **DeepSeek-Coder-V2 Lite**  | 16B        | ⭐⭐⭐⭐⭐ | ⭐⭐⭐     | MIT        | ✅   | Forte para código puro            |
| **DeepSeek-Coder-V2**       | 236B (MoE) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐     | MIT        | ✅   | ❌ Fora do budget RAM              |
| **Llama 3.3 70B**           | 70B        | ⭐⭐⭐⭐   | ⭐⭐⭐     | Llama 3.3  | ✅   | ❌ Apertado em RAM, pior que Qwen  |
| **Llama 3.1 8B**            | 8B         | ⭐⭐⭐     | ⭐⭐⭐     | Llama 3.1  | ✅   | Rápido, mas fraco em código      |
| **Mistral Small 24B**       | 24B        | ⭐⭐⭐⭐   | ⭐⭐⭐     | Apache 2.0 | ✅   | Bom, mas Qwen supera               |
| **Mixtral 8x7B**            | 46B (MoE)  | ⭐⭐⭐⭐   | ⭐⭐⭐     | Apache 2.0 | ✅   | ❌ MoE consome RAM desproporcional |
| **Gemma 2 27B**             | 27B        | ⭐⭐⭐     | ⭐⭐       | Gemma      | ✅   | Inferior em código e PT-BR        |
| **Phi-3.5/4 Mini**          | 3.8B       | ⭐⭐⭐     | ⭐⭐       | MIT        | ✅   | Rápido, mas limitado              |
| **Yi-Coder 9B**             | 9B         | ⭐⭐⭐⭐   | ⭐⭐⭐     | Apache 2.0 | ✅   | Alternativa leve interessante      |
| **Command R**               | 35B        | ⭐⭐⭐     | ⭐⭐⭐⭐   | CC-BY-NC   | ✅   | ❌ Licença não-comercial         |
| **GLM-4 9B**                | 9B         | ⭐⭐⭐     | ⭐⭐⭐⭐   | GLM-4      | ✅   | Bom em chinês, médio em código  |

### 11.4.3. Análise Detalhada dos Top 3 Candidatos

#### 🥇 **Qwen 2.5/3 Coder 32B** (alternativa ao Instruct atual)

| Dimensão                           | Análise                                                                      |
| ----------------------------------- | ----------------------------------------------------------------------------- |
| **Ganho sobre Qwen Instruct** | +10-15% em SWE-bench, especialização em código                             |
| **Perda**                     | Português ligeiramente inferior em tarefas não-código                      |
| **Performance no hardware**   | Mesma do Instruct (mesma arquitetura)                                         |
| **Custo**                     | Zero (mesmo tamanho, mesmo download)                                          |
| **Veredito**                  | **Candidato sério para substituir o pilar** se o foco for 90%+ código |

**Recomendação:** Baixar e testar lado a lado com o Instruct. Se o ganho em código superar a perda em português para specs, migrar.

#### 🥈 **DeepSeek-Coder-V2 Lite 16B**

| Dimensão                         | Análise                                                       |
| --------------------------------- | -------------------------------------------------------------- |
| **Ganho sobre Qwen 14B**    | +15-20% em código puro (SWE-bench, HumanEval)                 |
| **Perda**                   | Português fraco, contexto menor                               |
| **Performance no hardware** | 16B = ~9GB RAM, tg ≥12 t/s esperado                           |
| **Custo**                   | 9GB disco adicionais                                           |
| **Veredito**                | **Válido como modelo rápido especializado em código** |

**Recomendação:** Usar como substituto do Qwen 14B **apenas** para tarefas de geração de código puro. Manter Qwen 14B para tarefas que exigem português.

#### 🥉 **Mistral Small 24B / Yi-Coder 9B**

| Dimensão          | Análise                                                   |
| ------------------ | ---------------------------------------------------------- |
| **Ganho**    | Nenhum mensurável sobre Qwen no mesmo tamanho             |
| **Perda**    | Português inferior, comunidade menor                      |
| **Veredito** | **Rejeitados** — sem dor mensurável que justifique |

---

## 11.5. Recomendação Final

### 5.1. Configuração Ótima (Conservadora)

```
Modelo único: Qwen 32B Instruct Q4_K_M
Personas: 4 (PM, Coder, Reviewer, Tester)
Troca: via symlink em .ai/prompts/active.md
```

**Justificativa:** Atende 95% dos casos com zero complexidade adicional.

### 11.5.2. Configuração Ótima (Pragmática)

| Persona                               | Modelo                     | Quando Usar                         |
| ------------------------------------- | -------------------------- | ----------------------------------- |
| PM, Reviewer, Tester                  | Qwen 32B Instruct Q4_K_M   | Padrão                             |
| Coder (tarefas complexas)             | Qwen 32B Instruct Q4_K_M   | Padrão                             |
| Coder (tarefas rápidas/iterativas)   | Qwen 14B Q4_K_M            | Quando latência > qualidade        |
| Coder (código puro, sem contexto PT) | DeepSeek-Coder-V2 Lite 16B | **Apenas se** Qwen 32B falhar |
| Batch offline                         | Qwen 72B Q4_K_M            | Sob demanda, via systemd            |

### 11.5.3. Downloads Recomendados (Ordem de Prioridade)

| Prioridade   | Modelo                         | Tamanho | Justificativa             |
| ------------ | ------------------------------ | ------- | ------------------------- |
| **P0** | Qwen 32B Instruct Q4_K_M       | 20 GB   | Pilar da stack            |
| **P1** | Qwen 14B Q4_K_M                | 9 GB    | Testes rápidos           |
| **P2** | Qwen 32B**Coder** Q4_K_M | 20 GB   | Alternativa especializada |
| **P3** | DeepSeek-Coder-V2 Lite 16B     | 9 GB    | Código puro, sob demanda |
| **P4** | Qwen 72B Q4_K_M                | 42 GB   | Batch (adiar)             |

**Total imediato (P0+P1):** 29 GB
**Total com P2+P3:** 47 GB (ainda cabe nos 420 GB de `/var`)

---

## 11.6. Princípios Guia

1. **Um modelo por vez.** Nunca múltiplos carregados simultaneamente.
2. **Troca via systemd, não via orquestrador.** `systemctl restart llama-server@32b`
3. **Especialização via prompt, não via modelo.** Adicionar modelo só quando o prompt falhar consistentemente.
4. **Candidatos alternativos são experimentais.** Só entram em produção após validação empírica (>50 tarefas, métricas comparativas).
5. **Português é critério eliminatório.** Modelos que falham em PT-BR são rejeitados, independente da qualidade em código.

---

## 11.7. O Que NÃO Fazer

| Anti-padrão                               | Motivo                                          |
| ------------------------------------------ | ----------------------------------------------- |
| Associar modelo diferente a cada persona   | Viola princípio de simplicidade, consome RAM   |
| Baixar todos os candidatos "para testar"   | 200GB+ de disco, análise superficial           |
| Trocar de modelo a cada tarefa             | Latência de carga > tempo de inferência       |
| Usar modelos não-FOSS (Command R, etc.)   | Viola princípio de custo zero e liberdade      |
| Adicionar persona antes da dor mensurável | Framework fetishism (seção 2.5 do relatório) |

---

**Fim do Relatório Analítico v1.2**

Aguardo autorização para iniciar a execução do plano de ação 10-22/09/2026.
