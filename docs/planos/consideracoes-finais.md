# 4 CONSIDERAÇÕES FINAIS

> Rascunho. Os trechos marcados **[A CONFIRMAR]** dependem dos resultados do M3 (15/11/2026) e do M4 (15/12/2026) e devem ser fechados no encerramento (EAP N12).

## 4.1 Síntese do Projeto

O projeto COGME — Conversor de Ganhos em Moeda Estrangeira — nasceu de uma dor concreta. Profissionais brasileiros que prestam serviços ao exterior precisam juntar cotações, spreads, IOF e documentos de cobrança em ferramentas espalhadas. O projeto propôs uma solução web única, gratuita e de código aberto para simular ganhos em USD/EUR convertidos em reais, comparar cinco regimes de contratação e emitir invoices em PDF.

Mais do que o produto, o projeto foi o meio de aplicar na prática a disciplina de Gerência de Projetos. Para isso, adotou um modelo de governança híbrido: o PMBOK® 7ª edição como base de princípios e domínios de desempenho, o PMBOK® 6ª edição como dicionário de processos e o Kanban no GitHub Projects como método de execução.

## 4.2 Atendimento aos Objetivos SMART

| Objetivo | Meta | Resultado | Situação |
| --- | --- | --- | --- |
| Produto | MVP com simulação, 5 regimes, spread/IOF e PDF, ≤ 3 s | [A CONFIRMAR] | Pendente |
| Qualidade | Coverage ≥ 80 %, UAT sem defeitos críticos | [A CONFIRMAR: coverage final ___ %; 118+ testes] | Pendente |
| Inovação | Stack 100 % FOSS + SDD com IA local | Stack FOSS definida (ADR-001); IA local via llama.cpp/Qwen; 25 agentes governados por Constituição | Pendente |
| Cronograma | M1 22/09 · M2 30/09 · M3 15/11 · M4 15/12 | M1 entregue; demais [A CONFIRMAR] | Pendente |
| Documentação | 8 planos + consolidação | Planos 1–5 no M1; planos 6–8 (Recursos, Comunicações, Riscos) concluídos nesta etapa | Pendente |

## 4.3 Aplicação do PMBOK® 7ª Edição

- **Domínio Partes Interessadas:** papéis definidos (GP como CCB de membro único, avaliador acadêmico sem interferir na operação) e um plano de comunicações com o GitHub como fonte única de verdade.
- **Domínio Equipe:** WIP limit e limite de 20 h semanais como proteção contra burnout; revisão em pares como forma de aprender junto.
- **Domínio Abordagem de Desenvolvimento e Ciclo de Vida:** escolha consciente de um fluxo contínuo adaptativo em três macro-fases, em vez de cascata ou de sprints.
- **Domínio Planejamento:** entrega faseada dos planos (M1 e M2) e Governança Mínima Viável (GMV) para evitar documentação sem valor.
- **Domínio Trabalho do Projeto:** cards autossuficientes, tasklists (ADR-004), Conventional Commits e base de conhecimento viva (OKB, ADRs, lições aprendidas).
- **Domínio Entrega:** Definition of Ready e Definition of Done, critérios de aceite mensuráveis para cada requisito.
- **Domínio Medição:** substituição formal do EVM, que não se aplica com orçamento zero, por métricas de fluxo (Cycle Time, Throughput, CFD), com período de calibração.
- **Domínio Incerteza:** registro de riscos comuns e específicos, respostas sem custo (adapter, cache, TDD) e gestão de oportunidades (IA generativa).

## 4.4 Principais Dificuldades e Lições Aprendidas

- **LA-001 (MF1):** reestruturar o repositório ao mesmo tempo que se produziam artefatos causou perda de arquivos. Ação preventiva: branch dedicada, `git mv` e janela de congelamento.
- **Drift documental:** a auditoria AUD-2610-02 mostrou que nem sempre o que é produzido localmente chega ao repositório oficial. Exemplo: os planos 6–8 estavam vazios no GitHub. Lição: o DoD precisa incluir "publicado no `main`".
- **Equilíbrio entre governança e produto:** a estrutura de governança com IA (Constituição, 25 agentes) trouxe rastreabilidade, mas também complexidade. Fica a lição de aplicar o teste GMV também às ferramentas de governança. **[A CONFIRMAR com a equipe]**
- **Estimativas otimistas (Q-04, Q-05):** houve atraso de uma semana na documentação e de 5 dias no backend. Lição: dividir os cards estimados em mais de 6 h e recalibrar as estimativas com o tempo realmente gasto (Domínio de Medição). **[A CONFIRMAR]** Outras lições da MF2: ___
- **[A CONFIRMAR]** Lições do UAT: ___

## 4.5 Limitações

- Validação com um número pequeno de usuários-piloto (3 a 5), pouco representativo do público real.
- Valores de spread e IOF são **simulados** e não substituem orientação contábil ou cotação oficial.
- SQLite e execução local limitam o uso simultâneo e a disponibilidade pública.

## 4.6 Trabalhos Futuros

- Hospedagem pública gratuita, para uso real.
- Comparação entre plataformas de recebimento internacional, a partir da Wise Platform API (Comparison/Rates). Depende de conta e token, porque a API não é pública (RE-15, OP-05).
- Suporte a mais moedas (GBP, CAD etc.) e histórico de cotações com gráficos.
- Cadastro de usuários e histórico de invoices, com conformidade total à LGPD.
- Migração para PostgreSQL, caso o uso aumente.

## 4.7 Conclusão

**[A CONFIRMAR — parágrafo de fechamento após o M4]** Sugestão: o projeto mostrou que é possível conduzir um projeto de software completo com orçamento zero, ferramentas 100 % livres e governança baseada no PMBOK® 7ª. Os princípios — foco em valor, adaptação ao contexto, qualidade incorporada e resposta otimizada aos riscos — se mostraram mais úteis para uma equipe pequena do que um conjunto rígido de processos.

> Redação: impessoal, como no restante do documento.
