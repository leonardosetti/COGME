---
id: docs-governanca-communication-plan
title: Plano de Comunicação — COGME
type: governanca
version: 1.0.0
status: ativo
owner: agent-pm
derived-from:
- docs/conhecimento/templates/kb-template-communication-plan.md v1.0.0
- docs/governanca/stakeholder-register.md v1.0.0
- constitution.md Art. 4 (Comunicação e transparência)
- PMBOK 7ª — Domínio Partes Interessadas (Communications Management)
- OKB §7 (SSOT operacional — GitHub Projects)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- governanca
- comunicacao
- stakeholders
- pmbok
---

# Plano de Comunicação — COGME

> **Finalidade**: Definir **quem** recebe **qual** informação, com **qual frequência**, por **qual canal**, e **quem é responsável** por enviar. Alinha expectativas, evita ruído e garante rastreabilidade (auditoria).
> **Base**: Stakeholder Register (`docs/governanca/stakeholder-register.md`).
> **Revisão**: A cada Gate (1, 2, 3) ou mudança de stakeholder chave.

---

## 1. MATRIZ DE COMUNICAÇÃO (Stakeholders × Informações)

| Stakeholder / Grupo | Papel / Interesse | Informação Necessária | Formato / Canal | Frequência | Responsável (Emissor) | Confirmação de Recebimento |
|---|---|---|---|---|---|---|
| **GP Leonardo (CCB único)** | Patrocinador / Decisor final | Status executivo, decisões Gate, CRs, riscos críticos, orçamento | Status Report (Markdown) + Reunião 1:1 (videochamada) | Semanal + Ad-hoc Gates | agent-pm | Assinatura no Status Report / Ata CCB |
| **Coordenação Curso FATEC** | Governança acadêmica | Marco M1–M4, entregas acadêmicas, compliance LGPD, lições aprendidas | Relatório formal (Markdown/PDF) + Apresentação | Por Marco (M1, M2, M3, M4) + Final | agent-pm | Assinatura de aceite / Termo de encerramento |
| **Banca Avaliadora TCC** | Avaliador final | Documentação completa (TAP, Specs, ADRs, Testes, Código), Demo | Entrega antecipada (15 dias) via GitHub/Drive + Sessão defesa | Único (Defesa) | GP | Ata de defesa / Assinatura termo |
| **Equipe Técnica Core (3 pessoas)** | Executores | Sprint/Wave goals, impedimentos, decisões técnicas (ADRs), mudanças (CRs), deploy | GitHub Projects (SSOT) + Daily Standup (async Discord) + ADR/CR notificações | Contínuo (SSOT) + Diário (standup) | agent-pm / agent-devops | Check no Projects / Reação em Issue/PR |
| **Agentes SDD/IA (46 promulgados)** | Força de trabalho automatizada | Contexto de tarefa, contratos (registry.yaml), health checks, decisões arquiteturais | Nexus Prime Ultimate (L0) routing + Registry YAML + CI/CD health | Por tarefa / Contínuo (CI) | nexus-prime-ultimate (L0) | parcel.dod / Health check green |
| **Beta Testers / Usuários Piloto** | Validadores UAT | Release Notes, guias de uso, known issues, canais de feedback | GitHub Releases + Discord #beta + Formulário feedback | Por Release + Ad-hoc | agent-qa-sdet / agent-frontend-dev | Issues de feedback / UAT results |
| **Banco Central do Brasil (BCB/PTAX)** | Fornecedor API fallback | Uso respeitoso, User-Agent, cache, monitoramento erros | User-Agent header + Monitoramento passivo | Contínuo (implícito) | agent-backend-dev | Monitoramento 429/5xx / Logs |
| **Frankfurter API** | Fornecedor API primária | Uso respeitoso, fallback se instável | User-Agent header + Monitoramento passivo | Contínuo (implícito) | agent-backend-dev | Monitoramento 429/5xx / Logs |
| **Comunidade FOSS / GitHub** | Pares / Fornecedores stack | Issues, PRs, Security advisories, Contribuições | GitHub Issues / PRs / Security Advisories / Discussions | Ad-hoc / Contínuo | Equipe toda | Merge / Close / Response |

---

## 2. EVENTOS DE COMUNICAÇÃO RECORRENTES

| Evento | Participantes | Frequência | Duração | Canal | Pauta Padrão | Artefato Gerado |
|---|---|---|---|---|---|---|
| **Daily Standup (Async)** | Equipe Técnica (SH-004) | Diária (dias úteis) | 15 min | Discord #standup (texto/voz) | O que fiz? O que farei? Impedimentos? | Atualização no Projects (SSOT) |
| **Weekly Status Sync** | GP (SH-001) + Tech Leads | Semanal (segundas) | 30 min | Videochamada / Presencial | Status Report review, riscos, CRs, decisões | Status Report assinado |
| **Gate 1 Review (Início)** | CCB (GP) + Equipe + Coordenação FATEC | Início do projeto | 60 min | Videochamada | Charter, Business Case, Orçamento, Riscos iniciais | Ata Gate 1 / CR se needed |
| **Gate 2 Review (Desenho)** | CCB + Architect + PO + QA + Segurança | Pré-desenvolvimento wave | 90 min | Videochamada | PRD, ADRs, NFRs, Test Plan, Traceability | Ata Gate 2 / CR se needed |
| **Gate 3 Review (Go-Live)** | CCB + DevOps + QA + Segurança | Pré-deploy produção | 60 min | Videochamada | Test Report, Runbook, Release Notes, Rollback Plan | Ata Gate 3 / Go/No-Go |
| **Sprint/Wave Review (Demo)** | GP + Equipe + Stakeholders interessados | Fim de cada wave | 45 min | Videochamada | Demo funcional; feedback; ajustes | Gravação / Notes no Projects |
| **Retrospectiva / Lições Aprendidas** | Equipe Técnica | Fim de cada Wave / Marco | 60 min | Videochamada | What went well, what to improve, action items | Lições Aprendidas (MF) |
| **Post-Mortem (Blameless)** | Envolvidos no incidente | Pós-incidente grave (P1/P0) | 60-90 min | Videochamada | Timeline, Root Cause (5 Whys), Preventive Actions | Post-Mortem Report |

