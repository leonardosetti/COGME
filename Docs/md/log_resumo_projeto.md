\*## Análise de Viabilidade e Complexidade

### 1. Viabilidade Geral

O projeto é **viável** dentro do prazo de dois bimestres acadêmicos (aproximadamente 4 meses), desde que o escopo seja **adequadamente delimitado e priorizado**. A seguir, a análise detalhada:

| Dimensão                     | Avaliação        | Justificativa                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Escopo funcional**         | ⚠️ Médio-Alto    | O sistema proposto envolve: cadastro de usuário, configuração de contratos (hora/dia/semana/mês/ano/customizado), consumo de API de câmbio em tempo real, cálculo com spread e IOF, simulação com múltiplas plataformas (Wise, Remessa Online, etc.) e geração de invoice em PDF. Em 4 meses, com um único desenvolvedor, é necessário**priorizar o MVP** (Mínimo Produto Viável) e postergar funcionalidades não essenciais. |
| **Tecnologia (Open Source)** | ✅ Favorável     | O ecossistema FOSS é maduro e oferece todas as ferramentas necessárias: frameworks web (React/Vue.js + Node.js/Python/Django/Flask, ou PHP/Laravel), bibliotecas para consumo de APIs REST, geração de PDF (como Puppeteer, wkhtmltopdf, ou bibliotecas Python), e bancos de dados relacionais ou NoSQL. Não há impedimento técnico.                                                                                          |
| **Prazo (2 bimestres)**      | ⚠️ Desafiador    | O prazo é curto para um projeto com todas as funcionalidades descritas. A entrega parcial em 08/09/2026 (apenas documentação até Gerenciamento da Qualidade) é factível. A implementação completa dependerá de um**cronograma rigoroso** e da adoção de práticas ágeis para entregas incrementais.                                                                                                                            |
| **Equipe (1 pessoa)**        | ⚠️ Risco Crítico | Conforme mencionado, este é um risco relevante. Um único desenvolvedor acumulará os papéis de**gerente de projetos, analista, desenvolvedor e testador**. Isso exige disciplina, autogerenciamento e, idealmente, o uso de ferramentas de automação (CI/CD, testes automatizados) para compensar a falta de equipe.                                                                                                           |

### 2. Recomendações para Viabilização

1. **Escopo Mínimo Viável (MVP)** — Priorizar para a primeira entrega funcional:
   - Conversão de moeda em tempo real (consumo de API gratuita, ex: ExchangeRate-API);
   - Configuração de contrato por hora, dia, mês e valor fixo;
   - Cálculo com spread e IOF;
   - Geração de invoice em PDF simplificada.

2. **Funcionalidades a serem postergadas** (se o tempo não permitir):
   - Múltiplas plataformas de transferência com taxas específicas (podem ser adicionadas como evolução);
   - Customizações avançadas (bimestre, etc.);
   - Interface complexa com múltiplos perfis de usuário.

3. **Estratégia de desenvolvimento**:
   - Adotar um **framework ágil** (Scrum ou Kanban) para gerenciar o backlog e as sprints;
   - Utilizar **bibliotecas e componentes prontos** sempre que possível para acelerar o desenvolvimento;
   - Implementar **testes automatizados** desde o início para reduzir retrabalho.

### 3. Conclusão da Avaliação

O projeto é **viável**, mas com as seguintes condições:

- **Escopo controlado**: funcionalidades essenciais primeiro;
- **Gestão de risco ativa**: monitoramento constante do cronograma e da qualidade;
- **Uso intensivo de ferramentas open source** que acelerem o desenvolvimento (frameworks, bibliotecas, templates).

A entrega parcial (documentação até Gerenciamento da Qualidade) em 08/09/2026 é **plenamente factível**, pois a documentação pode ser elaborada em paralelo ao desenvolvimento inicial.

---

## Termo de Abertura do Projeto (TAP) – Seção 1

### 1. Objetivos deste Documento

O presente **Termo de Abertura do Projeto (TAP)** tem como objetivos fundamentais:

1. **Autorizar formalmente o projeto** "Sistema de Conversão de Ganhos em Moeda Estrangeira", conferindo-lhe existência oficial perante a instituição de ensino (Fatec Taquaritinga) e perante o patrocinador/professor orientador da disciplina de Gerência de Projetos.
2. **Conceder autoridade formal ao gerente do projeto** (o próprio aluno-desenvolvedor) para aplicar os recursos organizacionais, planejar as atividades, tomar decisões e mobilizar os recursos necessários para a execução do projeto.
3. **Estabelecer o vínculo entre o projeto e os objetivos estratégicos da disciplina**, demonstrando que o desenvolvimento deste sistema atende aos requisitos acadêmicos de aplicação prática dos conceitos de gerenciamento de projetos conforme o Guia PMBOK® 6ª edição.
4. **Definir os limites preliminares do projeto**, incluindo escopo de alto nível, premissas, restrições, riscos iniciais, cronograma de marcos e orçamento preliminar, servindo como base para o planejamento detalhado das áreas de conhecimento.
5. **Identificar as principais partes interessadas** (stakeholders) e seus papéis, alinhando expectativas e estabelecendo canais de comunicação iniciais.
6. **Servir como documento de referência** ao longo de todo o ciclo de vida do projeto, garantindo que todas as decisões e alterações sejam avaliadas à luz dos objetivos e restrições aqui estabelecidos.

Este documento é elaborado na fase de **Iniciação** do projeto, como saída do processo _Desenvolver o Termo de Abertura do Projeto_ (PMBOK 6ª ed., processo 4.1), e servirá de entrada para os processos de planejamento subsequentes.

---

> **Nota**: As demais seções do Termo de Abertura do Projeto (Justificativa, Objetivos SMART, Requisitos de Alto Nível, Premissas e Restrições, Riscos Iniciais, Cronograma de Marcos, Orçamento Preliminar, Partes Interessadas e Aprovações) deverão ser elaboradas nas etapas seguintes, conforme o modelo do PMO.\*2. SITUAÇÃO ATUAL E JUSTIFICATIVA DO PROJETO\*\*

**2.1. Situação Atual**
O cenário econômico e laboral contemporâneo tem sido profundamente transformado pela consolidação do trabalho remoto e pela globalização dos contratos de prestação de serviços. No Brasil, um contingente crescente de profissionais de tecnologia, design, marketing e consultoria atua como Pessoa Jurídica (PJ) ou _freelancer_ para empresas sediadas nos Estados Unidos, Europa e demais mercados que remuneram em moeda estrangeira (predominantemente USD e EUR).

Entretanto, a gestão financeira desses ganhos apresenta uma complexidade que as ferramentas atualmente disponíveis no mercado não resolvem de maneira integrada. Para obter uma estimativa confiável do valor que efetivamente receberá em moeda nacional, o profissional é forçado a consultar múltiplos sites, planilhas manuais e calculadoras dispersas. Esse processo é moroso, suscetível a erros de digitação e de interpretação de taxas, além de não oferecer uma visão consolidada e comparativa em tempo real das diferentes variáveis que impactam a conversão.

