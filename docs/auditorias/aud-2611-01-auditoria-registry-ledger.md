---
id: AUD-2611-01
title: AUD-2611-01 — Auditoria de registry + ledger + circuito de roteamento (TA-0032)
version: 1.0.0
class: relatorio-auditoria
status: draft
owner: agent-project-analyst
derived-from:
- docs/auditorias/aud-2611-01-auditoria-registry-ledger.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a — somente task IDs; varredura e-mail/CPF/telefone/nome = 0 hits
tags:
- auditorias
- docs
- normalizado
---

# AUD-2611-01 — Auditoria de registry + ledger + circuito de roteamento (TA-0032)

## 1. Escopo e método

Auditoria **somente-leitura** de `.ai/agents/registry.yaml`, `.ai/agents/ledger.yaml` e do
circuito de roteamento (`scripts/nexus_dispatcher.py`, `scripts/validate_nexus_yaml.py`,
`scripts/sync_agent_registry.py`, `scripts/mcp_nexus_ledger.py`). Nada foi corrigido nesta
onda; correção é onda seguinte ou escala (§8, §9).

Comandos executados (evidência = exit code):

| Verificação | Comando | Exit |
| --- | --- | --- |
| Sync do SSOT | `python3 scripts/sync_agent_registry.py --check` | 0 — `[OK] registry em sincronia com o disco` |
| Contratos de agente | `python3 scripts/validate_nexus_yaml.py` | 0 |
| Relatório da DAG | `python3 scripts/nexus_dispatcher.py --report` | 0 — 46 promulgados, `missing_from_dag: []` |
| Suíte baseline | `python3 -m pytest tests/agents -q` | 0 (coleta) — **4 failed / 149 passed / 1 skipped** |
| Replay self-delegação | `nexus_dispatcher.py --check` com TA-999 sender==target | **1** — `self-delegation proibida ... (Art. 4.5)` |
| Replay ação do ledger | `nexus_dispatcher.py --check` com `action: fix-table` | **1** — `action fora do vocabulário` |
| Replay entry TA-0028 | `nexus_dispatcher.py --check` (sender/target do ledger) | **1** — 3 errors (target fora da DAG, action, self-delegação) |
| Schema do ledger (Art. 4.10) | `mcp_nexus_ledger.validate_ledger(load_ledger())` | **ValueError: Missing required field: version** |
| Append-only do ledger | `git diff --numstat -- .ai/agents/ledger.yaml` | `41 1` (a única "remoção" é a linha idêntica regravada com newline de EOF) |
| LGPD no ledger | regex e-mail/CPF/telefone/nome-pessoa | 0 hits |

## 2. Mapa do circuito (AC2)

### 2.1 Camadas — `AGENT_TOPOLOGY` (scripts/validate_nexus_yaml.py:15-71)

| Camada | Qtd | Membros (resumo) |
| --- | --- | --- |
| L0 | 1 | agent-nexus-prime-ultimate (orchestrator, único dispatcher) |
| L1 | 8 | sdd-specialist, pm, po, architect, project-analyst, business-analysis, project-design, project-patterns-standards |
| L2 | 30 | specialists (api, backend, frontend, qa-sdet, docker, python, dba, devops, 5× sddai, agile, cobit, itil, six-sigma, iso-26514, …) |
| L3 | 4 | reviewer, gatekeeper, project-auditor, clean-code-evaluator (`role: gate`) |
| META | 1 | skill-master (forge) |
| FORGE-LEGACY | 1 | agent-factory-architect (legacy-forge) |
| **Total canônico** | **45** | `KNOWN_SLUGS` = union (validate_nexus_yaml.py:72) |

Registry declara **46** promulgados (44 `promulgado` + 2 `legacy-forge`) — saída do
dispatcher (`promulgados: 46`). A diferença é `agent-factory-architect-ultimate`, que está no
registry mas **fora** da topologia (ver F-06).

### 2.2 Regras de roteamento vigentes (`scripts/nexus_dispatcher.py`)

1. `task_id` no padrão `^[A-Z]{2}-\d{3,4}$` (nexus_dispatcher.py:41, validado em :90).
2. `target` deve pertencer a `KNOWN_SLUGS` (:92) **e** estar promulgado/legacy-forge no
   registry (:94-97).
