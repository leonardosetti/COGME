# GLOSSÁRIO DO PROJETO COGME v3.1

**Versão:** 3.1  
**Data:** 20/09/2026  
**Status:** Atualizado conforme OKB v3.1 e análise de auditoria v2.0  
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carleto  
**Referências:** `OKB_COGME_v3.1.md`, `analise_arquitetural.md` v2.0, `Canon_Stack_SDD.md` v1.0, `TAP v3` (18/09/2026)  
**Hierarquia de autoridade:** TAP > OKB > Glossário > ADRs

---

## 1. Siglas e Acrônimos do Projeto

| Termo | Significado | Contexto COGME |
| --- | --- | --- |
| COGME | Conversor de Ganhos em Moeda Estrangeira | Nome do projeto/produto |
| TAP | Termo de Abertura do Projeto | Documento de iniciação (Project Charter) — **NÃO integra EAP nem PDCA** (v3.1) |
| EAP/WBS | Estrutura Analítica do Projeto / Work Breakdown Structure | Decomposição hierárquica do escopo (13 fases + 48 pacotes Nível 2) |
| ADR | Architecture Decision Record | Registro de decisões arquiteturais (formato: Contexto → Decisão → Consequências) |
| CCB | Change Control Board | Comitê de controle de mudanças (GP Leonardo — membro único, TAP v3 §1.c) |
| DoD | Definition of Done | Critérios de conclusão de incremento |
| DoR | Definition of Ready | Critérios de prontidão para desenvolvimento |
| SDD | Spec-Driven Development | Desenvolvimento guiado por especificação com IA local (llama.cpp + Qwen 32B) |
| FOSS | Free and Open Source Software | Licenciamento obrigatório do projeto (MIT, Apache 2.0, BSD, GPL) |
| CI/CD | Continuous Integration / Continuous Deployment | Pipeline automatizado de build e deploy (GitHub Actions) |
| UAT | User Acceptance Testing | Testes de aceitação do usuário |
| GMV | Governança Mínima Viável | Princípio operacional: cada artefato deve justificar sua existência (OKB v3.1 §3.2) |
| SSOT | Single Source of Truth | Fonte única de verdade (GitHub Projects para monitoramento) |
| MF | Macro-Fase | Agrupamento temporal de fases da EAP (MF1: Fundação, MF2: Construção, MF3: Consolidação) |
| WIP | Work In Progress | Limite de trabalho em progresso no Kanban (3 cards/pessoa) |
| LGPD | Lei Geral de Proteção de Dados | Conformidade tratada como pós-entrega |
| OWASP | Open Web Application Security Project | Análise de riscos de segurança (pós-entrega) |
| WCAG | Web Content Accessibility Guidelines | Acessibilidade tratada como pós-entrega |
| i18n | Internationalization | Internacionalização tratada como pós-entrega |
| PDCA | Plan-Do-Check-Act | Ciclo de melhoria contínua (aplicado a planos e código, **NÃO ao TAP**) |
| GP | Gerente de Projeto | Leonardo David Silva Setti |
| PMO | Project Management Office | Escritório de Projetos (referência acadêmica) |

---

## 2. Gerência de Projetos — PMBOK 7ª Edição (Governança Primária)

| Termo | Definição | Aplicação no COGME |
| --- | --- | --- |
| Princípios | 12 fundamentos do PMBOK 7ª | Governança primária (ex: P1 - Valor sobre documentação) |
| Domínios de Desempenho | 8 áreas de foco do PMBOK 7ª | Stakeholders, Equipe, Abordagem, Planejamento, Trabalho, Entrega, Medição, Incerteza |
| Domínio de Entrega | Foco em gerar valor tangível | Meta: MVP funcional com ≥ 80% cobertura de testes |
| Domínio de Medição | Métricas de desempenho | Cycle time, throughput, CFD (substitui EVM) |
| Domínio de Incerteza | Gestão de riscos e ambiguidade | Risk backlog + matriz prob./impacto |
| Domínio de Integração | Coordenação de todos os domínios | TAP como documento de autorização (não gerenciado) |
| Stakeholder | Pessoa/grupo afetado pelo projeto | Prof. Dr. Nivaldo Carleto (único formal) |
| Valor Entregue | Benefício tangível gerado | Princípio orientador: Valor > Satisfação > Conformidade |
| Princípio P6 | Especialização via prompt, não via modelo | 1 modelo (Qwen 32B) + N prompts = N especialistas SDD |
| Princípio P9 | Separação ontológica TAP ≠ EAP ≠ PDCA | TAP autoriza o projeto, não é gerenciado por ele |

