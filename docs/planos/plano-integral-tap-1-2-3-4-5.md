# COGME — CONVERSOR DE GANHOS EM MOEDA ESTRANGEIRA
## Redação Integral do Projeto — Marco M1 (Entrega Parcial Documental)

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira · Instituição: Fatec Taquaritinga — Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas · Disciplina: Gerência de Projetos · Gerente de Projeto: Leonardo David Silva Setti · Equipe: Leonardo David Silva Setti, Fabricio de Lima Cabral, Edson Luis Silva · Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto · Governança: PMBOK® 7ª edição (primária), PMBOK® 6ª edição (dicionário complementar), Kanban via GitHub Projects (execução) · Abrangência desta redação: Áreas de Conhecimento 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade).

---

# INTRODUÇÃO

O presente documento consolida a base autorizativa e os planos de gerenciamento das Áreas de Conhecimento 1 a 5 do projeto COGME, constituindo a entrega parcial documental do Marco M1 (22/09/2026). Sua abertura reproduz, de maneira integral e não subnumerada, o conteúdo do Termo de Abertura do Projeto (TAP), documento de autorização emitido em 18/09/2026 e mantido em regime de congelamento (*freeze*) desde então, nos termos da Premissa P9 e da Nota de Contexto NC-00: o TAP autoriza o projeto, não integra a Estrutura Analítica do Projeto (EAP) e não é objeto de ciclos de melhoria (PDCA).

O projeto COGME — Conversor de Ganhos em Moeda Estrangeira — é autorizado formalmente por este termo, conferindo-lhe existência oficial perante a instituição de ensino (Fatec Taquaritinga) e perante o professor orientador da disciplina de Gerência de Projetos, Prof. Dr. Nivaldo Carleto. Concede-se autoridade formal ao aluno Leonardo David Silva Setti, no papel de gerente do projeto, para aplicar os recursos organizacionais, planejar as atividades, tomar decisões e mobilizar os recursos necessários à execução do projeto, em conjunto com os demais membros da equipe. Estabelece-se o vínculo entre o projeto e os objetivos estratégicos da disciplina, demonstrando que o desenvolvimento deste sistema atende aos requisitos acadêmicos de aplicação prática dos conceitos de gerenciamento de projetos conforme o Guia PMBOK® 7ª edição (governança primária), com o Guia PMBOK® 6ª edição atuando como dicionário complementar de processos quando necessário, e a metodologia ágil Kanban como método de execução operacional via GitHub Projects. Definem-se, ainda, os limites preliminares do projeto, incluindo escopo de alto nível, premissas, restrições, riscos iniciais, cronograma de marcos e orçamento preliminar; identificam-se as principais partes interessadas e seus papéis; e institui-se este termo como documento de referência ao longo de todo o ciclo de vida do projeto.

O cenário econômico e laboral contemporâneo tem sido profundamente transformado pela consolidação do trabalho remoto e pela globalização dos contratos de prestação de serviços. No Brasil, um contingente crescente de profissionais de tecnologia, design, marketing e consultoria atua como Pessoa Jurídica (PJ) ou freelancer para empresas sediadas nos Estados Unidos, Europa e demais mercados que remuneram em moeda estrangeira (predominantemente USD e EUR). Entretanto, a gestão financeira desses ganhos apresenta uma complexidade que as ferramentas atualmente disponíveis no mercado não resolvem de maneira integrada: para obter uma estimativa confiável do valor que efetivamente receberá em moeda nacional, o profissional é forçado a consultar múltiplos sites, planilhas manuais e calculadoras dispersas, processo moroso, suscetível a erros de digitação e de interpretação de taxas, além de não oferecer visão consolidada e comparativa em tempo real das variáveis que impactam a conversão. O projeto justifica-se pela lacuna prática existente no ecossistema de software atual: não há, até o momento, solução única, gratuita e de código aberto que reúna, em um mesmo ambiente, a simulação cambial completa, a comparação entre diferentes regimes de cálculo e a emissão de documentos fiscais e financeiros associados. A determinação de utilizar exclusivamente tecnologias abertas (*open source*) é valor fundante do projeto, sustentada pelos pilares de transparência e auditabilidade, gratuidade e acessibilidade, sustentabilidade e comunidade, e alinhamento institucional com a educação pública.

**Tabela 1 — Identificação do projeto**

| Campo | Descrição |
| --- | --- |
| Projeto | COGME — Conversor de Ganhos em Moeda Estrangeira |
| Instituição | Fatec Taquaritinga — Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas |
| Disciplina | Gerência de Projetos |
| Gerente de Projeto | Leonardo David Silva Setti |
| Equipe | Leonardo David Silva Setti, Fabricio de Lima Cabral, Edson Luis Silva |
| Stakeholder-Avaliador | Prof. Dr. Nivaldo Carleto |
| Data de autorização do TAP | 18/09/2026 (versão 3 — regime de *freeze*) |

Fonte: Elaborado pelos autores (2026).

A Estrutura Analítica do Projeto (EAP), decomposição hierárquica do escopo total, é apresentada integralmente na Tabela 2, organizada em nível 0 (raiz), doze fases de nível 1 e trinta e sete pacotes de trabalho de nível 2, agrupados em três macro-fases temporais (MF1 — Fundação, MF2 — Construção, MF3 — Consolidação). A representação gráfica complementar é fornecida pelas Figuras 1 e 2.

**Tabela 2 — Estrutura Analítica do Projeto (EAP): fases e pacotes de trabalho**

| Fase (Nível 1) | Pacotes de Trabalho (Nível 2) | Macro-Fase |
| --- | --- | --- |
| N1. Iniciação e Planejamento | N1.1 Identificação de Stakeholders; N1.2 Planos de Gerenciamento; N1.3 Plano da Qualidade; N1.4 Política de Licenciamento FOSS; N1.5 Definição do Backlog e Kanban | MF1 |
| N2. Levantamento de Requisitos | N2.1 Requisitos Funcionais; N2.2 Requisitos Não Funcionais; N2.3 Casos de Uso e Histórias de Usuário | MF1 |
| N3. Modelagem e Prototipação | N3.1 Arquitetura da Solução; N3.2 Protótipo UX/UI; N3.3 Modelagem de Dados (DER) | MF1 |
| N4. Configuração de Ambiente | N4.1 Seleção e Validação da Stack FOSS; N4.2 Repositório Git + CI/CD; N4.3 Setup Local e Homologação; N4.4 Auditoria de Licenças | MF1 |
| N5. Desenvolvimento do Sistema | N5.1 Backend — Lógica de Negócio; N5.2 Backend — API de Câmbio + Cache; N5.3 Frontend — Interface e Simulações; N5.4 Módulo PDF (WeasyPrint); N5.5 SDD com IA (Prompts + Revisão) | MF2 |
| N6. Garantia da Qualidade | N6.1 Testes Unitários/Integração (≥ 80%); N6.2 Testes de Aceitação (UAT); N6.3 Aplicação de Ferramentas da Qualidade (12 PDCAs + Ishikawa 6M) | MF2 |
| N7. DevOps e CI/CD | N7.1 Pipeline CI (lint + testes) | MF2 |
| N8. Comunicação | N8.1 Matriz de Comunicação (RACI); N8.2 Canais Oficiais (GitHub, e-mail) | MF1 |
| N9. Base de Conhecimento | N9.1 ADRs (decisões arquiteturais); N9.2 Lições Aprendidas Contínuas; N9.3 Catálogo de Prompts SDD | MF1 |
| N10. Gestão de Mudanças | N10.1 Registro de Solicitações de Mudança; N10.2 Label *change-request* no GitHub; N10.3 Aprovação e Versionamento | MF2 |
| N11. Documentação do Projeto | N11.1 Documentação Técnica (Arquitetura, APIs); N11.2 Consolidação da Documentação Parcial | MF3 |
| N12. Encerramento | N12.1 Lições Aprendidas Finais; N12.2 Verificação SMART; N12.3 Apresentação Final + Aceite | MF3 |

Fonte: Elaborado pelos autores (2026), conforme TAP §4. Total: 12 fases de nível 1 + 37 pacotes de nível 2.

Figura 1 — Estrutura Analítica do Projeto (EAP): visão macro e macro-fases

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-eap-nivel-0-macro.svg]**

Nota: Representação da linha de base estrutural do escopo, canônica conforme o TAP (§4). O diagrama fracionado em camadas substitui a EAP tradicional de página única, que sofreria com sobreposições e ilegibilidade devido aos 12 níveis de fase e 37 pacotes de trabalho. A visualização hierárquica agrupa os pacotes nas três macro-fases (MF1: Fundação, MF2: Construção, MF3: Consolidação), garantindo rastreabilidade imediata entre a raiz do projeto (N0) e os entregáveis de valor.
Fonte: Elaborado pelos autores (2026).

Figura 2 — Estrutura Analítica do Projeto (EAP): visão executiva consolidada

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-01-eap-executiva.svg]**

Nota: A representação visual da EAP em visão executiva materializa o Processo 5.4 (Criar EAP/WBS) do PMBOK® 6ª edição (dicionário) e o Domínio de Planejamento do PMBOK® 7ª edição. A estrutura hierárquica apresenta a raiz N0 (COGME) no topo, decomposta em 12 fases de nível 1 (N1 a N12) agrupadas em três macro-fases temporais: MF1 — Fundação (6 fases, 20 pacotes), MF2 — Construção (4 fases, 12 pacotes) e MF3 — Consolidação (2 fases, 5 pacotes), totalizando 37 pacotes de trabalho de nível 2, conforme a linha de base canônica aprovada no TAP §4. A opção pela não abertura dos 37 pacotes nesta visão executiva preserva a legibilidade em documentos A4 e evita poluição visual, em conformidade com o princípio de Governança Mínima Viável (GMV).
Fonte: Elaborado pelos autores (2026).

Os requisitos principais das entregas, consolidados no T §5 do TAP e reproduzidos integralmente na Tabela 3, constituem a base de verificação do escopo e da qualidade. O TAP exerce provisoriamente a função de documentação de requisitos até a publicação do artefato canônico em `/docs/requisitos/requisitos.md`, prevista para o marco M2.

**Tabela 3 — Requisitos principais das entregas (REQ-01 a REQ-15)**

| ID | Requisito | Critério de Aceite | Rastreabilidade |
| --- | --- | --- | --- |
| REQ-01 | Simulação de conversão cambial em tempo real (USD/EUR → BRL) | Cotação obtida via API externa com latência ≤ 2s | TAP §3 (Produto) + N5.2 |
| REQ-02 | Suporte a 5 regimes de contratação (hora, dia, semana, mês, valor fixo) | 100% dos regimes operacionais em UAT | TAP §3 (Produto) + N5.1 |
| REQ-03 | Aplicação de encargos financeiros simulados (spread + IOF) | Cálculo auditável com precisão de 2 casas decimais | TAP §3 (Produto) + N5.1 |
| REQ-04 | Emissão de invoice em formato PDF | Geração via WeasyPrint em ≤ 3s por documento | TAP §3 (Produto) + N5.4 |
| REQ-05 | Tempo de resposta da aplicação | ≤ 3s em 95% das requisições (ambiente homologação) | TAP §3 (Produto) + N5.1 |
| REQ-06 | Interface web responsiva (FOSS) | Compatível com Chrome/Firefox/Edge (últimas 2 versões) | TAP §3 (Inovação) + N5.3 |
| REQ-07 | Cache de cotações (SQLite) | Redução de ≥ 50% das chamadas à API externa | Decisão arquitetural documentada + N5.2 |
| REQ-08 | Cobertura de testes automatizados | ≥ 80% do código (unitários + integração via pytest + coverage.py) | TAP §3 (Qualidade) + N6.1 |
| REQ-09 | Testes de aceitação (UAT) | 100% dos fluxos críticos passando, zero defeitos críticos/bloqueantes | TAP §3 (Qualidade) + N6.2 |
| REQ-10 | Aplicação de ferramentas da qualidade (PDCA + Ishikawa 6M) | 12 PDCAs consolidados + diagrama de causa e efeito documentado | TAP §3 (Qualidade) + N6.3 |
| REQ-11 | Pipeline CI funcional | Lint + testes rodando em ≤ 5 min por push | Padrão de integração contínua + N7.1 |
| REQ-12 | ADRs para decisões arquiteturais críticas | Mínimo 3 ADRs registrados (stack, Kanban, métricas) | Política de documentação técnica + N9.1 |
| REQ-13 | Rastreabilidade de prompts SDD | 100% dos prompts catalogados em .ai/handoffs/ | Política de rastreabilidade de prompts + N9.3 |
| REQ-14 | Documentação técnica consolidada | Arquitetura + APIs (OpenAPI) revisadas e aprovadas | TAP §3 (Produto) + N11.1 |
| REQ-15 | Licenciamento 100% FOSS | Todas as dependências com licenças OSI-approved | TAP §3 (Inovação) + N1.5 + N4.4 |

Fonte: Elaborado pelos autores (2026), conforme TAP §5.

O cronograma de alto nível é expresso por quatro marcos oficiais e uma milestone auxiliar de calibração, conforme Tabela 4. Em caso de divergência entre seções do TAP em matéria temporal, a seção §6 (Marcos) é canônica, nos termos da NC-00.

**Tabela 4 — Marcos do projeto**

| ID | Macro-Fase (EAP) | Descrição do Marco (Entrega de Valor) | Data Alvo | Critério de Aceite |
| --- | --- | --- | --- | --- |
| M1 | MF1: Fundação | Entrega Parcial Documental: aprovação do TAP + Planos de Gerenciamento das Áreas 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade) + 12 PDCAs consolidados + Diagrama de Ishikawa | 22/09/2026 | Documentação submetida via GitHub e validada pelo Prof. Dr. Nivaldo Carleto sem achados críticos |
| M2 | MF1: Fundação | Ambiente e Modelagem Concluídos: stack FOSS definida e validada, ambiente local/CI configurado, DER e Protótipo UX/UI aprovados | 30/09/2026 | Pipeline CI "verde" e artefatos de modelagem versionados no repositório |
| M3 | MF2: Construção | MVP Funcional (Beta): código-fonte full-stack operacional (Backend, Frontend, PDF, SDD com IA), com cobertura de testes ≥ 80% e validado em UAT local | 15/11/2026 | Zero defeitos críticos/bloqueantes; métricas de fluxo dentro da baseline |
| M4 | MF3: Consolidação | Encerramento e Aceite Final: documentação técnica consolidada, lições aprendidas, verificação dos critérios SMART e apresentação final com aceite formal | 15/12/2026 | Validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4 e repositório com tag de release final |

