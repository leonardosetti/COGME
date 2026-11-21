---
id: docs-especificacoes-spec-prop-024-identidade-composta-e-cadastro
title: Proposta de Spec — Identidade composta, cadastro, login e recuperação
type: spec
version: 0.2.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-009-crud-usuarios-dashboard-anonimo.md
- .ai/specs/spec-017-identity-access-session-v1.md (emenda)
- .ai/specs/spec-022-account-lifecycle-privacy-v1.md (dependência)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md
- docs/decisoes/adr-017-dependencia-argon2id.md
- docs/decisoes/adr-019-seguranca-multiusuario.md (§4.4)
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-03, P-14, P-15)
- docs/auditorias/aud-cr-009-2026-11-17-pre-producao.md
last-revised: '2026-11-17'
lgpd-class: sensível
tags:
- proposta
- spec
- identidade
- cadastro
- autenticacao
- seguranca
- lgpd
proposal-id: PROP-024
rastreia-req:
- CR-009
- CR9-D01
- CR9-D02
- CR9-D06
- CR9-D09
- CR9-D12
- CR9-D13
- CR9-D15
- CA-02
- CA-03
- CA-04
- CA-07
- CA-11
- CA-14
- CA-16
- CA-17
- CA-18
- CA-19
testes-vinculados: []
---

# Proposta de Spec — Identidade composta, cadastro, login e recuperação

## 1. Ideia / Draft

Esta proposta emenda a **SPEC-017** para tornar explícito o contrato de identidade composta pedido na CR-009:

- toda conta tem **e-mail e senha**;
- CPF e CNPJ são identificadores opcionais, validados e únicos;
- o login aceita qualquer identificador ativo;
- o servidor guarda apenas HMAC dos identificadores, nunca o valor em claro;
- a conta só existe depois de uma transação completa;
- a recuperação de senha passa a ter entrega real de e-mail.

Ela **não substitui** a SPEC-017. Onde houver conflito, esta emenda prevalece; o restante da SPEC-017 continua vigente.

## 2. Derivação e limites

### 2.1 O que muda

| Tema | SPEC-017 vigente | Emenda proposta |
|------|------------------|-----------------|
| Identificador de cadastro | um entre e-mail, CPF ou CNPJ | e-mail sempre; CPF e CNPJ opcionais, independentes e cumulativos |
| `users.email` | NOT NULL | obrigatório para novas contas; nullable apenas para legado |
| `users.cpf` | NOT NULL | nullable; espelho do CPF quando informado |
| Verificação de e-mail | não existe | `email_verified_at` + token de duplo opt-in |
| Documento de emissão | confundido com login | `provider_profiles.cpf` e `provider_cnpjs`, separados do login |
| Hash de identificador | HMAC-SHA-256 | HMAC-SHA-256 com mensagem `kind:valor` e pepper ≥ 32 bytes |
| `internal_username_hash` | HMAC de UUID | mantido, com HMAC real e UUID aleatório |
| Senha | Argon2id | Argon2id obrigatório, sem fallback silencioso em produção |
| Reset | token gerado | token entregue por SMTP e tela de confirmação |
| Perfil | somente leitura | edição de nome, telefone, e-mail e senha |

### 2.2 O que não muda

- CPF/CNPJ de **login** são imutáveis após o cadastro; documento de emissão é outro conceito.
- Sessão é token opaco, hash SHA-256 com pepper, cookie HttpOnly/Secure/SameSite=Lax.
- CSRF é double-submit; logout deixa de ser isento.
- Zero PII em log.
- Isolamento por proprietário (P-14).
- Contas dormentes não autenticam; a reativação é tratada na SPEC-022/CR9-D05.

### 2.3 Fora de escopo

- Login social, 2FA, passkeys.
- Alteração de CPF/CNPJ de login pelo próprio usuário; correção é operação de suporte.
- Migração automática de senhas legadas para Argon2id em lote; a rehash ocorre no próximo login bem-sucedido.
- Scheduler de limpeza de contas não verificadas; a limpeza é preguiçosa no cadastro/reenvio.

## 3. Modelo de dados

### 3.1 `users`

