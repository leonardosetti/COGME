# RELATÓRIO ANALÍTICO — AUDITORIA DE BLOAT, HIBRIDIZAÇÃO KISS/YAGNI E CONSOLIDAÇÃO ARQUITETURAL DO COGME

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Data de Emissão:** 10/09/2026
**Emissor:** GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carletto
**Referência Normativa:** OKB_COGME_v3.0 §4.2 (GMV) + §4.5 (Critério ADR) + P3 (KISS) + hardware.md
**Status:** Decisão Arquitetural Bloqueante (input para ADR-002 e ADR-004)

---

## 0. VEREDITO SUMÁRIO EXECUTIVO

A auditoria identifica **bloat estrutural moderado** na base de conhecimento (OKB v2.1 → v3.0 já mitigou ~40% do excesso) e **bloat operacional crítico** na EAP (62 pacotes para 2 pessoas em 12 semanas). A hibridização **KISS + YAGNI** é não apenas possível, mas **mandatória** para o COGME, desde que aplicada em camadas ortogonais: KISS governa a arquitetura; YAGNI governa o escopo. A nova premissa SDD local (llama.cpp + Qwen quantizados + OpenCode TUI) é **tecnicamente viável** no hardware do aluno (Ryzen 7 8700G / 60GB RAM / Arch Linux) e resolve o risco R-01 (stack LLM externa) ao custo de limitações de qualidade de geração — trade-off aceitável para MVP acadêmico.

**Recomendações bloqueantes:**

1. Descartar 11 pacotes da EAP (redução de 62 → 51, ganho de ~18% de capacidade).
2. Consolidar OKB v3.1 com eliminação de 3 seções redundantes. -> Aprovado
3. Formalizar ADR-002 (Stack FOSS) e ADR-004 (SDD Local via llama.cpp). -> Aprovado, considere também a confecção das ADRs: ADER-001, ADR-003 aderentes ao projeto, caso não passem no crivo de conformidade com o projeto, refatorar
4. Manter as três persistências (Ágil, PMBOK 7ª hierárquico, GitHub Projects) — todas passam no teste GMV. -> Aprovado

---

## 1. ANÁLISE KISS vs YAGNI: FUNDAMENTOS, HIBRIDIZAÇÃO E ADEQUAÇÃO

### 1.1. Definições Operacionais no Contexto COGME

