# ⚔️ RELATÓRIO BRUTAL DE MAPEAMENTO ESTRUTURAL — COBECO MVP v3.2
**Documento de Instrução para Agente Orquestrador**
**Data:** 22/10/2026 | **Classificação:** Governança Operacional | **Status:** ACIONAL IMEDIATA
**Fontes canônicas consultadas:** PMBOK 7 (Princípios + Domínios de Desempenho), Manifesto Ágil, PMO (governança por SSOT e registros de decisão), GitHub Flow / GitHub Projects / GitHub Actions / Agent Skills.

---

## 0. VEREDITO EXECUTIVO (SEM EUFEMISMOS)

1. **O projeto é 100% documentação e 0% software.** Não existe uma única linha de código-fonte, `docker-compose.yml`, `.github/workflows`, `.gitignore` ou `.env.example` no repositório. O README descreve um sistema que **não existe** e instructions de execução (`docker-compose up`) que são **mentira operacional**.
2. **A soberania documental está fragmentada e autorreferente.** Há **três artefatos reivindicando ser SSOT** (`macro_report.md` v3.2, `relatorio_analitico_COBECO.md` v3.1 "Final — SSOT", `brain/md/analise_fundamental_MVP.md` v2.1 "Fonte Primária de Verdade"). Isso viola o próprio conceito de Single Source of Truth. A cadeia de precedência abaixo (§2) restaura a soberania.
3. **Conflito fatal de stack:** README oficial afirma React/NestJS/PostgreSQL/TanStack/Prisma; o estado da arte v3.2 (ADRs aprovados) determina **Vanilla JS + FastAPI + MySQL InnoDB**. O README está obsoleto desde 12/09/2026 e é a face pública do repositório — risco direto de nota e de indução da equipe a erro.
4. **Cronograma estourado e fictício.** Os marcos S1–S5 terminam em **15/10/2026**; hoje é **22/10/2026**. Zero sprints executadas. A "Fase 1: 🟢 Em andamento" do README é status inflado sem evidência (no commits de código). Data-limite global: **13/11/2026** → restam ~22 dias corridos contra 30 dias planejados de desenvolvimento, já com 7 dias de atraso.
5. **Há defeitos internos na própria documentação canônica** (IDs duplicados de UCs, referências cruzadas erradas, DERs divergentes). Um agente que "obedecer o SSOT" cegamente propagará esses erros ao código. A §6 lista cada defeito com ação de saneamento prescritiva.

**Conclusão brutal:** a maturidade analítica do projeto é alta; a maturidade de execução é nula; a integridade da baseline é duvidosa. O caminho ótimo (YAGNI) é: **saneamento documental cirúrgico (1 dia) → alinhamento do repositório ao GitHub como plataforma de gestão (1 dia) → Sprint 1 imediatamente (§8).**

---

## 1. INVENTÁRIO COMPLETO DE ARTEFATOS (cada arquivo foi aberto e validado)

### 1.1 Núcleo canônico (v3.2 — manter na raiz, promover a `/docs` após aprovação)

| Arquivo | Papel real | Estado | Decisão |
|---|---|---|---|
| `macro_report.md` | Pacote DOC-01..04 consolidado, v3.2, 14/09/2026 | ✅ Mais recente e completo | **SSOT PRIMÁRIO** |
| `REQUISITOS.md` | RF01–RF18 + RNF01–RNF10, v3.2 | ✅ Consistente com macro | SSOT derivado (canônico p/ requisitos) |
| `CASOSDEUSO.md` | 29 UCs, v3.2 | ⚠️ Defeitos internos (§6-D1..D3) | Canônico **após correção** |
| `CAMADADEDADOS.md` | DER 8 tabelas PT-BR, MySQL, v3.2 | ✅ Coerente com macro | Canônico p/ dados |
| `analise-UseCase-consistencia.md` | Happy paths/exceções/edge-cases, v3.2 | ⚠️ Defeitos (§6-D2,D4) | Canônico p/ fluxos |
| `board_roadmap.md` | Blueprint GitHub Projects: colunas, labels, 5 milestones, issues por sprint | ✅ Excelente, pronto p/ execução | **Instrução direta ao orquestrador** |
| `pre_DOCUMENTO.md` | Rascunho ABNT da monografia (5 integrantes nomeados) | ⚠️ Pré-documental, placeholders `[Nome do Seu Curso]` | Monitorar/alimentar `COBECO_Monografia_new.docx` |

