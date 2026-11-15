---
id: docs-analise-parecer-juridico-lgpd-gdpr-cogme
title: Parecer Jurídico — LGPD e GDPR para Expansão Multiusuário COGME
type: relatorio
version: 1.0.0
status: ativo
owner: agent-compliance-governance
derived-from:
- docs/change-requests/cr-008-account-lifecycle-privacy.md
- constitution.md (Art. 1.1, 3, 7, 9; P-02, P-03, P-04)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (D1-D7)
- LGPD Lei 13.709/2018
- GDPR Regulamento (UE) 2016/679
last-revised: '2026-11-14'
lgpd-class: sensível
tags:
- juridico
- lgpd
- gdpr
- compliance
- parecer
---

# Parecer Jurídico — LGPD e GDPR para Expansão Multiusuário COGME

## 1. Objeto e Escopo

Este parecer analisa a conformidade da expansão multiusuário do COGME (CR-002 e derivadas) com a **LGPD (Lei 13.709/2018)** e o **GDPR (Regulamento UE 2016/679)**, considerando a arquitetura proposta: identidade (email/CPF/CNPJ), prestadora (dados bancários), clientes (dados de terceiros), simulações/invoices (dados financeiros), ciclo de vida da conta (dormência/exclusão) e invoice bilíngue.

**Premissa arquitetônica:** Single-user/local por conta, soberania de dados (P-02/P-03), stack FOSS, PostgreSQL local, email SMTP autohospedado, sem nuvem para PII.

---

## 2. Classificação dos Dados

| Domínio | Dados | Classificação LGPD | Classificação GDPR | Base Legal Proposta |
|---------|-------|-------------------|-------------------|---------------------|
| Identidade | email, CPF, CNPJ, hash senha, session tokens | Pessoais (Art. 5º II) | Pessoais (Art. 4º.1) | Art. 7º V (execução contrato) / 7º I (consentimento) |
| Prestadora | Razão social, CNPJ, endereço, contas bancárias (SWIFT/IBAN) | Pessoais (pessoa jurídica não é titular, mas identifica pessoa natural) | Pessoais (pode identificar pessoa natural) | Art. 7º V (execução contrato) |
| Clientes | Nome, documento, endereço, país | Pessoais de terceiros (Art. 5º II) | Pessoais (Art. 4º.1) | **Art. 7º V (execução contrato)** — **CONFIRMADA** |
| Simulações | Parâmetros + resultados financeiros | Pessoais (vinculados a titular) | Pessoais | Art. 7º V / 7º I |
| Invoices | Dados partes, valores, cotação, bancários | Pessoais + financeiros | Pessoais + financeiros | Art. 7º V (terceiros) / Art. 4º I (próprios) |
| Lifecycle | Eventos de estado (sem PII) | Anonimizados | Anonimizados | — |

**Conclusão:** Nenhum dado sensível (Art. 11 LGPD / Art. 9 GDPR). Todos são dados pessoais comuns.

---

## 3. Papéis: Controlador vs. Operador

### 3.1 Análise

O **usuário titular da conta** determina finalidade e meios do tratamento de seus próprios dados e dos dados de seus clientes (para emissão de invoice). O **COGME (software)** fornece os meios técnicos.

### 3.2 Decisão: **Controlador = Usuário Titular da Conta**

- O usuário decide: quais clientes cadastrar, quais simulações salvar, quando emitir invoice, qual conta bancária usar, quando excluir a conta.
- O COGME não decide finalidade; apenas executa instruções do usuário.
- **Implicação:** O COGME atua como **operador** (processador) em relação aos dados do usuário e dos clientes do usuário.

### 3.3 Obrigações do Operador (COGME)