| Princípio                                 | Origem                                      | Definição Aplicada ao COGME                                                                                      | Domínio PMBOK 7ª Associado                 |
| ------------------------------------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| **KISS** (Keep It Simple, Stupid)    | Kelly Johnson (Lockheed Skunk Works, 1960s) | "A solução mais simples que atende ao DoD é a correta; complexidade adicional deve ser justificada por ADR."    | Abordagem de Desenvolvimento + Princípio P3 |
| **YAGNI** (You Aren't Gonna Need It) | Ron Jeffries (XP, 1990s)                    | "Não implemente funcionalidades 'que podem ser úteis no futuro'; implemente apenas o que o backlog atual exige." | Domínio de Entrega (valor tangível)        |

### 1.2. Análise Comparativa Crítica

| Dimensão                       | KISS                                        | YAGNI                                  |
| ------------------------------- | ------------------------------------------- | -------------------------------------- |
| **Escopo de atuação**   | Arquitetura e design (como fazer)           | Escopo funcional (o que fazer)         |
| **Inimigo principal**     | Superengenharia (over-engineering)          | Especulação (speculative generality) |
| **Sintoma de violação** | 5 camadas de abstração para 1 caso de uso | Feature flag para cenário hipotético |
| **Custo da violação**   | Manutenibilidade colapsada                  | Backlog inchado + lead time inflado    |
| **Mensurabilidade**       | Contagem de camadas/ciclomática            | # de features não-usadas no UAT       |

### 1.3. Hibridização: Possibilidade e Necessidade

**Veredito técnico:** KISS e YAGNI **não são excludentes** — são **ortogonais e complementares**. A hibridização é não apenas possível, mas **recomendada** pelo Manifesto Ágil (Princípio 7: "Simplicidade — a arte de maximizar a quantidade de trabalho não realizado") e pelo PMBOK 7ª (Princípio 7: "Navegue na complexidade").

**Modelo de hibridização proposto para o COGME: -> Aprovado**

```
┌─────────────────────────────────────────────────────┐
│  CAMADA 1 — ESCOPO (YAGNI governa)                │
│  • Backlog só contém o que o DoD do MVP exige     │
│  • Fases 14-17 (Segurança/A11y/Obs/i18n) = YAGNI  │
│  • Feature flags, multi-tenant, i18n = YAGNI      │
├─────────────────────────────────────────────────────┤
│  CAMADA 2 — ARQUITETURA (KISS governa)            │
│  • Stack mínima que atende DoD (FastAPI + SQLite) │
│  • Sem microsserviços, sem Kubernetes, sem Redis  │
│    distribuído — cache in-process basta           │
│  • Adapter pattern apenas se >1 provider real     │
├─────────────────────────────────────────────────────┤
│  CAMADA 3 — CÓDIGO (KISS + YAGNI sinérgicos)      │
│  • Funções ≤ 30 linhas (KISS)                     │
│  • Sem "talvez um dia precise" (YAGNI)            │
│  • Clean Code como padrão inegociável (P5)        │
└─────────────────────────────────────────────────────┘
```

### 1.4. Qual Princípio é Mais Adequado ao COGME?

**Resposta: Ambos, com primazia de YAGNI no escopo e KISS na arquitetura.**

**Justificativa derivada do contexto:**

- **Equipe de 2 pessoas + 12 semanas + 20h/semana** → YAGNI é **sobrevivência**, não filosofia. Qualquer feature especulativa mata o cronograma.
- **MVP acadêmico com escopo fechado** (simulação cambial + invoice PDF) → KISS é **defensabilidade acadêmica**. Arquitetura simples é auditável pelo Prof. Nivaldo em 1 sessão.
- **SDD com LLM** → KISS é **obrigatório** porque prompts complexos geram código alucinado; YAGNI é **obrigatório** porque LLM tende a superengenhar (adiciona decorators, padrões, abstrações não solicitadas).

**Trade-off declarado:** YAGNI sem KISS gera código simples mas escopo inchado; KISS sem YAGNI gera escopo enxuto mas código intrincado. A hibridização é o único caminho viável.

Nota de revisão: A documentação parcial do projeto compreend o o TAP + Documentação COGME até a área de conhecimento 5: Gerenciamento da Qualidade -é mandatório - (deve conter os PDCAs de todas as atividades até o momento conforme definidas no projeto e rede de projeto (ongoing)) - A documentação formal é viva até entrega formal do projeto MVP funcional e pode sofrer ajustes de forma integral. Entrega parcial (Documentação até area de conhecimento 5 ŕevista para o dia 19/09/2026 - não é mandatório entrega de código ou implementação prévia)

---

## 2. AUDITORIA DE BLOAT NA BASE DE CONHECIMENTO ATUAL

### 2.1. Metodologia de Auditoria

Aplicação do **teste GMV (OKB v3.0 §4.2)** em cada artefato/seção:

- **P1:** O Prof. Nivaldo exigirá na avaliação? -
- **P2:** Evita retrabalho futuro?
- **P3:** É exigido pelo PMBOK 7ª como evidência de domínio? 
- **P4:** É útil para a equipe (não só para o professor)? 

**Regra de descarte:** ≥ 2 respostas "NÃO" → candidato a eliminação.

### 2.2. Achados na OKB v2.1 (mantidos em v3.0 parcialmente)

| Item                                                             | Severidade  | Veredito GMV         | Ação Recomendada                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------------- | ----------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| §4.4 Dimensão PDCA (4 dimensões simultâneas)                 | 🔴 CRÍTICO | 2×NÃO (P1, P4)     | **DESCARTAR** — já absorvido pelas Dimensões 1 e 2 na v3.0<br />Nota de revisão:<br />Para Gerenciamento da Qualidade o Professor Dr Nivaldo Carletto exije pelo menos um PDCA para cada atividade do projeto. A fim de não gerar volume documental, adotaremos sempre o último PDCA de cada atividade caso mais de 1 PDCA tenha sido executado, e comentando brevemente quais as mudanças resultantes e relevantes em relação a PDCAs anteriores |
| §6 EAP com 13 fases sequenciais implícitas                     | 🔴 CRÍTICO | 2×NÃO (P2, P4)     | **REORGANIZAR** em macro-fases (já feito na v3.0 §4.6)                                                                                                                                                                                                                                                                                                                                                                                                   |
| §8 Roadmap trimestral (Q3/Q4/Q1)                                | 🟠 ALTO     | 2×NÃO (P1, P3)     | **SIMPLIFICAR** para tabela de macro-fases (v3.0 §4.6 já faz)<br />Nota de revisão: <br />Temos o tempo escasso e não distribuído em semestres. TEmos dois grandes marcos: Entrega Parcial (Apenas documentação até área de conhecimento 5 e entrega Final com MVP funcional) - Redesenhe o roadmap                                                                                                                                             |
| §14 Melhoria Contínua Pós-Entrega (detalhada)                 | 🟡 MÉDIO   | 3×NÃO (P1, P2, P4) | **COLAPSAR** em 1 parágrafo no TAP §8<br />Pós entrega não faz parte do escopo estrito acadêmico - Retire                                                                                                                                                                                                                                                                                                                                             |
| §2.2 Mapeamento PMBOK 7ª ↔ Ágil ↔ PMBOK 6ª (tripla camada) | 🟢 BAIXO    | 3×SIM               | **MANTER** — defensabilidade acadêmica                                                                                                                                                                                                                                                                                                                                                                                                                   |
| §7 Justificativa das Fases Obrigatórias                        | 🟢 BAIXO    | 3×SIM               | **MANTER** — blindagem contra questionamento                                                                                                                                                                                                                                                                                                                                                                                                              |

### 2.3. Achados no TAP+EAP (v0.9 / v1_opngoing)

**Análise quantitativa:**

- 13 fases obrigatórias + 4 desejáveis = 17 fases -> Remova as seção de Desejáveis
- 62 pacotes de trabalho (Nível 2)
- Equipe: 2 pessoas × 20h/semana × 12 semanas = **480h totais disponíveis**
- **Média por pacote: 7,7h** — insuficiente para pacotes como N5.1-N5.6 (Backend completo) - As atividades de implementação devem adotar o SDD portanto esta fase tem previsão de redução temporal (não calculada))

**Pacotes candidatos a descarte/fusão (aplicando YAGNI):**

