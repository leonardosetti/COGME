---
id: ai-specs-spec-026-ssot-camada-5-completude-v1
title: 'SPEC spec-026 — ssot-camada-5-completude-v1 — Completação da camada 5 do SSOT (constituição Art. 2) e rastreabilidade final specs/integridade'
type: spec
version: 0.1.0
status: draft
owner: agent-project-analyst
derived-from:
- .planning/phases/1_5/HANDOFF.md (Fase 1.5: Especs/Integridade, TA-061 a TA-065)
- constitution.md (Art. 2 — hierarquia SSOT, Art. 6 — método SSOT)
- .ai/specs/MANIFEST.md (normalização TA-0031, template SS1)
last-revised: '2026-11-22'
lgpd-class: n/a
tags:
- specs
- docs
- ssot
- camada-5
- integridade
- completude
spec-id: spec-026
specname: ssot-camada-5-completude-v1
version: 0.1.0
status: draft
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-22
updated: 2026-11-22
origin: .planning/phases/1_5/HANDOFF.md (Fase 1.5 — Especs/Integridade)
task: "TA-303 | sender: agent-nexus-prime-ultimate"
kill_switch: inherited
trace:
  - .planning/phases/1_5/HANDOFF.md (Fase 1.5 — Especs/Integridade, TA-061 a TA-065)
  - constitution.md (Art. 2 SSOT hierarquia, Art. 6 método SSOT)
  - .ai/specs/MANIFEST.md (template SS1 camadas a-h)
---

# SPEC spec-026 — ssot-camada-5-completude-v1 — Completação da camada 5 do SSOT (constituição Art. 2) e rastreabilidade final specs/integridade

**Status:** DRAFT — pendente de ratificação pelo Gate G2 (Fase 3). Define a completude da camada 5 do SSOT após a Fase 1.5.

---

## 1. Contexto e Origem

### 1.1 Origem

Emitida por TA-303 (Fase 3, agent-nexus-prime-ultimate → agent-sdd-specialist, action: spec, 2026-11-22) para consolidar a completude da camada 5 do SSOT (constituição Art. 2) após a conclusão da Fase 1.5 (Especs/Integridade, 100% das tarefas TA-061 a TA-065).

### 1.2 Camada 5 do SSOT — Especs/Integridade

| Item | Artefato | Status |
|------|----------|--------|
| spec-004 (backend-mvp) | `.ai/specs/spec-004-backend-mvp-v1.spec.md` | v2.0.0, ratificada |
| spec-005 (container-layers) | `.ai/specs/spec-005-container-layers-v1.spec.md` | v0.4.0, ratificada |
| spec-006 a spec-015 | `.ai/specs/spec-006-*` a `spec-015-*` | existentes, integridade auditada (TA-062) |
| spec-017 a spec-022 | `.ai/specs/spec-017-*` a `spec-022-*` | existentes, integridade auditada (TA-062) |
| tap.md | `.ai/specs/tap.md` | repovoado (TA-063), linha de base congelada |
| eap.md | `.ai/specs/eap.md` | repovoado (TA-064), fases N1..N12 |
| requisitos.md | `.ai/specs/requisitos.md` | repovoado (TA-065), REQ-01..15, matriz 15/15 |

---

## 3. Critérios de Completude da Camada 5

| ID | Critério | Método |
|----|----------|--------|
| SSOT-AC-01 | Fase 1.5 100% concluída (34/34 tarefas) | .planning/STATE.md progresso |
| SSOT-AC-02 | tap.md não vazio + rastreabilidade arquivo:linha | Leitura do arquivo |
| SSOT-AC-03 | eap.md fases N1..N11 + rastreabilidade | Leitura do arquivo |
| SSOT-AC-04 | requisitos.md REQ-01..15 + matriz REQ→US 15/15 | Leitura do arquivo |
| SSOT-AC-05 | MAPA TA-0031 (camadas a-h) nas specs | Verificação de seção final |
| SSOT-AC-06 | Nenhum imutável alterado | `git status` nos caminhos imutáveis |
| SSOT-AC-07 | `sync_agent_registry.py --check` exit 0 | Execução do comando |

---

## 4. Rastreabilidade

| Fonte | Seção |
|-------|-------|
| HANDOFF Fase 1.5 | Todas |
| constitution.md | Art. 2 (hierarquia SSOT), Art. 6 (método SSOT) |
| .ai/specs/MANIFEST.md | Template SS1, normalização TA-0031 |
| Fase 1.5 (TA-061 a TA-065) | Execução completa |

---

## 5. Fora de Escopo (YAGNI)

- Promover requisitos a "aprovado" (proibido na Fase 1.5 por TA-065)
- Alterar imutáveis (constitution, ADRs, ledger, .opencode)
- Gate G5 (parecer LGPD) — fase posterior

---

## CHANGELOG

- 0.1.0 — 2026-11-22: emissão inicial como DRAFT; define completude da camada 5 do SSOT após Fase 1.5, critérios SSOT-AC-01..07, rastreabilidade dos artefatos specs/tap/eap/requisitos. Pendente de ratificação CCB/Gate G2.
