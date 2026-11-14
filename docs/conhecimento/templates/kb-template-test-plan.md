---
id: kb-template-test-plan
title: Template de Plano de Testes / QA Plan — COGME
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-qa-sdet
derived-from:
  - IEEE 829 / ISO/IEC/IEEE 29119 (Test Documentation)
  - PMBOK 7ª — Domínio Entrega (Quality)
  - constitution.md Art. 4.8 (Qualidade fechada, coverage ≥ 80%)
  - CI-CD-GOV-001 (Política CI/CD fail-closed)
  - OKB §6 (Métricas e fluxo)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
  - template
  - qualidade
  - test-plan
  - qa
  - pmbok
  - ieee829
---

# Template de Plano de Testes / QA Plan — COGME

> **Finalidade**: Definir **estratégia, escopo, abordagem, recursos, cronograma e critérios** de validação da qualidade do software COGME. Cobre **todos os níveis** de teste: Unitário, Integração, Sistema (E2E), Performance, Segurança, Acessibilidade, Aceitação (UAT).
> **Obrigatório para Gate 2 (Desenho)** — deve ser aprovado pelo CCB antes de escalar desenvolvimento.
> **Atualização**: A cada wave/marco (M1–M4) ou CR que afete qualidade.

---

## 1. INTRODUÇÃO

### 1.1 Propósito
Documentar a estratégia de testes para o projeto COGME (Conversor de Ganhos em Moeda Estrangeira), garantindo que **todos os requisitos (REQ-XXX)** sejam validados com **evidência rastreável** (RTM), atendendo aos **Critérios de Aceite (AC-XXX)** e **NFRs**.

### 1.2 Escopo
| Em Escopo | Fora de Escopo |
|---|---|
| Backend API (FastAPI): rates, simulate, invoice, health | Testes de carga extrema (>1000 req/s) — não é requisito |
| Frontend (Jinja2 + HTMX + Tailwind): simulator, invoice view | Testes de compatibilidade IE11 / browsers legados |
| Banco de dados (PostgreSQL 15+): schema, migrations, queries | Testes de caos em produção (Chaos Engineering) — wave futura |
| Infraestrutura (Docker Compose, Nginx proxy) | Testes de recuperação de desastre (DR) — wave futura |
| Segurança (Argon2id, HMAC, criptografia, FOSS compliance) | |
| Observabilidade (health, metrics, logs, tracing) | |
| LGPD / Marco Civil compliance (dados, retenção, consentimento) | |

### 1.3 Referências
- Constitution.md (Art. 3, 4.8, 7, 9.3)
- PRD / Specs (SPEC-004, SPEC-008, SPEC-017–023)
- ADRs (ADR-001, ADR-003, ADR-010, ADR-017, ADR-019)
- NFRs consolidados (`docs/conhecimento/arquitetura/nfrs.md`)
- RTM (`docs/planos/plan-rtm.md`)
- CI-CD-GOV-001, DEVSECOPS-001

---

## 2. ESTRATÉGIA DE TESTES (Test Strategy)

### 2.1 Pirâmide de Testes (Alvo)

```
           ████████████
         ██  E2E / UAT  ██        ← 10%  (Críticos, alto valor, lento)
       ████████████████████
     ██  Integração / API  ██      ← 30%  (Contratos, fluxos, DB, ext. APIs)
   ████████████████████████████
 ██  Unitários (Funções, Classes) ██  ← 60%  (Rápidos, isolados, alta cobertura)
██████████████████████████████████
```

### 2.2 Critérios de Qualidade (Quality Gates) — **Bloqueiam Merge/Deploy**

| Gate | Métrica | Threshold | Ferramenta | Onde Aplicado |
|---|---|---|---|---|
| **G1 — Pre-Commit** | Formatação (ruff/black), Tipagem (mypy strict), Lint | Zero erros | pre-commit hooks | Local / CI |
| **G2 — Unit** | Cobertura de linhas (line coverage) | ≥ 80% | pytest-cov / coverage.py | CI (todo push) |
| **G2 — Unit** | Cobertura de branches | ≥ 70% | pytest-cov | CI |
| **G3 — Integração** | Testes de integração passing | 100% | pytest | CI (todo push) |
| **G4 — E2E** | Cenários críticos passing | 100% | pytest + Playwright (opcional) | CI (PR / nightly) |
| **G5 — Performance** | P95 latency (simulate) | ≤ 2s | Custom benchmark | CI (PR) / Gate 3 |
| **G5 — Performance** | P95 latency (PDF invoice) | ≤ 3s | Custom benchmark | CI (PR) / Gate 3 |
| **G6 — Segurança** | Vulnerabilidades High/Critical | 0 | Trivy / Snyk / bandit | CI (todo push) |
| **G6 — Segurança** | Segredos no código | 0 | TruffleHog / detect-secrets | CI (todo push) |
| **G7 — FOSS** | Licenças não-FOSS | 0 | license-checker / FOSSA | CI (todo push) |
| **G8 — Acessibilidade** | WCAG 2.1 AA (frontend) | 0 violações AA | axe-core / pa11y | CI (PR) |
| **G9 — SDDAI** | Pipeline SDDAI verify | 7/7 passos | `.github/workflows/sddai-verify.yml` | CI (todo push) |

