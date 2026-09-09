# BASE DE CONHECIMENTO OPERACIONAL — PROJETO COGME v2.1

## Veredito Sumário

O projeto COGME opera sob **hibridização evolutiva**: PMBOK 7ª (princípios e domínios de desempenho) como governança primária, Kanban via GitHub Projects como método de execução, e PMBOK 6ª como dicionário de processos complementares quando necessário. A base de conhecimento funciona como **árbitro de conflitos** e **fonte única de verdade técnica**, não como catálogo burocrático.

**Princípio orientador**: Valor entregue > Satisfação do stakeholder > Conformidade documental.

---

## 1. Princípios Constitutivos do Projeto (Imutáveis)

| # | Princípio | Fundamentação |
|---|-----------|---------------|
| P1 | **Valor sobre documentação** | PMBOK 7ª — Princípio 1: "Seja um administrador diligente, respeitoso e cuidadoso" |
| P2 | **FOSS absoluto** | Restrição pedagógica + valor social (TAP §2.4) |
| P3 | **KISS como métrica de arquitetura** | Cada decisão técnica deve ser justificada pela simplicidade |
| P4 | **SDD com IA auditável** | Todo código gerado por LLM deve ter rastreabilidade via commit |
| P5 | **ACID e Clean Code como padrão** | Restrição técnica inegociável |
| P6 | **Entrega incremental via fluxo contínuo** | Kanban + GitHub Projects (sem sprints fixas) |
| P7 | **Stakeholder único formal** | Prof. Dr. Nivaldo Carletto como patrocinador-avaliador |

---

## 2. Abordagem Híbrida de Governança

### 2.1. Hierarquia de Resolução de Conflitos

Em caso de contradição, aplicar na ordem:

1. **Valor entregue ao usuário final** (PMBOK 7ª — Domínio de Entrega)
2. **Ementa da disciplina + orientação do Prof. Nivaldo**
3. **PMBOK 7ª** (12 princípios + 8 domínios de desempenho)
4. **Manifesto Ágil + Kanban** (método de execução)
5. **PMBOK 6ª** (apenas como dicionário de processos quando necessário)
6. **Literatura técnica complementar**

**Regra de ouro**: Se houver conflito entre documentação e valor entregue, **o valor prevalece**, desde que justificado via ADR (Architecture Decision Record).

### 2.2. Mapeamento PMBOK 7ª ↔ Ágil ↔ PMBOK 6ª (Tripla Camada)

| Domínio PMBOK 7ª | Ritual Ágil (Kanban/GitHub Projects) | Processo PMBOK 6ª (quando aplicável) | Artefato |
|---|---|---|---|
| Stakeholders | Review com Prof. Nivaldo | 13.1 Identificar Stakeholders | Matriz de comunicação |
| Equipe | Daily assíncrona (GitHub Issues/Discussions) | 9.1 Planejar Recursos | RACI simplificado |
| Abordagem de Desenvolvimento | Kanban flow (GitHub Projects) | 4.1 Desenvolver TAP | TAP + Guardrail |
| Planejamento | Refinement semanal do backlog | 5.2 Coletar Requisitos | Backlog + EAP |
| Trabalho do Projeto | Pull system + WIP limits | 4.3 Orientar e Gerenciar | Código-fonte |
| Entrega | Deploy contínuo | 5.3 Criar EAP | MVP funcional |
| Medição | Cycle time + Throughput (GitHub Insights) | 4.5 Monitorar e Controlar | Dashboard GitHub |
| Incerteza | Risk backlog | 11.2 Identificar Riscos | Matriz Prob./Impacto |

---

## 3. Domínios de Desempenho (PMBOK 7ª) — Aplicação ao COGME

