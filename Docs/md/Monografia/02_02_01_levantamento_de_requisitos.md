# 2.2.1 Levantamento de requisitos

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** REQ-01 a REQ-15 estão no TAP; REQ-16 a REQ-19 foram encontrados na monografia e dependem de conciliação com o escopo do TAP. As referências a N9 (base de conhecimento) e N11 (documentação) no texto de origem seguem a numeração do TAP; no Quadro 7 da monografia essas entregas são N10 e N12. REQ-01 menciona tempo real, enquanto REQ-16 exige PTAX de fechamento por dia útil: distinguir atualização da consulta e data da cotação. As metas abaixo são critérios planejados, não resultados de testes.

Os requisitos do projeto foram levantados a partir dos objetivos SMART definidos no TAP (§3) e organizados em consonância com os domínios de Partes Interessadas e de Entrega do PMBOK® 7ª edição, sendo cada requisito mensurável, rastreável e vinculado a um pacote de trabalho específico da EAP. O Quadro 4 apresenta os requisitos funcionais e não funcionais relativos ao MVP web (Fase N5 da EAP).

**Quadro 4 — Requisitos funcionais e não funcionais do MVP**

| ID | Requisito | Critério de Aceite |
| --- | --- | --- |
| REQ-01 | Simulação de conversão cambial em tempo real (USD/EUR → BRL) | Cotação obtida via API externa com latência ≤ 2s |
| REQ-02 | Suporte a 5 regimes de contratação (hora, dia, semana, mês, valor fixo) | 100% dos regimes operacionais em UAT |
| REQ-03 | Aplicação de encargos financeiros simulados (spread + IOF) | Cálculo auditável com precisão de 2 casas decimais |
| REQ-04 | Emissão de invoice em formato PDF | Geração via WeasyPrint em ≤ 3s por documento |
| REQ-05 | Tempo de resposta da aplicação | ≤ 3s em 95% das requisições (ambiente homologação) |
| REQ-06 | Interface web responsiva (FOSS) | Compatível com Chrome/Firefox/Edge (últimas 2 versões) |
| REQ-07 | Cache de cotações (SQLite) | Redução de ≥ 50% das chamadas à API externa |
| REQ-16 | Integração com a API de cotações oficiais do Banco Central do Brasil (PTAX) | Cotação PTAX de fechamento obtida por dia útil, com registro de data, moeda e tipo (compra/venda) |
| REQ-17 | Comparativo de custo entre provedores de pagamento internacional | Mínimo de 4 provedores comparados, com spread, tarifa fixa e valor líquido estimado por operação |
| REQ-18 | Ranqueamento por menor custo efetivo total | Ordenação automática pelo valor líquido a receber, com detalhamento da composição do custo |
| REQ-19 | Encaminhamento do usuário ao provedor selecionado | Link direto para o site oficial do provedor escolhido, com aviso de que a operação ocorre fora do COGME |

Fonte: elaborado pelos autores (2026).

Complementarmente, o Quadro 5 apresenta os requisitos não funcionais e de processo relativos à garantia da qualidade (Fase N6), à integração contínua (Fase N7), à base de conhecimento (Fase N9), à documentação técnica (Fase N11) e à conformidade FOSS (Fases N1 e N4) do projeto.

**Quadro 5 — Requisitos de qualidade, integração contínua e implantação**

| ID | Requisito | Critério de Aceite |
| --- | --- | --- |
| REQ-08 | Cobertura de testes automatizados | ≥ 80% do código (unitários e integração via pytest e coverage.py) |
| REQ-09 | Testes de aceitação (UAT) | 100% dos fluxos críticos aprovados, zero defeitos críticos ou bloqueantes |
| REQ-10 | Aplicação de ferramentas da qualidade (PDCA + Ishikawa 6M) | 12 PDCAs consolidados e diagrama de causa e efeito documentados no Plano de Qualidade |
| REQ-11 | Pipeline CI funcional | Lint + testes rodando em até 5 minutos por push |
| REQ-12 | ADRs para decisões arquiteturais críticas | Mínimo de 3 ADRs registrados (stack, Kanban, métricas) |
| REQ-13 | Rastreabilidade de prompts SDD | 100% dos prompts catalogados no repositório do projeto |
| REQ-14 | Documentação técnica consolidada | Arquitetura e APIs (OpenAPI) revisadas e aprovadas |
| REQ-15 | Licenciamento 100% FOSS | Todas as dependências com licenças aprovadas pela OSI (MIT, Apache 2.0, BSD, GPL) |

Fonte: elaborado pelos autores (2026).

## Fontes documentais

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.2.1 e respectivos quadros.
- [Termo de Abertura do Projeto v1_opngoing.docx](../../docx/Termo%20de%20Abertura%20do%20Projeto%20v1_opngoing.docx), objetivos, EAP, requisitos e restrições.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

Uma lista de funcionalidades precisa ser complementada por origem, prioridade e condições verificáveis. No COGME, expressões como tempo real e cálculo correto devem resultar em regras explícitas sobre cotação, data, arredondamento e encargos.

- [ ] Criar matriz com ID, tipo, descrição, origem, prioridade, regra de negócio, critério de aceite, pacote EAP, teste, situação e validação.
- [ ] Especificar entradas inválidas, moedas suportadas, data e tipo da cotação, ausência de cotação no dia consultado, encargos parametrizados, arredondamento, empates no comparativo e campos da invoice.
- [ ] Diferenciar requisito funcional, não funcional e regra de negócio; levantar dúvidas com o orientador e registrar a decisão, incluindo aprovação dos requisitos adicionais.

**Entrega esperada:** Exemplo proposto de aceite: dada uma cotação de teste e encargos definidos, o resultado deve coincidir com o cálculo de referência documentado e exibir a data e a fonte utilizadas.
