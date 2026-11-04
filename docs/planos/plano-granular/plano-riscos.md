# 2.8 GERENCIAMENTO DOS RISCOS DO PROJETO

**Responsável pelo gerenciamento dos riscos:** Leonardo David Silva Setti (GP).
**Rastreabilidade ao TAP:** Seção "Riscos" (R1–R5) · Restrição de Riscos (sem contingência formal, dependência de APIs gratuitas) · Orçamento zero (reserva de contingência = R$ 0,00).
**Domínio PMBOK® 7ª:** Incerteza (com apoio dos Domínios de Medição e Planejamento).
**Princípios PMBOK® 7ª aplicados:** "Otimizar respostas aos riscos"; "Navegar na complexidade"; "Adotar adaptabilidade e resiliência"; "Reconhecer, avaliar e responder às interações do sistema".
**Processos PMBOK® 6ª (dicionário):** 11.1 Planejar · 11.2 Identificar · 11.3 Análise Qualitativa · 11.5 Planejar Respostas · 11.6 Implementar Respostas · 11.7 Monitorar os Riscos. A análise quantitativa (11.4) foi **dispensada** por GMV: não há base histórica nem orçamento para modelagem estatística.

O Domínio de Incerteza do PMBOK® 7ª vai além do "risco" tradicional. Ele inclui **ambiguidade** (requisitos e regras pouco claros), **complexidade** (muitas partes interagindo, como os 25 agentes de IA e a stack) e **volatilidade** (mudanças rápidas, como a cotação cambial e as regras de IOF). Como o projeto tem orçamento zero, as respostas se apoiam em **ações preventivas sem custo**: arquitetura (adapter, cache), processo (WIP, CI, revisão em pares) e flexibilidade de escopo.

### Metodologia

| Elemento | Definição |
| --- | --- |
| Identificação | Brainstorming nas retrospectivas, lista de verificação (riscos comuns), análise de premissas e restrições do TAP, lições aprendidas (LA-001) e auditorias |
| Registro | GitHub Issue com label `risk` (fonte de verdade) + quadro desta seção |
| Responsável (*owner*) | Cada risco tem um dono que monitora o gatilho e executa a resposta |
| Revisão | Quinzenal, na retrospectiva (risk backlog). Extraordinária quando um gatilho dispara |
| Escalonamento | Severidade CRÍTICA → Gestão de Mudanças (EAP N10) e, se afetar um marco, comunicação ao avaliador |

**Escala de Probabilidade (P)**

| Nível | Valor | Faixa |
| --- | --- | --- |
| Muito baixa | 1 | ≤ 10 % |
| Baixa | 2 | 11–30 % |
| Média | 3 | 31–50 % |
| Alta | 4 | 51–70 % |
| Muito alta | 5 | > 70 % |

**Escala de Impacto (I)**

| Nível | Valor | Efeito nos objetivos SMART |
| --- | --- | --- |
| Muito baixo | 1 | Insignificante, absorvido no fluxo |
| Baixo | 2 | Atraso < 2 dias ou retrabalho pequeno |
| Médio | 3 | Atraso de 2–5 dias ou perda de requisito *should* |
| Alto | 4 | Ameaça a um marco ou a um requisito *must* |
| Muito alto | 5 | Inviabiliza o MVP ou a aprovação acadêmica |

**Severidade = P × I** → 1–4 BAIXA · 5–9 MÉDIA · 10–15 ALTA · 16–25 CRÍTICA.

**Estratégias de resposta (PMBOK® 7ª):**
- Ameaças: **Evitar · Escalar · Transferir · Mitigar · Aceitar** (ativa ou passiva).
- Oportunidades: **Explorar · Escalar · Compartilhar · Melhorar · Aceitar**.
- Transferir quase nunca se aplica, porque não há orçamento para seguro ou terceirização.

---

## 2.8.1 Riscos Comuns

Riscos típicos de qualquer projeto de software acadêmico com equipe pequena, identificados por lista de verificação.

