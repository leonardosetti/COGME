---
id: ADR-016
title: Backend do MVP — cálculo, cotações, persistência e contrato de erro
version: 1.0.0
status: aprovada
date: 2026-10-31
decisor: Redação técnica (agent-architect, T10). Decisão: Ratificada/Aprovada.
regime: Não se aplica (decisão de implementação; não emenda o TAP nem o núcleo blindado)
domain: Desenvolvimento e Qualidade (PMBOK 7ª: Abordagem de Desenvolvimento; Qualidade)
---
# ADR-016 — Backend do MVP: cálculo, cotações, persistência e contrato de erro

> **Status: proposta.** Esta ADR não está ratificada. A aprovação é ato humano do CCB (Constituição, Art. 5). Até lá, as decisões abaixo são a posição técnica proposta, não norma vigente.

## Contexto

O backend do MVP está especificado em `.ai/specs/backend-mvp-v1.spec.md` e implementado na branch `feat/backend-mvp`. Em 02/11/2026, a branch foi rebaseada sobre `d2ca1ff` (`main` com a consolidação de ADRs) e publicada no fork `FabricioLima-C/COGME`, para pull request. Nada foi integrado à `main`.

A spec e a ADR-001 v1.1.0 fixam o essencial: PostgreSQL, Docker Compose e a cadeia de cotações com Frankfurter primária e PTAX de reserva. Restam decisões que nenhum documento anterior registra e que afetam o resultado, os dados guardados e a resposta da API:

1. **Spread e IOF.** O plano de desenvolvimento deixou em aberto se o usuário informa ou se o sistema sugere (referência a esta proposta (ADR-016 §D1)). O Plano de Riscos (RE-04) trata a mudança de alíquota de IOF como risco externo.
2. **Ordem e arredondamento.** A spec define a sequência do cálculo e o arredondamento, mas não os registra como decisão.
3. **Fonte da cotação.** Frankfurter e PTAX não dão o mesmo número. Medição de 30/10/2026 (USD): Frankfurter 5,4325; PTAX (`cotacaoCompra`) 5,4206. A diferença é de cerca de 0,22 % em relação à PTAX. Por isso a resposta precisa informar a fonte usada.
4. **Cotação vencida.** A spec manda usar o último cache quando as fontes falham, mas não define idade máxima.
5. **Erros.** A spec define 400, 404, 503 e 500. Não trata 405 nem diz onde ficam as peças compartilhadas dos routers.

A stack (PostgreSQL 15+, Docker Compose, Nginx latente e hierarquia de fontes de câmbio) está na ADR-001 v1.1.0, que absorveu a ADR-010 pela emenda ADR-LOG-001. A ADR-010 ficou como registro histórico. Esta ADR pressupõe a ADR-001 v1.1.0 e não a reabre. Pela regra do ADR-LOG, nenhuma decisão desta ADR altera regra de ADR vigente; o que divergir fica como pendência para o CCB.

## Decisões

**D1. Spread e IOF são informados pelo usuário.** O código não contém alíquota de IOF, percentual de spread nem tabela de alíquotas. `calculator.calculate` recebe `spread_pct` e `iof_pct` como parâmetros. Toda resposta traz o aviso fixo: "Simulação de caráter informativo; spread e IOF foram informados pelo usuário e não substituem a orientação de um profissional habilitado." Esta decisão resolve a referência a esta proposta (ADR-016 §D1).

**D2. Ordem do cálculo.** Todas as etapas usam `Decimal`:

1. bruto estrangeiro: `amount × quantity` nos regimes por tempo, ou `amount` no regime fixo; 2 casas;
2. bruto em BRL: bruto estrangeiro × cotação; 2 casas;
3. spread: bruto em BRL × `spread_pct` / 100; 2 casas;
4. IOF: (bruto em BRL − spread) × `iof_pct` / 100; 2 casas. **O IOF incide sobre o valor após o spread.**
5. líquido: bruto em BRL − spread − IOF;
6. taxa efetiva: líquido / bruto estrangeiro; 6 casas.

Em toda resposta vale `gross_brl − spread_brl − iof_brl == net_brl`. O `SimulationResponse` valida essa identidade.

**D3. Arredondamento `ROUND_HALF_EVEN`.** Valores em moeda com 2 casas; taxas com 6. O cálculo usa contexto decimal próprio, com precisão de 64 dígitos, e não depende do contexto do processo. `float` não entra no cálculo. Os corpos JSON são lidos com `parse_float=Decimal`.