---

## 3. NÍVEIS DE TESTE (Test Levels)

### 3.1 Testes Unitários (Unit Tests)
| Aspecto | Detalhe |
|---|---|
| **Escopo** | Funções puras, classes de domínio, calculadores, validadores, serializers, helpers |
| **Ferramentas** | `pytest`, `pytest-asyncio`, `hypothesis` (property-based), `unittest.mock` / `pytest-mock` |
| **Isolamento** | **Sem I/O real** — mock de DB, HTTP, filesystem, time, random |
| **Cobertura Alvo** | ≥ 80% linhas, ≥ 70% branches |
| **Localização** | `tests/unit/` espelhando `src/` |
| **Exemplos** | `test_calculator.py`, `test_schemas.py`, `test_invoice_number.py`, `test_rate_providers.py` |
| **Execução** | `pytest tests/unit -xvs --cov=src --cov-report=term-missing` |

### 3.2 Testes de Integração (Integration Tests)
| Aspecto | Detalhe |
|---|---|
| **Escopo** | Interação entre componentes: API ↔ DB, API ↔ External APIs (Frankfurter/PTAX), Service ↔ Repository, Migration ↔ Schema |
| **Ferramentas** | `pytest`, `pytest-asyncio`, `httpx.AsyncClient` (FastAPI TestClient), `sqlalchemy` (test DB), `testcontainers` (PostgreSQL real) ou DB compartilhado CI |
| **Banco de Dados** | **PostgreSQL real** (não SQLite) — container `testcontainers` ou service CI; fixtures via `alembic upgrade head` + seed data |
| **APIs Externas** | **Mock obrigatório** (respx / httpx-mock) — não depender de rede externa no CI |
| **Localização** | `tests/integration/` |
| **Exemplos** | `test_rates.py` (rate service + cache + fallback), `test_invoice.py` (invoice service + PDF + DB), `test_simulations.py` |
| **Execução** | `pytest tests/integration -xvs --cov=src --cov-append` |

### 3.3 Testes de Sistema / End-to-End (E2E Tests)
| Aspecto | Detalhe |
|---|---|
| **Escopo** | Fluxos completos de usuário: Simulador → Resultado → Invoice PDF; Login → Sessão → Logout; Multiusuário isolamento |
| **Ferramentas** | `pytest` + `Playwright` (headless Chromium/Firefox/WebKit) **OU** `httpx` + parsing HTML (mais leve, sem browser real) |
| **Ambiente** | **Staging-like**: Docker Compose completo (db, back, front, proxy) — `docker compose -f docker-compose.test.yml up` |
| **Dados** | Seed determinístico + cleanup entre testes (transação rollback ou truncate) |
| **Localização** | `tests/e2e/` |
| **Exemplos** | `test_e2e_simulator.py`, `test_e2e_invoice_pdf.py`, `test_e2e_multiusuario.py`, `test_e2e_auth_flow.py` |
| **Execução** | `pytest tests/e2e -xvs` (tag `@postgres` para DB real) |

### 3.4 Testes de Performance (Performance Tests)
| Aspecto | Detalhe |
|---|---|
| **Escopo** | Latência (P50, P95, P99), Throughput, Resource Usage (CPU, RAM, DB connections) sob carga |
| **Ferramentas** | `locust` / `k6` / custom `asyncio` benchmark script |
| **Cenários** | 1. Simulação única (baseline) 2. Carga contínua 50 req/s por 60s 3. Pico 200 req/s por 30s 4. Soak test 10 req/s por 1h |
| **Métricas Alvo** | P95 simulate ≤ 2s; P95 PDF ≤ 3s; CPU < 70% sustentado; RAM < 80%; DB connections < 80% pool |
| **Execução** | Manual / Agendado (nightly) / Gate 3 obrigatório — **não bloqueia CI diário** |
| **Relatório** | `docs/relatorios/rel-performance-YYYYMMDD.md` |

