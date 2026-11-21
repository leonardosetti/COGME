---
id: docs-change-requests-cr-009-crud-usuarios-dashboard-anonimo
title: CR-009 — Ciclo de vida do usuário, clientes multiempresa, dashboard e fluxo anônimo
type: change-request
version: 0.2.1
status: ativo
owner: agent-project-analyst
derived-from:
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9.1-9.3; P-03, P-14, P-15)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md (OS-01, US-004, US-016/US-017)
- .ai/specs/spec-004-backend-mvp-v1.spec.md (contrato HTTP e limites)
- .ai/specs/spec-017-identity-access-session-v1.md (identidade, HMAC, sessão, CSRF)
- .ai/specs/spec-019-client-directory-v1.md (diretório de clientes)
- .ai/specs/spec-020-simulation-invoice-history-v1.md (simulações e invoices)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.md (ciclo de vida e erase)
- .ai/specs/spec-023-ui-spec-v1.md (UI, acessibilidade e responsividade)
- docs/decisoes/adr-019-seguranca-multiusuario.md
- manifestação do PO/GP em 2026-11-17 (CRUD de usuários, dashboard e fluxo anônimo)
last-revised: '2026-11-17'
lgpd-class: sensível
tags:
- change-request
- identidade
- cadastro
- clientes
- dashboard
- anonimo
- lgpd
- gdpr
- ui
cr-number: CR-009
impacto: crítico
prazo-analise-gp: '2026-11-21'
decisao-ccb: aprovado
instrumento: GitHub Issue #68 (label `change-request`, Constitution Art. 9.3(i))
github-issue: 68
data-decisao: '2026-11-17'
decisor: GP Leonardo (CCB de membro único — TAP v3 §1.c, Premissa P7)
parent-cr: CR-002
auditoria-vinculada: docs/auditorias/aud-cr-009-2026-11-17-pre-producao.md
---

# CR-009 — Ciclo de vida do usuário, clientes multiempresa, dashboard e fluxo anônimo

## 1. Resumo

Esta CR registra a evolução do ciclo de vida do usuário do COGME em cinco frentes:

1. **Fluxo anônimo sem persistência**: qualquer visitante simula e emite uma invoice avulsa em PDF, sem conta, sem cookie de sessão e sem gravação de dados pessoais.
2. **Cadastro com identidade composta**: e-mail e senha sempre obrigatórios; CPF e/ou CNPJ opcionais, validados e independentes; a identidade de login é `(kind, HMAC-SHA-256(pepper, valor_normalizado))`; todos os identificadores informados ficam únicos e utilizáveis para login.
3. **Clientes multiempresa**: um usuário mantém zero, uma ou várias empresas clientes, nacionais ou internacionais, com isolamento por proprietário.
4. **Perfil e dashboard**: área autenticada para editar os próprios dados, gerir clientes, consultar simulações e invoices e acompanhar o estado da conta.
5. **CNPJ secundário e página Sobre**: a prestadora passa a ter mais de um CNPJ e um documento de emissão separado do login; "Sobre o COGME" deixa de ser seção da home e vira página própria, com os cards distribuídos pelo contexto de cada página.

A CR **não autoriza implementação**. Ela abre a tramitação do Art. 9.3, exige decisões do CCB/PO e só libera código depois de spec ratificada e auditoria sem bloqueadores. A CR **não inclui CRUD administrativo de usuários**, listagem administrativa, impersonação ou painel de operador.

## 2. Regra aplicável e necessidade da CR

A Emenda Constitucional E-20 (2026-11-14) já admitiu escopo multiusuário, identidade, clientes, histórico, invoice bilíngue e ciclo de vida da conta. Portanto, esta CR **não pede nova emenda de escopo**. Ela pede:

- decisão do CCB sobre o contrato de identidade composta e sobre a obrigatoriedade de e-mail;
- emenda à **SPEC-017** (identidade) e à **SPEC-019** (clientes), sem duplicação;
- emenda ao **ADR-019 §4.4**, porque o hash de identidade atual não é HMAC-SHA-256;
- separação entre identificador de login e documento de emissão da prestadora;
- correção do handler canônico de erros, que hoje converte 401/403/422 em 500;
- correção de desvios já implementados, listados na auditoria vinculada;
- spec nova para perfil/dashboard/página Sobre.

O fluxo aplicável é o de `constitution.md` Art. 9.3 e o runbook `docs/operacao/proc-cr-spec-approval-workflow.md`:

1. Issue `change-request` com label `change-request`;
2. análise de impacto e decisão CCB;
3. spec proposta → spec ratificada;
4. implementação com testes;
5. auditoria de conformidade;
6. promoção a produção.

Esta CR está na etapa 2. Nenhum item abaixo está aprovado.

## 3. Demanda declarada

