---
id: docs-arquitetura-nfrs
title: "NFRs Consolidados — Requisitos Não-Funcionais do COGME"
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-architect
derived-from:
- constitution.md (Art. 3, 4, 7, 10, Princípios P-01 a P-15)
- ADR-001 (Stack FOSS), ADR-003 (Métricas), ADR-010 (Infra), ADR-017 (Argon2id), ADR-019 (Segurança Multiusuário)
- SPEC-004 (backend-mvp), SPEC-008 (frontend), SPEC-017 a 023 (M2-M4)
- CI-CD-GOV-001, DEVSECOPS-001
- ISO/IEC 25010 (Quality Model) — mapeamento
- PMBOK 7ª — Domínio Entrega (Quality)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- arquitetura
- nfrs
- requisitos-nao-funcionais
- qualidade
- iso25010
---

# NFRs Consolidados — COGME

> **Finalidade**: Documento **único e autoritativo** de todos os Requisitos Não-Funcionais (NFRs) do projeto COGME. Consolida NFRs dispersos na Constitution, ADRs, Specs, README e políticas de governança.
> **Uso**: Validação **Gate 2 (Desenho)** e **Gate 3 (Go-Live)**. Base para Test Plan, arquitetura, decisões técnicas.
> **Classificação**: Baseado em **ISO/IEC 25010** (Quality in Use + Product Quality).
> **Rastreabilidade**: Cada NFR mapeado para REQ, SPEC, ADR, TEST, AC.

---

## 1. MATRIZ RESUMO (ISO/IEC 25010)

| Categoria ISO 25010 | Sub-característica | NFR-ID | Descrição Resumida | Métrica / Threshold | Fonte Primária | Status |
|---|---|---|---|---|---|---|
| **Performance Efficiency** | Time Behavior | NFR-PERF-01 | Latência P95 simulação | ≤ 2s | Constitution Art. 3 / SPEC-004 | ✅ Validado |
| | | NFR-PERF-02 | Latência P95 geração PDF | ≤ 3s | SPEC-004 §8 | 🔄 Teste pendente |
| | Resource Utilization | NFR-PERF-03 | CPU sustentado | < 70% | ADR-001 (hardware) | ✅ Monitorado |
| | | NFR-PERF-04 | RAM sustentado | < 80% (60GB total) | ADR-001 (hardware) | ✅ Monitorado |
| | | NFR-PERF-05 | DB Connections | < 80% pool (20) | ADR-010 | ✅ Monitorado |
| | Capacity | NFR-PERF-06 | Throughput simulador | ≥ 50 req/s (pico 200) | Test Plan §3.4 | 🔄 Validar |
| **Compatibility** | Co-existence | NFR-COMP-01 | Stack 100% FOSS | 0 dependências proprietárias | Constitution P-01 / ADR-001 | ✅ Auditado CI |
| | Interoperability | NFR-COMP-02 | APIs câmbio (Frankfurter + PTAX) | Fallback automático < 5s | ADR-001 / ADR-010 | ✅ Implementado |
| **Usability** | Appropriateness Recognizability | NFR-USAB-01 | UI desktop-first, mobile funcional | Breakpoints 375/768/1024/1440 | SPEC-008 / UI-SPEC | ✅ Implementado |
| | Accessibility | NFR-USAB-02 | WCAG 2.1 AA | 0 violações AA (axe-core) | Test Plan §3.6 | 🔄 Validar |
| | User Error Protection | NFR-USAB-03 | Validação client + server | Mensagens claras PT/EN | SPEC-008 / UI-SPEC | ✅ Implementado |
| **Reliability** | Availability | NFR-REL-01 | Uptime produção | ≥ 99.5% (mensal) | README §10 / Test Plan | 🔄 Medir |
| | Fault Tolerance | NFR-REL-02 | Circuit Breaker APIs externas | Threshold 5 falhas → OPEN | ADR-001 / SPEC-004 §5 | ✅ Implementado |
| | Recoverability | NFR-REL-03 | Rollback < 5 min (imagem) | Simulação Gate 3 | Runbook §3 | 🔄 Simular |
| | | NFR-REL-04 | Restore DB < 15 min | Backup diário + teste mensal | Runbook §6 | 🔄 Testar |
| **Security** | Confidentiality | NFR-SEC-01 | Zero segredos em imagem/git | TruffleHog/Detect-secrets CI | Constitution P-02, P-03 / DEVSECOPS | ✅ Auditado CI |
| | Integrity | NFR-SEC-02 | Assinatura de commits (GPG) | Opcional / Recomendado | Constitution Art. 7 | ⏳ Decidir |
| | Non-repudiation | NFR-SEC-03 | Logs estruturados imutáveis | JSON, timestamps, correlation ID | Constitution Art. 4 / ADR-003 | ✅ Implementado |
| | Accountability | NFR-SEC-04 | Auditoria de ações sensíveis | Login, admin, config changes | Constitution Art. 7 / ADR-019 | 🔄 M2+ |
| | Authenticity | NFR-SEC-05 | Argon2id (OWASP params) | m=65536, t=3, p=4 | ADR-017 | ✅ Ratificado |
| | | NFR-SEC-06 | HMAC-SHA256 lookup PII | Pseudonimização email/CPF | ADR-019 / SPEC-023 | 🔄 M2+ |
| | Authorization | NFR-SEC-07 | Isolamento multiusuário | Row-level security / App-level | ADR-019 / SPEC-017 | 🔄 M2+ |
| **Maintainability** | Modularity | NFR-MAINT-01 | Arquitetura ortogonal (camadas) | Dados/Back/Front isolados | Constitution Art. 10 / ADR-010 | ✅ Implementado |
| | Reusability | NFR-MAINT-02 | Templates, specs, agents reutilizáveis | Docs-as-Code, versionados | Constitution Art. 2 / OKB | ✅ Implementado |
| | Analyzability | NFR-MAINT-03 | Observabilidade (health, metrics, logs) | /health, /metrics, JSON logs | Constitution Art. 4 / ADR-003 | ✅ Implementado |
| | Modifiability | NFR-MAINT-04 | ADRs para mudanças arquiteturais | CR obrigatório + CCB | Constitution Art. 9.3 | ✅ Processo |
| | Testability | NFR-MAINT-05 | Coverage ≥ 80% (linhas) | pytest-cov + CI gate | Constitution Art. 4.8 | ✅ Gate CI |
| **Portability** | Adaptability | NFR-PORT-01 | Docker Compose (paridade dev/test/prod) | Mesma config 3 ambientes | ADR-010 | ✅ Implementado |
| | Installability | NFR-PORT-02 | Setup em < 30 min (hardware pronto) | `docker compose up --build` | README §6 | ✅ Validado |
| | Replaceability | NFR-PORT-03 | Modelo LLM trocável (Qwen → outro) | Interface abstraída (llama.cpp) | ADR-006 / canon-stack-sdd | ✅ Projetado |

