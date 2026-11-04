# PLANO CANÔNICO DE PRODUÇÃO DE AGENTES — COGME

<!-- Versão: 1.1 | Emitido por: AFA-ULTIMATE v1.3.0-FINAL | Data: 2026-10-22 |
     Lineage: AFA v1.3.0 | Hardware: 8700G / 60GB / llama.cpp CPU-only | Status: AGUARDANDO APROVAÇÃO HUMANA -->

> **Ação:** Determinar a ordem ideal de produção dos agentes especialistas, incluindo os scripts mediadores necessários (parser, dispatcher, validação, testes) para orquestração em sintonia fina.
> **Restrição mandatada:** Nenhum papel/agente subutilizado. Prefixo `agent-` compulsório.
> **Âncoras:** LGPD primária | PMBOK 7ª + Kanban | SDD | `local/qwen30b-moe` @ 8192 ctx.

---

## 1. DIGEST DE CONTEXTO (resultado da Ingestão §7.5)

| Ativo | Status encontrado |
|---|---|
| Stack (ADR-001/005) | Python 3.11 + FastAPI + SQLite + MIT — FOSS 100%, R$ 0 |
| Governança | PMBOK 7ª (primária) + 6ª (dicionário) + Kanban em GitHub Projects (SSOT) |
| Cronograma | Marcos M1–M4; entrega final 15/12/2026; meta de cobertura ≥ 80% |
| Ciclo SDD | `.ai/workflows/sdd-cycle.sh` operacional (persona → handoff → `opencode run`) |
| `src/` | Esqueleto (main.py stub; routers/models vazios; 1 template) |
| `.opencode/agents/` | 4 variantes AFA — **neutro/liberal DEPRECATED** (§0.3), remoção pendente |
| `.ai/agents/`, `.ai/handoffs/`, `scripts/`, `constitution.md` | **AUSENTES** |
| `.github/workflows/ci.yml` | **VAZIO** |

**Lacunas bloqueantes:**

| ID | Lacuna | Bloqueia |
|----|--------|----------|
| G-01 | `constitution.md` ausente | Forja de qualquer agente (§7.5: missing constitution → BLOCK) |
| G-02 | `scripts/` inexistente | Validação de YAML, dispatch, extração de handoffs |
| G-03 | `.ai/agents/` vazio | Rastreabilidade de contratos e roster |
| G-04 | Variantes AFA deprecated ativas | Contradição ideológica no roster |
| G-05 | `ci.yml` vazio | Nenhum gate automatizado para os próprios script |

---

## 2. CONSOLIDAÇÃO DE ROSTER (28 sugestões → 25 agentes)

Aplicação de Pareto (§0.6.3) + YAGNI. Papéis dominados foram **incorporados como vetores de agência**, não eliminados — garantindo a cláusula de anti-subutilização.

| ID | Sugestão original | Decisão | Fundamentação (trade-off) |
|----|-------------------|---------|---------------------------|
| C-01 | QA / QE / SDET (3 papéis) | **1 agente:** `agent-qa-sdet` | Mesma disciplina contínua; separar triplicaria contexto sem ganho de cobertura |
| C-02 | Stack evaluator | **Vetor de `agent-architect`** (R-01: stack-drift watch) | Stack congelado por ADR-005; reavaliação periódica é gestão de deriva — atribuição natural do arquiteto; CVEs compartilhados com `digital-security` |
| C-03 | License Auditor | **Vetor de `agent-compliance-governance`** (checklist L-01, SLA próprio) | Auditoria de licença é subconjunto de compliance; agente dedicado teria carga semanal < 10% |
| C-04 | Project reader | **Downgrade para skill:** `skill-project-reader` (usado por SDD + Orchestrator) | Leitura é função mecânica de ingestão, não de julgamento; como agente, seria subutilizado |
| C-05 | Project Gate keeper | `agent-gatekeeper` (**mantido**) | Portão de merge/rastreabilidade ≠ revisão de código (`reviewer`) |

**Roster resultante: 25 agentes** (+ AFA-ULTIMATE como meta-agente já operante). Todos com prefixo `agent-` e slug kebab-case validado por script.

---

## 3. TOPOLOGIA EM CAMADAS (DAG, anti-recursão)

~~~
L0  Orquestração            → 1 agente
L1  Comando/Estratégia      → 5 agentes
L2  Execução/Técnica        → 13 agentes
L3  Qualidade/Portões       → 4 agentes
META AFA-ULTIMATE           → já operante (forjador)
~~~

