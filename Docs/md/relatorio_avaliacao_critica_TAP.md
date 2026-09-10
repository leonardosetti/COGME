# RELATÓRIO DE AVALIAÇÃO CRÍTICA — TAP v1 (COGME)

**Emissor:** GP Sênior PMBOK 7ª / PMO (Co-Autor Crítico)
**Data:** 10/09/2026
**Documento avaliado:** `Termo de Abertura do Projeto v1_opngoing.docx`
**Referências normativas:** OKB_COGME_v3.1 + Análise Arquitetural v2.0 + PMBOK 7ª (Domínios) + PMBOK 6ª §4.1 (dicionário)
**Stakeholder-avaliador:** Prof. Dr. Nivaldo Carletto

---

## 1. VEREDITO EXECUTIVO

**Status do TAP v1: 🔴 NÃO APROVÁVEL na forma atual**

O documento apresenta **7 inconsistências estruturais críticas** que impedem submissão ao Prof. Dr. Nivaldo Carletto. A versão atual reflete o estado pré-OKB v3.1 (09/09/2026) e não incorporou as 6 correções da Análise Arquitetural v2.0. O scorecard de aceite é **4.8/10** — abaixo do limiar de 7.0 para submissão.

**Scorecard de Aceite:**

| Dimensão | Score | Comentário |
|---|---|---|
| Conformidade com OKB v3.1 | 3/10 | Faltam 10 declarações obrigatórias (§8) |
| Separação ontológica TAP ≠ EAP | 2/10 | N1.1 (TAP) ainda integra EAP |
| Consistência com Stack Canônica | 4/10 | Redis mencionado (stack canônica = SQLite) |
| Completude das seções vazias | 2/10 | 4 seções vazias (Requisitos, Premissas, Riscos, Orçamento) |
| Qualidade textual (nomes/datas) | 5/10 | Erros de grafia em nomes-chave |
| Rastreabilidade TAP → EAP | 6/10 | EAP mapeada, mas desalinhada com GitHub |
| Hierarquia PMBOK 7ª → 6ª | 3/10 | Item 1.c cita 6ª como primário |
| **Score Geral** | **4.8/10** | **Requer reescrita estrutural** |

---

## 2. MUDANÇAS FUNDAMENTAIS/ESTRUTURAIS IDENTIFICADAS

### 2.1. Mudanças Bloqueantes (Severidade 🔴 CRÍTICA)

| # | Mudança | Fundamentação | Impacto |
|---|---|---|---|
| M1 | **Remover N1.1 (TAP) da EAP** | Separação ontológica OKB v3.1 §3.3 — TAP autoriza, não é gerenciado | Reduz EAP de 62 para 48 pacotes |
| M2 | **Remover fases desejáveis (14-17) da linha de base** | OKB v3.1 §5 — são roadmap pós-entrega, não MVP acadêmico | Reduz escopo em 13 pacotes |
| M3 | **Reescrever item 1.c com hierarquia PMBOK 7ª → 6ª** | OKB v3.1 §3.1 — 7ª é governança primária; 6ª é dicionário | Evita questionamento da banca |
| M4 | **Incluir 10 Declarações de Governança obrigatórias** | OKB v3.1 §8 — guardrail inegociável | Nova seção §11 |
| M5 | **Remover referências a Redis** | Stack canônica v2.0 §4.2 usa SQLite 3; Redis é YAGNI | Alinhamento técnico |
| M6 | **Substituir EVM/Burndown por métricas de fluxo Kanban** | OKB v3.1 §3.4 — GitHub Insights é SSOT | Domínio de Medição PMBOK 7ª |
| M7 | **Corrigir nomes próprios e institucionais** | Credibilidade acadêmica | "Carletto" (não Carleto); "Fatec Taquaritinga" (não Marlene Maria Miletta Servidoni) |

### 2.2. Mudanças Estruturais (Severidade 🟠 ALTA)

