# GLOSSÁRIO DO PROJETO COGME v2.1

## 1. Siglas e Acrônimos do Projeto

| Termo | Significado | Contexto COGME |
|-------|-------------|----------------|
| **COGME** | Conversor de Ganhos em Moeda Estrangeira | Nome do projeto/produto |
| **TAP** | Termo de Abertura do Projeto | Documento de iniciação (Project Charter) |
| **EAP/WBS** | Estrutura Analítica do Projeto / Work Breakdown Structure | Decomposição hierárquica do escopo |
| **ADR** | Architecture Decision Record | Registro de decisões arquiteturais |
| **CCB** | Change Control Board | Comitê de controle de mudanças (Prof. Nivaldo) |
| **DoD** | Definition of Done | Critérios de conclusão de incremento |
| **DoR** | Definition of Ready | Critérios de prontidão para desenvolvimento |
| **SDD** | Spec-Driven Development | Desenvolvimento guiado por especificação com IA |
| **FOSS** | Free and Open Source Software | Licenciamento obrigatório do projeto |
| **CI/CD** | Continuous Integration / Continuous Deployment | Pipeline automatizado de build e deploy |
| **UAT** | User Acceptance Testing | Testes de aceitação do usuário |
| **EVM** | Earned Value Management | Gestão de valor agregado (substituído por métricas de fluxo) |
| **SPI** | Schedule Performance Index | Índice de desempenho do cronograma (meta: ≥ 0.9) |
| **CPI** | Cost Performance Index | Índice de desempenho de custos (meta: ≥ 0.9) |
| **WIP** | Work In Progress | Limite de trabalho em progresso no Kanban |
| **LGPD** | Lei Geral de Proteção de Dados | Conformidade tratada como pós-entrega |
| **OWASP** | Open Web Application Security Project | Análise de riscos de segurança (pós-entrega) |
| **WCAG** | Web Content Accessibility Guidelines | Acessibilidade tratada como pós-entrega |
| **i18n** | Internationalization | Internacionalização tratada como pós-entrega |

## 2. Gerência de Projetos — PMBOK 7ª Edição

| Termo | Definição | Aplicação no COGME |
|-------|-----------|-------------------|
| **Princípios** | 12 fundamentos do PMBOK 7ª | Governança primária (ex: P1 - Valor sobre documentação) |
| **Domínios de Desempenho** | 8 áreas de foco do PMBOK 7ª | Stakeholders, Equipe, Abordagem, Planejamento, Trabalho, Entrega, Medição, Incerteza |
| **Domínio de Entrega** | Foco em gerar valor tangível | Meta: MVP funcional com ≥ 80% cobertura de testes |
| **Domínio de Medição** | Métricas de desempenho | Cycle time, throughput, SPI, CPI |
| **Domínio de Incerteza** | Gestão de riscos e ambiguidade | Risk backlog + matriz prob./impacto |
| **Stakeholder** | Pessoa/grupo afetado pelo projeto | Prof. Dr. Nivaldo Carletto (único formal) |
| **Valor Entregue** | Benefício tangível gerado | Princípio orientador: Valor > Satisfação > Conformidade |

## 3. Gerência de Projetos — PMBOK 6ª Edição

| Termo | Definição | Aplicação no COGME |
|-------|-----------|-------------------|
| **49 Processos** | Processos de gestão do PMBOK 6ª | Dicionário complementar quando necessário |
| **10 Áreas de Conhecimento** | Integração, Escopo, Cronograma, Custos, Qualidade, Recursos, Comunicações, Riscos, Aquisições, Partes Interessadas | 8 áreas ativas (exclui Aquisições e Partes Interessadas) |
| **Processo 4.1** | Desenvolver Termo de Abertura | Geração do TAP |
| **Processo 5.2** | Coletar Requisitos | Product Backlog Refinement |
| **Processo 5.4** | Criar EAP/WBS | Decomposição em épico → feature → user story |
| **Processo 6.4** | Estimar Custos | Planning Poker / T-shirt sizing |
| **Processo 6.5** | Desenvolver Cronograma | Sprint Planning + Roadmap |
| **Processo 8.3** | Controlar Qualidade | DoD + Code Review + TDD |
| **Processo 11.2** | Identificar Riscos | Sprint Retrospective + Risk Backlog |
| **Linha de Base** | Baseline aprovada de escopo/prazo/custo | Referência para controle de mudanças |
| **Caminho Crítico** | Sequência de atividades sem folga | Identificado na rede de atividades |

