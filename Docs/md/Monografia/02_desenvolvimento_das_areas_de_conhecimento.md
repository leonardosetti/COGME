# 2. Desenvolvimento das Áreas de conhecimento

O desenvolvimento das áreas de conhecimento do projeto COGME — Conversor de Ganhos em Moeda Estrangeira — organiza o trabalho necessário para transformar os objetivos estabelecidos no Termo de Abertura do Projeto (TAP) em entregas verificáveis. O projeto atende a uma necessidade apresentada nos documentos de referência: apoiar profissionais brasileiros que recebem por serviços prestados ao exterior e precisam estimar seus ganhos em reais, considerando a moeda de origem, o regime de contratação e os encargos envolvidos. Nesse contexto, o gerenciamento deve orientar tanto a construção do sistema quanto a produção da documentação acadêmica, mantendo coerência entre o que se pretende entregar, os recursos disponíveis e os critérios de aceitação.

O núcleo do produto definido no TAP compreende um sistema web capaz de simular a conversão de USD e EUR para BRL, contemplar remuneração por hora, dia, semana, mês ou valor fixo, aplicar encargos financeiros simulados e gerar uma invoice em PDF. A monografia detalha esse propósito com a utilização da cotação PTAX do Banco Central do Brasil e a comparação informativa de provedores de pagamento internacional, considerando tarifas, spread e valor líquido estimado. Esse detalhamento orienta o planejamento do produto, devendo os requisitos adicionais ser conciliados com o TAP no gerenciamento do escopo. Conforme a delimitação apresentada na monografia, o COGME permite consultar, simular e comparar informações e encaminhar o usuário ao provedor escolhido; a execução de transferências e a integração transacional com plataformas de pagamento permanecem fora da entrega acadêmica prevista.

O escopo do projeto abrange o trabalho necessário para produzir esse resultado: levantamento de requisitos, modelagem, configuração do ambiente, desenvolvimento, testes, disponibilização da aplicação, documentação e apresentação para aceite. A Estrutura Analítica do Projeto (EAP) organiza essas entregas, que deverão ser decompostas em atividades com responsáveis, dependências e critérios de conclusão. Para o COGME, disponibilizar uma tela de simulação, por exemplo, exige definir as regras de cálculo, obter e identificar a cotação utilizada, tratar as entradas do usuário, apresentar os resultados e verificar seu funcionamento por testes. Essa relação entre entrega e trabalho necessário permite estimar o esforço com maior consistência e evita considerar uma funcionalidade concluída apenas pela existência de sua interface.

A condução do projeto está vinculada à realidade de uma equipe de dois integrantes: Leonardo David Silva Setti, como gerente e desenvolvedor, e Fabricio de Lima Cabral, como desenvolvedor, sob orientação de Nivaldo Carleto, que também exerce o papel de cliente acadêmico. Os integrantes compartilham atividades de análise, programação, testes e documentação e conciliam o projeto com outras obrigações acadêmicas e profissionais. A monografia prevê até 20 horas semanais por integrante como referência de disponibilidade, a ser considerada na distribuição das tarefas. Por isso, a possibilidade técnica de executar atividades em paralelo deve ser confrontada com a capacidade efetiva da equipe, reservando tempo para revisão, correção de falhas e preparação das entregas.

As restrições econômicas também influenciam as decisões de gerenciamento. O TAP estabelece ausência de financiamento institucional e restrição à aquisição de ferramentas e serviços pagos, direcionando o planejamento para equipamentos próprios, software livre e serviços gratuitos compatíveis com o MVP. A inexistência de verba para aquisições não elimina o consumo de energia, conectividade e tempo de trabalho, identificados na monografia como recursos necessários à execução. Cabe ao gerenciamento de custos tornar essas necessidades visíveis e verificar sua compatibilidade com as restrições do projeto. Despesas que contrariem o TAP, como a assinatura de IA mencionada na planilha da monografia, dependem de conciliação antes de integrarem um orçamento aprovado.

