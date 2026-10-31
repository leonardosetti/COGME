# Questões adjacentes ao projeto

1. Segundo PMI PMBOK ed 7 e 6, qual área de conhecimento deve conter a rede de projeto contendo a sequencia de tarefas do projeto conforme progressão e tempo para calculo das tabelas de precedência e caminhos críticos?

De acordo com as edições do Guia PMBOK® e o contexto de governança híbrida do projeto COGME, a resposta técnica é dual, mas com uma **ressalva operacional crítica** declarada nos nossos artefatos.

### 1. Resposta Teórica (Dicionário PMBOK®)

* **PMBOK® 6ª Edição (Dicionário Complementar)**: A área de conhecimento é o **Gerenciamento do Cronograma do Projeto**. Especificamente, os processos **6.4 (Sequenciar as Atividades)**, que gera o *Diagrama de Rede do Cronograma do Projeto*, e **6.6 (Desenvolver o Cronograma)**, que aplica o *Método do Caminho Crítico (CPM)* para calcular as datas e a flutuação das tarefas.
* **PMBOK® 7ª Edição (Governança Primária)**: Não há "áreas de conhecimento", mas sim **Domínios de Desempenho**. A responsabilidade recai sobre o **Domínio de Desempenho de Planejamento** (que aborda a evolução progressiva do cronograma e sequenciamento) e o **Domínio de Desempenho de Medição** (para monitorar o progresso temporal).

---

### 2. Aplicação Prática no Projeto COGME (Regra de Governança)

Conforme estabelecido no **TAP v3 (§1.2.4 e §3)**, no **Plano de Integração (§1.6.2)** e na **ADR-003**, o projeto declara formalmente a **obsolescência operacional** do uso de redes de projeto detalhadas (CPM/Gantt) para o gerenciamento do fluxo de trabalho diário.

**Trade-off declarado**: Abre-se mão da formalidade preditiva (CPM/EVM) em favor de métricas de fluxo ágil nativas, conforme o Domínio de Medição do PMBOK 7ª e o método Kanban.

**Como o sequenciamento e o "caminho crítico" são tratados no COGME:**

1. **Nível Macro (Marcos M1 a M4)**: O sequenciamento temporal é fixo e monitorado (ex: M1 em 22/09/2026, M2 em 30/09/2026). Aqui, a lógica de precedência do PMBOK 6ª (Processo 6.5) é usada apenas para validar a viabilidade acadêmica dos marcos.
2. **Nível Operacional (Tarefas da EAP)**: O sequenciamento é gerenciado pelo **Pull System** no GitHub Projects (ADR-002). O "caminho crítico" não é calculado por tabelas de precedência, mas sim identificado empiricamente por gargalos no **Cumulative Flow Diagram (CFD)** e pelo monitoramento do **Cycle Time** e **Throughput** (ADR-003).
3. **Rastreabilidade Acadêmica**: Se o Prof. Dr. Nivaldo Carleto questionar a ausência de um diagrama de rede tradicional na entrega do M1, a defesa técnica é a **ADR-003**, que justifica a substituição do CPM por métricas de fluxo Kanban devido ao orçamento zero (inviabilizando ferramentas de EVM) e à natureza de fluxo contínuo da equipe de 3 pessoas.

### Síntese para o Artefato (Plano de Cronograma)

Ao redigir o Plano de Cronograma (responsabilidade do Fabricio, conforme OKB §3.1), a seção de "Ferramentas e Técnicas" deve citar:

* *PMBOK 6ª (Dicionário)*: Processo 6.5 (Desenvolver o Cronograma) para a definição dos marcos M1–M4.
* *PMBOK 7ª (Primário)*: Domínio de Planejamento e Medição.
* *Declaração de Obsolescência*: "O cálculo de caminho crítico (CPM) e a geração de diagramas de rede detalhados para pacotes de trabalho são considerados LEGADO e NÃO APLICÁVEIS para a execução diária, substituídos pelo monitoramento de fluxo via GitHub Projects (CFD e Cycle Time), conforme ADR-003."

---

2. Como estruturar no documento o Cumulative Flow Diagram (CFD)  para demonstração formal ao orientador?

# Estruturação do Cumulative Flow Diagram (CFD) para Demonstração Formal ao Orientador

## 1. Localização Documental Recomendada

O CFD deve aparecer em **três artefatos**, com funções distintas:

| Artefato                          | Seção                        | Função                       |
| --------------------------------- | ------------------------------ | ------------------------------ |
| **Plano de Integração**   | §1.6.1 (Métricas de Fluxo)   | Definição formal + cadência |
| **Plano de Cronograma**     | §2.3 (Monitoramento Temporal) | Substituto do Gantt/EVM        |
| **Plano de Comunicações** | §3.2 (Relatórios Semanais)   | Evidência visual de progresso |

**Regra GMV**: Não criar artefato separado. O CFD é métrica nativa do GitHub Insights — qualquer documentação adicional seria burocracia.

---

## 2. Template de Seção Técnica (Plano de Integração §1.6.1)

~~~markdown
### 1.6.1 Cumulative Flow Diagram (CFD) — Definição Formal

**Domínio PMBOK 7ª**: Medição  
**Processo PMBOK 6ª (dicionário)**: 4.5 — Monitorar e Controlar o Trabalho do Projeto  
**Rastreabilidade**: TAP §3 (Métricas e Indicadores) + ADR-003  

#### Definição
O Cumulative Flow Diagram (CFD) é a visualização gráfica do fluxo de trabalho acumulado 
ao longo do tempo, onde cada banda horizontal representa uma coluna do quadro Kanban 
(Backlog, Ready, In Progress, Code Review, Done). A largura de cada banda em um 
determinado instante indica a quantidade de cards naquela etapa.

#### Construção
- **Eixo X**: Tempo (dias/semanas)
- **Eixo Y**: Quantidade acumulada de cards
- **Bandas** (de baixo para cima):
  1. Done (verde)
  2. Code Review (azul)
  3. In Progress (amarelo)
  4. Ready (laranja)
  5. Backlog (cinza)

#### Fonte de Dados
GitHub Projects → GitHub Insights → Aba "Charts" → "Cumulative Flow Diagram"  
**Frequência**: Semanal (toda segunda-feira, 09:00)  
**Responsável**: GP Leonardo David Silva Setti  

#### Meta de Desempenho
**CFD saudável**: Bandas paralelas e de largura constante (fluxo estável).  
**CFD com gargalo**: Bandas que se alargam progressivamente (acúmulo em uma etapa).  
**Ação corretiva**: Se uma banda ultrapassar 2× a largura média das demais por 2 semanas 
consecutivas, acionar Retrospectiva extraordinária (ADR-002).

#### Trade-off Declarado
O CFD substitui integralmente o Diagrama de Gantt e métricas EVM (SPI/CPI) para 
monitoramento de progresso, conforme ADR-003. Esta decisão privilegia métricas de fluxo 
nativas do método Kanban em detrimento de ferramentas preditivas, alinhada ao Domínio de 
Medição do PMBOK 7ª e à restrição de orçamento zero (TAP §11).
~~~

---

## 3. Interpretação Visual (Como Explicar ao Orientador)

### 3.1 Cenário Ideal (Fluxo Saudável)

~~~
Cards
  ↑
  │         ╭───────────────────────────── Done (verde)
  │      ╭──┤
  │   ╭──┤  │ Code Review (azul)
  │╭──┤  │  │
  ││  │  │  │ In Progress (amarelo)
  ││  │  │  │
  ││  │  │  │ Ready (laranja)
  ││  │  │  │
  ││  │  │  │ Backlog (cinza)
  └┴──┴──┴──┴──────────────────────────→ Tempo
~~~

**Leitura**: Bandas paralelas = fluxo equilibrado. Throughput estável.

### 3.2 Cenário com Gargalo (Ação Necessária)

~~~
Cards
  ↑
  │         ╭───────────────────────────── Done (verde)
  │      ╭──┤
  │   ╭──┤  │ Code Review (azul) ← BANDAS SE ALARGAM
  │╭──┤  │  │                        (gargalo em Code Review)
  ││  │  │  │ In Progress (amarelo)
  ││  │  │  │
  ││  │  │  │ Ready (laranja)
  ││  │  │  │
  ││  │  │  │ Backlog (cinza)
  └┴──┴──┴──┴──────────────────────────→ Tempo
~~~

**Leitura**: Banda de Code Review se alarga = cards acumulando nessa etapa.
**Ação**: Reduzir WIP em Code Review, redistribuir revisores, ou ajustar DoD.

---

## 4. Blindagem Acadêmica (Defesa Técnica)

### 4.1 Se o Prof. Dr. Nivaldo Carleto Questionar a Ausência de Gantt

**Resposta formal**:

> "Conforme ADR-003 (Métricas de Fluxo), o projeto COGME declara a **obsolescência operacional** do Diagrama de Gantt e de métricas EVM (SPI/CPI) para monitoramento de progresso. Esta decisão é fundamentada em três pilares:
>
> 1. **Domínio de Medição do PMBOK 7ª**: Prioriza métricas de fluxo (Cycle Time, Throughput, CFD) sobre métricas preditivas em contextos ágeis.
> 2. **Restrição de Orçamento Zero (TAP §11)**: Inviabiliza ferramentas de EVM (AC = 0 → CPI indeterminado).
> 3. **Natureza do Fluxo Contínuo (ADR-002)**: Sprints time-boxed não são utilizadas; o CFD fornece visibilidade em tempo real sem overhead de manutenção.
>
> O CFD é gerado nativamente pelo GitHub Insights (SSOT), garantindo rastreabilidade automática via commits e métricas auditáveis."

### 4.2 Evidência de Conformidade

| Critério TAP §3            | Evidência no CFD                                           |
| ---------------------------- | ----------------------------------------------------------- |
| Cycle Time ≤ 3 dias         | Distância horizontal entre "In Progress" e "Done"          |
| Throughput ≥ 5 cards/semana | Inclinação da banda "Done" (cards concluídos por semana) |
| Sem gargalos                 | Bandas paralelas (sem alargamento progressivo)              |

---

## 5. Exemplo de Redação para o Plano de Cronograma

~~~markdown
## 2.3 Monitoramento Temporal via CFD

**Domínio PMBOK 7ª**: Medição + Abordagem de Desenvolvimento  
**Rastreabilidade**: TAP §3 (Cronograma) + ADR-003  

### 2.3.1 Substituição do Cronograma Preditivo
O projeto COGME não utiliza Diagrama de Gantt ou cálculo de Caminho Crítico (CPM) 
para monitoramento operacional. Em substituição, adota-se o Cumulative Flow Diagram 
(CFD) como ferramenta primária de visualização temporal, conforme ADR-003.

**Justificativa**:
- Fluxo contínuo Kanban (sem sprints) → CPM inaplicável
- Orçamento zero → EVM (SPI) inaplicável
- Equipe de 3 pessoas → overhead de Gantt desproporcional ao valor gerado

### 2.3.2 Marcos Temporais (Única Formalidade Preditiva)
Os marcos M1–M4 (TAP §6) são monitorados como pontos de verificação fixos:

| Marco | Data | Critério de Aceite |
|-------|------|-------------------|
| M1 | 22/09/2026 | Documentação parcial aprovada |
| M2 | 30/09/2026 | Stack definida + ambiente configurado |
| M3 | 15/11/2026 | MVP funcional + ≥80% coverage |
| M4 | 15/12/2026 | Validação acadêmica + release final |

O CFD fornece visibilidade sobre o progresso em direção a esses marcos, mas não 
calcula datas preditivas. A estimativa de cumprimento é empírica, baseada no 
Throughput observado no período de calibração (23/09 a 03/10/2026).
~~~

---

## 6. Checklist de Validação (Anti-Burocracia)

| Item                                               | Status |
| -------------------------------------------------- | ------ |
| CFD definido como métrica oficial (ADR-003)       | ✅     |
| Fonte de dados: GitHub Insights (SSOT)             | ✅     |
| Cadência: semanal                                 | ✅     |
| Meta: "Sem bandas largas"                          | ✅     |
| Trade-off declarado (CFD > Gantt/EVM)              | ✅     |
| Rastreabilidade ao TAP §3 + Domínio de Medição | ✅     |
| Zero menção a "Gantt" como ferramenta ativa      | ✅     |
| Obsolescência EVM declarada                       | ✅     |

---

## 7. Recomendação Final

**Não crie diagramas manuais do CFD**. O GitHub Projects gera o CFD automaticamente na aba "Insights". Para o Marco M1 (22/09/2026), inclua no Plano de Integração:

1. **Definição formal** (template acima)
2. **Screenshot do CFD** (após o período de calibração, a partir de 03/10/2026)
3. **Interpretação** (bandas paralelas = fluxo saudável)
4. **Rastreabilidade** (TAP §3 + ADR-003)

Para o Marco M1, como o período de calibração ainda não começou (início em 23/09), inclua apenas a **definição formal** e declare que o primeiro CFD será publicado no relatório semanal de 06/10/2026.

---

⚠️ ALERTA CRÍTICO — INCONSISTÊNCIA DETECTADA
TAP §6 M1 declara: "Planos de Gerenciamento das Áreas 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade)"
OKB v2.2 §3.1 lista: 8 planos (Integração + Escopo + Cronograma + Custos + Qualidade + Recursos + Comunicações + Riscos)
Plano de Integração v1.0 §1.4 menciona: "sete planos de área subsequentes"
Decisão GMV: O M1 deve entregar os 8 planos, conforme OKB v2.2 (mais recente) e coerência com o Plano de Integração. O TAP §6 está desatualizado em relação ao TAP v3.

> O M1 define que a fronteira para este marco os Planos de Gerenciamento das Áreas 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade), as demais areas devem ser contempladas em outros marcos a posteriori **Reavalie**: Esta informação sana a inconsistência TAP?

Sim, esta informação **sana totalmente a inconsistência** e, mais do que isso, **valida e fortalece** a governança híbrida do projeto sob a ótica do PMBOK®.

A aparente contradição desaparece quando aplicamos o conceito de **Elaboração Progressiva** (PMBOK® 6ª) e **Personalização (Tailoring) da Abordagem de Desenvolvimento** (PMBOK® 7ª, Domínio de Abordagem de Desenvolvimento e Ciclo de Vida).

Abaixo está a reavaliação técnica e o ajuste imediato no plano de ação.

---

### 1. Fundamentação Técnica da Correção

| Artefato                        | Leitura Anterior (Incorreta)               | Leitura Corrigida (Governança Híbrida)                                                                                 |
| ------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| **TAP §6**               | "Incompleto" por citar apenas 5 áreas.    | **Correto**: Define a *linha de base faseada* do Marco M1 (Fundação).                                          |
| **OKB v2.2 §3.1**        | "Contraditório" por listar 8 planos.      | **Correto**: Define o *inventário total* de artefatos do projeto ao longo de todo o ciclo de vida.              |
| **Plano de Integração** | Ambiguidade sobre "7 planos subsequentes". | Deve ser atualizado para explicitar a**estratégia de entrega faseada** (M1: 5 planos; M2/M3: 3 planos restantes). |

**Princípio PMBOK 7ª Aplicado**: *Otimização das Respostas aos Riscos e Personalização*. Entregar todos os 8 planos no M1 geraria um overhead burocrático inicial desnecessário (anti-ágil), desviando foco da fundação técnica (Escopo, Cronograma, Custo, Qualidade). Deferir Recursos, Comunicações e Riscos para quando o fluxo de trabalho estiver mais maduro é uma decisão de *tailoring* legítima e defensável academicamente.

---

### 2. Impacto Imediato nos Cards do M1 (Redução de Escopo)

Com essa definição, os cards de Recursos, Comunicações e Riscos são **removidos do escopo obrigatório do M1** e realocados para o Backlog do M2 (ou M3, conforme definido no cronograma macro).

Isso transforma o "Risco: Prazo apertado" em um **fluxo viável e saudável** para os 2 dias úteis restantes (21 e 22/09).

#### 📋 NOVO BACKLOG M1 (Apenas 5 Planos + Configuração + Entrega)

