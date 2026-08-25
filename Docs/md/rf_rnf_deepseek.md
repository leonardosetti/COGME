## 5. PRINCIPAIS REQUISITOS DAS PRINCIPAIS ENTREGAS/PRODUTOS

Com base na consolidação definitiva da arquitetura e na aplicação do princípio **KISS Profissional**, esta seção estabelece os requisitos de alto nível que orientarão todo o desenvolvimento do **MVP (Produto Mínimo Viável)** do sistema COGME. 

Os requisitos aqui descritos refletem as decisões irremovíveis sobre a stack tecnológica (FastAPI + PostgreSQL + Redis + WeasyPrint + Vite/Alpine.js), o modelo de negócio (apenas Jornada por Hora e Mensal Fixo) e as premissas de segurança (JWT em Cookie HttpOnly). Todo item está rigorosamente alinhado às restrições documentadas na Seção 8 e ao cronograma apertado (2 bimestres, equipe de 2 pessoas).

---

### 5.1. VISÃO GERAL DOS REQUISITOS

O sistema COGME será uma aplicação *web* monocontainer (em desenvolvimento) e multicontainer (em produção) que permite ao usuário:

- Gerenciar seu perfil e configuração de ganhos em moeda estrangeira.
- Simular em tempo real (com cache) a conversão de seus rendimentos para Real Brasileiro (BRL), considerando *spread* bancário e IOF.
- Criar, gerenciar e finalizar faturas (*invoices*) com base nos regimes de contratação.
- Exportar as faturas finalizadas em formato PDF com alta fidelidade visual.

**Escopo do MVP vs. Backlog (Cortes Explícitos):**
- ❌ **Fora do MVP:** Gráficos de evolução cambial, exportação para DOCX, comparador de múltiplas plataformas (Wise, Remessa), jornadas por Dia/Semana/Ano, e painel administrativo multi-usuário.
- ✅ **Dentro do MVP:** Simulação com Spread/IOF, gestão de invoices com status ("Rascunho"/"Finalizada"), clonagem atômica, e geração de PDF via backend.

---

### 5.2. REQUISITOS FUNCIONAIS (RF)

#### Módulo 1: Autenticação e Segurança (RF-01 a RF-04)
| **ID** | **Requisito** | **Critério de Aceitação / Detalhamento Técnico** |
| :--- | :--- | :--- |
| **RF-01** | O sistema deve permitir o cadastro de novos usuários com nome, e-mail, senha (hash bcrypt) e dados bancários iniciais (opcionais no cadastro). | O e-mail deve ser único. A senha deve ter tamanho mínimo de 8 caracteres. O banco de dados deve armazenar o hash gerado pelo `bcrypt` com fator de custo 12. |
| **RF-02** | O sistema deve realizar login utilizando e-mail e senha, emitindo um JWT (JSON Web Token) armazenado em cookie **HttpOnly**, `Secure` e `SameSite=Lax`. | O token deve ter expiração de **1 hora**. O backend deve ler o token exclusivamente pelo cookie (`request.cookies.get('access_token')`) e não pelo cabeçalho `Authorization`. O front-end (Axios) deve utilizar `withCredentials: true`. |
| **RF-03** | O sistema deve permitir logout, invalidando a sessão no front-end (limpeza de estado) e, idealmente, removendo o cookie no backend. | O logout deve redirecionar o usuário para a tela de login. O cookie deve ser deletado ou sobrescrito com data de expiração passada. |
| **RF-04** | Todas as rotas protegidas (exceto `/login` e `/register`) devem validar o JWT recebido via cookie e retornar **HTTP 401 Unauthorized** em caso de token inválido ou expirado. | Implementar middleware no FastAPI que injete o `user_id` na requisição. Aplicar Rate Limiting (`slowapi`) de **5 tentativas/minuto** na rota de login para mitigar ataques de força bruta. |

---

#### Módulo 2: Perfil e Configuração de Jornada (RF-05 a RF-07)
| **ID** | **Requisito** | **Critério de Aceitação / Detalhamento Técnico** |
| :--- | :--- | :--- |
| **RF-05** | O usuário deve poder editar seus dados pessoais, bancários (Beneficiary Name, Account, Routing, Bank Address) e sua **jornada de trabalho padrão**. | A jornada deve ser restrita a apenas duas opções: <br> *(a)* **Por Hora**: definir `hourly_rate` (valor) e moeda (USD/EUR/GBP). <br> *(b)* **Mensal Fixo**: definir `monthly_salary` (valor) e moeda. <br> *Não serão aceitos valores negativos.* |
| **RF-06** | O sistema deve persistir a configuração de jornada no banco de dados, vinculada ao `user_id`, e carregá-la automaticamente ao criar uma nova Invoice. | Os campos de valor e moeda devem ser pré-preenchidos no formulário de criação de Invoice. |
| **RF-07** | O usuário deve poder simular cenários de ganho **sem vincular à sua jornada padrão** (simulação avulsa). | Na tela de simulação, o usuário insere valor, moeda de origem, e percentuais de Spread/IOF (valores default, mas editáveis). O resultado em BRL deve ser exibido em tempo real (após debounce). |

