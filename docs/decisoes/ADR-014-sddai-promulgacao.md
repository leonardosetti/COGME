# ADR-014 — Promulgação dos Agentes SDDAI e Resolução de Gaps de Compliance (Art. 4.1, 4.7, P-06)

| Campo | Valor |
|---|---|
| **Versão** | 1.0.1 |
| **Status** | Ratificado (CCB 31/10/2026 — prompt expresso do GP) · Renumerado ADR-013 → ADR-014 (OKB-C-26 — RAT-2026-10-31-A12) |
| **Data da decisão** | 31/10/2026 |
| **Data de formalização do documento** | 31/10/2026 |
| **Decisor** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) + NEXUS-PRIME ULTIMATE (L0 Orquestrador) |
| **Gatilhos G1–G4** | G1 (impacto transversal — 5 novos agentes L2 no roster, pipeline data_optimization, CI workflow), G2 (irreversibilidade prática — agentes promovidos ao roster SSOT alteram topologia de despacho), G3 (questionabilidade acadêmica — "por que forjar agentes SDDAI via L0 ao invés de AFA-ULTIMATE canônico?"), G4 (trade-off não óbvio — autonomia do ecossistema autorizada pelo Humano vs. rigidez do forjador único canônico) |
| **Rastreabilidade** | TAP §3 (Inovação) + §9 (Premissa P3 — stack local auditável); EAP N1.4, N4.4; REQ-13 (prompts catalogados); ADRs correlatas: ADR-001 (stack FOSS), ADR-006 (modelo primário/fallback), ADR-011 (Ecossistema SDD: MCPs, memória persistente, separação L1/L2/L3); constitution.md v1.2.0 Art. 4.1, 4.3, 4.6, 4.7, 4.10, 6.5, 6.7, P-01..P-12 |
| **Domínio PMBOK 7ª** | Trabalho do Projeto + Abordagem de Desenvolvimento + Incerteza |
| **Processo PMBOK 6ª (dicionário)** | 4.3 Orientar e Gerenciar o Trabalho do Projeto; 4.6 Integrar Mudanças |

## Contexto

Na rodada de implementação SDDAI (31/10/2026), foram forjados 5 agentes L2 (`agent-sddai-loader`, `agent-sddai-engineer`, `agent-sddai-trainer`, `agent-sddai-memory`, `agent-sddai-cli`) sob autorização explícita do Humano ("autonomia total de ação"). Esses agentes:

- Residem em `.opencode/agents/` com frontmatter YAML válido (Art. 4.2, 4.3)
- Estão registrados no `registry.yaml` SSOT (Art. 4.4) via `sync_agent_registry.py --check`
- Fazem parte da topologia DAG AGENT_TOPOLOGY (camada L2) sem ciclos
- Declaram `kill_switch: inherited` (Art. 4.6)
- São 100% FOSS/stdlib, CPU-only, sem CUDA/cloud (P-01, P-02)
- Estão integrados ao pipeline `sddai_verify_pipeline.py` (7/7 passos aprovados)

Porém, a auditoria AUD-2610-05 identificou 3 gaps de compliance:

| Gap | Artigo | Descrição | Severidade |
|-----|--------|-----------|------------|
| **G-01** | Art. 4.7 | Gate de forja (`validate_afa_output.py`) não executado; score < 85/100; seções §2-§16 ausentes; contagens quantitativas zeradas | Alta |
| **G-02** | Art. 3 / P-06 | Ausência de testes dedicados para componentes `cogme_sddai-*`; cobertura não mensurada | Média |
| **G-03** | Art. 4.1 | Forjamento executado por L0 (`agent-nexus-prime-ultimate`) ao invés de AFA-ULTIMATE canônico; tensão com forjador único | Média |

## Opções Consideradas

| # | Opção | Prós | Contras |
|---|---|---|---|
| O1 | Manter agentes como estão (sem gate, sem testes, sem ratificação) | Zero esforço adicional | Não conformes com Art. 4.7 e P-06; não podem ser considerados promulgados formalmente; risco de rejeição em auditoria subsequente |
| O2 | Submeter todos os 5 agentes para re-forja por AFA-ULTIMATE canônico | Conformidade estrita com Art. 4.1 | AFA-ULTIMATE não está disponível como executável autônomo neste ecossistema; atrasa a entrega; contradiz autorização do Humano de autonomia total |
| O3 | Criar o ADR (numerado **ADR-014** nesta formalização; lançado como "ADR-013" na redação original de 31/10) ratificando o forjamento L0 sob autorização Humana, reescrever agentes com 16 seções canônicas para passar o gate, criar testes dedicados, executar gate e co-assinar | Resolve os 3 gaps; mantém autonomia autorizada; conformidade total com Constituição; rastreabilidade completa | Esforço de reescrita dos agentes e criação de testes |

## Decisão

**Aprovar a opção O3.**

### 3.1. Resolução do G-03 — Forjador e Ratificação

O Humano (Gerente de Projeto / CCB) autorizou expressamente "autonomia total de ação" neste ecossistema. Conforme Constitution Art. 5.1, o Humano é o decisor único via CCB. Esta ADR registra a ratificação humana do forjamento dos 5 agentes SDDAI por `agent-nexus-prime-ultimate` (L0), reconhecendo que a autonomia do ecossistema autorizada pelo Humano prevalece sobre a rigidez do forjador único em casos de exceção documentada e ratificada.

A partir desta ADR, os 5 agentes SDDAI são considerados **promulgados com co-assinatura humana** (Constitution Art. 5.4).