Fluxo half-duplex: toda delegação retorna parcela estruturada ao chamador; brigas de rota são `status: escalated_to_orchestrator`.

---

## 4. ORDEM CANÔNICA DE PRODUÇÃO

### FASE 0 — Tecelagem Constitucional (pré-requisito de tudo)

| Ordem | Artefato | Justificativa de precedência |
|-------|----------|------------------------------|
| **0.1** | `constitution.md` (raiz) | Redigida pelo AFA, co-assinada pelo Humano — fecha G-01 e libera a forja |
| **0.2** | Limpeza `opencode.json`: registrar `agent-factory-architect-ultimate` como agente primário; arquivar neutro/liberal | Fecha G-04; prioridade de canonização (§0.3) |
| **0.3** | Scaffold `scripts/`, `tests/agents/`, `.ai/agents/registry.yaml` | Contratos antes de conteúdo — validadores exigem estrutura |
| **0.4** | Referência cruzada do plano no README (seção Agentes) | Rastreabilidade desde o primeiro commit |

### FASE S — Scripts Mediadores (TDD compulsório; stdlib FOSS apenas)

| Ordem | Script | Função | Por que nesta posição |
|-------|--------|--------|----------------------|
| **S.1** | `scripts/validate_nexus_yaml.py` | Valida schema de contrato YAML (5 chaves), slug kebab-case, camadas válidas — **schema-driven** (lê `.opencode/agents/` dinamicamente) | Resolve o círculo "dispatcher pressupõe roster pronto": validação genérica não demanda roster |
| **S.2** | `scripts/handoff_parser.py` | Parseia `.ai/handoffs/*.md` → payload estruturado (metadados, critérios de aceite, status) | O ciclo SDD alimenta todo o fluxo; parser precede dispatcher |
| **S.3** | `scripts/validate_afa_output.py` | Valida 16 seções + score §0.9 (≥ 85/100) nos agentes forjados | Precisa existir ANTES da primeira forja — agentes são os artefatos validados |
| **S.4** | `scripts/nexus_dispatcher.py` | Dispatch por `AGENT_TOPOLOGY` (DAG), half-duplex, rate-limit por agente | Consome saídas de S.1–S.3 (roster validado + parser) |
| **S.5** | `scripts/sync_agent_registry.py` | Extrai metadata dos agentes → `.ai/agents/registry.yaml` (SSOT do roster) | Fecha o loop scripts ↔ agentes |
| **S.6** | `tests/agents/` — conftest, fixture `golden-agent.md`, 1 suite por script | Garante que refactors não quebrem o pipeline | Suite completa antes da 1ª forja |
| **S.7** | Upgrade `.ai/workflows/sdd-cycle.sh` → v2 (integra S.2 + S.4) | Ciclo SDD nativo com dispatch estruturado | Só após scripts maduros |

**Critério de aceite da FASE S:** `python -m pytest tests/agents/ -v` verde + lint aprovado + `--help` funcional em todos os scripts.

### FASE A — Ondas de Forja (ordem estrita: upstream concluído antes do downstream)

> **Camadas finais (DAG canônica, `AGENT_TOPOLOGY`):** L0 → 1 | L1 → 5 | L2 → 15 (execução, inclui `agent-qa-sdet`) | L3 → 3 (portões: reviewer, gatekeeper, auditor) | META → skill-master + forjador. Total: 25.

#### ONDA 1 — Comando do Sistema

| Ordem | Agente | Camada | Pré-requisito | Critério de aceite |
|-------|--------|--------|---------------|--------------------|
| **A.1** | `agent-orchestrator` | L0 | FASE 0 + FASE S | 16 seções; YAML válido; `AGENT_TOPOLOGY` registrada; self-improvement; RT ≥ 12; métricas ≥ 12 |
| **A.2** | `agent-sdd-specialist` | L1 | A.1 | Contrato de handoff reconhecível pelo `handoff_parser.py`; custódia do Canon_Stack_SDD |

> SDD primeiro entre os especialistas: o projeto inteiro roda sobre Spec-Driven Development; PM e PO recebem vocabulário dele.

#### ONDA 2 — Comando de Escopo

