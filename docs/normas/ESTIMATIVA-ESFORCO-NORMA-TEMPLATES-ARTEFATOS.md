---
id: docs-normas-estimativa-esforco-norma-templates-artefatos
title: Estimativa de esforço — Norma global de templates para artefatos *.md
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/normas/ESTIMATIVA-ESFORCO-NORMA-TEMPLATES-ARTEFATOS.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- normas
- docs
- adequado-a-norma
---
# Estimativa de esforço — Norma global de templates para artefatos *.md

**Tipo:** estimativa de esforço (análise apenas — não aplica a norma)  
**Versão:** 1.0.0  
**Status:** proposta  
**Data:** 2026-11-05  
**Autor:** análise de contexto (investigate-first + levantamento de FS)  
**Escopo:** repositório COGME, todos os artefatos `*.md`  
**Aplica:** não ainda (fase de planejamento)

---

## 1. Contexto e decisão

O repositório já possui uma normalização parcial de frontmatter aplicada em `docs/*/*` (auditoria de 2026-11-05, 186 artefatos, frontmatter genérico). A norma requerida vai além: um padrão global para **todo** artefato `*.md` do projeto, com **template próprio por tipo de artefato** (Specs, ADRs, Change-Requests, Audits, Tests, Handoffs, Personas, Planos, Procedimentos, Relatórios, Requisitos, Métricas, Constituição, etc.), incluindo frontmatter para padronização de informação, governança e compliance (LGPD, rastreabilidade, versionamento, status, owner).

Esta fase **não aplica** a norma. Calcula apenas o esforço para, em fase subsequente, ser submetida a Change-Request e ratificada pelo CCB (Art. 9 da Constituição) antes de qualquer alteração nos 331 artefatos.

---

## 2. Escopo real (levantado em 2026-11-05)

Total de artefatos `*.md` do projeto COGME (fora `.opencode/` skills instaladas, `.git`, `node_modules`, `.venv`, `.pytest_cache`, `graphify-out`): **331**.

| Grupo | Diretório | Qtd | Tipo de artefato predominante | Já tem frontmatter |
|-------|-----------|-----|-------------------------------|--------------------|
| Documentação | `docs/` | 194 | ADRs, Audits, Change-Requests, Planos, Relatórios, Especificações, Requisitos, Conhecimento, TAP, Compliance, Governança, UAT, Archive | 186 (8 docs sem FM: auditoria-normalizacao, auditoria-renomeacao, troubleshooting, uat/README, uat/rodada-001, 2 analise) |
| Especificações SDD | `.ai/specs/` | 23 | Specs SDD, requisitos, TAP, MANIFEST, kb-taxonomy, changelog, template ADR | 18 (5 sem FM: afa-changelog, input-canonico, tap, requisitos, MANIFEST) |
| Handoffs | `.ai/handoffs/` | 58 | Handoff SDD | 56 (2 sem FM: INDEX, relatorio-analise-constituicao) |
| Personas | `.ai/personas/` | 7 | Personas L2 | 0 |
| MCP | `.ai/mcp/` | 2 | Inventário/ratificação | 0 |
| Agentes/registry | `.ai/agents/` + deprecated | 2 | Ledger/registry | 1 (ledger-deprecated-nota sem FM) |
| Skills OpenCode | `.agents/skills/` | 40 | Skills de terceiros (README, SECURITY, CLAUDE) | 26 (14 sem FM) |
| Raiz | raiz + `.planning` + `.recon` | 5 | Constituição, AGENTS, README, GRAPH_REPORT | 0 (5 sem FM: constitution, AGENTS, README, GRAPH_REPORT, recon/AGENTS) |
| **Total** | | **331** | | **292 com FM / 39 sem FM** |

**Exclusões deliberadas deste escopo:** `.opencode/` (skills instaladas do OpenCode, de terceiros, regidas por seus próprios mantenedores — 607 `.md` não contados), `graphify-out/` (grafo gerado automaticamente), `.git/`, `node_modules/`, `.venv/`, `.pytest_cache/`. Não-Markdown (`.docx`, `.pdf`, `.png`, `.svg`, `.drawio`) fica fora do escopo de frontmatter, conforme auditoria anterior.

---

## 3. Norma proposta (resumo — não aplicada ainda)

### 3.1 Frontmatter comum (todos os `*.md`)
```yaml
---
id: <slug-unico>
title: <título>
type: <classe-de-artefato>   # spec | adr | change-request | audit | test | handoff | persona | plano | procedimento | relatorio | requisito | metrica | evidencia | governanca | constituicao | readme | conhecimento | archive
version: <MAJOR.MINOR.PATCH>
status: <ativo | draft | ratificado | obsoleto | arquivado>
owner: <responsável>          # papel ou humano (sem nome civil)
derived-from:
  - <fonte canônica>
last-revised: <YYYY-MM-DD>
lgpd-class: <classe LGPD>     # n/a | interno | sensível
tags:
  - <tag>
---
```

