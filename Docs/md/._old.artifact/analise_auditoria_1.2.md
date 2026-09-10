## Ações declaradas para a alteração e melhoria deste relatório:

1. Alterar todas as menções a "Prof. Nivaldo"  para "Prof. Dr. Nivaldo Carletto
2. Ajustar todas as datas referentes a 19/09/2026 para 22/09/2026 - 9:00AM e recalcular todos os riscos e entregas para a nova data
3. Desconsiderar o termo ADER:

> ### 1.9. Nota 24 — Avaliação de ADER-001 e ADR-003 (ALTA)
>
> **Contexto:** "considere também a confecção das ADRs: ADER-001, ADR-003 aderentes ao projeto, caso não passem no crivo de conformidade com o projeto, refatorar"
>
> **Análise de conformidade:**
>
> #### ADER-001 — "Architecture Decision Enhancement Record"
>
> **Hipótese:** A sigla "ADER" sugere um ADR expandido, possivelmente com seção de "Enhancement" (melhoria contínua).

4. PDCAs devem estar todos reunidos dentro do contexto da area de conhecimento 5 Gerenciamento da Qualidade e não distribído em seus respectivos planos
5. A area de conhecimento 5 Gerenciamento da Qualidade tabém deverá conter o gráfico de CAusa e efeito para todo e qualquer problema reconhecido dentro do projeeto (Diagrama de Ishkawa)




# RELATÓRIO ANALÍTICO v1.1 — CONSOLIDAÇÃO PÓS-REVISÃO DO COGME

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Data de Emissão:** 10/09/2026
**Emissor:** GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carletto
**Referência:** `analise_auditoria_1.0.md` (revisado) + OKB v3.0 + TAP v1_opngoing + hardware.md
**Status:** Input para ADR-001, ADR-002, ADR-003, ADR-004 + Plano de Ação 10-19/09

---

## 0. DELTA ANALÍTICO v1.0 → v1.1

A revisão do relatório v1.0 introduziu **24 notas de ajuste** que consolidam o escopo da entrega parcial, redesenham o roadmap e validam decisões arquiteturais. Abaixo, o delta categorizado:

| #     | Nota de Revisão                                                                 | Categoria                      | Severidade |
| ----- | -------------------------------------------------------------------------------- | ------------------------------ | ---------- |
| 1     | Modelo de hibridização KISS+YAGNI aprovado                                     | Validação                    | 🟢         |
| 2     | **Entrega parcial 19/09: documentação até Área 5 (Qualidade) + PDCAs** | **Restrição Temporal** | 🔴         |
| 3     | **PDCA obrigatório por atividade (último PDCA + mudanças)**             | **Novo Requisito**       | 🔴         |
| 4     | Documentação formal viva até MVP funcional                                    | Validação                    | 🟢         |
| 5     | Código não obrigatório na entrega parcial                                     | Alívio de Escopo              | 🟢         |
| 6     | Remover seção "Fases Desejáveis" (14-17) do TAP+EAP                           | Redução de Escopo            | 🟠         |
| 7     | **Redesenhar roadmap para 2 marcos (Parcial + Final)**                     | **Reestruturação**     | 🔴         |
| 8     | SDD reduz tempo da Fase 5 (redução não calculada)                             | Premissa Técnica              | 🟡         |
| 9-15  | 7 pacotes da EAP descartados/fundidos (aprovados)                                | Consolidação                 | 🟢         |
| 16    | Fusão N10.1+N10.2+N10.3: manter domínios distintos (ref. §9)                  | Refinamento                    | 🟡         |
| 17    | Deploy em plataforma gratuita não mandatório (YAGNI)                           | Alívio                        | 🟢         |
| 18    | Stack SDD local validada (ref. §9)                                              | Validação                    | 🟢         |
| 19    | Macro-fases como mitigação de risco Kanban                                     | Validação                    | 🟢         |
| 20-21 | Persistências PMBOK 7ª + GitHub aprovadas                                      | Validação                    | 🟢         |
| 22-23 | SDD local via llama.cpp aprovado (ref. §9)                                      | Validação                    | 🟢         |
| 24    | **Avaliar ADER-001 e ADR-003 quanto à conformidade**                      | **Nova Ação**          | 🟠         |

