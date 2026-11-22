# PLAN — Fase 3: CR-009 Produção / Gate G2 (specs 024–026)

## Fase
Número: 3 | Slug: `cr-009-produ-o-gate-g2-specs-024-026` | Status: planejado

## Goal
Liberar o COGME para produção (CR-009) e ratificar os specs 024/025/026 via Gate G2, completando o ciclo de pré-produção aprovado na Fase 2.

## Contexto
- Fase 1.5 (Especs/Integridade) concluída — 100% (34/34 tarefas), desbloqueando o Gate G2.
- Fase 2 (pré-produção CR-009) concluída e aprovada por CCB (2026-11-22): 15 BLOQ + 12 ALTO implementados, suíte 1294 passed / 0 failed, pipeline verde.
- Gate G2 (ratificação specs 024/025/026) depende da Fase 1.5; esta fase executa a ratificação e libera a produção.
- Os specs 024/025/026 ainda não existem como arquivo; levantar do HANDOFF da Fase 1.5 e da decisão CCB da Fase 2.

## Escopo (TA-301 a TA-304)

### TA-301 — Emitir spec-024 (pendente de Gate G2)
| ID | Task | Dependências |
|----|------|--------------|
| T1 | Levantar conteúdo do spec-024 a partir do HANDOFF da Fase 1.5 e decisão CCB da Fase 2 | Fase 1.5 concluída |
| T2 | Emitir spec-024 com frontmatter SS1.1, H1, camadas a–h (template TA-0031) | T1 |
| T3 | Submeter spec-024 à ratificação Gate G2 | T2 |

### TA-302 — Emitir spec-025 (pendente de Gate G2)
| ID | Task | Dependências |
|----|------|--------------|
| T4 | Levantar conteúdo do spec-025 a partir do HANDOFF da Fase 1.5 e decisão CCB da Fase 2 | Fase 1.5 concluída |
| T5 | Emitir spec-025 com frontmatter SS1.1, H1, camadas a–h (template TA-0031) | T4 |
| T6 | Submeter spec-025 à ratificação Gate G2 | T5 |

### TA-303 — Emitir spec-026 (pendente de Gate G2)
| ID | Task | Dependências |
|----|------|--------------|
| T7 | Levantar conteúdo do spec-026 a partir do HANDOFF da Fase 1.5 e decisão CCB da Fase 2 | Fase 1.5 concluída |
| T8 | Emitir spec-026 com frontmatter SS1.1, H1, camadas a–h (template TA-0031) | T7 |
| T9 | Submeter spec-026 à ratificação Gate G2 | T8 |

### TA-304 — Validar CR-009 para produção
| ID | Task | Dependências |
|----|------|--------------|
| T10 | Confirmar todos os 17 BLOQ + 12 ALTO da Fase 2 em main | — |
| T11 | `sync_agent_registry.py --check` exit 0 | — |
| T12 | `nexus_dispatcher.py --report` JSON válido | — |
| T13 | `validate_afa_output.py` score ≥ 85/100 (5 agentes SDDAI) | — |
| T14 | Suíte de testes verde (1294 passed / 0 failed) | — |
| T15 | Nenhum imutável (constitution, ADRs, ledger) alterado | — |
| T16 | Liberar CR-009 para produção (aprovação final) | T1–T15, Gate G2 ratificado |

## Critérios de aceite (checkáveis)
- [ ] CR-009 liberado para produção (17 BLOQ + 12 ALTO validados em main) (TA-304)
- [ ] Specs 024/025/026 emitidas e ratificadas via Gate G2 (TA-301/302/303)
- [ ] `sync_agent_registry.py --check` exit 0 (TA-304)
- [ ] `nexus_dispatcher.py --report` JSON válido (TA-304)
- [ ] `validate_afa_output.py` score ≥ 85/100 (TA-304)
- [ ] Nenhum imutável (constitution, ADRs, ledger) alterado (TA-304)

## Riscos
- Specs 024/025/026 ainda não existem; conteúdo depende de decisão CCB/Gate G2 (pendente de validação).
- Nenhum imutável pode ser alterado (constitution, ADRs, ledger, .opencode).

## Arquivos de referência
- `.planning/phases/1_5/HANDOFF.md` — handoff da Fase 1.5 (aponta para esta fase)
- `.planning/phases/2/PLAN.md` — PLAN da Fase 2 (CR-009 pré-produção, concluída)
- `docs/decisoes/ccb-aprovacao-fase-2-pre-producao.md` — decisão CCB da Fase 2
- `docs/auditorias/aud-cr-009-2026-11-22-aprovacao-producao.md` — auditoria CR-009 aprovada
- `constitution.md` — Art. 2 (hierarquia), Art. 6 (método SSOT)
- `.ai/specs/MANIFEST.md` — template SS1, regras de bump e CHANGELOG

## Próximo comando
`/gsd-execute-phase` (fase 3) após revisão deste PLAN.md.
