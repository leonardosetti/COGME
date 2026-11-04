"""Ambiente do Alembic (assíncrono) do backend COGME.

A URL do banco vem exclusivamente de ``COGME_DATABASE_URL``. Nenhum valor é
impresso, para não vazar credenciais em logs.
"""

from __future__ import annotations

import asyncio
import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine

from src.backend.models.database import Base

# Importa os modelos para registrá-los em Base.metadata (autogenerate/check).
from src.backend.models import quote  # noqa: F401

DATABASE_URL_ENV = "COGME_DATABASE_URL"

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name, disable_existing_loggers=False)

target_metadata = Base.metadata


def get_database_url() -> str:
    """Lê a URL do banco do ambiente.

    Returns:
        A URL SQLAlchemy async informada em ``COGME_DATABASE_URL``.

    Raises:
        SystemExit: Se a variável estiver ausente ou vazia.
    """
    url = os.environ.get(DATABASE_URL_ENV, "").strip()
    if not url:
        raise SystemExit(
            f"Variável de ambiente {DATABASE_URL_ENV} ausente ou vazia. "
            "Defina-a com a URL 'postgresql+asyncpg://...' antes de rodar "
            "o Alembic."
        )
    return url


def run_migrations_offline() -> None:
    """Gera o SQL das migrações sem abrir conexão (modo ``--sql``)."""
    context.configure(
        url=get_database_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Executa as migrações em uma conexão síncrona do Alembic.

    Args:
        connection: Conexão fornecida por ``run_sync``.
    """
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Abre um engine assíncrono descartável e roda as migrações."""
    engine = create_async_engine(get_database_url(), poolclass=pool.NullPool)
    try:
        async with engine.connect() as connection:
            await connection.run_sync(do_run_migrations)
    finally:
        await engine.dispose()


def run_migrations_online() -> None:
    """Ponto de entrada do modo online (com conexão)."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