### 1.2 Camada histórica superseded (v3.1 e anteriores)

| Arquivo | Conteúdo | Veredito |
|---|---|---|
| `relatorio_analitico_COBECO.md` | ADRs v3.1, ainda cita SQLite3/FastAPI/Vanilla (ADR-003 "revisado para MySQL" anotado inline) | **ARQUIVAR** (mover p/ `_archive/`). Manter apenas como trilha de auditoria dos ADRs |
| `analise_REQ_CasosDeUso.md` | Análise v3.1 com registro das falhas F1–F10 | **ARQUIVAR** — mas suas resoluções F1–F10 são **normativas**: o orquestrador deve tratá-las como decisões vigentes |
| `diagrama_DER.md` | DER v3.1: inglês (`supplier_categories`, `deleted_at`) + base SQLite WAL | **ARQUIVAR** — substituído por `CAMADADEDADOS.md` (PT-BR/MySQL). Conflito de nomenclatura em §6-D5 |
| `README.md` | Projeto público | **NÃO arquivar — REESCREVER** (§7 C1): é a interface do repo e está errado |

### 1.3 Artefatos de design/protótipo

| Arquivo(s) | Avaliação | Decisão |
|---|---|---|
| `COBECO_prtp_high_v1.0.html`, `v1.1.html`, `v2.0.html` | Alta fidelidade versionado; v2.0 vigente | Manter v2.0 ativo; **arquivar v1.0/v1.1** |
| `COBECO_prtp_low_v1.0.excalidraw` + `.png` | Baixa fidelidade v1.0 | Ativo (entrega acadêmica) |
| `COBECO_figma_export.html` | Export morto (sem fonte editável) | Monitorar; candidato a arquivo se v2.0 HTML cobrir |
| `uc.drawio`, `uc.drawio.xml`, `uc.drawio.png`, `der.drawio`, `der.drawio.png` | Diagramas UML/DER binários/fonte | **Duplicação perigosa:** `uc.drawio` vs `uc.drawio.xml` e PNGs gerados. Definir fonte primária = `.drawio`; PNGs = derivados regeneráveis |
| `excalidraw_baixa/1..6_grp.svg` | SVGs de grupos de trabalho | Ativos p/ monografia |
| `Projeto_COBECO.docx` (20,8 MB!) e `prj_docs/COBECO_Monografia_new.docx` (1 MB) | **Dois docx concorrentes**, um gigante (binário no git = inchaço de clone) | Investigar qual é a monografia vigente; extrair imagens do 20MB; considerar Git LFS ou mover para Releases |
| `prj_docs/wrk_grp.md` | Enunciado oficial da disciplina (entrega docs 18/09/2026 19h; apresentação ≥30min; nomes obrigatórios) | **CANÔNICO EXTERNO** — restrições contratuais do cliente acadêmico. Nunca arquivar |

### 1.4 Diretório `brain/` (cérebro histórico)

| Subdiretório | Conteúdo | Decisão |
|---|---|---|
| `brain/_old-artifact/` | Escopos/objetivos antigos + **3 arquivos ZEROLINE** (`req_func.md`, `req_n-func.md`, `tech_stack.md` vazios) | Arquivar como está; **deletar os vazios** (artefato vazio rastreado é ruído) |
| `brain/md/` | 5 documentos v1.0–v2.1 que ainda citam **React/NestJS/PostgreSQL** | **ARQUIVAR explicitamente** — são exatamente os documentos apontados como causadores da falha F1 pelo próprio SSOT ("Arquivar documentos anteriores como histórico") |
| `brain/diagrams/` | `prt_baixa_v1/v2/v5.excalidraw`, UC v0.3 drawio | Arquivar v1/v2 (há v1.0 na raiz como vigente); manter v5 se for a fonte do low-fi atual |