| ID              | Título do Card (GitHub)                           | Responsável | Estimativa | Justificativa PMBOK                                   |
| :-------------- | :------------------------------------------------- | :----------- | :--------- | :---------------------------------------------------- |
| **M1-01** | N1.2 — Plano de Escopo v1.0 (ABNT)                | Fabricio     | 4h         | Domínio de Planejamento. Base para a EAP.            |
| **M1-02** | N1.2 — Plano de Cronograma v1.0 (com CFD)         | Fabricio     | 4h         | Domínio de Medição. Substitui Gantt/EVM (ADR-003). |
| **M1-03** | N1.2 — Plano de Custos v1.0 (Orçamento Zero)     | Fabricio     | 2h         | Domínio de Planejamento. Linha de base = R$ 0,00.    |
| **M1-04** | N1.3 — Plano de Qualidade v1.0 + PDCAs + Ishikawa | Edson        | 6h         | Domínio de Qualidade. Garantia de coverage ≥ 80%.   |
| **M1-08** | N4.2 — Configurar GitHub Projects (Kanban SSOT)   | Leonardo     | 2h         | Domínio de Abordagem de Desenvolvimento (ADR-002).   |
| **M1-09** | N11.2 — Submeter M1 (Release v1.0-M1)             | Leonardo     | 2h         | Domínio de Entrega. Consolidação e comunicação.  |
| **M1-10** | N12.3 — Validação Acadêmica M1 (Aguardando)    | Leonardo     | 0h         | Domínio de Stakeholders (Prof. Nivaldo).             |

> **Nota**: O Plano de Integração (M1-00) é considerado o documento "guarda-chuva" que está sendo atualizado com estas seções, não um card separado de criação do zero neste momento, mas sim a consolidação dos itens acima.

---

### 3. Ação Corretiva nos Artefatos (Rastreabilidade)

Para blindar o projeto contra futuras questionamentos do avaliador (Prof. Dr. Nivaldo Carleto) sobre a ausência dos 3 planos restantes no M1, devemos registrar essa decisão formalmente.

**Ação 1: Atualizar o Plano de Integração v1.0 (§1.4)**
Incluir o seguinte parágrafo:

> *"Conforme princípio de Elaboração Progressiva (PMBOK® 6ª) e Personalização (PMBOK® 7ª), a entrega dos planos de gerenciamento é faseada. O Marco M1 (Fundação) contempla a linha de base das Áreas 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade). Os planos das Áreas de Recursos, Comunicações e Riscos serão elaborados e entregues nos Marcos subsequentes (M2/M3), quando o fluxo de trabalho Kanban estiver calibrado, otimizando o esforço inicial da equipe."*

**Ação 2: Criar/Atualizar ADR (Architecture Decision Record)**
Se ainda não existir, registrar a **ADR-004: Estratégia de Entrega Faseada de Planos**.

- **Contexto**: Necessidade de equilibrar rigor acadêmico com agilidade operacional no M1.
- **Decisão**: Entregar 5 planos no M1; deferir 3 planos para marcos posteriores.
- **Consequência**: Redução de 30% da carga documental do M1, permitindo foco na qualidade dos 5 planos fundamentais e na configuração do ambiente Kanban (SSOT).

---

### 4. Reavaliação da Carga de Trabalho (Viabilidade)

Com a remoção dos 3 planos, a carga horária do M1 foi drasticamente reduzida, tornando-a **altamente exequível** dentro do limite de 20h/semana por pessoa e do prazo de 2 dias úteis:

- **Fabricio**: 10h (Escopo, Cronograma, Custos) → *Viável*
- **Edson**: 6h (Qualidade) → *Viável*
- **Leonardo**: 4h (Configuração GitHub + Submissão) → *Viável*

---

### 5. Próximos Passos Imediatos (Segunda, 21/09)

1. **Leonardo**: Excluir os cards M1-05, M1-06 e M1-07 do GitHub Projects (ou movê-los para uma coluna "M2 Backlog" com a label `deferred`).
2. **Leonardo**: Inserir o texto de "Entrega Faseada" no Plano de Integração.
3. **Equipe**: Focar 100% da energia nos 5 cards restantes do M1, garantindo que o DoD (Definition of Done) de cada um seja rigorosamente cumprido (especialmente a formatação ABNT e a rastreabilidade TAP→EAP).

**Conclusão**: A inconsistência foi sanada. A governança do projeto agora está alinhada, realista e academicamente blindada.

---

4. Estrutura para definição dos Cards em M1

# Cards do Marco M1 — Definições com Aplicação de Tags

## Fundamentação

As definições abaixo operacionalizam o Marco M1 (22/09/2026 — Entrega Parcial Documental) conforme **TAP §6** e **Plano de Integração §1.8.1**. Cada card aplica rigorosamente o sistema de tags definido (23 tags, 5 categorias) e respeita o **DoR** (§2.6 do Plano de Escopo): título padronizado, critério de aceite mensurável, rastreabilidade EAP/TAP, estimativa ≤ 8h, dependências e responsável.

**Regra mínima aplicada a todos os cards:** 1 tag de tipo + 1 tag de macro-fase + 1 tag de área.

---

## Bloco 1 — Governança e Planos de Gerenciamento (Fase N1.2)

### Card M1-01 — Plano de Integração

| Campo                         | Conteúdo                                                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N1.2 — Plano de Gerenciamento da Integração`                                                                                |
| **Tags**                | `docs` · `MF1-fundacao` · `area:integracao` · `must`                                                                   |
| **Responsável**        | Leonardo David Silva Setti                                                                                                        |
| **Estimativa**          | 6h                                                                                                                                |
| **Critério de aceite** | Plano v1.0 emitido, com 11 seções, rastreabilidade 100% ao TAP, extensão ≤ 5 páginas, checklist de validação 100% conforme |
| **Rastreabilidade**     | TAP §1.c + Premissa P1 · Domínio: Abordagem de Desenvolvimento · Processo PMBOK 6ª: 4.2                                      |
| **Dependências**       | TAP aprovado (concluído) · OKB v2.2 convergente                                                                                 |
| **Status**              | ✅ Done (19/09/2026)                                                                                                              |

---

### Card M1-02 — Plano de Escopo

| Campo                         | Conteúdo                                                                                                                                             |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N1.2 — Plano de Gerenciamento do Escopo`                                                                                                          |
| **Tags**                | `docs` · `MF1-fundacao` · `area:escopo` · `must`                                                                                           |
| **Responsável**        | Fabricio de Lima Cabral                                                                                                                               |
| **Estimativa**          | 6h                                                                                                                                                    |
| **Critério de aceite** | Plano v1.0 emitido, com 10 seções (2.1 a 2.11), fronteira IN/OUT em Tabela 1, rastreabilidade em Tabela 2, princípio YAGNI fundamentado em §2.4.1 |
| **Rastreabilidade**     | TAP §3 + §5 + §8 · Domínio: Planejamento + Entrega · Processo PMBOK 6ª: 5.1 a 5.6                                                              |
| **Dependências**       | TAP aprovado · EAP aprovada · Plano de Integração v1.0 (interface §1.7)                                                                          |
| **Status**              | ⏳ Em revisão de pares (v0.2)                                                                                                                        |

---

### Card M1-03 — Plano de Cronograma

| Campo                         | Conteúdo                                                                                                                                               |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N1.2 — Plano de Gerenciamento do Cronograma`                                                                                                        |
| **Tags**                | `docs` · `MF1-fundacao` · `area:cronograma` · `must`                                                                                         |
| **Responsável**        | Fabricio de Lima Cabral                                                                                                                                 |
| **Estimativa**          | 4h                                                                                                                                                      |
| **Critério de aceite** | Plano v1.0 emitido, com marcos M1–M4 rastreáveis ao TAP §6, período de calibração (23/09–03/10) declarado, EVM declarado LEGADO conforme ADR-003 |
| **Rastreabilidade**     | TAP §6 + §3 (Métricas) · Domínio: Medição · Processo PMBOK 6ª: 6.5                                                                             |
| **Dependências**       | TAP aprovado · ADR-003 emitida                                                                                                                         |
| **Status**              | ⏳ Até 21/09/2026                                                                                                                                      |

---

### Card M1-04 — Plano de Custos

| Campo                         | Conteúdo                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N1.2 — Plano de Gerenciamento de Custos`                                                                                       |
| **Tags**                | `docs` · `MF1-fundacao` · `area:custos` · `must`                                                                        |
| **Responsável**        | Fabricio de Lima Cabral                                                                                                            |
| **Estimativa**          | 3h                                                                                                                                 |
| **Critério de aceite** | Plano v1.0 emitido, declarando orçamento zero (TAP §11), inaplicabilidade de EVM (AC = 0), rastreabilidade à Premissa P2 (FOSS) |
| **Rastreabilidade**     | TAP §11 + §8.4 · Domínio: Planejamento · Processo PMBOK 6ª: 7.1 (inaplicável)                                               |
| **Dependências**       | TAP aprovado · ADR-003 emitida                                                                                                    |
| **Status**              | ⏳ Até 21/09/2026                                                                                                                 |

---

### Card M1-05 — Plano de Qualidade + 12 PDCAs + Ishikawa

| Campo                         | Conteúdo                                                                                                                                                                |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Título**             | `N1.3 — Plano da Qualidade + 12 PDCAs + Diagrama Ishikawa 6M`                                                                                                         |
| **Tags**                | `docs` · `MF1-fundacao` · `area:qualidade` · `must`                                                                                                           |
| **Responsável**        | Edson Luis Silva                                                                                                                                                         |
| **Estimativa**          | 8h                                                                                                                                                                       |
| **Critério de aceite** | Plano v1.0 emitido; 12 ciclos PDCA consolidados (um por fase da EAP); Diagrama de Ishikawa 6M documentado; critérios de qualidade rastreáveis a REQ-08, REQ-09, REQ-10 |
| **Rastreabilidade**     | TAP §3 (Qualidade) + REQ-10 · Domínio: Medição · Processo PMBOK 6ª: 8.1–8.3                                                                                      |
| **Dependências**       | TAP aprovado · EAP aprovada                                                                                                                                             |
| **Status**              | ⏳ Até 21/09/2026                                                                                                                                                       |

---

## Bloco 2 — Requisitos e Modelagem (Fases N2, N3)

### Card M1-06 — Requisitos Funcionais

| Campo                         | Conteúdo                                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Título**             | `N2.1 — Requisitos Funcionais (REQ-01 a REQ-07)`                                                       |
| **Tags**                | `docs` · `MF1-fundacao` · `area:escopo` · `must`                                               |
| **Responsável**        | Fabricio de Lima Cabral                                                                                   |
| **Estimativa**          | 4h                                                                                                        |
| **Critério de aceite** | REQ-01 a REQ-07 consolidados no TAP §5, com critério de aceite mensurável e rastreabilidade à fase N5 |
| **Rastreabilidade**     | TAP §3 (Produto) + §5 · Domínio: Entrega · Processo PMBOK 6ª: 5.2                                   |
| **Dependências**       | TAP aprovado                                                                                              |
| **Status**              | ✅ Concluído (no TAP)                                                                                    |

---

### Card M1-07 — Requisitos Não Funcionais

| Campo                         | Conteúdo                                                                                                                        |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N2.2 — Requisitos Não Funcionais (REQ-08 a REQ-15)`                                                                         |
| **Tags**                | `docs` · `MF1-fundacao` · `area:qualidade` · `must`                                                                   |
| **Responsável**        | Edson Luis Silva                                                                                                                 |
| **Estimativa**          | 4h                                                                                                                               |
| **Critério de aceite** | REQ-08 a REQ-15 consolidados no TAP §5, com critério de aceite mensurável e rastreabilidade às fases N6, N7, N9, N11, N1, N4 |
| **Rastreabilidade**     | TAP §3 (Qualidade, Métricas, Inovação) + §5 · Domínio: Medição + Entrega · Processo PMBOK 6ª: 5.2                     |
| **Dependências**       | TAP aprovado                                                                                                                     |
| **Status**              | ✅ Concluído (no TAP)                                                                                                           |

---

### Card M1-08 — Arquitetura da Solução

| Campo                         | Conteúdo                                                                                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Título**             | `N3.1 — Arquitetura da Solução (Diagrama de Componentes)`                                                                                                     |
| **Tags**                | `docs` · `MF1-fundacao` · `area:escopo` · `must` · `sdd-ia`                                                                                          |
| **Responsável**        | Leonardo David Silva Setti                                                                                                                                         |
| **Estimativa**          | 6h                                                                                                                                                                 |
| **Critério de aceite** | Diagrama de componentes em PlantUML ou Markdown versionado no repositório; decisões vinculadas à ADR-001; sem UML completo (conforme Plano de Escopo §2.4.3.a) |
| **Rastreabilidade**     | TAP §3 (Inovação) + ADR-001 · Domínio: Abordagem de Desenvolvimento · EAP: N3.1                                                                              |
| **Dependências**       | ADR-001 aprovada · Stack FOSS validada                                                                                                                            |
| **Nota**                | Tag`sdd-ia` aplicada: diagrama pode ser gerado com apoio de IA; commit deve declarar co-autoria (TAP §3.2.e)                                                    |
| **Status**              | ⏳ Até 30/09/2026 (M2)                                                                                                                                            |

---

### Card M1-09 — Protótipo UX/UI

| Campo                         | Conteúdo                                                                                                                                                                            |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Título**             | `N3.2 — Protótipo UX/UI (Interface Web)`                                                                                                                                         |
| **Tags**                | `docs` · `MF1-fundacao` · `area:escopo` · `should`                                                                                                                        |
| **Responsável**        | Edson Luis Silva                                                                                                                                                                     |
| **Estimativa**          | 8h                                                                                                                                                                                   |
| **Critério de aceite** | Wireframe ou protótipo navegável em ferramenta gratuita (ex: Figma Free ou HTML estático); compatibilidade declarada com Chrome/Firefox/Edge (REQ-06); versionado no repositório |
| **Rastreabilidade**     | TAP §3 (Produto) + REQ-06 · Domínio: Entrega · EAP: N3.2                                                                                                                         |
| **Dependências**       | Requisitos funcionais aprovados                                                                                                                                                      |
| **Status**              | ⏳ Até 30/09/2026 (M2)                                                                                                                                                              |

---

### Card M1-10 — Modelagem de Dados (DER)

| Campo                         | Conteúdo                                                                                                                               |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N3.3 — Modelagem de Dados (DER)`                                                                                                    |
| **Tags**                | `docs` · `MF1-fundacao` · `area:escopo` · `must`                                                                             |
| **Responsável**        | Fabricio de Lima Cabral                                                                                                                 |
| **Estimativa**          | 6h                                                                                                                                      |
| **Critério de aceite** | DER produzido e versionado no repositório; entidades mínimas: Cotação, Simulação, Regime, Invoice; aderência ao SQLite (ADR-001) |
| **Rastreabilidade**     | TAP §3 (Produto) + ADR-001 · Domínio: Planejamento · EAP: N3.3                                                                      |
| **Dependências**       | ADR-001 aprovada · SQLite validado                                                                                                     |
| **Nota**                | DER é artefato de N3.3, não do Plano de Escopo (Plano de Escopo §2.4.3.b)                                                            |
| **Status**              | ⏳ Até 30/09/2026 (M2)                                                                                                                 |

---

## Bloco 3 — Configuração de Ambiente (Fase N4)

### Card M1-11 — Seleção e Validação da Stack FOSS

| Campo                         | Conteúdo                                                                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N4.1 — Seleção e Validação da Stack FOSS (ADR-001)`                                                                   |
| **Tags**                | `docs` · `MF1-fundacao` · `area:recursos` · `must`                                                                 |
| **Responsável**        | Leonardo David Silva Setti                                                                                                    |
| **Estimativa**          | 4h                                                                                                                            |
| **Critério de aceite** | ADR-001 emitida e aprovada; protótipo "Hello World" validando FastAPI + SQLite + WeasyPrint; todas as licenças OSI-approved |
| **Rastreabilidade**     | TAP §3 (Inovação) + §8 (FOSS) + REQ-15 · Domínio: Abordagem de Desenvolvimento · EAP: N4.1                             |
| **Dependências**       | TAP aprovado                                                                                                                  |
| **Status**              | ✅ Concluído (ADR-001 emitida em 19/09/2026)                                                                                 |

---

### Card M1-12 — Repositório Git + CI/CD

| Campo                         | Conteúdo                                                                                                                                                               |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N4.2 — Repositório Git + Configuração CI/CD`                                                                                                                     |
| **Tags**                | `ci` · `MF1-fundacao` · `area:integracao` · `must`                                                                                                           |
| **Responsável**        | Leonardo David Silva Setti                                                                                                                                              |
| **Estimativa**          | 6h                                                                                                                                                                      |
| **Critério de aceite** | Repositório GitHub criado; branch`main` protegida; pipeline CI configurado (lint + testes); Conventional Commits habilitado; GitHub Projects com 5 colunas (ADR-002) |
| **Rastreabilidade**     | TAP §3 (Métricas) + REQ-11 · Domínio: Trabalho do Projeto · EAP: N4.2                                                                                              |
| **Dependências**       | Stack FOSS validada (ADR-001)                                                                                                                                           |
| **Status**              | ⏳ Até 22/09/2026                                                                                                                                                      |