| Coluna | Tipo | Regra |
|--------|------|-------|
| `id` | BIGINT PK | — |
| `internal_username_hash` | VARCHAR(64) | HMAC-SHA-256(pepper, UUID4), único |
| `name` | VARCHAR(120) | obrigatório, 1..120 |
| `email` | VARCHAR(255) | obrigatório para novas contas; lowercase; único parcial |
| `email_verified_at` | TIMESTAMPTZ | NULL = não verificado; grandfather para contas antigas com e-mail |
| `phone` | VARCHAR(30) | opcional |
| `cpf` | CHAR(11) | opcional; só dígitos; único parcial |
| `password_hash` | VARCHAR(255) | Argon2id encoded |
| `status` | VARCHAR(16) | `active`, `dormant`, `deleted` |
| `created_at`, `updated_at` | TIMESTAMPTZ | — |

Índices:

```sql
CREATE UNIQUE INDEX uq_users_email_partial ON users (email) WHERE email IS NOT NULL;
CREATE UNIQUE INDEX uq_users_cpf_partial   ON users (cpf)   WHERE cpf   IS NOT NULL;
```

`users.email` e `users.cpf` são **espelhos de compatibilidade**. A fonte de verdade do login é `user_login_identifiers`.

### 3.2 `user_login_identifiers`

| Coluna | Tipo | Regra |
|--------|------|-------|
| `id` | BIGINT PK | — |
| `user_id` | BIGINT FK | `ON DELETE CASCADE` |
| `kind` | VARCHAR(16) | `email`, `cpf`, `cnpj` |
| `lookup_hmac` | VARCHAR(64) | HMAC-SHA-256 hex |
| `created_at` | TIMESTAMPTZ | — |
| `retired_at` | TIMESTAMPTZ | NULL = ativo |

Índices:

```sql
CREATE UNIQUE INDEX uq_user_login_kind_hmac
    ON user_login_identifiers (kind, lookup_hmac);
CREATE UNIQUE INDEX uq_user_login_user_kind_active
    ON user_login_identifiers (user_id, kind) WHERE retired_at IS NULL;
CREATE INDEX ix_user_login_hmac ON user_login_identifiers (lookup_hmac);
```

Regra de negócio:

- e-mail sempre gera uma linha `kind='email'`;
- CPF, quando informado, gera uma linha `kind='cpf'`;
- CNPJ, quando informado no cadastro, gera uma linha `kind='cnpj'`;
- CNPJ secundário da prestadora **não** gera linha de login;
- todos os identificadores ativos do mesmo usuário podem autenticar;
- o valor em claro nunca é persistido; a busca é sempre pelo HMAC.

### 3.3 `email_verification_tokens`

| Coluna | Tipo | Regra |
|--------|------|-------|
| `id` | BIGINT PK | — |
| `user_id` | BIGINT FK | `ON DELETE CASCADE` |
| `token_hash` | VARCHAR(64) | SHA-256(token + pepper), único |
| `expires_at` | TIMESTAMPTZ | TTL 24h |
| `used_at` | TIMESTAMPTZ | NULL = não usado |
| `created_at` | TIMESTAMPTZ | — |

```sql
CREATE UNIQUE INDEX uq_email_verification_token ON email_verification_tokens (token_hash);
CREATE INDEX ix_email_verification_expires ON email_verification_tokens (expires_at);
CREATE INDEX ix_email_verification_user ON email_verification_tokens (user_id);
```

Ao emitir um novo token, os anteriores não usados do mesmo usuário são invalidados (`used_at = now()`).

### 3.4 `identity_change_log`

| Coluna | Tipo | Regra |
|--------|------|-------|
| `id` | BIGINT PK | — |
| `user_id` | BIGINT FK | `ON DELETE CASCADE` |
| `kind` | VARCHAR(16) | `email`, `cpf`, `cnpj` |
| `actor` | VARCHAR(80) | operador de suporte |
| `ticket_ref` | VARCHAR(80) | referência do ticket |
| `old_hmac` | VARCHAR(64) | HMAC do valor anterior |
| `new_hmac` | VARCHAR(64) | HMAC do valor novo |
| `created_at` | TIMESTAMPTZ | — |

Nenhuma coluna guarda o valor em claro. O log é append-only e não tem rota pública.

### 3.5 `password_reset_tokens`

Mantida. Adiciona-se `delivered_at TIMESTAMPTZ NULL` para auditoria de entrega, sem registrar o destinatário. O reset confirmado também marca `users.email_verified_at`.

## 4. Normalização e validação

### 4.1 E-mail

1. `trim`.
2. lowercase.
3. máximo 255 caracteres.
4. formato: exatamente um `@`, parte local não vazia, domínio com ao menos um ponto, sem espaços.
5. rejeitar caracteres de controle.
6. não normalizar pontos ou subendereçamento (`+tag`); o valor é tratado como opaco.

