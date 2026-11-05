---
id: HF-0602
title: "Consulta de dominio: frontend web responsivo (B.1/REQ-06)"
task: TA-0046
sender: agent-nexus-prime-ultimate
agent: agent-ui-ux-advisor
action: consult
created: 2026-11-03
kill_switch: inherited
status: dispatched
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0602 — Consulta de dominio: frontend web responsivo (B.1/REQ-06)

## Tarefa (meio-duplex — sem escrita de arquivos)
1. Leia seu contrato: .opencode/agents/agent-ui-ux-advisor.md
2. Leia as fontes citadas abaixo.
3. Produza PARCELA DE CONSULTA (JSON) com recomendacoes para a futura spec-008 (interface web responsiva 100% FOSS, camada `front` da spec-005): browsers alvo (REQ-06: Chrome/Firefox/Edge ultimas 2 versoes), requisitos de templates, UX dos fluxos cotacao/invoice (US-001..015 em spec-002), acessibilidade baseline, o estado vazio atual (index.html 0 B, static/ vazio), e o que DEVE ficar `UNKNOWN - verify`.
NAO crie arquivos. NAO edite nada. Responda apenas a parcela.

## Fontes
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:33 (item B.1), :58 (D.1 onda 4 A.11-A.12)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md:67 (REQ-06)
- .ai/specs/spec-005-container-layers-v1.spec.md:30 (index.html 0 B, static/ vazio), camada front
- docs/planos/plano-granular/plano-producao-agentes.md:121-131 (onda 4)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0046","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}

## RESPOSTA — PARCELA DE CONSULTA (TA-0046 / agent-ui-ux-advisor, 2026-11-03)

```json
{
  "task_id": "TA-0046",
  "status": "accepted",
  "parcel": {
    "dod": true,
    "artifacts": [],
    "notes": "(1) BROWSERS: matriz aceite = Chrome/Firefox/Edge ultimas 2 versoes (REQ-06, spec-002:67; US-005 sem quebra funcional). Mobile-first em CSS; mobile nativo OS-06 OUT; nao prometer Safari. Server-side templates Jinja2, HTML5+CSS3+JS vanilla (ADR-001:34) com progressive enhancement: formularios funcionam sem JS; HTMX so via ADR whiteliste (hoje ADR-001 manda vanilla — decisao de dependencia = ADR). Assets open-license vendored em static/; zero recursos remotos (url_fetcher recusa remotos, spec-004:130).\n(2) TEMPLATES: base.html + index/simulacao + invoice form + partials resultado/erro; cada tela com estados loading/empty/error/success; labels 1:1 com schemas.py (currency, regime, amount, quantity, spread_pct, iof_pct; RateQuote.rate/source/quoted_at/stale); numeros pt-BR 1.234,56; jargao definido no primeiro uso; copy PT-BR sem promessa de ganho (kill switch financeiro).\n(3) FLUXOS: cotacao -> POST /v1/simulate (form curto; regime 5 opcoes; valor; quantidade condicional; spread/IOF default); resultado com trilha auditavel bruto->despesas->liquido (2 casas); loading ate 3s P95 (C-07: 2s API vs 3s E2E); banner defasagem se stale (US-007 so se CCB ratificar); erros 400 por ErrorKey por campo e 503 com retry. Invoice -> POST /v1/invoice; valores nunca aceitos do cliente (spec-004:130); form depende do modelo GAP-04 (spec-007); download anexado.\n(4) A11Y: contraste 4.5:1 light/dark, foco visivel, labels + aria-required, tabelas navegaveis, alvos >=44px, lang=pt-BR, sem texto em imagem, sem dark patterns.\n(5) ESTADO VAZIO: index.html 0 B e static/ vazios (spec-005:30) = greenfield; spec-008 define primeiro template real e inventario src/frontend/; servico separado, mesma origem, usuario so via proxy 127.0.0.1:8080 (spec-005 SS4.3).\n(6) UNKNOWN - verify: formula spread/IOF (GAP-03); campos invoice (GAP-04/spec-007); TTL/stale (GAP-06); ratificacao US-007/016/017; whitelist HTMX via ADR; destino evidencias UAT front (spec-005:342)."
  },
  "kill_switch": "inherited"
}
```


## Critérios de Aceite
- [ ] Parcelo de consulta entregue com recomendações de UX/UI para camada front
- [ ] Todas as fontes citadas (spec-002, spec-005, plano-producao-agentes) foram lidas
- [ ] Nenhuma decisão promovida — apenas recomendações para futura spec-008
