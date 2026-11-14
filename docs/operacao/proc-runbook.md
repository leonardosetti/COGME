---
id: docs-operacao-runbook
title: Runbook / Playbook Operacional — COGME
type: procedimento
version: 1.0.0
status: ativo
owner: agent-devops
derived-from:
- constitution.md Art. 10 (Infraestrutura e Isolamento) / Art. 7 (Segurança)
- ADR-010 (Stack Infraestrutura) / ADR-001 (Stack FOSS)
- CI-CD-GOV-001 (Política CI/CD) / DEVSECOPS-001 (Política DevSecOps)
- PMBOK 7ª — Domínio Entrega e Operações
- README.md §6 (Operação) / §8 (Arquitetura) / §9 (Tailscale)
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- operacao
- runbook
- playbook
- deploy
- rollback
- monitoramento
- incident-response
- backup
---

# Runbook / Playbook Operacional — COGME

> **Finalidade**: Guia operacional **passo a passo** para: **Deploy**, **Rollback**, **Monitoramento**, **Resposta a Incidentes**, **Backup/Restore**, **Manutenção**. Obrigatório para **Gate 3 (Go-Live)** — deve ser validado em simulação de staging antes de produção.
> **Público**: DevOps, Backend Dev, GP/CCB, Plantão (se houver).
> **Atualização**: A cada release, mudança de infra, ou incidente (lições aprendidas).

---

## 1. VISÃO GERAL DA INFRAESTRUTURA

### 1.1 Topologia (Docker Compose — `docker-compose.yml`)

| Serviço | Imagem | Porta Host | Porta Container | Rede | Volumes | Health Check |
|---|---|---|---|---|---|---|
| **db** | `postgres:15-alpine` | 5432 | 5432 | `cogme-internal` | `pgdata:/var/lib/postgresql/data` | `pg_isready -U ${POSTGRES_USER}` |
| **migrate** | `cogme-backend:latest` | — | — | `cogme-internal` | — | `alembic upgrade head` (init container) |
| **back** | `cogme-backend:latest` | — | 8000 | `cogme-internal` | — | `GET /health` (FastAPI) |
| **front** | `cogme-frontend:latest` | — | 8080 | `cogme-internal` | — | `GET /` (nginx) |
| **proxy** | `nginx:alpine` | **8080** | 80 | `cogme-internal` + `cogme-external` | `./nginx.conf:/etc/nginx/nginx.conf:ro` | `GET /health` (proxy) |

> **Rede**: `cogme-internal` (isolada, sem internet) — db, migrate, back, front, proxy. `cogme-external` (apenas proxy) — acesso via Tailscale (0.0.0.0:8080).
> **Usuários**: Containers rodam com usuário não-root (UID 10001). `back` **não publica porta no host** — só acessível via proxy/front.

### 1.2 Variáveis de Ambiente Críticas (`.env` — **NUNCA versionar valores reais**)

| Variável | Descrição | Obrigatória | Exemplo | Onde Usada |
|---|---|---|---|---|
| `POSTGRES_DB` | Nome do banco | Sim | `cogme` | db, back, migrate |
| `POSTGRES_USER` | Usuário DB | Sim | `cogme` | db, back, migrate |
| `POSTGRES_PASSWORD` | Senha DB (forte, única) | Sim | `*****` | db, back, migrate |
| `DATABASE_URL` | URL conexão async | Sim | `postgresql+asyncpg://user:pass@db:5432/cogme` | back, migrate |
| `FRANKFURTER_API_URL` | API primária cotações | Sim | `https://api.frankfurter.app` | back (rate_providers) |
| `PTAX_API_URL` | API fallback PTAX/BCB | Sim | `https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata` | back (rate_providers) |
| `PTAX_ENABLED` | Habilita fallback PTAX | **Sim** | `true` | back (circuit breaker) |
| `SECRET_KEY` | Chave JWT/sessões (32+ chars) | Sim | `*****` | back (auth, sessions) |
| `ARGON2_MEMORY_COST` | Argon2id memory (KB) | Sim | `65536` | back (password_hasher) |
| `ARGON2_TIME_COST` | Argon2id iterations | Sim | `3` | back (password_hasher) |
| `ARGON2_PARALLELISM` | Argon2id threads | Sim | `4` | back (password_hasher) |
| `HMAC_SECRET_KEY` | Chave HMAC para lookup PII | Sim | `*****` | back (pseudonimização) |
| `TAILSCALE_IP` | IP Tailscale do host (para acesso remoto) | Não | `100.98.x.x` | Docs / Acesso |

