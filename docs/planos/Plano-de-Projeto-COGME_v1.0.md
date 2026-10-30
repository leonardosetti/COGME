# COGME — CONVERSOR DE GANHOS EM MOEDA ESTRANGEIRA
## Marco M1 (Entrega Parcial Documental)

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Instituição: Fatec Taquaritinga — Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas
Disciplina: Gerência de Projetos
Gerente de Projeto: Leonardo David Silva Setti
Equipe: Leonardo David Silva Setti, Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto
Abrangência: Áreas de Conhecimento 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade)

---

# INTRODUÇÃO — TERMO DE ABERTURA DO PROJETO

## Controle de Versões

| Versão | Data | Autores | Notas da Revisão |
| --- | --- | --- | --- |
| 1 | 24/08/2026 | Leonardo David Silva Setti, Fabricio de Lima Cabral | Sem revisões |
| 2 | 15/09/2026 | Leonardo David Silva Setti, Fabricio de Lima Cabral | Adesão, ajuste de mais um recurso de equipe: Edson Luis Silva |
| 3 | 18/09/2026 | Leonardo David Silva Setti | Reinterpretação de governança: Prof. Dr. Nivaldo Carleto redefinido como avaliador acadêmico nos marcos (sem ingerência operacional); GP consolidado como CCB de membro único; remoção de "Termo de Aceite assinado" em favor de "validação acadêmica". Alinhamento com Plano de Integração. |

## Objetivos deste documento

O presente Termo de Abertura do Projeto (TAP) tem como objetivos fundamentais:

a) Autorizar formalmente o projeto "Conversor de Ganhos em Moeda Estrangeira" (COGME), conferindo-lhe existência oficial perante a instituição de ensino (Fatec Taquaritinga) e perante o professor orientador da disciplina de Gerência de Projetos do Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas, Prof. Dr. Nivaldo Carleto.

b) Conceder autoridade formal ao aluno Leonardo David Silva Setti, no papel de gerente do projeto, para aplicar os recursos organizacionais, planejar as atividades, tomar decisões e mobilizar os recursos necessários à execução do projeto, em conjunto com os demais membros da equipe (Fabricio de Lima Cabral e Edson Luis Silva).

c) Estabelecer o vínculo entre o projeto e os objetivos estratégicos da disciplina, demonstrando que o desenvolvimento deste sistema atende aos requisitos acadêmicos de aplicação prática dos conceitos de gerenciamento de projetos conforme o Guia PMBOK® 7ª edição (governança primária, baseada em princípios e domínios de desempenho), com o Guia PMBOK® 6ª edição atuando como dicionário complementar de processos quando necessário, e a metodologia ágil Kanban como método de execução operacional via GitHub Projects.

d) Definir os limites preliminares do projeto, incluindo escopo de alto nível, premissas, restrições, riscos iniciais, cronograma de marcos e orçamento preliminar, servindo como base para o planejamento detalhado das áreas de conhecimento.

e) Identificar as principais partes interessadas (stakeholders) e seus papéis, alinhando expectativas e estabelecendo canais de comunicação iniciais.

f) Servir como documento de referência ao longo de todo o ciclo de vida do projeto, garantindo que todas as decisões e alterações sejam avaliadas à luz dos objetivos e restrições aqui estabelecidos.

## Situação atual e justificativa do projeto

**Situação Atual**

O cenário econômico e laboral contemporâneo tem sido profundamente transformado pela consolidação do trabalho remoto e pela globalização dos contratos de prestação de serviços. No Brasil, um contingente crescente de profissionais de tecnologia, design, marketing e consultoria atua como Pessoa Jurídica (PJ) ou freelancer para empresas sediadas nos Estados Unidos, Europa e demais mercados que remuneram em moeda estrangeira (predominantemente USD e EUR).

Entretanto, a gestão financeira desses ganhos apresenta uma complexidade que as ferramentas atualmente disponíveis no mercado não resolvem de maneira integrada. Para obter uma estimativa confiável do valor que efetivamente receberá em moeda nacional, o profissional é forçado a consultar múltiplos sites, planilhas manuais e calculadoras dispersas. Esse processo é moroso, suscetível a erros de digitação e de interpretação de taxas, além de não oferecer uma visão consolidada e comparativa em tempo real das diferentes variáveis que impactam a conversão.

O projeto "Conversor de Ganhos em Moeda Estrangeira" será desenvolvido desde o início.

**Justificativa e Ineditismo do Projeto**

O projeto "Conversor de Ganhos em Moeda Estrangeira" justifica-se, em primeiro plano, pela inegável lacuna prática existente no ecossistema de software atual: não há, até o momento, uma solução única, gratuita e de código aberto que reúna, em um mesmo ambiente, a simulação cambial completa, a comparação entre diferentes regimes de cálculo e a emissão de documentos fiscais/financeiros associados.

Além disso, o projeto possui ineditismo no âmbito acadêmico-aplicado. Diferentemente de abordagens puramente teóricas ou de sistemas de baixa complexidade (como CRUDs convencionais), este projeto aborda um domínio de negócio real — o mercado financeiro-cambial aliado ao trabalho remoto internacional — que exige rigor na gestão de requisitos, tratamento de dados dinâmicos e usabilidade centrada no usuário final. Essa complexidade oferece um campo fértil para a aplicação prática e aprofundada de todas as áreas de conhecimento do gerenciamento de projetos.

**Alinhamento com os Objetivos da Disciplina e da FATEC**

A proposta atende plenamente à premissa pedagógica da disciplina de Gerência de Projetos: aplicar na prática as dez áreas de conhecimento do PMBOK® 6ª edição (Integração, Escopo, Cronograma, Custo, Qualidade, Recursos, Comunicações, Riscos, Aquisições e Partes Interessadas) em um ciclo de vida completo de projeto. Ao desenvolver um sistema com requisitos funcionais e não funcionais claros, o aluno-gerente vivenciará situações reais de tomada de decisão, negociação de escopo, mitigação de riscos e garantia da qualidade, consolidando a aprendizagem significativa exigida pelo curso de Análise e Desenvolvimento de Sistemas da Fatec Taquaritinga.

**Compromisso com o Software Livre (FOSS) e o Impacto Social**

A determinação de utilizar exclusivamente tecnologias open source não é uma restrição técnica, mas sim um valor fundante do projeto, plenamente justificável pelos seguintes pilares:

1. Transparência e Auditabilidade: O usuário final e a comunidade técnica poderão verificar os procedimentos de cálculo, eliminando a desconfiança sobre "caixas-pretas" financeiras;
2. Gratuidade e Acessibilidade: Profissionais autônomos e Microempreendedores Individuais (MEIs), muitas vezes com recursos financeiros limitados, terão acesso a uma ferramenta profissional sem custos de licenciamento;
3. Sustentabilidade e Comunidade: O código aberto viabiliza que a comunidade de desenvolvedores e usuários contribua com melhorias e evoluções, perpetuando o projeto para além do ciclo acadêmico;
4. Alinhamento Institucional: A escolha é coerente com a filosofia da educação pública, gratuita e de qualidade, promovendo a disseminação do conhecimento e da tecnologia como bens comuns.

**Público-Alvo e Impacto Esperado**

O sistema destina-se a profissionais brasileiros que prestam serviços ao exterior (desenvolvedores, designers, tradutores, consultores, arquitetos, entre outros), bem como a pequenas agências que gerenciam contratos internacionais. O impacto direto esperado é o fortalecimento da autonomia financeira do usuário: ao dispor de simulações precisas e rápidas, ele poderá negociar contratos com base em dados concretos, planejar seus rendimentos em moeda nacional com maior segurança e reduzir as incertezas inerentes à volatilidade cambial, otimizando sua margem de ganho real.

## Objetivos SMART e critérios de sucesso do projeto

Esta seção estabelece os objetivos mensuráveis do projeto e os critérios formais que determinarão seu sucesso ou fracasso ao final do ciclo de vida. Todos os objetivos estão alinhados à premissa fundamental de desenvolvimento exclusivamente com tecnologias Open Source (FOSS) e à abordagem híbrida de governança declarada no item 1.c deste documento (PMBOK® 7ª edição como governança primária de princípios e domínios de desempenho, com o PMBOK® 6ª edição atuando como dicionário complementar de processos quando necessário).

**Tabela 1 — Objetivos SMART do Projeto**

| Categoria | Objetivo (Declaração SMART) | Componentes SMART |
| --- | --- | --- |
| Produto (Escopo) | Específico e Mensurável: Desenvolver e entregar um Minimum Viable Product (MVP) de um sistema web funcional que realize simulações de conversão de moeda estrangeira para moeda nacional, permitindo ao usuário configurar diferentes regimes de contratação (hora, dia, semana, mês e valor fixo), aplicar encargos financeiros simulados e emitir uma invoice em formato PDF. O sistema deverá processar as simulações em até 3 segundos. | S — Configuração de regimes e emissão de PDF; M — Tempo de resposta ≤ 3s; A — Responsável: Aluno-Gerente; R — Escopo viável para 3 pessoas; T — Entrega final até o término do 2º bimestre letivo (previsão: Novembro/2026). |
| Qualidade e Testes | Mensurável: O software entregue deverá apresentar, no mínimo, 80% de cobertura de código por testes automatizados (unitários e de integração) e deverá ser aprovado em um roteiro de testes de aceitação (User Acceptance Testing — UAT) que cubra 100% dos fluxos funcionais críticos (cálculo, configuração e geração de PDF), sem a presença de defeitos classificados como críticos ou bloqueantes. | S — Definição de métrica de cobertura; M — ≥ 80% de cobertura e zero defeitos críticos; A — Responsável: Aluno-Gerente; R — Factível com bibliotecas FOSS de teste; T — Verificado na entrega final (Novembro/2026). |
| Cronograma (Marcos) | Temporal: O projeto deverá obrigatoriamente cumprir dois marcos temporais principais: i) Entrega parcial da documentação do projeto (do TAP até o plano de Gerenciamento da Qualidade) até o dia 22 de setembro de 2026; ii) Entrega final do MVP funcional com sua respectiva documentação consolidada até o encerramento do 2º bimestre acadêmico (Novembro/2026). | S — Datas específicas; M — Verificação por entrega física/digital; A — Responsável: Aluno-Gerente; R — Prazos institucionais fixos; T — 22/09/2026 e Novembro/2026. |
| Métricas e Indicadores | Mensurável: Durante toda a execução, o gerente do projeto deverá coletar e divulgar semanalmente as métricas de fluxo Kanban — especificamente Cycle Time (tempo médio de um card do "In Progress" ao "Done"), Throughput (número de cards concluídos por semana) e Cumulative Flow Diagram (visualização de gargalos no fluxo) — por meio do GitHub Insights, garantindo a rastreabilidade do progresso conforme o Domínio de Medição do PMBOK® 7ª edição. Será estabelecido um período de calibração inicial (23/09 a 03/10/2026) para coleta de baseline antes da fixação de metas definitivas. | S — Métricas de fluxo Kanban (Cycle Time, Throughput, CFD) via GitHub Insights; M — Cycle Time médio ≤ 3 dias e Throughput ≥ 5 cards/semana (após calibração); CFD publicado semanalmente; A — Responsável: Aluno-Gerente; R — Métricas nativas do método Kanban; T — Durante todo o ciclo (Set a Nov/2026), com baseline estabelecida até 03/10/2026. |
| Inovação e Ferramentas | Atribuível e Realístico: Todo o ciclo de vida do projeto (gerenciamento, modelagem, desenvolvimento, testes e documentação) será conduzido exclusivamente com ferramentas de código aberto (FOSS). Ademais, o projeto deverá empregar Inteligência Artificial Generativa (LLMs) para auxiliar na redação dos artefatos e na implementação do código, adotando a abordagem Specification-Driven Development (SDD) para garantir que o código gerado esteja estritamente aderente às especificações funcionais previamente validadas. | S — FOSS e SDD com LLM; M — Verificação da licença de todas as ferramentas; A — Responsável: Aluno-Gerente; R — Ecossistema FOSS maduro; T — Aplicado do início ao fim do projeto. |

Fonte: Elaborado pelos autores (2026).

**Critérios de Sucesso do Projeto**

O projeto será formalmente considerado um SUCESSO se, e somente se, todos os critérios abaixo forem integralmente atendidos até a data de encerramento (Novembro/2026), conforme o Domínio de Entrega e o Domínio de Medição do PMBOK® 7ª edição:

a) Critério de Aceitação Final: O MVP entregue for validado academicamente pelo Prof. Dr. Nivaldo Carleto e pelos stakeholders representativos (usuários-piloto) em uma sessão de validação prática, demonstrando que a ferramenta resolve a dor da falta de integração nas simulações cambiais.

b) Critério de Conformidade (FOSS): 100% das ferramentas, bibliotecas e frameworks utilizados possuírem licenças reconhecidas pela Open Source Initiative (OSI), e a lista completa de dependências for documentada e auditável no repositório oficial do projeto.

c) Critério de Qualidade: O código-fonte entregue atingir o índice mínimo de 80% de cobertura de testes automatizados (unitários e de integração) e não apresentar defeitos de severidade crítica ou alta no ambiente de homologação, conforme verificado via pipeline CI e testes de aceitação (UAT).

d) Critério Documental: Todos os planos de gerenciamento das áreas de conhecimento (conforme PMBOK® 6ª edição, atuando como dicionário complementar) e todos os artefatos de requisitos forem entregues dentro do prazo estipulado (22/09/2026 para a parcela inicial — do TAP até o Plano de Gerenciamento da Qualidade — e Novembro/2026 para a entrega final), com o devido versionamento e rastreabilidade de alterações via GitHub.

e) Critério de Inovação Controlada: A utilização de IA Generativa para Specification-Driven Development (SDD) deve ser devidamente registrada, demonstrando que o código gerado foi revisado, testado e integrado ao repositório por meio de commits assinados pelo gerente-desenvolvedor, garantindo a propriedade intelectual e a conformidade ética com as políticas acadêmicas da Fatec Taquaritinga.

f) Critério de Métricas de Fluxo: As métricas de fluxo Kanban (Cycle Time, Throughput e Cumulative Flow Diagram) forem coletadas e divulgadas semanalmente via GitHub Insights, com período de calibração concluído até 03/10/2026 e metas realistas estabelecidas para o restante do projeto, conforme o Domínio de Medição do PMBOK® 7ª edição.

g) Critério de Cronograma: O marco M1 (Entrega Parcial Documental em 22/09/2026) for cumprido integralmente, e o marco M4 (Encerramento e Aceite Final em 15/12/2026) for atingido com a validação acadêmica formal pelo Prof. Dr. Nivaldo Carleto e o repositório com tag de release final.

Nota sobre usuários-piloto: Os stakeholders representativos serão selecionados entre colegas de curso e professores da Fatec Taquaritinga, em número limitado (3 a 5 pessoas), para validação de usabilidade e funcionalidade em ambiente acadêmico controlado. Esta amostra não reflete plenamente a diversidade do público-alvo real, conforme restrição documentada na seção de Restrições de Qualidade.

**Condições de Fracasso (Não Sucesso)**

O projeto será considerado não bem-sucedido caso, ao término do 2º bimestre letivo, ocorra qualquer uma das seguintes condições:

a) O MVP não esteja funcional em ambiente de homologação, impedindo a validação prática pelo Prof. Dr. Nivaldo Carleto.

b) Algum dos critérios de qualidade, conformidade, métricas de fluxo ou cronograma (itens b, c, f ou g dos critérios de sucesso) não seja atingido, sem justificativa formal aprovada via processo de gestão de mudanças.

c) Os marcos intermediários (especialmente o marco M1 de 22/09/2026) não forem cumpridos sem uma justificativa formal e aprovada por meio de solicitação de mudança registrada no GitHub (label change-request).

d) A cobertura de testes automatizados ficar abaixo de 70% (limiar mínimo aceitável, considerando a meta de 80%), comprometendo a confiabilidade do MVP entregue.

e) Mais de 30% das dependências do projeto possuírem licenças incompatíveis com FOSS (MIT, Apache 2.0, BSD, GPL), violando o Critério de Conformidade (item b).

## Estrutura Analítica do Projeto (EAP/WBS)

**NÍVEL 0 — RAIZ**

| ID | Nó | Descrição | Macro-Fase |
| --- | --- | --- | --- |
| N0 | — | COGME — Conversor de Ganhos em Moeda Estrangeira | — |

**NÍVEIS 1 E 2 — FASES OBRIGATÓRIAS (MVP Acadêmico)**

| ID Nível 1 | Fase (Nível 1) | ID Nível 2 | Pacote de Trabalho (Nível 2) | Macro-Fase |
| --- | --- | --- | --- | --- |
| N1 | 1. Iniciação e Planejamento | N1.1 | 1.1. Identificação de Stakeholders | MF1 |
| | | N1.2 | 1.2. Planos de Gerenciamento | MF1 |
| | | N1.3 | 1.3. Plano da Qualidade | MF1 |
| | | N1.4 | 1.4. Política de Licenciamento FOSS | MF1 |
| | | N1.5 | 1.5. Definição do Backlog e Kanban | MF1 |
| N2 | 2. Levantamento de Requisitos | N2.1 | 2.1. Requisitos Funcionais | MF1 |
| | | N2.2 | 2.2. Requisitos Não Funcionais | MF1 |
| | | N2.3 | 2.3. Casos de Uso e Histórias de Usuário | MF1 |
| N3 | 3. Modelagem e Prototipação | N3.1 | 3.1. Arquitetura da Solução | MF1 |
| | | N3.2 | 3.2. Protótipo UX/UI | MF1 |
| | | N3.3 | 3.3. Modelagem de Dados (DER) | MF1 |
| N4 | 4. Configuração de Ambiente | N4.1 | 4.1. Seleção e Validação da Stack FOSS | MF1 |
| | | N4.2 | 4.2. Repositório Git + CI/CD | MF1 |
| | | N4.3 | 4.3. Setup Local e Homologação | MF1 |
| | | N4.4 | 4.4. Auditoria de Licenças | MF1 |
| N5 | 5. Desenvolvimento do Sistema | N5.1 | 5.1. Backend — Lógica de Negócio | MF2 |
| | | N5.2 | 5.2. Backend — API de Câmbio + Cache | MF2 |
| | | N5.3 | 5.3. Frontend — Interface e Simulações | MF2 |
| | | N5.4 | 5.4. Módulo PDF (WeasyPrint) | MF2 |
| | | N5.5 | 5.5. SDD com IA (Prompts + Revisão) | MF2 |
| N6 | 6. Garantia da Qualidade | N6.1 | 6.1. Testes Unitários/Integração (≥ 80%) | MF2 |
| | | N6.2 | 6.2. Testes de Aceitação (UAT) | MF2 |
| | | N6.3 | 6.3. Aplicação de Ferramentas da Qualidade (12 PDCAs + Ishikawa 6M) | MF2 |
| N7 | 7. DevOps e CI/CD | N7.1 | 7.1. Pipeline CI (lint + testes) | MF2 |
| N8 | 8. Comunicação | N8.1 | 8.1. Matriz de Comunicação (RACI) | MF1 |
| | | N8.2 | 8.2. Canais Oficiais (GitHub, e-mail) | MF1 |
| N9 | 9. Base de Conhecimento | N9.1 | 9.1. ADRs (decisões arquiteturais) | MF1 |
| | | N9.2 | 9.2. Lições Aprendidas Contínuas | MF1 |
| | | N9.3 | 9.3. Catálogo de Prompts SDD | MF1 |
| N10 | 10. Gestão de Mudanças | N10.1 | 10.1. Registro de Solicitações de Mudança | MF2 |
| | | N10.2 | 10.2. Label change-request no GitHub | MF2 |
| | | N10.3 | 10.3. Aprovação e Versionamento | MF2 |
| N11 | 11. Documentação do Projeto | N11.1 | 11.1. Documentação Técnica (Arquitetura, APIs) | MF3 |
| | | N11.2 | 11.2. Consolidação da Documentação Parcial | MF3 |
| N12 | 12. Encerramento | N12.1 | 12.1. Lições Aprendidas Finais | MF3 |
| | | N12.2 | 12.2. Verificação SMART | MF3 |
| | | N12.3 | 12.3. Apresentação Final + Aceite | MF3 |

Fonte: Elaborado pelos autores (2026). TOTAL: 12 fases Nível 1 + 37 pacotes Nível 2.

**Lista Hierárquica Aninhada**