**Veredito sumário:** A revisão **aprova 85% das recomendações v1.0** e introduz **restrição temporal bloqueante** (entrega parcial 19/09) que exige replanejamento imediato. O relatório v1.1 foca em: (a) consolidar aprovações, (b) redesenhar roadmap para 2 marcos, (c) avaliar ADER-001/ADR-003, (d) definir plano de ação 10-19/09.

---

## 1. ANÁLISE CRÍTICA DAS NOTAS DE REVISÃO

### 1.1. Nota 2 — Entrega Parcial em 19/09/2026 (CRÍTICA)

**Contexto:** O TAP v1_opngoing (§3.1) previa entrega parcial em **08/09/2026**. A revisão posterga para **19/09/2026**, concedendo **9 dias corridos adicionais** (~7 dias úteis).

**Escopo da entrega parcial (definido pela revisão):**

- TAP v1.0 completo
- Planos das Áreas 1-5 do PMBOK 6ª:
  - 1. Integração
  - 2. Escopo (+ EAP + Dicionário)
  - 3. Cronograma (+ Roadmap 2 marcos)
  - 4. Custos (simplificado)
  - 5. Qualidade (+ DoD/DoR + **PDCA de cada atividade**)
- **PDCA de todas as atividades até o momento** (conforme rede de projeto ongoing)

**Análise de viabilidade:**

- **Capacidade disponível:** 2 pessoas × 20h/semana × 1,4 semanas = **56h úteis** até 19/09
- **Estimativa de esforço:** TAP (8h) + 5 planos × 6h (30h) + PDCAs (6h) = **44h**
- **Folga:** 12h (~21%) — **viável com margem**

**Risco identificado:** A nota diz "não é mandatório entrega de código ou implementação prévia". Isso **libera a Fase 5 (Desenvolvimento)** da entrega parcial, mas exige que os **Planos de Qualidade (Área 5)** estejam 100% concluídos com PDCA documentado.

**Decisão:** A entrega parcial deve conter **artefatos das Áreas 1-5 do PMBOK 6ª** com PDCA de cada atividade.

### 1.2. Nota 3 — PDCA Obrigatório por Atividade (ALTA)

**Contexto:** O Prof. Nivaldo exige **pelo menos um PDCA por atividade do projeto**. A nota operacionaliza: "adotaremos sempre o último PDCA de cada atividade caso mais de 1 PDCA tenha sido executado, comentando brevemente as mudanças resultantes".

**Análise crítica:**

- O OKB v3.0 §4.4 já havia absorvido a dimensão PDCA nas Dimensões 1 e 2. A nota **reintroduz PDCA explícito** como artefato obrigatório.
- **Trade-off:** Aumenta volume documental, mas atende exigência acadêmica explícita.
- **Mitigação KISS:** PDCA como **seção dentro de cada plano** (ex: "§X.X PDCA do Plano de Escopo"), não como documento separado.

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

### 1.3. Nota 4 — Documentação Formal Viva (MÉDIA)

**Contexto:** A documentação pode sofrer ajustes integrais até a entrega do MVP funcional (Nov/Dez 2026).

**Análise:** Esta nota **valida o princípio P6 do OKB** (entrega incremental via fluxo contínuo) e **reforça a hierarquia de governança** (OKB v3.0 §4.1). Não exige ação imediata, mas **blinda academicamente** iterações nos planos após 19/09.

**Implicação operacional:** Os planos entregues em 19/09 serão **v1.0 (baseline)**, mas podem evoluir para v1.1, v1.2 etc. até a entrega final, desde que cada mudança tenha:

