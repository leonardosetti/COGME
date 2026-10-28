# 2.6 GERENCIAMENTO DOS RECURSOS DO PROJETO

**Responsável pelo gerenciamento dos recursos:** Edson Luis Silva.
**Rastreabilidade ao TAP:** Premissas P2, P5, P6 e P7 · Restrição de Recursos (equipe de 3 pessoas, hardware modesto) · Restrição de Custo (orçamento zero).
**Domínios PMBOK® 7ª:** Equipe · Trabalho do Projeto · Planejamento.
**Princípios PMBOK® 7ª aplicados:** "Criar um ambiente colaborativo da equipe do projeto"; "Demonstrar comportamentos de liderança"; "Fazer a adaptação (tailoring) com base no contexto".
**Processos PMBOK® 6ª (dicionário):** 9.1 Planejar o Gerenciamento dos Recursos · 9.2 Estimar os Recursos das Atividades · 9.3 Adquirir Recursos · 9.4 Desenvolver a Equipe · 9.5 Gerenciar a Equipe · 9.6 Controlar os Recursos.

Este plano define como os recursos humanos, físicos e tecnológicos do COGME são identificados, alocados, desenvolvidos e controlados. Conforme a estratégia de entrega faseada (Plano de Integração §1.4.1), foi redigido após o período de calibração do fluxo Kanban (23/09 a 03/10/2026), com dados reais de capacidade da equipe.

No PMBOK® 7ª, o Domínio de Desempenho da Equipe trata de criar uma equipe de alto desempenho com liderança compartilhada. O COGME o aplica por meio de autonomia na escolha dos cards (pull system), WIP limit como proteção contra sobrecarga e revisão em pares como mecanismo de aprendizagem.

---

## 2.6.1 Escritório de Projeto

### 2.6.1.1 Caracterização do Escritório de Projetos (PMO)

O COGME não pertence a uma organização com PMO formal. Por isso adota um **PMO virtual de suporte**, enxuto e embutido no repositório GitHub. Ele segue o princípio de Governança Mínima Viável (GMV, Plano de Integração §1.2.3) e a ideia de *tailoring* do PMBOK® 7ª.

| Tipo de PMO (PMBOK® 6ª §2.4.4.3) | Grau de controle | Aplicação no COGME |
| --- | --- | --- |
| De suporte | Baixo | **Adotado.** Fornece modelos (cards ubíquos, ADRs, planos), boas práticas, base de conhecimento (OKB, glossário, lições aprendidas) e métricas de fluxo. |
| De controle | Moderado | Parcial. A conformidade é verificada por gates automáticos (CI, coverage ≥ 80 %, auditoria de licenças FOSS) e pela Constituição do projeto. |
| Diretivo | Alto | Não aplicável. O GP é o decisor operacional único (CCB de membro único), sem PMO acima dele. |

Fonte: Elaborado pelos autores (2026).

### 2.6.1.2 Funções do Escritório de Projeto

| Função | Como é exercida | Responsável | Artefato / ferramenta |
| --- | --- | --- | --- |
| Padronização | Modelos de card (Padrão A documental / Padrão B User Story), ADR, plano de área | GP | `docs/`, OKB §9.3 |
| Gestão do portfólio de trabalho | Backlog único priorizado (MoSCoW + P0–P3) | GP | GitHub Projects |
| Monitoramento | Cycle Time, Throughput, CFD, WIP, coverage, self-report de horas | GP (publicação semanal) | GitHub Insights, CI |
| Gestão do conhecimento | OKB, glossário, ADRs, lições aprendidas por macro-fase, catálogo de prompts SDD | Todos | `docs/conhecimento/`, `.ai/handoffs/` |
| Controle de mudanças | Issue com label `change-request`, análise ≤ 48 h, decisão ≤ 24 h | GP (CCB) | GitHub Issues |
| Auditoria e conformidade | Auditorias contra a Constituição, registro de violações (VIO) | GP + agentes auditores | `docs/auditorias/` |
| Apoio à equipe | Refinement semanal, retrospectiva quinzenal, pareamento em code review | Todos | GitHub Projects / reuniões |

Fonte: Elaborado pelos autores (2026).

### 2.6.1.3 Recursos Humanos (Equipe do Projeto)

