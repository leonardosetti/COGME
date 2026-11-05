---
id: dependencias-registro
title: Registro de Dependências e Imagens
version: 1.0.0
class: registro-dependencias
status: active
owner: agent-project-analyst
derived-from:
- docs/dependencias/registro.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- dependencias
- docs
- normalizado
---
# Registro de Dependências e Imagens

Registro exigido por ADR-010 §6 (alínea e) e §Auditoria: componentes de terceiros do backend do MVP, com versão exata, licença, origem e finalidade.

- **Fonte dos limites:** `pyproject.toml`. **Versões exatas:** `requirements.txt` (runtime) e `requirements-dev.txt` (desenvolvimento).
- **Como a licença foi obtida:** lida do metadata instalado no ambiente (`importlib.metadata`: campo `License-Expression`, `License` ou classificadores `License ::`), em 2026-10-31, com Python 3.12.10. Nada foi presumido.
- **Origem:** PyPI oficial (`https://pypi.org/project/<nome>/<versão>/`), exceto as imagens Docker.
- **Pendências:** ver a seção "Pendências e observações".

## 1. Dependências diretas de runtime

| Componente | Versão exata | Licença (metadata) | Origem | Finalidade |
|---|---|---|---|---|
| fastapi | 0.162.0 | MIT | [PyPI](https://pypi.org/project/fastapi/0.162.0/) | Framework HTTP e OpenAPI automático (REQ-14). |
| uvicorn[standard] | 0.54.0 | BSD-3-Clause | [PyPI](https://pypi.org/project/uvicorn/0.54.0/) | Servidor ASGI (`uvicorn src.backend.main:app`). |
| pydantic | 2.14.2 | MIT | [PyPI](https://pypi.org/project/pydantic/2.14.2/) | Validação e contrato de dados (`src/shared/schemas.py`). |
| pydantic-settings | 2.16.2 | MIT | [PyPI](https://pypi.org/project/pydantic-settings/2.16.2/) | Configuração por variáveis `COGME_*` (`src/backend/config.py`). |
| httpx | 0.28.1 | BSD-3-Clause | [PyPI](https://pypi.org/project/httpx/0.28.1/) | Cliente HTTP assíncrono para Frankfurter e PTAX. |
| SQLAlchemy[asyncio] | 2.1.6 | MIT | [PyPI](https://pypi.org/project/SQLAlchemy/2.1.6/) | ORM/Core assíncrono sobre PostgreSQL (REQ-07). |
| asyncpg | 0.32.0 | Apache-2.0 | [PyPI](https://pypi.org/project/asyncpg/0.32.0/) | Driver PostgreSQL assíncrono. |
| alembic | 1.20.1 | MIT | [PyPI](https://pypi.org/project/alembic/1.20.1/) | Migrações de esquema com `upgrade` e `downgrade`. |
| Jinja2 | 3.1.6 | BSD (classificador `License :: OSI Approved :: BSD License`; BSD-3-Clause segundo o projeto upstream) | [PyPI](https://pypi.org/project/Jinja2/3.1.6/) | Template HTML da invoice, com autoescape (REQ-04). |
| weasyprint | 70.0 | BSD (classificador `License :: OSI Approved :: BSD License`; BSD-3-Clause segundo o projeto upstream) | [PyPI](https://pypi.org/project/weasyprint/70.0/) | Renderização do PDF da invoice. Exige Pango no sistema (ver observações). |
| tzdata | 2026.6 | Apache-2.0 | [PyPI](https://pypi.org/project/tzdata/2026.6/) | Base de fusos para `zoneinfo` (horário de Brasília da PTAX), sobretudo em Windows e imagens enxutas. |

## 2. Dependências de desenvolvimento (`requirements-dev.txt`)

| Componente | Versão exata | Licença (metadata) | Origem | Finalidade |
|---|---|---|---|---|
| pytest | 9.2.0 | MIT | [PyPI](https://pypi.org/project/pytest/9.2.0/) | Executor de testes. |
| pytest-asyncio | 1.4.1 | Apache-2.0 | [PyPI](https://pypi.org/project/pytest-asyncio/1.4.1/) | Testes de código `async` (`asyncio_mode = "auto"`). |
| pytest-cov | 7.1.0 | MIT | [PyPI](https://pypi.org/project/pytest-cov/7.1.0/) | Cobertura de testes (meta de 80 % sobre `src/`). |
| flake8 | 7.5.0 | MIT | [PyPI](https://pypi.org/project/flake8/7.5.0/) | Lint. |
| mypy | 2.4.1 | MIT | [PyPI](https://pypi.org/project/mypy/2.4.1/) | Verificação estática de tipos. |

## 3. Dependências transitivas instaladas

Resolvidas pelo pip a partir dos limites acima; não são fixadas em `requirements*.txt` (não há arquivo de lock nesta versão). Versões e licenças são as do ambiente validado.

| Componente | Versão | Licença (metadata) | Trazida por | Finalidade |
|---|---|---|---|---|
| starlette | 1.10.0 | BSD-3-Clause | fastapi | Núcleo ASGI. |
| annotated-doc | 0.0.5 | MIT | fastapi | Anotação de documentação de parâmetros. |
| opentelemetry-api | 1.45.2 | Apache-2.0 | fastapi/starlette | Somente a API de instrumentação; sem exportador, não envia dados a terceiros. |
| pydantic_core | 2.50.2 | MIT | pydantic | Núcleo de validação. |
| annotated-types | 0.8.0 | MIT | pydantic | Tipos anotados. |
| typing-inspection | 0.4.4 | MIT | pydantic | Introspecção de tipos. |
| typing_extensions | 4.16.0 | PSF-2.0 | pydantic e outros | Backports de `typing`. |
| python-dotenv | 1.2.4 | BSD-3-Clause | pydantic-settings, uvicorn[standard] | Leitura de arquivo `.env`. |
| anyio | 4.15.1 | MIT | starlette, httpx | Camada assíncrona. |
| idna | 3.20 | BSD-3-Clause | anyio, httpx | Nomes de domínio internacionais. |
| httpcore | 1.0.9 | BSD-3-Clause | httpx | Transporte HTTP. |
| h11 | 0.16.0 | MIT | httpcore, uvicorn | Protocolo HTTP/1.1. |
| certifi | 2026.10.23 | MPL-2.0 | httpx | Certificados raiz para TLS. |
| click | 8.5.0 | BSD-3-Clause | uvicorn | CLI do uvicorn. |
| colorama | 0.4.6 | BSD (classificador `BSD License`) | click, pytest (Windows) | Cores de terminal no Windows. |
| httptools | 0.9.0 | MIT | uvicorn[standard] | Parser HTTP rápido. |
| watchfiles | 1.3.0 | MIT | uvicorn[standard] | Recarga automática em desenvolvimento. |
| websockets | 17.4 | BSD-3-Clause | uvicorn[standard] | Suporte a WebSocket. |
| PyYAML | 6.0.3 | MIT | uvicorn[standard] | Leitura de configuração de log. |
| uvloop | 0.23.0 | MIT | uvicorn[standard] (apenas Linux/macOS) | Loop de eventos rápido. Presente na imagem Linux; ausente no Windows (ambiente de desenvolvimento). |
| greenlet | 3.5.6 | MIT AND PSF-2.0 | SQLAlchemy[asyncio] | Ponte síncrono/assíncrono do SQLAlchemy. |
| Mako | 1.4.3 | MIT | alembic | Templates de migração. |
| MarkupSafe | 3.0.4 | BSD-3-Clause | Jinja2, Mako | Escape seguro de HTML. |
| pydyf | 0.13.0 | BSD (classificador `BSD License`) | weasyprint | Geração de PDF. |
| cffi | 2.1.1 | MIT-0 | weasyprint | Ligação com bibliotecas nativas (Pango). |
| pycparser | 3.12 | BSD-3-Clause | cffi | Analisador C usado pelo cffi. |
| cssselect2 | 0.10.1 | BSD (classificador `BSD License`) | weasyprint | Seletores CSS. |
| tinycss2 | 1.5.1 | BSD (classificador `BSD License`) | weasyprint | Parser CSS. |
| tinyhtml5 | 2.1.0 | MIT (classificador `MIT License`) | weasyprint | Parser HTML5. |
| webencodings | 0.6.1 | BSD (classificador `BSD License`) | tinycss2 | Codificações de texto da web. |
| fonttools | 4.68.0 | MIT | weasyprint | Manipulação de fontes. |
| brotli | 1.2.1 | MIT | fonttools, httpx | Compressão Brotli. |
| zopfli | 0.4.3 | Apache-2.0 | fonttools | Compressão para fontes WOFF. |
| pillow | 13.0.0 | MIT-CMU (OSI-approved; ver observações) | weasyprint, pydyf | Imagens no PDF. |
| pyphen | 0.18.1 | GPLv2+ / LGPLv2+ / MPL 1.1 (classificadores; tri-licença) | weasyprint | Hifenização. |
| iniconfig | 2.3.1 | MIT | pytest | Leitura de INI. |
| pluggy | 1.7.0 | MIT | pytest | Sistema de plugins. |
| packaging | 26.3 | Apache-2.0 OR BSD-2-Clause | pytest e outros | Versões e especificadores. |
| Pygments | 2.21.0 | BSD-2-Clause | pytest, httpx | Realce de sintaxe em relatórios. |
| coverage | 7.17.0 | Apache-2.0 | pytest-cov | Medição de cobertura. |
| pycodestyle | 2.15.0 | MIT | flake8 | Verificação de estilo. |
| pyflakes | 4.1.0 | MIT | flake8 | Verificação de erros estáticos. |
| mccabe | 0.7.0 | Expat (classificador `MIT License`) | flake8 | Complexidade ciclomática. |
| mypy_extensions | 1.1.0 | MIT | mypy | Extensões de tipos. |
| pathspec | 1.1.1 | MPL-2.0 (classificador) | mypy | Padrões de caminho. |
| librt | 0.16.0 | MIT | mypy | Runtime de suporte do mypy. |
| ast_serialize | 0.13.1 | MIT | mypy | Serialização de AST do mypy. |

## 4. Imagens Docker

Todas as imagens são oficiais do Docker Hub, referenciadas por digest imutável (Constituição Art. 10.2) no `Dockerfile`, no `docker-compose.yml` e no `services:` do CI. Digests obtidos com `docker pull` + `docker inspect` em 2026-10-31 (download pontual de build, Art. 10.3); são os digests da lista de manifestos (multi-arquitetura). Para atualizar uma imagem, puxar a nova tag, trocar o digest nos três arquivos e neste registro.

| Imagem | Tag | Versão exata (verificada) | Digest | Licença | Origem | Finalidade |
|---|---|---|---|---|---|---|
| python | `3.12-slim` | Python 3.12.16, Debian 13 (trixie) | `sha256:aa943ce411423c7582288f18707ff66eddcbaeb510502d747a72aeb34f30d159` | PSF-2.0 para o CPython (texto em `/usr/local/lib/python3.12/LICENSE.txt` na imagem); pacotes Debian com licenças próprias | Docker Hub, imagem oficial (`docker.io/library/python`) | Base da imagem `web`/`migrate` (`Dockerfile`, ADR-010). |
| postgres | `15-alpine` | PostgreSQL 15.19 (Alpine) | `sha256:54e0dd8e8cddcdbb9156c2486eed5a43eccb7214d7c6828097d41ce049fb3984` | PostgreSQL License (declarada pelo projeto upstream; a imagem não traz o texto, não verificada localmente) | Docker Hub, imagem oficial (`docker.io/library/postgres`) | Banco de dados (ADR-010); também usado como `services:` efêmero no CI. |
| nginx | `alpine` | nginx 1.31.8 (Alpine) | `sha256:785835ea65db4bba6f021acc0f3be91b0fef76a53fe41f8588c6698d2aed0606` | BSD-2-Clause (metadata do pacote apk `nginx-1.31.8-r1`: "2-clause BSD-like license") | Docker Hub, imagem oficial (`docker.io/library/nginx`) | Proxy reverso latente, profile `proxy` do compose (ADR-010). |

Bibliotecas nativas instaladas por `apt` sobre a imagem Python (Debian 13), versões lidas com `dpkg-query` na imagem construída:

| Pacote Debian | Versão | Licença | Finalidade |
|---|---|---|---|
| libpango-1.0-0 | 1.56.3-1 | LGPL-2+ e LGPL-2.1+ (arquivo `copyright` do pacote) | Layout de texto do WeasyPrint. |
| libpangoft2-1.0-0 | 1.56.3-1 | LGPL-2+ predominante; o `copyright` do pacote-fonte também lista Apache-2, Bitstream-Vera, OFL-1.1, Unicode e Chromium-BSD-style | Integração Pango/FreeType do WeasyPrint. |
| libharfbuzz-subset0 | 10.2.0-1+deb13u1 | Expat (MIT) predominante; o `copyright` também lista Apache-2.0, CC0-1.0, FSFAP e FSFUL | Subconjunto de fontes ao gerar o PDF. |
| fontconfig | 2.15.0-2.3 | licença não conferida localmente (upstream: MIT-like) | Descoberta de fontes e cache. |
| fonts-dejavu-core | 2.37-8 | Bitstream-Vera e GPL-2+ (arquivo `copyright` do pacote) | Fonte padrão do PDF da invoice. |

## 5. Pendências e observações

1. **Pillow 13.0.0, licença `MIT-CMU`:** confirmada em 2026-11-01. O PyPI declara `license_expression: MIT-CMU`, e a [OSI](https://opensource.org/license/mit-cmu) lista a CMU License (identificador SPDX `MIT-CMU`) como aprovada em 20/09/2024. Atende à alínea (a) da ADR-010 §6. É permissiva e sem copyleft: exige manter o aviso de copyright e veda usar o nome do titular em publicidade sem autorização. O arquivo `licenses.json` da lista SPDX consultado na mesma data ainda traz `isOsiApproved: false`; prevalece o registro da OSI, que é quem aprova.
2. **pyphen (tri-licença GPL/LGPL/MPL):** todas as três são OSI-approved. Como é oferecida sob licença escolhível, usar sob LGPLv2+ ou MPL 1.1. O código do projeto não a modifica. Registrar a escolha na T9.
3. **certifi e pathspec (MPL-2.0):** OSI-approved, copyleft fraco no nível de arquivo; sem modificação.
4. **Sem lock completo:** transitivas variam conforme a resolução do pip. Em 2026-11-01, a resolução já trazia `anyio` 4.16.0, e não a 4.15.1 desta tabela. Gerar lock com hashes é decisão futura (ADR-016, P1).
5. **Nenhuma licença não OSI-approved foi identificada** nos metadados lidos. O item 2 é o único ponto de atenção ainda aberto.