| ID | Demanda | Origem |
|----|---------|--------|
| D-01 | Usuário anônimo simula e emite invoice avulsa sem cadastro e sem persistência | PO/GP 2026-11-17 |
| D-02 | E-mail e senha sempre obrigatórios; CPF e/ou CNPJ opcionais, únicos e atrelados a HMAC, utilizáveis para login | PO/GP 2026-11-17 |
| D-03 | CPF e CNPJ são independentes: um pode existir sem o outro, e ambos podem coexistir | PO/GP 2026-11-17 |
| D-04 | Usuário logado cadastra múltiplas empresas clientes, nacionais ou internacionais; zero empresas também é válido | PO/GP 2026-11-17 |
| D-05 | Usuário tem perfil e dashboard para gerir invoices, clientes, próprios dados e CNPJ secundário | PO/GP 2026-11-17 |
| D-06 | "Sobre o COGME" vira página separada, com cards distintos e bem distribuídos por contexto | PO/GP 2026-11-17 |
| D-07 | Design otimizado e sem quebra visual; aceite visual pendente | PO/GP 2026-11-17 |

## 4. Escopo proposto

### 4.1 Fluxo anônimo sem persistência

**Comportamento atual preservado:** `POST /v1/simulate` e `POST /v1/invoice` já são públicos e não gravam dados. A CR transforma esse comportamento em contrato explícito e testado.

Regras:

- `POST /v1/simulate` calcula a simulação com a cotação vigente e devolve o detalhamento; não abre transação de escrita.
- `POST /v1/invoice` recalcula a simulação no servidor e devolve PDF com `Cache-Control: no-store`; não grava invoice, cliente, simulação, usuário ou sessão.
- Nenhum cookie de sessão é criado no fluxo anônimo. O cookie CSRF pode existir, mas não é exigido para essas rotas.
- Nenhum identificador pessoal (nome, CPF, CNPJ, e-mail, endereço, valor) aparece em log.
- A resposta não depende de `client_id`, `simulation_id` ou de qualquer registro persistido.
- Limites: `POST /v1/simulate` 30/min/IP; `POST /v1/invoice` 10/min/IP. O limite é por IP real do cliente, não por IP do proxy.
- Teste de aceite compara a contagem das tabelas `users`, `clients`, `simulations`, `invoices`, `invoice_sequences` antes e depois do fluxo: nenhuma linha criada, nenhum sequencial consumido.

**Fora de escopo:** numeração oficial de invoice anônima. O número exibido no PDF é informado pelo usuário e não é reservado em `invoice_sequences`.

### 4.2 Cadastro com identidade composta

Contrato canônico:

```json
POST /v1/auth/register
{
  "name": "Nome Completo",
  "email": "usuario@exemplo.com",
  "password": "senha-com-8-a-128-caracteres",
  "cpf": "12345678901",
  "cnpj": "12345678000195"
}
```

- `email`, `password` e `name` são **sempre** obrigatórios.
- `cpf` e `cnpj` são opcionais, independentes e podem coexistir. Cada campo, quando presente, é normalizado, validado e gera um identificador de login próprio.
- CPF e CNPJ passam por normalização (somente dígitos), rejeição de sequências repetidas e validação dos dígitos verificadores.
- E-mail passa por `trim`, lowercase e validação de formato; tamanho máximo 255.
- Senha usa Argon2id; nunca é gravada em claro nem logada.
- A transação de cadastro é atômica: `users` + `user_login_identifiers` + `provider_profiles` + `provider_cnpjs` (quando houver CNPJ). Falha em qualquer etapa desfaz tudo.
- Cada identificador informado gera uma linha em `user_login_identifiers` com `lookup_hmac = HMAC-SHA-256(login_pepper, kind + ":" + valor_normalizado)`.
- Unicidade: `UNIQUE (kind, lookup_hmac)` para identificadores ativos. Conflito de e-mail, CPF ou CNPJ retorna `409 conflict`, sem revelar qual campo colidiu.
- O login aceita qualquer identificador ativo do usuário: e-mail, CPF ou CNPJ.
- CPF/CNPJ de login são **imutáveis** após o cadastro. Não existe rota de autoatendimento para adicionar ou trocar identificador de login.
- Correção de erro de digitação é operação de suporte, via CLI com valor lido de stdin, `--dry-run` obrigatório e registro em `identity_change_log` sem PII.
- A conta nasce com `email_verified_at = NULL` e só autentica depois da verificação de posse do e-mail. Reenvio e confirmação usam token de uso único com TTL de 24 horas.
- O campo legado `identifier` continua aceito por 90 dias apenas quando contém e-mail. CPF/CNPJ em `identifier` retorna `400 validation_error` pedindo `email` explícito.
- O CNPJ informado no cadastro vira o CNPJ primário da prestadora e é espelhado em `provider_profiles.cnpj`; o CPF é espelhado em `users.cpf` e `provider_profiles.cpf`.

**Legado:** contas antigas cadastradas só com CNPJ têm `users.email = NULL`. A CR exige uma estratégia de completude (decisão CR9-D01), não um backfill inventado. Contas antigas com e-mail são consideradas verificadas na migration; somente contas novas passam pelo duplo opt-in.

### 4.3 Clientes multiempresa, nacionais e internacionais

