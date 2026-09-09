# REFORMULAÇÃO INTEGRAL DA BASE DE CONHECIMENTO DO PROJETO COGME

## PARTE 1 — CRÍTICA SEVERA DO ESTADO DA ARTE (DIAGNÓSTICO)

O documento atual ("RELATÓRIO ANALÍTICO — BASE DE CONHECIMENTO COMPLEMENTAR") apresenta **seis falhas estruturais** que o tornam inadequado como guardrail operacional para um projeto ágil com restrições reais de equipe e prazo:

### 1.1. Anacronismo Metodológico (PMBOK 6ª como Dogma)

O documento trata o PMBOK 6ª como **fonte primária de verdade**, quando a disciplina já permite abertura para PMBOK 7ª e práticas ágeis puras. Isso gera:

- **Redundância processual**: 49 processos do PMBOK 6ª mapeados 1:1 para rituais ágeis criam dupla contagem (ex: "6.4 Estimar Custos" ↔ "Planning Poker" são a mesma atividade vista por lentes diferentes).
- **Burocratização de artefatos**: A árvore documental atual (00 a 09) exige 10 documentos formais para uma equipe de 2 pessoas em 3 meses — isso é **anti-KISS** e viola o próprio princípio constitucional do projeto.

### 1.2. Ausência de Domínios de Desempenho (PMBOK 7ª)

O documento ignora completamente os **8 Domínios de Desempenho** do PMBOK 7ª (Stakeholders, Equipe, Abordagem de Desenvolvimento e Ciclo de Vida, Planejamento, Trabalho do Projeto, Entrega, Medição, Incerteza), que são mais adequados para projetos ágeis do que os 49 processos da 6ª edição.

### 1.3. EAP Incompleta (Fases Críticas Omitidas)

A EAP atual (11 fases) omite entregáveis essenciais para um MVP de produção web em 2026:

- **Comunicação formal** (não apenas "stakeholders")
- **Base de Conhecimento contínua** (ADRs, lições aprendidas)
- **Segurança e Privacidade** (LGPD, OWASP Top 10)
- **Acessibilidade** (WCAG 2.1 AA)
- **Observabilidade** (logs, métricas, tracing)
- **Internacionalização** (i18n — crítico para sistema de câmbio multi-moeda)
- **Gestão de Mudanças** (CCB formal)

### 1.4. Rastreabilidade Frágil

O documento exige "rastreabilidade ao TAP" mas não define **mecanismo concreto** (IDs, tags, links). Em projetos com SDD por IA, a rastreabilidade deve ser **automática via metadados de commit**, não manual.

### 1.5. Critérios de Qualidade Desalinhados com SDD

Os critérios de qualidade atuais (PDCA, DoR/DoD) não contemplam a realidade do **Specification-Driven Development com LLMs**, onde a qualidade deve ser medida por:

- Aderência do código gerado à especificação
- Taxa de alucinação/rejeição da IA
- Cobertura de testes dos _prompts_ críticos

### 1.6. Hierarquia de Conflitos Rígida Demais

A hierarquia atual (Ementa > PMBOK 6ª > PMBOK 7ª > Ágil > Literatura) é **inversa ao que um projeto ágil moderno exige**. Em 2026, a ordem correta é: **Valor entregue > Satisfação do stakeholder > Conformidade documental**.

---

## PARTE 2 — PROPOSTA DE REFORMULAÇÃO INTEGRAL

Abaixo, o novo documento substituto, estruturado como **Guardrail Operacional Híbrido** (PMBOK 7ª + Ágil + PMBOK 6ª complementar).

---

# BASE DE CONHECIMENTO OPERACIONAL — PROJETO COGME v2.0

## Veredito Sumário

O projeto COGME opera sob **hibridização evolutiva**: PMBOK 7ª (princípios e domínios de desempenho) como governança primária, Kanban como método de execução, e PMBOK 6ª como dicionário de processos complementares quando necessário. A base de conhecimento funciona como **árbitro de conflitos** e **fonte única de verdade técnica**, não como catálogo burocrático.

## 1. Princípios Constitutivos do Projeto (Imutáveis)

