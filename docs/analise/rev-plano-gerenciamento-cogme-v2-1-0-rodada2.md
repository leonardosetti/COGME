---
id: docs-analise-rev-plano-gerenciamento-cogme-v2-1-0-rodada2
title: REV-PLANO-GER-002 — Rodada 2 de revisão do Plano de Gerenciamento v2.1.0
type: relatorio
version: 1.0.0
status: ativo
owner: nexus-prime-ultimate
derived-from:
- docs/analise/rev-plano-gerenciamento-cogme-v2-1-0-rodada2.md (normalizado em 2026-11-05)
last-revised: '2026-11-02'
lgpd-class: n/a
tags:
- analise
- docs
- normalizado
---

# REV-PLANO-GER-002 — Rodada 2 de revisão do Plano de Gerenciamento v2.1.0

**Sujeito:** `docs/planos/plano-de-gerenciamento-cogme-v2-1-0.md` (2370 linhas)
**Método:** leitura integral (2 blocos), cruzamento contra o repositório de conhecimento vivo e verificação direta dos achados de maior severidade.
**Critério de relevância (metadados):** apenas fontes com status `active/ratified/promulgado` em `KB-INDEX.md`/frontmatter; `docs/archive/` (imutável) e `docs/conhecimento/drafts/` (não promulgado) excluídos como autoridade — exceto para sinalizar citação a rascunho.
**Total: 64 achados — 18 ALTA, 33 MÉDIA, 13 BAIXA.**

---

## G1 — Estrutura e numeração do documento

| ID | Sev | Linha(s) | Achado | Evidência |
|---|---|---|---|---|
| P-01 | ALTA ✓ | 688–774 vs 776–879 | Seção 4 com dois blocos concorrentes e dois esquemas de numeração; `4.6`, `4.9`, `4.11` duplicados; `4.5.1` duplicado (611/650) | 688 `## 4.6 Controle do Cronograma` × 776 `## 4.6 Desenvolvimento do Cronograma`; 703 × 856; 740 × 881; 757 × 873 |
| P-02 | ALTA ✓ | 2098 / 2126 | `9.4` duplicado em níveis diferentes | 2098 `### 9.4 Riscos Comuns` × 2126 `## 9.4 Oportunidades` |
| P-03 | ALTA ✓ | 1109–1115, 1522–1530 | Tabelas de rastreabilidade de §5 e §6 numeram seções `4.x`/`5.x` (numeração legada dos planos satélite) — apontam para seções inexistentes no consolidado | `## 5.9 Declaração de Rastreabilidade` lista `4.1…4.8`; `## 6.10` lista `5.1…5.9` |
| P-04 | MÉDIA ~ | 119/467/600, 179/482/797, 613, 742/858 | IDs de figura/tabela duplicados e fora de ordem: 3× `[FIG-1]`, 3× `[FIG-2]`; `[TABELA 40]` antes de `[TABELA 3]`; TABELA 42 ≡ TABELA 4 com conteúdo divergente | — |
| P-05 | MÉDIA ✓ | 883–889 vs 2361–2365 | Duas tabelas de controle de versão contraditórias (datas 1.0 distintas); histórico por seção pula v2.0 e datas de "1.1" divergem (25/10 × 31/10) | 885 `1.0 \| 21/09/2026` × 2363 `1.0 \| 31/10/2026` |
| P-06 | MÉDIA ~ | 1762, 2004, 2209, 2266 | §7–§10 sem os blocos obrigatórios (Rastreabilidade / Premissas / Notas de Contexto / Controle de Versões) adotados por §2–§6 — padrão documental autoimposto quebrado | — |
| P-07 | BAIXA ~ | 16–26, 2359 | Âncoras do SUMÁRIO com slug incorreto (falta 1 hífen) e "CONTROLE DE VERSÕES — PLANO GERAL" fora do sumário | — |

## G2 — Estado de governança × canon (versões, status, registros)

