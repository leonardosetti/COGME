---
id: ai-specs-spec-024-gate-g2-ratificacao-v1
title: 'SPEC spec-024 — gate-g2-ratificacao-v1 — Gate G2: ratificação specs 024/025/026 e liberação CR-009 produção'
type: spec
version: 0.1.0
status: draft
owner: agent-project-analyst
derived-from:
- .planning/phases/1_5/HANDOFF.md (Fase 1.5 handoff, TA-061 a TA-065)
- .planning/phases/2/PLAN.md (Fase 2: pré-produção CR-009 concluída)
- docs/decisoes/ccb-aprovacao-fase-2-pre-producao.md (CCB 2026-11-22)
- constitution.md (Art. 2, Art. 5.1, Art. 6)
last-revised: '2026-11-22'
lgpd-class: n/a
tags:
- specs
- docs
- gate-g2
- producao
- cr-009
- ratificacao
spec-id: spec-024
specname: gate-g2-ratificacao-v1
version: 0.1.0
status: draft
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-22
updated: 2026-11-22
origin: .planning/phases/1_5/HANDOFF.md (Handoff Fase 1.5, Gate G2)
task: "TA-301 | sender: agent-nexus-prime-ultimate"
kill_switch: inherited
trace:
  - .planning/phases/1_5/HANDOFF.md (Fase 1.5 — Especs/Integridade)
  - .planning/phases/2/PLAN.md (Fase 2 — Pré-produção CR-009)
  - docs/decisoes/ccb-aprovacao-fase-2-pre-producao.md (CCB aprovação Fase 2)
  - constitution.md (Art. 2 SSOT, Art. 5.1 decisão Humana/CCB, Art. 6 método SSOT)
---

# SPEC spec-024 — gate-g2-ratificacao-v1 — Gate G2: ratificação specs 024/025/026 e liberação CR-009 produção

**Status:** DRAFT — pendente de ratificação pelo Gate G2 (Fase 3). Emissão inicial com base no HANDOFF da Fase 1.5 e decisão CCB da Fase 2 (2026-11-22).

---

## 1. Contexto e Origem

### 1.1 Origem

Emitida por TA-301 (Fase 3, agent-nexus-prime-ultimate → agent-sdd-specialist, action: spec, 2026-11-22) para definir o Gate G2 que ratifica os specs 024/025/026 e libera o COGME para produção (CR-009), completando o ciclo de pré-produção aprovado na Fase 2.

### 1.2 Decisões de Base (CCB Fase 2, 2026-11-22)

| ID | Decisão | Fonte | Status |
|----|---------|-------|--------|
| CR2-D01 | Fase 2 pré-produção aprovada (15 BLOQ + 12 ALTO) | ccb-aprovacao-fase-2-pre-producao.md | ✅ APROVADA |
| CR2-D02 | Completude sistema 86.2% (100% itens bloqueio produção) | relatorio-completude-sistema.md | ✅ APROVADA |
| CR2-D03 | Gate G2 depende da Fase 1.5 (specs/integridade) | .planning/phases/1_5/HANDOFF.md | ✅ APROVADA |

---

## 2. Objetivo do Gate G2

Ratificar os specs 024 (esta spec), 025 e 026 e liberar o CR-009 para produção, assegurando que:
- Todos os 17 BLOQ + 12 ALTO da Fase 2 estão em main e validados
- A camada 5 do SSOT (constituição Art. 2) está completa (Fase 1.5, 100%)
- Nenhum imutável (constitution, ADRs, ledger, .opencode) foi alterado
- Critérios de execução da Fase 1.5 atendidos (sync_agent_registry, nexus_dispatcher, validate_afa_output, suíte de testes)

---

## 3. Critérios de Aceite do Gate G2

| ID | Critério | Método de Verificação |
|----|----------|----------------------|
| G2-AC-01 | Specs 024/025/026 emitidas com frontmatter SS1.1 e camadas a–h | Leitura de arquivo + grep frontmatter |
| G2-AC-02 | Specs 024/025/026 ratificadas por decisão CCB/Gate G2 | Ata da reunião CCB / decisão registrada |
| G2-AC-03 | `sync_agent_registry.py --check` exit 0 | Execução do comando |
| G2-AC-04 | `nexus_dispatcher.py --report` JSON válido | Execução do comando + validação JSON |
| G2-AC-05 | `validate_afa_output.py` score ≥ 85/100 (5 agentes SDDAI) | Execução do comando |
| G2-AC-06 | Suíte de testes verde (1294 passed / 0 failed) | `python3 -m pytest tests/ -q` |
| G2-AC-07 | Nenhum imutável alterado (constitution/ADRs/ledger/.opencode) | `git status` nos caminhos imutáveis |
| G2-AC-08 | Handoffs Fase 1.5 devolvidos com dod:true | .ai/handoffs/task-TA-006{1..5}.json |

---

## 4. Rastreabilidade

| Fonte | Seção |
|-------|-------|
| HANDOFF Fase 1.5 | Todas |
| PLAN Fase 2 (pré-produção CR-009) | Contexto de base |
| Decisão CCB Fase 2 | CR2-D01..D03 |
| constitution.md | Art. 2, 5.1, 6 |
| Fase 1.5 (TA-061 a TA-065) | Pré-requisito do Gate G2 |

---

## 5. Fora de Escopo (YAGNI)

- Implementação dos specs 024/025/026 como código (esta spec apenas define o gate de ratificação)
- Alteração de imutáveis (constitution, ADRs, ledger, .opencode)
- Gate G5 (parecer LGPD) — depende da Fase 1.5, entra em fase posterior

---

## CHANGELOG

- 0.1.0 — 2026-11-22: emissão inicial como DRAFT; define Gate G2, critérios de aceite G2-AC-01..08, rastreabilidade Fase 1.5 e Fase 2. Pendente de ratificação CCB/Gate G2.
