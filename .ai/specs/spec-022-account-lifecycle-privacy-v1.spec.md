---
id: ai-specs-spec-022-account-lifecycle-privacy-v1-spec
title: SPEC spec-022 — account-lifecycle-privacy-v1 — Ciclo de vida de conta, dormência, exclusão e privacidade LGPD/GDPR
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/decisoes/ccb-CR-002.md (CR2-D02, D03, D04, D07 ratificadas)
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-01..07)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (v0.3.0, D1-D7 ratificadas, CP-1..CP-5 executáveis)
- constitution.md v1.3.0 (Art. 1.2, P-14, P-15, Art. 7)
- docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (Gate B liberado, §13.1, §15)
- LGPD Lei 13.709/2018 (art. 4º I, 6º III, 7º V, 16, 18)
- GDPR Reg. 2016/679 (art. 6, 17, 25, 32)
last-revised: '2026-11-14'
lgpd-class: dados-pessoais
tags:
- specs
- docs
- adequado-a-norma
- lgpd
- gdpr
- lifecycle
---
---
spec_id: spec-022
specname: account-lifecycle-privacy-v1
version: 1.0.0
status: ratificada
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: CR-002 Gate B (docs/decisoes/ccb-CR-002.md, CR2-D02/D03/D04/D07) + DEC-01..07 (docs/decisoes/ccb-lgpd-decisoes.md)
task: CR-002 | sender: agent-project-analyst | kill_switch: inherited
trace:
  - docs/decisoes/ccb-CR-002.md (CR2-D02: controlador=titular/base art.7ºV; D03: retenção 5a+6m; D04: dormência 180d; D07: cenário A completo)
  - docs/decisoes/ccb-lgpd-decisoes.md (DEC-01..07: base legal, inventário, retenção/erase, draft/finalized, numeração, bilíngue)
  - .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (v0.3.0: D1 persistir+erase, D2 controlador, D3 base legal, D4 inventário, D5 logs, D6 retenção, D7 limpeza)
  - constitution.md v1.3.0 (Art. 1.2 escopo multiusuário, P-14 isolamento por proprietário, P-15 LGPD/GDPR por design, Art. 7 segurança/privacidade)
  - docs/especificacoes/spec-prop-017-conta-multiusuario.md v0.2.0 (§12.5 vereditos, §13.1 Gate B SPEC-022, §15 tabela decisões)
  - LGPD art. 4º I, 6º III, 7º V, 16, 18; GDPR art. 6, 17, 25, 32
lgpd-class: dados-pessoais
---

# SPEC spec-022 — account-lifecycle-privacy-v1 — Ciclo de vida de conta, dormência, exclusão e privacidade LGPD/GDPR

**Status: RATIFICADA** — Emissão autorizada por CCB/GP via CR-002 Gate B (2026-11-14). Decisões DE-01..07 ratificadas. Precede implementação de dados sensíveis (SPEC-017, 018, 019, 020, 021).

---

## 1. Contexto e origem

Esta spec deriva da **CR-002** (contas multiusuário), especificamente do **Gate B** (Privacidade/Lifecycle), que é pré-requisito para as demais specs (SPEC-017 a SPEC-021). Consolida as decisões LGPD/GDPR ratificadas em `docs/decisoes/ccb-lgpd-decisoes.md` (DEC-01 a DEC-07) e os critérios de produto executáveis da `spec-015` v0.3.0 (CP-1 a CP-5).

**Objetivo:** Definir regras obrigatórias para:
- Ciclo de vida da conta: `active` → `dormant` → exclusão definitiva
- Retenção e eliminação de dados (invoices, simulações, perfil, clientes, banco)
- Base legal unificada (LGPD art. 7º V / GDPR art. 6.1.b)
- Controles de privacidade por design (P-14, P-15)
- ROPA simplificado (registro de operações de tratamento)

---

## 2. Resolução de conflitos

| Tema | Decisão desta spec | Fonte vencedora | Texto superado |
|------|-------------------|-----------------|----------------|
| Base legal LGPD | **art. 7º V (execução de contrato)** — invoice carrega dados de terceiros/cliente | DEC-01/02 (ccb-lgpd-decisoes.md) | Cenário art. 4º I (exclusivamente particular) — **DESCARTADO** |
| Controlador | **Usuário titular da conta** (single-user design) | DEC-01/02; CR2-D02 | Não definido anteriormente |
| Retenção invoices | **5 anos + 6 meses** pós-última-invoice + anonimização irreversível | DEC-04; CR2-D03; spec-015 CP-3 | `spec-004:126` (invoice nunca persistida) — superado por E-20 |
| Rota erase | **DELETE hard obrigatório** + cascade órfãos + backup 30d | DEC-04; spec-015 CP-3; LGPD art. 18 | Não existia |
| Dormência | **180 dias sem login** → `dormant`; reativação = reset senha + verificação | DEC-04; CR2-D04 | Não existia |
| Inventário mínimo | **Aprova DEC-03** — endereço/bancários NULLable | DEC-03; spec-015 §3.1 | Não ratificado anteriormente |
| Numeração | **INV-{YYYYMM}-{SEQ:04d}** por emissor/mês (tabela `invoice_sequences`) | DEC-06 | Não definido |
| Bilíngue | **País→locale** (`BR`→pt-BR, demais→en); templates separados | DEC-07; CR2-D05 | Não definido |

