---
id: plan-business-case
title: "Business Case — COGME (Conversor de Ganhos em Moeda Estrangeira)"
type: plano
version: 1.0.0
status: draft
owner: agent-pm
derived-from:
  - constitution.md Art. 3 (Objetivos SMART) / TAP §3 (Inovação) / TAP §11 (Orçamento Zero)
  - OKB §3 (Estado canônico) / §6 (Métricas e fluxo)
  - canon-stack-sdd.md (Arquitetura convergente, hardware, stack FOSS)
  - PMBOK 7ª — Domínio Partes Interessadas e Planejamento (Business Case)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
  - plano
  - business-case
  - pmbok
  - viabilidade
  - investimento
---

# Business Case — COGME

> **Finalidade**: Justificar o investimento (tempo, esforço, hardware, oportunidade) no projeto COGME, comparando **custos**, **benefícios esperados** e **ROI** (Retorno sobre Investimento) em formato adequado à realidade **orçamento zero recorrente, FOSS, hardware local, acadêmico-profissional**.
> **Separado do OKB** por decisão CCB (2026-11-14) — artefato de governança executiva, não operacional.
> **Gate 1 (Início)**: Requer ratificação CCB antes de Gate 2 (Desenho).

---

## 1. SUMÁRIO EXECUTIVO

| Item | Detalhe |
|---|---|
| **Projeto** | COGME — Conversor de Ganhos em Moeda Estrangeira |
| **Patrocinador / CCB** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| **Instituição** | FATEC Taquaritinga — Gerência de Projetos |
| **Período** | Set/2026 a Dez/2026 (M1–M4) + sustentação 2027 |
| **Metodologia** | Híbrida (PMBOK 7 governança executiva + SDD/Ágil execução) |
| **Orçamento Recorrente** | **R$ 0,00** (FOSS only, hardware próprio, zero cloud) |
| **Investimento Principal** | Hardware (já existente: Ryzen 7 8700G + 60GB RAM) + Esforço humano (equipe 3 pessoas) |
| **ROI Esperado** | Qualitativo: Entrega acadêmica (TCC/TAP), portfólio profissional, ferramenta útil para freelancers/devs brasileiros, base de conhecimento reutilizável |

---

## 2. PROBLEMA / OPORTUNIDADE

### 2.1 Contexto
Profissionais brasileiros que recebem em moeda estrangeira (developers, freelancers, consultores, creators) enfrentam:
- **Cálculo manual** propenso a erro (planilhas, cotações desatualizadas)
- **Falta de documento formal** (invoice) compatível com requisitos brasileiros (PT-BR) e internacionais (EN)
- **Dependência de SaaS pagos** ou planilhas complexas para histórico e simulação
- **Risco cambial** não visualizado (volatilidade, spread, fontes não oficiais)

### 2.2 Dor Quantificada (Estimativa)
| Dor | Impacto Estimado | Fonte |
|---|---|---|
| Tempo gasto em cálculo manual por mês | 2–4 horas / profissional | Entrevistas informais (n=12) |
| Erros de cotação / spread oculto | 0.5–2% do valor recebido | Relatos comunidade |
| Ausência de invoice bilingue profissional | Impede fechamento com clientes internacionais | Feedback direto |
| Ansiedade cambial (não saber valor real até cair na conta) | Intangível — bem-estar | Qualitativo |

---

## 3. SOLUÇÃO PROPOSTA (COGME MVP)

### 3.1 Escopo M1–M4 (Até 15/12/2026)
| Marco | Entrega Principal | Valor para Usuário |
|---|---|---|
| **M1** | Simulador USD/EUR → BRL (latência ≤2s), Invoice PDF bilingue (PT/EN), Cache local 7d, Fallback PTAX | Cálculo instantâneo confiável + documento profissional |
| **M2** | Identidade multiusuário (Argon2id, sessões, recovery), Isolamento de dados por usuário | Uso compartilhado seguro (equipes, famílias, contadores) |
| **M3** | Perfil prestadora (MEI/PJ), Contas bancárias (SWIFT/IBAN), Diretório de clientes | Gestão completa de recebíveis internacionais |
| **M4** | Histórico de simulações/invoices, Privacidade LGPD (retenção, exclusão, consentimento) | Conformidade + visão temporal de ganhos |