---

## 3. Gerência de Projetos — PMBOK 6ª Edição (Dicionário Complementar)

| Termo | Definição | Aplicação no COGME |
| --- | --- | --- |
| 49 Processos | Processos de gestão do PMBOK 6ª | Dicionário complementar quando necessário |
| 10 Áreas de Conhecimento | Integração, Escopo, Cronograma, Custos, Qualidade, Recursos, Comunicações, Riscos, Aquisições, Partes Interessadas | 8 áreas ativas (exclui Aquisições e Partes Interessadas) |
| Processo 4.1 | Desenvolver Termo de Abertura | Geração do TAP (documento de autorização, não pacote de trabalho) |
| Processo 5.2 | Coletar Requisitos | Product Backlog Refinement |
| Processo 5.4 | Criar EAP/WBS | Decomposição em épico → feature → user story (48 pacotes) |
| Processo 6.2 | Definir Atividades | **Decomposição de pacotes EAP em atividades** (PMBOK 6ª §6.2) |
| Processo 6.4 | Estimar Custos | Planning Poker / T-shirt sizing |
| Processo 6.5 | Desenvolver Cronograma | Roadmap + Kanban (sem sprints fixas) |
| Processo 8.3 | Controlar Qualidade | DoD + Code Review + TDD |
| Processo 11.2 | Identificar Riscos | Retrospectiva + Risk Backlog |
| Linha de Base | Baseline aprovada de escopo/prazo/custo | Referência para controle de mudanças |
| Caminho Crítico | Sequência de atividades sem folga | Identificado na rede de atividades |
| Atividades Derivadas | Ações (verbos) necessárias para gerar entregas (substantivos) da EAP | Ex: N4.1 (entrega) → A4.1.1, A4.1.2, A4.1.3, A4.1.4 (ações) |

---

## 4. Metodologias Ágeis e Kanban

| Termo | Definição | Aplicação no COGME |
| --- | --- | --- |
| Kanban | Método de gestão visual de fluxo | GitHub Projects como ferramenta primária |
| Pull System | Sistema puxado (trabalho iniciado quando há capacidade) | WIP limits no Kanban (3 cards/pessoa) |
| Cycle Time | Tempo médio de um card do "To Do" ao "Done" | Meta: ≤ 3 dias (após calibração 23/09 – 03/10) |
| Throughput | Número de cards concluídos por semana | Meta: ≥ 5 cards/semana (após calibração) |
| Cumulative Flow Diagram (CFD) | Visualização de gargalos no fluxo | Métrica de saúde do Kanban |
| Backlog | Lista priorizada de trabalho pendente | Product Backlog refinado semanalmente |
| User Story | Requisito formatado como história de usuário | Formato: "Como [papel], quero [ação] para [benefício]" |
| Épico | Grande corpo de trabalho divisível em features | Nível 1 da EAP |
| Feature | Capacidade do sistema divisível em user stories | Nível 2 da EAP |
| Fluxo Contínuo | Execução sem iterações time-boxed fixas | Kanban sem sprints (substitui Scrum) |
| Retrospective | Reunião de melhoria contínua | Risk backlog + lições aprendidas |
| Refinement | Refinamento do backlog | Semanal, com DoR claro |
| Pair Review | Revisão em pares | Check manual no PDCA |
| Manifesto Ágil | 4 valores e 12 princípios ágeis | Hierarquia 4 na resolução de conflitos |
| Macro-Fase (MF) | Agrupamento temporal de fases da EAP | MF1 (Fundação), MF2 (Construção), MF3 (Consolidação) |
| Sprint | Iteração time-boxed (Scrum) | **NÃO UTILIZADO** — fluxo contínuo Kanban |
| Card Ubíquo | Card autossuficiente que declara o quê, por quê, como será aceito e a quem pertence | Padrão A (documental) + Padrão B (User Story GWT) |
| Tasklist Markdown | Checklist nativo do GitHub (`- [ ]`) no corpo da Issue | ADR-004 — controle de progresso interno de cards complexos |
| Subissue | Issue filha vinculada a uma Issue pai | **REJEITADO** formalmente pela ADR-004 |

