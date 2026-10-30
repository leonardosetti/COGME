# ADR-005 — Regime de Freeze do TAP e Precedência Intra-TAP

| Campo | Valor |
|---|---|
| Versão | 1.0.0 |
| Status | Regularização Tardia — ratificação CCB pendente da verificação da data 25/09 informada na memória do GP |
| Data da decisão efetiva | 21/09/2026 (NC-00, Plano de Cronograma §3.8) |
| Data de formalização do documento | 28/10/2026 |
| Decisor | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Gatilhos G1–G4 | G1 (impacto transversal — todos os 8 planos), G3 (questionabilidade acadêmica), G4 (trade-off não óbvio — imutabilidade × leitura operacional) |
| Rastreabilidade | TAP §6 (precedência intra-TAP) + §3/§9 P9 (status ontológico do TAP); EAP N9.1; REQ-12; NC-00 (Plano de Cronograma §3.8 — locus canônico da decisão); Glossário §11; ADRs correlatas: ADR-001–004 (todas sob o regime de freeze); Integração §1.4 |
| Domínio PMBOK 7ª | Trabalho do Projeto + Incerteza |
| Processo PMBOK 6ª (dicionário) | 4.6 |

**Tipo:** Regularização tardia
**Data da decisão efetiva:** 21/09/2026
**Data da formalização:** 28/10/2026
**Motivo da tardança:** emissões 001–004 comprometidas em commit 0 byte (dd3b087, 21/09/2026); stubs contraditórios detectados 26/10; a emissão prometida da ADR-005 "antes do M2" (≤ 30/09/2026, Plano de Cronograma §3.9/Tabela 3) não se consumou.
**Lição aprendida:** decisões do GP com ≥ 2 gatilhos devem ser formalizadas em arquivo canônico com corpo no mesmo ciclo do commit de emissão; não deixar a formalização última da fila (política OKB Aditivo §2.3). Auditoria de stubs 0B na lista de verificação de cada marco.

## Contexto

O TAP encontra-se congelado desde o início do planejamento (última versão 18/09/2026, anterior aos planos): não é revisado, reversionado ou corrigido ao longo do ciclo, em conformidade com seu status ontológico (Premissa P9; Glossário §11; PMBOK 6ª §4.1 como dicionário). Divergências entre seções do TAP precisavam de locus formal de resolução sem tocar o termo autorizativo. Fonte integral da decisão (texto canônico): Plano de Cronograma §3.8 NC-00 (docs/planos/plano-cronograma.md).

## Decisão

1. **Freeze:** o TAP não é revisado ao longo do ciclo — nenhuma nota de contexto o corrige.
2. **Precedência intra-TAP:** em divergência entre seções do TAP, a seção §6 Marcos é canônica para matéria temporal e de marcos.
3. **Locus de contexto:** o Plano de Cronograma (§3.8) detém, com precedência, as Notas de Contexto (NCs) que registram a leitura operacional vigente do TAP congelado; divergências jamais são tratadas como correções do TAP.
4. **Trade-off declarado:** aceita-se divergência textual entre o termo autorizativo imutável e a leitura operacional, em favor da imutabilidade da referência de autorização e da trilha auditável de interpretações.

## Alternativas Consideradas

- Revertionar/corrigir o TAP (novas versões) — rejeitado: viola P9, status ontológico e auditabilidade do termo autorizativo.
- Deixar cada plano resolver divergências de forma independente — rejeitado: incoerência entre as 8 áreas e perda de trilha única.
- Corrigir apenas os artefatos vivos (Glossário, ADRs, baseline) por saneamento — adotado parcialmente: registro de saneamento do Plano de Cronograma §3.8 (tabela de pendências por artefato vivo).

## Consequências e Trade-offs

- ✅ Positivas: imutabilidade da referência de autorização; trilha auditável de interpretações; blindagem acadêmica (Prof. Dr. Nivaldo Carleto vê coerência ontológica).
- ⚠️ Riscos: custo de manutenção das NCs; risco de leitura divergente em planos que não adotarem o locus.
- 🔄 Fallback: divergência não coberta por NC → change-request + decisão do GP + registro em NC subsequente.
- **Registro de mudança de compromisso:** a formalização migrou do compromisso de "emissão antes do M2 (≤ 30/09)" para formalização em 28/10/2026 — consequência direta da tardança dos termos acima.

## Governança

- Custódia: agent-architect (ADRs) + agent-pm (Notas de Contexto).
- Emenda: qualquer mudança de marco oficial exige change-request + aprovação do CCB + ADR + comunicação ao Prof. Dr. Nivaldo Carleto no marco subsequente (Integração §1.7.3).
- Incorporação da cláusula na próxima revisão do Plano de Integração §1.4 (Plano de Cronograma Tabela 3).
- kill_switch: screened.

## Histórico

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 28/10/2026 | agent-architect | Regularização tardia: formalização do corpo (decisão efetiva 21/09/2026, NC-00); status reflete pendência de ratificação CCB da data 25/09 alegada em memória do GP |