> **Arquivo modelo**: `.env.example` (versionado, sem segredos). **Produção**: `.env` gerado no deploy, injetado via CI/CD secrets ou gerenciador de segredos local.

---

## 2. DEPLOY (Procedimento Padrão)

### 2.1 Pré-Deploy Checklist (Gate 3 — Obrigatório)

- [ ] **Gate 3 Aprovado** (CCB Go/No-Go assinado)
- [ ] **Test Plan Executado** — All Quality Gates Green (CI passing)
- [ ] **Release Notes** geradas e revisadas (`docs/conhecimento/templates/kb-template-release-notes.md`)
- [ ] **Runbook** revisado e simulado em staging (esta seção)
- [ ] **Rollback Plan** validado (simulação de rollback OK)
- [ ] **Backup DB** realizado (ver §6)
- [ ] **Variáveis `.env`** conferidas (staging vs prod)
- [ ] **Imagens Docker** buildadas e tagueadas (`vX.Y.Z` + `latest`)
- [ ] **Health Checks** configurados e testados
- [ ] **Monitoring/Alerting** ativo (ver §4)

### 2.2 Passos de Deploy (Produção)

```bash
# 1. No host de produção (via SSH ou local)
cd /opt/cogme  # ou diretório do projeto

# 2. Backup pré-deploy (ver §6.1)
./scripts/backup_pre_deploy.sh

# 3. Pull imagens novas (se registry remoto) OU build local
# Opção A: Registry (se configurado)
docker compose pull

# Opção B: Build local (padrão COGME — zero registry)
git fetch origin
git checkout vX.Y.Z  # tag da release
docker compose build --no-cache  # --no-cache para evitar segredos em layer

# 4. Parar serviços gracefully (exceto db)
docker compose stop front back proxy

# 5. Rodar migrações (idempotente, seguro)
docker compose run --rm migrate

# 6. Subir serviços em ordem de dependência
docker compose up -d db
docker compose up -d migrate  # já rodou no step 5, mas garante
docker compose up -d back
docker compose up -d front
docker compose up -d proxy

# 7. Verificar health checks (wait até healthy)
timeout 60 bash -c 'until docker compose ps | grep -E "(back|front|proxy).*healthy"; do sleep 2; done'

# 8. Smoke tests pós-deploy (ver §3.1)
./scripts/smoke_tests.sh

# 9. Notificar stakeholders (ver Communication Plan)
# Discord #deploy + GitHub Release + E-mail se crítico
```

### 2.3 Deploy Staging (Preview / PR)

```bash
# Automatizado via GitHub Actions (.github/workflows/deploy-staging.yml)
# Trigger: PR opened/updated → deploy para staging.<tailscale-ip>.nip.io
# Steps: build → test → migrate → up → smoke tests → comment PR with URL
# TTL: 24h ou até PR closed/merged
```

### 2.4 Validação Pós-Deploy (Smoke Tests)

| Teste | Comando | Critério Sucesso |
|---|---|---|
| Health Check API | `curl -f http://localhost:8080/health` | HTTP 200 + JSON `{"status":"healthy"}` |
| Health Check DB | `curl -f http://localhost:8080/health/db` | HTTP 200 + `{"db":"connected"}` |
| Rate API (USD) | `curl -f http://localhost:8080/v1/rates/USD` | HTTP 200 + JSON com `rate`, `source` |
| Simulate Endpoint | `curl -X POST -d '{"amount":1000,"currency":"USD"}' http://localhost:8080/v1/simulate` | HTTP 200 + `brl_amount` > 0 |
| Frontend Carrega | `curl -f http://localhost:8080/` | HTTP 200 + HTML contém "COGME" |
| Invoice PDF | `curl -X POST ... /v1/invoice` | HTTP 200 + Content-Type `application/pdf` |

> **Script**: `scripts/smoke_tests.sh` (retorna exit code 0 se todos passam).

---

## 3. ROLLBACK (Procedimento de Reversão)

### 3.1 Quando Acionar Rollback
- Smoke tests falham pós-deploy
- Métricas degradadas (latência P95 > 2x baseline, error rate > 5%)
- Incidente segurança detectado
- Decisão CCB / GP (Nível 3 escalação)

### 3.2 Rollback Rápido (Imagens Anteriores — < 5 min)