Fonte: Elaborado pelos autores (2026), conforme TAP §6.

As premissas (Tabela 5) e as restrições (Tabela 6) completam a base autorizativa e condicionam todos os planos subsequentes.

**Tabela 5 — Premissas do projeto (TAP §9)**

| ID | Premissa | Justificativa de Alto Nível |
| --- | --- | --- |
| P1 | Governança híbrida: PMBOK 7ª como base de princípios e domínios, PMBOK 6ª como dicionário complementar, Kanban como método de execução | Alinhamento com as diretrizes acadêmicas da disciplina |
| P2 | Projeto desenvolvido exclusivamente com tecnologias FOSS | Premissa pedagógica e de valor social |
| P3 | Uso de IA Generativa (LLMs) como apoio ao desenvolvimento (SDD) autorizado, com rastreabilidade e revisão humana | Diretrizes acadêmicas atuais de uso ético de IA |
| P4 | Código-fonte funcional (MVP full-stack) constitui deliverable formal | Natureza prática do curso de ADS |
| P5 | Equipe manterá disponibilidade média de até 20 horas semanais por membro | Capacidade realística para projeto acadêmico noturno |
| P6 | Hardware local adequado e suficiente para desenvolvimento, modelagem, testes e execução do MVP | Condição base para desenvolvimento sem nuvem paga |
| P7 | Professor Orientador atua como stakeholder-avaliador único nos marcos (M1 a M4), sem ingerência operacional; CCB delegada ao GP | Simplificação pedagógica e autonomia do GP |
| P8 | Áreas de "Aquisições" e "Gerenciamento das Partes Interessadas" tratadas com simplificação pedagógica | Foco nas 8 áreas restantes |
| P9 | Separação ontológica TAP ≠ EAP ≠ PDCA: o TAP autoriza, não integra a EAP nem é objeto de ciclos PDCA | Preservação do status autorizativo do TAP |

Fonte: Elaborado pelos autores (2026), conforme TAP §9.

**Tabela 6 — Restrições consolidadas (TAP §8 e §11)**

| Categoria PMBOK | Restrições Aplicáveis |
| --- | --- |
| Escopo | MVP acadêmico; desenvolvimento do zero |
| Cronograma | 2 bimestres (com ≈ 25% já decorrido); marco 22/09/2026; curso noturno |
| Custo | Orçamento zero; proibição de ferramentas pagas |
| Recursos | Equipe de 3 pessoas (múltiplos papéis); hardware modesto; dependência externa |
| Qualidade | Testes com tempo limitado; ambiente de validação restrito |
| Riscos | Sem plano de contingência formal; APIs gratuitas instáveis |
| Tecnológicas | FOSS/gratuito obrigatório; SDD experimental; licença open source final |

Fonte: Elaborado pelos autores (2026), conforme TAP §8 e §11.

---

# 1 GERENCIAMENTO DA INTEGRAÇÃO DO PROJETO

## 1.1 Identificação e propósito

Este Plano de Gerenciamento da Integração coordena a execução integrada do projeto COGME, garantindo que os sete planos de área subsequentes — quatro entregues no marco M1 (Escopo, Cronograma, Custos, Qualidade, além deste) e três diferidos para o marco M2 (Recursos, Comunicações, Riscos), conforme a estratégia de entrega faseada da subseção 1.7 —, o código-fonte e os artefatos de governança permaneçam coerentes com os Objetivos SMART aprovados no TAP. Sua função ontológica é complementar e subordinada ao TAP: o TAP autoriza; este plano coordena. Ele não duplica conteúdo do TAP — define os mecanismos de coerência entre todos os artefatos do ciclo de vida. Domínio PMBOK 7ª: Abordagem de Desenvolvimento. Processo PMBOK 6ª (dicionário, obsolescência assumida): 4.2 — Desenvolver o Plano de Gerenciamento do Projeto.

## 1.2 Modelo de governança híbrida e hierarquia normativa

O projeto adota um modelo trifásico de governança, declarado no TAP (§1.c) e ilustrado na Figura 3: (i) governança primária, exercida pelo PMBOK® 7ª edição (12 princípios e 8 domínios de desempenho), que define por que e para quê e orienta decisões por valor; (ii) dicionário complementar, exercido pelo PMBOK® 6ª edição, cujos processos são citados apenas para rastreabilidade acadêmica e blindagem terminológica, com obsolescência formalmente declarada para métricas preditivas (EVM); e (iii) método de execução, constituído pelo Manifesto Ágil e pelo Kanban via GitHub Projects, que define como o trabalho é executado diariamente.

**Tabela 7 — Camadas do modelo de governança híbrida**

| Camada | Fonte Normativa | Função no COGME |
| --- | --- | --- |
| Governança primária | PMBOK® 7ª edição — 12 Princípios + 8 Domínios de Desempenho | Define por que e para quê; orienta decisões por valor |
| Dicionário complementar | PMBOK® 6ª edição — processos citados apenas para rastreabilidade acadêmica | Fornece vocabulário estrutural quando necessário |
| Método de execução | Manifesto Ágil (4 valores) + Kanban (fluxo contínuo) | Define como o trabalho é executado diariamente |

Fonte: Elaborado pelos autores (2026), conforme TAP §1.c.

Figura 3 — Modelo de Governança Híbrida Trifásico

**[PLACEHOLDER — IMAGEM: docs/diagramas/integracao/fig-1-governanca-hibrida.svg]**

Nota: Ilustração da hierarquia normativa que rege o projeto COGME. A camada superior (PMBOK® 7ª) define os princípios e domínios de desempenho ("por que" e "para quê"); a camada intermediária (PMBOK® 6ª) atua estritamente como dicionário de processos, com obsolescência formalmente declarada para métricas preditivas (EVM); e a camada inferior (Kanban/Manifesto Ágil) define o método de execução operacional ("como"). A seta de realimentação representa o ciclo contínuo de lições aprendidas, blindando o projeto contra questionamentos de falta de estrutura formal.
Fonte: Elaborado pelos autores (2026).

Em caso de conflito entre fontes normativas, aplica-se a seguinte ordem de precedência: (a) valor entregue ao usuário final (Domínio de Entrega — PMBOK 7ª); (b) ementa da disciplina e orientação do Prof. Dr. Nivaldo Carleto; (c) PMBOK® 7ª edição (princípios e domínios); (d) Manifesto Ágil + Kanban (método de execução); (e) PMBOK® 6ª edição (dicionário de processos). Trade-off declarado: esta hierarquia favorece velocidade de entrega sobre completude documental, alinhada ao Princípio "Foco em Valor" (PMBOK 7ª) e ao Valor Ágil "Software funcionando sobre documentação abrangente".

Os papéis de governança são: Gerente de Projeto (Leonardo David Silva Setti), decisor operacional único e Change Control Board (CCB) de membro único, com autoridade para aprovações, rejeições e controle de mudanças; Desenvolvedores (Fabricio de Lima Cabral e Edson Luis Silva), responsáveis pela execução técnica, revisão em pares e autoavaliação de carga horária; e Stakeholder-Avaliador (Prof. Dr. Nivaldo Carleto), responsável pela avaliação acadêmica nos marcos M1–M4, sem ingerência em decisões operacionais.

Todo artefato de governança deve justificar sua existência pelo teste de Governança Mínima Viável (GMV): (a) o Prof. Dr. Nivaldo Carleto exigirá este artefato na avaliação? (b) este artefato evita retrabalho futuro? (c) este artefato é útil para a equipe (não apenas para avaliação)? Se duas ou mais respostas forem negativas, o artefato é candidato a simplificação ou eliminação, por decisão final do GP. Declara-se, ainda, a obsolescência formal do PMBOK® 6ª edição (2017) como instrumento de gestão: métricas EVM (SPI/CPI) são LEGADO — NÃO APLICÁVEIS, substituídas por métricas de fluxo Kanban conforme ADR-003.

## 1.3 Fonte única de verdade e fluxo de execução

O repositório GitHub e seu módulo GitHub Projects constituem o artefato primário de integração, cronograma e monitoramento, conforme ADR-002, substituindo qualquer ferramenta preditiva de planejamento como instrumento ativo. Justificativa: para uma equipe de 3 pessoas com fluxo contínuo, ferramentas preditivas impõem overhead de manutenção desproporcional ao valor gerado; o Kanban via GitHub Projects fornece visibilidade em tempo real, métricas nativas de fluxo e rastreabilidade automática via commits. Domínio PMBOK 7ª: Medição + Trabalho do Projeto.

**Tabela 8 — Mapeamento Kanban ↔ Processos PMBOK 6ª**

| Coluna Kanban (ADR-002) | Processo PMBOK 6ª | Domínio PMBOK 7ª | Regra Operacional |
| --- | --- | --- | --- |
| Backlog | 5.2 Coletar Requisitos | Planejamento | Card criado com DoR pendente |
| Ready (DoR) | 4.3 Orientar Trabalho (preparação) | Trabalho | DoR atendido; aguardando capacidade |
| In Progress | 4.3 Orientar e Gerenciar Trabalho | Trabalho | WIP limit: máx. 3 cards/pessoa |
| Code Review | 4.5 Monitorar e Controlar | Medição | Revisão em pares obrigatória |
| Done (DoD) | 5.4 Criar EAP (aceite do pacote) | Entrega | DoD atendido; commit mergeado |

Fonte: Elaborado pelos autores (2026), conforme ADR-002.

Figura 4 — Fluxo Kanban Oficial com gates de qualidade e WIP limits

**[PLACEHOLDER — IMAGEM: docs/diagramas/integracao/fig-2-fluxo-kanban-oficial.svg]**

Nota: O diagrama materializa operacionalmente a ADR-002 (Kanban como método de execução) e a ADR-004 (tasklists Markdown como substituto de subissues). As cinco colunas representam o fluxo contínuo do trabalho (Backlog → Ready → In Progress → Code Review → Done), com quatro gates de qualidade intermediários: (i) Gate DoR na entrada de Ready, exigindo critérios de prontidão atendidos; (ii) Gate WIP na entrada de In Progress, respeitando o limite de 3 cards por pessoa (prevenção de burnout, Domínio de Equipe PMBOK 7ª); (iii) Gate Tasklist na entrada de Code Review, exigindo 100% dos itens da tasklist Markdown concluídos (ADR-004); e (iv) Gate DoD na entrada de Done, exigindo critérios de conclusão atendidos (coverage ≥ 80%, revisão de pares aprovada, commit mergeado). O destaque vermelho sobre a coluna In Progress evidencia o WIP limit como mecanismo de controle de capacidade.
Fonte: Elaborado pelos autores (2026).

As regras de fluxo são: (a) *pull system* — cards migram para "In Progress" somente quando há capacidade disponível (WIP limit respeitado); (b) WIP limit de 3 cards em "In Progress" por pessoa (Domínio de Equipe — prevenção de burnout, R3 do TAP §10); (c) tasklists Markdown (ADR-004) — cards com estimativa ≥ 6h ou múltiplos entregáveis devem possuir tasklist no corpo da Issue (mínimo 3, máximo 7 itens; último item obrigatoriamente "Validação final"), sendo subissues reais formalmente rejeitadas, de modo que a unidade atômica de métrica e de backlog permanece o card pai, que só migra para Code Review com 100% dos itens concluídos; (d) SDD com LLM — código gerado com apoio de IA passa por revisão humana obrigatória antes do merge, com commits declarando co-autoria. Os rituais são: daily assíncrona (GitHub Issues, diária, 15 min), refinement (Product Backlog, semanal, 30 min) e retrospectiva (risk backlog + lições aprendidas, quinzenal, 30 min). Sprints time-boxed NÃO são utilizadas: o fluxo é contínuo (ADR-002).

O SSOT opera sobre três mecanismos complementares de organização. Milestones GitHub: 5 milestones — M1 (22/09), M2 (30/09), Calibração (03/10, auxiliar), M3 (15/11), M4 (15/12); cada Issue vincula-se a exatamente uma milestone, e Issues sem milestone são backlog não planejado; milestone não é fechada enquanto houver Issues abertas com label change-request ou blocked. Sistema de tags: todo card porta no mínimo 3 labels (1 tipo + 1 macro-fase + 1 área de conhecimento), habilitando filtragem, métricas de fluxo por categoria (ADR-003) e rastreabilidade TAP → EAP → Card; a taxonomia completa (27 labels em 5 categorias) reside na configuração do repositório e não é replicada neste plano (GMV). Padrão de redação (Card Ubíquo): todo card é autossuficiente — declara o quê, por quê, como será aceito e a quem pertence, sem exigir leitura de outro artefato; cards documentais seguem o Padrão A (título N{X}.{Y} — Descrição, contexto ubíquo, critérios de aceite binários, rastreabilidade dupla); cards de produto seguem o Padrão B (User Story com critérios Given/When/Then), com aplicação efetiva a partir de M2; a prioridade temporal P0–P3 complementa a classificação MoSCoW (P0 = caminho crítico do marco; P3 = postergável).

Os oito planos de área são versionados no repositório sob /docs/. Cada plano: inicia com frase de rastreabilidade ao TAP (Premissa + Restrição + Domínio PMBOK 7ª); possui extensão máxima de 4 páginas (princípio GMV); é versionado via Conventional Commits; e passa por revisão em pares antes de ser considerado "Done". Regra de coerência cruzada: nenhum plano pode contradizer datas de marcos (M1–M4), premissas (P1–P9) ou restrições (§8) do TAP; inconsistências detectadas em revisão acionam correção imediata antes do merge.

## 1.4 Governança documental: fontes canônicas e documentação transitória

O projeto utiliza documentação auxiliar de suporte à cobertura gerencial. Avaliada a árvore documental vigente, propõe-se e adota-se a seguinte classificação normativa, que rege toda citação e todo uso de conteúdo nesta redação e nos planos dela integrantes:

**Tabela 9 — Classificação documental: conjunto canônico e conjunto transitório**

