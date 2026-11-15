---
id: docs-decisoes-adr-018-tap-replanejamento-m4
title: ADR-018 — Replanejamento TAP/M4 — Extensão para 30/12/2026 (Cenário A Completo)
type: adr
version: 1.0.0
status: ratificado
owner: agent-project-analyst
derived-from:
- constitution.md (Art. 1.1, 1.2, 1.3, 9.3.ii, 9.3.v)
- docs/decisoes/ccb-CR-002.md (CR2-D09, Gate A)
- docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md (§5, §13)
- docs/planos/plano-granular/desenvolvimento.md
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- adr
- tap
- marcos
- replanejamento
- cr-002
adr-number: 018
impacto: alto
---

# ADR-018 — Replanejamento TAP/M4 — Extensão para 30/12/2026 (Cenário A Completo)

## 1. Contexto

A CR-002 (contas multiusuário) expande o escopo do MVP com 6 specs derivadas (SPEC-017 a SPEC-022) + 5 specs emendadas (002, 004, 007, 008, 015). Estimativa total: **264–408 horas**.

**Marco M4 original:** 15/12/2026 (entrega final disciplina Fatec)  
**Dias úteis restantes (14/11 → 15/12):** ~22 dias = ~176h (insuficiente para cenário A)

**Decisão CCB (CR2-D09):** **Não criar M5. Estender M4 para 30/12/2026** (15 dias úteis adicionais = +120h). Recurso **AI-Driven processing** alocado para acelerar desenvolvimento.

## 2. Decisão

**Estender marco M4 de 15/12/2026 para 30/12/2026** e executar **Cenário A — Completo** (todas as 6 specs + 5 emendas).

## 3. Cronograma Revisado M4 Estendido

| Período | Dias Úteis | Horas Disponíveis | Atividades |
|---------|------------|-------------------|------------|
| **14/11 – 28/11** | 11 | 88h | ADRs (017, 018, 019), specs 017, 022, emendas 002, 004, 007 |
| **29/11 – 12/12** | 10 | 80h | Specs 018, 019, 020, 021, emendas 008, 015 |
| **13/12 – 23/12** | 9 | 72h | Implementação núcleo (identidade, sessão, lifecycle, prestadora, clientes) |
| **24/12 – 30/12** | 5 | 40h | Integração, testes, UAT, documentação, deploy |
| **Total** | **35** | **280h** | **Cabe no cenário A (264–408h) com buffer AI-driven** |

> **Recurso AI-Driven:** Processamento paralelo de specs, geração de código boilerplate, testes automatizados — estima-se ganho de 30–40% na velocidade de especificação e implementação inicial.

## 4. Cenários de Corte (se necessário)

| Cenário | Escopo | Horas | Risco M4 30/12 |
|---------|--------|-------|----------------|
| **A — Completo (APROVADO)** | 6 specs + 5 emendas | 264–408h | ✅ Viável com AI-driven |
| B — Core | 4 specs (017, 018, 019, 022) + 3 emendas | ~180–240h | ✅ Confortável |
| C — Mínimo | 2 specs (017, 022) + 2 emendas | ~120–160h | ✅ Folga total |

**Gatilho de fallback para B/C:** Se até 28/11 as specs 017/022/emendas 002/004/007 não estiverem emitidas e validadas.

## 5. Impacto no TAP v3 e Planos de Gerenciamento

| Artefato | Ação | Responsável | Prazo |
|----------|------|-------------|-------|
| `docs/planos/plano-granular/desenvolvimento.md` | Nota de Contexto: extensão M4, novas ondas, redistribuição pacotes | `agent-project-analyst` | 2026-11-15 |
| `docs/planos/plano-granular/custos.md` | Atualizar estimativas (264–408h adicionais) | `agent-project-analyst` | 2026-11-15 |
| `docs/planos/plano-granular/riscos.md` | Novos riscos: dependência Argon2id, AI-driven, extensão prazo | `agent-project-analyst` | 2026-11-15 |
| `eap.md` | Revisar pacotes de trabalho (adicionar 6 specs + emendas) | `agent-sdd-specialist` | 2026-11-16 |
| `tap.md` | Emenda formal via ADR-018 (Art. 1.3, ADR-005 §6) | `agent-project-analyst` | 2026-11-16 |

**Nota:** Per ADR-005 §6, o TAP v3 congelado não é alterado diretamente; a emenda de marcos é registrada via ADR e Nota de Contexto nos planos operacionais.

## 6. Ondas de Implementação (Mapeamento)

| Onda | Specs | Entregáveis | Duração Estimada |
|------|-------|-------------|------------------|
| **Onda 1** (14–28/11) | SPEC-022, SPEC-017, emendas 002/004/007 | Identidade, sessão, lifecycle, privacy, OS-01 revogada, contrato HTTP, modelo invoice | 2 semanas |
| **Onda 2** (29/11–12/12) | SPEC-018, 019, 020, 021, emendas 008/015 | Prestadora/banco, clientes, simulações/histórico, bilíngue, frontend, LGPD | 2 semanas |
| **Onda 3** (13–23/12) | Implementação | Código, migrações, testes, integração | 1.5 semanas |
| **Onda 4** (24–30/12) | Validação | UAT, security review, docs, deploy | 1 semana |

## 7. Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| AI-driven não entrega ganho esperado | Média | Alto | Buffer de 40h no cronograma; fallback para Cenário B |
| Argon2id build falha em CI | Baixa | Médio | ADR-017 prevê fallback bcrypt; testar build antecipado |
| Specs 017/022 atrasam emissão | Média | Alto | Paralelizar com `agent-sdd-specialist` + `agent-compliance-governance` |
| Integração specs 018–021 complexa | Média | Médio | Contratos de dados definidos nas specs; testes de integração obrigatórios |
| UAT comprimida na última semana | Alta | Alto | Automatizar testes de regressão; foco UAT em fluxos críticos |

## 8. Conformidade

- **Constitution Art. 1.1:** Marco final ajustado para 30/12/2026 (ainda dentro do semestre letivo)
- **Constitution Art. 1.3:** Emenda E-20 autoriza mudança de escopo; ADR-018 documenta replanejamento
- **Constitution Art. 9.3.ii + v:** ADR específica para mudança de marcos + declaração de specs derivadas, custos, gates
- **P-11 YAGNI:** Cenário A aprovado por valor integral; cortes B/C como contingência declarada

## 9. Rastreabilidade

- CR-002: `docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md`
- CCB Decision: `docs/decisoes/ccb-CR-002.md` (CR2-D09)
- Emenda Constitucional: E-20 (`constitution.md` v1.3.0)
- ADRs relacionadas: ADR-017 (Argon2id), ADR-019 (Segurança)
- Specs derivadas: SPEC-017 a SPEC-022 (ordem §13 CR-002)

---

## CHANGELOG

- **1.0.0 — 2026-11-14:** Emissão inicial, aprovada por CCB/GP via CR-002 CR2-D09. Responsável: `agent-project-analyst`.