---

#### Módulo 3: Câmbio, Cálculo e Cache (RF-08 a RF-10)
| **ID** | **Requisito** | **Critério de Aceitação / Detalhamento Técnico** |
| :--- | :--- | :--- |
| **RF-08** | O sistema deve consumir a **Frankfurter API** (`https://api.frankfurter.dev/v1/latest`) para obter a cotação atual das moedas permitidas (USD, EUR, GBP) em relação ao BRL. | A API deve ser consultada **assincronamente** com `httpx`. Em caso de falha (timeout ou 5xx), o sistema deve tentar novamente com backoff exponencial (biblioteca `tenacity` com `stop_after_attempt=3` e `wait_exponential`). |
| **RF-09** | O sistema deve armazenar as cotações em **cache Redis** com **TTL de 300 segundos (5 minutos)**. | A chave do cache deve ser a moeda de origem (ex: `USD_BRL`). Se o cache estiver vazio, a API Frankfurter é chamada e o Redis é atualizado. O Redis deve ter persistência ativada via volume Docker para evitar perda total em caso de reinício. |
| **RF-10** | A lógica de cálculo da simulação deve aplicar a fórmula: `(Valor * Cotação) * (1 + Spread%) * (1 + IOF%)`. | O Spread e o IOF devem ser editáveis pelo usuário (valores default: Spread = 1.5%, IOF = 1.1%). O cálculo deve ser feito no **backend** e retornado via JSON para evitar inconsistências. |

---

#### Módulo 4: Gestão de Invoices (RF-11 a RF-16)
| **ID** | **Requisito** | **Critério de Aceitação / Detalhamento Técnico** |
| :--- | :--- | :--- |
| **RF-11** | O sistema deve permitir a criação de uma Invoice a partir dos dados do perfil (jornada e dados bancários) e de um período de trabalho (data de início e fim, **não retroativas**). | A `data_inicio` e `data_fim` devem ser validadas pelo Pydantic no backend. Datas anteriores ao dia atual (`date.today()`) devem ser rejeitadas com erro HTTP 422. O front-end deve desabilitar datas passadas no input `type="date"` usando `min`. |
| **RF-12** | Cada Invoice deve conter: ID único, Número Sequencial (`invoice_number`), dados do usuário (nome, CPF/CNPJ), dados da empresa, detalhamento do serviço (jornada), valores em moeda estrangeira e em BRL, status, data de emissão (UTC). | O **número sequencial** (`invoice_number`) deve ser gerado automaticamente pelo banco de dados utilizando **`CREATE SEQUENCE`** para garantir unicidade atômica e evitar race conditions no código Python. |
| **RF-13** | A Invoice deve possuir **apenas dois status**: `DRAFT` (Rascunho) e `FINALIZED` (Finalizada). | No status `DRAFT`, todos os campos são editáveis. Ao mudar para `FINALIZED`, a Invoice torna-se **read-only**. Não há status intermediários. |
| **RF-14** | O sistema deve permitir a **clonagem** de uma Invoice. | A clonagem deve: (1) Ler os dados da Invoice original; (2) Criar um novo registro; (3) Atribuir um **novo número sequencial** (próximo valor da Sequence); (4) Definir a data de emissão como `date.today()`; (5) Resetar o status para `DRAFT`. Este deve ser um endpoint dedicado (`POST /invoices/{id}/clone`). |
| **RF-15** | O sistema deve exibir uma lista paginada das Invoices do usuário, ordenadas por data de criação (mais recentes primeiro). | A lista deve exibir: Número da Invoice, Data, Status, Valor Total (em BRL), e botões de ação (Visualizar/Editar/Clonar). |
| **RF-16** | Invoices no status `FINALIZED` devem ter o botão "Editar" oculto/desabilitado, permitindo apenas Visualização, Clonagem e Download do PDF. | Validar no backend que nenhuma rota de `PUT/PATCH` aceite edição de uma Invoice com status `FINALIZED`. |

---

#### Módulo 5: Exportação e PDF (RF-17 a RF-18)
| **ID** | **Requisito** | **Critério de Aceitação / Detalhamento Técnico** |
| :--- | :--- | :--- |
| **RF-17** | O sistema deve gerar um arquivo **PDF** a partir da Invoice finalizada. | A geração deve ser feita no **backend** utilizando **WeasyPrint**. O template HTML da visualização da Invoice deve ser reutilizado para compor o PDF (WYSIWYG). O PDF deve conter layout profissional (dados bancários, valores, instruções de wire transfer). |
| **RF-18** | O sistema deve possuir um endpoint `/warmup` (ou similar) que pré-carrega as bibliotecas do WeasyPrint (Cairo/Pango) no momento em que o container sobe. | Este endpoint deve ser chamado no `entrypoint.sh` do container ou via healthcheck do Docker Compose, para evitar o "Cold Start" (atraso de até 20s) na primeira geração de PDF. |

