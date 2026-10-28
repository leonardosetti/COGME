# RELATÓRIO CONSOLIDADO — ANÁLISE DE REQUISITOS, CONSTITUIÇÃO, GAPS E PROPOSTAS

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira  
**Instituição:** Fatec Taquaritinga — ADS  
**Disciplina:** Gerência de Projetos  
**Gerente de Projeto:** Leonardo David Silva Setti  
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carleto  
**Versão:** 1.0  
**Data:** 27/10/2026  
**Status:** Para decisão e submissão ao repositório  
**Artefato base:** constitution.md v1.1.0, TAP v3 congelado (18/09/2026), plano-escopo v1.1, plano-producao-agentes v1.1

---

## 1. RESUMO EXECUTIVO

Este relatório consolida as análises críticas realizadas sobre a base normativa e de requisitos do projeto COGME, com foco em subsidiar a tomada de decisão para a escrita de specs (Specification-Driven Development — SDD).

O diagnóstico aponta que o projeto possui **15 requisitos canônicos** (REQ-01 a REQ-15) no TAP §5, mas apresenta **gaps estruturais críticos**: o artefato canônico de requisitos (`docs/requisitos/requisitos.md`) está vazio; os diretórios SDD (`.ai/specs/`, `.ai/handoffs/`) não existem; o roster de agentes (`.opencode/agents/`) está vazio; o TAP.md tem 0 linhas. Além disso, há **contradições fundamentais** entre a Constituição e os planos operacionais (modelo de IA, slug do orquestrador L0, fronteira IN/OUT vs requisitos órfãos da monografia).

O relatório propõe uma **taxonomia de níveis de necessidade (NN-1 a NN-4), prioridade (P0 a P3) e criticidade (C-1 a C-4)**, uma matriz de requisitos consolidada (existentes + novos), e um plano de ação corretiva ordenado por criticidade antes que qualquer spec funcional seja escrito.

---

## 2. METODOLOGIA E FONTES ANALISADAS

Foram analisados os seguintes artefatos do repositório:

| Artefato | Caminho | Status observado |
|---|---|---|
| Constituição do Projeto COGME | `constitution.md` | v1.1.0, co-assinada CCB 26/10/2026 |
| TAP Integral | `docs/planos/plano-integral-tap-1-2-3-4-5.md` | v3 congelado 18/09/2026 |
| TAP.md (referenciado) | `docs/tap/TAP.md` | **0 linhas** (vazio) |
| Plano de Escopo | `docs/planos/plano-escopo.md` | v1.1, 20/09/2026 |
| Plano de Produção de Agentes | `docs/planos/plano-producao-agentes.md` | v1.1, aguardando aprovação humana |
| Seção §5 Requisitos (draft) | `docs/conhecimento/drafts/principais_requisitos_entregas.md` | 11/09/2026 |
| Requisitos (artefato canônico) | `docs/requisitos/requisitos.md` | **0 linhas** (vazio) |
| Levantamento de Requisitos (monografia) | `Docs/md/Monografia/02_02_01_levantamento_de_requisitos.md` | REQ-01 a REQ-19 |
| Funcionalidades (monografia) | `Docs/md/Monografia/03_02_funcionalidades.md` | REQ-01 a REQ-19 |
| OKB v3.0 | `docs/conhecimento/OKB.md` | 20/09/2026 |
| ADRs | `docs/decisoes/ADR-001` a `ADR-006` | Misto Finalized/Draft |
| Scripts de governança | `scripts/nexus_dispatcher.py`, `validate_nexus_yaml.py`, `validate_afa_output.py`, `sync_agent_registry.py` | Presentes |
| Código-fonte | `src/` | Esqueleto (arquivos vazios) |
| Diretórios SDD | `.ai/specs/`, `.ai/handoffs/` | **Ausentes** |
| Roster de agentes | `.opencode/agents/` | **Vazio** |

---

## 3. ANÁLISE DA CONSTITUIÇÃO (v1.1.0)

### 3.1 Gap Estruturais (Arquitetura do Documento e Referências)