## 4. Metodologias Ágeis e Kanban

| Termo | Definição | Aplicação no COGME |
|-------|-----------|-------------------|
| **Kanban** | Método de gestão visual de fluxo | GitHub Projects como ferramenta primária |
| **Pull System** | Sistema puxado (trabalho iniciado quando há capacidade) | WIP limits no Kanban |
| **Cycle Time** | Tempo médio de um card do "To Do" ao "Done" | Meta: ≤ 3 dias |
| **Throughput** | Número de cards concluídos por semana | Meta: ≥ 5 cards/semana |
| **Cumulative Flow Diagram** | Visualização de gargalos no fluxo | Métrica de saúde do Kanban |
| **Backlog** | Lista priorizada de trabalho pendente | Product Backlog refinado semanalmente |
| **User Story** | Requisito formatado como história de usuário | Formato: "Como [papel], quero [ação] para [benefício]" |
| **Épico** | Grande corpo de trabalho divisível em features | Nível 1 da EAP |
| **Feature** | Capacidade do sistema divisível em user stories | Nível 2 da EAP |
| **Sprint** | Iteração time-boxed (não usado no COGME) | Substituído por fluxo contínuo Kanban |
| **Retrospective** | Reunião de melhoria contínua | Risk backlog + lições aprendidas |
| **Refinement** | Refinamento do backlog | Semanal, com DoR claro |
| **Pair Review** | Revisão em pares | Check manual no PDCA |
| **Manifesto Ágil** | 4 valores e 12 princípios ágeis | Hierarquia 4 na resolução de conflitos |

## 5. Desenvolvimento de Software e Qualidade

| Termo | Definição | Aplicação no COGME |
|-------|-----------|-------------------|
| **MVP** | Minimum Viable Product | Escopo mínimo entregável (Nov/2026) |
| **Full-Stack** | Desenvolvimento front-end + back-end + banco | Arquitetura do COGME |
| **ACID** | Atomicity, Consistency, Isolation, Durability | Padrão inegociável de transações |
| **Clean Code** | Código legível, manutenível, testável | Princípio P5 do COGME |
| **TDD** | Test-Driven Development | Escrever testes antes do código |
| **Code Review** | Revisão de código por pares | Parte do DoD |
| **Coverage** | Cobertura de testes automatizados | Meta: ≥ 80% |
| **Adapter Pattern** | Padrão de projeto para abstrair dependências | Múltiplos provedores de câmbio |
| **Cache** | Armazenamento temporário para performance | Redis para API de câmbio |
| **PDF Generation** | Geração de documentos em PDF | WeasyPrint para invoices |
| **Health Check** | Endpoint de verificação de saúde | `/health`, `/warmup` (pós-entrega) |
| **Logging Estruturado** | Logs em formato JSON | Observabilidade (pós-entrega) |
| **JWT** | JSON Web Token | Autenticação (pós-entrega) |

## 6. Ferramentas e Tecnologias (Brands)

