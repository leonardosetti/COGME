---
id: docs-governanca-raid-log
title: RAID Log — Riscos, Premissas, Issues e Dependências do COGME
type: governanca
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/conhecimento/templates/kb-template-raid-log.md v1.0.0
- constitution.md Art. 2 (hierarquia normativa)
- PMBOK 7ª Edição — Domínio Incerteza
- OKB §5 (Premissas e restrições vigentes)
- OKB §10 (Inconsistências, lacunas e pendências)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- governanca
- riscos
- raid
- pmbok
- ativo
---

# RAID Log — COGME

> **Finalidade**: Registro único e vivo de Riscos, Premissas (Assumptions), Issues (Problemas) e Dependências do projeto. Atualizado a cada mudança de estado relevante (máx. semanal). Fonte de verdade para Gate 2 (Desenho) e Gate 3 (Go-Live).
> **Próxima Revisão Obrigatória**: 2026-11-21 (semanal) ou no próximo Gate/CR/Incidente.

---

## 1. RISCOS (Risk Register)

| ID | Descrição do Risco | Categoria | Prob. (1-5) | Impacto (1-5) | Exposição (P×I) | Status | Estratégia | Plano de Mitigação / Contingência | Dono | Data Identificação | Última Atualização | Gatilho de Revisão |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RISK-001 | Indisponibilidade da API Frankfurter (primária) | Técnico / Externo | 3 | 4 | 12 | Aberto | Mitigar | Fallback automático para PTAX/BCB (ADR-001); circuit breaker configurado (5 falhas → aberto); alerta se ambas falharem; cache local 7 dias | agent-backend-dev | 2026-11-14 | 2026-11-14 | Mudança de provedor; falha real; ajuste threshold CB |
| RISK-002 | Vazamento de segredos em imagem Docker / repo | Segurança | 2 | 5 | 10 | Aberto | Mitigar | Build com --no-cache; scan de segredos no CI (trufflehog); variáveis apenas em runtime via .env; base images por digest imutável; .gitignore rigoroso | agent-digital-security | 2026-11-14 | 2026-11-14 | Novo CVE crítico; mudança de base image; incidente segurança |
| RISK-003 | Escopo emergente além da capacidade do hardware (Qwen 30B MoE, 60GB RAM) | Técnico / Recursos | 3 | 3 | 9 | Monitorando | Aceitar com monitoramento | Métricas de uso de RAM/CPU no CI; alerta se >80% sustentado; plano B: modelo menor (Qwen 14B Q4_K_M); otimização de contexto | agent-architect | 2026-11-14 | 2026-11-14 | Nova wave de agentes; aumento de contexto; benchmark |
| RISK-004 | Não conformidade LGPD / Marco Civil (dados sensíveis, retenção, consentimento) | Legal / Compliance | 2 | 5 | 10 | Aberto | Mitigar | DPIA lightweight; criptografia em repouso (AES-256 via PostgreSQL pgcrypto); HMAC lookup para PII; política de retenção/exclusão; auditoria trimestral | agent-compliance-governance | 2026-11-14 | 2026-11-14 | Nova spec com PII; mudança regulatória; auditoria |
| RISK-005 | Dependência de único mantenedor (GP Leonardo = CCB único + dev principal) | Organizacional | 3 | 4 | 12 | Aberto | Mitigar | Documentação viva (Docs-as-Code); onboarding automatizado; bus factor ≥ 2 para áreas críticas (arch, devops, security); succession plan draft | agent-pm | 2026-11-14 | 2026-11-14 | Saída de membro chave; overload GP |
| RISK-006 | Baseline de métricas simulada (não empírica) — decisões baseadas em seeds | Métricas / Governança | 3 | 3 | 9 | Aberto | Mitigar | Coletar dados reais do GitHub Projects a partir de 01/11/2026; recalibrar baseline até 01/12/2026; alerta se métricas divergem >50% do seed | agent-project-analyst | 2026-11-01 | 2026-11-14 | Calibração completada; nova wave com dados reais |
| RISK-007 | ADR-013 colisão (duas ADRs com mesmo número: Regime Emenda TAP + SDDAI Promulgação) | Governança / Rastreabilidade | 2 | 4 | 8 | Em Correção | Corrigir | Renumerar ADR-013 (SDDAI) para ADR-014; atualizar todas referências cruzadas (OKB, canon-stack-sdd, CCB log); validar integridade | agent-project-analyst | 2026-11-02 | 2026-11-14 | Correção concluída; auditoria OKB-C-26 fechada |
| RISK-008 | Ausência de Runbook / Playbook validado para Gate 3 (Go-Live) | Operacional | 3 | 4 | 12 | Aberto | Mitigar | **Ação prioritária**: criar runbook completo (deploy, rollback, monitoring, incident response, backup/restore) até 2026-11-30; simulação de rollback em staging | agent-devops | 2026-11-14 | 2026-11-14 | Runbook v1.0 concluído; simulação OK |

