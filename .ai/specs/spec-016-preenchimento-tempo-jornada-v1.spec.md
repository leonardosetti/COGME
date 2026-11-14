---
id: ai-specs-spec-016-preenchimento-tempo-jornada-v1-spec
title: SPEC spec-016 — preenchimento-tempo-jornada-v1 — Preenchimento de tempo por regime de jornada
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/especificacoes/proposta-spec-preenchimento-tempo-jornada.md (PROP-001, aprovada e promulgada pelo CCB em 2026-11-13)
- constitution.md Art. 1.2 (escopo: simulação, 5 regimes de contratação)
- .ai/specs/spec-004-backend-mvp-v1.spec.md §3 (contrato Regime + quantity)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md (US-002 five-engagement-regimes)
last-revised: '2026-11-13'
lgpd-class: n/a
tags:
- specs
- docs
- adequado-a-norma
---
---
spec_id: spec-016
specname: preenchimento-tempo-jornada-v1
version: 1.0.0
status: ratificada
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-13
updated: 2026-11-13
origin: PROP-001 (docs/especificacoes/proposta-spec-preenchimento-tempo-jornada.md), aprovada pelo CCB em 2026-11-13
task: PROP-001 | sender: agent-project-analyst | kill_switch: inherited
trace:
  - docs/especificacoes/proposta-spec-preenchimento-tempo-jornada.md (PROP-001, proposta aprovada)
  - .ai/specs/spec-004-backend-mvp-v1.spec.md §3 (contrato Regime = hourly|daily|weekly|monthly|fixed + quantity)
  - .ai/specs/spec-002-requisitos-review-round-1.spec.md (US-002 five-engagement-regimes; REQ-02 regimes de contratação)
  - constitution.md Art. 1.2 e Art. 1.3 (escopo canônico e congelamento TAP v3)
lgpd-class: n/a
---

# SPEC spec-016 — preenchimento-tempo-jornada-v1 — Preenchimento de tempo por regime de jornada

Status: RATIFICADA — contrato de preenchimento de tempo por regime de jornada emitido; complementa a `spec-004` (contrato HTTP `POST /v1/simulate`) e a `US-002` (5 regimes operacionais em UAT). Não altera o contrato HTTP nem os regimes existentes; define a forma de preenchimento do campo `quantity` (ou equivalente) por regime.

## 1. Contexto e origem

Emitida a partir da PROP-001 (docs/especificacoes/proposta-spec-preenchimento-tempo-jornada.md), aprovada pelo CCB em 2026-11-13. Fecha a lacuna de UX/modelo de dados para preencher o montante de tempo da simulação de forma natural a cada regime de jornada (hora, dia, semana, mês), já previstos no contrato `spec-004` §3 (`Regime = hourly|daily|weekly|monthly|fixed` + `quantity`) e exigidos por `US-002 five-engagement-regimes` (spec-002).

O regime "valor fixo" (`fixed`) já contemplado pelo contrato permanece inalterado e está fora do escopo desta spec.

## 2. Resolução de conflitos

| Tema | Decisão desta spec | Fonte vencedora | Texto superado / não promovido |
|------|-------------------|-----------------|--------------------------------|
| Regime de preenchimento por jornada | Cada regime preenche o tempo de forma natural: horas (campo numérico), dias (calendário início/fim com opções), semanas (seleção de semanas), mês (seleção de meses) | PROP-001 + spec-004 §3 + spec-002 US-002 | Nenhum texto prévio; lacuna de UX aberta |
| Regime "valor fixo" (fixed) | Permanece inalterado, fora do escopo | PROP-001 escopo | Não entra nesta spec |
| Cálculo líquido × dias úteis/feriados | Esta spec só conta o tempo de jornada para a entrada da simulação; não aplica dias úteis/feriados no valor final (cláusula "sem calendário corporativo" mantida) | spec-002:204 (review:17) | Qualquer tentativa de aplicar feriados no cálculo líquido |
| Tabela de feriados | Tabela de referência persistida no banco, customizável por região/país; não são dados pessoais (sem LGPD) | PROP-001 | Automação de feriados via API de terceiros (fora do FOSS-first) |

## 3. Requisitos funcionais por regime

