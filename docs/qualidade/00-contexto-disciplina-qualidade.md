---
id: docs-qualidade-00-contexto-disciplina
title: Contexto da Disciplina de Qualidade de Software — COGME
type: plano
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/planos/plano-granular/plano-qualidade.md (v1.1.0, §5)
- .ai/specs/spec-010-qualidade-pdca-ishikawa-v1.spec.md (REQ-10, fase N6.3)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- qualidade
- disciplina
- istqb
- rastreabilidade
---

# Contexto da Disciplina de Qualidade de Software — COGME

## 1. Objetivo

Instituir, para o projeto COGME, uma disciplina de qualidade de software aplicada transversalmente à produção (backend, frontend, infra, docs, specs), baseada no ISTQB Certified Tester Foundation Level (CTFL) e alinhada ao PMBOK 7ª (domínios Medição, Entrega, Melhoria) e ao Plano de Gerenciamento da Qualidade vigente (`docs/planos/plano-granular/plano-qualidade.md`).

A disciplina cobre: estratégia de teste (pirâmide), Shift-Left, automação (pytest em unidade; Playwright com Screenplay Pattern em funcional/integração), rastreabilidade de requisitos (RTM) e todos os artefatos de teste defendidos pelo ISTQB.

## 2. Escopo da disciplina

| Dimensão | Objeto | Artefato |
|---|---|---|
| Prevenção | Código e arquitetura | Code review, SDD auditável, clean code, type safety |
| Detecção | Cobertura e defeitos | pytest unitário, Playwright funcional/integração, coverage gate |
| Correção | Melhoria de processo | 12 ciclos PDCA (REQ-10), Ishikawa 6M, RCA de incidentes |
| Rastreabilidade | Requisito → Caso de teste → Evidência | Matriz de Rastreabilidade de Requisitos (RTM) |

## 3. Frameworks aplicados transversalmente

### 3.1 Pirâmide de Testes

Camadas (de maior volume e menor custo para menor volume e maior custo):

1. **Unidade (pytest):** regras de negócio, schemas, serviços, repositórios, cálculo decimal. Execução rápida, sem rede, sem banco.
2. **Integração (pytest + TestClient):** contratos HTTP `/v1`, persistência, lifespan, PDF render, erro canônico. Dublês em memória; sem rede real.
3. **Funcional/E2E (Playwright + Screenplay Pattern):** fluxos críticos pela UI (simulação, emissão de invoice PDF) contra o stack rodando (front + back + db).

Regra: quanto maior a camada, menos casos; quanto menor a camada, mais casos. A detecção de defeito acontece o mais cedo possível (Shift-Left).

### 3.2 Shift-Left

Qualidade é inserida no início do ciclo, não inspecionada no fim:

- Requisitos revisados antes do código (DoR: critérios GWT, rastreáveis a REQ).
- Testes unitários escritos antes/durante a implementação (TDD quando aplicável, plano-qualidade §5.6 PDCA-N5).
- Análise estática (flake8, mypy, frontmatter, nomes de arquivo) em cada push (CI lint job).
- Security scan, FOSS compliance, health check de agentes no CI (antes do merge).
- Gate de cobertura (`--cov-fail-under=95`, CI `test-suite`) e zero testes pulados bloqueiam o merge.

## 4. Automação de testes

| Nível | Ferramenta | Linguagem | Padrão | Onde |
|---|---|---|---|---|
| Unitário | pytest | Python | Fixtures + dublês determinísticos | `tests/unit` |
| Integração | pytest + FastAPI TestClient | Python | Dublês de provedores/repositório/relógio | `tests/integration` |
| Funcional/E2E | Playwright | Python | Screenplay Pattern | `tests/e2e_playwright` |

## 5. Matriz de Rastreabilidade (RTM)

Mantida em `docs/qualidade/10-rtm-qualidade.md`. Mapeia 1:1:

REQ → US → Caso de Teste (unit/integração/funcional) → Espec → Evidência → Status.

## 6. Artefatos ISTQB produzidos

Todos os artefatos defendidos pelo ISTQB CTFL, atualizados a cada rodada de teste:

| # | Artefato ISTQB | Caminho |
|---|---|---|
| 1 | Plano de Testes (Test Plan) | `docs/qualidade/03-plano-testes-istqb.md` |
| 2 | Especificação de Projeto de Teste (Test Design Specification) | `docs/qualidade/04-especificacao-projeto-teste.md` |
| 3 | Especificação de Caso de Teste (Test Case Specification) | `docs/qualidade/05-casos-de-teste.md` |
| 4 | Especificação de Procedimento de Teste (Test Procedure Specification) | `docs/qualidade/06-procedimento-de-teste.md` |
| 5 | Relatório de Item de Teste Transmitido (Test Item Transmittal Report) | `docs/qualidade/06-procedimento-de-teste.md` (seção) |
| 6 | Registro de Teste (Test Log) | `docs/qualidade/07-registro-de-teste.md` |
| 7 | Relatório de Incidente de Teste (Test Incident Report) | `docs/qualidade/08-relatorio-incidente-de-teste.md` |
| 8 | Relatório Resumo de Teste (Test Summary Report) | `docs/qualidade/09-relatorio-resumo-de-teste.md` |
| 9 | Matriz de Rastreabilidade de Requisitos (RTM) | `docs/qualidade/10-rtm-qualidade.md` |
| 10 | Board de Análise de Resultados + RCA | `docs/qualidade/11-board-resultados-qualidade.md` |

## 7. Papéis (RACI da onda 6, spec-010 §3.4)

| Atividade | GP | qa-sdet | reviewer | gatekeeper | auditor |
|---|---|---|---|---|---|
| Consolidar PDCAs e Ishikawa | R/A | C | I | I | C |
| Produzir/manter Ishikawa e RTM | R/A | C | C | I | C |
| Verificar métricas (coverage, defeitos) | A | R | C | C | I |
| Regra de ouro no Done (CI verde + coverage + review + tasklist) | I | C | R | A | I |
| Auditoria fim-a-fim REQ-10 (evidências + rastreabilidade) | C | I | I | C | R/A |

## 8. Critérios de aceitação da disciplina

- Pirâmide respeitada: unidade >> integração >> funcional em volume de casos.
- Shift-Left: todo PR novo traz teste para o código que adiciona/altera.
- Cobertura ≥ 95% sobre `src/` (gate CI `test-suite`), zero testes pulados.
- RTM 100% preenchida: todo REQ mapeado a ao menos um caso de teste e vice-versa.
- Todo incidente de teste tem RCA, prioridade, impacto e severidade registrados no board de resultados.

## 9. Rastreabilidade da disciplina

| Fonte | Onde |
|---|---|
| plano-qualidade.md §5 (Qualidade) | §1, §3, §5, §6, §7, §8 |
| spec-010 (REQ-10, N6.3) | §1, §4, §7, §6 (artefatos 2,3,6,7,8,9) |
| spec-011 (CI/CD, REQ-11) | §4, §8 (gate, tempo ≤ 5 min) |
| Constitution (P-01 FOSS, P-08 fatos citáveis) | §1, §8 (sem métricas sem fonte) |

---

## Controle de versões

| Versão | Data | Alteração | Responsável |
|---|---|---|---|
| 1.0.0 | 14/11/2026 | Emissão inicial da disciplina: contexto, pirâmide, Shift-Left, automação pytest+Playwright Screenplay, RTM e artefatos ISTQB | agent-project-analyst |