3. `action` deve pertencer a `VALID_ACTIONS` — vocabulário **global** de 24 ações
   (:35-40, validado em :98). Não há mapa camada→ações.
4. `handoff` no padrão `HF-\d{3,4}` ou `\d{3,4}-…` (:100-102).
5. Anti self-delegação Art. 4.5: `sender == target` → erro (:104-108);
   constitution.md:122 (Art. 4.5: fluxo half-duplex, delegação circular proibida).
6. Contrato half-duplex: `reply_contract` fixo no envelope (:81); fail-closed — qualquer
   erro → `status: rejeitado` e exit 1 (:109-111, :152).
7. `--report`: agrupa promulgados por camada via `_layer_of()` (:63-67) e devolve
   `missing_from_dag = KNOWN_SLUGS - promulgados` (:132) — **apenas uma direção** (ver F-06).

### 2.3 Desvios doc↔código do dispatcher (achado)

- **D-01**: docstring declara "conjunto válido de ações **por camada**"
  (nexus_dispatcher.py:7), mas o código usa `VALID_ACTIONS` **global** (:35-40) — nenhum
  agrupamento por camada existe. Desvio doc↔código confirmado.
- **D-02**: defaults de `sender` divergentes: `"agent-orchestrator"` no envelope (:75, :79)
  vs `"agent-nexus-prime-ultimate"` na checagem de self-delegação (:105) — mesmo campo, dois
  valores-default; `agent-orchestrator` nem existe na DAG.
- **D-03**: `sender` **não** é validado contra `KNOWN_SLUGS` (só `target`, :92-93) — remetente
  livre é aceito (demonstrado no replay de TA-0027: único erro foi `action`).

## 3. Subutilização (AC3)

- **F-01 (3 gates L3 sem consumidor)**: `downstream: []` em
  `.ai/agents/registry.yaml:174` (clean-code-evaluator), `:336` (gatekeeper), `:614`
  (reviewer) — refletidos dos frontmatters `.opencode/agents/agent-clean-code-evaluator.md:8`,
  `agent-gatekeeper.md:8`, `agent-reviewer.md:8`. Evidência de falha:
  `tests/agents/test_onda7_agents.py:121` → `agentes sem consumidores:
  {'agent-reviewer', 'agent-gatekeeper', 'agent-clean-code-evaluator'}`.
  **Impacto**: cadeia de merge sem acionamento declarado — o wire do plano
  `qa → reviewer → gatekeeper → auditor` (`tests/agents/test_onda6_agents.py:92-96`) não é
  representável no registry: `gatekeeper` declara `reviewer` como upstream
  (`agent-gatekeeper.md:7`) mas `reviewer` não declara `gatekeeper` downstream, e `gatekeeper`
  não declara `auditor` downstream (`registry.yaml:336`).
- **F-02 (isenção assimétrica no teste anti-subutilização)**: o conjunto `terminal` do teste
  isenta auditor, skill-master, 2 legacy-forge, `sddai-trainer` e `sddai-cli`
  (`tests/agents/test_onda7_agents.py:113-115`) — os 3 gates L3 **não** são isentos e também
  têm `downstream: []`. Nota: `sddai-cli` (`registry.yaml:650`) e `sddai-trainer`
  (`registry.yaml:706`) têm `downstream: []` e passam apenas pela isenção.
- **F-03 (def morto no mesmo teste)**: `test_no_loose_ends_too_early` é definido **duas vezes**
  (`tests/agents/test_onda7_agents.py:103` e `:109`); a primeira é sombreada e nunca coletada
  (`pytest --collect-only -q` → 14 testes, apenas `…:121` coletado). A regra mais estrita da
  linha 103 está silenciosamente inoperante (P-06).
- **F-04 (WIP zero por camada)**: receivers do ledger = L1×4 (sdd-specialist ×3,
  project-analyst ×1), L3×2 (project-auditor), 1× slug sem prefixo (`nexus-prime-ultimate`) —
  **L2 (30 agentes) tem WIP zero no ledger** (ledger.yaml:1-56). Corpus `.ai/handoffs` (38
  arquivos) + ledger: **14/46 agentes nunca referenciados** por slug exato —
  agent-agile-specialist, agent-artifact-builder, agent-bash-specialist,
  agent-business-analysis-specialist, agent-compliance-governance, agent-frontend-dev,
  agent-github-specialist, agent-infrastructure-specialist, agent-itil-specialist, agent-pm,
  agent-po, agent-quality-architect-specialist, agent-skill-master, agent-ui-ux-advisor
  (método: busca literal do slug; `UNKNOWN - verify` se alguma menção existir sem prefixo
  completo).