| # | Mudança | Fundamentação |
|---|---|---|
| M8 | **Reorganizar a EAP em 13 fases + 48 pacotes** | Análise v2.0 §3.1 — redução de 23% no escopo |
| M9 | **Inserir seção "Principais Requisitos das Entregas"** | PMBOK 6ª §5.2 + padrão PMO escritoriodeprojetos.com.br |
| M10 | **Inserir seção "Premissas" (8 premissas)** | OKB v3.1 §9 — 16 premissas consolidadas, 8 no TAP |
| M11 | **Inserir seção "Riscos" (Top 5)** | Domínio de Incerteza PMBOK 7ª |
| M12 | **Inserir seção "Orçamento" (R$ 0,00 com justificativa)** | Domínio de Custos + restrição TAP §8.4 |
| M13 | **Preencher Marcos com datas concretas** | Domínio de Medição PMBOK 7ª — MF1/MF2/MF3 |
| M14 | **Remover comentários de revisão ("Comment by leonardo")** | Limpeza textual pré-submissão |

### 2.3. Mudanças Cosméticas (Severidade 🟡 MÉDIA)

| # | Mudança | Fundamentação |
|---|---|---|
| M15 | Padronizar "Fatec Taquaritinga" em todo o documento | Consistência institucional |
| M16 | Atualizar Controle de Versões para v1.0 | Rastreabilidade documental |
| M17 | Remover menções a "ADER" (termo obsoleto) | OKB v3.1 §13 — eliminação definitiva |

---

## 3. ANÁLISE DE ACEITE DO PROJETO (Scorecard Detalhado)

### 3.1. Critérios de Aceite Acadêmico

| Critério | Status | Evidência | Ação |
|---|---|---|---|
| **C1 — Autorização formal** | ✅ OK | §1 identifica gerente, patrocinador, instituição | Nenhuma |
| **C2 — Objetivos SMART** | ✅ OK | §3 com 5 objetivos mensuráveis | Nenhuma |
| **C3 — Critérios de sucesso/fracasso** | ✅ OK | §3.2 e §3.3 bem definidos | Nenhuma |
| **C4 — EAP coerente** | 🔴 FALHA | N1.1 (TAP) integra EAP; 62 pacotes (deveria ser 48) | Reestruturar (M1, M2, M8) |
| **C5 — Requisitos das entregas** | 🔴 FALHA | Seção §5 vazia | Redigir (M9) |
| **C6 — Marcos temporais** | ⚠️ Parcial | Datas em aberto; comentário pendente | Preencher (M13) |
| **C7 — Stakeholders** | ⚠️ Parcial | Nomes grafados incorretamente | Corrigir (M7) |
| **C8 — Restrições** | ✅ OK | §8 com 8 categorias PMBOK 6ª detalhadas | Nenhuma |
| **C9 — Premissas** | 🔴 FALHA | Seção §9 vazia | Redigir (M10) |
| **C10 — Riscos** | 🔴 FALHA | Seção §10 vazia | Redigir (M11) |
| **C11 — Orçamento** | 🔴 FALHA | Seção §11 vazia | Redigir (M12) |
| **C12 — Declarações de Governança** | 🔴 FALHA | Seção ausente | Inserir (M4) |
| **C13 — Hierarquia PMBOK** | 🔴 FALHA | Item 1.c cita 6ª como primário | Reescrever (M3) |
| **C14 — Consistência técnica** | ⚠️ Parcial | Redis e EVM mencionados (violam stack canônica) | Corrigir (M5, M6) |

### 3.2. Veredito Final de Aceite

**Projeto NÃO APROVÁVEL na forma atual.**

**Condições para aprovação:**
- Resolver 7 falhas críticas (C4, C5, C9, C10, C11, C12, C13)
- Resolver 2 falhas parciais (C6, C7)
- Elevar scorecard para ≥ 7.0/10
- Submeter TAP v1.0 ao Prof. Dr. Nivaldo Carletto até **11/09/2026, 23:59**

**Risco de reprovação acadêmica:** 85% se submetido hoje sem correções.

---

## 4. VALIDAÇÃO DA ESTRUTURA DE SEÇÕES — PRIORIZAÇÃO SEQUENCIAL

