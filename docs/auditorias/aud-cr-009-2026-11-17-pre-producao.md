---
id: docs-auditorias-aud-cr-009-2026-11-17-pre-producao
title: Auditoria de conformidade — CR-009 (pré-produção)
type: audit
version: 1.1.0
status: ativo
owner: agent-security-auditor
derived-from:
- docs/change-requests/cr-009-crud-usuarios-dashboard-anonimo.md
- .ai/specs/spec-017-identity-access-session-v1.md
- .ai/specs/spec-018-provider-profile-bank-account-v1.md
- .ai/specs/spec-019-client-directory-v1.md
- .ai/specs/spec-020-simulation-invoice-history-v1.md
- .ai/specs/spec-022-account-lifecycle-privacy-v1.md
- .ai/specs/spec-004-backend-mvp-v1.spec.md
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md
- docs/decisoes/adr-017-dependencia-argon2id.md
- docs/decisoes/adr-019-seguranca-multiusuario.md
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-03, P-14, P-15)
last-revised: '2026-11-17'
lgpd-class: sensível
tags:
- auditoria
- pre-producao
- seguranca
- lgpd
- identidade
- clientes
- invoices
- ui
cr: CR-009
gate: pré-produção
veredito: REPROVADO
---

# Auditoria de conformidade — CR-009 (pré-produção)

## 1. Sumário executivo

**Veredito: REPROVADO para produção.**

A implementação atual cobre o caminho feliz do MVP (cadastro, login, clientes, invoices, simulação), mas não atende aos contratos de segurança, identidade, isolamento e apresentação exigidos pela CR-009 e pelas specs ratificadas.

Contagem de achados (revisão 1.1.0, 2026-11-17):

| Severidade | Ativos | Possíveis | Total |
|------------|--------|-----------|-------|
| **BLOQ** (bloqueia produção) | 17 | — | 17 |
| **ALTO** | 12 | — | 12 |
| **MÉDIO** | 6 | — | 6 |
| **Possível/condicional** | — | 10 | 10 |
| **Drift spec × código** | 6 | — | 6 |
| **Total** | **41** | **10** | **51** |

Dois bloqueadores novos entraram na rodada de confirmação: **B-16** (handler canônico converte 401/403/422 em 500) e **B-17** (dependência de sessão sem tipo quebra `/me`, `/logout`, `/aliases` e `/aliases/cnpj`). Ambos foram reproduzidos no container em execução.

Nenhum item `BLOQ` pode ser aceito como débito pós-produção. Os itens `ALTO` devem ser fechados antes de beta público. Os `MÉDIO` podem entrar em onda seguinte com registro.

## 2. Escopo e método

### 2.1 O que foi auditado

- Código backend: `src/backend/routers/`, `models/`, `middleware/`, `schemas/`, `config.py`, `main.py`.
- Migrações: `migrations/versions/0001..0009`.
- Frontend: `src/frontend/app.py`, templates, CSS e JS.
- Infra: `Dockerfile`, `docker-compose.yml`, `infra/nginx/default.conf`.
- Specs ratificadas: 004, 015, 017, 018, 019, 020, 022, 023.
- ADRs 017 e 019.

### 2.2 Como foi verificado

1. Leitura integral dos arquivos citados.
2. `grep` por padrões de risco (PII em log, CSRF, owner, rate limit, unique, tokens).
3. Consulta ao banco em execução (`docker compose exec db psql`) para `alembic_version`, índices e schema.
4. Execução do `alembic heads` e `alembic history`.
5. Verificação do runtime do container (`_ARGON2_AVAILABLE`, import de `argon2`).
6. Teste manual dos fluxos de cadastro/login/cliente/invoice registrados na sessão anterior.
7. Reprodução viva contra o container (`http://localhost:8080`) do comportamento de erro e de sessão, que originou B-16 e B-17.
8. Suíte de testes (`pytest -q`) — resultado no §9.

### 2.3 Limites

- Não foi feito teste de penetração externo.
- Não foi executada análise dinâmica de CSP (CSP ainda não existe).
- Não foi validada a entrega real de e-mail (SMTP não configurado).
- Não foi feito teste visual com usuário humano; o aceite visual continua pendente.
- A auditoria cobre o código no estado local (alterações não commitadas), não uma tag publicada.

## 3. Achados bloqueadores (BLOQ)

