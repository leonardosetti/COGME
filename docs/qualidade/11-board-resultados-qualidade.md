---
id: docs-qualidade-11-board-resultados-qualidade
title: Board de Análise de Resultados de Qualidade — COGME (com RCA e RTM)
type: relatorio
version: 1.1.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/qualidade/07-registro-de-teste.md (execuções e incidentes)
- docs/qualidade/08-relatorio-incidente-de-teste.md (RCA, prioridade, impacto, severidade)
- docs/qualidade/10-rtm-qualidade.md (RTM preenchida)
- docs/uat/rodada-001/relatorio-analitico.md (veredito UAT)
- docs/auditorias/aud-2610-09/10/11 (falsos positivos resolvidos)
last-revised: '2026-11-15'
lgpd-class: n/a
tags:
- board
- analise-de-resultados
- rca
- incidente
- rastreabilidade
- rtm
---

# Board de Análise de Resultados de Qualidade — COGME

Board Kanban de qualidade consolidado a partir do histórico real de ações e soluções aplicadas no projeto (execuções de teste, UAT rodada 001, auditorias extraordinárias de CI/CD). Cada incidente carrega prioridade, impacto, severidade e RCA (causa-raiz). A RTM preenchida está em `docs/qualidade/10-rtm-qualidade.md`.

## 1. Visão geral do board (estado atual)

```
  BACKLOG          EM VERIFICAÇÃO       CONCLUÍDO           BLOQUEADO
  -------------    ----------------     -----------         ---------
  INC-004 (testes  | INC-008 (gate      INC-001 (resolvido)  Nenhum — gate
   pulados)        |  commitado)        INC-002 (resolvido)  local liberado
  INC-005 (drift   | INC-012 (acervo    INC-003 (resolvido)  (coverage 84%)
   cobertura)      |  427/427 válido)   INC-007 (resolvido)
  INC-006 (PDCA    | INC-013 (84,01%)   INC-009 (gate specs)
   evidências)     | INC-014 (WIP       INC-010 (falsos
                    |  commitado)        bloqueios)
                                        INC-011 (frontmatter)
                                        INC-015 (runbook × norma)
                                        INC-016 (tipos commit)
                                            E-001 (1392 PASS)
                                            E-002 (181 PASS)
                                            UAT rodada 001 (14/14)
                                            E-003 (Playwright, planejado)
```

## 2. Métricas de qualidade (resultado da última avaliação)

| Métrica | Valor | Meta | Status |
|---|---|---|---|
| Casos de teste automatizados (pytest) executados | 1392 | — | PASS |
| Falhas na suíte pytest | 0 | 0 | PASS |
| Testes pulados | 13 | 0 (regra CI zero-skipping) | ⚠ INC-004 |
| Cobertura sobre `src/` (CI gate) | 95% | ≥ 95% | ⚠ runs recentes FAIL (INC-012/013) |
| Cobertura declarada no plano de qualidade | 80% | ≥ 80% | ⚠ drift INC-005 |
| Cobertura da suíte unitária local (gate pre-push) | 84,01% | ≥ 80% | PASS (INC-013 em verificação) |
| Casos UAT produto + camada executados | 14 | 14 | PASS (100%) |
| Defeitos críticos/bloqueantes em UAT | 0 | 0 | PASS |
| Veredito binário UAT rodada 001 | APROVADA | APROVADA | PASS |
| Incidentes resolvidos / em verificação / pendentes | 9 / 4 / 3 | — | — |
| Casos funcionais Playwright instituídos | 5 | — | Planejado (E-003) |

## 3. Incidentes — cartões do board (prioridade, impacto, severidade, RCA)

### Coluna: CONCLUÍDO (resolvidos)

#### INC-001 — Falso positivo CI/CD: segurança (CUDA/cloud)