---

## 5. Stack SDD Local Canônica (NOVO v3.1)

| Termo | Definição | Aplicação no COGME |
| --- | --- | --- |
| SDD Local | Spec-Driven Development executado localmente com LLM | llama.cpp + Qwen 32B + OpenCode (zero custo, P2) |
| llama.cpp | Motor de inferência FOSS para LLMs | Versão 0.4.0-dev com Vulkan + LTO + AVX-512 |
| Vulkan | API gráfica de baixo nível | Backend GPU para inferência (radv Mesa 26.2.1) |
| radv | Driver Vulkan open-source da Mesa | Driver oficial para AMD RDNA 3 (Radeon 780M) |
| Mesa | Coleção de drivers gráficos open-source | Versão 26.2.1 (suporte Vulkan 1.4.357) |
| AVX-512 | Conjunto de instruções CPU (512-bit) | Fallback para inferência CPU (Zen 4) |
| Zen 4 | Arquitetura CPU AMD | Ryzen 7 8700G (8C/16T, AVX-512 nativo) |
| RDNA 3 | Arquitetura GPU AMD | Radeon 780M (12 CUs, VRAM compartilhada) |
| Q4_K_M | Quantização 4-bit com precisão média | Formato dos modelos Qwen (balance RAM/quality) |
| Q5_K_M | Quantização 5-bit com precisão média | Variante de maior qualidade (P2) |
| gguf | Formato de modelo quantizado | Formato padrão do llama.cpp |
| tg | Tokens per second | Métrica de throughput de inferência (meta: ≥6 t/s para 32B) |
| TTFT | Time To First Token | Latência até primeiro token (meta: <2s) |
| KV Cache | Memória de contexto do modelo | 16k tokens (32B), 32k+ tokens (14B) |
| systemd | Gerenciador de serviços Linux | Ciclo de vida do llama-server |
| symlink | Link simbólico | Troca de persona SDD (active.md → coder.md) |
| Persona SDD | Papel especializado no ciclo SDD | PM, Coder, Reviewer, Tester (núcleo de 4) |
| active.md | Symlink para persona ativa | Define qual persona o OpenCode usa |
| _base.md | Persona base compartilhada | Instruções comuns a todas as personas |
| .ai/ | Diretório de contexto da IA | Versionado no Git, lido pelo OpenCode |
| docs/ | Diretório de documentação humana | Planos, roadmaps, atas (não lido pela IA) |
| handoff | Artefato entre fases SDD | .ai/handoffs/NNN-*-fase.md |
| spec | Especificação imutável | .ai/specs/*.md (regras, contratos) |
| workflow | Automação bash do ciclo SDD | .ai/workflows/sdd-cycle.sh (~30 linhas) |
| OpenCode | IDE que lê persona ativa via API | Interface principal de desenvolvimento SDD |
| Obsidian | Ferramenta de gestão de conhecimento | Vault por projeto (interface, não repositório) |
| vault | Espaço de trabalho do Obsidian | Dedicado por projeto, com symlinks para .ai/ |
| Qwen 32B Instruct | Modelo LLM 32B parâmetros | Pilar SDD (P0, ~20GB RAM, ≥6 t/s) |
| Qwen 14B Instruct | Modelo LLM 14B parâmetros | Acelerador (P1, ~9GB RAM, ≥12 t/s) |
| Qwen 72B Instruct | Modelo LLM 72B parâmetros | **ADIADO** (42GB RAM, insuficiente) |
| DeepSeek-Coder-V2 Lite | Modelo especializado em código | Condicional (P4, apenas se P0 falhar) |

---

## 6. Desenvolvimento de Software e Qualidade

| Termo | Definição | Aplicação no COGME |
| --- | --- | --- |
| MVP | Minimum Viable Product | Escopo mínimo entregável (Nov/2026) |
| Full-Stack | Desenvolvimento front-end + back-end + banco | Arquitetura do COGME (Python + FastAPI + SQLite + HTMX) |
| ACID | Atomicity, Consistency, Isolation, Durability | Padrão inegociável de transações |
| Clean Code | Código legível, manutenível, testável | Princípio P5 do COGME |
| TDD | Test-Driven Development | Escrever testes antes do código |
| Code Review | Revisão de código por pares | Parte do DoD |
| Coverage | Cobertura de testes automatizados | Meta: ≥ 80% (pytest + coverage.py) |
| Adapter Pattern | Padrão de projeto para abstrair dependências | Múltiplos provedores de câmbio |
| Cache | Armazenamento temporário para performance | Redis para API de câmbio |
| PDF Generation | Geração de documentos em PDF | WeasyPrint para invoices |
| Health Check | Endpoint de verificação de saúde | `/health`, `/warmup` (pós-entrega) |
| Logging Estruturado | Logs em formato JSON | Observabilidade (pós-entrega) |
| JWT | JSON Web Token | Autenticação (pós-entrega) |
| OpenAPI | Especificação de API | Documentação automática (FastAPI) |
| REST | Representational State Transfer | Arquitetura da API |
| SQLite | Banco de dados relacional leve | Banco principal (FOSS, zero-config) |
| FastAPI | Framework web Python | Backend (async, type-safe) |
| HTMX | Biblioteca para interatividade sem JS | Frontend (simplicidade, P3) |
| Tailwind CSS | Framework CSS utility-first | Estilização (rapidez, P3) |
| WeasyPrint | Motor de renderização HTML para PDF | Geração de invoices |

---

## 7. Ferramentas e Tecnologias (Brands)

| Ferramenta | Categoria | Uso no COGME |
| --- | --- | --- |
| GitHub Projects | Gestão de projetos | Kanban operacional (fonte de verdade) |
| GitHub Issues/Discussions | Colaboração | Daily assíncrona |
| GitHub Insights | Métricas | Cycle time, throughput |
| GitHub Actions | CI/CD | Pipeline automatizado |
| Redis | Banco de dados | Cache de API de câmbio |
| WeasyPrint | Geração de PDF | Módulo de invoices |
| draw.io | Diagramas | Roadmap, DER, UML |
| Mermaid | Diagramas como código | Rede de atividades |
| ProjectLibre | Gantt | Apenas se exigido academicamente (derivado do Kanban) |
| OWASP ZAP | Segurança | Pentest básico (pós-entrega) |
| Axe DevTools | Acessibilidade | Auditoria WCAG (pós-entrega) |
| Lighthouse | Performance/Acessibilidade | Auditoria automatizada |
| NVDA/VoiceOver | Leitores de tela | Testes de acessibilidade |
| Prometheus/Grafana/Loki | Observabilidade | Stack de monitoramento (pós-entrega) |
| i18next | Internacionalização | Biblioteca de i18n (pós-entrega) |
| OpenCode | IDE SDD | Interface principal de desenvolvimento |
| Obsidian | Gestão de conhecimento | Vault por projeto (interface) |
| llama.cpp | Motor de inferência | SDD local (Vulkan + AVX-512) |
| pytest | Framework de testes | Testes automatizados Python |
| coverage.py | Medição de cobertura | Meta ≥80% |
| htop | Monitoramento de recursos | Validação de RAM pico (≤30GB) |
| huggingface-cli | Download de modelos | Download de modelos GGUF |

---

## 8. Termos Acadêmicos e Institucionais

| Termo | Definição | Contexto |
| --- | --- | --- |
| Fatec Taquaritinga | Instituição de ensino | Faculdade de Tecnologia |
| ADS | Análise e Desenvolvimento de Sistemas | Curso técnico |
| Prof. Dr. Nivaldo Carleto | Stakeholder-avaliador | Patrocinador + avaliador contínuo |
| Disciplina de Gerência de Projetos | Contexto acadêmico | PMBOK 6ª como bibliografia base |
| Simplificação Pedagógica | Restrição didática | Exclusão de Aquisições e Partes Interessadas |
| Obsolescência Assumida | Declaração de maturidade | PMBOK 6ª (2017) vs. 7ª (2021) |
| Banca Acadêmica | Avaliadores | Apenas Prof. Dr. Nivaldo Carleto no COGME |
| Entrega Parcial | Marco intermediário | Consolidação documental (22/09/2026) |
| Entrega Final | Marco de conclusão | MVP + documentação (Nov/Dez 2026) |
| Rastreabilidade de Prompts | Auditoria de LLM | Prompts catalogados em `.ai/handoffs/` |
| Compliance Acadêmico | Dimensão de qualidade | Rastreabilidade ao TAP + conformidade PMBOK 7ª |
| GMV (Governança Mínima Viável) | Princípio de eficiência | Cada artefato deve passar pelo teste GMV (OKB v3.1 §3.2) |

---

## 9. Métricas e Indicadores

| Métrica | Fórmula/Definição | Meta COGME |
| --- | --- | --- |
| Cycle Time | Tempo médio To Do → Done | ≤ 3 dias (após calibração) |
| Throughput | Cards concluídos/semana | ≥ 5 cards (após calibração) |
| CFD | Cumulative Flow Diagram | Sem bandas largas |
| Coverage | Linhas testadas / linhas totais | ≥ 80% |
| WIP Limit | Cards em "In Progress" por pessoa | 3 cards |
| Burnout | Carga horária semanal | ≤ 20h/pessoa |
| Scope Creep | Desvio do backlog original | < 15% |
| tg (tokens/s) | Tokens gerados por segundo | ≥ 6 t/s (32B), ≥ 12 t/s (14B) |
| TTFT | Time To First Token | < 2s (32B) |
| RAM Pico | Memória máxima durante inferência | ≤ 30GB (32B) |
| Parsing Determinístico | Taxa de sucesso de handoffs | 100% |
| Custo Financeiro | Custo total da stack | R$ 0,00 (100% FOSS) |

---

## 10. Princípios Constitutivos do COGME (Atualizado v3.1)

| Código | Princípio | Fundamentação |
| --- | --- | --- |
| P1 | Valor sobre documentação | PMBOK 7ª — Princípio 1 |
| P2 | FOSS absoluto | Restrição pedagógica + valor social (TAP §2.4) |
| P3 | KISS como métrica de arquitetura | Simplicidade justificada |
| P4 | SDD com IA auditável | Rastreabilidade via commit + handoffs |
| P5 | ACID e Clean Code | Padrão inegociável |
| P6 | Especialização via prompt, não via modelo | 1 modelo (Qwen 32B) + N prompts = N especialistas (NOVO v3.1) |
| P7 | Entrega incremental via fluxo contínuo | Kanban sem sprints fixas |
| P8 | Stakeholder único formal | Prof. Dr. Nivaldo Carleto como patrocinador-avaliador |
| P9 | Separação ontológica TAP ≠ EAP ≠ PDCA | TAP autoriza, não é gerenciado (NOVO v3.1) |

---

## 11. Separação Ontológica (NOVO v3.1)

| Artefato | Natureza | Integra EAP? | Tem PDCA? |
| --- | --- | --- | --- |
| TAP | Autorização + base de referência | ❌ NÃO | ❌ NÃO |
| Planos de Gerenciamento (01-10) | Execução do escopo autorizado | ✅ SIM | ✅ SIM |
| Código-fonte (11) | Produto final | ✅ SIM | ✅ SIM |

**Fundamento:** O TAP é o documento que AUTORIZA o projeto e concede autoridade ao gerente. Ele antecede o planejamento e não é objeto de gerenciamento — é a base sobre a qual o gerenciamento se constrói. (PMBOK 6ª §4.1 / PMBOK 7ª Domínio de Integração)

---

## 12. Hierarquia de Resolução de Conflitos (OKB v3.1 §3.1)

1. Valor entregue ao usuário final (PMBOK 7ª — Domínio de Entrega)
2. Ementa da disciplina + orientação do Prof. Dr. Nivaldo Carleto
3. PMBOK 7ª (12 princípios + 8 domínios de desempenho)
4. Manifesto Ágil + Kanban (método de execução)
5. PMBOK 6ª (apenas como dicionário de processos quando necessário)
6. Literatura técnica complementar

**Adendo v3.1:** Em caso de conflito entre velocidade de entrega e completude documental, a entrega de valor prevalece, desde que justificada via ADR e comunicada ao Prof. Dr. Nivaldo Carleto em até 48h.

---

## 13. Teste GMV (Governança Mínima Viável) (OKB v3.1 §3.2)

Todo artefato de governança deve passar pelo teste GMV antes de ser produzido:

| Pergunta | Se SIM | Se NÃO |
| --- | --- | --- |
| O Prof. Dr. Nivaldo Carleto exigirá este artefato na avaliação? | Produzir completo | Simplificar ou eliminar |
| Este artefato evita retrabalho futuro? | Produzir | Avaliar custo-benefício |
| Este artefato é exigido pelo PMBOK 7ª como evidência de domínio? | Produzir | Documentar em 1 parágrafo no TAP |
| Este artefato é útil para a equipe (não apenas para o professor)? | Produzir | Eliminar |

**Regra:** Se ≥ 2 respostas forem NÃO, o artefato é candidato a eliminação. Decisão final via CCB (GP Leonardo).

---

## 14. Estrutura Documental (OKB v3.1 §7)

~~~
PROJETO COGME
 ├── 00. TAP (Termo de Abertura)                          [GMV: OBRIGATÓRIO — NÃO integra EAP/PDCA]
 ├── 01. Plano de Integração                               [GMV: OBRIGATÓRIO]
 ├── 02. Plano de Escopo + EAP/WBS + Dicionário + Atividades Derivadas [GMV: OBRIGATÓRIO]
 ├── 03. Plano de Cronograma + Roadmap + Kanban Setup      [GMV: OBRIGATÓRIO]
 ├── 04. Plano de Custos + Orçamento                       [GMV: SIMPLIFICAR*]
 ├── 05. Plano de Qualidade + Métricas + DoD/DoR + Ishikawa + 12 PDCAs [GMV: OBRIGATÓRIO]
 ├── 06. Plano de Recursos + RACI                          [GMV: SIMPLIFICAR*]
 ├── 07. Plano de Comunicações + Matriz                    [GMV: OBRIGATÓRIO]
 ├── 08. Plano de Riscos + Matriz + Respostas              [GMV: OBRIGATÓRIO]
 ├── 09. Base de Conhecimento                              [GMV: OBRIGATÓRIO]
 │   ├── 09.1. ADRs (apenas decisões críticas)
 │   ├── 09.2. Lições Aprendidas
 │   ├── 09.3. Prompts SDD (em .ai/handoffs/)
 │   └── 09.4. Runbooks [DESCARTADO — YAGNI]
 ├── 10. Plano de Gestão de Mudanças (CCB)                 [GMV: SIMPLIFICAR*]
 └── 11. Código-Fonte (MVP) + DER + Diagramas + .ai/       [GMV: OBRIGATÓRIO]
~~~

*SIMPLIFICAR = 1-2 páginas no máximo, foco em premissas e restrições, sem planilhas complexas ou simulações de EVM.

---

## 15. Notas de Uso

Este glossário deve ser consultado durante redação e revisão de artefatos para garantir consistência terminológica. Em caso de conflito entre definições, aplicar a hierarquia de governança (OKB v3.1 §3.1).

**Mudanças críticas em relação ao v2.2:**
- ✅ Adicionada Seção 5: Stack SDD Local Canônica (30+ termos técnicos)
- ✅ Adicionada Seção 11: Separação Ontológica (TAP ≠ EAP ≠ PDCA)
- ✅ Adicionados princípios P6 (especialização via prompt) e P9 (separação ontológica)
- ✅ Atualizado "QwenStudio" para "OpenCode + llama.cpp + Qwen 32B"
- ✅ Atualizado "/docs/prompts/" para ".ai/handoffs/"
- ✅ Adicionado "Prof. Dr." ao nome do stakeholder (consistência)
- ✅ Eliminado termo "ADER" (substituído por "ADR")
- ✅ Adicionados termos técnicos SDD (Vulkan, radv, Mesa, AVX-512, Zen 4, RDNA 3, Q4_K_M, gguf, tg, TTFT, KV cache, systemd, symlink, persona, handoff, spec, workflow, vault)
- ✅ Adicionados termos de governança (GMV, SSOT, Macro-Fase, Atividades Derivadas)
- ✅ Atualizadas métricas para incluir tg, TTFT, RAM Pico, Parsing Determinístico
- ✅ Adicionado Teste GMV (Seção 13)
- ✅ Atualizada estrutura documental (Seção 14)
- ✅ EAP atualizada: 13 fases + 48 pacotes (não 12 + 37)
- ✅ PDCAs consolidados: 12 (não 13, TAP removido)
- ✅ Hardware real: 58GB RAM (não 60GB nominais)

---

**Versão:** 3.1  
**Data:** 20/09/2026  
**Autor:** GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico)  
**Status:** Pronto para aplicação imediata  
**Próxima revisão:** 30/09/2026 (fechamento da MF1 — Fundação)