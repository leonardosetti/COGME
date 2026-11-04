# 3 CRONOGRAMA

**Plano de Gerenciamento do Cronograma**
**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Versão:** 1.2 · **Data:** 21/09/2026
**Autores:** Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

Este plano deriva diretamente das Premissas P1 (governança híbrida), P5 (disponibilidade de até 20h semanais por membro) e P7 (stakeholder-avaliador único nos marcos), e das Restrições de Cronograma e de Recursos (TAP §8) e de Orçamento (TAP §11), respeitando o Domínio de Planejamento e o Domínio de Medição do PMBOK® 7ª edição. Aplicam-se a este documento o regime de freeze do TAP e as Notas de Contexto registradas na seção 3.8 (NC-00).

### 3.1 Identificação e Propósito

Este Plano de Gerenciamento do Cronograma define como o tempo do projeto COGME é estruturado, estimado, consolidado e controlado. Sua função ontológica é complementar e subordinada ao TAP como fonte autorizativa: o TAP fixa os marcos M1–M4 (§6), o Plano de Escopo decompõe o trabalho em pacotes e cards (§2.5) e este plano governa o sequenciamento, a estimativa e o controle temporal entre ambos, sem duplicar o roadmap nem os gates DoR/DoD (Escopo §2.6).

Canonicidade e regime de freeze: o TAP, o Plano de Integração e o Plano de Escopo permanecem fontes canônicas de autorização, coordenação e escopo. O TAP encontra-se em regime de freeze desde o início do planejamento — sua última versão (18/09/2026) precede os planos de gerenciamento e não é objeto de revisão ao longo do ciclo, em conformidade com seu status ontológico já declarado: o TAP autoriza, não integra a EAP e não é gerenciado por ciclos PDCA (Premissa P9; Glossário §11; PMBOK® 6ª §4.1, dicionário). Em caso de divergência entre seções do TAP, a seção §6 Marcos é canônica para matéria temporal (NC-00). Este plano detém as Notas de Contexto (§3.8) como mecanismo exclusivo de registro de leituras operacionais do TAP congelado.

Domínios PMBOK 7ª: Planejamento (evolução progressiva do cronograma) e Medição (monitoramento temporal do progresso).
Processos PMBOK 6ª (dicionário, obsolescência formalmente declarada conforme Integração §1.2.4): 6.1 Planejar o Gerenciamento do Cronograma; 6.2 Definir as Atividades; 6.3 Sequenciar as Atividades; 6.4 Estimar as Durações das Atividades; 6.5 Desenvolver o Cronograma; 6.6 Controlar o Cronograma. A numeração canônica aqui adotada é objeto da NC-02 (seção 3.8), frente a divergências registradas em artefatos vivos (base de conhecimento operacional e Glossário).

### 3.2 Abordagem de Gerenciamento do Cronograma (processo 6.1)

O cronograma é gerenciado em três camadas temporais distintas, materializando a Personalização da Abordagem de Desenvolvimento (PMBOK 7ª) e a ADR-002:

| Camada      | Objeto                                                 | Mecanismo de controle                                                                                                  | Estabilidade                     |
| ----------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| Macro       | Marcos M1–M4                                          | Datas fixas do TAP §6; alteração somente via change-request + ADR + comunicação (Integração §1.7.3; OKB §9.2) | Inegociável sem CCB             |
| Meso        | Macro-fases MF1–MF3 + milestone auxiliar Calibração | Períodos declarados (Integração §1.8.1; OKB §9.2); gates de fechamento entre macro-fases                          | Ajustável apenas via CCB        |
| Operacional | Cards Kanban (≤ 8h)                                   | Fluxo contínuo pull, WIP de 3 cards/pessoa, sem sprints e sem datas por atividade (ADR-002)                           | Emergente, refinado semanalmente |

