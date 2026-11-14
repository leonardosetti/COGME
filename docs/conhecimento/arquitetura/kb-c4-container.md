---
id: docs-arquitetura-c4-container
title: "Diagrama C4 — Nível 2: Contêineres (Container Diagram)"
type: conhecimento
version: 1.0.0
status: ativo
owner: agent-architect
derived-from:
- ADR-001 (Stack Tecnológica FOSS)
- ADR-010 (Stack Infraestrutura)
- constitution.md Art. 10 (Infraestrutura e Isolamento)
- README.md §8 (Arquitetura)
- C4 Model (Simon Brown) — https://c4model.com/
last-revised: '2026-11-14'
lgpd-class: n/a
tags:
- arquitetura
- c4
- containers
- diagramas
---

# Diagrama C4 — Nível 2: Contêineres (Container Diagram)

> **Finalidade**: Mostra a **decomposição do sistema COGME em contêineres executáveis** (aplicações, bancos de dados, proxies), suas **tecnologias**, **comunicação** (protocolos, portas) e **isolamento de rede**.
> **Público**: Equipe técnica (Devs, DevOps, Arch, DBA, Security), auditores técnicos.
> **Ferramenta**: Mermaid.js.

---

## 1. Diagrama de Contêineres (Mermaid)

```mermaid
C4Container
title Diagrama de Contêineres — COGME

Enterprise_Boundary(b0, "Host Físico (Ryzen 7 8700G + 60GB RAM)") {
    System_Boundary(s1, "Rede Docker: cogme-internal (Isolada, Sem Internet)") {
        Container(db, "PostgreSQL 15+", "Docker Image: postgres:15-alpine", "Banco de dados canônico\nTabelas: fx_quotes, invoices, users (M2+)\nPorta: 5432 (apenas rede interna)\nVolume: pgdata (persistência)\nUsuário: não-root (UID 999)")
        
        Container(migrate, "Alembic Migrations", "Docker Image: cogme-backend:latest\nCommand: alembic upgrade head", "Migrações de schema (init container)\nExecuta antes do backend subir\nIdempotente, forward-only\nAcesso: DB (rede interna)")
        
        Container(back, "Backend API (FastAPI)", "Docker Image: cogme-backend:latest\nPython 3.12 + FastAPI + Uvicorn\nPorta: 8000 (apenas rede interna)\nUsuário: não-root (UID 10001)\nHealth: GET /health", "Rotinas: /v1/rates, /v1/simulate, /v1/invoice\nCache: fx_quotes (PostgreSQL)\nExterno: Frankfurter API, PTAX/BCB\nAuth: Argon2id (M2+), JWT (M2+)\nObservabilidade: /health, /metrics, logs estruturados")
        
        Container(front, "Frontend (Nginx + Jinja2)", "Docker Image: cogme-frontend:latest\nNginx (static) + Jinja2 Templates\nPorta: 8080 (apenas rede interna)\nUsuário: não-root (UID 10001)\nHealth: GET /", "UI: Simulador, Invoice View, History (M4+)\nTech: Jinja2 + HTMX + Tailwind (sem build step)\nSame-origin com Backend (via Proxy)\nAssets: CSS/JS servidos pelo Nginx")
    }
    
    System_Boundary(s2, "Rede Docker: cogme-external (Acesso Externo)") {
        Container(proxy, "Nginx Reverse Proxy", "Docker Image: nginx:alpine\nPorta Host: 8080 (0.0.0.0)\nPorta Container: 80\nConfig: nginx.conf (rate limit, headers, SSL term)\nUsuário: não-root (UID 101)", "Terminação TLS (se certificado)\nRoteamento: / → front, /v1/* → back\nHeaders segurança: CSP, HSTS, X-Frame-Options\nRate limiting: 100 req/min / IP\nAccess log + Error log")
    }
}

System_Ext(frankfurter, "Frankfurter API", "Primária: https://api.frankfurter.app\nREST/HTTPS\nCache-Control headers\nSem autenticação\nRate limit público")
System_Ext(ptax, "PTAX / BCB", "Fallback: https://olinda.bcb.gov.br/...\nREST/HTTPS (OData)\nAutenticação: Nenhuma (pública)\nFonte oficial brasileira")
System_Ext(tailscale, "Tailscale", "Overlay Network (WireGuard)\nTailnet: dispositivos autorizados\nAcesso: IP Tailscale:8080 → Proxy\nZero exposição internet pública")

Rel_L(proxy, front, "Encaminha", "HTTP/1.1 (porta 8080 container front)")
Rel_R(proxy, back, "Encaminha", "HTTP/1.1 (porta 8000 container back)\nPath: /v1/*")
Rel_D(back, db, "Lê/Escreve", "PostgreSQL Async (asyncpg)\nPool: 20 conexões\nSchema: public")
Rel_U(migrate, db, "Migra", "PostgreSQL (psycopg2)\nAlembic upgrade head")
Rel_D(back, frankfurter, "Consulta", "HTTPS/REST\nTimeout: 5s\nCircuit Breaker: 5 falhas → OPEN")
Rel_D(back, ptax, "Consulta (fallback)", "HTTPS/REST\nTimeout: 10s\nApenas se CB OPEN")
Rel_D(user, tailscale, "Conecta", "WireGuard/Overlay\nAcesso remoto autorizado")
Rel_D(tailscale, proxy, "Encaminha", "TCP/8080 (host) → Proxy container")
```

