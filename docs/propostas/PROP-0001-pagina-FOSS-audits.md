---
id: <TBD>
title: Template de Proposta de Nova Spec
type: plano
version: 0.0.1
status: draft
owner: agent-project-analyst
derived-from:
- docs/conhecimento/templates/proposta-spec-template.md (criado em 2026-11-07)
- docs/conhecimento/templates/proposta-spec-template.md (atualizado em 2026-11-07: multi-spec + agentes responsáveis)
last-revised: '2026-11-07'
lgpd-class: n/a
tags:
- docs
- proposta
- spec
- avaliacao
---

## 1. Ideia / Draft (obrigatório)

**Título da proposta:** Página extra Auditoria FOSS
**Autor:** Leonardo Setti
**Data:** $date
**Contexto / problema que resolve:** Publica conformidade FOSS do projeto
**Descrição breve da solução proposta:** Listar toda a abordagem técnica e suas licenças com índice de taxa de conformidade ou boolean [FOSS/Não-FOSS | Atende/Não-Atende]
**Escopo inicial (o que está DENTRO):** Resultados de auditoria FOSS, relatório legível para qualquer pessoa para análise, para cada licença link para a política oficial da licença. a FRONTPAGE DO PROJETO DEVE INCLUIR LINK PARA ESTA PAGINA.
**Fora de escopo (o que NÃO está):** Não incluir descrição da licença

---

## 2. Análise de Derivação Multi-Spec

> **Regra:** Uma única proposta pode gerar **múltiplas specs independentes** se atender a **QUALQUER** dos critérios abaixo. O avaliador deve marcar e justificar.

| Critério de Divisão                                                 | Aplica-se? (Sim/Não) | Justificativa / Specs Resultantes |
| --------------------------------------------------------------------- | --------------------- | --------------------------------- |
| Domínios técnicos disjuntos (ex: backend + frontend + infra)        |                       |                                   |
| Entregáveis com ciclos de vida independentes (deploy, versão, dono) |                       |                                   |
| Stakeholders / OKRs distintos por módulo                             |                       |                                   |
| Complexidade total > threshold da wave (ex: > 40h dev)                |                       |                                   |
| Requisitos regulatórios / compliance separados por módulo           |                       |                                   |
| Dependências técnicas que permitem desenvolvimento paralelo         |                       |                                   |

**Resultado da análise:**

- [X] **Uma spec única** — proposta mantida como escopo coeso
- [ ] **Múltiplas specs** — listar abaixo:

| Spec Derivada (ID sugerido) | Título | Escopo Resumido | Agente Dono Sugerido |
| --------------------------- | ------- | --------------- | -------------------- |
| SPEC-XXXX-A                 |         |                 |                      |
| SPEC-XXXX-B                 |         |                 |                      |

> Se múltiplas specs: cada uma segue fluxo independente a partir da **Seção 6** (critérios de aceite individuais).

---

## 3. Viabilidade Técnica (para avaliação do agente)

| Critério                                           | Avaliação (Sim/Parcial/Não) | Observações |
| --------------------------------------------------- | ------------------------------ | ------------- |
| Tecnologias necessárias existem no stack atual?    |                                |               |
| Requer nova dependência externa?                   |                                |               |
| Impacta arquitetura existente (camadas, contratos)? |                                |               |
| Complexidade estimada (baixa/média/alta)?          |                                |               |
| Riscos técnicos conhecidos?                        |                                |               |

---

## 4. Viabilidade Negocial (para avaliação do agente)

| Critério                                        | Avaliação | Observações |
| ------------------------------------------------ | ----------- | ------------- |
| Alinhado com OKRs / roadmap do produto?          |             |               |
| Gera valor mensurável para usuário final?      |             |               |
| Esforço estimado vs. retorno (ROI qualitativo)? |             |               |
| Dependências de outras teams / stakeholders?    |             |               |
| Janela de oportunidade / urgência?              |             |               |

---

## 5. Custo Técnico Estimado

| Item                                     | Estimativa | Notas |
| ---------------------------------------- | ---------- | ----- |
| Horas de desenvolvimento (dev)           |            |       |
| Horas de design / UX                     |            |       |
| Horas de QA / testes                     |            |       |
| Infra / custos recorrentes               |            |       |
| Dívida técnica introduzida (se houver) |            |       |
| **Total estimado**                 |            |       |

---

## 6. Aderência ao Projeto / Produto

- **Princípios constitucionais atendidos?** (constitution.md Art. 2)
- **Compatível com AGENT_TOPOLOGY e ondas de produção?** (plano-producao-agentes.md)
- **LGPD / Marco Civil / soberania de dados?**
- **FOSS-first / zero vendor lock-in?**

---

## 7. Critérios de Aceite para Promoção à Spec

A proposta (ou cada spec derivada) será promovida a **spec oficial** se **TODOS** forem atendidos:

- [ ] Viabilidade técnica: **Sim** (sem bloqueadores)
- [ ] Viabilidade negocial: **Sim** ou **Parcial com mitigação documentada**
- [ ] Custo técnico: **Aprovado pelo PO/PM** (assinatura ou issue vinculada)
- [ ] Aderência: **100% nos 4 itens da seção 6**
- [ ] Riscos mapeados com plano de mitigação
- [ ] Definição de **Done** clara para a spec (entregáveis, validação)

> Se algum critério falhar → **Rejeitada** com justificativa registrada no ledger.

---

## 8. Agentes Responsáveis pela Análise e Decisão