~~~
N0: COGME — Conversor de Ganhos em Moeda Estrangeira
 │
 ├── N1: 1. Iniciação e Planejamento [MF1]
 │   ├── N1.1: Identificação de Stakeholders
 │   ├── N1.2: Planos de Gerenciamento
 │   ├── N1.3: Plano da Qualidade
 │   ├── N1.4: Política de Licenciamento FOSS
 │   └── N1.5: Definição do Backlog e Kanban
 │
 ├── N2: 2. Levantamento de Requisitos [MF1]
 │   ├── N2.1: Requisitos Funcionais
 │   ├── N2.2: Requisitos Não Funcionais
 │   └── N2.3: Casos de Uso e Histórias de Usuário
 │
 ├── N3: 3. Modelagem e Prototipação [MF1]
 │   ├── N3.1: Arquitetura da Solução
 │   ├── N3.2: Protótipo UX/UI
 │   └── N3.3: Modelagem de Dados (DER)
 │
 ├── N4: 4. Configuração de Ambiente [MF1]
 │   ├── N4.1: Seleção e Validação da Stack FOSS
 │   ├── N4.2: Repositório Git + CI/CD
 │   ├── N4.3: Setup Local e Homologação
 │   └── N4.4: Auditoria de Licenças
 │
 ├── N5: 5. Desenvolvimento do Sistema [MF2]
 │   ├── N5.1: Backend — Lógica de Negócio
 │   ├── N5.2: Backend — API de Câmbio + Cache
 │   ├── N5.3: Frontend — Interface e Simulações
 │   ├── N5.4: Módulo PDF (WeasyPrint)
 │   └── N5.5: SDD com IA (Prompts + Revisão)
 │
 ├── N6: 6. Garantia da Qualidade [MF2]
 │   ├── N6.1: Testes Unitários/Integração (≥ 80%)
 │   ├── N6.2: Testes de Aceitação (UAT)
 │   └── N6.3: Aplicação de Ferramentas da Qualidade
 │
 ├── N7: 7. DevOps e CI/CD [MF2]
 │   └── N7.1: Pipeline CI (lint + testes)
 │
 ├── N8: 8. Comunicação [MF1]
 │   ├── N8.1: Matriz de Comunicação (RACI)
 │   └── N8.2: Canais Oficiais (GitHub, e-mail)
 │
 ├── N9: 9. Base de Conhecimento [MF1]
 │   ├── N9.1: ADRs (decisões arquiteturais)
 │   ├── N9.2: Lições Aprendidas Contínuas
 │   └── N9.3: Catálogo de Prompts SDD
 │
 ├── N10: 10. Gestão de Mudanças [MF2]
 │   ├── N10.1: Registro de Solicitações de Mudança
 │   ├── N10.2: Label change-request no GitHub
 │   └── N10.3: Aprovação e Versionamento
 │
 ├── N11: 11. Documentação do Projeto [MF3]
 │   ├── N11.1: Documentação Técnica (Arquitetura, APIs)
 │   └── N11.2: Consolidação da Documentação Parcial
 │
 └── N12: 12. Encerramento [MF3]
     ├── N12.1: Lições Aprendidas Finais
     ├── N12.2: Verificação SMART
     └── N12.3: Apresentação Final + Aceite
~~~

**Declaração de Rastreabilidade (TAP → EAP)**

| Origem (TAP) | Destino (EAP) | Domínio PMBOK 7ª |
| --- | --- | --- |
| §3 Objetivos SMART (Produto) | Fases 5, 6, 7 (MVP funcional + qualidade + CI) | Entrega |
| §3 Objetivos SMART (Qualidade) | Fases 6 (testes + ferramentas qualidade), 11, 12 | Medição |
| §3 Objetivos SMART (Cronograma) | Macro-fases MF1/MF2/MF3 | Abordagem de Desenvolvimento |
| §3 Objetivos SMART (Inovação) | Fases 5.5, 9.3 (SDD com IA) | Trabalho do Projeto |
| Escopo (implícito) | Todas as 12 fases obrigatórias | Planejamento |
| Restrições (FOSS) | Fases 1.4, 4.1, 4.4 | Abordagem de Desenvolvimento |
| Premissas (LLM/SDD) | Fases 5.5, 9.3 | Trabalho do Projeto |
| Riscos | Fase 10 (Gestão de Mudanças) | Incerteza |

Verificação de completude: 100% dos objetivos SMART possuem ao menos uma fase da EAP associada.

Figura 1 — Estrutura Analítica do Projeto (EAP) — Visão Macro e Macro-Fases

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-eap-nivel-0-macro.svg]**

Nota: Representação da linha de base estrutural do escopo, canônica conforme o TAP. O diagrama fracionado em camadas substitui a EAP tradicional de página única, que sofreria com sobreposições e ilegibilidade devido aos 12 níveis de fase e 37 pacotes de trabalho. A visualização hierárquica agrupa os pacotes nas três Macro-Fases (MF1: Fundação, MF2: Construção, MF3: Consolidação), garantindo rastreabilidade imediata entre a raiz do projeto (N0) e os entregáveis de valor.
Fonte: Elaborado pelos autores (2026).

Figura 2 — Detalhamento da Macro-Fase 1 (MF1) — Fundação

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-eap-mf1-fundacao.svg]**

Nota: Decomposição dos pacotes de trabalho de Nível 2 referentes à iniciação, planejamento, levantamento de requisitos, modelagem, configuração de ambiente, comunicação e base de conhecimento. Esta camada sustenta os entregáveis do Marco M1 (22/09/2026), incluindo os 5 planos de gerenciamento iniciais e a configuração do SSOT (GitHub Projects), em conformidade com o Domínio de Planejamento do PMBOK® 7ª edição.
Fonte: Elaborado pelos autores (2026).

Figura 3 — Detalhamento da Macro-Fase 2 (MF2) — Construção

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-eap-mf2-construcao.svg]**

Nota: Decomposição dos pacotes de trabalho focados na execução técnica: desenvolvimento do sistema (incluindo SDD com IA), garantia da qualidade (meta de coverage ≥ 80%), DevOps/CI/CD e gestão de mudanças. Esta camada materializa o Domínio de Entrega e sustenta o Marco M3 (15/11/2026), onde o MVP funcional deve estar operacional e validado em UAT.
Fonte: Elaborado pelos autores (2026).

Figura 4 — Detalhamento da Macro-Fase 3 (MF3) — Consolidação

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-eap-mf3-consolidacao.svg]**

Nota: Decomposição dos pacotes de trabalho finais, abrangendo a consolidação da documentação técnica e o encerramento formal do projeto. Esta camada garante a rastreabilidade dos critérios de aceite do Marco M4 (15/12/2026), incluindo a verificação SMART e a validação acadêmica final, alinhada ao Domínio de Entrega do PMBOK® 7ª edição.
Fonte: Elaborado pelos autores (2026).

Figura 5 — Estrutura Analítica do Projeto (EAP) — Visão Executiva Consolidada

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-01-eap-executiva.svg]**

Nota: A representação visual da EAP em visão executiva materializa o Processo 5.4 (Criar EAP/WBS) do PMBOK® 6ª edição (dicionário) e o Domínio de Planejamento do PMBOK® 7ª edição. A estrutura hierárquica apresenta a raiz N0 (COGME) no topo, decomposta em 12 fases de Nível 1 (N1 a N12) agrupadas em três Macro-Fases temporais: MF1 — Fundação (6 fases, 20 pacotes), MF2 — Construção (4 fases, 12 pacotes) e MF3 — Consolidação (2 fases, 5 pacotes), totalizando 37 pacotes de trabalho de Nível 2, conforme a baseline canônica aprovada. A opção pela não abertura dos 37 pacotes nesta visão executiva preserva a legibilidade em documentos A4 e evita poluição visual, em conformidade com o princípio de Governança Mínima Viável (GMV).
Fonte: Elaborado pelos autores (2026).

## Principais requisitos das principais entregas/produtos

Esta seção documenta os requisitos fundamentais dos produtos e entregas identificados na Estrutura Analítica do Projeto (EAP), conforme o Processo 5.2 (Coletar Requisitos) do PMBOK® 6ª edição e o Domínio de Entrega do PMBOK® 7ª edição. Cada requisito é mensurável, rastreável aos Objetivos SMART e vinculado a um pacote de trabalho específico da EAP.

Regra de consistência: Todo requisito deve possuir critério de aceite quantificável, rastreabilidade ao Objetivo SMART do TAP, mapeamento ao pacote da EAP e domínio PMBOK 7ª associado.

**Tabela 2 — Requisitos Principais das Entregas**

| ID | Requisito | Critério de Aceite | Rastreabilidade |
| --- | --- | --- | --- |
| REQ-01 | Simulação de conversão cambial em tempo real (USD/EUR → BRL) | Cotação obtida via API externa com latência ≤ 2s | Produto + N5.2 |
| REQ-02 | Suporte a 5 regimes de contratação (hora, dia, semana, mês, valor fixo) | 100% dos regimes operacionais em UAT | Produto + N5.1 |
| REQ-03 | Aplicação de encargos financeiros simulados (spread + IOF) | Cálculo auditável com precisão de 2 casas decimais | Produto + N5.1 |
| REQ-04 | Emissão de invoice em formato PDF | Geração via WeasyPrint em ≤ 3s por documento | Produto + N5.4 |
| REQ-05 | Tempo de resposta da aplicação | ≤ 3s em 95% das requisições (ambiente homologação) | Produto + N5.1 |
| REQ-06 | Interface web responsiva (FOSS) | Compatível com Chrome/Firefox/Edge (últimas 2 versões) | Inovação + N5.3 |
| REQ-07 | Cache de cotações (SQLite) | Redução de ≥ 50% das chamadas à API externa | Decisão arquitetural + N5.2 |
| REQ-08 | Cobertura de testes automatizados | ≥ 80% do código (unitários + integração via pytest + coverage.py) | Qualidade + N6.1 |
| REQ-09 | Testes de aceitação (UAT) | 100% dos fluxos críticos passing, zero defeitos críticos/bloqueantes | Qualidade + N6.2 |
| REQ-10 | Aplicação de ferramentas da qualidade (PDCA + Ishikawa 6M) | 12 PDCAs consolidados + diagrama de causa e efeito documentado no Plano de Qualidade | Qualidade + N6.3 |
| REQ-11 | Pipeline CI funcional | Lint + testes rodando em ≤ 5 min por push | Integração contínua + N7.1 |
| REQ-12 | ADRs para decisões arquiteturais críticas | Mínimo 3 ADRs registrados (stack, Kanban, métricas) | Documentação técnica + N9.1 |
| REQ-13 | Rastreabilidade de prompts SDD | 100% dos prompts catalogados em .ai/handoffs/ | Rastreabilidade de prompts + N9.3 |
| REQ-14 | Documentação técnica consolidada | Arquitetura + APIs (OpenAPI) revisadas e aprovadas | Produto + N11.1 |
| REQ-15 | Licenciamento 100% FOSS | Todas dependências com licenças OSI-approved (MIT, Apache 2.0, BSD, GPL) | Inovação + N1.5 + N4.4 |

Fonte: Elaborado pelos autores (2026).

**Matriz de Rastreabilidade Consolidada (Objetivos SMART → EAP → Requisitos)**

| Objetivo SMART | Fases EAP Associadas | Requisitos Cobertos | Domínio PMBOK 7ª |
| --- | --- | --- | --- |
| Produto (Escopo) — MVP funcional com simulação cambial, 5 regimes, invoice PDF, ≤ 3s | N5 (Desenvolvimento) | REQ-01 a REQ-07 | Entrega |
| Qualidade e Testes — ≥ 80% coverage, UAT 100% fluxos críticos, zero defeitos críticos | N6 (Garantia da Qualidade) | REQ-08, REQ-09, REQ-10 | Medição |
| Cronograma (Marcos) — 22/09 (parcial) + Nov/2026 (final) | Macro-fases MF1/MF2/MF3 | Todos (indiretamente) | Abordagem de Desenvolvimento |
| Métricas e Indicadores — Cycle Time + Throughput via GitHub Insights | N7 (DevOps) + N9 (Base de Conhecimento) | REQ-11 | Medição |
| Inovação e Ferramentas — FOSS + SDD com IA auditável | N1.5, N4.4, N5.5, N9.1, N9.3 | REQ-12, REQ-13, REQ-15 | Trabalho do Projeto |

Fonte: Elaborado pelos autores (2026). Verificação de completude: 100% dos Objetivos SMART possuem ao menos um requisito associado.

## Marcos

Esta seção define os pontos de verificação temporal críticos (milestones) do projeto COGME, conforme o Processo 6.5 (Desenvolver o Cronograma) do PMBOK® 6ª edição e o Domínio de Medição do PMBOK® 7ª edição. Os marcos estão diretamente vinculados às Macro-Fases (MF) da Estrutura Analítica do Projeto (EAP) e servem como gatilhos para entregas de valor e validação pelo stakeholder.

Regra de consistência: Todo marco deve possuir data alvo realista, descrição clara do entregável de valor, vínculo com a Macro-Fase da EAP e critério de aceite objetivo.

**Tabela 3 — Marcos Principais**

| ID | Macro-Fase (EAP) | Descrição do Marco (Entrega de Valor) | Data Alvo | Critério de Aceite |
| --- | --- | --- | --- | --- |
| M1 | MF1: Fundação | Entrega Parcial Documental: Aprovação do TAP + Planos de Gerenciamento das Áreas 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade) + 12 PDCAs consolidados + Diagrama de Ishikawa. | 22/09/2026 | Documentação submetida via GitHub e validada pelo Prof. Dr. Nivaldo Carleto sem achados críticos. |
| M2 | MF1: Fundação | Ambiente e Modelagem Concluídos: Stack FOSS definida e validada, ambiente local/CI configurado, DER e Protótipo UX/UI aprovados. | 30/09/2026 | Pipeline CI "verde" e artefatos de modelagem versionados no repositório. |
| M3 | MF2: Construção | MVP Funcional (Beta): Código-fonte full-stack operacional (Backend, Frontend, PDF, SDD com IA), com cobertura de testes ≥ 80% e validado em UAT local. | 15/11/2026 | Zero defeitos críticos/bloqueantes; métricas de fluxo (Cycle Time/Throughput) dentro da baseline. |
| M4 | MF3: Consolidação | Encerramento e Aceite Final: Documentação técnica consolidada, lições aprendidas, verificação dos critérios SMART e apresentação final com aceite formal. | 15/12/2026 | Validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4 e repositório com tag de release final. |

Fonte: Elaborado pelos autores (2026).

**Premissas Temporais e Riscos Associados**

1. Janela de Entrega Parcial: O marco M1 (22/09/2026) é inegociável para fins de avaliação acadêmica intermediária. Qualquer desvio superior a 3 dias úteis acionará o processo de Gestão de Mudanças (Fase N10 da EAP).
2. Paralelismo via Kanban: As datas representam o target de conclusão da Macro-Fase. Dentro de cada MF, as fases da EAP não são estritamente sequenciais; o paralelismo é gerenciado via pull system e WIP limits no GitHub Projects.
3. Risco de Atraso (R1 e R8): A sobrecarga da equipe ou a indefinição da stack podem impactar os marcos M2 e M3. A mitigação depende da aplicação rigorosa do princípio de Governança Mínima Viável (GMV) e do fallback para modelos LLM mais leves (Qwen 14B) se necessário.

**Declaração de Rastreabilidade (Marcos → EAP → Objetivos SMART)**

| Marco | Fases da EAP Abrangidas | Objetivo SMART Atendido |
| --- | --- | --- |
| M1 | N1, N2, N3, N4, N9, N10 (parcial) | Cronograma (Marcos) e Inovação (FOSS/SDD) |
| M2 | N4 (conclusão), N3 (conclusão) | Produto (Escopo) e Inovação (Ferramentas) |
| M3 | N5, N6, N7 | Produto (Escopo) e Qualidade e Testes |
| M4 | N11, N12 | Qualidade e Testes e Cronograma (Marcos) |

Fonte: Elaborado pelos autores (2026).

Figura 6 — Roadmap Macro do Cronograma (Macro-Fases e Marcos)

**[PLACEHOLDER — IMAGEM: docs/diagramas/cronograma/fig-02-roadmap-macro.svg]**

Nota: Representação temporal de nível macro com três faixas horizontais — MF1 (01/09–30/09), MF2 (01/10–15/11) e MF3 (16/11–15/12) — e cinco marcadores de milestone (M1, M2, Calibração, M3, M4), com a Calibração graficamente distinguida como auxiliar. Constitui a única representação tipo Gantt admitida, restrita ao nível macro e derivada do SSOT (OKB); o nível operacional é regido por fluxo contínuo Kanban (ADR-002).
Fonte: Elaborado pelos autores (2026).

## Partes interessadas do projeto

**Tabela 4 — Partes Interessadas**

| Empresa | Participante | Função |
| --- | --- | --- |
| FATEC | Prof. Dr. Nivaldo Carleto | Avaliador Acadêmico (Cliente simulado) |
| COGME | Leonardo David Silva Setti, Fabricio de Lima Cabral, Edson Luis Silva | Desenvolvedores do projeto |

Fonte: Elaborado pelos autores (2026).

## Restrições

**Contexto Aplicado**

O presente projeto está sujeito a um conjunto de limitações concretas que condicionam sua execução, decorrentes de seu ambiente acadêmico, da infraestrutura disponível e das premissas tecnológicas adotadas. Estas restrições não podem ser desconsideradas ou violadas sob pena de inviabilização parcial ou total do empreendimento. Elas atuam como parâmetros fixos dentro dos quais a equipe deve planejar, executar e monitorar todas as atividades, exigindo uma gestão de escopo rigorosa, priorização constante e tomada de decisão orientada à mitigação de impactos. A seguir, as restrições são detalhadas conforme as categorias fundamentais do PMBOK® 6ª edição, aplicadas diretamente à realidade do projeto.

**Tabela 5 — Restrições de Escopo**

| Restrição | Descrição e Impacto |
| --- | --- |
| Escopo restrito ao MVP | O projeto entregará um Produto Mínimo Viável (MVP) em regime acadêmico. Funcionalidades não essenciais (ex: múltiplas plataformas de transferência, cadastro de múltiplos usuários, relatórios gerenciais avançados) ficarão para versões futuras, salvo aprovação formal em mudança de escopo. |
| Desenvolvimento do zero | Não haverá reaproveitamento de código ou sistemas legados. Toda a construção ocorrerá a partir de requisitos originais, demandando esforço integral de modelagem, codificação e testes no período letivo. |

Fonte: Elaborado pelos autores (2026).

**Tabela 6 — Restrições de Cronograma**

| Restrição | Descrição e Impacto |
| --- | --- |
| Prazo letivo inegociável | Dois bimestres acadêmicos, com marco intermediário obrigatório em 22/09/2026 (entrega documental até o plano de Gerenciamento da Qualidade). Cerca de 25% do tempo total já transcorreu, restando aproximadamente 3 meses para execução plena. |
| Disponibilidade reduzida | O curso é noturno, limitando a carga horária semanal dedicada ao projeto. A equipe (3 pessoas) concilia as atividades com outras disciplinas e compromissos profissionais, exigindo planejamento granular e produtividade otimizada. |

Fonte: Elaborado pelos autores (2026).

**Tabela 7 — Restrições de Custo (Orçamento)**

| Restrição | Descrição e Impacto |
| --- | --- |
| Orçamento nulo | Não há verba institucional ou patrocínio. Todos os custos operacionais (hospedagem, ferramentas, serviços) serão absorvidos pela equipe ou obtidos via planos gratuitos. |
| Proibição de aquisições pagas | Nenhuma ferramenta, biblioteca ou serviço oneroso poderá ser utilizado. A seleção da stack tecnológica fica restrita a soluções gratuitas e de código aberto (FOSS) ou com planos gratuitos suficientes para o escopo acadêmico. |

Fonte: Elaborado pelos autores (2026).

**Tabela 8 — Restrições de Recursos (Peopleware)**

| Restrição | Descrição e Impacto |
| --- | --- |
| Equipe reduzida (3 pessoas) | A equipe é composta por apenas três membros, que acumularão múltiplos papéis: gerência, análise, desenvolvimento, testes, documentação e DevOps. A paralelização é limitada e a dependência de cada membro é alta. |
| Hardware modesto | Os equipamentos pessoais dos integrantes possuem capacidade computacional limitada, impactando tempos de build, execução de testes pesados e simulações. |
| Dependência de serviços externos gratuitos | APIs de câmbio e hospedagem dependem de provedores terceiros sem garantia de estabilidade, disponibilidade ou continuidade, sujeitos a limites de requisição e mudanças em suas políticas. |

Fonte: Elaborado pelos autores (2026).

**Tabela 9 — Restrições de Qualidade**

| Restrição | Descrição e Impacto |
| --- | --- |
| Tempo restrito para testes | Com prazo reduzido, os testes deverão ser priorizados nos fluxos críticos (cálculo de câmbio, configuração de regimes, geração de PDF). A meta de 80% de cobertura é desafiadora, mas factível com uso de ferramentas automatizadas FOSS. |
| Ambiente de validação acadêmico | Os testes de aceitação e usabilidade serão conduzidos com um número limitado de usuários-piloto (colegas e professores), não refletindo plenamente a diversidade do público-alvo real. |

Fonte: Elaborado pelos autores (2026).

**Tabela 10 — Restrições de Riscos**

| Restrição | Descrição e Impacto |
| --- | --- |
| Sem contingência formal | A equipe não dispõe de recursos extras (financeiros, humanos ou tecnológicos) para planos de contingência estruturados. A gestão de riscos dependerá de ações preventivas e adaptações rápidas. |
| Dependência crítica de APIs gratuitas | O consumo de cotação cambial em tempo real é função central; a eventual indisponibilidade ou limitação da API escolhida pode bloquear o MVP. |

Fonte: Elaborado pelos autores (2026).

**Tabela 11 — Restrições Tecnológicas e Operacionais**

| Restrição | Descrição e Impacto |
| --- | --- |
| Stack exclusivamente FOSS/gratuita | Todo o ciclo de vida (gerenciamento, desenvolvimento, testes, documentação, CI/CD, hospedagem) utilizará ferramentas gratuitas, preferencialmente open source. Isso restringe o leque de opções e exige pesquisa de compatibilidade. |
| Abordagem experimental (SDD com IA) | O uso de Specification-Driven Development com suporte de LLMs é inovador e não garantido. Os artefatos gerados por IA demandam revisão humana rigorosa, sob risco de erros lógicos ou de segurança. |
| Licenciamento do produto final | O software entregue deverá ser licenciado como open source (ex: MIT, GPLv3), condição imposta pelo uso de ferramentas FOSS e pelo caráter acadêmico, restringindo futura comercialização. |

