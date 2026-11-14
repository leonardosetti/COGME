---
id: ai-specs-spec-022-account-lifecycle-privacy-v1
title: 'SPEC spec-022 — account-lifecycle-privacy-v1 — Ciclo de vida da conta, dormência, exclusão e privacidade LGPD/GDPR executiva'
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-008-account-lifecycle-privacy.md
- docs/analise/parecer-juridico-lgpd-gdpr-cogme.md
- docs/analise/threat-model-multiusuario.md
- docs/decisoes/ccb-003-multiusuario-lgpd.md (CR8-D01..D06 ratificadas)
- constitution.md (Arts. 1.1, 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04, P-14, P-15)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.md (D1-D7 ratificadas)
- .ai/specs/spec-004-backend-mvp-v1.md (LGPD logs, erase route)
- .ai/specs/spec-007-invoice-data-model-v1.md (modelo canônico invoice)
- LGPD Lei 13.709/2018 (art. 4º I, 5º II, 6º I/III, 7º V, 11, 18)
- GDPR Regulamento (UE) 2016/679 (art. 3, 17, 25, 32, 44-50)
last-revised: '2026-11-14'
lgpd-class: sensível
tags:
- specs
- docs
- lifecycle
- privacidade
- lgpd
- gdpr
- dormencia
- exclusao
spec-id: spec-022
specname: account-lifecycle-privacy-v1
version: 1.0.0
status: ratificado
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-14
updated: 2026-11-14
origin: docs/change-requests/cr-008-account-lifecycle-privacy.md (CR-008, SPEC-022)
task: "TA-0070 | sender: agent-nexus-prime-ultimate"
kill_switch: inherited
lgpd-class: sensível
trace:
  - docs/change-requests/cr-008-account-lifecycle-privacy.md (CR-008, SPEC-022)
  - docs/analise/parecer-juridico-lgpd-gdpr-cogme.md (parecer jurídico LGPD/GDPR)
  - docs/analise/threat-model-multiusuario.md (threat model aprovado)
  - docs/decisoes/ccb-003-multiusuario-lgpd.md (CR8-D01..D06 ratificadas)
  - constitution.md (Arts. 1.1, 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04, P-14, P-15)
  - .ai/specs/spec-015-lgpd-produto-proposta-v1.md (D1-D7 ratificadas)
  - .ai/specs/spec-004-backend-mvp-v1.md (LGPD logs, erase route)
  - .ai/specs/spec-007-invoice-data-model-v1.md (modelo canônico invoice)
  - LGPD Lei 13.709/2018
  - GDPR Regulamento (UE) 2016/679
---

# SPEC spec-022 — account-lifecycle-privacy-v1 — Ciclo de vida da conta, dormência, exclusão e privacidade LGPD/GDPR executiva

**Status:** **RATIFICADA** — CCB-003 (2026-11-14) deliberou CR8-D01..D06; SPEC-015 promovida a EXECUTIVA; esta spec é condição de liberação para SPEC-017..021.

---

## 1. Contexto e Origem

### 1.1 Origem

Emitida por TA-0070 / CR-008 (agent-nexus-prime-ultimate → agent-sdd-specialist, action: spec, 2026-11-14) para resolver as decisões fundamentais de privacidade, ciclo de vida da conta e conformidade LGPD/GDPR que **bloqueavam** a implementação de todas as specs derivadas da CR-002 (SPEC-017 a SPEC-021).

### 1.2 Decisões Ratificadas (CCB-003, 2026-11-14)

| ID | Decisão | Status |
|----|---------|--------|
| **CR8-D01** | Anonimização seletiva de invoices (5 anos retenção) | ✅ APROVADA |
| **CR8-D02** | Controlador = Usuário; Base legal 7º V (contrato) próprios e terceiros | ✅ APROVADA |
| **CR8-D03** | Dormência automática 365 dias; leitura permitida, escrita bloqueada | ✅ APROVADA |
| **CR8-D04** | Reativação: reset senha + verificação email (link único TTL 1h) | ✅ APROVADA |
| **CR8-D05** | SMTP local/autohospedado obrigatório (Postfix container) | ✅ APROVADA |
| **CR8-D06** | Anonimização: hash irreversível (nomes/documentos) + supressão (endereço/banco) | ✅ APROVADA |

---

## 2. Modelo de Dados

### 2.1 Tabela `account_lifecycle_events`

