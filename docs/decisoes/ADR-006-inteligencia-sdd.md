
# ADR-006 — Módulo de Inteligência SDD: Modelo Primário, Fallback e Flexibilização Cloud/FREE

| Campo                                         | Valor                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Versão**                             | 2.0.0                                                                                                                                                                                                                                                                                                                                                         |
| **Status**                              | Finalizado (ratificado pelo CCB-001 em 29/10/2026)                                                                                                                                                                                                                                                                                                            |
| **Data da decisão**                    | 26/10/2026                                                                                                                                                                                                                                                                                                                                                    |
| **Data de formalização do documento** | 29/10/2026                                                                                                                                                                                                                                                                                                                                                    |
| **Decisor**                             | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7)                                                                                                                                                                                                                                                                                                         |
| **Gatilhos G1–G4**                     | G1 (impacto transversal — todas as fases de execução SDD), G2 (irreversibilidade prática — troca de modelo GGUF implica recompilação e revalidação de throughput), G3 (questionabilidade acadêmica — "por que MoE e não denso?"), G4 (trade-off não óbvio — eficiência computacional × complexidade operacional de dois modos de execução) |
| **Rastreabilidade**                     | TAP §3 (Inovação) + §8 (Restrições FOSS/orçamento zero) + §9 (Premissa P3 — stack local); EAP N1.4, N4.4; REQ-12 (ADRs), REQ-13 (prompts catalogados); ADRs correlatas: ADR-001 (stack FOSS, sobreposta parcialmente), ADR-005 (freeze), ADR-011 (MCPs e memória persistente, sobreposta parcialmente por esta em relação ao roteamento)          |
| **Domínio PMBOK 7ª**                  | Abordagem de Desenvolvimento + Trabalho do Projeto + Incerteza                                                                                                                                                                                                                                                                                                |
| **Processo PMBOK 6ª (dicionário)**    | 4.3 Orientar e Gerenciar o Trabalho do Projeto; 8.2 Realizar Garantia da Qualidade                                                                                                                                                                                                                                                                            |

## Contexto

O ecossistema SDD do COGME opera exclusivamente em hardware local (AMD Ryzen 7 8700G, Radeon 780M, 58GB RAM reais, Arch Linux). O motor de inferência é o `llama.cpp` compilado com Vulkan, LTO e AVX-512. A interface é o OpenCode.

Na versão 1.0 desta ADR, o modelo primário era Qwen 32B Instruct (denso, ~20GB RAM ativa). Após materialização do risco RE-08 (*overengineering* de governança consumindo capacidade de desenvolvimento), constatou-se que o modelo denso limitava fluxos paralelos de agentes, degradando throughput abaixo de 6 t/s em cenários de múltiplas personas ativas simultaneamente.

Adicionalmente, a Constituição v1.1.0 proibia qualquer tráfego de dados do projeto para nuvem (P-02 absolutista). Essa restrição, embora defensável academicamente, impedia resiliência operacional em picos de carga sem comprometer orçamento zero.

## Opções Consideradas

| #  | Opção                                       | Prós                                                                                     | Contras                                                                                                       |
| -- | --------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| O1 | Manter Qwen 32B Instruct denoso               | Simplicidade; um único modo de execução                                                | Throughput insuficiente para fluxos paralelos; RAM pico elevado; sem resiliência                             |
| O2 | Migrar para Qwen3-30B-A3B MoE (Q4_K_M)        | ~3B parâmetros ativos por token vs. 30B; ~4GB RAM ativa; ≥ 12 t/s esperados; Apache-2.0 | Complexidade adicional (dois modos: local + cloud fallback); necessidade de reconciliar `download_model.sh` |
| O3 | Adicionar modelos cloud free tier (whitelist) | Resiliência em sobrecarga local; custo zero; Hugging Face/OpenRouter/Groq/GitHub Models  | Risco de soberania de dados; violação potencial da Constituição v1.1.0 se não emendada                   |
| O4 | Combinar O2 + O3 com restrições             | Melhor equilíbrio entre eficiência, resiliência e soberania                            | Maior superfície de configuração; exige kill switch claro                                                  |

