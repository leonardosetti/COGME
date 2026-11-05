# RELATÓRIO ANALÍTICO — COGME: Specs, Roadmap, Epics e User Stories

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira  
**Data:** 2026-11-05 | **Status specs:** 15 emitidas (001–015), 13 `draft`, 2 `in_progress`  
**Marco final (M4):** 15/12/2026 | **Equipe:** 2 membros, ≤20 h/semana (P5)

---

## 1. O QUE ESTÁ FEITO (inventário das specs)

Todas as specs seguem o template canônico TA-0031 (MANIFEST camadas a–h) e vivem em `.ai/specs/`.

| # | Spec | Domínio | Status | Versão | Cobre REQ |
|---|------|---------|--------|--------|-----------|
| 001 | constitution-round-1-proposta | Emenda constitucional rodada 1 | in_progress | 0.1.0 | — |
| 002 | requisitos-review-round-1 | Inventário REQ-01..15 + US-001..17 | in_progress | 0.1.0 | REQ-01..15 |
| 003 | sdd-conf-memory | Memória persistente / SDD / SDDAI | draft | 3.1.0 | — |
| 004 | backend-mvp-v1 | Backend `/v1`: cálculo, cotação, invoice | in_progress | 1.1.0 | REQ-01..05,07,14 |
| 005 | container-layers-v1 | Camadas Dados/Back/Front + proxy | draft | 0.3.0 | REQ-08,11,15 |
| 006 | nfr-consolidados-v1 | NFR-01..25 (fase N2.2) | draft | 0.1.0 | REQ-01,04,05,07,08,11 |
| 007 | invoice-data-model-v1 | Modelo de dados da invoice (GAP-04) | draft | 0.1.0 | REQ-04, US-004 |
| 008 | frontend-web-responsive-v1 | Camada `front` (REQ-06) | draft | 0.1.0 | REQ-06, US-005 |
| 009 | uat-produto-v1 | Plano UAT de produto (fase N6.2) | draft | 0.1.0 | REQ-09, US-009 |
| 010 | qualidade-pdca-ishikawa-v1 | 12 PDCAs + Ishikawa (fase N6.3) | draft | 0.1.0 | REQ-10 |
| 011 | cicd-pipeline-v1 | Pipeline CI/CD (REQ-11) | draft | 0.1.0 | REQ-11 |
| 012 | rastreabilidade-prompts-sdd-v1 | Catálogo handoffs (REQ-13) | draft | 0.1.0 | REQ-13 |
| 013 | documentacao-tecnica-v1 | Doc arquitetura + OpenAPI (REQ-14) | draft | 0.1.0 | REQ-14 |
| 014 | runtime-agentes-ci-layers-v1 | Camadas CI + runtime agentes (Art. 10.1) | draft | 0.1.0 | REQ-15 (Bypass P-01) |
| 015 | lgpd-produto-proposta-v1 | Proposta LGPD produto (B.3/GAP-08) | draft (proposta) | 0.1.0 | — |

**Placeholders 0 B ainda vazios:** `requisitos.md`, `tap.md`, `eap.md` (camada 5, não-specs, aguardam gate E).

---

## 2. REVISÃO DAS SPECS — O QUE FUNCIONA E O QUE FALHA

### Pontos fortes (são specs reais, não rascunhos)
- **Template consistente:** todas as 15 aplicam camadas a–h (frontmatter SS1.1, H1, seções, MAPA TA-0031).
- **Zero invenção:** lacunas marcadas `UNKNOWN - verify` (P-08); alegações com `arquivo:linha`.
- **Hierarquia respeitada:** Constituição > TAP congelado > ADRs > specs > código (Art. 2.1).
- **Rastreabilidade dupla:** cada spec cita origem (handoff/task) e destino (REQ/ADR/Art.).

### Problemas críticos que travam a implementação