| Domínio | Meta Mensurável | Responsável |
|---|---|---|
| **Stakeholders** | 100% das entregas validadas pelo Prof. Nivaldo em até 48h | Gerente |
| **Equipe** | Zero burnout (carga ≤ 20h/semana por membro) | Auto-gestão |
| **Abordagem de Desenvolvimento** | 100% FOSS + Kanban + SDD auditável | Devs |
| **Planejamento** | Backlog refinado semanalmente com DoR claro | Gerente |
| **Trabalho do Projeto** | Cycle time médio ≤ 3 dias por card | Devs |
| **Entrega** | MVP funcional até Nov/2026 com ≥ 80% cobertura de testes | Devs |
| **Medição** | SPI ≥ 0.9 e CPI ≥ 0.9 quinzenalmente | Gerente |
| **Incerteza** | Zero riscos críticos sem plano de resposta | Gerente |

---

## 4. Critérios de Qualidade Unificados (PDCA + DoD + SDD)

Todo artefato deve satisfazer **simultaneamente**:

### 4.1. Dimensão PMBOK 7ª (Valor)
- Deriva de um princípio constitucional (P1 a P7)
- Atende a um domínio de desempenho mensurável
- Gera valor tangível ao stakeholder

### 4.2. Dimensão Ágil (Fluxo)
- DoR (Definition of Ready) antes de produzir
- DoD (Definition of Done) após produzir
- Card no Kanban (GitHub Projects) com ciclo de vida rastreável

### 4.3. Dimensão SDD (IA Auditável)
- Prompt de geração registrado em `/docs/prompts/`
- Código gerado revisado e commitado com assinatura
- Testes automatizados cobrindo a especificação

### 4.4. Dimensão PDCA (Melhoria Contínua)
- **Plan**: artefato versionado (v0.1, v0.2, v1.0)
- **Do**: produção conforme escopo
- **Check**: revisão automática (CI) + manual (pair review)
- **Act**: ajuste via ADR se necessário

---

## 5. Estrutura Documental Obrigatória (Árvore de Artefatos v2.1)

```
PROJETO COGME
├── 00. TAP (Termo de Abertura)
├── 01. Plano de Integração (guarda-chuva)
├── 02. Plano de Escopo + EAP/WBS + Dicionário
├── 03. Plano de Cronograma + Roadmap + Kanban Setup
├── 04. Plano de Custos + Orçamento
├── 05. Plano de Qualidade + Métricas + DoD/DoR
├── 06. Plano de Recursos + RACI
├── 07. Plano de Comunicações + Matriz + Canais
├── 08. Plano de Riscos + Matriz + Respostas
├── 09. Base de Conhecimento
│   ├── 09.1. ADRs (Architecture Decision Records)
│   ├── 09.2. Lições Aprendidas Contínuas
│   ├── 09.3. Prompts de SDD Catalogados
│   └── 09.4. Runbooks Operacionais
├── 10. Plano de Gestão de Mudanças (CCB)
└── 11. Código-Fonte (MVP full-stack) + DER + Diagramas
```

**Regra de consistência**: Todo artefato 02-10 deve referenciar explicitamente o TAP (seção X, parágrafo Y) e possuir um ADR associado quando houver decisão técnica relevante.

---

## 6. EAP Revisada e Expandida (13 Fases Obrigatórias + 4 Desejáveis)

### NÍVEL 0 (RAIZ)
📁 **Projeto COGME — Conversor de Ganhos em Moeda Estrangeira**

### NÍVEL 1 e 2 — FASES OBRIGATÓRIAS (MVP Acadêmico)