### B-01 — PII em log de cadastro

- **Evidência:** `src/backend/routers/auth.py:178` e `:208`.
- **Violação:** SPEC-017 AC-09; SPEC-015 CP-2/P-15; ADR-019 §4.4; P-15.
- **Descrição:** o cadastro loga `identifier` (e-mail/CPF/CNPJ) e `name`; o conflito loga o identificador. CPF/CNPJ são dados pessoais e não podem aparecer em log.
- **Correção:** remover `identifier` e `name`; logar apenas `user_id` após criação e `kind` do identificador. Para conflito, logar apenas `kind` e um contador.
- **Teste:** `caplog` em cadastro sucesso, conflito e erro; assert de que nenhum valor de entrada aparece.

### B-02 — Hash de identidade não é HMAC e hash interno não tem sal

- **Evidência:** `src/backend/routers/auth.py:125-126` e `:215`.
- **Violação:** SPEC-017 §2.2; ADR-019 §4.4.
- **Descrição:** `_lookup_hmac` é `SHA-256("kind:value:pepper")`, não HMAC-SHA-256. `internal_username_hash` é `SHA-256(normalized)`, sem sal, permitindo dicionário/rainbow table de CPF/CNPJ/e-mail.
- **Correção:** `HMAC-SHA-256(pepper, "kind:value")` e `HMAC-SHA-256(pepper, uuid4().hex)`. Pepper ≥ 32 bytes em produção.
- **Teste:** vetor conhecido de HMAC; assert de que `internal_username_hash` não muda com o identificador.

### B-03 — Senha em PBKDF2; Argon2id inativo por import quebrado

- **Evidência:** `src/backend/routers/auth.py:55-58`, `:60`, `:88-101`.
- **Violação:** ADR-017; SPEC-017 §2.4.
- **Descrição:** `from argon2.Type import ID` falha no container (`ModuleNotFoundError: No module named 'argon2.Type'`); `_ARGON2_AVAILABLE=False`. Todo hash usa PBKDF2-SHA256 210k, não Argon2id. Além disso, o caminho Argon2 usa `hash_secret_raw` e persiste só o hash hexadecimal, sem salt/parâmetros; `verify_secret` espera hash encoded.
- **Correção:** `from argon2 import PasswordHasher, Type`; usar `PasswordHasher(type=Type.ID, time_cost=3, memory_cost=65536, parallelism=4)` e persistir o encoded hash. Em produção, falhar startup se `argon2-cffi` ausente. Rehash no próximo login.
- **Teste:** registrar, verificar prefixo `$argon2id$`, login, rehash de hash PBKDF2 legado.

### B-04 — Numeração de invoice colide entre emissores

- **Evidência:** `migrations/versions/0005_create_invoices_and_sequences.py:32-47` e `:167`; `src/backend/models/invoice_repository.py:341-349`.
- **Violação:** SPEC-020 DEC-06; CR-009 CR9-D10.
- **Descrição:** `next_invoice_number` é por `issuer_tax_id_digits`, mas `invoices.invoice_number` tem unique global. Dois emissores no mesmo mês geram `INV-202611-0001`; o segundo `INSERT` falha.
- **Correção:** remover `uq_invoices_invoice_number`; criar unique `(issuer_tax_id_digits, invoice_number)`.
- **Teste:** dois usuários com CNPJs distintos criam a primeira invoice no mesmo mês; ambas `201`.

### B-05 — Cross-owner em `client_id` e `simulation_id` de invoice

- **Evidência:** `src/backend/routers/invoices.py:358-395`; `src/backend/models/invoice_repository.py:194-210`.
- **Violação:** P-14; SPEC-020 §3; ADR-019.
- **Descrição:** `create_invoice` grava `payload.client_id` e `payload.simulation_id` sem consultar se pertencem ao usuário. Um usuário pode referenciar cliente/simulação de outro e capturar o snapshot no PDF.
- **Correção:** carregar `Client`/`Simulation` por `(id, owner_user_id)`; 404 se ausente. Derivar o snapshot do banco; rejeitar divergência.
- **Teste:** usuário A cria cliente; usuário B tenta `POST /v1/invoices` com o ID; 404 e contagem inalterada.

### B-06 — CSRF double-submit inutilizável; logout isento

