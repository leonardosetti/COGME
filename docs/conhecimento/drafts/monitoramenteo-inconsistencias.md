---
id: drafts-monitoramenteo-inconsistencias
title: Monitoramenteo_Inconsistencias
version: 1.0.0
class: conhecimento
status: active
owner: agent-project-analyst
derived-from:
- docs/conhecimento/drafts/monitoramenteo-inconsistencias.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- drafts
- docs
- normalizado
---
 ## MONITORAMENTO DE INCONSISTÊNCIAS NO TAP

Conforme solicitado, sigo sinalizando as inconsistências críticas que **ainda persistem** no documento `Termo de Abertura do Projeto v1_opngoing.docx` e que devem ser corrigidas antes da submissão ao Prof. Dr. Nivaldo Carleto:

| ID | Inconsistência | Localização Atual no TAP | Ação Corretiva Obrigatória | Severidade |
|---|---|---|---|---|
| **INC-01** | Data de marco ultrapassada | §3 (Cronograma) e §8.3: menciona "08/09/2026" | Alterar para **22/09/2026** (Entrega Parcial Documental). | 🔴 Crítica |
| **INC-02** | Grafia incorreta do Stakeholder | §1, §3.2, §7, §13: "Nivaldo Carleto" | Corrigir para **Nivaldo Carleto** (com dois 't'). | 🔴 Crítica |
| **INC-03** | Grafia incorreta do Gerente | §13 (Aprovações): "Leonardo David Siva Setti" | Corrigir para **Leonardo David Silva Setti** (com 'l' no Silva). | 🔴 Crítica |
| **INC-04** | Nome da Instituição desatualizado/incorreto | §1, §2.3, §13: "FATEC Marlene Maria Miletta Servidoni" | Padronizar para **Fatec Taquaritinga** (nome oficial e atual). | 🟠 Alta |
| **INC-05** | Menção a EVM e Burndown | §3 (Métricas e Indicadores): cita SPI, CPI e Burndown Chart. | Substituir por: **"Métricas de fluxo Kanban (Cycle Time e Throughput) via GitHub Insights"**. | 🟠 Alta |
| **INC-06** | Comentário de revisão visível | §8.9 (Síntese): `Comment by leonardo: Verificar com o Profº...` | **Excluir** o comentário do Word antes da geração do PDF final. | 🟠 Alta |
| **INC-07** | Menção a "Cache Redis" na EAP | EAP (versão antiga ainda presente em algumas partes): N5.2 | Garantir que esteja apenas como "Cache" (genérico), conforme decisão de usar SQLite. | 🟡 Média |

---