| ID | Sev | Linha(s) | Achado | Evidência (canon) |
|---|---|---|---|---|
| P-08 | ALTA ✓ | 44, 66–78, 2328 (15×) | Constitution citada como `v1.2.0`; vigente é `1.2.1` | `constitution.md:7` `Versão: 1.2.1 — VIGENTE-PLENA` (0 ocorrências de "1.2.1" no plano) |
| P-09 | ALTA ✓ | 44, 2096, 2317, 2330–2336 (7×) | `OKB v5.1.0` — duas versões defasadas | `KB-INDEX.md:55` = 5.2.0; frontmatter do `OKB.md` em voo = 5.3.0 |
| P-10 | ALTA ✓ | 2284–2296 | 11 dos 13 caminhos de ADR do Apêndice A não existem | no repo: `ADR-001-stack.md`, `ADR-002-kanban.md`…; só `ADR-008.md`/`ADR-009.md` resolvem |
| P-11 | ALTA ✓ | 2288, 2293, 2296 | Status de ADRs invertidos em relação ao registro canônico | `ADR-LOG.md:53` ADR-005 **Vigente (incorpora ADR-013 e ADR-015)**; `:61` ADR-013 **Supersedida**; `:58` ADR-010 **Supersedida por ADR-001** — plano diz o inverso nos três |
| P-12 | ALTA ✓ | 2278, 2289–2296 | ADR-014 e ADR-015 (ratificadas) com **0** citações; Apêndice A "001–013"; títulos errados de ADR-006/007 | `KB-INDEX.md:49-50`; `ADR-LOG.md:62-63` |
| P-13 | ALTA ✓ | 2315, 2349 | CR-001 declarada `Pendente` | `CR-001…md:7` "aprovado por manifestação do CCB" + `ADR-015…md:6` `status: ratified` |
| P-14 | ALTA ✓ | 2305–2307 | Delta Log (TABELA 37) registra só REQ-07 e omite a emenda do Marco M2 | `docs/tap/delta-v3-1.md:10` (30/09/2026 → 15/11/2026, CR-001 + ADR-015) |
| P-15 | ALTA ✓ | 222, 620, 788, 1997, 2153 | M2 segue `30/09/2026` e Q-01 ainda manda "abrir Issue change-request" — emenda já ratificada | `delta-v3.1.md:10`; `ADR-015` ratified 31/10/2026 |
| P-16 | ALTA ✓ | 562, 705, 795, 821, 854 (9×) | "Regime de freeze … nenhuma revisão do TAP é prevista" | `ADR-005-regime-tap.md:6` `Status: Ratificado` (v1.1.0, baseline vivo) + `delta-v3.1.md` com 2 emendas aplicadas |
| P-17 | ALTA ✓ | 213 | Hierarquia de autoridade `TAP > OKB > Glossário > ADRs` é a ordem **expressamente revogada** | `OKB.md:156` ("ordem praticada até o OKB v3.0 está revogada"); `constitution.md:43-48` (ADRs 3ª, Glossário 6ª) |
| P-18 | MÉDIA ✓ | 88–94 vs 126–132 | "Hierarquia de Resolução de Conflitos" sem nenhuma camada do canon (Constituição/TAP/ADRs/OKB) e as duas cópias divergem entre si | `constitution.md:41-50` (ordem absoluta de 8 níveis); `constitution.md:78` ("resolve-se de cima para baixo") |
| P-19 | MÉDIA ✓ | 42, 2355 | Autodeclaração de "artefato canônico único de governança" | `constitution.md:47` — planos são camada 5, subordinados a Constituição/TAP/ADRs/OKB |
| P-20 | ALTA ✓ | 2355 | Plano **não registrado** no KB-INDEX (0 ocorrências) — pela regra do próprio índice é "fora do canon vivo" | `KB-INDEX.md:26` |
| P-21 | MÉDIA ✓ | 447, 2094, 2254, 2332, 2335 | ADR-010 citada como norma vigente (stack, cache, pipeline) | `ADR-010-Stack-Infraestrutura.md:8` `Supersedida por ADR-001 v1.1.0` |
| P-22 | MÉDIA ✓ | 1249–1272, 2335 | CI-CD-GOV-001 e DEVSECOPS-001 com 0 citações; resumo do `ci.yml` embutido não reflete o job `kill-switch-check` real | `ccb-log.md:55-56` (promulgados RAT A10); `.github/workflows/ci.yml:17` |
| P-23 | MÉDIA ✓ | 2085 | RE-08 dimensiona "25 agentes" | `registry.yaml` 46 `status:` / `ccb-log.md:48` "46 promulgados" |
| P-24 | MÉDIA ~ | global | 0 referências a KB-INDEX, ccb-log, ADR-LOG, registry.yaml, vio-register — governança citada só genericamente | — |
| P-25 | MÉDIA ~ | 10 | Origem declara PED-003 como fonte consolidada | `ccb-log.md:42-44` — A-008/PED-003 é rascunho **não promulgado** |

