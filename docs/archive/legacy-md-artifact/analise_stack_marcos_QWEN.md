Este é o **Confronto Final e a Síntese Definitiva**. 

Após colocar a "Análise 1" (Minimalismo Extremo) e a "Análise 2" (Robustez Profissional) lado a lado, e cruzando com a realidade do hardware disponível (32GB a 60GB de RAM, CPUs modernas) e as restrições inegociáveis do TAP (2 pessoas, FOSS, SDD com IA, prazo até Dezembro/2026, marco em 08/09/2026), chegamos à verdade absoluta do projeto.

A filosofia que guia esta síntese é o **KISS Profissional**: *KISS não significa usar ferramentas amadoras ou criar gambiarras para "economizar" recursos que já temos de sobra. KISS significa escolher a ferramenta padrão da indústria que resolve o problema com a menor quantidade de código customizado, menor taxa de bugs e maior compatibilidade com geração por IA (SDD).*

Abaixo está o caminho ótimo integral para o COGME.

---

### 1. ANÁLISE DEFINITIVA: O BATIMENTO (Decisões Irrevogáveis)

| Ponto de Conflito | Decisão Final (Caminho Ótimo) | Justificativa (Por que esta é a escolha definitiva?) |
| :--- | :--- | :--- |
| **Cache de Câmbio** | **Redis 7 (Container)** | A "tabela no Postgres" exige lógica customizada de cron/verificação. O `lru_cache` falha em múltiplos workers do FastAPI. Com 32GB+ de RAM, um container Redis consome 50MB, resolve o problema nativamente, é padrão de mercado e a IA sabe configurá-lo perfeitamente. |
| **Geração de PDF** | **WeasyPrint (Backend)** | Bibliotecas de PDF no frontend (`html2pdf.js`) falham miseravelmente em quebras de página, tabelas longas e fidelidade de impressão. WeasyPrint garante WYSIWYG. O "Cold Start" é resolvido com um endpoint `/warmup` no boot. |
| **Autenticação** | **JWT em Cookie `HttpOnly`** | `localStorage` é vulnerável a XSS. Configurar CORS com `credentials: true` no FastAPI leva 15 minutos. Prevenir um roubo de token vale infinitamente mais do que a "facilidade" do localStorage em um projeto acadêmico que será avaliado por critérios de qualidade. |
| **Front-end Build** | **Vite + Tailwind + Alpine.js** | Bootstrap CDN é fácil, mas Tailwind + Vite é o padrão moderno. O Vite é instantâneo (HMR em milissegundos). A IA gera código Tailwind/Alpine com altíssima precisão. Não há "configuração complexa", apenas `npm create vite@latest`. |
| **Modelos de Jornada** | **Apenas "Valor por Hora" e "Mensal Fixo"** | Elimina a "inferno dos calendários" (feriados, dias úteis, semanas). O cálculo é puramente aritmético (`valor * quantidade`), garantindo previsibilidade e zero bugs lógicos no MVP. |
| **Numeração de Invoice** | **Sequences do PostgreSQL** | Resolver a condição de corrida (Race Condition) na clonagem de invoices no código Python é propenso a erros. Usar `CREATE SEQUENCE` no banco garante unicidade atômica e ACID, delegando a responsabilidade a quem sabe fazer isso melhor. |

---

### 2. STACK TECNOLÓGICA DEFINITIVA (Blindada e Justificada)

Esta stack foi escolhida por ser **100% FOSS**, ter **curva de aprendizado mínima para SDD com IA** e oferecer **robustez de produção** sem exigir esforço hercúleo da equipe de 2 pessoas.

*   **Front-end**: Vite (Build) + HTML5 + Tailwind CSS (Estilização) + Alpine.js (Reatividade leve via CDN ou NPM) + Axios (HTTP com `withCredentials: true`).
*   **Back-end**: Python 3.12 + FastAPI (Roteamento, Validação Pydantic, OpenAPI auto-gerada) + `slowapi` (Rate Limiting) + `tenacity` (Retries resilientes).
*   **Banco de Dados**: PostgreSQL 16 (ACID, JSONB para metadados, Sequences para numeração de invoices).
*   **Cache**: Redis 7 (Persistência via volume Docker, TTL 300s para cotações).
*   **PDF**: WeasyPrint (Python) + Endpoint `/warmup` para pré-carregamento de libs (Cairo/Pango) no startup do container.
*   **Infraestrutura**: Docker Compose (4 serviços: `frontend` [Nginx em prod], `backend`, `db`, `cache`).
*   **DevOps**: GitHub Actions (CI: Lint + Pytest; CD: Build e Push da imagem Docker).