- **Evidência:** `src/backend/middleware/csrf.py:59-60` (cookie `HttpOnly`), `:17-26` (logout isento); nenhum template/JS envia `X-CSRF-Token`.
- **Violação:** SPEC-017 §2.6; ADR-019 §4.5.
- **Descrição:** o cookie CSRF é `HttpOnly`, então o frontend não consegue lê-lo; nenhuma requisição envia o header. Toda mutação autenticada via navegador retorna 403, exceto logout, que fica sem proteção.
- **Correção:** cookie CSRF sem `HttpOnly`; helper JS lê o cookie e envia `X-CSRF-Token`; remover `/v1/auth/logout` da lista de isenção.
- **Teste:** login, `POST /v1/clients` com e sem header; 201/403. Logout sem header 403.

### B-07 — Reset de senha não entrega o token e link 404

- **Evidência:** `src/backend/routers/auth.py:366-394`; `src/frontend/app.py:103-112`; `src/frontend/templates/auth/login.html:38`.
- **Violação:** SPEC-017 §2.7; CR-009 CR9-D09.
- **Descrição:** o token é gerado e persistido, mas não é retornado, não é enviado por e-mail e não há rota GET `/auth/password/reset-request`. O link do login aponta para uma rota POST-only, resultando em 405/404.
- **Correção:** SMTP próprio + template de e-mail; `GET /auth/reset?token=`; `POST /v1/auth/password/reset-confirm`; fallback dev em arquivo `0600`.
- **Teste:** request sempre 202; token chega ao fake SMTP; confirm troca a senha; segundo uso falha.

### B-08 — Exclusão de conta corrompe unicidade e não apaga dados

- **Evidência:** `src/backend/routers/account.py:60-66` e `:77`.
- **Violação:** SPEC-022; LGPD art. 18; P-15.
- **Descrição:** a exclusão grava `email=""`, `cpf="00000000000"`, `internal_username_hash=""`. A segunda exclusão viola os índices parciais únicos (`""` e `"00000000000"` não são NULL). Identificadores em `user_login_identifiers`, clientes, simulações, invoices e provider não são apagados/anonimizados. `from_status` é capturado depois de `status = deleted`, então sempre `None`.
- **Correção:** anonimizar com valores únicos/NULL compatíveis com os índices; aposentar identificadores; tratar dados relacionados conforme retenção de 5 anos; capturar `from_status` antes da mudança.
- **Teste:** excluir duas contas distintas; excluir a mesma duas vezes; verificar que nenhum identificador antigo autentica.

### B-09 — Reativação de conta dormente é impossível

- **Evidência:** `src/backend/routers/auth.py:288-292`; `src/backend/routers/account.py:84-95`.
- **Violação:** SPEC-022; CR-009 CR9-D05.
- **Descrição:** o login rejeita conta dormente com 403 e não cria sessão; `/v1/account/reactivate` exige sessão válida. Não há caminho para reativar.
- **Correção:** `POST /v1/account/reactivate` público com identificador + senha, mesma verificação e rate limit do login; ou token de reativação de curta duração.
- **Teste:** dormente + credenciais corretas → 200 e sessão; credenciais erradas → 401.

### B-10 — Sessão não revalida status do usuário

- **Evidência:** `src/backend/middleware/session.py:65-78`; `src/backend/routers/auth.py:288-292`.
- **Violação:** SPEC-017; SPEC-022; P-14.
- **Descrição:** `get_current_session` consulta apenas `user_sessions`, sem `users.status`. Uma sessão emitida antes da dormência/exclusão continua válida; a exclusão revoga sessões, mas a dormência não.
- **Correção:** juntar `users.status` na validação ou checar status a cada requisição; revogar sessões ao entrar em dormência.
- **Teste:** criar sessão, marcar usuário como `dormant`/`deleted`, chamar `/v1/auth/me`; 401/403.

### B-11 — Revisão Alembic incompatível com `varchar(32)`

- **Evidência:** `migrations/versions/0009_fix_users_nullable_email_cpf.py:14`; banco `alembic_version = 0009_fix_users_nullable` (23 chars).
- **Violação:** operação de deploy; rastreabilidade de schema.
- **Descrição:** a revisão declarada tem 35 caracteres; a coluna é `VARCHAR(32)`; o banco contém um valor manual de 23. `alembic current` não reconhece e `alembic upgrade head` não resolve.
- **Correção:** renomear a revisão para `0009_fix_users_nullable`; teste que valida `len(revision) <= 32` em todas as migrations.
- **Teste:** banco limpo `upgrade head`; banco existente `current`; downgrade.

