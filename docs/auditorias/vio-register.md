---
id: vio-register
title: Registro de violações COGME (VIO-NNN) — append-only, nunca reescrito (persona agent-project-auditor §VIOLATION REGISTER)
version: 1.0.0
class: register-vio
status: active
owner: agent-project-auditor
derived-from:
  - .ai/agents/ledger.yaml (TA-0010 — AUD-2610-01: "5 VIO propostos (registro pendente de autorização de escrita)")
  - .ai/agents/ledger.yaml (TA-0013 — CCB 23/10: C1..C5, autorização de correção)
  - .opencode/agents/agent-project-auditor.md (custódia; addenda only)
last-revised: 2026-10-23
lgpd-class: n/a
caveats:
  - "AUD-2610-01 não existe como arquivo datado em FS (evidence gap declarado): os 5 VIO abaixo são reconstruídos dos temas documentados no ledger TA-0010/TA-0013; numeração atribuída agora, na primeira materialização do registro"
  - "Imutabilidade: entradas após emissão só via addenda (status closed/open); falses ficam marcados, nunca apagados (persona §DON'T 3)"
---

# Registro VIO — COGME (append-only)

| VIO-NNN | data | ator | tipo | evidência | status |
|---|---|---|---|---|---|
| VIO-001 | 2026-10-22 | (drift técnico, agente não identificado em ledger) | sandbox fora-de-escopo (drift R-01: Next/React/mysql2/auth multiusuário vs canônica FastAPI/SQLite/HTMX) | ledger TA-0009; TA-0013 C1; `git status` staged `D .experimental/COGME/*` (51+ paths); FS vivo sem `.experimental` (find maxdepth 2 = vazio) | **RESOLVIDO** (CCB C1 23/10 — git rm executado; eliminação staged, commit pendente na onda; sem registro formal exigido) |
| VIO-002 | 2026-10-22 | artefatos doc (glossário e derivados) | grafia incorreta do stakeholder "Carletto" (canônico TAP v3: "Carleto") | ledger TA-0013 C2; `docs/conhecimento/glossario.md` v3.2.0 (changelog linha 23: 8 fix CCB C2); uso vigente em docs vivo = 0; 15 hits residuais todos metadados de correção (OKB.md:501/507/550 histórico C5; KB-INDEX.md:16/79/90 resíduo); resíduo declarado: `docs/slides_apresentacao/capa.svg` (1 ocorrência textual) + PDFs binários | **RESOLVIDO-COM-RESSALVA** (correção vigente executada; restantes: plano-qualidade.md:388, plano-cronograma.md:152 e plano-integral ainda listam saneamento do glossário como "próxima revisão (pós-M1)" — metadado desatualizado; resíduos capa.svg/PDF pendem CCB) |
| VIO-003 | 2026-10-22 | orchestrator/ondu antecedente | artefatos autorizativos prometidos vazios/0B (ADRs 001-004, planos 6-8, docs/requisitos, TAP.md) | ledger TA-0008 ("planos 6-8 vazios, ADR-001..004 vazios"); FS 23/10: ADR-001..004 4,2–4,9KB com frontmatter 10 campos status=ratified v1.1.0 (ls + head meta); plano-riscos/recursos/comunicacoes 4,1–5,0KB status=active v1.0.0; .ai/specs/tap-eap-requisitos 6,1–7,0KB; TAP.md 1026B ponteiro | **RESOLVIDO-COM-RESSALVA** (corpo autorizativo vivo; baselines `docs/metricas/baseline.md` 392B e `docs/dependencias/registro.md` 379B permanecem stubs frontmatter-only com gap declarado DoR — TA-0014) |
| VIO-004 | 2026-10-22 | custódia KB | contradição canônica (OKB multiplicado em 3 corpora; map_report COBECO estranho) | ledger TA-0007 ("OKB em 3 corpora"); TA-0013 C5; OKB.md v4.0.0 594l (wc -l), 10 seções + histórico; `docs/archive/legacy-md-artifact/OKB_COGME_v3.1-draft-aplicado-em-v4.md` arquivado (find); KB-TAX-001 ratified 1.1.0 | **RESOLVIDO** (corpora única v4.0.0; variantes históricas arquivadas por proveniência) |
| VIO-005 | 2026-10-22 | governança | roster sem ratificação expressa e LGPD divergente (diretriz persona LGPD-primary vs decisão CCB de estacionar no MVP) | ledger TA-0013 C3 (ratificação expressa: validate 27/27 ok) e C4 (LGPD fora do MVP por decisão Humana Art. 5.1 — consideração pós-entrega; LGPD segue em persona FS) | **RESOLVIDO** (C3+C4 ratificados; co-assinatura humana da constitution.md 1.2.0 segue pendente — pendência ratificatória à parte, não violação) |

**Nota de custódia (append-only conforme método):** primeira materialização do registro em FS em 2026-10-23 (AUD-2610-02). Entradas anteriores viviam somente no ledger (TA-0010). Nada é reescrito; correções futuras = linhas novas.
