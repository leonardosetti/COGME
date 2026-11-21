---
id: docs-especificacoes-spec-prop-025-clientes-multiempresa-e-fluxo-anonimo
title: Proposta de Spec — Clientes multiempresa, clientes internacionais e fluxo anônimo
type: spec
version: 0.2.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-009-crud-usuarios-dashboard-anonimo.md
- .ai/specs/spec-019-client-directory-v1.md (emenda)
- .ai/specs/spec-020-simulation-invoice-history-v1.md (emenda)
- .ai/specs/spec-004-backend-mvp-v1.spec.md (contrato HTTP e limites)
- .ai/specs/spec-017-identity-access-session-v1.md (sessão e CSRF)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 7, 9; P-03, P-14, P-15)
- docs/auditorias/aud-cr-009-2026-11-17-pre-producao.md
last-revised: '2026-11-17'
lgpd-class: sensível
tags:
- proposta
- spec
- clientes
- multiempresa
- internacional
- anonimo
- invoices
- seguranca
proposal-id: PROP-025
rastreia-req:
- CR-009
- CR9-D03
- CR9-D10
- CR9-D15
- CA-01
- CA-05
- CA-06
- CA-09
- CA-14
- CA-19
- CA-20
testes-vinculados: []
---

# Proposta de Spec — Clientes multiempresa, clientes internacionais e fluxo anônimo

## 1. Ideia / Draft

Esta proposta emenda a **SPEC-019** (diretório de clientes) e a **SPEC-020** (simulações e invoices) para:

- permitir zero, uma ou várias empresas clientes por usuário;
- aceitar clientes nacionais (CPF/CNPJ) e internacionais (documento livre ou ausente);
- persistir e-mail e telefone do cliente;
- impedir referências cruzadas entre proprietários em invoices;
- corrigir a colisão de numeração entre emissores;
- congelar o fluxo anônimo como contrato sem persistência.

A spec **não substitui** as specs 019/020; ela altera apenas os pontos listados.

## 2. Derivação e limites

### 2.1 O que muda

| Tema | SPEC-019/020 vigente | Emenda proposta |
|------|----------------------|-----------------|
| Clientes por usuário | N, sem limite explícito | 0..100 ativos |
| Documento do cliente | CPF/CNPJ 11/14 dígitos, NOT NULL | nacional obrigatório com checksum; internacional opcional até 32 |
| País | `CHAR(2)` sem validação | ISO 3166-1 validado contra `countries` |
| E-mail/telefone | schema aceita, criação descarta | persistidos e devolvidos |
| Duplicidade | `IntegrityError` → 500 | `409 conflict` |
| Invoice com `client_id` | aceita ID sem validar dono | valida dono e deriva snapshot do banco |
| Invoice com `simulation_id` | aceita ID sem validar dono | valida dono |
| Emissor | aceita qualquer CNPJ | exige documento de emissão ativo do próprio usuário (`provider_profiles.cpf` ou `provider_cnpjs`) |
| Numeração | unique global de `invoice_number` | unique `(issuer_tax_id_digits, invoice_number)` |
| Fluxo anônimo | público, sem persistência | contrato explícito + testes + rate limit |
| Listas | array cru | envelope `{items,total,limit,offset}` |

### 2.2 O que não muda

- Isolamento por proprietário (P-14).
- Invoice finalizada é imutável; clone cria draft.
- Retenção LGPD de 5 anos + 6 meses para invoices finalizadas.
- PDF bilíngue.
- Cliente fictício continua permitido no fluxo avulso e no persistido.

### 2.3 Fora de escopo

- Cadastro de fornecedores.
- Múltiplos endereços por cliente.
- Validação de documento estrangeiro por país.
- Sincronização com Receita Federal ou VIES.
- Numeração oficial para invoice anônima.

## 3. Modelo de dados de clientes

### 3.1 `clients`

