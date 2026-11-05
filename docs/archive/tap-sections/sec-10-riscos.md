---
id: tap-sections-sec-10-riscos
title: Sec_10_Riscos
version: '2.0'
class: conhecimento
status: active
owner: agent-project-analyst
derived-from:
- docs/archive/tap-sections/sec-10-riscos.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- tap-sections
- docs
- normalizado
---
Esta seção documenta os principais riscos de alto nível identificados no projeto COGME, conforme o Processo 11.1 (Identificar Riscos) do PMBOK® 6ª edição e o Domínio de Incerteza do PMBOK® 7ª edição. Riscos são eventos ou condições incertas que, caso ocorram, podem impactar positiva ou negativamente os objetivos do projeto. Esta seção apresenta uma visão estratégica dos riscos; o detalhamento operacional (matriz completa, planos de contingência, gatilhos de resposta) será tratado no **Plano de Riscos (§08 da árvore documental)**.

**Regra de consistência:** Todo risco deve possuir (a) descrição clara do evento incerto, (b) probabilidade e impacto estimados, (c) severidade consolidada, (d) estratégia de resposta de alto nível, e (e) rastreabilidade aos Objetivos SMART do TAP §3.

#### 10.1. Principais Riscos de Alto Nível

| ID           | Risco                                                                                                                                                                                                                                               | Probabilidade | Impacto | Severidade            | Estratégia de Resposta                                                                                                                                                                                                                                   |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **R1** | **Entrega parcial (22/09/2026) não concluída no prazo**, comprometendo o marco de avaliação acadêmica e a transição para a MF2 (Construção).                                                                                         | Média (40%)  | Alto    | **ALTA**        | **Mitigar**: Aplicar princípio GMV (governança mínima viável) para priorizar artefatos obrigatórios; monitorar progresso semanalmente via GitHub Projects; acionar plano de contingência (redução de escopo não-crítico) se desvio > 15%. |
| **R2** | **Stack tecnológica FOSS selecionada apresentar instabilidade, incompatibilidade ou curva de aprendizado superior ao previsto**, impactando a Fase N5 (Desenvolvimento do Sistema) e o cronograma da MF2.                                    | Baixa (25%)   | Alto    | **ALTA**        | **Mitigar**: Validar stack com protótipo "Hello World" antes da Fase N5 (Fase N4.1); manter alternativas FOSS equivalentes identificadas; documentar decisão via ADR-002 para rastreabilidade.                                                    |
| **R3** | **Sobrecarga da equipe (burnout)** devido à acumulação de múltiplos papéis (gerência, desenvolvimento, testes, documentação) e conciliação com outras disciplinas, resultando em queda de produtividade ou afastamento temporário. | Média (50%)  | Médio  | **ALTA**        | **Mitigar**: Respeitar limite de 20h/semana por membro (Domínio de Equipe PMBOK 7ª); aplicar WIP limits no Kanban (máx. 3 cards em progresso por pessoa); monitorar métrica de burnout via self-report semanal.                                 |
| **R4** | **Cobertura de testes automatizados ficar abaixo da meta de 80%**, comprometendo o Critério de Qualidade (§3.2) e a confiabilidade do MVP entregue.                                                                                         | Média (45%)  | Alto    | **ALTA**        | **Mitigar**: Adotar abordagem TDD (Test-Driven Development) desde a Fase N5; integrar pipeline CI (Fase N7.1) com verificação automática de coverage; priorizar testes nos fluxos críticos (cálculo cambial, geração de PDF).                |
| **R5** | **API externa de cotação cambial apresentar indisponibilidade, instabilidade ou alteração de política de uso**, bloqueando a funcionalidade central de simulação em tempo real (REQ-01).                                               | Baixa (20%)   | Alto    | **MÉDIA-ALTA** | **Mitigar**: Implementar adapter pattern para permitir troca de provedor; manter cache local de cotações (Fase N5.2) como fallback; documentar provedor selecionado via ADR-002.                                                                  |

#### 10.2. Declaração de Rastreabilidade (Riscos → Objetivos SMART → EAP)

| Risco                | Objetivo SMART Afetado (TAP §3)              | Fases EAP v2.0 Relacionadas                               | Domínio PMBOK 7ª           |
| -------------------- | --------------------------------------------- | --------------------------------------------------------- | ---------------------------- |
| R1 (Entrega parcial) | Cronograma (Marcos) — 22/09/2026             | Macro-fase MF1 (todas as fases)                           | Abordagem de Desenvolvimento |
| R2 (Stack instável) | Produto (Escopo) — MVP funcional ≤ 3s       | N4.1 (Seleção da Stack), N5 (Desenvolvimento)           | Abordagem de Desenvolvimento |
| R3 (Burnout)         | Inovação e Ferramentas — FOSS + SDD com IA | Todas as fases (transversal)                              | Equipe                       |
| R4 (Coverage < 80%)  | Qualidade e Testes — ≥ 80% coverage         | N6.1 (Testes Unitários/Integração), N7.1 (Pipeline CI) | Medição                    |
| R5 (API externa)     | Produto (Escopo) — Simulação em tempo real | N5.2 (Backend — API de Câmbio + Cache)                  | Incerteza                    |

**Verificação de completude:** 100% dos Objetivos SMART do TAP §3 possuem ao menos um risco associado na seção §10.

#### 10.3. Observações sobre a Gestão de Riscos

1. **Riscos positivos (oportunidades)**: O projeto identifica como oportunidade o uso de IA generativa (SDD) para acelerar a produção de artefatos e código-fonte, desde que com rastreabilidade adequada (Critério de Inovação Controlada, §3.2).
2. **Reserva de contingência**: Dada a restrição de orçamento zero (§8.4), não há reserva financeira para contingências. A gestão de riscos depende de ações preventivas e adaptações rápidas, conforme princípio GMV.
3. **Monitoramento contínuo**: Os riscos serão monitorados quinzenalmente via GitHub Projects (label `risk` ou `blocked`), com revisão formal no Plano de Riscos (§08).
4. **Gatilhos de reavaliação**: Caso algum risco se materialize ou novos riscos sejam identificados com severidade CRÍTICA, o processo formal de gestão de mudanças (Fase N10 da EAP v2.0) será acionado.