- Um usuário pode ter **zero** clientes. Zero clientes é estado válido e não bloqueia o dashboard.
- A emissão de invoice aceita `client_id` **ou** `client_fictitious=true` com os dados do cliente no payload. O primeiro caminho usa o registro persistido; o segundo não persiste cliente.
- Um usuário pode ter N clientes. O limite operacional proposto é 100 clientes ativos por usuário, para conter abuso; acima disso, erro `422`.
- Cliente nacional (`country_code = "BR"`): `tax_id` obrigatório, CPF (11) ou CNPJ (14) com dígitos verificadores válidos.
- Cliente internacional (`country_code != "BR"`): `country_code` validado contra a tabela `countries` (ISO 3166-1 alpha-2); `tax_id` opcional, até 32 caracteres, tipo `foreign`; sem documento, tipo `none`; `name` obrigatório; `address` obrigatório quando não houver `email`.
- `email` e `phone` do cliente são persistidos e usados na invoice quando presentes. Hoje são aceitos no schema e descartados na criação; isso é corrigido.
- Duplicidade por proprietário: `(owner_user_id, tax_id_digits)` quando `tax_id_digits` não é nulo; conflito retorna `409 conflict`, nunca `500`.
- Toda leitura, edição, ativação e inativação filtra por `owner_user_id` da sessão. Recurso de outro dono retorna `404`.
- A UI de clientes tem estado vazio explícito, formulário nacional/internacional, lista com busca por nome/documento/país e ação de inativar/reativar.
- Listas de clientes, invoices e simulações usam o envelope `{items,total,limit,offset}`; o dashboard usa `total` para os contadores, sem endpoint de agregação novo.
- A emissão persistida valida o emissor contra os documentos de emissão da prestadora: CPF em `provider_profiles.cpf` ou CNPJ ativo em `provider_cnpjs`. Identificador de login não é documento de emissão.

### 4.4 Perfil e dashboard

Rotas de frontend novas, server-side, com guarda de sessão:

| Rota | Conteúdo | Sem sessão |
|------|----------|------------|
| `/dashboard` | resumo de invoices por status, últimas invoices, últimas simulações, total de clientes, pendências de perfil | redireciona para `/auth/login?next=/dashboard` |
| `/perfil` | nome, e-mail, telefone, identificadores mascarados, troca de senha, troca de e-mail, estado da conta | idem |
| `/clientes` | CRUD de clientes multiempresa | idem |
| `/sobre` | página pública "Sobre o COGME" | pública |

Contratos de backend:

- `GET /v1/auth/me` devolve `id`, `name`, `email`, `email_verified`, `phone`, `status`, `created_at`, `identifiers` mascarados, `documents` de emissão e `profile_completion_required`.
- `PATCH /v1/auth/me` altera `name` e `phone`; exige sessão e CSRF.
- `PUT /v1/auth/me/email` exige senha atual, valida unicidade, aposenta o identificador antigo e cria o novo na mesma transação; exige CSRF.
- `PUT /v1/auth/me/password` exige senha atual, aplica Argon2id e revoga as outras sessões; exige CSRF.
- `POST /v1/auth/email/verify` consome token de verificação e marca `email_verified_at`.
- `POST /v1/auth/email/resend` reenvia verificação com resposta genérica e rate limit.
- O dashboard usa os endpoints existentes (`/v1/invoices`, `/v1/simulations`, `/v1/clients`) com `limit=5` e lê `total` do envelope; não cria endpoint de agregação novo.
- A navbar passa a refletir a sessão: visitante vê Entrar/Cadastre-se; autenticado vê Dashboard, Clientes, Perfil e Sair.
- "Sair" envia `POST /v1/auth/logout` com `X-CSRF-Token` e recarrega a home.
- As rotas de perfil e dashboard só renderizam depois de validar a sessão e o status do usuário; 401/403 do backend são propagados corretamente, nunca convertidos em 500.

### 4.5 CNPJ secundário e documentos de emissão da prestadora

- **Identificador de login** e **documento de emissão** são conceitos separados. `user_login_identifiers` guarda a chave da conta; `provider_profiles.cpf` e `provider_cnpjs` guardam os documentos usados na invoice.
- Nova tabela `provider_cnpjs` (1:N com `users`), com `cnpj` único, `label`, `is_primary` e `status`.
- O CNPJ informado no cadastro é migrado para `provider_cnpjs` como primário; sem CNPJ no cadastro, o primeiro CNPJ adicionado no perfil vira primário.
- A migration 0010 também importa CNPJs legados de `user_login_identifiers.kind='cnpj'`, porque o cadastro antigo não gravava `provider_profiles.cnpj`.
- Um usuário pode manter até 10 CNPJs ativos, com no máximo um primário.
- `provider_profiles.category` passa a ser nullable e aceita `individual`, `mei` e `legal_entity`. Categoria é definida no perfil; `individual` exige CPF de emissão, `mei` e `legal_entity` exigem CNPJ.
- Cadastro, edição, remoção e troca de primário passam por validação de dígitos verificadores e normalização.
- A emissão de invoice com `issuer_tax_id_digits` exige documento de emissão ativo do usuário. CNPJ de outro usuário retorna `403 issuer_not_allowed`, nunca é aceito no snapshot.
- Correção de CNPJ: sem invoice finalizada, substitui o registro; com invoice finalizada, mantém o CNPJ antigo como `inactive` e adiciona o novo. Clone com emissor inativo retorna `409 issuer_inactive`.
- A UI de perfil lista os CNPJs, permite adicionar secundário, definir primário e informar o CPF de emissão.