| ID | Risco (causa → evento → efeito) | Categoria | P | I | Sev. | Estratégia | Resposta | Owner | Gatilho |
| --- | --- | --- | :-: | :-: | :-: | --- | --- | --- | --- |
| RC-01 (R3 TAP) | Acúmulo de papéis e outras disciplinas → sobrecarga (burnout) → queda de produtividade ou afastamento | Equipe | 3 | 3 | 9 MÉDIA | Mitigar | WIP 3/pessoa; limite de 20 h/semana; self-report semanal; redistribuir cards | GP | > 20 h/semana por 2 semanas |
| RC-02 | Ausência de um membro (doença, trabalho, trancamento) → perda de capacidade → atraso | Equipe | 2 | 4 | 8 MÉDIA | Mitigar | Revisão em pares (conhecimento compartilhado); documentação ubíqua nos cards; nenhum módulo com um único conhecedor | GP | Membro sem daily por 3 dias |
| RC-03 | Inclusão de funcionalidades sem controle (*scope creep*) → sobrecarga → atraso no M3 | Escopo | 3 | 4 | 12 ALTA | Evitar | Escopo congelado (ADR-005); toda mudança via `change-request`; MoSCoW | GP | Backlog cresce > 15 % do original |
| RC-04 | Estimativas otimistas → cards maiores que o previsto → Cycle Time > 3 dias | Cronograma | 4 | 3 | 12 ALTA | Mitigar | Baseline de calibração; cards ≥ 6 h com tasklist (ADR-004); quebrar cards grandes | GP | Cycle Time > 3 dias por 2 semanas |
| RC-05 | Requisitos ambíguos (regras de spread/IOF, regimes) → implementação errada → retrabalho | Escopo / Incerteza (ambiguidade) | 3 | 3 | 9 MÉDIA | Mitigar | Critérios de aceite Given/When/Then; DoR exige regra de cálculo explícita; validação com usuário-piloto | Fabricio | Card devolvido no review por dúvida de regra |
| RC-06 | Falha de comunicação (decisões em canal informal) → informação perdida → retrabalho | Comunicações | 3 | 2 | 6 MÉDIA | Mitigar | Regra de registro em 24 h no GitHub (Plano 2.7) | GP | Decisão sem Issue detectada na retro |
| RC-07 (R4 TAP) | Pouco tempo para testes → coverage < 80 % → critério de qualidade não atendido | Qualidade | 3 | 4 | 12 ALTA | Mitigar | TDD; CI com `--cov-fail-under=80`; foco nos fluxos críticos | Edson | Coverage < 80 % no CI; < 70 % por 2 semanas = escalar |
| RC-08 | Perda ou corrupção de artefatos (reestruturação, `git add -A`, merge errado) → retrabalho | Tecnológico | 2 | 3 | 6 MÉDIA | Mitigar | Lição LA-001: branch dedicada, `git mv`, revisar a árvore antes do commit, tag de rollback | GP | Arquivo "sumido" ou 0 bytes no `main` |
| RC-09 | Desalinhamento entre documentação e código/realidade (*drift* documental) → reprovação na avaliação | Qualidade / Integração | 4 | 3 | 12 ALTA | Mitigar | Auditoria por marco; revisão cruzada dos planos; DoD inclui a documentação | GP | Auditoria aponta artefato prometido vazio (ex.: planos 6–8 com 0 B no GitHub) |
| RC-10 | Falta de experiência com a stack → curva de aprendizado → atraso na MF2 | Tecnológico | 2 | 3 | 6 MÉDIA | Mitigar | Protótipo "Hello World" (N4.1); fallback FastAPI → Flask | Fabricio | Card técnico parado > 3 dias |
| RC-11 | Segredo ou credencial commitado no repositório → incidente de segurança | Segurança | 2 | 4 | 8 MÉDIA | Evitar | `.gitignore`; só chaves *dummy* versionadas (Constituição 7.2); variáveis de ambiente | Todos | Revisão de PR / alerta do GitHub |
| RC-12 | Indisponibilidade do GitHub ou estouro da cota gratuita de Actions → CI parado | Externo | 1 | 2 | 2 BAIXA | Aceitar (ativa) | Rodar os testes localmente; reduzir os gatilhos do workflow | GP | Falha do CI por cota |