---

## 3. Requisitos funcionais

### 3.1 Ciclo de vida da conta (`users.status`)

| Estado | Transição | Gatilho | Efeitos |
|--------|-----------|---------|---------|
| `active` | → `dormant` | 180 dias sem login (`last_login_at`) | Revoga todas sessões (`user_sessions.revoked_at = now()`); bloqueia criação/alteração de recursos (simulações, invoices, clientes, perfil, banco); mantém dados conforme retenção |
| `dormant` | → `active` | Reativação solicitada | Exige: reset de senha (fluxo `password_reset_tokens`) + verificação de identidade (email/CPF/CNPJ) |
| `active`/`dormant` | → **exclusão definitiva** | Solicitação do titular (LGPD art. 18) | Hard delete: usuários, aliases, sessões, tokens, perfil, banco, clientes, simulações, lifecycle_events. **Invoices**: retenção 5a+6m → anonimização → erase. Logs de erase auditados. |

### 3.2 Retenção e eliminação de dados

| Dado | Retenção Primária | Pós-Contrato | Eliminação |
|------|------------------|--------------|------------|
| `invoices` (finalizadas) | 5 anos (art. 206 §5º CC) | + 6 meses após última invoice do cliente | Anonimização irreversível (campos PII → hash/NULL) → hard delete |
| `simulations` | Enquanto conta ativa | 6 meses após exclusão conta | Hard delete (cascade ON DELETE) |
| `provider_profiles`, `provider_bank_accounts` | Enquanto conta ativa | Imediato na exclusão | Hard delete (dados bancários criptografados) |
| `clients` | Enquanto conta ativa | 6 meses após exclusão conta | Hard delete |
| `user_login_identifiers`, `user_sessions`, `password_reset_tokens` | Enquanto conta ativa | Imediato na exclusão | Hard delete |
| `account_lifecycle_events` | 5 anos + 6 meses | Mesmo período | Anonimização (`user_id` → hash) → hard delete |
| `fx_quotes` | Indeterminado (dados públicos) | N/A | Política de manutenção futura (não LGPD) |

### 3.3 Rota de Erase (LGPD art. 18, VI)

**Endpoint:** `DELETE /v1/account` (exclusão da conta) + `DELETE /v1/invoices/{id}` (erase individual de invoice)

**Comportamento:**
1. Valida `owner_user_id` da sessão (P-14, middleware `require_owner`)
2. Inicia transação:
   - Hard delete: `users`, `user_login_identifiers`, `user_sessions`, `password_reset_tokens`
   - Hard delete: `provider_profiles`, `provider_bank_accounts`, `clients`, `simulations`
   - `account_lifecycle_events`: anonimiza `user_id` (HMAC-SHA256 com pepper) + mantém por 5a+6m
   - `invoices`: **não deleta imediatamente** — agenda job de anonimização (5a+6m)
3. Registra evento `account_lifecycle_events` (`event_type = 'erase_requested'`, sem PII)
4. Retorna 202 Accepted com `erase_scheduled_at` (timestamp da anonimização future)

**Job de anonimização invoices (diário):**
- Para invoices com `finalized_at < now() - 5 anos - 6 meses`:
  - Substitui PII: `issuer_name` → `ANONIMIZADO`, `issuer_tax_id_digits` → `HASH`, `client_name` → `ANONIMIZADO`, `client_tax_id_digits` → `HASH`, `issuer_address`/`client_address` → `NULL`, dados bancários → `NULL`
  - Mantém: valores calculados, cotação, regime, numeração, `locale`, `status`
  - Registra log de auditoria: `invoice_id`, `owner_user_id` (hash), `timestamp`, `ator = 'system_anonymization'`

**Exclusão de backups (30 dias pós-erase):**
- Script `scripts/backup_erase_cleanup.py` remove `invoice_id`/`user_id` de backups armazenados
- Log de auditoria: `backup_id`, `invoice_ids_removed`, `timestamp`

### 3.4 ROPA Simplificado (Registro de Operações)

Tabela `processing_activities` (nova, para compliance):

