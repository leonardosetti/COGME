---
id: analise-lista-specs-pendentes-2026-11-02
title: LISTA DE SPECS PENDENTES DE CRIAÇÃO — 2026-11-02
version: 1.1.0
class: relatorio-levantamento
status: active
owner: agent-project-analyst
derived-from:
- docs/analise/lista-specs-pendentes-2026-11-02.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- analise
- docs
- normalizado
---
---
id: LISTA-SPECS-PENDENTES-2026-11-02
title: Lista de specs pendentes de criação — 2026-11-02
status: active
version: 1.1.0
created: 2026-11-02
updated: 2026-11-03T00:55Z
owner: agent-sdd-specialist (.ai/specs/)
task: TA-0031 | handoff: HF-0031 | sender: agent-nexus-prime-ultimate
kill_switch: inherited
---

# LISTA DE SPECS PENDENTES DE CRIAÇÃO — 2026-11-02

Emitida por TA-0031 (HF-0031 §Tarefa 6). Método: derivação das fontes citadas —
REQ-01..15, `docs/planos/plano-granular/plano-producao-agentes.md` (ondas), TAP/EAP,
ADRs e gaps conhecidos (G-01..G-13, GAP-01..GAP-08). **Cada item traz origem
`arquivo:linha`; nada foi inventado.** Slug provisório dos itens novos segue o padrão
`spec-NNN-<specname>.spec.md` do MANIFEST (numeração atribuída na emissão, não aqui).

## A. Placeholders EXISTENTES, conteúdo pendente (não são novos arquivos)

| # | Artefato (`.ai/specs/`) | Estado | Origem | Resumo proposicional |
|---|---|---|---|---|
| A.1 | `requisitos.md` | 0 B — camada 5 sem conteúdo executável; repovoamento bloqueado pelo gate E | `spec-001-constitution-round-1-proposta.spec.md:132-141` (G-08); `spec-002-requisitos-review-round-1.spec.md:100` (GAP-01); `docs/conhecimento/okb.md:38` (OKB-C-08); `spec-002-...spec.md:208-224` (gate E) | Repovoar `.ai/specs/requisitos.md` (0 B) para dar conteúdo executável à camada 5 e fechar o GAP-01/G-08, usando as fontes sobreviventes do TAP v3 (plano-integral e PDF, `spec-001-...spec.md:137-139`). Entregável: artefato de requisitos não vazio com citações `arquivo:linha`; escrita depende das decisões do gate E — re-emissão de ADRs + CCB sobre E-01..E-08 (`spec-002-...spec.md:208-224`). |
| A.2 | `tap.md` | 0 B — baseline de escopo TAP; conteúdo sobrevive só em `plano-integral` | `spec-001-...spec.md:132-141` (G-08); `docs/conhecimento/okb.md:38`; `spec-002-...spec.md:45` (tabela A.1) | Restaurar `.ai/specs/tap.md` (0 B) como baseline de escopo TAP da camada 5, transcrevendo o TAP v3 em regime de congelamento que sobrevive em `plano-integral-tap-1-2-3-4-5.md` e no PDF (G-08; OKB-C-08). Entregável: espelho não vazio da linha de base congelada. |
| A.3 | `eap.md` | 0 B — fases EAP (N1..N11) sem artefato | `spec-001-...spec.md:132-141` (G-08); `docs/conhecimento/okb.md:38` | Criar `.ai/specs/eap.md` (0 B) declarando as fases EAP (N1..N11) hoje sem artefato na camada 5 (G-08; OKB-C-08), derivadas das fontes sobreviventes (plano-integral, PDF). Entregável: artefato EAP não vazio com as fases e rastreabilidade às fontes citadas. |

## B. Specs de domínio pendentes de criação