| Ferramenta | Categoria | Uso no COGME |
|-----------|-----------|--------------|
| **GitHub Projects** | Gestão de projetos | Kanban operacional (fonte de verdade) |
| **GitHub Issues/Discussions** | Colaboração | Daily assíncrona |
| **GitHub Insights** | Métricas | Cycle time, throughput |
| **GitHub Actions** | CI/CD | Pipeline automatizado |
| **Redis** | Banco de dados | Cache de API de câmbio |
| **WeasyPrint** | Geração de PDF | Módulo de invoices |
| **draw.io** | Diagramas | Roadmap, DER, UML |
| **Mermaid** | Diagramas como código | Rede de atividades |
| **ProjectLibre** | Gantt | Apenas se exigido academicamente |
| **Notion** | Documentação | Roadmap estratégico (alternativa) |
| **OWASP ZAP** | Segurança | Pentest básico (pós-entrega) |
| **Axe DevTools** | Acessibilidade | Auditoria WCAG (pós-entrega) |
| **Lighthouse** | Performance/Acessibilidade | Auditoria automatizada |
| **NVDA/VoiceOver** | Leitores de tela | Testes de acessibilidade |
| **Prometheus/Grafana/Loki** | Observabilidade | Stack de monitoramento (pós-entrega) |
| **i18next** | Internacionalização | Biblioteca de i18n (pós-entrega) |
| **QwenStudio** | LLM | Ferramenta autorizada de apoio |

## 7. Termos Acadêmicos e Institucionais

| Termo | Definição | Contexto |
|-------|-----------|----------|
| **Fatec Taquaritinga** | Instituição de ensino | Faculdade de Tecnologia |
| **ADS** | Análise e Desenvolvimento de Sistemas | Curso técnico |
| **Prof. Dr. Nivaldo Carletto** | Stakeholder-avaliador | Patrocinador + avaliador contínuo |
| **Disciplina de Gerência de Projetos** | Contexto acadêmico | PMBOK 6ª como bibliografia base |
| **Simplificação Pedagógica** | Restrição didática | Exclusão de Aquisições e Partes Interessadas |
| **Obsolescência Assumida** | Declaração de maturidade | PMBOK 6ª (2017) vs. 7ª (2021) |
| **Banca Acadêmica** | Avaliadores | Apenas Prof. Nivaldo no COGME |
| **Entrega Parcial** | Marco intermediário | Consolidação documental (08/09/2026) |
| **Entrega Final** | Marco de conclusão | MVP + documentação (Nov/Dez 2026) |
| **Rastreabilidade de Prompts** | Auditoria de LLM | Prompts catalogados em `/docs/prompts/` |

## 8. Métricas e Indicadores

| Métrica | Fórmula/Definição | Meta COGME |
|---------|-------------------|------------|
| **Cycle Time** | Tempo médio To Do → Done | ≤ 3 dias |
| **Throughput** | Cards concluídos/semana | ≥ 5 cards |
| **SPI** | EV / PV (Earned Value / Planned Value) | ≥ 0.9 |
| **CPI** | EV / AC (Earned Value / Actual Cost) | ≥ 0.9 |
| **Coverage** | Linhas testadas / linhas totais | ≥ 80% |
| **WIP Limit** | Cards em "In Progress" por pessoa | 3 cards |
| **Burnout** | Carga horária semanal | ≤ 20h/pessoa |
| **Scope Creep** | Desvio do backlog original | < 15% |

## 9. Princípios Constitutivos do COGME

| Código | Princípio | Fundamentação |
|--------|-----------|---------------|
| **P1** | Valor sobre documentação | PMBOK 7ª — Princípio 1 |
| **P2** | FOSS absoluto | Restrição pedagógica + valor social |
| **P3** | KISS como métrica de arquitetura | Simplicidade justificada |
| **P4** | SDD com IA auditável | Rastreabilidade via commit |
| **P5** | ACID e Clean Code | Padrão inegociável |
| **P6** | Entrega incremental via fluxo contínuo | Kanban sem sprints fixas |
| **P7** | Stakeholder único formal | Prof. Nivaldo como patrocinador-avaliador |

---

**Nota de Uso:** Este glossário deve ser consultado durante redação e revisão de artefatos para garantir consistência terminológica. Em caso de conflito entre definições, aplicar a hierarquia de governança (OKB_COGME_v2.1 §2.1).

**Versão:** 2.1  
**Data:** 07/09/2026  
**Status:** Complemento ao guardrail operacional