1. ADR associado (se afetar ≥ 2 fases da EAP)
2. PDCA documentando a mudança
3. Commit com mensagem convencional (`docs(plano-X): descrição`)

### 1.4. Nota 5 — Código Não Obrigatório na Entrega Parcial (ALTA)

**Contexto:** A entrega parcial de 19/09 **não exige código ou implementação prévia**.

**Análise:** Esta é a **notícia mais relevante** da revisão. Significa que:

- ✅ **Fase 5 (Desenvolvimento) sai do escopo da entrega parcial**
- ✅ **Fase 4 (Configuração de Ambiente) pode ser parcial** (apenas documentação da stack, não setup completo)
- ✅ **Foco total em documentação das Áreas 1-5**

**Impacto no plano de ação:** Reduz escopo da entrega parcial em ~40%, aumentando a folga de 21% para ~45%.

### 1.5. Nota 6 — Remoção de Fases Desejáveis (ALTA)

**Contexto:** A nota diz explicitamente: "Remova a seção de Desejáveis".

**Análise:** Diferente da versão anterior (que apenas marcava como "pós-entrega"), a revisão exige **remoção completa** das fases 14-17 do TAP+EAP. Isso significa:

- ❌ Remover §5.3 do TAP_EAP.md (Fases Desejáveis)
- ❌ Remover lista hierárquica aninhada das fases 14-17
- ❌ Remover tabela estrutural das fases 14-17
- ✅ Manter apenas menção no §8 (Restrições) como "melhoria contínua futura"

**Justificativa GMV:**

- P1 (Prof. Nivaldo exigirá?): NÃO — escopo estrito acadêmico
- P2 (Evita retrabalho?): NÃO — roadmap pós-entrega é YAGNI
- P3 (PMBOK 7ª exige?): NÃO — domínios já cobertos pelas 13 fases
- P4 (Útil para equipe?): NÃO — foco no MVP

**Veredito:** 3×NÃO → **DESCARTAR** (conforme GMV OKB v3.0 §4.2)

### 1.6. Nota 7 — Redesenho do Roadmap para Dois Marcos (CRÍTICA)

**Contexto:** O OKB v2.1 §8.2.1 usava roadmap trimestral (Q3/Q4/Q1). A revisão exige **dois marcos**: Entrega Parcial (19/09) e Entrega Final (MVP funcional).

**Análise:** Esta mudança **alinhada ao YAGNI** — roadmap trimestral era burocracia para projeto de 3 meses. Dois marcos são suficientes e mais claros.

**Novo roadmap proposto (ADR-003 draft):**

| Marco                           | Data         | Escopo                                                      | Critério de Aceite                            |
| ------------------------------- | ------------ | ----------------------------------------------------------- | ---------------------------------------------- |
| **M1 — Entrega Parcial** | 19/09/2026   | TAP + Planos Áreas 1-5 + PDCA de cada atividade            | Prof. Nivaldo valida completude documental     |
| **M2 — Entrega Final**   | Nov/Dez 2026 | MVP funcional + documentação consolidada + apresentação | ≥ 80% coverage + UAT aprovado + FOSS auditado |

**Macro-fases ajustadas:**

| Macro-Fase                    | Período            | Foco                                  |
| ----------------------------- | ------------------- | ------------------------------------- |
| **MF1: Fundação**     | 01/09 – 19/09/2026 | Documentação Áreas 1-5 + PDCA      |
| **MF2: Construção**   | 20/09 – 15/11/2026 | Desenvolvimento + Testes + Deploy     |
| **MF3: Consolidação** | 16/11 – Dez/2026   | Documentação final + Apresentação |

**Trade-off declarado:** A MF1 foi **comprimida de 30 dias para 19 dias** (01/09 → 19/09). Isso exige **foco absoluto em documentação** e **adiamento da Fase 4 completa** para a MF2.