| Coluna | Hoje | Proposta |
|--------|------|----------|
| `id` | BIGINT PK | mantido |
| `owner_user_id` | BIGINT FK | mantido, `ON DELETE CASCADE` |
| `name` | VARCHAR(120) NOT NULL | mantido, 1..120 |
| `tax_id_digits` | CHAR(14) NOT NULL | VARCHAR(32) NULL |
| `tax_id_type` | VARCHAR(16) NOT NULL | `cpf`, `cnpj`, `foreign`, `none` |
| `email` | VARCHAR(255) NULL | persistido, validado quando presente |
| `phone` | VARCHAR(30) NULL | persistido, normalizado |
| `address` | VARCHAR(240) NULL | mantido; obrigatório para `foreign` quando não houver e-mail |
| `country_code` | CHAR(2) NOT NULL default BR | validado contra `countries` |
| `status` | active/inactive | mantido |
| `created_at`, `updated_at` | TIMESTAMPTZ | mantidos |

### 3.2 Restrições

```sql
ALTER TABLE clients
    ALTER COLUMN tax_id_digits TYPE VARCHAR(32) USING tax_id_digits::varchar(32),
    ALTER COLUMN tax_id_digits DROP NOT NULL;

ALTER TABLE clients
    ADD CONSTRAINT chk_clients_tax_id_type
    CHECK (tax_id_type IN ('cpf', 'cnpj', 'foreign', 'none'));

ALTER TABLE clients
    DROP CONSTRAINT IF EXISTS uq_clients_owner_tax;
CREATE UNIQUE INDEX uq_clients_owner_tax
    ON clients (owner_user_id, tax_id_digits)
    WHERE tax_id_digits IS NOT NULL;
```

Regras:

- `tax_id_digits` é sempre normalizado (dígitos para CPF/CNPJ; `trim` para `foreign`).
- Cliente nacional: `tax_id_type ∈ {cpf, cnpj}` e `tax_id_digits` obrigatório.
- Cliente internacional com documento: `tax_id_type = foreign`, `tax_id_digits` opcional, mas quando presente tem 1..32 caracteres.
- Cliente internacional sem documento: `tax_id_type = none`, `tax_id_digits = NULL`.
- `country_code` deve existir em `countries`; `BR` é o default.
- `email` quando presente: mesmo validador do usuário (§4.1 da SPEC-024).
- `phone` quando presente: até 30 caracteres; dígitos, `+`, espaço, parênteses e hífen.
- Limite de 100 clientes ativos por usuário; acima disso, `422 limit_exceeded`.

### 3.3 Migração de dados existentes

- Linhas com `tax_id_digits` de 11 dígitos → `tax_id_type = 'cpf'`.
- Linhas com 14 dígitos → `tax_id_type = 'cnpj'`.
- Linhas com `country_code != 'BR'` e documento não brasileiro → `tax_id_type = 'foreign'`.
- Nenhuma linha é apagada.
- Documentos existentes sem checksum válido permanecem, mas não podem ser usados em novas invoices até correção; a UI sinaliza `invalid_tax_id`.

## 4. Contrato HTTP de clientes

### 4.1 `GET /v1/clients`

Sessão obrigatória.

Query:

| Parâmetro | Valores | Default |
|-----------|---------|---------|
| `status` | `active`, `inactive`, `all` | `active` |
| `country` | ISO alpha-2 | todos |
| `q` | busca em nome/documento/e-mail | vazio |
| `limit` | 1..100 | 20 |
| `offset` | ≥ 0 | 0 |

Resposta:

```json
{
  "items": [
    {
      "id": 1,
      "name": "ACME LLC",
      "tax_id": "12-3456789",
      "tax_id_type": "foreign",
      "email": "billing@acme.com",
      "phone": "+1 415 555 0100",
      "address": "1 Market St, San Francisco, CA",
      "country_code": "US",
      "status": "active",
      "created_at": "2026-11-17T12:00:00Z",
      "updated_at": "2026-11-17T12:00:00Z"
    }
  ],
  "total": 1,
  "limit": 20,
  "offset": 0
}
```

- `total` conta apenas os clientes do proprietário e respeita os filtros.
- Ordenação padrão: `name ASC, id ASC`.
- Nunca retorna cliente de outro proprietário.

### 4.2 `POST /v1/clients`

Sessão + CSRF.

Request nacional:

```json
{
  "name": "Empresa Brasileira Ltda",
  "tax_id": "12.345.678/0001-95",
  "tax_id_type": "cnpj",
  "email": "financeiro@empresa.com.br",
  "phone": "+55 11 3333-4444",
  "address": "Rua A, 100, São Paulo/SP",
  "country_code": "BR"
}
```

Request internacional:

