---
id: HF-0620
title: "Repovoar .ai/specs/eap.md (A.3) — fases N1..N11 com rastreabilidade"
task: TA-0064
sender: agent-nexus-prime-ultimate
target: agent-sdd-specialist
action: spec
created: 2026-11-03
kill_switch: inherited
status: emitted
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0620 — Repovoar .ai/specs/eap.md (A.3) — fases N1..N11 com rastreabilidade

## Tarefa
Repovoar .ai/specs/eap.md (0 B, item A.3 da LISTA): artefato NAO VAZIO declarando as fases EAP (N1..N11) derivadas das fontes sobreviventes (plano-integral-tap-1-2-3-4-5.md; PDF:645), com rastreabilidade arquivo:linha por fase. Frontmatter conforme MANIFEST SS1 adaptado a arquivo pinned (id, title, status: draft, version: 1.0.0 — KB-INDEX EAP-001, custody, task: TA-0064, sender, kill_switch: inherited, trace). ATENCAO ao DoR da classe diagrama (KB-INDEX EAP-001: SVGs placeholders exigem fonte svg/mermaid): inclua diagrama mermaid textual (fonte valida) quando derivado do plano-integral, ou declare `UNKNOWN - verify` para o que nao tiver fonte. Validar a correspondencia das fases com o corpo do plano-integral (grep N1..N11).

## Fontes obrigatorias
- Seu contrato: .opencode/agents/agent-sdd-specialist.md
- Template: .ai/specs/MANIFEST.md (SS1 adaptado a arquivo pinned)
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:27 (A.3)
- docs/planos/plano-granular/plano-integral-tap-1-2-3-4-5.md (FONTE PRIMARIA — fases N1..N11)
- .ai/specs/kb-taxonomy.md (DoR classe diagrama)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0064","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}