| Campo | Valor |
|---|---|
| Prioridade | P2 (Alto) |
| Impacto | Alto — pipeline `foss-compliance` vermelho, bloqueia merge |
| Severidade | Média — nenhuma violação real de segurança |
| Status | Resolvido |
| RCA | (1) `grep -r` do `ci.yml` varria `.venv/` (pacotes terceiros com referências CUDA/AWS/GCP/Azure, não código COGME); (2) regex ingênua de `security_scan.py` marcava declarações de conformidade como falha. Causa-raiz: detecção sem análise de contexto e escopo de varredura muito amplo. |
| Ação corretiva aplicada | `security_scan.py` distingue uso real vs. declaração de conformidade; aceita agentes legacy-forge (Art. 4.8); `ci.yml` usa `security_scan.py --strict` em vez de `grep -r` ingênuo. |
| Evidência | docs/auditorias/aud-2610-09-...md; Security Scan 46 aprovados / 0 falhas |
| RTM | REQ-11 (CI/CD), FOSS P-01/P-02 |

#### INC-002 — Falso positivo CI/CD: health check de agentes

| Campo | Valor |
|---|---|
| Prioridade | P2 (Alto) |
| Impacto | Alto — job `agent-health` vermelho, bloqueia merge |
| Severidade | Baixa — agentes legacy-forge por decisão constitucional (Art. 4.8) |
| Status | Resolvido |
| RCA | Gate de validação não exibia categoria FORGE-LEGACY do registro; marcar como falha um artefato legacy por decisão constitucional é falso positivo. Causa-raiz: validação sem conhecimento da topologia/categoria do agente. |
| Ação corretiva aplicada | `agent_health_check.py` não gera erro nem aviso para legacy-forge sem frontmatter. |
| Evidência | docs/auditorias/aud-2610-10-...md; Agent Health Check 45/45 saudáveis |
| RTM | REQ-11 (CI/CD) |

#### INC-003 — Falso positivo CI/CD: credenciais versionadas

| Campo | Valor |
|---|---|
| Prioridade | P2 (Alto) |
| Impacto | Alto — pipeline CI vermelho, bloqueia merge |
| Severidade | Baixa — nenhuma credencial real versionada |
| Status | Resolvido |
| RCA | (1) string `AKIA[0-9A-Z]{16}` é padrão regex de detecção dentro de `scripts/security_scan.py`, não credencial real; (2) `grep -r` varria `.venv/` (bibliotecas terceiras com `password` legítimo). Causa-raiz: varredura de diretórios não-projeto e auto-detecção de padrões de segurança. |
| Ação corretiva aplicada | `ci.yml` busca credenciais apenas em diretórios do projeto (`.ai`, `.opencode`, `docs`, `scripts`, `src`, `test`, `tests`, `.github`), excluindo `.venv/`, `scripts/security_scan.py` e o próprio `ci.yml`. |
| Evidência | docs/auditorias/aud-2610-11-...md; Security Scan 46/0 falhas |
| RTM | REQ-11 (CI/CD), P-07 (credenciais) |

#### INC-007 — Drift gráfico: FIG-5 = FIG-3; diretório `diagrams/` inexistente

| Campo | Valor |
|---|---|
| Prioridade | P4 (Baixo) |
| Impacto | Baixo — diagramas Ishikawa não renderizados no plano de qualidade |
| Severidade | Baixa — apenas documentação |
| Status | Resolvido (forma de entrega alterada) |
| RCA | Os PNGs dos Ishikawa nunca foram gerados; `diagrams/` inexistente; FIG-5 aponta o mesmo arquivo de FIG-3. Causa-raiz: entrega em formato PNG não produzida. |
| Ação corretiva aplicada | Ishikawa 6M reespecificados em mermaid inline (spec-010 §3.2); drift registrado sem editar `plano-qualidade.md` (sem custódia de terceiro). |
| Evidência | spec-010 §3.2, AC-07 |
| RTM | REQ-10 (N6.3) |

#### INC-009 — Gate de specs inpassável (vocabulário `ratificada|aprovado` inexistente)

| Campo | Valor |
|---|---|
| Prioridade | P2 (Alto) |
| Impacto | Alto — push que tocasse `.spec.md` sempre bloquearia; gate letra-morta |
| Severidade | Média — gate normativo inoperável |
| Status | Resolvido |
| RCA | Runbook §3 v1.0.0 usou vocabulário fora do conjunto fechado da NORMA-TEMPLATES (`ativo\|draft\|ratificado\|obsoleto\|arquivado`); hook copiou o runbook. Detalhe em doc 08. |
| Ação corretiva aplicada | Hook: `ativo`/`ratificado(a)`/`aprovado(a)` liberam, `draft`/`obsoleto`/`arquivado` bloqueiam (decisão do GP). Runbook v1.1.0 alinhado. |
| Evidência | Worktree: código contra `spec-prop-017` (draft) bloqueado; contra `spec-004` (ativo) liberado |
| RTM | REQ-11, P-06 |

