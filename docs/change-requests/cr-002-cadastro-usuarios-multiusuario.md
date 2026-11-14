---
id: docs-change-requests-cr-002-cadastro-usuarios-multiusuario
title: CR-002 — Contas de usuários, sessões e histórico de invoices
type: change-request
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- constitution.md (Arts. 1.2, 1.3, 3, 5.1, 9.1-9.3)
- .ai/specs/spec-002-requisitos-review-round-1.spec.md (OS-01, C-03, US-004, US-016/US-017)
- .ai/specs/spec-004-backend-mvp-v1.spec.md (fora de escopo de autenticação e persistência)
- .ai/specs/spec-007-invoice-data-model-v1.spec.md (modelo canônico de invoice)
- .ai/specs/spec-008-frontend-web-responsive-v1.spec.md (i18n, autenticação e histórico fora de escopo)
- .ai/specs/spec-015-lgpd-produto-proposta-v1.spec.md (critérios LGPD ainda condicionais)
- manifestação do PO/GP em 2026-11-13 (demanda de contas multiusuário)
last-revised: '2026-11-13'
lgpd-class: n/a
tags:
- change-request
- autenticacao
- multiusuario
- invoices
- lgpd
- gdpr
cr-number: CR-002
impacto: critico
prazo-analise-gp: '2026-11-15'
decisao-ccb: pendente
instrumento: pendente
github-issue: '#35'
---

# CR-002 — Contas de usuários, sessões e histórico de invoices

## 1. Resumo

Esta CR abre a mudança de escopo necessária para o COGME deixar de operar como aplicação local sem identidade e passar a oferecer:

1. contas de usuário com sessão individual;
2. acesso isolado às simulações salvas e às invoices do próprio usuário;
3. cadastro da empresa prestadora, dos clientes e das contas bancárias de depósito;
4. histórico persistente e confiável de simulações e invoices;
5. emissão de invoice em português para cliente nacional e em inglês para cliente estrangeiro;
6. ciclo de vida da conta — ativo, dormente e exclusão definitiva — com regras LGPD e GDPR.

A CR **não aprova a iniciativa**. Ela registra o impacto, ativa a decisão do CCB e bloqueia qualquer implementação até a tramitação normativa exigida.

## 2. Regra aplicável e necessidade da CR

A iniciativa conflita com o escopo canônico vigente:

- `constitution.md:45` limita o produto a simulação cambial, comparação de regimes, spread/IOF e emissão de invoice PDF.
- `constitution.md:47` exige emenda constitucional prévia para qualquer item fora do escopo congelado.
- `.ai/specs/spec-002-requisitos-review-round-1.spec.md:142,154-165` classifica autenticação e cadastro multiusuário como **OS-01**, fora de escopo.
- `.ai/specs/spec-004-backend-mvp-v1.spec.md:54` exclui autenticação, cadastro e histórico de simulações do backend.
- `.ai/specs/spec-008-frontend-web-responsive-v1.spec.md:242` exclui i18n multi-idioma, autenticação/multiusuário e histórico de simulações.

O fluxo aplicável está em `constitution.md:217-222`:

1. toda mudança abre Issue com label `change-request`;
2. o GP analisa o impacto em até 48 horas;
3. a decisão ocorre em até 24 horas depois;
4. mudança do escopo do MVP, da linha de base ou dos marcos exige ADR específica;
5. divergência com a Constituição é resolvida por emenda, nunca por ADR.

Consequência: **cadastro de usuários, histórico persistido, diretório de clientes, dados bancários e invoice bilíngue exigem CR, parecer de auditoria/compliance, ADR quando aplicável e emenda constitucional antes da implementação.**

## 3. Demanda aprovada para avaliação

A demanda humana de 2026-11-13 define:

- login por qualquer identificador associado à conta: email, CPF ou CNPJ;
- identificador interno opaco, gerado e pesquisado por hash;
- senha e recuperação de senha por email;
- sessão individual e isolamento dos dados por proprietário;
- perfil do usuário: nome, email, telefone, CPF, categoria MEI/Pessoa Jurídica, CNPJ quando aplicável, endereço e dados bancários da empresa;
- carteira de clientes com estado ativo/inativo; cliente não cadastrado continua válido para invoice com dados fictícios;
- edição dos dados do usuário, exceto email e CPF;
- simulação salva somente por escolha explícita do usuário;
- acesso ao histórico próprio de simulações e invoices;
- invoice em PT-BR para cliente nacional e em inglês para cliente estrangeiro;
- exclusão definitiva da conta e conta dormente/suspensa, sujeitas a LGPD/GDPR.

## 4. Escopo proposto

### 4.1 Identidade e acesso

- cadastro, login, logout, recuperação de senha e revogação de sessão;
- autenticação por email, CPF ou CNPJ normalizados;
- alias de login armazenado por HMAC com chave secreta, não por hash simples;
- senha armazenada com Argon2id;
- sessão opaca, revogável e expirada; token persistido apenas como hash;
- autorização server-side por `owner_user_id` obtido da sessão, nunca aceito do cliente.

