---
spec_id: spec-004
specname: backend-mvp-v1
version: 1.0.0
status: in_progress
custody: agent-sdd-specialist (.ai/specs/)
created: 2026-11-01
updated: 2026-11-02
origin: commit f6e0455 (2026-11-01, "docs(spec): especificar backend do MVP") + record .ai/handoffs/HF-0500-backend-mvp.md | creation_handoff: UNKNOWN - verify
task: UNKNOWN - verify | sender: agent-nexus-prime-ultimate
kill_switch: inherited
---

# SPEC spec-004 — backend-mvp-v1 — Backend do MVP COGME (REQ-01 a REQ-05, REQ-07, REQ-14)

Status: IMPLEMENTADA EM BRANCH, COM COMMITS LOCAIS, PENDENTE DE PUSH E MERGE | Branch: `feat/backend-mvp` | Orquestrador: agent-nexus-prime-ultimate

Fonte única das decisões do backend. Em conflito, vale a hierarquia do Art. 2 da Constituição.

## 1. Resolução de conflitos documentais

| Tema | Decisão | Fonte vencedora | Texto superado |
|---|---|---|---|
| Banco | PostgreSQL 15+, SQLAlchemy async, asyncpg, Alembic | Constituição 10.1, ADR-010, Delta REQ-07 | ADR-001 e prompts dba/backend-dev/python (SQLite) |
| Cotação | Frankfurter primária; PTAX fallback obrigatório | ADR-010 §4 | desenvolvimento.md (PTAX primária) |
| Pydantic | v2 (exigido pelo FastAPI atual) | Código de terceiros | prompt api-specialist ("v1-style") |
| Dependências | Permitidas via ADR-010 §6, registradas em `docs/dependencias/registro.md` | ADR-010 §6 | prompts "stdlib + FastAPI only" |
| Python | `>=3.11`; ambiente local e CI usam 3.12 | CI vigente | prompt python-specialist ("pinned 3.11") |
| Spread/IOF | Informados pelo usuário; nenhuma alíquota no código | Plano de Riscos RE-04 | [A CONFIRMAR] desenvolvimento.md §3.2.3 |

Fora do escopo: autenticação, cadastro, histórico de simulações, comparador Wise, telas (N5.3).

## 2. Regras de negócio (REQ-02, REQ-03)

Dinheiro é sempre `Decimal`; `float` é proibido. Arredondamento `ROUND_HALF_EVEN`, 2 casas nos valores em moeda; taxas com 6 casas.

Bruto estrangeiro por regime:

| regime | Fórmula | quantity |
|---|---|---|
| `hourly`, `daily`, `weekly`, `monthly` | `amount × quantity` | obrigatória, > 0 |
| `fixed` | `amount` | proibida |

Com `rate` = cotação em BRL por 1 unidade estrangeira:

1. `gross_foreign = q2(bruto)`
2. `gross_brl = q2(gross_foreign × rate)`
3. `spread_brl = q2(gross_brl × spread_pct / 100)`
4. `iof_brl = q2((gross_brl − spread_brl) × iof_pct / 100)`
5. `net_brl = gross_brl − spread_brl − iof_brl`
6. `effective_rate = q6(net_brl / gross_foreign)`

Propriedade obrigatória: `gross_brl − spread_brl − iof_brl == net_brl` em toda resposta.

Exemplo sintético: USD, `hourly`, amount 30, quantity 160, rate 5.000000, spread 2, iof 0.38 →
gross_foreign 4800.00, gross_brl 24000.00, spread_brl 480.00, iof_brl 89.38 (23520 × 0,0038 = 89,376), net_brl 23430.62, effective_rate 4.881379.

## 3. Contrato HTTP `/v1`

Decimais trafegam como string JSON. Enums: `Currency = USD|EUR`; `Regime = hourly|daily|weekly|monthly|fixed`; `RateSource = frankfurter|ptax`.

| Verbo | Rota | Entrada | Saída | Erros |
|---|---|---|---|---|
| GET | `/v1/health` | — | 200 `{"status":"ok"}` | — |
| GET | `/v1/rates/{currency}` | path `Currency` | 200 `RateQuote` | 400, 503 |
| POST | `/v1/simulate` | `SimulationRequest` | 200 `SimulationResponse` | 400, 503 |
| POST | `/v1/invoice` | `InvoiceRequest` | 200 `application/pdf` | 400, 503 |

