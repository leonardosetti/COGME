---
id: docs-tap-tap
title: TAP COGME — Termo de Abertura do Projeto (linha de base v3, congelada)
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/planos/plano-granular/plano-integral-tap-1-2-3-4-5.md (fonte canônica integral do TAP v3)
- constitution.md (Art. 2.1: TAP v3 como ato autorizativo)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- tap
- termo-abertura
- baseline
- congelado
---

# TAP COGME — Termo de Abertura do Projeto (linha de base v3, congelada)

> **Ponteiro canônico:** o conteúdo integral do TAP v3 (emissão 18/09/2026, regime de *freeze*) reside em `docs/planos/plano-granular/plano-integral-tap-1-2-3-4-5.md` (seção INTRODUÇÃO e Tabelas 1–N). Este arquivo declara o resumo executivo e o cross-reference obrigatório; não duplica o corpo integral (OKB §8.1 — cross-reference substitui duplicação).

## 1. Identificação do projeto (Tabela 1 do plano-integral)

| Campo | Valor |
|---|---|
| Projeto | COGME — Conversor de Ganhos em Moeda Estrangeira |
| Instituição | Fatec Taquaritinga — CST em Análise e Desenvolvimento de Sistemas |
| Disciplina | Gerência de Projetos |
| Gerente de Projeto | Leonardo David Silva Setti |
| Equipe | Leonardo David Silva Setti, Fabricio de Lima Cabral, Edson Luis Silva |
| Stakeholder-Avaliador | Prof. Dr. Nivaldo Carleto |
| Data de autorização do TAP | 18/09/2026 (versão 3 — regime de *freeze*) |
| Orçamento-teto | R$ 0,00 (100% FOSS) |

## 2. Objeto e justificativa

Conversor cambial FOSS, gratuito, de jurisdição brasileira (LGPD primária), para simulação de ganhos em moeda estrangeira (USD/EUR → BRL), comparação de 5 regimes de contratação, cálculo de spread/IOF e emissão de invoice PDF. Justificado pela lacuna de solução única, gratuita e open source para conversão e comparação de regimes de cotação.

## 3. EAP canônica

**12 fases (N1–N12) + 37 pacotes de nível 2**, agrupados em 3 macro-fases:
- MF1 — Fundação (N1–N4, N8, N9, N10 parcial)
- MF2 — Construção (N5–N7, N10)
- MF3 — Consolidação (N11, N12)

Fonte integral: `docs/planos/plano-granular/plano-integral-tap-1-2-3-4-5.md` (Tabela 2 do plano-integral).

## 4. Marcos (TAP §6, núcleo blindado sob ADR-013-a)

| Marco | Data canônica | Conteúdo |
|---|---|---|
| M1 — Entrega Parcial Documental | 22/09/2026 | 5 planos + 12 PDCAs + Ishikawa |
| M2 — Ambiente e Modelagem | 30/09/2026 (TAP §6) → 15/11/2026 (CR-001 / ADR-015) | CI verde + DER + UX/UI versionados |
| Calibração (auxiliar) | 03/10/2026 | Baseline de métricas (seed SIMULADO) |
| M3 — MVP Funcional (Beta) | 15/11/2026 | Coverage ≥ 80%, UAT sem defeitos críticos |
| M4 — Encerramento | 15/12/2026 | Documentação consolidada + aceite formal |

## 5. Regime de controle

- **Congelamento (*freeze*):** o TAP não é revisado, reversionado ou corrigido ao longo do ciclo (Premissa P9; ADR-005).
- **Precedência intra-TAP:** em divergência entre seções, o §6 Marcos é canônico para matéria temporal (ADR-005).
- **Emenda controlada:** ajuste pontual apenas via Delta Log (`docs/tap/delta-v3-1.md`) + ADR de emenda + CCB, sob o regime da ADR-013-a (baseline viva com núcleo blindado). O núcleo (objeto, objetivos SMART, justificativa, orçamento-teto R$ 0,00, EAP 12/37) é intocável sem Emenda MAJOR.
- **Notas de Contexto (NCs):** locus de leitura operacional no Plano de Cronograma (§3.8); divergências jamais são tratadas como correções do TAP.

## 6. Rastreabilidade

- Hierarquia normativa: `constitution.md` > TAP v3 > ADRs > OKB > Planos > Glossário > Specs > Código (Constitution Art. 2.1; OKB §1.1).
- Fonte canônica integral: `docs/planos/plano-granular/plano-integral-tap-1-2-3-4-5.md`.
- Emendas registradas: `docs/tap/delta-v3-1.md` (REQ-07 SQLite→PostgreSQL; M2 30/09→15/11).