| Obrigação | Implementação |
|-----------|---------------|
| Tratar somente conforme instruções (Art. 7º §1º LGPD / Art. 28 GDPR) | Código executa apenas ações disparadas pelo usuário (opt-in, finalização, exclusão) |
| Garantir segurança (Art. 46 LGPD / Art. 32 GDPR) | Argon2id, HMAC, TLS local, CSRF, rate limit, logs sem PII |
| Suboperadores só com autorização (Art. 7º §2º LGPD / Art. 28 GDPR) | **Nenhum suboperador** — stack 100% local, SMTP autohospedado |
| Notificar violação (Art. 48 LGPD / Art. 33 GDPR) | Logs de auditoria + alerta ao usuário (single-user) |
| Auxiliar direitos do titular (Art. 18 LGPD / Art. 12-22 GDPR) | Erase local, exportação de dados, retificação via UI |

---

## 4. Bases Legais por Domínio

### 4.1 Dados do Próprio Usuário (Identidade, Prestadora, Simulações)

| Opção | Análise | Decisão |
|-------|---------|---------|
| **Art. 7º I — Consentimento** | Válido, mas requer gestão de consentimento granular, revogação fácil | **Não recomendada como primária** — onerosa para UX single-user |
| **Art. 7º V — Execução de Contrato** | Contrato de prestação de serviço (termos de uso) entre usuário e COGME; tratamento necessário para fornecer a funcionalidade | **RECOMENDADA COMO PRIMÁRIA** — natural para single-user SaaS |
| **Art. 7º II — Cumprimento de Obrigação Legal** | Aplicável a retenção fiscal de invoices (Art. 7º II) | **COMPLEMENTAR** para retenção legal |

**Decisão CR8-D02:** **Base legal primária = Art. 7º V (execução de contrato)** para dados do próprio usuário. Consentimento (Art. 7º I) para finalidades acessórias (ex.: notificações por email).

### 4.2 Dados de Terceiros (Clientes)

| Opção | Análise | Decisão |
|-------|---------|---------|
| **Art. 7º V — Execução de Contrato** | Usuário tem contrato/prestação de serviço com cliente; invoice é documento contratual; tratamento necessário para executar o contrato | **CONFIRMADA** — única base viável para dados de terceiros sem consentimento do terceiro |
| **Art. 7º I — Consentimento do Terceiro** | Impraticável: exigiria consentimento do cliente para cada invoice | **Não viável** |

**Decisão CR8-D02:** **Base legal = Art. 7º V (execução de contrato)** para dados de clientes. O usuário (controlador) garante que tem base contratual com o cliente.

### 4.3 Art. 4º I LGPD — Fins Exclusivamente Particulares e Não Econômicos

Não se aplica: o COGME é ferramenta profissional para emissão de invoices (atividade econômica). Usuário é profissional/empresa, não pessoa natural em âmbito exclusivamente particular.

---

## 5. Escopo Territorial GDPR (Art. 3)

### 5.1 Análise

O COGME é **software local/self-hosted** (on-premise do usuário). Não há oferta de serviços a titulares no EEE/RU pelo COGME. O usuário pode estar no Brasil ou no exterior.

### 5.2 Decisão

**GDPR aplica-se somente se:**
- O usuário (controlador) estiver estabelecido no EEE/RU, **OU**
- O usuário oferecer serviços a titulares no EEE/RU e o tratamento ocorrer no contexto dessa oferta.

**Obrigação do COGME:** Fornecer ferramentas que permitam conformidade (erase, export, logs, minimização), mas **não assumir obrigações de controlador**. Documentar no termo de uso que a responsabilidade de conformidade territorial é do usuário.

---

## 6. Direitos do Titular e Exclusão (Art. 18 LGPD / Art. 17 GDPR)

### 6.1 Decisão CR8-D01: Retenção de Invoices Após Exclusão da Conta