Fonte: Elaborado pelos autores (2026).

---

## 2.8.2 Riscos Específicos (do projeto)

Riscos ligados ao domínio do COGME (câmbio, tributação, geração de documentos, IA local, FOSS e LGPD).

| ID | Risco (causa → evento → efeito) | Categoria | P | I | Sev. | Estratégia | Resposta | Owner | Gatilho |
| --- | --- | --- | :-: | :-: | :-: | --- | --- | --- | --- |
| RE-01 (R5 TAP) | API PTAX do Banco Central (serviço Olinda) fica fora do ar ou muda o contrato OData → simulação (REQ-01) bloqueada | Externo / Tecnológico | 2 | 5 | 10 ALTA | Mitigar | *Adapter pattern* (provedor PTAX substituível); cache SQLite (REQ-07); mensagem clara de "cotação PTAX de [data/hora]" quando vier do cache | Fabricio | HTTP 4xx/5xx ou latência > 2 s em sequência |
| RE-14 | A PTAX é publicada em **boletins** (abertura, intermediários de hora em hora, fechamento) e **só em dias úteis** → não é "tempo real" no sentido estrito, o que conflita com a redação do REQ-01; nos fins de semana e feriados não há cotação do dia | Escopo / Incerteza (ambiguidade) | 5 | 3 | 15 ALTA | Mitigar | Redefinir o REQ-01 como "cotação oficial PTAX mais recente disponível"; buscar o último dia útil quando não houver boletim; mostrar o tipo de boletim e a data/hora; registrar em ADR (mudança de redação, não de escopo) | Fabricio | Consulta sem resultado em fim de semana ou feriado |
| RE-15 | A integração com a **Wise** (cotação e comparação de plataformas de pagamento internacional) **exige autenticação por token** (`/rates` retorna HTTP 401 `missing_token`; a Comparison API exige autenticação e "não deve ser usada em fluxos críticos") → pode não existir acesso gratuito para uso acadêmico, e o token passa a ser um segredo a proteger | Externo / Escopo | 4 | 3 | 12 ALTA | Evitar no MVP / Explorar depois | Manter a Wise **fora do caminho crítico do MVP** (prioridade *could*); avaliar no sandbox (`api.wise-sandbox.com`) com conta de teste; token só em variável de ambiente, nunca versionado (RC-11); exigir `change-request` + ADR antes de incluir | Fabricio | Decisão de incluir a Wise no escopo / pedido de criação de conta |
| RE-02 | Cotação em cache desatualizada é exibida como atual → usuário toma decisão com valor errado | Qualidade / Ético | 3 | 3 | 9 MÉDIA | Mitigar | TTL do cache definido; carimbo de data/hora na tela e no PDF; aviso de "simulação, não é cotação oficial" | Fabricio | Teste de TTL falha / reclamação no UAT |
| RE-03 | Erro de arredondamento (uso de `float` em vez de `Decimal`) → valores com centavos errados (REQ-03 exige 2 casas) | Qualidade | 3 | 4 | 12 ALTA | Evitar | Usar `Decimal` com arredondamento definido; testes com casos-limite e valores de referência calculados à mão | Edson | Divergência ≥ R$ 0,01 em teste |
| RE-04 | Mudança na legislação do IOF/câmbio durante o projeto → alíquota *hard-coded* fica errada | Externo / Volatilidade | 3 | 3 | 9 MÉDIA | Mitigar | Alíquotas configuráveis (não fixas no código), com fonte e data de vigência registradas; aviso de caráter simulado | Fabricio | Publicação de decreto que altera o IOF |
| RE-05 | WeasyPrint depende de bibliotecas nativas (Pango, Cairo/GTK) difíceis no Windows → PDF não gera em alguma máquina | Tecnológico | 3 | 3 | 9 MÉDIA | Mitigar | Documentar a instalação por SO; homologar em Linux/WSL; CI gerando o PDF como teste | Fabricio | Falha do teste de PDF / geração > 3 s (REQ-04) |
| RE-06 | Código gerado por LLM com erro lógico ou de segurança (alucinação) → defeito em produção | Tecnológico / Qualidade | 3 | 4 | 12 ALTA | Mitigar | Revisão humana obrigatória; testes antes do merge; prompts catalogados (REQ-13); coautoria declarada no commit | GP | Defeito rastreado até um trecho gerado por IA |
| RE-07 | LLM local (Qwen via llama.cpp, CPU) lento demais para o fluxo → produtividade cai | Recursos | 3 | 2 | 6 MÉDIA | Mitigar | Fallback para modelo menor (ex.: Qwen 14B); usar a IA só onde agrega valor | GP | Tempo de resposta inviável para o ciclo SDD |
| RE-08 | Complexidade da governança de agentes (Constituição, 25 agentes, 8 ondas) consome o tempo do produto → *overengineering* e atraso no MVP | Incerteza (complexidade) | 4 | 4 | 16 CRÍTICA | Mitigar / Escalar | Aplicar o teste GMV também aos agentes; congelar novas ondas até o M3; priorizar cards de produto (P0) | GP | Throughput de cards de produto < 3/semana |
| RE-09 | Dependência com licença não-OSI entra na stack → viola o critério FOSS (REQ-15) | Conformidade | 2 | 4 | 8 MÉDIA | Evitar | Auditoria de licenças (N4.4); whitelist/blacklist do Plano de Custos | Edson | Nova dependência no `requirements.txt` sem auditoria |
| RE-10 | Invoice em PDF contém dados pessoais (nome, CPF/CNPJ, endereço) armazenados sem base legal → não conformidade com a LGPD | Legal / Conformidade | 2 | 4 | 8 MÉDIA | Evitar | Minimização: não persistir PII, gerar o PDF sob demanda; dados fictícios nos testes e no UAT (Constituição 7.3) | GP | PII encontrada no SQLite ou em artefatos |
| RE-11 | SQLite com concorrência limitada → travamentos em uso simultâneo | Tecnológico | 1 | 2 | 2 BAIXA | Aceitar (passiva) | Aceito para MVP acadêmico (ADR-001); PostgreSQL fica para trabalhos futuros | Fabricio | — |
| RE-12 | Usuários-piloto pouco representativos (só colegas) → MVP aprovado, mas pouco útil para o público real | Partes interessadas | 3 | 2 | 6 MÉDIA | Aceitar (ativa) | Incluir ao menos 1 profissional PJ/freelancer real, se possível; registrar a limitação | Edson | — |
| RE-13 | Cobrança automática ou mudança de plano no provedor de API/hospedagem → custo ≠ R$ 0,00 | Custos | 1 | 3 | 3 BAIXA | Evitar | Só planos sem cartão cadastrado; alternativa FOSS/gratuita mapeada | GP | Aviso de cobrança do provedor |