| #   | Princípio                            | Fundamentação                                                                     |
| --- | ------------------------------------ | --------------------------------------------------------------------------------- |
| P1  | **Valor sobre documentação**         | PMBOK 7ª — Princípio 1: "Seja um administrador diligente, respeitoso e cuidadoso" |
| P2  | **FOSS absoluto**                    | Restrição pedagógica + valor social (TAP §2.4)                                    |
| P3  | **KISS como métrica de arquitetura** | Cada decisão técnica deve ser justificada pela simplicidade                       |
| P4  | **SDD com IA auditável**             | Todo código gerado por LLM deve ter rastreabilidade via commit                    |
| P5  | **ACID e Clean Code como padrão**    | Restrição técnica inegociável                                                     |
| P6  | **Entrega incremental**              | Kanban + fluxos contínuos (sem sprints fixas)                                     |
| P7  | **Stakeholder único formal**         | Prof. Dr. Nivaldo Carletto como patrocinador-avaliador                            |

## 2. Abordagem Híbrida de Governança

### 2.1. Hierarquia de Resolução de Conflitos (Revisada)

Em caso de contradição, aplicar na ordem:

1. **Valor entregue ao usuário final** (PMBOK 7ª — Domínio de Entrega)
2. **Ementa da disciplina + orientação do Prof. Nivaldo**
3. **PMBOK 7ª** (12 princípios + 8 domínios de desempenho)
4. **Manifesto Ágil + Kanban** (método de execução)
5. **PMBOK 6ª** (apenas como dicionário de processos quando necessário)
6. **Literatura técnica complementar**

**Regra de ouro**: Se houver conflito entre documentação e valor entregue, **o valor prevalece**, desde que justificado via ADR (Architecture Decision Record).

### 2.2. Mapeamento PMBOK 7ª ↔ Ágil ↔ PMBOK 6ª (Tripla Camada)

| Domínio PMBOK 7ª             | Ritual Ágil (Kanban)      | Processo PMBOK 6ª (quando aplicável) | Artefato              |
| ---------------------------- | ------------------------- | ------------------------------------ | --------------------- |
| Stakeholders                 | Review com Prof. Nivaldo  | 13.1 Identificar Stakeholders        | Matriz de comunicação |
| Equipe                       | Daily assíncrona (GitHub) | 9.1 Planejar Recursos                | RACI simplificado     |
| Abordagem de Desenvolvimento | Kanban flow               | 4.1 Desenvolver TAP                  | TAP + Guardrail       |
| Planejamento                 | Refinement semanal        | 5.2 Coletar Requisitos               | Backlog + EAP         |
| Trabalho do Projeto          | Pull system + WIP limits  | 4.3 Orientar e Gerenciar             | Código-fonte          |
| Entrega                      | Deploy contínuo           | 5.3 Criar EAP                        | MVP funcional         |
| Medição                      | Cycle time + Throughput   | 4.5 Monitorar e Controlar            | Dashboard GitHub      |
| Incerteza                    | Risk backlog              | 11.2 Identificar Riscos              | Matriz Prob./Impacto  |

## 3. Domínios de Desempenho (PMBOK 7ª) — Aplicação ao COGME

| Domínio                          | Meta Mensurável                                           | Responsável |
| -------------------------------- | --------------------------------------------------------- | ----------- |
| **Stakeholders**                 | 100% das entregas validadas pelo Prof. Nivaldo em até 48h | Gerente     |
| **Equipe**                       | Zero burnout (carga ≤ 20h/semana por membro)              | Auto-gestão |
| **Abordagem de Desenvolvimento** | 100% FOSS + Kanban + SDD auditável                        | Devs        |
| **Planejamento**                 | Backlog refinado semanalmente com DoR claro               | Gerente     |
| **Trabalho do Projeto**          | Cycle time médio ≤ 3 dias por card                        | Devs        |
| **Entrega**                      | MVP funcional até Nov/2026 com ≥ 80% cobertura de testes  | Devs        |
| **Medição**                      | SPI ≥ 0.9 e CPI ≥ 0.9 quinzenalmente                      | Gerente     |
| **Incerteza**                    | Zero riscos críticos sem plano de resposta                | Gerente     |