## Decisão

**Aprovar a opção O4.**

1. **Modelo primário:** substituir Qwen 32B Instruct por **Qwen3-30B-A3B Q4_K_M** (MoE: 30B totais, ~3B ativos por token, ~18 GB em disco, ~4 GB RAM ativa). Licença: Apache-2.0.
2. **Modelo fallback local:** manter **Qwen 14B Q4_K_M** (denso, ~9 GB, ~10 GB RAM, ≥ 12 t/s) como reversão imediata via symlink `active.md`.
3. **Modelo batch (deferred):** registrar **Qwen 72B Q4_K_M** no catálogo, mas NÃO baixar até necessidade real comprovada (~42 GB, contexto limitado a 4k).
4. **Modelo deprecated:** registrar **Qwen3.8-27B Q4_K_M** como mantido em disco para backup forense, mas PROIBIDO para uso ativo (INC-F01).
5. **Flexibilização cloud:** autorizar provedores em free tier da whitelist constitucional (Hugging Face Inference API, OpenRouter, Groq, GitHub Models), **exclusivamente para tarefas não sensíveis**, nos termos da emenda constitucional v1.2.0 (Art. 3, P-02 revisado e Art. 7.4).
6. **Contexto configurado:** 32.768 tokens. Orçamento efetivo de execução: 24.000 tokens (75%, margem de segurança). Output máximo: 4.096 tokens.
7. **Performance alvo:** ≥ 12 t/s (geração), ≥ 25 t/s (processamento de prompt). TTFT < 2 s.

## Consequências

- Positivas: aumento significativo de throughput em fluxos paralelos; redução de consumo de RAM ativa; resiliência operacional via fallback cloud condicionado; alinhamento com ADR-011 (MCPs e separação L1/L2/L3).
- Negativas: complexidade de gestão de dois modos de execução (local + cloud); necessidade de auditoria contínua de soberania de dados; overhead de reconciliação do `download_model.sh`.
- Neutras: o modelo denso Qwen 32B permanece disponível como fallback secundário, mas não é mais o primário.

## Trade-offs Declarados

| Aspecto                  | Ganho                           | Perda/Risco                                                    | Mitigação                                                                                         |
| ------------------------ | ------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| MoE vs. Denso            | Eficiência (3B ativos vs. 30B) | Menor profundidade de raciocínio em tarefas complexas únicas | Fallback para Qwen 72B deferred se necessário; revisão humana obrigatória                        |
| Cloud free tier          | Resiliência em sobrecarga      | Risco de soberania de dados                                    | Proibição absoluta de dados sensíveis; whitelist auditável; kill switch imediato                |
| Dois modos de execução | Flexibilidade                   | Complexidade operacional                                       | Symlink `active.md` como mecanismo canônico de troca; MCP `nexus-dispatch` gerencia roteamento |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo                                                                                               | Domínio PMBOK 7ª           | Data       |
| -------------- | -------- | ---------------------------------------------------------------------------------------------------- | ---------------------------- | ---------- |
| ADR-001        | Parcial  | Substituição do modelo LLM primário (Qwen 32B → Qwen3-30B-A3B MoE) + flexibilização Cloud/FREE | Abordagem de Desenvolvimento | 29/10/2026 |

## kill_switch

Reversão automática para Qwen 14B via alteração do symlink `.ai/personas/active.md` se:

- throughput < 12 t/s por 5 minutos consecutivos;
- detecção de envio de dados sensíveis para cloud não autorizada;
- corrupção do ledger de sessão impedindo roteamento determinístico.

## Governança

- **Custódia:** `agent-nexus-prime-ultimate` (L0 orquestrador).
- **Emenda:** somente via change-request + CCB humano (GP Leonardo) + ADR MAJOR.
- **Auditoria:** `project-auditor` verifica conformidade com P-02/P-03 em cada milestone.
- **Registro de handoffs:** todos os prompts enviados ao modelo primário ou fallback devem ser catalogados em `.ai/handoffs/task-ta-*.json` (REQ-13).
