---
id: kb-template-change-request
title: Template de Change Request (CR) — Solicitação de Mudança Formal
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
  - constitution.md Art. 9.3 (Fluxo de mudança integrado)
  - docs/governanca/ccb-log.md (processo CCB atual)
  - PMBOK 7ª — Domínio Trabalho do Projeto (Controle Integrado de Mudanças)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
  - template
  - governanca
  - change-request
  - cr
  - pmbok
---

# Template de Change Request (CR) — COGME

> **Finalidade**: Formalizar toda proposta de alteração no escopo, prazo, custo, qualidade, arquitetura ou baseline técnica já acordada. Obrigatório para qualquer mudança pós-Gate 1 (Início). Fluxo: Preenchimento → Análise de Impacto → Decisão CCB → Registro no CCB Log → Implementação → Verificação.

---

## 1. IDENTIFICAÇÃO DA MUDANÇA

| Campo | Preenchimento |
|---|---|
| **CR-ID** | CR-YYYY-NNN (ex: CR-2026-003) — sequencial por ano |
| **Título** | Breve, descritivo (máx. 80 chars) |
| **Tipo de Mudança** | [ ] Escopo / Requisitos  [ ] Arquitetura / Stack (ADR)  [ ] Prazo / Cronograma  [ ] Custo / Orçamento  [ ] Qualidade / NFRs  [ ] Processo / Governança  [ ] Segurança / Compliance  [ ] Outro: ___________ |
| **Origem** | [ ] Stakeholder  [ ] Equipe Técnica  [ ] Auditoria / Compliance  [ ] Incidente  [ ] Melhoria Contínua  [ ] Dependência Externa |
| **Solicitante** | Nome / Papel / Contato |
| **Data da Solicitação** | YYYY-MM-DD |
| **Urgência** | [ ] Baixa (próximo ciclo)  [ ] Média (esta wave)  [ ] Alta (bloqueante)  [ ] Crítica (produção) |

---

## 2. DESCRIÇÃO DA MUDANÇA

### 2.1 O que muda (Escopo da Alteração)
> Descreva objetivamente **o que** será alterado, referenciando artefatos afetados (ex: "ADR-001 §Decisão", "spec-prop-017 §3.2", "constitution.md Art. 7.2", "src/backend/services/rate_service.py").

### 2.2 Por que muda (Justificativa / Causa Raiz)
> Explique a **necessidade** da mudança: novo requisito, defeito, oportunidade, risco materializado, mudança regulatória, decisão técnica, etc. Cite evidências (issue, auditoria, métrica, stakeholder).

### 2.3 Como era / Como fica (Estado Atual vs. Proposto)
| Aspecto | Estado Atual (Baseline) | Estado Proposto (Pós-Mudança) |
|---|---|---|
| Ex: Banco de dados | SQLite (fixture apenas) | PostgreSQL 15+ canônico (ADR-001 v1.1.0) |
| Ex: Frontend stack | HTML5/CSS3/JS vanilla | Jinja2 + HTMX + Tailwind (ADR-001 v1.2.0) |

---

## 3. ANÁLISE DE IMPACTO (Obrigatória para Decisão CCB)

| Dimensão | Impacto (Nenhum / Baixo / Médio / Alto / Crítico) | Descrição Detalhada | Esforço Estimado (h/dias) | Custo Adicional | Risco Residual |
|---|---|---|---|---|---|
| **Escopo** | | | | R$ 0 (orçamento zero) | |
| **Prazo / Cronograma** | | | | | |
| **Arquitetura / Stack** | | | | | |
| **Qualidade / Testes** | | | | | |
| **Segurança / LGPD** | | | | | |
| **Operação / Runbook** | | | | | |
| **Documentação** | | | | | |
| **Equipe / Capacidade** | | | | | |
| **Dependências Externas** | | | | | |
| **Conformidade / Auditoria** | | | | | |

> **Regra**: Se qualquer dimensão for **Alto** ou **Crítico**, a mudança **exige** Gate 2 (Desenho) ou Gate 3 (Go-Live) dedicado, com validação técnica par a par e aprovação CCB expressa.

---

## 4. ALTERNATIVAS CONSIDERADAS

| Alternativa | Descrição | Prós | Contras | Por que Não Escolhida |
|---|---|---|---|---|
| 1. Manter estado atual (não fazer a mudança) | | | | |
| 2. Solução alternativa A | | | | |
| 3. Solução alternativa B | | | | |

---

## 5. PLANO DE IMPLEMENTAÇÃO (Se Aprovado)

| Atividade | Responsável | Início Previsto | Fim Previsto | Critério de Aceite | Dependências |
|---|---|---|---|---|---|
| 1. | | | | | |
| 2. | | | | | |
| 3. | | | | | |

**Rollback Plan**: Descreva como reverter se a mudança causar regressão ou falha em produção.

---

## 6. DECISÃO DO CCB (Change Control Board)

| Campo | Preenchimento |
|---|---|
| **Reunião CCB** | Data / Participantes / Ata ref. |
| **Decisão** | [ ] **Aprovada**  [ ] **Aprovada com Condições**  [ ] **Rejeitada**  [ ] **Deferida** (reavaliar em: ____ ) |
| **Condições / Restrições** | (se "Aprovada com Condições") |
| **Justificativa da Decisão** | |
| **Assinatura CCB (GP Leonardo)** | _________________________ / Data: ____ |

---

## 7. RASTREABILIDADE PÓS-DECISÃO

| Artefato Atualizado | Versão | Commit / PR | Validação |
|---|---|---|---|
| Ex: ADR-001 | v1.2.0 | commit abc123 | Testes verdes; revisão par a par |
| Ex: constitution.md | v1.3.0 | commit def456 | Co-assinatura CCB; hash normativo conferido |
| Ex: Runbook | v1.0.0 | commit ghi789 | Simulação de rollback OK |

---

## 8. METADADOS DE CONTROLE

| Campo | Valor |
|---|---|
| **CR-ID** | CR-2026-NNN |
| **Status** | [ ] Rascunho  [ ] Em Análise  [ ] Aguardando CCB  [ ] Aprovado  [ ] Em Implementação  [ ] Implementado  [ ] Verificado  [ ] Fechado  [ ] Rejeitado  [ ] Cancelado |
| **Criado em** | YYYY-MM-DD |
| **Última Atualização** | YYYY-MM-DD |
| **Fechado em** | YYYY-MM-DD (se aplicável) |
| **Link para Issue/PR Relacionado** | |
| **Link para CCB Log Entry** | docs/governanca/ccb-log.md # RAT-YYYY-MM-DD-XXX |

---

> **Fluxo Obrigatório**: Rascunho → Análise de Impacto (autor: agente domínio) → Submissão CCB → Decisão → Registro no CCB Log → Implementação (commits atômicos) → Verificação (testes + revisão) → Fechamento. **Nenhuma mudança em baseline técnica (ADR, Constitution, Specs, Schema DB) entra sem CR aprovado.**