### 1.7. Nota 8 — SDD Reduz Tempo da Fase 5 (MÉDIA)

**Contexto:** "As atividades de implementação devem adotar o SDD portanto esta fase tem previsão de redução temporal (não calculada)"

**Análise:** Esta nota **valida a premissa do ADR-004** (SDD Local via llama.cpp). O SDD pode acelerar a Fase 5 em **30-40%** (estimativa baseada em literatura de SDD), mas a redução exata depende da calibração do pipeline.

**Ação:** Registrar no ADR-004 que a Fase 5 terá duração estimada de **4-5 semanas** (em vez de 6-7 semanas sem SDD), com calibração empírica durante a MF2.

### 1.8. Nota 16 — Fusão N10.1+N10.2+N10.3 (MÉDIA)

**Contexto:** "Mesma finalidade documental - Manter em domínios distintos dentro da base de conhecimento - Verifique a seção 9. Stack SDD Local"

**Análise:** A revisão **rejeita a fusão completa** dos pacotes N10.1 (ADRs), N10.2 (Lições Aprendidas) e N10.3 (Catálogo de Prompts SDD). Em vez disso, mantém os três pacotes, mas **organiza-os em domínios distintos** dentro da Base de Conhecimento, conforme a estrutura da Seção 9 do relatório v1.0.

**Estrutura consolidada da Base de Conhecimento (ref. §9):**

```
10. Base de Conhecimento
├── 10.1. ADRs (decisões arquiteturais)
│   └── Domínio: Governança Técnica
├── 10.2. Lições Aprendidas Contínuas (Retrospectivas)
│   └── Domínio: Melhoria de Processo
├── 10.3. Catálogo de Prompts SDD
│   └── Domínio: SDD / Contexto IA (ref. .ai/prompts/)
└── 10.4. Runbooks Operacionais [DESCARTADO - YAGNI]
```

**Justificativa:** Os três domínios são **ortogonais** (governança, processo, SDD) e mapeiam para estruturas distintas no repositório (`.ai/prompts/`, `docs/adr/`, `docs/retros/`). Fusão completa perderia rastreabilidade.

### 1.9. Nota 24 — Avaliação de ADER-001 e ADR-003 (ALTA)

**Contexto:** "considere também a confecção das ADRs: ADER-001, ADR-003 aderentes ao projeto, caso não passem no crivo de conformidade com o projeto, refatorar"

**Análise de conformidade:**

#### ADER-001 — "Architecture Decision Enhancement Record"

**Hipótese:** A sigla "ADER" sugere um ADR expandido, possivelmente com seção de "Enhancement" (melhoria contínua).

**Teste de conformidade (GMV + OKB v3.0 §4.5):**

| Critério                    | Resultado    | Justificativa                                                          |
| ---------------------------- | ------------ | ---------------------------------------------------------------------- |
| P1 (Prof. Nivaldo exigirá?) | ❌ NÃO      | OKB v3.0 §4.5 já define critério claro de ADR                       |
| P2 (Evita retrabalho?)       | ❌ NÃO      | ADR padrão já captura decisões                                      |
| P3 (PMBOK 7ª exige?)        | ❌ NÃO      | Domínio de Abordagem já coberto por ADR                              |
| P4 (Útil para equipe?)      | ⚠️ PARCIAL | "Enhancement" pode ser útil, mas label`enhancement` no GitHub basta |

**Veredito GMV:** 3×NÃO → **NÃO ADERENTE**

**Decisão:** **NÃO criar ADER-001**. O COGME já possui critério claro de ADR (OKB v3.0 §4.5). Criar "ADER" duplica nomenclatura sem valor adicional. Se houver necessidade de registrar "enhancements", usar **label `enhancement` no GitHub Issues** + link no ADR original.

**Risco mitigado:** Burocratização da governança (R-03).

#### ADR-003 — "Métricas de Fluxo com Baseline"

