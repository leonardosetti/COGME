# ANALISE DE VIABILIDADE — ONDA 8 (Expansão Administrativa/Gerencial/Desenvolvimento)
**Projeto:** COGME | **Forjador:** AFA-ULTIMATE v1.3.0-FINAL | **Data:** 2026-10-23
**Hardware:** 8700G / 60GB / llama.cpp CPU-only @ 8 t/s | **Jurisdição:** LGPD primária
**Metodo:** Pareto (§0.6.3) + Anti-subutilização (P-09) + Simplex (§0.6.2) + CSP (§0.6.4)

---

## 1. PAPEIS SOLICITADOS (45 itens brutos)

Foram solicitados 45 papeis (23 specialistas + 16 evaluadores + 1 arte/comunicacao/marketing/PR).
Aplicacao de Pareto + P-09: papeis dominados por agentes existentes sao incorporados como **vetores de agencia**, nao forjados como agentes ociosos.

### 1.1 Consolidacao por vetor de agencia (NAO forjados)

| Solicitado | Decisao | Absorvido por | Fundamento (trade-off Pareto) |
|---|---|---|---|
| Cyber Security Specialist | VETOR | agent-digital-security (L2) | Mesmo domínio; digital-security já cobre threat model, OWASP, CVE, segredos |
| Compliance Specialist | VETOR | agent-compliance-governance (L2) | Mesmo domínio; já cobre LGPD, Marco Civil, licenças, Bypass |
| Governance Specialist | VETOR | agent-compliance-governance (L2) | Governança é subconjunto de compliance; agente dedicado teria carga < 10% |
| QA/QE/SDET Master | VETOR | agent-qa-sdet (L2) | Consolidação C-01 já aplicada; triplicar contexto sem ganho |
| SDD Master | VETOR | agent-sdd-specialist (L1) | Já existe; SDD é o método canônico do projeto |
| Tech Architect Specialist | VETOR | agent-architect (L1) | Mesmo papel; ADR lifecycle e stack-drift já cobertos |

**Economia:** 6 agentes não forjados = ~21.000 tokens de prompt economizados + ~30 turnos de emissão evitados.

---

## 2. NOVOS AGENTES A FORJAR (25 agentes)

### 2.1 L1 — Comando/Estratégia (3 agentes)

| Slug | Camada | Papel | Justificativa |
|---|---|---|---|
| agent-business-analysis-specialist | L1 | specialist | Elicitacao de requisitos, modelagem de processos, analise de partes interessadas — gap atual no roster |
| agent-project-patterns-standards-specialist | L1 | specialist | Padroes reutilizaveis, padroes de codificacao, templates — cadeia de padroes ausente |
| agent-project-design-specialist | L1 | specialist | Solucao de design, padroes de design, esbocos arquitetonicos — design precede implementacao |

### 2.2 L2 — Execucao/Tecnica (12 agentes)

| Slug | Camada | Papel | Justificativa |
|---|---|---|---|
| agent-copyright-specialist | L2 | specialist | Autoria, obras derivadas, licencacao de saida criativa, dominio publico vs copyleft |
| agent-sldc-process-specialist | L2 | specialist | Ciclo de vida de desenvolvimento de software, portoes, criterios de entrada/saida |
| agent-quality-architect-specialist | L2 | specialist | Atributos de qualidade, design de portoes de qualidade, planejamento SQA |
| agent-iso-26514-specialist | L2 | specialist | ISO/IEC/IEEE 26514:2022 — requisitos de documentacao de sistemas e software |
| agent-ai-llm-rag-dag-mcp-roster-master-specialist | L2 | specialist | Engenharia de IA, inferencia local, pipeline RAG, orquestracao DAG, ponte MCP, dominio do roster |
| agent-cobit-specialist | L2 | specialist | COBIT — governanca de TI, objetivos de controle, praticas de gerencia |
| agent-itil-specialist | L2 | specialist | ITIL — gerenciamento de servicos de TI, incidente/mudanca/problema/service desk |
| agent-six-sigma-specialist | L2 | specialist | Six Sigma — DMAIC/DMADV, reducao de variacao, prevencao de defeitos |
| agent-art-communication-marketing-pr-specialist | L2 | specialist | Identidade visual, estrategia de comunicacao, relacoes publicas, apresentacao de entregaveis |

### 2.3 L3 — Evaluadores/Portoes (10 agentes)

| Slug | Camada | Papel | Justificativa |
|---|---|---|---|
| agent-clean-code-evaluator | L3 | gate | Avaliacao de codigo contra principios de clean code |
| agent-clean-architecture-evaluator | L3 | gate | Avaliacao de arquitetura contra principios de clean architecture |
| agent-pattern-evaluator | L3 | gate | Avaliacao de uso de padroes de projeto, deteccao de anti-padroes |
| agent-business-analysis-evaluator | L3 | gate | Avaliacao de qualidade de requisitos, revisao de analise de partes interessadas |
| agent-cyber-security-evaluator | L3 | gate | Avaliacao de controles de seguranca, revisao de modelagem de ameacas |
| agent-copyright-evaluator | L3 | gate | Avaliacao de conformidade de direitos autorais, avaliacao de obras derivadas |
| agent-compliance-evaluator | L3 | gate | Avaliacao de conformidade regulamentar, verificacao de trilha de auditoria |
| agent-governance-evaluator | L3 | gate | Avaliacao de governanca de TI, avaliacao de eficacia de controles |
| agent-sldc-process-evaluator | L3 | gate | Avaliacao de processo de desenvolvimento de software, eficacia de portoes |
| agent-architecture-evaluator | L3 | gate | Avaliacao de decisoes arquiteturais, revisao de integridade de design |
| agent-quality-architecture-evaluator | L3 | gate | Avaliacao de atributos de qualidade, revisao de eficacia SQA |
| agent-software-quality-guarantee-evaluator | L3 | gate | Avaliacao de garantia de qualidade de software, verificacao de prevencao de defeitos |
| agent-project-design-evaluator | L3 | gate | Avaliacao de solucao de design, revisao de esbocos arquitetonicos |