**2.2. Justificativa e Ineditismo do Projeto**
O projeto "Conversor de Ganhos em Moeda Estrangeira" justifica-se, em primeiro plano, pela **inegável lacuna prática** existente no ecossistema de software atual: não há, até o momento, uma solução única, gratuita e de código aberto que reúna, em um mesmo ambiente, a simulação cambial completa, a comparação entre diferentes regimes de cálculo e a emissão de documentos fiscais/financeiros associados.

Além disso, o projeto possui **ineditismo no âmbito acadêmico-aplicado**. Diferentemente de abordagens puramente teóricas ou de sistemas de baixa complexidade (como CRUDs convencionais), este projeto aborda um domínio de negócio real — o mercado financeiro-cambial aliado ao trabalho remoto internacional — que exige rigor na gestão de requisitos, tratamento de dados dinâmicos e usabilidade centrada no usuário final. Essa complexidade oferece um campo fértil para a aplicação prática e aprofundada de todas as áreas de conhecimento do gerenciamento de projetos.

**2.3. Alinhamento com os Objetivos da Disciplina e da FATEC**
A proposta atende plenamente à premissa pedagógica da disciplina de Gerência de Projetos: aplicar na prática as dez áreas de conhecimento do PMBOK® 6ª edição (Integração, Escopo, Cronograma, Custo, Qualidade, Recursos, Comunicações, Riscos, Aquisições e Partes Interessadas) em um ciclo de vida completo de projeto. Ao desenvolver um sistema com requisitos funcionais e não funcionais claros, o aluno-gerente vivenciará situações reais de tomada de decisão, negociação de escopo, mitigação de riscos e garantia da qualidade, consolidando a aprendizagem significativa exigida pelo curso de Análise e Desenvolvimento de Sistemas da Fatec Taquaritinga.

**2.4. Compromisso com o Software Livre (FOSS) e o Impacto Social**
A determinação de utilizar exclusivamente tecnologias _open source_ não é uma restrição técnica, mas sim um **valor fundante** do projeto, plenamente justificável pelos seguintes pilares:

- **Transparência e Auditabilidade**: O usuário final e a comunidade técnica poderão verificar os procedimentos de cálculo, eliminando a desconfiança sobre "caixas-pretas" financeiras;
- **Gratuidade e Acessibilidade**: Profissionais autônomos e Microempreendedores Individuais (MEIs), muitas vezes com recursos financeiros limitados, terão acesso a uma ferramenta profissional sem custos de licenciamento;
- **Sustentabilidade e Comunidade**: O código aberto viabiliza que a comunidade de desenvolvedores e usuários contribua com melhorias e evoluções, perpetuando o projeto para além do ciclo acadêmico;
- **Alinhamento Institucional**: A escolha é coerente com a filosofia da educação pública, gratuita e de qualidade, promovendo a disseminação do conhecimento e da tecnologia como bens comuns.

**2.5. Público-Alvo e Impacto Esperado**
O sistema destina-se a profissionais brasileiros que prestam serviços ao exterior (desenvolvedores, _designers_, tradutores, consultores, arquitetos, entre outros), bem como a pequenas agências que gerenciam contratos internacionais. O impacto direto esperado é o **fortalecimento da autonomia financeira** do usuário: ao dispor de simulações precisas e rápidas, ele poderá negociar contratos com base em dados concretos, planejar seus rendimentos em moeda nacional com maior segurança e reduzir as incertezas inerentes à volatilidade cambial, otimizando sua margem de ganho real.

---

### Análise Crítica da Abordagem Proposta

A abordagem está **conceitualmente correta** e todos os elementos listados são absolutamente pertinentes para o sucesso do projeto. Contudo, para que o **terceiro tópico do TAP** não invada os domínios dos planos de gerenciamento posteriores (Escopo, Cronograma, Qualidade, Recursos), é imprescindível aplicar o seguinte filtro:

| Elemento Solicitado                 | Tratamento Correto no TAP (Alto Nível)                                                                                                                  | Tratamento Incorreto (Invasão)                                                                                                           |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Índice de Qualidade do Software** | Definir uma meta mensurável de alto nível, ex: "cobertura de testes automatizados ≥ 80%" ou "zero defeitos críticos na entrega".                        | Detalhar*quais* ferramentas de teste (Jest, PyTest) ou _quais_ métricas de qualidade (complexidade ciclomática, manutenibilidade).       |
| **Testes de Software**              | Estabelecer como critério de sucesso a aprovação em um conjunto de testes de aceitação (UAT) para os fluxos principais.                                 | Descrever a estratégia de testes (unitário, integração, caixa-branca) ou o ambiente de homologação.                                      |
| **Prazos (2 bimestres)**            | Declarar as datas-marco de maneira específica (08/09/2026 e fim do 2º bimestre).                                                                        | Detalhar o cronograma detalhado com dependências e precedências (isto é do plano de cronograma).                                         |
| **Uso exclusivo de FOSS**           | Transformar em uma**restrição/condição de sucesso** verificável (ex: "todas as ferramentas utilizadas deverão possuir licenças aprovadas pela OSI").    | Especificar a*stack* tecnológica exata (ex: Django, React, PostgreSQL).                                                                  |
| **Métricas do Projeto**             | Definir a obrigatoriedade de entregar relatórios de desempenho (ex: medição de Valor Agregado - EVM) ao final de cada sprint.                           | Especificar a ferramenta de medição ou a fórmula exata de cada indicador (isso pertence ao plano de gerenciamento de custos/cronograma). |
| **IA Generativa (Redação)**         | Estabelecer a premissa de que LLMs serão usados como ferramenta de apoio, mas que todos os artefatos serão revisados e validados pelo gerente.          | Descrever o*prompt engineering* ou o fluxo de trabalho com a IA.                                                                         |
| **IA + SDD (Implementação)**        | Definir como meta a adoção do paradigma*Specification-Driven Development* com LLMs, garantindo que o código gerado atenda às especificações funcionais. | Especificar a arquitetura de microsserviços ou o padrão de projeto (MVC, Clean Architecture).                                            |

---

**3. OBJETIVOS SMART E CRITÉRIOS DE SUCESSO DO PROJETO**

Este tópico estabelece os objetivos mensuráveis do projeto e os critérios formais que determinarão seu sucesso ou fracasso ao final do ciclo de vida. Todos os objetivos estão alinhados à premissa fundamental de desenvolvimento exclusivamente com tecnologias _Open Source_ (FOSS).

**3.1. Objetivos SMART do Projeto**