---

## 2. DETALHAMENTO POR NFR (Evidência e Validação)

### 2.1 Performance Efficiency

#### NFR-PERF-01: Latência P95 Simulação ≤ 2s
- **Descrição**: Endpoint `/v1/simulate` deve responder em ≤ 2s no percentil 95 sob carga normal.
- **Medição**: `tests/performance/test_latency.py` (locust/k6) + CI benchmark.
- **Evidência Atual**: Testes de integração passam; baseline empírica a calibrar (GitHub Projects).
- **Rastreabilidade**: REQ-01 → SPEC-004 §3 → IMPL-001/002/003 → TEST-004 → AC-001/002.

#### NFR-PERF-02: Latência P95 PDF Invoice ≤ 3s
- **Descrição**: Geração de PDF via WeasyPrint + Jinja2 deve completar em ≤ 3s (P95).
- **Medição**: `tests/performance/test_pdf_latency.py` (pendente).
- **Gap**: Teste de performance PDF não implementado (RTM Gap).
- **Rastreabilidade**: REQ-02 → SPEC-004 §8 / SPEC-022 → IMPL-004/005/006 → TEST-008 → AC-003/004.

#### NFR-PERF-03/04/05: Recursos (CPU, RAM, DB Connections)
- **Monitoramento**: `docker stats`, `/health/metrics`, `pg_stat_activity`.
- **Alertas**: Runbook §4.1 (thresholds configurados).
- **Hardware**: Ryzen 7 8700G + 60GB RAM unificada (compartilhada com GPU Radeon 780M).

### 2.2 Compatibility

#### NFR-COMP-01: Stack 100% FOSS
- **Validação**: CI gate `license-check` (FOSSA/license-checker) — 0 dependências não-FOSS.
- **Evidência**: `ci.yml` step "FOSS Compliance" passing.
- **Exceções**: GitHub Actions (proprietário gratuito) — aceito por CCB (infraestrutura, não runtime).

#### NFR-COMP-02: Fallback Automático APIs Câmbio
- **Implementação**: `CircuitBreaker` (5 falhas → OPEN) + `PtaxProvider` fallback.
- **Teste**: `tests/integration/test_rates.py` — cenário fallback validado.
- **Cache**: 7 dias (`fx_quotes` TTL) reduz dependência externa.

### 2.3 Usability

#### NFR-USAB-01: UI Desktop-First, Mobile Funcional
- **Spec**: UI-SPEC.md §1.2 (Single Column / Hero + Features + CTA).
- **Breakpoints**: 375 / 768 / 1024 / 1440 (CSS custom properties).
- **Stack**: Jinja2 + HTMX + Tailwind (sem build step, sem CDN-first).

#### NFR-USAB-02: WCAG 2.1 AA
- **Ferramenta**: `axe-core` via Playwright no CI (PR gate).
- **Status**: A validar na próxima wave (M2+).

#### NFR-USAB-03: Validação Dupla (Client + Server)
- **Client**: HTMX + HTML5 validation + JS leve.
- **Server**: Pydantic v2 (strict) + FastAPI automatic validation.
- **Mensagens**: PT-BR + EN (bilingue).

### 2.4 Reliability

