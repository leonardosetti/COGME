---
id: HF-0604
title: "Consulta de dominio: CI/CD, drift G-05 e camada CI (B.7/B.10/C.4)"
task: TA-0048
sender: agent-nexus-prime-ultimate
agent: agent-devops
action: consult
created: 2026-11-03
kill_switch: inherited
status: dispatched
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0604 — Consulta de dominio: CI/CD, drift G-05 e camada CI (B.7/B.10/C.4)

## Tarefa (meio-duplex — sem escrita de arquivos)
1. Leia seu contrato: .opencode/agents/agent-devops.md
2. Leia as fontes citadas abaixo.
3. Produza PARCELA DE CONSULTA (JSON) com recomendacoes para a futura spec-011 (pipeline CI/CD: lint+testes <=5 min/push, falha bloqueando merge) e para spec-014 (camada CI como camada do Art. 10.1): estado REAL de .github/workflows/ci.yml (audite o drift G-05: ledger:24 registra ci.yml nao vazio enquanto plano dizia vazio), nome exato do job de rede de contratos (fecha C.4: spec-005:210 `UNKNOWN - verify`), gates pytest+cobertura>=80, disciplina Free Tier GitHub Actions, e o que DEVE ficar `UNKNOWN - verify`.
NAO crie arquivos. NAO edite nada. Responda apenas a parcela.

## Fontes
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:39 (B.7), :42 (B.10), :51 (C.4), :59 (D.2 onda 5)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md:72 (REQ-11), :167 (US-011)
- .ai/specs/spec-005-container-layers-v1.spec.md:198-210 (SS8), :210, :352
- .ai/agents/ledger.yaml:24 (drift G-05)
- docs/planos/plano-granular/plano-producao-agentes.md:33 (G-05), :133-143 (onda 5)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0048","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}

## RESPOSTA — PARCELA DE CONSULTA (TA-0048 / agent-devops, 2026-11-03)

```json
{
  "task_id": "TA-0048",
  "status": "accepted",
  "parcel": {
    "dod": true,
    "artifacts": [],
    "notes": "ESTADO REAL ci.yml (189 linhas, 7170 B, auditado 2026-11-03): 6 jobs — kill-switch-check (ci.yml:17, primeiro, Art. 4.6), foss-compliance (:36, scanner credenciais :50-59), sdd-validation (:69, validate_nexus_yaml+dag_validator), agent-health (:91), test-suite (:108, pytest --cov-fail-under=80 fail-closed :170, Postgres digest-pinned :117), final-status (:176); triggers push/PR main + concurrency cancel-in-progress (:9-11); timeout 15min (:111). sddai-verify.yml 44 linhas (confere spec-005:203).\nDRIFT G-05 CONFIRMADO/FECHAVEL: plano-producao-agentes.md:33 ('ci.yml vazio') obsoleto; ledger.yaml:24 (TA-0029, HISTORICO nao editar) ja registrava 189 linhas; spec-011 registra G-05 como FECHADO por implementacao preexistente, delta only.\nC.4 FECHA: job 'contract-network' NAO EXISTE (grep sem match). Recomendacao: spec-011 FIXA nome contract-network como job novo: stack efemera digest-pinned, casos SS7.3 spec-005, needs:[test-suite], timeout <=10, sem porta no host.\nCORRECOES RECOMENDADAS spec-011: (1) US-011 nao atendido — timeout 15 -> <=5 min, paralelizar flake8/mypy em job proprio; (2) adicionar permissions: contents: read (ausente); (3) SHA-pin de actions (checkout@v4 :23, setup-python@v5 :136 — kill switch #4); (4) artifact upload coverage.xml+junit (filenames LGPD-safe); (5) REMOVER append final-status em ledger.yaml (:185-189) — escrita perdida em runner efemero, nunca pushed; substituir por GITHUB_STEP_SUMMARY + run URL (CI le, nunca muta repo); (6) merge-bloqueio: CI green = pre-condicao, nunca aprovacao (gatekeeper+Humano).\nFREE TIER P-01 (Bypass registrado spec-005:211/constitution:84): triggers minimos, cancel-in-progress, sem matriz, sem self-hosted com secrets, auditoria mensal de minutes.\nATENCAO: pytest tests/ inclui tests/agents baseline 4F/149P — UNKNOWN - verify se CI fica verde; proibido skip (kill switch #1); escopo explicito (unit+integration+agents).\nUNKNOWN - verify: (a) required status checks/branch protection (config GitHub, nao filesystem); (b) wall-clock real por run; (c) build-layers docker compose no orcamento Free Tier; (d) B.10 — recomendo spec-014 cobrir SO a camada CI (workflows como camada Art. 10.1, Bypass P-01, boundaries: gates como contratos de fronteira, zero secrets) e desagregar L1 runtime de agentes para spec propria."
  },
  "kill_switch": "inherited"
}
```


## Critérios de Aceite
- [ ] Parcelo de consulta entregue com recomendações de CI/CD
- [ ] Drift G-05 auditado e documentado (estado real do ci.yml vs plano)
- [ ] Nome do job contract-network proposto (não decisão final)
