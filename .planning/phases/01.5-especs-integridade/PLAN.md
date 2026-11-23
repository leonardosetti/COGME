---
id: cogme-plan-1-5
title: COGME — PLAN Fase 1.5
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .planning/phases/1_5/HANDOFF.md
last-revised: '2026-11-22'
lgpd-class: n/a
tags:
- planejamento
- fase-1-5
- planejamento
---

# PLAN — Fase 1.5: Especs/Integridade (TA-061 a TA-065)

## Fase
Número: 1.5 | Slug: `especs-integridade` | Status: planejado

## Goal
Completar a camada de especificações e integridade (specs 017–022, tap.md, eap.md, requisitos.md) para completar a camada 5 do SSOT (constituição Art. 2) e permitir a ratificação dos specs 024/025/026 (Gate G2).

## Contexto (do HANDOFF)
- Fase 2 (código/pré-produção) concluída e aprovada por CCB (`docs/decisoes/ccb-aprovacao-fase-2-pre-producao.md`).
- Auditoria CR-009 aprovada (`docs/auditorias/aud-cr-009-2026-11-22-aprovacao-producao.md`).
- Completude do sistema: 86.2% (100% nos itens que bloqueiam produção).
- Os specs 017–022 já existem como implementação; falta a camada de especificação canônica e rastreabilidade (SDD).
- Gate G2 (ratificação specs 024/025/026) depende desta fase.
- Sem ROADMAP.md; esta fase é planejada a partir de `.planning/phases/1_5/HANDOFF.md` (context capturado no discuss-phase).

## Escopo (TA-061 a TA-065)

### TA-061 — Emendas spec-004/005 (HF-0617)
| ID | Task | Dependências |
|----|------|--------------|
| T1 | spec-004: SS11 preenchida com critérios de aceite próprios (linhas 228-230); SS13 fora de escopo adicional (linhas 243-245) | — |
| T2 | spec-005: job contract-network resolvido com estado real auditado (parcela TA-0048, linha 210); destino evidências UAT resolvido (parcela TA-0047, linha 342) | — |
| T3 | C.3 resolvida por processo (não editar spec-003/004 frontmatter histórico) | — |
| T4 | Bump versão 1.0.0→1.1.0 (spec-004) e 0.2.0→0.3.0 (spec-005) + CHANGELOG | — |
| T5 | Parcela half-duplex dod:true devolvida (TA-0061) | — |

### TA-062 — Auditoria integridade specs 017–022 (HF-0618)
| ID | Task | Dependências |
|----|------|--------------|
| T6 | spec-006 a spec-015 existem e não vazias | — |
| T7 | Conformidade template (frontmatter SS1.1, H1, seções, MAPA TA-0031) | — |
| T8 | Nomenclatura spec-NNN-specname.spec.md | — |
| T9 | Uso correto de `UNKNOWN - verify` (sem invenção P-08) | — |
| T10 | Emendas spec-004 1.1.0 e spec-005 0.3.0 com CHANGELOG + decisões preservadas | T4 |
| T11 | tap.md e eap.md não vazios + rastreabilidade | T18, T23 (TA-063/064) |
| T12 | pytest tests/agents baseline 4F/149P/1S sem novas falhas | — |
| T13 | `sync_agent_registry.py --check` exit 0 | — |
| T14 | Nenhum imutável alterado (constitution/ADRs/ledger/.opencode) | — |
| T15 | Handoffs HF-0601 a HF-0620 e task JSONs presentes | — |
| T16 | Relatório de auditoria emitido em docs/auditorias/ | — |
| T17 | Parcela final dod:true (TA-062) | — |

### TA-063 — Repovoar tap.md (HF-0619)
| ID | Task | Dependências |
|----|------|--------------|
| T18 | tap.md repovoado com conteúdo não vazio (espelho TAP v3) | — |
| T19 | Frontmatter documento pinned (id, title, status: draft, version: 1.0.0, custody, task: TA-0063, kill_switch: inherited, trace) | — |
| T20 | Rastreabilidade arquivo:linha para cada seção transcrita | — |
| T21 | Cabeçalho declara regime congelamento (ADR-005/ADR-013) + fontes canônicas | — |
| T22 | Fonte: plano-integral-tap-1-2-3-4-5.md + referências PDF | — |