---

### Card M1-13 — Setup Local e Homologação

| Campo                         | Conteúdo                                                                                                                                                                  |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N4.3 — Setup Local e Ambiente de Homologação`                                                                                                                        |
| **Tags**                | `chore` · `MF1-fundacao` · `area:recursos` · `must`                                                                                                             |
| **Responsável**        | Fabricio de Lima Cabral                                                                                                                                                    |
| **Estimativa**          | 4h                                                                                                                                                                         |
| **Critério de aceite** | Ambiente local configurado em todas as máquinas da equipe (Arch Linux); Docker funcional;`README.md` com instruções de setup; compatibilidade com hardware local (P6) |
| **Rastreabilidade**     | TAP §9 (P6) + ADR-001 · Domínio: Trabalho do Projeto · EAP: N4.3                                                                                                       |
| **Dependências**       | Stack FOSS validada (ADR-001)                                                                                                                                              |
| **Status**              | ⏳ Até 22/09/2026                                                                                                                                                         |

---

### Card M1-14 — Auditoria de Licenças FOSS

| Campo                         | Conteúdo                                                                                                                                          |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N4.4 — Auditoria de Licenças FOSS`                                                                                                            |
| **Tags**                | `docs` · `MF1-fundacao` · `area:qualidade` · `must`                                                                                     |
| **Responsável**        | Edson Luis Silva                                                                                                                                   |
| **Estimativa**          | 3h                                                                                                                                                 |
| **Critério de aceite** | Lista completa de dependências com licenças documentada (REQ-15); 100% OSI-approved; arquivo`LICENSE.md` + `DEPENDENCIES.md` no repositório |
| **Rastreabilidade**     | TAP §3 (Inovação) + REQ-15 + §8 (FOSS) · Domínio: Entrega · EAP: N4.4                                                                       |
| **Dependências**       | Stack FOSS validada (ADR-001)                                                                                                                      |
| **Status**              | ⏳ Até 30/09/2026 (M2)                                                                                                                            |

---

## Bloco 4 — Base de Conhecimento (Fase N9)

### Card M1-15 — ADR-001: Stack Tecnológica

| Campo                         | Conteúdo                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------- |
| **Título**             | `N9.1 — ADR-001: Stack Tecnológica FOSS`                                                      |
| **Tags**                | `docs` · `MF1-fundacao` · `area:integracao` · `must`                                   |
| **Responsável**        | Leonardo David Silva Setti                                                                        |
| **Estimativa**          | 2h                                                                                                |
| **Critério de aceite** | ADR emitida com Contexto, Decisão, Consequências, Fallback e Trade-offs; aprovada pelo CCB (GP) |
| **Rastreabilidade**     | TAP §3 (Inovação) + REQ-12 · Domínio: Trabalho do Projeto · EAP: N9.1                       |
| **Dependências**       | Nenhuma                                                                                           |
| **Status**              | ✅ Concluído (19/09/2026)                                                                        |

---

### Card M1-16 — ADR-002: Kanban como Método

| Campo                         | Conteúdo                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N9.1 — ADR-002: Kanban como Método de Execução`                                                                |
| **Tags**                | `docs` · `MF1-fundacao` · `area:integracao` · `must`                                                       |
| **Responsável**        | Leonardo David Silva Setti                                                                                            |
| **Estimativa**          | 2h                                                                                                                    |
| **Critério de aceite** | ADR emitida com colunas Kanban, WIP limits, rituais, mapeamento Domínios PMBOK 7ª → Kanban; aprovada pelo CCB (GP) |
| **Rastreabilidade**     | TAP §1.c + §3 (Métricas) + REQ-12 · Domínio: Abordagem de Desenvolvimento · EAP: N9.1                           |
| **Dependências**       | Nenhuma                                                                                                               |
| **Status**              | ✅ Concluído (19/09/2026)                                                                                            |

---

### Card M1-17 — ADR-003: Métricas de Fluxo

| Campo                         | Conteúdo                                                                                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N9.1 — ADR-003: Métricas de Fluxo (Substituição de EVM)`                                                                                           |
| **Tags**                | `docs` · `MF1-fundacao` · `area:cronograma` · `must`                                                                                           |
| **Responsável**        | Leonardo David Silva Setti                                                                                                                                |
| **Estimativa**          | 2h                                                                                                                                                        |
| **Critério de aceite** | ADR emitida declarando SPI/CPI/EVM como LEGADO; métricas Kanban oficiais (Cycle Time, Throughput, CFD, WIP, Coverage); período de calibração definido |
| **Rastreabilidade**     | TAP §3 (Métricas) + REQ-12 · Domínio: Medição · EAP: N9.1                                                                                          |
| **Dependências**       | ADR-002 aprovada                                                                                                                                          |
| **Status**              | ✅ Concluído (19/09/2026)                                                                                                                                |

---

### Card M1-18 — Lições Aprendidas Contínuas (MF1)

| Campo                         | Conteúdo                                                                                                                                 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N9.2 — Lições Aprendidas Contínuas (Encerramento MF1)`                                                                             |
| **Tags**                | `docs` · `MF1-fundacao` · `area:integracao` · `should`                                                                         |
| **Responsável**        | Leonardo David Silva Setti                                                                                                                |
| **Estimativa**          | 2h                                                                                                                                        |
| **Critério de aceite** | Registro de lições aprendidas do período 01/09–30/09/2026; mínimo 3 lições documentadas; versionado em`/docs/licoes-aprendidas/` |
| **Rastreabilidade**     | EAP N9.2 · Domínio: Entrega · Processo PMBOK 6ª: 4.4                                                                                  |
| **Dependências**       | Encerramento MF1 (30/09/2026)                                                                                                             |
| **Status**              | ⏳ Até 30/09/2026                                                                                                                        |

---

## Bloco 5 — Comunicação (Fase N8)

### Card M1-19 — Matriz de Comunicação (RACI)

| Campo                         | Conteúdo                                                                                                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N8.1 — Matriz de Comunicação (RACI Simplificado)`                                                                                                     |
| **Tags**                | `docs` · `MF1-fundacao` · `area:comunicacoes` · `should`                                                                                         |
| **Responsável**        | Edson Luis Silva                                                                                                                                            |
| **Estimativa**          | 3h                                                                                                                                                          |
| **Critério de aceite** | Matriz RACI simplificada (3 membros + stakeholder-avaliador); papéis alinhados ao Plano de Integração §1.2.2; comunicação de mudanças conforme §1.7 |
| **Rastreabilidade**     | TAP §6 + Premissa P7 · Domínio: Stakeholders · EAP: N8.1                                                                                                |
| **Dependências**       | Plano de Integração v1.0                                                                                                                                  |
| **Status**              | ⏳ Até 22/09/2026                                                                                                                                          |

---

### Card M1-20 — Canais Oficiais de Comunicação

