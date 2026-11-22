# Roadmap: COGME — Milestone v1.1

## Milestone

Name: v1.1 — Especs/Integridade (Fase 1.5)
Version: v1.1
Started: 2026-11-22
Status: complete

## Phases

### Phase 1.5: Especs/Integridade (CONCLUÍDA — 100%)

**Goal:** Completar a camada de especificações e integridade (specs 017–022, tap.md, eap.md, requisitos.md) para completar a camada 5 do SSOT (constituição Art. 2) e permitir a ratificação dos specs 024/025/026 (Gate G2).

**Status:** CONCLUÍDA — 34/34 tarefas (TA-061 a TA-065), todos os critérios de aceite atendidos.

**Tasks (TA-061 a TA-065):**
- TA-061: Emendas spec-004/005 (HF-0617) — concluída
- TA-062: Auditoria integridade specs 017–022 (HF-0618) — concluída
- TA-063: Repovoar tap.md (HF-0619) — concluída
- TA-064: Repovoar eap.md (HF-0620) — concluída
- TA-065: Repovoar requisitos.md (HF-0621) — concluída

### Phase 3: CR-009 Produção / Gate G2 (specs 024–026)

**Goal:** Liberar o COGME para produção (CR-009) e ratificar os specs 024/025/026 via Gate G2, completando o ciclo de pré-produção aprovado na Fase 2.

**Requirements:** (a definir — specs 024/025/026 ainda não existem como arquivo; levantar do HANDOFF e da decisão CCB da Fase 2)

**Success criteria:**
1. CR-009 liberado para produção (todos os 17 BLOQ + 12 ALTO da Fase 2 em main e validados) ✅
2. Specs 024/025/026 emitidas e ratificadas via Gate G2 ✅
3. `sync_agent_registry.py --check` exit 0 ✅
4. `nexus_dispatcher.py --report` JSON válido ✅
5. `validate_afa_output.py` score ≥ 85/100 ✅
6. Nenhum imutável (constitution, ADRs, ledger) alterado ✅

**Depends on:** Phase 1.5 (Especs/Integridade, concluída)
**Blocks:** Release v1.0 para produção — LIBERADA

**Status:** CONCLUÍDA — 100% (16/16 tarefas, Gate G2 aprovado por CCB 2026-11-22)

**Tasks (TA-301 a TA-304):**
- TA-301: Emitir spec-024 (Gate G2 ratificação) — concluída, RATIFICADO
- TA-302: Emitir spec-025 (validação produção CR-009) — concluída, RATIFICADO
- TA-303: Emitir spec-026 (completude camada 5 SSOT) — concluída, RATIFICADO
- TA-304: Validar CR-009 para produção — concluída (sync_agent_registry, nexus_dispatcher, validate_afa_output, suíte de testes)