### B-12 — `Secure` cookie sobre HTTP quebra login

- **Evidência:** `src/backend/routers/auth.py:312-319`; `infra/nginx/default.conf:8`.
- **Violação:** CR-009 CR9-D08.
- **Descrição:** o cookie de sessão é sempre `Secure`; o proxy só escuta HTTP na porta 80. Em acesso por Tailscale/IP (não localhost), o navegador descarta o cookie e o login não persiste.
- **Correção:** TLS em produção; `COGME_ENV=development` permite `Secure=false` apenas em localhost; documentar.
- **Teste:** login via `http://localhost` e via IP da rede; comportamento esperado por ambiente.

### B-13 — Clientes internacionais são impossíveis

- **Evidência:** `src/backend/routers/clients.py:43`, `:45`, `:93-102`; `src/backend/models/client.py` (`tax_id_digits CHAR(14) NOT NULL`).
- **Violação:** CR-009 CA-06; SPEC-019 §2.
- **Descrição:** `tax_id` exige 11/14 dígitos; cliente `US` sem CPF/CNPJ não passa na validação. `country_code` não é validado contra ISO 3166. `email`/`phone` são aceitos no schema e descartados na criação.
- **Correção:** `tax_id_digits VARCHAR(32) NULL`; `tax_id_type foreign`; validar país em `countries`; persistir e-mail/telefone.
- **Teste:** criar cliente `US` sem tax_id; país inválido 400; email/phone devolvidos.

### B-14 — Rate limits ausentes fora do auth

- **Evidência:** apenas `src/backend/routers/auth.py:156`, `:247`, `:356`; `src/backend/main.py:338`.
- **Violação:** SPEC-004 §8; ADR-019 §7.
- **Descrição:** `/v1/simulate`, `/v1/invoice`, `/v1/invoices`, `/v1/clients`, `/v1/provider` e `/v1/account` não têm limite. O fluxo anônimo e a emissão de PDF são abusáveis.
- **Correção:** aplicar limites da SPEC-025 §6.4; testar 429.
- **Teste:** rajada acima do limite em cada rota.

### B-15 — Rate limit vê IP do proxy, não do cliente

- **Evidência:** `Dockerfile:69` (uvicorn sem `--proxy-headers`); `src/backend/middleware/rate_limit.py:13` (`get_remote_address`); `infra/nginx/default.conf:23-25,35-37` (envia `X-Real-IP`/`X-Forwarded-For`).
- **Violação:** SPEC-004 §8; ADR-019 §7.
- **Descrição:** sem `--proxy-headers`, o backend enxerga o IP do container nginx. Todos os usuários compartilham o mesmo bucket; um atacante derruba o serviço para todos.
- **Correção:** `uvicorn --proxy-headers --forwarded-allow-ips=<rede do proxy>`; validar o header no proxy; teste com IPs distintos.
- **Teste:** duas origens distintas não compartilham contador.

### B-16 — Handler canônico converte 401/403/422 em 500

- **Evidência:** `src/backend/main.py:214-245` (`_handle_http_error`); reproduzido no container em execução.
- **Violação:** CR-009 §5.5; SPEC-024 §6.2; SPEC-025 §4.6; SPEC-017; P-03.
- **Descrição:** `_handle_http_error` só mapeia 400, 404, 405 e 409. Qualquer outro status cai no ramo genérico e vira `500 internal_error`. Prova viva:

  ```text
  POST /v1/auth/login  senha errada  -> 500 internal_error
  GET  /v1/clients     sem sessão    -> 500 internal_error
  GET  /v1/invoices    sem sessão    -> 500 internal_error
  ```

  Credencial inválida e sessão ausente devem ser `401 unauthorized`, não erro interno. O 500 mascara falha de autenticação e quebra o contrato de erro das specs.
- **Correção:** mapear 401, 403, 422 e 429 no handler; chaves específicas (`account_dormant`, `email_unverified`, `profile_incomplete`, `issuer_not_allowed`, `issuer_inactive`, `limit_exceeded`) via `DomainError`; nunca converter status conhecido em `internal_error`.
- **Teste:** senha errada → 401; sem sessão → 401; emissor de terceiro → 403 `issuer_not_allowed`; limite excedido → 422 `limit_exceeded`; rate limit → 429; nenhuma dessas respostas é 500.

