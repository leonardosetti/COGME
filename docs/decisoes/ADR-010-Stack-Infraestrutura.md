# ADR-010 — Stack de Infraestrutura: PostgreSQL, Docker Compose, Nginx Latente e Hierarquia de APIs de Câmbio

| Campo | Valor |
|---|---|
| **Versão** | 1.0.0 |
| **Status** | Aprovado (ratificado pelo CCB-001 em 29/10/2026) |
| **Data da decisão** | 29/10/2026 |
| **Data de formalização do documento** | 29/10/2026 |
| **Decisor** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| **Gatilhos G1–G4** | G1 (impacto transversal — Backend, Dados, CI/CD, Frontend, Testes), G2 (irreversibilidade prática — migração SQLite → PostgreSQL exige schema, migrations e adaptação de ORM), G3 (questionabilidade acadêmica — "por que não manter SQLite mais simples?"), G4 (trade-off não óbvio — realismo de produção × overhead de infraestrutura) |
| **Rastreabilidade** | TAP §8 (Restrições FOSS) + §11 (Orçamento Zero); EAP N5.1–N5.4, N7.1; REQ-07 (persistência de cotações/cache), REQ-14 (OpenAPI automático); ADRs correlatas: ADR-001 (stack FOSS original, sobreposta parcialmente), ADR-005 (freeze — esta ADR emenda a stack dentro dos limites permitidos), ADR-011 (integração com MCPs e separação L1/L2/L3); Plano de Custos §4.5/§4.6 (gates de registro) |
| **Domínio PMBOK 7ª** | Abordagem de Desenvolvimento + Trabalho do Projeto + Qualidade |
| **Processo PMBOK 6ª (dicionário)** | 4.3 Orientar e Gerenciar o Trabalho; 8.2 Realizar Garantia da Qualidade |

## Contexto

A ADR-001 estabeleceu inicialmente SQLite como banco de dados canônico do produto, justificando-o por simplicidade e adequação ao MVP. Contudo, ao longo das rodadas de planejamento técnico, identificaram-se limitações estruturais:

1. **Tipagem fraca:** SQLite não impõe constraints rigorosas de tipo, aumentando risco de bugs silenciosos em cálculos cambiais (REQ-03 exige precisão de 2 casas decimais).
2. **Concorrência:** apesar de o MVP ser single-user, a arquitetura prevê endpoints assíncronos FastAPI que podem acessar o banco simultaneamente; SQLite locks tornam-se gargalo.
3. **Realismo de produção:** para fins acadêmicos e de portfólio, demonstrar domínio de PostgreSQL agrega valor significativamente superior a SQLite.
4. **Paridade de ambientes:** a ausência de containerização gerava o problema clássico "works on my machine".

Simultaneamente, definiu-se a necessidade de uma hierarquia robusta de fontes de cotação cambial (REQ-01, REQ-07), com fallback mandatório para dados oficiais brasileiros (PTAX/BCB), garantindo conformidade fiscal e soberania de dados.

## Opções Consideradas

### Banco de Dados

| # | Opção | Prós | Contras |
|---|---|---|---|
| DB1 | Manter SQLite | Simplicidade; zero setup | Tipagem fraca; lock em concorrência; menos realismo acadêmico |
| DB2 | Migrar para PostgreSQL 15+ | Tipagem estrita; concorrência MVCC; ecossistema maduro; valor acadêmico | Overhead de instalação/container; curva de aprendizado marginal |
| DB3 | MySQL/MariaDB | Alternativa válida | Menor aderência ao ecossistema Python async (asyncpg > aiomysql em maturidade) |

### Orquestração

| # | Opção | Prós | Contras |
|---|---|---|---|
| ORCH1 | Sem containerização | Simplicidade máxima | "Works on my machine"; dificuldade de replicar ambiente em CI |
| ORCH2 | Docker + Docker Compose | Paridade dev/test/prod; isolamento limpo; portabilidade | Consumo adicional de RAM (mitigado por 58GB disponíveis) |
| ORCH3 | Kubernetes | Escalabilidade extrema | Absolutamente desnecessário para MVP; overengineering flagrante |

### Servidor Web

| # | Opção | Prós | Contras |
|---|---|---|---|
| WEB1 | Apenas Uvicorn expondo porta | Simples | Sem TLS termination nativo; sem serving de estáticos otimizado |
| WEB2 | Nginx como reverse proxy latente | Profissional; pronto para HTTPS futuro; serve estáticos eficientemente | Um serviço extra no compose (opcional/desativável) |

### APIs de Câmbio

| # | Estratégia | Prós | Contras |
|---|---|---|---|
| API1 | Apenas Frankfurter | Gratuita; MIT; ECB confiável | Sem validação cruzada com dados BR |
| API2 | Apenas PTAX/BCB | Oficial brasileira; soberania | Latência variável; sem cobertura EUR/múltiplas moedas em tempo real |
| API3 | Circuit Breaker: Frankfurter → Fallbacks → PTAX/BCB obrigatório | Resiliência; conformidade fiscal; multi-fonte | Complexidade de implementação; necessidade de adapter pattern |

