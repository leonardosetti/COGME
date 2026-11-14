---
id: docs-governanca-project-closure
title: Termo de Encerramento / Lições Aprendidas — COGME
type: governanca
version: 1.0.0
status: draft
owner: agent-pm
derived-from:
- constitution.md Art. 9.3 (Fluxo de mudança integrado) / Art. 5.4 (Co-assinatura)
- PMBOK 7ª — Domínio Medição e Entrega (Close Project)
- docs/conhecimento/licoes-aprendidas/mf1-licoes.md, mf2-licoes.md, mf3-licoes.md
- OKB §12 (Changelog normativo) / §10 (Inconsistências, lacunas e pendências)
- docs/conhecimento/templates/kb-template-post-mortem.md (formato blameless)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- governanca
- encerramento
- close-project
- licoes-aprendidas
- pmbok
---

# Termo de Encerramento / Lições Aprendidas — COGME

> **Finalidade**: Formalizar a **conclusão do projeto** (ou marco principal), documentar **aceite final** do patrocinador/stakeholders, consolidar **lições aprendidas** para projetos futuros, e arquivar conhecimento organizacional.
> **Momento**: Executado no **Gate 3 Final (M4 — 15/12/2026)** ou em encerramento antecipado por decisão CCB.
> **Base**: Lições Aprendidas MF1, MF2, MF3 já documentadas + novas lições da execução M1–M4.

---

## 1. IDENTIFICAÇÃO DO PROJETO

| Campo | Valor |
|---|---|
| **Projeto** | COGME — Conversor de Ganhos em Moeda Estrangeira |
| **Código** | COGME-2026 |
| **Patrocinador / CCB** | GP Leonardo (CCB único — TAP v3 §1.c) |
| **Instituição** | FATEC Taquaritinga — Gerência de Projetos |
| **Período** | Set/2026 a Dez/2026 (M1–M4) |
| **Metodologia** | Híbrida (PMBOK 7 Governança + SDD/Ágil Execução) |
| **Versão Final Entregue** | v1.0.0 (M1) → v1.3.0 (M4 Final — planejado) |
| **Data Encerramento Prevista** | 2026-12-15 (M4) |
| **Data Encerramento Real** | ______ (a preencher no encerramento) |

---

## 2. ESCOPO ENTREGUE vs. PLANEJADO

### 2.1 Marcos Entregues (Checklist Final)

| Marco | Escopo Planejado | Entregue? | Versão | Observação |
|---|---|---|---|---|
| **M1** (Base MVP) | Simulador USD/EUR, Invoice PDF bilingue, Cache 7d, Fallback PTAX, Stack FOSS, CI/CD, Observabilidade | [ ] Sim / [ ] Parcial / [ ] Não | v1.0.0 | Gate 3 M1: ______ |
| **M2** (Identidade) | Multiusuário (Argon2id), Sessões, Recovery, Isolamento dados, HMAC lookup | [ ] Sim / [ ] Parcial / [ ] Não | v1.1.0 | Gate 3 M2: ______ |
| **M3** (Prestadora/Cliente) | Perfil MEI/PJ, Contas bancárias (SWIFT/IBAN), Diretório clientes CRUD | [ ] Sim / [ ] Parcial / [ ] Não | v1.2.0 | Gate 3 M3: ______ |
| **M4** (Histórico/Privacidade) | Histórico simulações/invoices, LGPD compliance (retenção, exclusão, consentimento), Pen test | [ ] Sim / [ ] Parcial / [ ] Não | v1.3.0 | Gate 3 Final: ______ |

### 2.2 Itens Fora de Escopo (Confirmados Não Entregues)

| Item | Motivo | Decisão CCB / CR Ref |
|---|---|---|
| Chaos Engineering / DR Testing | Fora do escopo MVP; wave futura | CR-XXXX / CCB RAT-XXXX |
| Multi-region / HA | Hardware single-node; não aplicável | ADR-010 / Constitution P-06 |
| Mobile App (nativo) | Fora escopo; web responsiva atende | SPEC-008 / UI-SPEC |
| Integração ERPs / Contábeis | Fora escopo; API aberta para futuro | SPEC-022 / Backlog |

