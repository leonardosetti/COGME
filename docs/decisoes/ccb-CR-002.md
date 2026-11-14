---
id: docs-decisoes-ccb-cr-002
title: Registro de Decisões CCB/GP — CR-002 Contas Multiusuário
type: decisao-ccb
version: 1.0.0
status: ratificada
owner: agent-project-analyst
derived-from:
- docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md
- constitution.md (Arts. 1.2, 1.3, 5.1, 5.4, 9.1-9.4)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- ccb
- cr-002
- multiusuario
- emenda-constitucional
- marcos
---

# Registro de Decisões CCB/GP — CR-002

**Data da sessão:** 2026-11-14  
**Participantes:** Gerente de Projeto (CCB de membro único)  
**Instrumento:** Prompt expresso do CCB — ratificação única  
**Emenda constitucional associada:** E-20 (constitution.md v1.2.2 → v1.3.0)

---

## Decisões CR2-D01 a CR2-D09 — APROVADAS

| ID | Decisão | Veredito | Fundamento | Especs Liberadas |
|----|---------|----------|------------|------------------|
| **CR2-D01** | Admitir contas multiusuário no escopo e reverter OS-01 | **APROVADA** | Demanda de valor direto para usuário final; viabilidade técnica confirmada | Gate A — pré-requisito de todas |
| **CR2-D02** | Papel controlador/operador, bases legais e direitos LGPD/GDPR | **APROVADA** | Controlador = usuário titular; base legal art. 7º V LGPD (execução de contrato); GDPR aplica-se se oferta/monitoramento EEE/UK | Gate B — SPEC-022 |
| **CR2-D03** | Retenção de invoices finalizadas: **retenção legal mínima (5 anos art. 206 §5º CC) + anonimização pós-período** | **APROVADA** | Obrigação legal civil prevalece sobre direito ao esquecimento; anonimização irreversível após 5 anos | Gate B — SPEC-022 |
| **CR2-D04** | Dormência: 180 dias sem login → `dormant`; reativação exige reset senha + verificação identidade | **APROVADA** | Alinhado a boas práticas OWASP e LGPD art. 16 (direito de restringir) | Gate B — SPEC-022 |
| **CR2-D05** | Regra de idioma: `client.country_code` canônico; `BR` → `pt-BR`, demais → `en`; cliente fictício exige país explícito | **APROVADA** | Simples, determinística, auditável | Gate D — SPEC-021 |
| **CR2-D06** | Canal de email: **SMTP local/autohospedado** (Postfix/Dovecot em container); reset TTL 1h; pepper HMAC rotacionado 90 dias | **APROVADA** | Soberania de dados (P-03); sem cloud não autorizada | Gate C — SPEC-017 |
| **CR2-D07** | Ratificar identity, histórico e diretório de clientes como escopo do MVP (cenário A — Completo) | **APROVADA** | Valor integral da demanda; M4 estendido para 30/12/2026 | Gate E — confirmação retroativa |
| **CR2-D08** | Ciclo Rascunho/Finalizada: rascunho editável; finalizada imutável; clonagem cria novo rascunho com `supersedes_invoice_id` | **APROVADA** | Garante integridade histórica e auditoria | Gate D — SPEC-020 |
| **CR2-D09** | **Não criar M5. Estender M4 para 30/12/2026** (15 dias úteis adicionais). Recurso AI-Driven processing disponível. Cenário A — Completo (264–408h) viável no M4 estendido. | **APROVADA** | Evita fragmentação de milestones; recurso computacional alocado | Gate A — pré-requisito de implementação |

---

## Emenda Constitucional E-20 — RATIFICADA

- **Versão anterior:** v1.2.2 (`373c391124dd93c386d6296f8ca10d2ffcf98711f9c2fe0f91cc7fd54e4beaa7`)
- **Versão nova:** v1.3.0
- **Commit Git:** `a1b2c3d4e5f6` (placeholder — será preenchido no commit real)
- **Hash normativo v1.3.0:** `pending` (calculado no commit)
- **Data:** 2026-11-14
- **Papel:** Gerente de Projeto — CCB de membro único
- **Instrumento:** Prompt expresso CCB 2026-11-14 — ratificação única CR-002 + E-20

> **Nota:** O bloco CO-ASSINATURA em `constitution.md` será atualizado com hash e commit reais no momento do `git commit`.

---

## ADRs Autorizadas (para emissão imediata)

| ADR | Título | Responsável | Prazo |
|-----|--------|-------------|-------|
| ADR-017 | Dependência Argon2id (`argon2-cffi`) para hash de senhas | `agent-architect` | 2026-11-15 |
| ADR-018 | Replanejamento TAP/M4 — extensão para 30/12/2026, cenário A Completo | `agent-project-analyst` | 2026-11-15 |
| ADR-019 | Segurança Multiusuário — threat model, sessão, CSRF, rotação alias, rate limit | `agent-digital-security` | 2026-11-16 |

---

## Próximos Passos Imediatos

1. **Commit da emenda E-20** em `constitution.md` (v1.2.2 → v1.3.0) com co-assinatura Art. 5.4
2. **Emitir ADR-017, ADR-018, ADR-019** conforme prazos acima
3. **Retificar `spec-015-lgpd-produto-proposta-v1.spec.md`**: mover D1 para §2 (resolvida por ADR-016 D4), limpar §4, atualizar CHANGELOG
4. **Revisitar `spec-prop-017-conta-multiusuario.md`** para Gate B: alinhar SPEC-022 com decisões D2/D3/D4 ratificadas
5. **Agendar parecer de auditoria/compliance** pós-commit (Gate 1)
6. **Emitir SPEC-017..022** em sequência conforme gates

---

## Rollback (se necessário)

Se qualquer ADR for rejeitada ou emenda não conferir hash:
- Reverter commit `a1b2c3d4e5f6`
- `constitution.md` permanece v1.2.2 `VIGENTE-PLENA`
- CR-002 marcada `recusada`; specs derivadas `arquivado`
- Zero migração de banco, zero impacto runtime