| Classe | Artefatos | Valor normativo | Uso nesta redação |
| --- | --- | --- | --- |
| Canônica — nível 1 (autorizativa) | TAP v3 (congelado em 18/09/2026) | Autorização e base de referência; não integra EAP nem PDCA (P9) | Reproduzido integralmente na Introdução |
| Canônica — nível 2 (governança operacional) | OKB v3.1; Glossário v3.1; ADRs 001–004 (e ADR-005 quando emitida) | Definem mecanismos, vocabulário e decisões arquiteturais | Citados como fonte de mecanismos e termos |
| Canônica — nível 3 (planos e registros) | Planos de Gerenciamento das Áreas 1–8 (este documento); requisitos; baseline de métricas (pós-03/10); lições aprendidas | Execução do escopo autorizado | Constituem o corpo desta redação |
| Contextual (canônica por derivação) | Notas de Contexto (NC-00 a NC-06, NC-C1 a NC-C4, NC-Q1 a NC-Q5) | Registram a leitura operacional vigente do TAP congelado; divergências jamais são tratadas como correções do TAP | Mantidas nas seções 3, 4 e 5 |
| Transitória / não canônica (desprezada) | Notas adjacentes; drafts em docs/conhecimento/drafts/; arquivos [legacy] e archive/; renderizações Mermaid (.mmd.png); temporários de editor | Nenhum valor normativo; suporte histórico de raciocínio | Não citadas; não fundamentam afirmações |

Fonte: Elaborado pelos autores (2026).

Regra de uso: somente artefatos das classes canônicas e contextuais fundamentam afirmações técnicas desta redação (anti-alucinação: cada afirmação deriva de fonte verificável ou de ADR). Documentação transitória é preservada no repositório apenas como trilha histórica de raciocínio (classificação chore), sem efeito normativo e sem citação acadêmica. Em caso de conflito entre artefatos canônicos, aplica-se a hierarquia: TAP > OKB > Glossário > ADRs > Planos; e, para matéria temporal, a precedência intra-TAP da seção §6 (NC-00).

## 1.5 Monitoramento e controle integrado

Dada a restrição de orçamento zero (TAP §11), o Earned Value Management é inaplicável. As métricas de desempenho são exclusivamente baseadas no fluxo Kanban (ADR-003), conforme Tabela 10.

**Tabela 10 — Métricas de fluxo Kanban (oficiais — ADR-003)**

| Métrica | Definição | Meta (pós-calibração) | Frequência |
| --- | --- | --- | --- |
| Cycle Time | Tempo médio de um card de "In Progress" a "Done" | ≤ 3 dias | Semanal |
| Throughput | Cards concluídos por semana | ≥ 5 cards/semana | Semanal |
| CFD (Cumulative Flow Diagram) | Visualização de gargalos no fluxo | Sem bandas largas | Semanal |
| WIP em fluxo | Cards ativos em "In Progress" | ≤ 9 (3 × 3 pessoas) | Contínua |
| Coverage | Linhas testadas / linhas totais | ≥ 80% | Por push (CI) |
| Burnout (autorrelato) | Carga horária semanal declarada | ≤ 20h/pessoa | Semanal |

Fonte: Elaborado pelos autores (2026), conforme ADR-003.

Definição canônica do CFD (referência para os Planos de Cronograma e Comunicações): o Cumulative Flow Diagram é a visualização gráfica do fluxo de trabalho acumulado no tempo, onde cada banda horizontal representa uma coluna do quadro Kanban e sua largura instantânea indica a quantidade de cards naquela etapa. Fonte de dados: GitHub Insights. Responsável pela publicação semanal: GP. CFD saudável: bandas paralelas de largura constante. CFD com gargalo: bandas que se alargam progressivamente. Ação corretiva: banda com largura superior a 2× a média das demais por 2 semanas consecutivas aciona Retrospectiva extraordinária (ADR-002). A Figura 5 ilustra os dois padrões.

Figura 5 — Cumulative Flow Diagram (CFD): padrão saudável versus padrão com gargalo

**[PLACEHOLDER — IMAGEM: docs/diagramas/integracao/fig-3-cfd-saudavel-vs-gargalo.svg]**

Nota: Ferramenta visual de monitoramento temporal que substitui formalmente o Gráfico de Gantt e o Earned Value Management (EVM), declarados inaplicáveis devido ao orçamento zero e ao escopo emergente (ADR-003). O painel (a) demonstra o estado ideal de fluxo estável (bandas paralelas); o painel (b) ilustra a detecção empírica de gargalos (alargamento progressivo de uma banda). Conforme a regra de ação corretiva, se uma banda ultrapassar 2× a largura média das demais por 2 semanas consecutivas, aciona-se uma Retrospectiva extraordinária, atendendo ao Domínio de Medição do PMBOK® 7ª edição.
Fonte: Elaborado pelos autores (2026).

As métricas legado (SPI, CPI, EVM) são declaradas NÃO APLICÁVEIS: SPI é inaplicável por inexistir linha de base preditiva em fluxo contínuo; CPI é indeterminado porque o custo real é zero; EVM é inaplicável pela combinação de escopo emergente e orçamento nulo. De 23/09/2026 a 03/10/2026 decorre o período de calibração, no qual as métricas são coletadas sem meta fixa, estabelecendo a baseline empírica de desempenho real da equipe; após a calibração, metas são ajustadas com base na média observada ± 20% e formalizadas via ADR. A milestone auxiliar "Calibração" (03/10) rastreia este período no SSOT sem substituir o M2. Trade-off declarado: abre-se mão da formalidade EVM em favor de métricas acionáveis e nativas do método, conforme Domínio de Medição (PMBOK 7ª) e ADR-003.

## 1.6 Controle integrado de mudanças

O Gerente de Projeto atua como Change Control Board (CCB) de membro único, com autoridade formal delegada pelo TAP (§1.b, §9 P7). O Prof. Dr. Nivaldo Carleto não participa do fluxo de aprovação de mudanças; sua atuação restringe-se à avaliação acadêmica nos marcos M1–M4. O fluxo de solicitação de mudança compreende quatro etapas (Tabela 11) e é ilustrado na Figura 6.

**Tabela 11 — Fluxo de solicitação de mudança**

| Etapa | Ação | Responsável | Prazo |
| --- | --- | --- | --- |
| 1 | Abertura de GitHub Issue com label change-request | Qualquer membro da equipe | Imediato |
| 2 | Análise de impacto (escopo, prazo, qualidade) | GP (Leonardo) | ≤ 48h |
| 3 | Aprovação ou rejeição via comentário na Issue | GP (Leonardo) | ≤ 24h após análise |
| 4 | Atualização do backlog + planos afetados + commit | Equipe | ≤ 24h após aprovação |

Fonte: Elaborado pelos autores (2026).

Figura 6 — Fluxo de Controle Integrado de Mudanças

**[PLACEHOLDER — IMAGEM: docs/diagramas/integracao/fig-4-controle-mudancas.svg]**

Nota: Materialização do Processo 4.6 do PMBOK® 6ª (dicionário) adaptado ao fluxo contínuo Kanban. O diagrama evidencia o CCB de membro único (Gerente de Projeto), os SLAs de resposta (≤ 48h para análise, ≤ 24h para decisão) e a bifurcação de tratamento: mudanças simples são resolvidas via commit e atualização do backlog, enquanto alterações de marco ou escopo do MVP exigem registro formal via ADR e comunicação ao avaliador no marco subsequente.
Fonte: Elaborado pelos autores (2026).

Limiar de formalidade: mudanças que NÃO alteram marcos (M1–M4) nem escopo do MVP são aprovadas pelo GP com registro em commit e comentário na Issue; mudanças que ALTERAM marcos ou escopo do MVP são aprovadas pelo GP com registro formal via ADR e comunicação ao Prof. Dr. Nivaldo Carleto no marco de avaliação subsequente. Valor Ágil aplicado: "Responder a mudanças sobre seguir um plano" — o processo é leve, mas auditável.

## 1.7 Estratégia de entrega faseada e encerramento

Conforme o princípio de Elaboração Progressiva (PMBOK 6ª, dicionário) e a Personalização/Tailoring da Abordagem de Desenvolvimento (PMBOK 7ª), a entrega dos planos de gerenciamento é faseada: M1 (22/09/2026) contempla Integração, Escopo, Cronograma, Custos e Qualidade (Áreas 1–5), como fundação documental mínima viável e atendimento integral ao critério de aceite do TAP §6; M2 (30/09/2026) contempla Recursos, Comunicações e Riscos (Áreas 6–8), redigidos após a calibração do fluxo Kanban (23/09–03/10), com dados empíricos de capacidade da equipe. Trade-off declarado: redução de aproximadamente 30% da carga documental do M1, permitindo foco na qualidade dos cinco planos fundamentais e na configuração do SSOT.

Os critérios de encerramento por macro-fase são: MF1 (01/09–30/09/2026) — TAP aprovado, 5 planos submetidos no M1, 3 planos até o M2, EAP sincronizada, stack definida (ADR-001), ambiente e CI configurados; MF2 (01/10–15/11/2026) — MVP funcional, coverage ≥ 80%, UAT aprovado, pipeline CI verde, baseline calibrada; MF3 (16/11–15/12/2026) — documentação consolidada, apresentação final, validação acadêmica no marco M4, tag de release. O encerramento formal do projeto exige: tag de release final no repositório; lições aprendidas finais consolidadas; verificação dos cinco Objetivos SMART do TAP §3; e validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4.

## 1.8 Condições de fracasso e escalation

Derivados do TAP §3.3, os seguintes gatilhos acionam ação corretiva imediata pelo GP: desvio > 3 dias úteis em qualquer marco (M1–M4) — Issue change-request + proposta de replanejamento + ADR; coverage < 70% por 2 semanas consecutivas — revisão de prioridade de testes + ajuste de escopo; burnout detectado (> 20h/semana por 2 semanas) — redução de WIP + redistribuição de cards; scope creep > 15% do backlog original — congelamento de novas features + CCB; throughput < 3 cards/semana por 2 semanas consecutivas — revisão de WIP limits (fallback ADR-002) + reavaliação do escopo do MVP (fallback ADR-003); MVP não funcional em homologação até M3 — contingência técnica com redução de escopo não crítico. A escalation ao Prof. Dr. Nivaldo Carleto ocorre apenas nos marcos de avaliação ou quando o GP identificar risco de não cumprimento dos critérios SMART do TAP §3.

## 1.9 Declaração de rastreabilidade

**Tabela 12 — Rastreabilidade interna do Plano de Integração**

| Seção | Origem no TAP | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 1.2 (Governança) | §1.c + Premissa P1 | Abordagem de Desenvolvimento | 4.1, 4.2 |
| 1.3 (SSOT + milestones + cards) | Premissa P1 + §3 (Métricas) | Medição + Trabalho | 4.3, 4.5 |
| 1.4 (Governança documental) | §1.c + Premissa P9 | Trabalho do Projeto | 4.4 |
| 1.5 (Monitoramento) | §3 (Métricas) + §11 (Orçamento zero) | Medição | 4.5 |
| 1.6 (Mudanças) | §3.3 (Fracasso) + Premissa P7 | Incerteza | 4.6 |
| 1.7 (Entrega faseada + encerramento) | §6 (Marcos M1–M4) | Abordagem de Desenvolvimento + Entrega | 4.2, 4.7 |
| 1.8 (Escalation) | §3.3 (Fracasso) + §10 (Riscos) | Incerteza | 4.5, 4.6 |

Fonte: Elaborado pelos autores (2026). Verificação: 100% das seções possuem rastreabilidade a ao menos uma premissa, restrição ou objetivo SMART do TAP.

---

# 2 GERENCIAMENTO DO ESCOPO

## 2.1 Identificação e propósito

Este Plano de Gerenciamento do Escopo define os mecanismos pelos quais o escopo do COGME é coletado, declarado, decomposto, validado e controlado ao longo do ciclo de vida. Sua função ontológica é complementar e subordinada ao TAP: o TAP autoriza o escopo de alto nível, a EAP o decompõe estruturalmente e este plano governa a evolução de ambos, garantindo coerência com os Objetivos SMART aprovados. Em conformidade com a Premissa P9, o TAP não integra a EAP nem é objeto de ciclos PDCA; este plano e a EAP, por sua vez, integram a estrutura de execução e melhoria contínua do projeto. O plano ancora-se no Domínio de Planejamento e no Domínio de Entrega do PMBOK® 7ª edição e, como dicionário complementar com obsolescência formalmente declarada, nos processos 5.1 a 5.6 do PMBOK® 6ª edição. Este documento é entregável do marco M1, conforme a estratégia de entrega faseada (Seção 1.7).

## 2.2 Abordagem híbrida e gestão de requisitos

Conforme a Premissa P1 e a ADR-002, o escopo é gerenciado em duas camadas complementares: a linha de base estrutural, materializada pela EAP aprovada no TAP §4, que define o escopo obrigatório do MVP acadêmico; e o fluxo emergente, operacionalizado pelo backlog Kanban no GitHub Projects, que define a ordem de execução e permite evolução progressiva sem sprints time-boxed. O trade-off declarado privilegia a completude acadêmica, garantida pela EAP, em detrimento da rigidez preditiva, e assegura adaptabilidade por meio do fluxo contínuo. Qualquer alteração fora da linha de base aciona o controle integrado de mudanças (Seção 1.6).

Os requisitos foram coletados por duas técnicas complementares, em conformidade com o processo 5.2 do PMBOK® 6ª: análise de domínio, conduzida a partir da dor do público-alvo — profissionais brasileiros que prestam serviços ao exterior em moeda estrangeira — e do mapeamento das ferramentas dispersas hoje utilizadas para simulação cambial; e brainstorm estruturado da equipe, do qual derivaram as quinze necessidades consolidadas como requisitos (Tabela 3). A combinação é justificável pelo contexto acadêmico, que dispensa técnicas de maior formalidade, em conformidade com o princípio GMV. Os requisitos REQ-01 a REQ-15 foram formalizados com critério de aceite mensurável, rastreabilidade ao TAP e vínculo à fase da EAP, formato suficiente para o marco M1; a conversão para o formato canônico de User Story — "Como [papel], quero [ação], para [benefício]", com critérios de aceite Given/When/Then — será realizada a posteriori, até o marco M2 (30/09/2026), conforme fase N2.3 da EAP, utilizando o Padrão B de redação de cards.

O escopo inclui, como requisito formal (REQ-12 e REQ-13), a utilização de Specification-Driven Development (SDD) com apoio de Inteligência Artificial Generativa, conforme a Premissa P3. A abordagem SDD opera sobre a stack local canônica do projeto — llama.cpp como motor de inferência, modelo Qwen 32B e OpenCode como interface de desenvolvimento —, garantindo custo zero e conformidade FOSS em aderência à Premissa P2. A formalização da stack na ADR-001 encontra-se em avaliação e poderá sofrer atualizações de impacto relevante; a inclusão, a exclusão ou a troca de ferramentas, modelos ou motores exigirá ADR específica, conforme a política de ADRs do projeto e o fluxo de mudanças da Seção 1.6. O detalhamento operacional — prompts, personas e handoffs — reside no Catálogo de Prompts SDD (fase N9.3, diretório .ai/handoffs/) e nas ADRs (fase N9.1).