Schemas em `src/shared/schemas.py` (SSOT, `extra="forbid"`):

- `RateQuote`: `currency`, `rate`, `source`, `quoted_at` (datetime UTC), `bulletin: str|None`, `stale: bool`.
- `SimulationRequest`: `currency`, `regime`, `amount` (>0, máx. 2 casas, ≤ 1.000.000.000), `quantity: Decimal|None` (>0, máx. 2 casas, ≤ 100.000), `spread_pct` e `iof_pct` (0 a 100, máx. 4 casas). Validador cruza `regime` e `quantity` (§2).
- `SimulationResponse`: `currency`, `regime`, `gross_foreign`, `gross_brl`, `spread_brl`, `iof_brl`, `net_brl`, `effective_rate`, `spread_pct`, `iof_pct`, `quote: RateQuote`, `notice: str`.
- `InvoiceParty`: `name` (1–120), `tax_id: str|None` (≤40), `address: str|None` (≤240).
- `InvoiceRequest`: `simulation: SimulationRequest`, `issuer: InvoiceParty`, `client: InvoiceParty`, `invoice_number` (1–40), `issue_date: date`, `description` (1–500).

`notice` é constante: "Simulação de caráter informativo; spread e IOF foram informados pelo usuário e não substituem a orientação de um profissional habilitado."

Modelo canônico de erro (todas as falhas, inclusive validação, 404 e 500):

```json
{"error": {"key": "validation_error", "message": "Dados inválidos.", "details": [{"field": "amount", "message": "..."}]}}
```

| HTTP | key | Quando |
|---|---|---|
| 400 | `validation_error` | Corpo, path ou enum inválidos (substitui o 422 do FastAPI) |
| 404 | `not_found` | Rota inexistente |
| 503 | `rates_unavailable` | Sem fonte disponível e sem cache |
| 503 | `pdf_unavailable` | WeasyPrint/Pango ausente ou falha de renderização |
| 500 | `internal_error` | Inesperado, sem traceback nem dados do usuário |

Mensagens em PT-BR. `details` nunca ecoa o valor enviado.

## 4. Cotações (REQ-01, REQ-07)

Adapter `RateProvider` (Protocol) com `async fetch(currency) -> RateQuote`.

- **Frankfurter:** `GET https://api.frankfurter.dev/v1/latest?base=USD&symbols=BRL` → `{"amount":1.0,"base":"USD","date":"2026-10-30","rates":{"BRL":5.4325}}`. `quoted_at` = meia-noite UTC de `date`; `bulletin=None`.
- **PTAX:** OData `CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)` com `@moeda='USD'`, janela dos últimos 7 dias (datas `MM-DD-YYYY`), `$top=1`, `$orderby=dataHoraCotacao desc`, `$format=json`. Usa `cotacaoCompra` (o profissional vende moeda) e `tipoBoletim` em `bulletin`. `dataHoraCotacao` vem em `YYYY-MM-DD HH:MM:SS.ffffff`, horário de Brasília (`America/Sao_Paulo`), e é convertido para UTC. Janela sem linhas é falha da fonte.
- JSON lido com `parse_float=Decimal` para não passar por binário.

Aceite de cotação (anti-envenenamento, kill switch DBA 5): `Decimal` finito, `0 < rate < 1000`. Fora disso é falha da fonte e nada é gravado.

Fluxo de `RateService.get_quote(currency)`:

1. Cache com idade ≤ `COGME_RATE_TTL_SECONDS` (padrão 3600) → devolve sem chamar a rede. A idade conta de `fetched_at`.
2. Entra na fila da moeda (single-flight). Quem esperou e viu uma cadeia terminar herda o desfecho dela. Quem assume relê o cache, salvo se a primeira leitura falhou, e percorre a cadeia Frankfurter → PTAX, pulando provedor com circuito aberto. Sucesso grava e devolve.
3. Falha geral: última linha do cache com `stale=true`.
4. Sem cache: `RatesUnavailableError` (503).

Circuit breaker por provedor, em memória: abre após 3 falhas consecutivas e fica aberto por 60 s; depois admite uma tentativa. Relógio injetável. Cancelamento e corte pelo prazo da cadeia liberam a tentativa com `record_release`, sem contar como falha da fonte.