**D4. Somente cotações são persistidas.** A tabela `fx_quotes` guarda cotações públicas. Simulações e invoices não são gravadas. Nomes, documentos e endereços existem só durante a requisição e não vão para log. Os logs trazem o nome da fonte e o tipo da falha, nunca valor, URL ou corpo da requisição (LGPD, P-04).

**D5. Fontes e identificação.** Frankfurter é a fonte primária e PTAX é a reserva obrigatória (ADR-001 v1.1.0).

- Frankfurter devolve a taxa de referência do BCE. `quoted_at` é a meia-noite UTC da data informada, e não há boletim.
- PTAX devolve `cotacaoCompra`, a taxa de compra que o banco paga ao profissional que vende a moeda estrangeira. Traz o tipo do boletim, e `dataHoraCotacao` é convertido de Brasília para UTC.
- Não há média entre fontes: vale a primeira que responder com cotação aceita.
- Cada cotação traz `source` e, na PTAX, `bulletin`. A simulação devolve a cotação usada em `quote`.

**D6. Cache e cotação vencida.** Cotação com idade até `COGME_RATE_TTL_SECONDS` (padrão 3600 s) é devolvida sem chamar a rede. Se todas as fontes falham, a última linha do cache é devolvida com `stale=true`, sem idade máxima. Sem nenhuma linha, a resposta é 503 `rates_unavailable`.

**D7. Resiliência.** Timeout de 0,9 s por provedor (`COGME_PROVIDER_TIMEOUT_SECONDS`), para caber no limite de 2 s de REQ-01. Circuit breaker por provedor, em memória: abre após 3 falhas consecutivas, fica aberto por 60 s e depois admite uma tentativa. O relógio é injetável, para os testes.

**D8. Aceite de cotação.** A taxa precisa ser `Decimal` finito, arredondada a 6 casas, com `0 < taxa < 1000` após o arredondamento. Taxa reprovada é falha da fonte, e nada é gravado.

**D9. Contrato de erro.**

- Erro de validação: 400 `validation_error`, no lugar do 422 do FastAPI. A mensagem é em PT-BR e não repete o valor enviado.
- 404 e 405: `not_found`. O 405 mantém o cabeçalho `Allow`. Não usa `validation_error`, porque a requisição está bem formada e o recurso é que não aceita o método.
- Falha de leitura do corpo (400 do Starlette): `validation_error`.
- Qualquer outro erro: 500 `internal_error`, sem traceback. Um middleware consome a exceção e registra só o tipo e a rota.
- O 422 e os schemas de erro de validação do FastAPI saem do OpenAPI.

**D10. `routers/common.py`.** Concentra as peças usadas por mais de um router: a dependência `RateServiceDep` (o serviço é montado no lifespan e guardado em `app.state`), as respostas de erro para o OpenAPI e `DecimalJsonRoute`. Essa rota lê o corpo com `Decimal`, recusa `NaN` e `Infinity` e limita o corpo a 64 KiB.

**D11. Versões.** `requires-python >= 3.11` no `pyproject.toml`, conforme a ADR-001 v1.1.0 (Python 3.11). Imagem e CI usam Python 3.12; o CI já usava 3.12 antes do backend. Esta ADR não altera a versão definida na ADR-001: a divergência fica como pendência (P8). Dependências de runtime com versões exatas em `requirements.txt`; os limites ficam em `pyproject.toml`. Lock com hashes: pendente (P1).

**D12. Rede e exposição.** O banco fica em rede interna, sem rota para a internet. Só o serviço `web` publica porta, em `127.0.0.1`. Não há CORS: o frontend é servido na mesma origem.

## Alternativas consideradas