A priorização opera em duas camadas distintas e complementares: a classificação de valor de escopo aplica o método MoSCoW aos requisitos (Must: REQ-01 a REQ-09, REQ-11 e REQ-15; Should: REQ-10, REQ-12, REQ-13 e REQ-14; Could e Won't: vazias, registrando a última as exclusões da subseção 2.3); a classificação de urgência temporal aplica a escala P0–P3 aos cards do backlog, sendo P0 o caminho crítico do marco e P3 o item postergável. Ambas são aplicadas e revisadas no refinement semanal.

## 2.3 Declaração de escopo e fronteira

Em respeito ao princípio GMV e para evitar proliferação documental, a Declaração de Escopo é consolidada neste plano, em vez de constituir artefato separado. A fronteira do escopo é apresentada na Tabela 13; a coluna de exclusões é fundamentada no princípio YAGNI (You Aren't Gonna Need It), em conformidade com a restrição de escopo do TAP §8.1: funcionalidades não essenciais ao MVP acadêmico são explicitamente excluídas do ciclo atual, podendo ser reconsideradas apenas mediante solicitação formal de mudança (Seção 1.6). Esta exclusão explícita operacionaliza a restrição de MVP e previne scope creep por acréscimo incremental não autorizado.

**Tabela 13 — Fronteira do escopo (IN / OUT)**

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

Fonte: Elaborado pelos autores (2026), com base no TAP §3 e §8.

O escopo será considerado aceito quando: todos os requisitos da classe Must estiverem operacionais em UAT; a cobertura de testes atingir oitenta por cento, validada via integração contínua; não houver defeitos críticos ou bloqueantes; cem por cento das dependências possuírem licenças aprovadas pela Open Source Initiative; e houver validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4. Para prevenir invasão de contexto, declara-se que não compõem o escopo deste plano: (a) diagramas UML completos, sendo a arquitetura da solução (fase N3.1) documentada por diagrama de componentes em Markdown ou PlantUML; (b) o Diagrama Entidade-Relacionamento, produzido na fase N3.3 e versionado no repositório; (c) a estrutura de diretórios do repositório, documentada no README.md na fase N5; e (d) os arquivos de configuração do pipeline, versionados em .github/workflows/ na fase N7.1.

## 2.4 Estrutura Analítica do Projeto e regras de decomposição

A EAP aprovada no TAP §4 constitui a linha de base estrutural do escopo: nível 0 (raiz COGME), doze fases de nível 1 (N1 a N12), trinta e sete pacotes de trabalho de nível 2 e três macro-fases (MF1 Fundação, MF2 Construção, MF3 Consolidação), conforme Tabela 2 e Figuras 1 e 2. O detalhamento gráfico por macro-fase é fornecido pelas Figuras 7, 8 e 9.

Figura 7 — Detalhamento da Macro-Fase 1 (MF1): Fundação

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-eap-mf1-fundacao.svg]**

Nota: Decomposição dos pacotes de trabalho de nível 2 referentes à iniciação, planejamento, levantamento de requisitos, modelagem, configuração de ambiente, comunicação e base de conhecimento. Esta camada sustenta os entregáveis do Marco M1 (22/09/2026), incluindo os 5 planos de gerenciamento iniciais e a configuração do SSOT (GitHub Projects), em conformidade com o Domínio de Planejamento do PMBOK® 7ª edição.
Fonte: Elaborado pelos autores (2026).

Figura 8 — Detalhamento da Macro-Fase 2 (MF2): Construção

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-eap-mf2-construcao.svg]**

Nota: Decomposição dos pacotes de trabalho focados na execução técnica: desenvolvimento do sistema (incluindo SDD com IA), garantia da qualidade (meta de coverage ≥ 80%), DevOps/CI/CD e gestão de mudanças. Esta camada materializa o Domínio de Entrega e sustenta o Marco M3 (15/11/2026), onde o MVP funcional deve estar operacional e validado em UAT.
Fonte: Elaborado pelos autores (2026).

Figura 9 — Detalhamento da Macro-Fase 3 (MF3): Consolidação

**[PLACEHOLDER — IMAGEM: docs/diagramas/eap/fig-eap-mf3-consolidacao.svg]**

Nota: Decomposição dos pacotes de trabalho finais, abrangendo a consolidação da documentação técnica e o encerramento formal do projeto. Esta camada garante a rastreabilidade dos critérios de aceite do Marco M4 (15/12/2026), incluindo a verificação SMART e a validação acadêmica final, alinhada ao Domínio de Entrega do PMBOK® 7ª edição.
Fonte: Elaborado pelos autores (2026).

Nota de canonicidade (decisão do GP, 20/09/2026): a linha de base da EAP é canônica no TAP §4. O TAP e o Plano de Integração constituem as fontes canônicas de autorização e de coordenação do projeto. O Glossário é artefato terminológico volátil, atualizado a cada rodada de redação dos planos, e não constitui linha de base: eventuais divergências de contagem de fases ou pacotes são resolvidas pela prevalência do TAP, sem necessidade de solicitação de mudança. A contagem de treze fases e quarenta e oito pacotes registrada em versão anterior do Glossário não corresponde à linha de base aprovada e será corrigida na próxima revisão do próprio Glossário.

Três regras de governança aplicam-se à decomposição. Primeira: nenhum pacote de trabalho pode ser adicionado, removido ou renomeado sem aprovação formal via change-request. Segunda: cada pacote de nível 2 decompõe-se em cards Kanban com esforço estimado inferior ou igual a oito horas, redigidos conforme os Padrões A (documental) ou B (User Story GWT). Terceira: quando necessário à execução, o card decompõe-se em atividades derivadas — ações verbais que detalham a entrega substantiva, em conformidade com o processo 6.2 do PMBOK® 6ª (dicionário) — materializadas como tasklist Markdown no corpo da Issue, conforme a ADR-004, que rejeita formalmente subissues. A cadeia completa é representada na Figura 10.

Figura 10 — Cadeia de decomposição do escopo e gates de qualidade

**[PLACEHOLDER — IMAGEM: docs/diagramas/escopo/fig-2-cadeia-decomposicao-escopo.svg]**

Nota: O diagrama materializa a operacionalização do Processo 6.2 (Definir Atividades) do PMBOK® 6ª edição (dicionário) no método Kanban adotado pelo COGME (ADR-002). A cadeia de decomposição apresenta três níveis encadeados horizontalmente: (i) Pacote de Trabalho EAP de nível 2 — entrega substantiva (ex.: N5.1 — Backend: Lógica de Negócio), com rastreabilidade à fase, macro-fase, requisitos e domínio PMBOK 7ª; (ii) Card Ubíquo Kanban — unidade atômica de backlog e de métrica (≤ 8h), redigido conforme os Padrões A ou B, com contexto ubíquo autocontido e critérios de aceite binários; (iii) Atividades Derivadas como Tasklist Markdown — checklist nativo do GitHub (3 a 7 itens verbais, último item obrigatoriamente "Validação final"), conforme ADR-004, que rejeita formalmente subissues. Os gates de qualidade anotados entre os níveis são: Gate DoR na entrada da coluna Ready; Gate Tasklist + Revisão de Pares na entrada da coluna Code Review (exigindo 100% dos itens da tasklist concluídos); e Gate DoD na entrada da coluna Done. A anotação lateral destaca que as métricas de fluxo (Cycle Time, Throughput, CFD) medem exclusivamente o card pai (ADR-003), preservando a unidade atômica de métrica e evitando distorção por fragmentação.
Fonte: Elaborado pelos autores (2026).

Em conformidade com a Premissa P9, a EAP e seus pacotes integram a estrutura de ciclos PDCA do projeto (doze ciclos, um por fase), enquanto o TAP permanece como documento de autorização, não gerenciado.

## 2.5 Definition of Ready e Definition of Done

Em conformidade com o Domínio de Entrega e o Domínio de Medição do PMBOK® 7ª, formalizam-se os gates de qualidade do fluxo Kanban. O DoR, gate de entrada, exige que o card possua: título padronizado no formato N{X}.{Y} — Descrição; contexto ubíquo autocontido; critério de aceite mensurável; rastreabilidade à fase da EAP e ao requisito do TAP; estimativa de esforço inferior ou igual a oito horas; dependências identificadas; responsável atribuído; no mínimo três labels (tipo, macro-fase e área de conhecimento); milestone vinculada; e revisão no refinement semanal. Cards documentais seguem o Padrão A e cards de produto seguem o Padrão B.

O DoD, gate de saída, exige que: (1) o código esteja implementado e commitado em feature branch; (2) os testes unitários estejam escritos com cobertura do módulo superior ou igual a oitenta por cento; (3) o pipeline de integração contínua esteja verde; (4) o Code Review tenha sido aprovado por pelo menos um par; (5) a documentação esteja atualizada, quando aplicável; (6) o card tenha sido movido para Done com data registrada; (7) se o código foi gerado com apoio de SDD, o commit declare co-autoria, conforme o Critério de Inovação Controlada do TAP §3.2.e; e (8) se o card possuir tasklist Markdown no corpo da Issue (conforme ADR-004), cem por cento dos itens estejam marcados como concluídos. Artefatos em status pair-review ou in-review não satisfazem o DoD e permanecem na coluna Code Review até a conclusão da revisão. O gate de tasklist (item 8) é definido canonicamente neste plano e referenciado pelo Plano de Integração (Seção 1.3) como regra de migração de fluxo — a Integração sinaliza o ponto de controle sem duplicar o conteúdo do DoD, em conformidade com a fronteira de escopo entre as duas áreas.

## 2.6 Validação, controle e mudanças de escopo

Os processos 5.5 (Validar o Escopo) e 5.6 (Controlar o Escopo) do PMBOK® 6ª são operacionalizados por rituais Kanban, conforme a ADR-002. A validação ocorre por Code Review e por User Acceptance Testing no marco M3, com evidência em Pull Request aprovado e relatório de UAT. O controle ocorre por refinement semanal e por análise do Cumulative Flow Diagram, cuja definição formal, cadência e regra de ação corretiva residem no Plano de Integração (Seção 1.5), com evidência no GitHub Projects e no GitHub Insights. A prevenção de scope creep aciona alerta quando o backlog cresce superior a quinze por cento em relação à linha de base de trinta e sete pacotes da EAP; nesse caso, o GP congela novas features, analisa o impacto via change-request e decide em até quarenta e oito horas. A métrica de controle é o Throughput semanal superior ou igual a cinco cards; se inferior a três cards por semana durante duas semanas consecutivas, o escopo é revisado conforme o fallback da ADR-003.

Qualquer alteração de escopo segue o fluxo do Plano de Integração (Seção 1.6): abertura de Issue com label change-request, análise de impacto pelo GP em até quarenta e oito horas, aprovação ou rejeição em até vinte e quatro horas e atualização do backlog, da EAP quando aplicável, e commit. Mudanças que alterem marcos (M1–M4) ou o escopo do MVP exigem registro formal via ADR e comunicação ao Prof. Dr. Nivaldo Carleto no marco de avaliação subsequente. A inclusão, exclusão ou renomeação de pacotes da EAP enquadra-se sempre neste limiar de formalidade. Mudanças na stack tecnológica — incluindo a stack SDD, conforme subseção 2.2 — seguem o mesmo fluxo e exigem ADR específica quando atendidos os gatilhos da política de ADRs do projeto.

## 2.7 Aceite, fracasso e rastreabilidade

Remetem-se aos critérios da subseção 2.3, acrescidos da verificação de que cem por cento dos requisitos da classe Must possuam rastreabilidade documentada a Objetivo SMART, fase da EAP e card do backlog. Derivados do TAP §3.3, os seguintes gatilhos específicos acionam ação corretiva: (a) requisito Must não implementado até M3, com contingência de redução de escopo Should; (b) EAP com mais de quinze por cento de pacotes não iniciados até M2, com replanejamento e ADR; (c) UAT com defeito crítico ou bloqueante, com retrabalho imediato e congelamento de novas features; (d) scope creep superior a quinze por cento, com congelamento e decisão do CCB; e (e) cobertura de requisitos inferior a cem por cento dos Must, com bloqueio do M3.

**Tabela 14 — Rastreabilidade interna do Plano de Escopo**

| Seção | Origem | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 2.2 (Abordagem híbrida + requisitos) | TAP §1.c + §3 + §5 + Premissas P1, P3 | Planejamento + Entrega | 5.1, 5.2 |
| 2.3 (Declaração de Escopo + fronteira) | TAP §3 + §8 + Premissa P2 | Entrega | 5.3 |
| 2.4 (EAP e decomposição; canonicidade) | TAP §4 + Premissa P9 | Planejamento | 5.4 + 6.2 (dicionário) |
| 2.5 (DoR/DoD) | TAP §3 (Qualidade) + §3.2.e | Entrega + Medição | 5.5 |
| 2.6 (Validação/controle/mudanças) | TAP §3 (Métricas) + §3.3 + Premissa P7 | Medição + Incerteza | 5.5, 5.6, 4.6 |
| 2.7 (Aceite/fracasso) | TAP §3.2 + §3.3 + §10 | Incerteza + Entrega | 5.5, 5.6 |

Fonte: Elaborado pelos autores (2026). Verificação: cem por cento das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa ou restrição do TAP; a fronteira OUT é adicionalmente fundamentada no princípio YAGNI; o gate de tasklist possui rastreabilidade cruzada com a ADR-004 e o Plano de Integração §1.3.

---

# 3 GERENCIAMENTO DO CRONOGRAMA

## 3.1 Identificação e propósito

Este Plano de Gerenciamento do Cronograma define como o tempo do projeto COGME é estruturado, estimado, consolidado e controlado. Sua função ontológica é complementar e subordinada ao TAP como fonte autorizativa: o TAP fixa os marcos M1–M4 (§6), o Plano de Escopo decompõe o trabalho em pacotes e cards (Seção 2.4) e este plano governa o sequenciamento, a estimativa e o controle temporal entre ambos, sem duplicar o roadmap nem os gates DoR/DoD (Seção 2.5). Canonicidade e regime de freeze: o TAP encontra-se congelado desde o início do planejamento — sua última versão (18/09/2026) precede os planos de gerenciamento e não é objeto de revisão ao longo do ciclo, em conformidade com seu status ontológico já declarado (Premissa P9; PMBOK® 6ª §4.1, dicionário). Em caso de divergência entre seções do TAP, a seção §6 (Marcos) é canônica para matéria temporal (NC-00). Domínios PMBOK 7ª: Planejamento e Medição. Processos PMBOK 6ª (dicionário): 6.1 a 6.6.

