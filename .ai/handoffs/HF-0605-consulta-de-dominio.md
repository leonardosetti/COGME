---
id: HF-0605
title: "Consulta de dominio: qualidade PDCA + Ishikawa 6M (B.6/REQ-10)"
task: TA-0049
sender: agent-nexus-prime-ultimate
target: agent-quality-architect-specialist
action: consult
created: 2026-11-03
kill_switch: inherited
status: emitted
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0605 — Consulta de dominio: qualidade PDCA + Ishikawa 6M (B.6/REQ-10)

## Tarefa (meio-duplex — sem escrita de arquivos)
1. Leia seu contrato: .opencode/agents/agent-quality-architect-specialist.md
2. Leia as fontes citadas abaixo.
3. Produza PARCELA DE CONSULTA (JSON) com recomendacoes para a futura spec-010 (entrega de qualidade REQ-10, fase N6.3): estrutura dos 12 ciclos PDCA consolidados, metodologia do diagrama Ishikawa 6M (6M: maquina, mao de obra, metodo, material, medida, meio-ambiente) aplicada ao COGME, relacao com plano-qualidade.md v1.1.0 e onda 6 do plano de producao (A.19-A.22), e o que DEVE ficar `UNKNOWN - verify`.
NAO crie arquivos. NAO edite nada. Responda apenas a parcela.

## Fontes
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:38 (B.6), :60 (D.3 onda 6)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md:71 (REQ-10)
- docs/planos/plano-granular/plano-producao-agentes.md:145-152 (onda 6)
- docs/planos/plano-granular/plano-qualidade.md (baseline v1.1.0)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0049","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}

## RESPOSTA — PARCELA DE CONSULTA (TA-0049 / agent-quality-architect-specialist, 2026-11-03)

```json
{
  "task_id": "TA-0049",
  "status": "accepted",
  "parcel": {
    "dod": true,
    "artifacts": [],
    "notes": "(1) 12 PDCAs JA EXISTEM: plano-qualidade.md v1.1.0 SS5.6 (PDCA-N1..N12, um por fase EAP, formato GMV 6 linhas: Problema->Acao->Responsavel->Metrica->Verificacao->Licao; NC-Q4 fixa 12 fases). Spec-010 NAO recria: referencia como baseline, consolida em 3 grupos por marco (MF1=N1-N4 verif M1; MF2=N5-N8+N10 verif M3; MF3=N9+N11-N12 verif M4), registra status executado/pendente (M1-M3 parcialmente vencidos), revalida metricas contra REQ-08 (>=80%), REQ-09 (zero criticos), REQ-11 (CI <=5min).\n(2) ISHIKAWA 6M: SS5.7 define 3 efeitos (coverage<80%; defeitos criticos UAT; cycle time>3 dias) com 6M = Metodo, Maquina, Mao de Obra, Material, Medida, Meio Ambiente. REQ-10 exige '12 PDCAs + diagrama' no singular (spec-002:71); adotar 3 diagramas (superset satisfaz minimo) com reconciliacao documentada. Formato mermaid flowchart LR, efeito a direita, 6M nos-branch, causas como folhas com IDs (ISH1-MED-01) ligadas as acoes SS5.7; substituir PNGs — drift: FIG-5 aponta mesmo PNG de FIG-3 (:326 vs :294).\n(3) ONDA 6: A.19 qa-sdet (evidencia coverage), A.20 reviewer (taxa aprovacao review), A.21 gatekeeper (regra de ouro SS5.2: CI verde+coverage+review+tasklist), A.22 auditor (verificacao fim-a-fim); gatilhos SS5.3; parcela quality gate pass|amend|block.\n(4) ACEITE: 12 PDCAs com 6 campos e metrica mensuravel; 3 Ishikawa 6M com causas especificas COGME zero genericas; 100% rastreabilidade arquivo:linha; RACI onda 6; fora escopo: NFR (B.2), UAT (B.5), CI (B.7) — cross-ref.\n(5) UNKNOWN - verify: singular/plural diagrama req_1.0.md:25; existencia PNGs em diagrams/; SSOT plano (contrato cita .ai/specs/plano-qualidade.md, real e docs/planos/plano-granular/plano-qualidade.md); status execucao real PDCAs N1-N7; conformidade P-01/P-02 de SonarQube Free Tier e codecov (nuvem); definicao canonica N6.3 (eap.md 0 B, A.3)."
  },
  "kill_switch": "inherited"
}
```
