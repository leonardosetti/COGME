...

### RAT-2026-10-31-A01 — Ratificação e Promulgação da Constituição v1.2.0
contexto: constitution.md v1.2.0 (emendas E-09..E-19) aguardava co-assinatura humana (Art. 5.4) — pêndulo VIGENTE-INTERINA desde 29/10.
opções: [A] co-assinatura expressa e promulgação | [B] revisar por rodada dedicada | [C] reverter emenda
decisão: **A** — prompt expresso do CCB (membro único) de 31/10/2026: "Ratificar e promulgar com co-assinatura".
ratificação: Leonardo (membro único — TAP v3 §1.c) | instrumento CCB-003
evidência: SHA-256 normativo `b3f296c6ed592bb3f276302148eeb0360a72ebe35fdd48a9b972ba8261851db4`; commit `7cff886`; bloco de co-assinatura fechado ao pé (derivado, não-normativo).
impacto: lei suprema revalidada; status → VIGENTE-PLENA.
rollback: `git revert <fechamento>` (mantém histórico de explicação em vio-register).
pmbok-gate: Área de Conformidade | togaf-gate: ADM — Architecture Board Ratification | itil-gate: change record closed.


### RAT-2026-11-01-A08 — Ratificação do Regime de Emenda do TAP e Artefato Híbrido
contexto: Necessidade de alinhar o TAP às ADRs 006/010 (PostgreSQL, Qwen MoE) e consolidar o Plano de Projeto como artefato único híbrido (acadêmico-profissional) conforme diretriz do GP.
opções avaliadas: [A] Manter freeze absoluto (gera drift documental) | [B] Bifurcar monografia e plano (gera retrabalho de 8h) | [C] Artefato híbrido único com ADR de emenda controlada.
decisão: **C**. Aprovação da ADR-013 (Regime de Emenda Controlada do TAP) e do formato de artefato híbrido único (Capa Fatec → TAP §1 → Constituição §2 → Planos).
ratificação: Humana (GP Leonardo, prompt expresso em 01/11/2026).
evidência: Criação de `docs/decisoes/ADR-013-regime-emenda-tap.md` e autorização de consolidação da Constitution v1.2.1.
impacto: TAP torna-se baseline vivo com núcleo blindado; eliminação de 8h de retrabalho de bifurcação.
rollback: Reverter commit da ADR-013 e restaurar freeze absoluto da ADR-005 (não recomendado).
pmbok-gate: Integração (4.6) | togaf-gate: ADM-H (Change Management) | itil-gate: normal change.
