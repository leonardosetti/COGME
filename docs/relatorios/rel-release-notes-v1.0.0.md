---
id: cogme-rel-release-v1
title: COGME — Release Notes v1.0.0
type: relatorio
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/relatorios/rel-release-notes-v1.0.0.md
last-revised: '2026-11-22'
lgpd-class: n/a
tags:
- relatorio
- release
- v1-0-0
---

# Release v1.0.0 — COGME

## 📋 Visão Geral

Primeira release pública do COGME — simulador de recebimento em moeda estrangeira (backend do MVP). Plataforma multiempresa com ciclo de vida do usuário, dashboard, fluxo anônimo, faturamento (invoices), simulações, provedores e taxas.

## 🚀 O que está incluído

### Fase 1: Saneamento de compliance (concluída)
- Fechamento VIO-030/031/032 (Auditoria de Compliance verde no CI)
- Sanamento de integridade dos agentes/ledger/registry (VIO-019, VIO-020..029)
- Instalação do pytest no CI (requerments.txt)
- 45/45 agentes com frontmatter completo

### Fase 2: Pré-produção CR-009 (concluída, aprovada por CCB 2026-11-22)
- 15 BLOQ (B-01 a B-15) e 12 ALTO (H-01 a H-12) implementados
- PII em log de cadastro, HMAC identidade, Argon2id ativo
- Invoice unique composto, cross-owner client/simulação
- CSRF cookie/logout, reset senha entrega token
- Exclusão conta unicidade, reativação dormente
- Sessão revalida status, Alembic ≤32 chars
- Cookie Secure só produção, clientes internacionais
- Rate limits não-auth e IP proxy
- Sliding expiration, IntegrityError → 409
- CNPJ único + checksum, dados bancários criptografados
- CSP/HSTS/Permissions-Policy, Google Fonts removido
- Navbar/dashboard/perfil/clientes/sobre, #sobre HTML válido
- Snapshot do banco no PDF, aliases reais mascarados
- /auth/me email e telefone, scripts inline → arquivo externo

### Fase 1.5: Especs/Integridade (concluída, 100%)
- spec-004/005 emendadas com bump de versão + CHANGELOG
- Specs 017–022 passam auditoria de integridade
- tap.md repovoado (TAP v3, rastreabilidade arquivo:linha)
- eap.md repovoado (fases N1..N11)
- requisitos.md repovoado (RF/RNF/US REQ-01..15, rastreabilidade 15/15)
- Gate G2 (ratificação specs 024/025/026) aprovado

### Fase 3: CR-009 Produção / Gate G2 (concluída, 100%)
- Specs 024/025/026 emitidas e ratificadas (RATIFICADO)
- CR-009 liberado para produção
- sync_agent_registry.py --check exit 0
- nexus_dispatcher.py --report JSON válido (44 agentes)
- validate_afa_output.py score 100/100 (5 agentes SDDAI)
- Nenhum imutável (constitution, ADRs, ledger) alterado

## 📦 Instalação

```bash
git clone https://github.com/leonardosetti/COGME.git
cd COGME
git checkout v1.0.0
pip install -r requirements.txt
```

## 🔧 Variáveis de Ambiente

Copie `.env.example` para `.env` e preencha:
- `COGME_DATABASE_URL` — conexão PostgreSQL
- `COGME_LOGIN_PEPPER` — pepper HMAC (256-bit aleatório)
- `COGME_SMTP_*` — configuração SMTP local (Postfix)

## 🧪 Testes

```bash
pip install -r requirements-dev.txt
python -m pytest tests/ -q
```

## ⚠️ Notas de Upgrade

Esta é a primeira release pública. Não há versões anteriores para migrar.

## 📊 Métricas

- Suíte de testes: 1294 passed / 0 failed (fase 2), 1549 passed (testes de unidade)
- Cobertura: 72% (hook pré-push: 70%)
- Pipeline Auditoria de Compliance: verde
- Pipeline SDDAI Verify: verde
- sync_agent_registry: exit 0
- nexus_dispatcher: JSON válido

## 📄 Licença

FOSS — Custo zero recorrente (P-01).

---

*Release gerada automaticamente pelo pipeline CR+Spec→Produção.*