### TA-064 — Repovoar eap.md (HF-0620)
| ID | Task | Dependências |
|----|------|--------------|
| T23 | eap.md repovoado com fases N1..N11 | — |
| T24 | Frontmatter documento pinned (id, title, status: draft, version: 1.0.0, KB-INDEX EAP-001, custody, task: TA-0064, kill_switch: inherited, trace) | — |
| T25 | Rastreabilidade arquivo:linha para cada fase | — |
| T26 | Diagrama mermaid textual (fonte válida) ou `UNKNOWN - verify` | — |
| T27 | Correspondência fases com plano-integral (grep N1..N11) | — |

### TA-065 — Repovoar requisitos.md (HF-0621)
| ID | Task | Dependências |
|----|------|--------------|
| T28 | requisitos.md repovoado com RF/RNF/US REQ-01..15 | — |
| T29 | Rastreabilidade REQ→US (15/15) declarada | — |
| T30 | Emendas E-01..E-08 incorporadas (E-02/E-03 impactam requisitos dados/LGPD) | — |
| T31 | NFR mapeados spec-006 (B.2) por cross-ref | — |
| T32 | Frontmatter (id, title, status: draft, version: 1.0.0, KB-INDEX REQ-SPEC-001, custody, task: TA-0065, kill_switch: inherited, trace) | — |
| T33 | Não editar spec-002/spec-001/constitution/ADRs | — |
| T34 | Não promover requisitos a "aprovado" | — |

## Critérios de aceite (checkáveis)
- [ ] spec-004 e spec-005 emendadas com bump de versão + CHANGELOG (TA-061)
- [ ] Specs 017–022 passam auditoria de integridade (TA-062)
- [ ] tap.md repovoado com conteúdo não vazio + rastreabilidade arquivo:linha (TA-063)
- [ ] eap.md repovoado com fases N1..N11 + rastreabilidade (TA-064)
- [ ] requisitos.md repovoado com RF/RNF/US REQ-01..15 + rastreabilidade 15/15 (TA-065)
- [ ] `sync_agent_registry.py --check` exit 0
- [ ] `nexus_dispatcher.py --report` JSON válido
- [ ] `validate_afa_output.py` score ≥ 85/100 (VIO-019 já fechado, manter)
- [ ] `docs/auditorias/` relatório de auditoria da rodada specs emitido
- [ ] Nenhum imutável (constitution, ADRs, ledger) alterado
- [ ] Handoffs devolvidos com parcela half-duplex dod:true

## Riscos
- Mudanças em ledger.yaml/registry.yaml podem quebrar agentes existentes (testar sync_agent_registry e nexus_dispatcher depois).
- VIO-026 (auto-delegação TA-0028) já encerrada por decisão CCB — não reabrir.
- VIO-019 (AFA SDDAI) já fechada (score 100/100) — manter nos 5 agentes SDDAI.
- Não reescrever arquivos imutáveis (constitution, ADRs, ledger pré-existente, .opencode).

## Arquivos de referência
- `.ai/specs/MANIFEST.md` — template SS1, regras de bump e CHANGELOG
- `.ai/specs/spec-004-backend-mvp-v1.spec.md` (linhas 228-230, 243-245)
- `.ai/specs/spec-005-container-layers-v1.spec.md` (linhas 210, 342)
- `.ai/specs/spec-006-nfr-consolidados-v1.spec.md` (NFR mapeados)
- `.ai/specs/spec-017` a `spec-022` (specs já implementadas)
- `.ai/specs/kb-taxonomy.md` — classe de artefato, DoR diagrama
- `constitution.md` — Art. 2 (hierarquia), Art. 4 (governança agentes), Art. 6 (método SSOT)
- `docs/planos/plano-integral-tap-1-2-3-4-5.md` — fonte TAP v3
- `docs/decisoes/ADR-005-freeze.md`, `ADR-013-regime-emenda-tap.md` — regime congelamento
- `docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md` — itens A.1, A.2, A.3, C.1-C.5

## Próximo comando
`/gsd-execute-phase` (fase 1.5) após revisão deste PLAN.md.