| # | Problema | Onde | Impacto |
|---|----------|------|---------|
| 1 | **ADR-016 não ratificada** (backend MVP, fórmula spread/IOF) | spec-004 §2; E.2 na LISTA | Fórmula de cálculo não pode ser congelada no código; US-003 bloqueada |
| 2 | **GAP-04 / GAP-06** (modelo de dados invoice + parâmetros cache) | spec-007; LISTA B.4 | US-004 não tem modelo canônico; D1 (persistência invoice) pendente CCB/PO |
| 3 | **Gap E.4**: REQ→US não convertido (backlog inexistente) | spec-002:106; LISTA E.4 | Não há backlog Kanban pronto para execution das US-018..024 |
| 4 | **CI não atende US-011** (`timeout-minutes: 15`, sem job `contract-network`) | spec-011; LISTA B.7 | Feedback ≤5 min/push não está em vigor |
| 5 | **INDEX.md não atende REQ-13** (1/34 prompts catalogados; 23 rejeitam parser) | spec-012 §3.5 | Rastreabilidade SDD não auditable; kill switch #3 |
| 6 | **Evidências UAT sem destino ratificado** | spec-005:342; spec-009 §3.8 | UAT não pode fechar sem decisão GP/CCB sobre `docs/uat/N6.2/` |
| 7 | **Fora de escopo declarado não implementado** (camadas CI/L1 como Art. 10.1) | spec-005:81/352 → spec-014 | Definição de camada feita, mas não implementada |

### Conclusão da revisão
As specs **especificam corretamente o quê**, mas não **implementam** (por design SDD: especifica → implementa → valida → registra). O gargalo agora é a camada de execução: código, CI, UAT e backlog.

---
# RELATÓRIO ANALÍTICO — COGME (parte 2 de 3)

## 3. NOVAS SPECS PROPOSTAS (gaps levantados da análise)

Nenhuma delas existe ainda. Cada uma fecha um item da LISTA-SPECS-PENDENTES-2026-11-02 ou um gap aberto nas specs existentes.

### Nova spec A — Backlog de User Stories (fecha GAP-07 / E.4)
- **Origem:** spec-002:106 (conversão REQ→US fase N2.3 não executada); LISTA E.4.
- **Escopo:** catálogo das US-001..US-017 existentes + candidatas US-018..024, com DoR/DoD, prioridade MoSCoW (Must: REQ-01..09,11,15; Should: 10,12,13,14), rastreabilidade REQ→US, atribuição a ondas A.11–A.25.
- **Por que é necessária:** sem backlog Kanban populado, não há execution ordenada. US-012 está BLOCKED (gate E); US-007/016/017 condicionais a CCB. Essa spec ordena o que entra em Ready.
- **Depende de:** ratificação ADR-016 (fórmula) e decisão D1 (persistência invoice).

### Nova spec B — Modelos de domínio e migrações Alembic (complementa spec-007)
- **Origem:** spec-007 é contrato de dados da invoice, mas sem DDL/migração; LISTA B.4.
- **Escopo:** entidades `invoices` (spec-007 §3.1), migrações Alembic upgrade/downgrade, repository Protocol, CHECK constraints, índice UNIQUE, seeds sintéticos. Só executável após D1 = "persistida com retenção+erase".
- **Por que é necessária:** US-004 e US-016/017 dependem do modelo materializado. Até D1 ser ratificada, spec-004:126 ("invoice nunca é persistida") segue vigente.

### Nova spec C — Gatilhos de qualidade e drifts (fecha lacunas da spec-010)
- **Origem:** spec-010 §3.1 (status execução dos PDCAs = `UNKNOWN - verify`); MF2-licoes.md e MF3-licoes.md = 0 B.
- **Escopo:** lista de lições aprendidas por macro-fase, gatilhos de métrica (coverage <80%, defeitos críticos em UAT, cycle time >3 dias), ações corretivas ISH-*. Não recria PDCAs (SSOT fica em plano-qualidade.md), apenas registra execução e status.
- **Por que é necessária:** REQ-10 exige evidência de ciclo, não apenas documento. Sem isso, a qualidade não é verificável.

### Nova spec D — Plano de LGPD de produto executiva (fecha B.3 após ratificação)
- **Origem:** spec-015 é PROPOSTA com D1-D7 pendentes CCB/PO.
- **Escopo:** após ratificação, vira spec executiva: política de logs sem PII, rota de erase, retenção de `fx_quotes` (dados públicos), base legal art. 7º V / exclusão art. 4º I.
- **Por que é necessária:** P-04 exige mínimo necessário e direito ao esquecimento por design. Hoje só existe como proposta (draft).

