---
id: docs-uat-readme
title: Pasta de evidências de UAT — COGME
type: readme
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/uat/README.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- uat
- docs
- adequado-a-norma
---
# Pasta de evidências de UAT — COGME

Destino único e definitivo de todas as evidências de UAT do projeto COGME, conforme decisão GP/CCB de 05/11/2026 (pendência #6 dos 7 bloqueantes — decisão fechada, não mais condicionante).

## Princípios (P-04, constitution.md:90)

- **Conteúdo exclusivamente sintético:** nenhum dado pessoal, financeiro ou de terceiros real aparece nas evidências.
- **Retenção permanente:** versionada em git como trilha de auditoria, sem exclusão.
- **Origem:** execuções de UAT de produto (fase N6.2) e de camadas (fase containers, spec-005 §12).
- **Classificação:** por rodada de execução (ex.: `rodada-001`, `rodada-002`, …).

## Estrutura por rodada

```
docs/uat/
├── README.md                          # este índice
├── rodada-001/
│   ├── relatorio-analitico.md         # relatório analítico da rodada (taxa de aceite, cobertura, ciclo)
│   └── evidencias/
│       ├── UAT-01__US-001__20261105__run01.log
│       ├── UAT-04__US-004__20261105__run01.png
│       └── F-01__container__20261105__run01.log
├── rodada-002/
│   └── ...
```

## Padrão de nomenclatura de arquivos de evidência

`<id>__US-<slug>__<yyyymmdd>__run<nn>.<ext>`

- `<id>`: `UAT-nn` (fluxos de produto, spec-009 §3.3) ou `F-0N` (casos de camada, spec-005 §12)
- `<slug>`: slug da User Story (ex.: `US-001`, `US-004`)
- `<yyyymmdd>`: data da execução
- `<nn>`: número de sequência da execução no dia

## Relato analítico de rodada

Cada rodada produz um `relatorio-analitico.md` com:

| Bloco | Conteúdo obrigatório |
|-------|----------------------|
| Taxa de aceite | % de fluxos críticos PASS (100% exigido para aprovação binária, spec-009 §3.2) |
| Cobertura analizada | quais REQ/US/trace ids foram cobertos, com rastreabilidade `arquivo:linha` |
| Ciclo de implementação | período entre o fechamento da rodada anterior e esta; datas de setup, execução e veredito |
| Registro de defeitos | schema `DEF-UAT-NNN` com severidade (critical/blocking/major/minor), trace_id, repro, status, decisão |
| Veredito binário | APROVADA (100% PASS + zero critical/blocking abertos) ou REPROVADA |

## Referências

- `spec-009-uat-produto-v1.spec.md` — plano e roteiro de UAT de produto (fase N6.2)
- `spec-005-container-layers-v1.spec.md` §12 — UAT de camadas (F-01..F-07)
- `constitution.md` Art. 5.1, Art. 7, P-04

## Histórico de rodadas

| Rodada | Período | Veredito | Relatório | Evidências |
|--------|---------|----------|-----------|------------|
| rodada-001 | 05/11/2026 | EM EXECUÇÃO | `rodada-001/relatorio-analitico.md` | `rodada-001/evidencias/` |