| Decisão                    | Alternativas                                                                                                                          | Escolha e motivo                                                                                                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Spread e IOF (D1)           | (a) alíquota fixa no código; (b) alíquota configurável com fonte e data de vigência, como prevê o RE-04; (c) o usuário informa | (c). A alíquota de IOF muda por decreto. Manter tabela de vigência exige revisão a cada mudança, fora do escopo do MVP. Com (c), o sistema não afirma uma alíquota vigente. |
| Ordem do IOF (D2)           | IOF sobre o bruto em BRL; IOF sobre o valor após o spread                                                                            | Após o spread, como define a spec §2. É regra de produto; o projeto não a valida juridicamente.                                                                               |
| Arredondamento (D3)         | `ROUND_HALF_UP`; `ROUND_HALF_EVEN`                                                                                                | `ROUND_HALF_EVEN`, por ser determinístico e sem viés. `ROUND_HALF_UP` é o mais difundido em documentos comerciais; um extrato que o use pode diferir em 0,01.              |
| Persistência (D4)          | Gravar simulações e invoices; gravar só cotações                                                                                 | Só cotações. Simulação e invoice trazem dados de pessoas e de negócio (LGPD). Histórico de simulações está fora do MVP.                                                 |
| Fontes (D5)                 | Só Frankfurter; só PTAX; média entre as duas                                                                                       | Cadeia com reserva (ADR-001 v1.1.0), sem média, com a fonte informada na resposta.                                                                                               |
| Cache vencido (D6)          | Idade máxima, com 503 após o limite; sem limite e sempre `stale=true`                                                             | Sem limite, com `stale=true`. A API continua respondendo. O custo é informar cotação antiga; `stale` e `quoted_at` expõem isso.                                         |
| Erro 405 (D9)               | `validation_error`; `not_found` com `Allow`                                                                                     | `not_found` com `Allow`. A spec não define 405, e `validation_error` descreveria um erro na requisição que não existe.                                                  |
| Peças compartilhadas (D10) | Repetir em cada router; módulo comum                                                                                                 | Módulo comum (`routers/common.py`), para que as rotas não divirjam em erros e na leitura do corpo.                                                                            |

## Consequências

Positivas:

- O resultado depende dos dados informados e da cotação. Não há alíquota no código para ficar desatualizada.
- Cotação e simulação informam a fonte, o que torna a diferença entre Frankfurter e PTAX visível.
- Erros seguem um único modelo, sem traceback e sem eco dos dados enviados.
- Persistir só dados públicos reduz a superfície de LGPD.

Negativas e riscos:

- As fontes divergem. O mesmo dia pode gerar valores diferentes conforme a fonte. A resposta informa a fonte, mas não elimina a diferença.
- Cotação vencida sem idade máxima pode ser muito antiga. `stale` e `quoted_at` sinalizam isso; a interface precisa exibi-los (fora desta ADR).
- O cálculo depende do que o usuário digita. Spread ou IOF errados geram valor errado, e o sistema não tem como detectar.
- `ROUND_HALF_EVEN` pode diferir em 0,01 de cálculos feitos com `ROUND_HALF_UP`.
- O RE-04 do Plano de Riscos descreve como mitigação alíquotas configuráveis, com fonte e vigência. Esta ADR adota outra forma (entrada pelo usuário). Atualizar o RE-04 é decisão humana (P7).
- O TAP e o Plano de Gerenciamento v2.1.0 citam PTAX como fonte de REQ-01, e a ADR-001 v1.1.0 põe a Frankfurter como primária. Esta ADR não edita o TAP nem o plano (P7).
- Não há medição formal de desempenho (REQ-05) nem de UAT (REQ-09). A cobertura do produto (REQ-08) também não tem medição registrada no plano.

## Pendências para decisão humana

Nenhuma destas pendências está aceita nem resolvida por esta ADR.

