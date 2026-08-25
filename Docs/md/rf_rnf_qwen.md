Com base em todo o confronto de análises, na validação da stack tecnológica "à prova de balas" e nas restrições inegociáveis do TAP (PMBOK 6ª ed., FOSS, equipe de 2 pessoas, prazo até 08/09/2026 para a primeira entrega e KISS absoluto), apresento a **Seção 5 do Termo de Abertura do Projeto (TAP)** totalmente formatada e pronta para ser inserida no documento.

Esta seção traduz as decisões arquiteturais e de negócio em requisitos auditáveis, servindo como a "bíblia" para o desenvolvimento assistido por IA (SDD) e para os testes de aceitação.

---

### 5. PRINCIPAIS REQUISITOS DAS PRINCIPAIS ENTREGAS/PRODUTOS

Esta seção define os requisitos funcionais (RF), não funcionais (RNF) e as regras de negócio (RN) que compõem o escopo do Minimum Viable Product (MVP) do sistema COGME. Estes requisitos foram elaborados em estrita conformidade com as premissas de uso exclusivo de tecnologias FOSS, princípio KISS, e arquitetura em containers.

#### 5.1. Requisitos Funcionais (RF)
Os requisitos funcionais descrevem as capacidades que o sistema deve possuir para atender às necessidades do usuário, agrupados por módulos lógicos.

| ID | Módulo | Descrição do Requisito | Critério de Aceitação (Definition of Done) |
| :--- | :--- | :--- | :--- |
| **RF-01** | Autenticação | O sistema deve permitir o cadastro de novos usuários com e-mail e senha. | A senha deve ser armazenada no banco de dados utilizando hashing `bcrypt` (fator de custo ≥ 12). |
| **RF-02** | Autenticação | O sistema deve realizar a autenticação do usuário e gerenciar a sessão via token JWT. | O token JWT deve ser armazenado exclusivamente em um **Cookie com atributos `HttpOnly`, `Secure` e `SameSite=Lax`**. O front-end não deve ter acesso ao token via JavaScript. |
| **RF-03** | Perfil | O sistema deve permitir que o usuário edite seus dados pessoais e bancários (Nome, CPF/CNPJ, Endereço, Dados para Wire Transfer). | Os dados devem ser persistidos no PostgreSQL e validados quanto ao formato antes do salvamento. |
| **RF-04** | Jornada | O sistema deve permitir que o usuário configure seu modelo de remuneração, restrito a duas modalidades: **"Valor por Hora"** ou **"Salário Mensal Fixo"**, associando uma moeda de origem (USD, EUR ou GBP). | O sistema deve rejeitar qualquer tentativa de configuração de jornadas por dia, semana ou ano (fora do escopo do MVP). |
| **RF-05** | Câmbio | O sistema deve exibir a cotação atual da moeda configurada em relação ao BRL. | A cotação deve ser obtida da API Frankfurter. Se a API falhar, o sistema deve retornar a última cotação válida armazenada no cache (Redis) com um aviso visual de "dados com defasagem". |
| **RF-06** | Simulação | O sistema deve permitir simulações avulsas de conversão, aplicando percentuais customizados de **Spread** e **IOF** sobre o valor bruto. | O cálculo deve ser processado e exibido na interface em **menos de 3 segundos**. A fórmula deve ser: `(Valor Bruto × Cotação) - IOF - Spread`. |
| **RF-07** | Invoice | O sistema deve permitir a criação de uma Invoice a partir do modelo de jornada configurado, definindo período (Data Início e Data Fim) e permitindo a inclusão de valores extras (Bônus, Horas Extras). | A Data Início e Data Fim não podem ser retroativas em relação à data atual do sistema. |
| **RF-08** | Invoice | O sistema deve gerenciar o ciclo de vida da Invoice através de dois estados: **"Rascunho"** (editável) e **"Finalizada"** (somente leitura). | Uma vez alterada para "Finalizada", nenhum campo da Invoice pode ser modificado, exceto através da função de clonagem. |
| **RF-09** | Invoice | O sistema deve permitir a **clonagem** de uma Invoice "Finalizada" para criar um novo "Rascunho". | A nova Invoice deve receber automaticamente um **novo número sequencial único** (gerado via Sequence do PostgreSQL) e a data de emissão deve ser atualizada para a data atual. |
| **RF-10** | Exportação | O sistema deve gerar e permitir o download da Invoice no formato **PDF**. | O PDF gerado deve manter a fidelidade visual idêntica à pré-visualização HTML na tela, incluindo todos os dados do contratante, contratado, período, cálculos e dados bancários. |

#### 5.2. Requisitos Não Funcionais (RNF)
Os requisitos não funcionais definem as restrições de qualidade, desempenho, segurança e infraestrutura que o sistema deve obedecer.