```json
{
  "name": "ACME LLC",
  "tax_id": "12-3456789",
  "tax_id_type": "foreign",
  "email": "billing@acme.com",
  "address": "1 Market St, San Francisco, CA",
  "country_code": "US"
}
```

Regras:

- `name` obrigatório.
- `country_code` obrigatório; default `BR` apenas quando omitido e o documento for brasileiro.
- `tax_id` obrigatório para `BR`; opcional para outros países.
- `tax_id_type` inferido: `cpf`/`cnpj` pelo tamanho em `BR`; `foreign` para não-BR com documento; `none` para não-BR sem documento.
- `email` e `phone` persistidos.
- Duplicidade `(owner_user_id, tax_id_digits)` → `409 conflict`.
- Limite de 100 ativos → `422 limit_exceeded`.
- `201` com o cliente criado.

### 4.3 `GET /v1/clients/{id}`

- `200` se pertence ao usuário.
- `404` se não existe **ou** pertence a outro usuário.

### 4.4 `PUT /v1/clients/{id}`

Sessão + CSRF.

- `name`, `email`, `phone`, `address`, `country_code`, `tax_id` podem mudar.
- `tax_id_type` é recalculado.
- `owner_user_id` é imutável.
- `404` cross-owner.
- `409` se o novo documento colidir com outro cliente do mesmo usuário.
- `200` com o cliente atualizado.

### 4.5 `POST /v1/clients/{id}/deactivate` e `/activate`

- Sessão + CSRF.
- `204`.
- `404` cross-owner.
- Cliente inativo não pode ser usado em nova invoice; invoices existentes permanecem.

### 4.6 Erros

| Situação | Status | `error.key` |
|----------|--------|-------------|
| Formato/documento inválido | 400 | `validation_error` |
| País inexistente | 400 | `validation_error` |
| Não autenticado | 401 | `unauthorized` |
| Sem permissão (emissor de terceiro) | 403 | `issuer_not_allowed` |
| Cross-owner | 404 | `not_found` |
| Duplicidade | 409 | `conflict` |
| Clone com emissor inativo | 409 | `issuer_inactive` |
| Limite excedido | 422 | `limit_exceeded` |
| Rate limit | 429 | `rate_limited` |

O handler canônico mapeia 401, 403, 409, 422 e 429. Status sem mapeamento não pode virar `500 internal_error`.

## 5. Regras de cliente nacional e internacional

### 5.1 Brasil

- `tax_id` obrigatório.
- CPF: 11 dígitos, dígitos verificadores válidos.
- CNPJ: 14 dígitos, dígitos verificadores válidos.
- `tax_id_type` deve corresponder ao tamanho.
- `name` é a razão social ou nome completo.
- `address` recomendado; não bloqueia.

### 5.2 Exterior

- `country_code` diferente de `BR`, validado contra `countries`.
- `tax_id` opcional; quando presente, 1..32 caracteres, sem validação de checksum.
- `tax_id_type = foreign` quando há documento; `tax_id_type = none` quando não há.
- `name` obrigatório.
- `address` obrigatório quando não houver `email`; caso contrário, opcional.
- `email`/`phone` opcionais.
- A invoice usa o nome do país a partir de `countries`, não do payload.

### 5.3 Cliente fictício

- `client_fictitious = true` exige `client_country_code` válido e `client_name`.
- Não cria linha em `clients`.
- Não exige `tax_id`.
- A invoice persistida guarda o snapshot no próprio registro.

## 6. Fluxo anônimo sem persistência

### 6.1 `POST /v1/simulate`

Público. Rate limit 30/min/IP.

Request e response permanecem os da SPEC-020. Regras adicionais:

- não abre transação de escrita;
- não cria sessão;
- não grava `simulations`;
- não consome `invoice_sequences`;
- não registra valores ou identificadores em log.

### 6.2 `POST /v1/invoice`

Público. Rate limit 10/min/IP.

Request: `InvoiceRequest` da SPEC-020 (simulação + emissor + cliente + número + data + descrição).

Regras:

- recalcula a simulação no servidor; nunca confia em valores calculados pelo cliente;
- não grava `invoices`, `clients`, `simulations` ou `users`;
- não consome `invoice_sequences`;
- resposta `application/pdf`, `Content-Disposition: attachment`, `Cache-Control: no-store`;
- não exige cookie de sessão;
- não cria cookie de sessão;
- não registra PII.