```bash
# 1. Identificar tag anterior estável
git tag --sort=-v:refname | head -5
# Ex: v1.2.3 (atual com problema), v1.2.2 (anterior estável)

# 2. Fazer checkout da tag anterior
git checkout v1.2.2

# 3. Rebuild e restart (preserva DB — migrações são idempotentes/forward-only)
docker compose build --no-cache
docker compose up -d --force-recreate back front proxy

# 4. Verificar health checks
timeout 60 bash -c 'until docker compose ps | grep -E "(back|front|proxy).*healthy"; do sleep 2; done'

# 5. Smoke tests
./scripts/smoke_tests.sh

# 6. Confirmar rollback no CCB Log + Status Report
```

### 3.3 Rollback de Banco de Dados (Se Migração Problemática — Raro)

> **Atenção**: Migrações Alembic são **forward-only** (não têm downgrade seguro em produção). Rollback de DB = **Restore from Backup** (ver §6.2).

```bash
# 1. Parar aplicação (manter DB rodando)
docker compose stop back front proxy

# 2. Restore backup mais recente (ver §6.2)
./scripts/restore_db.sh /backups/cogme_pre_deploy_YYYYMMDD_HHMMSS.dump

# 3. Checkout tag anterior
git checkout v1.2.2

# 4. Rebuild e restart
docker compose build --no-cache
docker compose up -d back front proxy

# 5. Verificar + Smoke tests
```

### 3.4 Validação de Rollback (Simulação Obrigatória em Staging)

| Cenário | Frequência | Critério Sucesso |
|---|---|---|
| Rollback rápido (imagem anterior) | **Por Release** (Gate 3) | < 5 min; smoke tests pass |
| Rollback + DB Restore | **Mensal** / Pré-Gate 3 Final | < 15 min; dados íntegros; smoke tests pass |

> **Registro**: Toda simulação de rollback documentada em `docs/operacao/rollback-simulations/YYYYMMDD.md`.

---

## 4. MONITORAMENTO E ALERTAS

### 4.1 Métricas Chave (Observabilidade)

| Métrica | Fonte | Threshold Alerta | Ação |
|---|---|---|---|
| **API Latency P95 (simulate)** | `back` (custom metrics endpoint) | > 4s (2x baseline) | Investigar; verificar circuit breaker |
| **API Latency P95 (invoice PDF)** | `back` | > 6s (2x baseline) | Verificar WeasyPrint / queue |
| **Error Rate (5xx)** | `proxy` (nginx access log) / `back` (logs) | > 1% em 5 min | Verificar logs; circuit breaker status |
| **DB Connections Used** | `pg_stat_activity` | > 80% pool (config: 20) | Verificar leaks; restart back se necessário |
| **Disk Usage (host)** | `df -h /opt/cogme` | > 80% | Limpar logs antigos; backup antigo; expandir volume |
| **Memory Usage (container back)** | `docker stats` | > 85% sustained | Verificar modelo LLM / memory leak |
| **CPU Usage (host)** | `docker stats` / `htop` | > 90% sustained | Verificar carga; escalar se possível |
| **Circuit Breaker State** | `back` (metrics) | `OPEN` por > 5 min | Verificar APIs externas; fallback ativo? |
| **Certificate Expiry (TLS)** | `openssl x509 -in cert.pem -noout -dates` | < 30 dias | Renovar certificado |

### 4.2 Dashboards e Logs

| Ferramenta | Acesso | O Que Monitora |
|---|---|---|
| **Docker Stats / Logs** | `docker compose logs -f back` / `docker stats` | Runtime, stdout/stderr, resource usage |
| **Nginx Access/Error Logs** | `docker compose logs proxy` | Requisições, latência, erros 4xx/5xx |
| **PostgreSQL Logs** | `docker compose logs db` | Queries lentas, erros, connections |
| **GitHub Actions** | https://github.com/leonardosetti/COGME/actions | CI/CD status, test results, security scans |
| **Tailscale Admin** | https://login.tailscale.com/admin/machines | Conectividade, dispositivos autorizados |

### 4.3 Alertas (Configuração Mínima)

```yaml
# Exemplo: .github/workflows/monitoring.yml (scheduled) OU script cron no host
# Alerta via Discord webhook + GitHub Issue auto-criada
alerts:
  - name: "High Latency Simulate"
    condition: "P95 > 4s por 5 min"
    action: "Discord #alerts + Issue GitHub (label: alert)"
  - name: "Error Rate Spike"
    condition: "5xx > 1% por 5 min"
    action: "Discord #alerts + Issue GitHub (label: alert)"
  - name: "Circuit Breaker OPEN"
    condition: "state=OPEN por > 5 min"
    action: "Discord #alerts + Issue GitHub (label: alert)"
  - name: "Disk Space Critical"
    condition: "disk > 85%"
    action: "Discord #alerts + Issue GitHub (label: alert)"
```