| Campo | Descrição |
|-------|-----------|
| `activity_id` | UUID PK |
| `name` | Ex.: "Emissão de invoice", "Gestão de conta", "Cálculo cambial" |
| `purpose` | Finalidade (art. 6º LGPD) |
| `legal_basis` | **`art_7_v_lgpd`** (execução contrato) / `art_6_1_b_gdpr` |
| `data_categories` | JSON: `["nome", "cpf_cnpj", "endereco", "dados_bancarios", "valores", "cotacao"]` |
| `data_subjects` | `["emitente", "cliente"]` |
| `retention_period` | Ex.: "5 anos + 6 meses" |
| `technical_measures` | JSON: `["argon2id", "hmac_aliases", "owner_check", "encryption_at_rest", "log_sanitization"]` |
| `international_transfer` | `false` (soberania local P-03) |
| `created_at`, `updated_at` | Timestamps |

**Atividades pré-definidas:**
1. **Emissão de invoice** — base art. 7º V; dados emitente+cliente; retenção 5a+6m
2. **Gestão de conta (cadastro/login/lifecycle)** — base art. 7º V; dados identidade; retenção enquanto ativa + 6m
3. **Cálculo cambial/simulação** — base art. 7º V; dados parâmetros+resultado; retenção opt-in (simulações salvas)
4. **Histórico de invoices/simulações** — base art. 7º V; snapshots; retenção 5a+6m (invoices) / enquanto ativa (simulações)

### 3.5 Controles de privacidade por design (P-14, P-15, spec-015 CP-1..CP-5)

| Controle | Implementação | Spec/Teste |
|----------|---------------|------------|
| **Isolamento por proprietário** (P-14) | Middleware `require_owner` em **todas** rotas de recurso; `owner_user_id` extraído da sessão; 404 se não owner | SPEC-017 AC-07 |
| **Minimização invoice** (CP-1, DEC-03) | Endereço/bancários NULLable; só coletados se frontend envia | SPEC-007 migration |
| **Logs sem PII** (CP-2, spec-015) | Error handler sanitiza; `fx_quotes` logs sem valores; middleware remove PII/corpo | SPEC-015 CP-2 test |
| **Rota erase operante** (CP-3, DEC-04) | `DELETE /v1/account` + job anonimização + backup cleanup | SPEC-022 AC-04 |
| **`lgpd-class` em artefatos** (CP-4) | Frontmatter `lgpd-class: dados-pessoais` em specs que tocam dados produto | Esta spec, SPEC-017, SPEC-018, SPEC-019, SPEC-020, SPEC-021 |
| **Limpeza drift E.1** (CP-5, DEC-07) | `docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md:67` removida/atualizada | Task separada |

### 3.6 GDPR (aplicável se oferta/monitoramento EEE/UK — CR2-D02)

| Requisito | Implementação |
|-----------|---------------|
| Base legal | `art_6_1_b_gdpr` (execução contrato) — mesmo fundamento LGPD |
| Direitos do titular | Erase local atende art. 17 (direito à eliminação); portabilidade via export JSON (futuro) |
| DPO/Encarregado | Fora de escopo (projeto acadêmico single-user) — §7 spec-015 |
| Transferência internacional | **Proibida** (P-03, soberania local); stack 100% local/autohospedada |
| Privacy by design | P-14, P-15, Argon2id, HMAC aliases, owner-check, criptografia banco, log sanitization |
| Registro (ROPA) | Tabela `processing_activities` (simplificada) |

---

## 4. Requisitos não funcionais

- **Fail-closed:** Qualquer falha na verificação de owner → 403/404; falha no erase → rollback + alerta
- **Auditabilidade:** Todos eventos de lifecycle em `account_lifecycle_events` (sem PII); logs de erase com `invoice_id`, `owner_user_id` (hash), `timestamp`
- **Performance:** Job de anonimização diário processa em lote (cursor pagination); índice em `invoices.finalized_at`
- **Segurança:** Dados bancários criptografados em repouso (`pgcrypto`/AES-256-GCM); pepper HMAC rotacionado 90d (ADR-019)
- **Testabilidade:** Seeds sintéticos apenas; fixtures sem PII real (spec-015 §7)

---

## 5. Critérios de aceite e testes