---

## 4. PRIORIZAÇÃO (MoSCoW + dependência)

**Must (bloqueia entrega M4 = 15/12/2026):**
1. Ratificar ADR-016 → libera fórmula spread/IOF (US-003).
2. Decisão D1 (persistência invoice) → libera spec-007 materialização (US-004).
3. Implementar backend MVP na branch `feat/backend-mvp` (spec-004, commits locais, pendente de push/merge).
4. Separar camadas Dados/Back/Front (spec-005, US-018).
5. CI: deltas D-01..D-06 + job `contract-network` (spec-011, US-011 ≤5 min/push).
6. UAT de produto 7 fluxos + camadas F-01..F-07 (spec-009, REQ-09).

**Should:**
7. Backlog de User Stories (nova spec A).
8. 12 PDCAs + Ishikawa (spec-010 já emite; precisa de execução e lições).
9. Rastreabilidade prompts sanitizar INDEX.md + HF-06xx (spec-012, REQ-13).
10. Doc de arquitetura + revisão OpenAPI (spec-013, REQ-14).

**Nice to have / backlog:**
11. Frontend templates (spec-008 implementação, US-022..024).
12. Modelo de dados invoice (nova spec B, após D1).
13. LGPD executiva (nova spec D, após ratificação).
14. ADR-010 emenda (proxy sempre ativo) — follow-up spec-005 §13.
15. US-007 (fallback cotação), US-016/017 (ciclo invoice) — condicionais a CCB.

---

## 5. CARDS PARA CRIAÇÃO DOS EPICS (sugestão de nomes)

Formato sugerido para cada Epic: título, objetivo, specs de entrada, USs, critério de conclusão, dono.

| Epic | Objetivo | Specs de entrada | USs | Critério de conclusão |
|------|----------|------------------|-----|-----------------------|
| E1 Backend MVP | API `/v1` completa: cálculo, cotação, invoice PDF | spec-004 | US-001, US-002, US-003, US-004 | Push/merge de `feat/backend-mvp`; ADR-016 ratificada; AC-01..18 verdes |
| E2 Camadas de infra | Dados/Back/Front separados, proxy ativo, rede `data`×`edge` | spec-005 | US-018, US-019, US-020 | `docker compose up --build` sobe 5 serviços healthy em ≤5 min |
| E3 Frontend MVP | Tela simulação + invoice, JS vanilla, 127.0.0.1:8080 | spec-008 | US-005, US-022, US-023, US-024 | Render server-side, estados empty/loading/error/success, zero recursos remotos |
| E4 CI/CD | Pipeline ≤5 min/push, gates, job contract-network | spec-011, spec-014 | US-011 | Lint+testes ≤5 min; coverage ≥80% fail-closed; build Docker no CI |
| E5 Qualidade | 12 PDCAs, Ishikawa, cobertura, lições | spec-010, nova spec C | US-010 | Relatório PDCA por marco; MF2-licoes.md e MF3-licoes.md preenchidas |
| E6 UAT | 7 fluxos produto + 7 camadas, fail-closed | spec-009 | US-009 | Relatorio-UAT com 100% PASS; zero defeitos críticos/bloqueantes |
| E7 Rastreabilidade SDD | 100% handoffs catalogados, INDEX.md, parser | spec-012 | US-013 | Comando B: rejeitados=0; Comando C: índice×disco sincronizado |
| E8 Documentação técnica | Doc arquitetura + OpenAPI aprovada | spec-013 | US-014 | `docs/arquitetura/` criada; veredito `pass` do reviewer |
| E9 LGPD produto | Critérios LGPD executados (após D1-D7) | spec-015, nova spec D | — | Logs sem PII; rota erase se persistida |
| E10 Backlog US | Catálogo REQ→US, DoR/DoD, ondas | nova spec A | US-001..017, US-018..024 | Kanban populado com ordem de execução |

---
# RELATÓRIO ANALÍTICO — COGME (parte 3 de 3)