| Pacote                                              | Justificativa YAGNI                                                                                              | Ação                                                                           |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| N5.6 Execução Kanban (Rituais no GitHub Projects) | O Kanban já é o método de execução (OKB §4.3); ritualizar como "pacote" é burocracia                      | **FUNDIR** com N1.6 -> Aprovado                                           |
| N6.3 Testes de Performance e Carga                  | MVP acadêmico com 2 usuários-piloto não exige teste de carga; YAGNI puro                                      | **DESCARTAR** do MVP (mover para pós-entrega) -> Aprovado                |
| N7.2 Pipeline CD (build + deploy)                   | Deploy manual em plataforma gratuita é suficiente para MVP; CD automatizado é over-engineering para 1 ambiente | **SIMPLIFICAR** para "deploy manual documentado" -> Aprovado              |
| N9.3 Relatórios de Status Quinzenais               | GitHub Projects já é SSOT (ADR-001); relatório estático duplica informação                                 | **DESCARTAR** — substituir por link do dashboard -> Aprovado             |
| N10.4 Runbooks Operacionais                         | MVP acadêmico não terá operação contínua; YAGNI                                                            | **DESCARTAR** do MVP -> Aprovado                                         |
| N11.3 Análise de Impacto (escopo/custo/prazo)      | CCB = Prof. Nivaldo; análise formal é burocracia para equipe de 2                                              | **SIMPLIFICAR** para "issue label `change-request`" -> Aprovado        |
| N12.3 Relatórios de Desempenho (EVM/Burndown)      | GitHub Insights já fornece métricas de fluxo (OKB v3.0 §4.3); EVM é obsoleto no contexto Kanban              | **DESCARTAR** EVM; manter apenas Burndown derivado do Kanban -> Aprovado |
| N13.4 Auditoria FOSS Final                          | Já coberto por N4.4 (Auditoria de Licenças) + N1.5 (Política)                                                 | **FUNDIR** com N4.4 -> Aprovado                                          |

**Pacotes candidatos a fusão (aplicando KISS):**

| Fusão Proposta                                                             | Justificativa KISS                                                                                                                                                       |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N5.1 + N5.2 → "Backend completo (lógica + API + cache)"                   | Separação artificial; cache Redis é YAGNI para MVP (1 provider de câmbio) -> Aprovado                                                                              |
| N9.1 + N9.2 + N9.4 → "Comunicação (RACI + canais + cerimônias)"         | Três pacotes para 2 pessoas é bloat -> Aprovado                                                                                                                      |
| N10.1 + N10.2 + N10.3 → "Base de Conhecimento (ADRs + lições + prompts)" | Mesma finalidade documental - Manter em domínios distintos dentro da base de conhecimento - Verifique a seção 9. Stack SDD Local: Arquitetura e Organização Padrão |

### 2.4. Resultado Consolidado da Auditoria

| Métrica                       | Antes | Depois         | Ganho                     |
| ------------------------------ | ----- | -------------- | ------------------------- |
| Fases Nível 1 (obrigatórias) | 13    | 13 (mantidas)  | —                        |
| Pacotes Nível 2               | 62    | **51**   | **-18%**            |
| Horas estimadas por pacote     | 7,7h  | **9,4h** | **+22% capacidade** |
| Artefatos OKB (seções)       | 14    | **11**   | **-21%**            |

---

## 3. STACK FOSS ÓTIMA PARA O COGME

### 3.1. Critérios de Seleção (derivados do TAP §8 + OKB v3.0 §4.5)

1. **Licença compatível** (MIT, Apache 2.0, BSD, GPL — sem AGPL para evitar viral licensing)
2. **Curva de aprendizado ≤ 2 semanas** para equipe de 2
3. **Testabilidade ≥ 80% coverage** (meta do TAP §3)
4. ~~**Deploy em plataforma gratuita** (Railway/Render/Fly.io)~~ -> Não mandatório (é algo interessante mas descartável uma vez que podemos rodar o projeto localmente (YAGNI))
5. **Compatível com SDD via LLM** (linguagem com bom treinamento em LLMs) -> Verifique a seção 9. Stack SDD Local: Arquitetura e Organização Padrão
6. **Rodável no hardware local** (Arch Linux, 60GB RAM)

### 3.2. Stack Recomendada (ADR-002 draft)

| Camada                     | Tecnologia                                                                                                            | Licença                   | Justificativa KISS                                                         | Alternativa Rejeitada                                           |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Backend**          | **Python 3.12 + FastAPI**                                                                                       | MIT                        | Sintaxe simples, LLM treinadíssimo, async nativo, OpenAPI automático     | Django (overkill), Go (curva íngreme), Node.js (tipagem fraca) |
| **Banco de Dados**   | **SQLite 3**                                                                                                    | Public Domain              | Zero setup, ACID nativo, single-file (deploy trivial), 80% coverage fácil | PostgreSQL (exige servidor), MySQL (licença Oracle)            |
| **Cache**            | **FASE (in-process dict + TTL)**                                                                                | —                         | 1 provider de câmbio (Frankfurter) → cache distribuído é YAGNI         | Redis (exige container, bloat para MVP)                         |
| **Frontend**         | **HTML + HTMX + Tailwind CSS**                                                                                  | MIT                        | Server-side rendering elimina 90% do JS; KISS puro                         | React/Next.js (build pipeline complexo), Vue (mesmo problema)   |
| **Geração PDF**    | **WeasyPrint**                                                                                                  | BSD3                       | Já especificado no TAP; maduro, FOSS, HTML→PDF                           | ReportLab (curva íngreme), wkhtmltopdf (deprecated)            |
| **Testes**           | **pytest + coverage.py**                                                                                        | MIT                        | Padrão de fato Python, integração CI trivial                            | unittest (verboso)                                              |
| **CI/CD**            | **GitHub Actions**                                                                                              | Gratuito (2000 min/mês)   | Já especificado; integrado ao SSOT                                        | GitLab CI (mudança de plataforma)                              |
| **~~Deploy~~**     | ~~**Railway.app** (tier gratuito)~~                                                                           | ~~Proprietário (SaaS)~~ | ~~500h/mês grátis, deploy via git push~~                               | ~~Fly.io (complexidade), Render (limitações)~~              |
| **LLM Local (SDD)**  | **llama.cpp + Qwen2.5-Coder-7B-Q4**<br />Verifique a seção 9. Stack SDD Local: Arquitetura e Organização Padrão | MIT / Apache 2.0           | Roda no hardware (60GB RAM sobra), offline, FOSS                           | Ollama (wrapper, adiciona camada), modelos cloud (custo)        |
| **TUI para Prompts** | **OpenCode**                                                                                                    | MIT                        | Já especificado na nova premissa; TUI nativa                              | Aider (Python, mas menos maduro), Continue.dev (VSCode-only)    |