Fonte: Elaborado pelos autores (2026).

**Tabela 12 — Síntese Consolidada das Restrições**

| Categoria PMBOK | Restrições Aplicáveis |
| --- | --- |
| Escopo | MVP acadêmico; desenvolvimento do zero |
| Cronograma | 2 bimestres (com ≈ 25% já decorrido); marco 22/09/2026; curso noturno |
| Custo | Orçamento zero; proibição de ferramentas pagas |
| Recursos | Equipe de 3 pessoas (múltiplos papéis); hardware modesto; dependência externa |
| Qualidade | Testes com tempo limitado; ambiente de validação restrito |
| Riscos | Sem plano de contingência formal; APIs gratuitas instáveis |
| Tecnológicas | FOSS/gratuito obrigatório; SDD experimental; licença open source final |

Fonte: Elaborado pelos autores (2026).

## Premissas

Esta seção documenta os fatores considerados verdadeiros, reais ou certos para fins de planejamento do projeto COGME, conforme o Processo 4.1 (Desenvolver o Termo de Abertura do Projeto) do PMBOK®. Premissas são declarações de alto nível que, caso se provem falsas durante a execução, exigirão reavaliação imediata do escopo, cronograma ou custos do projeto, podendo acionar o processo formal de gestão de mudanças.

**Tabela 13 — Premissas Estratégicas e Operacionais Fundamentais**

| # | Premissa | Justificativa de Alto Nível | Impacto se Invalidada |
| --- | --- | --- | --- |
| P1 | A governança do projeto seguirá o modelo híbrido: PMBOK 7ª como base de princípios e domínios, com PMBOK 6ª atuando como dicionário de processos complementares, e Kanban como método de execução. | Alinhamento com as diretrizes acadêmicas da disciplina e necessidade de adaptação a equipes enxutas. | Exigência de retrabalho massivo na documentação para adequação a um modelo puramente preditivo (cascata), inviabilizando o prazo. |
| P2 | O projeto será desenvolvido e entregue utilizando exclusivamente tecnologias de Software Livre e Código Aberto (FOSS). | Premissa pedagógica e de valor social, garantindo auditabilidade, gratuidade e sustentabilidade do artefato final. | Necessidade de aquisição de licenças, violando a restrição de orçamento zero e inviabilizando a entrega. |
| P3 | O uso de Inteligência Artificial Generativa (LLMs) como ferramenta de apoio ao desenvolvimento (SDD) é autorizado e esperado, desde que com rastreabilidade e revisão humana. | Reconhecimento das diretrizes acadêmicas atuais que permitem o uso ético e auditável de IA para potencializar a produtividade. | Perda de produtividade da equipe e necessidade de reescrita manual de artefatos e código, comprometendo o cronograma. |
| P4 | O código-fonte funcional (MVP full-stack) constitui um deliverable formal e parte integrante da documentação de sucesso do projeto, não apenas os artefatos textuais. | Alinhamento com a natureza prática do curso de Análise e Desenvolvimento de Sistemas. | O projeto seria considerado incompleto academicamente, mesmo com toda a documentação de gerenciamento perfeita. |
| P5 | A equipe do projeto (3 membros) manterá uma disponibilidade média de até 20 horas semanais dedicadas ao projeto, conciliando com as demais atividades acadêmicas. | Capacidade realística de alocação de recursos humanos para um projeto acadêmico noturno. | Atraso crônico nas entregas, burnout da equipe e necessidade de redução drástica do escopo do MVP. |
| P6 | O hardware local disponível para a equipe é adequado e suficiente para as tarefas de desenvolvimento, modelagem, testes e execução do MVP em ambiente local. | Condição base para que o desenvolvimento ocorra sem dependência de infraestrutura de nuvem paga. | Necessidade de migrar para ambientes de desenvolvimento em nuvem, gerando custos não previstos ou inviabilizando o trabalho. |
| P7 | O Professor Orientador atua como stakeholder-avaliador único nos marcos de entrega (M1 a M4), sem ingerência em decisões operacionais diárias. A autoridade de aprovação de mudanças (CCB) é delegada ao Gerente de Projeto. | Premissa de simplificação pedagógica e autonomia do GP, focando o esforço de gerenciamento no valor entregue e evitando gargalos de decisão incompatíveis com o prazo acadêmico. | Necessidade de envolver o avaliador em decisões operacionais, gerando gargalo e comprometendo a autonomia do GP. |
| P8 | As áreas de conhecimento de "Aquisições" e "Gerenciamento das Partes Interessadas" serão tratadas com simplificação pedagógica, conforme permitido pelo escopo acadêmico. | Foco do projeto nas 8 áreas de conhecimento restantes, otimizando o tempo da equipe para o desenvolvimento do produto. | Exigência de planos de aquisição complexos para um projeto de orçamento zero, desviando o foco do produto. |

Fonte: Elaborado pelos autores (2026).

**Declaração de Rastreabilidade das Premissas**

| Premissa | Domínio de Desempenho (PMBOK 7ª) | Artefato de Detalhamento (Pós-TAP) |
| --- | --- | --- |
| P1, P7, P8 | Abordagem de Desenvolvimento / Stakeholders | Plano de Integração (Papéis de Governança e Autoridade de Mudança) / Plano de Comunicações |
| P2, P6 | Abordagem de Desenvolvimento / Recursos | Plano de Recursos Tecnológicos |
| P3, P4 | Trabalho do Projeto / Entrega | Base de Conhecimento (ADRs e Prompts) |
| P5 | Equipe | Plano de Recursos (RACI simplificado) |

Fonte: Elaborado pelos autores (2026).

## Riscos

Esta seção documenta os principais riscos de alto nível identificados no projeto COGME, conforme o Processo 11.1 (Identificar Riscos) do PMBOK® 6ª edição e o Domínio de Incerteza do PMBOK® 7ª edição. Riscos são eventos ou condições incertas que, caso ocorram, podem impactar positiva ou negativamente os objetivos do projeto. Esta seção apresenta uma visão estratégica dos riscos; o detalhamento operacional (matriz completa, planos de contingência, gatilhos de resposta) será tratado no Plano de Riscos.

Regra de consistência: Todo risco deve possuir descrição clara do evento incerto, probabilidade e impacto estimados, severidade consolidada, estratégia de resposta de alto nível e rastreabilidade aos Objetivos SMART.

**Tabela 14 — Principais Riscos de Alto Nível**

| ID | Risco | Probabilidade | Impacto | Severidade | Estratégia de Resposta |
| --- | --- | --- | --- | --- | --- |
| R1 | Entrega parcial (22/09/2026) não concluída no prazo, comprometendo o marco de avaliação acadêmica e a transição para a MF2 (Construção). | Média (40%) | Alto | ALTA | Mitigar: Aplicar princípio GMV (governança mínima viável) para priorizar artefatos obrigatórios; monitorar progresso semanalmente via GitHub Projects; acionar plano de contingência (redução de escopo não-crítico) se desvio > 15%. |
| R2 | Stack tecnológica FOSS selecionada apresentar instabilidade, incompatibilidade ou curva de aprendizado superior ao previsto, impactando a Fase N5 (Desenvolvimento do Sistema) e o cronograma da MF2. | Baixa (25%) | Alto | ALTA | Mitigar: Validar stack com protótipo "Hello World" antes da Fase N5 (Fase N4.1); manter alternativas FOSS equivalentes identificadas; documentar decisão em registro formal de arquitetura. |
| R3 | Sobrecarga da equipe (burnout) devido à acumulação de múltiplos papéis (gerência, desenvolvimento, testes, documentação) e conciliação com outras disciplinas, resultando em queda de produtividade ou afastamento temporário. | Média (50%) | Médio | ALTA | Mitigar: Respeitar limite de 20h/semana por membro (Domínio de Equipe PMBOK 7ª); aplicar WIP limits no Kanban (máx. 3 cards em progresso por pessoa); monitorar métrica de burnout via self-report semanal. |
| R4 | Cobertura de testes automatizados ficar abaixo da meta de 80%, comprometendo o Critério de Qualidade e a confiabilidade do MVP entregue. | Média (45%) | Alto | ALTA | Mitigar: Adotar abordagem TDD (Test-Driven Development) desde a Fase N5; integrar pipeline CI (Fase N7.1) com verificação automática de coverage; priorizar testes nos fluxos críticos (cálculo cambial, geração de PDF). |
| R5 | API externa de cotação cambial apresentar indisponibilidade, instabilidade ou alteração de política de uso, bloqueando a funcionalidade central de simulação em tempo real (REQ-01). | Baixa (20%) | Alto | MÉDIA-ALTA | Mitigar: Implementar adapter pattern para permitir troca de provedor; manter cache local de cotações (Fase N5.2) como fallback; documentar provedor selecionado em registro formal de arquitetura. |

Fonte: Elaborado pelos autores (2026).

**Declaração de Rastreabilidade (Riscos → Objetivos SMART → EAP)**

| Risco | Objetivo SMART Afetado | Fases EAP Relacionadas | Domínio PMBOK 7ª |
| --- | --- | --- | --- |
| R1 (Entrega parcial) | Cronograma (Marcos) — 22/09/2026 | Macro-fase MF1 (todas as fases) | Abordagem de Desenvolvimento |
| R2 (Stack instável) | Produto (Escopo) — MVP funcional ≤ 3s | N4.1 (Seleção da Stack), N5 (Desenvolvimento) | Abordagem de Desenvolvimento |
| R3 (Burnout) | Inovação e Ferramentas — FOSS + SDD com IA | Todas as fases (transversal) | Equipe |
| R4 (Coverage < 80%) | Qualidade e Testes — ≥ 80% coverage | N6.1 (Testes), N7.1 (Pipeline CI) | Medição |
| R5 (API externa) | Produto (Escopo) — Simulação em tempo real | N5.2 (Backend — API de Câmbio + Cache) | Incerteza |

Fonte: Elaborado pelos autores (2026). Verificação de completude: 100% dos Objetivos SMART possuem ao menos um risco associado.

**Observações sobre a Gestão de Riscos**

1. Riscos positivos (oportunidades): O projeto identifica como oportunidade o uso de IA generativa (SDD) para acelerar a produção de artefatos e código-fonte, desde que com rastreabilidade adequada (Critério de Inovação Controlada).
2. Reserva de contingência: Dada a restrição de orçamento zero, não há reserva financeira para contingências. A gestão de riscos depende de ações preventivas e adaptações rápidas, conforme princípio GMV.
3. Monitoramento contínuo: Os riscos serão monitorados quinzenalmente via GitHub Projects (label risk ou blocked), com revisão formal no Plano de Riscos.
4. Gatilhos de reavaliação: Caso algum risco se materialize ou novos riscos sejam identificados com severidade CRÍTICA, o processo formal de gestão de mudanças (Fase N10 da EAP) será acionado.

## Orçamento do Projeto

Esta seção estabelece a estimativa preliminar de custos para o projeto COGME, conforme o Processo 4.1 (Desenvolver o Termo de Abertura do Projeto) do PMBOK® 6ª edição e o Domínio de Planejamento do PMBOK® 7ª edição. Dada a natureza acadêmica e simulada do projeto, aliada ao compromisso institucional com o Software Livre, o orçamento aprovado para a linha de base de custos é nulo.

**Tabela 15 — Linha de Base de Custos (Preliminar)**

| Categoria de Custo | Estimativa Preliminar | Justificativa e Premissa Associada |
| --- | --- | --- |
| Recursos Humanos | R$ 0,00 | Esforço acadêmico dos membros da equipe (3 pessoas). Não há folha de pagamento, terceirização ou horas extras remuneradas. |
| Software e Ferramentas | R$ 0,00 | Adoção estrita de tecnologias 100% FOSS (Free and Open Source Software). Ex: Python, FastAPI, SQLite, WeasyPrint, GitHub (Free Tier). |
| Infraestrutura e Hospedagem | R$ 0,00 | O MVP será desenvolvido, testado e validado em ambiente local (homologação). Não há contratação de serviços de cloud paga ou domínios comerciais. |
| Reserva de Contingência | R$ 0,00 | Não há verba financeira para absorver imprevistos. A mitigação de riscos dependerá exclusivamente de flexibilidade de escopo, alternativas FOSS e gestão de tempo. |
| Reserva de Gerenciamento | R$ 0,00 | Inaplicável em projetos sem patrocínio financeiro ou margem de lucro. |
| TOTAL DO ORÇAMENTO | R$ 0,00 | Linha de base de custos aprovada para o ciclo de vida do projeto. |

Fonte: Elaborado pelos autores (2026).

**Implicações Estratégicas do Orçamento Zero**

A ausência de recursos financeiros impõe condições específicas à gestão do projeto, que devem ser rigorosamente observadas:

1. Mitigação de Riscos sem Custo: Qualquer risco materializado (ex: instabilidade de uma API gratuita de câmbio) deve ser resolvido com alternativas técnicas gratuitas (ex: adapter pattern para outra API FOSS) ou ajuste de escopo, nunca com a aquisição de serviços pagos.
2. Plano de Recursos Tecnológicos: A seleção de todas as ferramentas (Fase N4.1 da EAP) está condicionada à existência de licenças compatíveis (MIT, Apache 2.0, GPL) e planos gratuitos que suportem a carga do MVP acadêmico.
3. Foco em Valor, não em Despesa: Conforme o Domínio de Medição do PMBOK 7ª, o sucesso do projeto será mensurado pela entrega de funcionalidades (Throughput, Cycle Time, cobertura de testes), e não por métricas financeiras tradicionais (como CPI ou SPI, que são inaplicáveis neste contexto).

**Rastreabilidade**

| Origem no TAP | Vínculo com o Orçamento |
| --- | --- |
| Objetivo: Inovação e Ferramentas | Exige que 100% do ciclo de vida utilize ferramentas FOSS, sustentando o custo zero. |
| Restrições de Custo | Estabelece a proibição formal de aquisições pagas e a inexistência de verba institucional. |
| Premissas | Assume que o hardware local da equipe é suficiente e que serviços externos gratuitos estarão disponíveis. |

Fonte: Elaborado pelos autores (2026).

Nota: O detalhamento de qualquer eventual custo indireto (ex: consumo marginal de energia elétrica ou internet) é considerado absorvido pelos recursos pessoais da equipe e não compõe a linha de base formal do projeto.

## Aprovações

**Tabela 16 — Aprovações**

| Participantes | Assinaturas | Datas |
| --- | --- | --- |
| COGME — Leonardo David Silva Setti, Fabricio de Lima Cabral, Edson Luis Silva | — | 16/09/2026 |
| Gerente do Projeto — Leonardo David Silva Setti | — | — |
| Cliente — Nivaldo Carleto | — | — |
| Patrocinador | N/A | — |
| Fornecedor | N/A | — |
| Investidor | N/A | — |
| Faculdade Parceira — FATEC Taquaritinga | — | — |
| Empresa Parceira | N/A | — |

Fonte: Elaborado pelos autores (2026).

---

# 1 GERENCIAMENTO DA INTEGRAÇÃO DO PROJETO

**Plano de Gerenciamento da Integração**

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Versão: 2.0 · Data: 20/09/2026
Autores: Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

Este plano deriva diretamente das Premissas P1 (governança híbrida), P3 (SDD com LLM), P4 (código como deliverable) e P7 (stakeholder-avaliador único nos marcos), e das Restrições de Cronograma e Custo do TAP, respeitando o Domínio de Abordagem de Desenvolvimento e o Domínio de Trabalho do Projeto do PMBOK® 7ª edição.

## 1.1 Identificação e Propósito

Este Plano de Gerenciamento da Integração coordena a execução integrada do projeto COGME, garantindo que os sete planos de área subsequentes — quatro entregues no marco M1 (Escopo, Cronograma, Custos, Qualidade) e três diferidos para o marco M2 (Recursos, Comunicações, Riscos), conforme a estratégia de entrega faseada da seção 1.4.1 —, o código-fonte e os artefatos de governança permaneçam coerentes com os Objetivos SMART aprovados no TAP.

Função ontológica: O TAP autoriza; este plano coordena. Ele não duplica conteúdo do TAP — define os mecanismos de coerência entre todos os artefatos do ciclo de vida.

Domínio PMBOK 7ª: Abordagem de Desenvolvimento.
Processo PMBOK 6ª (dicionário, obsolescência assumida): 4.2 — Desenvolver o Plano de Gerenciamento do Projeto.

## 1.2 Modelo de Governança Híbrida

O projeto adota um modelo trifásico de governança, declarado no TAP:

| Camada | Fonte Normativa | Função no COGME |
| --- | --- | --- |
| Governança primária | PMBOK® 7ª edição — 12 Princípios + 8 Domínios de Desempenho | Define por que e para quê; orienta decisões por valor |
| Dicionário complementar | PMBOK® 6ª edição — processos citados apenas para rastreabilidade acadêmica | Fornece vocabulário estrutural quando necessário |
| Método de execução | Manifesto Ágil (4 valores) + Kanban (fluxo contínuo) | Define como o trabalho é executado diariamente |

Figura 7 — Modelo de Governança Híbrida Trifásico

**[PLACEHOLDER — IMAGEM: docs/diagramas/integracao/fig-1-governanca-hibrida.svg]**

Nota: Ilustração da hierarquia normativa que rege o projeto COGME. A camada superior (PMBOK® 7ª) define os princípios e domínios de desempenho ("por que" e "para quê"); a camada intermediária (PMBOK® 6ª) atua estritamente como dicionário de processos, com obsolescência formalmente declarada para métricas preditivas (EVM); e a camada inferior (Kanban/Manifesto Ágil) define o método de execução operacional ("como"). A seta de realimentação representa o ciclo contínuo de lições aprendidas, blindando o projeto contra questionamentos de falta de estrutura formal.
Fonte: Elaborado pelos autores (2026).

### 1.2.1 Hierarquia de Resolução de Conflitos

Em caso de conflito entre fontes normativas, aplica-se a seguinte ordem de precedência:

1. Valor entregue ao usuário final (Domínio de Entrega — PMBOK 7ª)
2. Ementa da disciplina + orientação do Prof. Dr. Nivaldo Carleto
3. PMBOK® 7ª edição (princípios e domínios)
4. Manifesto Ágil + Kanban (método de execução)
5. PMBOK® 6ª edição (dicionário de processos)

Trade-off declarado: Esta hierarquia favorece velocidade de entrega sobre completude documental, alinhada ao Princípio "Foco em Valor" (PMBOK 7ª) e ao Valor Ágil "Software funcionando sobre documentação abrangente".

### 1.2.2 Papéis de Governança

| Papel | Titular | Responsabilidade |
| --- | --- | --- |
| Gerente de Projeto (GP) | Leonardo David Silva Setti | Decisor operacional único; CCB de membro único; autoridade para aprovações, rejeições e controle de mudanças |
| Desenvolvedores | Fabricio de Lima Cabral, Edson Luis Silva | Execução técnica; revisão em pares; self-report de carga horária |
| Stakeholder-Avaliador | Prof. Dr. Nivaldo Carleto | Avaliação acadêmica nos marcos M1–M4; sem ingerência em decisões operacionais |

### 1.2.3 Governança Mínima Viável (GMV)

Todo artefato de governança deve justificar sua existência pelo teste GMV:

| Pergunta | Se SIM | Se NÃO |
| --- | --- | --- |
| O Prof. Dr. Nivaldo Carleto exigirá este artefato na avaliação? | Produzir completo | Simplificar ou eliminar |
| Este artefato evita retrabalho futuro? | Produzir | Avaliar custo-benefício |
| Este artefato é útil para a equipe (não apenas para avaliação)? | Produzir | Eliminar |

Se ≥ 2 respostas forem NÃO, o artefato é candidato a simplificação ou eliminação. Decisão final do GP.

### 1.2.4 Obsolescência do PMBOK 6ª (Declaração Formal)

O PMBOK® 6ª edição (2017) é tratado exclusivamente como dicionário de processos. Processos preditivos são citados apenas para rastreabilidade acadêmica e blindagem terminológica. Métricas EVM (SPI/CPI) são declaradas LEGADO — NÃO APLICÁVEIS, substituídas por métricas de fluxo Kanban conforme ADR-003.

## 1.3 GitHub Projects como Fonte Única de Verdade (SSOT)

O repositório GitHub e seu módulo GitHub Projects constituem o artefato primário de integração, cronograma e monitoramento, conforme ADR-002. Esta decisão substitui qualquer ferramenta preditiva de planejamento como instrumento ativo.

Justificativa: Para uma equipe de 3 pessoas com fluxo contínuo, ferramentas preditivas impõem overhead de manutenção desproporcional ao valor gerado. O Kanban via GitHub Projects fornece visibilidade em tempo real, métricas nativas de fluxo e rastreabilidade automática via commits.

Domínio PMBOK 7ª: Medição + Trabalho do Projeto.
Valor Ágil: "Indivíduos e interações sobre processos e ferramentas."

### 1.3.1 Mapeamento Kanban ↔ Processos PMBOK 6ª

| Coluna Kanban (ADR-002) | Processo PMBOK 6ª | Domínio PMBOK 7ª | Regra Operacional |
| --- | --- | --- | --- |
| Backlog | 5.2 Coletar Requisitos | Planejamento | Card criado com DoR pendente |
| Ready (DoR) | 4.3 Orientar Trabalho (preparação) | Trabalho | DoR atendido; aguardando capacidade |
| In Progress | 4.3 Orientar e Gerenciar Trabalho | Trabalho | WIP limit: máx. 3 cards/pessoa |
| Code Review | 4.5 Monitorar e Controlar | Medição | Revisão em pares obrigatória |
| Done (DoD) | 5.4 Criar EAP (aceite do pacote) | Entrega | DoD atendido; commit mergeado |