Fonte: Elaborado pelos autores (2026).

### Oportunidades (riscos positivos)

| ID | Oportunidade | P | I | Estratégia | Ação |
| --- | --- | :-: | :-: | --- | --- |
| OP-01 | IA generativa local (SDD) acelera a produção de código e documentação | 4 | 4 | Explorar | Catalogar prompts que funcionaram; reutilizar especificações |
| OP-02 | O repositório público e organizado vira portfólio profissional dos membros | 4 | 3 | Melhorar | README completo, releases e demonstração |
| OP-03 | Contribuições da comunidade FOSS após a publicação (licença MIT) | 1 | 3 | Aceitar | Manter Issues abertas e um guia de contribuição |
| OP-04 | Reaproveitar a estrutura de governança (Constituição/agentes) em outros projetos acadêmicos | 2 | 2 | Compartilhar | Documentar o modelo como lição aprendida |
| OP-05 | Integrar APIs de empresas de pagamento internacional (começando pela Wise Comparison API) para comparar o custo real de recebimento entre plataformas, o que aumenta muito o valor para o público-alvo | 2 | 4 | Explorar (pós-MVP) | Prova de conceito no sandbox da Wise; o adapter de câmbio já prevê vários provedores |

Fonte: Elaborado pelos autores (2026).

