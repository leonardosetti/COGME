### Rede do Projeto (Diagrama de Precedências)

A rede do projeto representa a sequência lógica das atividades e permite calcular, pelo Método do Caminho Crítico (CPM), as datas mais cedo e mais tarde de cada atividade, as folgas e o caminho crítico. Pelo PMBOK® 6ª (dicionário), ela resulta do processo 6.3 (Sequenciar as Atividades) e alimenta o 6.5 (Desenvolver o Cronograma). No PMBOK® 7ª, apoia o Domínio de Planejamento e o Domínio de Medição. A rede é construída no nível dos **cards de marco** (MF1) e dos **pacotes de trabalho da EAP** (MF2 e MF3). Ela complementa, e não substitui, o sequenciamento operacional por fluxo descrito acima (ADR-003): serve para validar a viabilidade dos marcos e mostrar ao avaliador a lógica de precedências do projeto. Conforme a ADR-007, é um artefato de validação acadêmica no nível macro: "A rede valida o marco; o Kanban executa a tarefa." Nenhum card é planejado pelas datas da rede.

Para manter a legibilidade, a rede foi dividida em seis partes: (1) rede macro, com as macro-fases e os marcos; (2) MF1 — Parte 1, planejamento e governança; (3) MF1 — Parte 2, requisitos e modelagem; (4) MF1 — Parte 3, ambiente e encerramento da fase; (5) MF2 — Construção; e (6) MF3 — Consolidação. As ligações entre partes aparecem como conectores tracejados.

**Convenções adotadas:**

- Diagrama de precedências com atividade no nó (AON) e relações término-início (TI). Na MF2, as dependências de recurso (RD) também são término-início.
- Duração (D) em dias úteis = esforço estimado ÷ 4 h por dia (Premissa P5: até 20 h por semana por membro), arredondada para cima; marcos têm duração zero. Essa taxa é o teto da Premissa P5, não a produtividade medida; por isso a seção traz cenários de dedicação.
- MF1: atividades, esforço e predecessoras extraídos dos campos "Atribuição" e "Dependências" dos cards M1-01 a M1-21 no GitHub Projects. A dependência "TAP aprovado" é representada pelo marco inicial T0.
- MF2 e MF3: esforço estimado por julgamento de especialista, com base na classificação T-shirt do Plano de Cronograma. Os valores foram validados pela equipe em 25/10/2026 e servem de base para os cards de M3 e M4. A atividade N5.1a (12 h) foi acrescentada por causa da ADR-010, com estimativa ainda a validar pela equipe. N5.5 e N10 são atividades contínuas e ficam fora do cálculo.
- ES/EF: início e término mais cedo; LS/LF: início e término mais tarde; Folga = LS − ES. Atividades com folga zero formam o caminho crítico e aparecem em vermelho e em negrito.

![Rede macro](../diagramas/cronograma/redes/fig-rede-0-macro.png)

Figura R.0 — Rede macro do projeto: macro-fases e marcos.
Fonte: Elaborado pelos autores (2026).

#### MF1 — Fundação

![Rede MF1 parte 1](../diagramas/cronograma/redes/fig-rede-1-mf1-parte1.png)

Figura R.1 — Rede do projeto da MF1, Parte 1: planejamento e governança.
Fonte: Elaborado pelos autores (2026), com base nos cards do GitHub Projects.

| Atividade | Descrição | Responsável | Esforço (h) | D (dias úteis) | Predecessoras | ES | EF | LS | LF | Folga | Janela no GitHub Projects |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **T0** | **TAP e EAP aprovados** | Equipe | — | 0 | — | 0 | 0 | 0 | 0 | 0 | 20/08–26/08 |
| M1-15 | ADR-001: Stack Tecnológica | Leonardo | 2 | 1 | T0 | 0 | 1 | 1 | 2 | 1 | 31/08–19/09 |
| M1-16 | ADR-002: Kanban como Método | Leonardo | 2 | 1 | T0 | 0 | 1 | 1 | 2 | 1 | 28/08–19/09 |
| M1-17 | ADR-003: Métricas de Fluxo | Leonardo | 2 | 1 | M1-16 | 1 | 2 | 2 | 3 | 1 | 01/09–21/09 |
| **M1-01** | **Plano de Integração** | Leonardo | 6 | 2 | T0 | 0 | 2 | 0 | 2 | 0 | 07/09–19/09 |
| **M1-02** | **Plano de Escopo** | Fabricio | 6 | 2 | T0, M1-01 | 2 | 4 | 2 | 4 | 0 | 16/09–19/09 |
| M1-03 | Plano de Cronograma | Fabricio | 4 | 1 | T0, M1-17 | 2 | 3 | 3 | 4 | 1 | 19/09–19/09 |
| M1-04 | Plano de Custos | Fabricio | 3 | 1 | T0, M1-17 | 2 | 3 | 3 | 4 | 1 | 19/09–19/09 |
| M1-05 | Plano de Qualidade + PDCAs + Ishikawa | Edson | 8 | 2 | T0 | 0 | 2 | 2 | 4 | 2 | 19/09–20/09 |
| M1-19 | Matriz de Comunicação (RACI) | Edson | 3 | 1 | M1-01 | 2 | 3 | 3 | 4 | 1 | 19/09–20/09 |