---

## 5. RESPOSTA A INCIDENTES (Incident Response)

### 5.1 Classificação de Severidade

| Severidade | Definição | Exemplos | SLA Resposta | SLA Resolução | Escalação |
|---|---|---|---|---|---|
| **P0 — Crítico** | Produção parada; dados em risco; segurança | DB down; vazamento segredo; API 100% erro | **Imediato** (≤ 15 min) | ≤ 1h | Nível 3 (CCB + GP) |
| **P1 — Alto** | Funcionalidade principal degradada; SLA violado | Latência > 4s; fallback falhando; PDF não gera | ≤ 30 min | ≤ 4h | Nível 2 (GP + Tech Lead) |
| **P2 — Médio** | Funcionalidade secundária; workaround existe | Métricas não atualizam; log noise; UI bug menor | ≤ 2h | ≤ 24h | Nível 1 (Equipe) |
| **P3 — Baixo** | Melhoria; cosmetic; documentação | Typo; doc desatualizada; feature request | Next sprint | Next release | Backlog |

### 5.2 Fluxo de Resposta (P0/P1)

```mermaid
flowchart TD
    A[Alerta / Detecção] --> B{Severidade?}
    B -->|P0| C[IC Assume Comando Imediato]
    B -->|P1| D[Tech Lead Assume]
    C --> E[Comunicar: Discord @team + GP + Stakeholders]
    D --> E
    E --> F[Diagnóstico: Logs + Métricas + Health Checks]
    F --> G{Causa Identificada?}
    G -->|Sim| H[Aplicar Mitigação / Workaround]
    G -->|Não| I[Escalar Nível 3 + War Room]
    H --> J[Verificar Recuperação: Smoke Tests]
    I --> J
    J --> K{Resolvido?}
    K -->|Sim| L[Post-Mortem Agendado (24-48h)]
    K -->|Não| M[Investigação Profunda + Rollback se necessário]
    M --> J
```

### 5.3 Runbooks de Incidentes Comuns (Quick Reference)