### 6.3 CSRF

- `/v1/simulate` e `/v1/invoice` permanecem isentos: não há cookie de sessão nem estado no servidor.
- `/v1/auth/logout` deixa de ser isento e passa a exigir `X-CSRF-Token`.
- Todas as rotas autenticadas de clientes, provider, perfil, invoices persistidas e conta exigem CSRF.
- O frontend lê o cookie `csrf_token` (não-HttpOnly) e envia o header em `fetch` e formulários.

### 6.4 Rate limits

| Rota | Limite | Chave |
|------|--------|-------|
| `POST /v1/simulate` | 30/min | IP real |
| `POST /v1/invoice` | 10/min | IP real |
| `GET /v1/clients` | 120/min | usuário |
| `POST/PUT /v1/clients` | 30/min | usuário |
| `POST /v1/invoices` | 30/min | usuário |
| `POST /v1/invoices/{id}/finalize` | 30/min | usuário |
| `GET /v1/invoices` | 120/min | usuário |

O IP real vem de `X-Forwarded-For`/`X-Real-IP`; o backend deve rodar com `--proxy-headers` e `--forwarded-allow-ips` restrito à rede do proxy.

## 7. Invoices persistidas: propriedade e numeração

### 7.1 Validação de propriedade

`POST /v1/invoices` (plural, persistido) e `POST /v1/invoices/{id}/clone`:

1. `client_id`, quando presente, é carregado por `(id, owner_user_id)`. Ausente ou de outro dono → `404`.
2. `simulation_id`, quando presente, é carregado por `(id, owner_user_id)`. Ausente ou de outro dono → `404`.
3. Snapshot do cliente é derivado do registro persistido:
   - `client_name = client.name`
   - `client_tax_id_digits = client.tax_id_digits`
   - `client_address = client.address`
   - `client_country_code = client.country_code`
4. Se o payload enviar snapshot divergente, retornar `400 validation_error`; não sobrescrever silenciosamente.
5. Cliente inativo → `400 validation_error` (`client_inactive`).
6. `issuer_tax_id_digits`:
   - CPF: deve ser igual ao `provider_profiles.cpf` do titular (documento de emissão);
   - CNPJ: deve existir em `provider_cnpjs` **ativo** do titular;
   - identificador de login (`user_login_identifiers`) não é documento de emissão e não autoriza emissão;
   - caso contrário → `403 issuer_not_allowed`.
7. `owner_user_id` da invoice é sempre o da sessão; nunca vem do payload.

### 7.2 Numeração

- A função `next_invoice_number(issuer_tax_id_digits)` continua gerando `INV-YYYYMM-NNNN` por emissor e por mês.
- O unique global `uq_invoices_invoice_number` é removido.
- Novo unique: `(issuer_tax_id_digits, invoice_number)`.
- O índice de busca `ix_invoices_invoice_number` permanece não único.
- Duas contas com CNPJs diferentes podem ter `INV-202611-0001` cada uma.
- A busca por número continua escopada por `owner_user_id`.

Migração:

```sql
ALTER TABLE invoices DROP CONSTRAINT uq_invoices_invoice_number;
ALTER TABLE invoices
    ADD CONSTRAINT uq_invoices_issuer_number
    UNIQUE (issuer_tax_id_digits, invoice_number);
```

Pré-condição: verificar duplicidade antes de criar o constraint; se houver, falhar a migration com relatório, não apagar dados.

### 7.3 Clone

- Copia todos os snapshots da invoice original.
- Novo `invoice_number` gerado para o mesmo emissor.
- `owner_user_id` permanece o da sessão.
- `client_id`/`simulation_id` só são copiados se ainda pertencerem ao usuário.
- `supersedes_invoice_id` aponta para a original.
- Se o emissor da invoice original estiver inativo (CPF removido ou CNPJ marcado `inactive`), o clone retorna `409 issuer_inactive`. A invoice original permanece intacta e consultável.

### 7.4 Documentos de emissão e backfill legado