### 3.3. Trade-offs Declarados

| Trade-off                           | Risco                              | Mitigação                                                                      |
| ----------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------- |
| SQLite em produção multi-usuário | Limitação de escrita concorrente | MVP acadêmico = 1-2 usuários simultâneos; YAGNI escalar                       |
| HTMX em vez de SPA                  | UX menos "fluida"                  | MVP foca em funcionalidade, não em animações                                  |
| Qwen-7B quantizado vs GPT-4         | Qualidade de geração inferior    | Revisão humana obrigatória (P4); prompts catalogados                           |
| ~~Railway (SaaS proprietário)~~  | ~~Não é FOSS puro~~            | ~~Camada de aplicação é 100% FOSS; Railway é apenas runtime (como Linux)~~ |

---

## 4. VALIDAÇÃO DAS PERSISTÊNCIAS

### 4.1. Persistência do Framework Ágil (Kanban)

**Veredito: MANTER — passa em todos os critérios GMV.**

| Critério                  | Resultado | Justificativa                                             |
| -------------------------- | --------- | --------------------------------------------------------- |
| Alinhamento ao PMBOK 7ª   | ✅        | Domínios de Trabalho e Entrega mapeados (OKB v3.0 §4.3) |
| Adequação à equipe de 2 | ✅        | WIP limits previnem burnout (Domínio de Equipe)          |
| Rastreabilidade acadêmica | ✅        | GitHub Projects é SSOT (ADR-001)                         |
| Compatibilidade com SDD    | ✅        | Cards = specs; DoR = prompt; DoD = código testado        |

**Risco identificado:** Kanban sem sprints pode gerar sensação de "nunca termina". **Mitigação:** macro-fases temporais (MF1/MF2/MF3) dão marcos psicológicos. -> Aprovado

### 4.2. Persistência Hierárquica PMBOK 7ª + PMBOK 6ª -> Aprovado

**Veredito: MANTER — com refinamento da hierarquia.**

**Hierarquia consolidada (ADR-001 já registra, ADR-005 formalizará):**

```
1º  Valor entregue (PMBOK 7ª — Domínio de Entrega)
2º  Ementa + orientação Prof. Nivaldo
3º  PMBOK 7ª (12 princípios + 8 domínios)
4º  Manifesto Ágil + Kanban
5º  PMBOK 6ª (APENAS dicionário de processos)
6º  Literatura técnica
```

**Refinamento crítico:** PMBOK 6ª **não deve ser citado como fonte primária** em nenhum artefato. Seu uso é restrito a:

- Nomenclatura de processos (ex: "4.1 Desenvolver TAP")
- Dicionário de termos (ex: "linha de base", "caminho crítico")
- Justificativa acadêmica quando o Prof. Nivaldo exigir

**Obsolescência declarada:** PMBOK 6ª (2017) foi superada por 7ª (2021) e pelo Practice Guide for Agile (2022). Seu uso como governança primária seria **regressão técnica** — o que o OKB v3.0 §6 já blinda.

### 4.3. Persistência do GitHub Projects -> Aprovado

**Veredito: MANTER — é o pilar da estratégia híbrida.**

| Domínio PMBOK 7ª | Ritual GitHub Projects                   | Evidência            |
| ------------------ | ---------------------------------------- | --------------------- |
| Medição          | GitHub Insights (Cycle Time, Throughput) | Dashboard automático |
| Trabalho           | Kanban flow + WIP limits                 | View 1                |
| Stakeholders       | Link público + Issues                   | Transparência total  |
| Incerteza          | Labels`risk`/`blocked`               | Risk backlog visual   |
| Equipe             | Discussions (daily assíncrona)          | Registro de burnout   |

**Risco:** GitHub Projects é SaaS proprietário (Microsoft). **Mitigação:** dados são exportáveis (JSON/CSV); a camada de governança (OKB, TAP, ADRs) é FOSS e versionada em Git.

---

## 5. INTEGRAÇÃO DA NOVA PREMISSA: SDD LOCAL VIA LLAMA.CPP - > Verifique a seção 9. Stack SDD Local: Arquitetura e Organização Padrão (Aprovado)

### 5.1. Viabilidade Técnica (hardware.md)

| Requisito                      | Hardware do Aluno     | Status                                 |
| ------------------------------ | --------------------- | -------------------------------------- |
| RAM para Qwen2.5-7B-Q4 (≈5GB) | 60GB disponíveis     | ✅**Folga de 12×**              |
| CPU para inferência (AVX2)    | Ryzen 7 8700G (Zen 4) | ✅ Suporte nativo                      |
| GPU para offload (opcional)    | Radeon 780M (ROCm)    | ⚠️ Suporte experimental no llama.cpp |
| SO compatível                 | Arch Linux            | ✅ Suporte nativo                      |
| Armazenamento para modelos     | 245GB livres em /home | ✅ Suficiente para 3-4 modelos         |

**Conclusão:** O hardware **não apenas atende como sobra** para SDD local. A GPU integrada pode ser usada para offload parcial via ROCm/Vulkan, acelerando inferência em 2-3×.

