---
id: docs-impl-frontend-ifit
title: Artefato Responsável — Implantação da Interface COGME (ifit.com)
type: adr
version: 1.0.0
status: draft
owner: agent-project-analyst
derived-from:
- .ai/specs/spec-008-frontend-web-responsive-v1.spec.md (ratificada v0.2.0)
- src/frontend/prototype-ifit/index.html (protótipo aprovado)
- constitution.md (Art. 1.2, P-02, P-03, P-04, P-10, Art. 10.1)
- docs/decisoes/ccb-CR-002.md (CR2-D01, D07)
last-revised: '2026-11-16'
lgpd-class: n/a
tags:
- frontend
- implantação
- interface
- ui
- kanban
- artefato-responsável
---

# Artefato Responsável — Implantação da Interface COGME (ifit.com)

## 1. Objetivo

Este artefato é o documento responsável pela implantação total da interface web do COGME, com inspiração visual no design do https://www.ifit.com/ (limpo, tipografia forte, espaçamento generoso, transições de scroll, navbar fixa com desfocado, rodapé estruturado). Substitui o protótipo atual por uma implementação integrada ao backend FastAPI, respeitando as specs aprovadas (spec-008, CR-002, spec-004, spec-021).

## 2. Escopo da implantação

### 2.1 O que entra (In)

| Item | Descrição | Spec de referência |
|------|-----------|-------------------|
| Navbar fixa | Marca, links (Produto, Simulador, Invoice, Sobre), CTAs (Entrar, Cadastre-se), desfocado no scroll | spec-008 R-INT-01 |
| Hero | Tipografia forte (3rem, peso 800), CTA duplo, visual com gradiente animado | spec-008 §3 |
| Features | Grade de cartões com ícones, hover e reveal ao scroll | spec-008 §3 |
| Simulador integrado | Chamada real a `POST /v1/simulate`, estados loading/error/success, CSRF, rate limit | spec-004 §3, spec-008 §6.1 |
| Invoice | Emissão via `POST /v1/invoice`, preview PDF, bilíngue pt-BR/EN | spec-004 §3, spec-021 |
| Estados | empty/loading/error/success em todas as telas | spec-008 §5 |
| Acessibilidade | Contraste ≥4.5:1, foco visível, labels programáticos, landmarks | spec-008 §7 |
| Responsividade | Mobile-first (360px+), sem scroll horizontal, Chrome/Firefox/Edge últimas 2 versões | spec-008 §8 |
| Zero recursos remotos | Sem CDN, sem webfont externa, assets vendored em `static/` | spec-008 R-INT-04 |
| Mesmo origem | Sem CORS, frontend servido na mesma origem que `/v1/*` via proxy | spec-008 R-INT-02 |

### 2.2 O que fica fora (Out)

| Item | Motivo |
|------|--------|
| App mobile nativo | OS-06, espec-008 §12 |
| Tema dark | espec-008 §12 (fora de escopo) |
| i18n integral da interface/erros | espec-008 §12 (apenas invoice bilíngue) |
| Autenticação/multiusuário na UI | espec-008 §12 (OS-01) — fica no backend |
| e2e automatizado de navegador nesta onda | espec-005:181 |

## 3. Artefatos aderentes a criar/editar

| Artefato | Caminho | Tipo | Status |
|--------|---------|------|--------|
| Este artefato | `docs/impl/frontend-impl-ifit.md` | ADR | draft (este arquivo) |
| Navbar compartilhada | `src/frontend/templates/_navbar.html` | Template Jinja2 | novo |
| Rodapé compartilhado | `src/frontend/templates/_footer.html` | Template Jinja2 | novo |
| CSS do design system ifit | `src/frontend/static/css/app-ifit.css` | Estilo | novo |
| JS de interação (scroll, reveal, estados) | `src/frontend/static/js/app-ifit.js` | Script | novo |
| Página produto | `src/frontend/templates/produto.html` | Template | novo |
| Página simulador | `src/frontend/templates/simulador.html` | Template | novo |
| Página invoice | `src/frontend/templates/invoice-form.html` (atualizar) | Template | existente, ajustar |
| Rotas frontend | `src/frontend/app.py` | Código | existente, ajustar |
| Testes de integração UI | `tests/integration/test_frontend_ifit.py` | Teste | novo |