A organização deste capítulo por integração, escopo, custos, tempo, qualidade, recursos, comunicações e riscos acompanha a estrutura da monografia e o tratamento por áreas presente no TAP. Os princípios e domínios de desempenho do PMBOK® 7ª edição, adotados na monografia, orientam a adaptação dessas práticas ao porte do COGME. A estrutura por áreas e a orientação por princípios cumprem funções complementares na apresentação do planejamento, sem equivalência direta entre áreas e domínios. Na aplicação ao projeto, destacam-se a responsabilidade pelas decisões, a colaboração entre os integrantes, o envolvimento do orientador, o foco na utilidade do produto, a qualidade das entregas e a resposta às incertezas. O tratamento simplificado de aquisições e partes interessadas proposto na monografia mantém a necessidade de verificar ferramentas e serviços, identificar os envolvidos e registrar as aprovações pertinentes.

**Quadro 1 — Aplicação das áreas de conhecimento ao escopo do COGME**

| Área de conhecimento | Aplicação ao projeto | Instrumentos e resultados esperados |
| --- | --- | --- |
| Integração | Manter coerência entre TAP, requisitos, EAP, desenvolvimento e documentação; avaliar o efeito de mudanças sobre o conjunto das entregas. | Planos articulados, registros de decisão, solicitações de mudança e aceite das entregas. |
| Escopo | Definir os limites da simulação cambial, dos regimes de contratação, da invoice e do comparativo informativo, distinguindo essas funções da execução de pagamentos. | Requisitos com critérios de aceite, EAP e identificação das funcionalidades excluídas ou destinadas a versões futuras. |
| Custos | Estimar os gastos operacionais e verificar o uso de equipamentos e serviços frente à restrição de aquisições pagas. | Planilha de custos com premissas explícitas e acompanhamento das despesas atribuídas ao projeto. |
| Tempo | Sequenciar requisitos, modelagem, implementação, testes e documentação de acordo com suas dependências e a capacidade de duas pessoas. | Lista de atividades, precedências, cronograma de marcos e acompanhamento do trabalho em andamento. |
| Qualidade | Verificar a correção dos cálculos, os regimes de contratação, a identificação das cotações e a geração do PDF, além dos requisitos do comparativo. | Critérios de aceite, testes automatizados e de aceitação, registros de defeitos e ações de melhoria. |
| Recursos | Distribuir os papéis e as tarefas entre os integrantes, considerando disponibilidade, equipamentos próprios e ambiente de desenvolvimento. | Matriz de responsabilidade, alocação de atividades e acompanhamento da carga de trabalho. |
| Comunicações | Compartilhar impedimentos e decisões entre os integrantes e submeter dúvidas, mudanças e entregas ao orientador. | Registros no repositório, atualização do quadro de trabalho e histórico das validações. |
| Riscos | Tratar indisponibilidade da API de câmbio, desatualização das tarifas, falhas de cálculo, erros no código assistido por IA e sobrecarga da equipe. | Registro de riscos, respostas planejadas, responsáveis pelo acompanhamento e revisão das condições de execução. |

Fonte: elaboração a partir do Termo de Abertura do Projeto e do Modelo-Projeto-COGME (2026).

A integração entre essas áreas pode ser observada em uma situação possível no escopo descrito pela monografia: a inclusão de um novo provedor no comparativo. Embora pareça uma alteração pontual na interface, essa inclusão exige obter tarifas e datas de vigência, definir como compõem o valor líquido, implementar sua apresentação e acrescentar cenários de teste. A decisão envolve escopo, esforço, disponibilidade dos integrantes, qualidade dos dados e risco de desatualização. Antes de assumir a nova entrega, a equipe deverá avaliar seu impacto sobre as atividades já previstas e registrar a decisão correspondente. Esse procedimento aplica ao COGME o controle de mudanças necessário para preservar a viabilidade do projeto.