**Legenda Status**: `Aberto` | `Mitigado` | `Contingência Ativa` | `Encerrado` | `Transferido`
**Legenda Estratégia**: `Evitar` | `Mitigar` | `Transferir` | `Aceitar`

---

## 2. PREMISSAS (Assumptions Log)

| ID | Premissa | Descrição Detalhada | Validade | Impacto se Falsa | Status | Ação de Validação | Dono | Data Criação | Última Validação |
|---|---|---|---|---|---|---|---|---|---|
| ASSUMP-001 | Orçamento zero recorrente (FOSS only) | Nenhum custo de licença, cloud, inferência ou SaaS permitido. Apenas hardware local e ferramentas FOSS. | Todo o projeto | Bloqueio total se violado | Validada | Auditoria contínua no CI (FOSS check) | agent-compliance-governance | 2026-09-19 | 2026-11-14 |
| ASSUMP-002 | Hardware fixo: Ryzen 7 8700G + 60GB RAM unificada | Inferência local CPU-only (llama.cpp), sem GPU dedicada. Limite prático ~32GB para modelo. | Todo o projeto | Degradação severa ou impossibilidade de rodar agentes | Validada | Benchmark periódico no CI/CD | agent-infrastructure-specialist | 2026-10-31 | 2026-11-14 |
| ASSUMP-003 | PostgreSQL 15+ como banco canônico (não SQLite) | Persistência em PostgreSQL via Docker Compose; SQLite apenas fixture de teste isolado. | Todo o projeto | Perda de concorrência, tipagem, MVCC | Validada | Migration 0001 aplicada; testes de integração | agent-dba | 2026-10-31 | 2026-11-14 |
| ASSUMP-004 | APIs de câmbio: Frankfurter (primária) + PTAX/BCB (fallback obrigatório) | Hierarquia definida em ADR-001 v1.1.0; PTAX como âncora de soberania brasileira. | Todo o projeto | Risco de indisponibilidade total se ambas falharem | Validada | Testes de integração com mock; monitoramento uptime | agent-backend-dev | 2026-10-31 | 2026-11-14 |
| ASSUMP-005 | Stack Frontend: Jinja2 + HTMX + Tailwind (sem build step) | Definido em ADR-001 v1.2.0 (ADR-LOG-002); alinha roster/infra; encerra OKB-C-10. | Todo o projeto | Reescrita frontend se mudado | Validada | Implementação em `src/frontend/`; CI green | agent-frontend-dev | 2026-11-05 | 2026-11-14 |
| ASSUMP-006 | Inferência LLM 100% local (llama.cpp, Qwen3-30B-A3B Q4_K_M) | Sem nuvem, sem CUDA, CPU-only via AMD Ryzen 7 8700G + Radeon 780M. | Todo o projeto | Impossibilidade de rodar agentes SDD | Validada | Benchmark llama.cpp; health check agentes no CI | agent-architect | 2026-10-31 | 2026-11-14 |

**Legenda Status**: `Validada` | `Em Validação` | `Invalidada` | `Obsoleta`

---

## 3. ISSUES (Problemas Abertos / Issue Log)