| # | Spec pendente (escopo) | Origem (citação) | Condição/estado | Resumo proposicional |
|---|---|---|---|---|
| B.1 | **Frontend / interface web responsiva** — REQ-06 (browsers últ. 2 versões), templates, UX | `spec-002-...spec.md:67` (REQ-06); `spec-005-container-layers-v1.spec.md:30` (`index.html` 0 B, `static/` vazio em 2026-11-02); ondas A.11–A.12 em `docs/planos/plano-granular/plano-producao-agentes.md:129-131` | nenhuma spec de frontend existe (só `spec-005` define a camada `front`) | Especificar a interface web responsiva 100% FOSS do MVP — REQ-06: Chrome/Firefox/Edge últimas 2 versões, fase N5.3 (`spec-002-...spec.md:67`) — cobrindo templates, UX e integração browser, hoje ausente (`index.html` 0 B e `static/` vazio, `spec-005-...spec.md:30`). Entregável: spec de frontend para a camada `front`, com escopo derivado da onda 4 (A.11 `agent-ui-ux-advisor` → A.12 `agent-frontend-dev`, `plano-producao-agentes.md:129-131`). |
| B.2 | **Requisitos não funcionais consolidados (NFR)** | `spec-002-...spec.md:101` (GAP-02 — EAP previa fase N2.2, PDF:645, sem artefato) | pendente de criação | Criar o registro canônico de NFR inexistente, cobrindo a fase N2.2 "Requisitos Não Funcionais" prevista na EAP (PDF:645) sem artefato e mapeando P-06/P-07/P-04 a critérios de produto (GAP-02, `spec-002-...spec.md:101`). Entregável: artefato NFR consolidado, fonte única de verificação não funcional. |
| B.3 | **LGPD de produto** — minimização/tratamento em invoice e logs | `spec-002-...spec.md:107` (GAP-08 — "requer decisao CCB/PO"); `constitution.md:36` (P-04) | pendente de decisão CCB/PO antes da emissão | Especificar os critérios LGPD de produto — minimização e tratamento de dados pessoais/financeiros na invoice e nos logs — ausentes dos REQ-01..15 (GAP-08), sob a P-04 (mínimo necessário, sem PII em artefatos técnicos de agentes, direito ao esquecimento por design, `constitution.md:36`). Entregável: spec de LGPD de produto; emissão condicionada a decisão prévia de CCB/PO. |
| B.4 | **Modelo de dados da invoice** — campos bancários, CPF/CNPJ, período | `spec-002-...spec.md:103` (GAP-04); `spec-002-...spec.md:161` (US-004: "modelo de dados pendente — GAP-04") | FECHADO — modelo canônico em `spec-007-invoice-data-model-v1.spec.md` (RATIFICADA, decisão de persistência = PERSISTIR com rota de erase, ADR-016 D4, RAT-2026-11-05-A16-D4) | Modelo canônico de dados da invoice definido em `spec-007` §3.1 (tabela `invoices`, 25 campos tipados). Complementa a `spec-004` (contrato `POST /v1/invoice`). Alimenta US-004 (spec-002:161). Condicionantes D2-D6 da spec-015 ainda pendentes CCB/PO. |
| B.5 | **UAT (plano e roteiro)** — 100% fluxos críticos, zero defeitos críticos/bloqueantes | `spec-002-...spec.md:70` (REQ-09); `spec-002-...spec.md:165` (US-009); parcial em `spec-005-...spec.md:315-344` (§12, proposta restrita às camadas) | parcial: `spec-005` §12 cobre só containers; UAT de produto pendente; destino das evidências `UNKNOWN - verify` (`spec-005-...spec.md:342`) | Especificar o plano e o roteiro de UAT de produto (fase N6.2) com 100% dos fluxos críticos cobertos e passagem binária de zero defeitos críticos/bloqueantes (REQ-09, `spec-002-...spec.md:70`; US-009, `:165`); a proposta da `spec-005` §12 cobre só as camadas de containers (`spec-005-...spec.md:315-344`). Entregável: plano/roteiro de UAT de produto — destino das evidências `UNKNOWN - verify` (`spec-005-...spec.md:342`). |
| B.6 | **Qualidade (PDCA + Ishikawa 6M)** — 12 PDCAs + diagrama | `spec-002-...spec.md:71` (REQ-10); onda 6 em `plano-producao-agentes.md:145-152` (A.19–A.22) | pendente de criação | Especificar a entrega de qualidade da REQ-10: 12 PDCAs consolidados e diagrama Ishikawa 6M na fase N6.3 (`spec-002-...spec.md:71`). Entregável: spec de qualidade com os ciclos PDCA e o diagrama documentados, alinhada à onda 6 "Corrente da Qualidade" (A.19–A.22: qa-sdet, reviewer, gatekeeper, auditor, `plano-producao-agentes.md:145-152`). |
| B.7 | **Pipeline CI/CD** — lint+testes ≤5 min/push, gates | `spec-002-...spec.md:72` (REQ-11); `spec-002-...spec.md:167` (US-011); parcial em `spec-005-...spec.md:198-210` (§8, fase única; marcador `UNKNOWN - verify` em `:210`); G-05 em `plano-producao-agentes.md:33` | parcial; drift G-05 registrado em `.ai/agents/ledger.yaml:24` (ci.yml ≠ vazio — recomendar auditoria) | Especificar o pipeline CI/CD — lint+testes ≤5 min por push com falha bloqueando merge (REQ-11, `spec-002-...spec.md:72`; US-011, `:167`) — cobrindo o delta que a `spec-005` §8 declara só para a fase única (nome exato do job `contract-network` `UNKNOWN - verify`, `spec-005-...spec.md:210`). Entregável: spec de CI/CD, com auditoria do drift G-05 (`plano-producao-agentes.md:33` × `.ai/agents/ledger.yaml:24`). |
| B.8 | **Rastreabilidade de prompts SDD** — 100% catalogados em `.ai/handoffs/` | `spec-002-...spec.md:74` (REQ-13) | pendente de criação | Especificar a rastreabilidade de prompts SDD: 100% dos prompts catalogados em `.ai/handoffs/` (REQ-13, fase N9.3, `spec-002-...spec.md:74`) para auditoria de co-autoria. Entregável: spec de catálogo/rastreio dos prompts com critério de cobertura total. |
| B.9 | **Documentação técnica (arquitetura + OpenAPI revisada)** | `spec-002-...spec.md:75` (REQ-14); `spec-002-...spec.md:170` (US-014); `spec-004-...spec.md:239` (§12: REQ-14 "seção dedicada `UNKNOWN - verify`") | parcial: OpenAPI coberto por `spec-004` §3/`tests/integration/test_openapi.py`; doc de arquitetura pendente | Especificar a documentação técnica — arquitetura + APIs OpenAPI revisadas e aprovadas em Code Review (REQ-14, `spec-002-...spec.md:75`; US-014, `:170`); a OpenAPI já é coberta pela `spec-004` §3 (`tests/integration/test_openapi.py`), mas a seção dedicada à REQ-14 é `UNKNOWN - verify` (`spec-004-...spec.md:239`). Entregável: spec de documentação cobrindo o doc de arquitetura e a revisão da OpenAPI. |
| B.10 | **Camadas L1 (runtime de agentes) e CI como camadas do Art. 10.1** | `spec-005-...spec.md:81` (`UNKNOWN - verify` se há spec própria) e `spec-005-...spec.md:352` (follow-up listado) | escopo a confirmar pelo orquestrador antes de emitir | Especificar, se confirmado pelo orquestrador, as demais camadas do Art. 10.1 fora da `spec-005`: runtime de agentes SDD (L1/L3, Art. 6.5) e camada de CI (GitHub Actions Free Tier sob Bypass registrado, P-01, `spec-005-...spec.md:81`). Entregável: spec própria dessas camadas — escopo a confirmar; existência de spec própria `UNKNOWN - verify` (`spec-005-...spec.md:81`, follow-up em `:352`). |

