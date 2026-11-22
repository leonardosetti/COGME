# PLAN — Fase 4: Release v1.0 — Publicação e Pós-produção

## Fase
Número: 4 | Slug: `release-v1-0-publica-o-e-p-s-produ-o` | Status: planejado

## Goal
Publicar a release v1.0 do COGME para produção, com tag semver, release notes, documentação final e handoff para operação, após aprovação do Gate G2 (Fase 3).

## Contexto
- Fase 3 (CR-009 Produção / Gate G2) concluída — 100% (16/16 tarefas), Gate G2 aprovado por CCB 2026-11-22.
- Specs 024/025/026 ratificadas (RATIFICADO).
- CR-009 liberado para produção (17 BLOQ + 12 ALTO validados).
- Nenhum imutável (constitution, ADRs, ledger) alterado.
- `sync_agent_registry.py --check` exit 0; `nexus_dispatcher.py --report` JSON válido; `validate_afa_output.py` score 100/100.

## Escopo (TA-401 a TA-405)

### TA-401 — Criar tag v1.0.0 e push para origin/main (HF-0701)
| ID | Task | Dependências |
|----|------|--------------|
| T1 | Calcular versão semver v1.0.0 (primeira release pública) | Fase 3 concluída |
| T2 | Criar tag v1.0.0 no commit HEAD de main | T1 |
| T3 | Push tag v1.0.0 para origin/main | T2 |

### TA-402 — Publicar release v1.0.0 com release notes (HF-0702)
| ID | Task | Dependências |
|----|------|--------------|
| T4 | Escrever release notes (mudanças, correções, notas de upgrade) | T3 |
| T5 | Publicar release v1.0.0 no GitHub com release notes | T4 |
| T6 | Verificar que a release está visível e acessível | T5 |

### TA-403 — Verificar todos os pipelines CI/CD verdes (HF-0703)
| ID | Task | Dependências |
|----|------|--------------|
| T7 | Pipeline `ci.yml` verde (todos os 9 jobs) | T3 |
| T8 | Pipeline `sddai-verify.yml` verde | T3 |
| T9 | Pipeline `auditoria-compliance.yml` verde | T3 |
| T10 | `sync_agent_registry.py --check` exit 0 | T3 |
| T11 | `nexus_dispatcher.py --report` JSON válido | T3 |
| T12 | `validate_afa_output.py` score ≥ 85/100 | T3 |

### TA-404 — Revisar documentação de operação/runbook (HF-0704)
| ID | Task | Dependências |
|----|------|--------------|
| T13 | Revisar runbook de operação (health checks, procedimentos de rotina) | — |
| T14 | Verificar documentação de deploy (docker-compose, variáveis de ambiente) | — |
| T15 | Confirmar que nenhum imutável foi alterado na documentação | T13 |

### TA-405 — Handoff para operação (monitoramento, alertas, backup) (HF-0705)
| ID | Task | Dependências |
|----|------|--------------|
| T16 | Configurar monitoramento (uptime, saúde dos serviços) | — |
| T17 | Configurar alertas (falhas, degradação, segurança) | T16 |
| T18 | Confirmar estratégia de backup (banco, arquivos, configs) | — |
| T19 | Entregar handoff para operação (contatos, procedimentos, escalonamento) | T16, T17, T18 |

## Critérios de aceite (checkáveis)
- [ ] Tag v1.0.0 criada e pushada para origin/main (TA-401)
- [ ] Release v1.0.0 publicada no GitHub com release notes (TA-402)
- [ ] Pipeline `ci.yml` verde (todos os 9 jobs) (TA-403)
- [ ] Pipeline `sddai-verify.yml` verde (TA-403)
- [ ] Pipeline `auditoria-compliance.yml` verde (TA-403)
- [ ] `sync_agent_registry.py --check` exit 0 (TA-403)
- [ ] `nexus_dispatcher.py --report` JSON válido (TA-403)
- [ ] `validate_afa_output.py` score ≥ 85/100 (TA-403)
- [ ] Documentação de operação (runbook) revisada (TA-404)
- [ ] Handoff para operação entregue (monitoramento, alertas, backup) (TA-405)
- [ ] Nenhum imutável (constitution, ADRs, ledger) alterado (TA-404)

## Riscos
- Tag v1.0.0 já existente (recriar ou usar versão diferente)
- Falha em algum pipeline CI/CD (investigar e corrigir antes de publicar)
- Documentação de operação desatualizada (atualizar antes do handoff)
- Backup não testado (testar restauração antes do handoff)

## Arquivos de referência
- `.planning/phases/3/PLAN.md` — PLAN da Fase 3 (concluída, Gate G2 aprovado)
- `.planning/phases/1_5/HANDOFF.md` — handoff da Fase 1.5
- `docker-compose.yml` — stack de produção
- `docker-compose.staging.yml` — stack de staging (criado na correção de CI/CD)
- `.github/workflows/ci.yml` — pipeline CI/CD principal
- `.github/workflows/sddai-verify.yml` — pipeline SDDAI
- `.github/workflows/auditoria-compliance.yml` — pipeline de compliance
- `constitution.md` — Art. 2 (hierarquia SSOT), Art. 6 (método SSOT)

## Próximo comando
`/gsd-execute-phase` (fase 4) após revisão deste PLAN.md.