| ID | Descrição | Evidência | Severidade |
|---|---|---|---|
| **E-01** | Referência a `.ai/agents/registry.yaml` inexistente | Art. 4.4 declara como Roster SSOT; pasta `.ai/agents/` não existe | Crítica |
| **E-02** | Referência a `.opencode/agents/` inexistente | Art. 4.2 exige residência dos agentes; pasta não existe (glob vazio) | Crítica |
| **E-03** | Referência a `.ai/specs/` inexistente | Art. 6.1 e P-06 referenciam especificações SDD nesta pasta | Crítica |
| **E-04** | Referência a `.ai/handoffs/` inexistente | Art. 6.1 menciona handoffs parseados por `handoff_parser.py` | Crítica |
| **E-05** | TAP v3 referenciado é vazio/inesistente | Art. 1.3 ancorra congelamento em "TAP v3 (18/09/2026) §6"; `docs/tap/TAP.md` tem 0 linhas | Alta |
| **E-06** | ADR-005 referenciada como futura, mas existe como Draft vazia | Art. 1.3 diz que substitui TAP v3; `docs/decisoes/ADR-005-freeze.md` está Draft sem conteúdo | Alta |
| **E-07** | Ausência de índice/sumário e seção de definições | Documento sem sumário; termos como "marco M2", "promulgado", "CCB" não definidos | Média |
| **E-08** | Ausência de seção de revogações/disposições transitórias | Referencia versões anteriores (AFA v2.2, deprecated neutro/liberal) sem regras de transição | Média |

### 3.2 Incoerências Semânticas

| ID | Descrição | Evidência | Severidade |
|---|---|---|---|
| **S-01** | Conflito de modelo de IA: `qwen30b-moe` vs `Qwen 32B` | Art. 3 P-02 e âncora do cabeçalho declaram `qwen30b-moe`; `plano-escopo.md` §2.3.4 e `plano-producao-agentes.md` §1 declaram `Qwen 32B` | Alta |
| **S-02** | Identidade do orquestrador L0 dividida | Art. 4.5 e validador declaram `agent-nexus-prime-ultimate`; `plano-producao-agentes.md` (onda A.1) declara `agent-orchestrator` | Alta |
| **S-03** | CCB de "membro único" como decisor único | Art. 5.1 e 5.4 atribuem poder de veto/ratificação a um único Humano (GP) via "CCB de membro único" | Alta |
| **S-04** | "Promulgado" sem ciclo de vida definido | Termo aparece em Art. 4.4, 4.7, `nexus_dispatcher.py` mas não há definição de estados de agente | Média |
| **S-05** | Kill Switch enumerado parcialmente | Art. 4.6 cita apenas 6 vetores; diretiva AFA-ULTIMATE lista 15 vetores | Média |

### 3.3 Contradições Lógicas

| ID | Descrição | Evidência | Severidade |
|---|---|---|---|
| **L-01** | "Lei marcial inquestionável" vs processo de emenda | Cabeçalho final: "A Constituição é lei marcial: aplica-se, não se debate." Art. 9 prevê emendas | Média |
| **L-02** | Prazo de co-assinatura vencido sem não conformidade registrada | Art. 5.4: fechamento v1.0.0 deve ocorrer até M2 (30/09/2026); ocorreu 26/10/2026; sem registro de não conformidade pelo auditor | Alta |
| **L-03** | SHA-256 da v1.1.0 exclui a si mesmo | Changelog v1.1.0: hash sobre linhas anteriores ao bloco, não incluindo a si próprio; não verificável integralmente | Média |
| **L-04** | Gate de forja exige contagem divergente de seções | Art. 4.7: "19 cabeçalhos canônicos §§0–16"; `validate_afa_output.py`: "16 seções canônicas"; dicionário SECTIONS tem 19 entradas | Crítica |
| **L-05** | WIP ≤ 3 por pessoa vs total de 9 no time | Art. 4 (E-08 changelog) e plano-producao-agentes definem "3 × 3 pessoas = 9"; não há definição de quem são as 3 pessoas | Média |
| **L-06** | SDD requer `.ai/workflows/sdd-cycle.sh` não referenciado na Constituição | Plano-producao-agentes §1 e §4 referenciam `sdd-cycle.sh`; Constituição não o menciona nem inclui na hierarquia normativa (Art. 2) | Média |
| **L-07** | Containers Docker exigidos mas inexistentes no escopo técnico | Art. 10.1 exige camadas em containers Docker próprios; `plano-escopo.md` Tabela 1 não lista Docker como entregável; `.github/workflows/ci.yml` vazio | Alta |