A monografia organiza o trabalho nas macro-fases de Fundação, Construção e Consolidação, com horizonte de setembro a novembro de 2026. Nessa organização, a Fundação concentra a preparação do planejamento, dos requisitos e do ambiente; a Construção reúne a implementação e a verificação progressiva do produto; e a Consolidação compreende a documentação final e a preparação do aceite. O Kanban, previsto como método de acompanhamento, deverá tornar visíveis as atividades pendentes, em execução, em revisão e concluídas, permitindo identificar bloqueios e limitar a quantidade de trabalho simultâneo. As datas dos marcos e as métricas de acompanhamento serão detalhadas nos planos específicos, conciliando as diferenças entre o TAP e a monografia antes de sua adoção como referência única de controle.

A qualidade constitui um critério de entrega desde a definição dos requisitos. O TAP prevê tempo de resposta de até três segundos para as simulações, cobertura mínima de 80% do código por testes automatizados e aprovação de todos os fluxos críticos nos testes de aceitação. Esses valores são metas a verificar durante a execução. Para a simulação cambial, a conferência deve considerar os valores informados, a cotação de referência, os encargos utilizados e o resultado calculado. Para o comparativo, deverá abranger também a origem e a atualização das tarifas apresentadas. A abordagem de desenvolvimento orientado por especificações, apoiada por IA, deverá manter o vínculo entre requisitos, implementação e testes, com revisão humana dos artefatos produzidos.

O resultado esperado do gerenciamento é uma entrega compatível com o prazo acadêmico, sustentada por evidências de funcionamento e por documentação consistente. O valor do COGME para o usuário será avaliado pela capacidade de reunir informações úteis à estimativa de seus ganhos e reduzir o trabalho de comparação manual. Para a equipe e o orientador, os planos deverão permitir identificar o que será entregue, quem responde por cada atividade, quais critérios serão verificados e como eventuais desvios serão tratados. As seções seguintes desenvolvem esses instrumentos no nível de detalhe necessário ao escopo atual do projeto.

## Temas relacionados

- [2.1 Gerenciamento da Integração](02_01_gerenciamento_da_integracao.md)
- [2.2 Gerenciamento de Escopo](02_02_gerenciamento_de_escopo.md)
- [2.3 Gerenciamento dos Custos](02_03_gerenciamento_dos_custos.md)
- [2.4 Gerenciamento do tempo](02_04_gerenciamento_do_tempo.md)
- [2.5 Gerenciamento de Qualidade](02_05_gerenciamento_de_qualidade.md)
- [2.6 Gerenciamento de recursos](02_06_gerenciamento_de_recursos.md)
- [2.7 Gerenciamento das comunicações](02_07_gerenciamento_das_comunicacoes.md)
- [2.8 Gerenciamento dos Riscos](02_08_gerenciamento_dos_riscos.md)

## Fontes documentais analisadas

- [Termo de Abertura do Projeto v1_opngoing.docx](../../docx/Termo%20de%20Abertura%20do%20Projeto%20v1_opngoing.docx): objetivos do documento, objetivos SMART, EAP, requisitos e restrições.
- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx): introdução; capítulo 2, incluindo escopo, custos, tempo, qualidade, recursos, comunicações e riscos; capítulo 3 e considerações finais.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

O capítulo deve explicar como as decisões de gerenciamento sustentam a entrega do MVP. A unidade de análise é o projeto COGME: equipe de duas pessoas, prazo acadêmico, recursos próprios, simulação cambial e comparação informativa. Os conceitos da disciplina devem aparecer associados a decisões e evidências do projeto.

- [ ] Relacionar o benefício esperado — reduzir consultas manuais e melhorar a compreensão do valor líquido — a um roteiro de avaliação com usuários, sem declarar resultados ainda não medidos.
- [ ] Explicar a ligação objetivo → requisito → entrega da EAP → atividade → teste → aceite, utilizando a simulação USD/EUR para BRL como exemplo.
- [ ] Distinguir planejamento, execução e resultado comprovado; manter as edições do PMBOK utilizadas nos documentos, sem apresentar áreas e domínios como equivalentes.

**Entrega esperada:** Introdução que delimite produto, trabalho do projeto, abordagem, restrições e forma de comprovar os resultados.