### 4.2 Empresa prestadora e dados bancários

- perfil prestador com categoria MEI/Pessoa Jurídica;
- CNPJ obrigatório quando a categoria for Pessoa Jurídica;
- endereço da prestadora;
- uma ou mais contas bancárias de depósito, inclusive dados necessários a wire transfer;
- snapshot dos dados da prestadora e da conta bancária na invoice finalizada.

### 4.3 Carteira de clientes

- cadastro opcional de cliente com nome, documento, endereço, país e estado ativo/inativo;
- inativação por contrato suspenso ou encerrado;
- dados fictícios admittedos sem criação de registro na carteira;
- snapshot do cliente na invoice para que editions posteriores não alterem o histórico.

### 4.4 Simulações e histórico de invoices

- persistência opcional de simulação, por escolha explícita;
- snapshot da cotação e do resultado recalculado, para não depender da cotação vigente;
- `owner_user_id` obrigatório em simulations e invoices;
- consulta e download apenas dos próprios recursos;
- invoice em rascunho/finalizada, com finalizada imutável, para permitir histórico correto;
- numeração e clonagem de invoices continuam sujeitas à decisão do CCB.

### 4.5 Idioma da invoice

- idioma derivado do país do cliente: `BR` → `pt-BR`; qualquer outro país → `en`;
- cliente fictício exige país explícito, sem inferência silenciosa;
- Snapshots da invoice registram o idioma usado;
- erros e interface do produto permanecem em PT-BR; i18n integral da interface permanece fora de escopo.

### 4.6 Ciclo de vida e privacidade

- conta `active` ou `dormant`; conta dormente não cria novos recursos e pode ser reativada;
- exclusão definitiva revoga sessões e elimina credenciais, perfil, banco, clientes e simulações;
- retention de invoices finalizadas e eventual anonimização dependem de parecer jurídico e da obrigação legal aplicável;
- LGPD é a jurisdição primária; GDPR é aplicado quando a oferta ou o monitoramento alcance pessoas no EEE/Reino Unido;
- sem dado real em artefatos técnicos, logs, seeds ou fixtures.

## 5. Necessidade declarada de novas tabelas e campos

A initializer exige **novas tabelas**, não apenas campos em `invoices`. O modelo mínimo proposto é:

| Tabela | Natureza | Campos essenciais |
|---|---|---|
| `users` | nova | `id`, `internal_username_hash`, `name`, `email`, `phone`, `cpf`, `password_hash`, `status`, `dormant_since`, `last_login_at`, `created_at`, `updated_at` |
| `user_login_identifiers` | nova | `id`, `user_id`, `kind`, `lookup_hmac`, `created_at`, `retired_at` |
| `user_sessions` | nova | `id`, `user_id`, `token_hash`, `created_at`, `last_seen_at`, `expires_at`, `revoked_at` |
| `password_reset_tokens` | nova | `id`, `user_id`, `token_hash`, `created_at`, `expires_at`, `used_at` |
| `provider_profiles` | nova | `user_id`, `legal_name`, `category`, `cnpj`, endereço, `created_at`, `updated_at` |
| `provider_bank_accounts` | nova | `id`, `user_id`, tipo, banco, agência, conta, dígito, SWIFT/BIC, IBAN, moeda, `is_primary`, timestamps |
| `clients` | nova | `id`, `owner_user_id`, `name`, `tax_id`, `address`, `country_code`, `is_active`, `deactivated_at`, timestamps |
| `simulations` | nova | `id`, `owner_user_id`, entrada validada, resultado, cotação, `created_at` |
| `account_lifecycle_events` | nova | `id`, `user_id`, `event_type`, `from_status`, `to_status`, `created_at` |
| `invoices` | **emenda** | adicionar `owner_user_id`, `client_id`, `simulation_id`, `status`, `locale`, `client_country_code`, `finalized_at`, `supersedes_invoice_id` |

Regras estruturais indispensáveis:

- `users.email` e `users.cpf` são imutáveis;
- `provider_profiles.cnpj` pode ser alterado, mas o alias de login CNPJ deve ser rotacionado na mesma transação;
- unicidade por `(kind, lookup_hmac)` em `user_login_identifiers`;
- FK `ON DELETE` explícita para todo recurso pertencente ao usuário;
- `invoices` recebe constraints para status, locale e owner;
- invoice finalizada não pode ser alterada; alterações de perfil, cliente ou banco só afetam novos documentos.

O detalhamento normativo de tipos, constraints e índices consta da proposta `docs/especificacoes/spec-prop-017-conta-multiusuario.md`.

## 6. Artefatos afetados