## G3 — Contradições factuais internas

| ID | Sev | Linha(s) | Achado |
|---|---|---|---|
| P-26 | ALTA ~ | 635, 671, 681 | Três definições conflitantes de caminho crítico; `N4` não existe; `N3 → N3` |
| P-27 | ALTA ~ | 616–624 | Tabela de precedência viola finish-to-start: M1 com duração `0 dias` abrange 21 dias; N1 começa antes de terminar M1 |
| P-28 | ALTA ~ | 620, 626, 667 | Slack `25 dias (esgotados)` × `slack de 16 dias entre B1 e B2`; entidades B1/B2 inexistentes no repo; "esgotado" + "Crítico? Não" |
| P-29 | MÉDIA ~ | 657–665 | `106 dias úteis` somados como `106 dias corridos` (01/09→15/12 = 106 corridos) |
| P-30 | MÉDIA ✓ | 1831, 1988, 2153 | Coluna `In review` inexistente (ADR-002: `Code Review`); WIP `2/5` e `In progress 0/3` × limite de 3 cartões/pessoa (linha 84) |
| P-31 | MÉDIA ✓ | 1830, 1989, 1996 | `14 cards concluídos` × `Done 15` na mesma seção |
| P-32 | MÉDIA ✓ | 1369 vs 1971 | Meta de daily `100%` × `≥ 80% dos dias úteis` |
| P-33 | MÉDIA ✓ | 2196 | Placeholder aberto em risco do Top 10: `[A CONFIRMAR coverage atual]` |
| P-34 | MÉDIA ✓ | 2002 | Nota editorial em baseline: "Antes de submeter, refazer esta tabela…" |
| P-35 | MÉDIA ✓ | 365, 546, 1117 | Auto-certificação "Verificação: 100% das seções" falsa (tabelas incompletas; refs §1.x e OKB quebradas) |
| P-36 | MÉDIA ~ | 423 vs 829 | ADR-001 simultaneamente "consolidada e ratifieda" e "em avaliação" |
| P-37 | MÉDIA ~ | 1040, 1052 | GitHub Actions marcado ✅ com licença proprietária × critério "100% OSI-approved" |
| P-38 | MÉDIA ~ | 1018, 1049, 2119, 2120 | Deriva SQLite × PostgreSQL: whitelist e RE-11 tratam migração como "futuro" × REQ-07 (emendada para PostgreSQL 15+) |
| P-39 | MÉDIA ~ | 1758 | Frontend `HTML5/CSS3/JS vanilla` × `HTMX + Tailwind` em `plano-recursos.md:182` |
| P-40 | MÉDIA ~ | 2085–2122 | Riscos divergem de `plano-riscos.md` (RE-01, RE-09, RC-07/RC-09); `RC-01` duplicado com redação diferente (2093/2105) |
| P-41 | MÉDIA ~ | 1625 vs 2345 | Baseline "seed simulado" × "0 B (não calibrada)" |
| P-42 | MÉDIA ~ | 221–222 | M2 (30/09) declarado "redigido após a calibração 23/09–03/10" — impossível cronologicamente |
| P-43 | MÉDIA ~ | 505, 521 | Critério de fracasso de escopo mistura cards × pacotes EAP e dispara estruturalmente ao M2 |
| P-44 | BAIXA ~ | 299–300, 505, 509, 766, 1194 | SLA de mudança 48h × 48h+24h; faixa `4 < h < 6` sem regra; Technical Debt Ratio com denominador R$ 0,00 |

## G4 — Referências e caminhos quebrados