### 4.6 Página Sobre e correção do design system

- `index.html` deixa de conter a seção `#sobre`.
- Nova rota `/sobre` e template `sobre.html`, com conteúdo distribuído por contexto:
  - **Home**: produto, features, simulador, CTA.
  - **Sobre**: história, princípios, stack, qualidade, equipe, linha do tempo e privacidade.
- Navbar e footer apontam para `/sobre`; não resta nenhum `href="/#sobre"`.
- Cards do Sobre são autocontidos, sem aninhamento, com alturas iguais por linha e empilhamento correto em 360 px, 768 px e 1280 px.
- O CSS `app-ifit.css` passa a definir os tokens que hoje usa sem definir: `--space-1..16`, `--fs-xs..4xl`, `--radius-full`. A ausência desses tokens é a causa raiz do layout quebrado.
- Fontes remotas do Google são removidas. A pilha local é `Inter, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`; nenhum recurso remoto é carregado.
- Scripts inline são externalizados para `static/js/`; o CSP de produção passa a permitir `script-src 'self'`.
- Headers de segurança no proxy: CSP, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`; HSTS somente quando TLS estiver ativo.

## 5. Modelo de dados e contratos

### 5.1 Identidade

Sem tabela nova de login. Ajustes:

| Objeto | Situação | Ação |
|--------|----------|------|
| `users.email` | nullable, índice parcial único | novas contas sempre preenchem; legado NULL tratado por decisão CR9-D01 |
| `users.email_verified_at` | não existe | nova coluna; contas antigas com e-mail são grandfatherizadas na migration |
| `users.cpf` | `CHAR(11)`, nullable, índice parcial único | espelho legado do CPF de login; CNPJ continua só em `user_login_identifiers` |
| `user_login_identifiers` | `(kind, lookup_hmac)`, `retired_at` | fonte única de login; `lookup_hmac` passa a HMAC-SHA-256 real |
| `email_verification_tokens` | não existe | nova tabela: `user_id`, `token_hash`, `expires_at`, `used_at`; TTL 24h |
| `identity_change_log` | não existe | auditoria de correção de identificador: `user_id`, `kind`, `actor`, `ticket_ref`, `old_hmac`, `new_hmac`, `created_at`; sem valores em claro |
| `users.internal_username_hash` | SHA-256 sem sal do identificador | substituir por HMAC-SHA-256(pepper, UUID aleatório); backfill via CLI pós-migration |
| `provider_profiles.cpf` | não existe | novo documento de emissão do titular, separado do login |
| índices `uq_users_email_partial`, `uq_users_cpf_partial` | existem | manter como defesa em profundidade |

### 5.2 Clientes

| Campo | Hoje | Proposto |
|-------|------|----------|
| `tax_id_digits` | `CHAR(14) NOT NULL` | `VARCHAR(32) NULL`; validação por país |
| `tax_id_type` | `cpf`/`cnpj` inferido pelo tamanho | `cpf`, `cnpj`, `foreign`, `none`; CHECK no banco |
| `email`, `phone` | existem, mas `create_client` descarta | persistir e devolver |
| `country_code` | `CHAR(2)` default BR, sem validação | FK/lookup em `countries` (ISO 3166-1) |
| unicidade | `(owner_user_id, tax_id_digits)` | índice parcial `WHERE tax_id_digits IS NOT NULL` |
| duplicidade | `IntegrityError` vira 500 | `409 conflict` com `ErrorKey.CONFLICT` |

CHECK adicional:

```sql
CHECK (
  (country_code = 'BR' AND tax_id_type IN ('cpf', 'cnpj'))
  OR
  (country_code <> 'BR' AND tax_id_type IN ('foreign', 'none'))
)
```

### 5.3 CNPJs da prestadora

```sql
CREATE TABLE provider_cnpjs (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    cnpj CHAR(14) NOT NULL,
    label VARCHAR(80),
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    status VARCHAR(16) NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'inactive')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_provider_cnpjs_cnpj UNIQUE (cnpj)
);
CREATE UNIQUE INDEX uq_provider_cnpjs_primary
    ON provider_cnpjs (user_id)
    WHERE is_primary AND status = 'active';

ALTER TABLE provider_profiles
    ALTER COLUMN category DROP NOT NULL;
ALTER TABLE provider_profiles
    DROP CONSTRAINT chk_provider_category;
ALTER TABLE provider_profiles
    ADD CONSTRAINT chk_provider_category
    CHECK (category IS NULL OR category IN ('individual', 'mei', 'legal_entity'));

ALTER TABLE provider_profiles
    ADD COLUMN cpf CHAR(11) NULL;
CREATE UNIQUE INDEX uq_provider_profiles_cpf
    ON provider_profiles (cpf)
    WHERE cpf IS NOT NULL;
