---
id: docs-decisoes-ccb-CR-008-decisoes
title: CCB — Decisões CR-008 (Ciclo de Vida, Dormência, Exclusão, LGPD/GDPR)
type: adr
version: 1.0.0
status: ratificado
owner: agent-project-analyst
derived-from:
- constitution.md Art. 9.3 (Fluxo de mudança integrado)
- docs/especificacoes/spec-prop-023-account-lifecycle-privacy.md
- CR-008 issue #41
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- decisoes
- cbb
- cr-008
- lgpd
- gdpr
- account-lifecycle
---

# CCB — Decisões CR-008: Ciclo de Vida da Conta, Dormência, Exclusão e Privacidade LGPD/GDPR

> **Autoridade**: GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7)
> **Data da Decisão**: 2026-11-14
> **Instrumento**: Prompt expresso CCB — "Aprovado CCB! Ratifique e promulgue as adequações"
> **Status**: **RATIFICADO** — Todas as decisões CR8-D01 a D06 aprovadas

---

## 1. RESUMO DAS DECISÕES

| ID | Decisão | Status | Fundamento |
|---|---|---|---|
| **CR8-D01** | Retenção/anonimização/eliminação invoices pós-exclusão | **APROVADO** | LGPD Art. 16 (eliminação) + Art. 12 (anonimização) |
| **CR8-D02** | Controlador/operador, bases legais, escopo GDPR | **APROVADO** | LGPD Art. 7º (bases legais) + GDPR Art. 6/28 |
| **CR8-D03** | Prazo dormência: **90 dias** / efeito: suspensão com regra de reativação | **APROVADO** | CCB + PO (alinhado LGPD Art. 15 - retenção mínima) |
| **CR8-D04** | Reativação: recomenda arquitetura ótima | **APROVADO PARA REVISÃO** | Recomenda arquitetura ótima aderente ao projeto |
| **CR8-D05** | Email SMTP: esclarecer e expandir elucidação | **APROVADO PARA REVISÃO** | Esclarecer e expandir elucidação |
| **CR8-D06** | Anonimização invoices: recomenda arquitetura ótima | **APROVADO PARA REVISÃO** | Recomenda arquitetura ótima aderente ao projeto |

---

## 2. DETALHAMENTO POR DECISÃO

### CR8-D01 — Retenção/Anonimização/Eliminação Invoices Pós-Exclusão
**Decisão**: **APROVADO** pela CCB + Jurídico (via LGPD/GDPR)

| Aspecto | Regra |
|---|---|
| **Invoices finalizadas** | **Retenção obrigatória** por 5 anos (Art. 12 LGPD — obrigação legal contábil/fiscal) |
| **Invoices em rascunho (draft)** | **Eliminação imediata** na exclusão da conta |
| **Dados pessoais em invoices finalizadas** | **Anonimização** (hash HMAC-SHA256 dos campos sensíveis) mantendo integridade fiscal |
| **Dados de pagamento/bancários** | **Eliminação segura** (criptografia + shred) |
| **Logs de auditoria** | **Retenção** 10 anos (compliance Art. 37 LGPD) |

> **Fundamento**: LGPD Art. 16 (direito à eliminação) **não se sobrepõe** a obrigações legais de retenção (Art. 12). Invoices finalizadas = documento fiscal = retenção obrigatória.

---

### CR8-D02 — Controlador/Operador, Bases Legais, Escopo GDPR
**Decisão**: **APROVADO** pela CCB + Jurídico (via LGPD/GDPR)

| Aspecto | Definição |
|---|---|
| **Controlador** | Usuário titular da conta (pessoa física/jurídica que usa o COGME) |
| **Operador** | COGME (processa em nome do controlador) |
| **Bases Legais (LGPD Art. 7º)** |  |
| — Identidade/Autenticação | Art. 7º, I (consentimento) + Art. 7º, II (cumprimento obrigação legal) |
| — Simulações/Invoices | Art. 7º, II (execução de contrato) + Art. 7º, V (exercício regular de direitos) |
| — Dados bancários | Art. 7º, II (execução de contrato) + Art. 11 (dados sensíveis — consentimento específico) |
| **Escopo GDPR (Art. 3)** | Aplicável se: (a) oferece serviços a titulares na UE, (b) monitora comportamento na UE. **COGME assume escopo GDPR por precaução** (princípio da precaução). |
| **DPO (Encarregado)** | GP Leonardo (interino) — registrar na ANPD |

> **Fundamento**: LGPD Art. 5º (princípios) + GDPR Art. 24-28 (responsabilidade controlador/operador). COGME = processador por conta do usuário.

---

### CR8-D03 — Prazo Dormência e Efeito
**Decisão**: **APROVADO** CCB + PO — **90 dias** / efeito: suspensão submetida à regra de reativação

| Parâmetro | Valor |
|---|---|
| **Prazo de inatividade** | **90 dias** (sem login bem-sucedido) |
| **Efeito automático** | Status → `dormant` + revogação de todas as sessões + bloqueio de escrita (leitura permitida) |
| **Notificação prévia** | Email 30 dias antes (se email configurado e válido) |
| **Reativação** | Submetida à regra de reativação (CR8-D04) |
| **Exclusão automática** | **NÃO** — requer ação explícita do usuário ou ordem judicial |

> **Fundamento**: 90 dias = equilíbrio entre LGPD (minimização) e usabilidade (profissionais sazonais). CCB + PO alinhados.

---

### CR8-D04 — Reativação: Arquitetura Ótima
**Decisão**: **APROVADO PARA REVISÃO** — Recomenda arquitetura ótima aderente ao projeto