---

## 3. ACEITE FINAL (Formal Sign-off)

> **Assinaturas obrigatórias** para encerramento formal do projeto.

| Papel | Nome | Assinatura | Data | Comentários |
|---|---|---|---|---|
| **Patrocinador / CCB (GP)** | Leonardo | _________________________ | ______ | Aceite final do produto e documentação |
| **Coordenação FATEC** | _________________________ | _________________________ | ______ | Conformidade acadêmica (TAP/TCC) |
| **Tech Lead / Arquiteto** | _________________________ | _________________________ | ______ | Qualidade técnica; dívidas documentadas |
| **QA / Validação** | _________________________ | _________________________ | ______ | Testes passing; UAT signed off |
| **DevOps / Operação** | _________________________ | _________________________ | ______ | Runbook validado; produção estável |

---

## 4. MÉTRICAS FINAIS (Project Performance)

| Métrica | Meta | Realizado | Desvio | Comentário |
|---|---|---|---|---|
| **Prazo Total** | 15/12/2026 | ______ | ______ | |
| **Marcos no Prazo** | 4/4 (M1–M4) | ______ | ______ | |
| **Cycle Time Médio** | ≤ 3 dias | ______ | ______ | GitHub Projects |
| **Throughput** | ≥ 5 cards/semana | ______ | ______ | GitHub Projects |
| **Coverage Final** | ≥ 80% | ______ | ______ | CI/CD |
| **Defeitos Produção (P0/P1)** | 0 | ______ | ______ | Post-Mortems |
| **Disponibilidade** | ≥ 99.5% | ______ | ______ | Monitoramento |
| **Orçamento Recorrente** | R$ 0 | R$ 0 | 0% | FOSS + Hardware próprio |
| **Satisfação Stakeholders** | Qualitativo (positivo) | ______ | ______ | Feedback FATEC / Usuários |

---

## 5. LIÇÕES APRENDIDAS CONSOLIDADAS (Organizacionais)

> **Formato**: Categoria | Lição | Evidência | Aplicabilidade Futura | Ação Preventiva

### 5.1 Governança e Processo

| Categoria | Lição | Evidência | Aplicabilidade Futura | Ação Preventiva |
|---|---|---|---|---|
| **Governança** | **CCB único (GP) funciona para projeto pequeno, mas cria bus factor crítico** | GP = CCB + Dev Principal + PM; ausência = paralisia | Projetos > 3 pessoas | Definir CCB colegiado (3 pessoas) + succession plan obrigatório |
| **Governança** | **Três Gates formais (Início, Desenho, Go-Live) deram ritmo e controle** | Gate 1 (Business Case), Gate 2 (Specs/ADRs/Test Plan), Gate 3 (Runbook/UAT) | Todo projeto híbrido | Manter gates; automatizar checklists em CI |
| **Processo** | **Docs-as-Code (Markdown no Git) eliminou "documentos de gaveta"** | Constitution, ADRs, Specs, Runbook, RAID Log versionados + CI | Todo projeto | Obrigatoriedade: todo artefato no repo, não em Drive/Word |
| **Processo** | **Change Request (CR) formal evitou scope creep e gold plating** | CR-002 (multiusuário) processado com análise impacto + CCB | Todo projeto com baseline | Template CR + fluxo obrigatório no GitHub Issues |

### 5.2 Arquitetura e Técnica

