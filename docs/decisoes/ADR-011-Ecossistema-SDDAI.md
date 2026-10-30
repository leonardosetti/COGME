# ADR-011 — Ecossistema de Inteligência SDD: MCPs, Memória Persistente e Separação Ortogonal L1/L2/L3

| Campo | Valor |
|---|---|
| **Versão** | 1.0.0 |
| **Status** | Aprovado (ratificado pelo CCB-001 em 29/10/2026) |
| **Data da decisão** | 29/10/2026 |
| **Data de formalização do documento** | 29/10/2026 |
| **Decisor** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| **Gatilhos G1–G4** | G1 (impacto transversal — todos os agentes SDD, workflow de handoffs, specs, personas e roteamento), G2 (irreversibilidade prática — implementação de MCPs e ledger redefine arquitetura de memória do circuito), G3 (questionabilidade acadêmica — "por que não usar LangChain/AutoGen?"), G4 (trade-off não óbvio — determinismo e auditabilidade × velocidade de prototipagem com frameworks prontos) |
| **Rastreabilidade** | TAP §3 (Inovação) + §9 (Premissa P3 — stack local auditável); EAP N1.4, N4.4, N9.1; REQ-13 (prompts catalogados); ADRs correlatas: ADR-001 (stack FOSS), ADR-006 (modelo primário/fallback, sobreposta parcialmente), ADR-010 (infraestrutura, complementar); archtecture_report_Local_SDDAI.md; constitution.md v1.2.0 Art. 4.9, 4.10, 6.5, 6.6, 6.7 |
| **Domínio PMBOK 7ª** | Trabalho do Projeto + Abordagem de Desenvolvimento + Incerteza |
| **Processo PMBOK 6ª (dicionário)** | 4.3 Orientar e Gerenciar o Trabalho do Projeto; 4.6 Integrar Mudanças |

## Contexto

O ecossistema SDD do COGME utiliza Qwen3-30B-A3B MoE via llama.cpp e OpenCode como interface. Na configuração inicial, o circuito operava de forma stateless: cada interação começava do zero, sem memória persistente entre sessões, sem protocolo formal de handoffs estruturados além de arquivos JSON soltos, e sem separação clara entre camadas de responsabilidade.

Isso gerou problemas concretos:

1. **Perda de contexto:** informações cruciais (decisões anteriores, blockers, lições aprendidas) eram perdidas entre sessões, forçando reprocessamento redundante.
2. **Falta de auditabilidade:** não havia registro sistemático de quem fez o quê, quando e por quê, dificultando rastreamento de defeitos até prompts específicos.
3. **Acoplamento indevido:** modificações em infraestrutura (troca de modelo) impactavam diretamente metodologia (specs, handoffs), violando princípio de separação de responsabilidades.
4. **Ausência de guardrails:** sem validação automática de schemas e estados, erros humanos ou alucinações do modelo passavam despercebidos até fases tardias.

Frameworks existentes (LangChain, AutoGen, CrewAI) ofereceriam soluções rápidas, mas introduziriam dependências pesadas, black boxes opacas e potencial violação de soberania de dados (telemetria embutida, calls para serviços externos não autorizados).

## Opções Consideradas

| # | Opção | Prós | Contras |
|---|---|---|---|
| O1 | Manter estadoless puro | Simplicidade máxima; zero overhead | Perda constante de contexto; baixa auditabilidade; retrabalho elevado |
| O2 | Adotar framework externo (LangChain/AutoGen) | Rapidez de implementação; comunidade ativa | Dependências pesadas; opacidade; risco de telemetria/lock-in; viola P-02/P-03 absolutistas |
| O3 | Construir camada própria de memória persistente + MCPs customizados + separação L1/L2/L3 | Determinismo total; auditabilidade completa; soberania preservada; leveza (Python stdlib + PyYAML) | Esforço inicial de implementação; necessidade de disciplina de manutenção |

## Decisão

**Aprovar a opção O3.**

### 3.1. Separação Ortogonal de Camadas (L1 / L2 / L3)

