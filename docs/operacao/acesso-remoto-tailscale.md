---
id: docs-operacao-acesso-remoto-tailscale
title: Acesso Remoto ao COGME via Tailscale (tailnet)
type: procedimento
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/operacao/acesso-remoto-tailscale.md (criado em 2026-11-06)
last-revised: '2026-11-06'
lgpd-class: n/a
tags:
- operacao
- tailscale
- acesso-remoto
- demo
- live-run
---
# Acesso Remoto ao COGME via Tailscale (tailnet)

Este documento descreve como acessar o COGME (**live run, demo, APIs, containers**) a partir de **qualquer máquina da sua tailnet** (Tailscale), sem expor nada na internet pública.

O comportamento é o mesmo das rodadas locais de implementação e testes: você sobe a stack em uma máquina (host) e acessa de outra máquina da mesma tailnet pelo IP privado do Tailscale (`100.x.y.z`).

---

## 1. Como funciona (visão geral)

O `docker-compose.yml` já publica as portas do host em **`0.0.0.0`** (todas as interfaces de rede, incluindo a interface do Tailscale), não só em `127.0.0.1`. Por isso, qualquer máquina da mesma tailnet alcança os serviços diretamente pelo IP privado (`100.x.y.z`) da máquina host.

| Serviço | Porta publicada (host) | Acessível via Tailscale | Observação |
|---------|------------------------|-------------------------|------------|
| `proxy` (Nginx — entrada única) | `0.0.0.0:8080:80` | ✅ `http://<ip-ts>:8080` | UI + API `/v1/*`. Caminho recomendado. |
| `front` (UI direta) | `0.0.0.0:8001:8000` | ✅ `http://<ip-ts>:8001` | Front direto (Jinja2/HTMX, mesma origem). |
| `db` (PostgreSQL) | `0.0.0.0:5432:5432` | ✅ `<ip-ts>:5432` | Só se precisar do banco direto. |
| `back` (FastAPI/Uvicorn) | — (nenhuma porta no host) | Indireto | Só dentro da rede interna `edge`; alcançado via `proxy` ou `front`. |

O serviço `back` (porta 8000) **não publica porta no host** intencionalmente: reduz a superfície de ataque (fail-closed, menor privilégio). Ele é alcançado apenas através do `proxy` (`/v1/*`) ou do `front`.

---

## 2. Pré-requisitos

| Item | Detalhe |
|------|---------|
| Tailscale | Instalado e autenticado (`tailscale up`) em **todas** as máquinas da tailnet, na mesma rede (tailnet) |
| Docker | Com o plugin Compose (`docker compose`) na máquina host que vai rodar o COGME |
| Repositório | Clone do COGME na máquina host |
| `.env` | Copiado de `.env.example` com senhas trocadas (não versionado) |

Confira que as máquinas enxergam umas às outras na tailnet:

```bash
# Na máquina host
tailscale ip            # ex.: 100.98.53.79
tailscale status        # lista as máquinas da tailnet e seus IPs
```

---

## 3. Passo a passo — subir o COGME e acessar da tailnet

### 3.1 Na máquina host (onde o COGME roda)

```bash
# 1. Entre na raiz do repositório
cd /caminho/para/COGME

# 2. Crie o .env a partir do exemplo (não versionado pelo Git)
cp .env.example .env

# 3. Edite o .env: troque POSTGRES_PASSWORD e ajuste COGME_DATABASE_URL
#    (use a mesma senha em ambos; com percent-encoding se houver caracteres especiais)

# 4. Suba a stack
docker compose up --build
```

Aguarde até que `proxy`, `front`, `back` e `db` reportem `healthy` (`docker compose ps`).

### 3.2 Descubra o IP do Tailscale da máquina host

```bash
tailscale ip
# Saída exemplo: 100.98.53.79
```

### 3.3 De qualquer outra máquina da tailnet

Abra o navegador ou use `curl`, substituindo `<IP-TAILSCALE-HOST>` pelo IP da máquina host:

```bash
# Interface (UI) — simulação de câmbio e emissão de invoice
curl http://<IP-TAILSCALE-HOST>:8080/

# API — health
curl http://<IP-TAILSCALE-HOST>:8080/v1/health

# API — cotação (USD ou EUR)
curl http://<IP-TAILSCALE-HOST>:8080/v1/rates/USD

# API — simulação
curl -s -X POST http://<IP-TAILSCALE-HOST>:8080/v1/simulate \
  -H "Content-Type: application/json" \
  -d '{"currency":"USD","regime":"hourly","amount":"30.00","quantity":"160","spread_pct":"2.00","iof_pct":"0.38"}'
```

No navegador, acesse `http://<IP-TAILSCALE-HOST>:8080/` para a UI completa.

---

## 4. Demo / live run em rodadas de implementação e testes

Use o mesmo fluxo das rodadas locais:

1. Host sobe a stack: `docker compose up --build`
2. Anote o IP do Tailscale: `tailscale ip`
3. Compartilhe o IP apenas com quem está na sua tailnet (máquinas de confiança)
4. Acesse `http://<ip-ts>:8080` de qualquer máquina da tailnet
5. Teste as rotas `/v1/health`, `/v1/rates/{currency}`, `/v1/simulate` e `/v1/invoice`

Para reiniciar apenas um serviço (ex.: só o `back`), sem tocar nas demais camadas:

```bash
docker compose restart back
```

Para derrubar tudo:

```bash
docker compose down
```

---

## 5. Segurança (tailnet ≠ internet pública)

- A tailnet é composta apenas por máquinas **suas / de confiança**. Não é exposta na internet pública.
- Mesmo assim, proteja os serviços com senha/auth quando houver (como o OpenCode exige).
- Não exponha o banco (`5432`) nem o front direto (`8001`) além do necessário; prefira entrar pelo `proxy` (`8080`).
- Se precisar expor para a **internet pública** com controle, use o **Tailscale Funnel** (opcional) em vez de abrir portas no roteador/firewall.
- Nunca credenciais reais no repositório: apenas `.env.example` (dummy) é versionado; o `.env` fica fora do Git.
- Zero Trust por padrão; princípio do menor privilégio (Constituição Art. 3).

---

## 6. Troubleshooting

| Sintoma | O que verificar |
|---------|-----------------|
| `conexão recusada` / `timeout` | `docker compose ps` — serviços estão `healthy`? `docker compose logs <serviço>` |
| IP do Tailscale não responde | `tailscale status` nas duas máquinas; ambas logadas na mesma tailnet; `ping <ip-ts>` |
| Porta não alcançável | Confirme que o `docker-compose.yml` usa `0.0.0.0` (não `127.0.0.1`) nas `ports` |
| 503 na invoice | Bibliotecas nativas do WeasyPrint (Pango/HarfBuzz) estão na imagem do container |
| Banco inacessível | `db` publica `5432` em `0.0.0.0`; confira `COGME_DATABASE_URL` e `POSTGRES_*` no `.env` |

---

## 7. Referências

- `README.md` — seção 6.1 (como executar o backend), seção 8 (arquitetura), seção 9 (acesso remoto via Tailscale)
- `docker-compose.yml` — orquestração `db` / `migrate` / `back` / `front` / `proxy`
- `infra/nginx/default.conf` — proxy reverso (`/` → front, `/v1/` → back)
- Tailscale: https://tailscale.com (Funnel para exposição pública opcional)

---

*Documento de operação. Regido por `constitution.md` (hierarquia normativa) e princípios inalienáveis: Zero Trust por padrão, menor privilégio, sem telemetria/lock-in, LGPD primária.*