```

Categoria `individual` exige CPF de emissão; `mei` e `legal_entity` exigem CNPJ. A validação é de aplicação porque cruza tabelas.

### 5.4 Endpoints novos ou alterados

| Método | Rota | Auth | Mudança |
|--------|------|------|---------|
| POST | `/v1/auth/register` | pública | e-mail obrigatório; `cpf`/`cnpj` opcionais; `202` com verificação pendente; 409 em duplicidade |
| POST | `/v1/auth/login` | pública | login por qualquer identificador ativo; 403 `account_dormant`; 403 `email_unverified` |
| POST | `/v1/auth/logout` | sessão + CSRF | deixa de ser isento de CSRF |
| GET | `/v1/auth/me` | sessão | inclui telefone, `email_verified`, identificadores mascarados, documentos e completude |
| PATCH | `/v1/auth/me` | sessão + CSRF | nome e telefone |
| PUT | `/v1/auth/me/email` | sessão + CSRF | troca de e-mail com senha e transação de identificadores |
| PUT | `/v1/auth/me/password` | sessão + CSRF | troca de senha e revogação das outras sessões |
| POST | `/v1/auth/email/verify` | pública | consome token e marca e-mail verificado |
| POST | `/v1/auth/email/resend` | pública | reenvia verificação com resposta genérica |
| GET/POST | `/v1/clients` | sessão (+CSRF no POST) | cliente nacional/internacional; email/phone; 409; envelope de lista |
| GET/PUT | `/v1/clients/{id}` | sessão (+CSRF no PUT) | detalhe e edição; 404 cross-owner |
| POST | `/v1/clients/{id}/activate` e `/deactivate` | sessão + CSRF | ativação e inativação |
| GET/POST | `/v1/provider/cnpjs` | sessão (+CSRF no POST) | lista/cria CNPJ secundário |
| PUT/DELETE | `/v1/provider/cnpjs/{id}` | sessão + CSRF | edita/remove CNPJ; troca de primário |
| PUT | `/v1/provider/profile` | sessão + CSRF | CPF de emissão, categoria e dados da prestadora |
| POST | `/v1/invoices` | sessão + CSRF | valida dono de cliente/simulação, deriva snapshot e valida emissor |
| GET | `/v1/invoices` | sessão | envelope `{items,total,limit,offset}` |
| GET | `/v1/invoices/{id}` | sessão | PDF escopado por proprietário |
| POST | `/v1/invoices/{id}/finalize` | sessão + CSRF | finaliza invoice |
| POST | `/v1/invoices/{id}/clone` | sessão + CSRF | clona draft; emissor inativo retorna 409 |
| DELETE | `/v1/invoices/{id}` | sessão + CSRF | remove draft |
| GET | `/v1/simulations` | sessão | envelope `{items,total,limit,offset}` |
| POST | `/v1/account/reactivate` | pública com credenciais | reativação sem sessão válida (decisão CR9-D05) |

### 5.5 Contrato de erro

O handler canônico precisa mapear todos os status, não apenas 400/404/405/409:

| Status | `error.key` | Uso |
|--------|-------------|-----|
| 400 | `validation_error` | formato, dígito verificador, país inválido |
| 401 | `unauthorized` | credenciais inválidas ou sessão ausente |
| 403 | `forbidden` | operação não permitida sem chave específica |
| 403 | `account_dormant` | conta não ativa |
| 403 | `email_unverified` | e-mail ainda não verificado |
| 403 | `profile_incomplete` | perfil obrigatório incompleto |
| 403 | `issuer_not_allowed` | emissor inexistente ou de outro proprietário |
| 404 | `not_found` | recurso inexistente **ou de outro proprietário** |
| 409 | `conflict` | e-mail, CPF, CNPJ, cliente ou CNPJ da prestadora duplicado |
| 409 | `issuer_inactive` | clone com emissor inativo |
| 422 | `limit_exceeded` | limite de clientes/CNPJs excedido |
| 429 | `rate_limited` | limite por IP/rota |
| 500 | `internal_error` | falha inesperada, sem vazar detalhe |

Chaves específicas são levantadas como `DomainError`; o handler HTTP genérico não pode convertê-las em `internal_error`.

## 6. Decisões requeridas do CCB/PO

| ID | Decisão | Recomendação | Responsável |
|----|---------|--------------|-------------|
| **CR9-D01** | Contas legadas com `email = NULL`: completar no próximo login (bloqueante para escritas) ou manter login por CNPJ e solicitar e-mail de forma não bloqueante? | Bloqueante para escritas, com tela de completude e prazo de 30 dias antes de dormência; login por CPF/CNPJ continua | CCB/PO |
| **CR9-D02** | Identidade composta: `cpf` e `cnpj` são campos separados, opcionais, independentes e podem coexistir? | Sim; ambos opcionais, e-mail sempre presente; identificadores de login imutáveis e sem autoatendimento para adicionar depois | CCB |
| **CR9-D03** | Cliente internacional: `tax_id` opcional e `country_code` ISO 3166-1; para BR, documento obrigatório com dígito verificador | Aprovar; `foreign` com até 32 caracteres; sem documento, `none` | CCB/PO |
| **CR9-D04** | CNPJ secundário: nova tabela `provider_cnpjs`, limite de 10 ativos, um primário; CNPJ do cadastro vira primário | Aprovar; migrar `provider_profiles.cnpj` e CNPJs legados de `user_login_identifiers`; emendar a SPEC-018 para deixar claro que CNPJ secundário é dado empresarial, **não** identificador de login e **não** rotaciona alias HMAC | CCB |
| **CR9-D05** | Reativação de conta dormente: `POST /v1/account/reactivate` com identificador + senha, sem sessão | Aprovar; mesma verificação e rate limit do login | CCB/Segurança |
| **CR9-D06** | Troca de e-mail: exige senha atual, aposenta identificador antigo e revoga outras sessões? | Sim; e-mail antigo deixa de logar imediatamente | CCB/Segurança |
| **CR9-D07** | Página Sobre: conteúdo próprio e remoção da seção inline; links antigos `/#sobre` passam a `/sobre` | Aprovar; sem redirect de fragmento | PO |
| **CR9-D08** | Cookies `Secure`: produção exige HTTPS; desenvolvimento local pode usar `COGME_COOKIE_SECURE=false` | Aprovar; TLS obrigatório em produção | CCB/DevOps |
| **CR9-D09** | Entrega de e-mail transacional (reset, verificação e boas-vindas): SMTP próprio no container, com fallback de desenvolvimento para arquivo local | Aprovar; sem provedor cloud; verificação de e-mail usa o mesmo SMTP | CCB/PO |
| **CR9-D10** | Numeração de invoice multi-emissor: manter `INV-YYYYMM-NNNN` por emissor e trocar o unique global por `(issuer_tax_id_digits, invoice_number)` | Aprovar; corrige colisão entre usuários | CCB |
| **CR9-D11** | Limites operacionais: 100 clientes ativos e 10 CNPJs ativos por usuário | Aprovar defaults configuráveis por ambiente | CCB/PO |
| **CR9-D12** | Verificação de posse do e-mail antes do login, com duplo opt-in e grandfather para contas existentes | Aprovar; token de 24h, reenvio com rate limit, reset confirmado também verifica | CCB/Segurança |
| **CR9-D13** | Correção de CPF/CNPJ de login: somente suporte, via CLI com valor em stdin, dry-run e auditoria sem PII | Aprovar; sem autoatendimento no MVP | CCB/Segurança |
| **CR9-D14** | Categoria da prestadora nullable (`individual`, `mei`, `legal_entity`), definida no perfil | Aprovar; remover hardcode `mei` do cadastro | CCB/PO |
| **CR9-D15** | Separar identificador de login de documento de emissão: `user_login_identifiers` para conta; `provider_profiles.cpf` + `provider_cnpjs` para invoice | Aprovar; resolve usuário cadastrado só com e-mail que depois precisa emitir | CCB |