---

### 3. ESCOPO: O QUE É MVP vs. O QUE É DESEJÁVEL (Backlog)

Para salvar o prazo de 08/09/2026 e a entrega final, o escopo deve ser cirúrgico.

#### ✅ MVP (Essencial para o Sucesso / Nota Máxima)
1.  **Autenticação**: Cadastro, Login (JWT HttpOnly), Logout e Edição de Perfil (Dados pessoais e bancários).
2.  **Configuração de Jornada**: Definir apenas "Valor por Hora" ou "Salário Mensal Fixo" e moeda (USD, EUR, GBP).
3.  **Simulação de Câmbio**: Input de valor, aplicação de Spread (%) e IOF (%), exibição do resultado em BRL em < 3 segundos (usando cache Redis).
4.  **Gestão de Invoices**: Criar, Listar, Visualizar. Status: "Rascunho" (editável) e "Finalizada" (read-only).
5.  **Clonagem de Invoice**: Botão que duplica os dados de uma invoice finalizada para um novo "Rascunho" com nova data e novo número sequencial (via DB Sequence).
6.  **Exportação PDF**: Geração de arquivo PDF formatado a partir da invoice finalizada.

#### ⏳ Backlog / Desejável (Cortar do MVP sem dó)
1.  **Gráficos de Evolução Cambial**: Substituir por um link externo para o BCB ou uma tabela simples dos últimos 5 dias. Gráficos consomem tempo desproporcional.
2.  **Exportação DOCX/Word**: Manter apenas PDF. DOCX exige manipulação de templates complexa e falha em formatação.
3.  **Múltiplas Plataformas de Câmbio (Wise, Remessa)**: O MVP foca na simulação genérica com Spread/IOF. Comparadores de plataformas são complexidade de negócio desnecessária agora.
4.  **Jornadas por Dia/Semana/Ano**: Como decidido, apenas Hora e Mês.
5.  **Painel Administrativo Multi-usuário**: O sistema é single-tenant por usuário logado. Não há "admin" que vê todos os usuários.

---

### 4. GAPS E PONTOS CEGOS REFINADOS (Checklist de Sobrevivência)

Estes são os erros que derrubam o projeto na semana da apresentação. A equipe deve ter estes itens marcados como "Resolvidos" antes da codificação pesada.

1.  **Gap do CORS Silencioso**: Ao usar cookies `HttpOnly`, o Axios *precisa* de `withCredentials: true` e o FastAPI *precisa* de `allow_credentials=True` no middleware. Testar isso no **Dia 1** do desenvolvimento.
2.  **Gap do Timezone (UTC)**: O banco de dados *deve* salvar tudo em UTC. O Pydantic deve serializar com o sufixo `Z` (ex: `2026-09-08T15:00:00Z`). O Alpine.js no front-end é o único responsável por formatar isso para `America/Sao_Paulo` na tela.
3.  **Gap da Clonagem Concorrente**: Garantir que o endpoint de clonagem não aceita um `invoice_number` manual, mas sim deixa o PostgreSQL gerar o próximo via `NEXTVAL('invoice_seq')`.
4.  **Gap do Warmup do PDF**: O script de entrada do container do backend (`entrypoint.sh`) deve chamar `curl http://localhost:8000/warmup` antes de declarar o serviço como "healthy" no Docker Compose.
5.  **Gap da API Frankfurter**: Implementar `tenacity` com `stop_after_attempt=3` e `wait_exponential` nas chamadas à API. Se falhar, retornar a última cotação do Redis com um aviso visual "Cotação com X minutos de atraso".

---

### 5. MARCOS DO PROJETO (CHECKPOINTS OBRIGATÓRIOS)

