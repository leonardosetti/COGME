---
id: ai-handoffs-hf-0030-nginx-aceito-demo
title: 'Handoff: Amenda Nginx aceito-e-mantido + comunicação integrada para demo local (TA-0030)'
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0030-nginx-aceito-demo.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---
# Handoff: Amenda Nginx aceito-e-mantido + comunicação integrada para demo local (TA-0030)

## Contexto

Ratificação Humana/GP recebida nesta sessão (2026-11-02, constitution.md Art. 5.1 — autoridade
de outorga/ratificação/promulgação outorgada e registrada em ledger): para a SPEC de camadas de
containers, o Nginx/proxy passa de "latente (profile opcional)" para **ACEITO E MANTIDO** —
serviço sempre ativo, com comunicação integrada entre TODOS os containers, de modo que, feito o
deploy e o clone do repo, seja possível executar localmente o MVP para demonstração real das
funcionalidades.

Estado atual verificado: `.ai/specs/container-layers-v1.spec.md` (344 linhas) trata o proxy como
`--profile proxy` opcional (§5, §8; `docker-compose.yml:89` `profiles: ["proxy"]`; ADR-010 descreve
"Nginx latente"). A SPEC é fase de especificação: o estado alvo declarado aqui é implementado na
onda seguinte (Art. 6.1 — especifica → implementa → valida → registra); a edição do
`docker-compose.yml` real NÃO faz parte desta tarefa.

## Tarefa

Amenda cirúrgica em `.ai/specs/container-layers-v1.spec.md` (ÚNICO arquivo editável):

1. **§3/§4/§5** — proxy promovido a camada aderente **aceita e mantida** (sempre ativa no fluxo
   padrão, não mais "profile opcional"); matriz quem-fala-com-quem (§4.2) integrada cobrindo
   TODOS os containers em cadeia: usuário → proxy → front → back → db (e migrate no boot), com
   healthchecks em cadeia; front alcançável pelo usuário somente via proxy em `127.0.0.1:8080`.
2. **§5** — caminho de demonstração passo-a-passo: `git pull` → `cp .env.example .env` →
   `docker compose up --build` (proxy incluído) → abrir `127.0.0.1:8080` → fluxos MVP
   (health, simulação cambial, invoice PDF) funcionando de ponta a ponta, local CPU-only.
3. **§2 (tabela de conflitos)** — registrar fonte vencedora: "proxy aceito e mantido" vence
   "Nginx latente", com citação `GP/Humano 2026-11-02, Art. 5.1`. NÃO alterar ADR-010;
   listar emenda de ADR-010 como follow-up pendente (arquiteto → CCB).
4. **Coerência** — ajustar SOMENTE os trechos que contradigam o proxy ativo (ex.: §7.1
   healthcheck do proxy, §8 CI, §13 fora-de-escopo, menções a profile opcional). Preservar
   US-018..021, AC, segurança, UAT e demais decisões intactos.
5. **Cabeçalho Status + CHANGELOG** do arquivo: data 2026-11-02, motivo da amenda,
   ratificação GP/Humano (Art. 5.1).

## Critérios de Aceite

- [ ] Proxy descrito como aceito e mantido (não-latente) em §3/§4/§5 da SPEC
- [ ] Matriz de comunicação integrada cobre TODOS os containers (proxy, front, back, db, migrate) com healthchecks em cadeia
- [ ] Caminho de demo `clone → .env → compose up → 127.0.0.1:8080` presente e local-only (CPU-only, sem cloud/CUDA)
- [ ] Ratificação GP/Humano 2026-11-02 (Art. 5.1) registrada na tabela de conflitos §2
- [ ] ADR-010 não alterado; emenda ADR-010 listada como follow-up pendente
- [ ] US/AC/segurança/UAT preservados; apenas trechos contraditórios com proxy ativo ajustados
- [ ] Cabeçalho Status e CHANGELOG do arquivo atualizados
- [ ] Nenhum outro arquivo modificado

## Restrições

- Editar EXCLUSIVELY `.ai/specs/container-layers-v1.spec.md`.
- Proibido tocar: `constitution.md`, `.ai/agents/registry.yaml`, `docs/decisoes/*` (ADRs),
  handoffs, `docker-compose.yml`, `Dockerfile`, workflows, código-fonte (implementação = onda seguinte).
- Narrativa PT-BR; identificadores/status/caminhos EN. Toda alegação cita `arquivo:linha`;
  incerteza marcada `UNKNOWN - verify`. Nada de invenção de status, datas ou métricas.
- Retorno obrigatório: parcel half-duplex (schema 6 do orquestrador), `dod` só com todos os
  critérios verificados. Resposta final ≤1200 tokens (conteúdo longo vai ao ARQUIVO).