| Membro | Papel | Áreas de conhecimento sob responsabilidade | Disponibilidade (P5) |
| --- | --- | --- | --- |
| Leonardo David Silva Setti | Gerente de Projeto / Arquiteto / CCB / Frontend | Integração, Riscos, arquitetura, frontend, governança de agentes IA | até 20 h/semana |
| Fabricio de Lima Cabral | Desenvolvedor (Backend e PDF) | Escopo, Cronograma, Custos, **Comunicações (registro das comunicações)**, backend (lógica de negócio, integração PTAX, cache), módulo PDF | até 20 h/semana |
| Edson Luis Silva | Desenvolvedor (Qualidade) | Qualidade, **Recursos (gerenciamento dos recursos do projeto)**, testes automatizados, UAT, PDCA/Ishikawa | até 20 h/semana |
| Prof. Dr. Nivaldo Carleto | Stakeholder-Avaliador (cliente simulado) | Avaliação acadêmica nos marcos M1–M4, sem interferir na operação | nos marcos |

Fonte: Elaborado pelos autores (2026).

**Divisão das áreas 6–8:** Edson Luis Silva gerencia os **Recursos** do projeto Fabricio de Lima Cabral registra as **Comunicações** e Leonardo David Silva Setti (GP) é responsável pelos **Riscos**.

**Capacidade da equipe:** 3 membros × 20 h = **60 h/semana** no máximo. WIP máximo em fluxo = 3 cards × 3 pessoas = **9 cards**.
**[A CONFIRMAR]** Baseline real da calibração (03/10/2026): Cycle Time médio = ___ dias; Throughput médio = ___ cards/semana; horas médias declaradas = ___ h/pessoa.

### 2.6.1.4 Recursos Tecnológicos e Físicos (Plano de Recursos Tecnológicos — Premissas P2 e P6)

| Recurso | Tipo | Licença / custo | Uso no projeto |
| --- | --- | --- | --- |
| Computadores pessoais dos membros | Físico | Próprio (R$ 0,00) | Desenvolvimento, testes, documentação |
| Estação de inferência local (AMD Ryzen 7 8700G, 60 GB RAM) | Físico | Próprio | Execução do LLM local (Qwen via llama.cpp) para SDD, sem enviar dados à nuvem (Constituição P-02) |
| GitHub (repositório, Projects, Issues, Insights) | Plataforma | Free Tier | SSOT de execução, versionamento, métricas |
| GitHub Actions | Plataforma | Free Tier | Pipeline CI (lint + testes + coverage) |
| Python 3.11, FastAPI, SQLite, WeasyPrint, HTMX, Tailwind, pytest | Software | FOSS (PSF/MIT/BSD/Public Domain) | Stack do produto (ADR-001) |
| llama.cpp + Qwen + OpenCode | Software | MIT / licença autorizada | Specification-Driven Development com IA local |
| API PTAX do Banco Central do Brasil (Olinda/OData) | Serviço externo público | Gratuito, sem cadastro nem chave | Fonte oficial das cotações USD/EUR → BRL (REQ-01) |
| API da Wise Platform (Exchange Rates / Comparison) | Serviço externo (avaliação) | Exige autenticação por token | **Em avaliação:** cotação e comparação de plataformas de recebimento internacional (evolução do MVP) |
| Laboratórios / internet da Fatec | Físico | Institucional | Encontros presenciais e apresentações |

Fonte: Elaborado pelos autores (2026).

**Recursos externos de dados (APIs):**
- **PTAX/BCB (adotada):** é a taxa de referência oficial do Banco Central, publicada pelo serviço de dados abertos Olinda (OData/JSON). O acesso é público e gratuito, sem chave, e por isso atende ao orçamento zero e à soberania de dados. A cotação sai em **boletins** (abertura por volta das 10h, intermediários de hora em hora e fechamento após as 13h) e **só em dias úteis**.
- **Wise Platform (em avaliação):** a equipe quer integrar APIs de empresas de pagamento internacional, começando pela Wise. A documentação consultada em 25/10/2026 mostra três coisas:
  1. o endpoint `GET /rates` (cotações) exige token. Um teste sem autenticação devolveu HTTP 401 `missing_token`;
  2. a **Comparison API** (`GET /comparisons`), que compara preço e prazo de vários provedores de transferência, exige autenticação, e a própria Wise avisa que os dados são informativos e não devem ser usados em fluxos críticos;
  3. a seção **Simulations** serve para simular mudanças de estado (transferências, cartões, KYC) no **sandbox** (`api.wise-sandbox.com`). Não é uma simulação de conversão.

  **Conclusão:** a Wise **não oferece API pública sem autenticação**. Usá-la exige uma conta e um token guardado como segredo, fora do repositório (Constituição 7.2). Por isso ela fica como **recurso opcional/evolutivo**, sujeito à aprovação do CCB e à confirmação de que o acesso é gratuito para uso acadêmico.