| Campo | Tipo | Constraints | Descrição |
|-------|------|-------------|-----------|
| `id` | UUID | PK | Identificador único |
| `user_id` | UUID | FK → `users.id`, ON DELETE CASCADE | Proprietário da conta |
| `event_type` | VARCHAR | NOT NULL, CHECK IN (`CREATED`, `ACTIVATED`, `DORMANT_AUTO`, `DORMANT_MANUAL`, `REACTIVATED`, `DELETED`, `ANONYMIZED`) | Tipo de evento |
| `from_status` | VARCHAR | NULLABLE, CHECK IN (`active`, `dormant`, `deleted`) | Estado anterior |
| `to_status` | VARCHAR | NOT NULL, CHECK IN (`active`, `dormant`, `deleted`) | Estado posterior |
| `created_at` | TIMESTAMPTZ | NOT NULL, DEFAULT `now()` | Timestamp do evento |

**Observação:** Tabela append-only, sem PII nos eventos. `ON DELETE CASCADE` com `users`.

### 2.2 Estados da Conta (`users.status`)

| Estado | Descrição | Transições Válidas |
|--------|-----------|-------------------|
| `active` | Conta ativa, uso normal | `active → dormant` (auto/manual), `active → deleted` |
| `dormant` | Inativada por tempo ou solicitação | `dormant → active` (reativação), `dormant → deleted` |
| `deleted` | Excluída definitivamente (terminal) | — |

---

## 3. Regras de Negócio

### 3.1 Dormência Automática (CR8-D03)

- **Gatilho:** Job diário verifica `last_login_at` (ou `updated_at` se login não disponível) > 365 dias.
- **Efeito:** Transação atômica:
  1. Revoga **todas** as sessões do usuário (`user_sessions.revoked_at = now()`).
  2. Atualiza `users.status = 'dormant'`, `users.dormant_since = now()`.
  3. Insere evento `DORMANT_AUTO` em `account_lifecycle_events`.
  4. Envia notificação email (se configurado) **30 dias antes** (job separado).
- **Permissões em dormência:**
  - ✅ Leitura de histórico (simulações salvas, invoices finalizadas).
  - ❌ Criação/alteração de simulações, invoices, clientes, perfil, banco.
  - ❌ Login (sessões revogadas).

### 3.2 Dormência Manual

- Usuário solicita via UI → mesma transação de `DORMANT_AUTO` mas com `event_type = 'DORMANT_MANUAL'`.

### 3.3 Reativação (CR8-D04)

- **Fluxo:** Usuário acessa "reativar conta" → informa email → sistema envia link único (token recovery, TTL 1h, single-use, hash no banco `password_reset_tokens`) → usuário define nova senha (Argon2id) → conta volta a `active` → nova sessão criada → evento `REACTIVATED`.
- **Verificação:** Posse do email cadastrado (único fator no MVP). MFA/TOTP registrado como melhoria futura (YAGNI).

### 3.4 Exclusão Definitiva (CR8-D01)

- **Gatilho:** Usuário solicita exclusão definitiva → confirmação em duas etapas (senha + digitar "EXCLUIR") → transação única:
  1. Revoga todas as sessões.
  2. Remove: `users`, `user_login_identifiers`, `user_sessions`, `password_reset_tokens`, `provider_profiles`, `provider_bank_accounts`, `clients`, `simulations`, `account_lifecycle_events` (via `ON DELETE CASCADE`).
  3. **Invoices finalizadas:** NÃO removidas — anonimizadas conforme §3.5.
  4. Insere evento `DELETED` em `account_lifecycle_events` (sem PII).
- **Estado `deleted`:** Terminal. Não há reativação.

### 3.5 Anonimização de Invoices Finalizadas (CR8-D01, CR8-D06)

- **Momento:** Job diário processa contas com `status = 'deleted'` (há >0 dias).
- **Transação por invoice finalizada:**
  1. `issuer_name`, `client_name` → HMAC-SHA-256(pepper, valor) + truncamento 8 chars.
  2. `issuer_tax_id_digits`, `client_tax_id_digits` → SHA-256(pepper + dígitos) + máscara `***`.
  3. `issuer_address`, `client_address` → supressão (NULL/empty).
  4. `banco`, `agencia`, `conta_com_digito`, `pix_key` → supressão (NULL/empty).
  5. **Mantidos:** `invoice_number`, `issue_date`, `description`, `periodo_inicio/fim`, `regime`, `currency`, `amount`, `quantity`, `spread_pct`, `iof_pct`, `gross_foreign`, `gross_brl`, `spread_brl`, `iof_brl`, `net_brl`, `effective_rate`, `rate`, `rate_source`, `quoted_at`, `bulletin`, `locale`, `client_country_code`, `finalized_at`, `supersedes_invoice_id`.
  6. Insere evento `ANONYMIZED` em `account_lifecycle_events` (referencia `invoice_id`, sem PII).