Orçamento de REQ-01: prazo total de 1,9 s por requisição (`total_timeout`), contado da chegada e válido inclusive na fila. Cada chamada ao repositório tem até 0,3 s (`repository_timeout`); estouro equivale a cache ausente na leitura e a gravação ignorada na escrita. Timeout por provedor de 0,9 s, com a cadeia inteira encerrada em t = 1,6 s, o que reserva 0,3 s à gravação. Pior caso: leitura 0,3 + releitura 0,3 + cadeia até 1,6 + gravação 0,3 = 1,9 s; a PTAX recebe o que restar depois da Frankfurter (0,1 a 0,7 s) enquanto o circuito desta não abre, e 0,9 s depois disso. Sem esse corte, 0,3 + 1,8 + 0,3 somariam 2,4 s.

Circuit breaker do repositório (`repository_breaker`), distinto dos provedores: abre após 3 estouros ou `RepositoryError` consecutivos e admite uma sonda a cada 5 s; sucesso fecha e cancelamento usa `record_release`. Aberto, leitura e gravação são puladas sem tocar no repositório: a leitura conta como cache ausente e a gravação é ignorada, com um registro por queda (`quote_cache_skipped`), não por requisição. Nesse período não há cache vencido para devolver, e sem fontes a resposta é 503. O circuito existe porque a consulta de DNS de um banco parado leva cerca de 3,8 s e não para quando a chamada é cortada: no uvloop ela ocupa o pool do libuv, compartilhado com o DNS das fontes. A primeira onda, anterior à abertura, ainda chega a 16 consultas, e o libuv padrão só admite 2 simultâneas; por isso a imagem define `UV_THREADPOOL_SIZE=64` no `Dockerfile`.

Seguidores herdam o desfecho do líder, inclusive falha: cotação, ou cache vencido próprio, ou 503, sem repetir a cadeia. O single-flight vale por processo, e o desfecho herdado vale só para quem chegou antes de a cadeia terminar.

## 5. Persistência (somente cotações)

Tabela `fx_quotes`: `id` bigint PK; `currency char(3)` com CHECK; `rate numeric(18,6)` CHECK `> 0`; `source varchar(20)`; `bulletin varchar(40)` NULL; `quoted_at timestamptz`; `fetched_at timestamptz`. Índice `(currency, fetched_at DESC)`. Retenção em manutenção futura; só há dados públicos.

Acesso via Repository (`QuoteRepository` Protocol), como exige o kill switch da ADR-010. Regra de negócio não importa SQLAlchemy. Migrações Alembic com `upgrade` e `downgrade`.

**LGPD:** invoice nunca é persistida. Nomes, documentos e endereços só existem durante a requisição e nunca vão para log. Logs não trazem valores nem corpo de requisição.

## 6. Invoice (REQ-04)

`POST /v1/invoice` recalcula no servidor a simulação recebida; não aceita valores prontos do cliente. Template Jinja2 `src/frontend/templates/invoice.html`, com autoescape ativo, em PT-BR, exibindo partes, descrição, regime, cotação com fonte, data e boletim, valores e `notice`. Renderiza com WeasyPrint em threadpool, com `import` tardio para a API subir sem Pango, e `url_fetcher` que recusa tudo, sem recursos remotos. Resposta com `Content-Disposition: attachment; filename="invoice.pdf"`.

## 7. Configuração e segurança

Variáveis: `COGME_DATABASE_URL`, `COGME_RATE_TTL_SECONDS`, `COGME_PROVIDER_TIMEOUT_SECONDS`, `COGME_LOG_LEVEL`. Sem valor padrão de banco que contenha credencial real; ausência de `COGME_DATABASE_URL` falha ao iniciar (fail-closed). O scanner do CI varre `src/` e `tests/` e rejeita `password=` literal em `.py`, `.yml` e `.yaml`: monte URLs sem esse padrão. `.env.example` exige exceção `!**/.env.example` no `.gitignore`. Compose publica portas só em `127.0.0.1`. Sem CORS: o frontend é servido na mesma origem.

## 8. Estrutura