| Fase (Nível 1) | Subfases / Pacotes de Trabalho (Nível 2) |
|---|---|
| **1. Iniciação e Planejamento** | 1.1. TAP<br>1.2. Identificação de Stakeholders<br>1.3. Planos de Gerenciamento (Escopo, Cronograma, Custo, Riscos)<br>1.4. Plano da Qualidade<br>1.5. Política de Licenciamento FOSS<br>1.6. Definição do Backlog e Kanban (GitHub Projects) |
| **2. Levantamento e Análise de Requisitos** | 2.1. Requisitos Funcionais<br>2.2. Requisitos Não Funcionais<br>2.3. Casos de Uso e Histórias de Usuário |
| **3. Modelagem e Prototipação** | 3.1. Arquitetura da Solução<br>3.2. Protótipo UX/UI<br>3.3. Modelagem de Dados (DER) |
| **4. Configuração de Ambiente** | 4.1. Seleção e Validação da Stack FOSS<br>4.2. Repositório Git + CI/CD<br>4.3. Setup Local e Homologação<br>4.4. Auditoria de Licenças |
| **5. Desenvolvimento do Sistema** | 5.1. Backend (Lógica de Negócio)<br>5.2. Backend (API de Câmbio + Cache Redis)<br>5.3. Frontend (Interface)<br>5.4. Módulo PDF (WeasyPrint)<br>5.5. SDD com IA (Prompts + Revisão)<br>5.6. Execução Kanban (Rituais no GitHub Projects) |
| **6. Garantia da Qualidade e Testes** | 6.1. Testes Unitários/Integração (≥ 80%)<br>6.2. Testes de Aceitação (UAT)<br>6.3. Testes de Performance e Carga |
| **7. DevOps e CI/CD** | 7.1. Pipeline CI (lint + testes)<br>7.2. Pipeline CD (build + deploy) |
| **8. Implantação (Deploy)** | 8.1. Publicação em Produção<br>8.2. Documentação de Deploy + Rollback |
| **9. Comunicação** | 9.1. Matriz de Comunicação (RACI)<br>9.2. Canais Oficiais (GitHub, e-mail, reuniões)<br>9.3. Relatórios de Status Quinzenais<br>9.4. Cerimônias com Stakeholder (Prof. Nivaldo) |
| **10. Base de Conhecimento** | 10.1. ADRs (decisões arquiteturais)<br>10.2. Lições Aprendidas Contínuas (Retrospectivas)<br>10.3. Catálogo de Prompts SDD<br>10.4. Runbooks Operacionais |
| **11. Gestão de Mudanças** | 11.1. CCB (Change Control Board) — Prof. Nivaldo<br>11.2. Registro de Solicitações de Mudança<br>11.3. Análise de Impacto (escopo/custo/prazo)<br>11.4. Aprovação e Versionamento |
| **12. Documentação do Projeto** | 12.1. Documentação Técnica (Arquitetura, APIs)<br>12.2. Manual do Usuário<br>12.3. Relatórios de Desempenho (EVM/Burndown)<br>12.4. Consolidação da Documentação Parcial (Entrega 08/09/2026) |
| **13. Encerramento** | 13.1. Lições Aprendidas Finais<br>13.2. Verificação SMART<br>13.3. Apresentação Final + Aceite<br>13.4. Auditoria FOSS Final |

### NÍVEL 1 e 2 — FASES DESEJÁVEIS (Melhoria Contínua Pós-Entrega)

> **Nota**: Estas fases foram identificadas como críticas para um produto profissional em produção, mas são **incompatíveis com o cronograma e recursos do MVP acadêmico** (2 pessoas, 3 meses). Devem ser tratadas como **roadmap de evolução pós-entrega**, não como entregáveis obrigatórios.

| Fase (Nível 1) | Subfases / Pacotes de Trabalho (Nível 2) | Justificativa para Pós-Entrega |
|---|---|---|
| **14. Segurança e Privacidade** ⭐ | 14.1. Análise de Riscos (OWASP Top 10)<br>14.2. Conformidade LGPD (dados pessoais)<br>14.3. Testes de Segurança (pentest básico)<br>14.4. Política de Senhas e JWT | Sistema lida com dados pessoais e financeiros. LGPD é obrigatório no Brasil, mas a implementação completa exige auditoria externa e consultoria jurídica que extrapolam o escopo acadêmico. |
| **15. Acessibilidade** ⭐ | 15.1. Auditoria WCAG 2.1 AA<br>15.2. Testes com leitores de tela<br>15.3. Contraste e navegação por teclado | Projeto acadêmico em instituição pública deve ser inclusivo, mas a auditoria completa de acessibilidade exige especialistas e ferramentas pagas (ex: Axe DevTools Pro). |
| **16. Observabilidade** ⭐ | 16.1. Logging Estruturado (JSON)<br>16.2. Health Checks (/health, /warmup)<br>16.3. Métricas de Negócio (simulações/dia)<br>16.4. Alertas de Falha (Keep-Alive) | Sistema depende de API externa e será hospedado em ambiente gratuito instável. Observabilidade completa exige stack adicional (Prometheus, Grafana, Loki) que consome tempo de setup. |
| **17. Internacionalização (i18n)** ⭐ | 17.1. Suporte a múltiplas moedas (USD, EUR, GBP, BRL)<br>17.2. Formatação de datas e números por locale<br>17.3. Preparação para tradução de UI (futuro) | Sistema de câmbio multi-moeda exige tratamento correto de locales, mas a internacionalização completa (tradução de UI, suporte a RTL, etc.) é complexa e não essencial para o MVP brasileiro. |