Figura 8 — Fluxo Kanban Oficial com Gates de Qualidade e WIP Limits

**[PLACEHOLDER — IMAGEM: docs/diagramas/integracao/fig-2-fluxo-kanban-oficial.svg]**

Nota: O diagrama materializa operacionalmente a ADR-002 (Kanban como método de execução) e a ADR-004 (tasklists Markdown como substituto de subissues). As cinco colunas representam o fluxo contínuo do trabalho (Backlog → Ready → In Progress → Code Review → Done), com quatro gates de qualidade intermediários: (i) Gate DoR na entrada de Ready, exigindo critérios de prontidão atendidos; (ii) Gate WIP na entrada de In Progress, respeitando o limite de 3 cards por pessoa (prevenção de burnout, Domínio de Equipe PMBOK 7ª); (iii) Gate Tasklist na entrada de Code Review, exigindo 100% dos itens da tasklist Markdown concluídos (ADR-004); e (iv) Gate DoD na entrada de Done, exigindo critérios de conclusão atendidos (coverage ≥ 80%, revisão de pares aprovada, commit mergeado). O destaque vermelho sobre a coluna In Progress evidencia o WIP limit como mecanismo de controle de capacidade. A regra de ação corretiva inferior demonstra que violações de gates bloqueiam o fluxo e gargalos persistentes acionam Retrospectiva extraordinária, em conformidade com o Domínio de Medição do PMBOK® 7ª edição.
Fonte: Elaborado pelos autores (2026).

### 1.3.2 Regras de Fluxo e Rituais

Regras de fluxo (ADR-002 e ADR-004):

- Pull system: Cards migram para "In Progress" somente quando há capacidade disponível (WIP limit respeitado).
- WIP limit: 3 cards em "In Progress" por pessoa (Domínio de Equipe — prevenção de burnout, risco R3).
- Tasklists Markdown (ADR-004): Cards com estimativa ≥ 6h ou múltiplos entregáveis devem possuir tasklist no corpo da Issue (mínimo 3, máximo 7 itens; último item obrigatoriamente "Validação final"). Subissues reais são formalmente rejeitadas — a unidade atômica de métrica e de backlog permanece o card pai. O card só migra para Code Review com 100% dos itens concluídos.
- SDD com LLM: Código gerado com apoio de IA passa por revisão humana obrigatória antes do merge. Commits declaram co-autoria.

Rituais (ADR-002):

| Ritual | Formato | Cadência | Duração |
| --- | --- | --- | --- |
| Daily assíncrona | GitHub Issues | Diária | 15 min |
| Refinement | Product Backlog (GitHub Projects) | Semanal | 30 min |
| Retrospectiva | Risk backlog + lições aprendidas | Quinzenal | 30 min |

Nota: Sprints time-boxed NÃO são utilizadas. O fluxo é contínuo (ADR-002).

### 1.3.3 Milestones e Identificação de Cards

O SSOT opera sobre três mecanismos complementares de organização:

Milestones GitHub: 5 milestones — M1 (22/09), M2 (30/09), Calibração (03/10, auxiliar), M3 (15/11), M4 (15/12). Cada Issue vincula-se a exatamente uma milestone; Issues sem milestone são backlog não planejado. Milestone não é fechada enquanto houver Issues abertas com label change-request ou blocked.

Sistema de tags: Todo card porta no mínimo 3 labels (1 tipo + 1 macro-fase + 1 área de conhecimento), habilitando filtragem, métricas de fluxo por categoria (ADR-003) e rastreabilidade TAP → EAP → Card. A taxonomia completa (27 labels em 5 categorias) reside na configuração do repositório e não é replicada neste plano (GMV).

Padrão de redação (Card Ubíquo): Todo card é autossuficiente — declara o quê, por quê, como será aceito e a quem pertence, sem exigir leitura de outro artefato. Cards documentais seguem o Padrão A (título N{X}.{Y} — Descrição, contexto ubíquo, critérios de aceite binários, rastreabilidade dupla); cards de produto seguem o Padrão B (User Story com critérios Given/When/Then), com aplicação efetiva a partir de M2. A prioridade temporal P0–P3 complementa a classificação MoSCoW (P0 = caminho crítico do marco; P3 = postergável).

## 1.4 Desenvolvimento e Manutenção do Plano de Gerenciamento

Processo PMBOK 6ª (dicionário): 4.2 — Desenvolver o Plano de Gerenciamento do Projeto.

Os oito planos de área são versionados no repositório GitHub sob /docs/. Cada plano:

- Inicia com frase de rastreabilidade ao TAP (Premissa + Restrição + Domínio PMBOK 7ª).
- Possui extensão máxima de 4 páginas (princípio GMV).
- É versionado via Conventional Commits: docs(plano-integracao): atualização §X.
- Passa por revisão em pares antes de ser considerado "Done".

Regra de coerência cruzada: Nenhum plano pode contradizer datas de marcos (M1–M4), premissas (P1–P8) ou restrições do TAP. Inconsistências detectadas em revisão acionam correção imediata antes do merge. A hierarquia de autoridade entre artefatos é: TAP > base de conhecimento operacional > Glossário > ADRs.

### 1.4.1 Estratégia de Entrega Faseada dos Planos

Conforme o princípio de Elaboração Progressiva (PMBOK 6ª, dicionário) e a Personalização/Tailoring da Abordagem de Desenvolvimento (PMBOK 7ª), a entrega dos planos de gerenciamento é faseada:

| Marco | Planos Entregues | Justificativa |
| --- | --- | --- |
| M1 (22/09/2026) | Integração, Escopo, Cronograma, Custos, Qualidade (Áreas 1–5) | Fundação documental mínima viável; atendimento integral ao critério de aceite do TAP para o M1 |
| M2 (30/09/2026) | Recursos, Comunicações, Riscos (Áreas 6–8) | Redigidos após a calibração do fluxo Kanban (23/09–03/10), com dados empíricos de capacidade da equipe |

Trade-off declarado: Redução de ~30% da carga documental do M1, permitindo foco na qualidade dos cinco planos fundamentais e na configuração do SSOT. Decisão alinhada ao Domínio de Abordagem de Desenvolvimento e Ciclo de Vida (PMBOK 7ª) e ao princípio GMV (§1.2.3).

## 1.5 Orientação e Gestão do Trabalho do Projeto

Processo PMBOK 6ª (dicionário): 4.3 — Orientar e Gerenciar o Trabalho do Projeto.
Domínio PMBOK 7ª: Trabalho do Projeto.

### 1.5.1 Execução Diária

- Trabalho puxado do backlog conforme capacidade (pull system), respeitando a prioridade temporal P0–P3 e o WIP limit.
- Cada card segue o padrão de redação ubíquo (§1.3.3): título padronizado (ex: N5.1 — Backend: Lógica de Negócio), labels obrigatórias, milestone vinculada, responsável e critérios de aceite binários.
- Cards ≥ 6h portam tasklist Markdown conforme ADR-004 (§1.3.2).
- Commits seguem Conventional Commits (feat, fix, docs, test, ci, chore).

### 1.5.2 Gestão do Conhecimento

Processo PMBOK 6ª (dicionário): 4.4 — Gerenciar o Conhecimento do Projeto.

- Estrutura de conhecimento: /docs/ no repositório (planos, diagramas, lições aprendidas, catálogo de prompts SDD).
- Lições aprendidas registradas ao final de cada macro-fase (MF1, MF2, MF3).
- Decisões que afetam ≥ 2 fases da EAP, envolvem troca de tecnologia ou seriam questionadas pelo Prof. Dr. Nivaldo Carleto em avaliação são formalmente registradas via ADR (Architecture Decision Record), conforme REQ-12 e fase N9.1 da EAP. Decisões menores ficam em commit messages.

## 1.6 Monitoramento e Controle Integrado

Processo PMBOK 6ª (dicionário): 4.5 — Monitorar e Controlar o Trabalho do Projeto.
Domínio PMBOK 7ª: Medição.

### 1.6.1 Métricas de Fluxo Kanban (Oficiais — ADR-003)

Dada a restrição de orçamento zero (TAP), o Earned Value Management é inaplicável. As métricas de desempenho são exclusivamente baseadas no fluxo Kanban:

| Métrica | Definição | Meta (pós-calibração) | Frequência |
| --- | --- | --- | --- |
| Cycle Time | Tempo médio de um card do "In Progress" ao "Done" | ≤ 3 dias | Semanal |
| Throughput | Cards concluídos por semana | ≥ 5 cards/semana | Semanal |
| CFD (Cumulative Flow Diagram) | Visualização de gargalos no fluxo | Sem bandas largas | Semanal |
| WIP em fluxo | Cards ativos em "In Progress" | ≤ 9 (3 × 3 pessoas) | Contínuo |
| Coverage | Linhas testadas / linhas totais | ≥ 80% | Por push (CI) |
| Burnout (self-report) | Carga horária semanal declarada | ≤ 20h/pessoa | Semanal |

Definição canônica do CFD (referência para os Planos de Cronograma e Comunicações): O Cumulative Flow Diagram é a visualização gráfica do fluxo de trabalho acumulado no tempo, onde cada banda horizontal representa uma coluna do quadro Kanban e sua largura instantânea indica a quantidade de cards naquela etapa. Fonte de dados: GitHub Insights. Responsável pela publicação semanal: GP. CFD saudável: bandas paralelas de largura constante. CFD com gargalo: bandas que se alargam progressivamente. Ação corretiva: banda com largura superior a 2× a média das demais por 2 semanas consecutivas aciona Retrospectiva extraordinária (ADR-002).

Figura 9 — Cumulative Flow Diagram (CFD) — Padrão Saudável vs. Padrão com Gargalo

**[PLACEHOLDER — IMAGEM: docs/diagramas/integracao/fig-3-cfd-saudavel-vs-gargalo.svg]**

Nota: Ferramenta visual de monitoramento temporal que substitui formalmente o Gráfico de Gantt e o Earned Value Management (EVM), declarados inaplicáveis devido ao orçamento zero e ao escopo emergente (ADR-003). O painel (a) demonstra o estado ideal de fluxo estável (bandas paralelas); o painel (b) ilustra a detecção empírica de gargalos (alargamento progressivo de uma banda). Conforme a regra de ação corretiva, se uma banda ultrapassar 2× a largura média das demais por 2 semanas consecutivas, aciona-se uma Retrospectiva extraordinária, atendendo ao Domínio de Medição do PMBOK® 7ª edição.
Fonte: Elaborado pelos autores (2026).

### 1.6.2 Métricas Legado (Não Aplicáveis — ADR-003)

| Métrica | Status | Justificativa |
| --- | --- | --- |
| SPI (Schedule Performance Index) | ❌ LEGADO | Inaplicável — fluxo contínuo sem linha de base preditiva |
| CPI (Cost Performance Index) | ❌ LEGADO | Inaplicável — orçamento zero (AC = 0) |
| EVM (Earned Value Management) | ❌ LEGADO | Inaplicável — escopo emergente + orçamento nulo |

### 1.6.3 Período de Calibração

De 23/09/2026 a 03/10/2026, as métricas são coletadas sem meta fixa, estabelecendo a baseline empírica de desempenho real da equipe. Após calibração, metas são ajustadas com base na média observada ± 20% e formalizadas via ADR. A milestone auxiliar "Calibração" (03/10) rastreia este período no SSOT sem substituir o M2.

Trade-off declarado: Abre-se mão da formalidade EVM em favor de métricas acionáveis e nativas do método, conforme Domínio de Medição (PMBOK 7ª) e ADR-003.

## 1.7 Controle Integrado de Mudanças

Processo PMBOK 6ª (dicionário): 4.6 — Realizar o Controle Integrado de Mudanças.
Domínio PMBOK 7ª: Incerteza.

### 1.7.1 Autoridade de Mudança (CCB)

O Gerente de Projeto (Leonardo David Silva Setti) atua como Change Control Board (CCB) de membro único, com autoridade formal delegada pelo TAP. O Prof. Dr. Nivaldo Carleto não participa do fluxo de aprovação de mudanças; sua atuação restringe-se à avaliação acadêmica nos marcos M1–M4.

### 1.7.2 Fluxo de Solicitação de Mudança

| Etapa | Ação | Responsável | Prazo |
| --- | --- | --- | --- |
| 1 | Abertura de GitHub Issue com label change-request | Qualquer membro da equipe | Imediato |
| 2 | Análise de impacto (escopo, prazo, qualidade) | GP (Leonardo) | ≤ 48h |
| 3 | Aprovação ou rejeição via comentário na Issue | GP (Leonardo) | ≤ 24h após análise |
| 4 | Atualização do backlog + planos afetados + commit | Equipe | ≤ 24h após aprovação |

Figura 10 — Fluxo de Controle Integrado de Mudanças

**[PLACEHOLDER — IMAGEM: docs/diagramas/integracao/fig-4-controle-mudancas.svg]**

Nota: Materialização do Processo 4.6 do PMBOK® 6ª (dicionário) adaptado ao fluxo contínuo Kanban. O diagrama evidencia o CCB de membro único (Gerente de Projeto), os SLAs de resposta (≤ 48h para análise, ≤ 24h para decisão) e a bifurcação de tratamento: mudanças simples são resolvidas via commit e atualização do backlog, enquanto alterações de marco ou escopo do MVP exigem registro formal via ADR e comunicação ao avaliador no marco subsequente.
Fonte: Elaborado pelos autores (2026).

### 1.7.3 Limiar de Formalidade

- Mudanças que NÃO alteram marcos (M1–M4) nem escopo do MVP: Aprovadas pelo GP com registro em commit e comentário na Issue.
- Mudanças que ALTERAM marcos ou escopo do MVP: Aprovadas pelo GP com registro formal via ADR e comunicação ao Prof. Dr. Nivaldo Carleto no marco de avaliação subsequente.

Valor Ágil aplicado: "Responder a mudanças sobre seguir um plano." O processo é leve, mas auditável.

## 1.8 Encerramento do Projeto ou Fase

Processo PMBOK 6ª (dicionário): 4.7 — Encerrar o Projeto ou Fase.
Domínio PMBOK 7ª: Entrega.

### 1.8.1 Critérios de Encerramento por Macro-Fase

| Macro-Fase | Período | Critério de Encerramento |
| --- | --- | --- |
| MF1: Fundação | 01/09 – 30/09/2026 | TAP aprovado + 5 planos (Áreas 1–5) submetidos no M1 + 3 planos (Áreas 6–8) até o M2 + EAP sincronizada + Stack definida (ADR-001) + Ambiente e CI configurados |
| MF2: Construção | 01/10 – 15/11/2026 | MVP funcional + ≥ 80% coverage + UAT aprovado + Pipeline CI verde + baseline de métricas calibrada |
| MF3: Consolidação | 16/11 – 15/12/2026 | Documentação consolidada + Apresentação final + Validação acadêmica no marco M4 + Tag de release |

### 1.8.2 Encerramento Formal do Projeto

- Tag de release final no repositório GitHub.
- Lições aprendidas finais consolidadas.
- Verificação dos cinco Objetivos SMART do TAP.
- Validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4.

## 1.9 Condições de Fracasso e Escalation

Derivado das Condições de Fracasso do TAP, os seguintes gatilhos acionam ação corretiva imediata pelo GP:

| Gatilho | Ação |
| --- | --- |
| Desvio > 3 dias úteis em qualquer marco (M1–M4) | Issue change-request + proposta de replanejamento + ADR |
| Coverage < 70% por 2 semanas consecutivas | Revisão de prioridade de testes + ajuste de escopo |
| Burnout detectado (> 20h/semana por 2 semanas) | Redução de WIP + redistribuição de cards |
| Scope creep > 15% do backlog original | Congelamento de novas features + CCB (GP) |
| Throughput < 3 cards/semana por 2 semanas consecutivas | Revisão de WIP limits (fallback ADR-002) + reavaliação do escopo do MVP (fallback ADR-003) |
| MVP não funcional em homologação até M3 | Contingência técnica: redução de escopo não-crítico |

Nota: Escalation ao Prof. Dr. Nivaldo Carleto ocorre apenas nos marcos de avaliação ou quando o GP identificar risco de não cumprimento dos critérios SMART do TAP.

## 1.10 Declaração de Rastreabilidade

| Seção | Origem no TAP | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 1.2 (Governança) | Governança híbrida + Premissa P1 | Abordagem de Desenvolvimento | 4.1, 4.2 |
| 1.3 (SSOT + Milestones + Cards) | Premissa P1 + Métricas | Medição + Trabalho | 4.3, 4.5 |
| 1.4.1 (Entrega Faseada) | Marcos M1/M2 | Abordagem de Desenvolvimento | 4.2 |
| 1.5 (Orientação) | Premissas P3, P4, P5 | Trabalho do Projeto | 4.3, 4.4 |
| 1.6 (Monitoramento) | Métricas + Orçamento zero | Medição | 4.5 |
| 1.7 (Mudanças) | Fracasso + Premissa P7 | Incerteza | 4.6 |
| 1.8 (Encerramento) | Marcos M1–M4 | Entrega | 4.7 |
| 1.9 (Escalation) | Fracasso + Riscos | Incerteza | 4.5, 4.6 |

Verificação: 100% das seções possuem rastreabilidade a ao menos uma premissa, restrição ou objetivo SMART do TAP.

## 1.11 Premissas e Restrições Aplicáveis

| Tipo | Referência TAP | Impacto neste Plano |
| --- | --- | --- |
| Premissa P1 | Governança híbrida | Fundamenta 1.2 |
| Premissa P3 | SDD com LLM autorizado | Fundamenta 1.3.2 e 1.5.2 |
| Premissa P5 | ≤ 20h/semana por membro | Fundamenta 1.3.2 e 1.9 |
| Premissa P6 | Hardware adequado e suficiente | Fundamenta 1.3 (viabilidade local) |
| Premissa P7 | Stakeholder-avaliador único nos marcos | Fundamenta 1.2.2 e 1.7.1 |
| Restrição Cronograma | Prazo letivo inegociável | Fundamenta 1.4.1 e 1.9 |
| Restrição Custo | Orçamento zero | Fundamenta 1.6.2 (inaplicabilidade EVM) |

**Controle de Versões — Seção 1**

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 19/09/2026 | Emissão inicial | Leonardo D. S. Setti |
| 2.0 | 20/09/2026 | Entrega faseada dos planos (§1.4.1); incorporação da ADR-004 (tasklists, §1.3.2); milestones, labels e padrão de cards ubíquos (§1.3.3); definição canônica do CFD (§1.6.1); gatilho de throughput (§1.9); critérios MF1 corrigidos (§1.8.1); 4 diagramas incorporados | Leonardo D. S. Setti |

**Fim da Seção 1 — Integração | COGME**

---

# 2 GERENCIAMENTO DO ESCOPO DO PROJETO

**Plano de Gerenciamento do Escopo**

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Versão: 1.1 · Data: 20/09/2026
Autores: Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

Este plano deriva diretamente das Premissas P1 (governança híbrida), P2 (FOSS absoluto), P3 (SDD com IA auditável), P4 (código como deliverable), P8 (simplificação pedagógica) e P9 (separação ontológica TAP ≠ EAP ≠ PDCA), e das Restrições de Escopo, Cronograma e Qualidade do Termo de Abertura do Projeto (TAP), respeitando o Domínio de Planejamento e o Domínio de Entrega do PMBOK® 7ª edição.

## 2.1 Identificação e Propósito

Este Plano de Gerenciamento do Escopo define os mecanismos pelos quais o escopo do COGME é coletado, declarado, decomposto, validado e controlado ao longo do ciclo de vida. Sua função ontológica é complementar e subordinada ao TAP: o TAP autoriza o escopo de alto nível, a Estrutura Analítica do Projeto (EAP) o decompõe estruturalmente e este plano governa a evolução de ambos, garantindo coerência com os Objetivos SMART aprovados. Em conformidade com a Premissa P9, o TAP não integra a EAP nem é objeto de ciclos PDCA; este plano e a EAP, por sua vez, integram a estrutura de execução e melhoria contínua do projeto.

O plano ancora-se em dois referenciais normativos: o Domínio de Planejamento e o Domínio de Entrega do PMBOK® 7ª edição (PROJECT MANAGEMENT INSTITUTE, 2021), que orientam a evolução progressiva do escopo e a geração de valor; e, como dicionário complementar com obsolescência formalmente declarada, os processos 5.1 a 5.6 do PMBOK® 6ª edição (PROJECT MANAGEMENT INSTITUTE, 2017). Este documento é entregável do marco M1, conforme a estratégia de entrega faseada dos planos de gerenciamento (Plano de Integração, seção 1.4.1).

## 2.2 Abordagem Híbrida de Gerenciamento do Escopo

Conforme a Premissa P1 e a ADR-002, o escopo é gerenciado em duas camadas complementares. A primeira, denominada linha de base estrutural, é materializada pela EAP aprovada no TAP e define o escopo obrigatório do MVP acadêmico. A segunda, denominada fluxo emergente, é operacionalizada pelo backlog Kanban no GitHub Projects, que define a ordem de execução e permite evolução progressiva sem sprints time-boxed.

O trade-off declarado privilegia a completude acadêmica, garantida pela EAP, em detrimento da rigidez preditiva, e assegura adaptabilidade por meio do fluxo contínuo, em conformidade com o valor ágil "responder a mudanças sobre seguir um plano". Qualquer alteração fora da linha de base aciona o controle integrado de mudanças do Plano de Integração, seção 1.7.

