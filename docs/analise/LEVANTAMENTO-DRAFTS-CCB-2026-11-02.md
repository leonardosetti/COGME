---
id: LEVANTAMENTO-DRAFTS-CCB-2026-11-02
title: Levantamento exaustivo de artefatos com status draft/pending para submissão à CCB (TA-0033)
version: 1.0.0
class: relatorio-levantamento
status: active
owner: agent-project-analyst
derived-from:
  - .ai/handoffs/HF-0033-levantamento-drafts-ccb.md (payload de TA-0033)
  - .ai/specs/, .ai/handoffs/, .ai/agents/, docs/decisoes/, docs/planos/, .ai/workflows/, PLANEJAMENTO.md, task-*.json
  - docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md, docs/analise/REV-PLANO-GERENCIAMENTO-COGME-v2.1.0-rodada2.md
last-revised: 2026-11-02
lgpd-class: n/a (sem PII)
task: TA-0033 | handoff: HF-0033 | sender: agent-nexus-prime-ultimate
kill_switch: inherited
caveats:
  - "Somente leitura: nenhum arquivo fora deste relatório foi alterado; imutáveis (constitution.md, registry, .opencode/agents/*, handoffs, ledger, ADRs, specs) intactos."
  - "Toda 'ação CCB recomendada' é RECOMENDAÇÃO (Art. 5.1 — a decisão é do Humano); nenhuma classificação aqui é veredicto."
  - "Classificação sem evidência suficiente é marcada `UNKNOWN - verify`; nada foi inventado de status, data ou origem."
  - "Árvore com realocação humana não-commitada em docs/planos/ (legacy/ + plano-granular/): caminhos VIVOS verificados por ls/git status."
---

# Levantamento de artefatos draft/pending para aprovação CCB — 2026-11-02

**Mandato:** TA-0033 / HF-0033 — rodada garantidora GP/Humano 2026-11-02 (Art. 5.1).
**Princípio reitor:** o agente recomenda; o Humano (CCB) decide. Nenhum item abaixo está
aprovado, rejeitado ou ratificado por este relatório.

---

## 1. Método (varredura declarada)

Comandos executados em `/` (árvore viva), somente leitura:

| # | Comando | Alvo |
|---|---|---|
| M1 | `grep -rn -i -E "status: *(draft\|pending\|proposta\|emenda)\|^Status: *(PENDENTE\|DRAFT\|ONGOING\|REVIS)" .ai/specs .ai/handoffs .ai/agents docs/decisoes docs/planos .ai/workflows PLANEJAMENTO.md` | status literais em frontmatter/linha `Status:` |
| M2 | `grep -rn -i -E "^status:\|^ *status:" .ai/handoffs/*.md .ai/agents/*.yaml .ai/agents/*.yml` | enum de handoffs (draft\|ready\|dispatched\|in_progress\|done\|blocked) + estados de agentes |
| M3 | `grep -rn -E "^\|? *Status" docs/decisoes/*.md` | campo Status das ADRs |
| M4 | `for f in <arquivo>; do sed -n 1,20p "$f"; done` | frontmatter completo (origem task/handoff) |
| M5 | `ls -R .ai/specs .ai/handoffs .ai/agents docs/decisoes docs/planos .ai/workflows` + `git status --short` | árvore viva + realocação não-commitada |
| M6 | `wc -c .ai/specs/*.md` | placeholders 0 B |
| M7 | `grep -c "^- \[ \]" .ai/handoffs/HF-*.md` | AC não marcados por handoff |
| M8 | `grep -rn -i -E "pendente\|draft\|proposta\|aguarda" docs/planos/ PLANEJAMENTO.md` | planos/rascunhos |
| M9 | `grep -rln "Status: DRAFT" .opencode/agents/*.md` + `grep -rn "status: draft" docs/auditorias docs/conhecimento/drafts` | varredura de apoio FORA do escopo declarado (sinalização, sem inventário) |
| M10 | `grep -n -i -E "pendente\|draft\|todo\|PENDING" .ai/workflows/sdd-cycle.sh` | workflows (0 ocorrências → limpo) |

**Escopo coberto (AC 2):** `.ai/specs` (12 arquivos), `.ai/handoffs` (12 HF + 37 envelopes
`task-*.json`), `.ai/agents` (5 arquivos), `docs/decisoes` (19 ADRs + LOG + tmp),
`docs/planos` (1 vivo + `legacy/` 6 + `plano-granular/` 15), `.ai/workflows` (1),
raiz (`PLANEJAMENTO.md`, `task-auditor-scheduler.json`, `task-retry-0100.json`).