```
src/shared/schemas.py            contrato
src/backend/main.py              app, lifespan, handlers de erro
src/backend/config.py            Settings
src/backend/errors.py            exceções de domínio
src/backend/routers/{health,rates,simulations,invoices}.py
src/backend/services/calculator.py   puro
src/backend/services/rate_providers.py
src/backend/services/circuit_breaker.py
src/backend/services/rate_service.py
src/backend/services/simulation_service.py
src/backend/services/invoice_service.py
src/backend/models/quote.py  models/database.py  models/repository.py
migrations/
tests/unit/  tests/integration/
```

Testes não usam rede nem relógio real. Integração com PostgreSQL usa `COGME_TEST_DATABASE_URL` e marcador `postgres`. Cobertura ≥ 80 % sobre `src/`. Dados de teste são sintéticos. `tests/agents/` não é alterado.

## 8.1 Assinaturas internas (contrato entre T5, T6 e T7)

```python
# services/calculator.py (puro)
@dataclass(frozen=True)
class Breakdown: gross_foreign; gross_brl; spread_brl; iof_brl; net_brl; effective_rate  # Decimal
def calculate(regime, amount, quantity, rate, spread_pct, iof_pct) -> Breakdown

# services/circuit_breaker.py
class CircuitBreaker:
    def __init__(self, failure_threshold=3, reset_seconds=60.0, clock=time.monotonic)
    def allow(self) -> bool
    def record_success(self) -> None
    def record_failure(self) -> None
    def record_release(self) -> None  # chamada sem veredito: libera a tentativa, sem penalizar

# services/rate_providers.py
class ProviderError(Exception)  # toda falha de fonte, inclusive timeout e aceite reprovado
class RateProvider(Protocol):
    name: RateSource
    async def fetch(self, currency: Currency) -> RateQuote
class FrankfurterProvider:  __init__(self, client: httpx.AsyncClient, timeout: float)
class PtaxProvider:         __init__(self, client: httpx.AsyncClient, timeout: float, today=<callable -> date>)

# services/rate_service.py
class RateService:
    def __init__(self, repository, providers: list[tuple[RateProvider, CircuitBreaker]],
                 ttl_seconds: int, now=<callable -> datetime UTC>,
                 repository_timeout: float = 0.3, total_timeout: float = 1.9,
                 repository_breaker: CircuitBreaker | None = None)  # padrão: 3 falhas, reset 5 s
    async def get_quote(self, currency: Currency) -> RateQuote

# services/simulation_service.py
async def simulate(request: SimulationRequest, rate_service: RateService) -> SimulationResponse

# services/invoice_service.py
async def render_invoice(request: InvoiceRequest, rate_service: RateService) -> bytes
```

Regras adicionadas na T2:

- `RateQuote` rejeita taxa com mais de 6 casas; o provedor quantiza com `q6` antes de montá-la. `ValidationError` no provedor vira `ProviderError`.
- Bruto que arredonda para 0.00 é erro de validação (`gross_rounds_to_zero`), o que evita divisão por zero em `effective_rate`.
- `SimulationResponse` valida a identidade do §2 e o `notice`.
- Corpos JSON são lidos com `parse_float=Decimal`, pois `json.loads` padrão colapsaria literais longos em `float` antes do schema.
- O handler de validação usa só `loc` e mensagem PT-BR, nunca `input` nem `ctx`, e traduz erros nativos da Pydantic por `type`. Em `extra_forbidden`, o nome da chave enviada não é ecoado.

## 9. Tarefas

| ID | Agente | Modelo | Entrega |
|---|---|---|---|
| T1 | python-specialist | Sonnet 5.5 | pyproject, requirements, registro de dependências, config.py |
| T2 | api-specialist | Opus 5.5 | schemas.py, errors.py |
| T3 | dba | Sonnet 5.5 | modelos, repositório, Alembic |
| T4 | devops + docker-specialist | Sonnet 5.5 | Dockerfile, compose, .env.example, CI |
| T5 | qa-sdet | Haiku 5.5 | Testes unitários e de contrato (primeiro) |
| T6 | backend-dev | Opus 5.5 | Serviços de cálculo, cotação e circuit breaker |
| T7 | backend-dev | Sonnet 5.5 | Routers, main.py, invoice |
| T8 | qa-sdet | Haiku 5.5 | Testes de integração e fechamento de cobertura |
| T9 | digital-security + reviewer | Sonnet 5.5 | Revisão de segurança e código |
| T10 | architect (redação) | Haiku 5.5 | ADR-016 proposta, README, status nos planos, handoff |
| T11 | backend-dev | Opus 5.5 | Timeouts do repositório, single-flight, prazo total, circuit breaker do repositório |
| T12 | devops + backend-dev | Sonnet 5.5 | Desconexão do cliente, endurecimento do compose, lint e Alembic no CI, .gitignore |
| T13 | qa-sdet | Haiku 5.5 | Teste instável, testes do circuit breaker do repositório e do lifespan |