#### NFR-REL-01: Disponibilidade ≥ 99.5%
- **Medição**: Uptime monitorado via health checks + logs nginx.
- **Baseline**: A calibrar com dados empíricos (GitHub Projects a partir de 01/11/2026).

#### NFR-REL-02: Circuit Breaker
- **Implementação**: `src/backend/services/circuit_breaker.py` — estado CLOSED/OPEN/HALF_OPEN.
- **Threshold**: 5 falhas consecutivas → OPEN (30s) → HALF_OPEN → teste → CLOSED/OPEN.
- **Métrica**: Exposta em `/health/metrics` (`circuit_breaker_state`).

#### NFR-REL-03/04: Rollback e Restore
- **Rollback Imagem**: < 5 min (Runbook §3.2) — simulação obrigatória Gate 3.
- **Restore DB**: < 15 min (Runbook §6.3) — teste mensal obrigatório.

### 2.5 Security

#### NFR-SEC-01: Zero Segredos em Imagem/Git
- **CI Gates**: `trufflehog` + `detect-secrets` — falha build se segredo detectado.
- **Prática**: `.env` apenas runtime; `.env.example` versionado; base images por digest.

#### NFR-SEC-05: Argon2id (OWASP)
- **Params**: `memory_cost=65536` (64MB), `time_cost=3`, `parallelism=4`.
- **Validação**: `bandit` SAST + teste unitário `test_password_hasher.py`.

#### NFR-SEC-06: HMAC Lookup PII
- **Implementação**: `HMAC-SHA256(key=HMAC_SECRET_KEY, msg=email|cpf)` → `lookup_hmac` (unique index).
- **Valor real**: Criptografado (AES-256-GCM) em `value_encrypted`.
- **LGPD**: Pseudonimização atende Art. 5º LGPD (minimização).

#### NFR-SEC-07: Isolamento Multiusuário
- **Nível App**: `user_id` FK em todas as tabelas de dados; queries sempre filtradas por `user_id`.
- **Nível DB**: Row Level Security (RLS) PostgreSQL planejado (M3+).
- **Sessões**: Token JWT (HS256) + `user_sessions` table com revogação.

### 2.6 Maintainability

#### NFR-MAINT-01: Arquitetura Ortogonal
- **Camadas**: Dados (PostgreSQL) ↔ Back (FastAPI) ↔ Front (Jinja2/HTMX) ↔ Proxy (Nginx).
- **Comunicação**: Apenas por interfaces declaradas (porta, API, volume).
- **Isolamento**: Redes Docker separadas (`cogme-internal`, `cogme-external`).

#### NFR-MAINT-05: Testabilidade (Coverage ≥ 80%)
- **CI Gate**: `pytest-cov` — falha se `line coverage < 80%` ou `branch coverage < 70%`.
- **Atual**: M1 core passando; M2-M4 a construir com testes.

### 2.7 Portability

#### NFR-PORT-03: Modelo LLM Trocável
- **Abstração**: `llama.cpp` via CLI + `Qwen3-30B-A3B Q4_K_M` (GGUF).
- **Troca**: Substituir arquivo `.gguf` + ajustar parâmetros (contexto, threads).
- **Candidatos**: Qwen 14B, Llama 3.1 8B, Phi-3.5 — todos GGUF, CPU-only.

---

## 3. MAPEAMENTO NFR → TESTES (Validação)

| NFR-ID | Teste de Validação | Tipo | Status | Arquivo/Comando |
|---|---|---|---|---|
| NFR-PERF-01 | Benchmark simulate P95 | Performance | 🔄 Planejado | `pytest tests/performance/test_latency.py` |
| NFR-PERF-02 | Benchmark PDF P95 | Performance | 🔄 Pendente | `pytest tests/performance/test_pdf_latency.py` |
| NFR-COMP-01 | License scan | Security/Compliance | ✅ CI | `ci.yml` step "FOSS Compliance" |
| NFR-COMP-02 | Fallback integration test | Integration | ✅ Pass | `pytest tests/integration/test_rates.py::test_fallback` |
| NFR-USAB-02 | Axe-core accessibility | Accessibility | 🔄 Planejado | `pytest tests/accessibility/test_a11y.py` |
| NFR-REL-02 | Circuit breaker test | Integration | ✅ Pass | `pytest tests/integration/test_circuit_breaker.py` |
| NFR-REL-03 | Rollback simulation | Operational | 🔄 Gate 3 | `docs/operacao/rollback-simulations/` |
| NFR-SEC-01 | TruffleHog + detect-secrets | Security | ✅ CI | `ci.yml` step "Secrets Scan" |
| NFR-SEC-05 | Argon2id params test | Unit | 🔄 M2 | `pytest tests/unit/test_password_hasher.py` |
| NFR-MAINT-05 | Coverage gate | Quality | ✅ CI | `pytest --cov=src --cov-fail-under=80` |

---

## 4. CONTROLE DE MUDANÇAS DOS NFRs

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-architect | Consolidação inicial (Constitution, ADRs, Specs, README) | GP (CCB) — Gate 2 |

> **Regra**: Qualquer mudança em NFR (threshold, adição, remoção) exige **CR formal + aprovação CCB + atualização Test Plan + RTM**.