### 3.2 Campos específicos por tipo de artefato
- **ADR:** `decision`, `status` (proposed | accepted | superseded | deprecated), `supersedes`, `consequences`, `domain-pmbok`
- **Change-Request:** `cr-number`, `impacto`, `prazo-analise-gp`, `decisao-ccb`, `instrumento`
- **Audit:** `audit-id`, `periodo`, `veredito`, `artigos-constitucionais`, `vio-referenciados`
- **Spec (SDD):** `spec-id`, `camada`, `estado-implementacao`, `rastreia-req`, `testes-vinculados`
- **Test:** `test-id`, `tipo` (unit | e2e), `spec-vinculada`, `cobertura`
- **Handoff:** `hf-id`, `sender`, `receiver`, `acao`, `dod`, `estado`
- **Persona:** `layer` (L1|L2|L3), `role`, `contrato-validado`
- **Plano/Procedimento:** `marco-vinculado`, `doD`, `revisao-periodica`
- **Constituição/AGENTS/README:** `hash-normativo` (quando aplicável), `co-assinatura`

### 3.3 Regras de governança
- Um tipo de artefato → um diretório canônico (mapeamento diretório → type).
- Alteração de tipo ou conteúdo normativo exige Change-Request + parecer de auditoria + ratificação CCB (Art. 9).
- Novo `.md` só entra com frontmatter completo, barrado por gate de CI (script de validação).
- Mensagem de commit padrão: `docs(norma): ...` ou `chore(docs): ...` conforme tipo.

---

## 4. Cálculo de esforço

Pressupostos: uma pessoa dedicada, familiarizada com o repositório; parte da adesão (frontmatter) automatizável por script, mas classificação de tipo/campos específicos exige revisão manual; revisão e ratificação humanas não comprimíveis.

| Fase | Atividade | Unidade | Qtd | Tempo/unidade | Subtotal (h) |
|------|-----------|---------|-----|---------------|--------------|
| F1 | Definição da meta-norma (regras, campos, mapeamento diretório→tipo, governança) | documento | 1 | 16 h | 16 |
| F2 | Criação dos 16 templates-padrão por tipo de artefato | template | 16 | 0,75 h | 12 |
| F3 | Registro do mapeamento diretório → type e regras de exceção | mapeamento | 1 | 4 h | 4 |
| F4 | Adesão dos 331 artefatos (classificar tipo, preencher/ajustar frontmatter específico, revisar) | artefato | 331 | 0,25–0,50 h | 83–165 (médio 124) |
| F5 | Revisão cruzada + parecer de auditoria + ratificação CCB | ciclo | 1 | 12 h | 12 |
| F6 | Script de validação de frontmatter/tipo para gate de CI + atualizar AGENTS.md e constitution.md | script + docs | 1 | 16 h | 16 |
| F7 | Treinamento/padrão de commit + divulgação ao roster de agentes | sessão | 1 | 6 h | 6 |
| **Total** | | | | | **150–260 h** |

**Total provável: 190 horas-homem** (≈ 24 pessoa-dia de 8 h; ≈ 24 story points se 1 SP = 8 h).  
Faixa: **150 h (mínimo, muita automação) a 260 h (máximo, revisão manual pesada + retrabalho de ADRs supersedidas).**

---

## 5. Cronograma indicativo (não vinculante)

| Semana | Atividade |
|--------|-----------|
| 1 | F1–F3 (norma + templates + mapeamento) |
| 2–3 | F4 (adesão dos 331 artefatos, por ondas de diretório) |
| 4 | F5–F7 (revisão, auditoria, CI gate, divulgação) |

---

## 6. Riscos e pressupostos

- `.agents/skills/` são skills de terceiros do OpenCode: incluídos na contagem por conservadorismo, mas podem ser excluídos do escopo da norma do projeto (reduz ~14 h).
- A adesão manual a 331 artefatos é o maior fator de variância; um script de preenchimento de frontmatter comum reduz F4 para ~0,25 h/artefato.
- Qualquer aplicação real exige Change-Request (label `change-request`) + parecer de auditoria + ratificação humana CCB (Constituição Art. 9.3), não coberta neste cálculo de esforço de definição.
- Não há impacto em código-fonte, testes, CI ou dados nesta fase (apenas documentação).

---

## 7. Recomendação

Aprovar a definição da norma (F1–F3) como Change-Request separada, e adiar a adesão em massa (F4) para a próxima milestra, após ratificação do CCB e definição do script de validação de gate de CI. **Nenhum `..md` foi alterado por esta estimativa.**

---