# RELATÓRIO ANALÍTICO — BASE DE CONHECIMENTO COMPLEMENTAR v3.0 (GUARDRAIL EVOLUÍDO)

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Data de Emissão:** 09/09/2026
**Versão anterior:** OKB_COGME_v2.1 (07/09/2026)
**Emissor:** GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)
**Stakeholder:** Prof. Dr. Nivaldo Carletto

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
