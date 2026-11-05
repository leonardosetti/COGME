---
id: ai-handoffs-hf-0621-requisitos-repovoar
title: Repovoar .ai/specs/requisitos.md (A.1) — gate E RATIFICADO (drift E.1 corrigido)
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0621-requisitos-repovoar.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---

# HF-0621 — Repovoar .ai/specs/requisitos.md (A.1)

## Condicao de desbloqueio VERIFICADA
A.1 era condicionada ao gate E (E-01..E-08). VERIFICADO no filesystem (Art. 2.5):
constitution.md:226 — "1.1.0 — 2026-10-26: CCB ratifica as emendas E-01..E-08 da Rodada 1";
tabela de co-assinatura constitution.md:245. Portanto o gate E foi DECIDIDO; a condicao
"re-emissao de ADRs + CCB" da spec-002:208-224 para E-01..E-08 esta satisfeita na parte
constitucional. O orquestrador autoriza a emisso com regra de ouro: TRANSCRICAO
rastreavel das fontes sobreviventes — NENHUM requisito novo inventado (P-08).

## Tarefa
Repovoar .ai/specs/requisitos.md (0 B, item A.1): SSOT de RF/RNF da camada 5.
Fontes obrigatorias e unicas: REQ-01..REQ-15 conforme .ai/specs/spec-002-requisitos-review-round-1.spec.md
(tabela A.1 e corpo; incluir US mapeadas), emendas ratificadas E-01..E-08 (constitution.md
CHANGELOG/tabela; E-02 e E-03 impactam requisitos de dados/LGPD), NFR mapeados para
spec-006 (B.2) por cross-ref. Frontmatter: id, title, status: draft, version: 1.0.0
(KB-INDEX REQ-SPEC-001), custody, task: TA-0065, sender, kill_switch: inherited, trace.
Para CADA requisito: rastreabilidade arquivo:linha. O que nao tiver fonte = `UNKNOWN - verify`.

## Regras
- NAO editar spec-002/spec-001/constitution/ADRs; apenas criar conteudo de requisitos.md.
- Marcadores de status: seguir estado declarado nas fontes; nao promover nada a "aprovado".
- Consulta TA-0050 (compliance): docs/uat/... decisoes D1-D7 sao condicionantes, nao requisitos aprovados.
- Documento ponteiro docs/requisitos/requisitos.md ja aponta para ca (KB-INDEX) — nao editar.
- Contrato de resposta: parcela JSON meio-duplex (dod, artifacts, notes).


## Critérios de Aceite
- [ ] Artefato requisitos.md repovoado com RF/RNF/US
- [ ] Rastreabilidade REQ→US (15/15) declarada
- [ ] Gate E verificado como satisfeito (constitution.md:226)