⭐ = **Fases movidas para "Melhoria Contínua Pós-Entrega"**

---

## 7. Justificativa das Fases Obrigatórias (MVP Acadêmico)

| Fase | Por que é crítica para o COGME? | Risco se omitida |
|---|---|---|
| **9. Comunicação** | Equipe de 2 pessoas + stakeholder único exige fluxo formal para evitar ruído e garantir rastreabilidade de decisões. | Decisões verbais não documentadas geram retrabalho e reprovação acadêmica. |
| **10. Base de Conhecimento** | SDD com IA gera conhecimento tácito (prompts, ADRs) que precisa ser capturado para não se perder entre desenvolvedores. | Perda de conhecimento em caso de afastamento de um membro; repetição de erros. |
| **11. Gestão de Mudanças** | Prazo apertado + escopo ambicioso exigem controle formal de mudanças para evitar scope creep. | Scope creep inviabiliza entrega no prazo; professor questiona mudanças não aprovadas. |

---

## 8. Roadmap e Gestão de Fluxo (Substituindo Gantt)

### 8.1. Por que não Gantt?

O diagrama de Gantt é adequado para projetos **predittivos** (cascata) com dependências rígidas e escopo fixo. O COGME opera sob **abordagem ágil (Kanban)** com escopo evolutivo e entregas incrementais. O Gantt geraria:
- Falsa sensação de controle (datas fixas em ambiente incerto)
- Burocratização desnecessária (atualização manual de barras)
- Desalinhamento com o método de execução (Kanban/GitHub Projects)

### 8.2. Abordagem Moderna: Roadmap + Kanban + GitHub Projects

#### 8.2.1. Roadmap Estratégico (Visão de Alto Nível)

O roadmap substitui o Gantt como ferramenta de comunicação com stakeholders. Ele mostra **marcos temporais e entregas de valor**, não tarefas detalhadas.

**Formato recomendado**: Roadmap em formato de tabela ou timeline visual (ex: Notion, GitHub Projects Roadmap view, ou draw.io).

| Trimestre | Marco | Entrega de Valor | Status |
|---|---|---|---|
| **Q3/2026** (Jul-Set) | Fundação e Documentação | TAP, Planos de Gerenciamento, EAP, Stack validada | 🟡 Em andamento |
| **Q4/2026** (Out-Dez) | MVP Funcional | Sistema web completo com simulação, invoices e PDF | ⚪ Não iniciado |
| **Q1/2027** (Jan-Mar) | Melhoria Contínua | Segurança, acessibilidade, observabilidade, i18n | ⚪ Não iniciado |

#### 8.2.2. Kanban Operacional (GitHub Projects)

O Kanban no GitHub Projects é a **ferramenta primária de gestão do trabalho diário**. Ele substitui o cronograma detalhado do PMBOK 6ª.

**Colunas recomendadas**:
1. **Backlog** (cards criados mas não priorizados)
2. **To Do** (cards priorizados e prontos para iniciar)
3. **In Progress** (cards em desenvolvimento — WIP limit: 3 por pessoa)
4. **Review** (cards em revisão de código ou documentação)
5. **Done** (cards concluídos e validados)

**Métricas de fluxo** (substituem EVM tradicional):
- **Cycle Time**: Tempo médio de um card do "To Do" ao "Done" (meta: ≤ 3 dias)
- **Throughput**: Número de cards concluídos por semana (meta: ≥ 5 cards/semana)
- **Cumulative Flow Diagram**: Visualização de gargalos no fluxo