| ID | Categoria | Descrição do Requisito | Métrica / Critério de Validação |
| :--- | :--- | :--- | :--- |
| **RNF-01** | **Tecnológica (FOSS)** | 100% das linguagens, frameworks, bibliotecas, ferramentas de CI/CD e imagens de container devem possuir licenças aprovadas pela OSI (ex: MIT, BSD, Apache 2.0, PostgreSQL). | Auditoria via `pip-licenses` (Back) e `license-checker` (Front) no pipeline de CI. Qualquer licença restritiva (ex: AGPL) bloqueará o merge. |
| **RNF-02** | **Performance** | O tempo de resposta para qualquer requisição à API RESTful (exceto geração de PDF) deve ser inferior a 3 segundos em rede local. | Testes de carga com `Locust` ou `k6` simulando 20 usuários simultâneos, com latência P95 ≤ 3s. |
| **RNF-03** | **Segurança** | O sistema deve ser resiliente a ataques de força bruta e exaustão de recursos. | Implementação de Rate Limiting (ex: `slowapi`) no endpoint de Login e nos endpoints de simulação de câmbio. |
| **RNF-04** | **Integridade (ACID)** | O banco de dados deve garantir a atomicidade e consistência das transações, especialmente na criação e clonagem de Invoices. | Uso de transações gerenciadas pelo ORM (SQLAlchemy) e Sequences do PostgreSQL para numeração, evitando Race Conditions. |
| **RNF-05** | **Resiliência** | O sistema deve lidar graciosamente com a indisponibilidade da API externa de câmbio (Frankfurter). | Implementação de mecanismo de Retry com backoff exponencial (ex: biblioteca `tenacity`) e fallback para o cache local (Redis com TTL de 300s). |
| **RNF-06** | **Qualidade de Código** | O código-fonte deve seguir padrões de Clean Code e ser passível de automação de testes. | Cobertura de testes automatizados (unitários e de integração) **≥ 80%**, validada pelo `pytest-cov` no GitHub Actions. |
| **RNF-07** | **Infraestrutura** | O sistema deve ser totalmente containerizado, garantindo paridade entre os ambientes de desenvolvimento, homologação e produção. | O comando `docker-compose up` deve provisionar e iniciar com saúde (healthcheck) os 4 serviços: Frontend (Nginx), Backend (FastAPI), DB (PostgreSQL) e Cache (Redis). |
| **RNF-08** | **Dados (Timezone)** | Todas as datas e horas armazenadas no banco de dados devem estar em UTC. | O backend (Pydantic) deve serializar os campos de data/hora com o sufixo `Z` (ex: `2026-09-08T15:00:00Z`). A conversão para o fuso horário local é de responsabilidade exclusiva do Frontend (Alpine.js). |

#### 5.3. Regras de Negócio (RN)
Regras intrínsecas ao domínio do problema que orientam o comportamento do sistema e os cálculos realizados.

*   **RN-01 (Cálculo de Conversão):** O valor líquido em BRL é calculado estritamente pela fórmula: `Valor Líquido = (Valor Bruto em Moeda Estrangeira × Cotação do Dia) - (Valor Bruto × Cotação × % IOF) - (Valor Bruto × Cotação × % Spread)`.
*   **RN-02 (Imutabilidade Fiscal):** Uma Invoice com status "Finalizada" representa um documento fiscal/financeiro emitido. Portanto, ela é imutável. Qualquer correção deve ser feita através da criação de uma nova Invoice via função "Clonar", que herda os dados, mas gera um novo número de documento e nova data.
*   **RN-03 (Simplificação de Jornada - KISS):** Para fins do MVP, o sistema não realizará cálculos automáticos baseados em dias úteis, feriados ou calendários corporativos. O cálculo de "Valor por Hora" é uma multiplicação direta (`Horas Trabalhadas × Valor da Hora`). O usuário é o único responsável por informar a quantidade total de horas/meses do período.
*   **RN-04 (Cache de Câmbio):** Para respeitar o limite de 1000 requisições/dia da API Frankfurter, o sistema deve consultar a API externa no máximo uma vez a cada 5 minutos (300 segundos). Todas as requisições intermediárias devem ser servidas pelo cache Redis.

---

### 💡 Notas de Implementação para a Equipe (SDD com IA)

1. **Para o Desenvolvedor Back-end:** Ao instruir a IA para gerar os endpoints de Invoice, especifique explicitamente: *"Use uma Sequence do PostgreSQL para o campo `invoice_number` e garanta que o endpoint de clone use uma transação atômica para buscar o `NEXTVAL` e inserir o novo registro"*. Isso previne o Gap de Race Condition.
2. **Para o Desenvolvedor Front-end:** Ao instruir a IA para o formulário de Login, especifique: *"Configure o Axios com `withCredentials: true` e não tente ler ou salvar o token no `localStorage`. O backend gerenciará o cookie HttpOnly"*. Isso previne o Gap de Segurança CORS.
3. **Para DevOps:** O `Dockerfile` do backend deve ser multi-stage. O estágio final deve ser baseado em `python:3.12-slim` e deve incluir a instalação via `apt-get` das bibliotecas `libcairo2`, `libpango-1.0-0` e `libgdk-pixbuf2.0-0` para que o WeasyPrint funcione sem inflar a imagem desnecessariamente.

---

Esta estrutura atende rigorosamente ao PMBOK (focando no *quê* o sistema deve fazer e *como* deve se comportar, sem cair na armadilha de descrever o *como* codificar, que é papel do projeto detalhado), ao mesmo tempo que blinda o projeto contra os pontos cegos técnicos e de escopo que identificamos.

**Deseja que eu prossiga para a elaboração da Seção 6 (Premissas) e Seção 7 (Riscos Iniciais e Plano de Resposta) do TAP, mantendo este mesmo nível de rigor e alinhamento com as decisões tomadas?**