| ID | Título | Descrição | Severidade | Status | Origem | Impacto no Prazo/Custo/Escopo | Plano de Ação | Dono | Data Abertura | Previsão Resolução | Resolução Real |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ISSUE-001 | ADR-013 colisão (C-26) — duas ADRs com mesmo número | ADR-013 usada para "Regime Emenda TAP" e "SDDAI Promulgação" | Alta | Em Correção | Auditoria OKB (OKB-C-26) | Risco de rastreabilidade quebrada; decisões não referenciáveis | Renumerar ADR-013 (SDDAI) → ADR-014; atualizar referências cruzadas | agent-project-analyst | 2026-11-02 | 2026-11-16 | — |
| ISSUE-002 | Baseline de métricas simulada (não empírica) | Cycle Time, Throughput, WIP, Coverage em docs/metricas/baseline.md são seeds simulados | Média | Aberto | OKB-C-08/16; README §10 | Decisões baseadas em dados irreais; impossibilidade de medir melhoria real | Coletar dados reais do GitHub Projects a partir de 01/11/2026; recalibrar | agent-project-analyst | 2026-11-01 | 2026-12-01 | — |
| ISSUE-003 | Ausência de OpenAPI/Swagger formal (contrato de API implícito no código) | Rotas FastAPI em `src/backend/routers/` sem spec OpenAPI versionada | Média | Aberto | Arquitetura / Auditoria | Dificulta integração externa; documentação viva ausente | Gerar `openapi.yaml` do código; versionar em `docs/conhecimento/arquitetura/`; validar no CI | agent-backend-dev | 2026-11-14 | 2026-11-25 | — |
| ISSUE-004 | Diagramas C4 incompletos (apenas DER + arquitetura lógica no README) | Falta: Contexto, Container, Component — padrão C4 | Baixa | Aberto | Arquitetura / Auditoria | Visão arquitetural incompleta para stakeholders não-técnicos | Criar diagramas Mermaid C4 Context + Container | agent-architect | 2026-11-14 | 2026-11-28 | — |
| ISSUE-005 | NFRs dispersos (Constitution, ADRs, Specs, README) — sem documento consolidado | Latência, coverage, FOSS, LGPD, disponibilidade em múltiplos locais | Baixa | Aberto | Arquitetura / Auditoria | Dificulta validação Gate 2/3; auditoria trabalhosa | Consolidar em `docs/conhecimento/arquitetura/nfrs.md` | agent-architect | 2026-11-14 | 2026-11-22 | — |

**Legenda Severidade**: `Crítica` | `Alta` | `Média` | `Baixa`
**Legenda Status**: `Aberto` | `Em Análise` | `Em Correção` | `Aguardando Validação` | `Resolvido` | `Não Resolvido (Aceito)`

---

## 4. DEPENDÊNCIAS (Dependency Log)

| ID | Descrição | Tipo | Origem (Quem entrega) | Destino (Quem consome) | Data Necessária | Status | Risco se Atrasar | Mitigação | Dono |
|---|---|---|---|---|---|---|---|---|---|
| DEP-001 | Ratificação CCB do Business Case | Governança | GP (CCB único) | Todo o projeto (Gate 1) | 2026-11-15 | Pendente | Bloqueia Gate 2 (Desenho) e alocação de esforço formal | Agendar sessão CCB dedicada | agent-pm |
| DEP-002 | Disponibilidade da API PTAX/BCB (fallback) | Externa / Técnica | Banco Central do Brasil | Backend (rates service) | Contínuo | Ativa | Falha simultânea com Frankfurter = indisponibilidade total | Cache local estendido (7 dias); alerta monitoramento; circuito breaker | agent-backend-dev |
| DEP-003 | Entrega do Runbook (deploy/rollback/monitoring) | Interna / Entrega | agent-devops | Operação (Gate 3) | 2026-11-30 | Planejada | Go-Live sem procedimento validado = risco operacional | Priorizar na wave atual; revisão par a par | agent-devops |
| DEP-004 | Ratificação CCB das Specs PROP-017 a PROP-023 (M2-M4) | Governança | GP (CCB único) | Equipe de desenvolvimento | Conforme wave | Planejada | Início de implementação bloqueado sem spec ratificada | Agendar CCB por wave; specs em análise paralela | agent-pm |
| DEP-005 | Pen Test LGPD (requisito REQ-08 / Gate 3 Final) | Externa / Segurança | Empresa especializada / Interno | Compliance / Gate 3 | 2026-12-01 | Planejada | Go-Live sem validação segurança = risco legal/reputacional | Agendar com antecedência; preparar escopo | agent-digital-security |

**Legenda Tipo**: `Interna` | `Externa` | `Técnica` | `Governança` | `Contratual`
**Legenda Status**: `Planejada` | `Ativa` | `Pendente` | `Cumprida` | `Atrasada` | `Cancelada`

---

## 5. CONTROLE DE MUDANÇAS DO RAID LOG

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-project-analyst | Criação inicial (baseado no template aprovado) | GP (CCB) |

> **Regra de Atualização**: Este documento deve ser revisado **no mínimo semanalmente** (próxima: 2026-11-21) ou a cada: (a) nova ADR ratificada, (b) CR aprovado, (c) incidente em produção, (d) mudança de escopo/recurso, (e) Gate 2 ou Gate 3. Atualizações registradas na tabela acima.