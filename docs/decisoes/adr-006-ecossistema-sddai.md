---
id: decisoes-adr-006-ecossistema-sddai
title: 'ADR-006 — Ecossistema SDDAI: Modelo, Agentes, MCPs e Separação L1/L2/L3'
version: 1.2.0
class: decisao-adr
status: obsoleto
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-006-ecossistema-sddai.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- normalizado
---
# ADR-006 — Ecossistema SDDAI: Modelo, Agentes, MCPs e Separação L1/L2/L3

| Campo | Valor |
|---|---|
| **Versão** | 2.1.0 |
| **Status** | Ratificado |
| **Data da decisão** | 26/10/2026 (modelo) / 31/10/2026 (promulgação agentes) |
| **Data de formalização do documento** | 31/10/2026 |
| **Decisor** | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| **Gatilhos G1–G4** | G1 (impacto transversal — todas as fases de execução SDD), G2 (irreversibilidade prática — troca de modelo GGUF implica recompilação e revalidação de throughput), G3 (questionabilidade acadêmica — "por que MoE e não denso?"), G4 (trade-off não óbvio — eficiência computacional × complexidade operacional de dois modos de execução) |
| **Rastreabilidade** | TAP §3 (Inovação) + §8 (Restrições FOSS/orçamento zero) + §9 (Premissa P3 — stack local auditável); EAP N1.4, N4.4; REQ-12 (ADRs), REQ-13 (prompts catalogados); ADRs correlatas: ADR-001 (stack FOSS, sobreposta parcialmente), ADR-005 (freeze), ADR-011 (MCPs e memória persistente, sobreposta parcialmente por esta em relação ao roteamento); constitution.md v1.2.0 Art. 4.1, 4.3, 4.6, 4.7, 4.10, 6.5, 6.7, P-01..P-12 |
| **Domínio PMBOK 7ª** | Trabalho do Projeto + Abordagem de Desenvolvimento + Incerteza |
| **Processo PMBOK 6ª (dicionário)** | 4.3 Orientar e Gerenciar o Trabalho do Projeto; 8.2 Realizar Garantia da Qualidade |

## Contexto

O ecossistema SDD do COGME opera exclusivamente em hardware local (AMD Ryzen 7 8700G, Radeon 780M, 58GB RAM reais, Arch Linux). O motor de inferência é o `llama.cpp` compilado com Vulkan, LTO e AVX-512. A interface é o OpenCode.

Na versão 1.0 desta ADR, o modelo primário era Qwen 32B Instruct (denso, ~20GB RAM ativa). Após materialização do risco RE-08 (*overengineering* de governança consumindo capacidade de desenvolvimento), constatou-se que o modelo denso limitava fluxos paralelos de agentes, degradando throughput abaixo de 6 t/s em cenários de múltiplas personas ativas simultaneamente.

Adicionalmente, a Constituição v1.1.0 proibia qualquer tráfego de dados do projeto para nuvem (P-02 absolutista). Essa restrição, embora defensável academicamente, impedia resiliência operacional em picos de carga sem comprometer orçamento zero.

## Opções Consideradas

| #  | Opção                                       | Prós                                                                                     | Contras                                                                                                       |
| -- | --------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| O1 | Manter Qwen 32B Instruct denso               | Simplicidade; um único modo de execução                                                | Throughput insuficiente para fluxos paralelos; RAM pico elevado; sem resiliência                             |
| O2 | Migrar para Qwen3-30B-A3B MoE (Q4_K_M)        | ~3B parâmetros ativos por token vs. 30B; ~4GB RAM ativa; ≥ 12 t/s esperados; Apache-2.0 | Complexidade adicional (dois modos: local + cloud fallback); necessidade de reconciliar `download_model.sh` |
| O3 | Adicionar modelos cloud free tier (whitelist) | Resiliência em sobrecarga local; custo zero; Hugging Face/OpenRouter/Groq/GitHub Models  | Risco de soberania de dados; violação potencial da Constituição v1.1.0 se não emendada                   |
| O4 | Combinar O2 + O3 com restrições             | Melhor equilíbrio entre eficiência, resiliência e soberania                            | Maior superfície de configuração; exige kill switch claro                                                  |

## Decisão

**Aprovar a opção O4.**

### 1. Modelo primário

Substituir Qwen 32B Instruct por **Qwen3-30B-A3B Q4_K_M** (MoE: 30B totais, ~3B ativos por token, ~18 GB em disco, ~4 GB RAM ativa). Licença: Apache-2.0.

### 2. Modelo fallback local

Manter **Qwen 14B Q4_K_M** (denso, ~9 GB, ~10 GB RAM, ≥ 12 t/s) como reversão imediata via symlink `active.md`.

### 3. Modelo batch (deferred)

Registrar **Qwen 72B Q4_K_M** no catálogo, mas NÃO baixar até necessidade real comprovada (~42 GB, contexto limitado a 4k).

### 4. Modelo deprecated

Registrar **Qwen3.8-27B Q4_K_M** como mantido em disco para backup forense, mas PROIBIDO para uso ativo (INC-F01).

### 5. Flexibilização cloud

Autorizar provedores em free tier da whitelist constitucional (Hugging Face Inference API, OpenRouter, Groq, GitHub Models), **exclusivamente para tarefas não sensíveis**, nos termos da emenda constitucional v1.2.0 (Art. 3, P-02 revisado e Art. 7.4).

### 6. Contexto configurado

32.768 tokens. Orçamento efetivo de execução: 24.000 tokens (75%, margem de segurança). Output máximo: 4.096 tokens.

### 7. Performance alvo