#### 8.2.3. Integração com PMBOK 6ª (Quando Necessário)

Se o Prof. Nivaldo exigir um cronograma formal (Gantt) para fins acadêmicos, ele deve ser gerado **automaticamente** a partir do Kanban:
- Exportar cards do GitHub Projects com datas de início/fim
- Importar em ferramenta de Gantt (ex: draw.io, Mermaid, ou ProjectLibre)
- Manter o Gantt como **artefato de compliance**, não como ferramenta de gestão

**Regra**: O Gantt é **derivado** do Kanban, não o contrário. O Kanban é a fonte de verdade.

---

## 9. Regras de Redação (Persona Redatora v2.1)

1. Linguagem técnica PMBOK 7ª + ágil, impessoal, objetiva
2. Citar **princípio ou domínio PMBOK 7ª** quando aplicável (ex: "conforme Domínio de Entrega do PMBOK 7ª")
3. Declarar premissas, restrições e fatores de risco explicitamente
4. **Sempre usar métricas** ("critério de aceite: 95% dos casos de teste passing") — nunca linguagem genérica
5. Cada seção deve responder: **O quê? Por quê? Quem? Quando? Como? Quanto?**
6. Para decisões técnicas: redigir ADR (Architecture Decision Record) no formato: Contexto → Decisão → Consequências

---

## 10. Regras de Revisão (Persona Revisora v2.1)

Para cada artefato, validar os **7 critérios**:

| # | Critério | Pergunta-Chave |
|---|---|---|
| 1 | **Rastreabilidade** | Deriva do TAP ou de um princípio constitucional? |
| 2 | **Consistência** | Datas/custos/escopo batem com outros planos? |
| 3 | **Valor (PMBOK 7ª)** | Atende a um domínio de desempenho? |
| 4 | **Fluxo Ágil** | DoR/DoD claros? Card no Kanban? |
| 5 | **SDD Auditável** | Prompts registrados? Código testado? |
| 6 | **Executabilidade** | Código corresponde ao escopo documentado? |
| 7 | **Linguagem** | Técnica, sem floreio, sem ambiguidade? |

Classificar achados: **CRÍTICA** (bloqueante) | **MÉDIA** (deve corrigir) | **BAIXA** (sugestão)

---

## 11. Declarações Obrigatórias no TAP (Atualizadas)

1. **Premissa 1**: "PMBOK 7ª adotado como governança primária (princípios e domínios), com PMBOK 6ª como dicionário complementar de processos quando necessário."
2. **Premissa 2**: "Metodologia ágil Kanban via GitHub Projects adotada como método de execução, com rituais mapeados aos domínios PMBOK 7ª."
3. **Premissa 3**: "Uso de LLM como ferramenta auxiliar autorizada, com rastreabilidade via ADRs e prompts catalogados na Base de Conhecimento."
4. **Premissa 4**: "Código-fonte (MVP full-stack) constitui marco de sucesso e parte da documentação formal."
5. **Premissa 5**: "Áreas de Aquisições e Partes Interessadas tratadas com simplificação pedagógica (stakeholder único: Prof. Nivaldo)."
6. **Premissa 6**: "Fases de Segurança, Acessibilidade, Observabilidade e i18n são tratadas como melhoria contínua pós-entrega, não como entregáveis obrigatórios do MVP acadêmico."

---

## 12. Condições de Validade e Gatilhos

**Válido enquanto**:
- Ementa da disciplina permitir abordagem híbrida (PMBOK 7ª + Ágil)
- Prof. Nivaldo mantiver o papel de stakeholder único formal
- Código continuar sendo deliverable formal

**Invalida se**:
- Professor exigir PMBOK 6ª como base **exclusiva** (regressão)
- Ementa migrar para framework ágil puro sem PMBOK
- Código deixar de ser deliverable formal
- Número de stakeholders expandir significativamente

**Gatilhos de reavaliação**:
- Novo artefato solicitado fora da árvore (seções 00-11)
- Mudança no critério de avaliação
- Scope creep detectado (> 15% de desvio do backlog original)
- Orientação verbal divergente deste guardrail

---

