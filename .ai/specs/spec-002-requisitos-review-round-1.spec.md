---
id: ai-specs-spec-002-requisitos-review-round-1-spec
title: SPEC spec-002 — requisitos-review-round-1 — Requisitos REVIEW — ROUND 1 (WS-3 · COGME)
type: spec
version: 2.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- constitution.md v1.3.0 (Art. 1.2 escopo multiusuário, P-14/P-15)
- docs/decisoes/ccb-CR-002.md (CR2-D01, D07, D08 ratificadas)
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-01..07)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md v1.0.0 (original)
- .ai/specs/spec-017-identity-access-session-v1.spec.md (identidade/sessão)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md (lifecycle/privacy)
last-revised: '2026-11-15'
lgpd-class: n/a
tags:
- specs
- docs
- adequado-a-norma
- requisitos
- review
- multiusuario
---
---
spec_id: spec-002
specname: requisitos-review-round-1
version: 2.0.0
status: ratificada
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-10-23
updated: 2026-11-15
origin: WS-3 · COGME · Requisitos Review Round 1 (emenda constitucional E-20 + CR-002)
task: TA-0031 | sender: agent-project-analyst | kill_switch: inherited
trace:
  - constitution.md v1.3.0 (E-20: escopo multiusuário, M4→30/12, P-14/P-15)
  - docs/decisoes/ccb-CR-002.md (CR2-D01, D07, D08 ratificadas)
  - docs/decisoes/ccb-lgpd-decisoes.md (DEC-01..07)
  - .ai/specs/spec-017-identity-access-session-v1.spec.md
  - .ai/specs/spec-022-account-lifecycle-privacy-v1.spec.md
  - LGPD Lei 13.709/2018 (art. 7º V, 16, 18)
lgpd-class: n/a
---

# SPEC spec-002 — requisitos-review-round-1 — Requisitos REVIEW — ROUND 1 (WS-3 · COGME)

**Status: RATIFICADA v2.0.0** — Emenda constitucional E-20 + CR-002: **OS-01 REVOGADA**, user stories multiusuário adicionadas, requisitos LGPD integrados.

---

## 1. Contexto e origem

Esta spec v2.0.0 emenda a spec-002 original (v1.0.0, 2026-10-23) para incorporar:
- **Emenda Constitucional E-20** (constitution.md v1.3.0): escopo expandido para identidade, contas multiusuário, prestadora/banco, clientes, histórico, invoice bilíngue, lifecycle conta
- **CR-002 Gates A/B/C/D ratificados** (docs/decisoes/ccb-CR-002.md): decisões CR2-D01..D09
- **Decisões LGPD** (docs/decisoes/ccb-lgpd-decisoes.md): DEC-01..07 ratificadas
- **Specs derivadas ratificadas**: SPEC-017 (identidade/sessão), SPEC-022 (lifecycle/privacy), SPEC-018/019/020/021

**Mudança principal:** **OS-01 (autenticação/multiusuário) REVOGADA** — era "fora de escopo", agora é **REQ-16/REQ-17** (dentro do escopo canônico Art. 1.2 v1.3.0).

---

## 2. Resolução de conflitos

| Tema | Decisão v2.0.0 | Fonte vencedora | Texto superado |
|------|----------------|-----------------|----------------|
| **OS-01 Autenticação/Multiusuário** | **REVOGADA** — agora REQ-16 (Identidade/Sessão) + REQ-17 (Histórico/Invoices) | Constitution v1.3.0 Art. 1.2 (E-20) + CR-002 CR2-D01 | spec-002 v1.0 §4.1: "OS-01: Autenticação e cadastro multiusuário — FORA DE ESCOPO" |
| **Base legal LGPD** | **art. 7º V** (execução contrato) para todos dados invoice (emitente + cliente) | DEC-01/02 (ccb-lgpd-decisoes.md) | Não definido anteriormente |
| **Inventário mínimo invoice** | Endereço/bancários **NULLable** (minimização art. 6º III) | DEC-03 | spec-007 v1.0 campos obrigatórios |
| **Retenção invoices** | **5 anos + 6 meses** + anonimização irreversível + erase hard | DEC-04 | spec-004:126 "invoice nunca persistida" |
| **Ciclo invoice** | **draft/editável** ↔ **finalized/imutável** + **clone** (novo draft + supersedes_invoice_id) | DEC-05 | Não existia |
| **Numeração** | **INV-{YYYYMM}-{SEQ:04d}** por emissor/mês (tabela invoice_sequences) | DEC-06 | Não definida |
| **Bilíngue** | **client_country_code → locale**: `BR`→pt-BR, demais→en; templates separados | DEC-07 | OS-02 i18n integral "fora de escopo" |