**Risco encerrado:** R1 do TAP (entrega parcial do M1 em 22/09/2026 fora do prazo) **não se materializou**, porque o M1 foi entregue. Fica registrado como encerrado.
**R2 do TAP** (stack instável) foi incorporado em RC-10 e RE-05.

### Riscos materializados (questões) — evidência do Kanban em 25/10/2026

| ID | Questão | Risco de origem | Evidência | Ação proposta | Owner |
| --- | --- | --- | --- | --- | --- |
| Q-01 | **Marco M2 (30/09/2026) atrasado em ≈ 25 dias.** Faltam DER (#18) e Protótipo UX/UI (#17) em *Ready*, Setup Local (#21) e ADR-001 (#23) em *In review*, Auditoria de Licenças (#22) e Lições MF1 (#26) em *Backlog* | RC-04 (estimativas) / RC-01 (sobrecarga) | Milestone M2 aberta com 6 cards | Como o desvio passa de 3 dias úteis, abrir Issue `change-request` com novo prazo e registrar em ADR (Plano de Integração §1.9); priorizar #18 e #21 (P1/P2) | GP |
| Q-02 | **Nenhum card de construção (M3) no quadro**, faltando ≈ 3 semanas para 15/11/2026 | RC-03 / RE-08 | Milestones Calibração, M3 e M4 sem cards | Criar os cards N5.1–N5.4, N6.1–N6.2 e N7.1 na próxima reunião de terça | GP + equipe |
| Q-03 | **Planos 6–8 vazios no `main`** | RC-09 (drift documental) | Arquivos com 0 bytes no GitHub | Publicar estes documentos (2.6, 2.7, 2.8) | GP |
| Q-04 | **Atraso de uma semana (7 dias) na documentação do projeto** | RC-04 (estimativas otimistas) / RC-01 (sobrecarga) / RC-09 | Relato da equipe (25/10/2026) | Repriorizar os cards documentais na reunião de terça; aplicar o teste GMV para focar nos artefatos obrigatórios; dividir a redação por responsável (Recursos: Edson; Comunicações: Fabricio; Riscos: Leonardo) | GP |
| Q-05 | **Atraso de 5 dias no desenvolvimento do backend** | RC-04 (estimativas) / RC-10 (curva de aprendizado da stack) | Relato da equipe (25/10/2026); arquivos de `src/` ainda vazios no `main` | Quebrar os cards de backend (N5.1/N5.2) em partes menores, com tasklist (ADR-004); revisar a estimativa com base no tempo real gasto; acompanhar o Cycle Time na reunião de terça | Fabricio |

Fonte: Elaborado pelos autores (2026), com base no GitHub Projects do COGME.

> **Q-01 confirmada pela equipe em 25/10/2026:** o atraso do marco M2 fica registrado oficialmente como questão (risco materializado). Ela será acompanhada nas reuniões de terça até o encerramento da milestone M2, com o novo prazo definido via `change-request`.

> **Q-04 e Q-05 (relatadas pela equipe em 25/10/2026):** os dois atrasos confirmam que o risco **RC-04 (estimativas otimistas)** se materializou, e com ele a probabilidade de novos desvios no cronograma. Como passaram do limite de 3 dias úteis do Plano de Integração (§1.9), seguem o mesmo tratamento da Q-01: acompanhamento nas reuniões de terça e `change-request` quando afetarem um marco. Pela visão do PMBOK® 7ª (Domínio de Medição), os desvios reais vão servir de base para recalibrar as estimativas dos próximos cards.
>
> **Lição aprendida (MF2):** as estimativas iniciais de documentação e de backend foram otimistas. Daqui em diante, cada card estimado em mais de 6 h deve ser dividido, e a estimativa deve ser comparada com o tempo realmente gasto.

**Classificação do RE-08 confirmada:** a equipe concordou, em 25/10/2026, em manter o RE-08 (complexidade da governança de agentes) como risco **CRÍTICO** (P4 × I4 = 16). A resposta adotada é mitigar e escalar: aplicar o teste GMV também aos agentes, congelar novas ondas de agentes até o M3 e priorizar os cards de produto (P0).

---

## 2.8.3 Quadro de Riscos

### 2.8.3.1 Matriz Probabilidade × Impacto

| P \ I | 1 Muito baixo | 2 Baixo | 3 Médio | 4 Alto | 5 Muito alto |
| --- | --- | --- | --- | --- | --- |
| **5 Muito alta** | | | RE-14 | | |
| **4 Alta** | | | RC-04, RC-09, RE-15 | RE-08 | |
| **3 Média** | | RC-06, RE-07, RE-12 | RC-01, RC-05, RE-02, RE-04, RE-05 | RC-03, RC-07, RE-03, RE-06 | |
| **2 Baixa** | | | RC-08, RC-10 | RC-02, RC-11, RE-09, RE-10 | RE-01 |
| **1 Muito baixa** | | RC-12, RE-11 | RE-13 | | |

Legenda: 16–25 🟥 CRÍTICA · 10–15 🟧 ALTA · 5–9 🟨 MÉDIA · 1–4 🟩 BAIXA.
Fonte: Elaborado pelos autores (2026).

### 2.8.3.2 Ranking por Severidade (Top 10)

| # | ID | Risco resumido | Sev. | Estratégia | Owner | Status |
| --- | --- | --- | :-: | --- | --- | --- |
| 1 | RE-08 | Complexidade da governança de agentes vs. tempo do MVP | 16 🟥 | Mitigar/Escalar | GP | Aberto (classificação confirmada pela equipe) |
| 2 | RE-14 | PTAX por boletins / só dias úteis vs. "tempo real" do REQ-01 | 15 🟧 | Mitigar | Fabricio | Aberto |
| 3 | RE-15 | API Wise exige autenticação (não é pública) | 12 🟧 | Evitar no MVP | Fabricio | Em avaliação |
| 4 | RC-03 | Scope creep | 12 🟧 | Evitar | GP | Aberto |
| 5 | RC-04 | Estimativas otimistas | 12 🟧 | Mitigar | GP | **Materializado (Q-01, Q-04, Q-05)** |
| 6 | RC-07 | Coverage < 80 % | 12 🟧 | Mitigar | Edson | [A CONFIRMAR coverage atual] |
| 7 | RC-09 | Drift documental | 12 🟧 | Mitigar | GP | **Em tratamento** (planos 6–8 sendo publicados) |
| 8 | RE-03 | Erro de arredondamento | 12 🟧 | Evitar | Edson | Aberto |
| 9 | RE-06 | Defeito em código gerado por IA | 12 🟧 | Mitigar | GP | Aberto |
| 10 | RE-01 | API PTAX indisponível | 10 🟧 | Mitigar | Fabricio | Aberto |

Fonte: Elaborado pelos autores (2026).

### 2.8.3.3 Monitoramento e Controle

- **Ritual:** revisão do quadro na retrospectiva quinzenal (atualizar P, I, status, novos riscos).
- **Ferramenta:** cada risco ALTO ou CRÍTICO tem uma Issue com label `risk`, owner atribuído e milestone.
- **Indicadores:** nº de riscos abertos por severidade; nº de gatilhos disparados no período; % de riscos com owner (meta 100 %).
- **Reserva:** reserva de contingência financeira = R$ 0,00 (TAP). A "reserva" é de **escopo**: requisitos *should* e *could* podem ser cortados para proteger os *must*.

---

**Controle de Versões — Seção 2.8**

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 25/10/2026 | Emissão inicial: riscos comuns, específicos, oportunidades e quadro | Leonardo David Silva Setti |
