"""Infraestrutura de banco assíncrono (SQLAlchemy 2 + asyncpg).

Este módulo não lê ``Settings`` nem o ambiente: a URL é sempre recebida como
argumento por quem monta a aplicação (``lifespan`` do FastAPI, Alembic ou
testes). Assim, importar o módulo não tem efeito colateral nem exige banco.
"""

from __future__ import annotations

from typing import Final

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

# Convenção de nomes determinística: o Alembic e o modelo geram os mesmos
# nomes de constraints e índices, o que evita drift em ``alembic check``.
NAMING_CONVENTION: Final[dict[str, str]] = {
    "ix": "ix_%(table_name)s_%(column_0_N_name)s",
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


# Limites do driver e do pool. O RateService corta cada chamada antes disso (0,3 s); estes
# valores protegem quem usa o repositório direto e encerram a limpeza da operação cortada. Sem
# eles o asyncpg espera 60 s para conectar e, com o banco travado, não desiste de um comando.
CONNECT_TIMEOUT_SECONDS: Final[float] = 1.0
COMMAND_TIMEOUT_SECONDS: Final[float] = 1.0
POOL_TIMEOUT_SECONDS: Final[float] = 0.25


class Base(DeclarativeBase):
    """Base declarativa de todos os modelos ORM do backend."""

    metadata = MetaData(naming_convention=NAMING_CONVENTION)


def create_engine(database_url: str) -> AsyncEngine:
    """Cria o ``AsyncEngine`` do PostgreSQL a partir de uma URL explícita.

    O engine é criado sem ``echo``: instruções SQL e parâmetros não vão para
    o log. A conexão só é aberta no primeiro uso (criação preguiçosa). O Alembic tem engine
    próprio, então migrações longas não sofrem com ``command_timeout``.

    Args:
        database_url: URL SQLAlchemy async (``postgresql+asyncpg://...``).

    Returns:
        O engine assíncrono. Quem o criou deve chamar
        ``await engine.dispose()`` no encerramento.
    """
    return create_async_engine(
        database_url,
        echo=False,
        pool_pre_ping=True,
        pool_timeout=POOL_TIMEOUT_SECONDS,
        connect_args={
            "timeout": CONNECT_TIMEOUT_SECONDS,
            "command_timeout": COMMAND_TIMEOUT_SECONDS,
        },
    )


def create_session_factory(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    """Cria a fábrica de sessões assíncronas ligada ao engine.

    ``expire_on_commit=False`` mantém os atributos acessíveis após o commit,
    sem novo acesso ao banco (necessário em contexto assíncrono).

    Args:
        engine: Engine retornado por :func:`create_engine`.

    Returns:
        Fábrica de ``AsyncSession``; cada chamada devolve uma sessão nova.
    """
    return async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