Fonte: Elaborado pelos autores (2026), com base nos cards do GitHub Projects.

![Rede MF1 parte 2](../diagramas/cronograma/redes/fig-rede-2-mf1-parte2.png)

Figura R.2 — Rede do projeto da MF1, Parte 2: requisitos e modelagem.
Fonte: Elaborado pelos autores (2026), com base nos cards do GitHub Projects.

| Atividade | Descrição | Responsável | Esforço (h) | D (dias úteis) | Predecessoras | ES | EF | LS | LF | Folga | Janela no GitHub Projects |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M1-06 | Requisitos Funcionais | Fabricio | 4 | 1 | T0 | 0 | 1 | 1 | 2 | 1 | 31/08–19/09 |
| M1-07 | Requisitos Não Funcionais | Edson | 4 | 1 | T0 | 0 | 1 | 3 | 4 | 3 | 01/09–19/09 |
| M1-09 | Protótipo UX/UI | Edson | 8 | 2 | M1-06 | 1 | 3 | 2 | 4 | 1 | 18/09–30/09 |
| M1-10 | Modelagem de Dados (DER) | Edson | 8 | 2 | M1-06 | 1 | 3 | 2 | 4 | 1 | 18/09–30/09 |

Fonte: Elaborado pelos autores (2026), com base nos cards do GitHub Projects.

![Rede MF1 parte 3](../diagramas/cronograma/redes/fig-rede-3-mf1-parte3.png)

Figura R.3 — Rede do projeto da MF1, Parte 3: ambiente e encerramento da fase.
Fonte: Elaborado pelos autores (2026), com base nos cards do GitHub Projects.

| Atividade | Descrição | Responsável | Esforço (h) | D (dias úteis) | Predecessoras | ES | EF | LS | LF | Folga | Janela no GitHub Projects |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **M1-11** | **Seleção e Validação da Stack FOSS** | Leonardo | 4 | 1 | T0 | 0 | 1 | 0 | 1 | 0 | 28/08–30/09 |
| M1-08 | Arquitetura da Solução | Leonardo | 6 | 2 | M1-15, M1-11 | 1 | 3 | 2 | 4 | 1 | 08/09–30/09 |
| **M1-12** | **Repositório Git + CI/CD** | Leonardo | 6 | 2 | M1-11 | 1 | 3 | 1 | 3 | 0 | 14/09–19/09 |
| M1-13 | Setup Local e Homologação | Fabricio | 4 | 1 | M1-11 | 1 | 2 | 3 | 4 | 2 | 19/09–21/09 |
| M1-14 | Auditoria de Licenças FOSS | Edson | 3 | 1 | M1-11 | 1 | 2 | 3 | 4 | 2 | 18/09–30/09 |
| **M1-20** | **Canais Oficiais de Comunicação** | Leonardo | 2 | 1 | M1-12 | 3 | 4 | 3 | 4 | 0 | 18/08–19/09 |
| **M1-21** | **Labels e Fluxo de Mudanças** | Leonardo | 2 | 1 | M1-12 | 3 | 4 | 3 | 4 | 0 | 19/09–19/09 |
| **M1-18** | **Lições Aprendidas (MF1)** | Leonardo | 2 | 1 | M1-02, M1-03, M1-04, M1-05, M1-19, M1-07, M1-09, M1-10, M1-08, M1-13, M1-14, M1-20, M1-21 | 4 | 5 | 4 | 5 | 0 | 18/09–30/09 |
| **M2** | **Marco M2 — Ambiente e Modelagem** | — | — | 0 | M1-18 | 5 | 5 | 5 | 5 | 0 | 30/09 |

Fonte: Elaborado pelos autores (2026), com base nos cards do GitHub Projects.

A rede da MF1 tem duração lógica mínima de **5 dias úteis**, com 3 caminhos críticos de mesma duração: T0 → M1-01 → M1-02 → M1-18 → M2; T0 → M1-11 → M1-12 → M1-20 → M1-18 → M2; T0 → M1-11 → M1-12 → M1-21 → M1-18 → M2. A janela real da MF1, porém, foi de 31 dias úteis (18/08 a 30/09/2026). A diferença mostra que a duração da fase foi determinada pela **disponibilidade da equipe** (curso noturno, outras disciplinas), e não pela lógica de precedências. Essa conclusão é coerente com o atraso registrado na questão Q-04 e com a opção do projeto pelo controle por fluxo (ADR-003). Os cards também mostram divergências entre janelas e lógica: M1-12 termina antes de M1-11, M1-03 e M1-04 terminam antes de M1-17, e M1-08 foi concluído com M1-15 ainda em revisão (situação de 25/10/2026). A rede registra a lógica prevista nos cards, não a ordem real de execução.