### B-17 — Dependência de sessão sem tipo quebra `/me`, `/logout`, `/aliases` e `/aliases/cnpj`

- **Evidência:** `src/backend/routers/auth.py:333-335`, `:449-451`, `:482-484`, `:520-522` (`Depends(lambda r, sf_, p: get_current_session(r, sf_, p))`); reproduzido no container em execução.
- **Violação:** SPEC-017 §2.5; SPEC-024 §6.3; CR-009 CA-04/CA-07.
- **Descrição:** os parâmetros do `lambda` não têm anotação de tipo, então o FastAPI os interpreta como query params obrigatórios. Prova viva:

  ```text
  GET /v1/auth/me -> 400
  {"details":[{"field":"query.r"},{"field":"query.sf_"},{"field":"query.p"}]}
  ```

  As quatro rotas ficam inutilizáveis: perfil, logout, aliases e rotação de alias CNPJ.
- **Correção:** uma dependency tipada única (`CurrentSession`) reutilizada pelas quatro rotas; nenhuma anotação sem tipo em `Depends`.
- **Teste:** `GET /v1/auth/me` com sessão válida devolve 200 com o corpo da SPEC-024 §6.3; sem sessão devolve 401 (não 400); logout com CSRF devolve 204.

## 4. Achados altos

| ID | Evidência | Violação | Correção |
|----|-----------|----------|----------|
| **H-01** | `src/backend/middleware/session.py:76-78` | SPEC-017 §2.5 | Sliding expiration só atualiza `last_seen_at`; não estende `expires_at` nem o cookie. Atualizar ambos. |
| **H-02** | `src/backend/routers/clients.py:85-108` | SPEC-019; CR-009 CA-06 | `IntegrityError` de duplicidade não é tratado; vira 500. Capturar e retornar 409 `conflict`. |
| **H-03** | `src/backend/routers/provider.py:139-182`; `src/backend/models/provider.py:46,52` | SPEC-018 | Um CNPJ por usuário (`user_id unique`); CNPJ duplicado vira 500; sem normalização/checksum. Criar `provider_cnpjs` e validar. |
| **H-04** | `src/backend/routers/provider.py:14-15` | P-15; ADR-010/018 | Dados bancários em texto simples, documentados como shortcut. Criptografar antes de produção. |
| **H-05** | `infra/nginx/default.conf:14-16` | P-03; SPEC-023 | Sem CSP, HSTS ou Permissions-Policy. Adicionar; HSTS só com TLS. |
| **H-06** | `src/frontend/templates/base.html:10-12` | P-03; SPEC-026 §7.3 | Google Fonts remoto. Remover; usar pilha local. |
| **H-07** | `src/frontend/templates/_navbar.html:12-18`; `src/frontend/app.py:81-112` | SPEC-026 §5.1/§5.5 | Navbar sempre deslogada; não existem `/dashboard`, `/perfil`, `/clientes`, `/sobre`. Implementar rotas e estado. |
| **H-08** | `src/frontend/templates/index.html:148-167` | CR-009 CA-10; SPEC-026 §6.1 | Seção `#sobre` inline e HTML malformado (`</p </p>`). Extrair para `/sobre` e corrigir. |
| **H-09** | `src/backend/routers/invoices.py:388-394` | SPEC-020; P-14 | Snapshot do cliente vem do payload, não do registro persistido. Derivar do banco e rejeitar divergência. |
| **H-10** | `src/backend/routers/auth.py:501-510` | SPEC-017 §2.2 | `/v1/auth/aliases` devolve máscaras fictícias (`m***@x.com`, `***.***.***-00`), não os identificadores reais mascarados. Corrigir ou remover o endpoint até ter dado real. |
| **H-11** | `src/backend/routers/auth.py:469`; `src/backend/routers/auth.py:505` | SPEC-017 | `GET /v1/auth/me` devolve `email=None` para contas CNPJ e não devolve telefone/identificadores. Completar o contrato da SPEC-024 §6.3. |
| **H-12** | `src/frontend/templates/auth/login.html:44`, `register.html:51`, `invoice_form.html:168` | SPEC-023; CSP | Scripts inline impedem `script-src 'self'`. Externalizar para `static/js/`. |

