---
id: governanca-plano-consolidacao-estrutural
title: Plano de Consolidação Estrutural — COGME
version: 1.0.0
class: plano-governanca
status: active
owner: agent-pm
derived-from:
- docs/governanca/ccb-log.md (cita este plano na entrada RAT-2026-10-31-A09 / OKB-C-25)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- governanca
- plano
- consolidacao-estrutural
---

# Plano de Consolidação Estrutural — COGME

## 1. Propósito

Consolidar em um único ponto de referência o estado estrutural dos artefatos vivos do projeto COGME (planos de gerenciamento, ADRs, normas técnicas, conhecimento operacional, specs SDD, ledger e registro de violações), suprindo a citação pendente no `docs/governanca/ccb-log.md` (OKB-C-25).

## 2. Escopo

Aplica-se aos artefatos de governança e conhecimento listados em §4. Não inclui código-fonte (`src/`, `tests/`) nem infraestrutura de runtime (Docker, systemd, modelos GGUF).

## 3. Estrutura documental consolidada (SSOT)

| Camada | Artefato | Versão | Status | Caminho |
|---|---|---|---|---|
| Lei suprema | Constitution | 1.2.1 | VIGENTE-PLENA | `constitution.md` |
| Termo autorizativo | TAP v3 (baseline viva) | — | congelado/núcleo blindado | `docs/planos/plano-integral-tap-1-2-3-4-5.md` + `docs/tap/delta-v3-1.md` |
| Decisões | ADR-001…017 | várias | ratificadas/supersedidas | `docs/decisoes/` |
| Conhecimento operacional | OKB | 5.2.0 | ratified | `docs/conhecimento/okb.md` |
| Conhecimento operacional | Glossário | 3.2.0 | active | `docs/conhecimento/glossario.md` |
| Índice SSOT | KB-INDEX | 1.3.0 | active | `docs/conhecimento/kb-index.md` |
| Planos de gerenciamento | 8 planos de área | 1.0.x–1.2.x | active | `docs/planos/` |
| Normas técnicas | CI-CD-GOV-001 / DEVSECOPS-001 | 1.0.0 | ratified | `docs/governanca/` |
| Registro de decisões | CCB-LOG | 0.1.0 | active | `docs/governanca/ccb-log.md` |
| Registro de violações | vio-register | 1.1.0 | active | `docs/auditorias/vio-register.md` |
| Ledger operacional | ledger.yaml | schema v2.0 | active | `.ai/agents/ledger.yaml` |

## 4. Regras de consolidação

- Um fato = um local (C-P-05 / SSOT informacional). Cross-reference substitui duplicação.
- Nenhuma alteração de ADR é válida sem registro em `docs/decisoes/ADR-LOG.md`.
- Mudanças na Constituição exigem ratificação humana explícita + co-assinatura (Art. 5.4).
- O núcleo blindado do TAP (§6 Marcos) não é alterado textualmente; leitura operacional vive nas Notas de Contexto (NC-XX) e no Delta Log (`docs/tap/delta-v3-1.md`).

## 5. Pendências conhecidas (decisão CCB)

- OKB-C-06b: colisão M2 = M3 em 15/11/2026 (deliberação futura do CCB).
- OKB-C-08: artefatos 0 B (`TAP.md`, `registro.md`, `requisitos.md`, `.ai/specs/{tap,eap,requisitos}.md`).
- OKB-C-22: propagação ADR-010 (SQLite → PostgreSQL) nos planos — parcialmente resolvida em requisitos/planos; pendente de verificação em cronograma/custos/recursos.

## 6. Rastreabilidade

- Citado por: `docs/governanca/ccb-log.md` (entrada RAT-2026-10-31-A09, artefato A-002) e OKB-C-25.
- Alinha-se a: Constitution v1.2.1 (Art. 2.1 hierarquia; Art. 9.3 fluxo de mudança integrado); OKB v5.2.0 (§1.1 hierarquia, §4 inventário, §10 inconsistências).

---

*Elaborado sob autoridade do CCB (GP Leonardo, membro único) para suprir OKB-C-25. Documento ativo; revisar a cada milestone.*