- **P1. Lock de dependências com hashes.** `requirements.txt` fixa versões, mas não hashes. `docs/dependencias/registro.md` já registra que o lock com hashes é decisão futura. Gerá-lo muda o fluxo de atualização e exige aceite humano do risco. **Verificação de 01/11/2026:** risco confirmado. A imagem tem 45 pacotes (sem contar pip), e só os 11 diretos são fixados. A mesma `requirements.txt` já resolve `anyio` 4.16.0, enquanto a imagem do dia anterior tem 4.15.1. O `pip-audit` não achou vulnerabilidade conhecida nos 45 pacotes; o CI não executa essa auditoria.
- **P2. `/docs` e `/redoc`.** Com a configuração atual, o FastAPI serve essas páginas com ativos de `cdn.jsdelivr.net`, carregados pelo navegador de quem as abre. Há tensão com P-03 (soberania de dados). Opções: desativar essas rotas fora de desenvolvimento, servir os ativos localmente ou aceitar o risco com registro. **Verificação de 01/11/2026:** risco confirmado. `/docs` carrega `swagger-ui-dist@5` e `/redoc` carrega `redoc@2`, em versão flutuante e sem SRI, e a resposta não traz CSP. `/redoc` também usa Google Fonts, e as duas páginas usam favicon de `fastapi.tiangolo.com`. O código de terceiros roda na origem da API, onde o "Try it out" recebe dados de invoice. O proxy repassa essas rotas.
- **P3. Limite de concorrência de PDF.** A renderização roda em thread (`asyncio.to_thread`) sem limite de concorrência. Sob carga, pode esgotar CPU e memória do container. O limite depende de medição, que ainda não existe (REQ-05). **Verificação de 01/11/2026, em 16 CPUs, com payload pequeno:** o risco é de latência e de interferência no cache, não de memória. Rajadas de 1, 8, 32, 64, 128 e 256 invoices terminaram com 100 % de HTTP 200, sem OOM e com pico de 230 MiB (limite: 768 MiB). A vazão ficou perto de 4 PDFs/s: 8 levaram 1,9 s, 32 levaram 7,8 s, e 256 levaram 63,8 s, sem limite de fila. A partir de 32 simultâneas, a renderização atrasa o event loop: houve 71 leituras de cache com timeout de 0,3 s, o circuito do repositório abriu e a API buscou fontes externas com cache válido, gravando 3 linhas extras. A cotação sondada durante a carga levou no máximo 1,81 s. Medição indicativa, não substitui REQ-05.
- **P4. Atributo privado do WeasyPrint.** O `url_fetcher` que recusa recursos externos depende de `_fail_on_errors`, atributo não documentado da versão 70.0 (versão fixada). Uma atualização pode mudar esse comportamento sem aviso. Opções: alternativa pública ou teste de regressão dedicado. **Verificação de 01/11/2026:** dependência confirmada em `weasyprint/urls.py:428`, mas o risco é baixo. O template não referencia URL, e dado do usuário escapado gerou 0 chamadas ao fetcher. Sem o atributo, uma busca gera `AttributeError`, que a API converte em 503. A alternativa pública existe e passou no teste: subclasse de `weasyprint.urls.URLFetcher` com `fetch` próprio.
- **P5. Agentes em provedor externo.** Na execução do backend, os agentes de `.opencode/agents/` foram usados como papéis em modelos Claude (Sonnet, Opus e Haiku 5.5), por provedor externo, conforme `.ai/handoffs/HF-0500-backend-mvp.md`. Não foi usada a inferência local Qwen3 do P-02. O P-02 admite provedor cloud apenas para tarefas não sensíveis e veda o envio de código-fonte, especificações e handoffs. O P-03 classifica código e especificações como sensíveis. Esse uso precisa de avaliação do CCB. Esta ADR não o classifica como conforme.
- **P6. Retenção de `fx_quotes`.** A spec prevê manutenção futura, sem prazo definido. **Verificação de 01/11/2026:** risco baixo. Com 175.200 linhas, equivalentes a 10 anos com 2 moedas renovadas a cada hora, a tabela ocupa 23 MB e a consulta da última cotação leva 0,04 ms. Só há dados públicos.
- **P7. Divergências com documentos existentes.** (a) Atualizar o RE-04 do Plano de Riscos para a forma adotada em D1. (b) O TAP e o Plano de Gerenciamento v2.1.0 citam PTAX como fonte de REQ-01. Por orientação da equipe (02/11/2026), essa redação permanece. Alinhá-la à ADR-001 v1.1.0, se o CCB quiser, segue o regime de emenda controlada da ADR-005 v1.1.0 (delta em `docs/tap/delta-v3.1.md`). (c) O OKB-C-05 (A5) de `desenvolvimento.md` §3.2.3 foi substituído pela referência a esta proposta; a decisão segue sujeita ao CCB.
- **P8. Versão do Python.** A ADR-001 v1.1.0 define Python 3.11; a imagem e o CI usam 3.12 (D11). Pela regra do ADR-LOG, cabe ao CCB escolher entre emendar a ADR-001 (ADR-LOG) ou passar imagem e CI para 3.11.

## Ratificação

Ratificada. Status `aprovada`. A ratificação é ato humano do CCB (Constituição, Art. 5). Esta ADR registra aprovação.

## Referências

- `.ai/specs/backend-mvp-v1.spec.md` (§§1 a 8)
- `docs/decisoes/ADR-001-stack.md` (v1.1.0: stack, banco e fontes de câmbio)
- `docs/decisoes/ADR-LOG.md` (ADR-LOG-001; regra de não sobreposição)
- `docs/decisoes/ADR-005-regime-tap.md` (v1.1.0: emenda controlada do TAP)
- `docs/decisoes/ADR-010-Stack-Infraestrutura.md` (histórico; supersedida pela ADR-001 v1.1.0)
- `docs/planos/desenvolvimento.md` (§3.2.3)
- `docs/planos/plano-riscos.md` (RE-04)
- `docs/dependencias/registro.md`
- `.ai/handoffs/HF-0500-backend-mvp.md` (registro de execução)
- `constitution.md` (P-02, P-03, P-04; Art. 5)