| Camada | Responsabilidade | Artefatos | Frequência de Mudança | Autoridade do Agente |
|---|---|---|---|---|
| **L1 — Infraestrutura** | Motor de inferência e hardware | `llama.cpp`, Vulkan/radv, systemd service, modelos GGUF, `opencode.json`, imagens Docker base | Raramente (semestral/anual) | ❌ Não modifica. Reporta blocker. |
| **L2 — Personas** | Comportamento do modelo via contexto | `.ai/personas/*.md` (`_base.md`, `pm.md`, `coder.md`, `reviewer.md`, `tester.md`, `all.md`), symlink `active.md` | Por agente ou papel | ✅ Lê e segue a persona ativa. Pode propor updates via PR. |
| **L3 — Metodologia** | Organização do trabalho e validação | `.ai/specs/*`, `.ai/handoffs/task-ta-*.json`, `.ai/agents/ledger.yaml`, ADRs, planos, lições aprendidas | Por tarefa/ciclo | ✅ Interage, lê e atualiza. Única camada mutável diariamente. |

**Regra de ouro:** mudanças em uma camada **NÃO** exigem mudanças em outras. Violação desta regra aciona kill switch operacional.

### 3.2. Protocolo de Memória Persistente

O estado do sistema é gerido exclusivamente via:

- **`ledger.yaml`** (`.ai/agents/ledger.yaml`): SSOT para `current_session`, `audit_trail`, `blocked_tasks`, `last_updated`, `context_budget_tokens` (24.000), `context_used_tokens`. Schema v2.0 obrigatório. Modificação somente por script ou MCP validado.
- **Handoffs estruturados** (`.ai/handoffs/task-ta-*.json`): envelope JSON contendo `task_id`, `from_agent`, `to_agent`, `payload`, `timestamp`, `parent_task_id`. Parseados por `handoff_parser.py` ou MCP equivalente.
- **Specs imutáveis** (`.ai/specs/*.md`): `tap.md`, `eap.md`, `requisitos.md`, `input-canonico-v4.1.1.md`. Once written, never modified without new version file.
- **Lições aprendidas acumulativas**: `MF1-licoes.md`, `MF2-licoes.md`, `MF3-licoes.md`, `transversais.md`. Formato markdown padronizado.

### 3.3. MCPs Customizados (Model Context Protocol)

Quatro servidores MCP implementados em Python puro (stdlib + PyYAML como única dependência externa permitida):

| MCP | Script | Função |
|---|---|---|
| `nexus-ledger` | `scripts/mcp_nexus_ledger.py` | Leitura/escrita estruturada do `ledger.yaml` com validação de schema e operações idempotentes |
| `nexus-dispatch` | `scripts/mcp_nexus_dispatch.py` | Despacho de envelopes de tarefa entre personas, respeitando topologia AGENT_TOPOLOGY e proibindo auto-delegação |
| `nexus-validate` | `scripts/mcp_nexus_validate.py` | Validação de schemas (frontmatter YAML de agentes, handoffs JSON, specs markdown) e registros de conformidade |
| `nexus-kb` | `scripts/mcp_nexus_kb.py` | Consulta indexada à OKB, Glossário e lições aprendidas via grep estruturado ou índice invertido leve |

**Requisitos técnicos dos MCPs:**
- Python preferencialmente com biblioteca padrão;
- Se usar YAML, empregar PyYAML (MIT) registrado em `requirements.txt` como dependência de desenvolvimento;
- Sem framework de orquestração externa obrigatório;
- Parsing determinístico;
- Operações idempotentes;
- Registro de auditoria em `audit_trail` do ledger;
- Bloqueio fail-closed em estado inconsistente.

### 3.4. Regras Operacionais da Camada `.ai/`

- **Regra de Ouro:** "Se não é lido pelo OpenCode, por MCP ou por script canônico, não pertence ao diretório `.ai/`."
- **Limite máximo:** 10 arquivos por diretório em `.ai/` (exceto `.ai/handoffs/`, que é append-only e deve ter índice `INDEX.md` e arquivamento trimestral de handoffs > 90 dias).
- **Revisão trimestral:** deletar ou arquivar arquivos não usados há > 90 dias.
- **Nenhum framework externo pesado:** apenas Markdown puro + scripts Shell/Python leves.
- **SSOT absoluto:** um fato = um local, nunca duplicar.

