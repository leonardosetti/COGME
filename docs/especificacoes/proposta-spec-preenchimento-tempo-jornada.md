---
id: docs-especificacoes-proposta-spec-preenchimento-tempo-jornada
title: Proposta de Spec — Preenchimento de Tempo por Regime de Jornada
type: proposta-spec
version: 1.0.0
status: aceita
owner: agent-project-analyst
derived-from:
- docs/conhecimento/templates/proposta-spec-template.md (template v1.1.0, 2026-11-07)
- constitution.md Art. 1.2 (escopo: simulação, 5 regimes de contratação)
- .ai/specs/spec-004-backend-mvp-v1.spec.md §3 (contrato Regime + quantity)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md (US-002 five-engagement-regimes)
last-revised: '2026-11-13'
lgpd-class: n/a
tags:
- proposta
- spec
- jornada
- tempo
- calendário
- feriados
---

# Proposta de Spec — Preenchimento de Tempo por Regime de Jornada

> Preencha as seções abaixo. O agente especialista avaliará viabilidade, custo, aderência e definirá critérios de aceite para promoção à spec oficial.

---

## 1. Ideia / Draft (obrigatório)

**Título da proposta:** Preenchimento de tempo por regime de jornada (horas / dias / semanas / mês)

**Autor:** Proponente (usuário/PO) — a definir no CCB

**Data:** 2026-11-13

**Contexto / problema que resolve:**
Hoje o usuário escolhe o tipo de jornada (horas, dias, semanas ou mês) na tela de simulação, mas o preenchimento do montante de tempo é genérico e não reflete a natureza de cada regime:
- Regime horário: não há campo dedicado a informar horas acumuladas de trabalho ou estimativa.
- Regime diário: não há calendário para definir início/fim, seleção de dias individuais, dias corridos ou exclusão de fins de semana/feriados.
- Regime semanal: não há seleção de semanas no calendário.
- Regime mensal: não há seleção de meses no calendário (e não deve contabilizar período por dias).

O contrato canônico já existe (`spec-004` §3: `Regime = hourly|daily|weekly|monthly|fixed` + `quantity`), e `US-002 five-engagement-regimes` (spec-002) exige que todos os regimes calculem resultado com parâmetros válidos. Esta proposta fecha a lacuna de UX/modelo de dados para preencher `quantity` (ou seu equivalente por regime) de forma adequada a cada tipo de jornada.

**Descrição breve da solução proposta:**
Estender a entrada de simulação para que, conforme o regime escolhido, o usuário preencha o tempo da forma natural a esse regime:
- **horas:** campo numérico de montante de horas acumuladas de trabalho ou estimativa.
- **dias:** calendário com seleção de início e fim do período; opções de dias corridos, dias individuais, exclusão de fins de semana e/ou feriados. Tabela de feriados persistida no banco, customizável por região/país.
- **semanas:** calendário com seleção de semanas (contagem de semanas, não de dias).
- **mês:** calendário com seleção de meses (contagem de meses, sem contabilizar dias).
O regime "valor fixo" (fixed) já existente no contrato permanece inalterado (fora do escopo desta proposta).

**Escopo inicial (o que está DENTRO):**
- Campo de horas para regime horário.
- Componente de calendário para regime diário (início/fim, dias individuais, dias corridos, excluir fins de semana, excluir feriados).
- Tabela de feriados no banco de dados, cadastro/edição por região/país.
- Seleção de semanas para regime semanal.
- Seleção de meses para regime mensal (sem contagem de dias).
- Validação de coerência entre regime escolhido e preenchimento de tempo.
- Mapeamento do preenchimento para o campo `quantity` (ou equivalente) do contrato `spec-004`.

**Fora de escopo (o que NÃO está):**
- Regime "valor fixo" (fixed) — já contemplado pelo contrato, não entra nesta proposta.
- Autenticação/multi-usuário (fora do Art. 1.2, OS-01).
- Novas moedas, NF-e/NFS-e, app mobile nativo, gráficos, painel admin (OS-02..OS-09).
- Histórico/auditoria de alterações de feriados (pode ser adicionado depois).
- Cálculo de dias úteis/feriados na regra de negócio do valor final — apenas a contagem de tempo de jornada; a fórmula de cálculo permanece em `spec-004`/`spec-002` (cláusula "sem calendário corporativo" no cálculo líquido, per review:17).

---

## 2. Análise de Derivação Multi-Spec (NOVO)

> **Regra:** Uma única proposta pode gerar **múltiplas specs independentes** se atender a **QUALQUER** dos critérios abaixo. O avaliador deve marcar e justificar.

