# Requirements: COGME

**Defined:** 2026-11-22
**Core Value:** Entregar specs/integridade (SSOT camada 5) ratificadas via Gate G2, mantendo 100% dos itens que bloqueiam produção e sem alterar imutáveis.

## v1 Requirements

Requirements for milestone v1.1 (Fase 1.5 — Especs/Integridade). Each maps to roadmap phases.

### Specs & Emendas (TA-061)

- [ ] **SPEC-01**: spec-004 SS11 preenchida com critérios de aceite próprios (linhas 228-230); SS13 fora de escopo adicional (linhas 243-245)
- [ ] **SPEC-02**: spec-005 job contract-network resolvido com estado real auditado (parcela TA-0048, linha 210)
- [ ] **SPEC-03**: spec-005 destino evidências UAT resolvido (parcela TA-0047, linha 342)
- [ ] **SPEC-04**: C.3 resolvida por processo (não editar spec-003/004 frontmatter histórico)
- [ ] **SPEC-05**: Bump versão spec-004 1.0.0→1.1.0 e spec-005 0.2.0→0.3.0 + CHANGELOG
- [ ] **SPEC-06**: Parcela half-duplex dod:true devolvida (TA-0061)

### Auditoria de Integridade (TA-062)

- [ ] **INTE-01**: spec-006 a spec-015 existem e não vazias
- [ ] **INTE-02**: Conformidade template (frontmatter SS1.1, H1, seções, MAPA TA-0031)
- [ ] **INTE-03**: Nomenclatura spec-NNN-specname.spec.md
- [ ] **INTE-04**: Uso correto de `UNKNOWN - verify` (sem invenção P-08)
- [ ] **INTE-05**: Emendas spec-004 1.1.0 e spec-005 0.3.0 com CHANGELOG + decisões preservadas
- [ ] **INTE-06**: tap.md e eap.md não vazios + rastreabilidade
- [ ] **INTE-07**: pytest tests/agents baseline 4F/149P/1S sem novas falhas
- [ ] **INTE-08**: `sync_agent_registry.py --check` exit 0
- [ ] **INTE-09**: Nenhum imutável alterado (constitution/ADRs/ledger/.opencode)
- [ ] **INTE-10**: Handoffs HF-0601 a HF-0620 e task JSONs presentes
- [ ] **INTE-11**: Relatório de auditoria emitido em docs/auditorias/
- [ ] **INTE-12**: Parcela final dod:true (TA-062)

### tap.md (TA-063)

- [ ] **TAP-01**: tap.md repovoado com conteúdo não vazio (espelho TAP v3)
- [ ] **TAP-02**: Frontmatter documento pinned (id, title, status: draft, version: 1.0.0, custody, task: TA-0063, kill_switch: inherited, trace)
- [ ] **TAP-03**: Rastreabilidade arquivo:linha para cada seção transcrita
- [ ] **TAP-04**: Cabeçalho declara regime congelamento (ADR-005/ADR-013) + fontes canônicas
- [ ] **TAP-05**: Fonte: plano-integral-tap-1-2-3-4-5.md + referências PDF

### eap.md (TA-064)

- [ ] **EAP-01**: eap.md repovoado com fases N1..N11
- [ ] **EAP-02**: Frontmatter documento pinned (id, title, status: draft, version: 1.0.0, KB-INDEX EAP-001, custody, task: TA-0064, kill_switch: inherited, trace)
- [ ] **EAP-03**: Rastreabilidade arquivo:linha para cada fase
- [ ] **EAP-04**: Diagrama mermaid textual (fonte válida) ou `UNKNOWN - verify`
- [ ] **EAP-05**: Correspondência fases com plano-integral (grep N1..N11)

### requisitos.md (TA-065)

- [ ] **REQ-01**: requisitos.md repovoado com RF/RNF/US REQ-01..15
- [ ] **REQ-02**: Rastreabilidade REQ→US (15/15) declarada
- [ ] **REQ-03**: Emendas E-01..E-08 incorporadas (E-02/E-03 impactam requisitos dados/LGPD)
- [ ] **REQ-04**: NFR mapeados spec-006 (B.2) por cross-ref
- [ ] **REQ-05**: Frontmatter (id, title, status: draft, version: 1.0.0, KB-INDEX REQ-SPEC-001, custody, task: TA-0065, kill_switch: inherited, trace)
- [ ] **REQ-06**: Não editar spec-002/spec-001/constitution/ADRs
- [ ] **REQ-07**: Não promover requisitos a "aprovado"

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### Gate G2 (Fase 3)

- **G2-01**: Ratificação specs 024/025/026 — depende da Fase 1.5

## Out of Scope

| Feature | Reason |
|---------|--------|
| VIO-026 (auto-delegação TA-0028) | Decisão Humana/CCB (Art. 5.1) — não reabrir |
| Reescrever constitution/ADRs/ledger/.opencode | Imutáveis desta fase |
| Promover requisitos a "aprovado" | Não promovido nesta fase (TA-065) |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| SPEC-01 .. SPEC-06 | Phase 1.5 | Pending |
| INTE-01 .. INTE-12 | Phase 1.5 | Pending |
| TAP-01 .. TAP-05 | Phase 1.5 | Pending |
| EAP-01 .. EAP-05 | Phase 1.5 | Pending |
| REQ-01 .. REQ-07 | Phase 1.5 | Pending |

**Coverage:**
- v1 requirements: 34 total
- Mapped to phases: 34
- Unmapped: 0 ✓

---
*Requirements defined: 2026-11-22*
*Last updated: 2026-11-22 after milestone v1.1 start*