## 7. Artefatos afetados

**Backend**

- `src/backend/models/user.py`, `src/backend/models/client.py`, `src/backend/models/provider.py`
- `src/backend/routers/auth.py`, `clients.py`, `provider.py`, `account.py`, `invoices.py`, `simulations.py`
- `src/backend/schemas/auth.py`, `src/backend/schemas/invoice.py`
- `src/backend/middleware/csrf.py`, `session.py`, `rate_limit.py`
- `src/backend/main.py`, `src/backend/config.py`, `src/backend/errors.py`
- `src/backend/cli/` (correção de identificador e backfill de hash interno)
- `src/shared/schemas.py` (`ErrorKey` com `unauthorized`, `forbidden`, `rate_limited`, `account_dormant`, `email_unverified`, `profile_incomplete`, `issuer_not_allowed`, `issuer_inactive`, `limit_exceeded`)

**Banco**

- `migrations/versions/0009_fix_users_nullable_email_cpf.py` (corrigir revision id e índices)
- nova migration `0010_provider_cnpjs_and_client_international.py`
- nova migration `0011_invoice_number_unique_per_issuer.py`
- nova migration `0012_email_verification_and_issuer_documents.py` (`email_verified_at`, `email_verification_tokens`, `identity_change_log`, `provider_profiles.cpf`, categoria nullable)
- grandfather: `UPDATE users SET email_verified_at = created_at WHERE email IS NOT NULL`
- backfill de `provider_cnpjs` a partir de `provider_profiles.cnpj` e `user_login_identifiers.kind='cnpj'`

**Frontend**

- `src/frontend/app.py` (rotas `/dashboard`, `/perfil`, `/clientes`, `/sobre`, guarda de sessão)
- `src/frontend/templates/base.html`, `_navbar.html`, `_footer.html`, `index.html`
- novos `dashboard.html`, `perfil.html`, `clientes.html`, `sobre.html`, `auth/reset.html`, `auth/verify-email.html`
- `src/frontend/static/css/app-ifit.css` (tokens e cards)
- `src/frontend/static/js/` (externalizar scripts inline e enviar CSRF)

**Infra**

- `infra/nginx/default.conf` (CSP, Permissions-Policy, HSTS condicional)
- `docker-compose.yml` / `Dockerfile` (`--proxy-headers`, `--forwarded-allow-ips`)
- `docs/especificacoes/spec-prop-024..026`, `.ai/specs/spec-017/019/020` (emendas)
- `docs/decisoes/adr-019-seguranca-multiusuario.md` (emenda §4.4)

**Testes**