## 13. Instrução de Uso deste Guardrail

- **Durante redação**: consulte as seções 2, 3, 5, 6. Todo artefato deve passar pelo checklist da seção 10 antes de ser considerado "pronto".
- **Durante revisão**: consulte as seções 3, 10. Classifique achados em CRÍTICA/MÉDIA/BAIXA.
- **Durante conflito**: aplique a hierarquia da seção 2.1.
- **Durante dúvida sobre escopo**: consulte a seção 5 (árvore de artefatos). Se não estiver na árvore, **questione antes de produzir**.
- **Durante decisão técnica**: redija ADR e arquive em `09. Base de Conhecimento / 09.1. ADRs`.
- **Durante gestão do trabalho**: use o Kanban no GitHub Projects como fonte de verdade. O Gantt (se exigido) é derivado do Kanban, não o contrário.

---

## 14. Melhoria Contínua Pós-Entrega (Roadmap de Evolução)

Após a entrega do MVP acadêmico (Dezembro/2026), o projeto COGME pode evoluir para um produto profissional incorporando as seguintes fases:

### 14.1. Segurança e Privacidade (Prioridade: ALTA)
- Implementar análise de riscos OWASP Top 10
- Adequar à LGPD (política de privacidade, consentimento, direito ao esquecimento)
- Realizar pentest básico (ferramentas FOSS: OWASP ZAP)
- Documentar política de senhas e JWT

### 14.2. Acessibilidade (Prioridade: MÉDIA)
- Auditar WCAG 2.1 AA (ferramentas FOSS: Axe, Lighthouse)
- Testar com leitores de tela (NVDA, VoiceOver)
- Garantir contraste mínimo e navegação por teclado

### 14.3. Observabilidade (Prioridade: ALTA)
- Implementar logging estruturado (JSON)
- Adicionar health checks (/health, /warmup)
- Configurar métricas de negócio (simulações/dia, invoices geradas)
- Implementar alertas de falha (Keep-Alive via GitHub Actions)

### 14.4. Internacionalização (i18n) (Prioridade: BAIXA)
- Suporte completo a múltiplas moedas (formatação por locale)
- Preparar UI para tradução (i18next ou similar)
- Suporte a idiomas adicionais (EN, ES)

### 14.5. Integração com APIs Alternativas (Prioridade: ALTA)
- Implementar adapter pattern para múltiplos provedores de câmbio
- Adicionar fallback automático para API do Banco Central do Brasil (BCB)
- Garantir resiliência em caso de indisponibilidade da Frankfurter

---

## CONCLUSÃO DO GP SÊNIOR

Esta reformulação transforma um guardrail burocrático em um **sistema operacional híbrido** adequado à realidade do projeto COGME: equipe enxuta (2 pessoas), prazo apertado (3 meses), hardware potente, e stakeholder acadêmico exigente.

As principais mudanças em relação à v1.0:
1. **Redução de burocracia**: Árvore documental reduzida de 16 para 11 artefatos obrigatórios
2. **Foco no Kanban**: GitHub Projects substitui o Gantt como ferramenta primária de gestão
3. **Fases desejáveis movidas para pós-entrega**: Segurança, Acessibilidade, Observabilidade e i18n são tratadas como melhoria contínua, não como entregáveis obrigatórios
4. **Roadmap estratégico**: Visão de alto nível para comunicação com stakeholders, sem o detalhamento rígido do Gantt

As **4 fases obrigatórias adicionadas** (Comunicação, Base de Conhecimento, Gestão de Mudanças, Documentação) são **entregáveis críticos** que separam um projeto acadêmico medíocre de um produto profissional defensável.

**Próximo passo recomendado**: Submeter esta reformulação ao Prof. Dr. Nivaldo para validação formal, especialmente quanto à abertura para PMBOK 7ª e à exclusão das fases de Segurança/Acessibilidade/Observabilidade/i18n do MVP acadêmico.

---

**Versão do documento**: 2.1  
**Data de criação**: 07/09/2026  
**Autor**: GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)  
**Status**: Pronto para submissão ao stakeholder (Prof. Nivaldo)