### 3.4 Inconsistências Léxicas

| ID | Descrição | Evidência | Severidade |
|---|---|---|---|
| **X-01** | Mistura de PT-BR e EN sem regra de transição clara | P-10 diz slugs/código/contratos em EN; narrativa e erros em PT-BR. Constituição é quase toda PT-BR, mas nomes de scripts, chaves YAML, statuses e ações são EN | Média |
| **X-02** | Termo "forge" usado como substantivo e verbo sem definição | Art. 4.1 ("Forjador único"), Art. 4.7 ("Gate de forja"), plano-producao-agentes ("FASE A — Ondas de Forja"); nunca definido formalmente | Média |
| **X-03** | Acrônimos sem glossário | CCB, GP, DoR, DoD, SDD, TAP, EAP, AFA, LGPD, PII usados sem primeira ocorrência definida | Média |
| **X-04** | Inconsistência de numeração de artigos vs seções | Art. 4.7 menciona "seção faltante" mas não define qual; Art. 9.3 referencia "ADR-005" sem vincular ao número existente | Baixa |

### 3.5 Problemas Sintáticos

| ID | Descrição | Evidência | Severidade |
|---|---|---|---|
| **T-01** | Referência anafórica ambígua em Art. 1.3 | "Esta referência é substituída pela ADR-005..." — não claro se "esta referência" é TAP v3, congelamento, ou decisão do GP de 21/09/2026 | Média |
| **T-02** | Art. 4.6 sem verbo de regência claro para lista de vetores | Lista sem conectivos nem enumeração; pode ser interpretada como exemplos ou lista exaustiva | Média |
| **T-03** | Art. 5.4 com sentença longa e múltiplas subordinadas | Duas regras distintas em uma mesma frase com ponto-e-vírgula; dificulta extração de requisitos testáveis | Baixa |
| **T-04** | Cabeçalho com metadados misturados ao texto normativo | Linha 3 contém versão, ratificação, método, jurisdição, stack em comentário HTML único | Baixa |
| **T-05** | Falta de numeração de linhas ou âncoras estáveis para citação | Não há numeração de parágrafos ou IDs estáveis; referências apenas por "Art. X.Y" | Baixa |

---

## 4. ANÁLISE DE REQUISITOS EXISTENTES

### 4.1 REQ-01 a REQ-15 (Canônicos no TAP §5)

| ID | Requisito | Critério de Aceite | Fase EAP | MoSCoW | Fonte |
|---|---|---|---|---|---|
| REQ-01 | Simulação conversão cambial tempo real (USD/EUR → BRL) | Cotação via API externa, latência ≤ 2s | N5.2 | Must | TAP §5 / plano-escopo §2.3.2a |
| REQ-02 | 5 regimes de contratação (hora, dia, semana, mês, valor fixo) | 100% operacionais em UAT | N5.1 | Must | TAP §5 / plano-escopo §2.3.2a |
| REQ-03 | Encargos financeiros simulados (spread + IOF) | Cálculo auditável, 2 casas decimais | N5.1 | Must | TAP §5 / plano-escopo §2.3.2a |
| REQ-04 | Emissão invoice em PDF | WeasyPrint, ≤ 3s por documento | N5.4 | Must | TAP §5 / plano-escopo §2.3.2a |
| REQ-05 | Tempo de resposta aplicação | ≤ 3s em 95% das requisições (homologação) | N5.1 | Must | TAP §5 / plano-escopo §2.3.2a |
| REQ-06 | Interface web responsiva (FOSS) | Chrome/Firefox/Edge últimas 2 versões | N5.3 | Must | TAP §5 / plano-escopo §2.3.2a |
| REQ-07 | Cache de cotações (SQLite) | Redução ≥ 50% chamadas API externa | N5.2 | Must | TAP §5 / plano-escopo §2.3.2a |
| REQ-08 | Cobertura testes automatizados | ≥ 80% (pytest + coverage.py) | N6.1 | Must | TAP §5 / plano-escopo §2.3.2b |
| REQ-09 | UAT — 100% fluxos críticos | Zero defeitos críticos/bloqueantes | N6.2 | Must | TAP §5 / plano-escopo §2.3.2b |
| REQ-10 | Ferramentas qualidade (PDCA + Ishikawa 6M) | 12 PDCAs + diagrama causa-efeito | N6.3 | Should | TAP §5 / plano-escopo §2.3.2b |
| REQ-11 | Pipeline CI funcional | Lint + testes ≤ 5 min por push | N7.1 | Must | TAP §5 / plano-escopo §2.3.2c |
| REQ-12 | ADRs decisões arquiteturais críticas | Mínimo 3 ADRs (stack, Kanban, métricas) | N9.1 | Should | TAP §5 / plano-escopo §2.3.2d |
| REQ-13 | Rastreabilidade prompts SDD | 100% prompts catalogados em `.ai/handoffs/` | N9.3 | Should | TAP §5 / plano-escopo §2.3.2d |
| REQ-14 | Documentação técnica consolidada | Arquitetura + APIs OpenAPI revisadas | N11.1 | Should | TAP §5 / plano-escopo §2.3.2e |
| REQ-15 | Licenciamento 100% FOSS | Todas dependências OSI-approved | N1.5 + N4.4 | Must | TAP §5 / plano-escopo §2.3.2f |