## 6. ROADMAP DE SEQUÊNCIA DE IMPLEMENTAÇÃO (até M4 = 15/12/2026)

Ordem respeita dependências técnicas e decisões humanas pendentes. Ondas A.11–A.25 do plano-producao-agentes.md mapeadas aos agentes.

### Fase 1 — Decisões humanas (bloqueantes, antes de código) — semanas 1–2 (nov/26)
| Card | Ação | Quem | Depende de |
|------|------|------|------------|
| F1.1 | Ratificar ADR-016 (fórmula spread/IOF) | GP/CCB | spec-004 §2 |
| F1.2 | Decisão D1: persistência invoice (transitória vs persistida+erase) | CCB/PO | spec-007, spec-004:126 |
| F1.3 | Decisão D2–D7 LGPD (base legal, campos, retenção) | CCB/PO | spec-015 |
| F1.4 | Correção drift E.1 LISTA (E-01..E-08 já ratificadas) | GP | spec-015 D7 |
| F1.5 | Popular backlog Kanban (nova spec A) | PO | spec-002 US-001..017 |

### Fase 2 — Backend MVP (E1) — semanas 3–5
| Card | Ação | Quem | Depende de |
|------|------|------|------------|
| F2.1 | Push/merge branch `feat/backend-mvp` (spec-004 commits locais) | backend-dev (A.10/A.14) | F1.1 |
| F2.2 | Testes unitários calculator + rate_service (T5/T6) | qa-sdet (A.19) | F2.1 |
| F2.3 | Testes integração PostgreSQL + lifespan + invoice (T8/T13) | qa-sdet (A.19) | F2.1 |
| F2.4 | Revisão segurança + código (T9) | digital-security + reviewer (A.17/A.20) | F2.2 |
| F2.5 | ADR-016 proposta + README + status planos (T10) | architect (A.23) | F1.1 |

### Fase 3 — Camadas de infra (E2) — semanas 5–6
| Card | Ação | Quem | Depende de |
|------|------|------|------------|
| F3.1 | Separar `web` → `back` + `front` (docker-compose) | devops + docker-specialist (A.15/A.23) | F2.1 |
| F3.2 | Ativar proxy sempre (remover `profiles: ["proxy"]`) | devops (A.15) | F3.1 |
| F3.3 | Hardening containers (non-root, cap_drop, read_only, digest) | digital-security + devops (A.17/A.15) | F3.1 |
| F3.4 | Testes contrato de rede (matriz §4.2 spec-005) | qa-sdet + digital-security (A.19/A.17) | F3.1 |

### Fase 4 — CI/CD (E4) — semanas 6–7
| Card | Ação | Quem | Depende de |
|------|------|------|------------|
| F4.1 | D-01: reduzir timeout test-suite 15→≤5 min | devops (A.15) | — |
| F4.2 | D-02: job lint+mypy paralelo | devops (A.15) | — |
| F4.3 | D-03/D-04: permissions + SHA-pin actions | devops (A.15) | — |
| F4.4 | D-05: artifacts coverage.xml + junit | devops (A.15) | — |
| F4.5 | D-06: remover append ledger, usar GITHUB_STEP_SUMMARY | devops (A.15) | — |
| F4.6 | Job `contract-network` (5 casos binários spec-005 §7.3) | devops + qa-sdet (A.15/A.19) | F3.1 |

### Fase 5 — Frontend (E3) — semanas 7–8
| Card | Ação | Quem | Depende de |
|------|------|------|------------|
| F5.1 | Templates base.html, index.html, invoice_form.html | frontend-dev (A.12) | F3.1 |
| F5.2 | static/css + js (progressive enhancement, JS off) | frontend-dev (A.12) | F5.1 |
| F5.3 | Estados empty/loading/error/success + labels 1:1 schema | frontend-dev (A.12) | F5.1 |
| F5.4 | Acessibilidade A1..A8 + responsividade 360px | ui-ux-advisor + frontend-dev (A.11/A.12) | F5.2 |
| F5.5 | Revisão contrato `/v1` inalterado (test_openapi verde) | reviewer (A.20) | F5.1 |