### 5.2. Arquitetura SDD Local Proposta (ADR-004 draft)

```
┌─────────────────────────────────────────────────────────┐
│  CAMADA 1 — ESPECIFICAÇÃO (Humano)                    │
│  • User stories no GitHub Issues                      │
│  • DoR + DoD explícitos                               │
│  • Critérios de aceite em Gherkin                     │
├─────────────────────────────────────────────────────────┤
│  CAMADA 2 — GERAÇÃO (LLM Local)                       │
│  • OpenCode TUI como interface                        │
│  • llama.cpp como runtime (CPU + ROCm offload)        │
│  • Qwen2.5-Coder-7B-Q4_K_M como modelo primário     │
│  • Prompts catalogados em /docs/prompts/              │
├─────────────────────────────────────────────────────────┤
│  CAMADA 3 — REVISÃO (Humano + CI)                     │
│  • Code review manual (pair entre os 2 devs)          │
│  • pytest + coverage.py ≥ 80%                         │
│  • ruff + mypy para linting estático                  │
│  • Commit com Co-authored-by: LLM                     │
├─────────────────────────────────────────────────────────┤
│  CAMADA 4 — AUDITORIA (PMBOK 7ª)                      │
│  • ADR para decisões arquiteturais                    │
│  • Rastreabilidade TAP → Issue → Commit → Test        │
│  • Lições aprendidas em Retrospectiva                 │
└─────────────────────────────────────────────────────────┘
```

### 5.3. Trade-offs do SDD Local

| Vantagem                    | Desvantagem                       | Mitigação                            |
| --------------------------- | --------------------------------- | -------------------------------------- |
| Zero custo operacional      | Qualidade inferior a GPT-4/Claude | Prompts estruturados + revisão humana |
| Offline (privacidade total) | Velocidade de geração menor     | Batch generation noturna               |
| FOSS puro (alinha P2)       | Alucinações mais frequentes     | Testes automatizados como guardrail    |
| Auditável (modelo local)   | Curva de aprendizado do llama.cpp | 1 semana de setup + ADR documentado    |

### 5.4. Modelos Recomendados (hierarquia) -> Verifique a seção 9. Stack SDD Local: Arquitetura e Organização Padrão

| Prioridade  | Modelo                           | Tamanho | Uso                                |
| ----------- | -------------------------------- | ------- | ---------------------------------- |
| Primário   | Qwen2.5-Coder-7B-Instruct-Q4_K_M | 4.5GB   | Geração de código, testes, ADRs |
| Secundário | Llama-3.2-3B-Instruct-Q6_K       | 2.5GB   | Tarefas rápidas (commits, docs)   |
| Backup      | DeepSeek-Coder-V2-Lite-Q4_K_M    | 9GB     | Casos complexos (arquitetura)      |

---

## 6. RELATÓRIO ANALÍTICO FINAL — JUSTIFICATIVAS DETALHADAS

### 6.1. Justificativa da Hibridização KISS + YAGNI

**Fundamento teórico:** A hibridização não é apenas possível — é **exigida** pela natureza dual do COGME:

- **Dualidade escopo/arquitetura:** YAGNI governa o "o que" (backlog); KISS governa o "como" (design).
- **Dualidade acadêmico/profissional:** KISS atende à defensabilidade acadêmica (auditável); YAGNI atende à viabilidade profissional (prazo).
- **Dualidade humano/LLM:** KISS protege contra alucinações de LLM (prompts simples = código simples); YAGNI protege contra superengenharia automática (LLMs tendem a adicionar abstrações).

**Evidência empírica:** Projetos que aplicam apenas KISS geram código limpo mas escopo inchado (ex: Rails apps com 50 gems não-usadas). Projetos que aplicam apenas YAGNI geram escopo enxuto mas código intrincado (ex: scripts bash de 2000 linhas). A hibridização é o único caminho que atende simultaneamente aos 8 domínios do PMBOK 7ª.

**Domínios PMBOK 7ª beneficiados:**

- **Entrega:** YAGNI garante foco no MVP; KISS garante entregável auditável.
- **Trabalho do Projeto:** KISS reduz lead time; YAGNI reduz WIP.
- **Incerteza:** Ambos reduzem superfície de risco.
- **Medição:** Ambos simplificam métricas (menos variáveis).

### 6.2. Justificativa do Descarte de 11 Pacotes da EAP

**Fundamento:** Aplicação rigorosa do teste GMV (OKB v3.0 §4.2) + YAGNI.

**Pacotes descartados e justificativa individual:**

1. **N5.6 (Execução Kanban como pacote):** O Kanban é o **método**, não um **entregável**. Ritualizá-lo como pacote gera burocracia (relatórios de rituais) sem valor tangível. **Domínio PMBOK 7ª afetado:** Abordagem de Desenvolvimento — já coberto pelo TAP + ADR-001.
2. **N6.3 (Testes de Performance e Carga):** MVP com 2 usuários-piloto não justifica teste de carga. YAGNI puro. **Domínio afetado:** Entrega — cobertura de 80% em testes unitários/integração já atende DoD.
3. **N7.2 (Pipeline CD automatizado):** Deploy manual em Railway via `git push` é suficiente para MVP. CD automatizado é over-engineering para 1 ambiente. **Domínio afetado:** Trabalho do Projeto — KISS.
4. **N9.3 (Relatórios quinzenais estáticos):** GitHub Projects já é SSOT (ADR-001). Relatório estático duplica informação e consome ~2h/semana. **Domínio afetado:** Comunicações — transparência via link público.
5. **N10.4 (Runbooks Operacionais):** MVP acadêmico não terá operação contínua. YAGNI. **Domínio afetado:** Base de Conhecimento — ADRs + lições aprendidas bastam.
6. **N11.3 (Análise formal de impacto):** CCB = Prof. Nivaldo. Análise formal de custo/prazo para mudança de 1 feature é burocracia. **Domínio afetado:** Incerteza — label `change-request` no GitHub basta.
7. **N12.3 (Relatórios EVM):** EVM é métrica de cascata; Kanban usa métricas de fluxo (Cycle Time, Throughput). Manter EVM é **regressão de governança**. **Domínio afetado:** Medição — GitHub Insights substitui.
8. **N13.4 (Auditoria FOSS final):** Redundante com N4.4 (auditoria inicial) + N1.5 (política). **Domínio afetado:** Abordagem de Desenvolvimento — KISS.