| ID | Sev | Linha(s) | Achado | Canon |
|---|---|---|---|---|
| P-45 | MÉDIA ✓ | 469, 484, 602, 639, 675, 799 (6×) | `docs/diagrams/` não existe | real: `docs/diagramas/` |
| P-46 | MÉDIA ✓ | 1294–1415 (12×) | `MF1.md`/`MF2.md`/`MF3.md` inexistentes | real: `MF1-licoes.md`… (`ADR-011:57`) |
| P-47 | ALTA ~ | 1428, 1444, 1460 | Imagens Ishikawa com path `../../../` que sai do repo; FIG-5 (Cycle Time) usa a imagem da FIG-3 | `docs/diagramas/qualidade/[legacy]-fig-05/06/07…` |
| P-48 | MÉDIA ✓ | 499, 539, 591, 750, 755, 871 | Citações OKB desalinhadas: `§9.3` "Padrões A/B" (real: ITIL 4), `§10.3` não existe, `§9.2` "milestones" (real: TOGAF) | `OKB.md:650` |
| P-49 | MÉDIA ~ | 690–755, 1122–1138, 1730, 1750, 2109 | Refs internas quebradas: Integração §1.6.1/§1.7.3/§1.9/§1.4 (blocos duplicados apontam §2.7.1/§2.8.3/§2.10); `§11.6` para script; `7.8.1.0`; "Q-02 no 9.8"; "Plano 2.7"; §4.4/§4.5 de custos |
| P-50 | MÉDIA ~ | 376–377, 435 vs 725, 841 | Cita subnumeração do TAP (`§8.1/§8.2/§8.4`) que as próprias NC proíbe presumir; `docs/tap/tap.md` tem 0 B — `TAP §x` não verificável; `§1.c` × `§1.b` divergem do plano-integral |
| P-51 | MÉDIA ~ | 403, 419 | `docs/requisitos/requisitos.md` prometido em M2 e com 0 B |

## G5 — Metadados, registro e relevância

| ID | Sev | Linha(s) | Achado | Evidência |
|---|---|---|---|---|
| P-52 | ALTA ✓ | 1–12 | Frontmatter não obedece `KB-TAX-001`: bloco não-YAML e sem os 10 campos obrigatórios (`id/title/version/class/status/owner/derived-from/last-revised/lgpd-class/caveats`); `Status: Draft` convive com claim de canonicidade | `.ai/specs/kb-taxonomy.md:24,43` |
| P-53 | MÉDIA ✓ | — | Estado **não commitado** em voo altera a relevância das fontes: `OKB.md` bump parcial 5.2.0→5.3.0 só no frontmatter (título/corpo 5.2.0); `KB-INDEX` +ADR-014/015; `constitution.md` +Art. 2.4.1 (máx. 10 ADRs ativas); `registry.yaml` downstream alterado; **`ledger.yaml` reduzido de 78→8 linhas** (trilha de auditoria removida, não commitada) | `git diff` |
| P-54 | MÉDIA ✓ | — | `docs/auditorias/aud-2610-03-resultados.md` (untracked) contém alegações falsas ("registry.yaml não encontrado", "OKB/KB-INDEX não encontrados", "plano desatualizado v2.1.0") — contamina o corpus | arquivo em `git status ??` |
| P-55 | BAIXA ✓ | 2319 | Alega carimbo `derived-as-of: 2026-11-02` no OKB — campo inexistente no artefato | `OKB.md` frontmatter |

## G6 — Gaps (PMBOK/ABNT e declarados)

| ID | Sev | Linha(s) | Achado |
|---|---|---|---|
| P-56 | MÉDIA ~ | 2348 | Matriz de partes interessadas "Não registrada" — lacuna do domínio Stakeholders sem mitigação registrada (OKB-C-24) |
| P-57 | MÉDIA ~ | — | Sem dicionário da EAP; `docs/planos/referencias.md` nunca citado; PMBOK sem edição/ISBN — referências ABNT ausentes |
| P-58 | MÉDIA ~ | 90–94, 126–132, 148–154 | Teste GMV com 3 perguntas × 4 canônicas; hierarquia de conflitos com 5 itens × 6 + Adendo 48h do glossário |
| P-59 | BAIXA ~ | 1908, 1929, 1950 | UAT sem data definitiva; coverage não instrumentado |

## G7 — Ontologia: termos, IDs e namespaces

