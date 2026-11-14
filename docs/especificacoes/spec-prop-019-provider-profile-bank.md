---
id: docs-especificacoes-spec-prop-019-provider-profile-bank
title: Proposta de Spec — Perfil da prestadora e contas bancárias de depósito
type: spec
version: 0.1.0
status: draft
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-004-provider-profile-bank.md
- docs/templates/proposta-spec-template.md
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9)
- .ai/specs/spec-007-invoice-data-model-v1.spec.md
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md
- .ai/specs/spec-023-ui-spec-v1.spec.md
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- proposta
- spec
- prestadora
- contas-bancarias
- lgpd
spec-id: PROP-019
camada: produto
estado-implementacao: nao-iniciada
rastreia-req:
- CR-004
testes-vinculados: []
---

# Proposta de Spec — Perfil da prestadora e contas bancárias de depósito

## 1. Ideia / Draft

**Título da proposta:** Perfil da prestadora (MEI/PJ) e contas bancárias de depósito

**Autor:** PO/GP — derivação da CR-004 (2026-11-14)

**Data:** 2026-11-14

**Contexto / problema que resolve:**

A emissão de invoice exige dados da empresa prestadora e conta bancária para depósito/wire transfer. O MVP atual não prevê cadastro desses dados (`spec-007:108-110` UNKNOWN). A CR-004 isola este domínio para validação de `agent-dba` e parecer LGPD sobre dados financeiros sensíveis.

**Descrição breve da solução proposta:**

Cadastrar perfil da prestadora vinculado 1:1 ao usuário (razão social, categoria MEI/PJ, CNPJ, endereço) e contas bancárias 1:N (tipo, banco, agência, conta, SWIFT/BIC, IBAN, moeda, conta primária). Snapshot dos dados na invoice finalizada para imutabilidade histórica. Criptografia em repouso para campos sensíveis.

**Escopo inicial (DENTRO):**

- Perfil prestadora: `legal_name`, `category ∈ {mei,legal_entity}`, `cnpj` (obrigatório se PJ), endereço completo, país
- Contas bancárias: tipo, banco (código COMPE + nome), agência, conta, dígito, SWIFT/BIC, IBAN, titular, moeda, `is_primary`
- Snapshot na invoice finalizada (cópia imutável de prestadora + conta primária)
- Criptografia em repouso para conta, SWIFT, IBAN (decisão CR4-D02)
- Validação de CNPJ (dígito verificador; consulta ReceitaWS opcional CR4-D03)

**Fora de escopo (NÃO está):**

- Múltiplas prestadoras por usuário
- Integração com plataformas de pagamento/transferência
- NF-e/NFS-e, envio automático de email
- Validação bancária via Open Banking / Pix
- Auditoria de alterações (pode ser adicionada depois)

## 2. Análise de Derivação Multi-Spec

**Resultado:** **Uma spec única** — domínio coeso de prestadora/banco com modelo, validações e snapshot próprios.

| Critério de Divisão | Aplica-se? | Justificativa |
|---|---:|---|
| Domínios técnicos disjuntos | Sim | Dados financeiros sensíveis, criptografia, snapshot em invoice |
| Ciclos de vida independentes | Parcial | Perfil/banco mudam raramente; snapshot na invoice é imutável |
| Requisitos regulatórios separados | Sim | LGPD/GDPR em dados bancários; criptografia em repouso |
| Dependências com desenvolvimento paralelo | Sim | Depende de SPEC-017 (identidade) e CR-008 (LGPD); pode especificar em paralelo |

**Spec derivada:** SPEC-018 — `provider-profile-bank-account-v1` | Agente dono: `agent-dba` + `agent-business-analysis-specialist`

## 3. Viabilidade Técnica

| Critério | Avaliação | Observações |
|---|---|---|
| Tecnologias no stack? | Sim | PostgreSQL, SQLAlchemy, `cryptography` ou `pgcrypto` para criptografia |
| Nova dependência? | Provável | `cryptography` (FOSS) ou extensão `pgcrypto` |
| Impacta arquitetura/contratos? | Sim | Novas tabelas, rotas CRUD, snapshot em invoice (emenda SPEC-007) |
| Complexidade | Média-Alta | Criptografia, validação CNPJ, snapshot transacional, LGPD |
| Riscos técnicos | Médios | Criptografia mal configurada, vazamento em log, snapshot inconsistente |

## 4. Viabilidade Negocial

| Critério | Avaliação | Observações |
|---|---|---|
| Alinhado com produto/roadmap? | Condicional | Requer emenda constitucional e decisões CR-004/CR-008 |
| Valor mensurável? | Sim | Dados reutilizáveis, invoice completa, wire transfer internacional |
| ROI | Positivo | Elimina retrabalho de dados por invoice; habilita cliente estrangeiro |
| Dependências externas | Sim | CCB, `agent-dba`, parecer LGPD, decisão criptografia |
| Urgência | Média | Após SPEC-017 e CR-008; antes de SPEC-020 |