| **Categoria**              | **Objetivo (Declaração SMART)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **Componentes SMART**                                                                                                                                                                                                                           |
| :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Produto (Escopo)**       | **Específico e Mensurável:** Desenvolver e entregar um _Minimum Viable Product_ (MVP) de um sistema _web_ funcional que realize simulações de conversão de moeda estrangeira para moeda nacional, permitindo ao usuário configurar diferentes regimes de contratação (hora, dia, semana, mês e valor fixo), aplicar encargos financeiros simulados e emitir uma _invoice_ em formato PDF. O sistema deverá processar as simulações em até 3 segundos.                                                                                     | **S** - Configuração de regimes e emissão de PDF; **M** - Tempo de resposta ≤ 3s; **A** - Responsável: Aluno-Gerente; **R** - Escopo viável para 1 pessoa; **T** - Entrega final até o término do 2º bimestre letivo (previsão: Dezembro/2026). |
| **Qualidade e Testes**     | **Mensurável:** O software entregue deverá apresentar, no mínimo, 80% de cobertura de código por testes automatizados (unitários e de integração) e deverá ser aprovado em um roteiro de testes de aceitação (_User Acceptance Testing - UAT_) que cubra 100% dos fluxos funcionais críticos (cálculo, configuração e geração de PDF), sem a presença de defeitos classificados como críticos ou bloqueantes.                                                                                                                             | **S** - Definição de métrica de cobertura; **M** - ≥80% de cobertura e zero defeitos críticos; **A** - Responsável: Aluno-Gerente; **R** - Factível com bibliotecas FOSS de teste; **T** - Verificado na entrega final (Dezembro/2026).         |
| **Cronograma (Marcos)**    | **Temporal:** O projeto deverá obrigatoriamente cumprir dois marcos temporais principais: (i) Entrega parcial da documentação do projeto (do TAP até o plano de Gerenciamento da Qualidade) até o dia **08 de setembro de 2026**; (ii) Entrega final do MVP funcional com sua respectiva documentação consolidada até o encerramento do 2º bimestre acadêmico (Dezembro/2026).                                                                                                                                                            | **S** - Datas específicas; **M** - Verificação por entrega física/digital; **A** - Responsável: Aluno-Gerente; **R** - Prazos institucionais fixos; **T** - 08/09/2026 e Dez/2026.                                                              |
| **Métricas e Indicadores** | **Mensurável:** Durante toda a execução, o gerente do projeto deverá produzir e entregar, quinzenalmente, relatórios de desempenho contendo os indicadores de valor agregado (_Earned Value Management - EVM_) - especificamente a Variação de Prazo (SPI) e Variação de Custo (CPI) - além do acompanhamento do _Burndown Chart_ de entregas, garantindo a rastreabilidade do progresso.                                                                                                                                                 | **S** - EVM e Burndown; **M** - Relatórios quinzenais; **A** - Responsável: Aluno-Gerente; **R** - Métricas padronizadas pelo PMBOK; **T** - Durante todo o ciclo (Set a Dez/2026).                                                             |
| **Inovação e Ferramentas** | **Atribuível e Realístico:** Todo o ciclo de vida do projeto (gerenciamento, modelagem, desenvolvimento, testes e documentação) será conduzido exclusivamente com ferramentas de código aberto (FOSS). Ademais, o projeto deverá empregar Inteligência Artificial Generativa (LLMs) para auxiliar na redação dos artefatos e na implementação do código, adotando a abordagem _Specification-Driven Development_ (SDD) para garantir que o código gerado esteja estritamente aderente às especificações funcionais previamente validadas. | **S** - FOSS e SDD com LLM; **M** - Verificação da licença de todas as ferramentas; **A** - Responsável: Aluno-Gerente; **R** - Ecossistema FOSS maduro; **T** - Aplicado do início ao fim do projeto.                                          |

**3.2. Critérios de Sucesso do Projeto**

O projeto será formalmente considerado um **SUCESSO** se, e somente se, todos os critérios abaixo forem integralmente atendidos até a data de encerramento:

1. **Critério de Aceitação Final:** O MVP entregue for aprovado pelo patrocinador (professor orientador) e pelos _stakeholders_ representativos (usuários piloto) em uma sessão de validação prática, demonstrando que a ferramenta resolve a dor da falta de integração nas simulações cambiais.
2. **Critério de Conformidade (FOSS):** 100% das ferramentas, bibliotecas e _frameworks_ utilizados possuírem licenças reconhecidas pela _Open Source Initiative_ (OSI), e a lista completa de dependências for documentada e auditável.
3. **Critério de Qualidade:** O código-fonte entregue atingir o índice mínimo de 80% de cobertura de testes e não apresentar defeitos de severidade crítica ou alta no ambiente de homologação.
4. **Critério Documental:** Todos os planos de gerenciamento das áreas de conhecimento (conforme PMBOK 6ª ed.) e todos os artefatos de requisitos forem entregues dentro do prazo estipulado (08/09/2026 para a parcela inicial), com o devido versionamento e rastreabilidade de alterações.
5. **Critério de Inovação Controlada:** A utilização de IA Generativa para SDD deve ser devidamente registrada, demonstrando que o código gerado foi revisado, testado e integrado ao repositório por meio de _commits_ assinados pelo gerente-desenvolvedor, garantindo a propriedade intelectual e a conformidade ética com as políticas acadêmicas da FATEC.

**3.3. Condições de Fracasso (Não Sucesso)**
O projeto será considerado **não bem-sucedido** caso, ao término do 2º bimestre, o MVP não esteja funcional, ou caso algum dos critérios de qualidade/conformidade acima não seja atingido, ou ainda se os marcos intermediários (especialmente o de 08/09/2026) não forem cumpridos sem uma justificativa formal e aprovada por meio de solicitação de mudança.

### Análise e Sugestão de Reformulação

1. **Fase "Planejamento de Projeto"** → Mantida, mas expandida para incluir a **Iniciação** (já que estamos redigindo o TAP) e os **Requisitos**, pois sem um levantamento detalhado não é possível desenvolver.
2. **Fase "Ferramentas" + "Configuração de Ambiente"** → **Fundidas** em uma única fase lógica, pois a seleção da stack FOSS e a configuração do ambiente andam juntas e são pré-requisitos para o desenvolvimento.
3. **Nova fase: "Modelagem e Prototipação"** → Essencial para alinhar a UX/UI antes da codificação, especialmente considerando a complexidade dos regimes de contratação.
4. **Nova fase: "Encerramento"** → Obrigatória pelo PMBOK, para formalizar o aceite final, lições aprendidas e entrega da documentação consolidada.
5. **Subfases específicas do negócio:** Incluí subitens para "Integração com API de Câmbio", "Regras de Cálculo (Spread/IOF)", "Geração de PDF" e "Uso de IA com SDD" dentro do Desenvolvimento.

Abaixo, apresento a **EAP estruturada** em notação **Mermaid**, seguida da descrição detalhada das subfases.

---

### 4. ESTRUTURA ANALÍTICA DO PROJETO (EAP) - FASES E PRINCIPAIS ENTREGAS

---

### Descrição Detalhada das Fases e Subfases