### 1.5 Ausências críticas (o que NÃO existe e precisa existir)

`src/` (domain/usecases/adapters/routers) • `frontend/` (8 módulos ES6 do ADR-001) • `docker-compose.yml` • `.env.example` • `.gitignore` • `.github/workflows/ci.yml` • `tests/` (pytest --cov) • `seed.py` • schema SQL • CODEOWNERS • Issue/PR templates • `LICENSE`.

---

## 2. HIERARQUIA DE SOBERANIA DOCUMENTAL (lei do orquestrador)

Em conflito, prevalece nesta ordem decrescente:

1. **`prj_docs/wrk_grp.md`** — contrato com o cliente (restrições imutáveis: ABNT, PDF, nomes, prazo).
2. **`macro_report.md` v3.2** + derivados oficiais v3.2 (`REQUISITOS.md`, `CAMADADEDADOS.md`, `CASOSDEUSO.md`, `analise-UseCase-consistencia.md`) — escopo, requisitos, dados, fluxos.
3. **Resoluções F1–F10 de `analise_REQ_CasosDeUso.md`** — jurisprudência de conflitos (ex.: access token só em memória; tela inicial = Criar Lista; não persistir comparações).
4. **ADRs v3.1 de `relatorio_analitico_COBECO.md`** — arquitetura, **com ADR-003 lido como MySQL InnoDB** (revisão registrada).
5. **`board_roadmap.md`** — execução/GitHub Projects (datas devem ser rebaselined, §7 C4).
6. **README.md** — após reescrita (§7 C1), passa a ser espelho derivado, nunca fonte.
7. Todo o resto (`brain/**`, protótipos antigos, DER v3.1) — histórico, valor probatório zero para decisões.

**Premissas inegociáveis herdadas:** KISS, YAGNI, SDD/OpenAPI-first, Clean Architecture 4 camadas, ACID (InnoDB), Desktop-only ≥1024px, FOSS, dados seed (sem scraping/APIs externas), testes ≥80%, CI GitHub Actions <5min.

---

## 3. STACK CANÔNICA VIGENTE (v3.2 — o que o agente DEVE construir)

| Camada | Decisão oficial (ADRs) | O que o README diz (ERRADO) |
|---|---|---|
| Frontend | HTML5 + Tailwind CDN + **Vanilla JS ES6 Modules** (8 módulos: app/state/api/auth/list/compare/export/ui) | React 18 + TS + Vite + shadcn/ui |
| Backend | **Python 3.12 + FastAPI + Pydantic** (domain→usecases→adapters→routers) | NestJS 10 + TS |
| Banco | **MySQL 8 InnoDB** (utf8mb4_unicode_ci), 8 tabelas PT-BR, sem ORM pesado | PostgreSQL 16 + Prisma |
| Auth | JWT: access 15min **memória JS**, refresh 7d cookie httpOnly SameSite=Strict, bcrypt salt=12, rate limit 6/15min | Resend/email 15min |
| Recuperação | Pergunta de segurança + modo log stdout (`RECOVERY_MODE=log`) — **sem email real** | Email via Resend/Mailhog |
| Export | **PDF server-side ReportLab** (UC08/UC29) + CSV client-side Blob (ADR-005) | Apenas CSV |
| Infra | Docker Compose (app+MySQL) + GitHub Actions | igual (este ok) |
| Testes | pytest+cov ≥80% | Jest/Vitest |

---

## 4. MATRIZ DE ARCHIVING (plano de organização estrutural)

**Ação proposta (commit único, rastreável, reversível):**

~~~
criar:  _archive/            # camada histórica normativa (v3.1)
        _archive/brain-md/   # docs v1.0–v2.1 com stack antiga
        docs/                # SSOT v3.2 + README corrigido
