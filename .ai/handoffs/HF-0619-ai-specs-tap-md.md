---
id: HF-0619
title: "Repovoar .ai/specs/tap.md (A.2) — transcricao da baseline congelada TAP v3"
task: TA-0063
sender: agent-nexus-prime-ultimate
agent: agent-sdd-specialist
action: spec
created: 2026-11-03
kill_switch: inherited
status: dispatched
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0619 — Repovoar .ai/specs/tap.md (A.2) — transcricao da baseline congelada TAP v3

## Tarefa
Repovoar .ai/specs/tap.md (0 B, item A.2 da LISTA): espelho NAO VAZIO da linha de base TAP v3 em regime de congelamento (ADR-005 freeze; ADR-013-a regime de emenda controlada), transcrevendo a partir das fontes sobreviventes: plano-integral-tap-1-2-3-4-5.md (fonte viva unica) e referencias do PDF. Templates: frontmatter conforme MANIFEST SS1 (spec_id NAO se aplica — arquivo pinned sem rename; use frontmatter de documento: id, title, status: draft, version: 1.0.0 (KB-INDEX TAP-001), custody, task: TA-0063, sender, kill_switch: inherited, trace). Incluir rastreabilidade arquivo:linha para cada secao transcrita e cabecalho declarando regime de congelamento + fonte canonicas (KB-INDEX: tap-cogme stub-ponteiro; TAP integral vivo = plano-integral).

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1 adaptado a arquivo pinned)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:26 (A.2)
- docs/planos/plano-granular/plano-integral-tap-1-2-3-4-5.md (FONTE PRIMARIA da transcricao)
- docs/decisoes/ADR-005-freeze.md, docs/decisoes/ADR-013-regime-emenda-tap.md (regime, leitura apenas)
- .ai/specs/kb-taxonomy.md (classe do artefato)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0063","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}


## Critérios de Aceite
- [ ] Artefato tap.md repovoado com conteúdo não vazio
- [ ] Rastreabilidade arquivo:linha para cada seção transcrita
- [ ] Regime de congelamento (ADR-005/ADR-013) declarado no cabeçalho