| **Fase**                                           | **Subfases (Entregáveis Principais)**                                                                                                                        | **Justificativa / Relação com o Escopo**                                                                                                                            |
| :------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Iniciação e Planejamento**                    | 1.1 TAP; 1.2 Stakeholders; 1.3 Planos de Gerência (Escopo, Cronograma, Custo, Riscos); 1.4 Plano da Qualidade                                                | Formaliza o projeto, define as bases para todas as decisões futuras e estabelece as métricas de qualidade (ex: 80% de cobertura de testes).                         |
| **2. Levantamento e Análise de Requisitos**        | 2.1 Requisitos Funcionais (regimes de contratação, cálculos, emissão de PDF); 2.2 Requisitos Não Funcionais (FOSS, tempo de resposta ≤ 3s); 2.3 Casos de Uso | Garante que toda a regra de negócio (simulação, plataformas, IOF) seja detalhada antes da codificação, evitando retrabalho.                                         |
| **3. Modelagem e Prototipação**                    | 3.1 Arquitetura; 3.2 Protótipo UX/UI; 3.3 Modelagem de Dados                                                                                                 | Traduz os requisitos em um desenho técnico, essencial para a comunicação visual e para guiar a implementação com IA (SDD).                                          |
| **4. Configuração de Ambiente e Ferramentas FOSS** | 4.1 Seleção da Stack; 4.2 Git; 4.3 Setup Local; 4.4 Setup Homologação                                                                                        | Atende à premissa de uso exclusivo de ferramentas*open source*. Cria a infraestrutura onde o código será versionado, testado e executado.                           |
| **5. Desenvolvimento do Sistema**                  | 5.1 Lógica de negócio; 5.2 API de câmbio; 5.3 Frontend; 5.4 Módulo PDF; 5.5 Implementação com IA (SDD)                                                       | Núcleo do projeto. A subfase 5.5 é inovadora e garante que a IA generativa seja usada de forma controlada, com código revisado e validado.                          |
| **6. Garantia da Qualidade e Testes**              | 6.1 Testes Unitários/Integração (≥80%); 6.2 Testes de Aceitação (zero defeitos críticos); 6.3 Testes de Performance                                          | Valida os critérios de sucesso definidos no tópico 3. É o filtro de qualidade antes da entrega.                                                                     |
| **7. DevOps e CI/CD**                              | 7.1 Pipeline CI (build/testes automáticos); 7.2 Pipeline CD (deploy automático)                                                                              | Automatiza o processo de entrega, reduzindo erros manuais e acelerando o feedback, crucial para um time de 1 pessoa.                                                |
| **8. Implantação (Deploy)**                        | 8.1 Publicação em Produção; 8.2 Plano de Rollback                                                                                                            | Disponibiliza o sistema para os usuários piloto (público-alvo), utilizando hospedagem FOSS (ex: VPS com Linux, ou serviços como Heroku/Railway na camada gratuita). |
| **9. Documentação do Projeto**                     | 9.1 Técnica; 9.2 Manual; 9.3 Relatórios EVM; 9.4 Parcial (até 08/09/2026)                                                                                    | Atende aos requisitos acadêmicos e gerenciais. A subfase 9.4 é o*deliverable* crítico do primeiro bimestre.                                                         |
| **10. Encerramento**                               | 10.1 Lições Aprendidas; 10.2 Verificação SMART; 10.3 Apresentação Final                                                                                      | Fecha formalmente o ciclo de vida do projeto, obtendo o aceite do patrocinador (professor) e documentando os aprendizados para a comunidade FOSS.                   |

---

### Nota sobre a EAP (Boas Práticas PMBOK)

- **Decomposição:** As fases representam o ciclo de vida completo (do conceito ao encerramento).
- **100% do Escopo:** Nenhuma atividade descrita nas seções anteriores (TAP, Justificativa, Objetivos SMART) ficou de fora.
- **Controle de Complexidade:** Dividi o "Desenvolvimento" em partes lógicas (Backend/API/Frontend/PDF/IA) para facilitar o gerenciamento, considerando que há um único recurso (1 pessoa) para executar todas as tarefas.

Excelentes observações! Vamos endereçar cada uma delas com o rigor que o PMBOK® 6ª edição exige.

### 1. Análise da Conformidade com o PMBOK® 6ª ed.

**Sobre o TAP como subfase:** Sua dúvida é procedente, mas nesse aspecto específico a estrutura está **correta**. No contexto da disciplina, a fase de "Iniciação" tem como principal entregável justamente o **Termo de Abertura (TAP)**. Ele é o marco zero do projeto. Portanto, mantê-lo como `1.1` é adequado, pois documenta a saída do processo _4.1 Desenvolver o Termo de Abertura_.

**O ERRO CRÍTICO (e você acertou em cheio):** A EAP (Estrutura Analítica do Projeto) exige a **Regra dos 100%**, que determina que o nó raiz deve ser o **nome do projeto** e que todos os pacotes de trabalho são seus descendentes diretos ou indiretos. No diagrama anterior, as fases estavam soltas (paralelas) no nível mais alto, o que fere a hierarquia da EAP.

**Correção:** Incluirei o nó raiz `"Projeto: Conversor de Ganhos em Moeda Estrangeira"` acima de todas as fases.

### 2. Melhoria Visual (Diagramação)

Você tem toda a razão sobre a poluição visual causada pelo uso excessivo de `&` (junção horizontal). Para resolver isso, reestruturarei o diagrama utilizando **Subgráficos (subgraphs)** no Mermaid. Isso agrupa cada fase e suas subfases em "caixas" visuais, organizando o fluxo de cima para baixo (Top-Down) e eliminando a dispersão horizontal excessiva. Caso prefira uma ferramenta ainda mais flexível e gratuita para edição manual, recomendo o **draw.io (diagrams.net)** — que possui integração com GitHub e é amplamente utilizado em escritórios de projeto.

### 3. Inclusão da Fase de "Validação de Licenças"

Adição da **Governança de Licenças FOSS** em dois momentos críticos:

- **Durante o Planejamento (1.5):** Para definir a política de seleção de ferramentas (ex: priorizar licenças MIT, GPL, Apache).
- **Como uma fase autônoma (11):** Para auditoria formal de todas as dependências (bibliotecas, frameworks, imagens Docker) e definição da licença do produto final (ex: GPLv3 ou MIT), garantindo que nenhum componente com licença restritiva (ex: AGPL com cláusulas comerciais) entre no escopo.

---

### EAP Revisada e Corrigida (Formato Mermaid com Subgráficos)

---

### Descrição dos Acréscimos (Novas Subfases)

| **Fase / Subfase**                                     | **Descrição e Justificativa**                                                                                                                                                                                                                                                                                                                    |
| :----------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1.5. Política de Licenciamento FOSS**                | Define os critérios de aceitação para escolha de ferramentas (ex: priorizar MIT/BSD, evitar GPL com cláusulas virais que exijam abertura do código-fonte do produto, caso contrário).                                                                                                                                                            |
| **4.5. Auditoria de Licenças das Dependências**        | Etapa prática de execução de ferramentas como`license-checker` (npm) ou `pip-licenses` para listar e validar TODAS as dependências antes do início da codificação pesada.                                                                                                                                                                        |
| **11. Governança e Conformidade (Licenciamento FOSS)** | Fase dedicada a garantir que o*produto final* (o sistema entregue) possua uma licença open source claramente definida e aplicada (nos cabeçalhos dos arquivos, no repositório e na documentação). É uma fase de "suporte" que permeia todo o projeto, mas que precisa de um pacote de trabalho específico para auditoria formal no encerramento. |

### Análise: Desenvolvimento Ágil como Fase na EAP

Sob a ótica do **PMBOK® 6ª edição**, a resposta é **NÃO**, o Desenvolvimento Ágil **não deve** ser uma fase autônoma (nível 1) na EAP.

