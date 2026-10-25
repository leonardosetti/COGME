Com base na análise comparativa rigorosa entre as propostas (DeepSeek e Qwen) e no objetivo de blindar o MVP do COGME contra falhas lógicas, de performance e de escopo, apresento a **Seção 5 do TAP totalmente refatorada e otimizada**.

Esta versão funde a **correção matemática e flexibilidade de negócio da Qwen** com a **resiliência operacional e otimizações de infraestrutura da DeepSeek**, garantindo o máximo de aderência ao princípio KISS, às restrições de 2 pessoas/2 bimestres e ao padrão PMBOK 6ª edição.

---

### 5. PRINCIPAIS REQUISITOS DAS PRINCIPAIS ENTREGAS/PRODUTOS

Esta seção define os requisitos funcionais (RF), não funcionais (RNF) e as regras de negócio (RN) que compõem o escopo do Minimum Viable Product (MVP) do sistema COGME. Estes requisitos foram consolidados para eliminar inconsistências financeiras, prevenir condições de corrida e garantir a resiliência do sistema em ambientes de hospedagem gratuita, servindo como contrato absoluto para o desenvolvimento assistido por IA (SDD).

#### 5.1. Regras de Negócio (RN)

_Regras intrínsecas ao domínio financeiro-cambial que orientam o comportamento e os cálculos do sistema._

- **RN-01 (Fórmula de Conversão Correta):** O valor líquido estimado em BRL deve ser calculado estritamente pela dedução dos encargos:  
  `Valor Líquido = (Valor Bruto em Moeda Estrangeira × Cotação do Dia) - (Valor Bruto × Cotação × % IOF) - (Valor Bruto × Cotação × % Spread)`. _(Correção crítica: taxas são subtraídas, nunca somadas)._
- **RN-02 (Simplificação KISS de Jornada):** Para o MVP, o sistema suportará apenas duas modalidades: **"Valor por Hora"** e **"Salário Mensal Fixo"**. O cálculo será uma multiplicação direta (`Valor × Quantidade`). O sistema **não** realizará cálculos automáticos baseados em dias úteis, feriados ou calendários corporativos; cabe ao usuário informar o total de horas ou meses do período.
- **RN-03 (Imutabilidade Fiscal):** Uma Invoice com status "Finalizada" representa um documento emitido e é estritamente _read-only_. Qualquer correção deve ser feita exclusivamente através da função de "Clonagem", que gera um novo documento.
- **RN-04 (Numeração Atômica):** A clonagem ou criação de uma nova Invoice deve gerar um número de documento sequencial único, obtido diretamente via `Sequence` do PostgreSQL, prevenindo _race conditions_ em acessos concorrentes.

#### 5.2. Requisitos Funcionais (RF)

_Capacidades que o sistema deve possuir para atender às necessidades do usuário, agrupadas por módulos._