- **Retenção:** 5 anos a partir de `finalized_at`.
- **Eliminação final:** Job periódico remove invoices anonimizadas com `finalized_at` > 5 anos.

### 3.6 Pepper HMAC (CR8-D06)

- **Armazenamento:** Variável de ambiente `COGME_HMAC_PEPPER` (256-bit aleatório).
- **Rotação:** Anual (job manual ou agendado). Pepper antigo mantido para verificação de hashes existentes; novo pepper para novos hashes.
- **Irreversibilidade:** Garantida por design. Rotação anual impede correlação cross-ano.

---

## 4. LGPD/GDPR — Implementação Executiva (CR8-D02)

### 4.1 Papéis

| Papel | Ator | Responsabilidade |
|-------|------|------------------|
| **Controlador** | Usuário titular da conta | Define finalidade/medios; decide quais clientes cadastrar, quando emitir invoice, quando excluir conta |
| **Operador** | COGME (software) | Processa sob instruções do usuário; fornece meios técnicos (erase, export, anonimização) |

### 4.2 Bases Legais

| Domínio | Base Legal LGPD | Base Legal GDPR | Justificativa |
|---------|-----------------|-----------------|---------------|
| Dados do usuário (identidade, prestadora, simulações) | Art. 7º V (execução de contrato COGME-usuário) | Art. 6.1(b) (execução de contrato) | Contrato de prestação de serviço COGME-usuário |
| Dados de terceiros (clientes) | Art. 7º V (execução de contrato usuário-cliente) | Art. 6.1(b) (execução de contrato) | Invoice é documento contratual; usuário garante base contratual com cliente |
| Finalidades acessórias (notificações) | Art. 7º I (consentimento) | Art. 6.1(a) (consentimento) | Opt-in granular no cadastro |

**Art. 4º I LGPD** (fins exclusivamente particulares): **Não se aplica** — atividade econômica/profissional.

### 4.3 GDPR Art. 3 — Escopo Territorial

- Aplica-se **somente se**: usuário (controlador) estabelecido no EEE/RU **OU** oferece serviços a titulares no EEE/RU.
- **Responsabilidade:** Do usuário (controlador). COGME fornece ferramentas (erase, export, anonimização, logs).
- **Termo de uso:** Deve declarar que conformidade territorial é responsabilidade do usuário.

### 4.4 Direitos do Titular (Art. 18 LGPD / Art. 12-22 GDPR)

| Direito | Implementação COGME |
|---------|---------------------|
| Acesso | Exportação de dados (JSON) via UI |
| Retificação | Edição de perfil/prestadora/banco/clientes (exceto email/CPF) |
| Eliminação (Esquecimento) | Exclusão definitiva + anonimização invoices (CR8-D01) |
| Restrição | Dormência (bloqueia escrita, permite leitura) |
| Portabilidade | Export JSON com todos os dados do usuário |
| Oposição | Não aplicável (base legal = contrato) |
| Decisão automatizada | Não aplicável |

---

## 5. SMTP Local/Autohospedado (CR8-D05)

- **Servidor:** Postfix em container dedicado (`docker-compose.yml`).
- **Configuração:** DKIM, SPF, DMARC locais.
- **Uso:** Apenas emails transacionais (recuperação senha, notificação dormência 30d).
- **Logs:** Apenas metadata (hash destinatário, timestamp, status) — **nunca corpo**.
- **Rate Limit:** 3 recovery/hora por email; queue local com backoff exponencial.
- **TLS:** STARTTLS obrigatório; certificado local autoassinado ou CA local.
- **Nenhum provedor externo** (SendGrid, Mailgun, SES, Gmail SMTP).

---

## 6. Segurança — Controles Obrigatórios (Threat Model Aprovado)

