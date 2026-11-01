"""Repositório de cotações sobre PostgreSQL real (spec backend-mvp-v1, §5; REQ-07).

Marcador ``postgres``. Sem ``COGME_TEST_DATABASE_URL`` o módulo inteiro é pulado. A migração
Alembic roda programaticamente até ``head`` e volta a ``base`` ao fim do módulo. A tabela é
esvaziada antes de cada teste. Relógios são falsos; o banco é o único recurso real.
"""

from __future__ import annotations

import os
import socket
from collections.abc import AsyncIterator, Iterator
from dataclasses import replace
from datetime import UTC, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import func, select, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncEngine

from src.backend.models.database import create_engine, create_session_factory
from src.backend.models.quote import FxQuote
from src.backend.models.repository import (
    RepositoryError,
    SqlAlchemyQuoteRepository,
    StoredQuote,
)
from src.backend.services.circuit_breaker import CircuitBreaker
from src.backend.services.rate_service import RateService
from src.shared.schemas import Currency, RateSource

from .fakes import FixedClock, FixedMonotonic, ScriptedProvider

DATABASE_URL_ENV = "COGME_TEST_DATABASE_URL"
DATABASE_URL = os.environ.get(DATABASE_URL_ENV, "")
ROOT = Path(__file__).resolve().parents[2]
TTL_SECONDS = 3600

pytestmark = [
    pytest.mark.postgres,
    pytest.mark.skipif(
        not DATABASE_URL,
        reason=f"{DATABASE_URL_ENV} não definida: teste de PostgreSQL pulado.",
    ),
]

BASE_INSTANT = datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC)
BASE_STORED = StoredQuote(
    currency="USD",
    rate=Decimal("5.432501"),
    source="frankfurter",
    bulletin=None,
    quoted_at=datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
    fetched_at=BASE_INSTANT,
)


def _alembic_config() -> Config:
    """Configuração do Alembic sem arquivo ini, para não reconfigurar o logging do pytest."""
    config = Config()
    config.set_main_option("script_location", str(ROOT / "migrations"))
    return config


@pytest.fixture(scope="module")
def migrated() -> Iterator[None]:
    """Aplica as migrações até ``head`` e desfaz até ``base`` ao fim do módulo."""
    config = _alembic_config()
    with pytest.MonkeyPatch.context() as patch:
        patch.setenv("COGME_DATABASE_URL", DATABASE_URL)
        command.upgrade(config, "head")
    yield
    with pytest.MonkeyPatch.context() as patch:
        patch.setenv("COGME_DATABASE_URL", DATABASE_URL)
        command.downgrade(config, "base")


@pytest.fixture
async def engine(migrated: None) -> AsyncIterator[AsyncEngine]:
    """Engine do projeto, com a tabela esvaziada antes de cada teste."""
    engine = create_engine(DATABASE_URL)
    async with engine.begin() as connection:
        await connection.execute(text("TRUNCATE TABLE fx_quotes RESTART IDENTITY"))
    yield engine
    await engine.dispose()


@pytest.fixture
async def repository(engine: AsyncEngine) -> SqlAlchemyQuoteRepository:
    """Repositório real, sobre o engine do teste."""
    return SqlAlchemyQuoteRepository(create_session_factory(engine))