### 3.5. Integração com OpenCode

Atualizar `.opencode/opencode.json` para registrar `mcpServers`, apontando para os quatro scripts acima. Não alterar modelo, contexto ou permissões além do necessário.

## Consequências

- Positivas: determinismo total; auditabilidade ponta a ponta (cada ação registrada no ledger); soberania preservada (zero telemetria externa); leveza (sem frameworks pesados); separação clara de responsabilidades facilitando manutenção e sucessão.
- Negativas: esforço inicial de implementação (~8–12h estimadas para MCPs básicos + ledger + specs); necessidade de disciplina rígida de manutenção (revisão trimestral, limite de arquivos); curva de aprendizado para novos membros da equipe entenderem o protocolo.
- Neutras: compatibilidade retroativa limitada — handoffs antigos (22 arquivos JSON já existentes) precisam ser migrados para o novo schema ou arquivados como legado.

## Trade-offs Declarados

| Aspecto | Ganho | Perda/Risco | Mitigação |
|---|---|---|---|
| MCPs próprios vs. frameworks | Controle total; soberania; leveza | Velocidade de entrega inicial menor | Foco em MVP funcional dos 4 MCPs essenciais; expandir gradualmente |
| Ledger como SSOT de estado | Auditabilidade perfeita | Ponto único de falha se corrompido | Backups periódicos do ledger; validação schema em cada escrita; fail-closed |
| Limite de 10 arquivos/diretório | Força consolidação; evita dispersão | Pode exigir arquivamento frequente em `.ai/handoffs/` | Índices automáticos (`INDEX.md`); política de rolagem trimestral clara |
| Separação L1/L2/L3 | Modularidade; independência de evolução | Rigidez percebida inicialmente | Documentação clara; exemplos práticos de como cada camada evolui isoladamente |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo | Domínio PMBOK 7ª | Data |
|---|---|---|---|---|
| ADR-006 | Parcial | Adição de MCPs, memória persistente, separação L1/L2/L3 e refinamento do roteamento de agentes | Trabalho do Projeto | 29/10/2026 |
| ADR-001 | Parcial | Especificação de contexto (32k configurado, 24k efetivo), reconciliação de scripts, perfis de hardware/modelo via YAML | Abordagem de Desenvolvimento | 29/10/2026 |

## kill_switch

Abortar imediatamente e retornar Parcel com `kill_switch_invoked: true` se:
1. Detecção de corrupção ou inconsistência do `ledger.yaml` (schema inválido, campos obrigatórios faltantes, conflito com handoffs processados);
2. Tentativa de um agente da camada L3 modificar arquivos da camada L1 sem passar pelo protocolo MCP adequado;
3. Tentativa de auto-delegação (agente despachando tarefa para si mesmo, violando princípio half-duplex);
4. Criação de arquivo órfão em `.ai/` que não seja lido por OpenCode, MCP ou script canônico;
5. Exceder limite de 10 arquivos por diretório em `.ai/` sem índice ou arquivamento canônico;
6. Envio de dados sensíveis para cloud não autorizada durante operação de MCP.

Ao abortar: registrar em `audit_trail` do ledger e marcar `ccb_action_required: true`.

## Governança

- **Custódia:** `agent-nexus-prime-ultimate` (L0 orquestrador) + `agent-architect` (guardião da separação L1/L2/L3).
- **Emenda:** mudança na arquitetura de memória ou adicion/remoção de MCP exige ADR específica + CCB humano.
- **Auditoria:** `project-auditor` verifica integridade do ledger, conformidade dos handoffs e ausência de arquivos órfãos em `.ai/` a cada semana.
- **Sucessão:** `.ai/agents/registry.yaml` + `constitution.md` + ADRs bastam para reconstruir contexto completo do circuito SDD.