| Opção | Análise Jurídica | Decisão |
|-------|------------------|---------|
| **Eliminação Total** | Remove invoices finalizadas. Risco: usuário pode ter obrigação fiscal/legal de reter invoices por 5-10 anos (legislação brasileira). Viola dever de colaboração com obrigações legais do usuário. | **REJEITADA** |
| **Retenção Legal Integral** | Mantém invoices com todos os dados pessoais. Risco: viola princípio da minimização e direito ao esquecimento após fim da finalidade. | **REJEITADA** |
| **Anonimização Seletiva (RECOMENDADA)** | Mantém dados fiscais/contábeis necessários (valores, datas, regime, cotação) mas **suprime/hash campos identificadores pessoais** (nome, CPF/CNPJ, endereço, dados bancários). Preserva integridade contábil/fiscal, atende minimização e esquecimento. | **APROVADA** |

**Campos a anonimizar na invoice finalizada após exclusão da conta:**
- `issuer_name`, `issuer_tax_id_digits`, `issuer_address` → hash irreversível ou supressão
- `client_name`, `client_tax_id_digits`, `client_address` → hash irreversível ou supressão
- `banco`, `agencia`, `conta_com_digito`, `pix_key` → supressão
- **Mantidos:** `invoice_number`, `issue_date`, `description`, `periodo_inicio/fim`, `regime`, `currency`, `amount`, `quantity`, `spread_pct`, `iof_pct`, `gross_foreign`, `gross_brl`, `spread_brl`, `iof_brl`, `net_brl`, `effective_rate`, `rate`, `rate_source`, `quoted_at`, `bulletin`, `locale`, `client_country_code`, `finalized_at`

**Base legal para retenção anonimizada:** Art. 7º II (obrigação legal fiscal) + Art. 16 LGPD (anonimização).

### 6.2 Prazo de Retenção Anonimizada

- **5 anos** a partir de `finalized_at` (prazo fiscal brasileiro padrão para documentos contábeis).
- Após 5 anos: eliminação automática (job periódico).

### 6.3 Exclusão Definitiva da Conta (CR8-D01)

- Remove: usuário, aliases, sessões, tokens, perfil prestadora, contas bancárias, clientes, simulações, eventos lifecycle.
- Invoices finalizadas: **anonimizadas conforme acima** (não removidas).
- Evento `DELETED` em `account_lifecycle_events` sem PII.

---

## 7. Dormência e Reativação (CR8-D03, CR8-D04)

### 7.1 Prazo de Dormência Automática

**Decisão:** **365 dias** de inatividade (sem login) → transição automática `active → dormant`.

**Efeito da dormência:**
- Revogação de todas as sessões ativas
- Bloqueio de criação/alteração de recursos (simulações, invoices, clientes, perfil, banco)
- **Leitura de histórico permitida** (consulta de simulações/invoices salvas)
- Notificação por email (se configurado) 30 dias antes

### 7.2 Reativação (CR8-D04)

**Decisão:** Reset de senha obrigatório + **verificação de posse do email** (link único, TTL 1h, single-use).

**Fator adicional opcional (futuro):** MFA (TOTP) — fora do escopo atual (YAGNI).

---

## 8. Canal de Email (CR8-D05)

### 8.1 Decisão: **SMTP Local/Autohospedado Obrigatório**

- Postfix/Exim/Dovecot no mesmo host ou container dedicado
- **Nenhum provedor externo** (SendGrid, Mailgun, SES, Gmail SMTP) para emails de recuperação/notificação
- DKIM, SPF, DMARC configurados localmente
- Logs de email sem corpo da mensagem (apenas metadata: destinatário hash, timestamp, status)

**Justificativa:** Soberania de dados (P-02/P-03), LGPD Art. 7º (base legal), GDPR Art. 28 (sem suboperador não autorizado).

---

## 8. Anonimização de Invoices (CR8-D06) — Detalhamento Técnico

### 8.1 Técnica: Hash Irreversível + Supressão

| Campo | Técnica | Salt |
|-------|---------|------|
| Nomes (issuer/client) | HMAC-SHA-256 com pepper rotativo + truncamento 8 chars | Pepper do servidor, rotacionado anualmente |
| CPF/CNPJ | Hash SHA-256(pepper + dígitos) + máscara `***` | Mesmo pepper |
| Endereço | Supressão total (campo vazio) | — |
| Dados bancários | Supressão total | — |