---

## 3. Requisitos Funcionais (RF) — Atualizados

### 3.1 Requisitos Originais (Mantidos)

| ID | Requisito | Descrição | Origem |
|----|-----------|-----------|--------|
| **REQ-01** | Simulação Cambial Tempo Real | USD/EUR→BRL com cotação PTAX/Frankfurter, spread/IOF configuráveis | WS-3 |
| **REQ-02** | 5 Regimes de Contratação | Hora, dia, semana, mês, valor fixo — todos operacionais em UAT | WS-3 |
| **REQ-03** | Encargos Spread + IOF | Cálculo com 2 casas decimais, auditoria de valores | WS-3 |
| **REQ-04** | Emissão Invoice PDF | Template profissional, dados completos, notice legal | WS-3 |
| **REQ-05** | Cotação com Fonte/Boletim | PTAX primário, Frankfurter fallback; stale > 24h | WS-3 |
| **REQ-06** | Interface Web Responsiva | 100% FOSS, HTML5/CSS3/JS vanilla, mobile-first | WS-3 |
| **REQ-07** | Cache Cotações | Reduz chamadas API; TTL configurável | WS-3 |
| **REQ-08** | Cobertura ≥ 80% | CI bloqueia merge se coverage < 80% | WS-3 |
| **REQ-09** | UAT Produto | 7 fluxos críticos (UAT-01..07) + casos camada | WS-3 |
| **REQ-10** | Qualidade PDCA + Ishikawa | 12 PDCAs + 6M para defeitos críticos | WS-3 |
| **REQ-11** | CI/CD Pipeline | Lint + testes ≤ 5 min/push; falha bloqueia merge | WS-3 |
| **REQ-12** | Rastreabilidade Prompts SDD | 100% handoffs catalogados em .ai/handoffs/ | WS-3 |
| **REQ-13** | Documentação Técnica | Arquitetura + revisão/aprovação OpenAPI | WS-3 |
| **REQ-14** | Runtime Agentes CI | Camadas L1/L3 como containers (Art. 10.1) | WS-3 |
| **REQ-15** | LGPD Produto (Condicional) | Critérios LGPD sujeitos a ratificação CCB | WS-3 |

### 3.2 Novos Requisitos (CR-002 / E-20)

| ID | Requisito | Descrição | Specs Derivadas | Critérios de Aceite |
|----|-----------|-----------|-----------------|---------------------|
| **REQ-16** | **Identidade, Autenticação e Sessão Multiusuário** | Cadastro, login (email/CPF/CNPJ), logout, reset senha (TTL 1h, SMTP local), sessão individual regenerada, aliases HMAC anti-enumeração, Argon2id (m=19456,t=2,p=1), rate limits, CSRF, require_owner middleware | SPEC-017, SPEC-022 | AC-01..AC-11 (SPEC-017) + ST-01..ST-10 (ADR-019) |
| **REQ-17** | **Perfil Prestadora, Contas Bancárias, Clientes, Histórico, Invoice Bilíngue, Lifecycle** | Perfil MEI/PJ (CNPJ obrigatório PJ), contas criptografadas (pgcrypto), 1 primária; clientes ativo/inativo + fictício exige country_code; simulações opt-in + snapshot cotação; invoice draft/finalized/clone + numeração INV-{YYYYMM}-{SEQ}; bilíngue BR→pt-BR/demais→en; lifecycle active/dormant(180d)/erase + retenção 5a+6m + anonimização | SPEC-018, 019, 020, 021, 022 | ACs respectivos de cada spec |
| **REQ-18** | **LGPD/GDPR por Design em Dados de Produto** | Base legal art. 7º V; minimização (endereço/bancários NULLable); logs sem PII/valores/corpo; rota erase operante; ROPA simplificado; `lgpd-class` em specs; GDPR art. 6.1.b se oferta EEE/UK | SPEC-015 (v0.3.0 ratificada), SPEC-022 | CP-1..CP-5 (SPEC-015) + AC-01..AC-10 (SPEC-022) |

---

## 4. User Stories (US) — Atualizadas

### 4.1 US Originais (Mantidas)