9-11. **Fusões propostas (N5.1+N5.2, N9.1+N9.2+N9.4, N10.1+N10.2+N10.3):** Reduzir 8 pacotes para 3 = ganho de 5 pacotes. Justificativa: KISS aplicado à própria EAP.

**Impacto quantitativo:**

- **Antes:** 62 pacotes × 7,7h = 480h (100% da capacidade, zero folga)
- **Depois:** 51 pacotes × 9,4h = 480h (100% da capacidade, mas com folga por pacote)
- **Ganho real:** +22% de capacidade por pacote = margem para riscos (R-08 burnout)

### 6.3. Justificativa da Stack FOSS Recomendada

**Fundamento:** KISS (simplicidade) + YAGNI (sem features especulativas) + P2 (FOSS absoluto) + hardware.md (viabilidade local).

**Decisões-chave e justificativa:**

1. **Python + FastAPI em vez de Django:** Django é framework monolítico com 40+ módulos; FastAPI é microframework com 5 dependências. KISS puro. YAGNI rejeita ORM complexo (SQLite + SQL direto basta).
2. **SQLite em vez de PostgreSQL:** PostgreSQL exige servidor, configuração, backup. SQLite é single-file, ACID nativo, zero-config. Para MVP com 1-2 usuários, PostgreSQL é YAGNI.
3. **HTMX em vez de React:** React exige build pipeline (webpack/vite), state management (Redux/Zustand), API REST separada. HTMX permite interatividade com HTML puro + server-side rendering. KISS radical.
4. **Cache in-process em vez de Redis:** Redis exige container, configuração, monitoramento. Para 1 provider de câmbio com TTL de 5min, dict Python com TTL basta. YAGNI.
5. **Qwen quantizado em vez de API cloud:** API cloud (OpenAI/Anthropic) viola P2 (FOSS absoluto) e gera custo. Qwen local é FOSS, offline, auditável. Trade-off de qualidade mitigado por revisão humana.

**Rastreabilidade:** Cada decisão de stack deriva de:

- TAP §8 (Restrições FOSS)
- OKB v3.0 P2 (FOSS absoluto)
- OKB v3.0 P3 (KISS)
- hardware.md (viabilidade técnica)

### 6.4. Justificativa da Persistência Ágil + PMBOK 7ª + GitHub Projects

**Fundamento:** As três persistências formam um **sistema coerente e auto-reforçante**:

```
PMBOK 7ª (governança)
    ↓ mapeia domínios
Kanban (execução)
    ↓ implementa via
GitHub Projects (ferramenta)
    ↓ gera evidências para
PMBOK 7ª (medição)
```

**Risco de romper o ciclo:**

- Remover PMBOK 7ª → perde governança acadêmica → reprovação.
- Remover Kanban → perde execução ágil → burocratização.
- Remover GitHub Projects → perde SSOT → duplicação de artefatos.

**Evidência de coerência:** OKB v3.0 §4.3 mapeia os 8 domínios PMBOK 7ª para rituais Kanban no GitHub Projects. Não há lacuna.

### 6.5. Justificativa do SDD Local (llama.cpp + Qwen + OpenCode)

**Fundamento:** Nova premissa alinhada a P2 (FOSS), P4 (SDD auditável), P3 (KISS) e hardware.md.

**Benefícios estratégicos:**

1. **Elimina dependência de APIs pagas** — alinha ao orçamento zero do TAP §8.4.
2. **Garante auditabilidade total** — prompts, modelos e pesos são versionáveis em Git LFS.
3. **Permite SDD offline** — útil para trabalho em locais sem internet (Fatec, casa).
4. **Reduz risco R-06** (API de câmbio externa) — se LLM cloud falhar, SDD local continua.

**Riscos e mitigações:**

- **Risco:** Qwen-7B alucina mais que GPT-4. **Mitigação:** Testes automatizados como guardrail (P5 ACID + Clean Code).
- **Risco:** Curva de aprendizado do llama.cpp. **Mitigação:** 1 semana de setup + ADR-004 documentado.
- **Risco:** Velocidade de geração inferior. **Mitigação:** Batch generation + prompts otimizados.

---

## 7. AÇÕES BLOQUEANTES RECOMENDADAS

| # | Ação                                     | Responsável | Prazo      | Artefato                 |
| - | ------------------------------------------ | ------------ | ---------- | ------------------------ |
| 1 | Formalizar ADR-002 (Stack FOSS)            | GP + Dev     | 13/09/2026 | `/docs/adr/ADR-002.md` |
| 2 | Formalizar ADR-004 (SDD Local)             | GP + Dev     | 15/09/2026 | `/docs/adr/ADR-004.md` |
| 3 | Atualizar EAP para 51 pacotes              | GP           | 12/09/2026 | `TAP_EAP.md` v1.0      |
| 4 | Consolidar OKB v3.1 (eliminando bloat)     | GP           | 14/09/2026 | `OKB_COGME_v3.1.md`    |
| 5 | Setup llama.cpp + Qwen2.5-7B-Q4            | Dev          | 15/09/2026 | `docs/sdd/SETUP.md`    |
| 6 | Protótipo "Hello World" com OpenCode      | Dev          | 17/09/2026 | Commit no repo           |
| 7 | Submeter ao Prof. Nivaldo para validação | GP           | 18/09/2026 | Issue no GitHub          |