## 3.2 Abordagem em três camadas e definição das atividades

O cronograma é gerenciado em três camadas temporais distintas, materializando a Personalização da Abordagem de Desenvolvimento (PMBOK 7ª) e a ADR-002: (a) camada macro — marcos M1–M4, com datas fixas do TAP §6, alteráveis somente via change-request + ADR + comunicação, inegociáveis sem CCB; (b) camada meso — macro-fases MF1–MF3 e milestone auxiliar Calibração, com períodos declarados e gates de fechamento entre macro-fases, ajustáveis apenas via CCB; (c) camada operacional — cards Kanban (≤ 8h), em fluxo contínuo pull, com WIP de 3 cards/pessoa, sem sprints e sem datas por atividade, emergente e refinada semanalmente. Aplica-se o planejamento em ondas sucessivas (elaboração progressiva, PMBOK 6ª como dicionário): o detalhe operacional emerge no refinement semanal, enquanto apenas as camadas macro e meso são objeto de controle formal de mudanças. Não existe linha de base preditiva de datas por pacote: a única linha de base temporal formal é o conjunto {marcos M1–M4 + macro-fases MF1–MF3 + milestone auxiliar Calibração}. Trade-off declarado: abre-se mão da previsibilidade preditiva por atividade em favor de confiabilidade empírica no nível do marco, alinhado ao Domínio de Medição (PMBOK 7ª), à ADR-003 e ao valor ágil "Responder a mudanças sobre seguir um plano".

A cadeia de decomposição temporal é idêntica à cadeia de decomposição do escopo (Figura 10): os 37 pacotes de trabalho de nível 2 da EAP decompõem-se em cards Kanban com esforço ≤ 8h, e estes, quando ≥ 6h ou com múltiplos entregáveis, decompõem-se em atividades derivadas materializadas como tasklist Markdown (3 a 7 itens; último item obrigatoriamente "Validação final"), conforme ADR-004, que rejeita formalmente subissues. Regras operacionais: (i) a unidade atômica de cronograma e de métrica temporal é o card pai (ADR-003 e ADR-004); itens de tasklist não geram previsão nem métrica própria; (ii) nenhum card migra para Ready sem estimativa de esforço e dependências identificadas (DoR, Seção 2.5); (iii) cards estimados acima de 8h são obrigatoriamente divididos antes de entrar no fluxo.

## 3.3 Sequenciamento e dependências

Conforme a ADR-003, não se constrói rede de precedências CPM no nível operacional: em fluxo contínuo com escopo emergente, uma rede de atividades ficaria obsoleta em dias, violando o princípio GMV. O sequenciamento opera por quatro mecanismos nativos do SSOT: (a) campo "Dependências" dos Padrões A e B de redação de cards; (b) gate DoR "dependências identificadas" (Seção 2.5); (c) label blocked com registro obrigatório da dependência no corpo da Issue; (d) regra P0: card que, ausente, impede o marco ou bloqueia dois ou mais outros cards integra o caminho crítico empírico. O caminho crítico é identificado empiricamente pela combinação de cards P0, alargamentos de banda no CFD e desvios de Cycle Time — definição formal, cadência e regra corretiva canonicamente na Seção 1.5 —, revisada a cada refinement semanal e a cada retrospectiva quinzenal. No nível macro, o sequenciamento é finish-to-start entre macro-fases, com gates explícitos: o M2 encerra a MF1; a milestone auxiliar Calibração (03/10/2026) libera a baseline empírica que autoriza metas na MF2; o M3 encerra a MF2; o M4 encerra a MF3. Dentro de cada macro-fase, o paralelismo é integral, gerenciado por pull system e WIP limits (TAP §6). A Figura 11 ilustra o modelo.

Figura 11 — Sequenciamento macro e caminho crítico empírico

**[PLACEHOLDER — IMAGEM: docs/diagramas/cronograma/fig-01-sequenciamento-macro-caminho-critico.svg]**

Nota: O diagrama ilustra a substituição da rede de precedências preditiva (CPM/Gantt) por um modelo de detecção empírica de gargalos, em estrita conformidade com a ADR-003 e o Domínio de Medição do PMBOK® 7ª edição. Os quatro detectores operacionais (cards P0, label blocked, alargamento de bandas no CFD e desvio persistente de Cycle Time) alimentam diretamente os rituais de refinement semanal e retrospectiva quinzenal. O feedback gerado promove o replanejamento e o ajuste de prioridades sem violar os gates de controle das macro-fases (MF1 a MF3), garantindo a governança do fluxo contínuo e a blindagem acadêmica contra a exigência de métricas EVM inaplicáveis.
Fonte: Elaborado pelos autores (2026).

## 3.4 Estimativa de esforço, duração e capacidade

Esforço é estimado em horas pelo responsável técnico (julgamento de especialista), com classificação relativa T-shirt (PP ≤ 2h, P ≤ 4h, M ≤ 6h, G = 8h) como verificação cruzada. As faixas são binárias quanto à governança: cards ≤ 4h são atômicos e não portam tasklist; cards ≥ 6h portam tasklist obrigatória; o teto absoluto é 8h (ADR-004; Seção 2.4). Capacidade semanal nominal: 3 membros × 20h/semana (Premissa P5) = 60h/semana, regulada pelo WIP limit de 3 cards em In Progress por pessoa (ADR-002), e não por taxa de utilização fixa. O overhead dos rituais (daily assíncrona, refinement semanal, retrospectiva quinzenal) é estimado em ≤ 1h/semana por membro e absorvido pela capacidade nominal. Verificação de capacidade do marco corrente: a distribuição de trabalho do backlog M1 registra aproximadamente 14h (Leonardo), 13h (Fabricio) e 11h (Edson), todos dentro do limite da Premissa P5 — evidência verificável de aderência (NC-06).

Duração calendarizada não é estimada por atividade: emerge do fluxo. O Cycle Time (definição operacional da ADR-003: In Progress → Done) possui meta de ≤ 3 dias após a calibração; a projeção de conclusão de cada marco é obtida dividindo-se o backlog ordenado por prioridade (P0 → P3) pelo Throughput empírico (meta ≥ 5 cards/semana pós-calibração; baseline em /docs/metricas/baseline.md após 03/10/2026, conforme ADR-003). Convenção de dias (NC-03): métricas de fluxo (Cycle Time, CFD) são medidas em dias corridos, por serem nativas do GitHub Insights e não exigirem recálculo; marcos, desvios de marco e capacidade são tratados em dias úteis, refletindo a disponibilidade real da equipe e coerente com o gatilho de escalation da Seção 1.8 ("desvio > 3 dias úteis"). Trade-off declarado: perde-se a previsão determinística por atividade e ganha-se previsão empírica por marco com overhead zero de estimativa.

## 3.5 Desenvolvimento do cronograma e marcos

O cronograma do COGME é materializado por três artefatos complementares: (i) o roadmap macro de marcos (Figura 12), única representação tipo Gantt admitida, restrita ao nível macro e derivada do SSOT; (ii) o backlog ordenado por P0–P3 e MoSCoW no GitHub Projects, que constitui o cronograma operacional vivo; e (iii) a linha de base temporal formal {M1–M4 + MF1–MF3 + Calibração}, única sujeita a controle integrado de mudanças. O período de calibração (23/09 a 03/10/2026) é um artefato de cronograma: converte métricas de fluxo em capacidade de previsão; até seu encerramento, as metas permanecem suspensas (Seção 1.5); após, metas ajustadas pela média observada ± 20% são formalizadas via ADR (ADR-003).

**Tabela 15 — Marcos, janelas e entregáveis de valor**

| Marco | Abertura SSOT | Data alvo | Entregável de valor | Critério de aceite |
| --- | --- | --- | --- | --- |
| M1 — Entrega Parcial Documental | 01/09/2026 | 22/09/2026 | TAP aprovado + 5 planos (Áreas 1–5, incluindo 12 PDCAs e Ishikawa no Plano de Qualidade) + ADRs 001–004 + SSOT configurado (backlog M1-01 a M1-21) | Submissão via GitHub validada pelo Prof. Dr. Nivaldo Carleto sem achados críticos |
| M2 — Ambiente e Modelagem | 23/09/2026 | 30/09/2026 | Stack FOSS definida e validada por protótipo (fase N4.1, conforme TAP §10 R2); ambiente local + CI verdes; DER e Protótipo UX/UI versionados; planos das Áreas 6–8 (ressalva NC-04) | Pipeline CI verde; artefatos de modelagem no repositório |
| Calibração (auxiliar) | 23/09/2026 | 03/10/2026 | Baseline empírica de fluxo + ADR de metas | Baseline publicada em /docs/metricas/baseline.md |
| M3 — MVP Funcional (Beta) | 04/10/2026 | 15/11/2026 | MVP full-stack operacional, coverage ≥ 80%, UAT sem defeitos críticos/bloqueantes | Métricas de fluxo dentro da baseline calibrada |
| M4 — Encerramento | 16/11/2026 | 15/12/2026 | Documentação técnica consolidada, lições aprendidas, verificação SMART, apresentação final, tag de release | Validação acadêmica pelo Prof. Dr. Nivaldo Carleto e tag de release final |

Fonte: Elaborado pelos autores (2026). Fontes primárias: TAP §6; Integração §1.7. Datas idênticas em todos os artefatos canônicos.

Figura 12 — Roadmap macro do cronograma (macro-fases e milestones)

**[PLACEHOLDER — IMAGEM: docs/diagramas/cronograma/fig-02-roadmap-macro.svg]**

Nota: Representação temporal de nível macro com três faixas horizontais — MF1 (01/09–30/09), MF2 (01/10–15/11) e MF3 (16/11–15/12) — e cinco marcadores de milestone nas datas da Tabela 15, com a Calibração graficamente distinguida como auxiliar. Constitui a única representação tipo Gantt admitida no projeto, derivada do SSOT; o nível operacional é regido por fluxo contínuo (ADR-002), sem datas preditivas por atividade.
Fonte: Elaborado pelos autores (2026).

Gantt operacional via ProjectLibre: não produzido proativamente (GMV); será derivado do Kanban somente se exigido formalmente pelo Prof. Dr. Nivaldo Carleto em avaliação.

## 3.6 Controle do cronograma

O monitoramento temporal é contínuo e nativo do SSOT (Domínio de Medição): o CFD exerce, neste plano, a função de monitoramento temporal substituto do Gantt/EVM (definição formal, cadência semanal e regra corretiva de banda 2× canonicamente na Seção 1.5, aqui apenas referenciadas); Cycle Time e Throughput são publicados semanalmente via GitHub Insights; o WIP em fluxo é verificado continuamente (≤ 9 cards). Gatilhos de ação corretiva com recorte temporal (derivados da Seção 1.8): desvio > 3 dias úteis em qualquer marco M1–M4 — Issue change-request + proposta de replanejamento + ADR (base: dias úteis); throughput < 3 cards/semana por 2 semanas consecutivas — revisão de WIP limits (fallback ADR-002) + reavaliação do escopo do MVP (fallback ADR-003) (base: semanas); banda do CFD > 2× a largura média por 2 semanas — retrospectiva extraordinária + replanejamento do gargalo (caminho crítico empírico, Seção 3.3) (base: semanas); card P0 com label blocked por > 48h — intervenção direta do GP + resolução ou substituição da dependência (base: horas corridas, NC-05). Fechamento de milestones: uma milestone não é fechada enquanto houver Issues abertas com label change-request ou blocked; o fechamento exige critérios atendidos, registro de lições aprendidas e comunicação ao Prof. Dr. Nivaldo Carleto quando aplicável (M1, M3, M4). Alteração de data de marco oficial exige change-request + aprovação do CCB (GP, membro único) + ADR + comunicação no marco subsequente; a milestone auxiliar Calibração pode ser reajustada pelo GP com registro em commit.

## 3.7 Notas de Contexto

NC-00 — Regime de freeze do TAP e precedência intra-TAP (decisão do GP, 21/09/2026). O TAP encontra-se congelado desde o início do planejamento (última versão datada de 18/09/2026, anterior a este plano): não é revisado, reversionado ou corrigido ao longo do ciclo, em conformidade com seu status ontológico (Premissa P9; PMBOK® 6ª §4.1 como dicionário). Duas regras derivam: (i) precedência intra-TAP — em divergência entre seções do TAP, a seção §6 (Marcos) é canônica para matéria temporal e de marcos; (ii) locus de contexto — os documentos de Planejamento (8 Áreas) detêm, com precedência, as Notas de Contexto que registram a leitura operacional vigente do TAP congelado; divergências jamais são tratadas como correções do TAP. Trade-off declarado: aceita-se divergência textual entre o termo autorizativo imutável e a leitura operacional, em favor da imutabilidade da referência de autorização e da trilha auditável de interpretações. A decisão atende aos gatilhos G1 (impacto transversal), G3 (questionabilidade acadêmica) e G4 (trade-off não óbvio) da Política de ADRs → ADR-005 encaminhada para emissão antes do M2.

NC-01 — Assimilação do SMART de Cronograma à seção §6. O objetivo SMART de Cronograma (TAP §3, item ii) registra "documentação consolidada" em novembro/2026, enquanto o TAP §6 e o critério de sucesso §3.2.g alocam consolidação e aceite no M4 (15/12/2026). Pela regra de precedência intra-TAP (NC-00), este plano operacionaliza a leitura do §6, sem alteração de datas: a entrega do MVP funcional que satisfaz o SMART ii na dimensão produto ocorre no M3 (15/11/2026, novembro); a consolidação documental acadêmica ocorre no M4. Nenhuma revisão do TAP é prevista ou citada (regime de freeze).

NC-02 — Numeração canônica dos processos de cronograma. Este plano adota a numeração oficial do PMBOK® 6ª edição (6.1–6.6); divergências registradas em artefatos vivos não são replicadas aqui e constam do registro de saneamento do OKB.

NC-03 — Convenção dupla de dias e definição operacional de Cycle Time. Métricas de fluxo em dias corridos (nativo GitHub Insights); marcos, desvios e capacidade em dias úteis. A definição operacional de Cycle Time aqui vigente é In Progress → Done (ADR-003), prevalecendo sobre redações divergentes em artefatos de origem.