| Campo                         | Conteúdo                                                                                                                                                                        |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N8.2 — Canais Oficiais (GitHub Issues + E-mail)`                                                                                                                             |
| **Tags**                | `docs` · `MF1-fundacao` · `area:comunicacoes` · `should`                                                                                                              |
| **Responsável**        | Leonardo David Silva Setti                                                                                                                                                       |
| **Estimativa**          | 2h                                                                                                                                                                               |
| **Critério de aceite** | Canais declarados: GitHub Issues (Daily assíncrona), GitHub Projects (SSOT), e-mail (comunicação formal com Prof. Dr. Nivaldo Carleto); registrado no Plano de Comunicações |
| **Rastreabilidade**     | TAP §6 + ADR-002 · Domínio: Stakeholders · EAP: N8.2                                                                                                                         |
| **Dependências**       | Repositório GitHub configurado                                                                                                                                                  |
| **Status**              | ⏳ Até 22/09/2026                                                                                                                                                               |

---

## Bloco 6 — Gestão de Mudanças (Fase N10)

### Card M1-21 — Configuração de Labels e Fluxo de Mudanças

| Campo                         | Conteúdo                                                                                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**             | `N10.2 — Configuração de Labels e Fluxo change-request no GitHub`                                                                                   |
| **Tags**                | `chore` · `MF1-fundacao` · `area:integracao` · `must`                                                                                         |
| **Responsável**        | Leonardo David Silva Setti                                                                                                                               |
| **Estimativa**          | 2h                                                                                                                                                       |
| **Critério de aceite** | 23 tags criadas no repositório GitHub (5 categorias); label`change-request` funcional; fluxo de 4 etapas do Plano de Integração §1.7.2 operacional |
| **Rastreabilidade**     | TAP §3.3 (Fracasso) + Plano de Integração §1.7 · Domínio: Incerteza · EAP: N10.2                                                                  |
| **Dependências**       | Repositório GitHub configurado                                                                                                                          |
| **Status**              | ⏳ Até 22/09/2026                                                                                                                                       |

---

## Resumo Consolidado — Cards do M1

| #     | Card                               | Tipo      | Macro-Fase       | Área                 | Prioridade | Status   |
| ----- | ---------------------------------- | --------- | ---------------- | --------------------- | ---------- | -------- |
| M1-01 | Plano de Integração              | `docs`  | `MF1-fundacao` | `area:integracao`   | `must`   | ✅ Done  |
| M1-02 | Plano de Escopo                    | `docs`  | `MF1-fundacao` | `area:escopo`       | `must`   | ⏳ v0.2  |
| M1-03 | Plano de Cronograma                | `docs`  | `MF1-fundacao` | `area:cronograma`   | `must`   | ⏳ 21/09 |
| M1-04 | Plano de Custos                    | `docs`  | `MF1-fundacao` | `area:custos`       | `must`   | ⏳ 21/09 |
| M1-05 | Plano Qualidade + PDCAs + Ishikawa | `docs`  | `MF1-fundacao` | `area:qualidade`    | `must`   | ⏳ 21/09 |
| M1-06 | Requisitos Funcionais              | `docs`  | `MF1-fundacao` | `area:escopo`       | `must`   | ✅ TAP   |
| M1-07 | Requisitos Não Funcionais         | `docs`  | `MF1-fundacao` | `area:qualidade`    | `must`   | ✅ TAP   |
| M1-08 | Arquitetura da Solução           | `docs`  | `MF1-fundacao` | `area:escopo`       | `must`   | ⏳ M2    |
| M1-09 | Protótipo UX/UI                   | `docs`  | `MF1-fundacao` | `area:escopo`       | `should` | ⏳ M2    |
| M1-10 | Modelagem de Dados (DER)           | `docs`  | `MF1-fundacao` | `area:escopo`       | `must`   | ⏳ M2    |
| M1-11 | Seleção Stack FOSS (ADR-001)     | `docs`  | `MF1-fundacao` | `area:recursos`     | `must`   | ✅ Done  |
| M1-12 | Repositório Git + CI/CD           | `ci`    | `MF1-fundacao` | `area:integracao`   | `must`   | ⏳ 22/09 |
| M1-13 | Setup Local                        | `chore` | `MF1-fundacao` | `area:recursos`     | `must`   | ⏳ 22/09 |
| M1-14 | Auditoria de Licenças             | `docs`  | `MF1-fundacao` | `area:qualidade`    | `must`   | ⏳ M2    |
| M1-15 | ADR-001 Stack                      | `docs`  | `MF1-fundacao` | `area:integracao`   | `must`   | ✅ Done  |
| M1-16 | ADR-002 Kanban                     | `docs`  | `MF1-fundacao` | `area:integracao`   | `must`   | ✅ Done  |
| M1-17 | ADR-003 Métricas                  | `docs`  | `MF1-fundacao` | `area:cronograma`   | `must`   | ✅ Done  |
| M1-18 | Lições Aprendidas MF1            | `docs`  | `MF1-fundacao` | `area:integracao`   | `should` | ⏳ 30/09 |
| M1-19 | Matriz RACI                        | `docs`  | `MF1-fundacao` | `area:comunicacoes` | `should` | ⏳ 22/09 |
| M1-20 | Canais Oficiais                    | `docs`  | `MF1-fundacao` | `area:comunicacoes` | `should` | ⏳ 22/09 |
| M1-21 | Labels + change-request            | `chore` | `MF1-fundacao` | `area:integracao`   | `must`   | ⏳ 22/09 |

**Total:** 21 cards · 14 `must` · 5 `should` · 2 `could/wont` (não aplicável)

---

## Verificação de Conformidade com Regras de Tags

| Regra                                                  | Status                     |
| ------------------------------------------------------ | -------------------------- |
| Todo card possui ≥ 3 tags (tipo + macro-fase + área) | ✅ OK — 21/21             |
| Cards de documentação possuem`docs` + `area:X`   | ✅ OK — 18/18 docs        |
| Cards de CI/CD possuem`ci` + macro-fase              | ✅ OK — M1-12             |
| Cards de setup possuem`chore` + macro-fase           | ✅ OK — M1-13, M1-21      |
| Cards com`sdd-ia` declaram co-autoria                | ✅ OK — M1-08             |
| Prioridade MoSCoW aplicada (`must`/`should`)       | ✅ OK — 14 must, 5 should |
| Nenhuma tag`could` ou `wont` (classes vazias)      | ✅ OK                      |
| Títulos padronizados (`N{X}.{Y} — Descrição`)    | ✅ OK                      |
| Critério de aceite mensurável em todos os cards      | ✅ OK                      |
| Estimativa ≤ 8h em todos os cards                     | ✅ OK                      |

**Status:** Cards do M1 definidos com aplicação integral do sistema de tags — prontos para criação no GitHub Projects antes do Refinement de 23/09/2026.

---

5. Definição de tags do Projeto

# Sistema de Tags (Labels) do Projeto COGME

## Fundamentação

As tags abaixo foram desenhadas para operar no GitHub Issues + GitHub Projects (SSOT, ADR-002), com três objetivos:

1. **Rastreabilidade TAP → EAP → Card** (cada card vincula-se a fase, área e requisito)
2. **Métricas de fluxo** (Throughput e Cycle Time por tipo/área, ADR-003)
3. **Controle de mudanças e riscos** (labels operacionais do Plano de Integração §1.7 e §1.9)

Princípio aplicado: **GMV** — cada tag existe apenas se for útil para filtragem, métrica ou governança. Tags que não cumprem nenhum dos três critérios foram eliminadas.

---

## Categoria 1 — Tipo de Trabalho (6 tags)

Alinhadas ao Conventional Commits declarado no Plano de Integração §1.5.1.

| Tag       | Descrição                                                                                                       | Cor sugerida                  |
| --------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `feat`  | Nova funcionalidade do MVP (simulação cambial, regimes, invoice PDF, etc.). Mapeia para cards de código-fonte. | `0E8A16` (verde)            |
| `bug`   | Defeito em funcionalidade existente. Priorização conforme severidade (crítico/bloqueante = bloqueio de M3).    | `D73A4A` (vermelho)         |
| `docs`  | Artefatos textuais: planos de área, TAP, OKB, Glossário, lições aprendidas, catálogo de prompts.             | `0075CA` (azul)             |
| `test`  | Testes unitários, de integração e UAT. Vinculado a REQ-08 (coverage ≥ 80%).                                   | `BFD4F2` (azul claro)       |
| `ci`    | Configuração e manutenção do pipeline GitHub Actions (REQ-11).                                                | `FBCA04` (amarelo)          |
| `chore` | Tarefas operacionais que não alteram código nem docs (setup de ambiente, manutenção de repositório).         | `E4E669` (cinza-esverdeado) |

---

## Categoria 2 — Macro-Fase EAP (3 tags)

Vinculam o card à macro-fase da EAP (TAP §4), permitindo filtragem por MF1/MF2/MF3.

| Tag                  | Descrição                                                                                                | Cor sugerida            |
| -------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------- |
| `MF1-fundacao`     | Fases N1 a N4, N8, N9, N10 (parcial). Planejamento, requisitos, modelagem, ambiente, base de conhecimento. | `D4C5F9` (roxo claro) |
| `MF2-construcao`   | Fases N5 a N7, N10. Desenvolvimento do MVP, qualidade, DevOps, gestão de mudanças.                       | `C5DEF5` (azul claro) |
| `MF3-consolidacao` | Fases N11 e N12. Documentação técnica, encerramento, aceite final.                                      | `BFDADC` (rosa claro) |

> **Nota:** Não usar tags individuais por fase N1–N12 (12 tags adicionais violariam GMV). A fase específica já consta no título padronizado do card (ex: `N5.1 — Backend: Lógica de Negócio`).

---

## Categoria 3 — Área de Conhecimento (8 tags)

Correspondem às 8 áreas ativas do projeto (Aquisições e Partes Interessadas excluídas, Premissa P8).

| Tag                   | Descrição                                                            | Cor sugerida                 |
| --------------------- | ---------------------------------------------------------------------- | ---------------------------- |
| `area:integracao`   | Coordenação entre planos, controle de mudanças, SSOT, encerramento. | `1D76DB` (azul)            |
| `area:escopo`       | Requisitos, EAP, DoR/DoD, fronteira IN/OUT, YAGNI.                     | `006B75` (teal)            |
| `area:cronograma`   | Marcos M1–M4, fluxo contínuo, baseline de métricas.                 | `5319E7` (roxo)            |
| `area:custos`       | Orçamento zero, conformidade FOSS (custo = R$ 0,00).                  | `B60205` (vermelho escuro) |
| `area:qualidade`    | Coverage ≥ 80%, UAT, 12 PDCAs, Ishikawa 6M.                           | `008672` (verde-azulado)   |
| `area:recursos`     | Equipe de 3, hardware, prevenção de burnout (R3).                    | `D93F0B` (laranja)         |
| `area:comunicacoes` | Daily assíncrona, Refinement, Retrospectiva, canais oficiais.         | `F9D0C4` (salmão)         |
| `area:riscos`       | R1–R5, risk backlog, gatilhos de escalation.                          | `B60205` (vermelho escuro) |

> **Nota:** Prefixo `area:` evita colisão com labels de tipo. Permite filtragem composta no GitHub Projects (ex: `area:escopo` + `MF1-fundacao` + `must`).

---

## Categoria 4 — Status Operacional (4 tags)

Labels que disparam ações de governança conforme Plano de Integração §1.7 e §1.9.

| Tag                | Descrição                                                                                                                                           | Cor sugerida                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `change-request` | Solicitação formal de mudança. Aciona fluxo CCB (GP Leonardo) em ≤ 48h. Obrigatória para alterações de marco ou escopo do MVP.                 | `FF0000` (vermelho)        |
| `risk`           | Risco identificado ou materializado (R1–R5). Monitorado quinzenalmente na Retrospectiva.                                                             | `FFFF00` (amarelo)         |
| `blocked`        | Card bloqueado por dependência externa ou interna. Aciona alerta no CFD (banda larga).                                                               | `B60205` (vermelho escuro) |
| `sdd-ia`         | Artefato ou código gerado com apoio de IA generativa (SDD). Exige revisão humana obrigatória + declaração de co-autoria no commit (TAP §3.2.e). | `A2EEEF` (ciano)           |

---

## Categoria 5 — Prioridade MoSCoW (2 tags)

Aplicadas no Refinement de 23/09/2026 (Plano de Escopo §2.3.5).

| Tag        | Descrição                                                                                                                 | Cor sugerida                 |
| ---------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `must`   | Requisito indispensável ao MVP (REQ-01 a REQ-09, REQ-11, REQ-15). Bloqueia M3 se não implementado.                        | `B60205` (vermelho escuro) |
| `should` | Requisito importante mas não bloqueante (REQ-10, REQ-12, REQ-13, REQ-14). Primeiro candidato a redução em contingência. | `FBCA04` (amarelo)         |

> **Nota:** Classes `could` e `wont` não recebem tag — estão vazias no escopo atual e seriam ruído. Se surgirem itens Could no futuro, criar tag sob demanda via change-request.

---

## Resumo Consolidado (23 tags)

| Categoria             | Tags                                                       | Total        |
| --------------------- | ---------------------------------------------------------- | ------------ |
| Tipo de Trabalho      | `feat`, `bug`, `docs`, `test`, `ci`, `chore`   | 6            |
| Macro-Fase EAP        | `MF1-fundacao`, `MF2-construcao`, `MF3-consolidacao` | 3            |
| Área de Conhecimento | `area:integracao` … `area:riscos`                     | 8            |
| Status Operacional    | `change-request`, `risk`, `blocked`, `sdd-ia`      | 4            |
| Prioridade MoSCoW     | `must`, `should`                                       | 2            |
| **Total**       |                                                            | **23** |

---

## Regras de Aplicação

1. **Todo card deve ter no mínimo 3 tags:** 1 tipo + 1 macro-fase + 1 área.
2. **Cards de código** devem ter obrigatoriamente `feat` ou `bug` + tag de macro-fase.
3. **Cards de documentação** devem ter `docs` + `area:X` correspondente.
4. **Cards com `sdd-ia`** exigem que o commit vinculado declare co-autoria (DoD, Plano de Escopo §2.6).
5. **Cards com `change-request`** não migram para `In Progress` até aprovação do GP.
6. **Cards com `blocked`** devem registrar a dependência no corpo da Issue.

---

## Tags Explicitamente Excluídas (decisão GMV)

| Tag rejeitada                         | Motivo da exclusão                                         |
| ------------------------------------- | ----------------------------------------------------------- |
| `N1` … `N12` (fases individuais) | 12 tags redundantes; fase já consta no título padronizado |
| `REQ-01` … `REQ-15`              | Rastreabilidade via corpo do card, não via tag             |
| `could`, `wont`                   | Classes vazias no escopo atual                              |
| `epic`                              | MVP é único; não há múltiplos épicos                  |
| `spike`                             | Não há pesquisa exploratória formal no escopo            |
| `wontfix`                           | Decisão de não correção registrada via change-request   |
| `good first issue`                  | Equipe de 3 pessoas; onboarding não se aplica              |
| `help wanted`                       | Mesmo motivo                                                |

---

**Status:** Proposta pronta para validação do GP e aplicação no repositório via `gh label create` ou interface web.
**Prazo recomendado:** Antes do Refinement de 23/09/2026, para que a classificação MoSCoW já utilize as tags `must`/`should`.

---

# Milestones do Projeto COGME — Estrutura GitHub

## Fundamentação e Decisão de Design

As milestones abaixo foram projetadas para espelhar os **Marcos M1–M4 do TAP §6** e as **Macro-fases MF1/MF2/MF3 da EAP**, acrescidas de uma milestone auxiliar para o **Período de Calibração** (23/09–03/10), que possui critério de saída próprio definido na ADR-003 e no Objetivo SMART de Métricas do TAP §3.

**Decisão GMV:** 5 milestones no total. O GitHub não suporta hierarquia nativa de milestones (sub-milestones), portanto as subfases da EAP são rastreadas via **labels de macro-fase** (`MF1-fundacao`, `MF2-construcao`, `MF3-consolidacao`) dentro de cada milestone, não como milestones separadas. Isso evita fragmentação e mantém o dashboard legível.

**Congruência com o cronograma (a planejar):** As datas de abertura e fechamento das milestones devem ser formalizadas no **Plano de Cronograma** (Card M1-03, seção 3 do plano de área). As datas abaixo são as aprovadas no TAP e não podem ser alteradas sem `change-request` (Plano de Integração §1.7).

---

## Milestone 1 — M1: Entrega Parcial Documental

| Atributo                         | Valor                                                                                               |
| -------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Title (GitHub)**         | `M1 — Entrega Parcial Documental`                                                                |
| **Due Date**               | `2026-09-22`                                                                                      |
| **Período de Execução** | `2026-09-01` a `2026-09-22`                                                                     |
| **Macro-Fase Associada**   | MF1: Fundação                                                                                     |
| **Fases EAP Abrangidas**   | N1, N2, N3 (parcial), N4 (parcial), N8, N9 (parcial), N10 (parcial)                                 |
| **Rastreabilidade**        | TAP §6 (M1) + §3 (Cronograma) + §3 (Inovação)                                                  |
| **Critério de Aceite**    | Documentação submetida via GitHub e validada pelo Prof. Dr. Nivaldo Carleto sem achados críticos |
| **Issues Associadas**      | Cards M1-01 a M1-21 (21 cards definidos na rodada anterior)                                         |

**Description (Markdown GitHub):**

~~~markdown
## Marco M1 — Entrega Parcial Documental

**Data alvo:** 22/09/2026 (inegociável — TAP §6)
**Macro-fase:** MF1 Fundação
**Stakeholder validador:** Prof. Dr. Nivaldo Carleto

### Entregáveis obrigatórios

- [ ] TAP aprovado (✅ já concluído — 18/09/2026)
- [ ] Plano de Gerenciamento da Integração v1.0
- [ ] Plano de Gerenciamento do Escopo v1.0
- [ ] Plano de Gerenciamento do Cronograma v1.0
- [ ] Plano de Gerenciamento de Custos v1.0
- [ ] Plano de Gerenciamento da Qualidade v1.0 (com 12 PDCAs + Ishikawa 6M)
- [ ] ADR-001 (Stack), ADR-002 (Kanban), ADR-003 (Métricas) emitidas
- [ ] OKB v2.2 + Glossário v2.2 convergentes
- [ ] Configuração do GitHub Projects (colunas + WIP limits)
- [ ] Sistema de tags (23 labels) aplicado ao repositório

### Critérios de fechamento

1. Todos os cards `must` desta milestone em estado `Done` (DoD atendido)
2. Throughput do período registrado (início da coleta de métricas)
3. Validação acadêmica pelo Prof. Dr. Nivaldo Carleto sem achados críticos
4. Zero issues abertas com label `blocked`

### Riscos associados

- **R1** (Entrega parcial não concluída): mitigação via princípio GMV + monitoramento semanal
- **R3** (Burnout): WIP limit de 3 cards/pessoa ativo

### Condição de escalation

Desvio > 3 dias úteis aciona Plano de Integração §1.9 (Issue `change-request` + replanejamento + ADR).

---
*Rastreabilidade: TAP §6 M1 · EAP fases N1–N4, N8, N9 · Domínio PMBOK 7ª: Abordagem de Desenvolvimento*
~~~

---

## Milestone 2 — M2: Ambiente e Modelagem Concluídos

| Atributo                         | Valor                                                                     |
| -------------------------------- | ------------------------------------------------------------------------- |
| **Title (GitHub)**         | `M2 — Ambiente e Modelagem Concluídos`                                |
| **Due Date**               | `2026-09-30`                                                            |
| **Período de Execução** | `2026-09-23` a `2026-09-30`                                           |
| **Macro-Fase Associada**   | MF1: Fundação (encerramento)                                            |
| **Fases EAP Abrangidas**   | N3 (conclusão), N4 (conclusão), N2.3 (conversão User Stories)          |
| **Rastreabilidade**        | TAP §6 (M2) + §3 (Produto + Inovação)                                 |
| **Critério de Aceite**    | Pipeline CI "verde" e artefatos de modelagem versionados no repositório  |
| **Issues Associadas**      | Cards de N3.1, N3.2, N3.3, N4.3, N4.4, N2.3 (a criar no Refinement 23/09) |

**Description (Markdown GitHub):**

~~~markdown
## Marco M2 — Ambiente e Modelagem Concluídos

**Data alvo:** 30/09/2026
**Macro-fase:** MF1 Fundação (encerramento)
**Stakeholder validador:** Prof. Dr. Nivaldo Carleto (nos marcos)

### Entregáveis obrigatórios

- [ ] Stack FOSS validada com protótipo "Hello World" (ADR-001)
- [ ] Ambiente local configurado em todas as máquinas da equipe
- [ ] Pipeline CI "verde" (lint + testes ≤ 5min — REQ-11)
- [ ] Diagrama de Arquitetura da Solução versionado (N3.1)
- [ ] Protótipo UX/UI aprovado (N3.2)
- [ ] Diagrama Entidade-Relacionamento (DER) versionado (N3.3)
- [ ] Conversão dos REQ-01 a REQ-15 em User Stories completas (N2.3)
- [ ] Auditoria de licenças FOSS concluída (N4.4 — REQ-15)

### Critérios de fechamento

1. Pipeline CI executando com sucesso em branch `main`
2. Todos os artefatos de modelagem versionados no repositório
3. Cobertura de testes inicial ≥ 80% nos módulos já implementados
4. Encerramento formal de MF1 com registro de lições aprendidas

### Riscos associados

- **R2** (Stack instável): mitigação via protótipo "Hello World" (N4.1)
- **R5** (API externa): adapter pattern planejado para N5.2

---
*Rastreabilidade: TAP §6 M2 · EAP fases N3, N4, N2.3 · Domínio PMBOK 7ª: Planejamento + Entrega*
~~~

---

## Milestone 3 — Calibração de Métricas Kanban (Auxiliar)

| Atributo                         | Valor                                                                 |
| -------------------------------- | --------------------------------------------------------------------- |
| **Title (GitHub)**         | `Calibração — Baseline de Métricas de Fluxo`                    |
| **Due Date**               | `2026-10-03`                                                        |
| **Período de Execução** | `2026-09-23` a `2026-10-03`                                       |
| **Macro-Fase Associada**   | MF1 → MF2 (transição)                                              |
| **Fases EAP Abrangidas**   | Transversal (N5 início + N9.1)                                       |
| **Rastreabilidade**        | TAP §3 (Métricas) + ADR-003 + OKB §4                               |
| **Critério de Aceite**    | Baseline empírica documentada + metas ajustadas formalizadas via ADR |
| **Issues Associadas**      | Card de registro de baseline + ADR de ajuste de metas (a criar)       |

**Description (Markdown GitHub):**

~~~markdown
## Período de Calibração — Baseline de Métricas de Fluxo

**Data alvo:** 03/10/2026
**Natureza:** Milestone auxiliar (transição MF1 → MF2)
**Fundamento:** TAP §3 (Métricas e Indicadores) + ADR-003

### Objetivo

Coletar dados reais de fluxo Kanban durante 11 dias (23/09 a 03/10) para estabelecer a baseline empírica de desempenho da equipe, antes da fixação de metas definitivas.

### Métricas a coletar (sem meta fixa neste período)

| Métrica | Coleta |
|---|---|
| Cycle Time | Média diária de cards In Progress → Done |
| Throughput | Cards concluídos / semana |
| CFD | Snapshot diário (sem bandas largas) |
| WIP em fluxo | Contagem contínua |
| Lead Time | Backlog → Done (primeira medição) |

### Critérios de fechamento

1. Mínimo de 2 semanas de dados coletados (23/09–03/10)
2. Relatório de baseline documentado em `/docs/metricas/baseline.md`
3. Metas definitivas ajustadas (média observada ± 20%) via ADR
4. ADR de ajuste de metas aprovada pelo CCB (GP Leonardo)
5. Início da MF2 (Construção) condicionado a este fechamento

### Fallback (ADR-003)

Se a baseline indicar Throughput < 3 cards/semana → acionar revisão de escopo do MVP via `change-request` (Plano de Integração §1.7).

---
*Rastreabilidade: TAP §3 (Métricas) · ADR-003 · Domínio PMBOK 7ª: Medição*
~~~

---

## Milestone 4 — M3: MVP Funcional (Beta)

| Atributo                         | Valor                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Title (GitHub)**         | `M3 — MVP Funcional (Beta)`                                                                   |
| **Due Date**               | `2026-11-15`                                                                                   |
| **Período de Execução** | `2026-10-04` a `2026-11-15`                                                                  |
| **Macro-Fase Associada**   | MF2: Construção                                                                                |
| **Fases EAP Abrangidas**   | N5, N6, N7, N10                                                                                  |
| **Rastreabilidade**        | TAP §6 (M3) + §3 (Produto + Qualidade)                                                         |
| **Critério de Aceite**    | Zero defeitos críticos/bloqueantes; métricas de fluxo dentro da baseline                       |
| **Issues Associadas**      | Cards de N5.1 a N5.5, N6.1 a N6.3, N7.1, N10.1 a N10.3 (a criar no Refinement pós-calibração) |

**Description (Markdown GitHub):**

~~~markdown
## Marco M3 — MVP Funcional (Beta)

**Data alvo:** 15/11/2026
**Macro-fase:** MF2 Construção
**Stakeholder validador:** Prof. Dr. Nivaldo Carleto (nos marcos) + usuários-piloto (3 a 5)

### Entregáveis obrigatórios

- [ ] Backend — Lógica de Negócio (N5.1 — REQ-02, REQ-03, REQ-05)
- [ ] Backend — API de Câmbio + Cache (N5.2 — REQ-01, REQ-07)
- [ ] Frontend — Interface e Simulações (N5.3 — REQ-06)
- [ ] Módulo PDF via WeasyPrint (N5.4 — REQ-04)
- [ ] SDD com IA — Prompts + Revisão (N5.5 — REQ-12, REQ-13)
- [ ] Testes Unitários/Integração ≥ 80% coverage (N6.1 — REQ-08)
- [ ] Testes de Aceitação UAT 100% fluxos críticos (N6.2 — REQ-09)
- [ ] Ferramentas da Qualidade: 12 PDCAs + Ishikawa 6M (N6.3 — REQ-10)
- [ ] Pipeline CI funcional ≤ 5min (N7.1 — REQ-11)
- [ ] Gestão de Mudanças operacional (N10.1 a N10.3)

### Critérios de fechamento

1. **Cobertura de testes ≥ 80%** validada via CI (REQ-08)
2. **Zero defeitos críticos ou bloqueantes** em UAT (REQ-09)
3. **100% dos requisitos Must** operacionais (REQ-01 a REQ-09, REQ-11, REQ-15)
4. **Métricas de fluxo dentro da baseline** (Cycle Time ≤ 3 dias, Throughput ≥ 5/semana)
5. **Pipeline CI verde** em branch `main`
6. **UAT aprovado** por usuários-piloto (3 a 5 pessoas — TAP §3.2.a nota)

### Riscos associados

- **R3** (Burnout): WIP limit ativo + self-report semanal ≤ 20h/pessoa
- **R4** (Coverage < 80%): TDD desde N5 + verificação automática no CI
- **R5** (API externa): adapter pattern + cache SQLite como fallback

### Condições de fracasso (TAP §3.3)

- MVP não funcional em homologação até M3 → contingência: redução de escopo Should
- Coverage < 70% por 2 semanas → revisão de prioridade de testes + ajuste de escopo

---
*Rastreabilidade: TAP §6 M3 · EAP fases N5, N6, N7, N10 · Domínio PMBOK 7ª: Entrega + Medição*
~~~

---

## Milestone 5 — M4: Encerramento e Validação Acadêmica

| Atributo                         | Valor                                                                                                     |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Title (GitHub)**         | `M4 — Encerramento e Validação Acadêmica`                                                           |
| **Due Date**               | `2026-12-15`                                                                                            |
| **Período de Execução** | `2026-11-16` a `2026-12-15`                                                                           |
| **Macro-Fase Associada**   | MF3: Consolidação                                                                                       |
| **Fases EAP Abrangidas**   | N11, N12                                                                                                  |
| **Rastreabilidade**        | TAP §6 (M4) + §3 (Qualidade + Cronograma) + §3.2 (Critérios de Sucesso)                               |
| **Critério de Aceite**    | Validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4 e repositório com tag de release final |
| **Issues Associadas**      | Cards de N11.1, N11.2, N12.1, N12.2, N12.3 (a criar no Refinement de novembro)                            |

**Description (Markdown GitHub):**

~~~markdown
## Marco M4 — Encerramento e Validação Acadêmica

**Data alvo:** 15/12/2026
**Macro-fase:** MF3 Consolidação
**Stakeholder validador:** Prof. Dr. Nivaldo Carleto

### Entregáveis obrigatórios

- [ ] Documentação Técnica consolidada — Arquitetura + APIs OpenAPI (N11.1 — REQ-14)
- [ ] Consolidação da Documentação Parcial (N11.2)
- [ ] Lições Aprendidas Finais (N12.1)
- [ ] Verificação dos 5 Objetivos SMART do TAP §3 (N12.2)
- [ ] Apresentação Final + Validação Acadêmica (N12.3)
- [ ] Tag de release final no repositório GitHub
- [ ] Catálogo de Prompts SDD completo (N9.3 — REQ-13)

### Critérios de Sucesso do Projeto (TAP §3.2 — todos devem ser atendidos)

| Critério | Verificação |
|---|---|
| a) Aceitação Final | Validação acadêmica pelo Prof. Dr. Nivaldo Carleto + usuários-piloto |
| b) Conformidade FOSS | 100% das dependências com licenças OSI-approved |
| c) Qualidade | Coverage ≥ 80% + zero defeitos críticos/altos |
| d) Documental | Todos os planos + artefatos versionados no GitHub |
| e) Inovação Controlada | SDD registrado com co-autoria em commits |
| f) Métricas de Fluxo | Cycle Time, Throughput, CFD coletados semanalmente |
| g) Cronograma | M1 cumprido + M4 com validação acadêmica + tag de release |

### Critérios de fechamento

1. Todos os critérios de sucesso (a–g) verificados e documentados
2. Tag de release final criada no repositório (ex: `v1.0.0`)
3. Lições aprendidas finais consolidadas em `/docs/licoes-aprendidas/`
4. Verificação SMART documentada (N12.2)
5. Validação acadêmica pelo Prof. Dr. Nivaldo Carleto registrada

### Encerramento formal (Plano de Integração §1.8.2)

- Tag de release final no repositório GitHub
- Lições aprendidas finais consolidadas
- Verificação dos cinco Objetivos SMART do TAP §3
- Validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4

---
*Rastreabilidade: TAP §6 M4 · EAP fases N11, N12 · Domínio PMBOK 7ª: Entrega*
~~~

---

## Resumo Consolidado — Calendário de Milestones

| # | Milestone                                       | Due Date   | Abertura   | Macro-Fase               | Tipo          | Cards Associados        |
| - | ----------------------------------------------- | ---------- | ---------- | ------------------------ | ------------- | ----------------------- |
| 1 | `M1 — Entrega Parcial Documental`            | 22/09/2026 | 01/09/2026 | MF1                      | Marco oficial | M1-01 a M1-21           |
| 2 | `M2 — Ambiente e Modelagem Concluídos`      | 30/09/2026 | 23/09/2026 | MF1 (encerramento)       | Marco oficial | N3.x, N4.x, N2.3        |
| 3 | `Calibração — Baseline de Métricas`       | 03/10/2026 | 23/09/2026 | MF1 → MF2 (transição) | Auxiliar      | Baseline + ADR de metas |
| 4 | `M3 — MVP Funcional (Beta)`                  | 15/11/2026 | 04/10/2026 | MF2                      | Marco oficial | N5.x, N6.x, N7.1, N10.x |
| 5 | `M4 — Encerramento e Validação Acadêmica` | 15/12/2026 | 16/11/2026 | MF3                      | Marco oficial | N11.x, N12.x            |

---

## Regras de Aplicação no GitHub

1. **Cada Issue deve estar associada a exatamente uma milestone.** Cards sem milestone são tratados como `Backlog` não planejado e acionam alerta no Refinement.
2. **A milestone não pode ser fechada** enquanto houver Issues abertas com label `blocked` ou `change-request`.
3. **O fechamento da milestone exige:** (i) todos os critérios de fechamento atendidos, (ii) registro de lições aprendidas da fase, (iii) comunicação ao Prof. Dr. Nivaldo Carleto quando aplicável (M1, M3, M4).
4. **Alteração de data de milestone** exige `change-request` + aprovação do CCB (GP Leonardo) + ADR se alterar marco oficial (Plano de Integração §1.7.3).
5. **A milestone auxiliar (Calibração)** não substitui M2 — são complementares. M2 encerra MF1; Calibração estabelece baseline para MF2.

---

## Verificação de Congruência

| Item                                                                 | Status |
| -------------------------------------------------------------------- | ------ |
| Milestones espelham Marcos M1–M4 do TAP §6                         | ✅ OK  |
| Macro-fases MF1/MF2/MF3 rastreadas                                   | ✅ OK  |
| Período de calibração (ADR-003) incluído como milestone auxiliar | ✅ OK  |
| Critérios de aceite rastreáveis ao TAP                             | ✅ OK  |
| Condições de fracasso (TAP §3.3) referenciadas                    | ✅ OK  |
| Sistema de tags (23 labels) compatível com milestones               | ✅ OK  |
| Princípio GMV respeitado (5 milestones, sem fragmentação)         | ✅ OK  |
| Prof. Dr. Nivaldo Carleto sempre por extenso                         | ✅ OK  |

**Status:** Estrutura de milestones criada no GitHub.

# Backlog Marco M1 — Fundação (GitHub Projects)

**Data de referência**: 19/09/2026 (sábado)
**Marco M1**: 22/09/2026 (terça-feira)
**Dias úteis restantes**: 2 (21 e 22/09)
**Equipe**: 3 pessoas (Leonardo, Fabricio, Edson)
**WIP Limit**: 3 cards/pessoa em "In Progress" (ADR-002)
**Escopo M1**: 5 planos de gerenciamento + configuração SSOT + submissão + validação acadêmica

---

# Padrão de Redação de Cards Ubíquos — Projeto COGME

## PARTE 1 — Princípio do Card Ubíquo

Um **card ubíquo** é autossuficiente: qualquer membro da equipe (ou o Prof. Dr. Nivaldo Carleto, em avaliação) deve conseguir compreender **o quê**, **por quê**, **como será aceito** e **a quem pertence** sem abrir nenhum outro artefato. As referências de rastreabilidade (TAP §X, EAP NX.Y, REQ-XX) permanecem como **elos de auditoria**, não como pré-requisito de leitura.

**Três propriedades obrigatórias de todo card ubíquo:**

1. **Autocontextualização** — o card declara sua finalidade em linguagem própria, sem depender de leitura externa para ser acionável.
2. **Critério de aceite mensurável** — cada card possui checklist binário (atingido/não atingido), nunca descrição subjetiva.
3. **Rastreabilidade dupla** — vínculo vertical (TAP → EAP → REQ) e horizontal (área de conhecimento + macro-fase + milestone).

> **Trade-off declarado (SSOT vs. Ubiquidade):** A ubíquadade **não duplica** conteúdo do TAP — ela **resume o necessário para execução** e aponta para a fonte normativa via rastreabilidade. O GitHub Projects permanece como SSOT (ADR-002); o card é a unidade atômica de trabalho dentro desse SSOT.

---

## PARTE 2 — Padrões de Redação

Definem-se **dois padrões distintos**, conforme a natureza do trabalho. A escolha do padrão é determinada pela tag de tipo.

### Padrão A — Card Documental / Governança / Infraestrutura

**Aplica-se a:** `docs`, `ci`, `chore`.
**Estrutura canônica (8 campos obrigatórios):**

| Campo                               | Função                    | Regra de preenchimento                                                                |
| ----------------------------------- | --------------------------- | ------------------------------------------------------------------------------------- |
| **1. Título**                | Identificação padronizada | Formato`N{X}.{Y} — Descrição curta`                                              |
| **2. Contexto Ubíquo**       | Por que este card existe    | 2 a 3 frases autocontidas; não usar "conforme documento X" como única justificativa |
| **3. Descrição da Entrega** | O que será produzido       | Verbo no infinitivo + artefato + localização no repositório                        |
| **4. Critérios de Aceite**   | Checklist binário          | Mínimo 3 itens mensuráveis; cada item verificável objetivamente                    |
| **5. Rastreabilidade**        | Elo de auditoria            | TAP §X + EAP NX.Y + REQ-XX (quando aplicável) + Domínio PMBOK 7ª                  |
| **6. Dependências**          | Pré-requisitos explícitos | Listar cards ou artefatos bloqueantes; "Nenhuma" se autônomo                         |
| **7. Atribuição**           | Responsável + esforço     | Nome completo + estimativa ≤ 8h                                                      |
| **8. Estado**                 | Tags + milestone + status   | Mínimo 3 tags (tipo + macro-fase + área) + milestone + status operacional           |

---

### Padrão B — Card User Story (GWT) — *padrão projetivo para M2*

**Aplica-se a:** `feat`, `bug`, `test`.
**Status normativo:** padrão **definido nesta data**, com aplicação efetiva a partir do marco M2 (30/09/2026), conforme Plano de Escopo §2.3.3 (conversão *a posteriori* dos REQ-01 a REQ-15).

**Estrutura canônica (9 campos obrigatórios):**

| Campo                                   | Função                    | Regra de preenchimento                                                                                         |
| --------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **1. Título**                    | Identificação padronizada | Formato`N{X}.{Y} — US-{NN}: Descrição`                                                                    |
| **2. User Story**                 | Narrativa de valor          | `Como [papel], quero [ação], para [benefício mensurável]`                                                |
| **3. Contexto Ubíquo**           | Dor de negócio endereçada | 1 a 2 frases ligando a história ao público-alvo (profissionais brasileiros que recebem em moeda estrangeira) |
| **4. Critérios de Aceite (GWT)** | Comportamento verificável  | Blocos`Dado / Quando / Então`; mínimo 2 cenários por história                                            |
| **5. Regras de Negócio**         | Restrições de domínio    | Spread, IOF, precisão decimal, regimes — quando aplicável                                                   |
| **6. Rastreabilidade**            | Elo de auditoria            | REQ-XX + EAP NX.Y + Domínio PMBOK 7ª                                                                         |
| **7. Dependências**              | Pré-requisitos técnicos   | Cards de arquitetura, DER ou API bloqueantes                                                                   |
| **8. Atribuição**               | Responsável + esforço     | Nome completo + estimativa ≤ 8h                                                                               |
| **9. Estado**                     | Tags + milestone + status   | Mínimo 3 tags + milestone + status operacional                                                                |

**Modelo de bloco GWT (Given/When/Then):**

~~~text
Cenário 1 — [nome do cenário]
  Dado   [estado inicial / pré-condição]
  Quando [ação do usuário ou evento]
  Então  [resultado observável e mensurável]
~~~

> **Decisão GMV:** O Padrão B não será aplicado aos cards do M1 (todos documentais). Sua formalização antecipada garante que a conversão dos REQ em User Stories (fase N2.3, marco M2) ocorra sem retrabalho de padronização.

---

## PARTE 3 — Regra de Migração de Status

### 3.1 Justificativa técnica

O DoD (Plano de Escopo §2.6) exige **revisão em pares** antes que qualquer card atinja `Done`. Cards documentais marcados como "Done" sem registro explícito de revisão em pares violam o gate de qualidade. Corrige-se esta inconsistência migrando-os para estado de revisão.

### 3.2 Estados de revisão definidos

| Status          | Semântica                                                                                | Aplica-se a                                            | Coluna Kanban equivalente |
| --------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------- |
| `pair-review` | Artefato redigido, aguardando validação de um par (Fabricio ou Edson)                   | Planos, requisitos, matrizes, documentos colaborativos | `Code Review`           |
| `in-review`   | Artefato aprovado pelo CCB, aguardando consolidação/versionamento final no repositório | ADRs, decisões formais, seleções de stack           | `Code Review`           |

### 3.3 Migração aplicada (7 cards)

| Card                             | Status anterior | Status corrigido | Justificativa                                       |
| -------------------------------- | --------------- | ---------------- | --------------------------------------------------- |
| M1-01 Plano de Integração      | ✅ Done         | `pair-review`  | Documento colaborativo — requer validação de par |
| M1-06 Requisitos Funcionais      | ✅ Concluído   | `pair-review`  | Consolidado no TAP — requer validação de par     |
| M1-07 Requisitos Não Funcionais | ✅ Concluído   | `pair-review`  | Consolidado no TAP — requer validação de par     |
| M1-11 Seleção Stack FOSS       | ✅ Concluído   | `in-review`    | Aprovado pelo CCB — aguarda versionamento          |
| M1-15 ADR-001 Stack              | ✅ Concluído   | `in-review`    | Aprovado pelo CCB — aguarda versionamento          |
| M1-16 ADR-002 Kanban             | ✅ Concluído   | `in-review`    | Aprovado pelo CCB — aguarda versionamento          |
| M1-17 ADR-003 Métricas          | ✅ Concluído   | `in-review`    | Aprovado pelo CCB — aguarda versionamento          |

> **Nenhum card do M1 permanece em `Done` até que a revisão em pares seja registrada.** Esta regra alinha o backlog ao DoD e ao Domínio de Entrega (PMBOK 7ª).

---

## PARTE 4 — Cards do M1 Reescritos (Formato Ubíquo)

### Bloco 1 — Governança e Planos de Gerenciamento

---

#### 🗂 Card M1-01 — Plano de Integração

| Campo                            | Conteúdo                                                                                                                                                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N1.2 — Plano de Gerenciamento da Integração`                                                                                                                                                                                                            |
| **Contexto Ubíquo**       | O COGME possui oito planos de área, código-fonte e artefatos de governança que precisam permanecer coerentes entre si. Este card produz o plano que coordena todos os demais, definindo mecanismos de controle de mudanças, SSOT e encerramento de fases. |
| **Descrição da Entrega** | Redigir e versionar o Plano de Gerenciamento da Integração em`/docs/plano-integracao.md`, com 11 seções, checklist de validação e frase de rastreabilidade ao TAP.                                                                                    |
| **Critérios de Aceite**   | ☑ 11 seções numeradas hierarquicamente · ☑ Rastreabilidade 100% ao TAP · <br />☑ Extensão ≤ 5 páginas · <br />☑ EVM declarado LEGADO · <br />☑ CCB = GP Leonardo (membro único)                                                                |
| **Rastreabilidade**        | TAP §1.c + Premissa P1 · Domínio: Abordagem de Desenvolvimento · Processo PMBOK 6ª: 4.2                                                                                                                                                                  |
| **Dependências**          | TAP aprovado · OKB convergente                                                                                                                                                                                                                               |
| **Atribuição**           | Leonardo David Silva Setti · 6h                                                                                                                                                                                                                              |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:integracao` · `must` · **Milestone M1** · **Status: `pair-review`**                                                                                                                                |

---

#### 🗂 Card M1-02 — Plano de Escopo

| Campo                            | Conteúdo                                                                                                                                                                                                                    |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N1.2 — Plano de Gerenciamento do Escopo`                                                                                                                                                                                 |
| **Contexto Ubíquo**       | O escopo do COGME precisa ser coletado, declarado, decomposto e controlado para evitar*scope creep* e garantir que a EAP permaneça coerente com os Objetivos SMART. Este card produz o plano que governa essa evolução. |
| **Descrição da Entrega** | Redigir e versionar o Plano de Gerenciamento do Escopo em`/docs/plano-escopo.md`, com fronteira IN/OUT em tabela, rastreabilidade tabular e princípio YAGNI fundamentado.                                                 |
| **Critérios de Aceite**   | ☑ Seções 2.1 a 2.11 · ☑ Fronteira IN/OUT em Tabela 1 · ☑ Rastreabilidade em Tabela 2 · ☑ YAGNI fundamentado em §2.4.1 · ☑ Premissa P3 presente em §2.11                                                         |
| **Rastreabilidade**        | TAP §3 + §5 + §8 · Domínio: Planejamento + Entrega · Processo PMBOK 6ª: 5.1 a 5.6                                                                                                                                     |
| **Dependências**          | TAP aprovado · EAP aprovada · Plano de Integração (interface §1.7)                                                                                                                                                      |
| **Atribuição**           | Fabricio de Lima Cabral · 6h                                                                                                                                                                                                |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:escopo` · `must` · **Milestone M1** · **Status: `pair-review`**                                                                                                   |

---

#### 🗂 Card M1-03 — Plano de Cronograma

| Campo                            | Conteúdo                                                                                                                                                                                       |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N1.2 — Plano de Gerenciamento do Cronograma`                                                                                                                                                |
| **Contexto Ubíquo**       | O COGME possui prazo letivo inegociável e quatro marcos (M1–M4). Este card produz o plano que governa os marcos, o período de calibração de métricas e declara a inaplicabilidade de EVM. |
| **Descrição da Entrega** | Redigir e versionar o Plano de Gerenciamento do Cronograma em`/docs/plano-cronograma.md`, com marcos M1–M4 rastreáveis ao TAP §6 e período de calibração declarado.                     |
| **Critérios de Aceite**   | ☑ Marcos M1–M4 rastreáveis ao TAP §6 · ☑ Período de calibração (23/09–03/10) declarado · ☑ EVM declarado LEGADO (ADR-003) · ☑ Métricas de fluxo como instrumento de controle     |
| **Rastreabilidade**        | TAP §6 + §3 (Métricas) · Domínio: Medição · Processo PMBOK 6ª: 6.5                                                                                                                     |
| **Dependências**          | TAP aprovado · ADR-003 emitida                                                                                                                                                                 |
| **Atribuição**           | Fabricio de Lima Cabral · 4h                                                                                                                                                                   |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:cronograma` · `must` · **Milestone M1** · **Status: ⏳ até 21/09**                                                                    |

---

#### 🗂 Card M1-04 — Plano de Custos

| Campo                            | Conteúdo                                                                                                                                                                                                       |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N1.2 — Plano de Gerenciamento de Custos`                                                                                                                                                                    |
| **Contexto Ubíquo**       | O COGME opera com orçamento zero (TAP §11), o que torna inaplicáveis as métricas financeiras tradicionais. Este card produz o plano que formaliza essa condição e direciona o foco para entrega de valor. |
| **Descrição da Entrega** | Redigir e versionar o Plano de Gerenciamento de Custos em`/docs/plano-custos.md`, declarando orçamento zero e inaplicabilidade de EVM.                                                                       |
| **Critérios de Aceite**   | ☑ Orçamento zero declarado (TAP §11) · ☑ Inaplicabilidade de EVM fundamentada (AC = 0) · ☑ Rastreabilidade à Premissa P2 (FOSS) · ☑ Foco em valor, não em despesa                                    |
| **Rastreabilidade**        | TAP §11 + §8.4 · Domínio: Planejamento · Processo PMBOK 6ª: 7.1 (inaplicável)                                                                                                                            |
| **Dependências**          | TAP aprovado · ADR-003 emitida                                                                                                                                                                                 |
| **Atribuição**           | Fabricio de Lima Cabral · 3h                                                                                                                                                                                   |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:custos` · `must` · **Milestone M1** · **Status: ⏳ até 21/09**                                                                                        |

---

#### 🗂 Card M1-05 — Plano de Qualidade + 12 PDCAs + Ishikawa

| Campo                            | Conteúdo                                                                                                                                                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N1.3 — Plano da Qualidade + 12 PDCAs + Diagrama Ishikawa 6M`                                                                                                                                                              |
| **Contexto Ubíquo**       | O COGME exige cobertura de testes ≥ 80%, UAT sem defeitos críticos e aplicação de ferramentas da qualidade. Este card produz o plano que operacionaliza esses critérios via 12 ciclos PDCA e diagrama de causa e efeito. |
| **Descrição da Entrega** | Redigir e versionar o Plano da Qualidade em`/docs/plano-qualidade.md`, com 12 ciclos PDCA (um por fase da EAP) e Diagrama de Ishikawa 6M.                                                                                   |
| **Critérios de Aceite**   | ☑ 12 ciclos PDCA consolidados · ☑ Diagrama Ishikawa 6M documentado · ☑ Critérios rastreáveis a REQ-08, REQ-09, REQ-10 · ☑ Meta de coverage ≥ 80% declarada                                                          |
| **Rastreabilidade**        | TAP §3 (Qualidade) + REQ-10 · Domínio: Medição · Processo PMBOK 6ª: 8.1–8.3                                                                                                                                           |
| **Dependências**          | TAP aprovado · EAP aprovada                                                                                                                                                                                                  |
| **Atribuição**           | Edson Luis Silva · 8h                                                                                                                                                                                                        |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:qualidade` · `must` · **Milestone M1** · **Status: ⏳ até 21/09**                                                                                                   |

---

### Bloco 2 — Requisitos e Modelagem

---

#### 🗂 Card M1-06 — Requisitos Funcionais

| Campo                            | Conteúdo                                                                                                                                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Título**                | `N2.1 — Requisitos Funcionais (REQ-01 a REQ-07)`                                                                                                                                                                            |
| **Contexto Ubíquo**       | O MVP do COGME precisa realizar simulação cambial, suportar cinco regimes de contratação, aplicar encargos e emitir invoice em PDF. Este card formaliza esses requisitos funcionais com critérios de aceite mensuráveis. |
| **Descrição da Entrega** | Consolidar REQ-01 a REQ-07 no TAP §5, com critério de aceite quantificável e vínculo à fase N5 da EAP.                                                                                                                    |
| **Critérios de Aceite**   | ☑ REQ-01 a REQ-07 consolidados · ☑ Critério de aceite mensurável em cada REQ · ☑ Rastreabilidade à fase N5 · ☑ Domínio de Entrega associado                                                                         |
| **Rastreabilidade**        | TAP §3 (Produto) + §5 · Domínio: Entrega · Processo PMBOK 6ª: 5.2                                                                                                                                                        |
| **Dependências**          | TAP aprovado                                                                                                                                                                                                                   |
| **Atribuição**           | Fabricio de Lima Cabral · 4h                                                                                                                                                                                                  |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:escopo` · `must` · **Milestone M1** · **Status: `pair-review`**                                                                                                     |