≥ 12 t/s (geração), ≥ 25 t/s (processamento de prompt). TTFT < 2 s.

### 8. Promulgação dos Agentes SDDAI

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

### 9. Resolução dos Gaps

#### G-03 — Forjador e Ratificação

O Humano (Gerente de Projeto / CCB) autorizou expressamente "autonomia total de ação" neste ecossistema. Conforme Constitution Art. 5.1, o Humano é o decisor único via CCB. Esta ADR registra a ratificação humana do forjamento dos 5 agentes SDDAI por `agent-nexus-prime-ultimate` (L0), reconhecendo que a autonomia do ecossistema autorizada pelo Humano prevalece sobre a rigidez do forjador único em casos de exceção documentada e ratificada.

A partir desta ADR, os 5 agentes SDDAI são considerados **promulgados com co-assinatura humana** (Constitution Art. 5.4).

#### G-01 — Gate de Forja (Art. 4.7)

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

#### G-02 — Testes Dedicados (P-06)

Serão criados testes unitários em `tests/agents/test_sddai_*.py` para cada componente `cogme_sddai-*`, cobrindo:

- Loader: ingestão, checksum, validação de entrada
- Memory: otimização, leitura de /proc/meminfo, garbage collection
- Engineer: transformação, features, checksum
- Trainer: treinamento determinístico, métricas, artifact
- CLI: orquestração do pipeline, falha em estágio, saída consolidada

Os testes serão integrados ao `sddai_verify_pipeline.py` (Passo 7).

## Consequências

- **Ganho:** Conformidade total com Constituição COGME (Art. 4.1, 4.3, 4.6, 4.7, P-01 a P-12); agentes plenamente promulgados; rastreabilidade via ledger e ADR; pipeline de verificação funcional; testes automatizados; co-assinatura humana registrada.
- **Negativas:** Esforço de reescrita dos 5 agentes e criação de testes; necessidade de manutenção dos testes à medida que os componentes evoluem.
- **Neutras:** Nenhuma alteração nas camadas L1 (infraestrutura) ou L2 (personas) — SDDAI opera exclusivamente em L3 (metodologia).

## Trade-offs Declarados

| Aspecto | Ganho | Perda/Risco | Mitigação |
|-------|-------|-------------|-----------|
| ADR-006 v2.1.0 + co-assinatura | Conformidade formal com Art. 4.1; ratificação humana | Dependência de decisão Humana | Documentação clara da autorização prévia ("autonomia total de ação") |
| Reescrita dos agentes SDDAI | Passagem no gate de forja (score ≥ 85) | Esforço de reescrita dos agentes; risco de erro na reescrita | Execução de `validate_afa_output.py` após cada alteração |
| Testes dedicados | Cobertura mensurada (P-06) | Manutenção contínua de testes | Integração ao pipeline de verificação existente |

## Kill Switch

Abortar imediatamente se:

1. Qualquer agente SDDAI falhar no `validate_afa_output.py` (score < 85 ou seção ausente)
2. Qualquer teste SDDAI falhar no pipeline de verificação
3. Tentativa de modificar agentes SDDAI sem atualizar o ledger e re-executar o gate
4. Desvio da separação L1/L2/L3 (tentativa de agente SDDAI tocar arquivos L1)

Ao abortar: registrar em `audit_trail` do ledger e marcar `ccb_action_required: true`.

## Governança

- **Custódia:** `agent-nexus-prime-ultimate` (L0 orquestrador) + `agent-architect` (guardião da separação L1/L2/L3)
- **Emenda:** mudança nos agentes SDDAI exige re-execução do gate de forja + atualização desta ADR + CCB humano
- **Auditoria:** `project-auditor` verifica conformidade dos agentes SDDAI a cada milestone
- **Sucessão:** `registry.yaml` + `constitution.md` + ADR-006 v2.1.0 bastam para reconstruir contexto

---

**Nota de renumeração (OKB-C-26 — RAT-2026-10-31-A12):** este artefato foi emitido originalmente como "ADR-013" (promulgação dos agentes SDDAI) e renumerado para **ADR-006 v2.1.0** por decisão do CCB de 31/10/2026, consolidando-se nesta ADR-006 que já tratava do modelo de inteligência SDD. A versão 1.0.0 é preservada como histórico; o conteúdo normativo foi re-hasheado na linha 1.0.1 da tabela de co-assinatura.

---

## CO-ASSINATURA (Constitution Art. 5.4)

| Versão | SHA-256 do conteúdo normativo | Commit Git | Data | Papel do ratificador humano | Instrumento |
|--------|------------------------------|------------|------|----------------------------|-------------|
| 1.0.0 | `48f3968897edd89d7441a200c765c7e3cf1fda6816de3018231b4183bd473e24` | `f6066829fcc3e63803ef5e213d87368c9c40c206` | 31/10/2026 | Gerente de Projeto — CCB de membro único | Promulgação dos agentes SDDAI via ADR-014 (original) + prompt expresso CCB 31/10/2026 |
| 2.1.0 | `ef53e1a6e30a313aba3f441c93181ba1c369acf486aa900e6ad049fc9beddec9` | commit A12 | 31/10/2026 | Gerente de Projeto — CCB de membro único | **Consolidação ADR-006 v2.0.0 + ADR-014 v1.0.1** — consolidação do ecossistema SDDAI (modelo + agentes + MCPs + separação L1/L2/L3) + prompt expresso CCB 31/10/2026 |

---

\*Promulgado sob AFA-ULTIMATE v1.3.0-FINAL. A Constituição é lei marcial: aplica-se, não se debate.*