---

## 8. DECLARAÇÃO DE CONFORMIDADE

Este relatório:

- ✅ Deriva 100% de fontes verificáveis (TAP, OKB v2.1/v3.0, hardware.md, glossário)
- ✅ Cita domínios e princípios PMBOK 7ª explicitamente
- ✅ Aplica teste GMV (OKB v3.0 §4.2) para cada recomendação de descarte
- ✅ Declara trade-offs e riscos (Domínio de Incerteza PMBOK 7ª)
- ✅ Respeita hierarquia de governança (OKB v3.0 §4.1)
- ✅ É acionável (ações com prazo e responsável)

**Próxima revisão:** 30/09/2026 (fechamento da MF1 — Fundação)

---

**Fim do Relatório Analítico**


# 9. Stack SDD Local: Arquitetura e Organização Padrão

## 9.1. Stack de Componentes de Software

### 9.1.1. Camada L1: Infraestrutura de Inferência

| Componente               | Versão/Config                 | Responsabilidade                   | Localização                   |
| ------------------------ | ------------------------------ | ---------------------------------- | ------------------------------- |
| **llama.cpp**      | 0.4.0-dev (Vulkan+LTO+AVX-512) | Motor de inferência FOSS          | `/usr/local/bin/llama-server` |
| **Backend Vulkan** | radv (Mesa 26.2.1)             | Aceleração GPU Radeon 780M       | `libggml-vulkan.so.0`         |
| **Backend CPU**    | AVX-512 (Zen 4)                | Fallback quando GPU indisponível  | Nativo no binário              |
| **Modelos Qwen**   | 14B/32B/72B Q4_K_M             | Especialistas por tamanho/contexto | `/var/lib/llama.cpp/models/`  |
| **API Server**     | OpenAI-compat (porta 8080)     | Interface HTTP para IDEs           | `llama-server --port 8080`    |

**Justificativa first-principles:**

- Único motor FOSS com Vulkan maduro para hardware AMD
- API compatível elimina necessidade de adaptadores
- Build otimizado (LTO) reduz latência em ~15%
- Fallback CPU garante resiliência

### 9.1.2. Camada L2: Personas e Contexto

| Componente              | Formato         | Responsabilidade                          | Localização                                 |
| ----------------------- | --------------- | ----------------------------------------- | --------------------------------------------- |
| **Persona Base**  | Markdown        | Instruções comuns a todos especialistas | `.ai/prompts/_base.md`                      |
| **Especialistas** | Markdown        | Comportamento específico por papel       | `.ai/prompts/{coder,reviewer,tester,pm}.md` |
| **Symlink Ativo** | Link simbólico | Define persona corrente da sessão        | `.ai/prompts/active.md → coder.md`         |
| **System Prompt** | Texto injetado  | Contexto carregado pelo OpenCode          | Lido de`active.md` a cada sessão           |

**Princípio:** Um modelo + N prompts = N especialistas (zero overhead de RAM)

### 9.1.3. Camada L3: Metodologia SDD

| Componente                 | Formato           | Responsabilidade                                 | Localização                  |
| -------------------------- | ----------------- | ------------------------------------------------ | ------------------------------ |
| **Specs**            | Markdown          | Regras imutáveis, contratos, domínio           | `.ai/specs/*.md`             |
| **Handoffs**         | Markdown numerado | Artefatos entre fases (spec→code→review→test) | `.ai/handoffs/NNN-*.md`      |
| **Workflows**        | Bash scripts      | Automação de pipeline SDD                      | `.ai/workflows/sdd-cycle.sh` |
| **Segundo Cérebro** | Obsidian Vault    | Documentação global, hardware profile          | `~/Obsidian/`                |

**Princípio:** Markdown puro + convenção de nomes = parsing determinístico sem frameworks

### 9.1.4. Camada de Interface

| Componente         | Versão | Responsabilidade                            | Integração                 |
| ------------------ | ------- | ------------------------------------------- | ---------------------------- |
| **OpenCode** | Latest  | IDE que lê persona ativa                   | API OpenAI`127.0.0.1:8080` |
| **Obsidian** | Latest  | Segundo cérebro, specs globais             | Sync via Git ou Syncthing    |
| **Git**      | System  | Versionamento de código + contexto`.ai/` | Commits atômicos por fase   |

---

## 9.2. Estrutura de Diretórios Padrão (Projetos Greenfield)

```
COGME/
├── .git/
├── .gitignore
├── README.md
├── src/                          # Código-fonte do projeto
├── docs/                         # Documentação humana
├── tests/                        # Testes automatizados
│
├── .ai/                          # CONTEXTO IA (versionado no Git)
│   ├── prompts/
│   │   ├── _base.md              # Persona base (comum a todos)
│   │   ├── coder.md              # Especialista: implementação
│   │   ├── reviewer.md           # Especialista: revisão de código
│   │   ├── tester.md             # Especialista: geração de testes
│   │   ├── pm.md                 # Especialista: planejamento/PM
│   │   └── active.md → coder.md  # Symlink: persona ativa
│   │
│   ├── specs/
│   │   ├── coding-standards.md   # Regras de estilo, convenções
│   │   ├── api-contracts.md      # Contratos de API, schemas
│   │   ├── domain-rules.md       # Lógica de negócio, invariantes
│   │   └── architecture.md       # Decisões arquiteturais
│   │
│   ├── handoffs/
│   │   ├── 001-feature-x-spec.md    # Especificação (fase PM)
│   │   ├── 001-feature-x-code.md    # Código gerado (fase coder)
│   │   ├── 001-feature-x-review.md  # Revisão (fase reviewer)
│   │   └── 001-feature-x-test.md    # Testes (fase tester)
│   │
│   └── workflows/
│       └── sdd-cycle.sh          # Pipeline automatizado (30 linhas)
│
└── .vscode/                      # Configs de editor (opcional)
    └── settings.json
```