## 4. Critérios de Qualidade Unificados (PDCA + DoD + SDD)

Todo artefato deve satisfazer **simultaneamente**:

### 4.1. Dimensão PMBOK 7ª (Valor)

- Deriva de um princípio constitucional (P1 a P7)
- Atende a um domínio de desempenho mensurável
- Gera valor tangível ao stakeholder

### 4.2. Dimensão Ágil (Fluxo)

- DoR (Definition of Ready) antes de produzir
- DoD (Definition of Done) após produzir
- Card no Kanban com ciclo de vida rastreável

### 4.3. Dimensão SDD (IA Auditável)

- Prompt de geração registrado em `/docs/prompts/`
- Código gerado revisado e commitado com assinatura
- Testes automatizados cobrindo a especificação

### 4.4. Dimensão PDCA (Melhoria Contínua)

- **Plan**: artefato versionado (v0.1, v0.2, v1.0)
- **Do**: produção conforme escopo
- **Check**: revisão automática (CI) + manual (pair review)
- **Act**: ajuste via ADR se necessário

## 5. Estrutura Documental Obrigatória (Árvore de Artefatos v2.0)

```
PROJETO COGME
├── 00. TAP (Termo de Abertura)
├── 01. Plano de Integração (guarda-chuva)
├── 02. Plano de Escopo + EAP/WBS + Dicionário
├── 03. Plano de Cronograma + Gantt + Roadmap
├── 04. Plano de Custos + Orçamento + Curva S
├── 05. Plano de Qualidade + Métricas + DoD/DoR
├── 06. Plano de Recursos + RACI + Histograma
├── 07. Plano de Comunicações + Matriz + Canais
├── 08. Plano de Riscos + Matriz + Respostas
├── 09. Plano de Segurança e Privacidade (LGPD/OWASP)
├── 10. Plano de Acessibilidade (WCAG 2.1 AA)
├── 11. Base de Conhecimento
│   ├── 11.1. ADRs (Architecture Decision Records)
│   ├── 11.2. Lições Aprendidas Contínuas
│   ├── 11.3. Prompts de SDD Catalogados
│   └── 11.4. Runbooks Operacionais
├── 12. Plano de Observabilidade (Logs, Métricas, Tracing)
├── 13. Plano de Internacionalização (i18n)
├── 14. Plano de Gestão de Mudanças (CCB)
└── 15. Código-Fonte (MVP full-stack) + DER + Diagramas
```

**Regra de consistência**: Todo artefato 02-14 deve referenciar explicitamente o TAP (seção X, parágrafo Y) e possuir um ADR associado quando houver decisão técnica relevante.

## 6. EAP Revisada e Expandida (16 Fases)

### NÍVEL 0 (RAIZ)

📁 **Projeto COGME — Conversor de Ganhos em Moeda Estrangeira**

### NÍVEL 1 e 2 (FASES E ENTREGÁVEIS)

