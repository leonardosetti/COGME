---
id: ai-specs-spec-adr-template-spec
title: Template Canônico de ADR — COGME
type: spec
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-018-nomeclatura-arquivos.md
- docs/conhecimento/compliance/auditoria-normalizacao-artefatos.md
- docs/conhecimento/okb.md §8.3
last-revised: '2026-11-16'
lgpd-class: n/a
tags:
- spec
- adr
- template
- norma
spec_id: spec-adr-template
specname: adr-template
---

# Template Canônico de ADR — COGME

Este template é a **norma de template para ADRs** do projeto COGME. Toda ADR nova ou emendada deve seguir esta estrutura. Não criar nova ADR sobrepondo regras de ADR anterior; usar emenda de versão (ADR-LOG).

## 1. Nomenclatura do arquivo (ADR-018)

`decisoes-adr-NNN-nome_artefato.md`

- `tipo_artefato` = `decisoes` (pasta `docs/decisoes/`)
- `id_artefato` = `adr-NNN` (ex.: `adr-001`, `adr-016`)
- `nome_artefato` = slug EN, kebab-case, descritivo curto (ex.: `stack`, `kanban`, `metricas`, `regime-tap`)
- Extensão: `.md`

## 2. Frontmatter YAML (obrigatório, único bloco)

Campos na ordem:

| Campo | Tipo | Obrigatório | Exemplo |
|-------|------|-------------|---------|
| `id` | slug | sim | `decisoes-adr-001-stack` |
| `title` | string | sim | `ADR-001 — Stack Tecnológica FOSS` |
| `version` | semver | sim | `1.1.0` |
| `class` | enum | sim | `decisao-adr` |
| `status` | enum | sim | `draft\|ratificado\|active\|supersedida\|deprecated\|obsoleto` |
| `owner` | slug | sim | `agent-project-analyst` |
| `derived-from` | lista | sim | `docs/decisoes/adr-001-stack.md (normalizado em 2026-11-05)` |
| `last-revised` | date | sim | `2026-11-05` |
| `lgpd-class` | string | sim | `n/a` |
| `tags` | lista | sim | `- decisoes\n- docs` |
| `data-decisao` | date | sim | `19/09/2026` |
| `data-formalizacao` | date | sim | `28/10/2026` |
| `decisor` | string | sim | `GP Leonardo (CCB único)` |
| `instrumento-ccb` | string | não | `RAT-2026-10-31-A13` |
| `gatilhos` | texto | sim | `G1, G3, G4` |
| `rastreabilidade` | texto | sim | `TAP §X; EAP Nx; REQ-xx; ADR-0xx` |
| `dominio-pmbok` | texto | sim | `Trabalho do Projeto + Abordagem de Desenvolvimento` |
| `processo-pmbok-6` | texto | não | `4.6` |
| `supersede` | slug | não | `decisoes-adr-010-stack-infraestrutura` |
| `superseded-by` | slug | não | `decisoes-adr-001-stack` |
| `kill-switch` | texto | sim | `screened` ou vetores aplicáveis |

## 3. Estrutura do corpo (obrigatório, nesta ordem)

### 3.1 Tabela de metadados (logo após o frontmatter)

```
| Campo | Valor |
|-------|-------|
| Versão | 1.1.0 |
| Status | Ratificado |
| Data da decisão | 19/09/2026 |
| Data de formalização | 28/10/2026 |
| Decisor | GP Leonardo (CCB único) |
| Gatilhos G1–G4 | G1, G3, G4 |
| Rastreabilidade | TAP §3; EAP N4.1; REQ-12 |
| Domínio PMBOK 7ª | ... |
| Processo PMBOK 6ª | ... |
```