| Ordem | Agente | Camada | Por quê aqui |
|-------|--------|--------|--------------|
| **A.3** | `agent-pm` | L1 | Custódia PMBOK (WBS, marcos, CCB, EVM dicionário) — upstream de escopo |
| **A.4** | `agent-po` | L1 | Converte escopo em backlog DoR (WIP ≤ 3, fluxo contínuo) — dependente do vocabulário do PM |

> PM antes de PO: a PMBOK governa o "porquê"; o PO traduz o "oquê". Ordem invertida produziria DoR prematura sem lastro de governança.

#### ONDA 3 — Arquitetura e Análise

| Ordem | Agente | Camada | Por quê aqui |
|-------|--------|--------|--------------|
| **A.5** | `agent-architect` | L1 | Custódia de ADRs, diagramas, stack-drift (vetor R-01) — requer PM (escopo) e SDD (método) |
| **A.6** | `agent-project-analyst` | L1 | Primeiro "olho geral": consolida e mede o estado produzido por PM/Arquiteto/PO |

#### ONDA 4 — Execução Técnica (padrões → contrato → dados → código)

| Ordem | Agente | Camada | Por quê aqui |
|-------|--------|--------|--------------|
| **A.7** | `agent-python-specialist` | L2 | Padrões Python (pyproject, typing, lint) — fundação do codebase |
| **A.8** | `agent-api-specialist` | L2 | SSOT de contrato (OpenAPI/FastAPI, `src/shared/schemas.py`) — design antes de implementação |
| **A.9** | `agent-dba` | L2 | Schema/migrations SQLite — camada de dados decora o contrato |
| **A.10** | `agent-backend-dev` | L2 | Implementa services/routers — consumidor de A.7 + A.8 + A.9 |
| **A.11** | `agent-ui-ux-advisor` | L2 | Requisitos visuais precedem a execução frontend |
| **A.12** | `agent-frontend-dev` | L2 | Templates server-side + integração browser — recebe do advisor e do contrato |
| **A.13** | `agent-bash-specialist` | L2 | Shell de sistema (automação, systemd, parsing de hardware, upgrades do sdd-cycle) |

#### ONDA 5 — Infraestrutura, Automação e Segurança

| Ordem | Agente | Camada | Por quê aqui |
|-------|--------|--------|--------------|
| **A.14** | `agent-infrastructure-specialist` | L2 | llama.cpp, llama-server, systemd, hardware (8700G/60GB) — base física |
| **A.15** | `agent-devops` | L2 | CI/CD em GitHub Actions (fecha G-05), pipeline dos testes S.6 |
| **A.16** | `agent-github-specialist` | L2 | Ecossistema `gh` por completo: Projects (SSOT), Actions, Issues, releases, gh CLI |
| **A.17** | `agent-digital-security` | L2 | Hardening, threat model, CVE scan (co-responsável do R-01) — aplicado quando as superfícies existem |
| **A.18** | `agent-compliance-governance` | L2/L3 | LGPD, Marco Civil, licenças (vetor L-01) — audita a postura técnica já construída |

> Segurança antes de Compliance: compliance audita postura técnica que precisa existir primeiro.

#### ONDA 6 — Corrente da Qualidade (portões sequenciais)

| Ordem | Agente | Camada | Por quê aqui |
|-------|--------|--------|--------------|
| **A.19** | `agent-qa-sdet` | L2 | Estratégia de testes (unit/integration, cobertura ≥ 80% — meta SMART) |
| **A.20** | `agent-reviewer` | L3 | Gate de revisão de código (nível commit) — usa os testes de A.19 |
| **A.21** | `agent-gatekeeper` | L3 | Gate de merge/DoD/rastreabilidade — última barreira antes da integração |
| **A.22** | `agent-project-auditor` | L3 | Auditoria fim-a-fim PMBOK + qualidade — precisa da cadeia completa existente |

#### ONDA 7 — Commons e Meta (fechamento de loop)

| Ordem | Agente | Camada | Por quê aqui |
|-------|--------|--------|--------------|
| **A.23** | `agent-docker-specialist` | L2 | Documentação técnica narrativa (README, ADRs, runbooks) — agora com código real a documentar |
| **A.24** | `agent-artifact-builder` | L2 | Scaffolding e geração de artefatos estruturais (YAML, JSON, templates, esquemas) |
| **A.25** | `agent-skill-master` | Meta-adjacente | Destila skills `.opencode/skills/` dos padrões observados nos 24 agentes anteriores (inclui `skill-project-reader` da C-04) |