## C. Lacunas de conteúdo declaradas dentro de specs EXISTENTES (não criam arquivo novo)

| # | Lacuna | Origem |
|---|---|---|
| C.1 | Critérios de aceite da spec backend: seção própria inexistente pré-TA-0031 → `UNKNOWN - verify` | `spec-004-...spec.md:228-230` (§11) |
| C.2 | Fora de escopo adicional (YAGNI) da spec backend: `UNKNOWN - verify` | `spec-004-...spec.md:243-245` (§13) |
| C.3 | Handoff/task de criação das specs 003/004: `UNKNOWN - verify` (sem envelope `task-ta-*.json`) | frontmatter de `spec-003-...spec.md:9` e `spec-004-...spec.md:9-10` |
| C.4 | Job/marcador `contract-network` do CI: nome exato `UNKNOWN - verify` | `spec-005-...spec.md:210` |
| C.5 | Destino/armazenamento das evidências da UAT: FECHADO — destino = `docs/uat/`, classificado por rodada (`docs/uat/rodada-NN/`), com relatório analítico por rodada (taxa de aceite, cobertura analizada, ciclo de implementação). Decisão GP/CCB fechada em 05/11/2026 (pendência #6 dos 7 bloqueantes resolvida). | `spec-005-...spec.md` §12 (atualizado); `spec-009-...spec.md` §3.8 (atualizado); `docs/uat/README.md` (criado); `docs/uat/rodada-001/relatorio-analitico.md` (criado) |

## D. Ondas do plano de produção que exigem specs ainda não criadas

| # | Onda (escopo) | Origem | Specs que faltam |
|---|---|---|---|
| D.1 | Onda 4 — Execução Técnica: A.11 `agent-ui-ux-advisor`, A.12 `agent-frontend-dev` | `plano-producao-agentes.md:121-131` | B.1 (frontend) |
| D.2 | Onda 5 — Infraestrutura, Automação e Segurança: A.14–A.18 (infra, devops, github, digital-security, compliance) | `plano-producao-agentes.md:133-143` | B.7 (CI/CD) + B.3 (LGPD) |
| D.3 | Onda 6 — Corrente da Qualidade: A.19–A.22 (qa-sdet, reviewer, gatekeeper, auditor) | `plano-producao-agentes.md:145-152` | B.5 (UAT), B.6 (qualidade), B.8 (rastreabilidade) |
| D.4 | Onda 7 — Commons e Meta | `plano-producao-agentes.md:154+` | B.8/B.9 conforme escopo da onda |

## E. Condicionantes NÃO-specs que bloqueiam emissão/aprovação (referência cruzada)

| # | Condicionante | Origem |
|---|---|---|
| E.1 | Emendas constitucionais E-01..E-08 pendentes de CCB (não são lei) | `spec-001-...spec.md:193-334`; cobrança em `spec-002-...spec.md:217` |
| E.2 | ADR-016 (backend) — RATIFICADA definitivamente em 05/11/2026 (RAT-2026-11-05-A16); decisões D1–D12 norma vigente; item fechado | `docs/decisoes/adr-016-backend-mvp.md` (frontmatter status: ratificada); `docs/decisoes/adr-log.md` (ADR-LOG-009) |
| E.3 | Emenda da ADR-010 ("Nginx latente" → proxy aceito) — follow-up arquiteto → CCB | `spec-005-...spec.md:349` (§13) |
| E.4 | GAP-07 — conversão REQ→User Story (fase N2.3) não executada; backlog inexistente | `spec-002-...spec.md:106` |
| E.5 | REQ-12 — mínimo de 3 ADRs para decisões críticas (documentos de decisão, não specs) | `spec-002-...spec.md:73` |
| E.6 | G-01..G-04 do plano (constitution/scripts/roster ausentes) — históricos; verificação de estado por auditoria, não por spec | `plano-producao-agentes.md:29-32` |

## F. Cobertura atual (o que JÁ tem spec — para não duplicar)

- `spec-004-backend-mvp-v1.spec.md` — REQ-01..REQ-05, REQ-07, REQ-14 (título, `spec-004-...spec.md:14`); fórmula de spread/IOF fixada em §2 (`:48-50`) — resolve o conteúdo do GAP-03 para o MVP, pendente de ratificação via ADR-016 (E.2).
- `spec-005-container-layers-v1.spec.md` — camadas Dados/Back/Front, REQ-08 (`:263`), REQ-11 parcial (`:292`), REQ-15 (`:277`), UAT de camadas (`:315-344`).
- `spec-001` / `spec-002` — rodadas de definição (emendas e revisão de requisitos), não specs de domínio.
- GAP-05 (nome da API de cotação) resolvido por ADR-010 + `spec-004` §1 (Frankfurter primário / PTAX fallback): `spec-004-...spec.md:25`; GAP-06 parcialmente coberto pelo TTL em `spec-004-...spec.md:107` (via `spec-005-...spec.md:77`).

---
*Emissão: TA-0031 / HF-0031 (2026-11-02). Nenhum item desta lista foi criado por esta tarefa — é lista de pendências para os próximos dispatches, com gate humano quando indicado (B.3, E.1–E.3).*
*Atualização: 2026-11-03T00:55Z — TA-0035 / HF-0034 (resumo proposicional dos 13 itens A.1–A.3 e B.1–B.10; frontmatter `version: 1.1.0`). Ratificação CCB — GP/Humano 2026-11-02 (Art. 5.1): dados propositivos + carimbo de hora.*