| ID | User Story | Critérios de Aceite | REQ |
|----|------------|---------------------|-----|
| **US-001** | Como usuário, quero simular conversão USD/EUR→BRL em tempo real para saber o valor líquido | Cotação PTAX/Frankfurter; spread/IOF 2 casas; resultado imediato | REQ-01, REQ-03, REQ-05 |
| **US-002** | Como usuário, quero escolher entre 5 regimes de contratação para calcular minha jornada | Hora, dia, semana, mês, fixo — todos calculam corretamente | REQ-02 |
| **US-003** | Como usuário, quero ver spread e IOF detalhados com 2 casas decimais para auditar valores | Valores corretos; breakdown visível | REQ-03 |
| **US-004** | Como usuário, quero emitir invoice PDF profissional para enviar ao cliente | Template completo; notice legal; download automático | REQ-04 |
| **US-005** | Como usuário, quero interface responsiva em mobile/desktop para acessar de qualquer dispositivo | 375/768/1024/1440px sem scroll horizontal; touch 44×44px | REQ-06 |
| **US-006** | Como usuário, quero cache de cotações para reduzir latência e chamadas API | TTL configurável; stale badge se > 24h | REQ-05, REQ-07 |
| **US-007** | Como usuário, quero cobertura de testes ≥ 80% para confiar no sistema | CI bloqueia merge < 80%; relatório coverage | REQ-08 |
| **US-008** | Como stakeholder, quero UAT de 7 fluxos críticos validados | UAT-01..07 PASS; casos camada PASS | REQ-09 |

### 4.2 Novas User Stories (CR-002 / REQ-16, REQ-17)

| ID | User Story | Critérios de Aceite | REQ | Spec |
|----|------------|---------------------|-----|------|
| **US-016** | Como usuário, quero criar minha conta (email/CPF/CNPJ), fazer login, resetar senha e ter sessão segura para acessar meus dados isolados | Cadastro valida CPF/CNPJ/email; login aceita 3 identificadores; reset TTL 1h email SMTP local; sessão regenerada HttpOnly/Secure/SameSite; Argon2id; rate limits | REQ-16 | SPEC-017 |
| **US-017** | Como usuário, quero salvar simulações (opt-in), ver histórico, gerar invoices draft/finalized/clonar, cadastrar prestadora/banco/clientes para ter histórico completo | Simulação salva opt-in; histórico paginado; invoice draft editável, finalized imutável, clone novo draft; numeração INV-{YYYYMM}-{SEQ}; prestadora MEI/PJ, banco criptografado, clientes ativo/inativo + fictício | REQ-17 | SPEC-018, 019, 020 |
| **US-018** | Como usuário, quero invoice em português (cliente BR) ou inglês (cliente estrangeiro) para enviar ao cliente no idioma correto | Regra client_country_code: BR→pt-BR, demais→en; fictício exige país; templates separados; locale snapshoteado imutável | REQ-17 | SPEC-021 |
| **US-019** | Como usuário, quero minha conta ficar dormente após 180 dias sem login e poder reativar com reset+verificação, ou excluir definitivamente com erase LGPD | Dormência 180d revoga sessões/bloqueia criações; reativação = reset+verificação; exclusão = hard delete + invoices 5a+6m anonimização; logs sem PII | REQ-17 + REQ-18 | SPEC-022 |
| **US-020** | Como usuário, quero que meus dados (CPF, banco, endereço) sejam coletados só se necessário, não vazem em logs, e eu possa solicitar eliminação completa | Minimização: endereço/banco NULLable; logs sanitizados (CP-2); erase rota DELETE + anonimização 5a+6m; ROPA art. 7º V | REQ-18 | SPEC-015, SPEC-022 |

---

## 5. Requisitos Não Funcionais (RNF) — Atualizados

| ID | RNF | Descrição | Spec/ADR |
|----|-----|-----------|----------|
| **RNF-01** | Performance | Simulação < 500ms (cache hit); login < 1s; PDF < 3s | SPEC-006, ADR-018 |
| **RNF-02** | Segurança | OWASP ASVS L1/L2; Argon2id; HMAC aliases; CSRF; rate limits; fail-closed | ADR-017, ADR-019, SPEC-017 |
| **RNF-03** | Privacidade | LGPD art. 7º V base; minimização; erase art. 18; logs sem PII; soberania local | SPEC-015, SPEC-022, Constitution P-15 |
| **RNF-04** | Disponibilidade | Single-instance local; health checks; rollback migrações | ADR-018, ADR-010 |
| **RNF-05** | Manutenibilidade | Cobertura ≥ 80%; docs técnicas; rastreabilidade handoffs | REQ-08, REQ-12, REQ-13 |
| **RNF-06** | Portabilidade | Stack FOSS (Python, PostgreSQL, Docker, Nginx); zero vendor lock-in | P-01, ADR-010 |
| **RNF-07** | Auditoria | Lifecycle events imutáveis; snapshots invoice; numeração sequencial por emissor | SPEC-020, SPEC-022, DEC-06 |

---

## 6. Fora de Escopo (YAGNI) — Atualizado