## 4. Regras de implantação

1. **Não quebrar o existente:** O endpoint `POST /v1/simulate` e `POST /v1/invoice` do backend continuam inalterados. O frontend consome via `fetch` mesmo origem.
2. **CSRF:** Rotas mutáveis do frontend precisam do token CSRF (double-submit cookie + header `X-CSRF-Token`).
3. **Sessão:** Rotas que exigem autenticação (histórico, conta) usam cookie `session` do backend. O simulador e invoice pública permanecem sem sessão (públicos).
4. **Erro canônico:** Todas as respostas de erro seguem o envelope `{"error": {"key", "message", "details"}}` do backend.
5. **PII:** Nenhum dado pessoal é persistido pelo frontend; logs sem valores do usuário (P-04, spec-004:126).
6. **LGPD:** `country_code` obrigatório para cliente fictício (spec-021, DEC-07); `locale` derivado server-side.

## 5. Critérios de aceite (CA)

| ID | Critério | Método |
|----|----------|--------|
| CA-01 | Navbar fixa com desfocado ao rolar, links e CTAs funcionando | Inspeção visual + clique |
| CA-02 | Hero com tipografia forte, CTA duplo, visual gradiente | Inspeção visual |
| CA-03 | Features em grade com cartões, hover e reveal ao scroll | Inspeção visual + scroll |
| CA-04 | Simulador chama `POST /v1/simulate` e exibe resultado líquido | Teste de integração com banco |
| CA-05 | Estados empty/loading/error/success funcionam | Teste de integração |
| CA-06 | CSRF double-submit em rotas mutáveis do frontend | Teste de integração |
| CA-07 | Invoice em PDF bilíngue (pt-BR/en) | Teste de integração |
| CA-08 | Contraste ≥4.5:1, foco visível, labels programáticos | Auditoria de acessibilidade |
| CA-09 | Sem recursos remotos (CDN/webfont) | Network inspector |
| CA-10 | Responsivo em 360px+, sem scroll horizontal | Inspeção em viewport estreita |

## 6. Rastreabilidade

| Fonte | Linha | O que cobre |
|-------|-------|-------------|
| spec-008 | §3, §5, §6.1, §7, §8 | Requisitos da interface |
| spec-004 | §3 | Contrato `/v1/simulate`, `/v1/invoice` |
| spec-021 | §2 | Regra bilíngue |
| spec-005 | §4 | Camada front, proxy |
| constitution.md | P-02, P-03, P-04, P-10 | Soberania, LGPD, idioma |

## 7. Cronograma (alinhado ao PLAN e CR-002 Onda 1)

| Semana | Atividade | Responsável |
|--------|-----------|-------------|
| Semana 1 | Criar templates navbar/footer, CSS ifit, rotas frontend | agent-frontend-dev |
| Semana 2 | Integrar simulador com `/v1/simulate`, estados, CSRF | agent-frontend-dev + agent-backend-dev |
| Semana 3 | Integrar invoice com `/v1/invoice`, bilíngue | agent-frontend-dev |
| Semana 4 | Testes de integração, acessibilidade, revisão | agent-qa-sdet + agent-reviewer |
| Semana 5 | UAT, aprovacao CCB, deploy | agent-project-analyst |

## 8. CHANGELOG

- **1.0.0 — 2026-11-16**: Emissão inicial deste artefato responsável. Define escopo, artefatos aderentes, regras de implantação, critérios de aceite e cronograma para implantação da interface COGME com inspiração ifit.com.