### 3.2 Diferenciais Competitivos
| Diferencial | Descrição |
|---|---|
| **100% FOSS + Local** | Zero custo recorrente, zero vendor lock-in, soberania de dados (LGPD nativo) |
| **PTAX como âncora oficial** | Não depende apenas de APIs privadas; fallback obrigatório para fonte governamental |
| **Invoice PDF bilingue nativo** | PT-BR (legal) + EN (internacional) — pronto para enviar ao cliente |
| **Stack acadêmica-profissional** | FastAPI, PostgreSQL, Docker, CI/CD, SDD, ADRs — portfolio real |
| **Hardware commodity** | Roda em laptop/desktop comum (CPU-only, sem GPU) |

---

## 4. ANÁLISE DE CUSTOS (Investimento Total)

### 4.1 Custos Diretos (Já Incorridos / Comprometidos)

| Item | Custo | Natureza | Status |
|---|---|---|---|
| Hardware (Ryzen 7 8700G + 60GB RAM + SSD) | ~R$ 5.500 | CAPEX (já existente, uso compartilhado) | Incorrido |
| Tempo equipe (3 pessoas × ~400h total estimado M1–M4) | ~R$ 0 (acadêmico / voluntário) | OPEX (horas alocadas) | Comprometido |
| Domínio / DNS / TLS (se produção pública) | ~R$ 50/ano | OPEX opcional | Não decidido |
| Ferramentas FOSS (GitHub Free, Docker, PostgreSQL, etc.) | R$ 0 | OPEX | Incorrido |

**Total Investimento Direto**: **~R$ 5.500** (hardware já alocado, sem novo desembolso)

### 4.2 Custos de Oportunidade
| Recurso | Alternativa | Valor Estimado |
|---|---|---|
| Horas equipe (1200h total) | Projetos remunerados / estágio | R$ 30.000–60.000 (mercado júnior) |
| Hardware | Outro projeto / uso pessoal | Baixo (hardware multiuso) |

---

## 5. BENEFÍCIOS ESPERADOS

### 5.1 Benefícios Tangíveis (Mensuráveis)
| Benefício | Métrica | Meta M4 (15/12/2026) | Meta 2027 (Sustentação) |
|---|---|---|---|
| **Usuários ativos** | nº usuários únicos/semana | 20 (beta testers FATEC + comunidade) | 200+ |
| **Simulações realizadas** | total / mês | 500 | 5.000 |
| **Invoices gerados** | total / mês | 100 | 1.000 |
| **Latência P95 (simulate)** | segundos | ≤ 2s | ≤ 1.5s |
| **Disponibilidade** | % uptime | ≥ 99.5% | ≥ 99.9% |
| **Cobertura de testes** | % linhas | ≥ 80% | ≥ 90% |
| **Defeitos em produção (P0/P1)** | count / mês | 0 | 0 |

### 5.2 Benefícios Intangíveis (Qualitativos)
| Benefício | Descrição | Evidência |
|---|---|---|
| **Entrega Acadêmica** | TAP/FATEC aprovado, banca satisfeita | Documentação completa, defesa agendada |
| **Portfólio Profissional** | Projeto real, FOSS, arquitetura documentada, CI/CD | GitHub público, releases, ADRs, specs |
| **Conhecimento Reutilizável** | Stack SDD, agentes, templates, governança | `.planning/`, `docs/`, `constitution.md` replicável |
| **Comunidade FOSS** | Contribuição para ecossistema (ex: llama.cpp, FastAPI) | Issues, PRs, documentação |
| **Soberania Digital** | Demonstração de stack 100% local, LGPD by design | Artigo técnico, palestra FATEC |

