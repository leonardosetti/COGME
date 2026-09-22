# 2.4.4 Tabela de Precedência

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** Tabela parcial reproduzida da monografia, sem tipos de vínculo, defasagens ou durações. N5.5 designa integração PTAX nesta tabela e também SDD na EAP. N5.6 não aparece como predecessor dos testes: incluir a validação do comparativo no planejamento. N3.2, N12.2 e N13.1 são referenciados, mas não têm suas próprias linhas de precedência. Essas lacunas impedem o uso da tabela como rede completa para cálculo do caminho crítico.

A tabela de precedência formaliza, para cada pacote de trabalho, seus predecessores imediatos e o tipo de dependência. O Quadro 10 apresenta a tabela de precedência dos pacotes do caminho principal do projeto, elaborada a partir das dependências obrigatórias identificadas; os pacotes não listados correspondem a atividades de apoio contínuo (comunicação, base de conhecimento e gestão de mudanças), executadas em paralelo ao longo de todo o ciclo e sem relação de precedência bloqueante.

**Quadro 10 — Tabela de precedência dos pacotes de trabalho**

| Pacote | Descrição | Predecessores Imediatos | Macro-Fase |
| --- | --- | --- | --- |
| N3.1 | Arquitetura da Solução | N2.1, N2.2, N2.3 | MF1 |
| N3.3 | Modelagem de Dados (DER) | N3.1 | MF1 |
| N4.1 | Seleção e Validação da Stack FOSS | N3.1 | MF1 |
| N4.2 | Repositório Git + CI/CD | N4.1 | MF1 |
| N4.3 | Setup Local e Homologação | N4.2 | MF1 |
| N5.1 | Backend — Lógica de Negócio | N3.3, N4.3 | MF2 |
| N5.2 | Backend — API de Câmbio + Cache | N5.1 | MF2 |
| N5.3 | Frontend — Interface e Simulações | N3.2, N5.1 | MF2 |
| N5.4 | Módulo PDF (WeasyPrint) | N5.1 | MF2 |
| N6.1 | Testes Unitários/Integração (≥ 80%) | N5.2, N5.3, N5.4 | MF2 |
| N6.2 | Testes de Aceitação (UAT) | N6.1 | MF2 |
| N7.1 | Pipeline CI (lint + testes) | N4.2, N6.1 | MF2 |
| N8.1 | Publicação em Produção | N6.2, N7.1 | MF2 |
| N8.2 | Documentação de Deploy + Rollback | N8.1 | MF2 |
| N12.1 | Documentação Técnica (Arquitetura, APIs) | N5.2, N8.1 | MF3 |
| N12.4 | Consolidação da Documentação Parcial | N12.1, N12.2 | MF3 |
| N13.2 | Verificação SMART | N8.1, N12.4 | MF3 |
| N13.3 | Apresentação Final + Aceite | N13.1, N13.2 | MF3 |
| N5.5 | Integração com a API do Banco Central (PTAX) | N5.2 | MF2 |
| N5.6 | Motor de Comparação de Provedores e Taxas | N5.5 | MF2 |

Fonte: elaborado pelos autores (2026).

## Fontes documentais

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.4.4 e respectivos quadros.
- [Termo de Abertura do Projeto v1_opngoing.docx](../../docx/Termo%20de%20Abertura%20do%20Projeto%20v1_opngoing.docx), objetivos, EAP, requisitos e restrições.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

A tabela deve explicar tanto a ordem de execução quanto a natureza do vínculo. Duas atividades podem depender do mesmo resultado sem depender uma da outra.

- [ ] Acrescentar código de atividade, descrição, duração, predecessora, vínculo, defasagem, justificativa e recurso.
- [ ] Distinguir término–início, início–início e término–término quando aplicáveis; adotar vínculos com base no trabalho real, sem encadear tudo artificialmente.
- [ ] Resolver predecessoras ausentes e incluir a validação do comparativo nos testes antes de calcular a rede.

**Entrega esperada:** Tabela consistente com o diagrama, sem referências a códigos inexistentes ou duplicados.
