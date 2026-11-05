---
id: docs-decisoes-adr-015-emenda-marco-m2
title: 'ADR-015 — Emenda de Marco: Repactuação Temporal do M2 (Regime ADR-013-a)'
type: adr
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-015-emenda-marco-m2.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- adequado-a-norma
---
---
id: decisoes-adr-015-emenda-marco-m2
title: ADR-015 — Emenda de Marco: Repactuação Temporal do M2 (Regime ADR-013-a)
version: 1.0.0
class: decisao-adr
status: ratificado
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-015-emenda-marco-m2.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- normalizado
- self-updated
data-decisao: '31/10/2026'
data-formalizacao: '31/10/2026'
decisor: GP Leonardo (CCB único)
instrumento-ccb: RAT-2026-10-31-A12
gatilhos: n/a (instrumento próprio)
rastreabilidade: TAP §6 (Marcos); EAP N9.1; REQ-12; ADRs correlatas: ADR-005 (regime de emenda controlada), ADR-013 (absorvida por ADR-005); CR-001 (replanejamento M2)
dominio-pmbok: Cronograma + Integração
processo-pmbok-6: 4.6, 6.6
kill-switch: screened
---

# ADR-015 — Emenda de Marco: Repactuação Temporal do M2 (Regime ADR-013-a)

## Contexto

1. **Marco afetado:** M2 — data original no TAP §6 (18/09/2026, congelado): **30/09/2026**.
2. **Desvio constatado:** atraso de aproximadamente 25 dias úteis (superior ao gatilho de escalonamento de 3 dias úteis do Plano de Cronograma §1.8), documentado em `docs/change-requests/cr-001-m2-replanejamento.md`.
3. **Causa raiz (CR-001):** overengineering de governança, atraso na materialização técnica, ausência de pipeline e de código de produto.
4. **Impacto:** risco crítico ao marco M3 (15/11/2026) — MVP funcional.
5. **Ação corretiva já aprovada verbalmente pelo CCB (CR-001):** nova data-alvo 15/11/2026; congelamento de novas ondas de agentes até M3; foco de 80% da capacidade em código e infraestrutura — pendente de registro formal em Issue GitHub quando o repositório remoto estiver acessível.
6. **Regime aplicável:** ADR-013-a — Regime de Emenda Controlada do TAP: o núcleo blindado (incluído §6 Marcos como texto autorizativo) permanece intacto; a emenda materializa-se via **Delta Log** (`docs/tap/delta-v3-1.md`) + ADR (presente documento) + Nota de Contexto (NC-07) no plano. *Ratificação retrospectiva:* a ação corretiva verbal do CR-001 é formalizada retroativamente por este ADR, eliminando o desvio de formalidade registral.

## Decisão

1. **Repactuação temporal operacional de M2:** data-alvo 30/09/2026 → **15/11/2026** (data declarada em CR-001), registrada no Delta Log. A **data do núcleo do TAP §6 (30/09/2026) permanece inalterada textualmente** — o desvio é tratado como leitura operacional, jamais como correção do TAP (NC-00; ADR-005 §llocus de contexto mantido).
2. **M3 mantido em 15/11/2026** — nenhuma renumeração de marcos é executada (respeita o mapeamento canônico macro-fase/marco do TAP §6 e a MF2 vigente 01/10–15/11).
3. **Ressalva aberta C-06b (não resolvida por este ADR):** a repactuação de M2 faz **M2 e M3 colidirem na mesma data (15/11/2026)**. O CCB declara-se ciente e **delibera tratar a colisão em decisão futura e específica** — opções em análise: fusão M2+M3 (checkpoint único), deslocamento de M3 restrito ao prazo acadêmico de M4 (15/12/2026), ou manutenção com M2 de natureza documental e M3 de natureza produto. Até deliberação, ambos os marcos subsistem com critérios de aceite próprios e independentes (Tabela 4 do Plano de Cronograma). **A colisão não bloqueia a execução da ação corretiva do CR-001.**
4. **Ação corretiva vinculante (CR-001):** congelamento de novas ondas de agentes até M3; redirecionamento de 80% da capacidade da equipe para código e infraestrutura. Esta ADR **ratifica e vincula** a resolução; o descumprimento é desvio reportável ao auditor (Art. 8 da Constituição).
5. **Delta Log:** é criado `docs/tap/delta-v3-1.md` (mecanismo da ADR-013, até agora ausente no repositório), com a emenda de M2 e a historiada emenda REQ-07 (SQLite → PostgreSQL 15+, ADR-010).
6. **Nota de Contexto:** incorporada **NC-07** ao Plano (Base) de Cronograma no plano-integral, registrando a leitura operacional da repactuação sem tocar a reprodução do TAP.
7. **Obrigações acessórias:** registro da repactuação em Issue GitHub (label `change-request`, milestone M2) quando o repositório remoto estiver acessível; comunicação no fechamento do marco subsequente (exigência já vigente do Plano de Cronograma §5); propagação no OKB (§3.2 marcos, §4 catálogo) no próximo ciclo de versionamento.