---

## 6. ANÁLISE DE VIABILIDADE (Viability Assessment)

### 6.1 Técnica — **VIÁVEL** ✅
- Stack validada (ADR-001, canon-stack-sdd): FastAPI + PostgreSQL + Docker + Jinja2/HTMX/Tailwind + llama.cpp/Qwen
- Hardware suficiente para inferência local (benchmarks OKB)
- Arquitetura ortogonal (ADR-010) — camadas isoladas, paridade dev/test/prod
- Riscos técnicos mapeados no RAID Log (RISK-001 a 008) com mitigações

### 6.2 Financeira — **VIÁVEL** ✅ (Orçamento Zero Recorrente)
- CAPEX já incorrido (hardware próprio)
- OPEX = R$ 0 (FOSS, local, sem cloud)
- Esforço humano = alocado no cronograma acadêmico/profissional
- Nenhum contrato de licença, SaaS, ou provedor cloud

### 6.3 Operacional — **VIÁVEL COM RESSALVAS** ⚠️
| Ressalva | Mitigação |
|---|---|
| Bus factor baixo (GP = CCB + dev principal) | Documentação viva, onboarding, succession plan draft |
| Métricas baseline simuladas | Calibração empírica a partir de 01/11/2026 (GitHub Projects) |
| Ausência de Runbook formal (Gate 3) | **Ação prioritária** — entrega até 2026-11-30 (RISK-008) |
| Pen test LGPD não agendado | Agendar até 2026-11-20 para Gate 3 Final (DEP-005) |

### 6.4 Legal / Compliance — **VIÁVEL** ✅
- LGPD by design (Constitution Art. 7, P-02, P-03, P-04, ADR-017, ADR-019)
- Marco Civil da Internet (neutralidade, liberdade, privacidade)
- Zero PII desnecessária; criptografia, HMAC, retenção controlada
- FOSS only — licenças OSI-approved (MIT, BSD, Apache, PostgreSQL, PSF)

### 6.5 Cronograma — **VIÁVEL COM RISCO MÉDIO** ⚠️
- M1–M4 até 15/12/2026 (10 semanas restantes a partir de 14/11)
- Dependências críticas: CCB ratificação specs (DEP-004), Runbook (DEP-003), Pen test (DEP-005)
- Buffer: 2 semanas (até 29/12) para contingência

---

## 7. ALTERNATIVAS ANALISADAS

| Alternativa | Descrição | Prós | Contras | Decisão |
|---|---|---|---|---|
| **A. COGME (Escolhida)** | Stack FOSS local, SDD, hardware próprio, orçamento zero | Soberania, custo zero, aprendizado, portfolio | Esforço inicial maior; manutenção própria | **APROVADA** (CCB 19/09/2026) |
| **B. SaaS Existente (Wise, Remessa Online, etc.)** | Usar ferramenta pronta | Zero esforço dev; suporte; compliance pronto | Custo recorrente; vendor lock-in; dados na nuvem; sem personalização | **REJEITADA** (violada P-01, P-02, P-03, orçamento zero) |
| **C. Planilha Google Sheets / Excel Avançado** | Modelo calculador em planilha | Baixo esforço inicial; familiar | Propenso a erro; sem invoice PDF; sem histórico; sem multiuser; sem API | **REJEITADA** (não atende REQ-01 a REQ-10) |
| **D. Cloud + GPU (AWS/GCP + GPU)** | Inferência LLM na nuvem | Escalabilidade; modelos maiores | Custo recorrente alto; vendor lock-in; dados saem do Brasil; viola P-01, P-02, P-03 | **REJEITADA** (violada restrições constitucionais) |
| **E. Abordagem Waterfall Tradicional** | Especificação completa upfront, depois dev | Previsibilidade teórica | Não comporta escopo emergente; documentação pesada; não ágil | **REJEITADA** (PMBOK 7 Tailoring → Híbrido) |

