---
id: docs-especificacoes-spec-prop-023-account-lifecycle-privacy
title: Proposta de Spec — Ciclo de vida da conta, dormência, exclusão e privacidade LGPD/GDPR
type: spec
version: 0.1.0
status: draft
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-008-account-lifecycle-privacy.md
- docs/conhecimento/templates/proposta-spec-template.md
- constitution.md (Arts. 1.1, 1.2, 1.3, 3, 5.1, 7, 9; P-02, P-03, P-04)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (D1-D7 condicionais)
- .ai/specs/spec-004-backend-mvp-v1.spec.md (LGPD logs)
- .ai/specs/spec-007-invoice-data-model-v1.spec.md (erase route)
- LGPD Lei 13.709/2018 (art. 4º I, 5º II, 6º I/III, 7º V, 11, 18)
- GDPR Regulamento (UE) 2016/679 (art. 3, 17, 25, 32, 44-50)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- proposta
- spec
- lifecycle
- privacidade
- lgpd
- gdpr
- dormencia
- exclusao
spec-id: PROP-023
camada: produto
estado-implementacao: nao-iniciada
rastreia-req:
- CR-008
testes-vinculados: []
---

# Proposta de Spec — Ciclo de vida da conta, dormência, exclusão e privacidade LGPD/GDPR

## 1. Ideia / Draft

**Título da proposta:** Ciclo de vida da conta, dormência, exclusão definitiva e privacidade LGPD/GDPR executiva

**Autor:** PO/GP — derivação da CR-008 (2026-11-14)

**Data:** 2026-11-14

**Contexto / problema que resolve:**

Todas as demais specs derivadas da CR-002 (identidade, prestadora, clientes, histórico, invoice bilíngue) dependem de decisões fundamentais de privacidade: retenção de invoices após exclusão, bases legais LGPD/GDPR, prazo de dormência, rota de erase, canal de email soberano. A CR-008 isola este domínio como **precedência máxima** (ordem 1 em §13 da PROP-017). A SPEC-015 atual é apenas PROPOSTA com D1-D7 condicionais; esta spec a promove a executiva.

**Descrição breve da solução proposta:**

- Estados da conta: `active` ↔ `dormant` (automática por inatividade ou manual), `deleted` (terminal)
- Dormência: job periódico verifica `last_login_at`/`updated_at` vs. prazo ratificado; revoga sessões, bloqueia escrita, permite leitura de histórico
- Reativação: reset de senha + verificação de identidade (fator a ratificar CR8-D04)
- Exclusão definitiva: transação única remove usuário, aliases, sessões, tokens, perfil, banco, clientes, simulações, eventos lifecycle; **invoices finalizadas: decisão CR8-D01** (retenção legal, anonimização ou eliminação)
- Evento `DELETED` em `account_lifecycle_events` sem PII
- Privacidade por design: minimização, logs sem PII/valores/corpo (herda `spec-004:126`), base legal art. 7º V (terceiros) vs. art. 4º I (próprio usuário), GDPR art. 3/17/25/32/44-50 se aplicável
- Canal de email: SMTP local/autohospedado (soberania P-02/P-03)
- Promoção da SPEC-015 de PROPOSTA para EXECUTIVA com D1-D7 ratificadas

**Escopo inicial (DENTRO):**

- Tabela `account_lifecycle_events` (auditoria sem PII)
- Transições de estado válidas e jobs de dormência automática
- Exclusão em transação única com `ON DELETE CASCADE` nas FKs dependentes
- Decisão CR8-D01 para invoices finalizadas (retenção/anonimização/eliminação)
- Parecer jurídico LGPD + GDPR (controlador/operador, bases legais, escopo territorial, transferências)
- Threat model completo (enumeração, fixation, CSRF, IDOR, erase route)
- Canal de email SMTP local/autohospedado
- Promoção SPEC-015 → executiva

**Fora de escopo (NÃO está):**

- Portal de exercício de direitos do titular (LGPD art. 18) — single-user/local torna erase local suficiente
- DPO/Encarregado, ROPA, relatórios ANPD, plano formal de resposta a incidentes — fora do escopo acadêmico
- Dados sensíveis (art. 11 LGPD) — não tratados
- Autenticação multiusuário avançada (MFA, SSO) — fora
- Telemetria/rastreio — proibidos por P-03

## 2. Análise de Derivação Multi-Spec

**Resultado:** **Uma spec única** — domínio transversal de privacidade/lifecycle que condiciona todas as demais.

