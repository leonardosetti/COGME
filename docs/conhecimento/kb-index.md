---
id: KB-INDEX-001
title: KB-INDEX — Índice do SSOT COGME
version: 1.3.0
class: spec
status: active
owner: agent-docker-specialist
derived-from:
- docs/conhecimento/kb-index.md (normalizado em 2026-11-05)
last-revised: '2026-10-31'
lgpd-class: n/a
tags:
- conhecimento
- docs
- normalizado
---

# KB-INDEX — Índice do SSOT COGME

Índice único da base de conhecimento, conforme `KB-TAX-001 v1.1.0` (ratified 23/10/2026). Toda alegação documental consulta este índice antes do corpo; artefato ausente da tabela = fora do canon vivo. Ciclo de vida: draft → active → ratified → archived. Status `draft` com caveat "stub 0B/stub-ponteiro" satisfaz o gate G3 (não-0B ou gap declarado).

## Artefatos classificados (atualização TA-0017 23/10; CCB-003 30/10; CCB-LOG A11 31/10/2026 — v1.3.0)

| id | caminho | classe | status | versão | owner | caveats |
|---|---|---|---|---|---|---|
| tap-cogme | docs/tap/tap.md | plan | draft | 1.0.0 | agent-pm | "stub-ponteiro (não-0B, CCB F-06 TA-0016)"; fonte canônica: plano-integral-tap-1-2-3-4-5.md; canal SDD: .ai/specs/tap.md |
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
| ADR-001 | docs/decisoes/adr-001-stack.md | doc-decisao | finalizado | **1.0.0** (real) | agent-architect | índice acompanhava '1.1.0 ratified' desde 23/10; versão real do arquivo é 1.0.0 (OKB-C-02) — ver caveats |
| ADR-002 | docs/decisoes/adr-002-kanban.md | doc-decisao | finalizado | **1.0.0** (real) | agent-architect | idem OKB-C-02 |
| ADR-003 | docs/decisoes/adr-003-metricas.md | doc-decisao | finalizado | **1.0.0** (real) | agent-architect | idem OKB-C-02; "UNKNOWN-GAP: docs/metricas/baseline.md é seed SIMULADO (A09-A-006) e docs/dependencias/registro.md 0B; medição real em M3" |
| ADR-004 | docs/decisoes/adr-004-tasklists.md | doc-decisao | finalizado | **1.0.0** (real) | agent-architect | idem OKB-C-02 |
| ADR-005 | docs/decisoes/adr-005-freeze.md | doc-decisao | ratified | 1.0.0 | agent-architect | [] |
| ADR-014 | docs/decisoes/adr-014-sddai-promulgacao.md | doc-decisao | ratified | 1.0.1 | NEXUS-PRIME ULTIMATE (L0) | Promulgação dos agentes SDDAI + gaps G-01/G-02/G-03; renumerada de ADR-013-b para ADR-014 (OKB-C-26, RAT-2026-10-31-A12); colisão encerrada; supersedida por ADR-006 v2.1.0 |
| ADR-015 | docs/decisoes/adr-015-emenda-marco-m2.md | doc-decisao | ratified | 1.0.0 | agent-architect | [] |
| TAP-001 | .ai/specs/tap.md | spec | draft | 1.0.0 | agent-sdd-specialist | "UNKNOWN-GAP: docs/tap/tap.md é stub-ponteiro (CCB F-06 TA-0016); TAP integral vivo reside no plano-integral" |
| EAP-001 | .ai/specs/eap.md | spec | draft | 1.0.0 | agent-sdd-specialist | "UNKNOWN-GAP: SVGs da EAP são placeholders; fonte svg/mermaid exigida pelo DoR da classe diagrama" |
| REQ-SPEC-001 | .ai/specs/requisitos.md | spec | draft | 1.0.0 | agent-sdd-specialist | SSOT RF/RNF declarado; docs/requisitos/requisitos.md é ponteiro |
| requisitos-cogme | docs/requisitos/requisitos.md | requisito | draft | 1.0.0 | agent-po | "ponteiro (CCB F-06 TA-0016): lista canônica RF/RNF reside em .ai/specs/requisitos.md" |
| OKB-001 | docs/conhecimento/okb.md | okb | ratified | **5.2.0** | agent-architect | ratificado por CCB-003 (30/10) + normalização RAT-2026-10-31-A11 (31/10): template canônico OKB-TEMPLATE-CANON v1.0; changelog VER-007; v3.0/v5.1.0 precedidos; corpo preservado |
| glossario-cogme | docs/conhecimento/glossario.md | glossario | active | **3.2.0 (real)** | agent-sdd-specialist | **SANITIZADO 31/10 (A11; encerra C-07/C-17)**: hierarquia corrigida, EAP 12/37, PostgreSQL canônico, Qwen3-30B-A3B MoE, refs → OKB v5.2.0; changelog próprio §16 |
| registro-dependencias | docs/dependencias/registro.md | log-baseline | draft | 1.0.0 | agent-pm | "stub 0B, gap declarado (DoR)"; popular no início da codificação |
| baseline-metricas | docs/metricas/baseline.md | log-baseline | active (seed) | 1.0.0 | agent-pm | **seed SIMULADO promulgado em A09-A-006 (31/10, declarado no registro)** — não é evidência de desempenho; medição real em M3 (OKB-C-16) |
| estrutura-de-diretorios | estrutura-de-diretorios.md (raiz) | spec | active | 0.2.1 | agent-sdd-specialist | [] |
| ccb-log | docs/governanca/ccb-log.md | register-decision | active | 0.1.0 | CCB | registro vivo CCB-LOG-NNN (append-only); classe fora do enum KB-TAX-001; cita plano-consolidacao-estrutural.md inexistente (OKB-C-25) |
| KB-INDEX (autorreferencial) | docs/conhecimento/kb-index.md | spec | active | 1.3.0 | agent-docker-specialist | atualizado na normalização do OKB v5.2.0 (CCB-LOG A11, 31/10/2026) |
| ADR-013-a ⚠️ | docs/decisoes/adr-013-regime-emenda-tap.md | doc-decisao | ratified | 1.0.0 | — (não declarada) | Regime de Emenda Controlada do TAP (baseline viva); supersedes ADR-005 parcialmente; frontmatter date 2026-11-01 vs instrumento 31/10 (OKB-C-28) |
| ADR-007..012 | docs/decisoes/ADR-00{7..12}*.md | doc-decisao | ratified | 1.1.0/1.0.0/1.1.0/1.0.0/1.0.0/1.0.1 | vários (OKB v5.2.0 §2.1) | registrados no índice nesta rodada (eram ausentes desde CCB-001/002) |
| ADR-016 | docs/decisoes/adr-016-backend-mvp.md | doc-decisao | proposta | 1.0.0 | agent-architect | NÃO ratificada: aprovação humana do CCB (Art. 5). O status `proposta` não consta do ciclo de vida de KB-TAX-001 (draft → active → ratified → archived). |
| CI-CD-GOV-001 | docs/governanca/ci-cd-governance.md | doc-norma | ratified | 1.0.0 | agent-devops | promulgado RAT-2026-10-31-A10 |
| DEVSECOPS-001 | docs/governanca/devsecops-policy.md | doc-norma | ratified | 1.0.0 | agent-devops | promulgado RAT-2026-10-31-A10 |
| Canon SDD | docs/conhecimento/canon-stack-sdd.md | okb-adjacente | promulgado | 2.0.0 | agent-sdd-specialist | promulgado A09-A-007 |
| Registro de ratificação | docs/governanca/ratificacao-promulgacao.md | register-decision | promulgado | 1.0.0 | agent-architect | promulgado A09-A-005; classe fora do enum KB-TAX (C-13) |
| AUD-2610-09 | docs/auditorias/aud-2610-09-okb-normalizacao.md | relatorio-auditoria | active | 1.0.0 | project-auditor | auditoria extraordinária dedicada ao OKB (A11); classe fora do enum (C-13) |
| — | docs/archive/legacy-md-artifact/okb-cogme-v3-0.md | archived | archived | 3.0.0 | agent-architect | corpus vivo até 30/10/2026; substituído pelo v5.1.0 (CCB-003); movido via git mv + linha de proveniência; imutável |
| — | docs/archive/legacy-md-artifact/okb-cogme-v3-1-draft-aplicado-em-v4.md | archived | archived | 3.1.0 | agent-docker-specialist | v3.1 draft aplicado pelo OKB v4.0.0; movido via git mv (conteúdo intacto + linha de proveniência); imutável |
| — | docs/archive/legacy-md-artifact/okb-cogme-v2-1.md | archived | archived | 2.1.0 | agent-docker-specialist | guardrail original; imutável |
| — | docs/archive/legacy-md-artifact/map-report-cobeco-artefato-estranho.md | archived | archived | — | agent-sdd-specialist | registrado como arquivado desde TA-0012 (linha migrada do registro vivo para comprovação); artefato COBECO legacy, stack divergente (TA-0009); imutável |