## 2.3 Coleta e Gestão de Requisitos

### 2.3.1 Métodos de Levantamento

Os requisitos foram coletados por duas técnicas complementares, em conformidade com o processo 5.2 do PMBOK® 6ª: análise de domínio, conduzida a partir da dor do público-alvo — profissionais brasileiros que prestam serviços ao exterior em moeda estrangeira — e do mapeamento das ferramentas dispersas hoje utilizadas para simulação cambial; e brainstorm estruturado da equipe, do qual derivaram as quinze necessidades consolidadas como requisitos. A combinação é justificável pelo contexto acadêmico, que dispensa técnicas de maior formalidade, como grupos focais ou prototipação de requisitos, em conformidade com o princípio de Governança Mínima Viável (GMV) declarado no Plano de Integração, seção 1.2.3.

### 2.3.2 Inventário e Documentação de Requisitos

Os quinze requisitos encontram-se consolidados no TAP, que exerce provisoriamente a função de documentação de requisitos até a publicação do artefato canônico em /docs/requisitos/requisitos.md, prevista para o marco M2. Distribuem-se em seis entregas principais, cada uma rastreável a um Objetivo SMART e a uma fase da EAP:

a) MVP Web Funcional (Fase N5): REQ-01 a REQ-07 — simulação cambial em tempo real, cinco regimes de contratação, spread e IOF, invoice em PDF, tempo de resposta inferior a três segundos, interface responsiva e cache de cotações;

b) Garantia da Qualidade (Fase N6): REQ-08 a REQ-10 — cobertura de testes superior a oitenta por cento, UAT com cem por cento dos fluxos críticos e ferramentas da qualidade;

c) DevOps e CI/CD (Fase N7): REQ-11 — pipeline de integração contínua;

d) Base de Conhecimento (Fase N9): REQ-12 e REQ-13 — ADRs e rastreabilidade de prompts SDD;

e) Documentação Técnica (Fase N11): REQ-14 — arquitetura e APIs consolidadas;

f) Conformidade FOSS (Fases N1 e N4): REQ-15 — licenciamento integralmente aberto.

### 2.3.3 Formato dos Requisitos e Conversão a Posteriori

Os requisitos REQ-01 a REQ-15 foram formalizados com critério de aceite mensurável, rastreabilidade ao TAP e vínculo à fase da EAP, formato suficiente para o marco M1. A conversão para o formato canônico de User Story — "Como [papel], quero [ação], para [benefício]" com critérios de aceite Given/When/Then — será realizada a posteriori, até o marco M2 (30/09/2026), conforme fase N2.3 da EAP, utilizando o Padrão B de redação de cards. A decisão é justificada pela restrição de prazo letivo e pelo princípio GMV.

### 2.3.4 Abordagem Specification-Driven Development (SDD)

O escopo inclui, como requisito formal (REQ-12 e REQ-13), a utilização de Specification-Driven Development com apoio de Inteligência Artificial Generativa, conforme a Premissa P3 e o Objetivo SMART de Inovação do TAP. A abordagem SDD opera sobre a stack local canônica do projeto — llama.cpp como motor de inferência, modelo Qwen 32B e OpenCode como interface de desenvolvimento —, garantindo custo zero e conformidade FOSS em aderência à Premissa P2. A formalização da stack na ADR-001 encontra-se em avaliação e poderá sofrer atualizações de impacto relevante; a inclusão, a exclusão ou a troca de ferramentas, modelos ou motores em todo o contexto da stack exigirá ADR específica, conforme a política de ADRs do projeto (gatilhos de impacto transversal e de irreversibilidade prática) e o fluxo de mudanças da seção 2.8. O detalhamento operacional — prompts, personas e handoffs — reside no Catálogo de Prompts SDD (fase N9.3, diretório .ai/handoffs/) e nas ADRs (fase N9.1). A política de co-autoria em commits e a rastreabilidade integral dos prompts constituem critérios de aceite dos requisitos REQ-12 e REQ-13.

### 2.3.5 Priorização de Requisitos e de Cards

A priorização opera em duas camadas distintas e complementares. A classificação de valor de escopo aplica o método MoSCoW aos requisitos: a classe Must compreende REQ-01 a REQ-09, REQ-11 e REQ-15; a classe Should compreende REQ-10, REQ-12, REQ-13 e REQ-14; as classes Could e Won't encontram-se vazias, registrando a última as exclusões da seção 2.4. A classificação de urgência temporal aplica a escala P0–P3 aos cards do backlog, sendo P0 o caminho crítico do marco e P3 o item postergável. Ambas as classificações são aplicadas e revisadas no Refinement semanal, cuja primeira sessão ocorre em 23/09/2026.

## 2.4 Declaração de Escopo do Projeto

Em respeito ao princípio GMV e para evitar proliferação documental, a Declaração de Escopo é consolidada neste plano, em vez de constituir artefato separado.

### 2.4.1 Fronteira do Escopo

A fronteira do escopo é apresentada na Tabela 17. A coluna de exclusões é fundamentada no princípio YAGNI (You Aren't Gonna Need It), em conformidade com a restrição de escopo do TAP: funcionalidades não essenciais ao MVP acadêmico são explicitamente excluídas do ciclo atual, podendo ser reconsideradas apenas mediante solicitação formal de mudança (Plano de Integração, seção 1.7). Esta exclusão explícita operacionaliza a restrição de MVP e previne scope creep por acréscimo incremental não autorizado.

**Tabela 17 — Fronteira do Escopo (IN / OUT)**

| Escopo aprovado (IN) | Escopo excluído (OUT) |
| --- | --- |
| Simulação cambial USD/EUR → BRL em tempo real | Suporte a outras moedas (GBP, JPY, CHF) |
| Cinco regimes de contratação (hora, dia, semana, mês, valor fixo) | Cadastro multiusuário ou autenticação |
| Cálculo de spread e IOF com precisão de duas casas decimais | Integração com plataformas de transferência |
| Emissão de invoice em PDF via WeasyPrint em até três segundos | Emissão de notas fiscais brasileiras (NF-e, NFS-e) |
| Interface web responsiva FOSS | Aplicativo mobile nativo |
| Cache SQLite de cotações | Banco relacional multiusuário (PostgreSQL) |
| Cobertura de testes ≥ 80% e UAT com 100% dos fluxos críticos | Testes de carga ou estresse |
| Pipeline CI com lint e testes em até cinco minutos | Continuous deployment para produção |
| ADRs e catálogo de prompts SDD | Documentação de usuário final em PDF |
| Stack 100% FOSS auditável | Bibliotecas proprietárias ou serviços pagos |

Fonte: Elaborado pelos autores (2026), com base no TAP.

### 2.4.2 Critérios de Aceite do Escopo

O escopo será considerado aceito quando todos os requisitos da classe Must estiverem operacionais em UAT; quando a cobertura de testes atingir oitenta por cento, validada via integração contínua; quando não houver defeitos críticos ou bloqueantes; quando cem por cento das dependências possuírem licenças aprovadas pela Open Source Initiative; e quando houver validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4.

### 2.4.3 Artefatos Técnicos Não Abrangidos por Este Plano

Para prevenir invasão de contexto, declara-se que não compõem o escopo deste plano: a) diagramas UML completos, sendo a arquitetura da solução (fase N3.1) documentada por diagrama de componentes em Markdown ou PlantUML; b) o Diagrama Entidade-Relacionamento, produzido na fase N3.3 e versionado no repositório; c) a estrutura de diretórios do repositório, documentada no arquivo README.md na fase N5; e d) os arquivos de configuração do pipeline, versionados em .github/workflows/ na fase N7.1.

## 2.5 Estrutura Analítica do Projeto

A EAP aprovada no TAP constitui a linha de base estrutural do escopo: nível 0 (raiz COGME), doze fases de nível 1 (N1 a N12), trinta e sete pacotes de trabalho de nível 2 e três macro-fases (MF1 Fundação, MF2 Construção, MF3 Consolidação), conforme representado na Figura 11.

Figura 11 — EAP do COGME — Visão Executiva

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-01-eap-executiva.svg]**

Nota: Raiz N0 no topo; doze caixas de nível 1 agrupadas em três faixas horizontais rotuladas MF1, MF2 e MF3; cada caixa de fase exibindo o identificador (N1…N12), o nome da fase e a contagem de pacotes de nível 2; sem abertura dos 37 pacotes, para preservar legibilidade. A EAP é o artefato nuclear do processo 5.4 (Criar EAP/WBS).
Fonte: Elaborado pelos autores (2026).

Nota de canonicidade (decisão do GP, 20/09/2026): a linha de base da EAP é canônica no TAP. O TAP e o Plano de Integração constituem as fontes canônicas de autorização e de coordenação do projeto. O Glossário é artefato terminológico volátil, atualizado a cada rodada de redação dos planos, e não constitui linha de base: eventuais divergências de contagem de fases ou pacotes são resolvidas pela prevalência do TAP, sem necessidade de solicitação de mudança.

Três regras de governança aplicam-se à decomposição. Primeira: nenhum pacote de trabalho pode ser adicionado, removido ou renomeado sem aprovação formal via change-request. Segunda: cada pacote de nível 2 decompõe-se em cards Kanban com esforço estimado inferior ou igual a oito horas, redigidos conforme os Padrões A (documental) ou B (User Story GWT). Terceira: quando necessário à execução, o card decompõe-se em atividades derivadas — ações verbais que detalham a entrega substantiva, em conformidade com o processo 6.2 do PMBOK® 6ª (dicionário) — materializadas como tasklist Markdown no corpo da Issue, conforme a ADR-004, que rejeita formalmente subissues. A cadeia completa é representada na Figura 12.

Figura 12 — Cadeia de Decomposição do Escopo e Gates de Qualidade

**[PLACEHOLDER — IMAGEM: docs/diagramas/escopo/fig-2-cadeia-decomposicao-escopo.svg]**

Nota: Três níveis encadeados da esquerda para a direita — (i) pacote de trabalho EAP nível 2 (entrega substantiva, ex.: "N5.1 — Backend: Lógica de Negócio"); (ii) card ubíquo Kanban (unidade atômica de backlog e de métrica, ≤ 8h, Padrão A ou B); (iii) atividades derivadas como tasklist Markdown (3 a 7 itens verbais, último item "Validação final", ADR-004); gates anotados entre colunas: DoR na entrada de Ready, tasklist 100% + revisão de pares na entrada de Code Review, DoD na entrada de Done; anotação lateral: "métricas de fluxo medem o card pai (ADR-003); subissues rejeitadas (ADR-004)". Materializa a operacionalização do processo 6.2 do PMBOK 6ª no método Kanban.
Fonte: Elaborado pelos autores (2026).

Em conformidade com a Premissa P9, a EAP e seus pacotes integram a estrutura de ciclos PDCA do projeto (doze ciclos, um por fase), enquanto o TAP permanece como documento de autorização, não gerenciado.

## 2.6 Definition of Ready e Definition of Done

Em conformidade com o Domínio de Entrega e o Domínio de Medição do PMBOK® 7ª, formalizam-se os gates de qualidade do fluxo Kanban.

O DoR, gate de entrada, exige que o card possua: título padronizado no formato N{X}.{Y} — Descrição; contexto ubíquo autocontido; critério de aceite mensurável; rastreabilidade à fase da EAP e ao requisito do TAP; estimativa de esforço inferior ou igual a oito horas; dependências identificadas; responsável atribuído; no mínimo três labels (tipo, macro-fase e área de conhecimento); milestone vinculada; e revisão no Refinement semanal. Cards documentais seguem o Padrão A e cards de produto seguem o Padrão B.

O DoD, gate de saída, exige que: 1) o código esteja implementado e commitado em feature branch; 2) os testes unitários estejam escritos com cobertura do módulo superior ou igual a oitenta por cento; 3) o pipeline de integração contínua esteja verde; 4) o Code Review tenha sido aprovado por pelo menos um par; 5) a documentação esteja atualizada, quando aplicável; 6) o card tenha sido movido para Done com data registrada; 7) se o código foi gerado com apoio de SDD, o commit declare co-autoria, conforme o Critério de Inovação Controlada do TAP; e 8) se o card possuir tasklist Markdown no corpo da Issue (conforme ADR-004), cem por cento dos itens estejam marcados como concluídos. Artefatos em status pair-review ou in-review não satisfazem o DoD e permanecem na coluna Code Review até a conclusão da revisão.

Nota (ADR-004): cards documentais seguem o Padrão A de redação (título N{X}.{Y} — Descrição, contexto ubíquo, critérios de aceite binários, rastreabilidade dupla); cards de produto seguem o Padrão B (User Story com critérios Given/When/Then), com aplicação efetiva a partir do marco M2 (30/09/2026). O gate de tasklist (item 8) é definido canonicamente neste plano e referenciado pelo Plano de Integração, seção 1.3.2, como regra de migração de fluxo — a Integração sinaliza o ponto de controle sem duplicar o conteúdo do DoD, em conformidade com a fronteira de escopo entre as duas áreas.

## 2.7 Validação e Controle de Escopo

Os processos 5.5 (Validar o Escopo) e 5.6 (Controlar o Escopo) do PMBOK® 6ª são operacionalizados por rituais Kanban, conforme a ADR-002. A validação ocorre por Code Review e por User Acceptance Testing no marco M3, com evidência em Pull Request aprovado e relatório de UAT. O controle ocorre por Refinement semanal e por análise do Cumulative Flow Diagram, cuja definição formal, cadência e regra de ação corretiva residem no Plano de Integração, seção 1.6.1, com evidência no GitHub Projects e no GitHub Insights.

A prevenção de scope creep aciona alerta quando o backlog cresce superior a quinze por cento em relação à linha de base de trinta e sete pacotes da EAP. Nesse caso, o GP congela novas features, analisa o impacto via change-request e decide em até quarenta e oito horas. A métrica de controle é o Throughput semanal superior ou igual a cinco cards; se inferior a três cards por semana durante duas semanas consecutivas, o escopo é revisado conforme o fallback da ADR-003.

## 2.8 Gestão de Mudanças de Escopo

Qualquer alteração de escopo segue o fluxo do Plano de Integração, seção 1.7: abertura de Issue com label change-request, análise de impacto pelo GP em até quarenta e oito horas, aprovação ou rejeição em até vinte e quatro horas e atualização do backlog, da EAP quando aplicável, e commit. Mudanças que alterem marcos (M1–M4) ou o escopo do MVP exigem registro formal via ADR e comunicação ao Prof. Dr. Nivaldo Carleto no marco de avaliação subsequente. A inclusão, exclusão ou renomeação de pacotes da EAP enquadra-se sempre neste limiar de formalidade. Mudanças na stack tecnológica — incluindo a stack SDD, conforme seção 2.3.4 — seguem o mesmo fluxo e exigem ADR específica quando atendidos os gatilhos da política de ADRs do projeto.

## 2.9 Critérios de Aceite e Condições de Fracasso

Esta seção consolida, em respeito ao princípio GMV, os critérios positivos de aceite e os gatilhos negativos de fracasso do escopo.

### 2.9.1 Critérios de Aceite

Remetem-se aos critérios da seção 2.4.2, acrescidos da verificação de que cem por cento dos requisitos da classe Must possuam rastreabilidade documentada a Objetivo SMART, fase da EAP e card do backlog.

### 2.9.2 Condições de Fracasso e Escalation

Derivados do TAP, os seguintes gatilhos específicos acionam ação corretiva: a) requisito Must não implementado até M3, com contingência de redução de escopo Should; b) EAP com mais de quinze por cento de pacotes não iniciados até M2, com replanejamento e ADR; c) UAT com defeito crítico ou bloqueante, com retrabalho imediato e congelamento de novas features; d) scope creep superior a quinze por cento, com congelamento e decisão do CCB; e e) cobertura de requisitos inferior a cem por cento dos Must, com bloqueio do M3.

## 2.10 Declaração de Rastreabilidade

A Tabela 18 apresenta a rastreabilidade de cada seção deste plano ao TAP, ao domínio de desempenho do PMBOK® 7ª correspondente e ao processo do PMBOK® 6ª utilizado como dicionário.

**Tabela 18 — Rastreabilidade interna do Plano de Escopo**

| Seção | Origem | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 2.2 (Abordagem híbrida) | Governança híbrida + Premissa P1 | Planejamento + Entrega | 5.1 |
| 2.3 (Requisitos) | Objetivos + Requisitos + Premissa P3 | Entrega | 5.2 |
| 2.3.4 (Stack SDD local + regra de ADR) | Premissa P3 + REQ-12/13 + Política de ADRs | Trabalho do Projeto | 5.2 |
| 2.4 (Declaração de Escopo) | Objetivos + Restrições + Premissa P2 | Entrega | 5.3 |
| 2.5 (EAP e decomposição; canonicidade) | EAP + Premissa P9 | Planejamento | 5.4 + 6.2 (dicionário) |
| 2.6 (DoR/DoD) | Qualidade + Inovação Controlada | Entrega + Medição | 5.5 |
| 2.6 — DoD item 8 (tasklist) | ADR-004 + Integração §1.3.2 | Trabalho do Projeto | 4.3 (dicionário) |
| 2.6 — Padrões de redação | Padrões A/B + ADR-002 | Entrega | 5.2 |
| 2.7 (Validação/Controle) | Métricas | Medição | 5.5, 5.6 |
| 2.8 (Mudanças) | Fracasso + Premissa P7 | Incerteza | 4.6 |
| 2.9 (Aceite/Fracasso) | Objetivos SMART + Fracasso + Riscos | Incerteza + Entrega | 5.5, 5.6 |

Fonte: Elaborado pelos autores (2026).

Verificação: cem por cento das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa ou restrição do TAP; a fronteira OUT da seção 2.4.1 é adicionalmente fundamentada no princípio YAGNI; o gate de tasklist e os padrões de redação possuem rastreabilidade cruzada com a ADR-004 e o Plano de Integração §1.3.2.

## 2.11 Premissas e Restrições Aplicáveis

As premissas aplicáveis a este plano são: P1 (governança híbrida), que fundamenta a seção 2.2; P2 (FOSS absoluto), que fundamenta a fronteira OUT da seção 2.4.1 e a stack SDD local da seção 2.3.4; P3 (SDD com IA auditável), que fundamenta a seção 2.3.4; P4 (código como deliverable), que fundamenta o DoD da seção 2.6; P8 (simplificação de Aquisições e Partes Interessadas), que fundamenta o escopo enxuto; e P9 (separação ontológica TAP ≠ EAP ≠ PDCA), que fundamenta a seção 2.5.

As restrições aplicáveis são: restrição de escopo (MVP acadêmico), que fundamenta a fronteira IN/OUT e a aplicação do princípio YAGNI na seção 2.4.1; restrição de cronograma (prazo letivo inegociável), que fundamenta a conversão a posteriori da seção 2.3.3 e os gatilhos da seção 2.9; e restrição de qualidade (tempo restrito para testes), que fundamenta o DoD com cobertura da seção 2.6.

**Controle de Versões — Seção 2**

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 0.0 | 19/09/2026 | Emissão para análise prévia | Leonardo D. S. Setti |
| 0.1 | 19/09/2026 | Inserção do princípio YAGNI na fronteira OUT | Leonardo D. S. Setti |
| 0.2 | 19/09/2026 | Remoção de versões internas; Premissa P3; Tabelas 1 e 2; fusão de aceite e fracasso | Leonardo D. S. Setti |
| 1.0 | 20/09/2026 | Incorporação da ADR-004 (DoD item 8); Padrões A/B e P0–P3; Premissa P9 e Atividades Derivadas; Figuras 1 e 2; otimização ABNT | Leonardo D. S. Setti |
| 1.1 | 20/09/2026 | Resoluções do GP: Nota de Canonicidade no §2.5; §2.3.4 com stack SDD local canônica; §2.6 com nota de canonicidade do DoD/Padrões e Tabela 2 expandida | Leonardo D. S. Setti |

**Fim da Seção 2 — Escopo | COGME v1.1**

---

# 3 GERENCIAMENTO DO CRONOGRAMA DO PROJETO

**Plano de Gerenciamento do Cronograma**

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Versão: 1.2 · Data: 21/09/2026
Autores: Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

Este plano deriva diretamente das Premissas P1 (governança híbrida), P5 (disponibilidade de até 20h semanais por membro) e P7 (stakeholder-avaliador único nos marcos), e das Restrições de Cronograma e de Recursos e de Orçamento do TAP, respeitando o Domínio de Planejamento e o Domínio de Medição do PMBOK® 7ª edição. Aplicam-se a este documento o regime de freeze do TAP e as Notas de Contexto registradas na seção 3.8.

## 3.1 Identificação e Propósito

Este Plano de Gerenciamento do Cronograma define como o tempo do projeto COGME é estruturado, estimado, consolidado e controlado. Sua função ontológica é complementar e subordinada ao TAP como fonte autorizativa: o TAP fixa os marcos M1–M4, o Plano de Escopo decompõe o trabalho em pacotes e cards (§2.5) e este plano governa o sequenciamento, a estimativa e o controle temporal entre ambos, sem duplicar o roadmap nem os gates DoR/DoD (Escopo §2.6).