#### MF2 — Construção

![Rede MF2](../diagramas/cronograma/redes/fig-rede-4-mf2.png)

Figura R.4 — Rede do projeto da MF2 (Construção), replanejada a partir de 03/11/2026 e nivelada por responsável.
Fonte: Elaborado pelos autores (2026).

| Atividade | Descrição | Responsável | Esforço (h) | D (dias úteis) | Predecessoras | ES | EF | LS | LF | Folga |
|---|---|---|---|---|---|---|---|---|---|---|
| **R0** | **Replanejamento (início em 03/11)** | — | — | 0 | — | 0 | 0 | 0 | 0 | 0 |
| **M1-10** | **Modelagem de Dados (DER)** | Edson | 8 | 2 | R0 | 0 | 2 | 0 | 2 | 0 |
| N7.1 | Pipeline CI (lint + testes + coverage) | Leonardo | 6 | 2 | R0 | 0 | 2 | 3 | 5 | 3 |
| M1-09 | Protótipo UX/UI | Edson | 8 | 2 | M1-10 (RD) | 2 | 4 | 6 | 8 | 4 |
| M1-14 | Auditoria de Licenças FOSS | Edson | 3 | 1 | M1-09 (RD) | 4 | 5 | 8 | 9 | 4 |
| N5.1a | Infraestrutura ADR-010 (Docker Compose, PostgreSQL, Alembic) | Leonardo | 12 | 3 | N7.1 | 2 | 5 | 5 | 8 | 3 |
| M1-18 | Lições Aprendidas (MF1) | Leonardo | 2 | 1 | M1-14, N5.1a (RD) | 5 | 6 | 10 | 11 | 5 |
| C0 | Gate M2 (Ambiente e Modelagem) | — | — | 0 | M1-18 | 6 | 6 | 11 | 11 | 5 |
| **N5.1** | **Backend — Lógica de Negócio** | Fabricio | 24 | 6 | M1-10 | 2 | 8 | 2 | 8 | 0 |
| N5.3 | Frontend — Interface e Simulações | Leonardo | 24 | 6 | C0 | 6 | 12 | 11 | 17 | 5 |
| N6.1a | Testes da lógica de negócio (TDD) | Edson | 10 | 3 | M1-14 (RD) | 5 | 8 | 9 | 12 | 4 |
| **N5.2** | **Backend — Câmbio (adapter e circuit breaker) e Cache** | Fabricio | 16 | 4 | N5.1a, N5.1 (RD) | 8 | 12 | 8 | 12 | 0 |
| N5.4 | Módulo PDF (WeasyPrint) | Fabricio | 12 | 3 | N5.2 (RD) | 12 | 15 | 14 | 17 | 2 |
| **N6.1b** | **Testes de integração (coverage ≥ 80 %)** | Edson | 10 | 3 | N5.2, N6.1a | 12 | 15 | 12 | 15 | 0 |
| **N6.3** | **PDCA + Ishikawa 6M** | Edson | 6 | 2 | N6.1b | 15 | 17 | 15 | 17 | 0 |
| **N6.2** | **Testes de Aceitação (UAT presencial)** | Edson | 8 | 2 | N5.3, N5.4, N6.3 (RD) | 17 | 19 | 17 | 19 | 0 |
| **M3** | **Marco M3 — MVP Funcional (Beta)** | — | — | 0 | N6.2 | 19 | 19 | 19 | 19 | 0 |

Fonte: Elaborado pelos autores (2026).

A rede original da MF2 partia do gate C0, que não foi atingido: em 31/10/2026 o M2 seguia aberto com 4 issues. Por isso, ela foi replanejada a partir de 03/11/2026 (R0), com quatro ajustes: os cards pendentes do M2 entram como atividades; N7.1 passa para o início, porque o CI é exigido para todo card chegar a Done; N6.1 é dividido em N6.1a, em paralelo ao backend, e N6.1b, de integração; e N5.5 e N10 passam a ser contínuas. A situação dos cards é a do quadro em 31/10/2026, com M1-13 e M1-15 já concluídos.

A rede também foi nivelada por responsável: as dependências de recurso já estão nas predecessoras, de modo que cada pessoa executa uma atividade por vez. A duração é de **19 dias úteis**, com o caminho crítico R0 → M1-10 → N5.1 → N5.2 → N6.1b → N6.3 → N6.2 → M3. O gate M2 fica em 10/11/2026 e o MVP, em 30/11/2026.