- unidade: HMAC, normalização, dígitos verificadores, máscaras, tokens, HMAC de UUID;
- integração: cadastro com `email`, `email+cpf`, `email+cnpj`, `email+cpf+cnpj`, duplicidade 409, verificação de e-mail, correção auditada, clientes multiempresa, cross-owner 404, CNPJ secundário, documentos de emissão, numeração multi-emissor, envelopes de lista, handler 401/403/422/429;
- e2e: anônimo sem sessão e sem persistência, verificação de e-mail, dashboard/perfil/clientes, Sobre em três viewports, navbar autenticada;
- segurança: zero PII em log, CSRF, rate limit, cookies, revogação de sessão, CLI sem PII em argv.

## 8. Avaliação

A CR só entra em implementação depois de aprovada pelo CCB e com as três specs ratificadas. A avaliação segue quatro dimensões.

| Dimensão | Pergunta | Evidência exigida |
|----------|----------|-------------------|
| Correção funcional | Os cinco escopos funcionam ponta a ponta? | testes de integração e e2e verdes; CAs 01–13 |
| Segurança e privacidade | Nenhuma PII vaza, sessão é revogável e CSRF cobre mutações? | testes de segurança; revisão de log; CAs 11 e 12 |
| Compatibilidade | Banco existente migra, contas legadas continuam e rollback funciona? | `alembic upgrade head` em banco existente; CA-13; rollback ensaiado |
| Experiência | Fluxos são compreensíveis e o layout não quebra? | aceite visual em 360/768/1280; CA-10 |

Baseline atual, medido em 2026-11-17 (registrar antes do primeiro commit da CR):

| Métrica | Baseline | Meta |
|---------|----------|------|
| Suíte total | `9 failed, 1455 passed, 37 skipped, 18 errors` | 0 `failed`, 0 `errors`; `passed` não regride |
| Cobertura de linhas | valor do relatório de cobertura no commit-base | não regride |
| Bloqueadores abertos na auditoria | 17 | 0 |
| Altos abertos | 12 | 0 |
| Médios abertos | 6 | 0 ou aceitos com justificativa do CCB |
| Rotas do contrato de erro exercitadas | 400/404/405/409 | 400/401/403/404/405/409/422/429 |
| Viewports do aceite visual | nenhum | 360, 768 e 1280 px |

A avaliação é uma das condições de encerramento. Se uma métrica não atingir a meta, a CR fica aberta com finding registrado na auditoria; não se aceita "verde parcial".

## 9. Specs propostas

| Spec | Escopo | Relação |
|------|--------|---------|
| **SPEC-024** | Identidade composta, cadastro, login, reset, perfil e hash | Emenda à SPEC-017 |
| **SPEC-025** | Clientes multiempresa nacionais/internacionais + fluxo anônimo sem persistência | Emenda à SPEC-019 e SPEC-020 |
| **SPEC-026** | Perfil, dashboard, CNPJ secundário e página Sobre + design system | Emenda à SPEC-018 e SPEC-023 |

As propostas estão em:

- `docs/especificacoes/spec-prop-024-identidade-composta-e-cadastro.md`
- `docs/especificacoes/spec-prop-025-clientes-multiempresa-e-fluxo-anonimo.md`
- `docs/especificacoes/spec-prop-026-perfil-dashboard-e-pagina-sobre.md`

## 10. Critérios para encerrar a CR

- **CA-01** Fluxo anônimo: simular e emitir invoice não cria linha em nenhuma tabela e não consome `invoice_sequences`.
- **CA-02** Cadastro funciona com `email`, `email+cpf`, `email+cnpj` e `email+cpf+cnpj`; `email`, `password` e `name` são obrigatórios nos quatro casos.
- **CA-03** CPF/CNPJ inválidos (dígito verificador) retornam `400 validation_error`; duplicados retornam `409 conflict`.
- **CA-04** Login funciona com qualquer identificador ativo do usuário e falha com credenciais erradas sem revelar existência.
- **CA-05** Usuário com zero clientes opera o dashboard e emite invoice com cliente fictício.
- **CA-06** Usuário cria, lista, edita e inativa clientes nacionais e internacionais; outro usuário recebe `404` em todos os acessos.
- **CA-07** Perfil altera nome, telefone, e-mail e senha; troca de e-mail invalida o login antigo; troca de senha revoga outras sessões.
- **CA-08** CNPJ secundário é criado, listado, promovido a primário e removido; CNPJ de outro usuário não pode ser usado como emissor.
- **CA-09** Duas contas distintas emitem a primeira invoice no mesmo mês sem colisão de numeração.
- **CA-10** `/sobre` é página própria; nenhum link `/#sobre` resta; cards não quebram em 360/768/1280 px.
- **CA-11** Nenhum log contém e-mail, CPF, CNPJ, nome, endereço ou valor de invoice.
- **CA-12** CSRF funciona no frontend (header presente) e logout deixa de ser isento.
- **CA-13** `alembic upgrade head` roda do zero e em banco existente; revision id cabe em `varchar(32)`.
- **CA-14** Suíte completa verde, incluindo os novos testes de segurança e e2e; cobertura não regride frente ao baseline da §8.
- **CA-15** Auditoria `aud-cr-009-2026-11-17-pre-producao.md` sem findings `BLOQ` abertos.
- **CA-16** Usuário cadastrado só com e-mail consegue definir `provider_profiles.cpf` ou adicionar CNPJ no perfil e emitir invoice persistida; identificador de login não é exigido como documento de emissão.
- **CA-17** Conta nova não autentica antes de verificar o e-mail; conta antiga com e-mail entra sem verificação forçada (grandfather). Reset confirmado também marca o e-mail como verificado.
- **CA-18** Correção de CPF/CNPJ via CLI lê o valor de stdin, `--dry-run` imprime apenas máscara e `identity_change_log` grava HMAC, nunca o valor.
- **CA-19** Migration importa CNPJs legados de `provider_profiles.cnpj` e de `user_login_identifiers.kind='cnpj'`; nenhum usuário legado perde a capacidade de emitir.
- **CA-20** Clone de invoice cujo emissor foi inativado retorna `409 issuer_inactive`; invoice histórica mantém o snapshot do emissor original.

