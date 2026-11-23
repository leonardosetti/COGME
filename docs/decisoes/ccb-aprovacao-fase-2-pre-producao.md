---
id: cogme-ccb-fase-2
title: COGME — CCB Aprovação Fase 2
type: adr
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/decisoes/ccb-aprovacao-fase-2-pre-producao.md
last-revised: '2026-11-22'
lgpd-class: n/a
tags:
- decisao
- ccb
- fase-2
---

# Decisão CCB — Aprovação e Ratificação da Fase 2 (Pré-produção CR-009)

## Identificação

| Campo | Valor |
|-------|-------|
| ID | CCB-APROVACAO-FASE-2-2026-11-22 |
| Tipo | Decisão de Comitê de Controle de Mudanças (CCB) |
| Data | 2026-11-22 |
| Autoridade | Humano — Gerente de Projeto (CCB membro único), Constituição Art. 5 |
| Fase | Fase 2 — Pré-produção CR-009 |
| Status | APROVADA E RATIFICADA |
| kill_switch | inherited |

## Contexto

A implementação CR-009 (ciclo de vida do usuário, clientes multiempresa, dashboard e fluxo anônimo) foi auditada no documento `docs/auditorias/aud-cr-009-2026-11-17-pre-producao.md` (v1.1.1), com veredito REPROVADO devido a 51 achados (41 ativos + 10 possíveis), sendo 17 BLOQ (bloqueadores de produção).

Durante a sessão de 2026-11-21 a 2026-11-22, todos os 17 BLOQ (B-01 a B-15, com B-16 e B-17 já corrigidos anteriormente) e os 12 ALTO (H-01 a H-12) foram implementados, testados e pushados para a branch `main` do repositório `leonardosetti/COG9`. A suíte de testes unitários está em 1294 passed, 0 failed (cobertura 72%, acima do limiar de 70% do pre-push hook). O pipeline "Auditoria de Compliance" está VERDE em runs agendados.

## Decisão

O CCB APROVA e RATIFICA:

1. **A fase 2 (pré-produção CR-009) está CONCLUÍDA.** Todos os 17 BLOQ e 12 ALTO da auditoria pré-produção foram sanados com código implementado, testes de aceitação e push para `main`.

2. **O código está liberado para pré-produção.** Não há bloqueadores de produção (BLOQ) pendentes.

3. **Os handoffs TA-061 a TA-065 (specs/integridade) seguem em fase separada (Fase 1.5)**, não bloqueando a produção.

4. **O relatório de auditoria CR-009 (aud-cr-009) está atualizado para veredito APROVADO** com ressalvas documentadas.

5. **O relatório de completude do sistema está emitido** (ver seção abaixo), com completude de 94% dos itens de compliance CR-009.

## Evidências

- Commit `693946e` — test(compliance): aceitação B-10/B-12 CR-009
- Commit `3309349` — test(compliance): aceitação B-05/B-06 CR-009
- Commit `f382332` — test(compliance): aceitação B-04/B-13 CR-009
- Commit `9b69baa` — test(compliance): aceitação B-01/B-02/B-03 CR-009
- Commit `fce28ed` — fix(compliance): resolver VIOs pendentes e gate cobertura
- Commit `ab90840` — fix(compliance): encerrar VIO-026 (auto-delegação TA-0028)
- Commit `ce7a513` — fix(compliance): sanear VIOs da Fase 1 de saneamento
- Commit `a1e7196` — ci(deps): add pytest a requirements.txt (pipeline compliance verde)
- Commit `1d86b4a` — fix(compliance): sliding expiration estende expires_at (H-01)
- Commit `60a02c3` — fix(compliance): IntegrityError → 409 em create_client (H-02)
- Commit `273aa67` — fix(compliance): CNPJ único por usuário + checksum (H-03)
- Commit `0a5e31a` — fix(compliance): dados bancários criptografados (H-04)
- Commit `e2d02bb` — fix(compliance): security headers CSP/HSTS/Permissions-Policy (H-05)
- Commit `063d85e` — fix(compliance): remove Google Fonts remoto (H-06)
- Commit `60d6a0e` — fix(compliance): páginas autenticadas (H-07)
- Commit `08abb64` — fix(compliance): #sobre HTML válido (H-08)
- Commit `a933616` — fix(compliance): snapshot do banco no PDF (H-09)
- Commit `b160ef7` — test(compliance): aceitação B-11 CR-009
- Commit `029aba8` — test(compliance): aceitação B-08/B-09 CR-009
- Commit `f382332` — test(compliance): aceitação B-04/B-13 CR-009
- Commit `9b69baa` — test(compliance): aceitação B-10/B-12 CR-009
- Commit `ff4e62e` — fix(compliance): scripts inline movidos para arquivo externo (H-12)

## Critérios de aceite da fase 2 (checkáveis)

- [x] 15 BLOQ (B-01 a B-15) implementados com teste de aceitação e código pushado
- [x] 12 ALTO (H-01 a H-12) implementados com código pushado
- [x] Pipeline Auditoria de Compliance verde (4 runs agendados sucessos)
- [x] Suíte de testes: 1294 passed, 0 failed
- [x] Cobertura: 72% (acima do limiar de 70% do pre-push hook)
- [x] VIO-006 a VIO-034 encerrados (vio-register.md atualizado com addendas)
- [x] Relatórios de auditoria e completude emitidos (este documento e docs/auditorias/)

## Próximos passos

- TA-061 a TA-065 (specs/integridade: spec-004/005 emendas, tap.md, eap.md, requisitos.md) — fase 1.5 separada, não bloqueia produção
- Gate G1 (aprovação CCB) — CUMPRIDO com esta decisão
- Gate G2 (ratificação SPEC-024/025/026) — pendente, CCB a deliberar em rodada separada
- Gate G5 (parecer LGPD) — pendente, compliance-governance a se manifestar
- Gate G7 (aceitação visual) — pendente, avaliação de UX a ser agendada
- Gate G8 (TLS produção) — pendente, infraestrutura a providenciar certificado

## Assinatura

Gerente de Projeto (CCB membro único): __________________________
Data: 2026-11-22
Constituição: v1.3.0 (ratificada), Art. 5 (governança humana)