| Fase (Nível 1)                              | Subfases / Pacotes de Trabalho (Nível 2)                                                                                                                                                                                   |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Iniciação e Planejamento**             | 1.1. TAP<br>1.2. Identificação de Stakeholders<br>1.3. Planos de Gerenciamento (Escopo, Cronograma, Custo, Riscos)<br>1.4. Plano da Qualidade<br>1.5. Política de Licenciamento FOSS<br>1.6. Definição do Backlog e Kanban |
| **2. Levantamento e Análise de Requisitos** | 2.1. Requisitos Funcionais<br>2.2. Requisitos Não Funcionais<br>2.3. Casos de Uso e Histórias de Usuário                                                                                                                   |
| **3. Modelagem e Prototipação**             | 3.1. Arquitetura da Solução<br>3.2. Protótipo UX/UI<br>3.3. Modelagem de Dados (DER)                                                                                                                                       |
| **4. Configuração de Ambiente**             | 4.1. Seleção e Validação da Stack FOSS<br>4.2. Repositório Git + CI/CD<br>4.3. Setup Local e Homologação<br>4.4. Auditoria de Licenças                                                                                     |
| **5. Desenvolvimento do Sistema**           | 5.1. Backend (Lógica de Negócio)<br>5.2. Backend (API de Câmbio + Cache)<br>5.3. Frontend (Interface)<br>5.4. Módulo PDF (WeasyPrint)<br>5.5. SDD com IA (Prompts + Revisão)<br>5.6. Execução Kanban (Rituais)             |
| **6. Garantia da Qualidade e Testes**       | 6.1. Testes Unitários/Integração (≥ 80%)<br>6.2. Testes de Aceitação (UAT)<br>6.3. Testes de Performance e Carga                                                                                                           |
| **7. DevOps e CI/CD**                       | 7.1. Pipeline CI (lint + testes)<br>7.2. Pipeline CD (build + deploy)                                                                                                                                                      |
| **8. Implantação (Deploy)**                 | 8.1. Publicação em Produção<br>8.2. Documentação de Deploy + Rollback                                                                                                                                                      |
| **9. Comunicação** ⭐                       | 9.1. Matriz de Comunicação (RACI)<br>9.2. Canais Oficiais (GitHub, e-mail, reuniões)<br>9.3. Relatórios de Status Quinzenais<br>9.4. Cerimônias com Stakeholder (Prof. Nivaldo)                                            |
| **10. Base de Conhecimento** ⭐             | 10.1. ADRs (decisões arquiteturais)<br>10.2. Lições Aprendidas Contínuas (Retrospectivas)<br>10.3. Catálogo de Prompts SDD<br>10.4. Runbooks Operacionais                                                                  |
| **11. Segurança e Privacidade** ⭐          | 11.1. Análise de Riscos (OWASP Top 10)<br>11.2. Conformidade LGPD (dados pessoais)<br>11.3. Testes de Segurança (pentest básico)<br>11.4. Política de Senhas e JWT                                                         |
| **12. Acessibilidade** ⭐                   | 12.1. Auditoria WCAG 2.1 AA<br>12.2. Testes com leitores de tela<br>12.3. Contraste e navegação por teclado                                                                                                                |
| **13. Observabilidade** ⭐                  | 13.1. Logging Estruturado (JSON)<br>13.2. Health Checks (/health, /warmup)<br>13.3. Métricas de Negócio (simulações/dia)<br>13.4. Alertas de Falha (Keep-Alive)                                                            |
| **14. Internacionalização (i18n)** ⭐       | 14.1. Suporte a múltiplas moedas (USD, EUR, GBP, BRL)<br>14.2. Formatação de datas e números por locale<br>14.3. Preparação para tradução de UI (futuro)                                                                   |
| **15. Gestão de Mudanças** ⭐               | 15.1. CCB (Change Control Board) — Prof. Nivaldo<br>15.2. Registro de Solicitações de Mudança<br>15.3. Análise de Impacto (escopo/custo/prazo)<br>15.4. Aprovação e Versionamento                                          |
| **16. Encerramento**                        | 16.1. Lições Aprendidas Finais<br>16.2. Verificação SMART<br>16.3. Apresentação Final + Aceite<br>16.4. Auditoria FOSS Final                                                                                               |

⭐ = **Fases novas adicionadas nesta reformulação**

## 7. Justificativa das Novas Fases Adicionadas

| Fase                            | Por que é crítica para o COGME?                                                                                         | Risco se omitida                                                                      |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **9. Comunicação**              | Equipe de 2 pessoas + stakeholder único exige fluxo formal para evitar ruído e garantir rastreabilidade de decisões.    | Decisões verbais não documentadas geram retrabalho e reprovação acadêmica.            |
| **10. Base de Conhecimento**    | SDD com IA gera conhecimento tácito (prompts, ADRs) que precisa ser capturado para não se perder entre desenvolvedores. | Perda de conhecimento em caso de afastamento de um membro; repetição de erros.        |
| **11. Segurança e Privacidade** | Sistema lida com dados pessoais (CPF/CNPJ, dados bancários) e financeiros. LGPD é obrigatório no Brasil.                | Vazamento de dados = reprovação + processo legal + dano reputacional.                 |
| **12. Acessibilidade**          | Projeto acadêmico em instituição pública deve ser inclusivo. WCAG 2.1 AA é padrão mínimo.                               | Exclusão de usuários com deficiência; nota acadêmica reduzida.                        |
| **13. Observabilidade**         | Sistema depende de API externa (Frankfurter) e será hospedado em ambiente gratuito instável.                            | Impossibilidade de diagnosticar falhas em produção; cold starts não detectados.       |
| **14. Internacionalização**     | Sistema de câmbio multi-moeda **exige** tratamento correto de locales (formato de moeda, datas, separadores).           | Valores exibidos incorretamente (ex: 1.000,00 vs 1,000.00) geram erros fiscais.       |
| **15. Gestão de Mudanças**      | Prazo apertado + escopo ambicioso exigem controle formal de mudanças para evitar scope creep.                           | Scope creep inviabiliza entrega no prazo; professor questiona mudanças não aprovadas. |