### Fase 6 — Qualidade e UAT (E5/E6) — semanas 9–11
| Card | Ação | Quem | Depende de |
|------|------|------|------------|
| F6.1 | Executar 12 PDCAs por marco; preencher lições MF2/MF3 | qa-sdet + auditor (A.19/A.22) | F2.2 |
| F6.2 | Diagramas Ishikawa mermaid (spec-010 §3.2 já emite) | quality-architect | F6.1 |
| F6.3 | UAT 7 fluxos produto + F-01..F-07 (relatorio-UAT) | qa-sdet (A.19) | F5.5, F4.6 |
| F6.4 | Aprovação humana UAT (GP via CCB) | GP/CCB | F6.3 |

### Fase 7 — Rastreabilidade e documentação (E7/E8) — semanas 11–12
| Card | Ação | Quem | Depende de |
|------|------|------|------------|
| F7.1 | Sanitizar INDEX.md (7 órfãos + 33 ausentes), corrigir HF-06xx | sdd-specialist | — |
| F7.2 | Auditoria parser: rejeitados=0, cobertura 100% | sdd-specialist + auditor (A.22) | F7.1 |
| F7.3 | Criar docs/arquitetura/ com visão camadas + matriz interfaces | docker-specialist (A.23) | F3.1, F2.1 |
| F7.4 | Revisão Code Review OpenAPI (veredito pass) | reviewer (A.20) | F7.3 |

### Fase 8 — LGPD (E9) — semana 12 (condicional a D1-D7)
| Card | Ação | Quem | Depende de |
|------|------|------|------------|
| F8.1 | Especificação executiva LGPD (nova spec D) | compliance-governance (A.18) | F1.3 |
| F8.2 | Logs sem PII/valores; rota erase se persistida | backend-dev + digital-security | F8.1, D1 |

---

## 7. CRITÉRIO DE ACEITE GLOBAL (M4, 15/12/2026)

- API `/v1` rodando com 4 rotas, cálculo auditável, invoice PDF.
- `docker compose up --build` sobe 5 serviços (db, migrate, back, front, proxy) healthy em ≤5 min.
- CI: lint+testes ≤5 min/push, coverage ≥80% fail-closed, job `contract-network` verde.
- UAT: 100% fluxos críticos PASS, zero defeitos críticos/bloqueantes.
- REQ-13: 100% handoffs catalogados (parser rejeitados=0).
- REQ-14: doc arquitetura + OpenAPI aprovada em Code Review.
- Zero PII em logs/artefatos (P-04); 100% dependências FOSS (P-01).

---

## 8. RISCOS PRINCIPAIS

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| ADR-016 não ratificada a tempo | Média | Alta (fórmula não congelada) | Decisão GP antecipada (F1.1) |
| D1 (persistência invoice) não decidida | Média | Média (US-004 fica em suspenso) | Manter spec-004:126 (não persistir) |
| CI >5 min não reduzido | Média | Alta (US-011 não atendido) | Executar D-01..D-06 na fase 4 |
| Equipe 2 pessoas, ≤20h/semana | Alta | Média (atraso cronograma) | Focar em Must; backlog no Kanban |
| Evidências UAT sem destino ratificado | Média | Média (UAT não fecha) | Decisão GP sobre `docs/uat/N6.2/` (F1.x) |

---

## 9. O QUE FICOU DE FORA (YAGNI deliberado)

- Autenticação/multiusuário (OS-01 fora).
- App mobile nativo, Safari, tema dark, i18n.
- Cache Redis separado (YAGNI spec-005 §3.2).
- Kubernetes, CDN, cloud paga, self-hosted runners.
- Testes de carga/estresse (OS-07 fora).
- Dashboard próprio de qualidade (GMV: GitHub Insights + coverage).
- Continuous deploy; staging/prod.

---

**Resumo executivo:** As 15 specs estão bem escritas e cobrem todo o escopo REQ-01..15. O que falta agora é execução: decisões humanas (ADR-016, D1-D7), push/merge do backend, separação de camadas, CI ≤5 min, frontend, UAT e sanitização do catálogo de handoffs. O roadmap acima organiza isso em 8 fases até 15/12/2026.