| Controle | Implementação | Spec Relacionada |
|----------|---------------|------------------|
| Senha | Argon2id (memory=64MB, iterations=3, parallelism=4) | SPEC-017 |
| Aliases Login | HMAC-SHA-256(pepper, identificador); pepper rotativo anual | SPEC-017 |
| Sessão | Token 256-bit aleatório; hash SHA-256; TTL 24h sliding; rotação pós-login | SPEC-017 |
| Recovery | Token 256-bit; hash SHA-256; TTL 1h; single-use; email local | SPEC-017 |
| CSRF | Double-submit cookie + header `X-CSRF-Token` | SPEC-017 |
| Rate Limit | Por IP + identificador (email/CPF/CNPJ) | SPEC-017 |
| Row-Level Security | PostgreSQL `CREATE POLICY` em todas tabelas `owner_user_id` | SPEC-017, 018, 019, 020 |
| Cifragem Banco | `pgcrypto` para dados bancários (SWIFT, IBAN, conta) | SPEC-018 |
| SMTP Local | Postfix container; DKIM/SPF/DMARC; zero provedor externo | SPEC-022 |
| Logs | Zero PII/valores/corpo; `account_lifecycle_events` auditoria | SPEC-004, 022 |
| WeasyPrint | `_RefusingUrlFetcher` recusa tudo; fontes locais | SPEC-008, 021 |

---

## 7. Critérios de Aceite e Testes

### 7.1 Critérios Funcionais

| ID | Critério | Método |
|----|----------|--------|
| AC-01 | Dormência automática aos 365 dias: sessões revogadas, status `dormant`, escrita bloqueada, leitura permitida | Teste integração (job + middleware) |
| AC-02 | Reativação: link único TTL 1h → nova senha → status `active` → nova sessão | Teste integração (fluxo completo) |
| AC-03 | Exclusão: remove dependentes (CASCADE), invoices anonimizadas (hash + supressão), evento `DELETED` | Teste integração (transação + job anonimização) |
| AC-04 | Anonimização: nomes/docs → hash 8 chars; CPF/CNPJ → SHA-256+mask; endereço/banco → NULL | Teste unitário (vetores conhecidos) |
| AC-05 | Retenção 5 anos: job remove invoices anonimizadas com `finalized_at` > 5 anos | Teste integração (time travel) |
| AC-06 | SMTP local: Postfix container sobe healthy; DKIM/SPF/DMARC pass; recovery email entregue | Teste integração (container + mailhog) |
| AC-07 | RLS: usuário A não acessa recursos de usuário B (simulações, invoices, clientes, perfil, banco) | Teste integração (multi-usuário paralelo) |
| AC-08 | Cifragem bancária: `account_number`, `swift_bic`, `iban` cifrados em repouso (`pgcrypto`) | Teste unitário (verifica ciphertext) |
| AC-09 | Logs zero PII: nenhum log contém email, CPF, CNPJ, nome, valores, corpo request | Teste automatizado (grep em logs de teste) |
| AC-10 | Pepper rotativo: job anual troca `COGME_HMAC_PEPPER`; hashes antigos ainda verificáveis | Teste unitário (simulação rotação) |

### 7.2 Critérios Não-Funcionais

| ID | Critério | Alvo |
|----|----------|------|
| NF-01 | Latência login (Argon2id) | < 500ms (P95) |
| NF-02 | Throughput rate limit | 100 req/s sem degradação |
| NF-03 | Cobertura testes | ≥ 80% (P-06) |
| NF-04 | Tempo anonimização por invoice | < 100ms |

---

## 8. Rastreabilidade

| Fonte | Seção |
|-------|-------|
| CR-008 (issue #41) | Todas |
| CCB-003 | CR8-D01..D06 |
| Parecer Jurídico | `docs/analise/parecer-juridico-lgpd-gdpr-cogme.md` |
| Threat Model | `docs/analise/threat-model-multiusuario.md` |
| Constitution | Arts. 1.1, 1.2, 1.3, 3 (P-14, P-15), 5.1, 7, 9 |
| SPEC-015 | D1-D7 ratificadas |
| SPEC-004 | LGPD logs, erase route |
| SPEC-007 | Modelo canônico invoice |

---

## 9. Fora de Escopo (YAGNI)

- Portal de exercício de direitos do titular (LGPD Art. 18) — single-user/local torna erase local suficiente.
- DPO/Encarregado, ROPA formal, relatórios ANPD, plano formal de resposta a incidentes — fora do escopo acadêmico.
- Dados sensíveis (Art. 11 LGPD) — não tratados.
- MFA/TOTP, SSO, federação de identidade — YAGNI.
- Telemetria/rastreio — proibidos por P-03.

---

## CHANGELOG

- 1.0.0 — 2026-11-14: SPEC-022 emitida como RATIFICADA (CCB-003); implementa CR8-D01..D06; condição de liberação para SPEC-017..021; modelo `account_lifecycle_events`, dormência 365d, reativação email, exclusão CASCADE + anonimização invoices 5 anos, pepper HMAC rotativo, SMTP local, LGPD/GDPR executivo, threat model aprovado.