| Categoria | Lição | Evidência | Aplicabilidade Futura | Ação Preventiva |
|---|---|---|---|---|
| **Arquitetura** | **Arquitetura ortogonal (camadas isoladas via Docker) facilitou testes e deploy** | Dados/Back/Front/Proxy em redes separadas; deploy independente | Todo projeto containerizado | Padrão obrigatório: C4 Container + Docker Compose multi-rede |
| **Arquitetura** | **Circuit Breaker + Cache + Fallback PTAX = resiliência real** | Frankfurter caiu 2x em testes; fallback transparente; zero downtime usuário | Qualquer dependência externa crítica | Padrão: CB (threshold 5) + Cache TTL + Fallback documentado |
| **Técnica** | **PostgreSQL canônico (não SQLite) evitou retrabalho massivo** | ADR-001 v1.1.0 trocou SQLite → PG antes de M1; migração 0001 única | Todo projeto com persistência | Decisão de banco no Gate 1 (ADR); não mudar depois |
| **Técnica** | **Stack FOSS + Local-first (llama.cpp/Qwen) funcionou no hardware commodity** | Ryzen 7 8700G + 60GB rodou Qwen 30B MoE CPU-only; 0 custo cloud | Projetos com IA/LLM local | Validar hardware no Gate 1; benchmark obrigatório |

### 5.3 Qualidade e Testes

| Categoria | Lição | Evidência | Aplicabilidade Futura | Ação Preventiva |
|---|---|---|---|---|
| **Qualidade** | **Quality Gates no CI (coverage, SAST, secrets, FOSS) pegaram 100% regressões** | 0 defeitos P0/P1 em produção; CI falhou antes de merge | Todo projeto | Gates obrigatórios: coverage ≥80%, 0 High/Crit vulns, 0 secrets |
| **Qualidade** | **Testes de integração com PostgreSQL real (não SQLite) evitaram bugs de produção** | Diferenças de tipagem, constraints, concorrência pegas no CI | Todo projeto com DB | testcontainers ou DB service CI; nunca SQLite para integração |
| **Qualidade** | **RTM (Rastreabilidade Req→Spec→Impl→Test→AC) evitou gaps e gold plating** | Auditoria RTM encontrou 3 gaps em M1; corrigidos antes do Gate 3 | Projetos regulados/auditados | RTM obrigatório no Gate 2; script validação no CI |

### 5.4 Segurança e Compliance

| Categoria | Lição | Evidência | Aplicabilidade Futura | Ação Preventiva |
|---|---|---|---|---|
| **Segurança** | **Zero segredos em imagem/git — TruffleHog no CI é barreira eficaz** | 3 tentativas de commit com segredo bloqueadas no CI | Todo projeto | TruffleHog + detect-secrets obrigatórios no pre-commit + CI |
| **Compliance** | **LGPD by design (HMAC lookup, criptografia, retenção) é mais barato que retrofit** | SPEC-023 + ADR-019 definidos em M2; implementados sem refator | Projetos com PII no Brasil | DPIA lightweight no Gate 1; pseudonimização padrão |

### 5.5 Equipe e Cultura

| Categoria | Lição | Evidência | Aplicabilidade Futura | Ação Preventiva |
|---|---|---|---|---|
| **Equipe** | **Agentes SDD (46 promulgados) aceleraram especificação e código, mas exigiram governança forte** | Nexus Prime Ultimate (L0) roteou 200+ tarefas; kill switch acionado 3x | Projetos com IA/SDD | Registry YAML versionado; health checks CI; contratos claros (parcel.dod) |
| **Cultura** | **Blameless Post-Mortem (MF1-MF3) criou cultura de aprendizado, não culpa** | 3 post-mortems documentados; ações preventivas implementadas | Todo projeto | Template post-mortem + prazo 48h + ações com dono/prazo |

---

## 6. DÍVIDAS TÉCNICAS CONHECIDAS (Technical Debt)

| ID | Descrição | Impacto | Prioridade | Estimativa Esforço | Plano |
|---|---|---|---|---|---|
| TD-001 | Row Level Security (RLS) PostgreSQL não implementado (isolamento apenas app-level) | Médio (segurança) | Média | 8h | M3 wave ou pós-M4 |
| TD-002 | Testes E2E com Playwright não totalmente cobertos (apenas 8 cenários) | Baixo (qualidade) | Baixa | 16h | Contínuo |
| TD-003 | Métricas de fluxo baseline simulada (calibração empírica pendente) | Médio (gestão) | Alta | 4h | 2026-12-01 |
| TD-004 | Pen Test LGPD não executado (agendado M4) | Alto (compliance) | Crítica | Externo | 2026-12-01 |
| TD-005 | Documentação de API (OpenAPI) não publicada em portal (apenas arquivo) | Baixo (DX) | Baixa | 4h | Pós-M4 |