### 2.6.1.5 Desenvolvimento e Gerenciamento da Equipe

- **Formação:** a equipe estuda as tecnologias da stack durante a validação "Hello World" (EAP N4.1), antes da construção (MF2).
- **Revisão em pares obrigatória:** todo card passa por *Code Review*, o que espalha conhecimento entre os membros e reduz a dependência de uma só pessoa.
- **Prevenção de burnout (risco R3):** WIP limit de 3 cards por pessoa e self-report semanal de horas. Se alguém passar de 20 h por duas semanas seguidas, o WIP é reduzido e os cards são redistribuídos (Plano de Integração §1.9).
- **Resolução de conflitos:** conversa direta na Issue → refinement semanal → decisão final do GP (CCB).
- **Reconhecimento:** coautoria registrada nos commits e citação dos responsáveis em cada plano.

### 2.6.1.6 Controle dos Recursos

| Indicador | Meta | Frequência | Ação se desviar |
| --- | --- | --- | --- |
| Horas declaradas por membro | ≤ 20 h/semana | Semanal | Redistribuir cards |
| WIP por pessoa | ≤ 3 cards | Contínuo | Bloquear a entrada de novos cards |
| Custo financeiro | R$ 0,00 | Por aquisição | Rejeitar a ferramenta e buscar alternativa FOSS (Plano de Custos) |
| Disponibilidade da API de câmbio | Cache cobre ≥ 50 % das chamadas (REQ-07) | Por release | Trocar o provedor via adapter |
| Cotas do GitHub Free Tier (minutos de Actions) | Dentro do limite gratuito | Mensal | Reduzir os gatilhos do CI |

Fonte: Elaborado pelos autores (2026).

---

## 2.6.2 Matriz de Responsabilidade

### 2.6.2.1 Legenda RACI

- **R — Responsável (Responsible):** executa o trabalho.
- **A — Aprovador (Accountable):** responde pelo resultado e aprova. Só um por atividade.
- **C — Consultado:** dá opinião antes ou durante o trabalho (comunicação nos dois sentidos).
- **I — Informado:** recebe o resultado (comunicação num só sentido).

### 2.6.2.2 Matriz RACI por Pacote da EAP

| EAP | Pacote de trabalho | Leonardo (GP) | Fabricio | Edson | Prof. Nivaldo | Agentes IA (SDD) |
| --- | --- | :-: | :-: | :-: | :-: | :-: |
| N1.1 | Identificação de Stakeholders | A/R | C | C | I | — |
| N1.2 | Planos de Gerenciamento (Integração) | A/R | C | C | I | C |
| N1.2 | Planos de Escopo, Cronograma e Custos | A | R | C | I | C |
| N1.3 | Plano da Qualidade | A | C | R | I | C |
| N1.2 | Plano de Recursos | A | C | R | I | C |
| N1.2 | Plano de Comunicações | A | R | C | I | C |
| N1.2 | Plano de Riscos | A/R | C | C | I | C |
| N1.4 | Política de Licenciamento FOSS | A/R | C | C | — | C |
| N1.5 | Backlog e Kanban | A/R | C | C | — | — |
| N2.1 | Requisitos Funcionais | A | R | C | I | C |
| N2.2 | Requisitos Não Funcionais | A | C | R | I | C |
| N3.1 | Arquitetura da Solução | A/R | C | C | I | C |
| N3.2 | Protótipo UX/UI | A | C | R | I | C |
| N3.3 | Modelagem de Dados (DER) | A | C | R | I | C |
| N4.1 | Seleção e Validação da Stack | A/R | C | C | I | C |
| N4.2 | Repositório Git + CI/CD | A/R | I | C | — | — |
| N4.3 | Setup Local e Homologação | A | R | C | — | — |
| N4.4 | Auditoria de Licenças | A | C | R | — | C |
| N5.1 | Backend — Lógica de Negócio | A | R | C | — | C |
| N5.2 | Backend — API de Câmbio (PTAX) + Cache | A | R | C | — | C |
| N5.3 | Frontend — Interface e Simulações | A/R | C | C | I | C |
| N5.4 | Módulo PDF (WeasyPrint) | A | R | C | — | C |
| N5.5 | SDD com IA (Prompts + Revisão) | A/R | C | C | — | R |
| N6.1 | Testes Unitários/Integração | A | C | R | — | C |
| N6.2 | Testes de Aceitação (UAT) | A | C | R | C | — |
| N6.3 | PDCA + Ishikawa | A | C | R | I | — |
| N7.1 | Pipeline CI | A/R | I | C | — | — |
| N8.1 | Matriz de Comunicação (RACI) | A | C | R | I | — |
| N8.2 | Canais Oficiais de Comunicação | A/R | I | C | I | — |
| N9.1–N9.3 | ADRs, Lições, Catálogo de Prompts | A/R | R | R | — | C |
| N10.1–N10.3 | Gestão de Mudanças | A/R | C | C | I | — |
| N11.1–N11.2 | Documentação Técnica e Consolidação | A | R | R | I | C |
| N12.1–N12.3 | Encerramento, Verificação SMART e Aceite | A/R | R | R | C | — |

