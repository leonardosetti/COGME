---
id: docs-governanca-stakeholder-register
title: Registro de Partes Interessadas (Stakeholder Register) — COGME
type: governanca
version: 1.0.0
status: ativo
owner: agent-pm
derived-from:
- PMBOK 7ª — Domínio Partes Interessadas (Stakeholder Register)
- constitution.md Art. 4 (Comunicação e transparência)
- docs/conhecimento/templates/communication-plan-template.md §1 (Matriz de Comunicação)
- OKB §7 (SSOT operacional — GitHub Projects)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- governanca
- stakeholders
- pmbok
- comunicacao
---

# Registro de Partes Interessadas — COGME

> **Finalidade**: Mapeamento formal de **todas as partes interessadas** (stakeholders) do projeto: identificação, expectativas, influência, interesse, necessidades de comunicação e estratégia de engajamento. Vai além da Matriz RACI (que foca em responsabilidades por entrega) — este registro foca em **relacionamento e gestão de expectativas**.
> **Base para**: Plano de Comunicação, Análise de Impacto de Mudanças (CR), Gestão de Riscos (RAID), Gate Reviews.

---

## 1. MAPEAMENTO DE STAKEHOLDERS (Identificação Completa)

| ID | Nome / Grupo | Cargo / Função | Organização | Categoria | Contato Principal |
|---|---|---|---|---|---|
| **SH-001** | **Leonardo (GP)** | Gerente de Projeto / CCB único / Desenvolvedor Principal | FATEC Taquaritinga | **Patrocinador / Decisor / Executor** | GitHub: @leonardosetti / Discord / E-mail institucional |
| **SH-002** | **Coordenação Curso FATEC** | Coordenador(a) de Curso / Responsável TCC/TAP | FATEC Taquaritinga | **Governança Acadêmica / Validador Final** | E-mail institucional / Reuniões formais |
| **SH-003** | **Banca Avaliadora TCC** | Professores avaliadores (3–5) | FATEC Taquaritinga | **Avaliador Externo / Aceite Final** | Via coordenação / Sessão de defesa |
| **SH-004** | **Equipe Técnica Core** (3 pessoas) | Dev Backend, Dev Frontend, DevOps/QA | Projeto COGME | **Equipe de Entrega / Executores** | GitHub / Discord / Daily async |
| **SH-005** | **Agentes SDD/IA** (46 promulgados) | Agentes especialistas (Arch, Backend, Frontend, QA, Security, etc.) | Ecossistema COGME | **Força de Trabalho Automatizada** | Nexus Prime Ultimate (L0) / Registry YAML |
| **SH-006** | **Beta Testers / Usuários Piloto** | Alunos FATEC, freelancers, devs comunidade | Externo / Comunidade | **Validadores UAT / Feedback** | GitHub Issues / Discord / Formulário |
| **SH-007** | **Banco Central do Brasil (BCB)** | Provedor API PTAX (fallback oficial) | Governo Federal | **Fornecedor Crítico Externo / Dependência** | API pública / Documentação técnica |
| **SH-008** | **Frankfurter API** | Provedor API primária de cotações | Serviço terceiros FOSS | **Fornecedor Primário Externo / Dependência** | API pública / GitHub / Documentação |
| **SH-009** | **Comunidade FOSS / GitHub** | Mantenedores FastAPI, PostgreSQL, Docker, llama.cpp, Qwen | Ecossistema Open Source | **Fornecedores de Stack / Pares** | GitHub / Fóruns / Issues |
| **SH-010** | **Família / Dependentes do GP** | Impactados por dedicação de tempo | Pessoal | **Impactados Indiretos / Suporte** | Pessoal |

---

## 2. ANÁLISE DE PODER / INTERESSE (Power/Interest Matrix)

> **Classificação**: **Alto Poder** = pode decidir/parar o projeto; **Alto Interesse** = afetado diretamente ou tem stakes alto.