## Decisão

**Aprovar combinações: DB2 + ORCH2 + WEB2 + API3.**

1. **SGBD:** substituir SQLite por **PostgreSQL 15+** como banco canônico de persistência de cotações, cache e dados transacionais (REQ-07). Acesso via SQLAlchemy async + asyncpg. Migrações gerenciadas por Alembic.
2. **Orquestração:** adotar **Docker + Docker Compose** para paridade de ambientes dev/test/prod. Serviços mínimos: `db` (postgres:15-alpine), `web` (FastAPI/Uvicorn custom image), `proxy` (nginx:alpine, opcional/latente).
3. **Servidor Web:** prever **Nginx** como reverse proxy no `docker-compose.yml`, inicialmente desabilitado ou em perfil opcional, pronto para ativação quando houver necessidade de TLS ou serving intensivo de estáticos.
4. **Hierarquia de APIs de câmbio:** implementar padrão **Circuit Breaker** com a seguinte cadeia:
   - **Primária:** Frankfurter (`https://frankfurter.dev/`, REST, MIT, dados ECB).
   - **Fallbacks candidatos:** `fawazahmed0 currency-api` (JSON estático, CC0), `CurrencyConverter` (Python offline, Apache-2.0), `AllRatesToday` starters (MIT), datasets de bancos centrais via jsDelivr, ECB Data Portal (SDMX).
   - **Fallback mandatório:** API PTAX do Banco Central do Brasil (`https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/`). Acionada obrigatoriamente para validação cruzada ou em caso de falha das fontes globais, garantindo conformidade com a realidade fiscal brasileira.
5. **Padrões de código:** Adapter Pattern na integração com APIs; cache com TTL no PostgreSQL para reduzir ≥ 50% das chamadas externas; type hints obrigatórios; docstrings padrão Google; coverage ≥ 80%.
6. **Flexibilidade FOSS controlada:** autorizada adoção de bibliotecas adicionais desde que: (a) licença OSI-approved; (b) auditáveis; (c) provenham de PyPI oficial/Docker Hub Official; (d) não violem orçamento zero; (e) sejam registradas em `docs/dependencias/registro.md`.

## Consequências

- Positivas: realismo de produção; tipagem estrita eliminando bugs siliciosos; paridade ambiental via containers; resiliência cambial multi-fonte com âncora brasileira; valor acadêmico acrescido.
- Negativas: overhead inicial de setup (Dockerfile, docker-compose.yml, alembic init); consumo adicional de RAM (~2–3GB para PostgreSQL containerizado, mitigado por 58GB totais); complexidade ligeiramente maior no CI (container efêmero PostgreSQL).
- Neutras: SQLite permanece como dependência transitiva possível (testes unitários isolados podem usar sqlite:///memory:), mas não é mais o banco canônico de persistência.

## Trade-offs Declarados

| Aspecto | Ganho | Perda/Risco | Mitigação |
|---|---|---|---|
| PostgreSQL > SQLite | Robustez, tipagem, concorrência | Overhead de infra | 58GB RAM comportam containers sem impacto perceptível |
| Docker Compose | Paridade ambiental | Complexidade de build | Makefile/scripts helper; documentação clara no README |
| Nginx latente | Pronto para produção futura | Serviço extra no compose | Perfil opcional no docker-compose; desativável por default |
| Circuit Breaker multi-API | Resiliência + conformidade BR | Complexidade de teste | Mocks determinísticos em testes; integration tests com fixtures locais |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo | Domínio PMBOK 7ª | Data |
|---|---|---|---|---|
| ADR-001 | Parcial | Substituição de SQLite por PostgreSQL; adição de Docker/Nginx; definição de hierarquia de APIs de câmbio | Abordagem de Desenvolvimento | 29/10/2026 |

## kill_switch

Se a migração para PostgreSQL causar regressão funcional não corrigível em ≤ 48h, ou se o consumo de recursos do Docker comprometer seriamente a inferência local (< 12 t/s sustentados), acionar rollback parcial: manter lógica de negócio desacoplada via Repository Pattern, permitindo troca transparente entre PostgreSQL e SQLite (esta última apenas como emergência temporária, nunca como estado final).

## Governança

- **Custódia:** `agent-backend-dev` (Fabricio) + `agent-devops` (Leonardo).
- **Emenda:** mudança de componente de infra exige ADR específica + CCB humano.
- **Auditoria:** `docs/dependencias/registro.md` deve listar todas as imagens Docker, versões exatas, licenças e URLs de origem.
- **CI:** pipeline GitHub Actions roda em container PostgreSQL efêmero (`services: postgres`) para garantir reprodutibilidade.