> Conforme **AGENT_TOPOLOGY** e **registry.yaml** (SSOT). O **nexus-prime-ultimate (L0)** roteia a proposta para **exatamente UM** agente avaliador primário, conforme domínio da proposta.

### 8.1 Agentes Avaliadores Primários (por domínio)

| Domínio da Proposta                                                     | Agente Primário (slug)                         | Camada | Papel      |
| ------------------------------------------------------------------------ | ----------------------------------------------- | ------ | ---------- |
| Requisitos, processos, stakeholders, análise de negócio                | `agent-business-analysis-specialist`          | L1     | specialist |
| Arquitetura, stack, ADRs, decisões técnicas transversais               | `agent-architect`                             | L1     | specialist |
| Padrões de projeto, coding standards, templates, convenções           | `agent-project-patterns-standards-specialist` | L1     | specialist |
| Design de solução, UX/UI, padrões de design, esboços arquitetônicos | `agent-project-design-specialist`             | L1     | specialist |
| Especificação SDD, contratos, specs formais                            | `agent-sdd-specialist`                        | L1     | specialist |
| Compliance, LGPD, Marco Civil, licenças, Bypass Protocol                | `agent-compliance-governance`                 | L2     | specialist |
| Segurança digital, threat model, OWASP, CVE, segredos                   | `agent-digital-security`                      | L2     | specialist |
| Qualidade, SQA, portões de qualidade, atributos                         | `agent-quality-architect-specialist`          | L2     | specialist |
| QA/TESTES, SDET, automação, estratégia de teste                       | `agent-qa-sdet`                               | L2     | specialist |
| Processo SDLC, portões, critérios entrada/saída                       | `agent-sldc-process-specialist`               | L2     | specialist |
| Direitos autorais, licenciamento saída criativa                         | `agent-copyright-specialist`                  | L2     | specialist |
| Análise de projeto, métricas, auditoria, health checks                 | `agent-project-analyst`                       | L1     | analyst    |

### 8.2 Orquestração e Escalação

| Situação                                                             | Agente / Ação                                                                                 |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Roteamento inicial (validação envelope + dispatch)                   | `nexus-prime-ultimate` (L0 orchestrator)                                                      |
| Conflito de domínio / proposta transversal > 1 agente                 | `nexus-prime-ultimate` escala para **Human (PM/CCB)** em PT-BR                          |
| Kill Switch acionado (qualquer violação constitucional)              | `nexus-prime-ultimate` → **BLOQUEIO IMEDIATO** + log + escalação Human               |
| Bypass Protocol solicitado (3 pilares: força maior + FOSS exit + CCB) | `agent-compliance-governance` analisa → `nexus-prime-ultimate` despacha → Human ratifica  |
| Promoção a spec oficial (após critérios atendidos)                 | Agente avaliador emite **parcel.dod=true** → `nexus-prime-ultimate` registra no ledger |

### 8.3 Matriz de Decisão (RACI simplificado)

| Atividade                              | Nexus (L0)  | Avaliador Primário | Compliance (L2) | Human (PM/CCB) |
| -------------------------------------- | ----------- | ------------------- | --------------- | -------------- |
| Receber proposta / validar envelope    | **R** | I                   | I               | I              |
| Analisar viabilidade técnica/negocial | I           | **R/A**       | C               | I              |
| Verificar aderência constitucional    | I           | C                   | **R/A**   | I              |
| Decidir multi-spec vs. spec única     | C           | **R**         | C               | **A**    |
| Aprovar custo técnico (PO)            | I           | C                   | I               | **R/A**  |
| Emitir parcel.dod (promoção)         | **R** | A                   | I               | I              |
| Escalation / Kill Switch               | **R** | I                   | I               | **A**    |
| Ratificar Bypass                       | I           | I                   | C               | **R/A**  |

**Legenda:** R = Responsible (executa), A = Accountable (aprova), C = Consulted (consultado), I = Informed (informado)

---

## 9. Fluxo de Vida da Proposta (Atualizado)

```mermaid
flowchart TD
    A[proposta-spec] --> B{nexus: valida envelope}
    B -->|reject| C[rejeitada: envelope inválido]
    B -->|accept| D[roteia para avaliador primário]
    D --> E{análise multi-spec<br/>(Seção 2)}
    E -->|uma spec| F[avaliação única]
    E -->|múltiplas specs| G[divide em N specs<br/>cada uma com avaliação]
    F --> H{critérios Seção 7<br/>todos atendidos?}
    G --> H
    H -->|sim| I[promoção a spec oficial]
    H -->|não| J[rejeitada + justificativa no ledger]
    I --> K[refinamento / amadurecimento]
    K --> L[spec madura]
    L --> M[implementação (wave)]
    J --> N[arquivada]
```

---

## 10. Próximos Passos (após avaliação)

| Ação                         | Responsável | Prazo |
| ------------------------------ | ------------ | ----- |
| Refinar requisitos detalhados  |              |       |
| Criar SPEC.md completo (SDD)   |              |       |
| Definir plano de testes / UAT  |              |       |
| Agendar implementação (wave) |              |       |

---

## 11. Metadados de Controle

| Campo                            | Valor                                                      |
| -------------------------------- | ---------------------------------------------------------- |
| ID da proposta                   | PROP-XXXX                                                  |
| Status                           | draft \| em_avaliacao \| aceita \| rejeitada \| multi-spec |
| Spec(s) gerada(s) (se aceita)    | SPEC-XXXX-A, SPEC-XXXX-B, ...                              |
| Link para issue / PR relacionado |                                                            |
| Histórico de decisões          |                                                            |
| Agente avaliador primário       |                                                            |
| Data da decisão                 |                                                            |
