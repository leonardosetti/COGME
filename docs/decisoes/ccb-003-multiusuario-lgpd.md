---
id: docs-decisoes-ccb-003-multiusuario-lgpd
title: "CCB-003 — Deliberação CR-008: Ciclo de Vida, LGPD/GDPR e Expansão Multiusuário"
type: adr
version: 1.0.0
status: ratificado
owner: Gerente de Projeto
derived-from:
- docs/change-requests/cr-008-account-lifecycle-privacy.md
- docs/analise/parecer-juridico-lgpd-gdpr-cogme.md
- docs/analise/threat-model-multiusuario.md
- constitution.md (Art. 5.1, 5.2, 5.4, 7, 9)
last-revised: '2026-11-14'
lgpd-class: sensível
tags:
- ccb
- cr-008
- lgpd
- gdpr
- multiusuario
- decisao
decision: accepted
supersedes: []
domain-pmbok: integracao
github-issue: '#41'
---

# CCB-003 — Deliberação CR-008: Ciclo de Vida, LGPD/GDPR e Expansão Multiusuário

## 1. Contexto

A **CR-008** (issue #41) estabelece as decisões fundamentais de privacidade, ciclo de vida da conta e conformidade LGPD/GDPR que **bloqueiam** a implementação de todas as specs derivadas da CR-002 (SPEC-017 a SPEC-021).

Foram produzidos dois artefatos de suporte à decisão:
- **Parecer Jurídico LGPD/GDPR** (`docs/analise/parecer-juridico-lgpd-gdpr-cogme.md`)
- **Threat Model** (`docs/analise/threat-model-multiusuario.md`)

Este registro formaliza a deliberação do CCB (Comitê de Controle de Mudanças) de membro único (GP).

---

## 2. Decisões Deliberadas

### CR8-D01 — Retenção de Invoices Após Exclusão da Conta

**Decisão:** **ANONIMIZAÇÃO SELETIVA** com retenção de 5 anos.

**Detalhamento:**
- Invoices finalizadas **não são eliminadas** nem retidas integralmente.
- Campos identificadores pessoais (nome, CPF/CNPJ, endereço, dados bancários) são **anonimizados** via hash irreversível (nomes/documentos) ou supressão (endereço/banco).
- Dados fiscais/contábeis (valores, datas, regime, cotação, número) são **mantidos** para integridade contábil/fiscal.
- Prazo de retenção anonimizada: **5 anos** a partir de `finalized_at`.
- Após 5 anos: eliminação física automática (job periódico).
- Base legal: Art. 7º II LGPD (obrigação legal fiscal) + Art. 16 LGPD (anonimização).

**Aprovação:** ✅ ACEITA

---

### CR8-D02 — Controlador/Operador e Bases Legais

**Decisão:** **Controlador = Usuário Titular da Conta**; **Base Legal Primária = Art. 7º V (Execução de Contrato)**.

**Detalhamento:**
- **Controlador:** Usuário titular da conta (determina finalidade e meios).
- **Operador:** COGME (software) — processa sob instruções do usuário.
- **Dados do próprio usuário** (identidade, prestadora, simulações): Art. 7º V (execução de contrato de prestação de serviço COGME-usuário). Consentimento (Art. 7º I) apenas para finalidades acessórias (notificações).
- **Dados de terceiros** (clientes): Art. 7º V (execução de contrato entre usuário e seu cliente). Invoice é documento contratual.
- **Art. 4º I LGPD** (fins exclusivamente particulares): **Não se aplica** — atividade econômica/profissional.
- **GDPR Art. 3:** Aplica-se somente se usuário (controlador) estiver no EEE/RU ou oferecer serviços a titulares no EEE/RU. Responsabilidade de conformidade territorial é do usuário.

**Aprovação:** ✅ ACEITA

---

### CR8-D03 — Dormência Automática

**Decisão:** **365 dias** de inatividade (sem login) → transição `active → dormant`.

**Detalhamento:**
- Job periódico (diário) verifica `last_login_at` vs. 365 dias.
- Efeito da dormência:
  - Revogação de **todas** as sessões ativas.
  - Bloqueio de **criação/alteração** de recursos (simulações, invoices, clientes, perfil, banco).
  - **Leitura de histórico PERMITIDA** (consulta de simulações/invoices salvas).
- Notificação por email (se configurado) **30 dias antes** da transição automática.
- Reativação via CR8-D04.

**Aprovação:** ✅ ACEITA

---

### CR8-D04 — Reativação de Conta Dormente

**Decisão:** **Reset de senha obrigatório + verificação de posse do email**.

**Detalhamento:**
- Fluxo: Usuário solicita reativação → email com link único (TTL 1h, single-use, hash no banco) → define nova senha (Argon2id) → conta volta a `active` → nova sessão.
- **Fator adicional (MFA/TOTP):** Fora do escopo atual (YAGNI). Registrado como melhoria futura.
- Verificação de identidade: posse do email cadastrado (único fator no MVP).

**Aprovação:** ✅ ACEITA

---

### CR8-D05 — Canal de Email (SMTP)

**Decisão:** **SMTP Local/Autohospedado Obrigatório** (Postfix/Exim em container dedicado).

**Detalhamento:**
- **Nenhum provedor externo** (SendGrid, Mailgun, SES, Gmail SMTP) para emails de recuperação/notificação.
- Configuração: DKIM, SPF, DMARC locais.
- Logs de email: **apenas metadata** (hash destinatário, timestamp, status) — **nunca corpo da mensagem**.
- Rate limit: 3 recovery/hora por email; queue local com backoff.
- TLS: STARTTLS obrigatório; certificado local.
- Justificativa: Soberania de dados (P-02/P-03), LGPD Art. 7º, GDPR Art. 28 (sem suboperador não autorizado).

**Aprovação:** ✅ ACEITA

---

### CR8-D06 — Anonimização de Invoices (Técnica)

**Decisão:** **Hash Irreversível (nomes/documentos) + Supressão (endereço/banco)**.

**Detalhamento:**

| Campo | Técnica | Parâmetros |
|-------|---------|------------|
| Nomes (issuer/client) | HMAC-SHA-256(pepper, valor) + truncamento 8 chars | Pepper rotativo anual |
| CPF/CNPJ | SHA-256(pepper + dígitos) + máscara `***` | Mesmo pepper |
| Endereço | Supressão total (campo vazio) | — |
| Dados bancários | Supressão total | — |

**Processo:**
1. Job diário verifica contas `deleted` há mais de 0 dias.
2. Para cada invoice finalizada: anonimização em transação atômica.
3. Evento `ANONYMIZED` em `account_lifecycle_events` (sem PII).
4. Após 5 anos de `finalized_at`: eliminação física automática.

**Irreversibilidade:** Garantida por design. Pepper rotativo anual impede correlação cross-ano.

**Aprovação:** ✅ ACEITA

---

## 3. Aprovação dos Artefatos de Suporte

| Artefato | Status | Observação |
|----------|--------|------------|
| Parecer Jurídico LGPD/GDPR | **APROVADO** | Fundamenta CR8-D01, D02, D06 |
| Threat Model | **APROVADO** | Fundamenta controles de segurança, ratifica SPEC-017/018/022 |

---

## 4. Consequências e Próximos Passos Obrigatórios

### 4.1 Emenda Constitucional (Imediata)

Ratificar emenda à `constitution.md` nos artigos:
- **Art. 1.1** — LGPD primária explícita para multiusuário
- **Art. 7** — Segurança e privacidade: incluir erase local, anonimização, dormência
- **Art. 9** — Fluxo de emenda: incluir CR-008 como precedente

### 4.2 Promoção SPEC-015 (Imediata)

Promover `.ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md` de **PROPOSTA (draft)** para **EXECUTIVA (ratificada)** com D1-D7 resolvidas conforme este CCB.

### 4.3 Emissão SPEC-022 Oficial (Imediata)

Emitir `spec-022-account-lifecycle-privacy-v1.spec.md` baseada em `docs/especificacoes/spec-prop-023-account-lifecycle-privacy.md` com status `ratificada`.

### 4.4 Liberação SPEC-017..021 (Após 4.1-4.3)

Promover as 5 specs derivadas de `draft` para `ratificada`:
- SPEC-017: `identity-access-session-v1`
- SPEC-018: `provider-profile-bank-account-v1`
- SPEC-019: `client-directory-v1`
- SPEC-020: `simulation-invoice-history-v1`
- SPEC-021: `invoice-bilingual-v1`

### 4.5 Implementação (Waves)

| Wave | Specs | Estimativa |
|------|-------|------------|
| W1 | SPEC-017 (Identidade), SPEC-022 (Lifecycle) | 120-180h |
| W2 | SPEC-018 (Prestadora/Banco), SPEC-019 (Clientes) | 100-150h |
| W3 | SPEC-020 (Histórico/Invoice), SPEC-021 (Bilíngue) | 100-150h |
| W4 | Integração, Testes, UAT, Documentação | 80-120h |

**Total estimado:** 400-600h — compatível com M5 (30/12/2026) se iniciado imediatamente.

---

## 5. Registro de Votação

| Papel | Nome | Voto | Data |
|-------|------|------|------|
| GP / CCB (membro único) | Leonardo Setti | **APROVADO** | 2026-11-14 |

**Instrumento:** Deliberação expressa do GP via CCB de membro único (constitution.md Art. 5.1, 5.2).

**Co-assinatura (Art. 5.4):**
```
Versão: 1.0.0
Hash normativo: [SHA-256 do conteúdo normativo]
Commit Git: [hash do commit]
Data: 2026-11-14
Papel: Gerente de Projeto — CCB de membro único
Instrumento: CCB-003 — Deliberação CR-008
```

---

## 6. Rastreabilidade

| Origem | Decisão CCB |
|--------|-------------|
| CR-008 (issue #41) | CR8-D01..D06 |
| Parecer Jurídico | `docs/analise/parecer-juridico-lgpd-gdpr-cogme.md` |
| Threat Model | `docs/analise/threat-model-multiusuario.md` |
| SPEC-015 (PROPOSTA → EXECUTIVA) | D1-D7 ratificadas |
| SPEC-022 (emissão) | `spec-022-account-lifecycle-privacy-v1.spec.md` |
| SPEC-017..021 (liberação) | Promoção condicionada a este CCB |

---

## CHANGELOG

- 1.0.0 — 2026-11-14: CCB-003 emitido; CR8-D01..D06 deliberadas e aprovadas; parecer jurídico e threat model aprovados; emenda constitucional, promoção SPEC-015, emissão SPEC-022, liberação SPEC-017..021 autorizadas.