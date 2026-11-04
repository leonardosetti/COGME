---
id: HF-0029
agent: agent-sdd-specialist
status: done
created: 2026-11-02
---
# Handoff: SPEC de camadas de containers para a produção ortogonal do COGME

## Contexto

A Constituição (Art. 10.1) manda que as camadas de execução do projeto rodem ortogonais:
cada camada em container Docker próprio, construída/versionada/reiniciada
independentemente, comunicando-se **apenas por interface declarada** (porta, volume ou
API) — nunca por estado implícito compartilhado. A stack canônica é
PostgreSQL + Docker Compose + Nginx latente (ADR-010; vence qualquer texto SQLite,
igual à tabela de conflitos de `.ai/specs/backend-mvp-v1.spec.md` §1).

Estado atual no filesystem (verificado em 2026-11-02): `docker-compose.yml` único com
serviços `db` (PostgreSQL 15-alpine pinnado por digest), `migrate` (Alembic), `web`
(FastAPI+Jinja num só serviço) e `proxy` (nginx, profile latente); redes `data`
(internal) e `edge`; `Dockerfile` multi-stage com USER 10001; `.env.example`;
`infra/nginx/default.conf`. Hoje **Back e Front estão fundidos no serviço `web`** — a
produção ortogonal pede a separação em camadas explícitas.

Esta SPEC entrega a camada de containers sob demanda do orquestrador (TA-0029).

## Tarefa

Produzir UMA spec em `./.ai/specs/` (estilo/cabeçalho/Status iguais a
`backend-mvp-v1.spec.md`), abordando no mínimo:

1. **Três camadas obrigatórias**: Dados (PostgreSQL + volumes), Back (API FastAPI),
   Front (serviço de apresentação — separação do `web` atual); camadas aderentes
   (migrate, proxy/edge, cache) só com justificativa explícita (YAGNI).
2. **Rede dockerizada**: topologia de redes declarada por camada, regra "interface
   declarada única" (Art. 10.1), isolamento `data` interno vs `edge`, who-talks-to-whom.
3. **Reprodutibilidade**: `git pull` → `.env` copiado de `.env.example` →
   `docker compose up --build` deve bastar em qualquer ambiente local (CPU-only,
   8700G/60GB — sem CUDA/cloud, Art. P-02); builds por digest imutável (Art. 10.2).
4. **Segurança**: non-root, `no-new-privileges`, `cap_drop: ALL`, `read_only`+tmpfs,
   portas presas em `127.0.0.1`, segredos só via `.env` (nunca commitado), imagens
   pinadas por digest, LGPD (zero PII em logs/volumes de terceiros, Art. 10.3).
5. **Testabilidade**: healthcheck por camada, pirâmide unit/contract/integration/e2e
   entre camadas, coverage ≥80% (US-008), testes de contrato de rede (quem fala com quem).
6. **CI/CD desta fase**: pipeline de build/teste das camadas (lint+testes ≤5min/push,
   US-011), gap G-05 (`.github/workflows/ci.yml` vazio), gates nunca bypassados.
7. **Interoperabilidade**: contrato declarado entre as três camadas (OpenAPI/versão de
   porta, volumes nomeados, healthchecks de dependência) e compatibilidade com o
   contrato `/v1` existente (`backend-mvp-v1.spec.md` §3).
8. **User Stories** no Padrão B — GWT (OKB §9.3, `docs/conhecimento/OKB.md:539`):
   narrativa "Como [papel], quero [ação], para [benefício]" + ≥2 cenários
   Dado/Quando/Então por story, numeração **US-018+** (US-001..017 já existem em
   `.ai/specs/requisitos-review-round-1.md`), com rastreabilidade dupla
   (REQ-NN / ADR-010 / Art. 10.x) e status.
9. **Acceptance Criteria** binários por story (testes necessários) e **proposta de
   UAT**: escopo, fluxos críticos, critério de passagem (100% dos fluxos críticos
   passam, zero defeitos críticos/bloqueantes — precedente US-009), papéis e evidências.

## Critérios de Aceite

- [x] Spec criada em `./.ai/specs/` com cabeçalho Status no estilo `backend-mvp-v1.spec.md`
- [x] Três camadas nomeadas (Dados/Back/Front) e camadas aderentes justificadas (ou explicitamente recusadas por YAGNI)
- [x] Topologia de redes docker declarada; regra de interface declarada única citada (Art. 10.1)
- [x] Fluxo de reprodutibilidade passo-a-passo (pull → .env → compose up) presente e local-only
- [x] Bloco de segurança completo: non-root, no-new-privileges, cap_drop, read_only, 127.0.0.1, segredos via .env, digest pinning, LGPD
- [x] Estratégia de testes por camada com coverage ≥80% e healthchecks declarados
- [x] Pipeline CI/CD da fase especificado, citando G-05 e US-011
- [x] Contrato de interoperabilidade entre as três camadas (API/porta/volume/versão) declarado
- [x] ≥3 User Stories Padrão B (GWT) numeradas US-018+ com ≥2 cenários AC cada e rastreabilidade
- [x] Proposta de UAT com fluxos críticos, critério de passagem e evidências
- [x] Conflito PostgreSQL vs SQLite resolvido por tabela de conflitos (Constituição 10.1 / ADR-010 vencem)

## Restrições

- SPEC only: nenhum arquivo de código, compose, Dockerfile ou workflow é alterado nesta tarefa (Art. 4.5 — implementação é onda seguinte).
- Nunca alterar: `constitution.md`, `.ai/agents/registry.yaml`, ADRs existentes, esta constituição de handoff.
- Hierarquia Art. 2: constituição > ADR-010 > planos > SDD > código.
- Identificadores/status em EN; narrativa em PT-BR. Zero dependência cloud/CUDA/proprietary.
- Editar somente o arquivo da spec (árvore de arquivos única, sem paralelismo).
- Retorno obrigatório em parcel half-duplex (schema 6 do orquestrador) com `dod` e artefatos.