### Classes sem artefato LIVE completo (honestidade declarada — G3)

| classe | estado atual | gap |
|---|---|---|
| requisito | arquivo único presente como PONTEIRO (`docs/requisitos/requisitos.md` → `.ai/specs/requisitos.md`) | back-link e conversão GWT pendentes (M2) |
| log-baseline | `docs/dependencias/registro.md` 0B; `docs/metricas/baseline.md` seed SIMULADO (A09-A-006, 1.04 KB) | registro de dependências a popular; baseline real em M3 (OKB-C-16) |
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
| C7 | **OKB v5.2.0** normalizado (template OKB-TEMPLATE-CANON v1.0) + glossário sanitizado v3.2.0 + patch list §8.4 + AUD-2610-09 | ✅ RESOLVIDO (CCB-LOG RAT-2026-10-31-A11, 31/10/2026; aprovação indireta via agente, gatilho de permissão prévia deliberativo do GP) |

## PENDENTE CCB (decisões humanas; NADA executado nesta onda)

1. **docx Plano-de-Projeto v1.1 canônico vs v1.0; mover docx para archive:** versão mais recente prevalece (KB-TAX-001 §4.6), mas o HUMANO AINDA NÃO DECIDIU a movimentação do docx — manter PENDENTE (não mover nesta onda).
2. **Back-link HF-*:** UNKNOWN-GAP da spec da taxonomia: handoffs desta onda ainda não numerados; back-link pendente pelo primeiro dispatch downstream.
3. **SVG EAP sem fonte:** figuras EAP do plano-integral são placeholders; fonte svg/mermaid exigida (classe diagrama, custódia architect).
4. **Grafia "Carleto" residual:** `docs/slides_apresentacao/capa.svg` (SVG textual, fora da lista autorizada desta onda) e PDFs binários — pendente onda futura/CCB.
5. **Merge remanescente de drafts (22 arquivos):** execução downstream (okb/glossario) — pendente de decisão/dispatch.
6. ~~**Saneamento Glossário:**~~ ✅ **RESOLVIDO 31/10/2026 (v3.2.0 sanitizado — CCB-LOG A11; encerra OKB-C-07/C-17).** Resíduo textual residual: "Processo 6.4/7.2" e Cycle Time a re-verificar na próxima auditoria.

## Nota de proveniência

Migração executada sob specs `KB-TAX-001 v1.1.0` (parcelas TA-0011 → TA-0012 → TA-0013..TA-0017; HF-0012, HF-0017). Nenhum conteúdo foi removido ou reescrito sem registro — o dedupe OKB (C5) registrou TODOS os conflitos e temas expirados com porquê (OKB v4.0 Seção 10). Ledger: `.ai/agents/ledger.yaml`. Estado verificado em git (cada edição citada; `git status` é a prova da onda).