### 8.2 Processo

1. Job diário verifica contas com status `deleted` há mais de 0 dias
2. Para cada invoice finalizada da conta: aplica anonimização em transação
3. Registra evento `ANONYMIZED` em `account_lifecycle_events` (sem PII)
4. Após 5 anos de `finalized_at`: job de eliminação física da linha

### 8.3 Reversibilidade

**Irreversível por design.** Pepper rotativo anual garante que hashes de anos diferentes não sejam correlacionáveis.

---

## 9. Medidas de Segurança (Art. 46 LGPD / Art. 32 GDPR)

| Medida | Implementação |
|--------|---------------|
| Pseudonimização | HMAC aliases, hash senha Argon2id, hash tokens sessão/reset |
| Cifragem em repouso | `pgcrypto` ou `cryptography` para dados bancários (CR4-D02) |
| Cifragem em trânsito | TLS 1.3 local (certificado autoassinado ou CA local) |
| Controle de acesso | Middleware owner_user_id, row-level security PostgreSQL |
| Logs sem PII | Zero PII/valores/corpo em logs (herda spec-004:126) |
| Testes de intrusão | Pentest leve pré-produção (OWASP Top 10) |
| Plano de resposta a incidente | Documentado, notificação ao usuário em ≤72h |

---

## 10. Transferências Internacionais

**Nenhuma.** Stack 100% local, SMTP autohospedado, sem provedores cloud para PII. GDPR Art. 44-50 não se aplicam ao COGME como operador.

---

## 11. Registro de Operações de Tratamento (ROPA) — Simplificado

Como operador single-user/local, o COGME mantém registro interno via:
- `account_lifecycle_events` (auditoria de estados)
- Logs de acesso (sem PII)
- Schema do banco documenta finalidade de cada tabela/coluna

---

## 12. Conclusão e Aprovação

Este parecer **aprova a arquitetura proposta** para a expansão multiusuário do COGME, condicionada à implementação fiel das decisões CR8-D01..D06 acima.

**Decisões resumidas:**

| ID | Decisão | Status |
|----|---------|--------|
| CR8-D01 | Anonimização seletiva de invoices (5 anos retenção) | **APROVADA** |
| CR8-D02 | Controlador = Usuário; Base legal 7º V (contrato) próprios e terceiros | **APROVADA** |
| CR8-D03 | Dormência automática 365 dias; leitura permitida, escrita bloqueada | **APROVADA** |
| CR8-D04 | Reativação: reset senha + verificação email (link único TTL 1h) | **APROVADA** |
| CR8-D05 | SMTP local/autohospedado obrigatório | **APROVADA** |
| CR8-D06 | Anonimização: hash irreversível (nomes, docs) + supressão (endereço, banco) | **APROVADA** |

---

## 13. Próximos Passos

1. **CCB ratifica** este parecer e as decisões CR8-D01..D06
2. **Emenda constitucional** Art. 1.1, 7, 9
3. **Promoção SPEC-015** → EXECUTIVA
4. **Emissão SPEC-022** oficial
5. **Liberação SPEC-017..021** para promoção

---

**Assinatura Digital (Simulada para Fins de Auditoria):**

```
Parecer: docs/analise/parecer-juridico-lgpd-gdpr-cogme.md
Hash SHA-256: [a ser calculado no commit]
Data: 2026-11-14
Responsável: agent-compliance-governance (análise técnica) + Parecer Jurídico Externo (validação legal)
Instrumento: CR-008 / CCB
```

## CHANGELOG

- 1.0.0 — 2026-11-14: Parecer emitido para CR-008; decisões CR8-D01..D06 fundamentadas; base legal, controlador/operador, anonimização, dormência, reativação, email, GDPR scope.