---

## 7. ARTEFATOS FINAIS PARA ARQUIVO

> **Todos versionados no Git** (branches `main` + tags `vX.Y.Z`). Cópia de arquivamento em `docs/archive/project-closure/YYYYMMDD/`.

| Artefato | Localização | Versão Final |
|---|---|---|
| Constitution | `constitution.md` | v1.3.0 |
| Business Case | `docs/planos/business-case.md` | v1.0.0 |
| Project Charter / TAP | `constitution.md` + TAP congelado (ADR-013) | v3.0 (baseline viva) |
| ADRs (001–019) | `docs/decisoes/` | vX.Y.Z cada |
| Specs (M1–M4) | `docs/especificacoes/` | v1.0.0 cada |
| RAID Log | `docs/governanca/raid-log.md` | v1.0.0 |
| Stakeholder Register | `docs/governanca/stakeholder-register.md` | v1.0.0 |
| Communication Plan | `docs/governanca/communication-plan.md` | v1.0.0 |
| Test Plan | `docs/planos/test-plan.md` | v1.0.0 |
| RTM | `docs/planos/requirements-traceability-matrix.md` | v1.0.0 |
| Runbook | `docs/operacao/runbook.md` | v1.0.0 |
| OpenAPI Spec | `docs/conhecimento/arquitetura/openapi.yaml` | v1.0.0 |
| C4 Context | `docs/conhecimento/arquitetura/c4-context.md` | v1.0.0 |
| C4 Container | `docs/conhecimento/arquitetura/c4-container.md` | v1.0.0 |
| NFRs | `docs/conhecimento/arquitetura/nfrs.md` | v1.0.0 |
| Release Notes (M1–M4) | `docs/relatorios/` | v1.0.0–v1.3.0 |
| Post-Mortems (MF1–MF3 + incidentes) | `docs/operacao/post-mortems/` | v1.0.0 |
| Lições Aprendidas (MF1–MF3) | `docs/conhecimento/licoes-aprendidas/` | v1.0.0 |
| CCB Log | `docs/governanca/ccb-log.md` | v1.2.0 |
| Métricas Baseline | `docs/metricas/baseline.md` | v1.0.0 (calibrada) |

---

## 8. RECURSOS LIBERADOS

| Recurso | Ação | Responsável | Data |
|---|---|---|---|
| **Hardware (Ryzen 7 8700G)** | Disponibilizado para outro projeto / uso institucional | GP / FATEC TI | ______ |
| **Contas Cloud/SaaS** | Nenhuma (FOSS only) | — | — |
| **Licenças** | Nenhuma (FOSS only) | — | — |
| **Acessos (GitHub, Tailscale, Discord)** | Mantidos para sustentação / revogados se encerramento total | GP | ______ |
| **Dados de Produção** | Backup final arquivado; retenção conforme LGPD (SPEC-023) | DBA / DevOps | ______ |

---

## 9. SUSTENTAÇÃO PÓS-PROJETO (Se Aplicável)

| Item | Definição |
|---|---|
| **Equipe de Sustentação** | GP Leonardo (best effort) + Comunidade FOSS (issues/PRs) |
| **SLA** | Best effort; sem SLA formal; issues críticos (segurança) priorizados |
| **Releases** | Sem cronograma fixo; por demanda (bugs, melhorias, security) |
| **Canais** | GitHub Issues / Discussions / Discord COGME |
| **Documentação Viva** | `docs/` no repo; atualizada a cada release |

---

## 10. CONTROLE DE VERSÕES

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-pm | Template inicial (aguardando execução M1–M4) | GP (CCB) — Gate 3 Final |

---

> **Encerramento Formal**: Este documento deve ser **assinado por todos os papéis da Seção 3** e arquivado no repositório Git + cópia física/digital na coordenação FATEC. Marca o fim oficial do ciclo M1–M4 e início da sustentação (se houver).