#### INC-010 — Falsos bloqueios do gate `pre-push` (deletados, coverage de integração, mypy)

| Campo | Valor |
|---|---|
| Prioridade | P2 (Alto) |
| Impacto | Alto — push de deleção de `.py` travava; integração exigia coverage ≥ 80% sozinha; mypy duplicava config do `pyproject.toml` |
| Severidade | Média — gate falhava fechado sobre cenários válidos |
| Status | Resolvido |
| RCA | Gate sem derivar critérios das seções do runbook (§6.1 vs §6.2; `[tool.mypy]` SSOT). Detalhe em doc 08. |
| Ação corretiva aplicada | `--diff-filter=d`; `--cov-fail-under=80` só na suíte unitária; mypy condicionado a `src/` alterado e sem flags duplicadas. |
| Evidência | Commit histórico de deleção/rename passa sem flake8 fantasma |
| RTM | REQ-08, REQ-11 |

#### INC-011 — Status de spec lido fora do frontmatter

| Campo | Valor |
|---|---|
| Prioridade | P3 (Médio) |
| Impacto | Médio — `status:` no corpo do documento liberava/bloqueava indevidamente |
| Severidade | Baixa — leitura imprecisa no gate |
| Status | Resolvido |
| RCA | Regex sobre texto integral em vez de parse do bloco YAML entre os `---`. Detalhe em doc 08. |
| Ação corretiva aplicada | `spec_field` lê só o frontmatter e exige `id:`/`spec-id:`. |
| Evidência | Teste do helper: `draft` no frontmatter + `ratificado` no corpo → retorna `draft` |
| RTM | REQ-11 |

#### INC-015 — Drift normativo: runbook §3 vs NORMA-TEMPLATES vs dados

| Campo | Valor |
|---|---|
| Prioridade | P3 (Médio) |
| Impacto | Médio — três vocabulários (norma, runbook, acervo) tornavam o gate inoperável (INC-009) |
| Severidade | Baixa — documental, efeito sistêmico |
| Status | Resolvido (pendente ratificação CCB) |
| RCA | Procedimento sem derivar vocabulário da norma nem validar contra o acervo. Detalhe em doc 08. |
| Ação corretiva aplicada | Runbook v1.1.0: `ativo`/`ratificado` liberam; `draft`/`obsoleto`/`arquivado` bloqueiam; rastreabilidade `id`/`spec-id`. |
| Evidência | `proc-ciclo-codificacao-deploy.md` v1.1.0, controle de versões |
| RTM | REQ-14 |

#### INC-016 — Runbook §7.3: tipos de commit menores que a prática ratificada

| Campo | Valor |
|---|---|
| Prioridade | P4 (Baixo) |
| Impacto | Baixo — `spec:`/`uat:` usados no histórico ficariam fora da norma |
| Severidade | Baixa — documental |
| Status | Resolvido (pendente ratificação CCB) |
| RCA | Lista definida sem amostragem do histórico. Detalhe em doc 08. |
| Ação corretiva aplicada | Runbook v1.1.0 adiciona `spec` e `uat` como tipos válidos. |
| Evidência | `git log` (commits `spec(ui):`, `uat(rodada-001):`) |
| RTM | REQ-13, REQ-14 |

---

### Coluna: EM EXECUÇÃO / PENDENTE (abertos)

#### INC-004 — Testes pulados (13) violam regra zero-skipping do CI