**Motivo:** A EAP (Estrutura Analítica do Projeto) decompõe **entregáveis** (produtos ou documentos), e não **metodologias** ou **ciclos de vida**. "Desenvolvimento Ágil" é uma abordagem de gerenciamento (como usar Scrum ou Kanban), e não um entregável em si. Incluí-lo como fase quebraria a **Regra dos 100%**, pois ele não gera um artefato final separado dos demais.

**Solução correta (para destacá-lo sem ferir o PMBOK):**
Incorporei o Ágil como **subfases operacionais** dentro das fases existentes, especialmente em:

- **Planejamento (1.6):** Definição do _Backlog_ do Produto e Estruturação das _Sprints_.
- **Desenvolvimento (5.6):** Execução das _Sprints_ (com Planning, Daily, Review e Retrospectiva).

---

### EAP Final Revisada e Estruturada para Draw.io

Como o Mermaid não está renderizando bem neste ambiente, preparei uma **lista hierárquica detalhada** para você construir manualmente no **draw.io** (diagrams.net) de forma rápida e profissional.

**Layout sugerido no draw.io:**

- Estrutura **Top-Down (árvore)**.
- Raiz no topo (nível 0).
- 11 fases principais (nível 1) descendo em blocos horizontais.
- Subfases (nível 2) abaixo de cada bloco.
- Utilize retângulos arredondados e setas conectoras.

---

**NÍVEL 0 (RAIZ)**

> **📁 Projeto: Conversor de Ganhos em Moeda Estrangeira**

---

**NÍVEL 1 e 2 (FASES E ENTREGÁVEIS)**

| **Fase (Nível 1)**                                    | **Subfases / Pacotes de Trabalho (Nível 2)**                                                                                                                                                                                                                                                     |
| :---------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Iniciação e Planejamento**                       | 1.1. Termo de Abertura (TAP)1.2. Identificação de Stakeholders1.3. Planos de Gerenciamento (Escopo, Cronograma, Custo, Riscos)1.4. Plano de Gerenciamento da Qualidade1.5. Política de Licenciamento FOSS**1.6. Definição do Backlog e Estruturação das Sprints (Ágil)**                         |
| **2. Levantamento e Análise de Requisitos**           | 2.1. Elicitação de Requisitos Funcionais (Regimes, Cálculos)2.2. Elicitação de Requisitos Não Funcionais (Performance, Segurança)2.3. Especificação de Casos de Uso e Histórias de Usuário                                                                                                       |
| **3. Modelagem e Prototipação**                       | 3.1. Arquitetura da Solução (Frontend/Backend/API)3.2. Protótipo de Interface (UX/UI)3.3. Modelagem de Dados                                                                                                                                                                                     |
| **4. Configuração de Ambiente e Ferramentas**         | 4.1. Seleção e Validação da Stack FOSS4.2. Configuração do Repositório Git4.3. Setup do Ambiente de Desenvolvimento Local4.4. Setup do Ambiente de Homologação4.5. Auditoria de Licenças das Dependências                                                                                        |
| **5. Desenvolvimento do Sistema (com Sprints Ágeis)** | 5.1. Backend - Lógica de Negócio (Câmbio, Spread, IOF)5.2. Backend - Consumo de API de Câmbio5.3. Frontend - Interface e Simulações5.4. Módulo de Geração de Invoice (PDF)5.5. Implementação Assistida por IA (SDD com LLM)**5.6. Execução das Sprints (Planejamento, Revisão e Retrospectiva)** |
| **6. Garantia da Qualidade e Testes**                 | 6.1. Testes Unitários e de Integração (Meta ≥ 80%)6.2. Testes de Aceitação (UAT - Zero defeitos críticos)6.3. Testes de Usabilidade e Performance                                                                                                                                                |
| **7. DevOps e CI/CD**                                 | 7.1. Pipeline de Integração Contínua (CI)7.2. Pipeline de Entrega Contínua (CD)                                                                                                                                                                                                                  |
| **8. Implantação (Deploy)**                           | 8.1. Publicação em Ambiente de Produção8.2. Documentação de Implantação e Plano de Rollback                                                                                                                                                                                                      |
| **9. Documentação do Projeto**                        | 9.1. Documentação Técnica (Arquitetura, APIs)9.2. Manual do Usuário9.3. Relatórios de Desempenho (EVM/Burndown)9.4. Consolidação da Documentação Parcial (Entrega 08/09/2026)                                                                                                                    |
| **10. Encerramento**                                  | 10.1. Relatório de Lições Aprendidas10.2. Verificação dos Critérios SMART10.3. Apresentação Final e Aceite do Patrocinador                                                                                                                                                                       |
| **11. Governança e Conformidade (FOSS)**              | 11.1. Validação de Licenças das Ferramentas de Desenvolvimento11.2. Validação de Licenças das Bibliotecas/Dependências11.3. Definição e Registro da Licença do Produto Final (Ex: MIT/GPL)                                                                                                       |

---

**Nota sobre as Subfases Ágeis (1.6 e 5.6):**
Com essa estrutura, o Ágil não é uma fase solta, mas sim a **mecânica de execução** do desenvolvimento e do planejamento. Isso atende à sua solicitação de "destacar" a regra ágil, mantendo a EAP 100% aderente ao rigor conceitual do PMBOK, pois todos os nós representam entregáveis ou atividades concretas (Backlog definido, Sprints executadas, Rituais documentados).

## 8. RESTRIÇÕES

### 8.1. Contexto Aplicado

O presente projeto está sujeito a um conjunto de limitações concretas que condicionam sua execução, decorrentes de seu ambiente acadêmico, da infraestrutura disponível e das premissas tecnológicas adotadas. Estas restrições **não podem ser desconsideradas ou violadas** sob pena de inviabilização parcial ou total do empreendimento. Elas atuam como parâmetros fixos dentro dos quais a equipe deve planejar, executar e monitorar todas as atividades, exigindo uma gestão de escopo rigorosa, priorização constante e tomada de decisão orientada à mitigação de impactos.

A seguir, as restrições são detalhadas conforme as categorias fundamentais do PMBOK® 6ª edição, aplicadas diretamente à realidade do projeto "Conversor de Ganhos em Moeda Estrangeira".

---

### 8.2. Restrições de Escopo

| **Restrição**               | **Descrição e Impacto**                                                                                                                                                                                                                                                                            |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Escopo restrito ao MVP**  | O projeto entregará um**Produto Mínimo Viável (MVP)** em regime acadêmico. Funcionalidades não essenciais (ex: múltiplas plataformas de transferência, cadastro de múltiplos usuários, relatórios gerenciais avançados) ficarão para versões futuras, salvo aprovação formal em mudança de escopo. |
| **Desenvolvimento do zero** | Não haverá reaproveitamento de código ou sistemas legados. Toda a construção ocorrerá a partir de requisitos originais, demandando esforço integral de modelagem, codificação e testes no período letivo.                                                                                          |

---

### 8.3. Restrições de Cronograma

| **Restrição**                | **Descrição e Impacto**                                                                                                                                                                                                                               |
| :--------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Prazo letivo inegociável** | Dois bimestres acadêmicos, com marco intermediário obrigatório em**08/09/2026** (entrega documental até o plano de Gerenciamento da Qualidade). Cerca de **25% do tempo total já transcorreu**, restando aproximadamente 3 meses para execução plena. |
| **Disponibilidade reduzida** | O curso é noturno, limitando a carga horária semanal dedicada ao projeto. A equipe (2 pessoas) concilia as atividades com outras disciplinas e compromissos profissionais, exigindo planejamento granular e produtividade otimizada.                  |