Canonicidade e regime de freeze: o TAP, o Plano de Integração e o Plano de Escopo permanecem fontes canônicas de autorização, coordenação e escopo. O TAP encontra-se em regime de freeze desde o início do planejamento — sua última versão (18/09/2026) precede os planos de gerenciamento e não é objeto de revisão ao longo do ciclo, em conformidade com seu status ontológico já declarado: o TAP autoriza, não integra a EAP e não é gerenciado por ciclos PDCA (Premissa P9; PMBOK® 6ª §4.1, dicionário). Em caso de divergência entre seções do TAP, a seção de Marcos é canônica para matéria temporal (NC-00). Este plano detém as Notas de Contexto (§3.8) como mecanismo exclusivo de registro de leituras operacionais do TAP congelado.

Domínios PMBOK 7ª: Planejamento (evolução progressiva do cronograma) e Medição (monitoramento temporal do progresso).

Processos PMBOK 6ª (dicionário, obsolescência formalmente declarada conforme Integração §1.2.4): 6.1 Planejar o Gerenciamento do Cronograma; 6.2 Definir as Atividades; 6.3 Sequenciar as Atividades; 6.4 Estimar as Durações das Atividades; 6.5 Desenvolver o Cronograma; 6.6 Controlar o Cronograma.

## 3.2 Abordagem de Gerenciamento do Cronograma (processo 6.1)

O cronograma é gerenciado em três camadas temporais distintas, materializando a Personalização da Abordagem de Desenvolvimento (PMBOK 7ª) e a ADR-002:

| Camada | Objeto | Mecanismo de controle | Estabilidade |
| --- | --- | --- | --- |
| Macro | Marcos M1–M4 | Datas fixas do TAP; alteração somente via change-request + ADR + comunicação (Integração §1.7.3) | Inegociável sem CCB |
| Meso | Macro-fases MF1–MF3 + milestone auxiliar Calibração | Períodos declarados (Integração §1.8.1); gates de fechamento entre macro-fases | Ajustável apenas via CCB |
| Operacional | Cards Kanban (≤ 8h) | Fluxo contínuo pull, WIP de 3 cards/pessoa, sem sprints e sem datas por atividade (ADR-002) | Emergente, refinado semanalmente |

Aplica-se o planejamento em ondas sucessivas (elaboração progressiva, PMBOK 6ª como dicionário): o detalhe operacional emerge no Refinement semanal (ADR-002), enquanto apenas as camadas macro e meso são objeto de controle formal de mudanças. Não existe linha de base preditiva de datas por pacote: a única linha de base temporal formal é o conjunto {marcos M1–M4 + macro-fases MF1–MF3 + milestone auxiliar Calibração}.

Trade-off declarado: abre-se mão da previsibilidade preditiva por atividade em favor de confiabilidade empírica no nível do marco, alinhado ao Domínio de Medição (PMBOK 7ª), à ADR-003 e ao valor ágil "Responder a mudanças sobre seguir um plano".

## 3.3 Definição das Atividades (processo 6.2)

A cadeia de decomposição temporal é idêntica à cadeia de decomposição do escopo, canonicamente representada na Figura 12 do Plano de Escopo (§2.5): os 37 pacotes de trabalho de nível 2 da EAP decompõem-se em cards Kanban com esforço ≤ 8h, e estes, quando ≥ 6h ou com múltiplos entregáveis, decompõem-se em atividades derivadas materializadas como tasklist Markdown (3 a 7 itens; último item obrigatoriamente "Validação final"), conforme ADR-004, que rejeita formalmente subissues.

Regras operacionais desta seção: (i) a unidade atômica de cronograma e de métrica temporal é o card pai (ADR-003 e ADR-004); itens de tasklist não geram previsão nem métrica própria; (ii) nenhum card migra para Ready sem estimativa de esforço e dependências identificadas (DoR, Escopo §2.6); (iii) cards estimados acima de 8h são obrigatoriamente divididos antes de entrar no fluxo.

## 3.4 Sequenciamento e Dependências (processo 6.3)

Conforme a ADR-003, não se constrói rede de precedências CPM no nível operacional: em fluxo contínuo com escopo emergente, uma rede de atividades ficaria obsoleta em dias, violando o princípio GMV. O sequenciamento opera por quatro mecanismos nativos do SSOT:

a) campo "Dependências" dos Padrões A e B de redação de cards;
b) gate DoR "dependências identificadas" (Escopo §2.6);
c) label blocked com registro obrigatório da dependência no corpo da Issue;
d) regra P0: card que, ausente, impede o marco ou bloqueia ≥ 2 outros cards integra o caminho crítico empírico.

O caminho crítico é identificado empiricamente pela combinação de cards P0, alargamentos de banda no CFD e desvios de Cycle Time — definição formal, cadência e regra corretiva canonicamente na Integração §1.6.1 —, revisada a cada Refinement semanal e a cada Retrospectiva quinzenal.

No nível macro, o sequenciamento é finish-to-start entre macro-fases, com gates explícitos: o M2 encerra a MF1; a milestone auxiliar Calibração (03/10/2026) libera a baseline empírica que autoriza metas na MF2; o M3 encerra a MF2; o M4 encerra a MF3. Dentro de cada macro-fase, o paralelismo é integral, gerenciado por pull system e WIP limits.

Figura 13 — Sequenciamento Macro e Caminho Crítico Empírico

**[PLACEHOLDER — IMAGEM: docs/diagramas/cronograma/fig-1-sequenciamento-macro-caminho-critico.svg]**

Nota: Faixa superior com as três macro-fases encadeadas por gates (MF1 → gate M2/Calibração → MF2 → gate M3 → MF3 → gate M4); faixa inferior com a camada operacional mostrando os quatro detectores do caminho crítico empírico (cards P0, label blocked, bandas do CFD, desvio de Cycle Time) alimentando a decisão de replanejamento no Refinement. Substitui visualmente a rede CPM rejeitada, demonstrando como o sequenciamento é controlado sem preditividade artificial.
Fonte: Elaborado pelos autores (2026).

## 3.5 Estimativa de Esforço e Duração (processo 6.4)

Esforço é estimado em horas pelo responsável técnico (julgamento de especialista), com classificação relativa T-shirt (PP ≤ 2h, P ≤ 4h, M ≤ 6h, G = 8h) como verificação cruzada. As faixas são binárias quanto à governança: cards ≤ 4h são atômicos e não portam tasklist; cards ≥ 6h portam tasklist obrigatória; o teto absoluto é 8h (ADR-004; Escopo §2.5).

Capacidade semanal nominal: 3 membros × 20h/semana (Premissa P5) = 60h/semana, regulada pelo WIP limit de 3 cards em In Progress por pessoa (ADR-002), e não por taxa de utilização fixa. O overhead dos rituais (daily assíncrona, Refinement semanal, Retrospectiva quinzenal — ADR-002) é estimado em ≤ 1h/semana por membro e absorvido pela capacidade nominal (premissa PA-3). Verificação de capacidade do marco corrente: a distribuição de trabalho do backlog M1 registra ~14h (Leonardo), ~13h (Fabricio) e ~11h (Edson), todos dentro do limite da Premissa P5 — evidência verificável de aderência (NC-06).

Duração calendarizada não é estimada por atividade: emerge do fluxo. O Cycle Time (definição operacional da ADR-003: In Progress → Done) possui meta de ≤ 3 dias após a calibração; a projeção de conclusão de cada marco é obtida dividindo-se o backlog ordenado por prioridade (P0 → P3) pelo Throughput empírico (meta ≥ 5 cards/semana pós-calibração; baseline em /docs/metricas/baseline.md após 03/10/2026, conforme ADR-003).

Convenção de dias (NC-03): métricas de fluxo (Cycle Time, CFD) são medidas em dias corridos, por serem nativas do GitHub Insights e não exigirem recálculo; marcos, desvios de marco e capacidade são tratados em dias úteis, refletindo a disponibilidade real da equipe e coerente com o gatilho de escalation da Integração §1.9 ("desvio > 3 dias úteis").

Trade-off declarado: perde-se a previsão determinística por atividade e ganha-se previsão empírica por marco com overhead zero de estimativa, conforme Domínio de Planejamento (PMBOK 7ª) e princípio GMV.

## 3.6 Desenvolvimento do Cronograma (processo 6.5)

O cronograma do COGME é materializado por três artefatos complementares: (i) o roadmap macro de marcos (Figura 6), única representação tipo Gantt admitida, restrita ao nível macro e derivada do SSOT; (ii) o backlog ordenado por P0–P3 e MoSCoW no GitHub Projects, que constitui o cronograma operacional vivo; e (iii) a linha de base temporal formal {M1–M4 + MF1–MF3 + Calibração}, única sujeita a controle integrado de mudanças.

O período de calibração (23/09 a 03/10/2026) é um artefato de cronograma: converte métricas de fluxo em capacidade de previsão. Até seu encerramento, as metas permanecem suspensas (Integração §1.6.3); após, metas ajustadas pela média observada ± 20% são formalizadas via ADR (ADR-003).

**Tabela 19 — Marcos, janelas e entregáveis de valor**

| Marco | Abertura SSOT | Data alvo | Entregável de valor | Critério de aceite |
| --- | --- | --- | --- | --- |
| M1 — Entrega Parcial Documental | 01/09/2026 | 22/09/2026 | TAP aprovado + 5 planos (Áreas 1–5, incluindo 12 PDCAs e Ishikawa no Plano de Qualidade) + ADRs 001–004 + SSOT configurado | Submissão via GitHub validada pelo Prof. Dr. Nivaldo Carleto sem achados críticos |
| M2 — Ambiente e Modelagem | 23/09/2026 | 30/09/2026 | Stack FOSS definida e validada por protótipo (fase N4.1); ambiente local + CI verdes; DER e Protótipo UX/UI versionados; planos das Áreas 6–8 (Ressalva NC-04) | Pipeline CI verde; artefatos de modelagem no repositório |
| Calibração (auxiliar) | 23/09/2026 | 03/10/2026 | Baseline empírica de fluxo + ADR de metas | Baseline publicada em /docs/metricas/baseline.md |
| M3 — MVP Funcional (Beta) | 04/10/2026 | 15/11/2026 | MVP full-stack operacional, coverage ≥ 80%, UAT sem defeitos críticos/bloqueantes | Métricas de fluxo dentro da baseline calibrada |
| M4 — Encerramento | 16/11/2026 | 15/12/2026 | Documentação técnica consolidada, lições aprendidas, verificação SMART, apresentação final, tag de release | Validação acadêmica pelo Prof. Dr. Nivaldo Carleto e tag de release final |

Fonte: Elaborado pelos autores (2026). Datas idênticas em todos os artefatos.

Nota de Contexto (NC-01): o objetivo SMART de Cronograma registra "documentação consolidada" em novembro/2026, enquanto o TAP e o critério de sucesso alocam consolidação e aceite no M4 (15/12/2026). Pela regra de precedência intra-TAP (NC-00), este plano operacionaliza a leitura da seção de Marcos, sem alteração de datas: a entrega do MVP funcional que satisfaz o SMART na dimensão produto ocorre no M3 (15/11/2026, novembro); a consolidação documental acadêmica ocorre no M4. A leitura é assimilada à luz da seção de Marcos, em conformidade com o regime de freeze.

Gantt operacional via ProjectLibre: não produzido proativamente (GMV); será derivado do Kanban somente se exigido formalmente pelo Prof. Dr. Nivaldo Carleto em avaliação.

## 3.7 Controle do Cronograma (processo 6.6)

O monitoramento temporal é contínuo e nativo do SSOT (Domínio de Medição): o CFD exerce, neste plano, a função de monitoramento temporal substituto do Gantt/EVM (definição formal, cadência semanal e regra corretiva de banda 2× canonicamente na Integração §1.6.1, aqui apenas referenciadas); Cycle Time e Throughput são publicados semanalmente via GitHub Insights; o WIP em fluxo é verificado continuamente (≤ 9 cards).

Gatilhos de ação corretiva com recorte temporal (derivados da Integração §1.9):

| Gatilho | Ação corretiva | Base temporal |
| --- | --- | --- |
| Desvio > 3 dias úteis em qualquer marco M1–M4 | Issue change-request + proposta de replanejamento + ADR | Dias úteis |
| Throughput < 3 cards/semana por 2 semanas consecutivas | Revisão de WIP limits (fallback ADR-002) + reavaliação do escopo do MVP (fallback ADR-003) | Semanas |
| Banda do CFD > 2× a largura média por 2 semanas | Retrospectiva extraordinária + replanejamento do gargalo (caminho crítico empírico, §3.4) | Semanas |
| Card P0 com label blocked por > 48h | Intervenção direta do GP + resolução ou substituição da dependência | Horas corridas (NC-05) |

Fechamento de milestones: uma milestone não é fechada enquanto houver Issues abertas com label change-request ou blocked; o fechamento exige critérios atendidos, registro de lições aprendidas e comunicação ao Prof. Dr. Nivaldo Carleto quando aplicável (M1, M3, M4). Alteração de data de marco oficial exige change-request + aprovação do CCB (GP, membro único) + ADR + comunicação no marco subsequente (Integração §1.7.3); a milestone auxiliar Calibração pode ser reajustada pelo GP com registro em commit.

## 3.8 Notas de Contexto e Registro de Saneamento dos Artefatos Vivos

NC-00 — Regime de freeze do TAP e precedência intra-TAP (decisão do GP, 21/09/2026). O TAP encontra-se congelado desde o início do planejamento: não é revisado, reversionado ou corrigido ao longo do ciclo, em conformidade com seu status ontológico (Premissa P9; PMBOK® 6ª §4.1 como dicionário). Duas regras derivam: (i) precedência intra-TAP — em divergência entre seções do TAP, a seção de Marcos é canônica para matéria temporal e de marcos; (ii) locus de contexto — este documento de Planejamento detém, com precedência, as Notas de Contexto que registram a leitura operacional vigente do TAP congelado; divergências jamais são tratadas como correções do TAP. Trade-off declarado: aceita-se divergência textual entre o termo autorizativo imutável e a leitura operacional, em favor da imutabilidade da referência de autorização e da trilha auditável de interpretações. A decisão atende aos gatilhos G1 (impacto transversal), G3 (questionabilidade acadêmica) e G4 (trade-off não óbvio) da Política de ADRs → ADR-005 encaminhada para emissão antes do M2.

NC-01 — Assimilação do SMART de Cronograma à seção de Marcos. Registro e resolução da divergência: prevalece a leitura da seção de Marcos — MVP funcional no M3 (novembro/2026) e consolidação documental acadêmica no M4 (15/12/2026). Aplicada em §3.6. Nenhuma revisão do TAP é prevista ou citada (regime de freeze).

NC-02 — Numeração canônica dos processos de cronograma. Este plano adota a numeração oficial do PMBOK® 6ª edição (6.1–6.6). Divergências registradas em artefatos vivos não são replicadas aqui e constam do registro de saneamento.

NC-03 — Convenção dupla de dias e definição operacional de Cycle Time. Métricas de fluxo em dias corridos (nativo GitHub Insights); marcos, desvios e capacidade em dias úteis. A definição operacional de Cycle Time aqui vigente é In Progress → Done (ADR-003), prevalecendo sobre redações divergentes em artefatos de origem.

NC-04 — Redação do critério M2 (stack). A expressão "Stack FOSS validada (ADR-001)" foi substituída por "definida e validada por protótipo (fase N4.1)", com ressalva de que a formalização na ADR-001 está em avaliação e mudanças de stack exigem ADR específica (Escopo §2.3.4). Aplicada na Tabela 19.

NC-05 — Base temporal do gatilho de bloqueio P0. O limiar de 48h para cards P0 blocked é medido em horas corridas (evento de fluxo), distinguindo-se da base de dias úteis aplicada a desvios de marco. Aplicada em §3.7.

NC-06 — Verificação de capacidade do marco corrente. Registrada como evidência verificável a distribuição de carga do backlog M1, com todos os membros dentro do limite de 20h semanais (Premissa P5). Aplicada em §3.5.

Entendimentos sobre o TAP congelado (notas de contexto — sem saneamento):

| Matéria | Seção do TAP (congelado) | Entendimento adotado neste plano |
| --- | --- | --- |
| SMART Cronograma × consolidação no M4 | Objetivos × Marcos | NC-01: Marcos prevalecem; MVP funcional no M3, consolidação no M4 |
| Cabeçalho "EAP v2.0" | Requisitos | EAP citada sem versão interna (regra já aplicada neste plano) |
| Subnumeração das restrições | Restrições | Restrições citadas por categoria nominal + orçamento; subnumeração não presumida |
| Cycle Time "To Do → Done" | Métricas | Definição operacional In Progress → Done (ADR-003), via NC-03 |

Registro de saneamento — artefatos vivos (não bloqueante):

| Pendência | Artefato vivo | Momento previsto |
| --- | --- | --- |
| Numeração 6.3/6.5 | Base de conhecimento operacional | Próxima revisão da base |
| "Processo 6.4 Estimar Custos" → 7.2 | Glossário | Próxima revisão do Glossário |
| Grafia do stakeholder | Glossário | Próxima revisão do Glossário |
| Cycle Time "To Do → Done" → "In Progress → Done" | Glossário | Próxima revisão do Glossário |
| Contagem EAP | Glossário | Próxima revisão do Glossário |
| Convenção dupla de dias | ADR-003 / Glossário / baseline | Formalização da baseline (após 03/10) |
| Cláusula NC-00 + ADR-005 | Integração / ADR-005 | Antes do M2 |

## 3.9 Declaração de Rastreabilidade

**Tabela 20 — Rastreabilidade interna do Plano de Cronograma**

| Seção | Origem | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 3.2 (Abordagem em 3 camadas) | Governança híbrida + Marcos + Premissa P1 | Abordagem de Desenvolvimento + Planejamento | 6.1 |
| 3.3 (Definição de atividades) | EAP + Escopo §2.5 + ADR-004 | Planejamento + Trabalho do Projeto | 6.2 |
| 3.4 (Sequenciamento e caminho crítico empírico) | Marcos + ADR-002 | Planejamento + Entrega | 6.3 |
| 3.5 (Estimativa; verificação de capacidade NC-06) | Premissa P5 + Restrições + ADR-003 | Planejamento + Medição | 6.4 |
| 3.6 (Roadmap, linha de base, calibração, NC-01/NC-04) | Marcos + SMART Cronograma + Escopo §2.3.4 | Planejamento + Medição | 6.5 |
| 3.7 (Controle e gatilhos; NC-05) | Fracasso + Métricas + Integração §1.9 | Medição + Incerteza | 6.6 |
| 3.8 (Notas de Contexto; regime de freeze) | Decisão do GP + Premissa P9 | Trabalho do Projeto + Incerteza | 4.6 (dicionário) |

Verificação: 100% das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa, restrição do TAP ou decisão formal do GP; referências cruzadas apontam exclusivamente para locais canônicos (Integração §1.6.1 para CFD; Escopo §2.5/§2.6 para decomposição e gates).

## 3.10 Premissas e Restrições Aplicáveis

Premissas do TAP: P1 (governança híbrida), fundamenta §3.2; P5 (20h/semana), fundamenta §3.5; P7 (avaliador nos marcos), fundamenta §3.7; P9 (separação ontológica TAP ≠ EAP ≠ PDCA), fundamenta o regime de freeze da §3.8.

Premissas específicas deste plano: PA-1 — datas de abertura e fechamento de milestones no GitHub são marcadores administrativos do SSOT, não dias trabalhados; PA-2 — convenção dupla de dias (NC-03); PA-3 — overhead de rituais ≤ 1h/semana por membro, absorvido pela capacidade nominal; PA-4 — GitHub Insights disponível e gratuito durante todo o ciclo (TAP).

Restrições: prazo letivo inegociável e curso noturno (Restrições de Cronograma e de Recursos), fundamentam §3.5 e §3.7; orçamento zero, veta ferramentas pagas de cronograma e fundamenta a rejeição de Gantt/CPM operacionais (ADR-003); equipe de 3 pessoas com múltiplos papéis (Restrições de Recursos), fundamenta o WIP limit como regulador de capacidade.

**Controle de Versões — Seção 3**

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 21/09/2026 | Emissão inicial para o M1: abordagem em 3 camadas; caminho crítico empírico; convenção dupla de dias; FIG-1 e FIG-2 | Leonardo D. S. Setti |
| 1.1 | 21/09/2026 | Revisão crítica: Notas de Correção NC-00 a NC-06; M2 reescrito (NC-04); base temporal do gatilho P0 (NC-05); verificação de capacidade (NC-06) | Leonardo D. S. Setti |
| 1.2 | 21/09/2026 | Diretriz D3 do GP: regime de freeze do TAP formalizado (NC-00); precedência intra-TAP da seção de Marcos; §3.8 reconstituída como Notas de Contexto; supressão integral de referências a correção/revisão/saneamento do TAP; saneamento restrito a artefatos vivos; ADR-005 redefinida (regime de freeze) e mantida antes do M2 | Leonardo D. S. Setti |

**Fim da Seção 3 — Cronograma | COGME v1.2**

---

# 4 GERENCIAMENTO DOS CUSTOS DO PROJETO

**Plano de Gerenciamento de Custos**

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Versão: 1.2 · Data: 21/09/2026
Autores: Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

## 4.1 Identificação e Propósito

Este Plano de Gerenciamento de Custos estabelece os mecanismos de governança para assegurar que o projeto COGME seja executado dentro da linha de base de custos aprovada: R$ 0,00 (zero reais).

Fundamentação: Deriva diretamente das Premissas P2 (FOSS absoluto), P6 (hardware adequado) e P9 (separação ontológica TAP ≠ EAP ≠ PDCA), e das Restrições de Custo do TAP, respeitando os Domínios de Planejamento, Medição e Entrega do PMBOK® 7ª edição.