NC-04 — Redação do critério M2 (stack). A expressão "Stack FOSS validada (ADR-001)" foi substituída por "definida e validada por protótipo (TAP §10, R2; fase N4.1)", com ressalva de que a formalização na ADR-001 está em avaliação e mudanças de stack exigem ADR específica (Seção 2.2).

NC-05 — Base temporal do gatilho de bloqueio P0. O limiar de 48h para cards P0 blocked é medido em horas corridas (evento de fluxo), distinguindo-se da base de dias úteis aplicada a desvios de marco.

NC-06 — Verificação de capacidade do marco corrente. Registrada como evidência verificável a distribuição de carga do backlog M1, com todos os membros dentro do limite de 20h semanais (Premissa P5).

## 3.8 Declaração de rastreabilidade

**Tabela 16 — Rastreabilidade interna do Plano de Cronograma**

| Seção | Origem | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 3.2 (Abordagem em 3 camadas + atividades) | TAP §1.c + §6 + Premissa P1 + ADR-004 | Abordagem de Desenvolvimento + Planejamento | 6.1, 6.2 |
| 3.3 (Sequenciamento e caminho crítico empírico) | TAP §6 + ADR-002 + ADR-003 | Planejamento + Entrega | 6.3 |
| 3.4 (Estimativa; capacidade NC-06) | Premissa P5 + TAP §8 + ADR-003 | Planejamento + Medição | 6.4 |
| 3.5 (Roadmap, linha de base, calibração, NC-01/NC-04) | TAP §6 + §3 (SMART Cronograma) + §10 (R2) | Planejamento + Medição | 6.5 |
| 3.6 (Controle e gatilhos; NC-05) | TAP §3.3 + §3 (Métricas) + Integração §1.8 | Medição + Incerteza | 6.6 |
| 3.7 (Notas de Contexto; freeze) | Decisão do GP (21/09/2026) + Premissa P9 | Trabalho do Projeto + Incerteza | 4.6 (dicionário) |

Fonte: Elaborado pelos autores (2026). Verificação: 100% das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa, restrição do TAP ou decisão formal do GP; referências cruzadas apontam exclusivamente para locais canônicos (Integração §1.5 para CFD; Escopo §2.4/§2.5 para decomposição e gates).

---

# 4 GERENCIAMENTO DOS CUSTOS

## 4.1 Identificação e propósito

Este Plano de Gerenciamento de Custos estabelece os mecanismos de governança para assegurar que o projeto COGME seja executado dentro da linha de base de custos aprovada: R$ 0,00 (zero reais). Deriva diretamente das Premissas P2 (FOSS absoluto), P6 (hardware adequado) e P9 (separação ontológica TAP ≠ EAP ≠ PDCA), e das Restrições de Custo do TAP (§8.4 e §11), respeitando os Domínios de Planejamento, Medição e Entrega do PMBOK® 7ª edição. Função ontológica: o plano não duplica a auditoria de licenças (EAP N4.4) nem a seleção de stack (EAP N4.1) — estabelece a governança sobre esses artefatos, garantindo que 100% das ferramentas, bibliotecas e serviços permaneçam dentro do perímetro FOSS/Free Tier ao longo de todo o ciclo de vida. Processo PMBOK 6ª (dicionário): 7.1 Planejar o Gerenciamento de Custos. Os processos 7.2 (Estimar Custos), 7.3 (Determinar Orçamento) e 7.4 (Controlar Custos) são inaplicáveis no sentido tradicional, pois: não há custos a estimar (todos os recursos são gratuitos); a linha de base é R$ 0,00; e métricas EVM (CPI, VAC) são matematicamente indeterminadas (AC = 0), conforme ADR-003. Trade-off declarado: abre-se mão da formalidade de estimativa/orçamento em favor de auditoria contínua de conformidade FOSS, alinhado ao Princípio "Foco em Valor" (PMBOK 7ª) e à Restrição TAP §8.4.

## 4.2 Abordagem de prevenção e linha de base

O gerenciamento de custos opera em três camadas de prevenção: (a) preventiva — seleção de stack e ferramentas, via ADR-001 e fase N4.1 (Seleção e Validação da Stack FOSS); (b) normativa — política de licenciamento, via whitelist/blacklist de licenças (subseção 4.4) e fase N1.4; (c) detectiva — auditoria de licenças, via fase N4.4 e checklist OSI-approved. Regra de ouro: nenhuma ferramenta, biblioteca, API ou serviço pode ser incorporado ao projeto sem (i) verificação de licença OSI-approved (whitelist), (ii) confirmação de plano gratuito suficiente para o MVP acadêmico e (iii) registro na ADR-001 ou em ADR específica (se mudança de stack). Hierarquia de resolução de conflitos aplicada a custos: (1) conformidade FOSS (restrição TAP §8.4); (2) funcionalidade do MVP (TAP §3 — Produto); (3) conveniência técnica (preferência do desenvolvedor). O fluxo de prevenção é ilustrado na Figura 13.

Figura 13 — Fluxo de Prevenção de Custos: conformidade FOSS

**[PLACEHOLDER — IMAGEM: docs/diagramas/custos/fig-01-fluxo-prevencao-custos.svg]**

Nota: O diagrama materializa operacionalmente a governança de custo zero (TAP §11), demonstrando que "orçamento nulo" não constitui ausência de controle, mas sim governança rigorosa sobre conformidade de licenciamento. Os três gates sequenciais (Gate 1: licença OSI-approved; Gate 2: plano gratuito suficiente para MVP acadêmico; Gate 3: registro em ADR-001 ou ADR específica) garantem que nenhuma dependência seja incorporada sem auditoria prévia. Desvios de qualquer gate acionam o fluxo de controle integrado de mudanças (Seção 1.6), com análise de impacto pelo GP (CCB de membro único) em ≤ 48h e registro formal via ADR quando a alteração impactar marcos ou escopo do MVP. A linha de base de custos (R$ 0,00) é imutável sem aprovação do CCB, em conformidade com a Premissa P2 (FOSS absoluto) e a Restrição TAP §8.4.
Fonte: Elaborado pelos autores (2026).

Conforme TAP §11, a linha de base de custos é: Recursos Humanos R$ 0,00 (esforço acadêmico voluntário, 3 membros); Software e Ferramentas R$ 0,00 (100% FOSS ou Free Tier, TAP §3 — Inovação); Infraestrutura e Hospedagem R$ 0,00 (ambiente local/homologação, sem cloud paga); Reserva de Contingência R$ 0,00 (inaplicável — linha de base zero inviabiliza reserva financeira; riscos de custo mitigados por substituição FOSS, Plano de Riscos, M2); Reserva de Gerenciamento R$ 0,00 (inaplicável — mesma razão); TOTAL R$ 0,00 (linha de base imutável sem CCB). Regra de imutabilidade: a linha de base só pode ser alterada via change-request + aprovação do CCB (GP como membro único, TAP §1.c) + ADR + comunicação ao Prof. Dr. Nivaldo Carleto no marco subsequente (Seção 1.6). Premissa crítica (P2): a disponibilidade contínua de ferramentas FOSS e Free Tier é assumida como verdadeira; caso uma ferramenta essencial migre para modelo pago durante o projeto, aciona-se: busca imediata de alternativa FOSS equivalente; se inexistente, redução de escopo (remoção da funcionalidade dependente); registro em ADR + lição aprendida.

## 4.3 Medição e controle

Dada a inaplicabilidade de EVM — formalmente declarada como LEGADO na ADR-003 e na Seção 1.5, pois AC = 0 torna CPI e VAC matematicamente indeterminados —, o controle de custos opera por métricas de conformidade: % Dependências Auditadas = (dependências com licença verificada / total de dependências) × 100, meta 100%, frequência por commit (CI), responsável pipeline + GP; Desvios de Licenciamento = número de dependências com licença não-OSI ou incompatível, meta 0, monitoramento contínuo, responsável GP; Custo Financeiro Acumulado = soma de todos os gastos realizados, meta R$ 0,00, frequência semanal, responsável GP (autorrelato); Alternativas FOSS Mapeadas = número de ferramentas críticas com pelo menos 1 alternativa FOSS identificada, meta ≥ 2 por ferramenta crítica, marco M2, responsável equipe. Gatilhos de ação corretiva: % Dependências Auditadas < 100% → bloqueio de merge até auditoria concluída; Desvios de Licenciamento > 0 → remoção imediata da dependência + change-request; Custo Financeiro Acumulado > R$ 0,00 → reembolso imediato pela equipe + lição aprendida. Decisão GMV: não será produzido dashboard próprio de conformidade FOSS, pois o GitHub Dependency Graph já fornece visibilidade nativa de licenças, vulnerabilidades e dependências sem overhead documental adicional; a evidência visual será capturada diretamente do GitHub Insights quando solicitada pelo Prof. Dr. Nivaldo Carleto em avaliação.

## 4.4 Regras de conformidade FOSS

Apenas as seguintes licenças são permitidas no projeto COGME, conforme ADR-001 e EAP N1.4: MIT (permissiva, sem restrições); Apache 2.0 (permissiva, sem restrições); BSD 2-clause e 3-clause (permissivas, sem restrições); GPL v2/v3 (copyleft, exige que derivativos também sejam GPL, aceitável para MVP acadêmico); LGPL (copyleft fraco, incluída para completude da whitelist FOSS acadêmica, sem uso previsto no MVP); ISC (permissiva, equivalente à MIT); PSF — Python Software Foundation (permissiva, adicionada para Python 3.11, ADR-001); Public Domain (domínio público, adicionada para SQLite, ADR-001). Licenças proibidas: proprietárias/comerciais; shareware/freeware sem código-fonte; Creative Commons (não é licença de software); licenças "Source Available" não-OSI (ex.: SSPL, BSL); licenças com restrições de uso comercial (violam definição OSI).

Delimitação de fronteiras (Área 4 versus Área 5): este plano estabelece a governança sobre conformidade FOSS (prevenção de custos ocultos por licenciamento inadequado), enquanto o Plano de Qualidade (Área 5) governa testes automatizados, coverage ≥ 80% e UAT (REQ-08 a REQ-10). A auditoria de licenças é compartilhada operacionalmente, mas a definição de whitelist/blacklist e os gatilhos de conformidade pertencem exclusivamente a esta Área de Custos, por derivação direta da Restrição TAP §8.4. A execução operacional da auditoria é realizada pela fase N4.4 da EAP, fundamentada na Política de Licenciamento da fase N1.4; este plano não duplica procedimentos operacionais — estabelece a governança sobre N1.4 e N4.4: responsável pela execução, equipe técnica; responsável pela supervisão, GP; frequência mínima, por marco (M1–M4) + revalidação a cada nova dependência; artefato de saída, /docs/dependencias/registro.md; critério de aceite, 100% das dependências com licença OSI-approved verificada; gatilho de escalation, qualquer dependência não-conforme → change-request imediato (Seção 1.6). A matriz de rastreabilidade de dependências (Figura 14) evidencia a auditabilidade da stack.

Figura 14 — Matriz de Rastreabilidade de Dependências: stack FOSS canônica

**[PLACEHOLDER — IMAGEM: docs/diagramas/custos/fig-02-matriz-rastreabilidade-dependencias.svg]**

Nota: A tabela apresenta seis exemplos reais de dependências da stack canônica (FastAPI ≥ 0.100, MIT; SQLite 3.x, Public Domain; WeasyPrint ≥ 59.0, BSD-3-Clause; pytest ≥ 7.0, MIT; GitHub Actions Free Tier, proprietário gratuito; llama.cpp 0.4.0-dev, MIT), todas com conformidade FOSS verificada. Cada dependência é rastreável à fase da EAP responsável pela auditoria (N1.4 — Política de Licenciamento FOSS ou N4.4 — Auditoria de Licenças) e à ADR-001 (Stack Tecnológica FOSS), que documenta a decisão arquitetural de adoção. A matriz demonstra ao avaliador que "custo zero" é auditável e rastreável, não apenas declarado.
Fonte: Elaborado pelos autores (2026).

## 4.5 Mudanças, fracasso e escalation

Qualquer alteração que possa impactar a linha de base de custos (mesmo que o impacto seja R$ 0,00) segue o fluxo do Plano de Integração (Seção 1.6): adição de dependência FOSS (ex.: incluir biblioteca httpx para chamadas HTTP assíncronas) — registro em commit + atualização de /docs/dependencias/registro.md; troca de ferramenta FOSS (ex.: substituir FastAPI por Flask) — ADR específica (gatilho G2 — irreversibilidade prática); mudança de licença de dependência existente (ex.: biblioteca X migra de MIT para licença proprietária) — change-request + substituição imediata + ADR; violação acidental de conformidade (dependência com licença não-OSI incorporada sem auditoria) — change-request + remoção + lição aprendida. Regra de escalation: se uma dependência crítica (ex.: FastAPI, SQLite) mudar de licença para não-FOSS durante o projeto, e não houver alternativa viável: (1) GP aciona change-request imediato; (2) avalia redução de escopo (remoção da funcionalidade dependente); (3) comunica ao Prof. Dr. Nivaldo Carleto no marco subsequente; (4) registra como risco materializado (Plano de Riscos, M2).

Derivadas do TAP §3.3, com distinção entre gatilhos de alerta preventivo (internos) e condições formais de fracasso (TAP): alerta preventivo — dependências não-OSI detectadas > 5% — auditoria emergencial + substituição ≤ 48h (GP, interno); fracasso formal — dependências incompatíveis com FOSS > 30% — condição de não sucesso do projeto (TAP §3.3.e); alerta preventivo — custo financeiro > R$ 0,00, qualquer valor — reembolso imediato + lição aprendida (GP, interno); alerta preventivo — dependência crítica sem alternativa FOSS, 1 ocorrência — redução de escopo + ADR ≤ 72h (GP + CCB); fracasso formal — falha na auditoria em 2 marcos consecutivos — revisão de processo + treinamento (GP). Nota de reconciliação (NC-C2): o limiar de 5% é um gatilho de alerta preventivo interno, mais restritivo que a condição formal de fracasso do TAP §3.3.e (30%); a intenção é detectar desvios precocemente, permitindo ação corretiva antes que o limiar formal seja atingido. Trade-off: maior rigor operacional em troca de margem de segurança.

## 4.6 Notas de Contexto e rastreabilidade

