
# ADR-007 — Redes de Projeto como Artefato Acadêmico Macro (Dualidade CPM × Kanban)

| Campo                                         | Valor                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Versão**                             | 1.1.0                                                                                                                                                                                                                                                                                                      |
| **Status**                              | Aprovado (ratificado pelo CCB-001 em 29/10/2026)                                                                                                                                                                                                                                                           |
| **Data da decisão**                    | 29/10/2026                                                                                                                                                                                                                                                                                                 |
| **Data de formalização do documento** | 29/10/2026                                                                                                                                                                                                                                                                                                 |
| **Decisor**                             | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7)                                                                                                                                                                                                                                                      |
| **Gatilhos G1–G4**                     | G1 (impacto transversal — Cronograma + Integração + Escopo), G3 (questionabilidade acadêmica — imposição do stakeholder-avaliador Prof. Dr. Nivaldo Carleto quanto à presença de redes CPM), G4 (trade-off não óbvio — dualidade de modelos preditivo macro × ágil micro)                    |
| **Rastreabilidade**                     | TAP §3 (Métricas) + §6 (Marcos M1–M4); EAP N3.1–N3.6; REQ-12; ADRs correlatas: ADR-002 (Kanban como método de execução), ADR-003 (métricas de fluxo, sobreposta parcialmente), ADR-005 (freeze do TAP); NC-01 e NC-04 do Plano de Cronograma §3.6; Figuras 16–21 e Tabelas 53–58 do Plano v2.0 |
| **Domínio PMBOK 7ª**                  | Planejamento + Medição + Entrega                                                                                                                                                                                                                                                                         |
| **Processo PMBOK 6ª (dicionário)**    | 6.3 Sequenciar Atividades; 6.5 Desenvolver Cronograma                                                                                                                                                                                                                                                      |

## Contexto

O Plano de Cronograma v2.0 (§3.4) apresentava redes CPM (Critical Path Method) com caminho crítico, folgas e sequenciamento preditivo. A ADR-003 havia declarado métricas EVM (SPI/CPI/VAC) como LEGADO — NÃO APLICÁVEIS, substituindo-as por métricas de fluxo Kanban (Cycle Time, Throughput, CFD, WIP, Coverage).

Essa tensão gerou contradição interna no documento: se EVM é inaplicável, por que manter redes CPM? Além disso, o Prof. Dr. Nivaldo Carleto, como stakeholder-avaliador, exigiu expressamente a presença de redes de projeto como artefato de validação acadêmica de viabilidade macro.

A questão central não era técnica, mas epistemológica: como conciliar um modelo preditivo (CPM/Gantt) com um modelo adaptativo (Kanban/fluxo contínuo) sem quebrar o SSOT operacional?

## Opções Consideradas

| #  | Opção                                                                     | Prós                                                           | Contras                                                                                               |
| -- | --------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| O1 | Eliminar completamente as redes CPM                                         | Pureza metodológica ágil; elimina contradição               | Viola imposição direta do stakeholder-avaliador; perde evidência acadêmica de viabilidade macro   |
| O2 | Manter redes CPM como linha de base operacional                             | Atende requisito acadêmico                                     | Contradiz ADR-003; reintroduz EVM implicitamente; confunde equipe sobre qual modelo executar          |
| O3 | Dualidade documentada: CPM macro (acadêmico) × Kanban micro (operacional) | Atende stakeholder sem quebrar SSOT; transparência pedagógica | Exige comunicação clara para evitar confusão operacional; overhead de manutenção de dois modelos |

## Decisão

**Aprovar a opção O3.**

1. As redes de projeto (Figuras 16–21, Tabelas 53–58 do Plano v2.0) são mantidas **exclusivamente como artefatos de validação acadêmica de viabilidade macro**, atendendo à imposição do Prof. Dr. Nivaldo Carleto.
2. O nível operacional permanece regido pelo fluxo Kanban (ADR-002) e métricas de fluxo (ADR-003). Nenhuma atividade diária, card ou sprint é planejada com base em datas preditivas derivadas das redes CPM.
3. A dualidade deve ser explicitada textualmente no Plano de Cronograma §2.4.4 com a frase canônica: *"A rede valida o marco; o Kanban executa a tarefa."*
4. As redes CPM devem ser refatoradas de PNG para SVG editável (ação P2.3 do input canônico), com caminho crítico destacado em `#C0392B`.
5. Métricas EVM continuam declaradas como LEGADO — NÃO APLICÁVEIS (ADR-003). As redes servem apenas para demonstrar coerência temporal macro entre marcos M1–M4, não para controle diário.

## Consequências

- Positivas: atende requisito acadêmico mandatório sem contaminar execução operacional; preserva integridade da ADR-002 e ADR-003; demonstra maturidade metodológica da equipe ao lidar com dualidade.
- Negativas: risco de confusão se a comunicação não for clara; overhead de manter dois modelos sincronizados nos marcos.
- Neutras: as redes não geram alertas automáticos nem gates operacionais; sua função é estritamente expositiva-acadêmica.

## Trade-offs Declarados

| Aspecto                       | Ganho                                         | Perda/Risco                              | Mitigação                                                                        |
| ----------------------------- | --------------------------------------------- | ---------------------------------------- | ---------------------------------------------------------------------------------- |
| CPM macro + Kanban micro      | Compliance acadêmico + agilidade operacional | Dualidade cognitiva para a equipe        | Comunicação explícita no Refinement semanal; blindagem textual no Plano §2.4.4 |
| Redes como artefato estático | Simplicidade de manutenção                  | Obsolescência rápida se marcos mudarem | Atualização obrigatória nas mudanças de marco via CR + ADR                     |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo                                                                                            | Domínio PMBOK 7ª       | Data       |
| -------------- | -------- | ------------------------------------------------------------------------------------------------- | ------------------------ | ---------- |
| ADR-003        | Parcial  | Autoriza redes CPM no nível macro/acadêmico, sem reintroduzir EVM/SPI/CPI no nível operacional | Planejamento + Medição | 29/10/2026 |

## kill_switch

Não aplicável diretamente. Contudo, se uma rede CPM for utilizada indevidamente como gate operacional (ex.: bloquear card por divergência de data preditiva), isso constitui violação da ADR-002 e ADR-003, acionando abortamento da operação e escalonamento ao CCB.

## Governança

- **Custódia:** `agent-scheduler` (área de Cronograma).
- **Validação:** cada mudança de marco (M1–M4) exige atualização das redes CPM correspondentes antes do fechamento do marco.
- **Comunicação:** o GP deve reiterar a dualidade em toda retrospectiva onde houver dúvida sobre precedência entre CPM e Kanban.
