---
id: kb-template-status-report
title: Template de Status Report — Relatório Periódico de Desempenho
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
  - PMBOK 7ª — Domínio Medição (Work Performance Report)
  - README.md §10 (Métricas de fluxo atuais)
  - OKB §6 (Métricas e fluxo)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
  - template
  - governanca
  - status-report
  - metricas
  - pmbok
---

# Template de Status Report — COGME

> **Finalidade**: Relatório padronizado para stakeholders (GP, CCB, equipe, FATEC) com visibilidade de progresso, métricas, impedimentos e decisões. **Cadência**: Semanal (segundas-feiras) + Ad-hoc em Gates (Gate 2, Gate 3). **Formato**: Markdown no repo + resumo em GitHub Projects (SSOT).

---

## 1. CABEÇALHO

| Campo | Valor |
|---|---|
| **Projeto** | COGME — Conversor de Ganhos em Moeda Estrangeira |
| **Período** | YYYY-MM-DD a YYYY-MM-DD (Semana NN/2026) |
| **Relatório Nº** | SR-YYYY-WNN |
| **Autor** | Nome / Papel |
| **Distribuição** | GP (CCB), Equipe Técnica, Stakeholders FATEC |
| **Classificação** | Interno — Não sensível (LGPD n/a) |

---

## 2. RESUMO EXECUTIVO (TL;DR — máx. 3 linhas)

> **Status Geral**: [ ] 🟢 Verde (no prazo, sem riscos críticos)  [ ] 🟡 Amarelo (desvios controlados, atenção)  [ ] 🔴 Vermelho (bloqueador crítico, escalação CCB)

> **Principais Realizações**: 1. __________  2. __________  3. __________

> **Principais Riscos/Impedimentos**: 1. __________  2. __________

---

## 3. MÉTRICAS DE FLUXO (Fonte: GitHub Projects / GitHub Insights)

| Métrica | Meta | Atual (Período) | Tendência (vs. anterior) | Status | Observação |
|---|---|---|---|---|---|
| **Cycle Time** (média Done − In Progress) | ≤ 3 dias | X.X dias | ▼ / ▲ / → | 🟢/🟡/🔴 | |
| **Throughput** (cards Done/semana) | ≥ 5 cards | N cards | ▼ / ▲ / → | 🟢/🟡/🔴 | |
| **WIP em Fluxo** (cards In Progress) | ≤ 9 (3×3 pessoas) | N cards | ▼ / ▲ / → | 🟢/🟡/🔴 | WIP limit = 3 por pessoa |
| **Coverage** (linhas testadas / total) | ≥ 80% | XX% | ▼ / ▲ / → | 🟢/🟡/🔴 | Por push (CI) |
| **Testes Passando** | 100% | N/N | → | 🟢/🟡/🔴 | CI pipeline green |
| **ADRs Ratificadas no Período** | — | N | — | — | |
| **CRs Processados** | — | Aprovados: N / Rejeitados: N / Pendentes: N | — | — | |

> **Nota**: Baselines em `docs/metricas/baseline.md` são seeds simulados (calibração 23/09–03/10). Dados empíricos a partir de 01/11/2026.

---

## 4. PROGRESSO POR MARCO / WAVE (Roadmap M1–M4)

| Marco / Wave | Escopo | Status | % Concluído | Previsão Término | Real Término | Desvio | Riscos |
|---|---|---|---|---|---|---|---|
| **M1** (Base MVP) | Backend rates, simulate, invoice PDF; Frontend básico; CI/CD; DER fx_quotes | 🟢/🟡/🔴 | XX% | 2026-XX-XX | | | |
| **M2** (Identidade/Acesso) | Users, sessions, auth, Argon2id (PROP-018/CR-002) | 🟢/🟡/🔴 | XX% | 2026-XX-XX | | | |
| **M3** (Prestadora/Banco/Clientes) | Provider profiles, bank accounts, clients (PROP-019/020) | 🟢/🟡/🔴 | XX% | 2026-XX-XX | | | |
| **M4** (Simulações/Invoices + Multiusuário) | Invoices, bilingual, multi-user, privacy (PROP-021/022/023) | 🟢/🟡/🔴 | XX% | 2026-12-15 | | | |

---

## 5. IMPEDIMENTOS E RISCOS ATIVOS (Top 5 — do RAID Log)

| ID (RAID) | Descrição | Severidade | Status | Ação / Dono | Previsão Resolução | Escalação |
|---|---|---|---|---|---|---|
| RISK-XXX | | 🔴/🟠/🟡 | | | | [ ] CCB |
| ISSUE-XXX | | 🔴/🟠/🟡 | | | | [ ] CCB |
| DEP-XXX | | 🔴/🟠/🟡 | | | | [ ] CCB |

---

## 6. MUDANÇAS PROCESSADAS NO PERÍODO (Change Requests)

| CR-ID | Título | Decisão | Impacto | Implementação |
|---|---|---|---|---|
| CR-2026-NNN | | Aprovada/Rejeitada/Deferida | Escopo/Prazo/Qualidade | Iniciada/Concluída/Pendente |

---

## 7. DECISÕES TÉCNICAS E GOVERNANÇA (ADRs / CCB Log)

| Artefato | Versão | Decisão | Impacto Prático |
|---|---|---|---|
| ADR-XXX | vX.Y.Z | Ratificada/Emendada | |
| CCB RAT-YYYY-MM-DD-XXX | | Aprovada | |

---

## 8. PRÓXIMOS PASSOS (Próxima Semana / Próximo Relatório)

| Ação | Responsável | Prazo | Dependência | Critério de Sucesso |
|---|---|---|---|---|
| 1. | | | | |
| 2. | | | | |
| 3. | | | | |

---

## 9. ANEXOS / EVIDÊNCIAS

- Link para GitHub Projects (SSOT): https://github.com/leonardosetti/COGME/projects
- Link para CI/CD Runs: https://github.com/leonardosetti/COGME/actions
- Commits do período: `git log --since="YYYY-MM-DD" --until="YYYY-MM-DD" --oneline`
- RAID Log atualizado: `docs/governanca/raid-log.md`

---

> **Assinatura**: _________________________ (Autor)  |  Data: YYYY-MM-DD  |  **Próximo Relatório**: YYYY-MM-DD