| Item | Justificativa |
|------|---------------|
| OAuth, SSO, MFA, federação identidade | Fora MVP; REQ-16 cobre auth local |
| Equipes, organizações, papéis admin, painel admin | Single-user por conta |
| NF-e/NFS-e, numeração fiscal oficial, envio automático email | CR-006 futuro |
| i18n integral interface/erros | Apenas invoice bilíngue (REQ-17/US-018) |
| Integração plataformas pagamento/transferência, Pix automático | Fora escopo |
| Múltiplas sessões simultâneas, expiração forçada senha | Fora MVP |
| Portal do cliente, área logada cliente | Fora single-user |
| Telemetria, rastreio, analytics | P-03 proibido |
| Cloud não autorizada para PII/sessão/email | P-03, Bypass Protocol |

---

## 7. Rastreabilidade

| REQ/US | Specs Derivadas | ADRs | Decisões CCB | Testes |
|--------|-----------------|------|--------------|--------|
| REQ-01..15 | Specs 004, 005, 006, 008, 009, 010, 011, 012, 013, 014 | ADR-001..016 | CCB-CR-002 (parcial) | UAT-01..09, ST-01..10 |
| **REQ-16** | **SPEC-017, SPEC-022** | **ADR-017, ADR-019** | **CR2-D01, D06, D09** | **AC-01..11, ST-01..10** |
| **REQ-17** | **SPEC-018, 019, 020, 021, 022** | **ADR-018, ADR-019** | **CR2-D02..D08** | **ACs specs 018-022** |
| **REQ-18** | **SPEC-015 (v0.3.0), SPEC-022** | **ADR-016 (D4)** | **CR2-D02, D03, D04** | **CP-1..5, AC-01..10** |

---

## 8. Critérios de Aceite Globais (v2.0.0)

- [ ] **OS-01 REVOGADA** — autenticação/multiusuário agora REQ-16/17 dentro do escopo
- [ ] **REQ-16, REQ-17, REQ-18** adicionados e ratificados
- [ ] **US-016..US-020** adicionadas com ACs rastreáveis às specs 017-022
- [ ] **LGPD/GDPR por design** — base legal art. 7º V, minimização, erase, ROPA, logs sem PII
- [ ] **Numeração invoice** INV-{YYYYMM}-{SEQ:04d} por emissor/mês implementada
- [ ] **Bilíngue** client_country_code → locale (BR→pt-BR, demais→en) funcional
- [ ] **Lifecycle conta** active/dormant(180d)/erase com retenção 5a+6m + anonimização
- [ ] **Todas specs 017-022 ratificadas** e emendas 002/004/007/008/015 validadas

---

## 9. Metadados da Emenda

- **Avaliador primário:** `agent-sdd-specialist` + `agent-project-analyst`
- **Ratificação:** CCB/GP via CR-002 + Emenda E-20 (2026-11-14/15)
- **Emenda:** v1.0.0 → v2.0.0 (MAJOR por escopo + OS-01 revogada)
- **parcel.dod:** true
- **Data da emenda:** 2026-11-15
- **Status da spec:** ativa / ratificada

---

## CHANGELOG

| Versão | Data | Task/Handoff | Mudança |
|--------|------|--------------|---------|
| 1.0.0 | 2026-10-23 | WS-3 / agent-project-analyst | Emissão original: REQ-01..15, US-001..008, OS-01 fora escopo, LGPD condicional |
| 2.0.0 | 2026-11-15 | CR-002 Onda 1 / agent-sdd-specialist | **Emenda E-20 + CR-002**: OS-01 REVOGADA; REQ-16/17/18 + US-016..20 adicionados; LGPD ratificada (DEC-01..07); numeração, bilíngue, lifecycle, LGPD por design integrados; specs 017-022 referenciadas |

---

## CAMADAS FUNDAMENTAIS — MAPA (TA-0031)

| Camada | Seção nesta spec | Estado |
|--------|------------------|--------|
| (a) cabeçalho | frontmatter (`spec_id: spec-002`, `version: 2.0.0`, `status: ratificada`) | aplicada |
| (b) Contexto/origem | §1 + frontmatter `origin`/`task` | aplicada |
| (c) Resolução de conflitos | §2 (8 conflitos resolvidos incl. OS-01 revogada) | aplicada |
| (d) Corpo de decisões/requisitos/contratos | §3 (RF originais + novos), §4 (US originais + novas), §5 (RNF atualizados) | aplicada |
| (e) Critérios de aceite/testes | §8 (globais) + specs 017-022 ACs | aplicada |
| (f) Rastreabilidade | §7 (tabela REQ→Specs→ADRs→CCB→Testes) | aplicada |
| (g) Fora de escopo (YAGNI) | §6 (atualizado) | aplicada |
| (h) Changelog | CHANGELOG | aplicada |