---

## 2. Tabela de Contêineres

| Contêiner | Tecnologia | Porta Interna | Porta Host | Rede | Usuário | Health Check | Responsabilidade Principal |
|---|---|---|---|---|---|---|---|
| **db** | PostgreSQL 15 Alpine | 5432 | — (apenas interna) | `cogme-internal` | 999 (postgres) | `pg_isready -U $POSTGRES_USER` | Persistência canônica (fx_quotes, invoices, users) |
| **migrate** | Python 3.12 + Alembic | — | — | `cogme-internal` | 10001 (app) | Exit code 0 | Migrações de schema (idempotente, forward-only) |
| **back** | FastAPI + Uvicorn | 8000 | — (apenas interna) | `cogme-internal` | 10001 (app) | `GET /health` (200 OK) | API REST: rates, simulate, invoice, health, metrics |
| **front** | Nginx + Jinja2 | 8080 | — (apenas interna) | `cogme-internal` | 10001 (app) | `GET /` (200 OK) | UI Server-side: templates, assets estáticos (CSS/JS) |
| **proxy** | Nginx Alpine | 80 | **8080 (0.0.0.0)** | `cogme-internal` + `cogme-external` | 101 (nginx) | `GET /health` (200 OK) | Reverse proxy, TLS termination, rate limiting, routing |

---

## 3. Comunicação e Protocolos

| Origem | Destino | Protocolo | Porta | Autenticação | Observações |
|---|---|---|---|---|---|
| **Usuário (Browser)** | **Proxy** | HTTPS (TLS) / HTTP | 8080 (host) | Nenhuma (MVP) | Via Tailscale IP; Same-origin |
| **Proxy** | **Frontend** | HTTP/1.1 | 8080 (container) | Nenhuma | Path `/` → front |
| **Proxy** | **Backend** | HTTP/1.1 | 8000 (container) | Nenhuma (MVP) | Path `/v1/*` → back |
| **Backend** | **PostgreSQL** | PostgreSQL (asyncpg) | 5432 | User/Pass (env) | Pool 20 conn; SSL mode prefer |
| **Backend** | **Frankfurter** | HTTPS/REST | 443 | Nenhuma | Timeout 5s; CB 5 falhas |
| **Backend** | **PTAX/BCB** | HTTPS/REST (OData) | 443 | Nenhuma | Timeout 10s; Apenas fallback |
| **Migrate** | **PostgreSQL** | PostgreSQL (psycopg2) | 5432 | User/Pass (env) | Init container; `alembic upgrade head` |

---

## 4. Isolamento e Segurança (Defense in Depth)

| Camada | Controle | Implementação |
|---|---|---|
| **Rede** | Segmentação Docker | `cogme-internal` (sem internet) + `cogme-external` (apenas proxy) |
| **Host** | Usuários não-root | Todos containers: UID 10001 (app) / 999 (postgres) / 101 (nginx) |
| **Imagem** | Base images por digest | `postgres:15-alpine@sha256:...`, `python:3.12-slim@sha256:...` |
| **Build** | `--no-cache` | Evita segredos em layers; rebuild limpo a cada deploy |
| **Segredos** | Runtime only (`.env`) | `.env` não versionado; injetado via `docker compose --env-file` |
| **TLS** | Terminação no Proxy | Certificados em volume `nginx-certs`; renovação Let's Encrypt |
| **Headers** | Security Headers | CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy |
| **Rate Limit** | Nginx | `limit_req_zone` 100 req/min/IP; burst 20 |
| **Acesso Externo** | Tailscale Only | Zero portas expostas na internet; apenas tailnet autorizada |

---

## 5. Decisões Arquiteturais Relacionadas (ADRs)

| ADR | Título | Impacto nos Contêineres |
|---|---|---|
| **ADR-001** | Stack Tecnológica FOSS | Define: Python/FastAPI (back), PostgreSQL (db), Nginx/Jinja2/HTMX/Tailwind (front), Docker Compose (orquestração) |
| **ADR-010** | Stack Infraestrutura | Define: PostgreSQL canônico (não SQLite), Docker Compose + Nginx proxy, hierarquia APIs (Frankfurter + PTAX) |
| **ADR-003** | Métricas de Fluxo | Backend expõe `/health/metrics` para coleta |
| **ADR-017** | Dependência Argon2id | Backend usa Argon2id para hash de senha (M2+) |
| **ADR-019** | Segurança Multiusuário | Backend implementa isolamento de dados, HMAC lookup, criptografia (M2+) |

---

## 6. Como Visualizar / Atualizar

1. **No GitHub**: Arquivo `.md` renderiza automaticamente o Mermaid
2. **No VS Code**: Extensão "Markdown Preview Mermaid Support"
3. **CLI**: `mmdc -i c4-container.md -o c4-container.png`

> **Atualização**: Sempre que houver mudança de contêiner, tecnologia, porta, rede, ou protocolo. Revisão obrigatória em Gate 2 (Desenho) de cada wave.