### 4.2 CPF

1. remover `.`, `-` e espaços.
2. exigir 11 dígitos.
3. rejeitar sequências com todos os dígitos iguais.
4. validar os dois dígitos verificadores pelo módulo 11.
5. zerar à esquerda não é permitido; CPF é sempre 11 dígitos.

### 4.3 CNPJ

1. remover `.`, `/`, `-` e espaços.
2. exigir 14 dígitos.
3. rejeitar sequências com todos os dígitos iguais.
4. validar os dois dígitos verificadores pelo módulo 11.
5. normalizar para 14 dígitos, sem máscara.

### 4.4 Senha

1. 8..128 caracteres.
2. aceitar qualquer caractere Unicode.
3. rejeitar senha igual ao e-mail, CPF ou CNPJ.
4. medir força apenas para aviso de UI; não bloquear por composição além do tamanho mínimo.
5. nunca logar, ecoar ou persistir em claro.

## 5. Hash, senha e tokens

### 5.1 Identificadores

```text
lookup_hmac = HMAC-SHA-256(
    key = COGME_LOGIN_PEPPER,
    msg = kind + ":" + normalized_value
).hex()
```

- `kind` ∈ `email|cpf|cnpj`.
- O pepper é lido de `COGME_LOGIN_PEPPER`.
- Produção exige pepper com ≥ 32 bytes aleatórios; o startup falha se menor.
- O valor normalizado nunca é persistido em `user_login_identifiers`.
- `users.email`/`users.cpf` são exceções de compatibilidade, não fonte de login.

### 5.2 `internal_username_hash`

```text
internal_username_hash = HMAC-SHA-256(pepper, uuid4().hex).hex()
```

Não deriva de e-mail, CPF ou CNPJ. Serve apenas para identificação opaca em logs/auditoria.

### 5.3 Senha

- `argon2-cffi >= 23.1,<24`, `Type.ID`.
- Parâmetros mínimos: `time_cost=3`, `memory_cost=65536` (64 MiB), `parallelism=4`, `salt_len=16`, `hash_len=32`.
- Persistir o **encoded hash** completo (`$argon2id$v=19$m=65536,t=3,p=4$...`), que inclui salt e parâmetros.
- `_verify_password` aceita encoded Argon2id e o formato legado PBKDF2; após verificação legada bem-sucedida, rehash para Argon2id e atualiza `password_hash` na mesma transação do login.
- Em produção, ausência de `argon2-cffi` é erro de startup, não fallback.
- Comparação sempre pela API da biblioteca; nunca comparar strings de hash.

### 5.4 Tokens de sessão e reset

- Sessão: 32 bytes aleatórios, `secrets.token_urlsafe(32)`; persistir `SHA-256(token + pepper)`.
- Reset: 32 bytes aleatórios; persistir `SHA-256(token + pepper)`; TTL 1 hora; single-use.
- Token de reset nunca aparece em resposta HTTP, log ou mensagem de erro.

## 6. Contrato HTTP

### 6.1 `POST /v1/auth/register`

Público. Rate limit 5/min/IP.

Request:

```json
{
  "name": "Maria Silva",
  "email": "maria@exemplo.com",
  "password": "uma-senha-forte",
  "cpf": "12345678901",
  "cnpj": "12345678000195"
}
```

Campos:

| Campo | Obrigatório | Regra |
|-------|-------------|-------|
| `name` | sim | 1..120 |
| `email` | sim | §4.1 |
| `password` | sim | §4.4 |
| `cpf` | não | §4.2; independente de `cnpj` |
| `cnpj` | não | §4.3; independente de `cpf` |

`cpf` e `cnpj` podem vir juntos. Não existe `tax_id_type`: o tipo é inferido pelo campo, nunca pelo tamanho de um campo genérico.

Respostas:

- `202` `{ "user_id": 1, "message": "Conta criada. Verifique seu e-mail para ativar o login." }`
- `400 validation_error` — formato, dígito verificador, campo legado com CPF/CNPJ.
- `409 conflict` — e-mail, CPF ou CNPJ já cadastrado. Mensagem genérica: `"Identificador já cadastrado."`
- `429 rate_limited`.

Compatibilidade: o campo legado `identifier` continua aceito por 90 dias **somente quando contém e-mail**. Se `identifier` for e-mail e `email` estiver ausente, ele é promovido a `email`. Se `identifier` contiver CPF/CNPJ, a resposta é `400 validation_error` com instrução para enviar `email` mais `cpf`/`cnpj` separados. O campo `email` tem precedência quando ambos vierem.

