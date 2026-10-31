---
id: ccb-log
title: Registro Vivo de Decisões do Ciclo de Vida de Mudanças (CCB-LOG-NNN) — append-only
version: 0.1.0
date: 2026-10-30
owner: CCB (Leonardo David Silva Setti, membro único — TAP v3 §1.c)
derived-from:
  - .ai/agents/ledger.yaml
  - docs/governanca/plano-consolidacao-estrutural.md
  - docs/auditorias/vio-register.md
  - .opencode/opencode.json
class: register-decision
status: active
audit-hook: docs/auditorias/ (AUD-* recorrentes referenciam este registro por CCB-LOG-NNN)
---

# CCB-LOG — Registro Vivo do Change Advisory Board (modelo CAB vivo, ITIL 4)

> Propósito: registro vivo do Change Advisory Board (modelo CAB, ITIL 4) com
> gate arquitetural TOGAF ADM e ciclo de vida PMBOK 7 — complementar às
> auditorias recorrentes em docs/auditorias/ e ao vio-register.md.
> Anchors constitucionais: Art. 2 hierarquia normativa; Art. 5 ratificação humana.

## Formato de entrada (imutável — addenda only)

```
─────────────────────────────────────────────
CCB-LOG-AAAA-MM-DD-NNN | data: AAAA-MM-DD
contexto: ...
opções avaliadas: [A|B|C] — trade-offs
decisão: ...
ratificação: humana | agent-digital-security interino
evidência: hashes, line-range, mtime, commit
impacto: [monograma de alto nível]
rollback: git <op> | pl assumado
pmbok-gate: PIE/π | togaf-gate: ADM fase | itil-gate: SEV/normal
─────────────────────────────────────────────
```

## Entradas — 2026-10-30 (sessão de desbloat/consolidação TA-9001)

### CCB-LOG-2026-10-30-A01 — Higiene de raiz (racionalizado por YAGNI)
contexto: dumps acidentais na raiz (16MB PS + 112KB ls-dump) versionados
acidentalmente violam Política de Dependência Simples (Art. §0.4 40%).
opções: [A] descartar + gitignore preventivo | [B] versionar dumps | [C] mover
decisão: **A**. Nenhum consumidor no DAG (prova: grep sem referências).
ratificação: Leonardo (mandato anti-bloat mensagem 4, em sintonia com hígiene).
evidência: `argparse` (32 MB PostScript), `lst.txt` (112KB eza dump).
rollback: `git show <commit> -- argparse` reconstrói descarte.
pmbok: R24 (qualidade): togaf: ADM-I/migración: itil: normal+standard.

### CCB-LOG-2026-10-30-A02 — Consolidação de legados em archive
contexto: `Docs/Monografia` (33 arq.) espalhados em raiz e COGME/ aninhado Next.js
pré-ADR-001 são bloat pending das ondas.
opções: [A] unificar em `docs/archive/apocrifo/` | [B] deletar tudo | [C] manter casca
decisão: **A** — por similaridade; single-source mídia binária; legado 100%
recuperável (git history) justifica deleção worktree. Divergência de conteúdo
arquivado validada: única variação vs. HEAD é correção normativa ADR-008 (Carletto→Carleto).
ratificação: Leonardo (mandato anti-bloat).
evidência: diff byte-range registrado no plano-consolidacao-estrutural §2.
rollback: `git revert 608c299`.
pmbok: punch-list A11 | togaf: ADM-H/Transition | itil: normal change.

### CCB-LOG-2026-10-30-A03 — Sanitização de segredo concreto
contexto: token literal no config versionado (LGPD/foresh: responsabilidade de bypass)
opções: [A] placeholder 12-factor | [B] gitignore do arquivo | [C] ignorar
decisão: **A** `token: "${COGME_SANDBOX_TOKEN}"` + gitignore preventivo.
ratificação: humana (recomendada via NEXUS). atinge SP-01 (segurança).
evidência: config/environment.yaml:5-7.
rollback: git revert higiene.
pmbok: R24 | togaf: Security Architecture | itil: standard.

### CCB-LOG-2026-10-30-A04 — Pendências aguardando co-assinatura (AGENDA)

| ID | Item | Ação | Bloqueia ratificação |
|-----|------|-----------------------|--------------|
| P01 | constitution.md v1.2.0 E-09..E-19 (~~VIGENTE-INTERINA~~) | ✅ **CLOSED 30/10** — A05: PLENA, co-assinatura expressa, commit `7cff886` | LEI SUPREMA (resolvido) |
| P02 | `.ai/personas/_base.md` trim 68→11 (delta perdido em I01) | re-aplicar se ratificado | personas |
| P03 | `.opencode/opencode.json` budget+deny-list | revisão SP-01 | Modelo runtime |
| P04 | Normalização nomenclatura/estrutura (proposta §4 plano) | onda pós-P01 | SSOT qualquer |

### CCB-LOG-2026-10-30-A05 — RATIFICAÇÃO + PROMULGAÇÃO da Constituição v1.2.0 (fechamento P01)
contexto: constitution.md v1.2.0 (emendas E-09..E-19) aguardava co-assinatura humana (Art. 5.4) — pêndulo VIGENTE-INTERINA desde 29/10.
opções: [A] co-assinatura expressa e promulgação | [B] revisar por rodada dedicada | [C] reverter emenda
decisão: **A** — prompt expresso do CCB (membro único) de 30/10/2026: "Aplique co-assinatura, ratifique e promulgue". Status → VIGENTE-PLENA.
evidência: SHA-256 normativo `b3f296c6…1851db4`; commit de conteúdo `7cff886`; bloco de co-assinatura fechado ao pé (derivado, não-normativo).
impacto: lei supma revalidada; P01 CLOSED; habilita P04 (normalização estrutural) como próxima onda.
rollback: `git revert <fechamento>` (mantém histórico de explicação em vio-register).
pmbok-gate: Área de Conformidade | togaf-gate: ADM — Architecture Board Ratification | itil-gate: change record closed.