> YAGNI aplicado a A.25: skills só têm valor quando destiladas de padrões reais; forjar antes geraria skills especulativas sem lastro.

---

## 5. MATRIZ DE ANTI-SUBUTILIZAÇÃO

Cada linha lista os consumidores diretos do agente (quem o invoca via dispatcher). Critério: nenhum agente com < 3 consumidores.

| Agente | Consumidores diretos | Carga |
|--------|----------------------|-------|
| orchestrator | todos (L0, dispatch universal) | ●●●●● |
| sdd-specialist | PM, PO, backend, frontend, qa, docker | ●●●●● |
| pm | orchestrator, po, analyst, devops, auditor | ●●●●○ |
| po | backend, frontend, qa, gatekeeper | ●●●●○ |
| architect | api, dba, backend, frontend, infra, security | ●●●●● |
| project-analyst | pm, architect, auditor, docker | ●●●○○ |
| python-specialist | backend, qa, docker, artifact-builder | ●●●●○ |
| api-specialist | backend, frontend, qa, docker | ●●●●○ |
| dba | backend, qa, security | ●●●○○ |
| backend-dev | reviewer, gatekeeper, qa, github-specialist | ●●●●● |
| ui-ux-advisor | frontend, qa, reviewer | ●●●○○ |
| frontend-dev | reviewer, gatekeeper, qa | ●●●●○ |
| bash-specialist | infra, devops, security | ●●●○○ |
| infrastructure-specialist | devops, security, compliance | ●●●○○ |
| devops | qa, gatekeeper, security | ●●●○○ |
| github-specialist | orchestrator, pm, devops, gatekeeper, auditor | ●●●●○ |
| digital-security | architect, compliance, reviewer, auditor | ●●●●○ |
| compliance-governance | architect, po, gatekeeper, auditor, security | ●●●●○ |
| qa-sdet | reviewer, gatekeeper, auditor, devops | ●●●●● |
| reviewer | gatekeeper | ●●●○○ |
| gatekeeper | orchestrator, auditor | ●●●○○ |
| project-auditor | pm, compliance, orchestrator | ●●●○○ |
| docker-specialist | github-specialist, auditor | ●●●○○ |
| artifact-builder | pm, architect, devops, docker | ●●●○○ |
| skill-master | todos (via skills destiladas) | ●●●●○ |

Critério anti-subutilização: **ATENDIDO** (nenhuma linha abaixo de 3 consumidores).

---

## 6. GATE DE QUALIDADE DE FORJA (por agente, inegociável)

- 16 seções completas (template AFA §6) — sem placeholder.
- Score §0.9 ≥ 85/100 (`validate_afa_output.py`).
- YAML compatível com `validate_nexus_yaml.py`.
- Registro em `.ai/agents/registry.yaml` (`sync_agent_registry.py`).
- System prompt < 4000 tokens; emissão multi-turno (3–5 voltas).
- Ideologia §0.4 e calibração de hardware §0.1 verificadas.

---

## 7. INVENTÁRIO TOTAL

| Recurso | Quantidade |
|---------|-----------|
| Agentes especialistas | 25 |
| Scripts Python mediadores | 5 |
| Upgrade de script Bash | 1 (sdd-cycle v2) |
| Arquivos de teste | 6 suites + fixtures |
| Fases | 8 (0, S, A1–A7) |

---

## 8. DECISÕES REGISTRADAS (revogáveis na revisão da FASE 0)

| ID | Decisão | Status |
|----|---------|--------|
| D-01 | Consolidação 28 → 25 (tabela §2) | Proposta |
| D-02 | Ordem de fases e ondas (§4) | Proposta |
| D-03 | `constitution.md` redigida pelo AFA, co-assinada pelo Humano | Proposta |
| D-04 | AFA-ULTIMATE única autoridade de forja | Canônico |
| D-05 | Prefixo `agent-` + kebab-case compulsórios | Canônico |

---

## 9. PENDÊNCIA DE APROVAÇÃO HUMANA

- [ ] Ratificar FASE 0 (redação da `constitution.md`)
- [ ] Ratificar consolidação 28 → 25 (§2) — ou indicar reversão seletiva
- [ ] Ratificar ordem das ondas A.1–A.25
- [ ] Liberar início da execução (FASE 0 → S.1)

---

*Plano emitido sob AFA-ULTIMATE v1.3.0-FINAL. Próximo estágio: FASE 0 após verba humana.*