| Incidente | Sintoma | Diagnóstico Rápido | Mitigação Imediata | Runbook Detalhado |
|---|---|---|---|---|
| **API Rates Indisponível** | `/v1/rates/USD` 503/timeout | `docker compose logs back` → circuit breaker OPEN? Frankfurter/PTAX down? | Ativar fallback manual (`PTAX_ENABLED=true`); restart back | `docs/operacao/incident-rates-api.md` |
| **DB Connection Exhausted** | `back` logs: `pool timeout` / `too many connections` | `docker exec db psql -c "SELECT * FROM pg_stat_activity;"` | Restart `back` (libera connections); aumentar pool se recorrente | `docs/operacao/incident-db-connections.md` |
| **PDF Generation Fails** | `/v1/invoice` 500 / WeasyPrint error | `docker compose logs back` → WeasyPrint log / missing font / memory | Verificar template Jinja2; restart back; fallback HTML | `docs/operacao/incident-pdf-generation.md` |
| **SSL/TLS Certificate Expired** | Browser: `NET::ERR_CERT_DATE_INVALID` | `openssl x509 -in /etc/nginx/certs/cert.pem -noout -dates` | Renovar cert (Let's Encrypt / manual); reload nginx | `docs/operacao/incident-tls-cert.md` |
| **Secrets Exposed** | TruffleHog alert / GitHub secret scanning | Verificar commit / .env / Docker layer | Rotacionar segredo IMEDIATAMENTE; rebuild --no-cache; audit log | `docs/operacao/incident-secrets-exposed.md` |

---

## 6. BACKUP E RESTORE

### 6.1 Backup Pré-Deploy (Automático no Deploy Script)

```bash
# scripts/backup_pre_deploy.sh
#!/bin/bash
set -euo pipefail
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups/cogme"
mkdir -p "$BACKUP_DIR"

# 1. Dump PostgreSQL (custom format, compressed)
docker compose exec -T db pg_dump -U "$POSTGRES_USER" -d "$POSTGRES_DB" -Fc -Z9 > "$BACKUP_DIR/cogme_pre_deploy_${TIMESTAMP}.dump"

# 2. Backup volumes Docker (db data) — opcional, se espaço
# docker run --rm -v cogme_pgdata:/data -v "$BACKUP_DIR":/backup alpine tar czf /backup/pgdata_${TIMESTAMP}.tar.gz -C /data .

# 3. Retenção: manter últimos 30 backups
find "$BACKUP_DIR" -name "cogme_pre_deploy_*.dump" -mtime +30 -delete

echo "Backup salvo: $BACKUP_DIR/cogme_pre_deploy_${TIMESTAMP}.dump"
```

### 6.2 Backup Agendado (Diário — Cron no Host)

```bash
# /etc/cron.d/cogme-backup
0 3 * * * root /opt/cogme/scripts/daily_backup.sh >> /var/log/cogme-backup.log 2>&1
```

```bash
# scripts/daily_backup.sh (similar ao pré-deploy, com tag "daily")
```

### 6.3 Restore (Procedimento)

```bash
# scripts/restore_db.sh
#!/bin/bash
set -euo pipefail
BACKUP_FILE="${1:?Uso: restore_db.sh <arquivo.dump>}"

# 1. Parar aplicação (manter DB)
docker compose stop back front proxy

# 2. Drop + Recreate DB (limpo)
docker compose exec -T db psql -U "$POSTGRES_USER" -c "DROP DATABASE IF EXISTS \"$POSTGRES_DB\"; CREATE DATABASE \"$POSTGRES_DB\";"

# 3. Restore
docker compose exec -T db pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" -Fc < "$BACKUP_FILE"

# 4. Subir aplicação
docker compose up -d back front proxy

# 5. Smoke tests
./scripts/smoke_tests.sh

echo "Restore concluído de $BACKUP_FILE"
```

### 6.4 Testes de Restore (Validação Obrigatória)

| Teste | Frequência | Critério |
|---|---|---|
| Restore backup pré-deploy em staging | **Por Release** (Gate 3) | Dados íntegros; smoke tests pass; < 10 min |
| Restore backup diário em ambiente isolado | **Mensal** | Dados íntegros; contagem registros confere; < 15 min |

---

## 7. MANUTENÇÃO PROGRAMADA

| Atividade | Frequência | Procedimento | Janela | Responsável |
|---|---|---|---|---|
| **Atualização Imagens Base** | Semanal | `docker compose pull` + rebuild `--no-cache` + deploy staging + smoke tests | Dom 02:00-04:00 | agent-devops |
| **Atualização Dependências (pip/npm)** | Quinzenal | `pip-audit` / `npm audit` → PR com updates → CI green → merge | Qua 10:00-12:00 | agent-backend-dev / agent-frontend-dev |
| **Rotação Segredos** | 90 dias | Gerar novas chaves → atualizar `.env` → rebuild → deploy | Conforme calendário | agent-digital-security |
| **Limpeza Logs Antigos** | Mensal | `find /var/log/cogme -mtime +30 -delete` + Docker log rotation | Primeiro dia do mês | agent-devops |
| **Revisão Runbook** | Por Release / Incidente | Atualizar lições aprendidas; validar procedimentos | Pós-release / Pós-incidente | agent-devops |

---

## 8. CONTATOS DE ESCALAÇÃO (Plantão)

| Nível | Nome | Cargo | Contato (Discord/Telefone/E-mail) | Disponibilidade |
|---|---|---|---|---|
| **Nível 1** | Equipe Core | Devs/QA | Discord #plantao | Horário útil |
| **Nível 2** | GP Leonardo | Tech Lead / GP | Discord @leonardosetti / Telefone | 24/7 (crítico) |
| **Nível 3** | CCB (GP único) | Decisor Final | Mesmo acima | 24/7 (crítico) |
| **Externo** | FATEC Coordenação | Governança Acadêmica | E-mail institucional | Horário útil |
| **Externo** | BCB / Frankfurter | APIs Externas | Canais oficiais suporte | Conforme SLA público |

---

## 9. CONTROLE DE VERSÕES

| Versão | Data | Autor | Mudança | Aprovação |
|---|---|---|---|---|
| 1.0.0 | 2026-11-14 | agent-devops | Criação inicial (baseado no template aprovado) | GP (CCB) — Gate 3 |

---

> **Validação Gate 3**: Este runbook deve ser **simulado em staging** (deploy → rollback → restore) antes da primeira release de produção. Evidência registrada em `docs/operacao/rollback-simulations/`.