**Cobertura por varredura:** 49 itens (65 artefatos/entradas + 1 evento de realocação)
com status draft/pending ou equivalente; 22 artefatos com `status: draft` fora do escopo
declarado (§6) são sinalizados, não inventariados.

---

## 2. TOP-3 MAIS BLOQUEANTES

1. **ADR-016 em `status: proposta` — trava toda a cadeia do backend.**
   Evidência: `docs/decisoes/ADR-016-backend-mvp.md:5` (`status: proposta`), `:14`
   ("não está ratificada"), `:123`; bloqueio explícito em
   `.ai/handoffs/HF-0500-backend-mvp.md:14` ("o único critério em aberto é a ratificação
   da ADR-016") e `:58` (AC "Ratificação da ADR-016 pelo CCB: pendente").
   Impacto: mantém `HF-0500` em `blocked` (`HF-0500:4`), `spec-004` em `in_progress`
   com push/merge pendentes (`.ai/specs/spec-004-backend-mvp-v1.spec.md:16`) e 5 REQs
   "Implementado em branch, pendente de merge"
   (`docs/planos/plano-granular/desenvolvimento.md:190-193,196`).
   **Ação recomendada: `ratificar` (ou `rejeitar` com motivo) — decisão humana.**

2. **Emendas constitucionais E-01..E-08 pendentes de ratificação — a Constituição
   proposta não é lei.**
   Evidência: `.ai/specs/spec-001-constitution-round-1-proposta.spec.md:193,209,228,253,270,291,307,326`
   (cada emenda marcada `[REQUER RATIFICAÇÃO CCB]`), `:190` ("TODAS as emendas abaixo…");
   cobrança em `.ai/specs/spec-002-requisitos-review-round-1.spec.md:217` e declaração
   "PENDENTES de CCB, nao sao lei" em `spec-002:17`.
   Impacto: é o **gate E** que bloqueia o repovoamento de `requisitos.md` e a emissão das
   specs de domínio B.1..B.10 (`docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:66`
   e `:24-41`).
   **Ação recomendada: `ratificar` emendas individualmente (Art. 5.2) — decisão humana.**

3. **Plano de Gerenciamento v2.1.0 em `Draft` com 64 achados e 7 gates abertos.**
   Evidência: `docs/planos/Plano-de-Gerenciamento-COGME_v2.1.0.md:6`
   ("**Status:** Draft — Consolidado para Pós-Produção"); achados em
   `docs/analise/REV-PLANO-GERENCIAMENTO-COGME-v2.1.0-rodada2.md:26`
   (64 achados — 18 ALTA / 33 MÉDIA / 13 BAIXA) e gates **G-1..G-7** em
   `REV-...-rodada2.md:151-157`, com "nenhum ajuste será aplicado sem ratificação"
   (`REV-...-rodada2.md:18`).
   Impacto: G-3 declara o registro como pré-condição de publicação (`REV-...-rodada2.md:153`);
   o plano é a fonte do CR-001 em aberto (`Plano-de-Gerenciamento...:2315`).
   **Ação recomendada: `remendar` após decisão do escopo em G-7 — decisão humana.**

> **Risco crítico adicional (fora do top-3 por não travar fila de trabalho):** realocação
> humana **não-commitada** em `docs/planos/` — 21 paths marcados `D` (ex. `docs/planos/plano-escopo.md`)
> e `docs/planos/legacy/` + `docs/planos/plano-granular/` ainda untracked (`git status --short`,
> 2026-11-02). Precedente de perda: LA-001 (`docs/planos/plano-granular/plano-integral-tap-1-2-3-4-5.md`
> / OKB §1.4). **Ação recomendada: `ratificar` a homologação e commitar.**

---

## 3. INVENTÁRIO — por domínio

Colunas: **Caminho:linha** (evidência do status) · **Status exato** · **Origem**
(task/HF/ADR que o gerou) · **Pendência** · **Ação CCB recomendada** (recomendação, não veredicto).

### 3.1 `.ai/specs` (11 itens)

| # | Caminho:linha | Status exato | Origem | Pendência | Ação CCB recomendada (justificativa) |
|---|---|---|---|---|---|
| S-01 | `.ai/specs/spec-001-constitution-round-1-proposta.spec.md:4` | `status: draft` | TA-0002 \| HF-0001 (`:9`) | Ratificação das emendas E-01..E-08 (§2) | `ratificar` — é proposta de emenda (Art. 5.2); sem ratificação não é lei (`spec-002:17`) |
| S-02 | `.ai/specs/spec-002-requisitos-review-round-1.spec.md:4` | `status: draft` | TA-0004 (`:9`, sem HF) | Revisão/CCB; depende do gate E (`:17`, `:217`) | `ratificar` — rodada de revisão válida, bloqueada por E-01..E-08 |
| S-03 | `.ai/specs/spec-003-sdd-conf-memory.spec.md:5` | `status: draft` | run CANON-20261029-01 + commit 149067f; `creation_handoff: UNKNOWN - verify` (`:10`) | Aprovação + origem do handoff de criação desconhecida | `ratificar` + verificar origem (`UNKNOWN - verify`) |
| S-04 | `.ai/specs/spec-004-backend-mvp-v1.spec.md:5` (e `:16`) | `status: in_progress`; linha `Status: … PENDENTE DE PUSH E MERGE` | commit f6e0455 + record HF-0500; `task: UNKNOWN - verify` (`:11`) | Push/merge da branch `feat/backend-mvp`; condicionada à ADR-016 | `aprovar` — autorizar push/merge após ratificação da ADR-016 (HF-0500:14) |
| S-05 | `.ai/specs/spec-005-container-layers-v1.spec.md:5` (e `:15`) | `status: draft`; `Status: … PENDENTE DE REVISÃO E DE IMPLEMENTAÇÃO` | HF-0029 (TA-0029) + amenda HF-0030 (TA-0030) (`:9`) | Revisão da amenda + implementação (onda seguinte, Art. 6.1) | `ratificar` — amenda do proxy já ratificada GP/Humano 2026-11-02 (`:15`); falta revisão/impl. |
| S-06 | `.ai/specs/requisitos.md` (0 B) | sem linha de status (`UNKNOWN - verify`) | placeholder camada 5 (custódia BA/design) | Conteúdo vazio; repovoamento bloqueado pelo gate E | `remendar` — repovoar pós-E-01..E-08 (`LISTA-SPECS-PENDENTES:24`) |
| S-07 | `.ai/specs/tap.md` (0 B) | sem linha de status (`UNKNOWN - verify`) | placeholder TAP | Baseline de escopo sem conteúdo | `remendar` — repovoar/reapontar para `plano-integral` (`LISTA:25`) |
| S-08 | `.ai/specs/eap.md` (0 B) | sem linha de status (`UNKNOWN - verify`) | placeholder EAP | Fases N1..N11 sem artefato | `remendar` — repovoar pós-gate (`LISTA:26`) |
| S-09 | `.ai/specs/kb-taxonomy.md:17` (e `:18`, `:19`) | `status: ratified` (`:6`) + caveats pendentes | KB-TAX-001 / TA-0013/0017 | Mescla docx v1.0/v1.1 do Plano-de-Projeto **PENDENTE de decisão humana**; 2 `UNKNOWN-GAP` (numeración HF, merge de 22 drafts) | `ratificar` — decidir R-03 (mescla docx) e ordenar merge downstream |
| S-10 | `.ai/specs/afa-changelog.md:7` | sem campo status; "SIR log (vazio — populado por workflows futuras)" (`UNKNOWN - verify`) | AFA-ULTIMATE (custódia Art. 15.4) | Log de melhoria vazio, sem estado declarado | `remendar` — declarar custódia/estado (não há matéria de aprovação) |
| S-11 | `.ai/specs/input-canonico-v4.1.1.md:4` | sem campo status; hierarquia aponta `constitution.md v1.2.0` (vigente v1.2.1) (`UNKNOWN - verify`) | input canônico derivativo | Drift de referência constitucional | `remendar` — atualizar referência para v1.2.1 |

### 3.2 `.ai/handoffs` (14 itens)

| # | Caminho:linha | Status exato | Origem | Pendência | Ação CCB recomendada (justificativa) |
|---|---|---|---|---|---|
| H-01 | `.ai/handoffs/HF-0030-nginx-aceito-demo.md:4` | `status: ready` | TA-0030 (aceita no ledger `.ai/agents/ledger.yaml:29`) | Drift: 8 AC desmarcados (`:46-53`) apesar de `accepted`; `:50` deixa ADR-010 como follow-up | `remendar` — sincronizar status/AC com o ledger (ou reabrir se AC real pendente, `UNKNOWN - verify`) |
| H-02 | `.ai/handoffs/HF-0031-specs-normalizacao.md:4` | `status: ready` | TA-0031 (aceita no ledger `.ai/agents/ledger.yaml:37`) | Drift: 10 AC desmarcados; `MANIFEST.md:204-209` mostra AC 4/6/8 já validados | `remendar` — atualizar checklist/estado |
| H-03 | `.ai/handoffs/HF-0033-levantamento-drafts-ccb.md:4` | `status: ready` (TA-0033 `dispatched`, `ledger.yaml:53`) | TA-0033 / despacho desta rodada | Estado do HF não reflete execução em curso; 7 AC (`:36-42`) ainda não marcados | `remendar` — atualizar após entrega da parcela |
| H-04 | `.ai/handoffs/HF-0400-sddai-loader.md:4` | `status: ready` | HF-0400 (ondata SDDAI, 2026-10-31) | Aguarda dispatch/execução; sem envelope `task-ta-04xx` correspondente (`UNKNOWN - verify`) | `aprovar` — autorizar dispatch da onda SDDAI |
| H-05 | `.ai/handoffs/HF-0401-sddai-memory.md:4` | `status: ready` | HF-0401 | Idem | `aprovar` — idem |
| H-06 | `.ai/handoffs/HF-0402-sddai-engineer.md:4` | `status: ready` | HF-0402 | Idem | `aprovar` — idem |
| H-07 | `.ai/handoffs/HF-0403-sddai-trainer.md:4` | `status: ready` | HF-0403 | Idem | `aprovar` — idem |
| H-08 | `.ai/handoffs/HF-0404-sddai-cli.md:4` | `status: ready` | HF-0404 | Idem | `aprovar` — idem |
| H-09 | `.ai/handoffs/HF-0500-backend-mvp.md:4` | `status: blocked` (`updated: 2026-11-01`) | TA-0100/HF-0500; registro T1–T14 (REQ-13) | Bloqueio único = ratificação da ADR-016 (`:14`); `:12` aponta caminho pré-normalização `.ai/specs/backend-mvp-v1.spec.md` (hoje `spec-004`) | `remendar` — atualizar caminho e desbloquear após decisão sobre a ADR-016 |
| H-10 | `.ai/handoffs/HF-RELATORIO-ANALISE-CONSTITUICAO.md:1` | sem frontmatter nem linha `status:` (`UNKNOWN - verify`) | UNKNOWN - verify (rodada de análise da Constituição) | Estado de execução/conclusão não declarado | `remendar` — declarar status no frontmatter |
| H-11 | `.ai/handoffs/INDEX.md:1-10` | catálogo desatualizado (só HF-001..007 + HF-0500) | catálogo manual v1.0 | Omite HF-0029, HF-0030, HF-0031, HF-0032, HF-0033 e HF-0400..0404 (10 HF vivos) | `remendar` — regerar índice (REQ-13 de rastreabilidade) |
| H-12 | `.ai/handoffs/task-ta-deleg-001.json:1` | envelope sem campo `status` (`UNKNOWN - verify`) | TA-DELEG-001 → agent-architect | Estado de execução não registrado | `remendar` — registrar estado no envelope/ledger |
| H-13 | `.ai/handoffs/task-ta-deleg-002.json:1` | envelope sem campo `status` (`UNKNOWN - verify`) | TA-DELEG-002 → agent-architect | Idem (produção das 5 ADRs + ADR-006) | `remendar` — idem |
| H-14 | `.ai/handoffs/task-ta-deleg-003.json:1` | envelope sem campo `status` (`UNKNOWN - verify`) | TA-DELEG-003 → agent-project-auditor | Idem (auditoria das correções) | `remendar` — idem |

*HF-0029 (`HF-0029:4` = `done`) e os envelopes `task-ta-0029..0033.json` não são
inventariados como pending (TA correspondente já `accepted`/`dispatched` no ledger).*

### 3.3 `.ai/agents` (7 itens)

| # | Caminho:linha | Status exato | Origem | Pendência | Ação CCB recomendada (justificativa) |
|---|---|---|---|---|---|
| A-01 | `.ai/agents/universal-adjustment-session.yaml:2` | `status: in_progress` (bloco `P6`) | sessão de ajuste universal (bloco P6) | Conclusão do bloco P6 (`next_block: P6`) | `aprovar` — acompanhar; não há matéria de decisão |
| A-02 | `.ai/agents/audit_trail.yml:3` | `status: "audit_maintenance_started"` | manutenção de auditoria (last_executed 2026-10-24, `:7`) | Validação semanal em aberto (`next_steps: maintain_lgpd_audits`, `:4`) | `aprovar` — acompanhar cadência; sem decisão pendente |
| A-03 | `.ai/agents/ledger.yaml:5` | `status: escalated` (TA-0027, `exit_status: 0`) | TA-0027 → agent-project-auditor (fix-table) | Entrada escalada sem fechamento explícito (notes citam formalização CCB §0.2) | `ratificar` — formalizar encerramento no ledger (append-only) |
| A-04 | `.ai/agents/ledger.yaml:45` | `status: dispatched` (TA-0032) | TA-0032 → agent-project-auditor (auditoria registry+ledger) | Aguarda parcel do auditor | `aprovar` — aguardar retorno (half-duplex) |
| A-05 | `.ai/agents/ledger.yaml:53` | `status: dispatched` (TA-0033) | TA-0033 → agent-project-analyst (esta tarefa) | Aguarda esta parcela | `aprovar` — em execução nesta rodada |
| A-06 | `.ai/agents/registry.yaml:294` e `:303` | `status: legacy-forge` | herança FORGE-LEGACY (agent-factory-architect*) | Revisão de legado: drift registry↔DAG registrado como F-08/F-09 (`docs/auditorias/AUD-2611-01-AUDITORIA-REGISTRY-LEDGER.md:150-156`) | `remendar` — regularizar topo/legado após auditoria TA-0032 |

### 3.4 `docs/decisoes` (6 itens)

| # | Caminho:linha | Status exato | Origem | Pendência | Ação CCB recomendada (justificativa) |
|---|---|---|---|---|---|
| D-01 | `docs/decisoes/ADR-005-freeze.md:6` | `Regularização Tardia — ratificação CCB pendente da verificação da data 25/09` | TA-DELEG-002 (envelope `.ai/handoffs/task-ta-deleg-002.json:1`) | Ratificação condicionada à verificação de data informada na memória do GP | `ratificar` — confirmar data 25/09 e encerrar a regularização tardia |
| D-02 | `docs/decisoes/ADR-016-backend-mvp.md:5` | `status: proposta` (`:14`, `:123` reforçam) | redação T10/T14 (`HF-0500:33,37`) | Ratificação humana (Art. 5) — ver Top-3 #1 | `ratificar` (ou `rejeitar` com motivo) — decisão humana que desbloqueia backend |
| D-03 | alvo `docs/decisoes/ADR-010-Stack-Infraestrutura.md` (emenda não aplicada) | emenda `follow-up pendente (arquiteto → CCB)` | `.ai/specs/spec-005-container-layers-v1.spec.md:349` (§13) e `HF-0030:50` | ADR-010 ainda descreve "Nginx latente"; proxy foi aceito/ratificado 2026-11-02 | `remendar` — emendar ADR-010 após ratificação (cadeia de supersede) |
| D-04 | `docs/decisoes/ADR-013-regime-emenda-tap.md:11` vs `docs/decisoes/ADR-005-regime-tap.md:6` | `status: superseded by ADR-005 v1.1.0` × `\| Status \| Ratificado \|` | IDs duplicados ADR-005 (freeze vs regime-tap) | Contradição de estado entre ADRs homônimas; ADR-005-freeze segue "ratificação pendente" (`ADR-005-freeze.md:6`) | `remendar` — reconciliar status/IDs (gate G-4, `REV-...-rodada2.md:154`) |
| D-05 | `docs/decisoes/ADR-006-ecossistema-sddai.md:6` × `docs/decisoes/ADR-006-inteligencia-sdd.md:6` | `Ratificado` × `Finalizado (ratificado pelo CCB-001 em 29/10/2026)` | duas ADRs com ID ADR-006 (títulos distintos) | Ambiguidade de ID canônico (G-4); ADR-014 aponta ADR-006 v2.1.0 como vigente (`ADR-014:1-3`) | `remendar` — definir ID/versão canônica de referência |
| D-06 | `docs/decisoes/_consolidado-adrs.tmp.md:1-7` | artefato temporário, "não canônico", mantido a pedido do GP | reconstrução pós-remoção acidental (CCB-LOG A01/A02) | Status de permanência/arquivamento indefinido; duplica conteúdo de 12 ADRs | `remendar` — decidir arquivamento ou rótulo permanente (1 fato = 1 local) |

### 3.5 `docs/planos` (10 itens — caminhos VIVOS pós-realocação)

| # | Caminho:linha | Status exato | Origem | Pendência | Ação CCB recomendada (justificativa) |
|---|---|---|---|---|---|
| P-01 | `docs/planos/Plano-de-Gerenciamento-COGME_v2.1.0.md:6` | `**Status:** Draft — Consolidado para Pós-Produção` | v2.1.0 (data-base 31/10/2026) + revisão rodada 2 | 64 achados e gates G-1..G-7 (`REV-...-rodada2.md:26,151-157`) — ver Top-3 #3 | `remendar` — aplicar ajustes conforme escopo decidido em G-7 |
| P-02 | `docs/planos/Plano-de-Gerenciamento-COGME_v2.1.0.md:2315` e `:2349` | CR-001 `Pendente` (linha de controle e "FORA desta rodada") | change-request CR-001 (OKB-C-06) | Decisão M2×M3, emissão de ADR de marco, atualização do cronograma | `ratificar` — decidir fusão/separação dos marcos e formalizar CR-001 |
| P-03 | `docs/planos/plano-granular/plano-consolidacao-estrutural.md:7` (e `:36`) | `ratification: PENDENTE CCB (Agenda A-03)`; `## 3. Ações PENDENTES de ratificação CCB` | agent-nexus-prime-ultimate (custódia), v0.1.0 (`:4`) | Desbloat/consolidação estrutural não autorizado | `ratificar` — agenda A-03 do CCB (remoção de lixo/bloat) |
| P-04 | `docs/planos/plano-granular/plano-producao-agentes.md:4` | `Status: AGUARDANDO APROVAÇÃO HUMANA` | AFA-ULTIMATE v1.3.0-FINAL, 2026-10-22 | Ondas A.1..A.22 de produção de agentes | `ratificar` — aprovar plano de ondas (ou remendar escopo por first-principles) |
| P-05 | `docs/planos/plano-granular/consideracoes-finais.md:15-19` | 5 linhas `Pendente` (Produtos/Qualidade/Inovação/Cronograma/Documentação) | consolidação pós-normalização | Evidências só pós-M3 (15/11) e M4 (15/12) | `aprovar` — manter como provisório até M4 (rótulo já explícito em `:3`) |
| P-06 | `docs/planos/plano-granular/desenvolvimento.md:190-193,196` (e `:124`, `:245`) | `Implementado em branch, pendente de merge` (REQ-01..04, REQ-07) | ADR-010/ADR-016 + branch `feat/backend-mvp` | Merge pendente; figuras N5.1/N5.2 pendentes; "revisão humana pendente" (`:245`) | `aprovar` — autorizar merge após ratificação da ADR-016 (Top-3 #1) |
| P-07 | `docs/planos/Plano-de-Projeto-COGME_v2.1-ONGOING.docx` + `docs/planos/legacy/Plano-de-Projeto-COGME_v2.0-ONGOING.docx` + `legacy/…v2.0.1-ONGOING.docx` | sufixo `ONGOING` no nome (sem campo status) | exports concorrentes | Decisão R-03 (mescla/concorrência sem `.md` canônico): `docs/conhecimento/OKB.md:391,429`; caveat `kb-taxonomy.md:17` | `ratificar` — decidir R-03 (manter um export canônico + `.md`) |
| P-08 | `docs/planos/.~ano-de-Projeto-COGME_v2.1-ONGOING.docx` (162 B) | lock temporário de editor (sem status) | editor aberto em 2026-11-02 19:19 | Lock órfão suja o diretório (padrão em `OKB.md:428`) | `remendar` — remover lock após confirmar editor fechado |
| P-09 | `docs/planos/legacy/` (6 arquivos) + `docs/planos/plano-granular/` (15 arquivos) vs 21 paths `D` em `docs/planos/` | realocação **não-commitada** (`git status --short`, 2026-11-02) | realocação humana manual | Árvore de trabalho diverge do HEAD; risco de perda (LA-001) | `ratificar` — homologar a realocação e commitar (ou reverter com evidência) |
| P-10 | `docs/planos/plano-granular/*.md` — 13 arquivos sem campo `Status:`/frontmatter (ex. `plano-cronograma.md:5`, `plano-escopo.md:6`, `plano-custos.md:6`) | sem declarar status (`UNKNOWN - verify`) | extração dos planos 1–8 | Estado (rascunho/vigente) não declarado por arquivo | `remendar` — adicionar frontmatter de status canônico (KB-TAX-001) |

### 3.6 `.ai/workflows` (0 itens)

`.ai/workflows/sdd-cycle.sh` — `grep -i -E "pendente|draft|todo|PENDING"` = **0 ocorrências**
(comando M10). Nenhum marcador de pendência; nenhum item a submeter.

### 3.7 Raiz (2 itens)

| # | Caminho:linha | Status exato | Origem | Pendência | Ação CCB recomendada (justificativa) |
|---|---|---|---|---|---|
| R-01 | `PLANEJAMENTO.md:3` (e `:42`) | "arquivos gerados anteriormente são **rascunhos preliminares**"; 31 temas com caixas desmarcadas | plano de monografia (tasklists ADR-004) | Incrementos pendentes em todos os temas; nenhuma caixa marcada | `aprovar` — manter como rascunho de trabalho, sem efeito de conclusão (formulação já é explícita) |
| R-02 | `task-auditor-scheduler.json:7` + `task-retry-0100.json:7` | envelope sem campo `status`; payload "Aguardando parcel com dod:true" | TA-0100 → agent-devops (scheduler 90 min) | Despacho/parcel não concluídos; `handoff: HF-0500` declarado no envelope, mas HF-0500 é registro do backend MVP (`HF-0500:8`) — possível mismatch (`UNKNOWN - verify`) | `aprovar` — retomar TA-0100 e esclarecer o handoff correto |

---

## 4. Pendências CCB já conhecidas (cross-referência — sem duplicar inventário)

| Conhecida | Evidência | Relação com o inventário |
|---|---|---|
| **Emendas E-01..E-08** (ratificação constitucional) | `.ai/specs/spec-001-constitution-round-1-proposta.spec.md:193` (E-01), `:209` (E-02), `:228` (E-03), `:253` (E-04), `:270` (E-05), `:291` (E-06), `:307` (E-07), `:326` (E-08); matriz `:349` | = Top-3 #2; itens **S-01**, **S-02** |
| **Proposta ADR-016** (`status: proposta`) | `docs/decisoes/ADR-016-backend-mvp.md:5` (e `:14`, `:123`); bloqueio `HF-0500:14`, AC `HF-0500:58` | = Top-3 #1; itens **D-02**, **H-09**, **S-04**, **P-06** |
| **Emenda da ADR-010** ("Nginx latente" → proxy aceito) | `.ai/specs/spec-005-container-layers-v1.spec.md:349`; `HF-0030:50` | item **D-03** (também `LISTA-SPECS-PENDENTES:68`) |
| **Gates humanos G-1..G-7** (rodada 2 do plano) | `docs/analise/REV-PLANO-GERENCIAMENTO-COGME-v2.1.0-rodada2.md:151` (G-1), `:152` (G-2), `:153` (G-3), `:154` (G-4), `:155` (G-5), `:156` (G-6), `:157` (G-7); 64 achados em `:26` | = Top-3 #3; itens **P-01**, **D-04**, **D-05** (G-4), **P-02** (G-2) |
| **LISTA-SPECS-PENDENTES** (specs de domínio + gaps) | `docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:24-26` (A.1–A.3 = `requisitos/tap/eap`), `:32-41` (B.1–B.10), `:47-51` (C.1–C.5), `:57-60` (D.1–D.4), `:66-71` (E.1–E.6) | itens **S-06**, **S-07**, **S-08**; condicionantes E.1–E.3 = itens acima; E.4–E.6 sem item novo |
| **Decisão R-03** (docx ONGOING concorrentes) | `docs/conhecimento/OKB.md:391`, `:429`; caveat `.ai/specs/kb-taxonomy.md:17` | itens **P-07**, **S-09** |
| **CR-001** (colisão M2×M3) | `docs/planos/Plano-de-Gerenciamento-COGME_v2.1.0.md:2315`, `:2349`; OKB-C-06 | item **P-02** |
| **Drafts de auditoria e de conhecimento** (fora do escopo declarado) | `docs/auditorias/AUD-2610-03.md:28` (6 emendas ADR `status: draft — aguardando ratificação Humana CCB`) com linhas `:91,122,145,166,184,210`; `docs/conhecimento/drafts/` (27 arquivos, 3 com `status: draft`) e merge pendente `kb-taxonomy.md:19` | §6 — sinalização, não inventariado |

---

## 5. Tabela consolidada (ordenada por ação CCB recomendada) + contagens

**49 itens — 65 artefatos/entradas + 1 evento.** Ação = recomendação (Art. 5.1); decisão é do Humano.

| Ação | Qtd. itens | IDs |
|---|---|---|
| `ratificar` | 13 | S-01, S-02, S-03, S-05, S-09, D-01, D-02, A-03, P-02, P-03, P-04, P-07, P-09 |
| `aprovar` | 14 | S-04, H-04, H-05, H-06, H-07, H-08, A-01, A-02, A-04, A-05, P-05, P-06, R-01, R-02 |
| `remendar` | 22 | H-01, H-02, H-03, H-09, H-10, H-11, H-12, H-13, H-14, D-03, D-04, D-05, D-06, P-01, P-08, P-10, A-06, S-06, S-07, S-08, S-10, S-11 |
| `rejeitar` | 0 | nenhum item com evidência suficiente para rejeição nesta rodada |
| **Total** | **49** | |

### Contagens por status exato (artefatos/entradas)

| Status exato (evidência) | Qtd. |
|---|---|
| `draft` (frontmatter `.ai/specs`: spec-001/002/003/005) | 4 |
| `proposta` (ADR-016:5) | 1 |
| `Draft` (Plano-de-Gerenciamento:6) | 1 |
| `in_progress` (spec-004:5; universal-adjustment-session.yaml:2) | 2 |
| `ready` (HF-0030, HF-0031, HF-0033, HF-0400..0404) | 8 |
| `blocked` (HF-0500:4) | 1 |
| `dispatched` (ledger.yaml:45, :53) | 2 |
| `escalated` (ledger.yaml:5) | 1 |
| `audit_maintenance_started` (audit_trail.yml:3) | 1 |
| `legacy-forge` (registry.yaml:294, :303) | 2 |
| pendente de CCB em texto livre (ADR-005-freeze:6; plano-consolidacao:7; plano-producao:4; CR-001; kb-taxonomy:17; docx R-03 ×3) | 6 |
| pendente de merge em texto (desenvolvimento.md:190-193,196) | 1 |
| 0 B / sem campo status / `UNKNOWN - verify` (requisitos, tap, eap, afa-changelog, input-canonico, HF-RELATORIO, INDEX, 3 envelopes deleg, PLANEJAMENTO, 2 task-*.json, plano-granular ×13, lock) | 27 |
| realocação não-commitada (evento; 21 paths `D` + 2 dirs untracked) | 1 |
| **Total no escopo** | **66** (65 artefatos + 1 evento) |
| Fora do escopo, somente-leitura (§6) | 22 |

---

## 6. Sinalização fora do escopo declarado (sem inventário, sem edição)

- **`.opencode/agents/*.md` — 13 contratos com `<!-- … | Status: DRAFT | … -->` (linha 12 em
  todos):** `agent-ai-llm-rag-dag-mcp-roster-master-specialist.md:12`,
  `agent-art-communication-marketing-pr-specialist.md:12`,
  `agent-business-analysis-specialist.md:12`, `agent-clean-code-evaluator.md:12`,
  `agent-cobit-specialist.md:12`, `agent-copyright-specialist.md:12`,
  `agent-iso-26514-specialist.md:12`, `agent-itil-specialist.md:12`,
  `agent-project-design-specialist.md:12`,
  `agent-project-patterns-standards-specialist.md:12`,
  `agent-quality-architect-specialist.md:12`, `agent-six-sigma-specialist.md:12`,
  `agent-sldc-process-specialist.md:12`.
  **Arquivo IMUTÁVEL para este agente — sem edição.** Drift conhecido: F-09
  (`docs/auditorias/AUD-2611-01-AUDITORIA-REGISTRY-LEDGER.md:158-161`) mostra
  `registry.yaml:168` gravando `promulgado` enquanto o cabeçalho diz DRAFT —
  `UNKNOWN - verify` se é intenção (ONDA 8 Lote 3) ou drift. **Ação recomendada (pela
  custódia própria): `remendar`.**
- **`docs/auditorias/AUD-2610-03.md` — 6 emendas ADR em `status: draft` aguardando CCB:**
  `:28` (declaração) e `:91` (ADR-001), `:122` (ADR-002), `:145` (ADR-003),
  `:166` (ADR-004), `:184` (ADR-005), `:210` (ADR-006-docker). Procedimento recomendado
  próprio R-00 em `:85`. **Ação recomendada: `ratificar`/`remendar` por suas custódias.**
- **`docs/conhecimento/drafts/` — 27 arquivos, 3 com `status: draft`**
  (`extracao-modular+normalizacao-documental-do-plano-de-projeto-COGME.md:51,1172`;
  `report-canon-extract-CCB.md:86`); merge downstream pendente declarado em
  `.ai/specs/kb-taxonomy.md:19`. **Ação recomendada: `remendar` (merge na OKB/glossário).**

---

## 7. Limitações e `UNKNOWN - verify`

- Origem de `spec-003`/`spec-004` (handoff de criação) e dos envelopes `task-ta-deleg-00x`
  não está registrada — `UNKNOWN - verify` (itens S-03, S-04, H-12..H-14).
- Existência de envelopes `task-ta-04xx` para HF-0400..0404 não localizada —
  `UNKNOWN - verify` (H-04..H-08).
- Mismatch `handoff: HF-0500` no envelope de TA-0100 (scheduler × backend) —
  `UNKNOWN - verify` (R-02).
- Estado efetivo dos AC de HF-0030/HF-0031 (marcados × executados) — `UNKNOWN - verify`
  (H-01, H-02): o ledger registra `accepted`, os checklists seguem desmarcados.
- Arquivos `.docx`/`.pdf` não têm frontmatter legível por grep: status inferido apenas de
  nome (`ONGOING`) e de referências canônicas (`OKB.md:391,429`) — `UNKNOWN - verify`.
- Nenhum imutável foi alterado; este relatório é o único arquivo escrito nesta tarefa.