| Critério de Divisão | Aplica-se? (Sim/Não) | Justificativa / Specs Resultantes |
|---------------------|----------------------|-----------------------------------|
| Domínios técnicos disjuntos (ex: backend + frontend + infra) | Não | O domínio (preenchimento de tempo de jornada) é coeso; frontend (calendário) e backend (validação + tabela de feriados) entregam uma única funcionalidade de usuário. |
| Entregáveis com ciclos de vida independentes (deploy, versão, dono) | Não | Tudo é parte da mesma tela de simulação e da mesma versão do produto. |
| Stakeholders / OKRs distintos por módulo | Não | Mesmo PO/usuário final, mesmo OKR de usabilidade da simulação. |
| Complexidade total > threshold da wave (ex: > 40h dev) | Não | Estimativa inferior ao threshold (ver Seção 5); viável como uma onda. |
| Requisitos regulatórios / compliance separados por módulo | Não | Feriados não são dados pessoais (LGPD não se aplica); sem compliance separado. |
| Dependências técnicas que permitem desenvolvimento paralelo | Não | A tabela de feriados é dependência do calendário diário; não há paralelo que justifique divisão. |

**Resultado da análise:**
- [x] **Uma spec única** — proposta mantida como escopo coeso
- [ ] **Múltiplas specs** — listar abaixo:

> Se múltiplas specs: cada uma segue fluxo independente a partir da **Seção 6** (critérios de aceite individuais).

---

## 3. Viabilidade Técnica (para avaliação do agente)

| Critério | Avaliação (Sim/Parcial/Não) | Observações |
|----------|----------------------------|-------------|
| Tecnologias necessárias existem no stack atual? | Sim | FastAPI + Jinja2 + Vanilla JS (sem build step), SQL/Alembic para tabela de feriados, `spec-004` já define contrato Regime/quantity. |
| Requer nova dependência externa? | Não | Calendário em Vanilla JS/CSS (sem biblioteca externa); tabela de feriados no banco existente. |
| Impacta arquitetura existente (camadas, contratos)? | Parcial | Estende o preenchimento de `quantity` do contrato `spec-004` e adiciona uma tabela de feriados; não altera o contrato HTTP nem os regimes existentes. |
| Complexidade estimada (baixa/média/alta)? | Média | Calendário interativo + tabela de feriados por região/país é a parte mais complexa. |
| Riscos técnicos conhecidos? | Sim | Consistência entre preenchimento de calendário e `quantity`; feriados customizados exigem manutenção contínua por região/país; evitar sobreposição com cláusula "sem calendário corporativo" do cálculo líquido. |

---

## 4. Viabilidade Negocial (para avaliação do agente)

| Critério | Avaliação | Observações |
|----------|-----------|-------------|
| Alinhado com OKRs / roadmap do produto? | Sim | Atende US-002 (5 regimes operacionais em UAT) e REQ-02 (regimes de contratação). |
| Gera valor mensurável para usuário final? | Sim | Preenchimento natural por regime reduz erros de entrada e melhora a precisão da estimativa de jornada. |
| Esforço estimado vs. retorno (ROI qualitativo)? | Sim | Esforço médio, retorno direto na usabilidade da tela principal do produto. |
| Dependências de outras teams / stakeholders? | Não | PO/CCB define regiões/países iniciais de feriados; dev executa. |
| Janela de oportunidade / urgência? | Média | Não é bloqueante para o MVP, mas melhora materialmente a simulação antes da promoção à spec oficial. |

---

## 5. Custo Técnico Estimado

| Item | Estimativa | Notas |
|------|------------|-------|
| Horas de desenvolvimento (dev) | 24–32 h | Backend (tabela feriados, validação, mapeamento quantity) + frontend (calendário Vanilla JS). |
| Horas de design / UX | 8–12 h | Fluxo de seleção por regime, estados de calendário, acessibilidade. |
| Horas de QA / testes | 8–12 h | Testes de validação por regime, calendário, feriados por região. |
| Infra / custos recorrentes | 0 | Sem nova infra; tabela no banco existente. |
| Dívida técnica introduzida (se houver) | Baixa | Tabela de feriados requer manutenção de dados por região/país (não é código). |
| **Total estimado** | **40–56 h** | Dentro do threshold de uma única onda/spec. |

---

## 6. Aderência ao Projeto / Produto

- **Princípios constitucionais atendidos?** (constitution.md Art. 2) — Sim. Alinha ao escopo canônico (simulação, 5 regimes de contratação) e ao congelamento do TAP v3 (ADR-005); nada fora do escopo congelado entra sem emenda constitucional prévia (Art. 1.3).
- **Compatível com AGENT_TOPOLOGY e ondas de produção?** (plano-producao-agentes.md) — Sim. Entregável em uma onda, agente dono a definir (agent-sdd-specialist para a spec, agent-project-analyst para avaliação).
- **LGPD / Marco Civil / soberania de dados?** — Sim. Feriados não são dados pessoais; sem coleta de dados do usuário além do já existente na simulação.
- **FOSS-first / zero vendor lock-in?** — Sim. Vanilla JS sem biblioteca externa; banco existente; sem serviços de terceiros para feriados (cadastro manual/região).