---

#### 🗂 Card M1-07 — Requisitos Não Funcionais

| Campo                            | Conteúdo                                                                                                                                                                                                            |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N2.2 — Requisitos Não Funcionais (REQ-08 a REQ-15)`                                                                                                                                                             |
| **Contexto Ubíquo**       | Além das funcionalidades, o COGME exige qualidade (coverage, UAT), DevOps (CI), base de conhecimento (ADRs, prompts SDD), documentação e conformidade FOSS. Este card formaliza esses requisitos não funcionais. |
| **Descrição da Entrega** | Consolidar REQ-08 a REQ-15 no TAP §5, com critério de aceite quantificável e vínculo às fases N6, N7, N9, N11, N1, N4.                                                                                          |
| **Critérios de Aceite**   | ☑ REQ-08 a REQ-15 consolidados · ☑ Critério de aceite mensurável em cada REQ · ☑ Rastreabilidade às fases correspondentes · ☑ Domínios Medição + Entrega associados                                     |
| **Rastreabilidade**        | TAP §3 (Qualidade, Métricas, Inovação) + §5 · Domínio: Medição + Entrega · Processo PMBOK 6ª: 5.2                                                                                                         |
| **Dependências**          | TAP aprovado                                                                                                                                                                                                         |
| **Atribuição**           | Edson Luis Silva · 4h                                                                                                                                                                                               |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:qualidade` · `must` · **Milestone M1** · **Status: `pair-review`**                                                                                        |