---

## 8. ROI (Retorno sobre Investimento) — **Qualitativo + Proxy Quantitativo**

> **Nota**: Projeto orçamento zero recorrente + acadêmico → ROI financeiro direto não aplicável. Usa-se **ROI Proxy** (valor entregue / esforço investido).

### 8.1 ROI Proxy Calculation
| Componente | Valor Atribuído (Proxy) | Base |
|---|---|---|
| **Entrega Acadêmica (TAP/TCC)** | R$ 50.000 | Valor de mercado de conclusão de curso + banca |
| **Portfólio Profissional (3 pessoas)** | R$ 30.000 | Aumento employability / taxa hora júnior→pleno |
| **Ferramenta Utilitária (usuários reais)** | R$ 20.000 | Economia de tempo usuários (2h/mês × 20 users × 12m × R$ 50/h) |
| **Conhecimento Reutilizável (Stack SDD + Governança)** | R$ 40.000 | Aplicável em projetos futuros (evita retrabalho) |
| **Contribuição FOSS / Comunidade** | R$ 10.000 | Reputação, networking, convites |
| **TOTAL BENEFÍCIOS (Proxy)** | **R$ 150.000** | |
| **CUSTO TOTAL (Hardware + Oportunidade)** | **R$ 35.500** | R$ 5.500 HW + R$ 30.000 oportunidade (conservador) |
| **ROI PROXY** | **322%** | (150.000 - 35.500) / 35.500 |

### 8.2 Payback Period
- **Imediato** (hardware já pago, benefícios acadêmicos/conhecimento iniciam no dia 1)
- **Break-even financeiro proxy**: Mês 2 (portfólio + primeiros usuários beta)

---

## 9. RISCOS DE NEGÓCIO (Business Risks) — Resumo do RAID Log

| Risco | Prob. | Impacto | Mitigação Principal |
|---|---|---|---|
| Não entrega no prazo acadêmico (15/12/2026) | Média | Crítico | Scope management rigoroso; M1–M3 core, M4 nice-to-have; buffer 2 semanas |
| Falha de hardware irrecuperável | Baixa | Crítico | Backup de configuração (Git); recovery plan; hardware commodity substituição < 48h |
| Mudança regulatória (LGPD, câmbio) | Baixa | Alto | Monitoramento jurídico; arquitetura adaptável (ADRs); FOSS facilita migração |
| Baixa adoção usuários reais | Média | Médio | Beta program FATEC; feedback loop; UAT rigoroso; marketing orgânico (GitHub, LinkedIn) |

---

## 10. RECOMENDAÇÃO E DECISÃO CCB

### 10.1 Recomendação
**APROVAR** o Business Case e autorizar:
1. Continuidade do projeto nos marcos M1–M4 (até 15/12/2026)
2. Alocação de esforço da equipe (3 pessoas) conforme cronograma
3. Priorização das ações de mitigação de riscos críticos (Runbook, Pen Test, CCB specs)
4. Calibração de métricas empíricas a partir de 01/11/2026

### 10.2 Decisão CCB (Aguardando Ratificação)

| Campo | Valor |
|---|---|
| **Decisão** | [ ] **APROVADO**  [ ] **APROVADO COM CONDIÇÕES**  [ ] **REJEITADO**  [ ] **DEFERIDO** |
| **Condições** | (se aplicável) |
| **Assinatura GP Leonardo (CCB único)** | _________________________ |
| **Data** | YYYY-MM-DD |
| **Instrumento** | Prompt expresso CCB / RAT-2026-11-XX-XX |

---

## 11. CONTROLE DE VERSÕES

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-pm | Criação inicial (separado do OKB por decisão CCB) | Aguardando CCB |

---

> **Próxima Revisão**: Pós-Gate 1 (ratificação CCB) ou em 2026-11-28 (o que ocorrer primeiro).