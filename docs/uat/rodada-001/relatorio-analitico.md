---
id: docs-uat-rodada-001-relatorio-analitico
title: Relatório Analítico — UAT Rodada 001 (COGME)
type: test
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/uat/rodada-001/relatorio-analitico.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- rodada-001
- docs
- adequado-a-norma
---
# Relatório Analítico — UAT Rodada 001 (COGME)

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira  
**Rodada:** 001  
**Data de execução:** 05/11/2026  
**Status da rodada:** EM EXECUÇÃO (primeira rodada; produto em finalização de implementação)  
**Destino:** `docs/uat/rodada-001/` (decisão GP/CCB fechada, pendência #6 resolvida)  
**Conteúdo:** exclusivamente sintético (P-04, constitution.md:90)

---

## 1. Taxa de aceite (critério binário, spec-009 §3.2)

O critério de aprovação da UAT é **fail-closed**: 100% dos fluxos críticos PASS e zero defeitos `critical`/`blocking` abertos. Qualquer falha = rodada REPROVADA.

| Métrica | Valor | Fonte / observação |
|---------|-------|--------------------|
| Fluxos críticos de produto planejados | 7 (UAT-01..UAT-07) | spec-009 §3.3 |
| Casos de camada planejados | 7 (F-01..F-07) | spec-005 §12, reuso por referência |
| Fluxos executados nesta rodada | 0 | produto ainda não implementado em `main` (commits locais em `feat/backend-mvp`, pendente de push/merge) |
| **Taxa de aceite** | **0% (não executada)** | aguardando conclusão da implementação do backend e separação de camadas |
| Defeitos `critical`/`blocking` abertos | 0 | nenhuma execução ainda |
| Veredito binário | **EM EXECUÇÃO** | não há rodada concluída |

**Condição para aprovação:** 100% dos 14 casos (7 produto + 7 camada) com resultado PASS e zero defeitos críticos/bloqueantes.

---

## 2. Cobertura analizada (rastreabilidade REQ → US → trace id → spec)

| Trace id | Fluxo | US | REQ | Spec que cobre | Cobertura rodada 001 |
|----------|-------|----|-----|----------------|----------------------|
| `REQ-01::UAT-01::product::sim-realtime` | Simulação tempo real USD/EUR→BRL | US-001 | REQ-01, REQ-05 | spec-004 §3-4, spec-006 NF-01/NF-02 | Não executada |
| `REQ-02::UAT-02::product::regimes-5` | 5 regimes de contratação | US-002 | REQ-02 | spec-004 §2-3 | Não executada |
| `REQ-03::UAT-03::product::spread-iof-audit` | Encargos spread+IOF, 2 casas | US-003 | REQ-03 | spec-004 §2, ADR-016 D1-D3 | Não executada |
| `REQ-04::UAT-04::product::invoice-pdf` | Emissão invoice PDF | US-004 | REQ-04 | spec-004 §6, spec-007 §3.1, ADR-016 D4 | Não executada |
| `REQ-06::UAT-05::product::ui-browsers` | Interface responsiva | US-005 | REQ-06 | spec-008 | Não executada |
| `REQ-07::UAT-06::product::cache-reduction` | Cache reduz chamadas API | US-006 | REQ-07 | spec-004 §4, spec-006 NF-04 | Não executada |
| `REQ-08::UAT-07::product::coverage-gate` | Cobertura ≥80% por CI | US-008 | REQ-08 | spec-011, ci.yml:170 | Não executada |
| `container::F-01` | Reprodutibilidade `docker compose up --build` | — | infra | spec-005 §12 F-01 | Não executada |
| `container::F-02` | Simulação E2E pelos 5 regimes | — | infra | spec-005 §12 F-02 | Não executada |
| `container::F-03` | Invoice PDF ≤3s, sem PII em logs | — | infra | spec-005 §12 F-03 | Não executada |
| `container::F-04` | Isolamento: `front` não alcança `db:5432` | — | infra | spec-005 §12 F-04 | Não executada |
| `container::F-05` | Degradação: `db` parado → 503 canônico | — | infra | spec-005 §12 F-05 | Não executada |
| `container::F-06` | Migração Alembic upgrade/downgrade | — | infra | spec-005 §12 F-06 | Não executada |
| `container::F-07` | Segurança: 100% controles do bloco §6 | — | infra | spec-005 §12 F-07 | Não executada |

**Cobertura de testes automatizados (baseline atual):** `pytest tests/agents/ -q` = 4 failed / 149 passed / 1 skipped (4 falhas preexistentes de report/wiring, não novas). Cobertura sobre `src/` exigida: ≥80% (`--cov-fail-under=80`, ci.yml:170).

**Cobertura analizada nesta rodada:** 0/14 casos executados. A cobertura analítica (mapeamento REQ→US→spec) está 100% mapeada acima, mas sem execução de produto.

---

## 3. Ciclo de implementação (fase N6.2)

| Marco | Data | Observação |
|-------|------|------------|
| Fechamento rodada anterior | — | primeira rodada; não há anterior |
| Setup do ambiente (stack separada) | EM EXECUÇÃO | `docker compose up --build` com db, migrate, back, front, proxy (commit `abc7350`) |
| Execução dos fluxos críticos | PENDENTE | aguarda produto rodando em `main` |
| Veredito binário | PENDENTE | APROVADA / REPROVADA |
| Fechamento desta rodada | PENDENTE | após veredito e registro de defeitos |

**Ciclo:** a rodada 001 inicia com o ambiente de camadas separado já implementado (commit `abc7350`) e CI/CD com gates (commit `d657118`..`2765903`). O ciclo fecha quando os 14 casos forem executados e o veredito binário for registrado neste relatório.

---

## 4. Registro de defeitos (schema DEF-UAT-NNN)

Sem defeitos registrados nesta rodada (não executada). Quando executados, cada defeito segue:

| Campo | Valores | Regra |
|-------|---------|-------|
| id | `DEF-UAT-NNN` | sequencial por run |
| severity | `critical` \| `blocking` \| `major` \| `minor` | critical/blocking = reprovam a UAT |
| trace_id | `REQ-x::UAT-nn::product::case` ou `container::F-0N` | caso reprodutor |
| repro | comando + run id + exit code + timestamp | obrigatório |
| status | `open` \| `backlog` \| `closed` | open em critical/blocking = UAT reprovada |
| decision | PO ou CCB | ato humano (constitution.md:53) |

---

## 5. Evidências desta rodada

Pasta: `docs/uat/rodada-001/evidencias/` — vazia (nenhuma execução ainda).

Padrão de arquivo: `<id>__US-<slug>__<yyyymmdd>__run<nn>.log\|.png`

Exemplos a serem gerados na execução:
- `UAT-04__US-004__20261105__run01.png` (invoice PDF)
- `F-01__container__20261105__run01.log` (reprodutibilidade)

Retenção: permanente, versionada em git, conteúdo exclusivamente sintético.

---

## 6. Rastreabilidade

| Fonte | Onde neste relatório |
|-------|----------------------|
| spec-009 (UAT produto) | §1 (critério binário), §2 (trace ids produto), §5 |
| spec-005 §12 (UAT camadas) | §2 (trace ids F-0N), §5 |
| spec-004 (backend) | §2 (cobertura REQ-01..04) |
| spec-007 (modelo invoice) | §2 (UAT-04) |
| spec-011 (CI/CD) | §2 (coverage UAT-07) |
| constitution.md (P-04) | header, retenção de evidências |

---

**Próximo passo:** executar os 14 casos quando o produto estiver rodando em `main`, preencher taxa de aceite, cobertura e registro de defeitos, e registrar o veredito binário neste mesmo arquivo.