| Critério de Divisão | Aplica-se? | Justificativa |
|---|---:|---|
| Domínios técnicos disjuntos | Sim | Transversal: decisões aqui afetam identidade, prestadora, clientes, histórico, invoice |
| Ciclos de vida independentes | Não | Estados da conta governam acesso a todos os recursos |
| Requisitos regulatórios separados | Sim | LGPD/GDPR exigem contrato único de privacidade executiva |
| Dependências com desenvolvimento paralelo | Não | **Bloqueia** SPEC-017..021 até decisões CR8-D01..D06 |

**Spec derivada:** SPEC-022 — `account-lifecycle-privacy-v1` | Agente dono: `agent-compliance-governance` + `agent-project-analyst` + **parecer jurídico externo**

## 3. Viabilidade Técnica

| Critério | Avaliação | Observações |
|---|---|---|
| Tecnologias no stack? | Sim | PostgreSQL, SQLAlchemy, Alembic, jobs periódicos (APScheduler/cron), SMTP local |
| Nova dependência? | Provável | `apscheduler` ou systemd timer para job de dormência; `aiosmtplib` para email |
| Impacta arquitetura/contratos? | Sim, crítico | Define FKs `ON DELETE CASCADE`, rota de erase, middleware de estado, logs |
| Complexidade | Alta | Transação de exclusão atômica, anonimização, job periódico, LGPD/GDPR, threat model |
| Riscos técnicos | Críticos | Exclusão incompleta, vazamento PII em log, erase route falha, email em nuvem não autorizada |

## 4. Viabilidade Negocial

| Critério | Avaliação | Observações |
|---|---|---|
| Alinhado com produto/roadmap? | **Bloqueador** | Sem esta spec, nenhuma das demais pode ser implementada |
| Valor mensurável? | Sim | Conformidade legal, confiança do usuário, base para produção |
| ROI | Essencial | Risco legal e reputacional se omitida |
| Dependências externas | Sim | **Parecer jurídico externo obrigatório**, CCB, threat model |
| Urgência | **Máxima** | Precede todas as demais specs derivadas da CR-002 |

## 5. Custo Técnico Estimado

| Item | Estimativa | Notas |
|---|---:|---|
| Desenvolvimento | 40–60 h | Estados, job dormência, exclusão atômica, erase route, eventos, email |
| Parecer jurídico LGPD/GDPR | 24–40 h | **Obrigatório** — controlador/operador, bases legais, art. 3 GDPR, transferências |
| Threat model | 16–24 h | `agent-digital-security` — enumeração, fixation, CSRF, IDOR, erase |
| QA/testes | 24–36 h | Lifecycle, dormência, exclusão, anonimização, erase, LGPD, email |
| LGPD/GDPR executiva (SPEC-015) | 16–24 h | Promoção de PROPOSTA para EXECUTIVA com D1-D7 ratificadas |
| **Total** | **120–184 h** | Inclui parecer jurídico externo |

## 6. Aderência ao Projeto / Produto

- **Constituição:** **Exige emenda** Art. 1.1 (LGPD primária), Art. 7 (segurança/privacidade), Art. 9 (emenda), P-02/P-03/P-04
- **AGENT_TOPOLOGY:** `agent-compliance-governance` + `agent-project-analyst` (primários), `agent-digital-security`, `agent-dba`, `agent-sdd-specialist`, `agent-business-analysis-specialist`, `agent-frontend-dev`, `agent-qa-sdet`, **parecer jurídico externo**
- **LGPD/GDPR:** **Não aderente até parecer jurídico e decisões CR8-D01..D06**. Esta spec as resolve.
- **FOSS/soberania:** Crítico — email SMTP local/autohospedado; nenhum PII em nuvem
- **YAGNI:** Portal de direitos, DPO, ROPA, ANPD, dados sensíveis — fora

## 7. Critérios de Aceite para Promoção à Spec

- [x] Viabilidade técnica: **Sim**, com riscos críticos declarados
- [x] Viabilidade negocial: **Bloqueadora** para todo o multiusuário
- [ ] Custo aprovado pelo PO/PM (inclui parecer jurídico externo)
- [ ] Aderência constitucional: **emenda ratificada** (Art. 1.1, 7, 9)
- [x] Riscos mapeados com mitigação (threat model obrigatório)
- [x] Done definido (parecer jurídico + threat model + decisões + SPEC-015 executiva)

**Resultado:** proposta em **draft**, **PRIORIDADE MÁXIMA**. **Nenhuma outra spec derivada (017-021) pode ser promovida antes desta.**

## 8. Agentes Responsáveis

**Avaliadores primários:** `agent-compliance-governance` + `agent-project-analyst`
**Consultados obrigatórios:** `agent-digital-security` (threat model), **parecer jurídico externo** (LGPD/GDPR), `agent-dba`, `agent-sdd-specialist`, `agent-business-analysis-specialist`, `agent-frontend-dev`, `agent-qa-sdet`
**Decisor:** CCB/GP