Aplica-se o planejamento em ondas sucessivas (elaboração progressiva, PMBOK 6ª como dicionário): o detalhe operacional emerge no Refinement semanal (ADR-002), enquanto apenas as camadas macro e meso são objeto de controle formal de mudanças. Não existe linha de base preditiva de datas por pacote: a única linha de base temporal formal é o conjunto {marcos M1–M4 + macro-fases MF1–MF3 + milestone auxiliar Calibração}.

Trade-off declarado: abre-se mão da previsibilidade preditiva por atividade em favor de confiabilidade empírica no nível do marco, alinhado ao Domínio de Medição (PMBOK 7ª), à ADR-003 e ao valor ágil "Responder a mudanças sobre seguir um plano".

### 3.3 Definição das Atividades (processo 6.2)

A cadeia de decomposição temporal é idêntica à cadeia de decomposição do escopo, canonicamente representada na Figura 2 do Plano de Escopo (§2.5): os 37 pacotes de trabalho de nível 2 da EAP (linha de base do TAP §4 — 12 fases) decompõem-se em cards Kanban com esforço ≤ 8h, e estes, quando ≥ 6h ou com múltiplos entregáveis, decompõem-se em atividades derivadas materializadas como tasklist Markdown (3 a 7 itens; último item obrigatoriamente "Validação final"), conforme ADR-004, que rejeita formalmente subissues.

Regras operacionais desta seção: (i) a unidade atômica de cronograma e de métrica temporal é o card pai (ADR-003 e ADR-004); itens de tasklist não geram previsão nem métrica própria; (ii) nenhum card migra para `Ready` sem estimativa de esforço e dependências identificadas (DoR, Escopo §2.6); (iii) cards estimados acima de 8h são obrigatoriamente divididos antes de entrar no fluxo.

### 3.4 Sequenciamento e Dependências (processo 6.3)

Conforme a base de conhecimento operacional (§8.1) e a ADR-003, **não se constrói rede de precedências CPM no nível operacional**: em fluxo contínuo com escopo emergente, uma rede de atividades ficaria obsoleta em dias, violando o princípio GMV. O sequenciamento opera por quatro mecanismos nativos do SSOT:

a) campo "Dependências" dos Padrões A e B de redação de cards (OKB §9.3);
b) gate DoR "dependências identificadas" (Escopo §2.6);
c) label `blocked` com registro obrigatório da dependência no corpo da Issue (OKB §9.1);
d) regra P0: card que, ausente, impede o marco ou bloqueia ≥ 2 outros cards integra o caminho crítico empírico (OKB §9.4).

O caminho crítico é **identificado empiricamente** pela combinação de cards P0, alargamentos de banda no CFD e desvios de Cycle Time — definição formal, cadência e regra corretiva canonicamente na Integração §1.6.1 —, revisada a cada Refinement semanal e a cada Retrospectiva quinzenal.

No nível macro, o sequenciamento é finish-to-start entre macro-fases, com gates explícitos: o M2 encerra a MF1; a milestone auxiliar Calibração (03/10/2026) libera a baseline empírica que autoriza metas na MF2; o M3 encerra a MF2; o M4 encerra a MF3. Dentro de cada macro-fase, o paralelismo é integral, gerenciado por pull system e WIP limits (TAP §6, premissa temporal 2).

[FIG-1 — Inserção obrigatória: Sequenciamento macro e caminho crítico empírico.] Conteúdo obrigatório: faixa superior com as três macro-fases encadeadas por gates (MF1 → gate M2/Calibração → MF2 → gate M3 → MF3 → gate M4); faixa inferior com a camada operacional mostrando os quatro detectores do caminho crítico empírico (cards P0, label `blocked`, bandas do CFD, desvio de Cycle Time) alimentando a decisão de replanejamento no Refinement. Formato sugerido: Mermaid `flowchart LR`, versionado em `/docs/diagrams/`. Necessidade real: substitui visualmente a rede CPM rejeitada, demonstrando ao Prof. Dr. Nivaldo Carleto como o sequenciamento é controlado sem preditividade artificial.