## 11. Rollback

1. Reverter deploy da aplicação para a imagem/tag anterior.
2. Reverter migrations na ordem inversa; `0010`, `0011` e `0012` têm `downgrade` testado.
3. Restaurar `uq_invoices_invoice_number` somente após garantir que não há duplicidade entre emissores.
4. Restaurar `users.email`/`users.cpf` NOT NULL apenas se não houver contas legadas com NULL; caso contrário, manter nullable.
5. Reverter rotas de frontend e navbar para o estado anterior; `/#sobre` volta a apontar para a seção inline.
6. Revogar todas as sessões emitidas durante a janela de rollback.
7. Desativar o envio de e-mail de verificação e restaurar o cadastro antigo; contas criadas na janela sem verificação são removidas ou completadas por suporte.
8. Manter `provider_cnpjs` e `provider_profiles.cpf` se o rollback for apenas de aplicação; o código antigo ignora as colunas novas.

## 12. Riscos e dependências

| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| Migração de contas legadas sem e-mail | usuário não completa login | decisão CR9-D01 + tela de completude + prazo |
| Colisão de numeração entre emissores | invoice não grava | unique composto + teste com dois emissores |
| `Secure` cookie sobre HTTP | login não persiste | TLS em produção; flag de dev |
| Reset/verificação sem SMTP | conta inacessível | SMTP próprio + fallback local |
| CSP com scripts inline | quebra de UI | externalizar JS antes de ativar CSP rígido |
| Design tokens ausentes | layout quebrado | definir tokens + teste visual |
| Rate limit em memória | burla ao escalar workers | documentar limite; migrar para Redis em onda futura |
| Dados bancários em texto simples | violação P-15 | débito já registrado; criptografar antes de produção |
| Handler de erro converte 401/403/422 em 500 | contrato quebrado e diagnóstico falso | B-16 corrigido antes de qualquer tela nova |
| Dependency de sessão sem tipo vira query param | `/me` e rotas irmãs inutilizáveis | B-17 corrigido com dependency tipada única |
| Migration 0009 com revision id de 35 caracteres | `alembic upgrade` falha | reduzir para 32 caracteres e testar do zero |
| Backfill de `provider_cnpjs` incompleto | usuário legado perde emissão | importar das duas fontes e validar contagem antes/depois |
| E-mail de verificação em massa no deploy | pico de SMTP e fila | grandfather de contas existentes; envio só para contas novas |
| CNPJ corrigido com invoice finalizada | histórico perde emissor | manter CNPJ antigo inativo e bloquear clone com 409 |

## 13. LGPD e privacidade

| Item | Decisão |
|------|---------|
| Base legal do cadastro | execução de contrato (Art. 7º, V) para conta e autenticação; obrigação legal (Art. 7º, II) para guarda fiscal de invoices |
| Dados de clientes | o usuário é controlador; o COGME atua como operador e só processa conforme instrução |
| Minimização | CPF/CNPJ de login são opcionais; documento de emissão só é exigido para emitir invoice persistida |
| Retenção | identificadores de login ficam enquanto a conta existir; invoices seguem prazo fiscal; `identity_change_log` guarda HMAC e metadados, nunca o valor |
| Direitos do titular | acesso e correção pelo perfil; exclusão pela rota de conta; correção de identificador de login via suporte com trilha |
| Segurança | HMAC com pepper para busca, Argon2id para senha, TLS em produção, log sem PII, sessão revogável |
| Transferência internacional | não há; SMTP e banco ficam na infraestrutura do projeto |
| Encarregado | contato publicado na página Sobre e no rodapé |

## CHANGELOG

| Versão | Data | Autor | Mudança |
|--------|------|-------|---------|
| 0.1.0 | 2026-11-17 | agent-project-analyst | Criação da CR-009 com escopo, decisões CCB, contratos, critérios e rollback |
| 0.2.0 | 2026-11-17 | agent-project-analyst | Correções da rodada de revisão: identidade composta com `cpf`/`cnpj`, verificação de e-mail com grandfather, CLI com valor em stdin, documento de emissão separado do login (CR9-D15), backfill de CNPJ legado, clone com emissor inativo, §8 Avaliação com baseline, CAs 16–20, §13 LGPD e riscos B-16/B-17 |
| 0.2.1 | 2026-11-17 | agent-project-analyst | Instrumento de CCB aberto: GitHub Issue #68 (`change-request`, Art. 9.3(i)) com as decisões CR9-D01..D15 para aprovação ou rejeição |
