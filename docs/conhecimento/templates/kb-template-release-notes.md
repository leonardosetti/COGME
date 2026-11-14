---
id: kb-template-release-notes
title: Template de Release Notes — Notas de Versão
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-devops
derived-from:
  - Keep a Changelog (https://keepachangelog.com/pt-BR/1.1.0/)
  - Semantic Versioning 2.0.0 (https://semver.org/lang/pt-BR/)
  - constitution.md Art. 9.3 (Fluxo de mudança integrado)
  - PMBOK 7ª — Domínio Entrega
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
  - template
  - entrega
  - release-notes
  - changelog
  - versionamento
---

# Template de Release Notes — COGME

> **Finalidade**: Comunicar **o que mudou** para stakeholders técnicos e não técnicos em cada release. Baseado em **Keep a Changelog** + **SemVer**. Publicado em **GitHub Releases** e replicado em `docs/relatorios/rel-release-notes-vX.Y.Z.md` para rastreabilidade.

---

## 1. CABEÇALHO DA RELEASE

| Campo | Valor |
|---|---|
| **Versão** | vX.Y.Z (SemVer: MAJOR.MINOR.PATCH) |
| **Data de Release** | YYYY-MM-DD |
| **Tipo** | [ ] Major (breaking)  [ ] Minor (feature)  [ ] Patch (fix)  [ ] Hotfix  [ ] RC / Beta |
| **Branch / Tag** | `main` / `vX.Y.Z` / `release/vX.Y.Z` |
| **Commit Base** | `git log -1 --format="%H %s"` |
| **Responsável Release** | Nome / Papel |
| **Aprovação Gate 3** | CCB Go/No-Go (ref: Ata Gate 3 / CR se houver) |

---

## 2. RESUMO EXECUTIVO (1-2 parágrafos)

> Descreva em linguagem **não técnica** o valor entregue: "Esta versão adiciona suporte a múltiplos usuários com isolamento de dados...", "Corrige cálculo de câmbio para EUR...", "Melhora performance de geração de PDF em 40%...".

---

## 3. NOVIDADES (Added) — Novas Funcionalidades

| ID / Ref | Funcionalidade | Descrição | Spec / ADR / CR | Valor para Usuário |
|---|---|---|---|---|
| FEAT-001 | Ex: Cadastro multiusuário (PROP-017/CR-002) | Criação de usuários, sessões, Argon2id, recovery | spec-prop-017 / CR-2026-002 | Permite uso compartilhado da ferramenta |
| FEAT-002 | | | | |

---

## 4. MELHORIAS (Changed) — Alterações em Funcionalidades Existentes

| ID / Ref | Componente | Antes | Depois | Motivo / Benefício |
|---|---|---|---|---|
| IMP-001 | Ex: Cálculo de câmbio | Apenas Frankfurter | Frankfurter + PTAX fallback (ADR-001 v1.1.0) | Resiliência; soberania PTAX |
| IMP-002 | | | | |

---

## 5. CORREÇÕES (Fixed) — Bug Fixes

| ID / Ref | Bug | Descrição | Causa Raiz | Teste de Regressão |
|---|---|---|---|---|
| FIX-001 | Ex: Invoice PDF com encoding errado em PT-BR | Caracteres acentuados quebrados | Fonte UTF-8 não embutida no WeasyPrint | UAT-04 (invoice-pdf) passou |
| FIX-002 | | | | |

---

## 6. REMOÇÕES (Removed) — Funcionalidades Removidas / Deprecadas

| ID / Ref | Item Removido | Substituto / Migração | Impacto |
|---|---|---|---|
| REM-001 | Ex: SQLite como banco canônico | PostgreSQL 15+ (ADR-001 v1.1.0) | Breaking: migração obrigatória |
| REM-002 | | | |

---

## 7. SEGURANÇA (Security) — Correções de Vulnerabilidades

| ID / Ref | CVE / Vulnerabilidade | Severidade (CVSS) | Componente | Ação | Verificação |
|---|---|---|---|---|---|
| SEC-001 | Ex: CVE-2026-XXXX em dependência X | Alta (7.5) | `httpx` | Upgrade para v0.28.1 | SCA scan green |
| SEC-002 | | | | | |

---

## 8. DEPRECIAÇÕES (Deprecated) — Avisos de Futura Remoção

| ID / Ref | Funcionalidade / API / Comportamento | Previsão Remoção | Alternativa Recomendada | Guia Migração |
|---|---|---|---|---|
| DEP-001 | Ex: Endpoint `/v1/rates/legacy` | v2.0.0 (2027-Q1) | `/v1/rates/{currency}` | Docs de migração |

---

## 9. QUEBRANTES (Breaking Changes) — **Apenas para Major Version**

| ID / Ref | O Que Quebra | Impacto | Migração Obrigatória | Prazo Suporte Legado |
|---|---|---|---|---|
| BRK-001 | Ex: Schema DB `fx_quotes` — coluna `source` agora NOT NULL | Migração 0002 obrigatória | Rodar `alembic upgrade head` | Imediato (v2.0.0) |
| BRK-002 | | | | |

---

## 10. DEPENDÊNCIAS E INFRAESTRUTURA

| Componente | Versão Anterior | Versão Nova | Tipo | Notas |
|---|---|---|---|---|
| Python | 3.11.x | 3.12.x | Runtime | |
| FastAPI | 0.115.x | 0.116.x | Framework | |
| PostgreSQL | 15.x | 16.x | Banco | Docker image update |
| Qwen Model | Qwen3-30B-A3B Q4_K_M | Same | LLM | |
| Docker Base | python:3.12-slim | python:3.12-slim (digest updated) | Imagem | Security patches |

---

## 11. TESTES E QUALIDADE (Quality Gate Results)

| Métrica | Meta | Resultado | Status | Evidência |
|---|---|---|---|---|
| **Unit Tests** | 100% pass | N/N | ✅/❌ | CI Run #XXX |
| **Integration Tests** | 100% pass | N/N | ✅/❌ | CI Run #XXX |
| **E2E Tests** | 100% pass | N/N | ✅/❌ | CI Run #XXX |
| **Coverage** | ≥ 80% | XX% | ✅/❌ | Codecov/coverage.xml |
| **Security Scan** | 0 High/Critical | N vulns | ✅/❌ | Trivy/Snyk report |
| **FOSS Compliance** | 100% FOSS | Sim/Não | ✅/❌ | License check |
| **Performance (P95)** | ≤ 2s (simulate) | X.XXs | ✅/❌ | Benchmark run |
| **Accessibility (WCAG)** | AA | Pass/Fail | ✅/❌ | axe-core report |

---

## 12. PROCEDIMENTOS OPERACIONAIS (Runbook Ref)

| Operação | Documento | Versão | Validado Em |
|---|---|---|---|
| **Deploy** | `docs/operacao/proc-runbook.md` §Deploy | vX.Y.Z | Gate 3 / Staging |
| **Rollback** | `docs/operacao/proc-runbook.md` §Rollback | vX.Y.Z | Gate 3 / Simulação |
| **Health Check** | `docs/operacao/proc-runbook.md` §Monitoring | vX.Y.Z | Pós-deploy |
| **Backup/Restore** | `docs/operacao/proc-runbook.md` §Backup | vX.Y.Z | Mensal / Ad-hoc |

---

## 13. ISSUES CONHECIDOS (Known Issues)

| ID | Descrição | Impacto | Workaround | Previsão Correção |
|---|---|---|---|---|
| KNOWN-001 | Ex: Latência PTAX > 5s em horário de pico | Timeout ocasional fallback | Retry automático (3x) + cache 7 dias | PR #XXX (otimização cache) |
| KNOWN-002 | | | | |

---

## 14. AGRADECIMENTOS / CRÉDITOS

> Contribuidores desta release: @user1 (feat), @user2 (fix), @user3 (review), @user4 (docs), @user5 (testes).

---

## 15. LINKS ÚTEIS

- **GitHub Release**: https://github.com/leonardosetti/COGME/releases/tag/vX.Y.Z
- **Changelog Completo**: `docs/relatorios/rel-release-notes-vX.Y.Z.md` (este arquivo)
- **Diff Completo**: `git log vX.Y-1..vX.Y.Z --oneline`
- **Milestone GitHub**: https://github.com/leonardosetti/COGME/milestone/XX
- **CI/CD Run**: https://github.com/leonardosetti/COGME/actions/runs/XXXXXXXX

---

> **Publicação**: Após Gate 3 Go, `git tag -a vX.Y.Z -m "Release vX.Y.Z"` + `git push origin vX.Y.Z` → GitHub Release automático (workflow) + cópia em `docs/relatorios/`.