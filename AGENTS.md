# COGME — agent instructions

COGME is a FOSS currency-conversion MVP (FastAPI + PostgreSQL 15 + Nginx, Python 3.11+; CI uses 3.12). Academic project, Fatec Taquaritinga.

## Governance (read first)

- `constitution.md` is the project's supreme law; it beats TAP v3, ADRs, OKB, plans, specs, and code in any conflict.
- Development is SDD: especifica → implementa → valida → registra. Specs in `.ai/specs/`; ADRs in `docs/decisoes/`.
- Kill switch: if `kill_switch.trigger` exists, CI halts (Constitution Art. 4.6). Never create it.
- CI never mutates the repo and never writes to `.ai/` (D-06).
- Language: identifiers/code/contracts in **EN**; human docs and user-visible text in **PT-BR**. No PII, real credentials, or secrets in artifacts — dummy keys only for local services.

## Setup

1. `cp .env.example .env` — `.env` is gitignored; never version it. Replace dummy `POSTGRES_PASSWORD` and set `COGME_DATABASE_URL` to match.
2. `docker compose up --build` — `db` (PostgreSQL 15), `migrate` (runs `alembic upgrade head`), `web` (FastAPI at http://127.0.0.1:8000). Ports bound to 127.0.0.1 only.
   - Optional Nginx reverse proxy: `docker compose --profile proxy up --build` → http://127.0.0.1:8080.
3. Outside Compose, with a reachable Postgres: `COGME_DATABASE_URL=... alembic upgrade head`; `alembic downgrade -1` undoes the last revision. `alembic.ini` has no DB URL — `migrations/env.py` reads `COGME_DATABASE_URL` from the environment and fails loudly if absent.

## Developer commands (run from repo root)

| Purpose | Command |
|---------|---------|
| Install dev deps | `python -m pip install -r requirements-dev.txt` |
| Lint (flake8, max-line 100) | `python -m flake8 src migrations tests/unit tests/integration` |
| Type check (mypy, strict) | `python -m mypy src migrations` |
| Dependency audit | `python -m pip-audit` |
| Full test suite | `python -m pytest tests/unit tests/integration --cov=src --cov-fail-under=80` |
| One test / one file | `python -m pytest tests/unit/test_calculator.py -q` |

Order that matters: `lint -> mypy -> test` (CI runs lint + pip-audit in parallel, then test-suite).

- pytest config is in `pyproject.toml` (`pythonpath = ["."]`, asyncio auto, `postgres` marker).
- Real-PostgreSQL integration tests (`postgres` marker) are skipped unless `COGME_TEST_DATABASE_URL` points to a **disposable** database — never real data. CI uses an ephemeral `postgres:15` service.
- WeasyPrint (invoice PDF) needs native Pango/HarfBuzz. The Docker image and CI install them; without them locally, `POST /v1/invoice` returns 503 `pdf_unavailable` while the API stays up.
- Windows: set `PYTHONUTF8=1` before running `tests/agents`.

## Entrypoints & boundaries

- App entrypoint: `src/backend/main.py` → `uvicorn src.backend.main:app` (Dockerfile CMD).
- Routes (`/v1`): GET `/v1/health`, GET `/v1/rates/{currency}` (USD|EUR), POST `/v1/simulate`, POST `/v1/invoice` (PDF). Errors: `{"error": {"key", "message", "details"}}`.
- `src/backend/` — routers, services, models. `src/shared/` — shared schema contract. `src/frontend/templates/` — Jinja invoice template (server-side rendered, no build chain, no CDN).
- `migrations/` — Alembic (`fx_quotes` quote cache). `infra/nginx/` — latent reverse proxy. `scripts/` — governance mediators (dispatcher, registry sync, DAG validator, handoff parser, AFA validator, security scan, SDDAI verify pipeline); their tests live in `tests/agents/`.

## Agent ecosystem

- Agent roster SSOT: `.ai/agents/registry.yaml` (synced by `scripts/sync_agent_registry.py`). DAG topology: `scripts/validate_nexus_yaml.py` (`AGENT_TOPOLOGY`) and `scripts/dag_validator.py`. Dispatch: `scripts/nexus_dispatcher.py` (half-duplex, fail-closed, no self-delegation). Handoffs: `.ai/handoffs/`. Ledger: `.ai/agents/ledger.yaml` (append-only, LGPD-safe, no PII).
- `.opencode/opencode.jsonc` — model `local/qwen-32b` via llama.cpp at 127.0.0.1:8080 (CPU-only, no CUDA/cloud inference). The agent Bash tool is denied `python`, `pip`, `sudo`, `systemctl`, and `curl | sh` — verify via CI workflows or your harness shell instead of agent Bash calls.

## CI (`.github/workflows/ci.yml`, push/PR to `main`)

kill-switch → foss-compliance (`security_scan.py --strict`, credential grep) → sdd-validation (registry + DAG) → agent-health → lint (flake8 + mypy + pip-audit) → test-suite (ephemeral Postgres, coverage **≥ 95%**, **zero skipped tests**, `-p no:cacheprovider`) → build-layers (`docker compose build`, images pinned by digest) → contract-network. Local equivalent of the quality gate: `flake8` + `mypy` + `pytest --cov-fail-under=80` (CI requires 95 and no skips).

## Do not

- Do not commit `.env`, real credentials, PII, or `.gguf` model weights (`models/` and `*.gguf` are gitignored).
- Do not skip tests — any skip blocks the CI gate.
- Do not let workflows write to `.ai/`.
- Do not add network/CDN build steps to the frontend — templates are server-side rendered, no build chain.