## 8. Regras de Redação (Persona Redatora v2.0)

1. Linguagem técnica PMBOK 7ª + ágil, impessoal, objetiva
2. Citar **princípio ou domínio PMBOK 7ª** quando aplicável (ex: "conforme Domínio de Entrega do PMBOK 7ª")
3. Declarar premissas, restrições e fatores de risco explicitamente
4. **Sempre usar métricas** ("critério de aceite: 95% dos casos de teste passing") — nunca linguagem genérica
5. Cada seção deve responder: **O quê? Por quê? Quem? Quando? Como? Quanto?**
6. Para decisões técnicas: redigir ADR (Architecture Decision Record) no formato: Contexto → Decisão → Consequências

## 9. Regras de Revisão (Persona Revisora v2.0)

Para cada artefato, validar os **7 critérios**:

| #   | Critério             | Pergunta-Chave                                   |
| --- | -------------------- | ------------------------------------------------ |
| 1   | **Rastreabilidade**  | Deriva do TAP ou de um princípio constitucional? |
| 2   | **Consistência**     | Datas/custos/escopo batem com outros planos?     |
| 3   | **Valor (PMBOK 7ª)** | Atende a um domínio de desempenho?               |
| 4   | **Fluxo Ágil**       | DoR/DoD claros? Card no Kanban?                  |
| 5   | **SDD Auditável**    | Prompts registrados? Código testado?             |
| 6   | **Executabilidade**  | Código corresponde ao escopo documentado?        |
| 7   | **Linguagem**        | Técnica, sem floreio, sem ambiguidade?           |

Classificar achados: **CRÍTICA** (bloqueante) | **MÉDIA** (deve corrigir) | **BAIXA** (sugestão)

## 10. Declarações Obrigatórias no TAP (Atualizadas)

1. **Premissa 1**: "PMBOK 7ª adotado como governança primária (princípios e domínios), com PMBOK 6ª como dicionário complementar de processos quando necessário."
2. **Premissa 2**: "Metodologia ágil Kanban adotada como método de execução, com rituais mapeados aos domínios PMBOK 7ª."
3. **Premissa 3**: "Uso de LLM como ferramenta auxiliar autorizada, com rastreabilidade via ADRs e prompts catalogados na Base de Conhecimento."
4. **Premissa 4**: "Código-fonte (MVP full-stack) constitui marco de sucesso e parte da documentação formal."
5. **Premissa 5**: "Áreas de Aquisições e Partes Interessadas tratadas com simplificação pedagógica (stakeholder único: Prof. Nivaldo)."
6. **Premissa 6**: "Segurança, privacidade (LGPD) e acessibilidade (WCAG 2.1 AA) são requisitos não funcionais inegociáveis."

## 11. Condições de Validade e Gatilhos

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

- Novo artefato solicitado fora da árvore (seções 00-15)
- Mudança no critério de avaliação
- Scope creep detectado (> 15% de desvio do backlog original)
- Orientação verbal divergente deste guardrail

## 12. Instrução de Uso deste Guardrail

- **Durante redação**: consulte as seções 2, 3, 5, 6. Todo artefato deve passar pelo checklist da seção 9 antes de ser considerado "pronto".
- **Durante revisão**: consulte as seções 3, 9. Classifique achados em CRÍTICA/MÉDIA/BAIXA.
- **Durante conflito**: aplique a hierarquia da seção 2.1.
- **Durante dúvida sobre escopo**: consulte a seção 5 (árvore de artefatos). Se não estiver na árvore, **questione antes de produzir**.
- **Durante decisão técnica**: redija ADR e arquive em `11. Base de Conhecimento / 11.1. ADRs`.