NC-C1 — Inaplicabilidade de Processos 7.2–7.4 do PMBOK 6ª: este plano declara formalmente que os processos "Estimar Custos" (7.2), "Determinar Orçamento" (7.3) e "Controlar Custos" (7.4) são inaplicáveis no sentido tradicional, pois a linha de base é R$ 0,00; o plano substitui estes processos por (a) governança sobre conformidade FOSS (N1.4 + N4.4), (b) prevenção de desvios de licenciamento e (c) métricas de conformidade (subseção 4.3); a substituição é fundamentada na ADR-003 (EVM LEGADO) e defensável academicamente pelo Domínio de Medição do PMBOK 7ª e pela Restrição TAP §11. NC-C2 — Delimitação de fronteiras (Área 4 versus Área 5 versus Escopo): as fases N1.4 e N4.4 são os artefatos canônicos de execução da conformidade FOSS; este plano estabelece exclusivamente a governança sobre N1.4 e N4.4, sem duplicar procedimentos operacionais; o Plano de Qualidade governa critérios de aceite de testes, não conformidade de licenças. NC-C3 — Numeração de processos no Glossário: o Glossário registra incorretamente "Processo 6.4 Estimar Custos"; a numeração canônica é Área 7 (Custos), Processo 7.2 (Estimar Custos); inconsistência registrada para saneamento na próxima revisão do Glossário (pós-M1). NC-C4 — Regime de freeze do TAP (Diretriz D3): o TAP é referência autorizativa congelada (última versão: 18/09/2026, anterior a todos os planos); divergências textuais entre este plano e o TAP são leituras operacionais, não correções do termo autorizativo; toda divergência é registrada como Nota de Contexto nesta seção.

**Tabela 17 — Rastreabilidade interna do Plano de Custos**

| Seção | Origem no TAP | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 4.1 (Propósito; freeze) | §11 + §8 + Premissa P9 | Planejamento + Entrega | 7.1 |
| 4.2 (Abordagem + linha de base) | §3 (Inovação) + §8 + §11 + EAP N1.4, N4.1 | Abordagem de Desenvolvimento + Planejamento | 7.1, 7.3 |
| 4.3 (Métricas de conformidade) | §3 (Métricas) + §11 + ADR-003 | Medição | 7.4 (substituição) |
| 4.4 (Conformidade FOSS) | §3 (Inovação) + §8 + ADR-001 | Entrega | 8.3 (controle aplicado) |
| 4.5 (Mudanças + fracasso) | §3.3 + §10 + Integração §1.6 | Incerteza + Entrega | 4.6 + 7.4 |
| 4.6 (Notas de Contexto) | Decisão do GP + Premissa P9 | Trabalho do Projeto | 4.6 (dicionário) |

Fonte: Elaborado pelos autores (2026). Verificação: 100% das seções possuem rastreabilidade a ao menos uma premissa, restrição ou objetivo SMART do TAP.

---

# 5 GERENCIAMENTO DA QUALIDADE

## 5.1 Identificação e propósito

Este Plano de Gerenciamento da Qualidade estabelece os mecanismos para garantir que o COGME atenda aos critérios de aceite técnicos: cobertura de testes ≥ 80%, UAT sem defeitos críticos/bloqueantes, e aplicação sistemática de ferramentas da qualidade (12 ciclos PDCA + 3 diagramas de Ishikawa 6M). Deriva das Premissas P1, P3, P4, P5 e P9, e das Restrições de Qualidade e Cronograma do TAP (§8.5 e §8.2), respeitando os Domínios de Medição, Entrega e Melhoria do PMBOK® 7ª edição. Função ontológica: o plano não duplica gates de qualidade do Escopo (Seção 2.5, DoR/DoD) — operacionaliza critérios técnicos de qualidade específicos para código, testes e documentação, garantindo conformidade com REQ-08, REQ-09 e REQ-10. Processos PMBOK 6ª (dicionário, obsolescência declarada): 8.1 Planejar o Gerenciamento da Qualidade, 8.2 Gerenciar a Qualidade, 8.3 Controlar a Qualidade. Trade-off declarado: abre-se mão de burocracia documental em favor de automação (pipeline CI) e melhoria contínua (PDCA por fase), alinhado ao Princípio "Foco em Valor" (PMBOK 7ª) e ao Valor Ágil "Software funcionando sobre documentação abrangente".

## 5.2 Abordagem, métricas e fluxo de garantia

A qualidade do COGME opera em três dimensões complementares: (a) preventiva — qualidade do código e arquitetura, via Code Review + SDD com IA auditável + Clean Code (fonte canônica: Escopo §2.5 + ADR-004); (b) detectiva — cobertura de testes e defeitos, via pipeline CI + pytest + coverage.py ≥ 80% (fonte canônica: REQ-08 + N6.1); (c) corretiva — melhoria contínua de processo, via 12 ciclos PDCA (um por fase da EAP) + Ishikawa 6M (fonte canônica: REQ-10 + N6.3). Regra de ouro: nenhum card migra para Done sem (i) pipeline CI verde, (ii) coverage ≥ 80% no módulo afetado, (iii) code review aprovado e (iv) tasklist 100% concluída (se aplicável, ADR-004). Hierarquia de resolução de conflitos aplicada à qualidade: (1) critérios de aceite do TAP §3.2 (coverage ≥ 80%, UAT sem defeitos críticos); (2) Clean Code e ACID; (3) conveniência técnica (preferência do desenvolvedor). O fluxo de garantia é ilustrado na Figura 15.

Figura 15 — Fluxo de Garantia da Qualidade

**[PLACEHOLDER — IMAGEM: docs/diagramas/qualidade/fig-01-fluxo-qualidade.svg]**

Nota: Fluxograma vertical com gates de qualidade sequenciais, destacando a revisão humana obrigatória para código gerado com apoio de SDD-IA e os critérios binários de aprovação. Materializa visualmente o DoD técnico, demonstrando ao avaliador que qualidade não é inspeção final, mas processo contínuo com gates automáticos (CI) e manuais (revisão de pares).
Fonte: Elaborado pelos autores (2026).

Dada a inaplicabilidade de EVM (ADR-003; Seção 1.5), o controle de qualidade opera por métricas técnicas automatizadas: Coverage = (linhas testadas / total de linhas) × 100, meta ≥ 80%, por push (CI), responsável pipeline + GP; Defeitos Críticos = número de bugs bloqueantes/críticos em UAT, meta 0, por marco (M3, M4), responsável GP + UAT; Taxa de Aprovação em Review = (PRs aprovados / total de PRs) × 100, meta ≥ 90%, semanal, responsável GP; Technical Debt Ratio = (dívida técnica / custo total), estimado via SonarQube Free Tier, meta < 5%, por marco, responsável GP; Tempo de Resposta = latência p95 das requisições da API, meta ≤ 3s, M3 (homologação), responsável pipeline + Edson. Nota: o SonarQube Free Tier é utilizado para análise estática de dívida técnica, em conformidade com TAP §11 (proibição de ferramentas pagas). Gatilhos de ação corretiva: coverage < 80% por 2 commits consecutivos → bloqueio de merge até correção; defeitos críticos > 0 em UAT → retrabalho imediato + congelamento de novas features; taxa de aprovação em review < 90% por 2 semanas → retrospectiva extraordinária + revisão de padrões de código. Decisão GMV: não será produzido dashboard próprio de métricas de qualidade, pois GitHub Insights + coverage.py + pytest já fornecem visibilidade nativa sem overhead documental; as evidências serão capturadas diretamente do GitHub Actions e dos relatórios de coverage quando solicitadas pelo Prof. Dr. Nivaldo Carleto em avaliação.

## 5.3 Critérios de aceite técnicos e ferramentas

Critérios de código-fonte: Clean Code — nomes significativos, funções ≤ 20 linhas, sem duplicação > 3 linhas, verificação por Code Review + pylint/flake8; Type Safety — type hints em 100% das funções públicas (Python 3.11+), verificação por mypy --strict (ferramenta complementar de análise estática, não parte da stack principal ADR-001, de utilização opcional e recomendada, sem impacto no orçamento, FOSS, licença MIT); Documentação Inline — docstrings em todas as classes e funções públicas (padrão Google), verificação por pydocstyle; SDD Auditável — commits de código gerado por IA declaram co-autoria e link para o prompt, verificação por git log + .ai/handoffs/. Critérios de testes automatizados: cobertura mínima ≥ 80% de linhas testadas (unitários + integração), verificação por coverage.py report; testes críticos — 100% dos fluxos REQ-01 a REQ-07 cobertos, verificação por coverage branch + UAT; tempo de execução — suíte completa em ≤ 5 minutos, verificação por GitHub Actions CI (REQ-11); isolamento — testes não dependem de ordem de execução ou estado global, verificação por pytest --random-order. Critérios de documentação: rastreabilidade — 100% dos requisitos (REQ-01 a REQ-15) mapeados a cards e testes, verificação por matriz de rastreabilidade; atualização — documentação atualizada antes do merge (código + docs no mesmo PR), verificação por Code Review; consistência — Glossário e OKB atualizados quando novos termos ou decisões surgirem, verificação no refinement semanal.

Conforme N7.1 da EAP e REQ-11, o pipeline CI executa automaticamente a cada push: checkout; setup Python 3.11; instalação de dependências; lint (flake8 + mypy --strict); testes com pytest (--cov=cogme --cov-report=xml --cov-fail-under=80); upload de coverage. Critérios de qualidade do pipeline: execução completa em ≤ 5 minutos (REQ-11); falha imediata se coverage < 80%; bloqueio de merge se pipeline vermelho.

## 5.4 Ciclos PDCA por fase da EAP

Cada uma das 12 fases da EAP (N1–N12, conforme linha de base do TAP §4) possui um ciclo PDCA específico, garantindo melhoria contínua sem burocracia excessiva; o TAP não integra ciclos PDCA (Premissa P9). Formato GMV: cada PDCA é documentado em máximo 6 linhas (Problema → Ação → Responsável → Métrica → Verificação → Lição). Síntese dos 12 ciclos consolidados:

**Tabela 18 — Ciclos PDCA consolidados (N1–N12)**

| Ciclo | Problema | Ação | Responsável | Métrica | Verificação |
| --- | --- | --- | --- | --- | --- |
| PDCA-N1 | Escopo mal definido ou premissas inválidas no início | Revisão em pares do TAP e EAP antes da submissão no M1 | Leonardo (GP) + Fabricio (par) | Zero inconsistências críticas no M1 | Validação acadêmica no M1 (22/09/2026) |
| PDCA-N2 | Requisitos ambíguos ou não rastreáveis | Conversão de REQ-01 a REQ-15 para User Story GWT (Padrão B) até M2 | Edson + Leonardo (revisão) | 100% dos requisitos Must com critérios GWT | Refinement semanal (23/09, 30/09) |
| PDCA-N3 | Arquitetura ou DER não validados antes da implementação | Protótipo "Hello World" da stack (N4.1) + revisão de DER antes de N5 | Fabricio (DER) + Edson (protótipo) | Zero retrabalho de arquitetura após início de N5 | Marco M2 (30/09/2026) |
| PDCA-N4 | Incompatibilidade de ferramentas FOSS ou ambiente instável | Validação de stack via protótipo funcional + auditoria de licenças (N4.4) | Leonardo (stack) + Edson (auditoria) | 100% das dependências OSI-approved (Custos §4.4) | M2 — /docs/dependencias/registro.md |
| PDCA-N5 | Código sem testes, coverage insuficiente ou SDD-IA sem revisão | TDD quando aplicável + code review obrigatório + tasklists (ADR-004) | Todos + GP (supervisão) | Coverage ≥ 80% por módulo; 100% commits SDD-IA com co-autoria | CI verde a cada push; Code Review |
| PDCA-N6 | Defeitos críticos em UAT ou coverage abaixo da meta | UAT estruturado com roteiro de testes + Ishikawa 6M (Seção 5.5) | Edson (UAT) + GP (Ishikawa) | Zero defeitos críticos/bloqueantes; coverage ≥ 80% | M3 (15/11/2026) — relatório UAT |
| PDCA-N7 | Pipeline lento (> 5 min, REQ-11) ou instável | Otimização de testes paralelos + cache de dependências | Leonardo (CI) + Fabricio (otimização) | Tempo de CI ≤ 5 min; taxa de sucesso ≥ 95% | GitHub Actions Insights (semanal) |
| PDCA-N8 | Falhas de comunicação entre equipe ou com stakeholder | Daily assíncrona padronizada + refinement semanal com pauta fixa | GP (facilitação) + equipe | 100% das dailies realizadas; zero cards bloqueados > 48h | GitHub Issues + GitHub Projects |
| PDCA-N9 | ADRs tardias ou prompts SDD não catalogados | Catálogo de prompts em .ai/handoffs/ + ADRs emitidas antes de M2 | Leonardo (ADRs) + todos (prompts) | 100% dos prompts versionados; ≤ 30% de ADRs tardias | /docs/decisoes/ + .ai/handoffs/ |
| PDCA-N10 | Mudanças não registradas ou scope creep > 15% (Escopo §2.6; Integração §1.8) | Label change-request obrigatória + análise de impacto em ≤ 48h (Integração §1.6) | GP (CCB) + equipe | 100% das mudanças registradas; scope creep < 15% | GitHub Issues com label change-request |
| PDCA-N11 | Documentação desatualizada ou inconsistente com código | Código + docs no mesmo PR + revisão de consistência antes de M4 | Todos + GP (consolidação) | 100% dos requisitos mapeados a docs; zero inconsistências TAP → código | M4 (15/12/2026) |
| PDCA-N12 | Lições aprendidas não consolidadas ou critérios SMART não verificados | Checklist de encerramento + lições finais + tag de release | GP (consolidação) + equipe | 100% dos critérios SMART verificados | M4 — validação acadêmica + tag |

Fonte: Elaborado pelos autores (2026). Lições de cada ciclo são registradas em /docs/conhecimento/licoes-aprendidas/ (MF1, MF2, MF3).

## 5.5 Diagramas de Ishikawa 6M (três análises)

Conforme REQ-10 e N6.3 da EAP, três diagramas de Ishikawa 6M são aplicados para análise de causa-raiz de problemas críticos de qualidade, cada um focado em um efeito indesejado específico. Nota sobre qualidade de processo versus produto: os dois primeiros diagramas (Coverage < 80% e Defeitos Críticos em UAT) analisam qualidade de produto; o terceiro (Cycle Time > 3 dias) analisa qualidade de processo — especificamente, eficiência do fluxo de trabalho; ambos os tipos são ferramentas da qualidade conforme REQ-10, e a delimitação entre eles é explicitada na subseção 5.6.

Figura 16 — Diagrama de Ishikawa 6M: coverage insuficiente (< 80%)

