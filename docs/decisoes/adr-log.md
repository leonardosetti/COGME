---
id: docs-decisoes-adr-log
title: ADR-LOG — Registro de Mudanças Autorizadas de ADRs (CCB Log)
type: adr
version: '3.1'
status: ratificado
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-log.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- normalizado
---
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
| ADR-LOG-002 | ADR-005 | 1.0.0 | 1.1.0 | 01/11/2026 | Regime de Emenda Controlada do TAP: revogação da proibição absoluta de revisão/reversão textual; núcleo blindado (objeto, objetivos SMART, justificativa, orçamento-teto R$ 0,00, EAP 12/37) intocado sem Emenda MAJOR; tabela delta em `docs/tap/delta-v3-1.md`. | RAT-2026-10-31-A12 | **APLICADA** |
| ADR-LOG-003 | ADR-008 | 1.0.0 | 1.1.0 | 29/10/2026 | Correção de grafia do stakeholder-avaliador: "Prof. Ms. Nivaldo Carleto" / "Carletto" (duplo t) → "Prof. Dr. Nivaldo Carleto" (único "t"). Saneamento global em todos os artefatos do repositório. | CCB-001 (29/10/2026) | **APLICADA** |
| ADR-LOG-004 | ADR-012 | 1.0.0 | 1.1.0 | 29/10/2026 | Promulgação da `constitution.md` como Lei Suprema com co-assinatura humana; estabelecimento de hierarquia de forja e governança de agentes; protocolo de detecção e restauração de corrupção constitucional. | CCB-002 (29/10/2026) | **APLICADA** |
| ADR-LOG-005 | ADR-013 | 1.0.0 | — | 01/11/2026 | **Não aplicada como emenda sobre ADR existente.** ADR-013 é instrumento próprio (Regime de Emenda Controlada do TAP) que supersede parcialmente ADR-005. Não gera emenda sobre ADR-005; estabelece regime próprio com delta log em `docs/tap/delta-v3-1.md`. | RAT-2026-11-01-A08 | **NAO APLICADA (ADR própria)** |
| ADR-LOG-006 | ADR-015 | 1.0.0 | — | 31/10/2026 | **Não aplicada como emenda sobre ADR existente.** ADR-015 é instrumento próprio (Emenda de Marco M2: 30/09/2026 → 15/11/2026) sob regime ADR-013-a. Não gera emenda sobre ADR-013; estabelece delta log em `docs/tap/delta-v3-1.md`. | RAT-2026-10-31-A12 | **NAO APLICADA (ADR própria)** |
| ADR-LOG-007 | ADR-013 | 1.0.0 | Supersedida por ADR-005 v1.1.0 | 31/10/2026 | Regime de Emenda Controlada do TAP (Regime de Emenda Controlada do TAP (Baseline Vivo)) incorporado integralmente na ADR-005 v1.1.0. ADR-013 permanece como artefato histórico. | RAT-2026-11-01-A08 | **APLICADA (supersedida por ADR-005 v1.1.0)** |
| ADR-LOG-008 | ADR-014 | 1.0.1 | Supersedida por ADR-006 v2.1.0 | 31/10/2026 | Promulgação dos Agentes SDDAI incorporada integralmente na ADR-006 v2.1.0 (Ecossistema SDDAI: Modelo, Agentes, MCPs e Separação L1/L2/L3). ADR-014 permanece como artefato histórico. | RAT-2026-10-31-A12 | **APLICADA (supersedida por ADR-006 v2.1.0)** |
| ADR-LOG-009 | ADR-016 | — | 1.1.0 | 05/11/2026 | Emissão e ratificação definitiva da ADR-016 (Backend do MVP: cálculo, cotações, persistência e contrato de erro). Decisões D1–D12 tornam-se norma vigente para o backend. Aderente à entrega funcional de 16/11/2026; pendências P1–P8 não bloqueiam a entrega e seguem como acompanhamento pós-entrega. | RAT-2026-11-05-A16 | **APLICADA** |
| ADR-LOG-010 | ADR-016 | 1.1.0 | 1.2.0 | 05/11/2026 | Emenda D4: persistência de invoice. Cada usuário pode gerar, armazenar persistentemente, baixar e imprimir a invoice conforme sua regra de jornada e rating de pagamento. Simulações não gravadas. Rota de erase (LGPD art. 18) obrigatória para invoices persistidas (condicionantes D1-D6 da spec-015). Substitui D4 anterior ("somente cotações são persistidas"). | RAT-2026-11-05-A16-D4 | **APLICADA** |
| ADR-LOG-011 | ADR-018 | — | 1.0.0 | 05/11/2026 | Norma de nomenclatura de arquivos de artefato: `tipo_artefato-id_artefato-nome_artefato.{ext}`. As specs existentes já seguem o caso particular `spec-NNN-specname.spec.md`. | RAT-2026-11-05-A18 | **APLICADA** |
| ADR-LOG-012 | specs Grupo A (004, 005, 006, 008, 009, 011) | — | ratificada | 05/11/2026 | Ratificação CCB das 6 specs do Grupo A (backend MVP, container layers, UAT produto, frontend web, NFR consolidados, CI/CD pipeline). Todas aderentes ao padrão TA-0031 (frontmatter camada a + camadas b-h), nomenclatura spec-NNN-specname.spec.md (ADR-018), campo wave (WS-4). Ambiguidade ≤ 0.20 em todas (gate gsd-spec-phase). Pronto para merge do backend e execução da UAT. | RAT-2026-11-05-A16 | **APLICADA** |
| ADR-LOG-013 | specs Grupo B (003, 001, 002, 013, 012, 014, 010) | — | ratificada | 05/11/2026 | Ratificação CCB das 7 specs do Grupo B (memória persistente SDD, emenda constitucional R1, requisitos review R1, documentação técnica, rastreabilidade prompts SDD, runtime agentes + camada CI, qualidade PDCA + Ishikawa). Todas aderentes ao padrão TA-0031 (frontmatter camada a + camadas b-h), nomenclatura spec-NNN-specname.spec.md (ADR-018), campo wave (WS-4/WS-6/WS-7). Ambiguidade ≤ 0.20 em todas (gate gsd-spec-phase). Pronto para ratificação do Grupo C. | RAT-2026-11-05-A16 | **APLICADA** |
| ADR-LOG-014 | ADRs 001, 002, 003, 005, 006, 007, 008, 009, 011, 012, 013, 014, 015, 016 | — | normalizada | 05/11/2026 | Normalização de frontmatter: alinhamento version/status ao corpo das ADRs, campos do template canônico (spec-adr-template v1.0.0: data-decisao, data-formalizacao, decisor, gatilhos, rastreabilidade, dominio-pmbok, processo-pmbok-6, kill-switch), cópias duplicadas marcadas históricas/supersedidas (adr-005-freeze, adr-006-inteligencia-sdd), frontmatter duplos unificados (adr-013, adr-014, adr-015, adr-016), tag self-updated onde derived-from aponta para si mesmo. Nenhuma sobreposição de ADR criada; regra ADR-LOG mantida. | RAT-2026-11-05-A19 | **APLICADA** |

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
| ADR-005 | 1.1.0 | ADR-LOG-002 | Vigente (incorpora ADR-013 e ADR-015) |
| ADR-006 | 2.1.0 | ADR-LOG-001 | Vigente (incorpora ADR-014) |
| ADR-007 | 1.1.0 | ADR-LOG-014 | Vigente |
| ADR-008 | 1.1.0 | ADR-LOG-003 | Vigente |
| ADR-009 | 1.0.0 | — | Vigente |
| ADR-010 | 1.0.0 | — | **Supersedida por ADR-001 v1.1.0** (conteúdo absorvido) |
| ADR-011 | 1.0.0 | — | Vigente (incorporada em ADR-006 v2.1.0) |
| ADR-012 | 1.0.1 | ADR-LOG-014 | Vigente |
| ADR-013 | 1.0.0 | — | **Supersedida por ADR-005 v1.1.0** (conteúdo absorvido) |
| ADR-014 | 1.0.1 | — | **Supersedida por ADR-006 v2.1.0** (conteúdo absorvido) |
| ADR-015 | 1.0.0 | — | **Incorporada em ADR-005 v1.1.0** (emenda de marco M2, registro de delta log em `docs/tap/delta-v3-1.md`) |
| ADR-016 | 1.2.0 | ADR-LOG-010 | **Ratificada** (norma vigente para o backend do MVP; D4 = persistência de invoice com rota de erase) |
| ADR-018 | 1.0.0 | ADR-LOG-011 | **Ratificada** (norma de nomenclatura de arquivos de artefato) |

---

## Histórico de Alterações deste Log

| Versão | Data | Alteração | Responsável |
|--------|------|-----------|-------------|
| 1.0.0 | 31/10/2026 | Emissão inicial: catálogo de 6 mudanças aplicadas (ADR-001, ADR-005, ADR-008, ADR-012) e 2 ADRs próprias não-emenda (ADR-013, ADR-015) | GP Leonardo (CCB) |
| 1.1.0 | 05/11/2026 | Normalização de frontmatter de 14 ADRs (ADR-LOG-014): alinhamento version/status ao corpo, template canônico (spec-adr-template v1.0.0), cópias duplicadas históricas (adr-005-freeze, adr-006-inteligencia-sdd), frontmatter duplos unificados (adr-013, adr-014, adr-015, adr-016), tag self-updated. | GP Leonardo (CCB) |

---

*Promulgado sob AFA-ULTIMATE v1.3.0-FINAL. Constituição é lei marcial: aplica-se, não se debate.*