### 4.2 REQ-16 a REQ-19 (Monografia — Órfãos)

| ID | Requisito | Status | Observação |
|---|---|---|---|
| REQ-16 | Integração API PTAX (Banco Central) | Pendente | Conflito possível com REQ-01 (API externa genérica vs PTAX específica) |
| REQ-17 | Comparativo custo entre provedores pagamento internacional | Pendente | Colapsa com fronteira OUT ("integração plataformas transferência") |
| REQ-18 | Ranqueamento menor custo efetivo total | Pendente | Depende de REQ-17 |
| REQ-19 | Encaminhamento usuário ao provedor selecionado | Pendente | Dependente de REQ-17/18 |

### 4.3 Fronteira de Escopo (IN / OUT)

| IN (aprovado) | OUT (excluído por YAGNI) |
|---|---|
| Simulação cambial USD/EUR → BRL tempo real | Outras moedas (GBP, JPY, CHF) |
| 5 regimes de contratação | Cadastro multiusuário / autenticação |
| Spread + IOF, 2 casas decimais | Integração plataformas transferência |
| Invoice PDF via WeasyPrint ≤ 3s | NF-e / NFS-e |
| Interface web responsiva FOSS | App mobile nativo |
| Cache SQLite cotações | Banco relacional multiusuário (PostgreSQL) |
| Coverage ≥ 80%, UAT 100% fluxos críticos | Testes carga/estresse |
| Pipeline CI lint+testes ≤ 5 min | Continuous deployment produção |
| ADRs + catálogo prompts SDD | Documentação usuário final PDF |
| Stack 100% FOSS auditável | Bibliotecas proprietárias / serviços pagos |

**Implicação:** REQ-17, REQ-18, REQ-19 exigem integração com plataformas de transferência (OUT). Especs para esses requisitos são scope creep sem change-request.

### 4.4 Gaps entre Fontes

| # | Problema | Fontes em conflito | Impacto |
|---|---|---|---|
| G-01 | `docs/requisitos/requisitos.md` vazio | plano-escopo §2.3.2 aponta para ele como canônico M2 | Sem fonte SSOT para specs |
| G-02 | Modelo de IA divergente | Constituição (`qwen30b-moe`) vs planos (`Qwen 32B`) | Specs de IA/LLM sem alvo técnico |
| G-03 | Slug L0 dividido | Constituição (`agent-nexus-prime-ultimate`) vs plano-producao-agentes (`agent-orchestrator`) | Specs de DAG/dispatcher ambíguos |
| G-04 | REQ-16 a REQ-19 não no TAP §5 | Monografia vs TAP Tabela 3 | Especs para esses requisitos fora do escopo autorizado |
| G-05 | REQ-17/18/19 conflitam com fronteira OUT | Monografia vs plano-escopo Tabela 1 | Necessário change-request antes de especar |
| G-06 | Datas de marcos divergentes | draft §5 C2 (22/09) vs TAP Tabela 4 (30/09 M2) | Datas de specs vinculadas a marcos precisam fonte canônica |
| G-07 | TAP.md vazio | docs/tap/TAP.md (0 linhas) vs plano-integral-tap | Referências a "TAP §5" apontam para documento inexistente |

