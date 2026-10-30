Esta seção define os pontos de verificação temporal críticos (milestones) do projeto COGME, conforme o Processo 6.5 (Desenvolver o Cronograma) do PMBOK® 6ª edição e o Domínio de Medição do PMBOK® 7ª edição. Os marcos estão diretamente vinculados às Macro-Fases (MF) da Estrutura Analítica do Projeto (EAP v2.0) e servem como gatilhos para entregas de valor e validação pelo stakeholder.

**Regra de consistência:** Todo marco deve possuir (a) data alvo realista, (b) descrição clara do entregável de valor, (c) vínculo com a Macro-Fase da EAP, e (d) critério de aceite objetivo.

#### 6.1. Tabela de Marcos Principais

| ID           | Macro-Fase (EAP)              | Descrição do Marco (Entrega de Valor)                                                                                                                                                                        | Data Alvo            | Critério de Aceite                                                                                   |
| ------------ | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| **M1** | **MF1: Fundação**     | **Entrega Parcial Documental:** Aprovação do TAP v1.0 + Planos de Gerenciamento das Áreas 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade) + 12 PDCAs consolidados + Diagrama de Ishikawa. | **22/09/2026** | Documentação submetida via GitHub e validada pelo Prof. Dr. Nivaldo Carleto sem achados críticos. |
| **M2** | **MF1: Fundação**     | **Ambiente e Modelação Concluídos:** Stack FOSS definida e validada (ADR-002), ambiente local/CI configurado, DER e Protótipo UX/UI aprovados.                                                       | **30/09/2026** | Pipeline CI "verde" e artefatos de modelagem versionados no repositório.                             |
| **M3** | **MF2: Construção**   | **MVP Funcional (Beta):** Código-fonte full-stack operacional (Backend, Frontend, PDF, SDD com IA), com cobertura de testes ≥ 80% e validado em UAT local.                                             | **15/11/2026** | Zero defeitos críticos/bloqueantes; métricas de fluxo (Cycle Time/Throughput) dentro da baseline.   |
| **M4** | **MF3: Consolidação** | **Encerramento e Aceite Final:** Documentação técnica consolidada, lições aprendidas, verificação dos critérios SMART e apresentação final com aceite formal.                                  | **15/12/2026** | Termo de Aceite assinado pelo Prof. Dr. Nivaldo Carleto e repositório com tag de release final.     |

#### 6.2. Premissas Temporais e Riscos Associados

1. **Janela de Entrega Parcial:** O marco M1 (22/09/2026) é inegociável para fins de avaliação acadêmica intermediária. Qualquer desvio superior a 3 dias úteis acionará o processo de Gestão de Mudanças (Fase N10 da EAP).
2. **Paralelismo via Kanban:** As datas representam o *target* de conclusão da Macro-Fase. Dentro de cada MF, as fases da EAP não são estritamente sequenciais; o paralelismo é gerenciado via *pull system* e WIP limits no GitHub Projects.
3. **Risco de Atraso (R-01 e R-08):** A sobrecarga da equipe ou a indefinição da stack podem impactar os marcos M2 e M3. A mitigação depende da aplicação rigorosa do princípio de Governança Mínima Viável (GMV) e do fallback para modelos LLM mais leves (Qwen 14B) se necessário.

#### 6.3. Declaração de Rastreabilidade (Marcos → EAP → Objetivos SMART)

| Marco | Fases da EAP v2.0 Abrangidas      | Objetivo SMART do TAP §3 Atendido          |
| ----- | --------------------------------- | ------------------------------------------- |
| M1    | N1, N2, N3, N4, N9, N10 (parcial) | Cronograma (Marcos) e Inovação (FOSS/SDD) |
| M2    | N4 (conclusão), N3 (conclusão)  | Produto (Escopo) e Inovação (Ferramentas) |
| M3    | N5, N6, N7                        | Produto (Escopo) e Qualidade e Testes       |
| M4    | N11, N12, N13                     | Qualidade e Testes e Cronograma (Marcos)    |
