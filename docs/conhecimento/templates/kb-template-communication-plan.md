---
id: kb-template-communication-plan
title: Template de Plano de Comunicação — COGME
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
  - PMBOK 7ª — Domínio Partes Interessadas (Communications Management)
  - constitution.md Art. 4 (Comunicação e transparência)
  - OKB §7 (SSOT operacional — GitHub Projects)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
  - template
  - governanca
  - comunicacao
  - stakeholders
  - pmbok
---

# Template de Plano de Comunicação — COGME

> **Finalidade**: Definir **quem** recebe **qual** informação, com **qual frequência**, por **qual canal**, e **quem é responsável** por enviar. Alinha expectativas, evita ruído e garante rastreabilidade (auditoria). Revisado a cada Gate e mudança de stakeholder relevante.

---

## 1. MATRIZ DE COMUNICAÇÃO (Stakeholders × Informações)

| Stakeholder / Grupo | Papel / Interesse | Informação Necessária | Formato / Canal | Frequência | Responsável (Emissor) | Confirmação de Recebimento |
|---|---|---|---|---|---|---|
| **GP Leonardo (CCB único)** | Patrocinador / Decisor final | Status executivo, decisões Gate, CRs, riscos críticos, orçamento | Status Report (Markdown) + Reunião 1:1 | Semanal + Ad-hoc Gates | agent-project-analyst | Assinatura no Status Report / Ata CCB |
| **Equipe Técnica (Devs, QA, Arch, DevOps, DBA)** | Executores | Sprint/Wave goals, impedimentos, decisões técnicas (ADRs), mudanças (CRs), deploy | GitHub Projects (SSOT) + Daily Standup (async/discord) + ADR/CR notificações | Contínuo (SSOT) + Diário (standup) | agent-pm / agent-devops | Check no Projects / Reação em Issue/PR |
| **FATEC / Coordenação Curso** | Governança acadêmica | Marco M1–M4, entregas acadêmicas, compliance LGPD, lições aprendidas | Relatório formal (PDF/Markdown) + Apresentação | Por Marco (M1, M2, M3, M4) + Final | agent-project-analyst | Assinatura de aceite / Termo de encerramento |
| **Stakeholders Técnicos Externos** (se houver) | Fornecedores API, BCB/PTAX | Contratos de API, SLAs, mudanças breaking, depreciações | E-mail técnico + Changelog (Release Notes) | Ad-hoc (mudança) + Por Release | agent-backend-dev | Confirmação de leitura / Issue de acompanhamento |
| **Usuários Finais (Beta/Testers)** | Validadores UAT | Release Notes, guias de uso, known issues, canais de feedback | GitHub Releases + Docs site (se houver) + Formulário feedback | Por Release | agent-frontend-dev / agent-qa-sdet | Issues de feedback / UAT results |

---

## 2. EVENTOS DE COMUNICAÇÃO RECORRENTES

| Evento | Participantes | Frequência | Duração | Canal | Pauta Padrão | Artefato Gerado |
|---|---|---|---|---|---|---|
| **Daily Standup (Async)** | Equipe Técnica | Diária (dias úteis) | 15 min | Discord / GitHub Discussions | O que fiz? O que farei? Impedimentos? | Atualização no Projects (SSOT) |
| **Weekly Status Sync** | GP + Tech Leads | Semanal (segundas) | 30 min | Videochamada / Presencial | Status Report review, riscos, CRs, decisões | Status Report assinado |
| **Gate 1 Review (Início)** | CCB + Equipe | Início do projeto / novo marco | 60 min | Videochamada | Charter, Business Case, Orçamento, Riscos iniciais | Ata Gate 1 / CR se needed |
| **Gate 2 Review (Desenho)** | CCB + Arquitetura + PO + QA | Pré-desenvolvimento wave | 90 min | Videochamada | PRD, ADRs, NFRs, Test Plan, Traceability | Ata Gate 2 / CR se needed |
| **Gate 3 Review (Go-Live)** | CCB + DevOps + QA + Segurança | Pré-deploy produção | 60 min | Videochamada | Test Report, Runbook, Release Notes, Rollback Plan | Ata Gate 3 / Go/No-Go |
| **Retrospectiva / Lições Aprendidas** | Equipe Técnica | Fim de cada Wave / Marco | 60 min | Videochamada | What went well, what to improve, action items | Lições Aprendidas (MF) |
| **Post-Mortem (Blameless)** | Envolvidos no incidente | Pós-incidente grave (P1/P0) | 60-90 min | Videochamada | Timeline, Root Cause (5 Whys), Preventive Actions | Post-Mortem Report |

---

## 3. REPOSITÓRIOS DE INFORMAÇÃO (Single Source of Truth)

| Repositório | Conteúdo | Acesso | Frequência Atualização | Responsável |
|---|---|---|---|---|
| **GitHub Projects (Kanban)** | Backlog, Sprint/Wave board, WIP limits, status cards | Equipe + GP (write), Stakeholders (read) | Contínuo | agent-pm |
| **Repositório Git (docs/)** | Constitution, ADRs, Specs, Templates, RAID Log, Reports | Público (repo público) / Equipe (write) | Por commit | agent-project-analyst |
| **GitHub Releases** | Release Notes, binários (se houver), changelog | Público | Por Release | agent-devops |
| **GitHub Actions / CI** | Build status, test results, coverage, quality gates | Equipe + GP | Contínuo (por push) | agent-devops |
| **CCB Log** | Decisões formais, ratificações, emendas | Equipe + GP | Por decisão CCB | agent-project-analyst |

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
| Release / Deploy Produção | Todos Stakeholders | GitHub Release + E-mail (se crítico) | No deploy | agent-devops |
| Incidente Produção (P1/P0) | GP + Equipe + Stakeholders afetados | Discord (urgente) + Post-Mortem depois | Imediato (alerta) + 48h (report) | agent-devops / agent-digital-security |

---

## 6. CONTROLE DE VERSÕES DO PLANO

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-project-analyst | Criação inicial (template aprovado) | GP (CCB) |

> **Revisão Obrigatória**: A cada Gate (1, 2, 3), mudança de stakeholder chave, ou a cada 2 meses (o que ocorrer primeiro).