## 5. Custo Técnico Estimado

| Item | Estimativa | Notas |
|---|---:|---|
| Desenvolvimento | 32–48 h | Tabelas, CRUD, criptografia, snapshot, validação CNPJ |
| Design/UX | 12–16 h | Telas perfil, contas, primária, validação |
| QA/testes | 16–24 h | Unit, integração, criptografia, snapshot, LGPD |
| Auditoria/LGPD | 8–12 h | Parecer base legal, retenção, criptografia |
| **Total** | **68–100 h** | |

## 6. Aderência ao Projeto / Produto

- **Constituição:** condicional — emenda Art. 1.2; Art. 7/9 (LGPD/GDPR em dados bancários)
- **AGENT_TOPOLOGY:** `agent-dba` (primário), `agent-business-analysis-specialist`, `agent-digital-security`, `agent-compliance-governance`, `agent-sdd-specialist`, `agent-frontend-dev`, `agent-qa-sdet`
- **LGPD/GDPR:** não aderente até CR4-D01..D04 e CR8-D01..D06. Propõe minimização, criptografia, base legal, retenção.
- **FOSS/soberania:** compatível — PostgreSQL local, `cryptography`/`pgcrypto` FOSS
- **YAGNI:** Uma prestadora por usuário; contas bancárias essenciais; multi-prestadora fora.

## 7. Critérios de Aceite para Promoção à Spec

- [x] Viabilidade técnica: **Sim**
- [x] Viabilidade negocial: **Parcial**, condicionada a emenda e decisões
- [ ] Custo aprovado pelo PO/PM
- [ ] Aderência constitucional: emenda ratificada
- [x] Riscos mapeados com mitigação
- [x] Done definido

**Resultado:** proposta em **draft**, em avaliação. Promoção depende de CR-004 e CR-008.

## 8. Agentes Responsáveis

**Avaliador primário:** `agent-dba`
**Consultados:** `agent-business-analysis-specialist`, `agent-digital-security`, `agent-compliance-governance`, `agent-sdd-specialist`, `agent-frontend-dev`, `agent-qa-sdet`
**Decisor:** CCB/GP

## 9. Modelo de Dados e Regras (Resumo)

### Tabelas

| Tabela | PK | Campos-chave | Constraints |
|---|---|---|---|
| `provider_profiles` | `user_id UUID` (FK users) | `legal_name`, `category`, `cnpj`, endereço, `country_code` | `category ∈ {mei,legal_entity}`; CNPJ obrigatório se PJ; `country_code` ISO 3166-1 |
| `provider_bank_accounts` | `id UUID` | `user_id FK`, `account_type`, `bank_code`, `branch`, `account_number` (cript), `swift_bic` (cript), `iban` (cript), `is_primary` | `account_type ∈ {checking,savings,payment,wire}`; `UNIQUE(user_id) WHERE is_primary`; FK `ON DELETE CASCADE` |

### Snapshot em invoice (emenda SPEC-007)

- Ao finalizar invoice: copiar `provider_profiles` + `provider_bank_accounts` (primária) para colunas de snapshot em `invoices`
- Snapshot imutável; alteração posterior não afeta invoice finalizada
- Decisão CR4-D04: copiar todos os campos ou apenas primários

## 10. Decisões Bloqueadoras (CR-004)

| ID | Decisão | Responsável |
|---|---|---|
| CR4-D01 | Campos mínimos por tipo de transferência | `agent-dba` + `agent-business-analysis-specialist` + CCB |
| CR4-D02 | Criptografia em repouso (conta, SWIFT, IBAN) | `agent-digital-security` + CCB |
| CR4-D03 | Validação CNPJ: dígito verificador vs. ReceitaWS | `agent-dba` + CCB |
| CR4-D04 | Snapshot: todos os campos ou apenas primários | `agent-sdd-specialist` + CCB |

## 11. Próximos Passos

| Ação | Responsável | Condição |
|---|---|---|
| Emitir modelagem de dados | `agent-dba` | Antes do CCB |
| Emitir parecer criptografia | `agent-digital-security` | Antes do CCB |
| Emitir parecer LGPD | `agent-compliance-governance` | Antes do CCB |
| Deliberar CR4-D01..D04 | CCB/GP | Após pareceres |
| Emitir SPEC-018 oficial | `agent-sdd-specialist` | Após ratificação |

## CHANGELOG

- 0.1.0 — 2026-11-14: Proposta derivada da CR-004; modelo de 2 tabelas, snapshot em invoice, criptografia em repouso, 4 decisões bloqueadoras, spec SPEC-018. Status draft.