| Stakeholder | Poder | Interesse | Quadrante | Estratégia de Engajamento |
|---|---|---|---|---|
| **SH-001 (GP/CCB)** | **ALTO** | **ALTO** | **Gerenciar de Perto (Key Player)** | Decisor único; envolvido em tudo; comunicação direta, diária; aprovação formal Gates/CRs |
| **SH-002 (Coordenação FATEC)** | **ALTO** | **MÉDIO** | **Manter Satisfeito** | Relatórios formais por marco; apresentações agendadas; aceite final TCC; não microgerência |
| **SH-003 (Banca TCC)** | **ALTO** (no final) | **BAIXO** (até defesa) | **Monitorar** | Apenas na defesa; documentação completa prévia; zero surpresas |
| **SH-004 (Equipe Core)** | **MÉDIO** | **ALTO** | **Manter Informado + Engajar** | Daily async; decisão técnica delegada; autonomia com alinhamento; retrospectivas |
| **SH-005 (Agentes SDD)** | **MÉDIO** (execução) | **ALTO** (domínio) | **Engajar Ativamente** | Roteamento via Nexus; contratos claros; health checks; feedback loop |
| **SH-006 (Beta Testers)** | **BAIXO** | **ALTO** | **Manter Informado + Consultar** | UAT estruturado; canal feedback fácil; reconhecimento público; priorizar bugs reportados |
| **SH-007 (BCB/PTAX)** | **MÉDIO** (dependência) | **BAIXO** | **Monitorar + Gerenciar Dependência** | SLA implícito (público); monitoramento uptime; fallback documentado; plano B se descontinuado |
| **SH-008 (Frankfurter)** | **MÉDIO** (dependência) | **BAIXO** | **Monitorar + Gerenciar Dependência** | SLA implícito (FOSS); monitoramento; circuit breaker; cache 7d reduz dependência |
| **SH-009 (Comunidade FOSS)** | **BAIXO** | **BAIXO** | **Monitorar** | Acompanhar releases/security advisories; contribuir de volta (issues/PRs); usar versões estáveis |
| **SH-010 (Família GP)** | **BAIXO** | **MÉDIO** | **Considerar** | Equilíbrio vida/trabalho; comunicar marcos importantes; não decisório |

---

## 3. EXPECTATIVAS E REQUISITOS POR STAKEHOLDER

| Stakeholder | Expectativas Principais | Requisitos de Comunicação | Preocupações / Riscos Percebidos |
|---|---|---|---|
| **SH-001 (GP/CCB)** | Entrega no prazo (15/12/2026); qualidade; governança auditável; portfolio | Status Report semanal; CCB Gates; RAID Log; Decisões técnicas (ADRs) | Escopo creep; burnout; bus factor; qualidade técnica |
| **SH-002 (Coordenação)** | TAP/TCC conforme normas FATEC; documentação completa; defesa tranquila | Relatório formal por marco (M1–M4); versão final impressa/digital; cronograma | Não conformidade acadêmica; prazos institucionais rígidos |
| **SH-003 (Banca)** | Rigor técnico; inovação; clareza na apresentação; contribuição acadêmica | Acesso antecipado à documentação (15 dias antes); slides; demo funcional | "Caixa preta" IA/SDD; falta de fundamentação teórica; escopo vago |
| **SH-004 (Equipe)** | Clareza de prioridades; autonomia técnica; ferramentas boas; reconhecimento | Daily async; GitHub Projects (SSOT); specs claras (ACs); code review construtivo | Burnout; specs mudando; dívida técnica; falta de direção |
| **SH-005 (Agentes)** | Contexto claro; contratos estáveis; feedback rápido; saúde monitorada | Nexus routing; registry YAML atualizado; CI/CD health checks; parcel.dod | Contexto desatualizado; contratos quebrados; kill switch acionado |
| **SH-006 (Beta Testers)** | Ferramenta que funciona; resolve dor real; fácil de usar; suporte rápido | UAT scripts claros; canal direto (Discord/GitHub); release notes; agradecimento | Bugs críticos; UX confusa; falta de feedback loop; abandono |
| **SH-007 (BCB)** | Uso respeitoso da API; cache adequado; não sobrecarga | Monitoramento de erros 429/5xx; User-Agent identificável; cache 7d | Banimento por abuso; mudança de API sem aviso; instabilidade |
| **SH-008 (Frankfurter)** | Uso respeitoso; fallback se instável | Mesma que BCB | Mesma que BCB |
| **SH-009 (FOSS)** | Relato de bugs; PRs úteis; uso de versões estáveis; licenças respeitadas | Security advisories; release notes upstream; contribuição | Vulnerabilidades não corrigidas; breaking changes; abandono projeto |
| **SH-010 (Família)** | Equilíbrio; previsibilidade de tempo; saúde do GP | Comunicação de marcos críticos; "não perturbe" em deep work | Burnout GP; negligência pessoal; estresse transferido |