**[PLACEHOLDER — IMAGEM: docs/diagramas/qualidade/fig-05-ishikawa-coverage.svg]**

Nota: Diagrama espinha-de-peixe tradicional com as seis categorias (Método, Mão de Obra, Máquina, Material, Medida, Meio Ambiente) e causas-raiz específicas do COGME para o efeito "coverage < 80%". Permite ao GP e à equipe identificar ações corretivas priorizadas (ex.: tornar coverage gate obrigatório no CI) em vez de tratar sintomas. Ações corretivas derivadas: Método — implementar TDD obrigatório para REQ-01 a REQ-07 (críticos); Medida — configurar --cov-fail-under=80 no pipeline CI (gate bloqueante); Mão de Obra — pair programming para módulos complexos (N5.1, N5.2).
Fonte: Elaborado pelos autores (2026).

Figura 17 — Diagrama de Ishikawa 6M: defeitos críticos em UAT

**[PLACEHOLDER — IMAGEM: docs/diagramas/qualidade/fig-06-ishikawa-uat.svg]**

Nota: Diagrama 6M focado em defeitos de UAT, destacando causas relacionadas a SDD-IA e à validação acadêmica. Evidencia para o Prof. Dr. Nivaldo Carleto que a equipe compreende as limitações do ambiente acadêmico (usuários-piloto limitados) e propõe mitigações (UAT estruturado). Ações corretivas derivadas: Método — roteiro de UAT com cenários Given/When/Then para REQ-01 a REQ-07; Mão de Obra — code review cruzado (Fabricio revisa Edson, Edson revisa Leonardo); Medida — label bug-critical no GitHub com template de reporte padronizado.
Fonte: Elaborado pelos autores (2026).

Figura 18 — Diagrama de Ishikawa 6M: desvio de Cycle Time (> 3 dias)

**[PLACEHOLDER — IMAGEM: docs/diagramas/qualidade/fig-07-ishikawa-cycletime.svg]**

Nota: Diagrama 6M focado em gargalos de fluxo, conectando causas a ADR-002 (Kanban) e ADR-004 (tasklists). Demonstra ao avaliador que "Cycle Time > 3 dias" não é falha individual, mas sistêmica, exigindo ações em múltiplas dimensões. Ações corretivas derivadas: Método — DoR gate rigoroso (Escopo §2.5) — card sem DoR não entra em Ready; Mão de Obra — cross-training para reduzir dependência de membro único; Medida — publicação semanal de CFD (Integração §1.5) + ação corretiva se banda > 2× média.
Fonte: Elaborado pelos autores (2026).

## 5.6 Gestão de melhoria contínua

Conforme ADR-002, retrospectivas ocorrem a cada 2 semanas com pauta fixa: (a) o que funcionou bem? (b) o que pode melhorar? (c) ações para o próximo ciclo (máximo 3). Registro: /docs/conhecimento/licoes-aprendidas/ (MF1, MF2, MF3). Conforme Cronograma §3.6 e Integração §1.5, o CFD e o Cycle Time alimentam a melhoria de processo: CFD com banda > 2× média por 2 semanas → retrospectiva extraordinária; throughput < 3 cards/semana por 2 semanas → revisão de WIP limits (fallback ADR-002). Fronteira com Cronograma: este plano usa métricas de fluxo como input para melhoria de qualidade de processo, não como métrica de qualidade de produto (que são coverage, defeitos etc.); a definição formal, cadência e regra corretiva do CFD residem canonicamente na Seção 1.5; o monitoramento temporal detalhado reside na Seção 3.6.

## 5.7 Notas de Contexto e rastreabilidade

NC-Q1 — Regime de freeze do TAP (Diretriz D3): o TAP é referência autorizativa congelada (última versão: 18/09/2026, anterior a todos os planos); divergências textuais entre este plano e o TAP são leituras operacionais, não correções do termo autorizativo. NC-Q2 — Numeração de processos no Glossário: o Glossário registra incorretamente "Processo 6.4 Estimar Custos" na seção de Cronograma; a numeração canônica é Área 7 (Custos), Processo 7.2; processos de qualidade (8.1–8.3) devem ser verificados no Glossário §3 na próxima revisão. NC-Q3 — Cycle Time e definição operacional: a definição operacional vigente é In Progress → Done (ADR-003), prevalecendo sobre redações divergentes em artefatos de origem; o saneamento aplica-se apenas aos artefatos vivos. NC-Q4 — EAP: 12 fases, não 13: este plano consolida 12 ciclos PDCA (N1–N12), conforme linha de base do TAP §4 (12 fases + 37 pacotes); a contagem "13 fases + 48 pacotes" registrada em versão do Glossário é volátil e não canônica; o TAP não integra ciclos PDCA (Premissa P9). NC-Q5 — Grafia do stakeholder: esta seção utiliza a grafia "Prof. Dr. Nivaldo Carleto" conforme TAP v3; a grafia "Carleto" registrada no Glossário é incorreta e será saneada na próxima revisão (pós-M1).

**Tabela 19 — Rastreabilidade interna do Plano de Qualidade**

| Seção | Origem no TAP | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 5.1 (Propósito; freeze) | §3.2 (Qualidade) + Premissa P9 | Medição + Entrega | 8.1 |
| 5.2 (Abordagem + métricas + fluxo) | §3 (Qualidade) + §8.5 + ADR-003 | Entrega + Melhoria + Medição | 8.2, 8.3 |
| 5.3 (Critérios técnicos + ferramentas) | §3.2.b + §3.2.c + REQ-11 | Entrega + Trabalho do Projeto | 8.3, 8.2 |
| 5.4 (12 PDCAs) | §3.2.c + REQ-10 + N6.3 | Melhoria | 8.2 |
| 5.5 (Ishikawa 6M) | REQ-10 + N6.3 | Melhoria + Incerteza | 8.3 |
| 5.6 (Melhoria contínua) | ADR-002 + Integração §1.5 | Melhoria | 8.2 |
| 5.7 (Notas de Contexto) | Decisão do GP (21/09/2026) + Premissa P9 | Trabalho do Projeto | 4.6 (dicionário) |

Fonte: Elaborado pelos autores (2026). Verificação: 100% das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa, restrição do TAP ou REQ-08/09/10; referências cruzadas apontam exclusivamente para locais canônicos (Escopo §2.5 para DoR/DoD; Custos §4.4 para auditoria FOSS; Integração §1.5 para CFD).

---
---

# RELATÓRIO ANALÍTICO — AVALIAÇÃO DA PRODUÇÃO DOCUMENTAL E ESTADO GERAL DO PROJETO (M1)

Emitido por: GP Sênior PMBOK 7ª/PMO (Co-Autor Crítico) · Data: 22/09/2026 · Destinatário: Prof. Dr. Nivaldo Carleto (stakeholder-avaliador) e equipe · Classificação: artefato de governança (não integra o corpo ABNT da redação).

## R1. Escopo e cobertura da produção

A redação integral do M1 cobre a Introdução (reprodução integral e não subnumerada do TAP: identificação, objetivos, justificativa, EAP com 12 fases e 37 pacotes, 15 requisitos, 4 marcos + milestone auxiliar, 9 premissas e 7 categorias de restrição) e as Áreas de Conhecimento 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade), conforme delimitação da entrega faseada (Integração §1.7; OKB v3.1 §2.4). As Áreas 6 a 8 (Recursos, Comunicações, Riscos) estão formalmente diferidas para o M2 (30/09/2026), com justificativa de tailoring documentada. Cobertura declarada: 100% do escopo documental do M1.

## R2. Conformidade estrutural e ABNT

(a) Introdução sem subnumeração, conforme diretriz; tabelas e figuras numeradas sequencialmente no corpo (Tabelas 1–19; Figuras 1–18), com identificação no topo, nota explicativa e fonte ("Elaborado pelos autores (2026)") na base, conforme NBR 14724/NBR 12225; (b) seções primárias numeradas (1 a 5) com subseções decimais; (c) ausência de anexos e de tabelas de versionamento de diagramas/figuras no corpo acadêmico (versionamento mantido exclusivamente no repositório e no OKB, por GMV); (d) placeholders de imagem padronizados com caminho e nome de arquivo canônicos, permitindo substituição direta por PNG/SVG na composição final .docx; (e) prosa técnica impessoal, com alíneas e trade-offs declarados.

## R3. Rastreabilidade e coerência interna

Cada seção possui tabela de rastreabilidade fechada (TAP → domínio PMBOK 7ª → processo PMBOK 6ª), com verificação declarada de 100%. Cadeia TAP → Escopo → EAP → Cronograma → Custos → Qualidade mantida sem quebras: a EAP canônica (12/37) é citada identicamente na Introdução, no Escopo (§2.4) e no Cronograma (§3.2); as datas M1–M4 + Calibração são idênticas no TAP §6, na Tabela 4, na Tabela 15 e no OKB v3.1 §7.2; a linha de base de custos R$ 0,00 é coerente entre TAP §11, Custos §4.2 e a matriz de dependências (Figura 14); as metas de qualidade (coverage ≥ 80%, UAT 100% fluxos críticos) são coerentes entre TAP §3.2, REQ-08/09, Qualidade §5.2 e o pipeline CI (§5.3).

## R4. Governança documental (avaliação da proposta da Seção 1.4)

A classificação normativa proposta (canônica níveis 1–3, contextual, transitória desprezada) é avaliada como adequada e suficiente: (i) elimina o risco de citação acadêmica de artefatos de rascunho (notas adjacentes, drafts, legados); (ii) preserva a trilha histórica de raciocínio no repositório sem valor normativo; (iii) institucionaliza as Notas de Contexto como único locus de leitura operacional do TAP congelado, sustentando o regime de freeze (NC-00) sem violar a Premissa P9. Recomenda-se manter a tabela de classificação (Tabela 9) como referência permanente nas próximas rodadas documentais.

## R5. Estado geral do projeto (fotografia em 22/09/2026)

**Tabela 20 — Estado do projeto no M1**

| Dimensão | Estado | Evidência |
| --- | --- | --- |
| Escopo documental M1 | ✅ Concluído e submetido | 5 planos + Introdução + 12 PDCAs + 3 Ishikawa |
| Backlog M1 (21 cards) | ✅ 13 concluídos / 8 diferidos conforme plano | OKB v3.1 §8.1 |
| Carga da equipe | ✅ Dentro do limite (14h/13h/11h vs 20h) | NC-06; Premissa P5 |
| Stack e ambiente | ✅ Configurados; ADR-001 em avaliação de impacto | M1-12, M1-13; NC-04 |
| Métricas de fluxo | ⏳ Em calibração (23/09–03/10); sem meta fixa | ADR-003; Integração §1.5 |
| Governança (ADRs) | ✅ 001–004 emitidas; ⏳ ADR-005 antes do M2 | OKB v3.1 §5 |
| Repositório | ⚠️ Normalização pendente pós-LA-001 | Seção R6 |
| Riscos ativos | Monitorados (R1–R8 do guardrail); sem materialização crítica | OKB histórico §3 |

## R6. Pendências, anomalias e plano de ação pós-M1

| # | Item | Severidade | Ação | Prazo |
| --- | --- | --- | --- | --- |
| 1 | Emitir ADR-005 (regime de freeze + precedência §6 + Notas de Contexto) | Alta | Redação + revisão de par + commit docs(adr) | Antes do M2 |
| 2 | Saneamento do Glossário v3.2 (contagem 13/48 → 12/37; grafia Carleto; Cycle Time In Progress → Done; numeração 6.4/7.2) | Média | Revisão do artefato vivo | Pós-M1 |
| 3 | Gerar Figura 12 (roadmap macro) — único placeholder sem arquivo | Média | Produção SVG + conversão PNG | Antes da composição .docx final |
| 4 | Normalização do repositório pós-LA-001: mover fig-4-controle-mudancas.svg para integracao/; relocar matriz de dependências para custos/; criar escopo/ para fig-2-cadeia-decomposicao-escopo.svg; remover prefixos [legacy] indevidos em qualidade/; recuperar ou regenerar fig-2-fluxo-kanban-oficial.svg e 1.svg via git reflog | Média | Commit chore(diagramas) em branch dedicada, com git mv | Até 26/09 |
| 5 | Planos das Áreas 6–8 (Recursos, Comunicações, Riscos) | Alta | Redação pós-calibração | M2 (30/09) |
| 6 | Baseline de métricas + ADR de metas | Média | Coleta 23/09–03/10 + ADR | 03/10 |
| 7 | Micro-ajuste opcional Integração §1.3 (reforço de rastreabilidade do DoD) | Baixa | Deliberação do GP | Aguardando |

## R7. Avaliação qualitativa da produção

Pontos fortes: (i) blindagem acadêmica explícita (hierarquia normativa, obsolescência declarada do PMBOK 6ª, substituição de EVM por métricas de fluxo com fundamentação em três pilares); (ii) disciplina de canonicidade e freeze, rara em documentação acadêmica de graduação e defensável perante avaliação; (iii) rastreabilidade fechada em todas as seções; (iv) figuras com notas explicativas densas que justificam cada escolha metodológica (anti-burocracia GMV com justificativa, não por omissão). Pontos de atenção: (i) concentração de conhecimento de governança no GP (mitigada por revisão em pares e cross-training previsto no Ishikawa-3); (ii) dependência de ferramentas gratuitas externas (GitHub Actions, API de câmbio), já registrada como risco com fallback; (iii) volume documental gerenciado exclusivamente por 3 pessoas — o princípio GMV deve permanecer como critério de corte nas próximas rodadas.

## R8. Veredito

A produção documental do M1 encontra-se aderente ao critério de aceite do TAP §6 (submissão sem achados críticos esperados), coerente com o OKB v3.1, o Glossário v3.1 (ressalvado o saneamento pendente) e as ADRs 001–004, e pronta para composição final em formato ABNT mediante substituição dos 18 placeholders pelos arquivos indicados (17 existentes + 1 a gerar). O estado geral do projeto é saudável: escopo controlado, cronograma com linha de base formal intacta, custos em conformidade FOSS verificável, qualidade com gates automatizados operacionais. Recomenda-se: (a) executar o plano de ação da Tabela 20/R6 na sequência priorizada; (b) iniciar o período de calibração em 23/09 sem antecipação de metas; (c) manter este relatório como linha de base comparativa para o PDCA de fechamento da MF1 (30/09/2026).

Fim do documento — Redação Integral M1 + Relatório Analítico | COGME | Fatec Taquaritinga | 22/09/2026.