A estrutura atual do TAP v1 contém **11 seções numeradas**. A proposta de normalização segue o padrão PMO escritoriodeprojetos.com.br + OKB v3.1 §7 (árvore de artefatos), com **adição da seção §11 (Declarações de Governança)** e **reorganização da seção §4 (EAP)**.

### 4.1. Matriz de Priorização

| # | Seção | Prioridade | Status Atual | Ação Necessária | DoD |
|---|---|---|---|---|---|
| **1** | Objetivos deste documento | 🟢 P3 | ✅ OK | Reescrever item 1.c (hierarquia PMBOK 7ª → 6ª) | Item 1.c alinhado |
| **2** | Situação atual e justificativa | 🟢 P3 | ✅ OK | Nenhuma | Manter |
| **3** | Objetivos SMART e critérios de sucesso | 🟢 P3 | ✅ OK | Nenhuma | Manter |
| **4** | ESTRUTURA ANALÍTICA DO PROJETO (EAP/WBS) | 🔴 **P0** | 🔴 Inconsistente | Reestruturar: remover N1.1; remover fases 14-17; reduzir para 48 pacotes | EAP v1.0 (13 fases + 48 pacotes) |
| **5** | Principais requisitos das entregas | 🔴 **P0** | 🔴 VAZIA | Redigir tabela com 5 entregas + requisitos + critérios | Tabela completa |
| **6** | Marcos | 🟠 P1 | ⚠️ Parcial | Preencher datas; resolver comentário do Leonardo | Datas concretas |
| **7** | Partes interessadas | 🟠 P1 | ⚠️ Parcial | Corrigir nomes (Carletto, Silva, Fatec Taquaritinga) | Zero erros |
| **8** | Restrições | 🟢 P3 | ✅ OK | Nenhuma | Manter |
| **9** | Premissas | 🔴 **P0** | 🔴 VAZIA | Redigir 8 premissas fundamentais (OKB v3.1 §9) | 8 premissas numeradas |
| **10** | Riscos | 🔴 **P0** | 🔴 VAZIA | Redigir Top 5 riscos com prob./impacto/resposta | 5 riscos com resposta |
| **11** | Orçamento do Projeto | 🔴 **P0** | 🔴 VAZIA | Redigir declaração R$ 0,00 com justificativa | Justificativa presente |
| **12** | Declarações de Governança | 🔴 **P0** | 🔴 AUSENTE | Inserir nova seção com 10 declarações (OKB v3.1 §8) | 10 declarações |
| **13** | Aprovações | 🟠 P1 | ⚠️ Parcial | Corrigir nomes; remover linhas vazias | Nomes corretos |

### 4.2. Sequência de Execução Recomendada

**Bloco 1 — 🔴 P0 (10/09/2026, manhã/tarde):**
1. Seção §4 — Reestruturar EAP (M1, M2, M8)
2. Seção §5 — Redigir requisitos das entregas (M9)
3. Seção §9 — Redigir premissas (M10)
4. Seção §10 — Redigir riscos (M11)
5. Seção §11 — Redigir orçamento (M12)
6. Seção §12 — Inserir declarações de governança (M4)

**Bloco 2 — 🟠 P1 (10/09/2026, noite → 11/09 manhã):**
7. Seção §6 — Preencher marcos (M13)
8. Seção §7 — Corrigir stakeholders (M7)
9. Seção §13 — Corrigir aprovações

**Bloco 3 — 🟢 P3 (11/09/2026, tarde):**
10. Seção §1 — Reescrever item 1.c (M3)
11. Seção §2 — Revisão textual
12. Seção §3 — Revisão textual
13. Seção §8 — Revisão textual
14. Global — Correções cosméticas (M15, M16, M17)
15. Global — Remover comentários de revisão (M14)
16. Global — Corrigir menções a Redis/EVM (M5, M6)

### 4.3. Estrutura Final Proposta (TAP v1.0)