| Artefato/área | Impacto | Ação necessária |
|---|---|---|
| `constitution.md` | inclui identidade, dados de cliente/banco, histórico e i18n | emenda de escopo após auditoria e ratificação CCB |
| TAP/plano de gerenciamento | altera escopo, marco M4, custo e capacidade | replanejamento e decisão de marco |
| `spec-002` | OS-01 hoje rejeita autenticação/multiusuário | nova versão da spec e user stories próprias |
| `spec-004` | rotas, schemas e persistência atuais | emenda de contrato HTTP e segurança |
| `spec-007` | modelo canônico de invoice sem owner, status e locale | emenda de modelo de dados |
| `spec-008` | UI sem login, perfil, clientes e históricos | emenda frontend e acessibilidade |
| `spec-015` | D2-D6 ainda pendentes; modelo passa a ter mais dados pessoais | parecer LGPD/GDPR e decisões de retenção/erase |
| Banco/Alembic | seis tabelas de identidade/domínio, simulations e clientes; emenda de `invoices` | specs e migrações `upgrade/downgrade` |
| Segurança | senha, sessão, reset, CSRF, autorização por recurso | threat model e testes negativos |
| Dependências | hash de senha requer biblioteca Argon2id FOSS | registro de dependência e teste de licença |
| Infra | recuperação de senha exige canal de email | SMTP local/autohospedado ou decisão de Bypass |

## 7. Decisões requeridas do CCB/PO

| ID | Decisão | Responsável |
|---|---|---|
| CR2-D01 | admitir contas multiusuário no escopo e reverter OS-01 | CCB/GP |
| CR2-D02 | Papel controlador/operador, bases legais e direitos LGPD/GDPR | CCB + parecer jurídico/compliance |
| CR2-D03 | retention de invoices finalizadas versus “exclusão sem retenção” | CCB + parecer jurídico |
| CR2-D04 | prazo e critérios de dormência/reativação | PO/CCB |
| CR2-D05 | regra de idioma: país do cliente como fonte canônica | PO/CCB |
| CR2-D06 | canal de email e reset dentro da soberania de dados | Arquitetura/CCB |
| CR2-D07 | ratificar identity, histórico e diretório de clientes como escopo do MVP | CCB/GP |
| CR2-D08 | cycle Rascunho/Finalizada e clonagem de invoice | CCB/PO |
| CR2-D09 | replanejar marco/custo ou recusar o escopo adicional | GP/CCB |

## 8. Avaliação

### 8.1 Viabilidade

- **Técnica:** viável no stack PostgreSQL/FastAPI/SQLAlchemy/Alembic/Jinja2, com uma dependência FOSS para Argon2id e desenho de sessão/segurança próprio.
- **Negociais:** valor direto para o usuário final, porém a iniciativa amplia o produto e não cabe no restante do MVP sem replanejamento.
- **Conformidade:** exige decisões jurídicas ainda abertas; a proposta técnica não substitui parecer jurídico.
- **Segurança:** aumenta a superfície de ataque; sessão, reset, CSRF, isolamento por owner e rotação de alias são gates, não enhancements.
- **Cronograma:** impacto crítico. A entrega final vigente é 15/12/2026 (`constitution.md:43`); a implementação estimada não é compatível com esse prazo sem redução de escopo ou novo marco.

### 8.2 Resultado da avaliação

**CR aprovada para tramitação; iniciativa condicionada.** A proposta de spec é tecnicamente viável e deve seguir para revisão, mas não pode ser promovida a spec oficial nem implementada antes das decisões CR2-D01..D09 e da emenda constitucional.

## 9. Specs diretamente relacionadas

A derivação completa, dependências e ordem de emissão estão em `docs/especificacoes/spec-prop-017-conta-multiusuario.md` §2 e §13.

| ID sugerido | Spec direta |
|---|---|
| SPEC-017 | Identidade, aliases de login, senha, sessões e recuperação |
| SPEC-018 | Perfil da prestadora e contas bancárias de depósito |
| SPEC-019 | Carteira de clientes e estado ativo/inativo |
| SPEC-020 | Simulações salvas, histórico e ciclo de vida das invoices |
| SPEC-021 | Invoice bilíngue PT-BR/EN |
| SPEC-022 | Ciclo de vida da conta, dormência, exclusão e privacidade LGPD/GDPR |

## 10. Critérios para encerrar a CR

- [ ] Issue da CR publicada com label `change-request` e link para este artefato.
- [ ] Parecer de auditoria/compliance anexado.
- [ ] ADR emitido se a decisão alterar arquitetura, stack ou baseline.
- [ ] Emenda constitucional ratificada pelo CCB, com changelog e co-assinatura.
- [ ] CR2-D01..D09 deliberadas e registradas.
- [ ] As seis specs diretas aprovadas ou explicitamente recusadas.
- [ ] TAP, cronograma e orçamento replanejados antes da implementação.

## 11. Rollback

Até a ratificação, nenhuma alteração de código ou banco é autorizada. Se a CR for recusada, esta proposta e a proposta associada serão marcadas `arquivado`/`obsoleto`, sem migração de dados e sem impacto no runtime.

## CHANGELOG

- 1.0.0 — 2026-11-13: CR aberta a partir da demanda humana de contas multiusuário; impacto constitucional, novo modelo de dados, decisões pendentes e deriva de seis specs documentados. Nenhum código, migração ou escopo vigente alterado.
