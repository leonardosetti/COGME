---
id: KB-INDEX-001
title: Índice SSOT da base de conhecimento COGME (mapa único da taxonomia KB-TAX-001)
version: 1.2.0
class: spec
status: active
owner: agent-docker-specialist
derived-from:
  - .ai/specs/kb-taxonomy.md (KB-TAX-001 v1.1.0 — ratified, CCB C1–C5 23/10/2026, ledger TA-0013)
  - TA-0012/TA-0013/TA-0016/TA-0017 via .ai/agents/ledger.yaml; handoff HF-0017
  - CCB-003 (30/10/2026, GP Leonardo) — ratificação do OKB v5.1.0 e promoção a corpus canônico único
last-revised: 2026-10-30
lgpd-class: n/a
caveats:
  - "UNKNOWN-GAP: handoffs HF-* desta onda pendentes de back-link pela orchestrator (spec da taxonomia)"
  - "Cobertura parcial: licoes/diagramas/drafts remanescentes ainda não frontmatter-classificados constam da Seção 'Cobertura declarada'"
  - "OKB v5.1.0 ratificado (CCB-003, 30/10/2026): índice aponta para o corpus novo; achados ainda ABERTOS no OKB: C-03, C-05, C-06, C-12, C-21, C-22, C-24, C-25; fechados nesta rodada: C-04 (duplicatas ADR-006), C-11 (custódia), C-15 (Constituição PLENA)"
  - "grafia 'Carleto' residual em artefatos NÃO editados nesta onda: docs/slides_apresentacao/capa.svg (SVG = texto, porém fora da lista autorizada TA-0017) e PDFs binários (COGME.pdf e exportados) — PDF (binário) não é editável na onda; pendente CCB/onda futura"
---

# KB-INDEX — Índice do SSOT COGME

Índice único da base de conhecimento, conforme `KB-TAX-001 v1.1.0` (ratified 23/10/2026). Toda alegação documental consulta este índice antes do corpo; artefato ausente da tabela = fora do canon vivo. Ciclo de vida: draft → active → ratified → archived. Status `draft` com caveat "stub 0B/stub-ponteiro" satisfaz o gate G3 (não-0B ou gap declarado).

## Artefatos classificados (atualização TA-0017 23/10/2026; CCB-003 30/10/2026)

