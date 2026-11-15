---
id: docs-decisoes-adr-017-dependencia-argon2id
title: ADR-017 — Dependência Argon2id (argon2-cffi) para Hash de Senhas
type: adr
version: 1.0.0
status: ratificado
owner: agent-architect
derived-from:
- constitution.md (Art. 9.3.ii, P-01, P-07)
- docs/decisoes/ccb-CR-002.md (CR2-D06, Gate C)
- docs/change-requests/cr-002-cadastro-usuarios-multiusuario.md (§3, §12.1)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- adr
- seguranca
- dependencia
- argon2id
- autenticacao
adr-number: 017
impacto: medio
---

# ADR-017 — Dependência Argon2id (`argon2-cffi`) para Hash de Senhas

## 1. Contexto

A CR-002 (contas multiusuário) exige armazenamento seguro de senhas com hash resistente a ataques de força bruta, GPU/ASIC e canal lateral. O stack atual (FastAPI, SQLAlchemy, PostgreSQL) não possui biblioteca de hash de senhas aprovada.

**Decisão CCB:** CR2-D06 (canal de email e reset dentro da soberania de dados) + Gate C (SPEC-017) requerem hash de senha robusto antes de qualquer implementação de identidade.

## 2. Decisão

**Adotar `argon2-cffi` (binding Python para Argon2id) como dependência obrigatória para hash de senhas.**

- Algoritmo: **Argon2id** (híbrido Argon2i + Argon2d), vencedor do Password Hashing Competition 2015, RFC 9106, recomendação OWASP.
- Pacote PyPI: `argon2-cffi` (FOSS, licença MIT, zero custo recorrente).
- Versão mínima: `argon2-cffi >= 23.1.0` (compatível Python 3.11+).

## 3. Justificativa Técnica

| Critério | Argon2id | bcrypt | PBKDF2 | scrypt |
|----------|----------|--------|--------|--------|
| Resistência GPU/ASIC | ✅ Alta (memória) | ⚠️ Média | ❌ Baixa | ✅ Alta |
| Resistência side-channel | ✅ Argon2i híbrido | ❌ Não | ❌ Não | ⚠️ Parcial |
| Padronização | ✅ RFC 9106 | ✅ Amplamente usado | ✅ NIST SP 800-132 | ⚠️ Menos adotado |
| Recomendação OWASP 2024 | **Primeira escolha** | Aceitável (fallback) | Não recomendado | Aceitável |
| Configurabilidade (m/t/p) | ✅ 3 parâmetros | ⚠️ 1 parâmetro (cost) | ⚠️ Iterações apenas | ✅ 3 parâmetros |
| FOSS / Licença | ✅ MIT | ✅ ISC | ✅ Domínio público | ✅ BSD-2 |

**Fontes:**
- OWASP Password Storage Cheat Sheet 2024: "Argon2id é a recomendação principal"
- RFC 9106: Especificação oficial do Argon2
- Daniel Donda (especialista segurança): "Argon2id é o hash de senha mais seguro do momento"

## 4. Parâmetros de Configuração (OWASP Minimum)

```python
# Em src/backend/security/password.py
from argon2 import PasswordHasher

ph = PasswordHasher(
    memory_cost=19456,    # 19 MiB (OWASP mínimo: m=19456)
    time_cost=2,          # 2 passadas (OWASP mínimo: t=2)
    parallelism=1,        # 1 thread (OWASP mínimo: p=1)
    hash_len=32,
    salt_len=16,
    type=Type.ID          # Argon2id
)
```

**Nota:** Para hardware mais potente (8700G, 60GB RAM), pode-se escalar para `memory_cost=65536` (64 MiB), `time_cost=3` conforme RFC 9106 perfil "restrito".

## 5. Conformidade Constitucional

| Princípio | Conformidade |
|-----------|--------------|
| **P-01 FOSS-ZERO-COST** | ✅ `argon2-cffi` é MIT, zero custo, sem telemetria |
| **P-02 SOBERANIA LOCAL** | ✅ Execução 100% local, sem cloud |
| **P-03 SOBERANIA DE DADOS** | ✅ Senhas nunca saem do processo; hash armazenado no PostgreSQL local |
| **P-07 SEGURANÇA** | ✅ Baseline OWASP atendido; fail-closed (hash falha = negação) |
| **Art. 9.3.ii** | ✅ ADR específica para mudança de stack tecnológica |
| **Art. 10.2** | ✅ Segredo (hash) nunca entra em camada de imagem Docker |

## 6. Impacto no Projeto

- **pyproject.toml:** Adicionar `argon2-cffi>=23.1.0` em `[project.dependencies]`
- **Dockerfile:** Build incluye compilação nativa (Rust/C) — tempo de build +~30s
- **src/backend/security/password.py:** Novo módulo com `hash_password()`, `verify_password()`
- **Testes:** Unit tests para hash/verify, timing attack resistance, parâmetros

## 7. Rota de Fuga (Bypass Protocol — se necessário)

Se `argon2-cffi` falhar em build ou runtime:
1. Fallback temporário: `bcrypt` (`passlib[bcrypt]`) — já no stack indireto
2. Prazo de detox: 30 dias para restaurar Argon2id
3. Documentado em ADR-017-BYPASS se acionado

## 8. Validação

- [x] Parecer `agent-architect`: viabilidade técnica confirmada
- [x] Parecer `agent-digital-security`: atende threat model (ADR-019)
- [x] Ratificação CCB: CR2-D06 + Gate C (docs/decisoes/ccb-CR-002.md)
- [ ] Build teste em CI (próximo push)
- [ ] Inclusão em `pyproject.toml` e `requirements.txt`

---

## CHANGELOG

- **1.0.0 — 2026-11-14:** Emissão inicial, aprovada por CCB/GP via CR-002 Gate C. Responsável: `agent-architect`.