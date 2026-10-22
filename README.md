# COGME — Conversor de Ganhos em Moeda Estrangeira

> Simulação cambial completa, comparação entre regimes de contratação e emissão de invoices em PDF — 100% FOSS, 100% gratuito.

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Coverage](https://img.shields.io/badge/Coverage-≥80%25-brightgreen)](tests/)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](.github/workflows/ci.yml)
[![Kanban](https://img.shields.io/badge/Método-Kanban-FF6F00)](https://github.com/users/Leonardo-Setti/projects)
[![PMBOK](https://img.shields.io/badge/Governança-PMBOK%207ª%20+6ª-1565C0)](docs/tap/TAP.md)
[![Orçamento](https://img.shields.io/badge/Orçamento-R$%200,00-2E7D32)](docs/planos/plano-custos.md)
[![FOSS](https://img.shields.io/badge/Stack-100%25%20FOSS-0E8A16)](docs/decisoes/ADR-001-stack.md)

---

## Sobre o Projeto

O **COGME** é um projeto acadêmico desenvolvido na disciplina de **Gerência de Projetos** do curso de **Análise e Desenvolvimento de Sistemas** da **Fatec Taquaritinga**.

O cenário: um contingente crescente de profissionais brasileiros atua como PJ ou freelancer para empresas nos EUA, Europa e demais mercados que remuneram em moeda estrangeira (USD/EUR). A gestão financeira desses ganhos exige consultar múltiplos sites, planilhas manuais e calculadoras dispersas — um processo moroso, suscetível a erros e sem visão consolidada.

O COGME preenche essa lacuna: uma solução única, gratuita e de código aberto que reúne simulação cambial completa, comparação entre regimes de contratação e emissão de documentos financeiros associados.

### Objetivos SMART

| Objetivo | Meta | Prazo |
|---|---|---|
| **Produto** | MVP funcional com simulação cambial, 5 regimes, spread/IOF e invoice PDF | M3 (15/11/2026) |
| **Qualidade** | Cobertura de testes ≥ 80%, UAT sem defeitos críticos | M3 (15/11/2026) |
| **Inovação** | Stack 100% FOSS + SDD com IA generativa local | M2 (30/09/2026) |
| **Cronograma** | Entrega dentro do prazo letivo | M4 (15/12/2026) |
| **Documentação** | Consolidação completa + validação acadêmica | M4 (15/12/2026) |

---

## Equipe

| Papel | Nome | Responsabilidade |
|---|---|---|
| **Gerente de Projeto** | Leonardo David Silva Setti | Decisor operacional único, CCB, arquitetura, integração |
| **Desenvolvedor** | Fabricio de Lima Cabral | Escopo, cronograma, custos, backend |
| **Desenvolvedor** | Edson Luis Silva | Qualidade, testes, UAT, Ishikawa/PDCA |
| **Stakeholder-Avaliador** | Prof. Dr. Nivaldo Carleto | Avaliação acadêmica nos marcos M1–M4 |

---

## Governança

O projeto adota um **modelo híbrido trifásico** declarado no [Termo de Abertura do Projeto](docs/tap/TAP.md):

```
┌─────────────────────────────────────────────────┐
│  PMBOK® 7ª Edição                               │  ← Governança primária
│  12 Princípios + 8 Domínios de Desempenho       │     (por que / para quê)
├─────────────────────────────────────────────────┤
│  PMBOK® 6ª Edição                               │  ← Dicionário complementar
│  Processos como vocabulário estrutural          │     (obsolescência assumida
│  EVM/SPI/CPI = LEGADO                           │      para métricas preditivas)
├─────────────────────────────────────────────────┤
│  Manifesto Ágil + Kanban (GitHub Projects)      │  ← Método de execução
│  Fluxo contínuo, WIP limits, métricas de fluxo  │     (como o trabalho flui)
└─────────────────────────────────────────────────┘
```

### Método de Execução

- **Ferramenta SSOT:** [GitHub Projects](https://github.com/users/Leonardo-Setti/projects) — Kanban com fluxo contínuo (sem sprints)
- **Colunas:** `Backlog` → `Ready (DoR)` → `In Progress` → `Code Review` → `Done (DoD)`
- **WIP Limit:** 3 cards por pessoa em `In Progress`
- **Métricas:** Cycle Time (≤ 3 dias), Throughput (≥ 5 cards/semana), CFD
- **Rituais:** Daily assíncrona (15min), Refinement semanal (30min), Retrospectiva quinzenal (30min)

### Decisões Arquiteturais (ADRs)

| ADR | Decisão | Status |
|---|---|---|
| [ADR-001](docs/decisoes/ADR-001-stack.md) | Stack tecnológica FOSS | ✅ Aprovada |
| [ADR-002](docs/decisoes/ADR-002-kanban.md) | Kanban como método de execução | ✅ Aprovada |
| [ADR-003](docs/decisoes/ADR-003-metricas.md) | Métricas de fluxo (substituição de EVM) | ✅ Aprovada |
| [ADR-004](docs/decisoes/ADR-004-tasklists.md) | Tasklists Markdown (rejeição de subissues) | ✅ Aprovada |
| [ADR-005](docs/decisoes/ADR-005-freeze.md) | Regime de freeze do TAP | ⏳ Antes do M2 |

### Tecelagem Constitucional e Agentes

A produção de agentes segue o [Plano Canônico de Produção](docs/planos/plano-producao-agentes.md), governado pela [Constituição do Projeto](constitution.md):

| Gate | Artefato | Validador |
|---|---|---|
| Lei suprema | `constitution.md` | auditoria humana (CCB) |
| Contratos de agentes | `.opencode/agents/*.md` | `scripts/validate_nexus_yaml.py` |
| Score de forja (≥ 85/100) | 16 seções AFA | `scripts/validate_afa_output.py` |
| Roster SSOT | `.ai/agents/registry.yaml` | `scripts/sync_agent_registry.py` |
| Dispatch half-duplex | DAG `AGENT_TOPOLOGY` | `scripts/nexus_dispatcher.py` |

Roster em consolidação: 25 agentes (`agent-*`) em 8 ondas de produção.

---

## Roadmap e Marcos

| Marco | Data | Entregável | Status |
|---|---|---|---|
| **M1** — Entrega Parcial Documental | 22/09/2026 | TAP + 5 planos (Integração, Escopo, Cronograma, Custos, Qualidade) + 12 PDCAs + Ishikawa | ✅ |
| **M2** — Ambiente e Modelagem | 30/09/2026 | Stack validada, CI configurado, DER, Protótipo UX/UI, 3 planos restantes | ⏳ |
| **Calibração** — Baseline de Métricas | 03/10/2026 | Baseline empírica de fluxo Kanban | ⏳ |
| **M3** — MVP Funcional (Beta) | 15/11/2026 | Código full-stack, coverage ≥ 80%, UAT aprovado | ⏳ |
| **M4** — Encerramento e Aceite | 15/12/2026 | Documentação consolidada, validação acadêmica, release final | ⏳ |

### Macro-Fases da EAP

```
MF1: Fundação (01/09 – 30/09)     → N1, N2, N3, N4, N8, N9
MF2: Construção (01/10 – 15/11)   → N5, N6, N7, N10
MF3: Consolidação (16/11 – 15/12) → N11, N12
```

**EAP:** 12 fases de Nível 1 + 37 pacotes de Nível 2 — [ver diagrama](docs/diagramas/eap/fig-01-eap-executiva.svg)

---

## Stack Tecnológica (100% FOSS)

Definida na [ADR-001](docs/decisoes/ADR-001-stack.md). Orçamento total: **R$ 0,00**.

| Camada | Tecnologia | Licença | Função |
|---|---|---|---|
| **Backend** | Python 3.11 + FastAPI | PSF / MIT | API assíncrona |
| **Banco de Dados** | SQLite 3.x | Public Domain | Cache de cotações + persistência |
| **Geração de PDF** | WeasyPrint ≥ 59.0 | BSD-3-Clause | Invoices |
| **Frontend** | HTML5 + HTMX + Tailwind CSS | MIT | Interface responsiva |
| **Testes** | pytest + coverage.py | MIT | Coverage ≥ 80% |
| **CI/CD** | GitHub Actions (Free Tier) | Proprietário gratuito | Pipeline automatizado |
| **SDD Local** | llama.cpp + Qwen 32B + OpenCode | MIT / Autorizada | IA generativa local |
| **Análise Estática** | mypy (opcional) | MIT | Type safety |

### Conformidade FOSS

Todas as dependências passam por auditoria de licenciamento ([EAP N4.4](docs/dependencias/registro.md)):

- **Whitelist:** MIT, Apache 2.0, BSD, GPL, LGPL, ISC, PSF, Public Domain
- **Blacklist:** Proprietárias, Shareware, Creative Commons, Source Available não-OSI

---

## Funcionalidades (MVP)

| REQ | Funcionalidade | Critério de Aceite |
|---|---|---|
| REQ-01 | Simulação cambial em tempo real (USD/EUR → BRL) | Latência ≤ 2s |
| REQ-02 | 5 regimes de contratação (hora, dia, semana, mês, valor fixo) | 100% operacionais em UAT |
| REQ-03 | Encargos financeiros simulados (spread + IOF) | Precisão de 2 casas decimais |
| REQ-04 | Emissão de invoice em PDF | Geração ≤ 3s via WeasyPrint |
| REQ-05 | Tempo de resposta | ≤ 3s em 95% das requisições |
| REQ-06 | Interface web responsiva (FOSS) | Chrome/Firefox/Edge (últimas 2 versões) |
| REQ-07 | Cache de cotações (SQLite) | Redução ≥ 50% das chamadas à API |
| REQ-08 | Cobertura de testes | ≥ 80% |
| REQ-09 | Testes de aceitação (UAT) | Zero defeitos críticos/bloqueantes |
| REQ-10 | Ferramentas da qualidade | 12 PDCAs + Ishikawa 6M |
| REQ-11 | Pipeline CI | Lint + testes ≤ 5 min |
| REQ-12 | ADRs para decisões críticas | Mínimo 3 registradas |
| REQ-13 | Rastreabilidade de prompts SDD | 100% catalogados em `.ai/handoffs/` |
| REQ-14 | Documentação técnica | Arquitetura + APIs aprovadas |
| REQ-15 | Licenciamento 100% FOSS | Todas as dependências OSI-approved |

---

## Estrutura do Repositório

```
COGME/
├── .ai/                          # Contexto SDD (lido pela IA)
│   ├── personas/                 # PM, Coder, Reviewer, Tester + active.md
│   ├── specs/                    # Especificações imutáveis
│   ├── handoffs/                 # Artefatos entre fases SDD
│   └── workflows/                # Automação bash (sdd-cycle.sh)
│
├── docs/
│   ├── planos/                   # 8 planos de gerenciamento
│   │   ├── plano-integracao.md
│   │   ├── plano-escopo.md
│   │   ├── plano-cronograma.md
│   │   ├── plano-custos.md
│   │   ├── plano-qualidade.md
│   │   ├── plano-recursos.md     ← M2
│   │   ├── plano-comunicacoes.md ← M2
│   │   └── plano-riscos.md       ← M2
│   ├── decisoes/                 # ADRs 001–005
│   ├── conhecimento/             # OKB, Glossário, Lições Aprendidas
│   ├── metricas/                 # Baseline de fluxo (pós-calibração)
│   ├── requisitos/               # REQ-01 a REQ-15
│   ├── diagramas/                # SVGs canônicos por área
│   │   ├── integracao/
│   │   ├── escopo/
│   │   ├── cronograma/
│   │   ├── custos/
│   │   ├── qualidade/
│   │   └── eap/
│   ├── dependencias/             # Registro de auditoria FOSS
│   ├── tap/                      # TAP.md + TAP.docx
│   └── archive/                  # Artefatos históricos (não canônicos)
│
├── src/
│   ├── backend/                  # FastAPI + SQLite
│   │   ├── main.py
│   │   ├── models/
│   │   ├── routers/
│   │   └── services/
│   ├── frontend/                 # HTMX + Tailwind
│   │   ├── templates/
│   │   └── static/
│   └── shared/                   # Schemas compartilhados
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── .github/workflows/ci.yml      # Pipeline CI
├── README.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

---

## Como Executar

### Pré-requisitos

- Python 3.11+
- Git

### Setup

```bash
# Clonar o repositório
git clone https://github.com/Leonardo-Setti/COGME.git
cd COGME

# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt
```

### Executar o Backend

```bash
uvicorn src.backend.main:app --reload --port 8000
```

### Executar Testes

```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=80
```

### Pipeline CI

O pipeline roda automaticamente a cada push via GitHub Actions:

```
lint (flake8 + mypy) → testes (pytest + coverage ≥ 80%) → relatório
```

---

## Qualidade

| Dimensão | Mecanismo | Meta |
|---|---|---|
| **Preventiva** | Code Review + SDD com IA auditável + Clean Code | Zero retrabalho |
| **Detectiva** | Pipeline CI + pytest + coverage.py | Coverage ≥ 80% |
| **Corretiva** | 12 ciclos PDCA + 3 diagramas Ishikawa 6M | Melhoria contínua |

### Ferramentas da Qualidade (REQ-10)

- **12 ciclos PDCA:** Um por fase da EAP (N1–N12)
- **3 diagramas Ishikawa 6M:** Coverage < 80%, Defeitos Críticos em UAT, Cycle Time > 3 dias
- **Retrospectivas quinzenais:** Pauta fixa (o que funcionou, o que melhorar, ações)

---

## Premissas e Restrições

### Premissas (TAP §9)

| # | Premissa |
|---|---|
| P1 | Governança híbrida: PMBOK 7ª + 6ª dicionário + Kanban |
| P2 | Projeto 100% FOSS |
| P3 | SDD com IA generativa autorizado, com rastreabilidade |
| P4 | Código-fonte funcional é deliverable formal |
| P5 | ≤ 20h/semana por membro |
| P6 | Hardware local adequado |
| P7 | Prof. Dr. Nivaldo Carleto = avaliador único nos marcos |
| P8 | Aquisições e Partes Interessadas simplificadas |
| P9 | Separação ontológica: TAP ≠ EAP ≠ PDCA |

### Restrições (TAP §8 + §11)

- MVP acadêmico — desenvolvimento do zero
- Prazo letivo inegociável (2 bimestres)
- **Orçamento zero** — proibição de ferramentas pagas
- Equipe de 3 pessoas com múltiplos papéis
- Stack 100% FOSS (OSI-approved)
- Curso noturno — disponibilidade limitada

---

## Documentação

| Documento | Localização |
|---|---|
| Termo de Abertura do Projeto (TAP) | [`docs/tap/TAP.md`](docs/tap/TAP.md) |
| Plano de Integração | [`docs/planos/plano-integracao.md`](docs/planos/plano-integracao.md) |
| Plano de Escopo | [`docs/planos/plano-escopo.md`](docs/planos/plano-escopo.md) |
| Plano de Cronograma | [`docs/planos/plano-cronograma.md`](docs/planos/plano-cronograma.md) |
| Plano de Custos | [`docs/planos/plano-custos.md`](docs/planos/plano-custos.md) |
| Plano de Qualidade | [`docs/planos/plano-qualidade.md`](docs/planos/plano-qualidade.md) |
| OKB (Base de Conhecimento) | [`docs/conhecimento/OKB.md`](docs/conhecimento/OKB.md) |
| Glossário | [`docs/conhecimento/glossario.md`](docs/conhecimento/glossario.md) |
| ADRs | [`docs/decisoes/`](docs/decisoes/) |
| Diagramas | [`docs/diagramas/`](docs/diagramas/) |

---

## Licença

Este projeto é licenciado sob a **MIT License** — veja o arquivo [LICENSE](LICENSE) para detalhes.

Todas as dependências são auditadas para conformidade FOSS. Consulte o [registro de dependências](docs/dependencias/registro.md) para a lista completa.

---

## Agradecimentos

- **Fatec Taquaritinga** — Instituição de ensino
- **Prof. Dr. Nivaldo Carleto** — Orientação e avaliação acadêmica
- Comunidade FOSS — FastAPI, SQLite, WeasyPrint, HTMX, Tailwind CSS, llama.cpp, Qwen

---

<div align="center">

**COGME** — Conversor de Ganhos em Moeda Estrangeira

Fatec Taquaritinga · Análise e Desenvolvimento de Sistemas · Gerência de Projetos

2026

</div>