---

## 3. SCRIPTS CRIADOS/ATUALIZADOS (ONDA 8)

| Script | Funcao | Status |
|---|---|---|
| scripts/validate_nexus_yaml.py | AGENT_TOPOLOGY expandida (52 slugs); VECTORES_AGENCIA mapeados | ATUALIZADO |
| scripts/nexus_dispatcher.py | VALID_ACTIONS expandidas (health, communicate, integrate, secure, scan, monitor, perf, mcp, rag, dag, evaluate, certify) | ATUALIZADO |
| scripts/sync_agent_registry.py | Le automaticamente os novos frontmaters | COMPATIVEL (sem mudanca) |
| scripts/agent_health_check.py | Disponibilidade: arquivo, frontmatter, registry, score, drift | NOVO |
| scripts/agent_communication_hub.py | Envelopes half-duplex entre agentes; anti-auto-delegacao; kill_switch | NOVO |
| scripts/security_scan.py | Segredos versionados, hardware proibido, Kill Switch, Bypass, FAIL-CLOSED | NOVO |
| scripts/performance_monitor.py | Orcamento de tokens, secoes canonicas, contagens quantitativas | NOVO |
| scripts/registry_drift_monitor.py | Drift disco vs registry vs topologia | NOVO |
| scripts/dag_validator.py | DAG aciclica, anti-recursao, L0 unico, portoes L3 | NOVO |
| scripts/mcp_bridge.py | Ponte stub para MCP futuro (capacidades por agente) | NOVO |
| scripts/rag_indexer.py | Indexador stub para corpus RAG futuro | NOVO |

---

## 4. OPencode.JSON

Registra todos os 52 agentes (27 existentes + 25 novos) com:
- `prompt`, `mode`, `layer`, `role`, `hardware`, `ideology`
- `agentAdministration` com caminhos de scripts, registry, hardware profile, compliance

---

## 5. CORRECOES DE DAG (ciclos quebrados)

Foram quebrados 4 ciclos na DAG existente (violacao Art. 4.5):
1. `agent-github-specialist → agent-pm` removido (downstream)
2. `agent-gatekeeper → agent-github-specialist` removido (downstream)
3. `agent-po → agent-backend-dev` removido (downstream)
4. `agent-sdd-specialist → agent-pm` removido (downstream)
5. `agent-po → agent-sdd-specialist` removido (downstream)
6. `agent-pm → agent-project-analyst` removido (downstream)

Resultado: DAG aciclica, 52 slugs, zero erros.

---

## 6. CRITERIOS DE ACEITE DA FORJA (por agente, inegociaveis)

Per Art. 4.7 da Constituição e §0.9 da AFA-ULTIMATE:
- 16 secoes canonicas completas (sem placeholder)
- Score §0.9 >= 85/100 (`validate_afa_output.py`)
- YAML compatível (`validate_nexus_yaml.py`)
- Registro em `.ai/agents/registry.yaml` (`sync_agent_registry.py`)
- System prompt < 4000 tokens; emissao multi-turno (3-5 voltas)
- Ideologia §0.4 (LEFT, FOSS-first, LGPD primaria)
- Calibracao hardware §0.1 (CPU-only, 8700G/60GB, 8 t/s)

---

## 7. PLANO DE FORJA (lotes)

| Lote | Agentes | Camadas | Turnos estimados |
|---|---|---|---|
| 1 | business-analysis, project-patterns-standards, project-design | L1 | 9-12 |
| 2 | copyright, sldc-process, quality-architect, iso-26514, ai-llm-rag-dag-mcp-roster-master, cobit, itil, six-sigma, art-communication-marketing-pr | L2 | 27-36 |
| 3 | 13 evaluadores | L3 | 39-52 |

**Total estimado:** 75-100 turnos de emissao multi-turno.

---

## 8. INTEGRACAO FUTURA: RAG, DAG, MCP

- **RAG:** `scripts/rag_indexer.py` prepara corpus (constitution, specs, ADRs, planos). Indexacao/embeddings locais a implementar quando o servidor RAG for provisionado.
- **DAG:** `scripts/dag_validator.py` garante aciclicidade. `AGENT_TOPOLOGY` em `validate_nexus_yaml.py` e a fonte unica.
- **MCP:** `scripts/mcp_bridge.py` mapeia capacidades por agente (tools, resources, prompts). Zero rede; stdio/local apenas.

---

## 9. AUTORIZACAO REQUERIDA (Art. 4.9)

Per constituição Art. 4.9, alteracoes em `.opencode/` exigem autorizacao expressa do Humano **ciclo a ciclo**.
Solicito autorizacao para iniciar o **Lote 1** (3 agentes L1).

**Resposta esperada:** "AUTORIZADO Lote 1" ou ajustes ao plano antes de prosseguir.