def _closed_port() -> int:
    """Descobre uma porta local sem ninguém escutando, já liberada pelo sistema.

    Returns:
        Um número de porta em 127.0.0.1 que não responde a conexões.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.bind(("127.0.0.1", 0))
        return int(probe.getsockname()[1])


@pytest.mark.parametrize("rate", ["0.000001", "5.432501", "5.430000", "999.999999"])
async def test_decimal_rate_round_trips_with_six_places_req07(
    repository: SqlAlchemyQuoteRepository, rate: str,
) -> None:
    """REQ-07: a taxa volta do banco como Decimal exato, com as 6 casas (§5)."""
    await repository.save(replace(BASE_STORED, rate=Decimal(rate)))

    row = await repository.get_latest("USD")

    assert row is not None
    assert str(row.rate) == rate
    assert row.rate == Decimal(rate)


async def test_timestamps_round_trip_across_timezones_req07(
    repository: SqlAlchemyQuoteRepository,
) -> None:
    """REQ-07: instantes com fuso de Brasília e microssegundos voltam como o mesmo instante (§4)."""
    brasilia = timezone(timedelta(hours=-3))
    quoted_at = datetime(2026, 10, 30, 13, 4, 18, 706316, tzinfo=brasilia)
    fetched_at = datetime(2026, 10, 30, 16, 4, 18, 706316, tzinfo=UTC)
    await repository.save(replace(BASE_STORED, quoted_at=quoted_at, fetched_at=fetched_at))

    row = await repository.get_latest("USD")

    assert row is not None
    assert row.quoted_at == quoted_at
    assert row.fetched_at == fetched_at
    assert row.quoted_at.microsecond == 706316
    assert row.quoted_at.utcoffset() == timedelta(0)


async def test_get_latest_picks_most_recent_fetched_at_req07(
    repository: SqlAlchemyQuoteRepository,
) -> None:
    """REQ-07: get_latest devolve a maior fetched_at, mesmo gravada antes das mais antigas."""
    newest = BASE_INSTANT + timedelta(hours=2)
    await repository.save(replace(BASE_STORED, rate=Decimal("5.300000"), fetched_at=newest))
    await repository.save(replace(BASE_STORED, rate=Decimal("5.100000")))
    await repository.save(
        replace(BASE_STORED, rate=Decimal("5.200000"),
                fetched_at=BASE_INSTANT + timedelta(hours=1)),
    )
    await repository.save(
        replace(BASE_STORED, currency="EUR", rate=Decimal("6.000000"),
                fetched_at=BASE_INSTANT + timedelta(hours=3)),
    )

    usd = await repository.get_latest("USD")
    eur = await repository.get_latest("EUR")

    assert usd is not None and usd.rate == Decimal("5.300000")
    assert usd.fetched_at == newest
    assert eur is not None and eur.rate == Decimal("6.000000")


async def test_get_latest_breaks_ties_by_last_insert_req07(
    repository: SqlAlchemyQuoteRepository,
) -> None:
    """REQ-07: com fetched_at igual, vence a gravada por último (ORDER BY id DESC)."""
    await repository.save(replace(BASE_STORED, rate=Decimal("5.100000")))
    await repository.save(replace(BASE_STORED, rate=Decimal("5.200000")))

    row = await repository.get_latest("USD")

    assert row is not None
    assert row.rate == Decimal("5.200000")


async def test_get_latest_on_empty_table_is_none_req07(
    repository: SqlAlchemyQuoteRepository,
) -> None:
    """REQ-07: sem linhas, get_latest devolve None, sem erro (§5)."""
    assert await repository.get_latest("USD") is None


async def test_check_rejects_unknown_currency_through_repository_req07(
    repository: SqlAlchemyQuoteRepository, engine: AsyncEngine,
) -> None:
    """REQ-07: a CHECK do banco recusa moeda fora de USD/EUR; vira RepositoryError."""
    with pytest.raises(RepositoryError) as info:
        await repository.save(replace(BASE_STORED, currency="GBP"))

    assert isinstance(info.value.__cause__, IntegrityError)
    async with engine.connect() as connection:
        count = await connection.scalar(select(func.count()).select_from(FxQuote))
    assert count == 0


async def test_check_rejects_unknown_currency_in_database_req07(engine: AsyncEngine) -> None:
    """REQ-07: a restrição fica no próprio banco, não só no código: INSERT direto também falha."""
    statement = text(
        "INSERT INTO fx_quotes (currency, rate, source, bulletin, quoted_at, fetched_at) "
        "VALUES (:currency, :rate, 'frankfurter', NULL, :instant, :instant)"
    )
    with pytest.raises(IntegrityError):
        async with engine.begin() as connection:
            await connection.execute(
                statement,
                {"currency": "GBP", "rate": Decimal("5.000000"), "instant": BASE_INSTANT},
            )


async def test_connection_to_closed_port_raises_repository_error_req07() -> None:
    """REQ-07: falha de conexão vira RepositoryError, com o OSError original em __cause__ (§5).

    Porta local sem ninguém escutando; a conexão é recusada na hora, sem rede externa.
    """
    url = f"postgresql+asyncpg://cogme@127.0.0.1:{_closed_port()}/cogme_test"
    engine = create_engine(url)
    try:
        repository = SqlAlchemyQuoteRepository(create_session_factory(engine))
        with pytest.raises(RepositoryError) as info:
            await repository.get_latest("USD")
        assert isinstance(info.value.__cause__, OSError)
    finally:
        await engine.dispose()


async def test_second_quote_within_ttl_is_read_from_database_req07(
    repository: SqlAlchemyQuoteRepository,
) -> None:
    """REQ-07: RateService real com repositório real: a segunda consulta não chama o provedor."""
    clock = FixedClock()
    provider = ScriptedProvider(RateSource.FRANKFURTER, rate="5.432501")
    service = RateService(
        repository=repository,
        providers=[(provider, CircuitBreaker(clock=FixedMonotonic()))],
        ttl_seconds=TTL_SECONDS,
        now=clock,
    )

    first = await service.get_quote(Currency.USD)
    second = await service.get_quote(Currency.USD)

    assert provider.calls == 1
    assert first.rate == second.rate == Decimal("5.432501")
    assert second.stale is False


async def test_expired_row_is_refetched_at_ttl_boundary_req07(
    repository: SqlAlchemyQuoteRepository,
) -> None:
    """REQ-07: no limite do TTL o cache vale; um segundo depois o provedor é chamado."""
    clock = FixedClock()
    provider = ScriptedProvider(RateSource.FRANKFURTER, rate="5.432501")
    service = RateService(
        repository=repository,
        providers=[(provider, CircuitBreaker(clock=FixedMonotonic()))],
        ttl_seconds=TTL_SECONDS,
        now=clock,
    )
    await service.get_quote(Currency.USD)

    clock.advance(TTL_SECONDS)
    await service.get_quote(Currency.USD)
    assert provider.calls == 1

    clock.advance(1)
    await service.get_quote(Currency.USD)
    assert provider.calls == 2