---

## PARTE 3 — FASES ADICIONAIS SUGERIDAS (NÃO CONTEMPLADAS NO MVP ORIGINAL)

Além das 7 fases já incorporadas na EAP v2.0 (Comunicação, Base de Conhecimento, Segurança, Acessibilidade, Observabilidade, i18n, Gestão de Mudanças), sugiro **avaliação crítica** das seguintes fases, que podem ser incorporadas conforme maturidade do projeto:

### 17. Gestão de Dados e Backup (Avaliar)

- **Justificativa**: Sistema armazena dados financeiros sensíveis. Perda de dados = fracasso do projeto.
- **Entregáveis**: Política de backup (pg_dump automatizado), estratégia de restore, testes de recuperação.
- **Prioridade**: ALTA — deve ser incorporada imediatamente.

### 18. Performance e Otimização (Avaliar)

- **Justificativa**: RNF-02 exige tempo de resposta ≤ 3s. Sem fase dedicada, otimização vira "bombeiro".
- **Entregáveis**: Testes de carga (k6/Locust), profiling de queries SQL, otimização de assets front-end.
- **Prioridade**: MÉDIA — pode ser subfase da fase 6 (Qualidade).

### 19. Documentação para o Usuário Final (Avaliar)

- **Justificativa**: MVP será usado por profissionais reais (PJ/freelancers). Sem manual, adoção falha.
- **Entregáveis**: Manual do usuário, FAQ, tutoriais em vídeo (opcional).
- **Prioridade**: MÉDIA — pode ser subfase da fase 16 (Encerramento).

### 20. Sustentabilidade e Manutenção (Avaliar)

- **Justificativa**: Projeto acadêmico deve ter vida pós-entrega (filosofia FOSS).
- **Entregáveis**: Guia de contribuição, CODE_OF_CONDUCT, roadmap de evoluções futuras.
- **Prioridade**: BAIXA — pode ser pós-encerramento.

### 21. Integração com APIs Alternativas (Avaliar)

- **Justificativa**: Frankfurter tem limite de 1000 req/dia. BCB como fallback é mandatório para resiliência.
- **Entregáveis**: Adapter pattern para múltiplos provedores de câmbio, fallback automático.
- **Prioridade**: ALTA — deve ser incorporada na fase 5.2 (API de Câmbio).

### 22. Gestão de Configuração e Versionamento de Dados (Avaliar)

- **Justificativa**: Migrações de banco (Alembic) e versionamento de schemas são críticos para ACID.
- **Entregáveis**: Política de migrações, rollback de schemas, seed de dados de teste.
- **Prioridade**: ALTA — deve ser subfase da fase 4 (Configuração de Ambiente).

---

## CONCLUSÃO DO GP SÊNIOR

A reformulação transforma um guardrail **burocrático e anacrônico** (PMBOK 6ª-cêntrico) em um **sistema operacional híbrido** (PMBOK 7ª + Ágil + SDD) adequado à realidade do projeto COGME: equipe enxuta, prazo apertado, hardware potente, e stakeholder acadêmico exigente.

As **7 novas fases** adicionadas à EAP não são "enfeite" — são **entregáveis críticos** que separam um projeto acadêmico medíocre de um produto profissional defensável. A omissão de qualquer uma delas expõe o projeto a riscos de reprovação, falha técnica ou dano reputacional.

**Próximo passo recomendado**: Submeter esta reformulação ao Prof. Dr. Nivaldo para validação formal, especialmente quanto à abertura para PMBOK 7ª e às 7 novas fases. Caso haja resistência, manter PMBOK 6ª como governança mas **incorporar obrigatoriamente** as fases 9 (Comunicação), 10 (Base de Conhecimento) e 11 (Segurança) — as três mais críticas.

Deseja que eu avance para a **formalização dos ADRs (Architecture Decision Records)** das decisões técnicas já tomadas (stack, cache, PDF, JWT), ou prefere que eu elabore o **Plano de Comunicações** (fase 9) como próximo artefato?