---

#### 🗂 Card M1-08 — Arquitetura da Solução

| Campo                            | Conteúdo                                                                                                                                                                                                                 |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N3.1 — Arquitetura da Solução (Diagrama de Componentes)`                                                                                                                                                            |
| **Contexto Ubíquo**       | Antes de desenvolver, o COGME precisa de uma visão arquitetural que conecte backend, frontend, banco e geração de PDF. Este card produz o diagrama de componentes, respeitando a decisão de não adotar UML completo. |
| **Descrição da Entrega** | Produzir diagrama de componentes em PlantUML ou Markdown, versionado no repositório, vinculado às decisões da ADR-001.                                                                                                 |
| **Critérios de Aceite**   | ☑ Diagrama versionado no repositório · ☑ Decisões vinculadas à ADR-001 · ☑ Sem UML completo (Plano de Escopo §2.4.3.a) · ☑ Componentes mínimos: backend, frontend, banco, PDF                                 |
| **Rastreabilidade**        | TAP §3 (Inovação) + ADR-001 · Domínio: Abordagem de Desenvolvimento · EAP: N3.1                                                                                                                                     |
| **Dependências**          | ADR-001 aprovada · Stack FOSS validada                                                                                                                                                                                   |
| **Atribuição**           | Leonardo David Silva Setti · 6h                                                                                                                                                                                          |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:escopo` · `must` · `sdd-ia` · **Milestone M2** · **Status: ⏳ até 30/09**                                                                                    |

> **Nota:** Tag `sdd-ia` aplicada — o diagrama pode ser gerado com apoio de IA; o commit deve declarar co-autoria (TAP §3.2.e).

---

#### 🗂 Card M1-09 — Protótipo UX/UI

| Campo                            | Conteúdo                                                                                                                                                                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N3.2 — Protótipo UX/UI (Interface Web)`                                                                                                                                                                                |
| **Contexto Ubíquo**       | O usuário final precisa de uma interface web responsiva e compatível com navegadores modernos. Este card produz o protótipo que orienta o desenvolvimento do frontend, garantindo usabilidade centrada no público-alvo. |
| **Descrição da Entrega** | Produzir wireframe ou protótipo navegável em ferramenta gratuita (Figma Free ou HTML estático), versionado no repositório.                                                                                              |
| **Critérios de Aceite**   | ☑ Protótipo versionado no repositório · ☑ Compatibilidade com Chrome/Firefox/Edge (REQ-06) · ☑ Ferramenta gratuita (restrição FOSS) · ☑ Fluxos críticos representados                                           |
| **Rastreabilidade**        | TAP §3 (Produto) + REQ-06 · Domínio: Entrega · EAP: N3.2                                                                                                                                                                |
| **Dependências**          | Requisitos funcionais aprovados                                                                                                                                                                                             |
| **Atribuição**           | Edson Luis Silva · 8h                                                                                                                                                                                                      |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:escopo` · `should` · **Milestone M2** · **Status: ⏳ até 30/09**                                                                                                  |

---

#### 🗂 Card M1-10 — Modelagem de Dados (DER)

| Campo                            | Conteúdo                                                                                                                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Título**                | `N3.3 — Modelagem de Dados (DER)`                                                                                                                                                                   |
| **Contexto Ubíquo**       | O COGME persiste cotações, simulações, regimes e invoices em SQLite. Este card produz o Diagrama Entidade-Relacionamento que estrutura esses dados, aderente à decisão de usar SQLite (ADR-001). |
| **Descrição da Entrega** | Produzir DER versionado no repositório, com entidades mínimas: Cotação, Simulação, Regime, Invoice.                                                                                              |
| **Critérios de Aceite**   | ☑ DER versionado no repositório · ☑ Entidades mínimas presentes · ☑ Aderência ao SQLite (ADR-001) · ☑ Cardinalidades definidas                                                               |
| **Rastreabilidade**        | TAP §3 (Produto) + ADR-001 · Domínio: Planejamento · EAP: N3.3                                                                                                                                     |
| **Dependências**          | ADR-001 aprovada · SQLite validado                                                                                                                                                                    |
| **Atribuição**           | Fabricio de Lima Cabral · 6h                                                                                                                                                                          |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:escopo` · `must` · **Milestone M2** · **Status: ⏳ até 30/09**                                                                               |

> **Nota:** O DER é artefato da fase N3.3, não do Plano de Escopo (Plano de Escopo §2.4.3.b).

---

### Bloco 3 — Configuração de Ambiente

---

#### 🗂 Card M1-11 — Seleção e Validação da Stack FOSS

| Campo                            | Conteúdo                                                                                                                                                                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N4.1 — Seleção e Validação da Stack FOSS (ADR-001)`                                                                                                                                                                       |
| **Contexto Ubíquo**       | A restrição FOSS (TAP §8) exige que toda a stack seja de código aberto. Este card formaliza a seleção da stack e sua validação prática por meio de protótipo, garantindo viabilidade técnica antes do desenvolvimento. |
| **Descrição da Entrega** | Emitir ADR-001 com a stack selecionada e validar via protótipo "Hello World" integrando FastAPI + SQLite + WeasyPrint.                                                                                                           |
| **Critérios de Aceite**   | ☑ ADR-001 emitida e aprovada · ☑ Protótipo "Hello World" funcional · ☑ 100% das licenças OSI-approved · ☑ Fallback documentado                                                                                           |
| **Rastreabilidade**        | TAP §3 (Inovação) + §8 (FOSS) + REQ-15 · Domínio: Abordagem de Desenvolvimento · EAP: N4.1                                                                                                                                 |
| **Dependências**          | TAP aprovado                                                                                                                                                                                                                      |
| **Atribuição**           | Leonardo David Silva Setti · 4h                                                                                                                                                                                                  |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:recursos` · `must` · **Milestone M1** · **Status: `in-review`**                                                                                                        |

---

#### 🗂 Card M1-12 — Repositório Git + CI/CD

| Campo                            | Conteúdo                                                                                                                                                                              |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N4.2 — Repositório Git + Configuração CI/CD`                                                                                                                                    |
| **Contexto Ubíquo**       | O GitHub é o SSOT do COGME (ADR-002). Este card configura o repositório com branch protegida, pipeline CI e GitHub Projects, criando a infraestrutura de execução do fluxo Kanban. |
| **Descrição da Entrega** | Criar repositório GitHub com branch`main` protegida, pipeline CI (lint + testes), Conventional Commits e GitHub Projects com 5 colunas.                                             |
| **Critérios de Aceite**   | ☑ Repositório criado · ☑ Branch`main` protegida · ☑ Pipeline CI configurado · ☑ Conventional Commits habilitado · ☑ GitHub Projects com 5 colunas (ADR-002)                |
| **Rastreabilidade**        | TAP §3 (Métricas) + REQ-11 · Domínio: Trabalho do Projeto · EAP: N4.2                                                                                                             |
| **Dependências**          | Stack FOSS validada (ADR-001)                                                                                                                                                          |
| **Atribuição**           | Leonardo David Silva Setti · 6h                                                                                                                                                       |
| **Estado**                 | `ci` · `MF1-fundacao` · `area:integracao` · `must` · **Milestone M1** · **Status: ⏳ até 22/09**                                                             |