Efeitos transacionais:

1. validar tudo antes de abrir transação;
2. inserir `users` com `email_verified_at = NULL`;
3. inserir identificadores (`email` sempre; `cpf`/`cnpj` quando presentes);
4. criar `provider_profiles` com `legal_name = name`, `category = NULL` e `cpf` espelhado quando houver;
5. quando houver CNPJ, inserir `provider_cnpjs` como primário;
6. emitir token de verificação e gravar apenas o hash;
7. commit; o envio SMTP ocorre depois do commit e falha de envio não desfaz a conta.
Qualquer `IntegrityError` → rollback → `409`.

Limpeza preguiçosa: se o e-mail já pertence a uma conta **não verificada** com 30 dias ou mais, a conta antiga é removida e a nova é criada na mesma transação. Conta não verificada com menos de 30 dias recebe reenvio do link e resposta genérica. Não há scheduler.

### 6.2 `POST /v1/auth/login`

Público. Rate limit 5/min/IP.

Request:

```json
{ "identifier": "maria@exemplo.com", "password": "uma-senha-forte" }
```

Fluxo:

1. normalizar e classificar `identifier`;
2. calcular HMAC;
3. buscar `user_login_identifiers` ativo;
4. verificar senha;
5. se `status = dormant` → `403 { "error": { "key": "account_dormant" } }`, sem sessão;
6. se `status = deleted` → `401` genérico;
7. se `email_verified_at IS NULL` e a conta for nova → `403 email_unverified`, sem sessão;
8. criar sessão, revogar as anteriores, setar cookie.

Respostas:

- `200` `{ "message": "Login realizado." }` + `Set-Cookie: session=...`
- `401 unauthorized` — credenciais inválidas, mesma mensagem para usuário inexistente e senha errada.
- `403 account_dormant`.
- `403 email_unverified` — conta nova; o frontend oferece reenvio.
- `429 rate_limited`.

Todas as rotas de sessão usam **uma dependency tipada única** (`CurrentSession`), nunca `lambda` com parâmetros sem tipo. FastAPI trata parâmetros de `lambda` sem anotação como query params; o sintoma é `400` com `query.r`, `query.sf_` e `query.p`.

Cookie:

```text
session=<token>; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=86400
```

`Secure` é obrigatório quando `COGME_ENV=production`; em desenvolvimento (`COGME_ENV=development`) pode ser `false` apenas para `localhost`.

### 6.3 `GET /v1/auth/me`

Sessão obrigatória.

```json
{
  "id": 1,
  "name": "Maria Silva",
  "email": "maria@exemplo.com",
  "email_verified": true,
  "phone": null,
  "status": "active",
  "created_at": "2026-11-17T12:00:00Z",
  "profile_completion_required": false,
  "identifiers": [
    { "kind": "email", "masked": "m***@exemplo.com" },
    { "kind": "cpf", "masked": "***.***.***-01" }
  ],
  "documents": {
    "cpf": "***.***.***-01",
    "cnpjs": [
      { "id": 7, "masked": "**.***.***/0001-95", "is_primary": true, "status": "active" }
    ]
  }
}
```

- `identifiers` nunca devolve HMAC nem valor completo e lista apenas identificadores de **login**.
- `documents` lista documentos de **emissão**; CNPJ adicionado no perfil aparece aqui, não em `identifiers`.
- `profile_completion_required = true` quando `users.email IS NULL` (legado) ou quando o nome está vazio.

### 6.4 `PATCH /v1/auth/me`

Sessão obrigatória. CSRF obrigatório.

Request:

```json
{ "name": "Maria Souza", "phone": "+55 11 99999-0000" }
```

- Campos ausentes não mudam.
- `name` 1..120; `phone` até 30, apenas dígitos, `+`, espaço, parênteses e hífen.
- `200` com o mesmo corpo de `GET /v1/auth/me`.
- `400 validation_error`.

### 6.5 `PUT /v1/auth/me/email`

Sessão obrigatória. CSRF obrigatório. Rate limit 3/hour/usuário.

Request:

```json
{ "new_email": "nova@exemplo.com", "password": "senha-atual" }
```

Fluxo transacional:

1. verificar senha atual;
2. validar novo e-mail;
3. verificar unicidade via HMAC;
4. inserir novo identificador;
5. `retired_at = now()` no identificador de e-mail antigo;
6. atualizar `users.email`;
7. revogar todas as outras sessões;
8. commit.

Respostas:

- `200` `{ "message": "E-mail atualizado." }`
- `400 validation_error`
- `401 unauthorized` — senha errada
- `409 conflict` — e-mail já usado
- `429 rate_limited`

O e-mail antigo deixa de autenticar imediatamente após o commit.

### 6.6 `PUT /v1/auth/me/password`

Sessão obrigatória. CSRF obrigatório. Rate limit 5/hour/usuário.

Request:

```json
{ "current_password": "senha-atual", "new_password": "senha-nova" }
```

- Verifica a senha atual.
- Valida a nova senha (§4.4) e rejeita igual à atual.
- Gera Argon2id encoded.
- Revoga todas as outras sessões; mantém a sessão atual.
- `200` `{ "message": "Senha atualizada." }`
- `401` senha atual incorreta; `400` nova senha inválida.

### 6.7 `POST /v1/auth/password/reset-request`

Público. Rate limit 3/hour/IP.

Request: `{ "identifier": "..." }`

- Sempre `202` `{ "message": "Se o identificador existir, enviaremos instruções." }`, exista ou não a conta.
- Gera token, persiste hash, envia e-mail com link `https://<host>/auth/reset?token=<token>`.
- Não registra token, e-mail ou identificador em log.

Entrega:

- SMTP próprio (`COGME_SMTP_HOST`, `COGME_SMTP_PORT`, `COGME_SMTP_USER`, `COGME_SMTP_PASSWORD`, `COGME_SMTP_FROM`).
- Em `COGME_ENV=development`, se SMTP ausente, gravar o link em `.secrets/reset-token` com permissão `0600`, uma linha por token, e nunca no log.
- Em produção, SMTP ausente é erro de startup.

### 6.8 `GET /auth/reset` e `POST /v1/auth/password/reset-confirm`

Frontend `GET /auth/reset?token=...` renderiza formulário com o token em campo oculto.

`POST /v1/auth/password/reset-confirm`:

```json
{ "token": "...", "new_password": "..." }
```

- Valida token não usado e não expirado.
- Valida nova senha.
- Atualiza `password_hash`.
- Marca `used_at`.
- Marca `users.email_verified_at = now()` quando ainda for NULL.
- Revoga todas as sessões do usuário.
- `204`.
- `400 validation_error` para token inválido/expirado, sem distinguir os casos.

### 6.9 `POST /v1/auth/email/verify`

Público. Rate limit 10/min/IP.

Request: `{ "token": "..." }`

- Valida token não usado e não expirado.
- Marca `users.email_verified_at = now()` e `used_at`.
- `204`.
- `400 validation_error` para token inválido/expirado, sem distinguir os casos.

### 6.10 `POST /v1/auth/email/resend`

Público. Rate limit 3/hour/IP.

Request: `{ "email": "..." }`

- Sempre `202` `{ "message": "Se a conta existir e não estiver verificada, enviaremos um novo link." }`.
- Conta verificada ou inexistente: não envia nada e responde igual.
- Conta não verificada: invalida tokens anteriores, emite novo token de 24h e envia.
- Conta não verificada com 30 dias ou mais: remove a conta e responde genérico; o próximo cadastro começa limpo.
- Não registra e-mail nem token em log.

### 6.11 Correção de identificador de login (suporte)

Não há rota HTTP. Operação de CLI, executada por suporte:

```bash
python -m src.backend.cli identifiers correct \
  --user-id 123 --kind cpf --ticket SUP-456 --actor agent-support --dry-run
# prompt: New value (hidden):
```

- O valor novo é lido de **stdin sem eco**, nunca de `argv`.
- `--dry-run` obrigatório na primeira execução e imprime apenas a máscara.
- A execução real exige `--confirm` e grava `identity_change_log` com `old_hmac`/`new_hmac`, ator e ticket.
- O identificador antigo é aposentado (`retired_at`), o novo é inserido na mesma transação.
- CPF/CNPJ nunca aparecem em histórico de shell, `ps`, log ou saída do comando.
- E-mail pode ser corrigido pelo próprio usuário em `/v1/auth/me/email`; a CLI cobre CPF/CNPJ.

### 6.12 `POST /v1/account/complete-email`

Fluxo de legado (CR9-D01), disponível apenas enquanto `users.email IS NULL`.

Request: `{ "email": "...", "password": "..." }`

- Verifica a senha atual.
- Valida e reserva o e-mail.
- Insere identificador, atualiza `users.email` e marca `email_verified_at` (o e-mail foi confirmado pela senha da conta).
- `200`.
- `409` se o e-mail já estiver em uso.

