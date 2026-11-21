---
id: docs-especificacoes-spec-prop-020-client-directory
title: Proposta de Spec — Carteira de clientes e estado ativo/inativo
type: spec
version: 0.1.0
status: obsoleto
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-005-client-directory.md
- docs/conhecimento/templates/proposta-spec-template.md
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9)
- .ai/specs/spec-007-invoice-data-model-v1.spec.md
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md
- .ai/specs/spec-023-ui-spec-v1.spec.md
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- proposta
- spec
- cliente
- carteira
- lgpd
spec-id: PROP-020
camada: produto
estado-implementacao: nao-iniciada
rastreia-req:
- CR-005
testes-vinculados: []
---

# Proposta de Spec — Carteira de clientes e estado ativo/inativo

## 1. Ideia / Draft

**Título da proposta:** Carteira de clientes (cadastro opcional, ativo/inativo, snapshot em invoice)

**Autor:** PO/GP — derivação da CR-005 (2026-11-14)

**Data:** 2026-11-14

**Contexto / problema que resolve:**

A invoice exige dados do cliente (nome, documento, endereço, país). O MVP atual não prevê carteira de clientes (`spec-007:79-81` campos opcionais sem persistência). A CR-005 isola este domínio para decisão LGPD sobre base legal art. 7º V (dados de terceiros) e para permitir cliente fictício sem cadastro.

**Descrição breve da solução proposta:**

Carteira de clientes 1:N por usuário com estado `is_active`/`deactivated_at`. Cliente fictício (dummy) admitido sem persistência, exigindo país explícito. Snapshot do cliente na invoice finalizada para imutabilidade. Inativação por contrato suspenso/encerrado; reativação permitida.

**Escopo inicial (DENTRO):**

- Cadastro opcional: nome*, documento, endereço, país (ISO 3166-1)
- Estado: `is_active` (default true), `deactivated_at`
- Inativação manual; reativação permitida
- Cliente fictício: sem registro em `clients`; país obrigatório no request
- Snapshot na invoice finalizada (cópia imutável)
- Listagem paginada, filtro ativo/inativo, busca por nome/documento
- Autocomplete no formulário de invoice (apenas ativos)

**Fora de escopo (NÃO está):**

- Hierarquia de clientes (empresa/filial)
- Portal do cliente, notificações automáticas
- Integração com CRM externo
- Importação em lote (CSV/Excel)
- Auditoria de alterações (pode ser adicionada depois)

## 2. Análise de Derivação Multi-Spec

**Resultado:** **Uma spec única** — domínio coeso de clientes com estado, snapshot e LGPD art. 7º V.

| Critério de Divisão | Aplica-se? | Justificativa |
|---|---:|---|
| Domínios técnicos disjuntos | Sim | Dados de terceiros, base legal LGPD própria, autocomplete UI |
| Ciclos de vida independentes | Parcial | Cliente muda estado; snapshot na invoice é imutável |
| Requisitos regulatórios separados | Sim | LGPD art. 7º V (execução de contrato) para dados de terceiros |
| Dependências com desenvolvimento paralelo | Sim | Depende de SPEC-017 e CR-008; pode especificar em paralelo |

**Spec derivada:** SPEC-019 — `client-directory-v1` | Agente dono: `agent-business-analysis-specialist` + `agent-dba`

## 3. Viabilidade Técnica

| Critério | Avaliação | Observações |
|---|---|---|
| Tecnologias no stack? | Sim | PostgreSQL, SQLAlchemy, autocomplete em vanilla JS |
| Nova dependência? | Não | Stack atual suficiente |
| Impacta arquitetura/contratos? | Sim | Nova tabela, rotas CRUD, snapshot em invoice (emenda SPEC-007) |
| Complexidade | Média | Estado ativo/inativo, cliente fictício, snapshot transacional |
| Riscos técnicos | Baixos-Médios | Vazamento de dados de terceiros em log, autocomplete sem autorização |

## 4. Viabilidade Negocial

| Critério | Avaliação | Observações |
|---|---|---|
| Alinhado com produto/roadmap? | Condicional | Requer emenda constitucional e decisões CR-005/CR-008 |
| Valor mensurável? | Sim | Reutilização de dados, menos erros, autocomplete |
| ROI | Positivo | Elimina redigitação por invoice; habilita histórico por cliente |
| Dependências externas | Sim | CCB, parecer LGPD art. 7º V, CR-008 |
| Urgência | Média | Após SPEC-017/018 e CR-008; antes de SPEC-020 |