---

#### 🗂 Card M1-13 — Setup Local e Homologação

| Campo                            | Conteúdo                                                                                                                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Título**                | `N4.3 — Setup Local e Ambiente de Homologação`                                                                                                                                                                |
| **Contexto Ubíquo**       | O COGME será desenvolvido e validado localmente (sem cloud paga). Este card configura o ambiente de desenvolvimento nas máquinas da equipe, garantindo compatibilidade com o hardware disponível (Premissa P6). |
| **Descrição da Entrega** | Configurar ambiente local (Arch Linux) com Docker funcional e documentar instruções de setup no`README.md`.                                                                                                    |
| **Critérios de Aceite**   | ☑ Ambiente configurado em todas as máquinas · ☑ Docker funcional · ☑`README.md` com instruções de setup · ☑ Compatibilidade com hardware local (P6)                                                    |
| **Rastreabilidade**        | TAP §9 (P6) + ADR-001 · Domínio: Trabalho do Projeto · EAP: N4.3                                                                                                                                               |
| **Dependências**          | Stack FOSS validada (ADR-001)                                                                                                                                                                                      |
| **Atribuição**           | Fabricio de Lima Cabral · 4h                                                                                                                                                                                      |
| **Estado**                 | `chore` · `MF1-fundacao` · `area:recursos` · `must` · **Milestone M1** · **Status: ⏳ até 22/09**                                                                                        |

---

#### 🗂 Card M1-14 — Auditoria de Licenças FOSS

| Campo                            | Conteúdo                                                                                                                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N4.4 — Auditoria de Licenças FOSS`                                                                                                                                    |
| **Contexto Ubíquo**       | O Critério de Conformidade FOSS (TAP §3.2.b) exige que 100% das dependências tenham licenças OSI-approved. Este card audita e documenta todas as licenças do projeto. |
| **Descrição da Entrega** | Auditar licenças de todas as dependências e documentar em`LICENSE.md` + `DEPENDENCIES.md` no repositório.                                                           |
| **Critérios de Aceite**   | ☑ Lista completa de dependências documentada · ☑ 100% OSI-approved · ☑`LICENSE.md` presente · ☑ `DEPENDENCIES.md` presente                                     |
| **Rastreabilidade**        | TAP §3 (Inovação) + REQ-15 + §8 (FOSS) · Domínio: Entrega · EAP: N4.4                                                                                               |
| **Dependências**          | Stack FOSS validada (ADR-001)                                                                                                                                              |
| **Atribuição**           | Edson Luis Silva · 3h                                                                                                                                                     |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:qualidade` · `must` · **Milestone M2** · **Status: ⏳ até 30/09**                                                |

---

### Bloco 4 — Base de Conhecimento

---

#### 🗂 Card M1-15 — ADR-001: Stack Tecnológica

| Campo                            | Conteúdo                                                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N9.1 — ADR-001: Stack Tecnológica FOSS`                                                                                                                        |
| **Contexto Ubíquo**       | Decisões arquiteturais críticas do COGME devem ser formalmente registradas (REQ-12). Este card produz a ADR que documenta a seleção da stack tecnológica FOSS. |
| **Descrição da Entrega** | Emitir ADR-001 com Contexto, Decisão, Consequências, Fallback e Trade-offs, aprovada pelo CCB.                                                                    |
| **Critérios de Aceite**   | ☑ ADR com estrutura completa · ☑ Aprovada pelo CCB (GP) · ☑ Trade-offs declarados · ☑ Fallback documentado                                                   |
| **Rastreabilidade**        | TAP §3 (Inovação) + REQ-12 · Domínio: Trabalho do Projeto · EAP: N9.1                                                                                         |
| **Dependências**          | Nenhuma                                                                                                                                                             |
| **Atribuição**           | Leonardo David Silva Setti · 2h                                                                                                                                    |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:integracao` · `must` · **Milestone M1** · **Status: `in-review`**                                        |

---

#### 🗂 Card M1-16 — ADR-002: Kanban como Método