Enquanto `profile_completion_required = true`, os endpoints de escrita de clientes, invoices, provider e perfil (exceto este) retornam `403 profile_incomplete`.

## 7. Migração e legado

### 7.1 Correção da revisão Alembic

O arquivo `0009_fix_users_nullable_email_cpf.py` declara `revision = "0009_fix_users_nullable_email_cpf"` (35 caracteres), mas `alembic_version.version_num` é `VARCHAR(32)` e o banco contém `0009_fix_users_nullable` (23 caracteres).

Ação:

1. alterar `revision` para `"0009_fix_users_nullable"` (23 caracteres);
2. manter `down_revision = "0008_alter_users_cpf_nullable"`;
3. adicionar teste que percorre `migrations/versions/*.py` e falha se `len(revision) > 32`;
4. em banco limpo, `alembic upgrade head` deve estampar o valor de 23 caracteres;
5. em banco existente, `alembic current` deve reconhecer a revisão sem `stamp` manual.

### 7.2 Contas legadas

- `users.email IS NULL` → `profile_completion_required = true`.
- Login continua permitido por CPF/CNPJ.
- Escritas bloqueadas até completar e-mail.
- Prazo de 30 dias; depois, conta entra em dormência conforme SPEC-022.
- Nenhum backfill inventado de e-mail.
- Contas com e-mail existente são **grandfatherizadas** na migration: `email_verified_at = created_at`. Só contas novas passam pelo duplo opt-in.

### 7.3 Rehash de senha

- Hashes PBKDF2 legados continuam válidos para login.
- No primeiro login bem-sucedido, rehash para Argon2id.
- Se o rehash falhar, o login continua e o erro é registrado sem PII.

### 7.4 Backfill de documentos de emissão

A migration `0012_email_verification_and_issuer_documents.py` executa o backfill em duas fontes:

1. **`provider_profiles.cnpj`** — quando preenchido, vira `provider_cnpjs` primário.
2. **`user_login_identifiers.kind='cnpj'`** — o CNPJ em claro não é recuperável de `lookup_hmac`. A migration lê a coluna legada de valor disponível na base de origem (ou uma tabela temporária de importação controlada) e grava o CNPJ em `provider_cnpjs`. Quando o valor não existir em lugar nenhum, o suporte importa por CLI a partir de lista conferida; o que não se admite é ignorar essa fonte e deixar o usuário sem emissor.

Regras:

- CNPJ do cadastro vira `provider_cnpjs` primário.
- CPF informado no cadastro é espelhado em `users.cpf` e `provider_profiles.cpf`.
- `ON CONFLICT (cnpj) DO NOTHING` evita duplicidade entre as duas fontes.
- Nenhum usuário legado perde a capacidade de emitir.
- Antes/depois da migration, contar usuários com CNPJ ativo e conferir que o número de emissores não diminuiu.

### 7.5 Backfill de `internal_username_hash`

`users.internal_username_hash` hoje é SHA-256 do identificador. A correção é comando pós-migration, com pepper:

```bash
python -m src.backend.cli backfill internal-username --dry-run
python -m src.backend.cli backfill internal-username --confirm
```

- Gera UUID4 aleatório por usuário e grava HMAC-SHA-256(pepper, uuid).
- Idempotente: não toca linha que já tem 64 hex de HMAC válido.
- `--dry-run` conta quantas linhas mudariam, sem imprimir hash nem identificador.

## 8. Critérios de aceite