---

## 10. Contexto e origem (camada b)

Spec de fonte única das decisões do backend, anterior à implementação na branch `feat/backend-mvp`: commit `f6e0455` (2026-11-01, "docs(spec): especificar backend do MVP") e registro de execução das tarefas em `.ai/handoffs/HF-0500-backend-mvp.md` (§9, `status: blocked` — única pendência declarada é a ratificação da ADR-016, ato humano do CCB). Decisão de stack correlata: `docs/decisoes/ADR-016-backend-mvp.md:18`. Handoff de criação da spec: `UNKNOWN - verify` (não há envelope `task-ta-*.json` correspondente em `.ai/handoffs/`).

## 11. Critérios de aceite e testes (camada e)

`UNKNOWN - verify` — esta SPEC não possuía seção própria de critérios de aceite antes da normalização TA-0031; nenhum critério foi inventado. Evidência observável de cobertura (fatos verificáveis, sem novo critério): os testes citam esta spec por seção nos docstrings (ex.: `tests/integration/test_api_contract.py:1` → §2, §3; `tests/unit/test_calculator.py:1` → §2, §3) e as tarefas T5/T8 de §9 definem quem entrega os testes.

## 12. Rastreabilidade consolidada (camada f)

| Fonte | Onde nesta spec |
|---|---|
| REQ-01, REQ-07 | §4 Cotações (título da seção) |
| REQ-02, REQ-03 | §2 Regras de negócio (título) |
| REQ-04 | §6 Invoice (título) |
| REQ-05, REQ-14 | declarados no H1 ("REQ-01 a REQ-05, REQ-07, REQ-14"); seção dedicada `UNKNOWN - verify` |
| ADR-016 | §9, tarefa T10 (proposta de ADR) + `docs/decisoes/ADR-016-backend-mvp.md:18` |
| Art. 2 (Constituição) | §1 (hierarquia de resolução de conflitos, parágrafo introdutório) |

## 13. Fora de escopo (camada g)

Escopo negativo já declarado em §1 (parágrafo "Fora do escopo: autenticação, cadastro, histórico de simulações, comparador Wise, telas (N5.3)"). Demais exclusões YAGNI: `UNKNOWN - verify` — a normalização TA-0031 não criou nenhuma nova decisão de escopo.

## 14. CHANGELOG (camada h)

- 1.0.0 — 2026-11-02 (TA-0031, HF-0031): versionamento inicial + template canônico (camadas a–h). Conteúdo pré-existente preservado integralmente (origem: commit `f6e0455`, 2026-11-01); slug antigo `backend-mvp-v1.spec.md` → `spec-004-backend-mvp-v1.spec.md` (mapa em `.ai/specs/MANIFEST.md`); nenhuma decisão reescrita; `status: in_progress` mapeado da linha `Status:` original (IMPLEMENTADA EM BRANCH, PENDENTE DE PUSH E MERGE).

## CAMADAS FUNDAMENTAIS — MAPA (TA-0031)

| Camada | Seção nesta spec | Estado |
|---|---|---|
| (a) cabeçalho — spec_id, versão, status, custódia, datas, origem | frontmatter (`spec_id: spec-004`, `version: 1.0.0`) | aplicada |
| (b) Contexto/origem | §10 + frontmatter `origin` + parágrafo introdutório | aplicada |
| (c) Resolução de conflitos | §1 | aplicada |
| (d) Corpo de decisões/requisitos/contratos | §§2–9 | aplicada |
| (e) Critérios de aceite/testes | §11 | `UNKNOWN - verify` (sem seção própria prévia; evidência em `tests/`) |
| (f) Rastreabilidade | §12 + títulos das §§2–6 | aplicada |
| (g) Fora de escopo (YAGNI) | §13 + §1 | aplicada |
| (h) Changelog | §14 | aplicada (criada em TA-0031) |