---

## 3. REPOSITÓRIOS DE INFORMAÇÃO (Single Source of Truth)

| Repositório | Conteúdo | Acesso | Frequência Atualização | Responsável |
|---|---|---|---|---|
| **GitHub Projects (Kanban)** | Backlog, Sprint/Wave board, WIP limits (≤3/pessoa), status cards | Equipe + GP (write), Stakeholders (read) | Contínuo | agent-pm |
| **Repositório Git (docs/)** | Constitution, ADRs, Specs, Templates, RAID Log, Reports, Business Case | Público (repo público) / Equipe (write) | Por commit | agent-project-analyst |
| **GitHub Releases** | Release Notes, binários (se houver), changelog | Público | Por Release | agent-devops |
| **GitHub Actions / CI** | Build status, test results, coverage, quality gates | Equipe + GP | Contínuo (por push) | agent-devops |
| **CCB Log** | Decisões formais, ratificações, emendas, Gates | Equipe + GP | Por decisão CCB | agent-project-analyst |
| **Discord (Servidor COGME)** | Comunicação async daily, alerts, beta feedback, agentes | Equipe + Beta Testers | Contínuo | GP / Mods |

---

## 4. ESCALAÇÃO DE COMUNICAÇÃO (Escalação de Issues/Riscos)

| Nível | Gatilho | Quem Aciona | Para Quem | Prazo Resposta | Canal |
|---|---|---|---|---|---|
| **Nível 1 — Equipe** | Impedimento técnico resolvível internamente | Dev/QA | Tech Lead / agent-pm | 4h (horário útil) | Discord / Issue GitHub |
| **Nível 2 — GP / Tech Lead** | Risco Alto/Crítico, desvio prazo >20%, CR impacto Alto | Tech Lead / agent-pm | GP (CCB) | 24h | Reunião + Status Report extraordinário |
| **Nível 3 — CCB / Patrocinador** | Bloqueador crítico (produção parada, segurança, compliance, orçamento) | GP | CCB (GP único) + Stakeholders FATEC | Imediato (até 2h) | Videochamada de emergência + Ata |
| **Nível 4 — Governança Externa** | Auditoria, regulatório, legal, FATEC institucional | GP | Direção FATEC / Órgãos reguladores | Conforme prazo legal | Ofício / E-mail formal |

---

## 5. COMUNICAÇÃO DE MUDANÇAS (Change Communication)

| Tipo de Mudança | Comunicado Para | Canal | Prazo Pós-Aprovação | Responsável |
|---|---|---|---|---|
| CR Aprovado (qualquer) | Equipe Técnica + GP | GitHub Issue/PR + Discord announcement | 24h | agent-project-analyst |
| ADR Ratificada/Emendada | Equipe Técnica + GP | Commit message + Discord + CCB Log | Imediato (no commit) | agent-architect |
| Nova Spec / Spec Atualizada | Equipe Técnica + PO | PR + GitHub Projects card | 24h | agent-sdd-specialist |
| Release / Deploy Produção | Todos Stakeholders | GitHub Release + Discord + E-mail (se crítico) | No deploy | agent-devops |
| Incidente Produção (P1/P0) | GP + Equipe + Stakeholders afetados | Discord (urgente) + Post-Mortem depois | Imediato (alerta) + 48h (report) | agent-devops / agent-digital-security |
| Mudança de Stakeholder Chave | Todos | E-mail formal + Atualização Stakeholder Register | 24h | agent-pm |

---

## 6. COMUNICAÇÃO DE RISCOS E ISSUES (Risk/Issue Communication)

| Item | Frequência | Canal | Destinatários | Responsável |
|---|---|---|---|---|
| **RAID Log Atualização** | Semanal (segundas) | Commit em `docs/governanca/raid-log.md` + Discord #governance | GP + Equipe | agent-project-analyst |
| **Risco Crítico Novo (Exposição ≥15)** | Imediato | Discord @GP + Issue GitHub (label: risk-critical) | GP + Tech Leads | Dono do risco |
| **Issue Bloqueador (Severidade Crítica)** | Imediato | Discord @team + Issue GitHub (label: blocker) | Equipe toda | Quem detectou |
| **Resolução de Risco/Issue Crítico** | No fechamento | Discord #governance + Status Report | GP + Equipe | Dono |

---

## 7. CONTROLE DE VERSÕES

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-pm | Criação inicial (baseado no template + Stakeholder Register) | GP (CCB) |

> **Revisão Obrigatória**: A cada Gate (1, 2, 3), mudança de stakeholder chave, ou a cada 2 meses (o que ocorrer primeiro).