## 5. Achados médios

| ID | Evidência | Descrição | Correção |
|----|-----------|-----------|----------|
| **M-01** | `src/backend/main.py:214-245` | `_handle_http_error` mapeia apenas 400, 404, 405 e 409; 401, 403, 422 e 429 caem no ramo genérico e viram `500 internal_error`. | Mapear 401/403/422/429 e chaves específicas; corrigido como bloqueador **B-16**, não como débito médio. |
| **M-02** | `src/backend/routers/account.py:77` | `from_status` sempre `None` porque `user.status` já foi alterado. | Capturar antes da mudança. |
| **M-03** | `src/backend/routers/auth.py:157-240` | Cadastro não verifica posse do e-mail; qualquer pessoa pode registrar o e-mail de outra. | Duplo opt-in ou, no mínimo, aviso e bloqueio de login até verificação (decisão CR9-D01). |
| **M-04** | `src/backend/schemas/auth.py:13-28` | `RegisterRequest` só tem `identifier`; não há `email`/`tax_id` separados. | Emenda SPEC-024 §6.1 com compatibilidade de 90 dias. |
| **M-05** | `src/backend/routers/simulations.py:153-175` | Listagem de simulações devolve array sem `total`; dashboard não consegue contar. | Adicionar `{items,total,limit,offset}` ou usar `limit=5` e rótulo "recentes". |
| **M-06** | `src/backend/routers/auth.py:52-54` | Comentário diz Argon2 `m=19456,t=2,p=1`; código usa `m=65536,t=3,p=4`. | Alinhar comentário e ADR-017; registrar parâmetros efetivos. |

## 6. Violações possíveis (condicionais)

| ID | Condição | Efeito | Mitigação |
|----|----------|--------|-----------|
| **P-01** | Duas contas com CNPJs distintos emitem no mesmo mês | Colisão de `invoice_number`; segundo `INSERT` falha | B-04 |
| **P-02** | Acesso por IP/Tailscale via HTTP | Cookie `Secure` descartado; login não persiste | B-12 |
| **P-03** | Job/manual marca conta como `dormant` | Sessões antigas continuam válidas; reativação impossível | B-09/B-10 |
| **P-04** | Segunda exclusão de conta | `email=""`/`cpf="00000000000"` colidem nos índices parciais | B-08 |
| **P-05** | Conta legada com `email = NULL` | Novo contrato "e-mail obrigatório" não a alcança; reset impossível | CR9-D01 + SPEC-024 §6.12 |
| **P-06** | Exclusão de conta com clientes/invoices | Dados pessoais permanecem; erase LGPD incompleto | B-08 + SPEC-022 |
| **P-07** | Reset request para e-mail inexistente vs existente | Diferença de timing pode enumerar contas | Resposta e tempo constantes; rate limit |
| **P-08** | Cadastro com e-mail de terceiro | Tomada de namespace de e-mail; reset futuro para o dono real | M-03 |
| **P-09** | Múltiplos workers/restart | Rate limit em memória zera e não é compartilhado | Migrar para Redis em onda futura; documentar |
| **P-10** | CSP ativado antes de externalizar scripts | UI quebra (login/register/invoice) | H-12 primeiro; CSP em Report-Only por 7 dias |

## 7. Drift spec × código

| ID | Spec | Código | Divergência | Ação |
|----|------|--------|-------------|------|
| **SD-01** | SPEC-017: `internal_username_hash` HMAC; e-mail/CPF NOT NULL | SHA-256 sem sal; nullable | Contrato de identidade não cumprido | B-02; emenda SPEC-024 |
| **SD-02** | SPEC-017/ADR-017: Argon2id | PBKDF2 | Algoritmo divergente | B-03 |
| **SD-03** | SPEC-018: CNPJ alterado rotaciona alias HMAC em `user_login_identifiers` | CNPJ não é identificador de login; sem rotação | CR-009 trata CNPJ secundário como dado empresarial, não login | Decisão CR9-D02/D04 + emenda SPEC-018 |
| **SD-04** | SPEC-019: `tax_id VARCHAR(40) NULLABLE`; `is_active` | `CHAR(14) NOT NULL`; `status` | Modelo diverge | SPEC-025 §3 |
| **SD-05** | SPEC-020: IDs UUID; `client_id`/`simulation_id` UUID | BIGINT; int | Modelo diverge | Emenda SPEC-020 ou correção de spec |
| **SD-06** | SPEC-004: rate limits por rota | Só auth tem limite | Contrato não cumprido | B-14 |