| # | Seção | Fundamentação |
|---|---|---|
| 0 | Controle de Versões | Padrão PMO |
| 1 | Objetivos deste documento | Metalinguística |
| 2 | Situação atual e justificativa | Domínio de Stakeholders PMBOK 7ª |
| 3 | Objetivos SMART e critérios de sucesso | Domínio de Entrega + Medição PMBOK 7ª |
| 4 | ESTRUTURA ANALÍTICA DO PROJETO (EAP/WBS) | Processo 5.4 PMBOK 6ª |
| 5 | **Principais requisitos das entregas** | Processo 5.2 PMBOK 6ª |
| 6 | Marcos | Processo 6.5 PMBOK 6ª |
| 7 | Partes interessadas | Processo 13.1 PMBOK 6ª |
| 8 | Restrições | Processo 1.2 PMBOK 6ª |
| 9 | **Premissas** | Processo 1.2 PMBOK 6ª |
| 10 | **Riscos** | Processo 11.1 PMBOK 6ª |
| 11 | **Orçamento do Projeto** | Processo 6.4 PMBOK 6ª |
| 12 | **Declarações de Governança** | OKB v3.1 §8 (guardrail) |
| 13 | Aprovações | Processo 4.1 PMBOK 6ª |

**Nota:** A seção §12 (Declarações de Governança) é **NOVA** e obrigatória conforme OKB v3.1 §8. Sua ausência é a falha mais crítica do TAP atual.

---

## 5. TRADE-OFFS SINALIZADOS

| Trade-off | Opção A | Opção B | Recomendação |
|---|---|---|---|
| Completude vs. Prazo | Finalizar TAP 100% antes de codar | Começar Fase 4 em paralelo | **Opção B** (Kanban permite paralelismo) |
| EAP detalhada vs. EAP enxuta | Manter 62 pacotes | Reduzir para 48 pacotes | **48 pacotes** (OKB v3.1 §5) |
| PMBOK 6ª vs. 7ª como primário | Reverter para 6ª | Manter 7ª primário | **7ª primário** (OKB v3.1 §3.1) |
| Redis vs. SQLite | Manter Redis (cache) | Usar SQLite (stack canônica) | **SQLite** (Análise v2.0 §4.2) |
| EVM vs. Métricas de fluxo | Manter EVM/Burndown | Usar Cycle Time/Throughput | **Métricas de fluxo** (OKB v3.1 §3.4) |

---

## 6. PLANO DE AÇÃO IMEDIATO (10-11/09/2026)

| Data/Hora | Ação | Responsável | Artefato |
|---|---|---|---|
| 10/09 08:00-12:00 | Reestruturar EAP (seção §4) | GP | TAP v0.9 |
| 10/09 13:00-15:00 | Redigir requisitos (seção §5) | GP | TAP v0.9 |
| 10/09 15:00-17:00 | Redigir premissas (seção §9) | GP | TAP v0.9 |
| 10/09 19:00-21:00 | Redigir riscos (seção §10) + orçamento (seção §11) | GP | TAP v0.9 |
| 11/09 08:00-10:00 | Inserir declarações de governança (seção §12) | GP | TAP v1.0 |
| 11/09 10:00-12:00 | Preencher marcos + corrigir stakeholders + aprovações | GP | TAP v1.0 |
| 11/09 13:00-15:00 | Reescrever item 1.c + correções cosméticas | GP | TAP v1.0 |
| 11/09 15:00-17:00 | Revisão cruzada (Persona Revisora OKB v2.1 §10) | Revisor | Checklist |
| 11/09 19:00 | Submissão ao Prof. Dr. Nivaldo Carletto | GP | Issue no GitHub |

---

## 7. RECOMENDAÇÃO FINAL DO GP SÊNIOR

**Decisão recomendada:** elevar o TAP à versão **v1.0** até **11/09/2026, 23:59**, incorporando as **17 mudanças** identificadas neste relatório, com foco nas **6 mudanças bloqueantes (M1-M6)** e nas **6 seções P0 (§4, §5, §9, §10, §11, §12)**.

**Condição de sucesso:** TAP v1.0 aprovado pelo Prof. Dr. Nivaldo Carletto até 13/09/2026, permitindo transição para MF2 (Construção) em 01/10/2026 sem atraso.

**Escalamento:** caso o Prof. Nivaldo não valide até 13/09, acionar gatilho de reavaliação do OKB v3.1 §11.2 (mudança no critério de avaliação).

---