- **AC-024-01** Cadastro só com e-mail funciona; `users.email` preenchido; um identificador `email`; `email_verified_at` NULL.
- **AC-024-02** Cadastro com e-mail + CPF válido funciona; dois identificadores; `users.cpf` e `provider_profiles.cpf` preenchidos.
- **AC-024-03** Cadastro com e-mail + CNPJ válido funciona; dois identificadores; `provider_cnpjs` primário; `users.cpf` NULL.
- **AC-024-03b** Cadastro com e-mail + CPF + CNPJ funciona; três identificadores; CPF e CNPJ coexistem sem sobrescrita.
- **AC-024-04** CPF/CNPJ com dígito verificador inválido retorna `400`, sem criar linha.
- **AC-024-05** E-mail, CPF ou CNPJ duplicado retorna `409 conflict`, sem revelar qual campo colidiu.
- **AC-024-06** Login funciona com e-mail, CPF e CNPJ do mesmo usuário.
- **AC-024-07** Senha errada e usuário inexistente retornam a mesma resposta `401`.
- **AC-024-08** `lookup_hmac` é HMAC-SHA-256 e não contém o valor normalizado; teste com pepper conhecido confere o digest.
- **AC-024-09** `internal_username_hash` não é SHA-256 do e-mail/CPF/CNPJ.
- **AC-024-10** Senha persistida é encoded Argon2id; login legado PBKDF2 é rehashed.
- **AC-024-11** Reset request sempre `202`; token não aparece na resposta nem em log; e-mail é entregue ou gravado em `.secrets/reset-token` no modo dev.
- **AC-024-12** Reset confirm consome o token uma única vez, revoga sessões, marca e-mail verificado e permite login com a nova senha.
- **AC-024-13** Troca de e-mail aposenta o identificador antigo, atualiza `users.email` e invalida login antigo.
- **AC-024-14** Troca de senha revoga outras sessões e mantém a atual.
- **AC-024-15** Conta legada sem e-mail recebe `403 profile_incomplete` nas escritas e conclui via `/v1/account/complete-email`.
- **AC-024-16** `alembic upgrade head` funciona do zero e em banco existente; `alembic current` reconhece a revisão.
- **AC-024-17** Nenhum log contém e-mail, CPF, CNPJ, nome ou token.
- **AC-024-18** Rate limits de registro, login e reset retornam `429`.
- **AC-024-19** Conta nova não autentica antes de `/v1/auth/email/verify`; resposta é `403 email_unverified`.
- **AC-024-20** Conta antiga com e-mail autentica sem verificação forçada após a migration (grandfather).
- **AC-024-21** Reenvio de verificação responde igual para conta inexistente, verificada e não verificada; novo token invalida os anteriores.
- **AC-024-22** E-mail de conta não verificada com 30 dias ou mais é liberado no novo cadastro; com menos de 30 dias, a conta antiga permanece e o link é reenviado.
- **AC-024-23** CLI de correção lê o valor de stdin, `--dry-run` mascara a saída e `identity_change_log` grava apenas HMAC.
- **AC-024-24** `GET /v1/auth/me` e rotas de sessão respondem sem exigir `query.r`, `query.sf_` ou `query.p` e propagam 401/403 corretamente.

## 9. Segurança e LGPD

### 9.1 Controles obrigatórios

| Controle | Regra |
|----------|-------|
| Hash de identificador | HMAC-SHA-256 com pepper ≥ 32 bytes |
| Hash de senha | Argon2id encoded, sem fallback silencioso em produção |
| Enumeração | mensagens genéricas em login, registro e reset |
| Sessão | token opaco, hash com pepper, revogação imediata |
| CSRF | double-submit; header `X-CSRF-Token`; logout não isento |
| Verificação de e-mail | duplo opt-in, token de 24h single-use, resposta genérica no reenvio |
| Correção de identificador | CLI com stdin sem eco, `--dry-run`, trilha em `identity_change_log` sem PII |
| Rate limit | login 5/min/IP; registro 5/min/IP; reset 3/h/IP; troca de e-mail 3/h/usuário |
| Cookies | HttpOnly, Secure em produção, SameSite=Lax, Path=/ |
| Logs | zero PII; usar `user_id` e `internal_username_hash` |
| Erros | não vazar stack, SQL, identificador ou existência de conta |
| Transporte | TLS obrigatório em produção |

### 9.2 LGPD/GDPR

- Base legal e controlador conforme SPEC-015/SPEC-022; contrato (Art. 7º, V) para identidade e autenticação.
- Minimização: só coletar CPF/CNPJ quando o usuário informar; e-mail é necessário para autenticação, verificação e recuperação.
- Documento de emissão (`provider_profiles.cpf`, `provider_cnpjs`) é dado empresarial, coletado só para emitir invoice persistida; não é identificador de login.
- Finalidade: identidade, login, verificação de posse, recuperação, comunicação transacional.
- Retenção: conta ativa enquanto necessária; tokens de verificação 24h; `identity_change_log` guarda HMAC e metadados, nunca valor.
- Direitos: acesso e correção via `/perfil`; exclusão via `/v1/account`; correção de CPF/CNPJ de login via suporte com trilha.
- Transferência internacional: SMTP próprio, sem provedor cloud.
- Dados de menores: produto B2B; não coletar idade; manter política vigente.

### 9.3 Ameaças e mitigação