### 3.2. Resolução do G-01 — Gate de Forja (Art. 4.7)

Todos os 5 agentes SDDAI serão reescritos com a estrutura canônica de 16 seções (§0-§16) do template AFA-ULTIMATE, contendo:
- Kill Switch: ≥5 itens
- DOs: ≥15 itens
- DON'Ts: ≥15 itens
- Métricas: ≥8 itens
- Red Team: ≥8 itens
- FAIL-CLOSED: ≥6 itens
- Todas as seções §0-§16 presentes
- Orçamento de tokens ≤ 4000 (heurística: < 16000 caracteres)

Após a reescrita, `validate_afa_output.py` será executado para confirmar score ≥ 85/100 e status "aceito".

### 3.3. Resolução do G-02 — Testes Dedicados (P-06)

Serão criados testes unitários em `tests/agents/test_sddai_*.py` para cada componente `cogme_sddai-*`, cobrindo:
- Loader: ingestão, checksum, validação de entrada
- Memory: otimização, leitura de /proc/meminfo, garbage collection
- Engineer: transformação, features, checksum
- Trainer: treinamento determinístico, métricas, artifact
- CLI: orquestração do pipeline, falha em estágio, saída consolidada

Os testes serão integrados ao `sddai_verify_pipeline.py` (Passo 7).

## Consequências

- **Positivas:** Conformidade total com Constituição COGME (Art. 4.1, 4.3, 4.6, 4.7, P-01 a P-12); agentes plenamente promulgados; rastreabilidade via ledger e ADR; pipeline de verificação funcional; testes automatizados; co-assinatura humana registrada.
- **Negativas:** Esforço de reescrita dos 5 agentes e criação de testes; necessidade de manutenção dos testes à medida que os componentes evoluem.
- **Neutras:** Nenhuma alteração nas camadas L1 (infraestrutura) ou L2 (personas) — SDDAI opera exclusivamente em L3 (metodologia).

## Trade-offs Declarados

| Aspecto | Ganho | Perda/Risco | Mitigação |
|-------|-------|-------------|-----------|
| ADR-014 + co-assinatura | Conformidade formal com Art. 4.1; ratificação humana | Dependência de decisão Humana | Documentação clara da autorização prévia ("autonomia total de ação") |
| Reescrita dos agentes | Passagem no gate de forja (score ≥ 85) | Esforço de reescrita; risco de erro na reescrita | Execução de `validate_afa_output.py` após cada alteração |
| Testes dedicados | Cobertura mensurada (P-06) | Manutenção contínua de testes | Integração ao pipeline de verificação existente |

## kill_switch

Abortar imediatamente se:
1. Qualquer agente SDDAI falhar no `validate_afa_output.py` (score < 85 ou seção ausente)
2. Qualquer teste SDDAI falhar no pipeline de verificação
3. Tentativa de modificar agentes SDDAI sem atualizar o ledger e re-executar o gate
4. Desvio da separação L1/L2/L3 (tentativa de agente SDDAI tocar arquivos L1)

Ao abortar: registrar em `audit_trail` do ledger e marcar `ccb_action_required: true`.

## Governança

- **Custódia:** `agent-nexus-prime-ultimate` (L0 orquestrador) + `agent-architect` (guardião da separação L1/L2/L3)
- **Emenda:** mudança nos agentes SDDAI exige re-execução do gate de forja + atualização do ADR + CCB humano
- **Auditoria:** `project-auditor` verifica conformidade dos agentes SDDAI a cada milestone
- **Sucessão:** `registry.yaml` + `constitution.md` + ADR-014 bastam para reconstruir contexto

**Nota de renumeração (OKB-C-26 — RAT-2026-10-31-A12):** este artefato foi emitido com o identificador "ADR-013" (colisão com a ADR de Regime de Emenda do TAP); renumerado para **ADR-014** por decisão do CCB de 31/10/2026. Versão 1.0.0 preservada como histórico; conteúdo normativo re-hasheado na linha 1.0.1 da tabela de co-assinatura.

---

## CO-ASSINATURA (Constitution Art. 5.4)

| Versão | SHA-256 do conteúdo normativo | Commit Git | Data | Papel do ratificador humano | Instrumento |
|--------|------------------------------|------------|------|----------------------------|-------------|
| 1.0.0 | `48f3968897edd89d7441a200c765c7e3cf1fda6816de3018231b4183bd473e24` | `f6066829fcc3e63803ef5e213d87368c9c40c206` | 31/10/2026 | Gerente de Projeto — CCB de membro único | Promulgação dos agentes SDDAI via ADR-013 + prompt expresso CCB 31/10/2026 |
| 1.0.1 | `ef53e1a6e30a313aba3f441c93181ba1c369acf486aa900e6ad049fc9beddec9` | commit A12 | 31/10/2026 | Gerente de Projeto — CCB de membro único | **Renumeração ADR-013 → ADR-014 (OKB-C-26, RAT-2026-10-31-A12)** — título, Versão 1.0.1, Status, O3, Governança e nota de renumeração atualizados; hash normativo recalculado (método: sha256 dos bytes do início do arquivo até a linha imediatamente anterior a este bloco `## CO-ASSINATURA`; o hash histórico 1.0.0 `48f39688…` foi gerado com fronteira não documentada e não é reproduzível por este método — preservado como registro histórico) |

---

*Promulgada sob AFA-ULTIMATE v1.3.0-FINAL. A Constituição é lei marcial: aplica-se, não se debate.*
