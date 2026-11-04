---
id: plano-consolidacao-estrutural
title: Plano de Consolidação Estrutural / Desbloat — first-principles + YAGNI
version: 0.1.0
date: 2026-10-30
owner: agent-nexus-prime-ultimate (custódio de roteamento)
ratification: PENDENTE CCB (Agenda A-03)
---

# Plano de Consolidação Estrutural (Desbloat) — COGME

> Mandato: remoção de lixo/bloat, normalização futura de estruturas e nomenclaturas
> por first-principles + YAGNI, consolidação por similaridade (exceto ADRs, TAs, CRs),
> aplicação ortogonal de PMBOK/TOGAF/ITIL. Registro vivo: `docs/governanca/ccb-log.md`.

## 1. Princípios norteadores

**First-principles:** todo artefato existe para responder UMA pergunta canônica. Se dois
artefatos respondem a mesma pergunta, permanece o canônico; o outro é arquivado ou removido.
**YAGNI:** não versionar nada que não tenha consumidor declarado no DAG (prova: front-matter
`downstream`); não criar estrutura sem demanda corrente.
**Single-source:** ADRs = decisões exclusivas (nunca consolidadas entre si); TAs = estado
de task; CRs = pedidos de mudança. Todo o resto admite consolidação temática.

## 2. Ações executadas (2026-10-30)

| ID | Ação | Bloco antigo | Registro |
|-----|------|--------------|----------|
| A01 | Descarte de dumps acidentais: `argparse` (16MB PS), `lst.txt`, lock `.~*.docx`, `.obsidian/`, `_consolidado-adrs.tmp.md` (impróprio por autodeclaração) | A + dedupe ADR-006 | commit higiene + `.gitignore` |
| A02 | Arquivamento canônico: `Docs/Monografia` → `docs/archive/apocrifo/md/`; mídia binária 6.4MB desdoublificada; `COGME/` aninhado (Next.js legado pré-ADR-001) removido (100% recuperável via histórico) | B | commit `608c299` |
| A03 | Remoção de manuais raiz duplicados (`SDD_Configuration_Manual.md` e variantes pt) — conteúdo consolidado em `docs/` | B | commit `608c299` |
| A04 | Dedupe de ADR-006: cópias byte-idênticas (`ADR-006-chunk-1.md`, `ADR-006-chunk-aa`, provas md5 em `_consolidado-adrs.tmp.md`) removidas; permanece 1 canônica | A/D | idem |
| A05 | SANITIZE: `config/environment.yaml` token literal → `${COGME_SANDBOX_TOKEN}` (12-factor; LGPD P-02) | segurança | pendência zero |
| A06 | `test/validation/test_nexus_yaml.py` RESTAURADO — deleção era potencial vetore KILL_SWITCH #4 (erosão de gate de CI) | C.10 | commit higiene |

## 3. Ações PENDENTES de ratificação CCB (não executar sem ratificação)

| ID | Item | Recomendação | Impacto |
|-----|------|--------------|---------|
| P01 | `constitution.md` v1.2.0 (E-09..E-19), status VIGENTE-INTERINA | co-assinatura humana (Art. 5.4) → commit único | lei suprema |
| P02 | `.ai/personas/_base.md`: trim 68→11 linhas (deltas perdidos em incidente de processo, ver I01) | re-aplicar trim intencional a partir de cópia do auditor, se ratificado | personas dos agentes |
| P03 | `.opencode/opencode.json`: ctx 32k→45.7k, reasoning default, deny-list endurecida | revisar budget (SP-01) e ratificar | comportamento modelo |
| P04 | Normalização de nomenclatura (`snake_cases` vs `kebab-case` na raiz; docs em pt/en mistos) | fase pós-ratificação P01, onda única com mapeamento de renames | SSOT estrutural |

## 4. Estado alvo (normalização pós-P01) — proposta MESO

```
documentos/                     # pt-BR: artefatos de governança e engenharia
  decisoes/      # ADRs (não consolidáveis; 1 arquivo por decisão)
  planos/        # TAP, planos de áreas PMBOK
  auditorias/    # AUD-*, vio-register.md, cidadania auditória
  governanca/    # ccb-log.md (vivo), matriz-raci.yaml
  conhecimento/  # KB/OKB única (sem drafts de sessão)
  requisito/     # REQ-*, EAP canônica
.ai/
  agents/ specs/ handoffs/ config/ governanca/    # fábrica + contratos + estado
src/ tests/ scripts/     # código, gates, ferramentaria (kebab-case)
```

## 5. Aplicação ortogonal PMBOK × TOGAF × ITIL

| Conceito | PMBOK 7 | TOGAF | ITIL 4 | Aplicação COGME |
|----------|---------|-------|--------|------------------|
| Mudança | Gerenc. de Mudanças | Architecture Board | Change Enablement (CAB) | **CCB-LOG vivo** = CAB digital |
| Decisão | Integr./Gerenc. de Projetos | ADR no ADM GAP | RFC → Change Record | ADR (isenta de consolidação) + CR |
| Arco de valor | Gerenc. de Valor/Stakeholders |打底裤 ADM Requirements Mgmt | Continual Improvement | auditorias recorrentes AUD-* |
| Risco | Risco (T) | Architecture Risk Mgmt | | vio-register.md (addenda) |
| Qualidade | Gerenc. de Qualidade | Compliance Reviews | Service Validation | gates nexus/dispatcher + pytest |
| Conhecimento | Lições Aprendidas | Architecture Repository | SKMS | docs/conhecimento/KB-INDEX.md |
| Escopo | Gerenc. de Escopo | Boundary Statements | | Art. 1.2 constituição + ADR-005 |

Ortogonalidade garantida: PMBOK responde "o QUE governar", TOGAF "O QUE arquiteturar",
ITIL "COMO operar a mudança CONTINUAMENTE". Nenhum duplica outro; instruções conflitantes
devem escalar ao CCB (Art. 2 hierarquia normativa).