### 3.5 Estimativa de Esforço e Duração (processo 6.4)

Esforço é estimado em horas pelo responsável técnico (julgamento de especialista), com classificação relativa T-shirt (PP ≤ 2h, P ≤ 4h, M ≤ 6h, G = 8h) como verificação cruzada, conforme vocabulário do Glossário (§3, processo 6.4). As faixas são binárias quanto à governança: cards ≤ 4h são atômicos e não portam tasklist; cards ≥ 6h portam tasklist obrigatória; o teto absoluto é 8h (ADR-004; Escopo §2.5).

Capacidade semanal nominal: 3 membros × 20h/semana (Premissa P5) = 60h/semana, regulada pelo WIP limit de 3 cards em `In Progress` por pessoa (ADR-002), e não por taxa de utilização fixa. O overhead dos rituais (daily assíncrona, Refinement semanal, Retrospectiva quinzenal — ADR-002) é estimado em ≤ 1h/semana por membro e absorvido pela capacidade nominal (premissa PA-3). Verificação de capacidade do marco corrente: a distribuição de trabalho do backlog M1 registra ~14h (Leonardo), ~13h (Fabricio) e ~11h (Edson), todos dentro do limite da Premissa P5, conforme tabela de distribuição da base de conhecimento operacional (§10.3) — evidência verificável de aderência (NC-06).

Duração calendarizada **não é estimada por atividade**: emerge do fluxo. O Cycle Time (definição operacional da ADR-003: `In Progress` → `Done`; divergências de redação em artefatos de origem tratadas na NC-03) possui meta de ≤ 3 dias após a calibração; a projeção de conclusão de cada marco é obtida dividindo-se o backlog ordenado por prioridade (P0 → P3) pelo Throughput empírico (meta ≥ 5 cards/semana pós-calibração; baseline em `/docs/metricas/baseline.md` após 03/10/2026, conforme ADR-003).

Convenção de dias (NC-03): métricas de fluxo (Cycle Time, CFD) são medidas em **dias corridos**, por serem nativas do GitHub Insights e não exigirem recálculo; marcos, desvios de marco e capacidade são tratados em **dias úteis**, refletindo a disponibilidade real da equipe e coerente com o gatilho de escalation da Integração §1.9 ("desvio > 3 dias úteis").

Trade-off declarado: perde-se a previsão determinística por atividade e ganha-se previsão empírica por marco com overhead zero de estimativa, conforme Domínio de Planejamento (PMBOK 7ª) e princípio GMV.

### 3.6 Desenvolvimento do Cronograma (processo 6.5)

O cronograma do COGME é materializado por três artefatos complementares: (i) o roadmap macro de marcos (Figura 2), única representação tipo Gantt admitida, restrita ao nível macro e derivada do SSOT, conforme autorização do OKB §8.1; (ii) o backlog ordenado por P0–P3 e MoSCoW no GitHub Projects, que constitui o cronograma operacional vivo; e (iii) a linha de base temporal formal {M1–M4 + MF1–MF3 + Calibração}, única sujeita a controle integrado de mudanças.

O período de calibração (23/09 a 03/10/2026) é um artefato de cronograma: converte métricas de fluxo em capacidade de previsão. Até seu encerramento, as metas permanecem suspensas (Integração §1.6.3); após, metas ajustadas pela média observada ± 20% são formalizadas via ADR (ADR-003).

Tabela 1 — Marcos, janelas e entregáveis de valor