- [ ] **AC-01:** Conta transita `active` → `dormant` aos 180 dias sem login; sessões revogadas; criações bloqueadas
- [ ] **AC-02:** Reativação `dormant` → `active` exige reset senha + verificação identidade
- [ ] **AC-03:** Exclusão definitiva (`DELETE /v1/account`) hard-deleta todos recursos exceto invoices (agenda anonimização)
- [ ] **AC-04:** Job diário anonimiza invoices com `finalized_at > 5a+6m`; substitui PII por ANONIMIZADO/HASH/NULL; mantém valores/cotação/numeração
- [ ] **AC-05:** Backup cleanup remove IDs de backups em ≤30 dias pós-erase; log de auditoria
- [ ] **AC-06:** Base legal `art_7_v_lgpd` registrada no ROPA para todas atividades; GDPR `art_6_1_b_gdpr` se aplicável
- [ ] **AC-07:** Middleware `require_owner` presente em 100% rotas de recurso (`simulations`, `invoices`, `clients`, `provider_profiles`, `provider_bank_accounts`); teste IDOR cross-user (ST-03 ADR-019)
- [ ] **AC-08:** Logs de erro/request não contêm PII, valores, corpo (spec-015 CP-2); teste automatizado ST-09 ADR-019
- [ ] **AC-09:** Tabela `invoice_sequences` + function `next_invoice_number()` implementadas; numeração `INV-{YYYYMM}-{SEQ:04d}` única por emissor/mês
- [ ] **AC-10:** Templates `invoice_pt_br.html` e `invoice_en.html` separados; compartilham macros; `locale` + `client_country_code` snapshoteados na invoice finalizada

---

## 6. Rastreabilidade

| Referência | Fonte |
|------------|-------|
| CR-002 Gate B | `docs/decisoes/ccb-CR-002.md` (CR2-D02, D03, D04, D07) |
| DEC-01..07 LGPD | `docs/decisoes/ccb-lgpd-decisoes.md` |
| spec-015 v0.3.0 (CP-1..CP-5) | `.ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md` |
| Constitution v1.3.0 (P-14, P-15, Art. 7) | `constitution.md` |
| ADR-017 (Argon2id) | `docs/decisoes/adr-017-dependencia-argon2id.md` |
| ADR-018 (M4 replanejamento) | `docs/decisoes/adr-018-tap-replanejamento-m4.md` |
| ADR-019 (Threat model) | `docs/decisoes/adr-019-seguranca-multiusuario.md` |
| spec-prop-017 §13.1/§15 | `docs/especificacoes/spec-prop-017-conta-multiusuario.md` |
| LGPD Lei 13.709/2018 | art. 4º I, 6º III, 7º V, 16, 18 |
| GDPR Reg. 2016/679 | art. 6, 17, 25, 32 |
| CC art. 206 §5º I | Retenção 5 anos |

---

## 7. Fora de escopo (YAGNI)

- DPO/Encarregado formal, ROPA completo, relatórios ANPD, plano resposta a incidentes (spec-015 §7)
- Fluxos remotos de exercício de direitos (portais, formulários, kanban) — single-user/local
- NF-e/NFS-e, numeração fiscal oficial, envio automático email
- i18n integral da interface/erros — apenas invoice bilíngue
- Equipes, organizações, papéis admin, OAuth, SSO, MFA, federação
- Integração plataformas pagamento/transferência, escrow, multiempresa, billing SaaS
- Telemetria/rastreio (P-03)
- Uso de cloud não autorizada para PII/sessão/email (P-03, Bypass Protocol)

---

## 8. Metadados de emissão

- **Avaliador primário:** `agent-compliance-governance` + `agent-project-analyst`
- **Ratificação:** CCB/GP via CR-002 Gate B (2026-11-14) — `docs/decisoes/ccb-CR-002.md`
- **parcel.dod:** true
- **Data da emissão:** 2026-11-14
- **Status da spec:** ativa / ratificada

---

## CHANGELOG

| Versão | Data | Task/Handoff | Mudança |
|--------|------|--------------|---------|
| 1.0.0 | 2026-11-14 | CR-002 Gate B / agent-compliance-governance | Emissão inicial, ratificada por CCB/GP. Consolida DEC-01..07, CP-1..CP-5, ciclo vida, retenção/erase, ROPA, GDPR, numeração, bilíngue. |

---

## CAMADAS FUNDAMENTAIS — MAPA (TA-0031)

| Camada | Seção nesta spec | Estado |
|--------|------------------|--------|
| (a) cabeçalho — spec_id, versão, status, custódia, datas, origem | frontmatter (`spec_id: spec-022`, `version: 1.0.0`, `status: ratificada`) | aplicada |
| (b) Contexto/origem | §1 + frontmatter `origin`/`task` | aplicada |
| (c) Resolução de conflitos | §2 (tabela 7 conflitos resolvidos) | aplicada |
| (d) Corpo de decisões/requisitos/contratos | §3 (ciclo vida, retenção/erase, ROPA, controles P-14/P-15, GDPR) | aplicada |
| (e) Critérios de aceite/testes | §5 (AC-01..AC-10) | aplicada |
| (f) Rastreabilidade | §6 + frontmatter `trace` | aplicada |
| (g) Fora de escopo (YAGNI) | §7 | aplicada |
| (h) Changelog | CHANGELOG | aplicada |