---

## 4. ESTRATÉGIA DE ENGAJAMENTO POR FASE

| Fase / Marco | Stakeholders Críticos | Ação de Engajamento | Frequência | Responsável |
|---|---|---|---|---|
| **Início (Gate 1)** | SH-001, SH-002 | Apresentação Business Case + Charter; alinhamento expectativas | Único (Gate 1) | GP |
| **Desenho (Gate 2 por Wave)** | SH-001, SH-004, SH-005 | Validação PRD/Specs/ADRs/NFRs/Test Plan; decisão técnica | Por wave (M1, M2, M3, M4) | GP + Architect |
| **Execução (Waves)** | SH-001, SH-004, SH-005 | Daily async; Sprint Review demo; Retrospectiva; Decisões técnicas (CR/ADR) | Diária / Semanal / Por wave | GP + Tech Leads |
| **Validação (Gate 3 / UAT)** | SH-001, SH-004, SH-006 | Test Report; Runbook demo; UAT execution; Go/No-Go | Por release / Gate 3 | GP + QA + DevOps |
| **Encerramento (TCC/TAP)** | SH-001, SH-002, SH-003 | Documentação final; Apresentação banca; Lições aprendidas; Termo aceite | Único (Defesa) | GP |
| **Pós-Projeto (Sustentação)** | SH-001, SH-006, SH-009 | Manutenção; Issues; Releases; Comunidade | Contínuo (best effort) | GP + Comunidade |

---

## 5. MATRIZ RACI (Responsabilidade por Entrega Principal) — *Resumo da Seção 8.3 do Template de Specs*

| Entrega / Atividade | GP (SH-001) | Coord. FATEC (SH-002) | Equipe Core (SH-004) | Agentes (SH-005) | Beta Testers (SH-006) |
|---|---|---|---|---|---|
| **Business Case / Charter** | **R/A** | C | I | I | I |
| **PRD / Specs** | A | I | **R** (PO/Dev) | **R** (Agentes especialistas) | C |
| **ADRs / Arquitetura** | A | I | C | **R/A** (Architect) | I |
| **Implementação Backend** | I | I | **R/A** (Backend Dev) | **R** (Backend Agent) | I |
| **Implementação Frontend** | I | I | **R/A** (Frontend Dev) | **R** (Frontend Agent) | I |
| **Testes / QA** | I | I | C | **R/A** (QA Agent) | **R** (UAT) |
| **DevOps / CI/CD / Deploy** | I | I | C | **R/A** (DevOps Agent) | I |
| **Segurança / LGPD** | A | I | C | **R/A** (Security Agent) | I |
| **Gate 1/2/3 Decisão** | **R/A** | C (Gate 1/3) | C | C | I (Gate 3) |
| **Documentação Final (TAP)** | **R/A** | A | **R** | C | I |

**Legenda**: R = Responsible (executa), A = Accountable (aprova), C = Consulted (consultado), I = Informed (informado)

---

## 6. CONTROLE DE MUDANÇAS DO REGISTRO

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-pm | Criação inicial (baseado no template aprovado) | GP (CCB) |

> **Revisão Obrigatória**: A cada Gate (1, 2, 3), mudança de stakeholder chave, ou a cada 2 meses. Atualizações registradas acima.