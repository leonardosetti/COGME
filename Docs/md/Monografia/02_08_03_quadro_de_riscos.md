# 2.8.3 Quadro de Riscos

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** Tabela reproduzida da monografia com 16 ameaças e 3 oportunidades. As situações não foram atualizadas com evidências de execução. Faltam responsáveis, prazos e critérios da escala de severidade. Os 28% citados são saldo de capacidade do marco parcial (18 de 64 horas-equipe), não folga de atividade calculada em rede nem reserva de cronograma formalmente demonstrada. R-13 depende da conciliação das datas 08/09 e 22/09; R-14 requer revisão da premissa sobre licenciamento e comercialização.

O Quadro 15 consolida o registro de riscos do projeto, organizado por categoria, reunindo primeiro as ameaças e, ao final, as oportunidades, com a respectiva qualificação de impacto e severidade, a resposta planejada e a situação de acompanhamento na data de elaboração deste trabalho.

O Domínio de Incerteza do PMBOK® 7ª edição trata a incerteza em ambas as direções, de modo que o registro contempla não apenas ameaças, mas também oportunidades — eventos incertos cuja ocorrência produz efeito favorável e que, por isso, demandam resposta deliberada de exploração, e não de mitigação. As oportunidades identificadas encontram-se ao final do quadro, sob a identificação O-01 a O-03. Registre-se, ainda, que a inexistência de orçamento de aquisições impede a constituição de reserva de contingência financeira; a reserva do projeto é, portanto, de cronograma, materializada na folga de 28% apurada no plano de ação do marco parcial e reservada exclusivamente à absorção de riscos materializados, não à ampliação de escopo.

**Quadro 15 — Registro de riscos do projeto**

| ID | Risco | Prob. | Impacto | Severidade | Resposta Planejada | Situação |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | Stack tecnológica FOSS indefinida bloqueia a fase de desenvolvimento | 80% | Alto | Crítica | Formalização do ADR-002 (stack e SDD local) | Encerrado |
| R-02 | EAP não sincronizada com o quadro Kanban | 60% | Alto | Alta | Mapeamento um para um entre pacotes e cartões | Em andamento |
| R-03 | Governança consome mais de 50% do tempo da equipe | 70% | Médio | Alta | Aplicação do princípio de governança mínima viável | Aberto |
| R-04 | Alteração não controlada de escopo (scope creep) | 50% | Alto | Alta | Comitê de controle de mudanças e critérios de prontidão | Monitorado |
| R-05 | Equipe excede 20 horas semanais (sobrecarga) | 50% | Médio | Alta | Limites de trabalho em progresso e métrica de sobrecarga | Monitorado |
| R-06 | Indisponibilidade ou limitação da API gratuita de câmbio | 40% | Alto | Alta | Cache local de cotações e provedor alternativo | Aberto |
| R-07 | Erros lógicos ou de segurança em código gerado por IA | 40% | Alto | Alta | Revisão humana obrigatória, testes e commits rastreáveis | Monitorado |
| R-08 | Ciclos PDCA não documentados por atividade | 40% | Médio | Média | Template padronizado de PDCA no Plano de Qualidade | Aberto |
| R-09 | Confusão conceitual entre TAP, EAP e PDCA | 30% | Médio | Média | ADR-004 e alinhamento da equipe | Aberto |
| R-10 | Exigência de cronograma tradicional (Gantt) | 30% | Médio | Média | ADR-001 e geração de Gantt derivado do Kanban | Mitigado |
| R-11 | Diagrama de Ishikawa incompleto | 30% | Médio | Média | Template padronizado dos 6M no Plano de Qualidade | Aberto |
| R-12 | Modelo de linguagem local não atinge o desempenho mínimo | 20% | Médio | Média | Fallback para modelo de menor porte já validado | Mitigado |
| R-13 | Entrega parcial de 22/09/2026 não concluída | 15% | Alto | Alta | Plano de ação de 10 a 22/09 com folga de 28% | Mitigado |
| R-14 | Licenciamento aberto restringe comercialização futura | 80% | Baixo | Baixa | Risco aceito, decorrente da premissa P2 e do escopo acadêmico | Aceito |
| R-15 | Tarifas e spreads de provedores desatualizados ou sem API pública | 60% | Alto | Alta | Base parametrizável com data de vigência e revisão manual periódica | Aberto |
| R-16 | Divergência entre a cotação PTAX e a taxa praticada pelo provedor | 40% | Médio | Média | Exibição explícita da fonte e da data de cada cotação no comparativo | Aberto |
| O-01 | Ganho de produtividade acima do previsto com o desenvolvimento guiado por especificação | 50% | Alto | Alta | Ampliar o escopo do comparativo para novos provedores, mediante aprovação formal | Aberto |
| O-02 | Reaproveitamento do motor de comparação como interface pública de consulta | 40% | Médio | Média | Documentar contratos de interface desde a construção, viabilizando exposição futura | Aberto |
| O-03 | Interesse da comunidade de software livre no repositório do projeto | 30% | Médio | Baixa | Publicar documentação de contribuição e licença desde a primeira entrega | Aberto |

Fonte: elaborado pelos autores (2026).

## Fonte documental

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.8.3.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

O quadro deve permitir saber quem acompanha o risco e quando a ação precisa ocorrer. Os estados existentes na monografia necessitam de evidências e data de atualização.

- [ ] Adicionar causa–evento–efeito, categoria, probabilidade, impacto, prioridade, proprietário, resposta, responsável pela ação, gatilho, prazo, situação, evidência e risco residual.
- [ ] Explicar a escala usada e atualizar as 16 ameaças e 3 oportunidades sem atribuir responsáveis ou datas fictícios.
- [ ] Distinguir reserva planejada, folga de cronograma e saldo de capacidade; rever a data do marco parcial e a justificativa do risco R-14.

**Entrega esperada:** Quadro rastreável e atualizado; campos desconhecidos devem constar como a definir, com a pendência identificada.