## 5. Custo Técnico Estimado

| Item | Estimativa | Notas |
|---|---:|---|
| Desenvolvimento | 24–32 h | Tabela, CRUD, estado, snapshot, autocomplete |
| Design/UX | 8–12 h | Tela carteira, inativação, autocomplete invoice |
| QA/testes | 12–16 h | Unit, integração, autorização, LGPD, snapshot |
| Parecer LGPD | 4–8 h | Base legal art. 7º V, retenção inativos |
| **Total** | **48–68 h** | |

## 6. Aderência ao Projeto / Produto

- **Constituição:** condicional — emenda Art. 1.2; Art. 7/9 (LGPD art. 7º V)
- **AGENT_TOPOLOGY:** `agent-business-analysis-specialist` (primário), `agent-dba`, `agent-compliance-governance`, `agent-digital-security`, `agent-sdd-specialist`, `agent-frontend-dev`, `agent-qa-sdet`
- **LGPD/GDPR:** não aderente até CR5-D01..D03 e CR8-D01..D06. Propõe minimização, base legal, retenção.
- **FOSS/soberania:** compatível — stack local
- **YAGNI:** Cadastro opcional, estado binário, snapshot; portal/CRM fora.

## 7. Critérios de Aceite para Promoção à Spec

- [x] Viabilidade técnica: **Sim**
- [x] Viabilidade negocial: **Parcial**, condicionada a emenda e decisões
- [ ] Custo aprovado pelo PO/PM
- [ ] Aderência constitucional: emenda ratificada
- [x] Riscos mapeados com mitigação
- [x] Done definido

**Resultado:** proposta em **draft**, em avaliação. Promoção depende de CR-005 e CR-008.

## 8. Agentes Responsáveis

**Avaliador primário:** `agent-business-analysis-specialist`
**Consultados:** `agent-dba`, `agent-compliance-governance`, `agent-digital-security`, `agent-sdd-specialist`, `agent-frontend-dev`, `agent-qa-sdet`
**Decisor:** CCB/GP

## 9. Modelo de Dados e Regras (Resumo)

### Tabela

| Tabela | PK | Campos-chave | Constraints |
|---|---|---|---|
| `clients` | `id UUID` | `owner_user_id FK`, `name`, `tax_id`, endereço, `country_code`, `is_active`, `deactivated_at` | `is_active NOT NULL DEFAULT true`; `country_code` ISO 3166-1; FK `owner_user_id` `ON DELETE CASCADE`; índice `(owner_user_id, is_active)` |

### Regras

- `owner_user_id` obrigatório; autorização por sessão
- Inativo: não aparece em autocomplete; permanece consultável para histórico
- Snapshot na invoice: copiar cliente para `invoices.client_snapshot` (imutável)
- Cliente fictício: sem registro em `clients`; país obrigatório no request
- LGPD: base legal art. 7º V (execução de contrato) — decisão CR2-D02/D03

## 10. Decisões Bloqueadoras (CR-005)

| ID | Decisão | Responsável |
|---|---|---|
| CR5-D01 | Base legal LGPD art. 7º V confirmada? | `agent-compliance-governance` + CCB |
| CR5-D02 | Retenção de clientes inativos vs. exclusão | `agent-compliance-governance` + CCB |
| CR5-D03 | Autocomplete: apenas ativos? | `agent-frontend-dev` + `agent-business-analysis-specialist` |

## 11. Próximos Passos

| Ação | Responsável | Condição |
|---|---|---|
| Emitir parecer LGPD art. 7º V | `agent-compliance-governance` | Antes do CCB |
| Deliberar CR5-D01..D03 | CCB/GP | Após pareceres |
| Emitir SPEC-019 oficial | `agent-sdd-specialist` | Após ratificação |

## CHANGELOG

- 0.1.0 — 2026-11-14: Proposta derivada da CR-005; modelo de 1 tabela, estado ativo/inativo, cliente fictício, snapshot em invoice, 3 decisões bloqueadoras, spec SPEC-019. Status draft.