## 4. Desvio de função (AC4)

- **F-05 docker-specialist (slug↔description)**: slug `agent-docker-specialist` e título
  `L2 · SPECIALIST · DOCUMENTATION` (`.opencode/agents/agent-docker-specialist.md:11`) com
  `description: "COGME documentation custody…"` (`:6`; `registry.yaml:277-279`). Confirma o
  sinal do handoff. **Já registrado como VIO-010** (`docs/auditorias/vio-register.md:33`,
  ABERTO-PENDÊNCIA AFA) — **não** emitir VIO duplicado; pendência de re-forja via AFA
  (Art. 4.1).
- **F-06 (assimetrias upstream/downstream)** — varredura completa do registry:
  - **108 pares** `A.downstream → B` sem `B.upstream → A` (ex.: `backend-dev → reviewer`
    com `reviewer.upstream = [nexus]` — `registry.yaml:125-128` vs `agent-reviewer.md:7`;
    `qa-sdet → gatekeeper` — `registry.yaml:583-585` vs `agent-gatekeeper.md:7`).
  - **49 pares** `A.upstream → B` sem `B.downstream → A` (ex.: `gatekeeper.upstream →
    reviewer` sem o arco reverso — `agent-gatekeeper.md:7` vs `agent-reviewer.md:8`;
    `python/backend/frontend → clean-code-evaluator` sem retorno —
    `agent-clean-code-evaluator.md:7`).
  - Assimetria estrutural crítica: `nexus.upstream = [agent-factory-architect-ultimate]`
    (`registry.yaml:410`) mas esse agente está **fora da DAG** e não declara downstream
    (F-08).
- **F-07 (ações do ledger fora do vocabulário)**: `fix-table` (`ledger.yaml:4`) e
  `review-plan-v2.1.0` (`ledger.yaml:12`) não pertencem a `VALID_ACTIONS`
  (`nexus_dispatcher.py:35-40`); replay rejeita com exit 1 (§1). Evidência adicional:
  apenas `spec`, `audit`, `analyze` do ledger são válidos.

## 5. Integridade do registry (AC4 do handoff / AC5 aqui)

