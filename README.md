---
id: readme
title: COGME — Conversor de Ganhos em Moeda Estrangeira
type: readme
version: 1.0.1
status: ativo
owner: agent-project-analyst
derived-from:
- README.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- ''
- docs
- adequado-a-norma
---
# COGME — Conversor de Ganhos em Moeda Estrangeira

[![COGME CI/CD Pipeline](https://github.com/leonardosetti/COGME/actions/workflows/ci.yml/badge.svg)](https://github.com/leonardosetti/COGME/actions/workflows/ci.yml)
[![SDDAI Verify Pipeline](https://github.com/leonardosetti/COGME/actions/workflows/sddai-verify.yml/badge.svg)](https://github.com/leonardosetti/COGME/actions/workflows/sddai-verify.yml)

Projeto acadêmico FOSS de conversão cambial, desenvolvido na disciplina de Gerência de Projetos da Fatec Taquaritinga, com entrega final prevista em 15/12/2026 e marcos M1–M4.

---

## 1. Caracterização do projeto

| Item | Dado |
|------|------|
| Nome | COGME — Conversor de Ganhos em Moeda Estrangeira |
| Natureza | Conversor cambial FOSS, gratuito, jurisdição brasileira |
| Licença | MIT (stack 100% FOSS, custo recorrente zero) |
| Contexto acadêmico | Gerência de Projetos — Fatec Taquaritinga |
| Stakeholder-avaliador canônico | Conforme ADR-008 (papel registrado na Constituição) |
| Escopo canônico | Simulação cambial, comparação de regimes de contratação, spread/IOF, emissão de invoice PDF |
| EAP canônica | 12 fases e 37 pacotes de trabalho (TAP v3 §4 + ADR-009) |
| Marcos | M1–M4; entrega final 15/12/2026 |
| Status da Constituição | v1.2.0 — VIGENTE-PLENA (ratificada 30/10/2026, co-assinatura humana via CCB) |
| Versão da diretriz de forja de agentes | AFA-ULTIMATE v1.3.0-FINAL |

### 1.1 Objetivos do projeto

**Objetivo geral.** Conversor de ganhos em moeda estrangeira (USD/EUR → BRL), gratuito, FOSS, de jurisdição brasileira (LGPD primária), entregue como disciplina de Gerência de Projetos (Fatec Taquaritinga), com marcos M1–M4 e entrega final em 15/12/2026. Stakeholder-avaliador canônico: Prof. Dr. Nivaldo Carleto (ADR-008).

**Objetivos específicos** (escopo canônico — Constituição Art. 1.2 / TAP v3 §4):

- Simulação cambial de recebimentos, com comparação de regimes de contratação (fixo e por hora, entre os 5 regimes do escopo).
- Cálculo de spread e IOF informados pelo usuário; nenhuma alíquota embutida no código (aviso fixo em toda resposta de simulação).
- Emissão de invoice PDF (WeasyPrint), com persistência opcional, download/impressão e rota de erase (LGPD art. 18).
- Rastreabilidade de decisões via ADR, cobertura de testes ≥ 80%, segurança OWASP com fail-closed.
- Zero custo recorrente, soberania computacional local (`llama.cpp`, CPU-only, sem CUDA/nuvem) e ausência de telemetria/lock-in.

---

## 2. Governança aplicada

### 2.1 Hierarquia normativa (ordem absoluta)

Em caso de conflito, prevalece a camada superior:

1. `constitution.md` (lei suprema do projeto)
2. TAP v3, congelado pela ADR-005 (ato autorizativo de escopo, marcos, orçamento e restrições)
3. ADRs aprovadas (`docs/decisoes/`)
4. OKB (base consolidada de conhecimento operacional, sem autonomia normativa própria)
5. Planos de gerenciamento (`docs/planos/`)
6. Glossário
7. Especificações SDD e inputs canônicos (`.ai/specs/`)
8. Código-fonte e testes (`src/`, `tests/`)

### 2.2 Método e princípios

- **Governança primária:** PMBOK® 7ª edição (princípios e domínios de desempenho). O PMBOK® 6ª edição atua apenas como dicionário terminológico.
- **Execução:** Kanban em GitHub Projects como SSOT de execução (Backlog → Ready → In Progress, WIP ≤ 3 → Code Review → Done).
- **Metodologia de desenvolvimento:** SDD (Spec-Driven Development): especifica → implementa → valida → registra.
- **Princípios inalienáveis (Art. 3 da Constituição):** FOSS-zero-custo, soberania computacional local, soberania de dados, LGPD primária, rastreabilidade de decisões (ADR), qualidade fechada (coverage ≥ 80%), segurança OWASP com fail-closed, honestidade intelectual (alegação sem fonte = knowledge gap), anti-subutilização de papéis, linguagem (identificadores em EN, narrativa humana em PT-BR), YAGNI e primeiros princípios.

### 2.3 Privacidade e proteção de dados

- LGPD é a legislação primária (P-04): mínimo necessário, sem PII em artefatos técnicos de agentes, direito ao esquecimento por design.
- Zero Trust por padrão; princípio do menor privilégio.
- Nenhuma credencial real é versionada. Apenas chaves dummy para serviços locais.
- Dados demonstrativos não contêm dados reais de terceiros sem consentimento documentado.
- Nenhuma telemetria, rastreio ou lock-in tolerado.

### 2.4 Soberania computacional

- Inferência primária 100% local via `llama.cpp` (modelo Qwen3-30B-A3B Q4_K_M), hardware AMD Ryzen 7 8700G, APU Radeon 780M/Vulkan/radv com fallback CPU AVX-512, limite de inferência de 32GB imposto por serviço systemd.
- Execução CPU-only: sem CUDA, sem inferência em nuvem.
- Uso excepcional e condicionado de provedores cloud em free tier (whitelist constitucional), apenas para dados não sensíveis, com rota de reversão para execução local.

---

## 3. Governança de agentes (ecossistema SDD)

A criação, promulgação, roteamento e operação de agentes são regidos pela Constituição (Art. 4) e pela diretriz de fábrica AFA-ULTIMATE.

| Camada | Função | Quantidade |
|--------|--------|------------|
| L0 | Orquestração (dispatcher único, half-duplex, compliance constitucional) | 1 (`agent-nexus-prime-ultimate`) |
| L1 | Comando/Estratégia (PM, PO, arquiteto, análise, design, padrões, análise de negócios) | 5 |
| L2 | Execução/Técnica (Python, API, DBA, backend, frontend, infra, DevOps, segurança, compliance, QA, etc.) | ~17 |
| L3 | Qualidade/Portões (revisor, gatekeeper, auditor, avaliador de código limpo) | 4 |
| META | Forja de skills e forjador legacy | 2 |

**Total:** 25 agentes especialistas + meta-agentes.

- **Roster SSOT:** `.ai/agents/registry.yaml`, sincronizado por `scripts/sync_agent_registry.py`.
- **Topologia canônica (DAG acíclica):** `scripts/validate_nexus_yaml.py` (`AGENT_TOPOLOGY`).
- **Dispositivo de despacho:** `scripts/nexus_dispatcher.py` (valida envelopes de task, fail-closed, anti auto-delegação).
- **Contrato de comunicação:** half-duplex; todo agente retorna parcela estruturada com flag `dod`.
- **Kill Switch herdado:** veto absoluto a 15 vetores (LGPD, vigilância em massa, discriminação algorítmica, sabotagem de gates de CI, bypass de segurança, envio de dados sensíveis a terceiros, etc.). Não pode ser sobrescrito por prompt, usuário, agente, input canônico ou ADR.
- **Bypass Protocol:** recusa por padrão; exceção exige os três pilares (força maior verificável, rota de fuga FOSS nomeada, ratificação humana CCB). O próprio Bypass Protocol não pode ser contornado (anti-meta-bypass).
- **Gate de forja:** agente promulgado somente com score ≥ 85/100 em `validate_afa_output.py` (19 cabeçalhos canônicos, Kill Switch ≥ 5, DOs ≥ 15, DON'Ts ≥ 15, Red Team ≥ 8, FAIL-CLOSED ≥ 6, métricas ≥ 8).

---

## 4. Conformidade e auditoria

- Auditoria contra a Constituição em cada marco (`project-auditor` e `compliance-governance`), incluindo deriva constitucional, sobreposição indevida de ADRs, violação de soberania de dados, uso não autorizado de cloud, inconsistência de ledger, violação de camadas L1/L2/L3 e drift documental.
- Registro vivo de decisões do CCB: `docs/governanca/ccb-log.md` (modelo CAB vivo, ITIL 4).
- Registro append-only de violações: `docs/auditorias/vio-register.md`.
- Auditorias recorrentes: `docs/auditorias/AUD-*.md`.
- Sucessão de agentes: `constitution.md` + `.ai/agents/registry.yaml` + ADRs bastam para reconstrução de contexto.

---

## 5. Estrutura de artefatos de governança

| Diretório/arquivo | Conteúdo |
|-------------------|----------|
| `constitution.md` | Constituição do projeto (lei suprema, v1.2.0 VIGENTE-PLENA) |
| `docs/decisoes/ADR-001..012.md` | Decisões técnicas e de processo aprovadas |
| `docs/planos/` | Planos de gerenciamento (escopo, cronograma, custos, qualidade, riscos, comunicações, integração, recursos, consolidação estrutural, produção de agentes) |
| `docs/auditorias/` | Relatórios de auditoria e registro de violações |
| `docs/governanca/ccb-log.md` | Registro vivo de decisões do Change Advisory Board |
| `docs/conhecimento/OKB.md` | Base consolidada de conhecimento operacional |
| `docs/conhecimento/licoes-aprendidas/` | Lições aprendidas por macro-fase (MF1, MF2, MF3) |
| `docs/conhecimento/glossario.md` | Glossário canônico |
| `.ai/agents/registry.yaml` | Roster SSOT de agentes |
| `.ai/agents/ledger.yaml` | Ledger operacional de sessão (append-only, LGPD-safe, sem PII) |
| `.ai/handoffs/` | Handoffs SDD (parseados por `handoff_parser.py`) |
| `.ai/specs/` | Especificações SDD e inputs canônicos |
| `.ai/personas/` | Personas do modelo (camada L2) |
| `scripts/` | Scripts mediadores de governança (dispatcher, validação, sincronização, parser de handoffs, validação de saída AFA, etc.) |
| `tests/agents/` | Suites de teste dos scripts de governança |
| `src/` | Backend do MVP: `backend/` (FastAPI, rotas `/v1`, cálculo, cotações, PDF), `shared/` (schemas do contrato) e `frontend/templates/` (template da invoice) |
| `migrations/` | Migrações Alembic do banco (tabela `fx_quotes`, cache de cotações) |
| `infra/` | Configuração de infraestrutura; hoje, `infra/nginx/`, do proxy reverso latente |
| `Dockerfile` | Imagem do backend: Python 3.12 slim, usuário sem privilégios, bibliotecas nativas do WeasyPrint |
| `docker-compose.yml` | Stack local: `db` (PostgreSQL 15), `migrate`, `web` e `proxy` opcional (`--profile proxy`) |

---

## 6. Stack e ambiente (caracterização técnica não sensível)

- Linguagem: Python 3.11+ (imagem e CI usam 3.12)
- Stack: FastAPI + PostgreSQL 15+ (Docker Compose) + Nginx (reverse proxy latente)
- Banco de dados: PostgreSQL 15+ (containerizado via Docker Compose)
- Interface: templates server-side (Jinja), HTMX, Tailwind (classes utilitárias comitadas, sem build chain, sem CDN-first)
- Testes: pytest, meta de cobertura ≥ 80%
- CI/CD: GitHub Actions Free Tier (bypass registrado, dados não sensíveis)
- Inferência de IA: local, CPU-only, `llama.cpp`, sem CUDA, sem nuvem

### 6.1 Como executar o backend

**Com Docker Compose (caminho recomendado).** Pré-requisito: Docker com o plugin Compose.

1. Copie o exemplo de configuração e troque os valores dummy:

   ```bash
   cp .env.example .env
   ```

   No PowerShell: `Copy-Item .env.example .env`.

   Troque `POSTGRES_PASSWORD` e use a mesma senha em `COGME_DATABASE_URL`. Se a senha tiver caracteres especiais, codifique-os na URL (percent-encoding). O `.env` é ignorado pelo Git e não deve ser versionado.

2. Suba a stack:

   ```bash
   docker compose up --build
   ```

   O serviço `migrate` aplica as migrações (`alembic upgrade head`) e termina antes de `web` iniciar. A API fica em `http://127.0.0.1:8000`. As portas são publicadas só em `127.0.0.1`, e o banco não tem porta no host.

   O proxy reverso (Nginx) sobe sempre ativo em `http://127.0.0.1:8080` com `docker compose up --build`.

**Rotas (`/v1`).**

| Método | Rota | Descrição |
|---|---|---|
| GET | `/v1/health` | Estado do serviço |
| GET | `/v1/rates/{currency}` | Cotação em BRL (`USD` ou `EUR`) |
| POST | `/v1/simulate` | Simulação de recebimento |
| POST | `/v1/invoice` | Invoice em PDF, como anexo |

Todo erro segue o mesmo modelo: `{"error": {"key": "...", "message": "...", "details": [...]}}`.

**Exemplo com dados sintéticos** (bash):

```bash
curl -s http://127.0.0.1:8000/v1/rates/USD

curl -s -X POST http://127.0.0.1:8000/v1/simulate \
  -H "Content-Type: application/json" \
  -d '{"currency":"USD","regime":"hourly","amount":"30.00","quantity":"160","spread_pct":"2.00","iof_pct":"0.38"}'
```

No PowerShell, use `curl.exe` (o alias `curl` chama `Invoke-WebRequest`) e escape as aspas do JSON.

Spread e IOF são informados por quem faz a simulação; o backend não tem alíquota. A cotação vem da fonte no momento da chamada. A resposta traz `quote.source` (`frankfurter` ou `ptax`) e, na PTAX, `quote.bulletin`. Se `quote.stale` for `true`, a cotação veio de cache vencido, obtido em consulta anterior; `quote.quoted_at` indica a data da cotação.

**Migrações.** Pelo Compose, são automáticas. Fora dele, com o banco acessível (troque pelos seus valores):

```bash
COGME_DATABASE_URL='postgresql+asyncpg://usuario:senha@127.0.0.1:5432/cogme' alembic upgrade head
```

`alembic downgrade -1` desfaz a última revisão. A revisão `0001` remove a tabela de cotações em cache, que é reobtida das fontes.

**Testes.**

```bash
python -m pip install -r requirements-dev.txt
python -m pytest tests/unit tests/integration --cov=src --cov-fail-under=80
```

- Os testes de integração com PostgreSQL (marcador `postgres`) são pulados sem `COGME_TEST_DATABASE_URL`. Aponte essa variável para um banco descartável, nunca para dados reais.
- Em Windows, defina `PYTHONUTF8=1` antes de rodar `tests/agents`, que não está no comando acima. No PowerShell: `$env:PYTHONUTF8 = "1"`.
- A CI roda `pytest tests/` com um PostgreSQL efêmero (ver `.github/workflows/ci.yml`).

**WeasyPrint e Pango.** A invoice é gerada com WeasyPrint, que depende das bibliotecas nativas Pango e HarfBuzz. Sem elas, a API sobe normalmente, mas `POST /v1/invoice` responde 503 `pdf_unavailable`. Por isso a geração real do PDF roda no container, que instala essas bibliotecas; o CI também as instala. No Windows, sem GTK/Pango instalado, a rota de invoice não gera PDF localmente.

### 6.2 Hook post-commit (opcional)

Após cada commit local, pode executar a verificação de CI local
(`scripts/ci_post_commit_check.py`) e, após push bem-sucedido, reescrever o
README com versão e governança (`scripts/atualizar_readme_governanca.py`).
O hook não é versionado pelo Git; ative manualmente em cada clone:

```sh
cp scripts/githooks/post-commit .git/hooks/post-commit
chmod +x .git/hooks/post-commit
```

O hook não bloqueia o commit. Apenas avisa quando flake8, pytest, frontmatter,
nomenclatura de `.md`, SDDAI verify ou security scan falharam.

Para publicar após um push bem-sucedido, rode:

```sh
./scripts/publicar_pos_push.sh
```

Ele executa a sanidade de CI (até 5 tentativas). Se passar, reescreve o
README (bump de versão + `last-revised`), comita e push. Se esgotar as
tentativas, anota a falha na seção `## Falha de pipeline (último push)` do
README e encerra com erro.

A variável `COGME_README_REWRITING=1` pula o hook na reescrita automática do
README e evita recursão infinita entre commit e reescrita.

---

## 7. Convenções

- Identificadores, slugs, código e contratos: **EN**, kebab-case com prefixo `agent-` para agentes.
- Narrativa estratégica, documentação humana e mensagens visíveis ao humano: **PT-BR**.
- Nunca publicar dados sensíveis, credenciais reais, PII ou detalhes estratégicos de execução neste README.

## 8. Arquitetura

Separação de camadas Dados / Back / Front (ADR-010), orquestradas via Docker Compose.

| Camada | Tecnologia | Papel |
| Dados | PostgreSQL 15+ (Docker) | Tabelas `fx_quotes` (cache de cotações) e `invoices`; SQLite só como fixture de teste isolado |
| Back | FastAPI, Python 3.11+ (imagem 3.12 slim, usuário sem privilégios) | Rotas `/v1` (health, rates/{currency}, simulate, invoice), cálculo em `Decimal`, cotação Frankfurter (primária) + PTAX (fallback), circuit breaker, contrato de erro padronizado |
| Front | HTML5 + CSS3 + JS vanilla, Jinja, HTMX, Tailwind (sem build chain, sem CDN-first) | Templates `index.html` e `invoice.html`, servidos na mesma origem (sem CORS) |
| Orquestração | Docker Compose (`db`, `migrate`, `web`, `proxy` opcional) + Nginx reverso latente (porta 8080) | Paridade dev/test/prod; banco sem rota para internet, apenas `web` publica porta em `127.0.0.1` |
| IA / agentes | `llama.cpp`, Qwen3-30B-A3B Q4_K_M, CPU-only (AMD Ryzen 7 8700G), fallback AVX-512, limite 32 GB | Inferência local para o ecossistema SDD; sem CUDA, sem nuvem |

Diagrama da arquitetura lógica: `docs/diagramas/desenvolvimento/fig-3-2-arquitetura-logica.png`.

Rotas detalhadas e exemplo de chamada: seção 6.1.

## 9. Métricas de fluxo

Substituem EVM/SPI/CPI (ADR-003; orçamento zero e escopo emergente tornam EVM indeterminado). Fonte: GitHub Insights / GitHub Projects (SSOT), sem stack de observabilidade dedicada.

| Métrica | Fórmula | Meta | Frequência |
| Cycle Time | Média (`Done − In Progress`) | ≤ 3 dias | Semanal |
| Throughput | Cards concluídos / semana | ≥ 5 cards | Semanal |
| WIP em fluxo | Cards em `In Progress` | ≤ 9 (3 × 3 pessoas) | Contínuo |
| Coverage | Linhas testadas / totais | ≥ 80% | Por push (CI) |

⚠️ Os valores de baseline em `docs/metricas/baseline.md` são **seeds simulados** (período de calibração 23/09–03/10 sem dados reais) e serão recalibrados com dados empíricos do GitHub Projects a partir de 01/11/2026.

## 10. Referências públicas

Artefatos públicos para rastreamento direto:

- Repositório: https://github.com/leonardosetti/COGME
- CI/CD — COGME CI/CD Pipeline: https://github.com/leonardosetti/COGME/actions/workflows/ci.yml
- SDDAI Verify Pipeline: https://github.com/leonardosetti/COGME/actions/workflows/sddai-verify.yml
- Kanban / Projects (SSOT de execução, Backlog → Done, WIP ≤ 3): https://github.com/leonardosetti/COGME/projects
- Issues / backlog: https://github.com/leonardosetti/COGME/issues
- Releases: https://github.com/leonardosetti/COGME/releases

---

*Documento de caracterização e governança. Não contém dados sensíveis nem estratégicos. Regido por `constitution.md` Art. 2 (hierarquia normativa) e Art. 3 (princípios inalienáveis).*