---

### 5.3. REQUISITOS NÃO FUNCIONAIS (RNF)

| **ID** | **Requisito** | **Critério de Aceitação / Detalhamento Técnico** |
| :--- | :--- | :--- |
| **RNF-01** | **Performance:** O endpoint de simulação de câmbio deve responder em menos de **3 segundos** (95º percentil). | Medido em ambiente de homologação com cache Redis ativo. O cold start da API Frankfurter é mitigado pelo cache. |
| **RNF-02** | **Segurança:** As senhas dos usuários devem ser armazenadas utilizando bcrypt (fator de custo 12). | O JWT deve ser transmitido exclusivamente via cookie `HttpOnly`. Todos os endpoints (exceto `/docs` e `/openapi.json`) devem exigir autenticação. O Rate Limiting deve proteger rotas públicas contra brute force. |
| **RNF-03** | **Portabilidade:** 100% do código e infraestrutura devem ser **FOSS** e executados via `docker-compose up`. | O projeto deve funcionar em qualquer máquina com Docker e Docker Compose instalados. As licenças de todas as dependências (Python, Node.js, NPM) devem ser compatíveis com MIT/BSD/Apache. |
| **RNF-04** | **Qualidade e Testes:** O código-fonte deve atingir **cobertura mínima de 80%** em testes unitários (Pytest). | O pipeline de CI/CD (GitHub Actions) deve executar os testes a cada push e bloquear o merge em caso de falha ou cobertura abaixo de 80%. |
| **RNF-05** | **Timezone:** Todas as datas e horários devem ser armazenados no banco de dados em **UTC (`TIMESTAMP WITH TIME ZONE`)**. | A conversão para o fuso horário do usuário (ex: `America/Sao_Paulo`) deve ocorrer exclusivamente na camada de exibição (Front-end/Alpine.js). A API deve retornar datas no formato ISO 8601 com sufixo `Z`. |
| **RNF-06** | **Disponibilidade:** O sistema deve estar disponível em uma URL pública durante as apresentações (Dez/2026). | Implementar script de **Keep-Alive** (ex: UptimeRobot ou GitHub Actions agendado) que chama o endpoint `/health` a cada 14 minutos para evitar que o container (em plataformas gratuitas) entre em modo "sleep". |
| **RNF-07** | **Manutenibilidade:** O código deve seguir padrões de Clean Code e estar documentado via OpenAPI (Swagger) automaticamente gerado pelo FastAPI. | A equipe de 2 pessoas deve conseguir compreender e modificar qualquer parte do sistema sem auxílio externo. |
| **RNF-08** | **Licenciamento:** O projeto final deve ser auditado para garantir que nenhuma dependência com licença restritiva (ex: GPL com cláusula de copyleft forte para uso comercial) seja utilizada. | Gerar relatório de licenças (`pip-licenses` e `license-checker`) na entrega final. |

---

### 5.4. CRITÉRIOS DE ACEITAÇÃO DAS PRINCIPAIS ENTREGAS (ALTO NÍVEL)

| **Entregável / Módulo** | **Critério de Aceitação (Condições para ser aprovado)** |
| :--- | :--- |
| **Autenticação e Perfil** | O usuário consegue se cadastrar, fazer login (recebendo o cookie JWT), acessar rotas protegidas, editar seus dados e fazer logout. O Login com senha incorreta deve retornar erro 401 e bloquear após 5 tentativas em 1 minuto. |
| **Simulação de Câmbio** | O usuário insere um valor e percentuais, e o sistema retorna o valor convertido em BRL em menos de 3 segundos. O Redis deve armazenar a cotação por 5 minutos. Se a Frankfurter API falhar, o sistema deve tentar até 3 vezes e retornar um erro amigável (não quebrar com 500). |
| **Criação e Gestão de Invoice** | O usuário cria uma Invoice (data não retroativa, jornada baseada no perfil). Edita enquanto `DRAFT`. Finaliza e a Invoice torna-se read-only. O Clone gera um novo número sequencial e nova data, resetando para `DRAFT`. |
| **Geração de PDF** | O PDF é gerado com layout idêntico ao HTML, contendo todos os dados bancários e valores. A primeira geração não deve demorar mais que 5 segundos (garantido pelo `/warmup`). |
| **Auditoria FOSS** | O relatório de dependências não apresenta licenças incompatíveis. A stack é 100% FOSS conforme documentado. |

---

**Nota Final:** Os requisitos listados nesta seção constituem a **baseline de escopo** do projeto, conforme definido pela *Declaração de Escopo* (a ser detalhada no Plano de Gerenciamento de Escopo). Qualquer solicitação de alteração que adicione, remova ou modifique significativamente estes itens deverá ser formalizada por meio de uma **Solicitação de Mudança** e aprovada pelo patrocinador (professor orientador). O foco da equipe deve ser 100% na entrega destes requisitos até os marcos estabelecidos no cronograma.