| ID | Sev | Linha(s) | Achado |
|---|---|---|---|
| P-60 | ALTA ~ | 619–623 vs 405, 415, 461 | IDs `N1/N2/N3` colidem: macro-fases da tabela de precedência × fases da EAP (`N2`=Desenvolvimento × `N5`=Desenvolvimento; `N3`=Consolidação × `N3`=Modelagem) |
| P-61 | MÉDIA ~ | 66–78, 213, 550 | Namespace `P#`: `P3`/`P8` do plano ≠ `P3`/`P8` do glossário; regra cita "P1–P9" existindo P1–P13 |
| P-62 | MÉDIA ✓ | 257 | "Cycle Time: In Progress → Done" × glossário "To Do → Done" |
| P-63 | MÉDIA ~ | 447, 734, 850, 1507, 1516 | "Cache PostgreSQL" × glossário `Cache = Redis`; saneamento "Carleto" é no-op (origem = destino) |
| P-64 | MÉDIA ~ | 2288–2296 | Colisão de ID ADR-013 (OKB-C-26) e IDs duplicados ADR-005/006 no repo não são mencionados — Apêndice A trata cada ID como entidade única |

## G8 — Estado do repositório (contexto do gate)

- `scripts/sync_agent_registry.py --check` → **em sincronia** ✓
- `scripts/validate_nexus_yaml.py` → **0 errors, 46 promulgados** ✓
- Frontmatters de `KB-INDEX.md`, `OKB.md`, `registry.yaml` → **parseiam** ✓ (o do plano, não: P-52)
- Alterações **não commitadas** que condicionam o gate: `constitution.md` (+Art. 2.4.1 — máximo de 10 ADRs ativas), `.ai/agents/registry.yaml`, `.ai/agents/ledger.yaml` (−78 linhas), `docs/conhecimento/okb.md` (bump parcial), `KB-INDEX.md` (+ADR-014/015), `scripts/validate_nexus_yaml.py`, `docs/auditorias/vio-register.md`, 4 agent files, `constitution.md`.

## Verificado e LIMPO

1. Aritmética de custos: Tabela 12 fecha em `R$ 0,00`, idêntica a `plano-custos.md`.
2. Matriz P×I, severidade e ranking de riscos batem célula a célula com `plano-riscos.md`.
3. Esforço (89 h / 21 cards), 60 h/semana, reunião de 50 min — aritmética correta.
4. Datas M1–M4 e MF1–MF3 coerentes internamente (a única fissura é a emenda M2, P-15).
5. EAP "12 fases / 37 pacotes" coerente com ADR-009 e glossário v3.2.0 (a contagem 13/48 é tratada como legado).
6. Lista Must de requisitos idêntica a `plano-escopo.md:57`; whitelist de dependências idêntica a `plano-custos.md`.
7. Métricas oficiais (Cycle ≤ 3 d, Throughput ≥ 5, WIP ≤ 9), tasklist ≥ 6 h e rituais conferem com ADR-002/003/004.
8. Papéis GP/CCB único conferem com `constitution.md` Art. 5.1 e glossário.
9. Somas de riscos, faixas de severidade e datas de marcos (fora M2) conferem com `plano-cronograma.md`.
10. Roster e topologia: sync e validação de YAML verdes.

## Decisões solicitadas ao gate humano

1. **G-1** Autorizar exclusão do bloco duplicado da Seção 4 (688–774) e renumeração canônica — ou manter como "notas de contexto" com rótulo explícito?
2. **G-2** Prazo de rebase do M2: propagar `15/11/2026` (ADR-015) em §2.5, §4, §8.5.4, §9/Q-01, ou preservar 30/09 como "linha de base original" com coluna de desvio?
3. **G-3** Registro do plano no KB-INDEX (entrada + bump do índice) é pré-condição de publicação — quem é o custódio de registro?
4. **G-4** Resolver antes de ajustar: OKB 5.2.0 × 5.3.0 (bump parcial não commitado), Constitution 1.2.0 × 1.2.1, colisão ADR-013, IDs duplicados ADR-005/006 — definir "versão canônica de referência" por artefato.
5. **G-5** Apêndice A: reescrever com os 15 ADRs e caminhos reais, ou reduzir a pointer para `ADR-LOG.md` (1 fato = 1 local)?
6. **G-6** Tratamento de `AUD-2610-03-RESULTADOS.md` (achados falsos): corrigir, reemeter ou arquivar?
7. **G-7** Escopo do ajuste: só ALTA (18), ALTA+MÉDIA (51) ou todos (64)?