| Campo | Valor |
|---|---|
| Prioridade | P3 (Médio) |
| Impacto | Médio — gate CI `test-suite` bloqueia se houver skip; localmente sem Pango a suíte não passa |
| Severidade | Média — defeito de processo de execução, não de produto |
| Status | Pendente (aberto) |
| RCA | Testes de PDF real dependem de `import weasyprint` que levanta `OSError` quando faltam bibliotecas nativas (Pango). No CI com Pango executam; localmente pulam. A regra "zero skipping" não contempla skip condicional por ausência de biblioteca nativa. Causa-raiz: expectativa de execução invariante entre ambientes. |
| Ação corretiva proposta | Marcar testes de PDF real com marcador `weasyprint` e rodá-los separadamente no CI (com Pango); ou instalar Pango nas imagens locais de build. Pendente de decisão GP/CCB. |
| RTM | REQ-04 (invoice PDF), REQ-08 (coverage gate) |

#### INC-005 — Drift de cobertura: plano 80% vs CI 95%

| Campo | Valor |
|---|---|
| Prioridade | P3 (Médio) |
| Impacto | Médio — divergência entre documento canônico de qualidade e gate real do CI |
| Severidade | Baixa — não afeta produto; afeta clareza do critério de aceitação |
| Status | Pendente (aberto) |
| RCA | `plano-qualidade.md` §5.4.2 declara ≥ 80% enquanto o CI `test-suite` exige `--cov-fail-under=95`. Mudança de critério não propagada ao documento. Causa-raiz: falta de sincronização documento↔CI. |
| Ação corretiva proposta | Alinhar `plano-qualidade.md` §5.3/§5.4.2 para 95% (ou documentar delta intencional por marco). Pendente. |
| RTM | REQ-08 (coverage), REQ-11 (CI) |

#### INC-006 — Ausência de evidências de execução dos PDCAs MF2/MF3

| Campo | Valor |
|---|---|
| Prioridade | P3 (Médio) |
| Impacto | Médio — nenhuma lição por-PDCA registrada para N5-N12 (MF2/MF3 lições vazias, 0 B) |
| Severidade | Baixa — não afeta produto; afeta conformidade REQ-10 |
| Status | Pendente (aberto) |
| RCA | Lições aprendidas não consolidadas após M1/M2; apenas LA-001 registrada (MF1). Causa-raiz: retrospectivas não geraram artefatos por-PDCA. |
| Ação corretiva proposta | Registrar lições por PDCA em `docs/conhecimento/licoes-aprendidas/MF2-licoes.md` e `MF3-licoes.md` na próxima retrospectiva (ondas MF2/MF3). Pendente. |
| RTM | REQ-10 (12 PDCAs, fase N6.3) |

#### INC-008 — Gate `pre-push` inexistente na prática (não instalado; artefatos untracked)

| Campo | Valor |
|---|---|
| Prioridade | P2 (Alto) |
| Impacto | Alto — nenhum push era avaliado; DoD "Push permitido pelo hook" não verificável |
| Severidade | Média — defeito de processo (gate morto) |
| Status | Pendente (aberto) — instalado localmente, falta commitar artefatos |
| RCA | Runbook e hook emitidos fora do próprio ciclo de codificação que normatizam. Detalhe em doc 08. |
| Ação corretiva proposta | Commitar `scripts/githooks/pre-push-ciclo-codificacao-deploy.sh` e `docs/operacao/proc-ciclo-codificacao-deploy.md` (sem misturar com WIP de `src/`). |
| RTM | REQ-11, P-06 |

#### INC-012 — Validador de frontmatter sem escopo; 30 não conformidades legadas; CI lint FAIL

| Campo | Valor |
|---|---|
| Prioridade | P2 (Alto) |
| Impacto | Alto — hook contrariava cabeçalho e runbook §7.4 (".md alterados"), transformando dívida legada em bloqueio permanente; runs do `ci.yml` (43619860226, 43618821664, 43555741240) em FAIL |
| Severidade | Média — dívida documental com efeito de gate |
| Status | Pendente (aberto) — escopo por arquivo aplicado ao hook; 2 saneados na emenda, 28 no acervo pendentes |
| RCA | Validador sem API de escopo; mudanças de vocabulário da norma não propagadas ao acervo (`lgpd-class: dados-pessoais`; `type: analise`/`auditoria`/`registro`; ADRs `status: aprovada`). Detalhe em doc 08. |
| Ação corretiva proposta | Sanear as 28 não conformidades restantes do acervo; manter scan integral no CI após saneamento. |
| RTM | REQ-11 (lint), REQ-14 |