### 3.5 Testes de Segurança (Security Tests)
| Aspecto | Detalhe |
|---|---|
| **Escopo** | SAST (código), DAST (runtime), SCA (dependências), Secrets, Config hardening, AuthZ/AuthN, Criptografia, LGPD |
| **Ferramentas** | `bandit` (SAST Python), `Trivy` / `Snyk` / `OWASP Dependency Check` (SCA), `TruffleHog` (secrets), `OWASP ZAP` / `nikto` (DAST - staging), `semgrep` (regras custom) |
| **Critérios** | 0 High/Critical vulns em dependências; 0 secrets em código; 0 findings SAST High; AuthZ bypass attempts blocked |
| **Execução** | SAST/SCA/Secrets: **todo push (CI)**; DAST: **PR + Gate 3** |
| **LGPD Específico** | Teste de: pseudonimização (HMAC lookup), criptografia em repouso, retenção/exclusão, consentimento, DPIA lightweight |

### 3.6 Testes de Acessibilidade (Accessibility Tests)
| Aspecto | Detalhe |
|---|---|
| **Escopo** | Frontend templates (Jinja2) → HTML renderizado: WCAG 2.1 AA |
| **Ferramentas** | `axe-core` (via Playwright/puppeteer) ou `pa11y` |
| **Critérios** | 0 violações **Críticas/Serias (AA)**; Melhorias AAA opcionais |
| **Execução** | CI (PR) + Gate 3 |

### 3.7 Testes de Aceitação do Usuário (UAT)
| Aspecto | Detalhe |
|---|---|
| **Escopo** | Validação com usuários reais (beta testers, FATEC) contra **Critérios de Aceite (AC-XXX)** |
| **Formato** | Roteiro de testes (Test Scripts) em Gherkin → executado manualmente ou semi-automatizado |
| **Critérios** | 100% ACs críticos passing; 0 defeitos P0/P1 abertos; Feedback qualitativo coletado |
| **Execução** | Gate 3 (Go-Live) + Pós-release (primeira semana) |
| **Documentação** | `docs/uat/rodada-NNN/relatorio-analitico.md` + evidências |

---

## 4. AMBIENTES DE TESTE

| Ambiente | Finalidade | Composição | Dados | Acesso | Refresh |
|---|---|---|---|---|---|
| **Local (Dev)** | Unit + Integration (dev loop) | Docker Compose (db, back) | Fixtures / Seed dev | Equipe | Sob demanda |
| **CI (GitHub Actions)** | Unit + Integration + SAST/SCA/Secrets + Lint | Ubuntu-latest + PostgreSQL service + Testcontainers | Fixtures / Seed CI | Público (logs) | Todo push |
| **Staging (Preview)** | E2E + DAST + Performance + UAT | Docker Compose completo (db, back, front, proxy) + Tailscale | Seed realístico (anonimizado) | Equipe + Stakeholders | Por PR / Diário |
| **Produção** | Smoke tests pós-deploy / Monitoramento | Docker Compose + Nginx + Tailscale | Dados reais | Restrito | N/A |

---

## 5. DADOS DE TESTE (Test Data Management)

| Tipo | Estratégia | Ferramenta | Responsável |
|---|---|---|---|
| **Fixtures Unitárias** | Factories (factory_boy / pytest-factoryboy) | `tests/factories/` | agent-qa-sdet |
| **Seed Integração/E2E** | Scripts SQL determinísticos + Alembic | `tests/seed/` + `alembic` | agent-dba |
| **Dados Sensíveis (PII)** | **NUNCA** dados reais — usar Faker / sintético | `faker` library | agent-compliance-governance |
| **LGPD** | Dados de teste têm "direito ao esquecimento" — cleanup automático | Transação rollback / truncate | agent-qa-sdet |

---

## 6. CRONOGRAMA DE TESTES (Test Schedule) — Por Wave/Marco

| Wave / Marco | Fases de Teste | Início | Fim | Critério de Saída (Exit Criteria) |
|---|---|---|---|---|
| **M1 (Base MVP)** | Unit → Integration → E2E (simulador, invoice) → Perf baseline → Security baseline | 2026-09-XX | 2026-10-XX | Gate 2: Test Plan aprovado; Gate 3: All quality gates green |
| **M2 (Identidade)** | Unit (auth) → Integration (login/session) → E2E (multiusuário) → Security (Argon2id, HMAC) | 2026-11-XX | 2026-11-XX | Gate 2/3 por wave |
| **M3 (Prestadora/Cliente)** | Unit → Integration → E2E (CRUDs) | 2026-11-XX | 2026-12-XX | Gate 2/3 por wave |
| **M4 (Histórico/Privacidade)** | Unit → Integration → E2E → LGPD Compliance → Pen Test → Perf Soak | 2026-12-XX | 2026-12-15 | Gate 3 Final: All gates green + UAT signed off |