| Marco                            | Abertura SSOT | Data alvo  | Entregável de valor                                                                                                                                                                                                                                                                                                    | Critério de aceite                                                                 |
| -------------------------------- | ------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| M1 — Entrega Parcial Documental | 01/09/2026    | 22/09/2026 | TAP aprovado + 5 planos (Áreas 1–5, incluindo 12 PDCAs e Ishikawa no Plano de Qualidade) + ADRs 001–004 + SSOT configurado (backlog M1-01 a M1-21)                                                                                                                                                                   | Submissão via GitHub validada pelo Prof. Dr. Nivaldo Carleto sem achados críticos |
| M2 — Ambiente e Modelagem       | 23/09/2026    | 30/09/2026 | Stack FOSS definida e validada por protótipo (fase N4.1, conforme TAP §10 R2); ambiente local + CI verdes; DER e Protótipo UX/UI versionados; planos das Áreas 6–8. Ressalva NC-04: formalização da stack na ADR-001 encontra-se em avaliação e pode sofrer atualização via ADR específica (Escopo §2.3.4) | Pipeline CI verde; artefatos de modelagem no repositório                           |
| Calibração (auxiliar)          | 23/09/2026    | 03/10/2026 | Baseline empírica de fluxo + ADR de metas                                                                                                                                                                                                                                                                              | Baseline publicada em`/docs/metricas/baseline.md`                                 |
| M3 — MVP Funcional (Beta)       | 04/10/2026    | 15/11/2026 | MVP full-stack operacional, coverage ≥ 80%, UAT sem defeitos críticos/bloqueantes                                                                                                                                                                                                                                     | Métricas de fluxo dentro da baseline calibrada                                     |
| M4 — Encerramento               | 16/11/2026    | 15/12/2026 | Documentação técnica consolidada, lições aprendidas, verificação SMART, apresentação final, tag de release                                                                                                                                                                                                     | Validação acadêmica pelo Prof. Dr. Nivaldo Carleto e tag de release final        |

Fontes: TAP §6; OKB §9.2; Integração §1.3.3 e §1.8.1. Datas idênticas em todos os artefatos.

Nota de Contexto (NC-01): o objetivo SMART de Cronograma (TAP §3, item ii) registra "documentação consolidada" em novembro/2026, enquanto o TAP §6 e o critério de sucesso §3.2.g alocam consolidação e aceite no M4 (15/12/2026). Pela regra de precedência intra-TAP (NC-00), este plano operacionaliza a leitura do §6, sem alteração de datas: a entrega do MVP funcional que satisfaz o SMART ii na dimensão produto ocorre no M3 (15/11/2026, novembro); a consolidação documental acadêmica ocorre no M4. A seção SMART é assim assimilada à luz da seção §6 Marcos, em conformidade com o regime de freeze — nenhuma revisão do TAP é prevista ou citada.

[FIG-2 — Inserção obrigatória: Roadmap macro do cronograma.] Conteúdo obrigatório: três faixas horizontais MF1 (01/09–30/09), MF2 (01/10–15/11) e MF3 (16/11–15/12); cinco marcadores de milestone nas datas da Tabela 1, com a Calibração graficamente distinguida como auxiliar; anotação "única representação tipo Gantt admitida — nível macro, derivada do SSOT (OKB §8.1); nível operacional regido por fluxo (ADR-002)". Formato sugerido: Mermaid `gantt` ou `timeline`, versionado em `/docs/diagrams/`. Necessidade real: supre a expectativa mínima de visualização temporal do avaliador sem reintroduzir preditividade operacional rejeitada pela ADR-003.

Gantt operacional via ProjectLibre: não produzido proativamente (GMV); será derivado do Kanban somente se exigido formalmente pelo Prof. Dr. Nivaldo Carleto em avaliação (Glossário §7).

### 3.7 Controle do Cronograma (processo 6.6)

O monitoramento temporal é contínuo e nativo do SSOT (Domínio de Medição): o CFD exerce, neste plano, a função de monitoramento temporal substituto do Gantt/EVM (função atribuída pela base de conhecimento operacional, §8.2; definição formal, cadência semanal e regra corretiva de banda 2× canonicamente na Integração §1.6.1, aqui apenas referenciadas); Cycle Time e Throughput são publicados semanalmente via GitHub Insights; o WIP em fluxo é verificado continuamente (≤ 9 cards).