mover:  relatorio_analitico_COBECO.md, analise_REQ_CasosDeUso.md, diagrama_DER.md → _archive/
mover:  brain/md/*.md → _archive/brain-md/          (preserva F1 como evidência resolvida)
mover:  COBECO_prtp_high_v1.0.html, v1.1.html → _archive/prototipos/
mover:  brain/diagrams/prt_baixa_v1,v2.excalidraw, diagrama_casos_de_uso_v0.3.drawio → _archive/prototipos/
deletar: brain/_old-artifact/{req_func.md, req_n-func.md, tech_stack.md}  (zero bytes)
manter ativo na raiz/docs: macro_report.md, REQUISITOS.md, CASOSDEUSO.md, CAMADADEDADOS.md,
        analise-UseCase-consistencia.md, board_roadmap.md, pre_DOCUMENTO.md, README.md,
        prj_docs/, excalidraw_baixa/, COBECO_prtp_high_v2.0.html, COBECO_prtp_low_v1.0.*, uc.drawio, der.drawio
regenerar: uc.drawio.png / der.drawio.png a partir das fontes .drawio (marcar como derivados no header do README de docs)
docx 20MB: extrair mídia, reduzir, ou migrar p/ GitHub Release; avaliar Git LFS
~~~

**Monitorar/validizar (não arquivar):** `pre_DOCUMENTO.md` (fonte da monografia), `COBECO_Monografia_new.docx` (entregável acadêmico P0 vencido em 18/09 — verificar se foi entregue fora do repo), protótipo v2.0 (validar aderência aos 29 UCs antes do frontend).

---

## 5. GAP ANALYSIS CONTRA PMI/PMBOK 7 E MANIFESTO ÁGIL

| Dimensão PMBOK 7 | Estado | Lacuna | Ação |
|---|---|---|---|
| **Baseline de escopo** | ✅ definida (18 RF/10 RNF/29 UC/8 tabelas) | IDs de UC inconsistentes na baseline | §6 D1–D4 |
| **Baseline de cronograma** | ❌ morta | Marcos S1–S5 expiraram 15/10 sem execução | Rebaseline §7 C4 |
| **Baseline de custo** | N/A (acadêmico FOSS) | — | — |
| **Entrega de valor** | ❌ zero incrementos | Valor demonstrável = 0 | Sprint 1 imediato |
| **Governança/PMO** | ⚠️ parcial | Múltiplos "SSOT", sem change log unificado, sem registro formal de mudanças v3.2→código | Instituir §2 + CHANGELOG.md |
| **Riscos** | ❌ não registrados | Prazo estourado é risco crítico não tratado em nenhum doc | Criar `RISCOS.md` (registro vivo) |
| **Stakeholders** | ⚠️ | README tem placeholders "[Nome do Stakeholder]" etc.; PO real citado no macro (Thais Cristina Casagrande) | §7 C5 |
| **Adaptação (ágil)** | ❌ | Docs excelentes mas processo waterfall-disfarçado: 45 dias só de análise | Time-box: docs congeladas, feedback via incremento |
| **Qualidade (DoD)** | ✅ boa | DoD definido (CI verde + review + cov≥80%) | Codificar em PR template |
| **Manifesto Ágil** | violação frontal | "Software funcionando sobre documentação abrangente" — proporção aqui é 100%/0% | Corrigir via execução, não via mais docs |

---

## 6. CONFLITOS INTERNOS DETECTADOS NA BASE CANÔNICA (defeitos que o agente deve sanear ANTES de codar)

| # | Severidade | Defeito | Evidência | Prescrição |
|---|---|---|---|---|
| D1 | 🔴 | **UC09 duplicado**: é "Cadastrar-se" (RF01) E "Imprimir" (RF18) simultaneamente | `macro_report.md` linhas 70 e 88; `CASOSDEUSO.md` linhas 28 e 61 | Renomear "Imprimir" para **UC19** (slot livre nos principais) nas 3 fontes v3.2; regenerar tabela do macro |
| D2 | 🟡 | **UC19 órfão**: cabeçalhos dizem "Grupo A … UC19" mas o catálogo principal não define UC19; fluxo de exceção de UC14 referencia "FK de produto (UC19)" quando deveria ser UC23 (Fornecer Catálogo) | `CASOSDEUSO.md:24`, `analise-UseCase-consistencia.md:166,245` | Corrigir referência cruzada p/ UC23; definir UC19 conforme D1 |
| D3 | 🟡 | Contagem declarada "19 principais + 10 internos = 29" mas a tabela principal lista 19 linhas com ID repetido → na prática 18 únicos | `macro_report.md` §3.1 | Recalcular após D1; adicionar checklist de contagem no rodapé de revisão |
| D4 | 🟡 | Tabela de atores/casos do macro usa formatação quebrada (pipes irregulares) e datas do histórico inconsistes (v2.0 "Auth adicionada +7 UCs" sem mapeamento) | `macro_report.md` §1, §3 | Higienizar markdown; truncar histórico ao essencial |
| D5 | 🔴 | **Duas versões de DER coexistem como "APROVADAS"**: v3.1 (inglês, `supplier_categories`, `deleted_at`, SQLite) vs v3.2 (PT-BR, `fornecedores_categorias`, `deletado_em`, MySQL) | `diagrama_DER.md` vs `CAMADADEDADOS.md` | v3.2 vence; marcar header do v3.1 com `⚠️ SUPERSEDED — ver CAMADADEDADOS.md` antes de arquivar |
| D6 | 🔴 | **README contradiz toda a base** (stack, email/Resend, fases, status "Em andamento" falso, equipe placeholder) | `README.md` inteiro | Reescrita total §7 C1 |
| D7 | 🟡 | `board_roadmap.md` ancora datas em 15/09/2026 e exige entrega de docs em 18/09 — ambas vencidas | §2, §3 | Rebaseline §7 C4 |
| D8 | 🟡 | `relatorio_analitico_COBECO.md` v3.1 auto-intitula "Final — SSOT" enquanto v3.2 existe | header | Editar header p/ "SUPERSEDED por macro_report.md v3.2" antes de arquivar |
| D9 | 🟢 | `analise_fundamental_MVP.md` v2.1 declara "este prevalece" — cláusula de soberania obsoleta | §1.1 | No archiving, prefixar nota de invalidação |
| D10 | 🟢 | Protótipo high v2.0 ainda não foi validado contra os 29 UCs v3.2 (UC03 pré-filtro e PDF surgiram depois) | — | Validar antes da Sprint 3 (pré-filtro) |

---

## 7. PLANO PROPOSITIVO DE SANEAMENTO (ordem exata de execução)

**Lote A — Integridade da baseline (dia 0, 100% documental, sem código):**
- C1. **Reescrever README.md**: stack v3.2 (§3), remover instruções inexequíveis (ou rotular "planejado"), status honesto ("Documentação aprovada; desenvolvimento não iniciado"), equipe real, link p/ `docs/`. Adicionar seção "Estrutura do repositório" apontando hierarquia §2.
- C2. Aplicar correções D1–D4, D5, D8, D9 (patch documental único, commit `docs: saneamento baseline v3.2.1`).
- C3. Executar matriz de archiving §4 (commit `chore: archive superseded artifacts`). Criar `CHANGELOG.md` registrando v3.2.1.

**Lote B — Plataforma GitHub como PMO (dia 0–1):**
- C4. Rebaselinear `board_roadmap.md`: S1 24/10→29/10, S2 →05/11, S3 →09/11, S4 →12/11, S5 buffer até 13/11 (com flag explícita de compressão de escopo: P1 podem ser cortados se P0 atrasar — decisão PO registrada).
- C5. Criar **GitHub Project (Kanban)** com as 5 colunas e labels P0/P1/P2 + frontend/backend/database/infra/docs definidas no roadmap; criar os 5 Milestones; converter as issues do roadmap em issues reais (uma issue por card, corpo copiado literalmente).
- C6. Configurar branch protection em `main`: PR obrigatório, CI verde obrigatório, padrão `feat/UC-XX-descricao`, `.github/PULL_REQUEST_TEMPLATE.md` com DoD checklist e campo "RF/UC atende".
- C7. Scaffold mínimo: `.gitignore` (node_modules? não — Python: `__pycache__`, `data/`, `.env`), `.env.example`, `CODEOWNERS`, `SECURITY` não aplicável (acadêmico — YAGNI).

**Lote C — Infraestrutura (Sprint 1, dias 1–6):**
- C8. `docker-compose.yml` (FastAPI uvicorn + MySQL 8 utf8mb4) + healthchecks; schema.sql das 8 tabelas PT-BR com FKs CASCADE/RESTRICT e `deletado_em`; `seed.py` (11 \cat + 10 forn + N:N + 50 prod + ~300 preços, <10s).
- C9. `.github/workflows/ci.yml`: job backend (lint ruff + pytest --cov-fail-under=80) e job docker-build, alvo <5min (RNF07). Sem job de frontend (Vanilla = YAGNI).

**Lote D — Desenvolvimento por valor (Sprints 2–5):** seguir estritamente o backlog de `board_roadmap.md`, ordem P0→P1, OpenAPI primeiro (RNF02), nada além do contrato.

---

## 8. CARTER DE DECISÃO PARA O ORQUESTRADOR (heurísticas operacionais)

1. **Nunca implemente algo não rastreável a RF/RNF/UC.** Sem ID → não existe (YAGNI).
2. **Nunca introduza dependência não listada no ADR** (no React, no Prisma, no Redis, no Celery, no OAuth).
3. **Conflito entre dois docs v3.2 → micro-decisão registrada em `CHANGELOG.md` com justificativa + princípio invocado**; >1 dia pendente → escalar ao PO. Nenhum doc novo de "análise" — decidir é o deliverable.
4. **Datas vencidas não se renegociam em silêncio**: rebaseline visível no GitHub Project (PMBOK: baseline muda por controle de mudança, não por edição sorrateira).
5. **Binários grandes fora do fluxo normal**: docx/png são entregáveis acadêmicos, mantê-los versionados, mas nenhuma nova versão sem substituição da anterior (inchar repo não é neutro — custo de clone/CI).
6. **Cada PR = 1 UC/milestone de card**; merge só com CI verde + 1 review (DoD do roadmap).
7. **Se P0 atrasar, corte P1 com aprovação do PO** — não estenda prazo (iron triangle: prazo fixo pelo calendário acadêmico).
8. **Prioridade máxima externa**: confirmar se a monografia (entrega 18/09, presentation 30min) foi efetivamente entregue; se não, isso sobrepõe qualquer sprint de código.

---

## 9. INDICADORES DE SAÚDE DO PROJETO (monitoramento contínuo)

| KPI | Hoje | Alvo S1 | Gatilho de alerta |
|---|---|---|---|
| % RF implementados | 0% | RF01–04 | <2 RFs P0/semana |
| Issues do roadmap convertidas | 0 | 100% S1+S2 | — |
| Documentos ativos vs arquivados | 100% ativos (caos) | 6 ativos | qualquer novo "SSOT" |
| Cobertura de testes | n/a | >0 (auth) | PR sem teste |
| Dias restantes até 13/11 | 22 | 16 ao fim S1 | burn-down plano |
| Commits de código/semana | 0 | ≥10 | 3 dias sem commit |

---

*Este relatório é autocontido: todo fato acima foi verificado por inspeção direta dos artefatos em `/workspace` (branch `qwen-code-*`, HEAD `881c971`, working tree limpo, histórico shallow de 1 commit). O orquestrador pode agir exclusivamente com base nele, respeitando a hierarquia do §2.*
