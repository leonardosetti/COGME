---
id: kb-template-raid-log
title: Template de RAID Log — Riscos, Premissas, Issues e Dependências
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
  - constitution.md Art. 2 (hierarquia normativa)
  - PMBOK 7ª Edição — Domínio Incerteza
  - OKB §5 (Premissas e restrições vigentes)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
  - template
  - governanca
  - riscos
  - raid
  - pmbok
---

# Template de RAID Log — COGME

> **Finalidade**: Registro único e vivo de Riscos, Premissas (Assumptions), Issues (Problemas) e Dependências do projeto. Deve ser atualizado a cada mudança de estado relevante (máx. semanal). Fonte de verdade para Gate 2 (Desenho) e Gate 3 (Go-Live).

---

## 1. RISCOS (Risk Register)

| ID | Descrição do Risco | Categoria | Probabilidade (1-5) | Impacto (1-5) | Exposição (P×I) | Status | Estratégia | Plano de Mitigação / Contingência | Dono | Data Identificação | Última Atualização | Gatilho de Revisão |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RISK-001 | Exemplo: Indisponibilidade da API Frankfurter (primária) | Técnico / Externo | 3 | 4 | 12 | Aberto | Mitigar | Fallback automático para PTAX/BCB (ADR-001); circuit breaker configurado; alerta se ambas falharem | agent-backend-dev | 2026-11-14 | 2026-11-14 | Mudança de provedor; falha real |
| RISK-002 | Exemplo: Vazamento de segredos em imagem Docker | Segurança | 2 | 5 | 10 | Aberto | Mitigar | Build com --no-cache; scan de segredos no CI (trufflehog); variáveis apenas em runtime via .env; base images por digest | agent-digital-security | 2026-11-14 | 2026-11-14 | Novo CVE crítico; mudança de base image |
| RISK-003 | Exemplo: Escopo emergente além da capacidade do hardware (Qwen 30B MoE) | Técnico / Recursos | 3 | 3 | 9 | Monitorando | Aceitar com monitoramento | Métricas de uso de RAM/CPU no CI; alerta se >80% sustentado; plano B: modelo menor (Qwen 14B) | agent-architect | 2026-11-14 | 2026-11-14 | Nova wave de agentes; aumento de contexto |

**Legenda Status**: `Aberto` | `Mitigado` | `Contingência Ativa` | `Encerrado` | `Transferido`
**Legenda Estratégia**: `Evitar` | `Mitigar` | `Transferir` | `Aceitar`

---

## 2. PREMISSAS (Assumptions Log)

| ID | Premissa | Descrição Detalhada | Validade | Impacto se Falsa | Status | Ação de Validação | Dono | Data Criação | Última Validação |
|---|---|---|---|---|---|---|---|---|---|
| ASSUMP-001 | Orçamento zero recorrente (FOSS only) | Nenhum custo de licença, cloud, inferência ou SaaS permitido. Apenas hardware local e ferramentas FOSS. | Todo o projeto | Bloqueio total se violado | Validada | Auditoria contínua no CI (FOSS check) | agent-compliance-governance | 2026-09-19 | 2026-11-14 |
| ASSUMP-002 | Hardware fixo: Ryzen 7 8700G + 60GB RAM unificada | Inferência local CPU-only (llama.cpp), sem GPU dedicada. Limite prático ~32GB para modelo. | Todo o projeto | Degradação severa ou impossibilidade de rodar agentes | Validada | Benchmark periódico no CI/CD | agent-infrastructure-specialist | 2026-10-31 | 2026-11-14 |
| ASSUMP-003 | PostgreSQL 15+ como banco canônico (não SQLite) | Persistência em PostgreSQL via Docker Compose; SQLite apenas fixture de teste isolado. | Todo o projeto | Perda de concorrência, tipagem, MVCC | Validada | Migration 0001 aplicada; testes de integração | agent-dba | 2026-10-31 | 2026-11-14 |

**Legenda Status**: `Validada` | `Em Validação` | `Invalidada` | `Obsoleta`

---

## 3. ISSUES (Problemas Abertos / Issue Log)

| ID | Título | Descrição | Severidade | Status | Origem | Impacto no Prazo/Custo/Escopo | Plano de Ação | Dono | Data Abertura | Previsão Resolução | Resolução Real |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ISSUE-001 | Exemplo: ADR-013 colisão (C-26) — duas ADRs com mesmo número | ADR-013 usada para "Regime Emenda TAP" e "SDDAI Promulgação" | Alta | Em Análise | Auditoria OKB (OKB-C-26) | Risco de rastreabilidade quebrada; decisões não referenciáveis | Renumerar uma das ADRs; atualizar todas referências cruzadas | agent-project-analyst | 2026-11-02 | 2026-11-16 | — |
| ISSUE-002 | Exemplo: Baseline de métricas simulada (não empírica) | Cycle Time, Throughput, WIP, Coverage em docs/metricas/baseline.md são seeds simulados | Média | Aberto | OKB-C-08/16; README §10 | Decisões baseadas em dados irreais; impossibilidade de medir melhoria real | Coletar dados reais do GitHub Projects a partir de 01/11/2026; recalibrar | agent-project-analyst | 2026-11-01 | 2026-12-01 | — |

**Legenda Severidade**: `Crítica` | `Alta` | `Média` | `Baixa`
**Legenda Status**: `Aberto` | `Em Análise` | `Em Correção` | `Aguardando Validação` | `Resolvido` | `Não Resolvido (Aceito)`

---

## 4. DEPENDÊNCIAS (Dependency Log)

| ID | Descrição | Tipo | Origem (Quem entrega) | Destino (Quem consome) | Data Necessária | Status | Risco se Atrasar | Mitigação | Dono |
|---|---|---|---|---|---|---|---|---|---|
| DEP-001 | Ratificação CCB do Business Case | Externa / Governança | GP (CCB único) | Todo o projeto (Gate 1) | 2026-11-15 | Pendente | Bloqueia Gate 2 (Desenho) e alocação de esforço | Agendar sessão CCB dedicada | agent-pm |
| DEP-002 | Disponibilidade da API PTAX/BCB (fallback) | Externa / Técnica | Banco Central do Brasil | Backend (rates service) | Contínuo | Ativa | Falha simultânea com Frankfurter = indisponibilidade total | Cache local estendido (7 dias); alerta monitoramento | agent-backend-dev |
| DEP-003 | Entrega do Runbook (deploy/rollback) | Interna / Entrega | agent-devops | Operação (Gate 3) | 2026-11-30 | Planejada | Go-Live sem procedimento validado = risco operacional | Priorizar na wave atual; revisão par a par | agent-devops |

**Legenda Tipo**: `Interna` | `Externa` | `Técnica` | `Governança` | `Contratual`
**Legenda Status**: `Planejada` | `Ativa` | `Pendente` | `Cumprida` | `Atrasada` | `Cancelada`

---

## 5. CONTROLE DE MUDANÇAS DO RAID LOG

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-project-analyst | Criação inicial (template aprovado) | GP (CCB) |

> **Regra de Atualização**: Este documento deve ser revisado **no mínimo semanalmente** ou a cada: (a) nova ADR ratificada, (b) CR aprovado, (c) incidente em produção, (d) mudança de escopo/recurso, (e) Gate 2 ou Gate 3. Atualizações registradas na tabela acima.