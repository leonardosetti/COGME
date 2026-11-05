---
id: docs-normas-norma-templates-artefatos
title: Norma Global de Templates para Artefatos Markdown
type: conhecimento
version: 1.0.0
status: ratificado
owner: agent-project-analyst
derived-from:
- constitution.md (Art. 2, Art. 3 P-05, Art. 9)
- docs/conhecimento/compliance/auditoria-normalizacao-artefatos.md (auditoria 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- norma
- template
- frontmatter
- governanca
---

# Norma Global de Templates para Artefatos *.md

## 1. Objetivo

Padronizar todo artefato `*.md` do projeto COGME com frontmatter YAML para rastreabilidade, governança e compliance (LGPD). Cada tipo de artefato (Specs, ADRs, Change-Requests, Audits, Tests, Handoffs, Personas, Planos, Procedimentos, Relatórios, Requisitos, Métricas, Constituição, README) submete-se ao seu próprio padrão.

## 2. Escopo

Aplica-se a **todos** os artefatos `*.md` do repositório COGME (331 arquivos), excluindo:
- `.opencode/skills/` (skills instaladas do OpenCode, mantidas externamente)
- `.git/`, `node_modules/`, `.venv/`, `.pytest_cache/`, `graphify-out/`

Não-Markdown (`.docx`, `.pdf`, `.png`, `.svg`, `.drawio`) fica fora do escopo.

## 3. Frontmatter comum (obrigatório em todo *.md)

```yaml
---
id: <slug-unico>
title: <título>
type: <classe-de-artefato>
version: <MAJOR.MINOR.PATCH>
status: <ativo | draft | ratificado | obsoleto | arquivado>
owner: <responsável>          # papel, sem nome civil
derived-from:
  - <fonte canônica>
last-revised: <YYYY-MM-DD>
lgpd-class: <n/a | interno | sensível>
tags:
  - <tag>
---
```

Regras:
- O bloco YAML deve ser a primeira coisa do arquivo (linha 1).
- `id`: slug único, kebab-case, sem colisão no repositório.
- `type`: um dos tipos da Seção 4, coerente com o diretório (Seção 5).
- `status`: valores fechados; `draft` para em elaboração, `ativo` para vigente, `ratificado` para aprovado pelo CCB, `obsoleto` para substituído, `arquivado` para histórico.
- `owner`: papel (ex.: `agent-project-auditor`, `Gerente de Projeto`), nunca nome civil.
- `derived-from`: lista de fontes canônicas (arquivos ou artigos da Constituição/TAP/ADR).
- `last-revised`: data da última revisão no formato ISO 8601.
- `lgpd-class`: `n/a` quando não há dados, `interno` para artefato interno, `sensível` se houver PII/dados de terceiros (proibido sem consentimento documentado).

## 4. Tipos de artefato e campos específicos

Além do frontmatter comum, cada tipo acrescenta campos próprios:

| Tipo | Diretório canônico | Campos específicos |
|------|-------------------|-------------------|
| `spec` | `docs/especificacoes/`, `.ai/specs/` | `spec-id`, `camada`, `estado-implementacao`, `rastreia-req`, `testes-vinculados` |
| `adr` | `docs/decisoes/` | `decision`, `status` (proposed\|accepted\|superseded\|deprecated), `supersedes`, `domain-pmbok` |
| `change-request` | `docs/change-requests/` | `cr-number`, `impacto`, `prazo-analise-gp`, `decisao-ccb`, `instrumento` |
| `audit` | `docs/auditorias/`, `docs/verification/` | `audit-id`, `periodo`, `veredito`, `artigos-constitucionais`, `vio-referenciados` |
| `test` | `docs/uat/`, `tests/` | `test-id`, `tipo` (unit\|e2e), `spec-vinculada`, `cobertura` |
| `handoff` | `.ai/handoffs/` | `hf-id`, `sender`, `receiver`, `acao`, `dod`, `estado` |
| `persona` | `.ai/personas/` | `layer` (L1\|L2\|L3), `role`, `contrato-validado` |
| `plano` | `docs/planos/` | `marco-vinculado`, `doD`, `revisao-periodica` |
| `procedimento` | `docs/operacao/` | `marco-vinculado`, `doD`, `revisao-periodica` |
| `relatorio` | `docs/relatorios/`, `docs/analise/` | (campos comuns apenas) |
| `evidencia` | `docs/evidencias/` | (campos comuns apenas) |
| `metrica` | `docs/metricas/` | (campos comuns apenas) |
| `requisito` | `docs/requisitos/` | (campos comuns apenas) |
| `governanca` | `docs/governanca/` | (campos comuns apenas) |
| `conhecimento` | `docs/conhecimento/`, `.ai/mcp/` | (campos comuns apenas) |
| `archive` | `docs/archive/` | (campos comuns apenas) |
| `constituicao` | `constitution.md` | `hash-normativo`, `co-assinatura` |
| `readme` | `README.md`, `AGENTS.md` | (campos comuns apenas) |

## 5. Mapeamento diretório → type

O `type` deve ser coerente com o diretório do arquivo:

| Diretório | type |
|-----------|------|
| `docs/decisoes/` | `adr` |
| `docs/change-requests/` | `change-request` |
| `docs/auditorias/` | `audit` |
| `docs/especificacoes/` | `spec` |
| `docs/planos/` | `plano` |
| `docs/operacao/` | `procedimento` |
| `docs/relatorios/` | `relatorio` |
| `docs/evidencias/` | `evidencia` |
| `docs/metricas/` | `metrica` |
| `docs/requisitos/` | `requisito` |
| `docs/governanca/` | `governanca` |
| `docs/conhecimento/` | `conhecimento` |
| `docs/archive/` | `archive` |
| `docs/analise/` | `relatorio` |
| `docs/uat/` | `test` |
| `docs/tap/` | `spec` |
| `docs/verification/` | `audit` |
| `.ai/specs/` | `spec` |
| `.ai/handoffs/` | `handoff` |
| `.ai/personas/` | `persona` |
| `constitution.md` | `constituicao` |
| `README.md`, `AGENTS.md` | `readme` |

Exceções são classificadas manualmente e registradas no `derived-from`.

## 6. Gate de validação

O script `scripts/validar_frontmatter_md.py` verifica todo `*.md` do escopo:
- frontmatter YAML válido na linha 1;
- todos os 10 campos comuns presentes;
- `type` coerente com o diretório (Seção 5);
- `status` e `lgpd-class` nos valores fechados;
- `id` único no repositório.

O CI roda o script no job `lint`. Qualquer `.md` fora do padrão bloqueia o pipeline. Novo `.md` só entra com frontmatter completo.

## 7. Governança de mudanças

- Alteração de `type` ou conteúdo normativo de um `.md` exige Change-Request (`docs/change-requests/`), parecer de auditoria e ratificação do CCB (Constituição Art. 9).
- Commit padrão: `docs(norma): <descricao>` ou `chore(docs): <descricao>`.
- O registro append-only `docs/auditorias/vio-register.md` nunca é reescrito; correções futuras entram como linha nova.

## 8. Adesão do estoque existente

Os 331 artefatos existentes são adequados por ondas de diretório (onda 1: os 39 sem frontmatter; ondas seguintes: os 292 com frontmatter genérico da auditoria de 2026-11-05, ajustando `class` → `type` e acrescentando campos específicos). Nenhum arquivo é apagado ou renomeado.

---