---

## 7. Critérios de Aceite para Promoção à Spec

A proposta será promovida a **spec oficial** se **TODOS** forem atendidos:

- [x] Viabilidade técnica: **Sim** (sem bloqueadores)
- [x] Viabilidade negocial: **Sim**
- [x] Custo técnico: **Aprovado pelo PO/PM** — assinatura CCB registrada (usuário/PO, 2026-11-13); custo estimado 40–56 h, dentro do threshold de uma onda.
- [x] Aderência: **100% nos 4 itens da seção 6**
- [x] Riscos mapeados com plano de mitigação (consistência calendário × quantity; manutenção de feriados por região/país; não misturar com cálculo líquido "sem calendário corporativo")
- [x] Definição de **Done** clara para a spec (entregáveis, validação)

> Se algum critério falhar → **Rejeitada** com justificativa registrada no ledger.

---

### Decisão de promoção e promulgação (CCB)

- **Avaliador primário:** `agent-project-analyst`
- **Veredito:** APROVADA — promovida a spec oficial
- **Ratificação / assinatura CCB:** usuário/PO (CCB), 2026-11-13 — custo técnico aprovado e spec promulgada
- **Spec gerada:** `spec-016-preenchimento-tempo-jornada-v1` (`.ai/specs/spec-016-preenchimento-tempo-jornada-v1.spec.md`)
- **parcel.dod:** true
- **Data da decisão:** 2026-11-13
- **Registro:** ledger (via `nexus-prime-ultimate`)
- **Status da proposta:** promulgada

---

## 8. Agentes Responsáveis pela Análise e Decisão

> Conforme **AGENT_TOPOLOGY** e **registry.yaml** (SSOT). O **nexus-prime-ultimate (L0)** roteia a proposta para **exatamente UM** agente avaliador primário, conforme domínio da proposta.

### 8.1 Agentes Avaliadores Primários (por domínio)

| Domínio da Proposta | Agente Primário (slug) | Camada | Papel |
|---------------------|------------------------|--------|-------|
| Especificação SDD, contratos, specs formais | `agent-sdd-specialist` | L1 | specialist |
| Análise de projeto, métricas, auditoria, health checks | `agent-project-analyst` | L1 | analyst |

Avaliador primário sugerido para esta proposta: **`agent-project-analyst`** (análise de proposta/especificação), com suporte de `agent-sdd-specialist` para o contrato de dados e `agent-qa-sdet` para critérios de teste.

### 8.2 Orquestração e Escalação

| Situação | Agente / Ação |
|----------|---------------|
| Roteiro inicial (validação envelope + dispatch) | `nexus-prime-ultimate` (L0 orchestrator) |
| Conflito de domínio / proposta transversal > 1 agente | `nexus-prime-ultimate` escala para **Human (PM/CCB)** em PT-BR |
| Kill Switch acionado (qualquer violação constitucional) | `nexus-prime-ultimate` → **BLOQUEIO IMEDIATO** + log + escalação Human |
| Bypass Protocol solicitado | `agent-compliance-governance` analisa → `nexus-prime-ultimate` despacha → Human ratifica |
| Promoção a spec oficial | Agente avaliador emite **parcel.dod=true** → `nexus-prime-ultimate` registra no ledger |

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

| Ação | Responsável | Prazo |
|------|-------------|-------|
| Refinar requisitos detalhados (histórias, ACs Given/When/Then) | agent-project-analyst / PO | a definir |
| Criar SPEC.md completo (SDD) com contrato de dados e UI | agent-sdd-specialist | a definir |
| Definir plano de testes / UAT por regime | agent-qa-sdet | a definir |
| Agendar implementação (wave) | nexus-prime-ultimate / PM | a definir |

---

## 11. Metadados de Controle

| Campo | Valor |
|-------|-------|
| ID da proposta | PROP-001 |
| Status | draft \| em_avaliacao \| aceita \| rejeitada \| multi-spec → **em_avaliacao** |
| Spec(s) gerada(s) (se aceita) | SPEC-preenchimento-tempo-jornada-v1 (a definir no .ai/specs/) |
| Link para issue / PR relacionado | a vincular pelo nexus |
| Histórico de decisões | — |
| Agente avaliador primário | agent-project-analyst (sugerido) |
| Data da decisão | — |

---