### 3.2 Contexto
### 3.3 Decisão
### 3.4 Alternativas Consideradas (tabela, quando houver ≥ 2 opções)
### 3.5 Consequências e Trade-offs (positivas / negativas e riscos / fallback / trade-offs aceitos)
### 3.6 Sobreposição de Decisões (tabela: ADR sobreposta, Natureza, Motivo, Domínio PMBOK 7ª, Data) — omitir se nenhuma
### 3.7 kill_switch (ou `Não aplicável diretamente.`)
### 3.8 Governança (custódia, emenda, auditoria)
### 3.9 Histórico (tabela: Versão, Data, Autor, Mudança)
### 3.10 Ratificação (instrumento CCB, data, status) — omitir se ainda não ratificada
### 3.11 Referências (lista de links a arquivos canônicos)

## 4. Regras de cross-reference

- Citar sempre com versão pinada: `[ADR-010 v1.0.0](docs/decisoes/adr-010-stack-infraestrutura.md)`
- Nunca citar `docs/archive/` como fonte viva
- Versão desconhecida → `UNKNOWN-GAP`, não omitir
- Um fato = um local; não duplicar texto de outra ADR, usar cross-reference

## 5. Ratificação e promulgação

Somente após revisão deste template e do corpo, a ADR é submetida ao CCB (GP Leonardo) para ratificação via instrumento `RAT-YYYY-MM-DD-A##`, com registro em `docs/decisoes/adr-log.md` e `docs/governanca/ccb-log.md`.

## 6. Critérios de aceite e testes (deste template)

- [ ] AC-01: arquivo não vazio, com frontmatter YAML completo (19 campos obrigatórios na ordem declarada).
- [ ] AC-02: campos `id`, `title`, `version`, `class`, `status`, `owner`, `derived-from`, `last-revised`, `lgpd-class`, `tags`, `data-decisao`, `data-formalizacao`, `decisor`, `gatilhos`, `rastreabilidade`, `dominio-pmbok`, `kill-switch` presentes no frontmatter.
- [ ] AC-03: corpo segue a ordem obrigatória: 3.1 tabela de metadados → 3.2 Contexto → 3.3 Decisão → 3.4 Alternativas → 3.5 Consequências → 3.6 Sobreposição → 3.7 kill_switch → 3.8 Governança → 3.9 Histórico → 3.10 Ratificação → 3.11 Referências.
- [ ] AC-04: regras de cross-reference respeitadas (versão pinada, nunca citar `docs/archive/`, `UNKNOWN-GAP` para versão desconhecida, um fato = um local).
- [ ] AC-05: ratificação via CCB com instrumento `RAT-YYYY-MM-DD-A##` e registro em `adr-log.md` + `ccb-log.md`.
- [ ] AC-06: nenhum outro arquivo editado nesta tarefa; nada commitado além deste template.

## 7. Rastreabilidade

| Seção deste artefato | Fonte |
|---|---|
| Frontmatter / spec_id | MANIFEST.md §1.1 (template canônico a–h); HF-0031 §2.1 |
| §1 Nomenclatura | docs/decisoes/adr-018-nomeclatura-arquivos.md (ADR-018) |
| §2 Frontmatter YAML | MANIFEST.md §1.1; ADR-018 |
| §3 Estrutura do corpo | docs/conhecimento/compliance/auditoria-normalizacao-artefatos.md §8.3; docs/conhecimento/okb.md §8.3 |
| §4 Regras de cross-reference | docs/conhecimento/okb.md §8.3; MANIFEST §4 |
| §5 Ratificação | docs/decisoes/adr-log.md; docs/governanca/ccb-log.md (modelo CAB vivo, ITIL 4) |
| §6 Critérios de aceite | MANIFEST §1.2 (camada e) |
| §7 Rastreabilidade | MANIFEST §1.2 (camada f) |

## 8. Fora de escopo (YAGNI)

- Criar ADRs concretas (este é apenas o template normativo).
- Alterar ADRs já ratificadas (usar emenda de versão, ADR-LOG).
- Citar `docs/archive/` como fonte viva (vedado por §4).

## CHANGELOG

- **1.0.0 — 2026-11-16 — normalização e aprovação (opção n)**: inclusão de `spec_id`, `specname`, status `ativo`, seções de critérios de aceite (§6) e rastreabilidade (§7), fora de escopo (§8) e CHANGELOG. Template aprovado como norma para emissão de novas ADRs.