## 8. Conformidade já atendida

- **Fluxo anônimo sem persistência:** `src/backend/routers/simulations.py:203-229` chama `simulate` sem repositório; `src/backend/routers/invoices.py:86-105` chama `render_invoice`, que não grava. Confirmado por inspeção; falta teste de contagem.
- **Duplicidade de cadastro:** e-mail, CPF e CNPJ retornam `409 conflict` (teste manual).
- **Sessão opaca:** token de 32 bytes, hash com pepper, cookie HttpOnly/SameSite=Lax, revogação no login.
- **Isolamento de clientes:** GET/PUT/activate/deactivate filtram `owner_user_id` e retornam 404 cross-owner.
- **Isolamento de invoices:** list/get/finalize/clone/delete usam `get_by_id(..., owner_user_id)`.
- **CSRF middleware existe:** falta integração do frontend e remoção da isenção de logout.
- **Erros canônicos:** `ErrorKey.CONFLICT` existe e `409` é mapeado (`main.py:243-244`); os demais status do contrato não são mapeados (B-16).
- **Testes:** 1455 passed, 9 failed, 37 skipped, 18 errors na execução desta auditoria; ver §9 para classificação.

## 9. Execução de testes

Resultado da suíte no estado local (2026-11-17):

```text
pytest -q
9 failed, 1455 passed, 37 skipped, 18 errors in 34.39s
```

Classificação:

| Grupo | Qtd. | Causa | Ação |
|-------|------|-------|------|
| `test_openapi::test_exactly_the_four_v1_routes_are_documented_req14` | 1 | teste espera apenas 4 rotas; a API já tem auth/clientes/provider/invoices | atualizar o teste para o contrato vigente |
| `test_frontend::*` | 5 | seletores/classes antigas (`card result-card visible`) após o redesenho visual | atualizar seletores e cobrir o novo markup |
| `test_lifespan::*` | 2 | expectativa de startup sem `COGME_DATABASE_URL` divergente do código atual | revisar teste e contrato de startup |
| `test_api_contract::test_unexpected_error_is_500_internal_error_without_leaks` | 1 | exceção genérica propagou para o TestClient em vez de virar 500 canônico | investigar handler/middleware antes de produção |
| `test_auth::*` | 10 erros | `COGME_TEST_DATABASE_URL` ausente no ambiente | rodar com a variável de teste |
| `e2e_playwright::*` | 8 erros | navegador/stack e2e não disponível no ambiente | rodar no CI/e2e dedicado |

Observação: a suíte **não** cobre os fluxos de segurança desta auditoria (PII em log, CSRF no navegador, cross-owner de invoice, numeração multi-emissor, rate limit atrás de proxy, exclusão repetida, dormência). Testes verdes não invalidam os achados. A última execução registrada antes desta auditoria era **1192 passed, 6 skipped**; o número subiu para 1455 passed, mas o estado não é verde.

## 10. Gates de liberação

| Gate | Critério | Estado |
|------|----------|--------|
| **G1 — CR aprovada** | Decisão CCB registrada | ❌ pendente |
| **G2 — Specs ratificadas** | SPEC-024/025/026 ratificadas | ❌ pendente |
| **G3 — BLOQ fechados** | 0 findings BLOQ abertos | ❌ 17/17 abertos |
| **G4 — Segurança** | Testes de PII, CSRF, cross-owner, rate limit, cookie | ❌ ausentes |
| **G5 — LGPD** | Parecer de retenção/erase e base legal | ❌ pendente |
| **G6 — Migrations** | `alembic upgrade head` do zero e em banco existente | ❌ falha |
| **G7 — Visual** | Aceite em 360/768/1280, cards sem quebra | ❌ pendente |
| **G8 — TLS** | HTTPS em produção, cookies Secure | ❌ HTTP apenas |
| **G9 — Observabilidade** | Zero PII em log, rate limit por IP real | ❌ falha |
| **G10 — Suíte** | Testes existentes + novos verdes | ❌ 9 failed, 1455 passed, 18 errors |

