# Auditoria implementação e conformidade FOSS — COGME

Data: 2026-11-06
Escopo: src/, pyproject.toml, requirements*.txt, package.json, Dockerfile, constitution.md, LICENSE, scripts/ de segurança.

## Licença do projeto

LICENSE = CC0 1.0 Universal (domínio público, máxima permissividade, FOSS-compatível). Sem patente/marca waivadas. OK.

## Dependências Python (pyproject.toml + requirements)

Todas FOSS, custo recorrente zero, alinhado P-01:
- fastapi (MIT), python-multipart (MIT), uvicorn (BSD), pydantic (MIT), pydantic-settings (MIT), httpx (MIT), sqlalchemy (MIT), asyncpg (BSD/Apache-2), alembic (MIT), jinja2 (BSD), weasyprint (BSD 3-clause), tzdata (public domain).
- uv.lock presente: lockfile determinístico, reprodutível. OK.

## Dependências front (package.json)

Apenas `@opencode-ai/models ^0.0.123`. Licença não declarada localmente; pendente confirmação FOSS. node_modules instalado.

## Imagem Docker (Dockerfile)

- Base `python:3.12-slim@sha256:...` fixada por digest imutável (Art. 10.2). Debian FOSS. OK.
- WeasyPrint native libs (pango, harfbuzz, fonts-dejavu) via apt Debian. OK.
- Usuário sem privilégios `cogme` (uid 10001), sem shell de login, sem root. OK.
- Nenhum segredo/PII em camada de imagem; config só por env em runtime. OK.

## Regras constitucionais FOSS

- P-01 FOSS-ZERO-COST: respeitado (zero dependência proprietária paga).
- P-02 soberania local: inferência local via llama.cpp/Qwen, cloud free-tier whitelist apenas exceção. OK.
- P-03 soberania de dados: nenhum dado sensível a nuvem; sem telemetria/rastreio/lock-in. OK.
- Bypass registrados: GitHub Actions Free Tier (CI/CD) e cloud free-tier whitelist (dados não sensíveis). OK.

## Implementação (estado pós-saneamento ponytail)

- src/frontend/app.py: filtros Jinja duplicados removidos; static/templates resolvidos via Path(__file__) (cwd-independente). OK.
- Suíte backend: não coleta por `pydantic_settings` ausente no ambiente (pré-existente, não causado por esta mudança). Não é regressão.
- Não há testes de frontend.

## Pontos de atenção

1. `@opencode-ai/models` (package.json): confirmar licença FOSS. Se não-FOSS, acionar Bypass Protocol ou trocar por alternativa FOSS.
2. `nohup.out` no root: arquivo de log solto, não deve ser versionado. Adicionar a .gitignore se ainda não estiver.
3. `task-ta-0068.json`, `task-ta-0069.json`, `task-ta-0100.json` no root: artefatos de tarefa soltos no root; mover para local adequado ou remover.

## Veredito

Conforme FOSS. Implementação saudável. Consertar os 3 pontos de atenção acima.
