"""Fixtures compartilhadas de tests/unit/ (spec backend-mvp-v1, §8).

Tudo aqui é sintético e determinístico: moedas, valores e datas são fictícios,
os relógios são falsos e nenhuma fixture acessa a rede. O módulo importa só o
repositório e os schemas, para que a coleta de test_schemas.py não dependa dos
serviços, que ainda não existem nesta etapa.
"""

from __future__ import annotations

from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from decimal import Decimal

import pytest

from src.backend.models.repository import StoredQuote
from src.shared.schemas import RateQuote

NOW_UTC: datetime = datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC)
SYNTHETIC_QUOTED_AT: datetime = datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC)


class FakeQuoteRepository:
    """Repositório em memória que cumpre o contrato ``QuoteRepository``.

    ``get_latest`` devolve a linha de maior ``fetched_at``. Em empate vence a
    gravada por último, como o ``ORDER BY fetched_at DESC, id DESC`` do banco.

    Attributes:
        rows: Linhas que o repositório considera existentes.
        saved: Cópia das gravações feitas por ``save``, na ordem em que ocorreram.
    """

    def __init__(self) -> None:
        self.rows: list[StoredQuote] = []
        self.saved: list[StoredQuote] = []

    async def get_latest(self, currency: str) -> StoredQuote | None:
        """Devolve a cotação mais recente da moeda, ou ``None``.

        Args:
            currency: Código da moeda.

        Returns:
            A linha de maior ``fetched_at`` ou ``None``.
        """
        matching = [quote for quote in self.rows if quote.currency == currency]
        if not matching:
            return None
        return max(reversed(matching), key=lambda quote: quote.fetched_at)

    async def save(self, quote: StoredQuote) -> None:
        """Grava a cotação em memória.

        Args:
            quote: Cotação a gravar.
        """
        self.rows.append(quote)
        self.saved.append(quote)

    def clear(self) -> None:
        """Remove as linhas existentes, sem apagar o histórico de gravações."""
        self.rows.clear()


class FakeMonotonicClock:
    """Relógio monotônico falso, chamável como ``time.monotonic``.

    Avança somente por ``advance``. Usado pelo CircuitBreaker.
    """

    def __init__(self) -> None:
        self.seconds: float = 0.0

    def __call__(self) -> float:
        """Devolve o instante atual, em segundos.

        Returns:
            O instante falso.
        """
        return self.seconds

    def advance(self, seconds: float) -> None:
        """Avança o relógio.

        Args:
            seconds: Quantidade de segundos a somar.
        """
        self.seconds += seconds


class FakeUtcClock:
    """Relógio UTC falso, chamável como ``RateService.now``.

    Avança somente por ``advance``.
    """

    def __init__(self) -> None:
        self.current: datetime = NOW_UTC

    def __call__(self) -> datetime:
        """Devolve o instante atual em UTC.

        Returns:
            O instante falso, com fuso UTC.
        """
        return self.current

    def advance(self, seconds: float) -> None:
        """Avança o relógio.

        Args:
            seconds: Quantidade de segundos a somar.
        """
        self.current += timedelta(seconds=seconds)


@pytest.fixture
def now() -> datetime:
    """Instante fixo de referência (2026-10-30 16:00 UTC).

    Returns:
        O instante de referência dos testes.
    """
    return NOW_UTC


@pytest.fixture
def utc_clock() -> FakeUtcClock:
    """Relógio UTC falso, começando em ``NOW_UTC``.

    Returns:
        Um relógio novo para o teste.
    """
    return FakeUtcClock()


@pytest.fixture
def mono_clock() -> FakeMonotonicClock:
    """Relógio monotônico falso, começando em zero.

    Returns:
        Um relógio novo para o teste.
    """
    return FakeMonotonicClock()


@pytest.fixture
def repository() -> FakeQuoteRepository:
    """Repositório em memória, vazio.

    Returns:
        Um repositório novo para o teste.
    """
    return FakeQuoteRepository()


@pytest.fixture
def make_stored_quote() -> Callable[..., StoredQuote]:
    """Fábrica de ``StoredQuote`` sintéticas.

    Returns:
        Função que monta a cotação com valores fictícios; ``fetched_at`` padrão é ``NOW_UTC``.
    """

    def _make(
        *,
        currency: str = "USD",
        rate: str = "5.000000",
        source: str = "frankfurter",
        bulletin: str | None = None,
        fetched_at: datetime | None = None,
    ) -> StoredQuote:
        return StoredQuote(
            currency=currency,
            rate=Decimal(rate),
            source=source,
            bulletin=bulletin,
            quoted_at=SYNTHETIC_QUOTED_AT,
            fetched_at=fetched_at or NOW_UTC,
        )

    return _make


@pytest.fixture
def make_rate_quote() -> Callable[..., RateQuote]:
    """Fábrica de ``RateQuote`` sintéticas.

    Returns:
        Função que monta a cotação de contrato com valores fictícios.
    """

    def _make(
        *,
        currency: str = "USD",
        rate: str = "5.000000",
        source: str = "frankfurter",
        bulletin: str | None = None,
        stale: bool = False,
    ) -> RateQuote:
        return RateQuote(
            currency=currency,
            rate=Decimal(rate),
            source=source,
            quoted_at=SYNTHETIC_QUOTED_AT,
            bulletin=bulletin,
            stale=stale,
        )

    return _make