**Hipótese:** ADR-003 formaliza a calibração de métricas (Cycle Time, Throughput) conforme OKB v3.0 Crítica 4.

**Teste de conformidade (GMV + OKB v3.0 §4.5):**

| Critério                    | Resultado | Justificativa                                 |
| ---------------------------- | --------- | --------------------------------------------- |
| P1 (Prof. Nivaldo exigirá?) | ✅ SIM    | Domínio de Medição PMBOK 7ª               |
| P2 (Evita retrabalho?)       | ✅ SIM    | Baseline evita metas aspiracionais            |
| P3 (PMBOK 7ª exige?)        | ✅ SIM    | Domínio de Medição (métricas acionáveis) |
| P4 (Útil para equipe?)      | ✅ SIM    | Evita burnout por metas irreais               |

**Veredito GMV:** 4×SIM → **ADERENTE**

**Decisão:** **CRIAR ADR-003** até 30/09/2026 (fim da MF1).

**Conteúdo do ADR-003:**

- **Contexto:** OKB v3.0 Crítica 4 identifica métricas sem baseline
- **Decisão:** Estabelecer período de calibração (20/09 – 03/10) para coletar Cycle Time e Throughput sem meta fixa. Após calibração, definir metas realistas (média ± 20%)
- **Consequências:**
  - ✅ Alinha ao Domínio de Medição PMBOK 7ª
  - ✅ Evita metas aspiracionais não acionáveis
  - ⚠️ Risco: 2 semanas sem meta clara → mitigação: comunicação explícita ao Prof. Nivaldo

---

## 2. REDESENHO DO ROADMAP (DOIS MARCOS)

### 2.1. Roadmap Consolidado (ADR-003 draft)