Gatilhos de ação corretiva com recorte temporal (derivados da Integração §1.9):

| Gatilho                                                | Ação corretiva                                                                              | Base temporal          |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------- | ---------------------- |
| Desvio > 3 dias úteis em qualquer marco M1–M4        | Issue`change-request` + proposta de replanejamento + ADR                                    | Dias úteis            |
| Throughput < 3 cards/semana por 2 semanas consecutivas | Revisão de WIP limits (fallback ADR-002) + reavaliação do escopo do MVP (fallback ADR-003) | Semanas                |
| Banda do CFD > 2× a largura média por 2 semanas      | Retrospectiva extraordinária + replanejamento do gargalo (caminho crítico empírico, §3.4) | Semanas                |
| Card P0 com label`blocked` por > 48h                 | Intervenção direta do GP + resolução ou substituição da dependência                    | Horas corridas (NC-05) |

Fechamento de milestones: uma milestone não é fechada enquanto houver Issues abertas com label `change-request` ou `blocked`; o fechamento exige critérios atendidos, registro de lições aprendidas e comunicação ao Prof. Dr. Nivaldo Carleto quando aplicável (M1, M3, M4), conforme regras da base de conhecimento operacional (§9.2). Alteração de data de marco oficial exige change-request + aprovação do CCB (GP, membro único) + ADR + comunicação no marco subsequente (Integração §1.7.3); a milestone auxiliar Calibração pode ser reajustada pelo GP com registro em commit.

### 3.8 Notas de Contexto e Registro de Saneamento dos Artefatos Vivos

**NC-00 — Regime de freeze do TAP e precedência intra-TAP (decisão do GP, 21/09/2026).** O TAP encontra-se congelado desde o início do planejamento (última versão datada de 18/09/2026, anterior a este plano): não é revisado, reversionado ou corrigido ao longo do ciclo, em conformidade com seu status ontológico (Premissa P9; Glossário §11; PMBOK® 6ª §4.1 como dicionário). Duas regras derivam: (i) precedência intra-TAP — em divergência entre seções do TAP, a seção §6 Marcos é canônica para matéria temporal e de marcos; (ii) locus de contexto — este documento de Planejamento (8 Áreas) detém, com precedência, as Notas de Contexto que registram a leitura operacional vigente do TAP congelado; divergências jamais são tratadas como correções do TAP. Trade-off declarado: aceita-se divergência textual entre o termo autorizativo imutável e a leitura operacional, em favor da imutabilidade da referência de autorização e da trilha auditável de interpretações. A decisão atende aos gatilhos G1 (impacto transversal — todos os 8 planos), G3 (questionabilidade acadêmica) e G4 (trade-off não óbvio) da Política de ADRs (Aditivo da base de conhecimento, §1.2) → ADR-005 encaminhada para emissão antes do M2, com incorporação da cláusula na próxima revisão do Plano de Integração (§1.4).

**NC-01 — Assimilação do SMART de Cronograma à seção §6.** Registro e resolução da divergência entre TAP §3 (item ii) e TAP §6/§3.2.g quanto à "documentação consolidada": prevalece a leitura do §6 — MVP funcional no M3 (novembro/2026) e consolidação documental acadêmica no M4 (15/12/2026). Aplicada em §3.6. Nenhuma revisão do TAP é prevista ou citada (regime de freeze).

**NC-02 — Numeração canônica dos processos de cronograma.** Este plano adota a numeração oficial do PMBOK® 6ª edição (6.1–6.6). Divergências registradas na base de conhecimento operacional (§8.1) e no Glossário (§3) — artefatos vivos — não são replicadas aqui e constam do registro de saneamento.

