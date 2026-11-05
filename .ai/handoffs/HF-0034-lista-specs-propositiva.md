---
id: ai-handoffs-hf-0034-lista-specs-propositiva
title: 'Handoff: Enriquecimento da lista de specs pendentes com dados propositivos + rodapé com hora e ratificação CCB (TA-0035)'
type: handoff
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- .ai/handoffs/HF-0034-lista-specs-propositiva.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- handoffs
- docs
- adequado-a-norma
---
# Handoff: Enriquecimento da lista de specs pendentes com dados propositivos + rodapé com hora e ratificação CCB (TA-0035)

## Contexto

Decisão do GP/Humano ratificada em CCB (2026-11-02, constitution.md Art. 5.1): atualizar
`docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md` (emitida na TA-0031, sua custódia —
frontmatter `owner: agent-sdd-specialist`) acrescentando, para CADA spec pendente, um
**resumo proposicional** — dados do que a spec propõe (objetivo, escopo, contratos/requisitos
que cobriria, entregáveis), em forma tabular coerente com o documento atual. O rodapé deve
passar a conter **data + hora** da atualização e o registro da **ratificação CCB**.

## Tarefa

1. **Resumo proposicional das 13 specs pendentes** (A.1–A.3 placeholders + B.1–B.10 domínio):
   para cada item, 1–2 frases com: objetivo da spec, escopo que cobriria (requisitos/contratos/
   artefatos), e entregável esperado. Apresentação: NOVA COLUNA `Resumo proposicional` nas
   tabelas A e B (mantendo o formato tabular; se a largura prejudicar a legibilidade, blocos
   por item imediatamente abaixo de cada tabela, mas sem quebrar a numeração A.n/B.n).
2. **Base de conteúdo = apenas as origens já citadas na própria lista** (leia-as):
   REQ-06/09/10/11/13/14, GAP-01/02/04/08, US-004/009/011/014, ondas A.11–A.22
   (`docs/planos/plano-granular/plano-producao-agentes.md`), P-04 (`constitution.md:36`),
   trechos de `spec-001/002/004/005` citados nas linhas de origem. **Proibido inventar**
   requisitos, prazos, status ou nomes não citados; incerteza = `UNKNOWN - verify`.
3. **Rodapé atualizado** (substituir o rodapé de emissão atual): manter a referência
   original (TA-0031/HF-0031) e acrescentar linha de atualização com **data e hora UTC**
   (obtenha com `date -u +%Y-%m-%dT%H:%MZ`), tarefa desta atualização (TA-0035/HF-0034) e
   registro: `Ratificação CCB — GP/Humano 2026-11-02 (Art. 5.1): dados propositivos + carimbo de hora`.
4. **Frontmatter**: bump `version: 1.0.0` → `1.1.0` e campo `updated:` com o mesmo timestamp.

## Critérios de Aceite

- [ ] Coluna/blocos de resumo proposicional presentes para TODOS os 13 itens (A.1–A.3, B.1–B.10), em PT-BR
- [ ] Todo resumo apoia-se em origem já citada na lista (nenhum requisito novo inventado; `UNKNOWN - verify` onde aplicável)
- [ ] Formato tabular do documento preservado; seções C/D/E/F intactas em conteúdo
- [ ] Rodapé com data + hora UTC da atualização, TA-0035/HF-0034 e registro de Ratificação CCB (Art. 5.1)
- [ ] Frontmatter `version: 1.1.0` + `updated:` com o mesmo timestamp
- [ ] EXCLUSIVAMENTE `docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md` editado (git status confirma)
- [ ] Imutáveis intocados: constitution.md, registry, .opencode/agents, handoffs, ledger, ADRs, .ai/specs/*

## Restrições

- Nenhum outro arquivo editado; nenhuma spec em `.ai/specs/` alterada.
- Narrativa PT-BR; identificadores/caminhos EN; evidência `arquivo:linha` nas origens dos resumos.
- Sem decisão de aprovação (CCB é o Humano — aqui só se registra a ratificação já dada).
- Retorno: parcel half-duplex schema 6 EXATO (enum `accepted|rejected|escalated|require_clarification`,
  `route` OBJETO {sender, receiver}, `notes` string — NÃO array), `dod` com todos os AC,
  `notes` ≤4 linhas. Resposta final ≤1200 tokens (conteúdo vai ao ARQUIVO).
