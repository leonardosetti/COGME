# syntax=docker/dockerfile:1
# Imagem de runtime do backend COGME (ADR-010, Constituição Art. 10).
# Base Python 3.12 slim (Debian 13) fixada por digest imutável (Art. 10.2).
# Para atualizar: docker pull python:3.12-slim, copiar o novo digest aqui e em
# docs/dependencias/registro.md.
ARG PYTHON_IMAGE=python:3.12-slim@sha256:aa943ce411423c7582288f18707ff66eddcbaeb510502d747a72aeb34f30d159

# ---------------------------------------------------------------------------
# Estágio 1: resolve as dependências Python em um venv isolado.
# --only-binary: só rodas pré-compiladas; assim o runtime não precisa de
# compilador e o build falha cedo se alguma dependência exigir um.
# ---------------------------------------------------------------------------
FROM ${PYTHON_IMAGE} AS builder

ENV PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN python -m venv /opt/venv
COPY requirements.txt /tmp/requirements.txt
RUN /opt/venv/bin/pip install --only-binary=:all: -r /tmp/requirements.txt

# ---------------------------------------------------------------------------
# Estágio 2: runtime enxuto, sem pip de build, sem segredos, sem root.
# ---------------------------------------------------------------------------
FROM ${PYTHON_IMAGE} AS runtime

# UV_THREADPOOL_SIZE: o DNS de um banco parado ocupa o pool do libuv, e sem esta
# folga o DNS das fontes de cotação fica preso na fila (spec §4).
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH=/opt/venv/bin:$PATH \
    XDG_CACHE_HOME=/tmp/.cache \
    UV_THREADPOOL_SIZE=64

# Bibliotecas nativas do WeasyPrint (Pango/HarfBuzz) e uma fonte básica para
# o PDF da invoice. Sem elas a API sobe, mas POST /v1/invoice responde 503.
# `fontconfig` gera o cache de fontes do sistema na instalação; o cache por
# usuário vai para /tmp (XDG_CACHE_HOME), que é gravável mesmo com rootfs
# somente leitura (tmpfs no compose).
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpango-1.0-0 \
        libpangoft2-1.0-0 \
        libharfbuzz-subset0 \
        fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Usuário sem privilégios e sem shell de login.
RUN groupadd --system --gid 10001 cogme \
    && useradd --system --uid 10001 --gid cogme --no-create-home \
        --shell /usr/sbin/nologin cogme

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app
# Código somente leitura para o usuário da aplicação (pertence a root).
COPY alembic.ini ./alembic.ini
COPY migrations ./migrations
COPY src ./src

USER cogme
EXPOSE 8000

# As migrações (alembic upgrade head) rodam no serviço `migrate` do compose,
# com esta mesma imagem, antes de o `web` iniciar. A configuração (inclusive
# COGME_DATABASE_URL) chega só por variável de ambiente em tempo de execução.
CMD ["uvicorn", "src.backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