---

### 8.4. Restrições de Custo (Orçamento)

| **Restrição**                     | **Descrição e Impacto**                                                                                                                                                                                                             |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Orçamento nulo**                | Não há verba institucional ou patrocínio. Todos os custos operacionais (hospedagem, ferramentas, serviços) serão absorvidos pela equipe ou obtidos via planos gratuitos.                                                            |
| **Proibição de aquisições pagas** | Nenhuma ferramenta, biblioteca ou serviço oneroso poderá ser utilizado. A seleção da stack tecnológica fica restrita a soluções**gratuitas e de código aberto (FOSS)** ou com planos gratuitos suficientes para o escopo acadêmico. |

---

### 8.5. Restrições de Recursos (Peopleware)

| **Restrição**                                  | **Descrição e Impacto**                                                                                                                                                                                                                               |
| :--------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Equipe reduzida (2 pessoas)**                | Embora tenha havido um reforço, a equipe é composta por apenas dois membros, que acumularão múltiplos papéis: gerência, análise, desenvolvimento, testes, documentação e DevOps. A**paralelização é limitada** e a dependência de cada membro é alta. |
| **Hardware modesto**                           | Os equipamentos pessoais dos integrantes possuem capacidade computacional limitada, impactando tempos de build, execução de testes pesados e simulações.                                                                                              |
| **Dependência de serviços externos gratuitos** | APIs de câmbio e hospedagem dependem de provedores terceiros sem garantia de estabilidade, disponibilidade ou continuidade, sujeitos a limites de requisição e mudanças em suas políticas.                                                            |

---

### 8.6. Restrições de Qualidade

| **Restrição**                       | **Descrição e Impacto**                                                                                                                                                                                                                      |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tempo restrito para testes**      | Com prazo reduzido, os testes deverão ser priorizados nos fluxos críticos (cálculo de câmbio, configuração de regimes, geração de PDF). A meta de**80% de cobertura** é desafiadora, mas factível com uso de ferramentas automatizadas FOSS. |
| **Ambiente de validação acadêmico** | Os testes de aceitação e usabilidade serão conduzidos com um número limitado de usuários-piloto (colegas e professores), não refletindo plenamente a diversidade do público-alvo real.                                                       |

---

### 8.7. Restrições de Riscos

| **Restrição**                             | **Descrição e Impacto**                                                                                                                                                                         |
| :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sem contingência formal**               | A equipe não dispõe de recursos extras (financeiros, humanos ou tecnológicos) para planos de contingência estruturados. A gestão de riscos dependerá de ações preventivas e adaptações rápidas. |
| **Dependência crítica de APIs gratuitas** | O consumo de cotação cambial em tempo real é função central; a eventual indisponibilidade ou limitação da API escolhida pode bloquear o MVP.                                                    |

---

### 8.8. Restrições Tecnológicas e Operacionais

| **Restrição**                           | **Descrição e Impacto**                                                                                                                                                                                                                 |
| :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stack exclusivamente FOSS/gratuita**  | Todo o ciclo de vida (gerenciamento, desenvolvimento, testes, documentação, CI/CD, hospedagem) utilizará ferramentas**gratuitas**, preferencialmente open source. Isso restringe o leque de opções e exige pesquisa de compatibilidade. |
| **Abordagem experimental (SDD com IA)** | O uso de**Specification-Driven Development** com suporte de LLMs é inovador e não garantido. Os artefatos gerados por IA demandam revisão humana rigorosa, sob risco de erros lógicos ou de segurança.                                  |
| **Licenciamento do produto final**      | O software entregue deverá ser licenciado como open source (ex: MIT, GPLv3), condição imposta pelo uso de ferramentas FOSS e pelo caráter acadêmico, restringindo futura comercialização.                                               |

---

### 8.9. Síntese Consolidada das Restrições

| **Categoria PMBOK** | **Restrições Aplicáveis**                                                     |
| :------------------ | :---------------------------------------------------------------------------- |
| **Escopo**          | MVP acadêmico; desenvolvimento do zero                                        |
| **Cronograma**      | 2 bimestres (com 25% já decorrido); marco 08/09/2026; curso noturno           |
| **Custo**           | Orçamento zero; proibição de ferramentas pagas                                |
| **Recursos**        | Equipe de 2 pessoas (múltiplos papéis); hardware modesto; dependência externa |
| **Qualidade**       | Testes com tempo limitado; ambiente de validação restrito                     |
| **Riscos**          | Sem plano de contingência formal; APIs gratuitas instáveis                    |
| **Tecnológicas**    | FOSS/gratuito obrigatório; SDD experimental; licença open source final        |

---

**Nota:** As restrições documentadas são de alto nível, conforme exigido pelo TAP. Os detalhamentos operacionais e as estratégias de mitigação serão desenvolvidos nos planos de gerenciamento específicos (Escopo, Cronograma, Custo, Recursos, Qualidade, Riscos). Alterações nestas restrições ao longo do projeto devem ser formalizadas por meio de solicitação de mudança e aprovadas pelo patrocinador (professor orientador).