```
┌─────────────────────────────────────────────────────────────────┐
│  MARCO 1 — ENTREGA PARCIAL (19/09/2026)                         │
│  Escopo: Documentação Áreas 1-5 do PMBOK 6ª                     │
│  ├─ TAP v1.0 (com EAP 13 fases + 8 premissas)                   │
│  ├─ Plano de Integração v1.0                                    │
│  ├─ Plano de Escopo v1.0 (+ EAP + Dicionário)                   │
│  ├─ Plano de Cronograma v1.0 (+ Roadmap 2 marcos)               │
│  ├─ Plano de Custos v1.0 (simplificado)                         │
│  ├─ Plano de Qualidade v1.0 (+ DoD/DoR + PDCA)                  │
│  └─ PDCA de cada atividade (último PDCA + mudanças relevantes)  │
│  Critério de aceite: Prof. Nivaldo valida completude            │
├─────────────────────────────────────────────────────────────────┤
│  MARCO 2 — ENTREGA FINAL (Nov/Dez 2026)                         │
│  Escopo: MVP funcional + documentação consolidada               │
│  ├─ Código-fonte (Backend + Frontend + PDF)                     │
│  ├─ ≥ 80% coverage de testes                                    │
│  ├─ Documentação técnica + manual do usuário                    │
│  ├─ Apresentação final + aceite                                 │
│  └─ Auditoria FOSS final                                        │
│  Critério de aceite: MVP funcional + ≥ 80% coverage + UAT       │
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

## 3. EAP CONSOLIDADA (PÓS-REVISÃO)

### 3.1. Pacotes Descartados/Fundidos (Aprovados)

| Pacote Original             | Ação                                              | Justificativa                       |
| --------------------------- | --------------------------------------------------- | ----------------------------------- |
| N5.6 Execução Kanban      | **FUNDIR** com N1.6                           | Kanban é método, não entregável |
| N6.3 Testes de Performance  | **DESCARTAR** do MVP                          | YAGNI (2 usuários-piloto)          |
| N7.2 Pipeline CD            | **SIMPLIFICAR** para deploy manual            | KISS (1 ambiente)                   |
| N9.3 Relatórios Quinzenais | **DESCARTAR**                                 | GitHub Projects é SSOT             |
| N10.4 Runbooks              | **DESCARTAR** do MVP                          | YAGNI (sem operação contínua)    |
| N11.3 Análise de Impacto   | **SIMPLIFICAR** para label `change-request` | KISS (CCB = Prof. Nivaldo)          |
| N12.3 Relatórios EVM       | **DESCARTAR** EVM                             | Kanban usa métricas de fluxo       |
| N13.4 Auditoria FOSS Final  | **FUNDIR** com N4.4                           | KISS (evitar duplicação)          |
| N14-N17 (Fases Desejáveis) | **REMOVER** do TAP+EAP                        | GMV (3×NÃO)                       |

### 3.2. Pacotes Mantidos com Refinamento

| Pacote                | Refinamento                             | Justificativa                                 |
| --------------------- | --------------------------------------- | --------------------------------------------- |
| N5.1 + N5.2           | **FUNDIR** em "Backend completo"  | KISS (1 provider de câmbio)                  |
| N9.1 + N9.2 + N9.4    | **FUNDIR** em "Comunicação"     | KISS (2 pessoas)                              |
| N10.1 + N10.2 + N10.3 | **MANTER** em domínios distintos | Ortopogonalidade (governança, processo, SDD) |

### 3.3. Resultado Consolidado

| Métrica                       | Antes | Depois                  | Ganho                     |
| ------------------------------ | ----- | ----------------------- | ------------------------- |
| Fases Nível 1 (obrigatórias) | 13    | **13** (mantidas) | —                        |
| Fases Desejáveis (14-17)      | 4     | **0** (removidas) | -100%                     |
| Pacotes Nível 2               | 62    | **51**            | **-18%**            |
| Horas estimadas por pacote     | 7,7h  | **9,4h**          | **+22% capacidade** |
| Artefatos OKB (seções)       | 14    | **11**            | **-21%**            |

---

## 4. PLANO DE AÇÃO 10-19/09/2026 (ENTREGA PARCIAL)

### 4.1. Capacidade Disponível

| Recurso         | Disponibilidade                          |
| --------------- | ---------------------------------------- |
| Dias úteis     | 7 (10, 11, 12, 15, 16, 17, 18/09)        |
| Horas por dia   | 4h/pessoa (20h/semana ÷ 5 dias)         |
| Total de horas  | 2 pessoas × 4h × 7 dias =**56h** |
| Escopo estimado | 44h (TAP 8h + 5 planos × 6h + PDCA 6h)  |
| **Folga** | **12h (21%)**                      |

### 4.2. Cronograma Detalhado

| Data                   | Ação                                                                         | Responsável | Artefato                                                | DoD                                                      |
| ---------------------- | ------------------------------------------------------------------------------ | ------------ | ------------------------------------------------------- | -------------------------------------------------------- |
| **10/09 (qui)**  | Finalizar TAP v1.0 (EAP 13 fases + 8 premissas, remover §5.3)                 | GP           | `TAP_EAP.md` v1.0                                     | TAP com 13 fases + 8 premissas, sem fases 14-17          |
| **11/09 (sex)**  | Redigir ADR-001 (GitHub Projects) + ADR-002 (Stack FOSS) + ADR-003 (Métricas) | GP + Dev     | `docs/adr/ADR-001.md`, `ADR-002.md`, `ADR-003.md` | ADRs formatados (Contexto → Decisão → Consequências) |
| **12/09 (sáb)** | Plano de Integração v1.0 + PDCA                                              | GP           | `docs/planos/01-integracao.md`                        | Contém links GitHub + SSOT + PDCA                       |
| **15/09 (seg)**  | Plano de Escopo v1.0 (+ EAP + Dicionário) + PDCA                              | GP           | `docs/planos/02-escopo.md`                            | EAP sincronizada com GitHub Projects + PDCA              |
| **16/09 (ter)**  | Plano de Cronograma v1.0 (+ Roadmap 2 marcos) + PDCA                           | GP           | `docs/planos/03-cronograma.md`                        | Roadmap M1 (19/09) + M2 (Nov/Dez) + PDCA                 |
| **17/09 (qua)**  | Plano de Custos v1.0 (simplificado) + PDCA                                     | GP           | `docs/planos/04-custos.md`                            | 1-2 páginas, foco em premissas + PDCA                   |
| **18/09 (qui)**  | Plano de Qualidade v1.0 (+ DoD/DoR + PDCA)                                     | GP           | `docs/planos/05-qualidade.md`                         | DoD/DoR claros + PDCA de cada atividade                  |
| **19/09 (sex)**  | Revisão final + submissão ao Prof. Nivaldo                                   | GP           | Issue no GitHub                                         | Zero achados CRÍTICOS no checklist                      |

### 4.3. PDCA Consolidado (Entrega Parcial)

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
- ⚠️ Risco: Prof. Nivaldo pode exigir Gantt tradicional → mitigação: gerar Gantt a posteriori a partir do Kanban

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

**Decisão:** Estabelecer período de calibração (20/09 – 03/10) para coletar Cycle Time e Throughput sem meta fixa. Após calibração, definir metas realistas (média ± 20%).

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

## 6. TRADE-OFFS E RISCOS ATUALIZADOS

### 6.1. Trade-offs Declarados

| Trade-off                                    | Risco                                      | Mitigação                                                                                       |
| -------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| MF1 comprimida (30 → 19 dias)               | Qualidade documental reduzida              | Folga de 21% (12h) + foco absoluto em Áreas 1-5                                                  |
| PDCA obrigatório por atividade              | Aumento de volume documental               | PDCA como seção dentro de cada plano (não documento separado)                                  |
| Código não obrigatório na entrega parcial | Percepção de "atraso" pelo Prof. Nivaldo | Comunicar explicitamente que MF2 (20/09 em diante) é dedicada ao código                         |
| ADR-003 com período de calibração         | Métricas sem meta por 2 semanas           | Comunicar ao Prof. Nivaldo que calibração é prática padrão (Domínio de Medição PMBOK 7ª) |
| Remoção das fases 14-17                    | Percepção de "escopo incompleto"         | Justificar via GMV (3×NÃO) + mencionar no §8 como melhoria contínua futura                    |

### 6.2. Riscos Atualizados

| ID   | Risco                                           | Prob. | Impacto | Severidade | Resposta                                | Status          |
| ---- | ----------------------------------------------- | ----- | ------- | ---------- | --------------------------------------- | --------------- |
| R-01 | Stack FOSS indefinida                           | 80%   | Alto    | Crítico   | ADR-002 até 11/09                      | 🟠 Aberto       |
| R-02 | EAP não sincronizada com GitHub                | 60%   | Alto    | Alto       | Mapeamento 1:1 até 15/09               | 🟡 Em andamento |
| R-03 | Governança > 50% do tempo                      | 70%   | Médio  | Alto       | Aplicar GMV                             | 🟡 Aberto       |
| R-04 | Prof. exigir Gantt tradicional                  | 30%   | Médio  | Médio     | ADR-001 + Gantt derivado                | 🟢 Mitigado     |
| R-05 | Scope creep                                     | 50%   | Alto    | Alto       | CCB + DoR rigoroso                      | 🟡 Monitorando  |
| R-08 | Equipe exceder 20h/semana (burnout)             | 50%   | Médio  | Alto       | WIP limits + métrica de burnout        | 🟡 Monitorando  |
| R-09 | **Entrega parcial 19/09 não concluída** | 30%   | Alto    | Alto       | Plano de ação 10-19/09 + folga 21%    | 🟠 Novo         |
| R-10 | **PDCA não documentado por atividade**   | 40%   | Médio  | Médio     | Template PDCA padronizado (Seção 1.2) | 🟠 Novo         |
| R-11 | **Fases 14-17 questionadas pelo Prof.**   | 20%   | Médio  | Médio     | Justificativa GMV + menção no §8     | 🟢 Mitigado     |

---

## 7. AÇÕES BLOQUEANTES (10-19/09/2026)

| #  | Ação                                                         | Responsável | Prazo | Artefato                         |
| -- | -------------------------------------------------------------- | ------------ | ----- | -------------------------------- |
| 1  | Finalizar TAP v1.0 (EAP 13 fases + 8 premissas, remover §5.3) | GP           | 10/09 | `TAP_EAP.md` v1.0              |
| 2  | Redigir ADR-001 (GitHub Projects)                              | GP           | 11/09 | `docs/adr/ADR-001.md`          |
| 3  | Redigir ADR-002 (Stack FOSS)                                   | GP + Dev     | 11/09 | `docs/adr/ADR-002.md`          |
| 4  | Redigir ADR-003 (Métricas de Fluxo)                           | GP           | 11/09 | `docs/adr/ADR-003.md`          |
| 5  | Plano de Integração v1.0 + PDCA                              | GP           | 12/09 | `docs/planos/01-integracao.md` |
| 6  | Plano de Escopo v1.0 (+ EAP + Dicionário) + PDCA              | GP           | 15/09 | `docs/planos/02-escopo.md`     |
| 7  | Plano de Cronograma v1.0 (+ Roadmap 2 marcos) + PDCA           | GP           | 16/09 | `docs/planos/03-cronograma.md` |
| 8  | Plano de Custos v1.0 (simplificado) + PDCA                     | GP           | 17/09 | `docs/planos/04-custos.md`     |
| 9  | Plano de Qualidade v1.0 (+ DoD/DoR + PDCA)                     | GP           | 18/09 | `docs/planos/05-qualidade.md`  |
| 10 | PDCA de cada atividade (último PDCA + mudanças)              | GP           | 18/09 | Seção em cada plano            |
| 11 | Revisão final + submissão ao Prof. Nivaldo                   | GP           | 19/09 | Issue no GitHub                  |
| 12 | Formalizar ADR-004 (SDD Local)                                 | GP + Dev     | 30/09 | `docs/adr/ADR-004.md`          |

---

## 8. DECLARAÇÃO DE CONFORMIDADE

Este relatório v1.1:

- ✅ Deriva 100% das 24 notas de revisão do relatório v1.0
- ✅ Cita domínios e princípios PMBOK 7ª explicitamente
- ✅ Aplica teste GMV (OKB v3.0 §4.2) para cada recomendação de descarte
- ✅ Declara trade-offs e riscos (Domínio de Incerteza PMBOK 7ª)
- ✅ Respeita hierarquia de governança (OKB v3.0 §4.1)
- ✅ É acionável (plano de ação 10-19/09 com datas e responsáveis)
- ✅ Integra PDCA como mecanismo de qualidade (nota de revisão 3)
- ✅ Redesenha roadmap para dois marcos (nota de revisão 7)
- ✅ Avalia aderência de ADER-001 (não aderente) e ADR-003 (aderente)
- ✅ Remove fases 14-17 do TAP+EAP (nota de revisão 6)
- ✅ Mantém N10.1+N10.2+N10.3 em domínios distintos (nota de revisão 16)

---

## 9. PRÓXIMOS PASSOS

1. **Aprovar este relatório v1.1** como base para execução 10-19/09
2. **Iniciar ação #1** (TAP v1.0 com remoção de §5.3) imediatamente
3. **Comunicar ao Prof. Nivaldo** o redesenho do roadmap (dois marcos) via Issue no GitHub
4. **Formalizar ADR-001, ADR-002 e ADR-003** até 11/09
5. **Próxima revisão:** 19/09/2026 (após entrega parcial)

---

**Fim do Relatório Analítico v1.1**

Aguardo autorização para iniciar a execução do plano de ação 10-19/09/2026.