## Mecanismo de Emenda (execução)

| Campo Alterado | Valor Anterior | Valor Novo | Justificativa (ADR/CR) | Data |
|---|---|---|---|---|
| Marco M2 — data-alvo (TAP §6) | 30/09/2026 | 15/11/2026 | CR-001 (atraso ~25 dias, risco crítico ao M3) ratificada como ADR-015 | 2026-10-31 |
| REQ-07 — Cache de cotações | SQLite | PostgreSQL 15+ | Alinhamento à ADR-010 (Stack Infra) | 2026-11-01 *(historizado de ADR-010)* |

Registros no `docs/tap/delta-v3-1.md` são append-only; emendas adicionais exigem CR + ADR (rodízio ADR-013-a).

## Consequências

- **Ganho:** realinhamento da baseline temporal ao estado real do projeto; flexibility documental auditável (Delta Log); formalização da ação corretiva que direciona capacidade ao caminho crítico (pipeline + código de produto); encerramento do finding C-06 do parecer AUD-2610-09.
- **Risco:** (i) perda da equivalência numérica entre data do TAP e leitura operacional — mitigada pela NC-00/NC-07 e pelo registro auditável; (ii) colisão M2=M3 em 15/11/2026 pode forçar decisão às cegas na véspera do marco — mitigada pela ressalva C-06b explicitamente agendada para deliberação futura; (iii) desgaste reputacional por reconhecer atraso — mitigado pela causa raiz documentada e ação corretiva vinculante.
- **Não mitigado por este ADR:** M4 (15/12/2026) permanece invariável como limite absoluto do prazo acadêmico; qualquer emenda futura que toque M4 exige contrapartida de compressão de escopo explicitamente deliberada.

## Ratificação

Ratificada em 31/10/2026 via **CCB-LOG RAT-2026-10-31-A12** (gatilho de permissão prévia deliberativo expresso do GP — CCB membro único), em consonância com o parecer AUD-2610-09 (finding C-06, prioridade crítica). Autoridade: TAP §6 irrevogável como fonte autorizativa; Constituição Art. 5 (governança humana), Art. 6 (SSOT), Art. 8 (auditoria).

## Referências

- `docs/change-requests/cr-001-m2-replanejamento.md` (origem da repactuação)
- `docs/decisoes/adr-013-regime-emenda-tap.md` (regime de emenda — instrumento habilitante)
- `docs/planos/plano-integral-tap-1-2-3-4-5.md` §6/Cronograma Tabela 4 + NC-00/NC-07
- `docs/auditorias/aud-2610-09-okb-normalizacao.md` (finding C-06; ressalva C-06b)
- `docs/governanca/ccb-log.md` (RAT-2026-10-31-A12)

## CO-ASSINATURA (Constitution Art. 5.4)

| Versão | SHA-256 do conteúdo normativo | Commit Git | Data | Papel do ratificador humano | Instrumento |
|--------|------------------------------|------------|------|----------------------------|-------------|
| 1.0.0 | `9cc2e3acdaa9ee26aee22a582fab9a2ca7cffa8a4e34d11e4738cbd90e7edc0e` | commit A12 | 31/10/2026 | Gerente de Projeto — CCB de membro único | Emenda M2 30/09 → 15/11/2026 (CR-001 + regime ADR-013-a); RAT-2026-10-31-A12 *(método: sha256 dos bytes do início do arquivo até a linha imediatamente anterior a este bloco `## CO-ASSINATURA`)* |

---

*Promulgada sob AFA-ULTIMATE v1.3.0-FINAL. A Constituição é lei marcial: aplica-se, não se debate.*
