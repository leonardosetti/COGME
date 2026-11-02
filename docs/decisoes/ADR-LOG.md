# ADR-LOG — Registro de Mudanças Autorizadas de ADRs (CCB Log)

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira  
**Autoridade:** GP Leonardo (CCB de membro único — TAP v3 §1.c, Premissa P7)  
**Versão:** 1.0.0  
**Data:** 31/10/2026  
**Status:** VIGENTE  
**Instrumento:** RAT-2026-10-31-A13 (ratificação humana via CCB-LOG)

---

## Princípio de Operação

Conforme determinação do GP (CCB), **não se cria nova ADR sobrepondo regras determinadas por ADR anterior**. Toda mudança de decisão já registrada em uma ADR existente deve ser aplicada como **emenda de versão** da própria ADR, com incremento de versão semântica (`MAJOR.MINOR.PATCH`) e registro neste log. A ADR original permanece como artefato histórico (read-only), e a versão atualizada carrega o delta de alteração com justificativa, data e autorização CCB.

Este log é o **instrumento único de ratificação** de mudanças de ADRs. Nenhuma mudança de ADR é considerada válida sem registro aqui com a correspondente atualização do arquivo da ADR alvo.

---

## Índice de Mudanças (ADR Log)

| ID | ADR Alvo | Versão Anterior | Versão Nova | Data | Justificativa | Instrumento CCB | Status |
|----|----------|-----------------|-------------|------|---------------|-----------------|--------|
| ADR-LOG-001 | ADR-001 | 1.0.0 | 1.1.0 | 31/10/2026 | Substituição de SQLite por PostgreSQL 15+ (stack de dados); adição de Docker Compose + Nginx latente como stack de infraestrutura; definição de hierarquia de APIs de câmbio (Frankfurter primária, PTAX/BCB fallback). | RAT-2026-10-31-A13 | **APLICADA** |
| ADR-LOG-002 | ADR-005 | 1.0.0 | 1.1.0 | 01/11/2026 | Regime de Emenda Controlada do TAP: revogação da proibição absoluta de revisão/reversão textual; núcleo blindado (objeto, objetivos SMART, justificativa, orçamento-teto R$ 0,00, EAP 12/37) intocado sem Emenda MAJOR; tabela delta em `docs/tap/delta-v3.1.md`. | RAT-2026-10-31-A12 | **APLICADA** |
| ADR-LOG-003 | ADR-008 | 1.0.0 | 1.1.0 | 29/10/2026 | Correção de grafia do stakeholder-avaliador: "Prof. Ms. Nivaldo Carleto" / "Carletto" (duplo t) → "Prof. Dr. Nivaldo Carleto" (único "t"). Saneamento global em todos os artefatos do repositório. | CCB-001 (29/10/2026) | **APLICADA** |
| ADR-LOG-004 | ADR-012 | 1.0.0 | 1.1.0 | 29/10/2026 | Promulgação da `constitution.md` como Lei Suprema com co-assinatura humana; estabelecimento de hierarquia de forja e governança de agentes; protocolo de detecção e restauração de corrupção constitucional. | CCB-002 (29/10/2026) | **APLICADA** |
| ADR-LOG-005 | ADR-013 | 1.0.0 | — | 01/11/2026 | **Não aplicada como emenda sobre ADR existente.** ADR-013 é instrumento próprio (Regime de Emenda Controlada do TAP) que supersede parcialmente ADR-005. Não gera emenda sobre ADR-005; estabelece regime próprio com delta log em `docs/tap/delta-v3.1.md`. | RAT-2026-11-01-A08 | **NAO APLICADA (ADR própria)** |
| ADR-LOG-006 | ADR-015 | 1.0.0 | — | 31/10/2026 | **Não aplicada como emenda sobre ADR existente.** ADR-015 é instrumento próprio (Emenda de Marco M2: 30/09/2026 → 15/11/2026) sob regime ADR-013-a. Não gera emenda sobre ADR-013; estabelece delta log em `docs/tap/delta-v3.1.md`. | RAT-2026-10-31-A12 | **NAO APLICADA (ADR própria)** |

---

## Regras de Operação

1. **Nenhuma nova ADR sobrepõe outra.** Se uma decisão impacta o conteúdo de uma ADR existente, a ADR existente é atualizada com novo número de versão (ex: `1.0.0` → `1.1.0`) e o delta é registrado neste log.
2. **ADRs próprias (novos instrumentos)** como ADR-013 (Regime de Emenda Controlada) e ADR-015 (Emenda de Marco M2) são registradas como novas ADRs, não como emendas sobre ADRs existentes.
3. **Cada entrada neste log exige ratificação CCB** (instrumento registrado na coluna "Instrumento CCB").
4. **O SHA-256 do conteúdo normativo da ADR atualizada é recalculado** sobre o corpo do arquivo (excluindo o bloco de co-assinatura) e registrado tanto aqui quanto no bloco de co-assinatura da ADR alvo.
5. **A ADR original permanece como artefato histórico (read-only)**. A versão atualizada substitui o conteúdo normativo, mas o arquivo original é preservado para rastreabilidade forense.

---

## Tabela de Referência Cruzada (ADR → Versão Atual)

| ADR | Versão Canônica Atual | Última Emenda (ADR-LOG ID) | Status |
|-----|----------------------|----------------------------|--------|
| ADR-001 | 1.1.0 | ADR-LOG-001 | Vigente |
| ADR-002 | 1.0.0 | — | Vigente |
| ADR-003 | 1.0.0 | — | Vigente |
| ADR-004 | 1.0.0 | — | Vigente |
| ADR-005 | 1.1.0 | ADR-LOG-002 | Supersedida parcialmente por ADR-013 |
| ADR-006 | 2.0.0 | — | Vigente |
| ADR-007 | 1.0.0 | — | Vigente |
| ADR-008 | 1.1.0 | ADR-LOG-003 | Vigente |
| ADR-009 | 1.0.0 | — | Vigente |
| ADR-010 | 1.0.0 | — | **Supersedida por ADR-001 v1.1.0** (conteúdo absorvido) |
| ADR-011 | 1.0.0 | — | Vigente |
| ADR-012 | 1.1.0 | ADR-LOG-004 | Vigente |
| ADR-013 | 1.0.0 | — | Vigente (instrumento próprio) |
| ADR-014 | 1.0.1 | — | Vigente (renumerada de ADR-013 via OKB-C-26) |
| ADR-015 | 1.0.0 | — | Vigente (instrumento próprio) |

---

## Histórico de Alterações deste Log

| Versão | Data | Alteração | Responsável |
|--------|------|-----------|-------------|
| 1.0.0 | 31/10/2026 | Emissão inicial: catálogo de 6 mudanças aplicadas (ADR-001, ADR-005, ADR-008, ADR-012) e 2 ADRs próprias não-emenda (ADR-013, ADR-015) | GP Leonardo (CCB) |

---

*Promulgado sob AFA-ULTIMATE v1.3.0-FINAL. Constituição é lei marcial: aplica-se, não se debate.*