A data-alvo vigente do M3 é 15/11/2026, um domingo e feriado. De 03/11 a 13/11/2026 restam 9 dias úteis, menos da metade do necessário, e por isso **o M3 em 15/11 não é viável**. A mudança para 30/11/2026 é uma **proposta**: depende de change-request, aprovação do CCB e ADR (Plano de Integração §1.7.3). A nova data ainda atende ao objetivo SMART de MVP em novembro.

#### MF3 — Consolidação

![Rede MF3](../diagramas/cronograma/redes/fig-rede-5-mf3.png)

Figura R.5 — Rede do projeto da MF3 (Consolidação).
Fonte: Elaborado pelos autores (2026).

| Atividade | Descrição | Responsável | Esforço (h) | D (dias úteis) | Predecessoras | ES | EF | LS | LF | Folga |
|---|---|---|---|---|---|---|---|---|---|---|
| **M3** | **Marco M3 — MVP Funcional** | — | — | 0 | — | 0 | 0 | 0 | 0 | 0 |
| **N11.1** | **Documentação Técnica (Arquitetura, APIs)** | Fabricio e Edson | 12 | 3 | M3 | 0 | 3 | 0 | 3 | 0 |
| **N11.2** | **Consolidação da Documentação Parcial** | Fabricio e Edson | 12 | 3 | M3 | 0 | 3 | 0 | 3 | 0 |
| **N12.1** | **Lições Aprendidas Finais** | Equipe | 4 | 1 | N11.2 | 3 | 4 | 3 | 4 | 0 |
| **N12.2** | **Verificação SMART** | Equipe | 4 | 1 | N11.1, N11.2 | 3 | 4 | 3 | 4 | 0 |
| **N12.3** | **Apresentação Final + Aceite** | Equipe | 8 | 2 | N12.1, N12.2 | 4 | 6 | 4 | 6 | 0 |
| **M4** | **Marco M4 — Encerramento** | — | — | 0 | N12.3 | 6 | 6 | 6 | 6 | 0 |

Fonte: Elaborado pelos autores (2026).

A MF3 tem duração lógica de **6 dias úteis**, com os caminhos críticos M3 → N11.1 → N12.2 → N12.3 → M4; M3 → N11.2 → N12.1 → N12.3 → M4; M3 → N11.2 → N12.2 → N12.3 → M4. Com a data vigente, a janela de 16/11 a 15/12/2026 tem 21 dias úteis. Com o M3 em 30/11 (proposta), a janela de 01/12 a 15/12/2026 tem 11 dias úteis: o M4 lógico fica em 08/12/2026, com folga de 5 dias úteis para absorver atrasos da MF2.

| Parte da rede | Caminho(s) crítico(s) | Duração lógica (dias úteis) | Janela disponível (dias úteis) |
|---|---|---|---|
| MF1 — Fundação | T0 → M1-01 → M1-02 → M1-18 → M2; T0 → M1-11 → M1-12 → M1-20 → M1-18 → M2; T0 → M1-11 → M1-12 → M1-21 → M1-18 → M2 | 5 | 31 (18/08–30/09) |
| MF2 — Construção | R0 → M1-10 → N5.1 → N5.2 → N6.1b → N6.3 → N6.2 → M3 | 19 (nivelada por responsável) | 9 (03/11–13/11) na data vigente; 19 (03/11–30/11) na proposta |
| MF3 — Consolidação | M3 → N11.1 → N12.2 → N12.3 → M4; M3 → N11.2 → N12.1 → N12.3 → M4; M3 → N11.2 → N12.2 → N12.3 → M4 | 6 | 21 (16/11–15/12) na data vigente; 11 (01/12–15/12) na proposta |

Fonte: Elaborado pelos autores (2026).

A rede considera 4 h por dia, o teto da Premissa P5. Como a dedicação real pode ser menor, a tabela a seguir recalcula as datas para três cenários, com a mesma lógica e o mesmo nivelamento.

| Dedicação por pessoa | Gate M2 | M3 | M4 |
|---|---|---|---|
| 20 h/semana (P5) | 10/11 | 30/11 | 08/12 (dentro do prazo) |
| 15 h/semana | 12/11 | 09/12 | 22/12 (fora do prazo) |
| 10 h/semana | 17/11 | 23/12 | 12/01/2027 (fora do prazo) |

Fonte: Elaborado pelos autores (2026).

Até 31/10/2026, os cards concluídos somavam cerca de 68 h estimadas em pouco mais de 10 semanas, perto de 2 h por pessoa por semana. O número é apenas indicativo, porque não há registro de horas reais e os cards não cobrem todo o trabalho. Mesmo assim, mostra que o cenário de 20 h/semana é otimista. Abaixo dele, cumprir o M4 em 15/12 exige cortar requisitos Should e Could.