- O emissor persistido vem de `provider_profiles.cpf` e `provider_cnpjs`, não de `users.cpf` nem de `user_login_identifiers`.
- Migration `0010` cria `provider_cnpjs` com `id BIGINT GENERATED BY DEFAULT AS IDENTITY`; DDL sem `identity` não gera id e quebra o backfill.
- Backfill (SPEC-024 §7.4) importa CNPJs de `provider_profiles.cnpj` e de `user_login_identifiers.kind='cnpj'`, sem remover a origem.
- Correção de CNPJ com invoice finalizada mantém o CNPJ antigo como `inactive` e adiciona o novo; o histórico preserva o snapshot original.
- Usuário cadastrado só com e-mail não tem documento de emissão até definir `provider_profiles.cpf` ou adicionar CNPJ no perfil; enquanto isso, só emite no fluxo anônimo.

### 7.5 Envelope de listas

Clientes, invoices e simulações respondem o mesmo envelope:

```json
{ "items": [], "total": 0, "limit": 20, "offset": 0 }
```

- `GET /v1/invoices`: `total` respeita os filtros e o `owner_user_id` da sessão. Hoje a rota descarta a contagem (`_total`); corrigir.
- `GET /v1/simulations`: hoje devolve lista crua; corrigir para envelope.
- `GET /v1/clients`: já previsto em §4.1.
- O dashboard lê `total` para os contadores; não cria endpoint de agregação.

## 8. Critérios de aceite

- **AC-025-01** Usuário sem clientes acessa dashboard e emite invoice com cliente fictício.
- **AC-025-02** Usuário cria 3 clientes nacionais com documentos distintos e os lista.
- **AC-025-03** CPF/CNPJ inválido retorna `400`; duplicado retorna `409`.
- **AC-025-04** Cliente `US` sem `tax_id` é criado com `tax_id_type='none'`; com documento, `tax_id_type='foreign'`.
- **AC-025-05** `country_code` inexistente retorna `400`.
- **AC-025-06** E-mail e telefone do cliente são persistidos e devolvidos.
- **AC-025-07** Cliente de outro usuário retorna `404` em GET/PUT/activate/deactivate.
- **AC-025-08** Cliente inativo não pode ser usado em nova invoice.
- **AC-025-09** Invoice com `client_id` de outro usuário retorna `404`; nenhuma linha é criada.
- **AC-025-10** Invoice com `simulation_id` de outro usuário retorna `404`.
- **AC-025-11** Snapshot da invoice vem do banco, não do payload; divergência retorna `400`.
- **AC-025-12** Emissor CNPJ de outro usuário retorna `403`.
- **AC-025-13** Dois emissores distintos emitem `INV-202611-0001` no mesmo mês sem colisão.
- **AC-025-14** `alembic upgrade head` cria o unique composto; downgrade restaura o global após checar duplicidade.
- **AC-025-15** `POST /v1/simulate` e `POST /v1/invoice` não alteram contagens de tabelas nem `invoice_sequences`.
- **AC-025-16** Fluxo anônimo não seta cookie de sessão e não exige CSRF.
- **AC-025-17** `/v1/auth/logout` sem `X-CSRF-Token` retorna `403`.
- **AC-025-18** Rate limits retornam `429` e usam IP real atrás do proxy.
- **AC-025-19** Nenhum log contém nome/documento/e-mail/endereço/valor de cliente.
- **AC-025-20** Suíte de clientes e invoices permanece verde.
- **AC-025-21** `GET /v1/invoices`, `GET /v1/simulations` e `GET /v1/clients` respondem `{items,total,limit,offset}`; `total` respeita os filtros.
- **AC-025-22** Emissor é validado contra `provider_profiles.cpf` e `provider_cnpjs`; CNPJ que é só identificador de login, sem documento de emissão, retorna `403 issuer_not_allowed`.
- **AC-025-23** Clone de invoice com emissor inativo retorna `409 issuer_inactive`; a invoice original não é alterada.
- **AC-025-24** Migration cria `provider_cnpjs` com coluna `id` identidade e importa CNPJs de `provider_profiles.cnpj` e de `user_login_identifiers.kind='cnpj'`; contagem de emissores não diminui.
- **AC-025-25** `422 limit_exceeded` é devolvido ao exceder 100 clientes ativos; `401`, `403` e `429` não viram `500`.

## 9. Segurança e LGPD

### 9.1 Controles