## 9. Modelo de Dados e Regras (Resumo)

### Tabela

| Tabela | PK | Campos-chave | Constraints |
|---|---|---|---|
| `account_lifecycle_events` | `id UUID` | `user_id FK`, `event_type`, `from_status`, `to_status`, `created_at` | `event_type ∈ {CREATED,ACTIVATED,DORMANT_AUTO,DORMANT_MANUAL,REACTIVATED,DELETED}`; `ON DELETE CASCADE` com `users`; **sem PII** |

### Estados e transições

| De → Para | Gatilho | Efeito |
|---|---|---|
| `active → dormant` | Job: inatividade > prazo (CR8-D03) OU solicitação manual | Revoga sessões; bloqueia escrita; leitura permitida |
| `dormant → active` | Reset senha + verificação identidade (CR8-D04) | Reativa conta; nova sessão |
| `active → deleted` | Solicitação exclusão definitiva | Transação única remove dependentes; evento DELETED |
| `dormant → deleted` | Solicitação exclusão definitiva | Idem |

### Exclusão e invoices (CR8-D01)

| Opção | Descrição | Decisão |
|---|---|---|
| Retenção legal | Manter invoices finalizadas por prazo legal (ex.: 5-10 anos) | CCB + jurídico |
| Anonimização | Suprimir/hash campos pessoais (nome, documento, endereço); manter valores | CCB + jurídico + `agent-dba` |
| Eliminação total | Remover invoices finalizadas do titular | CCB + jurídico |

### LGPD/GDPR (CR8-D02)

| Questão | Decisão necessária |
|---|---|
| Controlador vs. Operador | Quem decide finalidade/meios do tratamento? |
| Base legal próprios dados | Art. 4º I (fins exclusivamente particulares) OU art. 7º V? |
| Base legal dados terceiros | Art. 7º V (execução de contrato) confirmada? |
| Escopo territorial GDPR | Art. 3: oferta de serviço/monitoramento no EEE/RU? |
| Transferências internacionais | Email SMTP local garante soberania? Cláusulas contratuais tipo? |

## 10. Decisões Bloqueadoras (CR-008) — **TODAS DEVEM SER RESOLVIDAS ANTES DE QUALQUER IMPLEMENTAÇÃO**

| ID | Decisão | Responsável | Prioridade |
|---|---|---|---|
| **CR8-D01** | Retenção/anonimização/eliminação de invoices finalizadas após exclusão | CCB + parecer jurídico/compliance | **CRÍTICA** |
| **CR8-D02** | Controlador/operador, bases legais (art. 7º V vs. 4º I), escopo GDPR art. 3 | CCB + **parecer jurídico externo** | **CRÍTICA** |
| **CR8-D03** | Prazo dormência automática (ex.: 365d) e efeito (bloqueio total vs. leitura) | CCB/PO | **ALTA** |
| **CR8-D04** | Reativação: reset senha + verificação (qual fator?) | `agent-digital-security` + CCB | **ALTA** |
| **CR8-D05** | Canal email: SMTP local/autohospedado (soberania) | Arquitetura + CCB | **ALTA** |
| **CR8-D06** | Anonimização invoices: quais campos, técnica (hash, supressão, generalização) | `agent-dba` + `agent-compliance-governance` + CCB | **ALTA** |

## 11. Próximos Passos (ORDEM OBRIGATÓRIA)

| Ordem | Ação | Responsável | Condição |
|---:|---|---|---|
| 1 | **Contratar/obter parecer jurídico externo** LGPD + GDPR | GP/CCB | **Imediato** |
| 2 | Emitir threat model completo | `agent-digital-security` | Após parecer jurídico |
| 3 | Deliberar CR8-D01..D06 | CCB/GP | Após parecer jurídico + threat model |
| 4 | Ratificar emenda constitucional (Art. 1.1, 7, 9) | CCB/GP | Após decisões |
| 5 | Promover SPEC-015 de PROPOSTA para EXECUTIVA | `agent-sdd-specialist` | Após ratificação |
| 6 | Emitir SPEC-022 oficial | `agent-sdd-specialist` | Após ratificação |
| 7 | **Só então** promover SPEC-017..021 | `agent-sdd-specialist` | Após SPEC-022 |

## CHANGELOG

- 0.1.0 — 2026-11-14: Proposta derivada da CR-008; precedência máxima, tabela lifecycle_events, estados active/dormant/deleted, decisões LGPD/GDPR bloqueadoras (CR8-D01..D06), promoção SPEC-015, threat model obrigatório, spec SPEC-022. Status draft, **bloqueia todas as demais specs derivadas**.