---
id: HF-0601
title: "Consulta de dominio: modelo de dados da invoice (B.4/GAP-04)"
task: TA-0045
sender: agent-nexus-prime-ultimate
agent: agent-dba
action: consult
created: 2026-11-03
kill_switch: inherited
status: dispatched
source: docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md (rodada 1 de specs)
---

# HF-0601 — Consulta de dominio: modelo de dados da invoice (B.4/GAP-04)

## Tarefa (meio-duplex — sem escrita de arquivos)
1. Leia seu contrato: .opencode/agents/agent-dba.md
2. Leia as fontes citadas abaixo.
3. Produza PARCELA DE CONSULTA (JSON) com as recomendacoes de dominio de dados para a futura spec-007 (modelo canonico de dados da invoice): campos obrigatorios (dados bancarios, CPF/CNPJ, periodo de apuracao), tipagem, constraints, indices, integridade com o contrato POST /v1/invoice da spec-004, PostgreSQL como banco canonico (glossario v3.2.0), minimizacao LGPD P-04 (sem PII em logs/artefatos tecnicos), e o que DEVE ficar como `UNKNOWN - verify`.
NAO crie arquivos. NAO edite nada. Responda apenas a parcela.

## Fontes
- docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:36 (item B.4, origem GAP-04)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md:103 (GAP-04), :161 (US-004)
- .ai/specs/spec-004-backend-mvp-v1.spec.md (contrato POST /v1/invoice, SS2)
- docs/conhecimento/glossario.md (PostgreSQL canonico)
- constitution.md:36 (P-04)

## Contrato de resposta (meio-duplex)
Parcela JSON obrigatoria:
{"task_id":"TA-0045","status":"accepted|rejected","parcel":{"dod":true,"artifacts":["<paths>"],"notes":"<...>"},"kill_switch":"inherited"}

## RESPOSTA — PARCELA DE CONSULTA (TA-0045 / agent-dba, 2026-11-03)

```json
{
  "task_id": "TA-0045",
  "status": "accepted",
  "parcel": {
    "dod": true,
    "artifacts": [],
    "notes": "BANCO: PostgreSQL 15+ canonico (ADR-010, glossario v3.2.0) revoga SQLite; contrato agent-dba ancora ADR-001/SQLite — drift a corrigir em emenda propria. Alembic upgrade/downgrade obrigatorio (spec-004 SS5); Repository Protocol; regra de negocio fora de SQLAlchemy.\nTABELA invoices (se/quando persistir — ver UNKNOWN): invoice_number varchar(40) NOT NULL; issue_date DATE NOT NULL; issuer/client: name varchar(120) NOT NULL, tax_id_digits char(14) NULL CHECK char_length IN (11,14) — CPF/CNPJ normalizado sem mascara, digito validado app-side (CHECK SQL nao faz mod-11), address varchar(240) NULL; dados bancarios minimos (banco char(3), agencia varchar(10), conta+digito varchar(20), pix_key varchar(77) NULL) somente se template US-004 exigir (minimizacao P-04); periodo_inicio/periodo_fim DATE NOT NULL CHECK (fim>=inicio); regime CHECK IN 5 enums spec-004; currency char(3) CHECK ('USD','EUR'); amount numeric(18,2) >0; quantity numeric(12,2); spread_pct/iof_pct numeric(6,4) 0-100; gross_brl/spread_brl/iof_brl/net_brl numeric(18,2); effective_rate numeric(18,6); NUNCA float/REAL para dinheiro; created_at timestamptz DEFAULT now() explicito.\nCONSTRAINTS/INDICES: PK identity bigint; UNIQUE (issuer_tax_id, invoice_number); servidor recalcula simulacao (spec-004 SS6) — colunas de valores casam com reprocesso; NENHUM indice alem de PK/UNIQUE ate EXPLAIN QUERY PLAN real; FKs explicitas ON DELETE/UPDATE se surgirem.\nLGPD P-04 (constitution.md:90 — handoff citava :36, drift): tax_id/dados bancarios so com consentimento; sem PII em logs (spec-004:126 veta); path DELETE right-to-forget obrigatorio; seeds/fixtures sinteticos; backups sem PII ou exclusao documentada; sem secrets em rows.\nUNKNOWN - verify: (1) persistencia da invoice — spec-004:126 'nunca persistida' vs spec-007 -> decisao CCB/PO (depende B.3); (2) campos bancarios exatos do template (so legado); (3) numeracao global vs por emissor/ano; (4) tax_id aceita CPF, CNPJ ou ambos; (5) semantica do periodo por regime (hourly vs fixed); (6) retencao; (7) ratificacao ADR-010 via emenda Art. 1.3 (TAP congelado diz SQLite, plano-escopo:76)."
  },
  "kill_switch": "inherited"
}
```


## Critérios de Aceite
- [ ] Parcelo de consulta entregue com recomendações de domínio de dados da invoice
- [ ] Todas as fontes citadas (spec-004, spec-002, plano-integral) foram lidas e consideradas
- [ ] Nenhuma decisão promovida — apenas recomendações de domínio para futura spec-007