## 11. Plano de correção priorizado

### P0 — antes de qualquer produção (bloqueadores)

1. B-01, B-02, B-03: identidade, HMAC, Argon2id, zero PII.
2. B-04, B-05, B-09: numeração, cross-owner, snapshot.
3. B-06, B-07, B-10: CSRF, reset, status de sessão.
4. B-08: exclusão de conta e retenção.
5. B-11: revisão Alembic.
6. B-12, B-15: cookies/TLS e IP real.
7. B-13, B-14: clientes internacionais e rate limits.
8. B-16: handler canônico de erros (401/403/422/429).
9. B-17: dependency de sessão tipada nas quatro rotas de auth.

Correção de B-16 e B-17 vem antes de qualquer tela de perfil ou dashboard: sem elas, o frontend não distingue "não autenticado" de "erro interno" e o logout continua quebrado.

### P1 — antes de beta público

- H-01 a H-12.
- Testes de segurança e e2e.
- CSP em Report-Only e externalização de scripts.

### P2 — onda seguinte

- M-01 a M-06.
- P-07 a P-10.
- Migração de rate limit para armazenamento compartilhado.

## 12. Rastreabilidade CR/spec

| Achado | CR-009 | Spec proposta |
|--------|--------|---------------|
| B-01, B-02, B-03 | CR9-D02, CR9-D09 | SPEC-024 §5 |
| B-04 | CR9-D10 | SPEC-025 §7.2 |
| B-05, H-09 | CA-06 | SPEC-025 §7.1 |
| B-06 | CR9-D06 | SPEC-025 §6.3; SPEC-024 §6 |
| B-07 | CR9-D09 | SPEC-024 §6.7-6.8 |
| B-08 | CR9-D01 | SPEC-024 §6.12; SPEC-022 |
| B-09, B-10 | CR9-D05 | SPEC-024 §6.2; SPEC-022 |
| B-11 | CA-13 | SPEC-024 §7.1 |
| B-12 | CR9-D08 | SPEC-026 §8.3 |
| B-13 | CR9-D03 | SPEC-025 §3 |
| B-14, B-15 | CA-14 | SPEC-025 §6.4 |
| B-16 | CA-04; CR-009 §5.5 | SPEC-024 §6.2; SPEC-025 §4.6; SPEC-026 §4.5 |
| B-17 | CA-04; CA-07 | SPEC-024 §6.3 |
| H-01 | CA-04 | SPEC-024 §6.2 |
| H-02 | CA-06 | SPEC-025 §4.2 |
| H-03 | CR9-D04 | SPEC-026 §3 |
| H-05, H-06 | CR9-D07 | SPEC-026 §8 |
| H-07, H-08 | CA-10 | SPEC-026 §5-6 |

## 13. Veredito

**REPROVADO para produção.**

A aplicação pode continuar em ambiente de desenvolvimento e pode receber implementação corretiva, mas não deve ser promovida até:

1. CR-009 aprovada pelo CCB;
2. SPEC-024/025/026 ratificadas;
3. todos os 17 bloqueadores fechados com teste;
4. `alembic upgrade head` reproduzível;
5. TLS ativo com cookies `Secure`;
6. aceite visual registrado em 360/768/1280;
7. auditoria de revalidação sem findings BLOQ.

## 14. Assinatura

| Papel | Nome | Data | Resultado |
|-------|------|------|-----------|
| Auditor de segurança | agent-security-auditor | 2026-11-17 | REPROVADO |
| Revisor de identidade/LGPD | agent-compliance | pendente | — |
| Aceite PO/GP | pendente | — | — |

## CHANGELOG

| Versão | Data | Autor | Mudança |
|--------|------|-------|---------|
| 1.0.0 | 2026-11-17 | agent-security-auditor | Auditoria pré-produção da CR-009; 15 bloqueadores, 12 altos, 6 médios, 10 possíveis, 6 drifts |
| 1.1.0 | 2026-11-17 | agent-security-auditor | Revisão de confirmação: B-16 (handler converte 401/403/422 em 500) e B-17 (dependência de sessão sem tipo) adicionados e reproduzidos; M-01 reclassificado; contagem corrigida para 17 BLOQ, 41 ativos, 51 total; G3 17/17; rastreabilidade e prioridade P0 atualizadas |