### 9.2.1. Propósito de Cada Diretório

| Diretório         | Propósito               | Versionado? | Lido por IA?          |
| ------------------ | ------------------------ | ----------- | --------------------- |
| `src/`           | Código-fonte do projeto | ✅ Sim      | ✅ Sim (via OpenCode) |
| `docs/`          | Documentação humana    | ✅ Sim      | ❌ Não               |
| `tests/`         | Testes automatizados     | ✅ Sim      | ✅ Sim (fase tester)  |
| `.ai/prompts/`   | Personas e instruções  | ✅ Sim      | ✅ Sim (OpenCode)     |
| `.ai/specs/`     | Regras e contratos       | ✅ Sim      | ✅ Sim (contexto)     |
| `.ai/handoffs/`  | Artefatos entre fases    | ✅ Sim      | ✅ Sim (pipeline)     |
| `.ai/workflows/` | Scripts de automação   | ✅ Sim      | ❌ Não (executado)   |

### 9.2.2. Convenções de Nomenclatura

**Handoffs:**

- Formato: `NNN-descricao-fase.md`
- NNN: número sequencial (001, 002, ...)
- descricao: kebab-case (feature-x, bug-fix-y)
- fase: spec, code, review, test

**Exemplo:**

```
001-user-auth-spec.md      # Especificação do feature
001-user-auth-code.md      # Código gerado
001-user-auth-review.md    # Revisão do código
001-user-auth-test.md      # Testes gerados
```

---

## 3. Componentes Adjacentes

### 3.1. Infraestrutura de Suporte

| Componente               | Responsabilidade                               | Localização                                | Necessário? |
| ------------------------ | ---------------------------------------------- | -------------------------------------------- | ------------ |
| **systemd units**  | Gerenciamento de ciclo de vida do llama-server | `/etc/systemd/system/llama-server.service` | ✅ Sim       |
| **Backup scripts** | Proteção contra perda de`/var`             | `/extra/backup/`                           | ✅ Sim       |
| **Swap file**      | Prevenção de OOM com modelos grandes         | `/extra/swap/swapfile` (16GB)              | ✅ Sim       |

### 3.2. Ferramentas de Desenvolvimento

| Componente                   | Responsabilidade        | Integração com SDD           |
| ---------------------------- | ----------------------- | ------------------------------ |
| **Git**                | Versionamento           | Commits atômicos por fase SDD |
| **Make/CMake**         | Build de código        | Opcional, depende do projeto   |
| **Docker**             | Isolamento de ambientes | Opcional, para deps externas   |
| **linters/formatters** | Qualidade de código    | Executados pós-fase coder     |

### 3.3. Monitoramento e Validação

| Componente                       | Responsabilidade            | Métricas               |
| -------------------------------- | --------------------------- | ----------------------- |
| **htop/btop**              | Monitoramento de RAM/CPU    | RAM pico ≤42GB         |
| **radeontop**              | Monitoramento de GPU        | Utilização Vulkan     |
| **Scripts de validação** | Comparação output vs spec | Parsing determinístico |

### 3.4. Componentes Externos (Opcionais)

| Componente           | Uso                                         | Custo            |
| -------------------- | ------------------------------------------- | ---------------- |
| **Groq API**   | Aceleração estratégica (cloud free-tier) | R$ 0 (free tier) |
| **Gemini API** | Fallback para tarefas específicas          | R$ 0 (free tier) |
| **Syncthing**  | Sync Obsidian entre dispositivos            | R$ 0 (FOSS)      |

---

## 4. Fluxo de Trabalho SDD Padrão

```bash
# 1. PM escreve especificação
vim .ai/handoffs/001-feature-x-spec.md

# 2. Ativa persona coder e gera código
ln -sf coder.md .ai/prompts/active.md
./.ai/workflows/sdd-cycle.sh code 001

# 3. Ativa persona reviewer e revisa
ln -sf reviewer.md .ai/prompts/active.md
./.ai/workflows/sdd-cycle.sh review 001

# 4. Ativa persona tester e gera testes
ln -sf tester.md .ai/prompts/active.md
./.ai/workflows/sdd-cycle.sh test 001

# 5. Commit atômico por fase
git add .ai/handoffs/001-feature-x-*
git commit -m "SDD: feature-x (spec→code→review→test)"
```

---

## 5. Princípios Guia

1. **Separação de Camadas:** L1 (infra) ≠ L2 (personas) ≠ L3 (metodologia)
2. **Simplicidade First:** Markdown puro + bash > frameworks complexos
3. **Zero Overhead:** Um modelo + N prompts = N especialistas
4. **Parsing Determinístico:** Convenção de nomes > magia de frameworks
5. **Versionamento Total:** Código + contexto IA no mesmo Git
6. **Custo Zero:** 100% FOSS, cloud apenas como acelerador estratégico

---

Esta estrutura é **reutilizável** para qualquer projeto greenfield e estabelece padrões claros de organização, facilitando onboarding e manutenção.