| ID        | Módulo       | Descrição do Requisito                                           | Critério de Aceitação (Definition of Done)                                                                                                                                                                                                                                 |
| :-------- | :----------- | :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RF-01** | Autenticação | O sistema deve permitir cadastro e login de usuários.            | A senha deve ser armazenada no PostgreSQL utilizando hashing `bcrypt` (fator de custo ≥ 12).                                                                                                                                                                               |
| **RF-02** | Sessão       | O sistema deve gerenciar a sessão do usuário de forma segura.    | O token JWT deve ser armazenado exclusivamente em um **Cookie com atributos `HttpOnly`, `Secure` e `SameSite=Lax`**. O frontend não deve ter acesso ao token via JavaScript.                                                                                               |
| **RF-03** | Perfil       | O sistema deve permitir a edição de dados pessoais e bancários.  | Deve suportar campos para Nome, CPF/CNPJ, Endereço e dados completos para _Wire Transfer_ (SWIFT/IBAN).                                                                                                                                                                    |
| **RF-04** | Jornada      | O sistema deve permitir a configuração do modelo de remuneração. | Restrito a "Valor por Hora" ou "Salário Mensal Fixo", associado a uma moeda de origem (USD, EUR ou GBP).                                                                                                                                                                   |
| **RF-05** | Câmbio       | O sistema deve exibir a cotação atual e permitir simulações.     | O backend deve usar mecanismo de _retry_ com backoff exponencial (`tenacity`). Se a API Frankfurter falhar persistentemente, o sistema deve retornar o último valor válido do cache (Redis, TTL 300s) e o frontend deve exibir um aviso visual: _"Cotação com defasagem"_. |
| **RF-06** | Simulação    | O sistema deve processar simulações avulsas de conversão.        | O cálculo (aplicando RN-01) deve ser processado e exibido na interface em **menos de 3 segundos**.                                                                                                                                                                         |
| **RF-07** | Invoice      | O sistema deve permitir a criação de Invoices.                   | Deve ser baseada na jornada configurada, permitindo a inclusão opcional de campos de **"Valores Extras"** (Bônus, Horas Extras). As datas de período não podem ser retroativas.                                                                                            |
| **RF-08** | Status       | O sistema deve gerenciar o ciclo de vida da Invoice.             | Apenas dois estados: **"Rascunho"** (totalmente editável) e **"Finalizada"** (bloqueada para edição, permitindo apenas visualização e clonagem).                                                                                                                           |
| **RF-09** | Clonagem     | O sistema deve permitir clonar uma Invoice "Finalizada".         | Deve criar um novo registro em "Rascunho" com os mesmos dados, mas com a **data de emissão atualizada** e um **novo número sequencial** (via DB Sequence).                                                                                                                 |
| **RF-10** | Exportação   | O sistema deve gerar e permitir o download da Invoice em PDF.    | O PDF gerado (via WeasyPrint) deve manter fidelidade visual idêntica (WYSIWYG) à pré-visualização HTML, incluindo todos os dados e cálculos.                                                                                                                               |

#### 5.3. Requisitos Não Funcionais (RNF)

_Restrições de qualidade, desempenho, segurança e infraestrutura que o sistema deve obedecer._

| ID         | Categoria                | Descrição do Requisito                                                                                                                    | Métrica / Critério de Validação                                                                                                                                                                  |
| :--------- | :----------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RNF-01** | **Tecnológica (FOSS)**   | 100% das linguagens, frameworks, bibliotecas e imagens de container devem possuir licenças aprovadas pela OSI (ex: MIT, BSD, Apache 2.0). | Auditoria via `pip-licenses` (Back) e `license-checker` (Front) no pipeline de CI. Licenças restritivas bloqueiam o merge.                                                                       |
| **RNF-02** | **Performance**          | O tempo de resposta para qualquer requisição à API RESTful (exceto geração de PDF) deve ser inferior a 3 segundos.                        | Testes de carga com `k6` ou `Locust` simulando 20 usuários simultâneos, garantindo latência P95 ≤ 3s.                                                                                            |
| **RNF-03** | **Segurança**            | O sistema deve ser resiliente a ataques de força bruta e exaustão de recursos.                                                            | Implementação de Rate Limiting (ex: `slowapi`) nos endpoints de Login e Simulação de Câmbio.                                                                                                     |
| **RNF-04** | **Integridade (ACID)**   | O banco de dados deve garantir a atomicidade e consistência das transações.                                                               | Uso de transações gerenciadas pelo ORM (SQLAlchemy) e Sequences do PostgreSQL para numeração de invoices.                                                                                        |
| **RNF-05** | **Resiliência de Infra** | O sistema deve permanecer responsivo em ambientes de hospedagem gratuita que suspendem containers inativos.                               | Implementação de um script de **Keep-Alive** (ex: GitHub Actions agendado ou UptimeRobot) enviando requisição ao endpoint `/health` a cada 14 minutos.                                           |
| **RNF-06** | **Qualidade de Código**  | O código-fonte deve seguir padrões de Clean Code e ser passível de automação de testes.                                                   | Cobertura de testes automatizados **≥ 80%**, validada pelo `pytest-cov` no GitHub Actions.                                                                                                       |
| **RNF-07** | **Containerização**      | O sistema deve ser totalmente containerizado, com imagens otimizadas para deploy rápido.                                                  | `docker-compose.yml` com 4 serviços (Front, Back, DB, Redis). A imagem do backend deve ser _multi-stage_ (`python:3.12-slim` + libs Cairo/Pango), resultando em tamanho final **< 500MB**.       |
| **RNF-08** | **Dados (Timezone)**     | Todas as datas e horas devem ser tratadas de forma padronizada para evitar inconsistências.                                               | O backend (Pydantic) deve serializar campos de data/hora em UTC com sufixo `Z` (ex: `2026-09-08T15:00:00Z`). A conversão para o fuso local é responsabilidade exclusiva do Frontend (Alpine.js). |