| id | caminho | classe | status | versão | owner | caveats |
|---|---|---|---|---|---|---|
| tap-cogme | docs/tap/TAP.md | plan | draft | 1.0.0 | agent-pm | "stub-ponteiro (não-0B, CCB F-06 TA-0016)"; fonte canônica: plano-integral-tap-1-2-3-4-5.md; canal SDD: .ai/specs/tap.md |
| plano-integral-tap | docs/planos/plano-integral-tap-1-2-3-4-5.md | plan | active | 1.0.0 | agent-pm | [] |
| plano-projeto-cogme | docs/planos/Plano-de-Projeto-COGME_v1.0.md | plan | active | 1.0.0 | agent-pm | divergência docx v1.0/v1.1 PENDENTE de decisão humana CCB (KB-TAX-001 4.6/G6) |
| plano-integracao | docs/planos/plano-integracao.md | plan | active | 2.0.0 | agent-pm | [] |
| plano-escopo | docs/planos/plano-escopo.md | plan | active | 1.1.0 | agent-pm | [] |
| plano-cronograma | docs/planos/plano-cronograma.md | plan | active | 1.2.0 | agent-pm | [] |
| plano-custos | docs/planos/plano-custos.md | plan | active | 1.2.0 | agent-pm | [] |
| plano-qualidade | docs/planos/plano-qualidade.md | plan | active | 1.1.0 | agent-pm | [] |
| plano-recursos | docs/planos/plano-recursos.md | plan | active | 1.0.0 | agent-pm | [] (preenchido, CCB 23/10) |
| plano-comunicacoes | docs/planos/plano-comunicacoes.md | plan | active | 1.0.0 | agent-pm | [] (preenchido, CCB 23/10) |
| plano-riscos | docs/planos/plano-riscos.md | plan | active | 1.0.0 | agent-pm | [] (preenchido, CCB 23/10) |
| plano-producao-agentes | docs/planos/plano-producao-agentes.md | plan | active | 1.1.0 | agent-pm | "AGUARDANDO APROVAÇÃO HUMANA" (corpo declarado) |
| ADR-001 | docs/decisoes/ADR-001-stack.md | doc-decisao | ratified | 1.1.0 | agent-architect | [] (ratificado CCB 23/10) |
| ADR-002 | docs/decisoes/ADR-002-kanban.md | doc-decisao | ratified | 1.1.0 | agent-architect | [] (ratificado CCB 23/10) |
| ADR-003 | docs/decisoes/ADR-003-metricas.md | doc-decisao | ratified | 1.1.0 | agent-architect | "UNKNOWN-GAP: docs/metricas/baseline.md e docs/dependencias/registro.md permanecem 0B; popular no início da codificação" |
| ADR-004 | docs/decisoes/ADR-004-tasklists.md | doc-decisao | ratified | 1.1.0 | agent-architect | [] (ratificado CCB 23/10) |
| ADR-005 | docs/decisoes/ADR-005-freeze.md | doc-decisao | ratified | 1.0.0 | agent-architect | [] |
| TAP-001 | .ai/specs/tap.md | spec | draft | 1.0.0 | agent-sdd-specialist | "UNKNOWN-GAP: docs/tap/TAP.md é stub-ponteiro (CCB F-06 TA-0016); TAP integral vivo reside no plano-integral" |
| EAP-001 | .ai/specs/eap.md | spec | draft | 1.0.0 | agent-sdd-specialist | "UNKNOWN-GAP: SVGs da EAP são placeholders; fonte svg/mermaid exigida pelo DoR da classe diagrama" |
| REQ-SPEC-001 | .ai/specs/requisitos.md | spec | draft | 1.0.0 | agent-sdd-specialist | SSOT RF/RNF declarado; docs/requisitos/requisitos.md é ponteiro |
| requisitos-cogme | docs/requisitos/requisitos.md | requisito | draft | 1.0.0 | agent-po | "ponteiro (CCB F-06 TA-0016): lista canônica RF/RNF reside em .ai/specs/requisitos.md" |
| OKB-001 | docs/conhecimento/OKB.md | okb | ratified | 5.1.0 | agent-architect | ratificado por CCB-003 (GP, 30/10/2026); corpus único; v3.0 arquivado; cobertura metodológica PMBOK/TOGAF/ITIL em §9; achados abertos C-03/C-05/C-06/C-11/C-12/C-15/C-21/C-22/C-24 |
| glossario-cogme | docs/conhecimento/glossario.md | glossario | active | 3.2.0 | agent-sdd-specialist | "grafia sanitizada por CCB C2 23/10/2026"; link termo↔OKB + saneamento Cycle Time/EAP pendente |
| registro-dependencias | docs/dependencias/registro.md | log-baseline | draft | 1.0.0 | agent-pm | "stub 0B, gap declarado (DoR)"; popular no início da codificação |
| baseline-metricas | docs/metricas/baseline.md | log-baseline | draft | 1.0.0 | agent-pm | "stub 0B, gap declarado (DoR)"; correção = nova entrada, nunca reescrita |
| estrutura-de-diretorios | estrutura-de-diretorios.md (raiz) | spec | active | 0.2.1 | agent-sdd-specialist | [] |
| ccb-log | docs/governanca/ccb-log.md | register-decision | active | 0.1.0 | CCB | registro vivo CCB-LOG-NNN (append-only); classe fora do enum KB-TAX-001; cita plano-consolidacao-estrutural.md inexistente (OKB-C-25) |
| KB-INDEX (autorreferencial) | docs/conhecimento/KB-INDEX.md | spec | active | 1.2.0 | agent-docker-specialist | atualizado na promoção do OKB v5.1.0 (CCB-003, 30/10/2026) |
| — | docs/archive/legacy-md-artifact/OKB_COGME_v3.0.md | archived | archived | 3.0.0 | agent-architect | corpus vivo até 30/10/2026; substituído pelo v5.1.0 (CCB-003); movido via git mv + linha de proveniência; imutável |
| — | docs/archive/legacy-md-artifact/OKB_COGME_v3.1-draft-aplicado-em-v4.md | archived | archived | 3.1.0 | agent-docker-specialist | v3.1 draft aplicado pelo OKB v4.0.0; movido via git mv (conteúdo intacto + linha de proveniência); imutável |
| — | docs/archive/legacy-md-artifact/OKB_COGME_v2.1.md | archived | archived | 2.1.0 | agent-docker-specialist | guardrail original; imutável |
| — | docs/archive/legacy-md-artifact/map_report-COBECO-artefato-estranho.md | archived | archived | — | agent-sdd-specialist | registrado como arquivado desde TA-0012 (linha migrada do registro vivo para comprovação); artefato COBECO legacy, stack divergente (TA-0009); imutável |

### Classes sem artefato LIVE completo (honestidade declarada — G3)