---

## 7. RECURSOS E RESPONSABILIDADES (RACI)

| Atividade | QA/SDET | Backend Dev | Frontend Dev | DevOps | Architect | DBA | Security | GP/CCB |
|---|---|---|---|---|---|---|---|---|
| Escrever Test Plan | **R/A** | C | C | C | C | C | C | I |
| Criar Testes Unitários | C | **R/A** | **R/A** | I | C | I | I | I |
| Criar Testes Integração | **R/A** | **R** | C | C | C | **R** | I | I |
| Criar Testes E2E | **R/A** | C | **R** | C | C | C | I | I |
| Criar Testes Performance | **R/A** | C | I | **R** | C | C | I | I |
| Criar Testes Segurança | C | C | I | C | C | I | **R/A** | I |
| Executar CI/CD | I | I | I | **R/A** | I | I | C | I |
| Analisar Resultados | **R/A** | C | C | C | C | C | C | I |
| Aprovar Gate 2/3 | C | C | C | C | C | C | C | **R/A** |
| Manter Test Data | **R/A** | C | I | C | I | **R** | I | I |

---

## 8. ENTREGÁVEIS DE TESTE (Test Deliverables)

| Entregável | Formato | Frequência | Destino | Validação |
|---|---|---|---|---|
| **Test Plan (este doc)** | Markdown | Por wave / Marco | `docs/planos/plan-test-plan.md` | Gate 2 CCB |
| **Test Cases / Scripts** | Gherkin (.feature) + Python | Por feature | `tests/` + `docs/planos/test-cases/` | Code Review |
| **Test Execution Report** | Markdown + JSON (pytest) | Por execução CI | GitHub Actions Artifacts / `docs/relatorios/test-reports/` | QA Review |
| **Coverage Report** | HTML + XML (cobertura) | Por execução CI | Codecov / GitHub Actions | Gate: ≥ 80% |
| **Security Scan Report** | SARIF / JSON | Por execução CI | GitHub Security Tab / `docs/auditorias/` | Gate: 0 High/Crit |
| **Performance Report** | Markdown + Gráficos | Gate 3 + Nightly | `docs/relatorios/rel-performance-YYYYMMDD.md` | QA + Architect |
| **UAT Report** | Markdown + Evidências | Gate 3 + Pós-release | `docs/uat/rodada-NNN/` | GP + Stakeholders |
| **Defect/Bug Report** | GitHub Issues (labels: bug, severity) | Contínuo | GitHub Issues | Triage semanal |
| **RTM Atualizado** | Markdown + CSV | Por Spec/CR | `docs/planos/plan-rtm.md` | QA + Analyst |

---

## 9. RISCOS E MITIGAÇÕES (Test Risks)

| Risco | Prob. | Impacto | Mitigação | Dono |
|---|---|---|---|---|
| Flakiness em testes E2E (timing, rede) | Alta | Médio | Retry logic; timeouts generosos; testar em staging estável; isolar flaky | agent-qa-sdet |
| Cobertura < 80% em código legado | Média | Alto | Refator gradual com testes; "boy scout rule"; meta incremental por wave | agent-backend-dev / agent-qa-sdet |
| Falso positivo/negativo em security scans | Média | Médio | Baseline de suprimidos documentados; revisão manual semanal | agent-digital-security |
| Dependência de API externa (Frankfurter/PTAX) nos testes | Baixa | Alto | **Mock obrigatório** em CI; contract tests opcionais | agent-backend-dev |
| Performance degradada não pega no CI | Média | Alto | Benchmark automatizado no CI (threshold P95); alerta se regressão > 10% | agent-qa-sdet / agent-devops |

---

## 10. APROVAÇÃO E CONTROLE DE VERSÕES

| Versão | Data | Autor | Mudança | Aprovação (CCB) |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-qa-sdet | Criação inicial (template aprovado) | GP (CCB) |
| 1.1.0 | YYYY-MM-DD | Nome | Atualização para Wave M2/M3/M4 | |

---

> **Regra de Ouro**: **Teste não é fase — é atividade contínua**. Todo commit roda Unit+Integration+SAST/SCA. Todo PR roda E2E+Performance+DAST. Gate 3 = All Gates Green + UAT Signed Off.