```
OK;Retornemos agora para a seção 5 Principais requisitos das principais entregas/produtos.
Esta é uma seção com nível de criticidade alta, pois definirá de forma objetiva quais serão os requisitos que comporão o MVP.
Vamos considerar o objetivo do projeto e do produto alvo: COGME - Conversão de Ganhos em Moeda Estrangeira;
A fim de manter uma revisão clara, segue:
"
2.1. Situação Atual
O cenário econômico e laboral contemporâneo tem sido profundamente transformado pela consolidação do trabalho remoto e pela globalização dos contratos de prestação de serviços. No Brasil, um contingente crescente de profissionais de tecnologia, design, marketing e consultoria atua como Pessoa Jurídica (PJ) ou freelancer para empresas sediadas nos Estados Unidos, Europa e demais mercados que remuneram em moeda estrangeira (predominantemente USD e EUR).Entretanto, a gestão financeira desses ganhos apresenta uma complexidade que as ferramentas atualmente disponíveis no mercado não resolvem de maneira integrada. Para obter uma estimativa confiável do valor que efetivamente receberá em moeda nacional, o profissional é forçado a consultar múltiplos sites, planilhas manuais e calculadoras dispersas. Esse processo é moroso, suscetível a erros de digitação e de interpretação de taxas, além de não oferecer uma visão consolidada e comparativa em tempo real das diferentes variáveis que impactam a conversão.2.2. Justificativa e Ineditismo do Projeto
O projeto "Conversor de Ganhos em Moeda Estrangeira" justifica-se, em primeiro plano, pela inegável lacuna prática existente no ecossistema de software atual: não há, até o momento, uma solução única, gratuita e de código aberto que reúna, em um mesmo ambiente, a simulação cambial completa, a comparação entre diferentes regimes de cálculo e a emissão de documentos fiscais/financeiros associados.
"O que o MVP deve suportar, integrar e implementar para entrega final:Stack tecnológica máximo FOSS, se não, exceções para software de uso e acesso livre;Prevalência absoluta do princípio KISS (Keep it Simple...);Ambiente alvo do projeto é web-based (desktop);Adoção rigorosa de Clean Code;Adoção rigorosa de ACID (para bases de dados);Uso exclusivo da API https://frankfurter.dev/ disponível como OpenAPI em https://api.frankfurter.dev/v2/openapi.json;
5.1. Opcionalmente podemos usar uma API do próprio Banco Central Brasioleiro se houver, evitando o uso de uma API menos confiável;Separação e isolamento de camadas de aplicação através de containers docker (Front-end, Back-end e Dados);Adoção de API RESTFul;Otimização do código para automação de testes de qualidade (respeite o tópico 1 e 3 respectivamente);Não devem ser adotados frameworks de desenvolvimento - Ex. Reactjs, Vue etc;Base de dados deve ser relacional;Adoção exclusiva da metodologia Ágil usando Kanban;Uso do Github Projects para gerenciamento integral do projeto;Aplicação de DevOps CI/CD para garantia de entrega consistente;Por opção de viabilidade de projeto, determinar a stack de linguagem mais sólida e fluida para implementação (Ex.: Html + CSS + [JavaScript / TypeScript / Python / PHP / GoLang / Rust / Java etc];Por opção de viabilidade de projeto, determinar a stack de dados mais conveniente dada a stack de linguagem escolhida - Ex.: MariaDB, MySQL, PostgreSQL etc;Objetivo do MVP diante do aspecto de Negócio (geral):Este sistema deve compreender em seu desenvolvimento o uso de um formulário onde um determinado ator (usuário) fará conversões de valores em tempo real para conferência de estimativa de ganhos bseado na flutuação de câmbio do mercado financeiro.Desta forma um usuário poderá opcionalmnente apenas simular qualquer valor de uma moeda estrangeira para BRL e vice-versa OU a partir de um cadastro na plataforma definir um perfil onde serão fornecidas informações como:Modelo de jornada (horas, dias, semanas, meses, anos) neste ponto o usuário determinará qual o valor a receber a cada hora, dia, semana, mês ou ano) apesar de esta variação ser rara nos moldes de trabalho e ganhos no Brasil, há modelos de contratação onde o trabalhador rece valor/hora ou valor/dia ou valor/semana etc.
Ex. escolha [HORAS] valor [25] moeda [USD] ou
escolha [Semana] valor [480] moeda [GBP] ou
escolha [Mês] valor [2900] moeda [EUR]
Etc...Desta maneira teremos um elemento para a base de cálculo.2.1. Escolher entre a opção de cálculo baseado em estimativa de tempo onde o usuário poderá definir uma meta de tempo de trabalho e assim gerar uma estimativa de ganho.Ex: 1
O usuário escolhe a modalidade de jornada por horas, define o valor da hora trabalhada, e estabelece que trabalhará 160 horas no período configurado (dia 1 (dia deve ser do dia atual para o futura - não retroativo) até dia N desde que N não seja uma data retroativa).
O sistema deverá calcular com base no valor da hora vezes o valor da moeda de origem e converter para BRL (Real Brasileiro);2.1. Escolher entre a opção de cálculo baseado em tempo já decorrido, onde o usuário disponibilizará com base no modelo de jornada escolhido, o sistema fará um calculo do que realmente já foi contabilizado, dando a oportuniodade de consolidar o valor trabalhado e gerar uma INVOICE com todos os dados e detalhes necessários.A Invoice será um elemento (entidade) que poderá ser armazenada no sistema junto a conta  do usuário, para fins de consulta, ajuste e exportação para arquivoA invoice deve conter um ID único, os dados do trabalhador (Nome, CNPJ ou CPF se for o caso), VAlores a receber, campo extra para definição de ganhos não previstos como bônus, horas extras, auxílios excepcionais, dados da empresa contratante, banco para wiretransfer etc, como no arquivo anexo (para conferência)
A Invoice é um artefato que poderá ser a qualquer momento consultado via sistema, no caso de mais de uma invoice armazenada, deve haver uma lógica de sort, deve existir a opção de editar, clonar, deletar e exportar (arquivos no formato PDF ou DOC, DOCX se form mais conveniente);O usuário deve ser capaz de gerenciar seu perfil dando-lhe a possibilidade de alterar seus dados, manipular seu perfil, alterar modalidade de jornada, simular evento de ganho sem vínculo com sua modalidade e visualizar graficamente a evolução de taxa cambial de moeda.Ex.:
https://economia.uol.com.br/cotacoes/cambio/ OU
https://www.bcb.gov.br/estatisticas/detalhamentoGrafico/graficosestatisticas/cambioTodo este escopo acima compreende um contexto inicial global para o MVP. A partir desta informações e de todo o histórico deste projeto, realize uma análise crítica rigorosa e realista, aponte os elementos e pontos de: incongruência, forte complexidade (possível inviabilizador), gaps técnicos/lógicos, considerações releventes.*** A partir desta análise realizarei uma revisão para seguirmos adiante com as definições e levantamento de requisitos fincionais e não funcionais.
```

## Análise Crítica Rigorosa do Escopo MVP Proposto

A definição do escopo MVP é, de fato, o ponto mais crítico do projeto, pois dita a fronteira entre o **viável** e o **inviável** dentro do prazo e recursos disponíveis (2 pessoas, ±3 meses efetivos, hardware modesto).

Realizei uma dissecação profunda do seu levantamento. Abaixo, apresento os achados objetivos, classificados por gravidade.

---

### 1. INCONGRUÊNCIAS (Contradições internas que precisam ser resolvidas)

| **Item**                                | **Incongruência Identificada**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Análise e Recomendação**                                                                                                                                                                                                                                                                                                     |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Item 9 vs. Item 1 (KISS)**            | **"Não devem ser adotados frameworks de desenvolvimento - Ex. Reactjs, Vue"** — Esta é a **maior incongruência** de todo o levantamento. Construir formulários dinâmicos (com condicionais de horas/dias), gráficos históricos, CRUD de invoices e autenticação com **JavaScript puro (Vanilla JS)** vai contra o princípio KISS. A manipulação direta do DOM, estado e roteamento em Vanilla JS gera código extremamente verboso, propenso a "spaguetti" e de difícil manutenção, especialmente para 2 pessoas em prazo curto. | **Recomendação:** Flexibilizar para uso de **bibliotecas reativas leves** (ex: **Alpine.js** ou **Petite-Vue**) ou frameworks compilados (**Svelte**), que reduzem drasticamente a complexidade do front-end sem o peso de um React/Vue. Se o receio for o _build step_, o Alpine.js resolve isso com CDN e zero configuração. |
| **Item 14 (Stack) vs. Item 6 (Docker)** | Para atingir "clean code" e "RESTful" com containers, é**impraticável** não usar um _microframework_ no back-end (ex: Flask/FastAPI para Python, Express para Node, Echo para Go, ou Laravel Slim para PHP). Implementar um servidor HTTP com roteamento, middleware e ORM do zero viola a premissa de "viabilidade de projeto".                                                                                                                                                                                                | **Recomendação:** Assumir que a restrição do Item 9 aplica-se **apenas ao Front-end (UI)**. Para o Back-end, adotar microframeworks consagrados e FOSS (ex: **FastAPI** - Python, que gera OpenAPI automaticamente, ou **Gin** - Go) é mandatório.                                                                             |