### 3.1 Regime horário (hourly)
- Campo numérico para montante de horas acumuladas de trabalho ou estimativa.
- Validação: valor > 0.

### 3.2 Regime diário (daily)
- Componente de calendário com seleção de início e fim do período.
- Opções de seleção:
  - dias corridos (todos os dias entre início e fim);
  - dias individuais (seleção livre de dias no calendário);
  - exclusão de fins de semana;
  - exclusão de feriados (conforme tabela de feriados por região/país).
- As opções são combináveis (ex.: dias corridos excluindo fins de semana e feriados).
- O total de dias selecionados mapeia para o campo `quantity` do contrato.

### 3.3 Regime semanal (weekly)
- Componente de calendário com seleção de semanas.
- O total de semanas selecionadas mapeia para o campo `quantity` do contrato (contagem de semanas, não de dias).

### 3.4 Regime mensal (monthly)
- Componente de calendário com seleção de meses.
- O total de meses selecionados mapeia para o campo `quantity` do contrato (contagem de meses, sem contabilizar dias).

### 3.5 Tabela de feriados
- Tabela persistida no banco de dados existente (sem nova infra).
- Cadastro/edição de feriados por região/país.
- Não são dados pessoais; sem impacto LGPD/Marco Civil.
- Manutenção manual dos dados por região/país (não automação via API externa).

## 4. Requisitos não funcionais

- Validação de coerência entre o regime escolhido e o preenchimento de tempo (ex.: não permitir preenchimento de semanas em regime diário).
- Mensagens de erro em PT-BR, seguindo o modelo canônico de erro da `spec-004` §3.
- Sem nova dependência externa (calendário em Vanilla JS/CSS; tabela de feriados no banco existente).
- FOSS-first / zero vendor lock-in.

## 5. Critérios de aceite e testes

- [ ] AC-01: Regime horário aceita montante de horas > 0 e mapeia para `quantity`.
- [ ] AC-02: Regime diário permite seleção de dias corridos, dias individuais, exclusão de fins de semana e exclusão de feriados, combináveis.
- [ ] AC-03: Regime semanal permite seleção de semanas; total mapeia para `quantity` (contagem de semanas).
- [ ] AC-04: Regime mensal permite seleção de meses; total mapeia para `quantity` (contagem de meses, sem dias).
- [ ] AC-05: Tabela de feriados permite cadastro/edição por região/país e é usada na exclusão de feriados do regime diário.
- [ ] AC-06: Validação de coerência entre regime e preenchimento recusa combinações inválidas.
- [ ] AC-07: Nenhuma alteração no contrato HTTP `spec-004` nem nos regimes existentes (incluindo `fixed`).
- [ ] AC-08: Sem impacto LGPD (feriados não são dados pessoais).

## 6. Rastreabilidade

- REQ-02: regimes de contratação (hora, dia, semana, mês, valor fixo).
- US-002: five-engagement-regimes (100% dos regimes operacionais em UAT).
- spec-004 §3: contrato `Regime` + `quantity`.
- constitution.md Art. 1.2 / Art. 1.3.

## 7. Fora de escopo (YAGNI)

- Regime "valor fixo" (fixed) — já contemplado pelo contrato.
- Autenticação/multi-usuário (fora do Art. 1.2).
- Novas moedas, NF-e/NFS-e, app mobile nativo, gráficos, painel admin.
- Histórico/auditoria de alterações de feriados (pode ser adicionado depois).
- Cálculo de dias úteis/feriados na regra de negócio do valor final (permanece em spec-004/spec-002).

## 8. Metadados de ratificação (CCB)

- **Avaliador primário:** `agent-project-analyst`
- **Ratificação / assinatura CCB:** usuário/PO (CCB), 2026-11-13 — custo técnico aprovado e spec promulgada
- **parcel.dod:** true
- **Data da ratificação:** 2026-11-13
- **Status da spec:** ativa / promulgada

---

## CHANGELOG

| Versão | Data | Task/Handoff | Mudança |
|--------|------|--------------|---------|
| 1.0.0 | 2026-11-13 | PROP-001 / agent-project-analyst | Emissão inicial da spec, ratificada pelo CCB. |
| 1.0.0 | 2026-11-13 | CCB / usuário-PO | Ratificação formal e promulgação; custo técnico aprovado (40–56 h).