Considerando a data atual (**26 de agosto de 2026**), o foco absoluto até 08/09 é a documentação. A codificação roda em paralelo, mas a burocracia acadêmica é o gargalo imediato.

#### 🚩 FASE 1: Sobrevivência Acadêmica e Fundação (Até 08/09/2026)
*   [ ] **CP-01 (29/08)**: TAP, EAP, Planos de Escopo, Cronograma, Custo, Riscos e Qualidade revisados e prontos para entrega.
*   [ ] **CP-02 (02/09)**: Repositório GitHub criado, GitHub Projects (Kanban) configurado, README.md com instruções de `docker-compose up`.
*   [ ] **CP-03 (05/09)**: "Hello World" Dockerizado. Os 4 containers (Front, Back, DB, Redis) sobem sem erros. FastAPI responde `/docs` e `/health`.
*   [ ] **CP-04 (08/09)**: **ENTREGA PARCIAL FORMAL**. Documentação submetida. Contrato de API (JSON de exemplo de Login e Simulação) definido e acordado entre os 2 desenvolvedores.

#### 🚩 FASE 2: Núcleo do MVP (Até meados de Outubro/2026)
*   [ ] **CP-05 (20/09)**: Autenticação funcional. Cadastro, Login com Cookie HttpOnly e validação de rotas protegidas.
*   [ ] **CP-06 (04/10)**: Motor de Câmbio Resiliente. Integração Frankfurter + Cache Redis + Fallback de erro tratado.
*   [ ] **CP-07 (18/10)**: CRUD de Perfil e Jornada (apenas Hora/Mês) com validação de datas não retroativas.

#### 🚩 FASE 3: O Coração do Negócio (Até meados de Novembro/2026)
*   [ ] **CP-08 (01/11)**: Gestão de Invoices. Criação, listagem, transição de status (Rascunho -> Finalizada) e lógica de Clonagem com Sequence do DB.
*   [ ] **CP-09 (15/11)**: Pipeline de PDF. Endpoint `/warmup` validado. Geração de PDF via WeasyPrint com layout idêntico ao HTML.

#### 🚩 FASE 4: Qualidade, Endurecimento e Deploy (Até início de Dezembro/2026)
*   [ ] **CP-10 (22/11)**: Cobertura de Testes ≥ 80% (Pytest) rodando no GitHub Actions. Bloqueio de merge em caso de falha.
*   [ ] **CP-11 (29/11)**: Deploy em ambiente público (ex: Railway, Render ou VPS gratuita). Script de Keep-Alive configurado.
*   [ ] **CP-12 (06/12)**: Auditoria FOSS (`pip-licenses`, verificação de licenças NPM) e Documentação Técnica/Manual do Usuário finalizados.

#### 🚩 FASE 5: Encerramento (Até meados de Dezembro/2026)
*   [ ] **CP-13 (13/12)**: UAT (Testes de Aceitação) com usuários-piloto (colegas/professor) sem defeitos críticos.
*   [ ] **CP-14 (15/12)**: Apresentação Final. Demo ao vivo com vídeo de fallback gravado.

---

### CONCLUSÃO DO GERENTE DE PROJETOS

O confronto está encerrado. A "Análise 1" tinha razão sobre a necessidade de simplificar a *lógica de negócio* (cortar jornadas complexas e gráficos). A "Análise 2" tinha razão sobre a necessidade de *robustez técnica* (Redis, HttpOnly, WeasyPrint), pois o hardware disponível torna o custo dessas ferramentas próximo de zero, enquanto o custo de debugar as alternativas "gambiarra" seria altíssimo.

**Esta é a arquitetura final.** Ela é defensável academicamente, alinhada ao PMBOK, viável para 2 pessoas em 3 meses e utiliza o SDD com IA da forma mais eficiente possível (ferramentas padrão de mercado sobre as quais a IA foi massivamente treinada).

**Próximo passo imediato da equipe**: Congelar este documento como a "Bíblia Técnica" do projeto e iniciar a execução do **CP-01 a CP-04** com foco total na entrega documental de 08/09/2026. 

Deseja que eu gere agora a **Seção 5 do TAP (Requisitos Funcionais e Não Funcionais)** formatada exatamente com as regras de negócio e restrições técnicas que acabamos de consolidar?