### I01 — Incidente de processo (auto-registro NEXUS, transparência auditável nº. 2026-10-30-I01)
fluxo: `git checkout -- .ai` executado antes do commit de higiene reverteu deltas
não-comitados de sessões anteriores (personas/_base.md trim 68→11; all.md; tester.md;
kb-taxonomy.md; sdd-cycle.sh). Persona-trim delta NÃO RECUPERÁVEL (não versionado).
Reversão = estado comitado (versão longa, fontem консcripta).
Mitigação de recorrência: proibição de `git checkout -- <dir>` em sessões GT
(governança de trabalho); usar `git stash push -p` ou duplicar delta em
/tmp/opencode/ antes de descartar qualquer divergência de worktree.
lobby: LGPD inaplicável (sem PII state); risco arquitetural baixo—alto.
pmbok: LIA (logical artifacts) | togaf: Architecture Governance | itil: incident (P3).

### CCB-LOG-2026-10-30-A06 — Ratificação e promulgação do OKB v5.1.0 (documento de conhecimento canônico)
contexto: OKB vivo em v3.0 (20/09/2026) com metadados divergentes do índice (declarava 4.0.0),
catálogo de apenas 4 das 12 ADRs emitidas e hierarquia invertida contra o Art. 2.
opções: [A] ratificar v5.1.0 como corpus único | [B] manter v3.0 e corrigir só o índice | [C] adiar para a onda de normalização
decisão: **A** — v5.0.0-draft submetido a análise YAGNI / PMBOK 7ª / TOGAF ADM / ITIL 4, emendado
para v5.1.0 (nova §9 de cobertura metodológica, achados C-22..C-25, poda YAGNI) e ratificado.
ratificação: humana (prompt expresso do CCB, 30/10/2026 — instrumento CCB-003).
evidência: SHA-256 normativo `78c1f270d0a913be54284d63b8d4bd149ac033bf93808d61761dfadf1fe4bcdd`;
v3.0 arquivado em `docs/archive/legacy-md-artifact/OKB_COGME_v3.0.md` (git mv + proveniência);
KB-INDEX 1.1.0 → 1.2.0 (OKB-001 = 5.1.0 ratified).
impacto: corpus único; +§9 cobertura metodológica (8 domínios PMBOK, 10 fases ADM + requisitos, 11 práticas ITIL);
nenhuma alteração de Constituição, TAP congelado (ADR-005) ou ADRs.
rollback: `git revert <commit>` e `git mv` do arquivo arquivado de volta ao path vivo.
pmbok-gate: Trabalho do Projeto + Medição | togaf-gate: ADM-G/H (repositório e governança de arquitetura) | itil-gate: change record closed (normal)

### CCB-LOG-2026-10-30-A07 — Ratificação da normalização do .gitignore (CCB-004)
contexto: o .gitignore não reconhecia o ambiente Python. venv/, .venv/ e .pytest_cache/
apareciam como ignorados apenas por arquivos .gitignore internos gerados pelas ferramentas
(conteúdo: "*"); com a remoção desses arquivos, 25.796 entradas entrariam no índice de uma vez.
Diagnóstico completo em GITIGNORE-DIAGNOSTIC.md (fora do repo, snapshot COGME-20261030T162922).
opções: [A] 7 lacunas + remover guardas SDD órfãs | [B] manter e apenas documentar | [C] normalização mínima (só venv)
decisão: **A**, com três decisões do GP sobre os itens controversos:
  C.1 = (b) manter *.tmp.md ignorado; o consolidado de ADRs permanece artefato local, nunca versionado;
  C.2 = (b) remover as guardas SDD órfãs (nenhum dos alvos existe no repositório) por YAGNI;
  C.3 = (b) versionar nexus/data/persistent_storage.db (entra na rodada de commit do runtime nexus).
ratificação: humana (prompt expresso do CCB, 30/10/2026 — instrumento CCB-004).
evidência: .gitignore SHA-256 `f5375db809e7b4dc7a25f635025f231b5a8155a35ea322374fc1a0691f0602d3`;
`git add -A --dry-run` = 41 entradas (antes: 25.796 em risco); `git ls-files -ci` = 25, todos .pyc.
DEFEITO ENCONTRADO NA APLICAÇÃO (não estava no diagnóstico): a regra `models/` (restaurada em 26/10
por VIO-012) não era ancorada e mascarava o pacote Python `src/backend/models/` — qualquer arquivo
novo ali nascia invisível ao git status. Corrigido para `/models/` (ancorada na raiz). Sem evidência
de perda: o diretório não recebe arquivo desde 22/10, anterior à regra.
impacto: índice protegido contra 25.796 entradas acidentais; bytecode sai do controle de versão;
pacote src/backend/models/ deixa de ser armadilha; 5 regras mortas removidas.
rollback: `git checkout HEAD -- .gitignore` (o arquivo é versionado e a mudança é atômica).
risco residual declarado: `**/sdd/credentials.json` deixou de existir como guarda; compensada pela
guarda genérica `**/credentials.json`. Permanecem como guardas mortas (fora do escopo desta pergunta)
`**/docs/intermediate/` e `**/docs/legacy/`.
pmbok-gate: Trabalho do Projeto (qualidade do artefato de configuração) | togaf-gate: ADM-Preliminar (princípios de repositório) | itil-gate: change record closed (normal)