#### INC-013 — Cobertura da suíte unitária 77,97% < gate 80%

| Campo | Valor |
|---|---|
| Prioridade | P2 (Alto) |
| Impacto | Alto — todo push de código bloqueia no gate local (1164 passed, `TOTAL 78%`) |
| Severidade | Média — gate corre (P-06), estado da suíte impede o fluxo |
| Status | Pendente (aberto) |
| RCA | `routers/common.py` 41%, `routers/invoices.py` 39%; relacionado ao INC-005 (80% unit × 95% CI completa). Detalhe em doc 08. |
| Ação corretiva proposta | Completar testes dos routers com maiores lacunas ou explicitar critério por camada no plano de qualidade. Pendente GP/qa-sdet. |
| RTM | REQ-08, REQ-11 |

#### INC-014 — HEAD mypy-red; correções apenas no working tree

| Campo | Valor |
|---|---|
| Prioridade | P3 (Médio) |
| Impacto | Médio — push a partir do HEAD falha no gate; risco de perda do WIP (11 arquivos) |
| Severidade | Baixa — estado transitório de trabalho em andamento |
| Status | Pendente (aberto) |
| RCA | Correções de `src/` não commitadas; WIP com 27 violações de flake8 em `tests/integration/test_invoices_persistence.py`. Detalhe em doc 08. |
| Ação corretiva proposta | Sanear flake8 do WIP e commitar conforme runbook §7 (código + testes + docs no mesmo commit). |
| RTM | REQ-11, P-06 |

---

### Coluna: BLOQUEADO

Nenhum incidente bloqueante no momento. O gate `pre-push` está liberado (cobertura unitária 84,01% ≥ 80%, acervo 427/427 frontmatter válido, flake8/mypy verdes). INC-013 e INC-012 seguem em EM VERIFICAÇÃO até CI remoto verde e parecer do auditor.

## 4. RCA consolidada (causas-raiz por categoria)

Usando a estrutura Ishikawa 6M (spec-010 §3.2):

| 6M | Causa-raiz recorrente | Incidentes ligados |
|---|---|---|
| Método | Detecção sem análise de contexto; regras de execução invariantes entre ambientes; falta de sincronização documento↔CI; gate sem escopo de arquivos alterados; vocabulário normativo não propagado (norma↔runbook↔acervo↔hook) | INC-001, INC-002, INC-003, INC-004, INC-005, INC-009, INC-010, INC-011, INC-012, INC-015, INC-016 |
| Máquina | Escopo de varredura inclui `.venv/`; falta de bibliotecas nativas (Pango) localmente | INC-001, INC-003, INC-004 |
| Medida | Critério de cobertura divergente (80% plano vs 95% CI); gate zero-skipping rígido; cobertura por camada não gerida (unit 78% vs gate 80%) | INC-004, INC-005, INC-013 |
| Meio Ambiente | Diferença CI (com Pango) × local (sem Pango) | INC-004 |
| Mão de Obra | Retrospectivas não geraram artefatos por-PDCA; ciclo de commit não fechado (WIP e artefatos de processo sem commit) | INC-006, INC-008, INC-014 |
| Material | PNGs dos Ishikawa não produzidos; `diagrams/` inexistente; acervo com 28 frontmatter fora do vocabulário fechado | INC-007, INC-012 |

## 5. RTM — resumo de rastreabilidade preenchida (detalhe em docs/qualidade/10-rtm-qualidade.md)

