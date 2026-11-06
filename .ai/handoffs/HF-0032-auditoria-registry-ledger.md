---
id: ai-handoffs-hf-0032-auditoria-registry-ledger
title: 'Handoff: Auditoria dedicada de registry.yaml e ledger.yaml — circuito de agentes, regras de roteamento, subutilização
  e desvio de função (TA-0032)'
type: handoff
version: 1.0.0
status: ready
owner: agent-project-analyst
agent: agent-project-auditor
derived-from:
- .ai/handoffs/HF-0032-auditoria-registry-ledger.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
created: 2026-11-05
updated: 2026-11-06
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---
# Handoff: Auditoria dedicada de registry.yaml e ledger.yaml — circuito de agentes, regras de roteamento, subutilização e desvio de função (TA-0032)

## Contexto

Rodada garantidora do GP/Humano (2026-11-02, Art. 5.1): auditar o roster SSOT e o ledger,
garantindo que não há subutilização nem desvio de função dos agentes, e normatizar o que for
de custódia permitida. Sinais já coletados pelo orquestrador (VERIFICAR e confirmar/refutar
com evidência — não são veredictos):

- `sync_agent_registry.py --check` exit 0; `validate_nexus_yaml.py` exit 0;
  `nexus_dispatcher.py --report`: 46 promulgados; **`agent-factory-architect-ultimate` em
  camada UNKNOWN** (fora de AGENT_TOPOLOGY, não-dispatchável, mas consta como upstream de
  `agent-nexus-prime-ultimate` no registry); `missing_from_dag: []`.
- Suíte `tests/agents/` baseline 4 failed / 149 passed / 1 skipped:
  `test_topology_report`; `test_gate_promulgation[agent-nexus-prime-ultimate]`
  ("constitution.md Art. 4.7 budget"); `test_onda6_chain_wiring` e
  `test_onda7_no_loose_ends_too_early` ("agentes sem consumidores:
  {agent-reviewer, agent-gatekeeper, agent-clean-code-evaluator}").
- Suspeitas de desvio de função: `agent-docker-specialist` — description refere "documentation
  custody" (README/docs) enquanto o nome/slug sugere Docker (registry.yaml:272-287).
- Ledger (`.ai/agents/ledger.yaml`): entry TA-0028 com `sender == receiver`
  (nexus-prime-ultimate → nexus-prime-ultimate — auto-delegação, Art. 4.5); entry TA-0027
  `status: escalated` desde 2026-10-31 (possivelmente stale/aberto); entries TA-0029..0031
  desta sessão.

## Tarefa

Auditoria somente-leitura + relatório (nada é corrigido nesta tarefa; remediação é onda
seguinte ou escala):

1. **Mapa do circuito de agentes**: topologia por camada (L0/L1/L2/L3/META/FORGE-LEGACY),
   upstream/downstream do registry vs AGENT_TOPOLOGY (`scripts/validate_nexus_yaml.py`),
   regras de roteamento vigentes (`scripts/nexus_dispatcher.py`: KNOWN_SLUGS, VALID_ACTIONS,
   anti self-delegação Art. 4.5, contrato half-duplex) — incluindo verificar se o docstring
   do dispatcher ("conjunto válido de ações por camada") corresponde ao código (VALID_ACTIONS
   global): desvio doc↔código é achado.
2. **Subutilização**: agents promulgados sem consumidores/downstream efetivo (comece pelos 3
   gates do teste onda7), agents nunca referenciados em ledger/handoffs desde a criação,
   camadas com WIP zero persistente. Cada achado com evidência (`arquivo:linha` ou saída de
   script) e impacto (ex.: gate L3 sem consumidor = cadeia de merge sem acionamento).
3. **Desvio de função**: divergências slug↔description↔prompt do agente (ex.:
   docker-specialist), upstream/downstream assimétricos (A lista B mas B não lista A),
   ações do ledger fora do vocabulário do dispatcher (ex.: "fix-table", "review-plan-v2.1.0"
   em VALID_ACTIONS?).
4. **Integridade do registry**: sync em dia; entradas `legacy-forge`/null (version, description);
   header comment e version enum (imutáveis — DON'T 12) conferidos como intactos; drift
   `missing_from_dag`/UNKNOWN.
5. **Auditoria do ledger**: esquema por entry (task_id, sender, receiver, action, status,
   exit_status, timestamp, notes), append-only, auto-delegação (Art. 4.5), escalonamentos
   stale (TA-0027), PII/LGPD (só task IDs, zero dados pessoais), coerência de timestamps.
6. **Root-cause dos 4 testes vermelhos** (um por achado #2/3/4), classificando cada correção
   por custódia: (a) nexus/orquestrador-direto; (b) script (sync/validate/dispatcher);
   (c) forja de agente → AFA-ULTIMATE (Art. 4.1); (d) decisão Humana/CCB (Art. 5.1).
7. **Propostas de normatização** por achado, NÃO executadas — incluindo o que é normatizável
   sem tocar em arquivos de agente (custódia AFA) e o que exige promulgação.
8. Se (e somente se) houver violação confirmada com evidência: entradas **VIO-NNN** no
   registro append-only de violações (sua custódia), seguindo o padrão sequencial existente.

## Critérios de Aceite

- [ ] Relatório emitido em `docs/auditorias/` seguindo o padrão `AUD-YYMMDD-NN` existente (próximo número livre), com frontmatter e evidência `arquivo:linha`/exit code por achado
- [ ] Mapa do circuito completo (camadas + regras de roteamento dispatcher documentadas)
- [ ] Subutilização mapeada com evidência (inclui os 3 gates sem consumidores do onda7)
- [ ] Desvio de função mapeado (inclui docker-specialist e assimetrias upstream/downstream)
- [ ] Integridade do registry verificada (sync/header/version-enum/legacy/UNKNOWN)
- [ ] Ledger auditado: schema, append-only, auto-delegação TA-0028, stale TA-0027, LGPD
- [ ] Root-cause dos 4 testes vermelhos com classificação de custódia (a–d) por correção
- [ ] Propostas de normatização NÃO executadas; itens AFA/CCB sinalizados como pendência
- [ ] VIO-NNN emitidos apenas para violações confirmadas (ou justificativa de ausência)

## Restrições

- Auditoria = somente leitura + relatório (+ VIO se aplicável). NÃO editar registry.yaml,
  ledger.yaml, agent files, scripts, testes, constitution — correção é outra onda.
- NUNCA alterar: `constitution.md` (inclusive Art. 4.7), registry header comments/version
  enum, `.opencode/agents/*` (forja AFA, Art. 4.1), ADRs existentes.
- Cada afirmação cita `arquivo:linha` ou exit code de script; incerteza = `UNKNOWN - verify`.
- Narrativa PT-BR; identificadores/status EN. Sem invenção de status, datas ou métricas.
- Retorno: parcel half-duplex schema 6 (enum `accepted|rejected|escalated|require_clarification`,
  `route` objeto {sender, receiver}), `dod` com todos os AC, `notes` ≤5 linhas com top 3
  achados. Resposta final ≤1200 tokens (relatório vai ao ARQUIVO).
- kill_switch: inherited
- CPU-only, sem CUDA/cloud; FOSS-only; LGPD primária (zero PII em relatórios e volumes).