---

## 5. TAXONOMIA PROPOSTA PARA ESCRITA DE SPECS

### 5.1 Níveis de Necessidade (NN)

| Código | Nome | Definição | Regra de inclusão |
|---|---|---|---|
| **NN-1** | Core (Núcleo) | Indispensável para o MVP acadêmico; sem ele o projeto não cumpre o TAP | Incluir obrigatoriamente; spec com critério de aceite quantificável |
| **NN-2** | Estendido | Importante para qualidade operacional, mas não bloqueia o marco | Incluir com prioridade P1/P2; pode ser descerrado em change-request |
| **NN-3** | Opcional | Nice-to-have; valor incremental sem impacto na entrega acadêmica | Incluir apenas em backlog (Won't); não gera spec neste ciclo |
| **NN-4** | Externo/Futuro | Fora do escopo atual (YAGNI); exigiria change-request e alteração de fronteira | Não escrever spec; documentar como rejeitado ou diferido |

### 5.2 Prioridade (P)

| Código | Nome | Definição | Marco associado |
|---|---|---|---|
| **P0** | Bloqueante | Sem entrega, o marco não ocorre | M2 (ambiente), M3 (MVP) |
| **P1** | Necessário | Necessário para pleno funcionamento do marco | M3 |
| **P2** | Desejável | Melhora usabilidade/qualidade; não bloqueia | M4 |
| **P3** | Postergável | Pode ir para ciclo futuro | Pós-M4 |

### 5.3 Criticidade (C)

| Código | Nome | Definição | Impacto se não entregue |
|---|---|---|---|
| **C-1** | Crítica | Falha impede entrega do marco ou validação acadêmica | Não conformidade no M3/M4 |
| **C-2** | Alta | Degrada funcionalidade principal, mas há workaround | UAT com ressalvas |
| **C-3** | Média | Débito técnico ou limitação de usabilidade | Retrabalho pós-entrega |
| **C-4** | Baixa | Aperfeiçoamento sem impacto na entrega | Pode ser omitido |

---

## 6. MATRIZ DE REQUISITOS PROPOSTA (Existentes + Novos)

### 6.1 REQ-01 a REQ-15 (Canônicos)

| Req | NN | P | C | Justificativa | Specs a escrever |
|---|---|---|---|---|---|
| REQ-01 | NN-1 | P0 | C-1 | Coração do MVP; TAP §5; fronteira IN | `spec-conversao-cambial`, `spec-api-cotacao` |
| REQ-02 | NN-1 | P0 | C-1 | Obrigatório no TAP; UAT 100% | `spec-regimes-contratacao` |
| REQ-03 | NN-1 | P0 | C-1 | Encargos financeiros; precisão 2 casas | `spec-calculo-encargos` |
| REQ-04 | NN-1 | P0 | C-1 | Entrega documental; WeasyPrint ≤ 3s | `spec-emissao-pdf` |
| REQ-05 | NN-1 | P0 | C-2 | Desempenho; ambiente homologação | `spec-desempenho-aplicacao` |
| REQ-06 | NN-1 | P0 | C-2 | Navegadores FOSS; N5.3 | `spec-interface-web` |
| REQ-07 | NN-2 | P1 | C-2 | Redução ≥ 50% chamadas API | `spec-cache-cotacoes` |
| REQ-08 | NN-1 | P0 | C-1 | Qualidade fechada (P-06) | `spec-cobertura-testes` |
| REQ-09 | NN-1 | P0 | C-1 | Validação acadêmica; zero defeitos críticos | `spec-uat-fluxos-criticos` |
| REQ-10 | NN-2 | P2 | C-3 | Demanda acadêmica avaliador | `spec-ferramentas-qualidade` |
| REQ-11 | NN-1 | P0 | C-1 | DevOps; gate de integração | `spec-pipeline-ci` |
| REQ-12 | NN-2 | P1 | C-3 | Rastreabilidade arquitetural; mínimo 3 ADRs | `spec-adr-template` |
| REQ-13 | NN-1 | P0 | C-1 | SDD com IA auditável; `.ai/handoffs/` obrigatório | `spec-rastreabilidade-prompts` |
| REQ-14 | NN-2 | P2 | C-3 | M4; doc usuário final está OUT | `spec-documentacao-tecnica` |
| REQ-15 | NN-1 | P0 | C-1 | P-02, P-03, P-10; dependências OSI-approved | `spec-conformidade-foss` |

### 6.2 REQ-16 a REQ-19 (Decisão necessária)

| Req | NN | P | C | Decisão proposta |
|---|---|---|---|---|
| REQ-16 | NN-3 | P3 | C-3 | Diferir — change-request se necessário |
| REQ-17 | NN-4 | — | — | Rejeitar no MVP; reavaliar pós-M4 |
| REQ-18 | NN-4 | — | — | Rejeitar no MVP |
| REQ-19 | NN-4 | — | — | Rejeitar no MVP |

### 6.3 Novos Requisitos Sugeridos (Gaps Funcionais e de Governança)

| Novo Req | Nome | NN | P | C | Justificativa |
|---|---|---|---|---|---|
| REQ-20 | Artefato canônico de requisitos publicado | NN-1 | P0 | C-1 | `docs/requisitos/requisitos.md` vazio; specs precisam de fonte SSOT |
| REQ-21 | Diretórios SDD criados (`.ai/specs/`, `.ai/handoffs/`) | NN-1 | P0 | C-1 | Sem eles, REQ-13 e ciclo SDD impossíveis |
| REQ-22 | Agentes L0 e L1 promulgados no roster | NN-1 | P0 | C-1 | Sem agentes, specs não têm destino de execução |
| REQ-23 | Modelo de IA unificado (qwen30b-moe ou Qwen 32B) | NN-1 | P0 | C-2 | Divergência entre Constituição e planos |
| REQ-24 | Identidade L0 unificada (slug único) | NN-1 | P0 | C-2 | Dois slugs para orquestrador quebram DAG |
| REQ-25 | Taxonomia NN/P/C | NN-2 | P1 | C-3 | Specs precisam classificar Core vs Opcional |
| REQ-26 | LGPD/PII em specs (zero PII em artifacts técnicos) | NN-1 | P0 | C-1 | P-04 Constituição |
| REQ-27 | Critério de aceite quantificável obrigatório em todo spec | NN-1 | P0 | C-2 | P-08 (honestidade) |
| REQ-28 | Handoff associado a todo spec de implementação | NN-2 | P1 | C-2 | REQ-13; rastreabilidade SDD |
| REQ-29 | Revisão de pares obrigatória antes de aprovar spec | NN-2 | P1 | C-3 | P-06 (gate reviewer → gatekeeper) |
| REQ-30 | Observabilidade local (logs, métricas, sem nuvem) | NN-2 | P1 | C-3 | P-02 (soberania computacional) |

---

## 7. PROPOSTAS CORRETIVAS ORDENADAS POR CRITICIDADE

### 7.1 Corretivas Imediatas (antes de escrever qualquer spec funcional)

| ID | Ação | Gap endereçado | Responsável | Prazo |
|---|---|---|---|---|
| **C-01** | Publicar `docs/requisitos/requisitos.md` com REQ-01 a REQ-15 consolidados, incluindo colunas NN, P, C | GE-01 | GP / PO | Imediato |
| **C-02** | Criar `.ai/specs/` e `.ai/handoffs/` com template de spec vazio e handoff HF-0000 | GE-02 | SDD Specialist | Imediato |
| **C-03** | Criar `.opencode/agents/` com `agent-nexus-prime-ultimate.md` (frontmatter válido) e rodar `sync_agent_registry.py --check` até `[OK]` | GE-03, GF-05 | NEXUS-PRIME / AFA | Imediato |
| **C-04** | Preencher `docs/tap/TAP.md` com conteúdo canônico ou redirecionar referências para `plano-integral-tap-*.md` | GE-04 | GP | Curto prazo |
| **C-05** | Emitir ADR unificando modelo de IA: escolher `qwen30b-moe` (Constituição) ou `Qwen 32B` e atualizar todas as fontes | GF-04 | GP + Arquiteto | Curto prazo |
| **C-06** | Emitir ADR unificando slug L0: manter `agent-nexus-prime-ultimate` e corrigir `plano-producao-agentes.md` | GF-05 | NEXUS-PRIME | Curto prazo |
| **C-07** | Abrir change-request para REQ-16 a REQ-19: decidir incluir (alterar fronteira IN/OUT) ou rejeitar formalmente (Won't) | GF-01, GF-02 | GP / CCB | Antes de qualquer spec desses requisitos |

### 7.2 Corretivas de Governança de Specs

| ID | Ação | Gap endereçado | Responsável | Prazo |
|---|---|---|---|---|
| **C-08** | Aprovar taxonomia NN/P/C como política de specs | GF-03 | GP | Curto prazo |
| **C-09** | Criar template obrigatório de spec com campos: NN, P, C, rastreabilidade TAP/EAP, critério de aceite GWT, declaração LGPD (PII), handoff associado | GF-06, REQ-27, REQ-28 | SDD Specialist | Curto prazo |
| **C-10** | Definir fluxo de aprovação de specs: rascunho → revisão de pares (Padrão A/B OKB) → aprovação GP → publicação em `.ai/specs/` | GF-06, REQ-29 | Gatekeeper / Reviewer | Curto prazo |

### 7.3 Corretivas Funcionais (Escrita de specs)

| ID | Ação | Requisitos alvo | Prioridade |
|---|---|---|---|
| **C-11** | Escrever `spec-conversao-cambial` | REQ-01 | P0 / C-1 |
| **C-12** | Escrever `spec-regimes-contratacao` | REQ-02 | P0 / C-1 |
| **C-13** | Escrever `spec-calculo-encargos` | REQ-03 | P0 / C-1 |
| **C-14** | Escrever `spec-emissao-pdf` | REQ-04 | P0 / C-1 |
| **C-15** | Escrever `spec-pipeline-ci` | REQ-11 | P0 / C-1 |
| **C-16** | Escrever `spec-rastreabilidade-prompts` | REQ-13 | P0 / C-1 |
| **C-17** | Escrever `spec-conformidade-foss` | REQ-15 | P0 / C-1 |
| **C-18** | Escrever `spec-cobertura-testes` | REQ-08 | P0 / C-1 |
| **C-19** | Escrever `spec-uat-fluxos-criticos` | REQ-09 | P0 / C-1 |
| **C-20** | Escrever `spec-desempenho-aplicacao` | REQ-05 | P0 / C-2 |
| **C-21** | Escrever `spec-interface-web` | REQ-06 | P0 / C-2 |
| **C-22** | Escrever `spec-cache-cotacoes` | REQ-07 | P1 / C-2 |

---

## 8. ORDEM RECOMENDADA DE ESCRITA DE SPECS

Dado o WIP limit ≤ 3 (Constituição via E-08 / plano-escopo) e o half-duplex (NEXUS-PRIME ULTIMATE):

**Onda 1 — Fundação (specs que habilitam todos os outros):**
1. `spec-rastreabilidade-prompts` (REQ-13) — sem ela, não há SDD auditável
2. `spec-conformidade-foss` (REQ-15) — restringe todas as dependências dos specs seguintes
3. `spec-conversao-cambial` (REQ-01) — núcleo funcional do MVP

**Onda 2 — Funcionais MVP:**
4. `spec-regimes-contratacao` (REQ-02)
5. `spec-calculo-encargos` (REQ-03)
6. `spec-emissao-pdf` (REQ-04)

**Onda 3 — Qualidade e Infra:**
7. `spec-pipeline-ci` (REQ-11)
8. `spec-cobertura-testes` (REQ-08)
9. `spec-uat-fluxos-criticos` (REQ-09)

**Onda 4 — Não funcionais e estendidos:**
10. `spec-desempenho-aplicacao` (REQ-05)
11. `spec-interface-web` (REQ-06)
12. `spec-cache-cotacoes` (REQ-07)

**Não escrever specs para:** REQ-17, REQ-18, REQ-19 enquanto não houver change-request aprovado alterando a fronteira IN/OUT. REQ-16 apenas se aprovado como escopo estendido.

---

## 9. RESUMO EXECUTIVO PARA DECISÃO (PT-BR)

O COGME possui 15 requisitos canônicos no TAP, mas **não possui artefato canônico publicado** (`docs/requisitos/requisitos.md` vazio), **não possui diretórios SDD** (`.ai/specs/`, `.ai/handoffs/` ausentes) e **não possui agentes promulgados** (`.opencode/agents/` vazio). Além disso, 4 requisitos da monografia (REQ-16 a REQ-19) estão órfãos e colidem com a fronteira de escopo OUT.

Antes de escrever qualquer spec funcional, é obrigatório:
1. Publicar o artefato de requisitos consolidado (C-01);
2. Criar a infraestrutura SDD e o roster de agentes (C-02, C-03);
3. Unificar modelo de IA e identidade L0 (C-05, C-06);
4. Decidir o destino dos REQ-16 a REQ-19 via change-request (C-07);
5. Aprovar a taxonomia NN/P/C e o template de spec (C-08, C-09).

Somente após essas corretivas, a escrita de specs terá fonte de verdade, destino de execução e governança de qualidade, evitando retrabalho e scope creep.

---

## 10. APÊNDICES

### Apêndice A — Referências Cruzadas Constituição × Scripts

| Artigo Constituição | Script associado | Status do script | Gap identificado |
|---|---|---|---|
| Art. 4.2 | `validate_nexus_yaml.py` | Presente | `.opencode/agents/` vazio |
| Art. 4.4 | `sync_agent_registry.py` | Presente | `.ai/agents/registry.yaml` ausente |
| Art. 4.5 | `nexus_dispatcher.py` | Presente | Depende de registry e DAG válidos |
| Art. 4.7 | `validate_afa_output.py` | Presente | Contagem de seções divergente (16 vs 19) |
| Art. 6.1 | `handoff_parser.py` | Presente | `.ai/handoffs/` ausente |

### Apêndice B — Modelo de Template de Spec (Padrão SDD)

```markdown
# SPEC-XXX — <título>

## Metadados
- task_id: TA-NNNN
- requisito: REQ-XX (ou "NOVO — pendente change-request")
- fase_eap: NX.Y
- objetivo_smart: <Produto|Qualidade|Cronograma|Métricas|Inovação>
- dominio_pmbok: <Entrega|Medição|...>
- nn: <NN-1|NN-2|NN-3|NN-4>
- prioridade: <P0|P1|P2|P3>
- criticidade: <C-1|C-2|C-3|C-4>
- status: <rascunho|revisão|aprovado|obsoleto>
- dependencias: [SPEC-YYY, ...]
- handoff: HF-NNNN (se aplicável)
- lgpd_pii: "não" (declaração de ausência de PII)

## Contexto
<descrição do problema, origem (TAP/monografia/draft), por que este spec existe>

## Requisitos Funcionais
- RF-01: ...
- RF-02: ...

## Requisitos Não Funcionais
- RNF-01 (performance): ...
- RNF-02 (FOSS/licença): ...
- RNF-03 (LGPD/PII): ...

## Critérios de Aceite (Given/When/Then — Padrão B, OKB §9.3)
Dado <contexto>, quando <ação>, então <resultado mensurável>.

## Fronteira (IN / OUT)
O que este spec cobre e o que explicitamente exclui.

## Rastreabilidade
- ← TAP §5, Tabela 3
- ← EAP NX.Y
- ← plano-escopo Tabela 1 (IN/OUT)

## Decisões de Design
<ADR associada se houver impacto arquitetural>

## Testes Esperados
- unidade: ...
- integração: ...
- UAT: ...

## Open Questions
<itens que precisam de decisão do GP/CCB antes de implementar>
```

---

*Relatório produzido sob a ótica NEXUS-PRIME ULTIMATE L0. Não há implementação de código proposta; apenas roteiro de requisitos, gaps e decisões necessárias para escrita de specs.*