Função ontológica: O plano não duplica a auditoria de licenças (EAP N4.4) nem a seleção de stack (EAP N4.1) — estabelece a governança sobre esses artefatos, garantindo que 100% das ferramentas, bibliotecas e serviços permaneçam dentro do perímetro FOSS/Free Tier ao longo de todo o ciclo de vida.

Domínios PMBOK 7ª: Planejamento (prevenção de desvios de conformidade), Medição (métricas de conformidade como substituição de EVM) e Entrega (garantia de sustentabilidade econômica do produto).

Processo PMBOK 6ª (dicionário, obsolescência assumida conforme Integração §1.2.4): 7.1 Planejar o Gerenciamento de Custos. Os processos 7.2 (Estimar Custos), 7.3 (Determinar Orçamento) e 7.4 (Controlar Custos) são inaplicáveis no sentido tradicional, pois:

- Estimativa: não há custos a estimar (todos os recursos são gratuitos)
- Orçamento: linha de base = R$ 0,00
- Controle: métricas EVM (CPI, VAC) são matematicamente indeterminadas (AC = 0), conforme ADR-003

Trade-off declarado: Abre-se mão da formalidade de estimativa/orçamento em favor de auditoria contínua de conformidade FOSS, alinhado ao Princípio "Foco em Valor" (PMBOK 7ª) e à Restrição de orçamento zero do TAP.

## 4.2 Abordagem de Gerenciamento de Custos

O gerenciamento de custos do COGME opera em três camadas de prevenção:

| Camada | Objeto | Mecanismo de Controle | Fonte Canônica |
| --- | --- | --- | --- |
| Preventiva | Seleção de stack e ferramentas | ADR-001 + Fase N4.1 (Seleção e Validação da Stack FOSS) | ADR-001; EAP N4.1 |
| Normativa | Política de licenciamento | Whitelist/blacklist de licenças (§4.5.1) | EAP N1.4 |
| Detectiva | Auditoria de licenças | Fase N4.4 (Auditoria de Licenças) + checklist OSI-approved | EAP N4.4 |

Regra de ouro: Nenhuma ferramenta, biblioteca, API ou serviço pode ser incorporado ao projeto sem:

1. Verificação de licença OSI-approved (whitelist §4.5.1)
2. Confirmação de plano gratuito suficiente para o MVP acadêmico
3. Registro na ADR-001 ou em ADR específica (se mudança de stack)

Hierarquia de resolução de conflitos (aplicada a custos):

1. Conformidade FOSS (restrição do TAP)
2. Funcionalidade do MVP (TAP — Produto)
3. Conveniência técnica (preferência do desenvolvedor)

Figura 14 — Fluxo de Prevenção de Custos — Conformidade FOSS

**[PLACEHOLDER — IMAGEM: docs/diagramas/custos/fig-5-fluxo-prevencao-custos.svg]**

Nota: O diagrama materializa operacionalmente a governança de custo zero, demonstrando que "orçamento nulo" não constitui ausência de controle, mas governança rigorosa sobre conformidade de licenciamento. Os três gates sequenciais (Gate 1: licença OSI-approved; Gate 2: plano gratuito suficiente para MVP; Gate 3: registro em ADR-001 ou nova ADR) garantem que nenhuma dependência seja incorporada sem auditoria prévia. Desvios de qualquer gate acionam o fluxo de controle integrado de mudanças (Integração §1.7), com análise de impacto pelo GP (CCB de membro único) em ≤ 48h e registro formal via ADR quando a alteração impactar marcos ou escopo do MVP. A linha de base de custos (R$ 0,00) é imutável sem aprovação do CCB, em conformidade com a Premissa P2 (FOSS absoluto).
Fonte: Elaborado pelos autores (2026).

## 4.3 Linha de Base de Custos

Conforme o Orçamento do Projeto do TAP, a linha de base de custos é:

| Categoria | Valor Aprovado | Justificativa |
| --- | --- | --- |
| Recursos Humanos | R$ 0,00 | Esforço acadêmico voluntário (3 membros) |
| Software e Ferramentas | R$ 0,00 | 100% FOSS ou Free Tier (TAP — Inovação) |
| Infraestrutura e Hospedagem | R$ 0,00 | Ambiente local/homologação (sem cloud paga) |
| Reserva de Contingência | R$ 0,00 | Inaplicável — linha de base zero inviabiliza reserva financeira; riscos de custo mitigados por substituição FOSS (Plano de Riscos, M2) |
| Reserva de Gerenciamento | R$ 0,00 | Inaplicável — mesma razão |
| TOTAL | R$ 0,00 | Linha de base imutável sem CCB |

Regra de imutabilidade: A linha de base só pode ser alterada via change-request + aprovação do CCB (GP como membro único) + ADR + comunicação ao Prof. Dr. Nivaldo Carleto no marco subsequente (Integração §1.7.3).

Premissa crítica (P2): A disponibilidade contínua de ferramentas FOSS e Free Tier é assumida como verdadeira. Caso uma ferramenta essencial migre para modelo pago durante o projeto, aciona-se:

1. Busca imediata de alternativa FOSS equivalente
2. Se inexistente, redução de escopo (remoção da funcionalidade dependente)
3. Registro em ADR + lição aprendida

## 4.4 Estratégias de Medição e Controle

Dada a inaplicabilidade de EVM (Earned Value Management) — formalmente declarada como LEGADO na ADR-003 e na Integração §1.6.2, pois AC = 0 torna CPI e VAC matematicamente indeterminados —, o controle de custos opera por métricas de conformidade:

| Métrica | Fórmula/Definição | Meta | Frequência | Responsável |
| --- | --- | --- | --- | --- |
| % Dependências Auditadas | (Dependências com licença verificada / Total de dependências) × 100 | 100% | Por commit (CI, conforme pipeline definido no Plano de Integração) | Pipeline + GP |
| Desvios de Licenciamento | Número de dependências com licença não-OSI ou incompatível | 0 | Contínuo | GP |
| Custo Financeiro Acumulado | Soma de todos os gastos realizados | R$ 0,00 | Semanal | GP (self-report) |
| Alternativas FOSS Mapeadas | Número de ferramentas críticas com ≥ 1 alternativa FOSS identificada | ≥ 2 por ferramenta crítica | M2 | Equipe |

Gatilhos de ação corretiva:

- Se % Dependências Auditadas < 100% → bloqueio de merge até auditoria concluída
- Se Desvios de Licenciamento > 0 → remoção imediata da dependência + change-request
- Se Custo Financeiro Acumulado > R$ 0,00 → reembolso imediato pela equipe + lição aprendida

Nota sobre visibilidade de conformidade: O GitHub Dependency Graph fornece nativamente visibilidade de licenças, vulnerabilidades e dependências sem overhead documental adicional; a evidência visual será capturada diretamente do GitHub Insights quando solicitada pelo Prof. Dr. Nivaldo Carleto em avaliação.

## 4.5 Regras de Conformidade FOSS

### 4.5.1 Licenças Aprovadas (Whitelist)

Apenas as seguintes licenças são permitidas no projeto COGME, conforme ADR-001 e EAP N1.4:

| Licença | Família | Restrições |
| --- | --- | --- |
| MIT | Permissiva | Nenhuma |
| Apache 2.0 | Permissiva | Nenhuma |
| BSD (2-clause, 3-clause) | Permissiva | Nenhuma |
| GPL v2/v3 | Copyleft | Exige que derivativos também sejam GPL (aceitável para MVP acadêmico) |
| LGPL | Copyleft fraco | Incluída para completude da whitelist FOSS acadêmica; sem uso previsto no MVP |
| ISC | Permissiva | Equivalente à MIT |
| PSF (Python Software Foundation) | Permissiva | Adicionada para Python 3.11 (ADR-001) |
| Public Domain | Domínio público | Adicionada para SQLite (ADR-001) |

Licenças proibidas (Blacklist):

- ❌ Proprietárias / Comerciais
- ❌ Shareware / Freeware (sem código-fonte)
- ❌ Creative Commons (não é licença de software)
- ❌ Licenças "Source Available" não-OSI (ex: SSPL, BSL)
- ❌ Licenças com restrições de uso comercial (violam definição OSI)

### 4.5.2 Governança da Auditoria de Licenças

Delimitação de fronteiras (Área 4 vs Área 5): Este plano estabelece a governança sobre conformidade FOSS (prevenção de custos ocultos por licenciamento inadequado), enquanto o Plano de Qualidade (Área 5) governa testes automatizados, coverage ≥ 80% e UAT (REQ-08 a REQ-10). A auditoria de licenças é compartilhada operacionalmente, mas a definição de whitelist/blacklist e os gatilhos de conformidade pertencem exclusivamente a esta Área de Custos, por derivação direta da Restrição de orçamento zero do TAP.

A execução operacional da auditoria de licenças é realizada pela Fase N4.4 da EAP (conforme Plano de Escopo §2.5), fundamentada na Política de Licenciamento da Fase N1.4. Este plano não duplica procedimentos operacionais de auditoria — estabelece a governança sobre N1.4 e N4.4:

| Aspecto de Governança | Definição |
| --- | --- |
| Responsável pela execução | Equipe técnica (conforme EAP N4.4) |
| Responsável pela supervisão | GP |
| Frequência mínima | Por marco (M1–M4) + revalidação a cada nova dependência |
| Artefato de saída | /docs/dependencias/registro.md (conforme EAP N4.4) |
| Critério de aceite | 100% das dependências com licença OSI-approved verificada |
| Gatilho de escalation | Qualquer dependência não-conforme → change-request imediato (Integração §1.7) |

Figura 15 — Matriz de Rastreabilidade de Dependências — Stack FOSS Canônica

**[PLACEHOLDER — IMAGEM: docs/diagramas/custos/fig-6-matriz-rastreabilidade-dependencias.svg]**

Nota: A tabela apresenta seis exemplos reais de dependências da stack canônica (FastAPI ≥ 0.100, MIT; SQLite 3.x, Public Domain; WeasyPrint ≥ 59.0, BSD-3-Clause; pytest ≥ 7.0, MIT; GitHub Actions Free Tier, proprietário gratuito; llama.cpp 0.4.0-dev, MIT), usando ícones de conformidade, com colunas: Dependência, Versão, Licença, Conformidade, EAP N1.4/N4.4, ADR-001. Demonstra ao avaliador que "custo zero" é auditável e rastreável, não apenas declarado.
Fonte: Elaborado pelos autores (2026).

## 4.6 Gestão de Mudanças de Custos

Qualquer alteração que possa impactar a linha de base de custos (mesmo que o impacto seja R$ 0,00) segue o fluxo do Plano de Integração §1.7:

| Tipo de Mudança | Exemplo | Nível de Formalidade |
| --- | --- | --- |
| Adição de dependência FOSS | Incluir biblioteca httpx para chamadas HTTP assíncronas | Registro em commit + atualização de /docs/dependencias/registro.md |
| Troca de ferramenta FOSS | Substituir FastAPI por Flask | ADR específica (gatilho G2 — irreversibilidade prática) |
| Mudança de licença de dependência existente | Biblioteca X migra de MIT para licença proprietária | change-request + substituição imediata + ADR |
| Violação acidental de conformidade | Dependência com licença não-OSI incorporada sem auditoria | change-request + remoção + lição aprendida |

Regra de escalation: Se uma dependência crítica (ex: FastAPI, SQLite) mudar de licença para não-FOSS durante o projeto, e não houver alternativa viável:

1. GP aciona change-request imediato
2. Avalia redução de escopo (remoção da funcionalidade dependente)
3. Comunica ao Prof. Dr. Nivaldo Carleto no marco subsequente
4. Registra como risco materializado (Plano de Riscos, M2)

## 4.7 Premissas e Restrições Aplicáveis

Premissas:

- P2 (FOSS absoluto): Todas as ferramentas necessárias estão disponíveis sob licenças OSI-approved
- P6 (Hardware adequado): Não há necessidade de infraestrutura de nuvem paga
- P9 (Separação ontológica): O TAP é referência autorizativa congelada; este plano é leitura operacional que pode divergir textualmente sem constituir correção do TAP
- PA-C1 (Free Tier sustentável): APIs e serviços gratuitos (ex: GitHub Actions Free Tier) permanecem disponíveis durante todo o ciclo de vida

Restrições:

- Proibição absoluta de aquisições pagas
- Linha de base de custos = R$ 0,00 (imutável sem CCB)
- 100% das ferramentas devem ser FOSS ou Free Tier

## 4.8 Condições de Fracasso e Escalation

Derivadas do TAP, com distinção entre gatilhos de alerta preventivo (internos) e condições formais de fracasso (TAP):

| Tipo | Gatilho | Limiar | Ação | Base |
| --- | --- | --- | --- | --- |
| Alerta preventivo | Dependências não-OSI detectadas | > 5% | Auditoria emergencial + substituição ≤ 48h | GP (interno) |
| Fracasso formal | Dependências incompatíveis com FOSS | > 30% | Condição de não sucesso do projeto | TAP — Critério de Conformidade |
| Alerta preventivo | Custo financeiro > R$ 0,00 | Qualquer valor | Reembolso imediato + lição aprendida | GP (interno) |
| Alerta preventivo | Dependência crítica sem alternativa FOSS | 1 ocorrência | Redução de escopo + ADR ≤ 72h | GP + CCB |
| Fracasso formal | Falha na auditoria em 2 marcos consecutivos | 2 marcos | Revisão de processo + treinamento | GP |

Nota de reconciliação (NC-C2): O limiar de 5% é um gatilho de alerta preventivo interno, mais restritivo que a condição formal de fracasso do TAP (30%). A intenção é detectar desvios precocemente, permitindo ação corretiva antes que o limiar formal seja atingido. Trade-off: maior rigor operacional em troca de margem de segurança.

## 4.9 Declaração de Rastreabilidade

| Seção | Origem no TAP | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 4.1 (Propósito; freeze) | Orçamento + Restrições + Premissa P9 | Planejamento + Entrega | 7.1 |
| 4.2 (Abordagem) | Inovação + Restrições + EAP N1.4, N4.1 | Abordagem de Desenvolvimento | 7.1 |
| 4.3 (Linha de Base) | Orçamento Zero | Planejamento | 7.3 |
| 4.4 (Métricas) | Métricas + Orçamento + ADR-003 | Medição | 7.4 (substituição) |
| 4.5 (Conformidade FOSS) | Inovação + Restrições + ADR-001 | Entrega | 8.3 (controle aplicado) |
| 4.6 (Mudanças) | Fracasso + Riscos + Integração §1.7 | Incerteza | 4.6 + 7.4 |
| 4.8 (Fracasso) | Critério de Conformidade | Incerteza + Entrega | 7.4 |

Verificação: 100% das seções possuem rastreabilidade a ao menos uma premissa, restrição ou objetivo SMART do TAP.

## 4.10 Notas de Contexto e Registro de Saneamento dos Artefatos Vivos

NC-C1 — Inaplicabilidade de Processos 7.2–7.4 do PMBOK 6ª: Este plano declara formalmente que os processos "Estimar Custos" (7.2), "Determinar Orçamento" (7.3) e "Controlar Custos" (7.4) são inaplicáveis no sentido tradicional, pois a linha de base é R$ 0,00. O plano substitui estes processos por: (a) governança sobre conformidade FOSS (N1.4 + N4.4), (b) prevenção de desvios de licenciamento, (c) métricas de conformidade (§4.4). Esta substituição é fundamentada na ADR-003 (EVM LEGADO) e é defensável academicamente pelo Domínio de Medição do PMBOK 7ª (métricas adaptadas ao contexto) e pela Restrição de orçamento zero.

NC-C2 — Delimitação de Fronteiras (Área 4 vs Área 5 vs Escopo): A Fase N1.4 (Política de Licenciamento FOSS) e a Fase N4.4 (Auditoria de Licenças) são os artefatos canônicos de execução da conformidade FOSS. Este plano de custos estabelece exclusivamente a governança sobre N1.4 e N4.4 (whitelist/blacklist, gatilhos, métricas, escalation), sem duplicar procedimentos operacionais. Invasão de escopo prevenida por referência cruzada. O Plano de Qualidade (Área 5) governa critérios de aceite de testes (coverage ≥ 80%, UAT), não conformidade de licenças.

NC-C3 — Numeração de Processos no Glossário: A numeração canônica é: Área 7 (Custos), Processo 7.2 (Estimar Custos). Inconsistências registradas para saneamento na próxima revisão do Glossário (pós-M1).

NC-C4 — Regime de Freeze do TAP: O TAP é referência autorizativa congelada. Divergências textuais entre este plano e o TAP são leituras operacionais, não correções do termo autorizativo. Toda divergência é registrada como Nota de Contexto nesta seção.

**Controle de Versões — Seção 4**

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 21/09/2026 | Emissão inicial: abordagem de custo zero, conformidade FOSS, métricas de substituição de EVM | Leonardo D. S. Setti |
| 1.1 | 21/09/2026 | Revisão crítica: P9 e Domínio de Medição incluídos; §4.5.2 reescrita como governança sobre N4.4; NC-C4 (freeze do TAP) adicionada; reservas rejustificadas; ADR-003 referenciada; LGPL rejustificada; CCB com fonte TAP | Leonardo D. S. Setti |
| 1.2 | 21/09/2026 | Refinamento final: N1.4 adicionada como fonte canônica junto a N4.4; whitelist expandida com PSF e Public Domain (ADR-001); delimitação de fronteiras com Qualidade inserida; NC-C2 aprimorada; seção 4.8 reestruturada com distinção alerta/fracasso; Matriz de Rastreabilidade com exemplos reais da stack | Leonardo D. S. Setti |

**Fim da Seção 4 — Custos | COGME v1.2**

---

# 5 GERENCIAMENTO DA QUALIDADE DO PROJETO

**Plano de Gerenciamento da Qualidade**

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Versão: 1.1 · Data: 21/09/2026
Autores: Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

Este plano deriva diretamente das Premissas P1 (governança híbrida), P3 (SDD com IA auditável), P4 (código como deliverable), P5 (disponibilidade de 20h/semana) e P9 (separação ontológica TAP ≠ EAP ≠ PDCA), e das Restrições de Qualidade e Cronograma do TAP, respeitando os Domínios de Medição, Entrega e Melhoria do PMBOK® 7ª edição. Aplica-se o regime de freeze do TAP e as Notas de Contexto registradas na seção 5.9.

## 5.1 Identificação e Propósito

Este Plano de Gerenciamento da Qualidade estabelece os mecanismos para garantir que o COGME atenda aos critérios de aceite técnicos: cobertura de testes ≥ 80%, UAT sem defeitos críticos/bloqueantes, e aplicação sistemática de ferramentas da qualidade (12 ciclos PDCA + 3 diagramas de Ishikawa 6M).

Função ontológica: O plano não duplica gates de qualidade do Escopo §2.6 (DoR/DoD) — operacionaliza critérios técnicos de qualidade específicos para código, testes e documentação, garantindo conformidade com REQ-08, REQ-09 e REQ-10.

Domínios PMBOK 7ª: Medição (métricas de qualidade), Entrega (critérios de aceite) e Melhoria (ciclos PDCA).

Processos PMBOK 6ª (dicionário, obsolescência declarada conforme Integração §1.2.4): 8.1 Planejar o Gerenciamento da Qualidade, 8.2 Gerenciar a Qualidade, 8.3 Controlar a Qualidade.

Trade-off declarado: Abre-se mão de burocracia documental em favor de automação (pipeline CI) e melhoria contínua (PDCA por fase), alinhado ao Princípio "Foco em Valor" (PMBOK 7ª) e ao Valor Ágil "Software funcionando sobre documentação abrangente".

## 5.2 Abordagem de Gerenciamento da Qualidade

A qualidade do COGME opera em três dimensões complementares:

| Dimensão | Objeto | Mecanismo de Controle | Fonte Canônica |
| --- | --- | --- | --- |
| Preventiva | Qualidade do código e arquitetura | Code Review + SDD com IA auditável + Clean Code | Escopo §2.6 + ADR-004 |
| Detectiva | Cobertura de testes e defeitos | Pipeline CI + pytest + coverage.py ≥ 80% | REQ-08 + N6.1 |
| Corretiva | Melhoria contínua de processo | 12 ciclos PDCA (um por fase da EAP) + Ishikawa 6M | REQ-10 + N6.3 |

Regra de ouro: Nenhum card migra para Done sem: (i) pipeline CI verde, (ii) coverage ≥ 80% no módulo afetado, (iii) code review aprovado, (iv) tasklist 100% concluída (se aplicável, ADR-004).

Hierarquia de resolução de conflitos (aplicada à qualidade):

1. Critérios de aceite do TAP (coverage ≥ 80%, UAT sem defeitos críticos)
2. Clean Code e ACID (Premissa P5)
3. Conveniência técnica (preferência do desenvolvedor)

Figura 16 — Fluxo de Garantia da Qualidade

**[PLACEHOLDER — IMAGEM: docs/diagramas/qualidade/fig-01-fluxo-qualidade.svg]**

Nota: Fluxograma vertical com gates de qualidade sequenciais, destacando revisão humana para código SDD-IA e critérios binários de aprovação. Materializa visualmente o DoD técnico, demonstrando que qualidade não é inspeção final, mas processo contínuo com gates automáticos (CI) e manuais (revisão de pares).
Fonte: Elaborado pelos autores (2026).

## 5.3 Métricas de Qualidade

Dada a inaplicabilidade de EVM (ADR-003, Integração §1.6.2), o controle de qualidade opera por métricas técnicas automatizadas:

| Métrica | Fórmula/Definição | Meta | Frequência | Responsável |
| --- | --- | --- | --- | --- |
| Coverage | (Linhas testadas / Total de linhas) × 100 | ≥ 80% | Por push (CI) | Pipeline + GP |
| Defeitos Críticos | Número de bugs bloqueantes/críticos em UAT | 0 | Por marco (M3, M4) | GP + UAT |
| Taxa de Aprovação em Review | (PRs aprovados / Total de PRs) × 100 | ≥ 90% | Semanal | GP |
| Technical Debt Ratio | (Dívida técnica / Custo total) — estimado via SonarQube Free Tier | < 5% | Por marco | GP |
| Tempo de Resposta | Latência p95 das requisições da API | ≤ 3s | M3 (homologação) | Pipeline + Edson |

Nota (I5): SonarQube Free Tier é utilizado para análise estática de dívida técnica, em conformidade com o orçamento zero do TAP (proibição de ferramentas pagas). O Free Tier fornece análise básica sem custos.

Gatilhos de ação corretiva:

- Se Coverage < 80% por 2 commits consecutivos → bloqueio de merge até correção
- Se Defeitos Críticos > 0 em UAT → retrabalho imediato + congelamento de novas features
- Se Taxa de Aprovação em Review < 90% por 2 semanas → retrospectiva extraordinária + revisão de padrões de código

Nota sobre visibilidade de métricas: GitHub Insights + coverage.py + pytest já fornecem visibilidade nativa sem overhead documental; as evidências serão capturadas diretamente do GitHub Actions e relatórios de coverage quando solicitadas pelo Prof. Dr. Nivaldo Carleto em avaliação.

## 5.4 Critérios de Aceite Técnicos

### 5.4.1 Código-Fonte

| Critério | Descrição | Verificação |
| --- | --- | --- |
| Clean Code | Nomes significativos, funções ≤ 20 linhas, sem duplicação > 3 linhas | Code Review + pylint/flake8 |
| Type Safety | Type hints em 100% das funções públicas (Python 3.11+) | mypy --strict (ferramenta complementar de análise estática, não parte da stack principal ADR-001) |
| Documentação Inline | Docstrings em todas as classes e funções públicas (padrão Google) | pydocstyle |
| SDD Auditável | Commits de código gerado por IA declaram co-autoria e link para prompt | Git log + .ai/handoffs/ |

Nota (I6): mypy é ferramenta complementar de análise estática de tipos, não listada na ADR-001 (stack principal). Sua utilização é opcional e recomendada para garantir type safety, sem impacto no orçamento (FOSS, MIT License).

### 5.4.2 Testes Automatizados

| Critério | Descrição | Verificação |
| --- | --- | --- |
| Cobertura Mínima | ≥ 80% de linhas testadas (unitários + integração) | coverage.py report |
| Testes Críticos | 100% dos fluxos REQ-01 a REQ-07 cobertos | coverage branch + UAT |
| Tempo de Execução | Suíte completa em ≤ 5 minutos | GitHub Actions CI (REQ-11) |
| Isolamento | Testes não dependem de ordem de execução ou estado global | pytest --random-order |

### 5.4.3 Documentação

| Critério | Descrição | Verificação |
| --- | --- | --- |
| Rastreabilidade | 100% dos requisitos (REQ-01 a REQ-15) mapeados a cards e testes | Matriz de rastreabilidade |
| Atualização | Documentação atualizada antes do merge (código + docs no mesmo PR) | Code Review |
| Consistência | Glossário e base de conhecimento atualizados quando novos termos/decisões surgirem | Refinement semanal |

## 5.5 Ferramentas da Qualidade

### 5.5.1 Pipeline de Integração Contínua (CI)

Conforme N7.1 da EAP e REQ-11, o pipeline CI executa automaticamente a cada push:

~~~yaml
# .github/workflows/ci.yml (resumo)
name: CI Pipeline
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Lint
        run: flake8 . && mypy --strict cogme/
      - name: Test with pytest
        run: pytest --cov=cogme --cov-report=xml --cov-fail-under=80
      - name: Upload coverage
        uses: codecov/codecov-action@v3
~~~

Critérios de qualidade do pipeline:

- Execução completa em ≤ 5 minutos (REQ-11)
- Falha imediata se coverage < 80%
- Bloqueio de merge se pipeline vermelho

### 5.5.2 Ciclos PDCA por Fase da EAP

Fundamentação: Cada uma das 12 fases da EAP (N1–N12) possui um ciclo PDCA específico, garantindo melhoria contínua sem burocracia excessiva. O TAP não integra ciclos PDCA (Premissa P9).

Formato GMV: Cada PDCA é documentado em máximo 6 linhas: Problema → Ação → Responsável → Métrica → Verificação → Lição.

## 5.6 Ciclos PDCA Consolidados (12 Fases EAP)

**PDCA-N1: Iniciação e Planejamento**

| Etapa | Descrição |
| --- | --- |
| Problema | Risco de escopo mal definido ou premissas inválidas no início do projeto |
| Ação | Revisão em pares do TAP e EAP antes da submissão no M1; validação de premissas P1–P9 |
| Responsável | Leonardo (GP) + Fabricio (par) |
| Métrica | Zero inconsistências críticas identificadas pelo Prof. Dr. Nivaldo Carleto no M1 |
| Verificação | Validação acadêmica no M1 (22/09/2026) |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1-licoes.md |

**PDCA-N2: Levantamento de Requisitos**

| Etapa | Descrição |
| --- | --- |
| Problema | Requisitos ambíguos ou não rastreáveis a objetivos SMART |
| Ação | Conversão de REQ-01 a REQ-15 para formato User Story GWT (Padrão B) até M2 |
| Responsável | Edson + Leonardo (revisão) |
| Métrica | 100% dos requisitos Must (REQ-01 a REQ-09, REQ-11, REQ-15) com critérios GWT |
| Verificação | Refinement semanal (23/09, 30/09) |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1-licoes.md |

**PDCA-N3: Modelagem e Prototipação**

| Etapa | Descrição |
| --- | --- |
| Problema | Arquitetura ou DER não validados antes da implementação |
| Ação | Protótipo "Hello World" da stack (N4.1) + revisão de DER antes de N5 (Desenvolvimento) |
| Responsável | Fabricio (DER) + Edson (protótipo) |
| Métrica | Zero retrabalho de arquitetura após início de N5 |
| Verificação | Marco M2 (30/09/2026) — pipeline CI verde + DER versionado |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1-licoes.md |

**PDCA-N4: Configuração de Ambiente**

| Etapa | Descrição |
| --- | --- |
| Problema | Incompatibilidade de ferramentas FOSS ou ambiente local instável |
| Ação | Validação de stack via protótipo funcional + auditoria de licenças (N4.4) |
| Responsável | Leonardo (stack) + Edson (auditoria) |
| Métrica | 100% das dependências com licença OSI-approved (Custos §4.5) |
| Verificação | M2 (30/09/2026) — /docs/dependencias/registro.md atualizado |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1-licoes.md |

**PDCA-N5: Desenvolvimento do Sistema**

| Etapa | Descrição |
| --- | --- |
| Problema | Código sem testes, coverage insuficiente ou SDD-IA sem revisão |
| Ação | TDD quando aplicável + code review obrigatório + tasklists Markdown (ADR-004) |
| Responsável | Todos (desenvolvedores) + GP (supervisão) |
| Métrica | Coverage ≥ 80% por módulo; 100% dos commits SDD-IA com co-autoria declarada |
| Verificação | Pipeline CI verde a cada push; Code Review antes de merge |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2-licoes.md |

**PDCA-N6: Garantia da Qualidade**

| Etapa | Descrição |
| --- | --- |
| Problema | Defeitos críticos em UAT ou coverage abaixo da meta |
| Ação | UAT estruturado com roteiro de testes + Ishikawa 6M para defeitos recorrentes (seção 5.7) |
| Responsável | Edson (UAT) + GP (Ishikawa) |
| Métrica | Zero defeitos críticos/bloqueantes; coverage ≥ 80% consolidado |
| Verificação | M3 (15/11/2026) — relatório UAT + coverage.xml |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2-licoes.md |

**PDCA-N7: DevOps e CI/CD**

| Etapa | Descrição |
| --- | --- |
| Problema | Pipeline lento (> 5min, conforme REQ-11) ou instável |
| Ação | Otimização de testes paralelos + cache de dependências |
| Responsável | Leonardo (CI) + Fabricio (otimização) |
| Métrica | Tempo de CI ≤ 5 minutos (REQ-11); taxa de sucesso ≥ 95% |
| Verificação | GitHub Actions Insights (semanal) |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2-licoes.md |

**PDCA-N8: Comunicação**

| Etapa | Descrição |
| --- | --- |
| Problema | Falhas de comunicação entre equipe ou com stakeholder |
| Ação | Daily assíncrona padronizada + refinement semanal com pauta fixa |
| Responsável | GP (facilitação) + equipe (participação) |
| Métrica | 100% das dailies realizadas; zero cards bloqueados > 48h sem comunicação |
| Verificação | GitHub Issues (daily) + GitHub Projects (refinement) |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2-licoes.md |

**PDCA-N9: Base de Conhecimento**

| Etapa | Descrição |
| --- | --- |
| Problema | ADRs tardias ou prompts SDD não catalogados |
| Ação | Catálogo de prompts em .ai/handoffs/ + ADRs emitidas antes de M2 (quando aplicável) |
| Responsável | Leonardo (ADRs) + todos (prompts) |
| Métrica | 100% dos prompts versionados; ≤ 30% de ADRs tardias |
| Verificação | /docs/decisoes/ + .ai/handoffs/ (semanal) |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF3-licoes.md |

**PDCA-N10: Gestão de Mudanças**

| Etapa | Descrição |
| --- | --- |
| Problema | Mudanças não registradas ou scope creep > 15% (Escopo §2.7, Integração §1.9) |
| Ação | Label change-request obrigatória + análise de impacto em ≤ 48h (Integração §1.7) |
| Responsável | GP (CCB) + equipe (solicitações) |
| Métrica | 100% das mudanças registradas; scope creep < 15% (Escopo §2.7) |
| Verificação | GitHub Issues com label change-request |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2-licoes.md |

**PDCA-N11: Documentação do Projeto**

| Etapa | Descrição |
| --- | --- |
| Problema | Documentação desatualizada ou inconsistente com código |
| Ação | Código + docs no mesmo PR + revisão de consistência antes de M4 |
| Responsável | Todos (documentação) + GP (consolidação) |
| Métrica | 100% dos requisitos mapeados a docs; zero inconsistências TAP → código |
| Verificação | M4 (15/12/2026) — documentação consolidada |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF3-licoes.md |

**PDCA-N12: Encerramento**

| Etapa | Descrição |
| --- | --- |
| Problema | Lições aprendidas não consolidadas ou critérios SMART não verificados |
| Ação | Checklist de encerramento + lições finais + tag de release |
| Responsável | GP (consolidação) + equipe (lições) |
| Métrica | 100% dos critérios SMART verificados; lições consolidadas em /docs/conhecimento/ |
| Verificação | M4 (15/12/2026) — validação acadêmica + tag de release |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF3-licoes.md |

## 5.7 Diagrama de Ishikawa 6M (3 Análises)

Fundamentação: Conforme REQ-10 e N6.3 da EAP, três diagramas de Ishikawa 6M são aplicados para análise de causa-raiz de problemas críticos de qualidade. Cada diagrama foca em um efeito indesejado específico.

Nota sobre qualidade de processo vs. produto (I3): Os dois primeiros diagramas (Coverage < 80% e Defeitos Críticos em UAT) analisam qualidade de produto. O terceiro diagrama (Cycle Time > 3 dias) analisa qualidade de processo — especificamente, eficiência do fluxo de trabalho. Ambos os tipos são ferramentas da qualidade conforme REQ-10, e a delimitação entre eles é explicitada na seção 5.8.2.

**Ishikawa-1: Coverage < 80%**

Figura 17 — Diagrama de Ishikawa 6M: Coverage Insuficiente

**[PLACEHOLDER — IMAGEM: docs/diagramas/qualidade/fig-05-ishikawa-coverage.svg]**

Nota: Diagrama 6M (Método, Mão de Obra, Máquina, Material, Medida, Meio Ambiente) com causas-raiz específicas do COGME. Permite ao GP e equipe identificar ações corretivas priorizadas (ex: tornar coverage gate obrigatório no CI) em vez de tratar sintomas.
Fonte: Elaborado pelos autores (2026).

Ações corretivas derivadas:

- Método: Implementar TDD obrigatório para REQ-01 a REQ-07 (críticos)
- Medida: Configurar --cov-fail-under=80 no pipeline CI (gate bloqueante)
- Mão de Obra: Pair programming para módulos complexos (N5.1, N5.2)

**Ishikawa-2: Defeitos Críticos em UAT**

Figura 18 — Diagrama de Ishikawa 6M: Defeitos Críticos em UAT

**[PLACEHOLDER — IMAGEM: docs/diagramas/qualidade/fig-06-ishikawa-uat.svg]**

Nota: Diagrama 6M focado em defeitos de UAT, destacando causas relacionadas a SDD-IA e validação acadêmica. Evidencia para o Prof. Dr. Nivaldo Carleto que a equipe compreende as limitações do ambiente acadêmico (usuários-piloto limitados) e propõe mitigações (UAT estruturado).
Fonte: Elaborado pelos autores (2026).

Ações corretivas derivadas:

- Método: Roteiro de UAT com cenários Given/When/Then para REQ-01 a REQ-07
- Mão de Obra: Code review cruzado (Fabricio revisa Edson, Edson revisa Leonardo)
- Medida: Label bug-critical no GitHub com template de reporte padronizado

**Ishikawa-3: Desvio de Cycle Time > 3 dias**

Figura 19 — Diagrama de Ishikawa 6M: Cycle Time Excedido

**[PLACEHOLDER — IMAGEM: docs/diagramas/qualidade/fig-07-ishikawa-cycletime.svg]**

Nota: Diagrama 6M focado em gargalos de fluxo, conectando causas a ADR-002 (Kanban) e ADR-004 (tasklists). Demonstra ao avaliador que a equipe entende que "Cycle Time > 3 dias" não é falha individual, mas sistêmica, exigindo ações em múltiplas dimensões.
Fonte: Elaborado pelos autores (2026).

Ações corretivas derivadas:

- Método: DoR gate rigoroso (Escopo §2.6) — card sem DoR não entra em Ready
- Mão de Obra: Cross-training para reduzir dependência de membro único
- Medida: Publicação semanal de CFD (Integração §1.6.1) + ação corretiva se banda > 2× média

## 5.8 Gestão de Melhoria Contínua

### 5.8.1 Retrospectivas Quinzenais

Conforme ADR-002, retrospectivas ocorrem a cada 2 semanas com pauta fixa:

1. O que funcionou bem?
2. O que pode melhorar?
3. Ações para o próximo ciclo (máximo 3)

Registro: /docs/conhecimento/licoes-aprendidas/ (MF1, MF2, MF3)

### 5.8.2 Integração com Métricas de Fluxo

Conforme Cronograma §3.7 e Integração §1.6.1, o CFD e Cycle Time alimentam a melhoria de processo:

- CFD com banda > 2× média por 2 semanas → Retrospectiva extraordinária
- Throughput < 3 cards/semana por 2 semanas → Revisão de WIP limits (fallback ADR-002)

Fronteira com Cronograma (I4): Este plano usa métricas de fluxo como input para melhoria de qualidade de processo, não como métrica de qualidade de produto (que são coverage, defeitos, etc.). A definição formal, cadência e regra corretiva do CFD residem canonicamente em Integração §1.6.1; o monitoramento temporal detalhado reside em Cronograma §3.7.

## 5.9 Notas de Contexto e Registro de Saneamento dos Artefatos Vivos

NC-Q1 — Regime de Freeze do TAP: O TAP é referência autorizativa congelada. Divergências textuais entre este plano e o TAP são leituras operacionais, não correções do termo autorizativo.

NC-Q2 — Numeração de Processos no Glossário: A numeração canônica de custos é Área 7 (Custos), Processo 7.2 (Estimar Custos). Inconsistências registradas para saneamento na próxima revisão do Glossário (pós-M1). Processos de qualidade (8.1–8.3) verificados no Glossário.

NC-Q3 — Cycle Time e Definição Operacional: A definição operacional de Cycle Time aqui vigente é In Progress → Done (ADR-003), prevalecendo sobre redações divergentes em artefatos de origem. O saneamento aplica-se apenas aos artefatos vivos.

NC-Q4 — EAP: 12 Fases: Este plano consolida 12 ciclos PDCA (N1–N12), conforme baseline do TAP (12 fases + 37 pacotes). O TAP e Planos de Integração/Escopo são as fontes canônicas. O TAP não integra ciclos PDCA (Premissa P9).

NC-Q5 — Grafia do Stakeholder: Este plano utiliza a grafia "Prof. Dr. Nivaldo Carleto" conforme TAP. Eventuais grafias divergentes em artefatos vivos serão saneadas na próxima revisão do Glossário (pós-M1).

Registro de saneamento — artefatos vivos (não bloqueante):

| Pendência | Artefato vivo | Momento previsto |
| --- | --- | --- |
| Numeração de processos 8.1–8.3 | Glossário | Próxima revisão do Glossário |
| Contagem EAP | Glossário | Próxima revisão do Glossário |
| Cycle Time "To Do → Done" → "In Progress → Done" | Glossário | Próxima revisão do Glossário |
| Grafia do stakeholder | Glossário | Próxima revisão do Glossário |

## 5.10 Declaração de Rastreabilidade

| Seção | Origem no TAP | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 5.1 (Propósito; freeze) | Qualidade + Premissa P9 | Medição + Entrega | 8.1 |
| 5.2 (Abordagem 3 dimensões) | Qualidade + Restrições | Entrega + Melhoria | 8.2 |
| 5.3 (Métricas) | Métricas + ADR-003 | Medição | 8.3 (substituição) |
| 5.4 (Critérios técnicos) | Qualidade | Entrega | 8.3 |
| 5.5 (Ferramentas: CI) | Inovação + N7.1 | Trabalho do Projeto | 8.2 |
| 5.6 (12 PDCAs) | Qualidade + REQ-10 + N6.3 | Melhoria | 8.2 |
| 5.7 (Ishikawa 6M) | REQ-10 + N6.3 | Melhoria + Incerteza | 8.3 |
| 5.8 (Melhoria contínua) | ADR-002 + Integração §1.6.1 | Melhoria | 8.2 |
| 5.9 (Notas de Contexto) | Decisão do GP + Premissa P9 | Trabalho do Projeto | 4.6 (dicionário) |

Verificação: 100% das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa, restrição do TAP ou REQ-08/09/10; referências cruzadas apontam exclusivamente para locais canônicos (Escopo §2.6 para DoR/DoD; Custos §4.5 para auditoria FOSS; Integração §1.6.1 para CFD).

## 5.11 Premissas e Restrições Aplicáveis

Premissas do TAP:

- P1 (governança híbrida): fundamenta §5.2
- P3 (SDD com IA auditável): fundamenta §5.4.1 (código SDD)
- P4 (código como deliverable): fundamenta §5.4 (critérios técnicos)
- P5 (20h/semana): fundamenta §5.7 (Ishikawa-3: sobrecarga)
- P9 (separação ontológica TAP ≠ EAP ≠ PDCA): fundamenta §5.6 (12 PDCAs sem TAP) e §5.9 (freeze)

Premissas específicas deste plano:

- PA-Q1: GitHub Actions Free Tier permanece disponível e estável durante todo o ciclo
- PA-Q2: pytest + coverage.py são suficientes para atingir ≥ 80% de cobertura sem ferramentas pagas
- PA-Q3: Usuários-piloto (3–5 pessoas) são representativos o suficiente para UAT acadêmico
- PA-Q4: SonarQube Free Tier permanece disponível para análise de dívida técnica

Restrições:

- Qualidade: Tempo restrito para testes → priorização de fluxos críticos (REQ-01 a REQ-07)
- Cronograma: Prazo letivo inegociável → PDCAs enxutos (6 linhas cada, GMV)
- Orçamento zero: Proibição de ferramentas pagas de qualidade (ex: SonarCloud pago)

**Controle de Versões — Seção 5**

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 21/09/2026 | Emissão inicial: 12 PDCAs consolidados (N1–N12); 3 diagramas Ishikawa 6M; métricas de qualidade; exclusão de Dashboard de Métricas (GMV); NC-Q1 a NC-Q4 (freeze do TAP); delimitação de fronteiras com Custos §4.5 e Cronograma §3.7 | Leonardo D. S. Setti |
| 1.1 | 21/09/2026 | Refinamento pós-review: (I1) PDCA-N10 com referência a Escopo §2.7 e Integração §1.9; (I2) PDCA-N7 com referência a REQ-11; (I3) nota sobre qualidade de processo vs. produto na introdução §5.7; (I4) referência canônica em §5.8.2; (I5) especificação "SonarQube Free Tier" em §5.3; (I6) nota sobre mypy como ferramenta complementar em §5.4.1; (NC-Q5) grafia do stakeholder | Leonardo D. S. Setti |

**Fim da Seção 5 — Qualidade | COGME v1.1**

---

# CONTROLE DE VERSÕES GERAL DO DOCUMENTO

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 22/09/2026 | Redação Integral do Projeto — Marco M1: Introdução (TAP v3 integral, aderente ao padrão PMO) + Planos das Áreas 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade). Otimização para aderência ABNT (figuras com identificação no topo e fonte na base; tabelas numeradas). | Leonardo D. S. Setti |