| Ameaça | Mitigação |
|--------|-----------|
| Enumeração de contas | respostas genéricas + rate limit |
| Rainbow table de CPF/CNPJ | HMAC com pepper secreto |
| Credential stuffing | rate limit + Argon2id + revogação de sessões |
| Sequestro de sessão | HttpOnly/Secure/SameSite + rotação no login |
| CSRF | double-submit + SameSite |
| Reset poisoning | token single-use, TTL 1h, hash persistido |
| Escalada por e-mail duplicado | unique parcial + transação de troca |
| Downgrade de senha | rehash no login, sem fallback em produção |
| Squatting de e-mail | duplo opt-in + limpeza preguiçosa de conta não verificada |
| Verificação por e-mail trocado | token vinculado ao `user_id` e ao e-mail vigente |
| Vazamento de PII por CLI | valor lido de stdin sem eco; log guarda só HMAC |
| Confusão entre login e emissão | campos e tabelas separados; validação de emissor usa documentos de emissão |

## 10. Testes obrigatórios

### 10.1 Unidade

- normalização de e-mail/CPF/CNPJ;
- dígitos verificadores (casos válidos, inválidos, repetidos);
- HMAC determinístico com pepper fixo;
- `internal_username_hash` não derivado do identificador;
- Argon2id encoded + verify + rehash de PBKDF2;
- máscaras de e-mail/CPF/CNPJ;
- validação de senha;
- token de verificação: geração, expiração de 24h, uso único.

### 10.2 Integração

- matriz de cadastro: e-mail, e-mail+CPF, e-mail+CNPJ, e-mail+CPF+CNPJ, duplicados;
- `identifier` legado com e-mail é aceito; com CPF/CNPJ retorna `400` pedindo campos separados;
- login por cada identificador;
- conta dormente/deleted;
- verificação de e-mail: `403 email_unverified` antes do token; `204` depois; token expirado e reuso retornam `400`;
- grandfather: conta antiga com e-mail autentica sem token;
- reenvio genérico e limpeza preguiçosa aos 30 dias;
- reset request/confirm com SMTP fake;
- completude de conta legada;
- CLI de correção: dry-run mascarado, `identity_change_log` sem valor, valor ausente de `argv`;
- backfill de `provider_cnpjs` a partir das duas fontes, com contagem de emissores antes/depois;
- `alembic upgrade head` do zero e em banco com revisão de 23 caracteres.

### 10.3 Segurança

- `caplog` não contém PII em nenhum fluxo;
- token de reset e de verificação não aparecem em resposta/log;
- cookie flags;
- CSRF ausente retorna `403`;
- rate limit retorna `429`;
- 401 e 403 não viram `500` no handler canônico;
- `/me` não exige query params e responde `401` sem sessão;
- cross-owner não se aplica a esta spec (coberto na 025).

### 10.4 e2e

- cadastro por formulário com e-mail + CPF;
- cadastro por formulário só com e-mail;
- login e logout com CSRF;
- cadastro → e-mail de verificação → login;
- reset completo com link;
- troca de e-mail e login com o novo;
- completude de conta legada.

## 11. Rollback

1. Reverter rotas e templates para o contrato anterior (`identifier` único).
2. Manter `user_login_identifiers` e os índices parciais; são compatíveis com o modelo antigo.
3. Reverter `revision` de 0009 somente se o banco tiver sido migrado para o valor de 35 caracteres; caso contrário, manter o valor de 23.
4. Hashes Argon2id continuam verificáveis pelo código antigo somente se ele suportar encoded; caso contrário, manter o novo verificador durante o rollback.
5. Tokens de reset e de verificação emitidos na janela são invalidados por TTL.
6. Desativar o requisito de e-mail verificado e reativar o login por e-mail; `email_verified_at` e as tabelas novas podem permanecer.
7. Manter `provider_cnpjs` e `provider_profiles.cpf` se o rollback for só de aplicação; o código antigo ignora as colunas novas.

## CHANGELOG

| Versão | Data | Autor | Mudança |
|--------|------|-------|---------|
| 0.1.0 | 2026-11-17 | agent-project-analyst | Proposta inicial de emenda à SPEC-017 |
| 0.2.0 | 2026-11-17 | agent-project-analyst | Correções da revisão: campos separados `cpf`/`cnpj` (sem `tax_id_type`), `identifier` legado só para e-mail, verificação de e-mail por duplo opt-in com grandfather, limpeza preguiçosa aos 30 dias, CLI de correção com leitura de stdin e `identity_change_log` sem PII, backfill de `provider_cnpjs` a partir das duas fontes, dependency de sessão tipada, ACs 19–24 |