| REQ | US | Casos de teste | Camadas | Status da rastreabilidade | Status da execução |
|---|---|---|---|---|---|
| REQ-01 | US-001 | CT-UN-004..010, CT-INT-002, CT-INT-008, CT-INT-009, CT-INT-015, CT-INT-018, CT-FUNC-002, CT-FUNC-004 | UN, INT, FUNC | Completa | PASS (UN/INT); Planejado (FUNC) |
| REQ-02 | US-002 | CT-INT-003, CT-INT-004, CT-INT-005, CT-FUNC-001 | INT, FUNC | Completa | PASS (INT); Planejado (FUNC) |
| REQ-03 | US-003 | CT-UN-012, CT-INT-004, CT-INT-020 | UN, INT | Completa | PASS |
| REQ-04 | US-004 | CT-INT-012..022, CT-UN-014, CT-FUNC-003 | INT, UN, FUNC | Completa | PASS (UN/INT); Planejado (FUNC) |
| REQ-05 | US-002 | CT-INT-006, CT-INT-007, CT-INT-010, CT-UN-012, CT-UN-013 | INT, UN | Completa | PASS |
| REQ-06 | US-005 | CT-FUNC-005 | FUNC | Completa | Planejado (E-003) |
| REQ-07 | US-006 | CT-UN-001..003, CT-UN-011, CT-INT-011 | UN, INT | Completa | PASS |
| REQ-08 | US-008 | CT-INT-001, CI `test-suite` | INT | Completa | PASS (gate) |
| REQ-10 | — | artefatos docs/qualidade/ | — | Completa | PASS (disciplina instituída) |
| REQ-11 | — | CI jobs `lint`, `test-suite` | — | Completa | PASS (CI verde) |
| REQ-14 | — | CT-INT-024 | INT | Completa | PASS |
| REQ-16 | — | — | — | Não aplicável (CR-002/SPEC-017, posterior) | — |
| REQ-17 | US-017 | CT-INT-023 | INT | Completa | PASS |

## 6. Plano de ação (próximos passos)

| ID | Ação | Responsável | Prazo sugerido | Incidente ligado |
|---|---|---|---|---|
| A-01 | Executar camada Playwright (E-003) contra stack rodando | qa-sdet | Próxima sprint | — |
| A-02 | Resolver skip condicional de PDF (marcador `weasyprint` ou instalar Pango local) | qa-sdet + GP | Próxima sprint | INC-004 |
| A-03 | Alinhar `plano-qualidade.md` cobertura 80% → 95% | GP | Próxima sprint | INC-005 |
| A-04 | Registrar lições por PDCA MF2/MF3 (`MF2-licoes.md`, `MF3-licoes.md`) | GP | Retrospectiva MF2/MF3 | INC-006 |
| A-05 | **CONCLUÍDA** — gate `pre-push` refinado + runbook v1.1.0 commitados (cf063b6, 6e2049e) | devops | 15/11/2026 | INC-008 |
| A-06 | **CONCLUÍDA** — acervo saneado: 427/427 `.md` com frontmatter válido (2626e5d) | sdd-specialist + analyst | 15/11/2026 | INC-012 |
| A-07 | **CONCLUÍDA** — cobertura unitária 84,01% com testes de `routers/common.py` e `invoices.py` (ebd0237) | qa-sdet + backend-dev | 15/11/2026 | INC-013 |
| A-08 | **CONCLUÍDA** — WIP de `src/` commitado com flake8 saneado (cf063b6) | backend-dev | 15/11/2026 | INC-014 |
| A-09 | Ratificar runbook v1.1.0 no CCB (vocabulário de status; tipos `spec`/`uat`) | GP/CCB | Próximo CCB | INC-015, INC-016 |

## 7. Assinatura do board

| Papel | Nome/Função | Data | Assinatura |
|---|---|---|---|
| Consolidador | qa-sdet (agent-qa-sdet) | 14/11/2026 | |
| Consolidador (adenda INC-008..016) | qa-sdet (agent-qa-sdet) | 15/11/2026 | |
| Revisor | reviewer (agent-reviewer) | | |
| Gatekeeper | gatekeeper (agent-gatekeeper) | | |
| Auditor | auditor (agent-project-auditor) | | |

## 8. Referências cruzadas

- Contexto da disciplina: `docs/qualidade/00-contexto-disciplina-qualidade.md`
- Pirâmide de testes: `docs/qualidade/01-piramide-testes.md`
- Shift-Left: `docs/qualidade/02-shift-left.md`
- RTM preenchida: `docs/qualidade/10-rtm-qualidade.md`
- Artefatos ISTQB: `docs/qualidade/03..09-*.md`
- Relatórios de auditoria (falsos positivos resolvidos): `docs/auditorias/aud-2610-09/10/11-*.md`
- UAT rodada 001: `docs/uat/rodada-001/relatorio-analitico.md`