---

### 💡 5.4. Diretrizes de Implementação para SDD com IA (Specification-Driven Development)

Para que a equipe de 2 pessoas utilize a IA de forma eficiente e sem gerar _gaps_ técnicos, os _prompts_ e especificações para a IA devem conter obrigatoriamente as seguintes instruções:

1. **Para o Backend (FastAPI/Python):**
   - _"Ao criar o endpoint de clonagem de invoice, utilize uma transação atômica do SQLAlchemy e obtenha o novo número da invoice usando `NEXTVAL('invoice_number_seq')` do PostgreSQL. Nunca calcule o número sequencial no código Python."_
   - _"Configure o middleware CORS com `allow_credentials=True` e `allow_origins=['http://localhost:5173']` para suportar o envio de cookies HttpOnly."_
   - _"Implemente um endpoint `/warmup` que importa a biblioteca `weasyprint` e gera um PDF de 1 byte em memória durante o startup do container, evitando cold start na primeira requisição real."_
2. **Para o Frontend (Alpine.js + Axios):**
   - _"Configure todas as instâncias do Axios com `withCredentials: true`. Não tente ler, salvar ou manipular o token JWT no `localStorage` ou `sessionStorage`. O backend gerenciará o cookie automaticamente."_
   - _"Ao exibir datas recebidas da API (formato ISO com 'Z'), utilize o objeto `Date` do JavaScript ou uma função do Alpine.js para formatar para `dd/mm/yyyy HH:mm` no fuso horário local do navegador."_
3. **Para DevOps (Docker):**
   - _"O Dockerfile do backend deve ser multi-stage. Use `python:3.12-slim` como base final e inclua `apt-get install -y libcairo2 libpango-1.0-0 libgdk-pixbuf2.0-0` para garantir que o WeasyPrint funcione sem inflar a imagem."_

---

### ✅ Validação Final da Refatoração

Esta estrutura atende perfeitamente ao solicitado:

1. **Corrigiu a falha matemática** da DeepSeek (adotando a subtração de taxas da Qwen - RN-01).
2. **Manteve a flexibilidade de negócio** (Bônus/Extras - RF-07) protegida pela **simplificação KISS** (sem lógica de calendário - RN-02).
3. **Unificou a resiliência** (Retry no backend + Fallback visual no frontend - RF-05).
4. **Blindou a infraestrutura** (Warmup do PDF + Keep-Alive + Imagem Multi-stage < 500MB).

Esta é a versão definitiva e pronta para ser colada no documento do TAP. Ela fornece à equipe de desenvolvimento um norte técnico inquestionável, eliminando ambiguidades que costumam causar retrabalho em projetos acadêmicos com prazos apertados.

Deseja que eu avance para a elaboração da **Seção 6 (Premissas)** e **Seção 7 (Riscos Iniciais e Plano de Resposta)**, mantendo este mesmo nível de precisão e alinhamento com as decisões tomadas?