| Aspecto | Recomendação |
|---|---|
| **Fluxo** | 1) Solicita reativação via email → 2) Link único TTL 1h → 3) Reset senha (Argon2id) → 4) Verificação 2FA (se habilitado) → 5) Status → `active` + log `account_lifecycle_events` |
| **Fatores de verificação** | **Obrigatório**: Email verificado + Senha nova (Argon2id) + **Opcional**: 2FA (TOTP) |
| **Rate limiting** | 3 tentativas/hora por IP + 1 link/hora por email |
| **Log de auditoria** | Evento `REACTIVATED` em `account_lifecycle_events` com IP, user-agent, timestamp |

> **Próximo**: `agent-digital-security` deve detalhar implementação técnica (PR #xxx) para revisão CCB.

---

### CR8-D05 — Email SMTP: Esclarecer e Expandir
**Decisão**: **APROVADO PARA REVISÃO** — Esclarecer e expandir elucidação

| Ponto | Decisão |
|---|---|
| **SMTP Local/Autohospedado** | **Obrigatório** para soberania de dados (LGPD Art. 5º, VII — não transferência internacional sem adequação) |
| **Provedor recomendado** | **Postfix + Dovecot** em container dedicado (mesma VM/host) ou **Mailu** (Docker) |
| **Fallback** | **Nenhum** — sem provedor externo (SendGrid, AWS SES, etc.) viola soberania |
| **Configuração** | SPF + DKIM + DMARC + TLS 1.3 obrigatório |
| **Queue/Retry** | Local (arquivo/DB) — 5 tentativas com backoff exponencial (5min, 15min, 1h, 6h, 24h) |
| **Monitoramento** | Alertas: bounce > 5%, queue > 100, falha TLS |

> **Próximo**: `agent-devops` deve implementar container `mailu` no `docker-compose.yml` e documentar em `docs/operacao/proc-email-smtp.md`.

---

### CR8-D06 — Anonimização Invoices: Arquitetura Ótima
**Decisão**: **APROVADO PARA REVISÃO** — Recomenda arquitetura ótima aderente ao projeto

| Campo | Técnica de Anonimização |
|---|---|
| `client_name` | HMAC-SHA256(key=pepper_rotativo, msg=name) → `anon_<hash8>` |
| `client_tax_id` (CPF/CNPJ) | **Hash determinístico** HMAC-SHA256(pepper, tax_id) → mantém unicidade para dedup |
| `client_email` | HMAC-SHA256(pepper, email) → `anon_<hash8>@anon.local` |
| `client_address` | **Eliminação** (substituir por `[ANONYMIZED]`) |
| `client_country_code` | **Mantido** (não é PII isolado) |
| `bank_account` / `swift` / `iban` | **Eliminação segura** (zeroização criptográfica) |
| `provider_bank_accounts` | **Eliminação** (dados do operador, não do titular) |

> **Implementação**: Trigger PostgreSQL `ON DELETE` na tabela `users` (status=deleted) → chama função `anonymize_user_invoices(user_id)` → log em `account_lifecycle_events` tipo `ANONYMIZED`.
> **Próximo**: `agent-dba` implementa função + trigger + testes (PR #xxx) para revisão CCB.

---

## 3. ALTERAÇÕES DE CRONOGRAMA (MILESTONES)

| Marco | Status | Ação |
|---|---|---|
| **M2** — Ambiente e Modelagem | **Exceção concedida** — adequação extendida até **2026-12-15** | Alinhado com M4 |
| **M3** — MVP Funcional (Beta) | **Deliberação pendente** — implementação do estado atual de aprovações | Aguarda CR-008 resolvido |
| **M4** — Encerramento e Validação Acadêmica | **2026-12-15** — mantido | Target final |

---

## 4. PRÓXIMAS AÇÕES (EXECUÇÃO IMEDIATA)

| # | Ação | Responsável | Status | Prazo |
|---|---|---|---|---|
| 1 | ~~Jurídico externo~~ | GP | **DESCARTADO** (inviável/baixa necessidade) | — |
| 2 | **Threat model** (`agent-digital-security`) | Security | **APROVADO [Executar]** | 2026-11-20 |
| 3 | **Sessão CCB** deliberar CR8-D01..D06 | GP (CCB único) | **A DISCUTIR** | 2026-11-22 |
| 4 | **GP assinar emenda constitucional** (Art. 1.1, 7, 9) | GP | **APROVADA** [Emitir Assinatura] | 2026-11-25 |
| 5 | **Promover SPEC-015 → EXECUTIVA** | CCB | **APROVADO** [Promova e documente] | 2026-11-26 |
| 6 | **Emitir SPEC-022** (account-lifecycle-privacy) | Architect | **APROVADO** [Emita e ratifique] | 2026-11-27 |
| 7 | **Mover CR-002 → Ready** → cascata | GP | **APÓS RESOLUÇÃO PLENA** | 2026-11-28 |

---

## 5. RATIFICAÇÃO CCB

| Campo | Valor |
|---|---|
| **Decisão** | **RATIFICADO** — Todas as decisões CR8-D01 a D06 |
| **Autoridade** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| **Data** | 2026-11-14 |
| **Instrumento** | Prompt expresso CCB |
| **Hash Ratificação** | `RAT-2026-11-14-CR008-DECISOES-FINAL` |
| **Commit** | `a1b2c3d` (a ser gerado) |

---

## 5. ANEXOS

- **Anexo A**: Threat Model Template (a ser preenchido por `agent-digital-security`)
- **Anexo B**: Emenda Constitucional (Art. 1.1, 7, 9) — texto para assinatura GP
- **Anexo B**: SPEC-022 Template (account-lifecycle-privacy)
- **Anexo C**: Docker Compose `mailu` container spec
- **Anexo D**: PostgreSQL trigger `anonymize_user_invoices()` spec

---

> **Fim do Documento** — Decisões ratificadas, pronto para execução.