| classe | estado atual | gap |
|---|---|---|
| requisito | arquivo único presente como PONTEIRO (`docs/requisitos/requisitos.md` → `.ai/specs/requisitos.md`) | back-link e conversão GWT pendentes (M2) |
| log-baseline | dois stubs 0B (`docs/dependencias/registro.md`, `docs/metricas/baseline.md`) | gap declarado em ambos; popular no início da codificação |
| licoes | 3 arquivos em `docs/conhecimento/licoes-aprendidas/` NÃO frontmatter-classificados | cobertura parcial (ver Seção abaixo) |
| diagrama | 6 áreas com PNG+SVG; figuras EAP do plano-integral são placeholders | fonte svg/mermaid exigida pelo DoR da classe (EAP-001) |

## Cobertura declarada (mapeados pela KB-TAX-001 Seção 3, ainda não frontmatter-classificados)

- `docs/conhecimento/licoes-aprendidas/MF1..MF3-licoes.md` — classe `licoes`; MF2/MF3 são 0B (gap a declarar).
- `docs/diagramas/` (6 áreas, PNG+SVG) — classe `diagrama`; DoR: fonte SVG/Mermaid por área (EAP sem fonte).
- `docs/conhecimento/drafts/` (22 arquivos remanescentes após o dedupe C5) — merge → `okb`/`glossario` execução downstream; `[legacy]/*` → `archived`.
- `docs/archive/` (demais arquivos legados) — classe `archived` terminal; sem ação além de auditoria/sucessão.

## CCB — ledger de decisões (ondas 22–23/10/2026)

| Item CCB | Tema | Status |
|---|---|---|
| C1 | Planos de área riscos/recursos/comunicações preenchidos | ✅ RESOLVIDO (plan → active 1.0.0, ledger TA-0013) |
| C2 | Grafia "Carleto" → "Carleto" (glossário) | ✅ RESOLVIDA (glossário v3.2.0, TA-0017); resíduos capa.svg/PDFs pendentes (caveats acima) |
| C3 | Roster registry ratificado (v1.0) | ✅ RESOLVIDO (ledger TA-0013) |
| C4 | ADR-001..004 preenchidas + ratified 1.1.0 | ✅ RESOLVIDO (ledger TA-0013) |
| C5 | Dedupe OKB: 3 corpora → 1 | ✅ RESOLVIDO (OKB v4.0.0 único, TA-0017; v3.1 draft movido para archive com proveniência) |
| F-06 | requisitos/TAP ponteiros; specs tap/eap/requisitos preenchidas | ✅ RESOLVIDO (TA-0016) |
| C6 | OKB v5.1.0 ratificado como documento de conhecimento canônico (corpus único) | ✅ RESOLVIDO (CCB-003, 30/10/2026; v3.0 arquivado; índice 1.2.0) |

## PENDENTE CCB (decisões humanas; NADA executado nesta onda)

1. **docx Plano-de-Projeto v1.1 canônico vs v1.0; mover docx para archive:** versão mais recente prevalece (KB-TAX-001 §4.6), mas o HUMANO AINDA NÃO DECIDIU a movimentação do docx — manter PENDENTE (não mover nesta onda).
2. **Back-link HF-*:** UNKNOWN-GAP da spec da taxonomia: handoffs desta onda ainda não numerados; back-link pendente pelo primeiro dispatch downstream.
3. **SVG EAP sem fonte:** figuras EAP do plano-integral são placeholders; fonte svg/mermaid exigida (classe diagrama, custódia architect).
4. **Grafia "Carleto" residual:** `docs/slides_apresentacao/capa.svg` (SVG textual, fora da lista autorizada desta onda) e PDFs binários — pendente onda futura/CCB.
5. **Merge remanescente de drafts (22 arquivos):** execução downstream (okb/glossario) — pendente de decisão/dispatch.
6. **Saneamento Glossário:** Cycle Time "To Do → Done", contagem EAP "13/48", "Processo 6.4 Estimar Custos" → 7.2 — canônico já vigente (ADR-003/TAP §4), correção textual pendente.

## Nota de proveniência

Migração executada sob specs `KB-TAX-001 v1.1.0` (parcelas TA-0011 → TA-0012 → TA-0013..TA-0017; HF-0012, HF-0017). Nenhum conteúdo foi removido ou reescrito sem registro — o dedupe OKB (C5) registrou TODOS os conflitos e temas expirados com porquê (OKB v4.0 Seção 10). Ledger: `.ai/agents/ledger.yaml`. Estado verificado em git (cada edição citada; `git status` é a prova da onda).