---

### 2. FORTE COMPLEXIDADE (Possíveis inviabilizadores)

| **Item**                                         | **Complexidade Identificada**                                                                                                                                                                                                                                                                    | **Impacto no MVP**                                                                                                                                                                                                                                                                           |
| :----------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gráfico de Evolução Cambial**                  | Exigir um gráfico histórico similar ao UOL/BCB (Item 4 - Visualizar graficamente) é um**módulo pesado**. Requer puxar séries históricas (ex: últimos 30/90 dias), tratar datas, e renderizar SVG/Canvas. Sem um framework de UI, isso vira um pesadelo de desenvolvimento.                       | **Risco ALTO.** Sugiro **postergar** para uma versão 2.0 ou, no máximo, implementar um gráfico estático usando bibliotecas FOSS como **Chart.js** (que, mesmo com Vanilla JS, ainda exige integração). No MVP, foque nos números e tabelas, deixando a evolução gráfica como _nice-to-have_. |
| **Geração de Invoice (PDF/DOCX)**                | Gerar um documento com layout complexo (endereço, tabelas, instruções bancárias) em PDF já é desafiador (exige libs como`pdfmake` ou `WeasyPrint`). Incluir **DOCX** como opção eleva a complexidade enormemente, pois a fidelidade de conversão entre DOCX e PDF é historicamente problemática. | **Recomendação:** MVP deve suportar **apenas PDF**. O DOCX pode ser gerado futuramente via bibliotecas específicas (ex: `python-docx`), mas demanda trabalho extra de template. Mantenha o foco no PDF.                                                                                      |
| **Cálculo Período (Data atual até Data futura)** | Determinar "dia 1 até dia N" considerando carga horária (ex: 160h no mês) exige uma máquina de estados complexa (dias úteis vs. corridos, feriados?). Se não houver um calendário corporativo configurado, o cálculo será impreciso.                                                             | **Recomendação:** Para o MVP, adotar o cálculo mais simplificado: **multiplicação direta** (valor_hora \* total_horas), sem descontar feriados ou fins de semana, a menos que o usuário inpute explicitamente os dias trabalhados.                                                           |

---

### 3. GAPS TÉCNICOS E LÓGICOS (Omissões que travam o desenvolvimento)

| **Gap**                                 | **Descrição**                                                                                                                                                                                                                                | **Solução Proposta**                                                                                                                                                                                                                                                                |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **API de Câmbio (Frankfurter vs. BCB)** | A Frankfurter tem**limite de 1000 requisições/dia** (plano gratuito). O BCB (Banco Central) é oficial e ilimitado, mas sua API exige tratamento de XML/JSON complexo e tem latência variável.                                                | **Estratégia:** MVP deve usar **Frankfurter** pela simplicidade, mas **implementar cache local** (em memória ou Redis via Docker) para armazenar a cotação diária por 5 minutos, reduzindo drasticamente o consumo de requisições. Reserve o BCB como fallback/documentação futura. |
| **Sistema de Autenticação e Perfil**    | O escopo menciona "cadastro na plataforma" e "gerenciar perfil", mas**não define** o fluxo de login (JWT? Sessão?). Isso impacta a camada de dados e segurança.                                                                              | **Definir:** Adotar autenticação stateless com **JWT** (gerado pelo back-end), com senhas hashadas (bcrypt). O Front-end enviará o token via Bearer. Isso é padrão RESTful.                                                                                                         |
| **CRUD de Invoices + Edição/Clone**     | Editar uma Invoice já emitida é um problema fiscal/contábil no mundo real (notas não se editam, se cancelam). O sistema permitirá edição livre ou com restrições?                                                                            | **Recomendação:** MVP deve permitir **edição apenas enquanto o status for "Rascunho"**. Após "Finalizada" ou "Exportada", a edição deve ser bloqueada (mas permitir "Clonar" para criar uma nova a partir daquela).                                                                 |
| **Isolamento de Camadas (Docker)**      | Item 6 exige separação Front/Back/Dados via Docker. OK. Mas o**Front-end Vanilla JS** rodando em container precisará ser servido por um servidor estático (Nginx/Apache) ou pelo próprio back-end (ex: FastAPI servindo arquivos estáticos). | **Definir:** Estruturar com `docker-compose.yml` contendo 3 serviços: `db` (PostgreSQL), `backend` (FastAPI + Uvicorn), e `frontend` (Nginx servindo os arquivos HTML/CSS/JS estáticos).                                                                                            |

---

### 4. CONSIDERAÇÕES RELEVANTES (Impacto na Equipe e Prazo)

1. **Equipe de 2 pessoas e Papéis:** Com 2 recursos, a divisão natural é **Front-end + DevOps** (um) e **Back-end + Banco de Dados** (outro). Isso exige definição rigorosa das interfaces (contratos REST) na primeira semana para evitar bloqueios mútuos.
2. **CI/CD (Item 13):** Implementar pipeline robusta (GitHub Actions) com testes automatizados e deploy em homologação **consome cerca de 1 a 2 semanas de setup**. Isso deve ser contabilizado no cronograma. Sugiro manter o CI focado em **Linter + Testes Unitários**, e o CD apenas para subir a stack em um ambiente de homologação (ex: Heroku ou VPS gratuita) no final do desenvolvimento.
3. **Clean Code e ACID:** Sem um framework back-end, garantir ACID em transações (ex: criar Invoice e atualizar saldo) é difícil. Com **FastAPI + SQLAlchemy** (Python), as transações são gerenciadas automaticamente, atendendo ACID sem esforço extra.
4. **Stack Sugerida (Viabilidade Máxima):**
   - **Front-end:** HTML + CSS + **Alpine.js** (reatividade leve) + **Chart.js** (gráficos, se mantido).
   - **Back-end:** **Python + FastAPI** (gera OpenAPI/Swagger automaticamente, facilitando o front-end).
   - **Banco:** **PostgreSQL** (robusto, ACID, FOSS).
   - **Containerização:** Docker Compose.

---

### 5. RESUMO EXECUTIVO DA ANÁLISE

| **Categoria**                   | **Parecer**                                                                                                                                                                                     |
| :------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Inviabilizador Imediato**     | A proibição de frameworks front-end (Item 9) com a exigência de UI complexa (gráficos, CRUD, formulários dinâmicos).**Sem flexibilização, o projeto não será entregue com qualidade no prazo.** |
| **Alta Complexidade (Cuidado)** | Geração de Invoice em múltiplos formatos (PDF/DOCX) e Gráficos históricos.**MVP deve restringir a PDF e gráficos simplificados.**                                                               |
| **Gaps a Preencher**            | Definir modelo de dados (entidades: Usuário, Perfil, Invoice, Configuração de Jornada). Definir fluxo de autenticação (JWT). Definir política de cache da API de câmbio.                        |
| **Totalmente Viável**           | Uso de Docker, CI/CD (básico), API RESTful, Banco Relacional, e metodologia Ágil/Kanban com GitHub Projects.                                                                                    |

---