Fonte: Elaborado pelos autores (2026).

Notas:
1. A coluna "Agentes IA (SDD)" foi **mantida por decisão da equipe**. Pela Constituição do projeto (Art. 5.1), os agentes de IA são **conselho, nunca veto**. Por isso aparecem só como C ou como R de execução assistida, sempre com revisão humana antes do merge.
2. O Prof. Dr. Nivaldo Carleto não aprova mudanças (Premissa P7). Ele aparece como C apenas no UAT e no aceite final.
3. Verificação: todas as linhas têm exatamente um **A**.

4. As atribuições dos pacotes N1–N9 vêm do campo "Atribuição" dos cards M1-01 a M1-21 do GitHub Projects (consultado em 25/10/2026). Foram definidas nas reuniões presenciais de terça-feira (ver 2.7.1.0).

### 2.6.2.3 Carga Planejada por Membro (cards M1-01 a M1-21)

| Membro | Cards atribuídos | Horas estimadas |
| --- | --- | :-: |
| Leonardo David Silva Setti | M1-01 Integração (6 h), M1-08 Arquitetura (6 h), M1-11 Stack FOSS (4 h), M1-12 Repositório + CI/CD (6 h), M1-15 ADR-001 (2 h), M1-16 ADR-002 (2 h), M1-17 ADR-003 (2 h), M1-18 Lições MF1 (2 h), M1-20 Canais Oficiais (2 h), M1-21 Labels e Mudanças (2 h) | 34 h |
| Fabricio de Lima Cabral | M1-02 Escopo (6 h), M1-03 Cronograma (4 h), M1-04 Custos (3 h), M1-06 Requisitos Funcionais (4 h), M1-13 Setup Local e Homologação (4 h) | 21 h |
| Edson Luis Silva | M1-05 Qualidade + PDCAs + Ishikawa (8 h), M1-07 RNF (4 h), M1-09 Protótipo UX/UI (8 h), M1-10 DER (8 h), M1-14 Auditoria de Licenças (3 h), M1-19 Matriz RACI (3 h) | 34 h |
| **Total** | 21 cards | **89 h** |

Fonte: GitHub Projects do COGME, campo "Atribuição" dos cards (25/10/2026).

Distribuídas em cerca de 3 semanas de MF1, as cargas ficam dentro do limite de 20 h semanais por membro (Premissa P5). Leonardo e Edson concentram mais horas. Os cards pendentes de Edson (Protótipo UX/UI e DER, ambos em *Ready*) são justamente os que seguram o marco M2.

### 2.6.2.4 Responsabilidades na Construção (MF2 / M3)

Definidas pela equipe para os pacotes de construção, que ainda precisam virar cards no Kanban (ver questão Q-02 no 2.8):

| Pacote EAP | Entrega | Responsável (R) |
| --- | --- | --- |
| N5.1 / N5.2 | Backend: lógica de negócio, integração PTAX e cache | Fabricio de Lima Cabral |
| N5.3 | Frontend: interface e simulações (HTMX + Tailwind) | Leonardo David Silva Setti |
| N5.4 | Módulo PDF (WeasyPrint) | Fabricio de Lima Cabral |
| N6.1 / N6.2 / N6.3 | Testes unitários e de integração, UAT, PDCA/Ishikawa | Edson Luis Silva |

Fonte: Elaborado pelos autores (2026).

---

**Controle de Versões — Seção 2.6**

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 25/10/2026 | Emissão inicial (rascunho para revisão em pares) | Edson Luis Silva |