**NC-03 — Convenção dupla de dias e definição operacional de Cycle Time.** Métricas de fluxo em dias corridos (nativo GitHub Insights); marcos, desvios e capacidade em dias úteis. A definição operacional de Cycle Time aqui vigente é `In Progress` → `Done` (ADR-003), prevalecendo sobre redações divergentes em artefatos de origem; a leitura do TAP congelado é registrada por esta nota, e o saneamento aplica-se apenas aos artefatos vivos (ADR-003, Glossário, baseline).

**NC-04 — Redação do critério M2 (stack).** A expressão "Stack FOSS validada (ADR-001)" foi substituída por "definida e validada por protótipo (TAP §10, R2; fase N4.1)", com ressalva de que a formalização na ADR-001 está em avaliação e mudanças de stack exigem ADR específica (Escopo §2.3.4). Aplicada na Tabela 1.

**NC-05 — Base temporal do gatilho de bloqueio P0.** O limiar de 48h para cards P0 `blocked` é medido em horas corridas (evento de fluxo), distinguindo-se da base de dias úteis aplicada a desvios de marco. Aplicada em §3.7.

**NC-06 — Verificação de capacidade do marco corrente.** Registrada como evidência verificável a distribuição de carga do backlog M1 (base de conhecimento operacional, §10.3), com todos os membros dentro do limite de 20h semanais (Premissa P5). Aplicada em §3.5.

**Entendimentos sobre o TAP congelado (notas de contexto — sem saneamento):**

| Matéria                         | Seção do TAP (congelado) | Entendimento adotado neste plano                                                              |
| -------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------- |
| SMART ii × consolidação no M4 | §3 × §6                 | NC-01: §6 prevalece; MVP funcional no M3, consolidação no M4                               |
| Cabeçalho "Fases EAP v2.0"      | §5                        | EAP citada sem versão interna (regra já aplicada neste plano)                               |
| Subnumeração das restrições  | §8                        | Restrições citadas por categoria nominal + §11 (orçamento); subnumeração não presumida |
| Cycle Time "To Do → Done"       | §3 (Métricas)            | Definição operacional`In Progress` → `Done` (ADR-003), via NC-03                       |

**Registro de saneamento — artefatos vivos (não bloqueante):**

| Pendência                                                             | Artefato vivo                          | Momento previsto                         |
| ---------------------------------------------------------------------- | -------------------------------------- | ---------------------------------------- |
| Numeração 6.3/6.5 no §8.1                                           | Base de conhecimento operacional §8.1 | Próxima revisão da base                |
| "Processo 6.4 Estimar Custos" → 6.4 Estimar Durações (custos = 7.2) | Glossário §3                         | Próxima revisão do Glossário          |
| Grafia "Carleto" → "Carleto"                                         | Glossário                             | Próxima revisão do Glossário          |
| Cycle Time "To Do → Done" → "In Progress → Done"                    | Glossário                             | Próxima revisão do Glossário          |
| Contagem EAP "13/48" → 12/37 (baseline do TAP §4)                    | Glossário §1                         | Próxima revisão do Glossário          |
| Convenção dupla de dias                                              | ADR-003 / Glossário / baseline        | Formalização da baseline (após 03/10) |
| Cláusula NC-00 na hierarquia formal + ADR-005                         | Integração §1.4 / ADR-005           | Antes do M2                              |

### 3.9 Declaração de Rastreabilidade

Tabela 2 — Rastreabilidade interna do Plano de Cronograma