| Campo                            | Conteúdo                                                                                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Título**                | `N9.1 — ADR-002: Kanban como Método de Execução`                                                                                                                                     |
| **Contexto Ubíquo**       | O TAP declara Kanban como método de execução. Este card produz a ADR que operacionaliza o método, definindo colunas, WIP limits, rituais e o mapeamento Domínios PMBOK 7ª → Kanban. |
| **Descrição da Entrega** | Emitir ADR-002 com colunas Kanban, WIP limits, rituais e mapeamento de domínios, aprovada pelo CCB.                                                                                       |
| **Critérios de Aceite**   | ☑ Colunas Kanban definidas (Backlog → Ready → In Progress → Code Review → Done) · ☑ WIP limits declarados · ☑ Rituais definidos · ☑ Mapeamento Domínios → Kanban presente     |
| **Rastreabilidade**        | TAP §1.c + §3 (Métricas) + REQ-12 · Domínio: Abordagem de Desenvolvimento · EAP: N9.1                                                                                                |
| **Dependências**          | Nenhuma                                                                                                                                                                                    |
| **Atribuição**           | Leonardo David Silva Setti · 2h                                                                                                                                                           |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:integracao` · `must` · **Milestone M1** · **Status: `in-review`**                                                               |

---

#### 🗂 Card M1-17 — ADR-003: Métricas de Fluxo

| Campo                            | Conteúdo                                                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N9.1 — ADR-003: Métricas de Fluxo (Substituição de EVM)`                                                                                               |
| **Contexto Ubíquo**       | O orçamento zero torna EVM inaplicável. Este card produz a ADR que declara SPI/CPI/EVM como LEGADO e estabelece as métricas de fluxo Kanban como oficiais. |
| **Descrição da Entrega** | Emitir ADR-003 declarando EVM como LEGADO e definindo métricas Kanban oficiais (Cycle Time, Throughput, CFD, WIP, Coverage).                                 |
| **Critérios de Aceite**   | ☑ SPI/CPI/EVM declarados LEGADO · ☑ Métricas Kanban oficiais definidas · ☑ Período de calibração definido · ☑ Fallback documentado                 |
| **Rastreabilidade**        | TAP §3 (Métricas) + REQ-12 · Domínio: Medição · EAP: N9.1                                                                                              |
| **Dependências**          | ADR-002 aprovada                                                                                                                                              |
| **Atribuição**           | Leonardo David Silva Setti · 2h                                                                                                                              |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:cronograma` · `must` · **Milestone M1** · **Status: `in-review`**                                  |

---

#### 🗂 Card M1-18 — Lições Aprendidas Contínuas (MF1)

| Campo                            | Conteúdo                                                                                                                                                   |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N9.2 — Lições Aprendidas Contínuas (Encerramento MF1)`                                                                                               |
| **Contexto Ubíquo**       | A melhoria contínua é um princípio PMBOK 7ª. Este card registra as lições aprendidas do encerramento da Macro-Fase 1, alimentando decisões futuras.  |
| **Descrição da Entrega** | Registrar lições aprendidas do período 01/09–30/09/2026 em`/docs/licoes-aprendidas/`, com mínimo de 3 lições.                                      |
| **Critérios de Aceite**   | ☑ Mínimo 3 lições documentadas · ☑ Versionado em`/docs/licoes-aprendidas/` · ☑ Período 01/09–30/09 coberto · ☑ Ações de melhoria associadas |
| **Rastreabilidade**        | EAP N9.2 · Domínio: Entrega · Processo PMBOK 6ª: 4.4                                                                                                    |
| **Dependências**          | Encerramento MF1 (30/09/2026)                                                                                                                               |
| **Atribuição**           | Leonardo David Silva Setti · 2h                                                                                                                            |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:integracao` · `should` · **Milestone M2** · **Status: ⏳ até 30/09**                              |

---

### Bloco 5 — Comunicação

---

#### 🗂 Card M1-19 — Matriz de Comunicação (RACI)

| Campo                            | Conteúdo                                                                                                                                                                                          |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N8.1 — Matriz de Comunicação (RACI Simplificado)`                                                                                                                                            |
| **Contexto Ubíquo**       | A equipe de 3 membros acumula múltiplos papéis. Este card produz a matriz RACI que define responsabilidades de comunicação, alinhada aos papéis de governança do Plano de Integração.      |
| **Descrição da Entrega** | Produzir matriz RACI simplificada (3 membros + stakeholder-avaliador), versionada no repositório.                                                                                                 |
| **Critérios de Aceite**   | ☑ Matriz RACI com 3 membros + Prof. Dr. Nivaldo Carleto · ☑ Papéis alinhados ao Plano de Integração §1.2.2 · ☑ Comunicação de mudanças conforme §1.7 · ☑ Versionada no repositório |
| **Rastreabilidade**        | TAP §6 + Premissa P7 · Domínio: Stakeholders · EAP: N8.1                                                                                                                                       |
| **Dependências**          | Plano de Integração aprovado                                                                                                                                                                     |
| **Atribuição**           | Edson Luis Silva · 3h                                                                                                                                                                             |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:comunicacoes` · `should` · **Milestone M1** · **Status: ⏳ até 22/09**                                                                   |

---

#### 🗂 Card M1-20 — Canais Oficiais de Comunicação

| Campo                            | Conteúdo                                                                                                                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Título**                | `N8.2 — Canais Oficiais (GitHub Issues + E-mail)`                                                                                                                                                   |
| **Contexto Ubíquo**       | O COGME utiliza comunicação assíncrona e um stakeholder-avaliador externo. Este card declara os canais oficiais de comunicação, garantindo rastreabilidade e formalidade.                         |
| **Descrição da Entrega** | Declarar canais oficiais (GitHub Issues, GitHub Projects, e-mail) e registrá-los no Plano de Comunicações.                                                                                          |
| **Critérios de Aceite**   | ☑ GitHub Issues (Daily assíncrona) declarado · ☑ GitHub Projects (SSOT) declarado · ☑ E-mail (comunicação com Prof. Dr. Nivaldo Carleto) declarado · ☑ Registrado no Plano de Comunicações |
| **Rastreabilidade**        | TAP §6 + ADR-002 · Domínio: Stakeholders · EAP: N8.2                                                                                                                                               |
| **Dependências**          | Repositório GitHub configurado                                                                                                                                                                        |
| **Atribuição**           | Leonardo David Silva Setti · 2h                                                                                                                                                                       |
| **Estado**                 | `docs` · `MF1-fundacao` · `area:comunicacoes` · `should` · **Milestone M1** · **Status: ⏳ até 22/09**                                                                       |

---

### Bloco 6 — Gestão de Mudanças

---

#### 🗂 Card M1-21 — Configuração de Labels e Fluxo de Mudanças

| Campo                            | Conteúdo                                                                                                                                                                                       |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Título**                | `N10.2 — Configuração de Labels e Fluxo change-request no GitHub`                                                                                                                          |
| **Contexto Ubíquo**       | O controle de mudanças (Plano de Integração §1.7) opera via labels no GitHub. Este card configura o sistema de 23 tags e o fluxo`change-request`, habilitando a governança de mudanças. |
| **Descrição da Entrega** | Criar 23 tags no repositório GitHub (5 categorias) e configurar o fluxo`change-request` conforme Plano de Integração §1.7.2.                                                              |
| **Critérios de Aceite**   | ☑ 23 tags criadas (5 categorias) · ☑ Label`change-request` funcional · ☑ Fluxo de 4 etapas operacional · ☑ Cores aplicadas conforme padrão definido                                   |
| **Rastreabilidade**        | TAP §3.3 (Fracasso) + Plano de Integração §1.7 · Domínio: Incerteza · EAP: N10.2                                                                                                         |
| **Dependências**          | Repositório GitHub configurado                                                                                                                                                                 |
| **Atribuição**           | Leonardo David Silva Setti · 2h                                                                                                                                                                |
| **Estado**                 | `chore` · `MF1-fundacao` · `area:integracao` · `must` · **Milestone M1** · **Status: ⏳ até 22/09**                                                                   |

---

## PARTE 5 — Resumo Consolidado e Verificação

### 5.1 Tabela consolidada (com status corrigido)

| #     | Card                               | Tipo      | Macro-Fase       | Área                 | Prioridade | Milestone | Status            |
| ----- | ---------------------------------- | --------- | ---------------- | --------------------- | ---------- | --------- | ----------------- |
| M1-01 | Plano de Integração              | `docs`  | `MF1-fundacao` | `area:integracao`   | `must`   | M1        | 🔄`pair-review` |
| M1-02 | Plano de Escopo                    | `docs`  | `MF1-fundacao` | `area:escopo`       | `must`   | M1        | 🔄`pair-review` |
| M1-03 | Plano de Cronograma                | `docs`  | `MF1-fundacao` | `area:cronograma`   | `must`   | M1        | ⏳ 21/09          |
| M1-04 | Plano de Custos                    | `docs`  | `MF1-fundacao` | `area:custos`       | `must`   | M1        | ⏳ 21/09          |
| M1-05 | Plano Qualidade + PDCAs + Ishikawa | `docs`  | `MF1-fundacao` | `area:qualidade`    | `must`   | M1        | ⏳ 21/09          |
| M1-06 | Requisitos Funcionais              | `docs`  | `MF1-fundacao` | `area:escopo`       | `must`   | M1        | 🔄`pair-review` |
| M1-07 | Requisitos Não Funcionais         | `docs`  | `MF1-fundacao` | `area:qualidade`    | `must`   | M1        | 🔄`pair-review` |
| M1-08 | Arquitetura da Solução           | `docs`  | `MF1-fundacao` | `area:escopo`       | `must`   | M2        | ⏳ 30/09          |
| M1-09 | Protótipo UX/UI                   | `docs`  | `MF1-fundacao` | `area:escopo`       | `should` | M2        | ⏳ 30/09          |
| M1-10 | Modelagem de Dados (DER)           | `docs`  | `MF1-fundacao` | `area:escopo`       | `must`   | M2        | ⏳ 30/09          |
| M1-11 | Seleção Stack FOSS (ADR-001)     | `docs`  | `MF1-fundacao` | `area:recursos`     | `must`   | M1        | 🔄`in-review`   |
| M1-12 | Repositório Git + CI/CD           | `ci`    | `MF1-fundacao` | `area:integracao`   | `must`   | M1        | ⏳ 22/09          |
| M1-13 | Setup Local                        | `chore` | `MF1-fundacao` | `area:recursos`     | `must`   | M1        | ⏳ 22/09          |
| M1-14 | Auditoria de Licenças             | `docs`  | `MF1-fundacao` | `area:qualidade`    | `must`   | M2        | ⏳ 30/09          |
| M1-15 | ADR-001 Stack                      | `docs`  | `MF1-fundacao` | `area:integracao`   | `must`   | M1        | 🔄`in-review`   |
| M1-16 | ADR-002 Kanban                     | `docs`  | `MF1-fundacao` | `area:integracao`   | `must`   | M1        | 🔄`in-review`   |
| M1-17 | ADR-003 Métricas                  | `docs`  | `MF1-fundacao` | `area:cronograma`   | `must`   | M1        | 🔄`in-review`   |
| M1-18 | Lições Aprendidas MF1            | `docs`  | `MF1-fundacao` | `area:integracao`   | `should` | M2        | ⏳ 30/09          |
| M1-19 | Matriz RACI                        | `docs`  | `MF1-fundacao` | `area:comunicacoes` | `should` | M1        | ⏳ 22/09          |
| M1-20 | Canais Oficiais                    | `docs`  | `MF1-fundacao` | `area:comunicacoes` | `should` | M1        | ⏳ 22/09          |
| M1-21 | Labels + change-request            | `chore` | `MF1-fundacao` | `area:integracao`   | `must`   | M1        | ⏳ 22/09          |

**Total:** 21 cards · 15 `must` · 6 `should` · 7 migrados de Done para revisão (4 `pair-review` + 3 `in-review`... correção: 4 pair-review [M1-01, M1-02, M1-06, M1-07] + 4 in-review [M1-11, M1-15, M1-16, M1-17] = 8 migrados).

> **Correção de contagem:** 8 cards migrados — 4 para `pair-review` (M1-01, M1-02, M1-06, M1-07) e 4 para `in-review` (M1-11, M1-15, M1-16, M1-17).

---

### 5.2 Checklist de verificação

| Item                                                     | Status           |
| -------------------------------------------------------- | ---------------- |
| Padrão de redação documental (Padrão A) definido     | ✅ OK            |
| Padrão de redação User Story GWT (Padrão B) definido | ✅ OK            |
| Princípio do card ubíquo formalizado (3 propriedades)  | ✅ OK            |
| Todos os cards "Done" migrados para revisão             | ✅ OK — 8 cards |
| Nenhum card em`Done` sem registro de revisão em pares | ✅ OK            |
| Distinção`pair-review` vs `in-review` aplicada     | ✅ OK            |
| Todo card possui ≥ 3 tags (tipo + macro-fase + área)   | ✅ OK — 21/21   |
| Todo card possui milestone associada                     | ✅ OK — 21/21   |
| Todo card possui contexto ubíquo autocontido            | ✅ OK — 21/21   |
| Todo card possui critério de aceite mensurável         | ✅ OK — 21/21   |
| Prof. Dr. Nivaldo Carleto sempre por extenso             | ✅ OK            |
| Formatado em Markdown para GitHub                        | ✅ OK            |

---

**Status:** Padrão de redação definido + cards do M1 reescritos em formato ubíquo, com migração de status aplicada. Pronto para criação no GitHub Projects e validação no Refinement de 23/09/2026.

**Próximo passo recomendado:** Submeter esta estrutura à revisão dos pares (Fabricio + Edson) antes da criação efetiva dos cards no GitHub, garantindo que o Padrão B (User Story GWT) seja validado antes do marco M2.

---

# Sistema de Prioridade P0–P3 — Cards do Marco M1

## PARTE A — Definição da Escala de Prioridade

A escala abaixo é **complementar** ao MoSCoW (que classifica **valor de escopo**) e foca em **urgência temporal e criticidade de bloqueio** para o marco M1 (22/09/2026).

| Peso         | Definição                           | Critério objetivo                                                                    | Ação no Kanban                                       |
| ------------ | ------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **P0** | **Crítico / Caminho crítico** | Sem este card, o marco M1 não é atingido**ou** ele bloqueia ≥ 2 outros cards | Execução imediata; WIP reservado; Daily obrigatória |
| **P1** | **Alto**                        | Essencial para o marco, mas não bloqueia outros cards diretamente                    | Execução na janela M1 (até 22/09)                   |
| **P2** | **Médio**                      | Importante, mas pode deslizar para M2 (30/09) sem comprometer o aceite de M1          | Execução pós-M1, antes do M2                        |
| **P3** | **Baixo**                       | Desejável; postergável sem impacto formal no marco                                  | Backlog priorizado; puxar apenas se capacidade sobrar  |

**Regra de desempate:** Se dois cards têm o mesmo peso, prioriza-se aquele que **desbloqueia mais cards subsequentes** (análise de dependências).

**Trade-off declarado:** Um card `must` (MoSCoW) pode ser P2 se sua entrega puder deslizar para M2 sem violar o critério de aceite do M1. Exemplo: M1-08 (Arquitetura) é `must` mas P2, pois o critério de aceite do M1 não exige arquitetura — apenas documentação até o Plano de Qualidade.

---

## PARTE B — Atribuição de Prioridade por Card (21 cards)

### B.1 — P0: Caminho Crítico do M1 (6 cards)

| #               | Card                               | MoSCoW   | Status          | Justificativa P0                                                                                                              |
| --------------- | ---------------------------------- | -------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **M1-01** | Plano de Integração              | `must` | `pair-review` | Fundamento normativo dos outros 7 planos; sem ele, nenhuma rastreabilidade cruzada é validável                              |
| **M1-02** | Plano de Escopo                    | `must` | `pair-review` | Exigido explicitamente no critério de aceite do M1 (TAP §6)                                                                 |
| **M1-03** | Plano de Cronograma                | `must` | ⏳ 21/09        | Exigido explicitamente no critério de aceite do M1 (TAP §6)                                                                 |
| **M1-04** | Plano de Custos                    | `must` | ⏳ 21/09        | Exigido explicitamente no critério de aceite do M1 (TAP §6)                                                                 |
| **M1-05** | Plano Qualidade + PDCAs + Ishikawa | `must` | ⏳ 21/09        | Exigido explicitamente no M1 (TAP §6: "até o Plano de Gerenciamento da Qualidade") + maior esforço (8h)                    |
| **M1-12** | Repositório Git + CI/CD           | `must` | ⏳ 22/09        | **Bloqueante transversal**: sem repositório, nenhum outro card pode ser versionado nem o SSOT (ADR-002) é operacional |

### B.2 — P1: Alto (8 cards)

| #               | Card                              | MoSCoW   | Status          | Justificativa P1                                                                                           |
| --------------- | --------------------------------- | -------- | --------------- | ---------------------------------------------------------------------------------------------------------- |
| **M1-06** | Requisitos Funcionais             | `must` | `pair-review` | Já consolidado no TAP; falta apenas validação formal de par                                             |
| **M1-07** | Requisitos Não Funcionais        | `must` | `pair-review` | Já consolidado no TAP; falta apenas validação formal de par                                             |
| **M1-11** | Seleção Stack FOSS (protótipo) | `must` | `in-review`   | ADR-001 já aprovada; falta validar protótipo "Hello World"                                               |
| **M1-13** | Setup Local e Homologação       | `must` | ⏳ 22/09        | Pré-requisito para qualquer desenvolvimento; desbloqueia M1-11                                            |
| **M1-15** | ADR-001 Stack                     | `must` | `in-review`   | Aprovada pelo CCB; falta versionamento final no repositório                                               |
| **M1-16** | ADR-002 Kanban                    | `must` | `in-review`   | Aprovada pelo CCB; falta versionamento final no repositório                                               |
| **M1-17** | ADR-003 Métricas                 | `must` | `in-review`   | Aprovada pelo CCB; falta versionamento final no repositório                                               |
| **M1-21** | Labels + fluxo change-request     | `must` | ⏳ 22/09        | Habilita a governança de mudanças (Plano de Integração §1.7); bloqueia qualquer change-request futuro |

### B.3 — P2: Médio (5 cards)

| #               | Card                        | MoSCoW     | Status        | Justificativa P2                                                                              |
| --------------- | --------------------------- | ---------- | ------------- | --------------------------------------------------------------------------------------------- |
| **M1-08** | Arquitetura da Solução    | `must`   | ⏳ 30/09 (M2) | `must` para o MVP, mas não é critério de aceite do M1; pode deslizar para M2             |
| **M1-10** | Modelagem de Dados (DER)    | `must`   | ⏳ 30/09 (M2) | `must` para o MVP, mas não é critério de aceite do M1; pode deslizar para M2             |
| **M1-14** | Auditoria de Licenças FOSS | `must`   | ⏳ 30/09 (M2) | `must` para conformidade FOSS, mas pode ser concluída no M2                                |
| **M1-19** | Matriz RACI                 | `should` | ⏳ 22/09      | `should`; útil mas não bloqueante; papéis já definidos no Plano de Integração §1.2.2 |
| **M1-20** | Canais Oficiais             | `should` | ⏳ 22/09      | `should`; canais já operacionais informalmente (GitHub Issues + e-mail)                    |

### B.4 — P3: Baixo (2 cards)

| #               | Card                    | MoSCoW     | Status        | Justificativa P3                                                               |
| --------------- | ----------------------- | ---------- | ------------- | ------------------------------------------------------------------------------ |
| **M1-09** | Protótipo UX/UI        | `should` | ⏳ 30/09 (M2) | `should`; não bloqueia backend; pode ser substituído por wireframe simples |
| **M1-18** | Lições Aprendidas MF1 | `should` | ⏳ 30/09      | `should`; só faz sentido após encerramento formal de MF1 (30/09)           |

---

## PARTE C — Tabela Consolidada (ordem de execução recomendada)

| Ordem | #     | Card                               | Peso         | MoSCoW     | Macro-Fase | Área                 | Milestone | Status            | Responsável |
| ----- | ----- | ---------------------------------- | ------------ | ---------- | ---------- | --------------------- | --------- | ----------------- | ------------ |
| 1     | M1-12 | Repositório Git + CI/CD           | **P0** | `must`   | MF1        | `area:integracao`   | M1        | ⏳ 22/09          | Leonardo     |
| 2     | M1-01 | Plano de Integração              | **P0** | `must`   | MF1        | `area:integracao`   | M1        | 🔄`pair-review` | Leonardo     |
| 3     | M1-02 | Plano de Escopo                    | **P0** | `must`   | MF1        | `area:escopo`       | M1        | 🔄`pair-review` | Fabricio     |
| 4     | M1-03 | Plano de Cronograma                | **P0** | `must`   | MF1        | `area:cronograma`   | M1        | ⏳ 21/09          | Fabricio     |
| 5     | M1-04 | Plano de Custos                    | **P0** | `must`   | MF1        | `area:custos`       | M1        | ⏳ 21/09          | Fabricio     |
| 6     | M1-05 | Plano Qualidade + PDCAs + Ishikawa | **P0** | `must`   | MF1        | `area:qualidade`    | M1        | ⏳ 21/09          | Edson        |
| 7     | M1-21 | Labels + change-request            | **P1** | `must`   | MF1        | `area:integracao`   | M1        | ⏳ 22/09          | Leonardo     |
| 8     | M1-15 | ADR-001 Stack                      | **P1** | `must`   | MF1        | `area:integracao`   | M1        | 🔄`in-review`   | Leonardo     |
| 9     | M1-16 | ADR-002 Kanban                     | **P1** | `must`   | MF1        | `area:integracao`   | M1        | 🔄`in-review`   | Leonardo     |
| 10    | M1-17 | ADR-003 Métricas                  | **P1** | `must`   | MF1        | `area:cronograma`   | M1        | 🔄`in-review`   | Leonardo     |
| 11    | M1-13 | Setup Local e Homologação        | **P1** | `must`   | MF1        | `area:recursos`     | M1        | ⏳ 22/09          | Fabricio     |
| 12    | M1-11 | Seleção Stack FOSS (protótipo)  | **P1** | `must`   | MF1        | `area:recursos`     | M1        | 🔄`in-review`   | Leonardo     |
| 13    | M1-06 | Requisitos Funcionais              | **P1** | `must`   | MF1        | `area:escopo`       | M1        | 🔄`pair-review` | Fabricio     |
| 14    | M1-07 | Requisitos Não Funcionais         | **P1** | `must`   | MF1        | `area:qualidade`    | M1        | 🔄`pair-review` | Edson        |
| 15    | M1-19 | Matriz RACI                        | **P2** | `should` | MF1        | `area:comunicacoes` | M1        | ⏳ 22/09          | Edson        |
| 16    | M1-20 | Canais Oficiais                    | **P2** | `should` | MF1        | `area:comunicacoes` | M1        | ⏳ 22/09          | Leonardo     |
| 17    | M1-08 | Arquitetura da Solução           | **P2** | `must`   | MF1        | `area:escopo`       | M2        | ⏳ 30/09          | Leonardo     |
| 18    | M1-10 | Modelagem de Dados (DER)           | **P2** | `must`   | MF1        | `area:escopo`       | M2        | ⏳ 30/09          | Fabricio     |
| 19    | M1-14 | Auditoria de Licenças FOSS        | **P2** | `must`   | MF1        | `area:qualidade`    | M2        | ⏳ 30/09          | Edson        |
| 20    | M1-09 | Protótipo UX/UI                   | **P3** | `should` | MF1        | `area:escopo`       | M2        | ⏳ 30/09          | Edson        |
| 21    | M1-18 | Lições Aprendidas MF1            | **P3** | `should` | MF1        | `area:integracao`   | M2        | ⏳ 30/09          | Leonardo     |

**Distribuição:** 6 P0 · 8 P1 · 5 P2 · 2 P3 = 21 cards ✓

---

## PARTE D — Sequência de Execução para os Próximos 3 Dias (20–22/09)

Considerando o WIP limit de 3 cards/pessoa (ADR-002) e a restrição de 20h/semana por membro (Premissa P5), a distribuição recomendada é:

### Dia 1 — 20/09 (sábado)

| Membro             | Card 1                                           | Card 2                              | Card 3                             |
| ------------------ | ------------------------------------------------ | ----------------------------------- | ---------------------------------- |
| **Leonardo** | M1-12 (P0) Repositório Git + CI/CD              | M1-01 (P0) pair-review Integração | M1-21 (P1) Labels + change-request |
| **Fabricio** | M1-02 (P0) pair-review Escopo                    | M1-03 (P0) Plano de Cronograma      | M1-04 (P0) Plano de Custos         |
| **Edson**    | M1-05 (P0) Plano de Qualidade + PDCAs + Ishikawa | M1-07 (P1) pair-review RNF          | —                                 |

### Dia 2 — 21/09 (domingo)

| Membro             | Card 1                                   | Card 2                           | Card 3                           |
| ------------------ | ---------------------------------------- | -------------------------------- | -------------------------------- |
| **Leonardo** | M1-15 (P1) ADR-001 versionamento         | M1-16 (P1) ADR-002 versionamento | M1-17 (P1) ADR-003 versionamento |
| **Fabricio** | M1-13 (P1) Setup Local                   | M1-06 (P1) pair-review RF        | —                               |
| **Edson**    | M1-05 (P0) conclusão Plano de Qualidade | M1-19 (P2) Matriz RACI           | —                               |

### Dia 3 — 22/09 (segunda-feira) — Dia do Marco M1

| Membro             | Card 1                                        | Card 2                                 |
| ------------------ | --------------------------------------------- | -------------------------------------- |
| **Leonardo** | M1-11 (P1) validação protótipo Hello World | M1-20 (P2) Canais Oficiais             |
| **Fabricio** | Fechamento de issues P0/P1 abertas            | Verificação final do checklist M1    |
| **Edson**    | Fechamento de issues P0/P1 abertas            | Consolidação do pacote de entrega M1 |

**Checkpoint crítico (22/09, 18h):** Verificação de que **todos os cards P0 e P1 estão em `Done` ou `pair-review`/`in-review` registrado**. Qualquer P0 aberto após este horário aciona Plano de Integração §1.9 (Issue `change-request` + replanejamento + ADR).

---

## PARTE E — Regras de Aplicação no GitHub

1. **Label de prioridade:** criar as labels `P0`, `P1`, `P2`, `P3` no repositório (extensão do sistema de 23 tags para **27 tags**).
   - Cores sugeridas: `P0` = `#B60205` (vermelho escuro), `P1` = `#D93F0B` (laranja), `P2` = `#FBCA04` (amarelo), `P3` = `#0E8A16` (verde).
2. **Ordenação no GitHub Projects:** dentro da coluna `Ready`, cards são ordenados por prioridade (P0 no topo). O pull system respeita essa ordem.
3. **Regra de bloqueio:** Um card P0 com label `blocked` aciona alerta imediato no CFD e comunicação no Daily assíncrona.
4. **Revisão de prioridade:** Prioridades são reavaliadas no Refinement semanal (terças, 30min). Mudança de prioridade de um card `must` exige registro em commit.
5. **Compatibilidade com MoSCoW:** As labels `must`/`should` permanecem — elas classificam **valor**, enquanto P0–P3 classifica **urgência temporal**. Ambas coexistem sem conflito.

---

## PARTE F — Verificação de Congruência

| Item                                                                          | Status       |
| ----------------------------------------------------------------------------- | ------------ |
| Todos os 21 cards possuem prioridade atribuída                               | ✅ OK        |
| Distribuição P0 compatível com WIP limit (6 P0 ÷ 3 membros = 2 P0/membro) | ✅ OK        |
| Nenhum card P0 é`should` (todos são `must`)                             | ✅ OK        |
| Todos os cards exigidos no critério de aceite do M1 (TAP §6) são P0        | ✅ OK        |
| Cards com milestone M2 não são P0/P1 (exceto quando bloqueiam M1)           | ✅ OK        |
| Sistema de tags atualizado de 23 para 27 labels                               | ✅ Declarado |
| Rastreabilidade ao TAP §6 (critério de aceite M1) preservada                | ✅ OK        |
| Coerência com WIP limit da ADR-002                                           | ✅ OK        |
| Coerência com premissa P5 (≤ 20h/semana)                                    | ✅ OK        |

---

**Status:** Sistema de prioridade P0–P3 definido para os 21 cards do M1. Labels `P0`–`P3` aplicadas no repositório GitHub.

---