- **OK**: `sync --check` exit 0; `validate_nexus_yaml.py` exit 0; header comments intactos
  (`registry.yaml:1-4`); `registry.version: '1.0'` (`registry.yaml:7`) — enum de versão não
  alterado (DON'T 12 respeitado); entradas legacy-forge com `version: null` e
  `description: null` (`registry.yaml:288-305`) coerentes com o código que as gera
  (`sync_agent_registry.py:38-45`).
- **F-08 (drift registry↔DAG, UNKNOWN)**: `agent-factory-architect-ultimate` é upstream do L0
  (`registry.yaml:410`) mas não consta em `AGENT_TOPOLOGY` — só `agent-factory-architect`
  está em `FORGE-LEGACY` (`validate_nexus_yaml.py:68-70`). Efeito: saída do `--report` o
  coloca em camada `UNKNOWN` (exit 0) enquanto `missing_from_dag: []`
  (`nexus_dispatcher.py:132` só verifica a direção KNOWN→registry). O comentário do script
  afirma que "FORGE-LEGACY e agent-factory-architect-ultimate são legacy-forge"
  (`validate_nexus_yaml.py:14`) — **contradiz o próprio código** (comentário↔código drift).
- **F-09 (status não derivado do frontmatter)**: `agent-clean-code-evaluator.md:12` declara
  `Status: DRAFT` no comentário de cabeçalho, mas `registry.yaml:168` grava
  `status: promulgado` porque o sync **fixa** `status: "promulgado"` para frontmatter válido
  (`sync_agent_registry.py:60`) e o frontmatter não tem chave `status`. `UNKNOWN - verify`
  se DRAFT é intenção do plano (ONDA 8 Lote 3) ou drift documental.

## 6. Auditoria do ledger (AC6)

| Item | Veredito | Evidência |
| --- | --- | --- |
| Schema por entry (8 campos) | **OK** — 7/7 entries completas | script `yaml.safe_load` → `['task_id','sender','receiver','action','status','exit_status','timestamp','notes']` ausentes = nenhum |
| Append-only | **OK nesta rodada** | `git diff --numstat` = `41 1`; a única linha "-" reaparece idêntica em "+" (diferença = newline de EOF, `git diff` `\ No newline at end of file`) — nenhum conteúdo de entry reescrito |
| Coerência de timestamps | **OK** — monotônicos | `ledger.yaml:7` 2026-10-31T14:30Z → `:15` 11-02T00:00Z → `:23` 18:15Z → `:31` 20:20Z → `:39` 20:55Z → `:47/:55` 21:10Z |
| PII / LGPD | **OK** — só task IDs | regex e-mail/CPF/telefone/nome = 0 hits (§1) |
| Auto-delegação Art. 4.5 | **VIOLAÇÃO** — F-10 | `ledger.yaml:10-11`: `sender: nexus-prime-ultimate` == `receiver: nexus-prime-ultimate` (TA-0028); replay do dispatcher rejeita com exit 1 (`self-delegation proibida … Art. 4.5`) |
| Escalonamento stale | **F-11** | `ledger.yaml:5-7`: TA-0027 `status: escalated` desde 2026-10-31T14:30Z com `exit_status: 0` — aberto ≥ 2 dias (hoje 2026-11-02); notes dizem "Formalized with CCB" (`ledger.yaml:8`) → encerramento é decisão Humano/CCB |
| Vocabulário/sender | **F-12** | ações fora de `VALID_ACTIONS` (F-07) + `sender: nexus-prime-ultimate` sem prefixo `agent-` (`ledger.yaml:2,10,18,26,34,42,50`) — fora de `KNOWN_SLUGS` (`validate_nexus_yaml.py:72`) |
| Schema constitucional Art. 4.10 | **VIOLAÇÃO** — F-13 | `constitution.md:132` exige SSOT com `current_session`, `audit_trail`, `blocked_tasks`; `mcp_nexus_ledger.py:14-17` exige `version, current_session, audit_trail, last_updated` → `ValueError: Missing required field: version` (o ledger é uma lista pura de tasks, `ledger.yaml:1-56`) |
| Risco de reescrita total | **F-14** | `mcp_nexus_ledger.py:9-11` usa `yaml.safe_dump` com `'w'` — reescreve o arquivo inteiro, sem garantia de append-only (Art. 4.10 exige script/MCP validado) |

## 7. Root-cause dos 4 testes vermelhos + classificação de custódia (AC7)

| # | Teste / evidência | Root-cause | Custódia |
| --- | --- | --- | --- |
| 1 | `tests/agents/test_dispatcher_and_sync.py:120` — `assert 30 == 29` | Constante de baseline desatualizada: `AGENT_TOPOLOGY` e registry têm **L2 = 30** (contagem própria = 30; `registry` Counter L2 = 30), enquanto o teste espera 29; o próprio comentário da linha fecha a aritmética `24 + agent-agile-specialist + 5 SDDAI = 30` e contradiz o `assert`. Integração do `agent-agile-specialist` em L2 ocorreu no commit `db47610` (2026-10-30). SSOT e sync estão corretos (exit 0); o teste é que está stale. | **(a) nexus/orquestrador-direto** (edição de constante de teste; `tests/` não está na lista de imutáveis) — `UNKNOWN - verify` se a CCB exige aprovação para baseline de teste |
| 2 | `tests/agents/test_onda1_agents.py:31` — `assert 4109 <= 4000` | Prompt do L0 excede o orçamento autodeclarado `< 4000 tokens` (`.opencode/agents/agent-nexus-prime-ultimate.md:68`); `validate_afa_output.py` devolve `ok: True, score: 100, est_tokens: 4109`. **Atenção**: `constitution.md:126` (Art. 4.7) define score ≥ 85 e mínimos de seção, **não** contém limite de tokens (grep `token` em constitution.md = 0 hits) — a mensagem do teste cita Art. 4.7 sem lastro textual no artigo. | **(c) forja → AFA-ULTIMATE** (re-forjar/prompt slim, Art. 4.1) **ou (d) decisão Humana/CCB** se a decisão for codificar o limite de 4000 na constituição |
| 3 | `tests/agents/test_onda6_agents.py:94` — `assert 'agent-gatekeeper' in []` | Wiring L3 incompleto nos frontmatters forjados: `agent-reviewer.md:8 downstream: []` (esperado `[agent-gatekeeper]`) e `agent-gatekeeper.md:8 downstream: []` (linha 96 exigiria `agent-project-auditor`), embora `agent-gatekeeper.md:7` já declare `agent-reviewer` upstream → assimetria F-06; o registry só replica (`registry.yaml:336,614`). | **(c) AFA-ULTIMATE** (Art. 4.1 — arquivo de agente é da forja) + **(b) script** (`sync_agent_registry.py` para regenerar o registry); **(d)** se a CCB decidir que gatekeeper não aponta auditor (mudança de regra, não de dado) |
| 4 | `tests/agents/test_onda7_agents.py:121` — `orphans = {reviewer, gatekeeper, clean-code-evaluator}` | Mesma root-cause do #3 (3 gates com `downstream: []`, F-01) somada ao conjunto de isenções que não cobre gates L3 (`test_onda7_agents.py:113-115`) e ao def duplicado/morto (`:103` vs `:109`, F-03). | **(c) AFA-ULTIMATE** para o wiring; **(a) nexus** para atualizar isenções/def morto do teste; **(d) Humano/CCB** para decidir se gates L3 são terminais legítimos (isento da anti-subutilização) ou devem encadear ao auditor |

## 8. Propostas de normatização — NÃO EXECUTADAS (AC8)

Nada abaixo foi aplicado; cada item traz a custódia necessária.

| ID | Proposta | Custódia |
| --- | --- | --- |
| N-01 | Re-forjar os 3 gates L3 com `downstream` coerente (reviewer→gatekeeper, gatekeeper→auditor, clean-code→reviewer) e regenerar o registry | (c) AFA-ULTIMATE (Art. 4.1) → (b) sync |
| N-02 | Atualizar `dag_totals["L2"] = 30` em `test_dispatcher_and_sync.py:120` e corrigir o comentário interno | (a) nexus — `UNKNOWN - verify` sobre alçada CCB |
| N-03 | Slim do prompt do L0 para < 4000 tokens **ou** codificar o limite no Art. 4.7 por emenda | (c) AFA / (d) Humano-CCB |
| N-04 | Alinhar docstring do dispatcher com o código: declarar `VALID_ACTIONS` global **ou** implementar mapa ação↔camada (resolve D-01) | (b) script |
| N-05 | Validar `sender` contra `KNOWN_SLUGS` e unificar o default de `sender` (D-02, D-03) | (b) script |
| N-06 | `--report` bidirecional (registry→DAG também) e resolver o status de `agent-factory-architect-ultimate` (em `FORGE-LEGACY` no `AGENT_TOPOLOGY` **ou** removê-lo do upstream do L0) + corrigir o comentário `validate_nexus_yaml.py:14` | (b) script + (c) AFA para o frontmatter do L0 |
| N-07 | Normalizar o ledger: `sender` com prefixo `agent-`, ações do vocabulário do dispatcher, schema Art. 4.10 (`version/current_session/audit_trail/last_updated`), gravação estritamente append-only (hoje `safe_dump` reescreve tudo) | (a) nexus/orquestrador via script ou MCP validado (Art. 4.10) |
| N-08 | Decidir o destino de TA-0027 (stale escalated) e ratificar/retificar TA-0028 (auto-delegação) | (d) Humano/CCB — Art. 5.1 |
| N-09 | Definir norma para gates L3: isenção explícita da anti-subutilização **ou** encadeamento obrigatório ao auditor (fecha #3 e #4) | (d) Humano/CCB → (a)/(c) na execução |
| N-10 | Derivar `status` do frontmatter no sync (hoje fixo em `promulgado`, `sync_agent_registry.py:60`) para eliminar o drift DRAFT↔promulgado (F-09) | (b) script + (c) AFA |
| N-11 | Remover o def duplicado/morto `test_onda7_agents.py:103` (F-03) | (a) nexus |

## 9. VIO emitidos — somente violações confirmadas (AC9)

Emitidos em `docs/auditorias/vio-register.md` (append-only, próximo número sequencial):

| VIO | Violação confirmada | Evidência |
| --- | --- | --- |
| **VIO-026** | Auto-delegação registrada no ledger (TA-0028: `sender == receiver`) — Art. 4.5 | `ledger.yaml:10-11`; replay `nexus_dispatcher.py --check` = exit 1, `self-delegation proibida … (Art. 4.5)` |
| **VIO-027** | Ledger fora do contrato do dispatcher e do Art. 4.10 (ações `fix-table`/`review-plan-v2.1.0` fora de `VALID_ACTIONS`; `sender` sem prefixo `agent-`; schema sem `version/current_session/audit_trail/last_updated`) | `ledger.yaml:4,12,2`; `nexus_dispatcher.py:35-40`; replay exit 1; `validate_ledger` = `ValueError: Missing required field: version`; `constitution.md:132` |
| **VIO-028** | Drift registry↔DAG: `agent-factory-architect-ultimate` upstream do L0 mas fora de `AGENT_TOPOLOGY` → camada `UNKNOWN` silenciosa, `missing_from_dag: []` e comentário `validate_nexus_yaml.py:14` contradiz o código | `registry.yaml:410`; `validate_nexus_yaml.py:14,68-70`; `nexus_dispatcher.py:132`; saída `--report` (`UNKNOWN: [agent-factory-architect-ultimate]`, exit 0) |
| **VIO-029** | Anti-subutilização violada: 3 gates L3 promulgados com `downstream: []` (cadeia de merge sem acionamento declarado) | `registry.yaml:174,336,614`; `agent-{reviewer,gatekeeper,clean-code-evaluator}.md:8`; `tests/agents/test_onda7_agents.py:121` |

**Não emitidos (justificativa)**: docker-specialist = já VIO-010 (pendência AFA, não duplicar);
4 testes vermelhos #1/#2 = defect de baseline/orçamento com custódia (a)/(c)/(d) e lastro
constitucional incerto (`UNKNOWN - verify`) — sem violação de regra confirmada; D-01..D-03 =
desvios doc↔código normatizáveis pela N-04/N-05; TA-0027 stale = F-11, pendência de decisão
CCB (N-08), não violação autônoma.

## 10. Verificação dos critérios de aceite (AC1–AC9)

- [x] AC1 Relatório em `docs/auditorias/` no padrão `AUD-YYMMDD-NN` (próximo livre:
  `AUD-2611-01` — não havia emissões em 2611) com frontmatter e evidência por achado
- [x] AC2 Mapa do circuito completo (camadas §2.1 + regras do dispatcher §2.2 + desvios §2.3)
- [x] AC3 Subutilização mapeada com evidência (F-01..F-04, inclui os 3 gates do onda7)
- [x] AC4 Desvio de função mapeado (F-05 docker-specialist, F-06 assimetrias, F-07 ações)
- [x] AC5 Integridade do registry verificada (sync/header/version-enum/legacy/UNKNOWN — §5)
- [x] AC6 Ledger auditado (schema, append-only, auto-delegação TA-0028, stale TA-0027, LGPD — §6)
- [x] AC7 Root-cause dos 4 testes vermelhos com custódia a–d (§7)
- [x] AC8 Propostas de normatização NÃO executadas, itens AFA/CCB sinalizados (§8)
- [x] AC9 VIO-NNN apenas para violações confirmadas (§9 — 4 emitidos + justificativa de ausência)

## 11. Escalonamento (decisão Humano/CCB — Art. 5.1)

A auditoria está completa (9 AC), mas 3 achados exigem decisão Humana antes de qualquer
remediação: (i) destino de TA-0028 (auto-delegação já registrada em VIO-026) e de TA-0027
(stale escalated); (ii) orçamento de 4000 tokens do L0 — limite ausente do texto do Art. 4.7;
(iii) norma para gates L3 (encadeamento vs isenção da anti-subutilização), que destrava os
testes #3 e #4. Kill switch: inherited.
