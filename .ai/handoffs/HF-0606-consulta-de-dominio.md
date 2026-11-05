---
id: ai-handoffs-hf-0606-consulta-de-dominio
title: 'Consulta de dominio: LGPD de produto — fundamentos para CCB (B.3/GAP-08)'
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0606-consulta-de-dominio.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---

# HF-0606 — Consulta de dominio: LGPD de produto — fundamentos para CCB (B.3/GAP-08)

## Tarefa (meio-duplex — SEM escrita de arquivos; emissao condicionada a CCB/PO)
1. Leia seu contrato: .opencode/agents/agent-compliance-governance.md
2. Leia as fontes citadas abaixo.
3. Produza PARCELA DE CONSULTA (JSON) com os FUNDAMENTOS de compliance para a futura PROPOSTA de spec de LGPD de produto (B.3, GAP-08): criterios de minimizacao e tratamento de dados pessoais/financeiros na invoice e nos logs sob P-04 (minimo necessario, sem PII em artefatos tecnicos de agentes, direito ao esquecimento por design), LISTA EXPLICITA das decisoes que o CCB/PO precisa tomar antes da ratificacao (E-01..E-08 relacionadas), e o que DEVE ficar `UNKNOWN - verify`. IMPORTANTE: a emissao da spec e condicionada a decisao previa de CCB/PO (LISTA B.3); sua parcela NAO autoriza emissao aprovada — servira a uma PROPOSTA draft.
NAO crie arquivos. NAO edite nada. Responda apenas a parcela.

## Fontes
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:35 (B.3), :67 (E.1)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md:107 (GAP-08)
- constitution.md:36 (P-04) e Art. 3 (LGPD primary), Art. 5.1

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0050","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}

## RESPOSTA — PARCELA DE CONSULTA (TA-0050 / agent-compliance-governance, 2026-11-03)

```json
{
  "task_id": "TA-0050",
  "status": "accepted",
  "parcel": {
    "dod": true,
    "artifacts": [],
    "notes": "(1) MINIMIZACAO (LGPD art. 6, I/III): inventario minimo invoice — nome, CPF/CNPJ, periodo, descricao, valores; 'endereco' (spec-004:126) so se necessario a finalidade REQ-04. CPF/dados bancarios = pessoais COMUNS, nao sensiveis (art. 5, II) — basta base art. 7, sem regime art. 11.\n(2) LOGS: sem PII, sem valores, sem corpo de requisicao (spec-004:126), elevado a criterio de produto sob Art. 7 + P-04 (constitution.md:90); artefatos de agente com frontmatter lgpd-class (padrao spec-002:19; DoR item 10 spec-002:201).\n(3) ESQUECIMENTO POR DESIGN (art. 18): MVP single-user/local (sem auth — OS-01; P-02/P-03) -> erasure local sem propagacao remota; acesso do titular trivial (usuario = titular).\n(4) BASES LEGAIS (art. 7): invoice com dados de TERCEIROS (cliente) -> candidata primaria art. 7, V (execucao de contrato); so dados do proprio usuario -> avaliar exclusao art. 4, I (fins exclusivamente privados) — questao juridica nova, revisao humana.\nDRIFT DETECTADO (Art. 2.5): E-01..E-08 JA RATIFICADAS 26/10/2026 — constitution v1.1.0 (CHANGELOG :226; co-assinatura :245), v1.2.1 vigente. LISTA E.1 (:67) obsoleta. Relacao LGPD nas emendas: E-02 (minimizacao na co-assinatura, sem nome civil, spec-001:213-219) e E-03 (PII fora de camada de imagem, Art. 10.2, spec-001:238-239).\nDECISOES CCB/PO ANTES DA RATIFICACAO DE B.3 (Art. 5.1): D1 — tensao spec-004:126 ('invoice nunca persistida') vs US-016/017+GAP-04: transitoria OU persistida com retencao+erase; D2 — controlador/titular e exclusao art. 4, I; D3 — base legal art. 7, V se terceiros; D4 — conjunto minimo de campos (alimenta B.4); D5 — politica de logs sem PII/valores como criterio de aceite; D6 — retencao e rota de erase se persistida; D7 — corrigir drift E.1 da LISTA.\nUNKNOWN - verify: invoice inclui dados de terceiros/cliente (modelo GAP-04 inexistente; 'partes' em spec-004 SS6); aplicabilidade art. 4, I; CNPJ fora do escopo LGPD — confirmar; retencao fx_quotes (dados publicos, LGPD n/a, spec-004:122). Esta parcela NAO autoriza emissao aprovada."
  },
  "kill_switch": "inherited"
}
```


## Critérios de Aceite
- [ ] Parcelo de consulta entregue com fundamentos de LGPD de produto
- [ ] Lista explícita de decisões CCB/PO pendentes (D1-D7) identificada
- [ ] Nenhuma decisão promovida — apenas proposta condicionada a CCB