| Controle | Regra |
|----------|-------|
| Isolamento | toda query filtra `owner_user_id` |
| Cross-owner | 404, não 403, para não confirmar existência |
| Snapshot | derivado do banco; payload não sobrescreve |
| Emissor | documento de emissão ativo do titular (`provider_profiles.cpf` ou `provider_cnpjs`) |
| Duplicidade | unique parcial + 409 |
| Rate limit | por IP real e por usuário |
| CSRF | double-submit em todas as mutações autenticadas |
| Logs | zero PII |
| Cache | `no-store` no PDF anônimo |
| Numeração | unique por emissor, sem vazamento de sequência alheia |

### 9.2 LGPD/GDPR

- Cliente é dado de terceiro; o usuário declara base legal e finalidade.
- Coletar apenas nome, documento, e-mail, telefone, endereço e país.
- Cliente inativo mantém histórico de invoices; exclusão definitiva segue SPEC-022.
- O fluxo anônimo não persiste dados de terceiros.
- A invoice persistida é retida por 5 anos + 6 meses; dados pessoais são anonimizados após o prazo.
- Exportação/portabilidade e exclusão ficam no escopo da SPEC-022.

### 9.3 Ameaças

| Ameaça | Mitigação |
|--------|-----------|
| IDOR em `client_id` | filtro por dono + 404 |
| IDOR em `simulation_id` | filtro por dono + 404 |
| Sequestro de numeração | unique por emissor |
| Emissor falsificado | validação de CNPJ do titular |
| Enumeração de clientes | 404 uniforme + rate limit |
| Abuso do fluxo anônimo | rate limit por IP real |
| Vazamento em log | zero PII + revisão de `caplog` |
| CSRF | header obrigatório |

## 10. Testes obrigatórios

### 10.1 Unidade

- normalização e checksum de CPF/CNPJ;
- validação de país;
- inferência de `tax_id_type`;
- normalização de e-mail/telefone;
- montagem de snapshot a partir do cliente;
- validação de emissor.

### 10.2 Integração

- CRUD de clientes nacional/internacional;
- zero clientes;
- limite de 100;
- duplicidade 409;
- cross-owner 404 em GET/PUT/activate/deactivate;
- invoice com cliente persistido e fictício;
- invoice cross-owner;
- emissor cross-owner;
- emissor válido via `provider_profiles.cpf` e via `provider_cnpjs`;
- clone com emissor inativo retorna `409 issuer_inactive`;
- numeração com dois emissores;
- clone;
- envelope `{items,total,limit,offset}` em invoices e simulações;
- migration up/down.

### 10.3 Anônimo

- contagem de tabelas antes/depois;
- `invoice_sequences` inalterado;
- ausência de `Set-Cookie: session`;
- `Cache-Control: no-store`;
- rate limit.

### 10.4 e2e

- cliente nacional e internacional na UI;
- estado vazio;
- edição e inativação;
- invoice com cliente persistido;
- invoice fictícia;
- fluxo anônimo completo.

## 11. Rollback

1. Reverter rotas de clientes para o contrato anterior (array, CPF/CNPJ apenas).
2. Reverter `tax_id_digits` para `CHAR(14) NOT NULL` somente se não houver clientes internacionais; caso contrário, manter nullable.
3. Restaurar `uq_invoices_invoice_number` somente após remover duplicatas entre emissores.
4. Reverter CSRF de logout apenas se o frontend não enviar header; não recomendado.
5. Reverter rate limits se causarem indisponibilidade; registrar débito.
6. Manter `provider_cnpjs` e `provider_profiles.cpf` no rollback de aplicação; o código anterior ignora as colunas novas e o histórico de invoices é preservado.

## CHANGELOG

| Versão | Data | Autor | Mudança |
|--------|------|-------|---------|
| 0.1.0 | 2026-11-17 | agent-project-analyst | Proposta inicial de emenda à SPEC-019/020 |
| 0.2.0 | 2026-11-17 | agent-project-analyst | Correções da revisão: emissor validado contra documento de emissão (`provider_profiles.cpf` + `provider_cnpjs`), backfill de CNPJ legado, `id` com identity no DDL, clone com emissor inativo (`409 issuer_inactive`), envelope `{items,total,limit,offset}` em invoices e simulações, `tax_id_type='none'` para internacional sem documento, `422 limit_exceeded`, ACs 21–25 |