| Seção                                                 | Origem                                                                          | Domínio PMBOK 7ª                          | Processo PMBOK 6ª |
| ------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------- | ------------------ |
| 3.2 (Abordagem em 3 camadas)                            | TAP §1.c + §6 + Premissa P1                                                   | Abordagem de Desenvolvimento + Planejamento | 6.1                |
| 3.3 (Definição de atividades)                         | TAP §4 + Escopo §2.5 + ADR-004                                                | Planejamento + Trabalho do Projeto          | 6.2                |
| 3.4 (Sequenciamento e caminho crítico empírico)       | TAP §6 (premissa 2) + OKB §8.1 + ADR-002                                      | Planejamento + Entrega                      | 6.3                |
| 3.5 (Estimativa; verificação de capacidade NC-06)     | Premissa P5 + TAP §8 + OKB §10.3 + ADR-003                                    | Planejamento + Medição                    | 6.4                |
| 3.6 (Roadmap, linha de base, calibração, NC-01/NC-04) | TAP §6 + §3 (SMART Cronograma) + §10 (R2) + Escopo §2.3.4                   | Planejamento + Medição                    | 6.5                |
| 3.7 (Controle e gatilhos; NC-05)                        | TAP §3.3 + §3 (Métricas) + Integração §1.9                                | Medição + Incerteza                       | 6.6                |
| 3.8 (Notas de Contexto; regime de freeze)               | Decisão do GP (21/09/2026) + Premissa P9 + Glossário §11 + Aditivo OKB §1.2 | Trabalho do Projeto + Incerteza             | 4.6 (dicionário)  |

Verificação: 100% das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa, restrição do TAP ou decisão formal do GP; referências cruzadas apontam exclusivamente para locais canônicos (Integração §1.6.1 para CFD; Escopo §2.5/§2.6 para decomposição e gates; OKB §9.2 para regras de milestone).

### 3.10 Premissas e Restrições Aplicáveis

Premissas do TAP: P1 (governança híbrida), fundamenta §3.2; P5 (20h/semana), fundamenta §3.5; P7 (avaliador nos marcos), fundamenta §3.7; P9 (separação ontológica TAP ≠ EAP ≠ PDCA), fundamenta o regime de freeze da §3.8.
Premissas específicas deste plano: PA-1 — datas de abertura e fechamento de milestones no GitHub são marcadores administrativos do SSOT, não dias trabalhados (sana a leitura de abertura do M3 em 04/10/2026 frente ao início da MF2 em 01/10/2026); PA-2 — convenção dupla de dias (NC-03); PA-3 — overhead de rituais ≤ 1h/semana por membro, absorvido pela capacidade nominal; PA-4 — GitHub Insights disponível e gratuito durante todo o ciclo (TAP §11).
Restrições: prazo letivo inegociável e curso noturno (TAP §8 — Restrições de Cronograma e de Recursos), fundamentam §3.5 e §3.7; orçamento zero (TAP §11), veta ferramentas pagas de cronograma e fundamenta a rejeição de Gantt/CPM operacionais (ADR-003); equipe de 3 pessoas com múltiplos papéis (TAP §8 — Recursos), fundamenta o WIP limit como regulador de capacidade.

**Controle de Versões**

| Versão | Data       | Alteração                                                                                                                                                                                                                                                                                                                                             | Responsável         |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| 1.0     | 21/09/2026 | Emissão inicial para o M1: abordagem em 3 camadas; caminho crítico empírico; convenção dupla de dias; FIG-1 e FIG-2                                                                                                                                                                                                                                | Leonardo D. S. Setti |
| 1.1     | 21/09/2026 | Revisão crítica: Notas de Correção NC-00 a NC-06; M2 reescrito (NC-04); base temporal do gatilho P0 (NC-05); verificação de capacidade (NC-06)                                                                                                                                                                                                    | Leonardo D. S. Setti |
| 1.2     | 21/09/2026 | Rodada 10 — Diretriz D3 do GP: regime de freeze do TAP formalizado (NC-00); precedência intra-TAP da seção §6 Marcos; §3.8 reconstituída como Notas de Contexto; supressão integral de referências a correção/revisão/saneamento do TAP; saneamento restrito a artefatos vivos; ADR-005 redefinida (regime de freeze) e mantida antes do M2 | Leonardo D. S. Setti |
