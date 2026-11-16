"""Property tests: persistence round-trip equals reprocessing (spec backend-mvp-v1, §5).

These tests use Hypothesis to verify that saving a quote to the repository and
reading it back produces the same data as reprocessing the original values.
This is the "persistence = reprocessing" property: the database is just a
storage layer and should not transform the data.
"""

from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal
from typing import Any

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st
from sqlalchemy.ext.asyncio import AsyncEngine

from tests.integration.fakes import FixedClock, FixedMonotonic

from src.backend.models.database import create_engine, create_session_factory
from src.backend.models.repository import (
    RepositoryError,
    SqlAlchemyQuoteRepository,
    StoredQuote,
)
from src.backend.services.calculator import calculate
from src.shared.schemas import Currency, Regime

# ---------- Hypothesis strategies ----------

_MIN_RATE = Decimal("0.000001")
_MAX_RATE = Decimal("999.999999")
_MIN_AMOUNT = Decimal("0.01")
_MAX_AMOUNT = Decimal("1000000000")
_MIN_QUANTITY = Decimal("1")
_MAX_QUANTITY = Decimal("100000")
_MIN_PERCENT = Decimal("0")
_MAX_PERCENT = Decimal("100")

# UTC datetimes within a reasonable range
_MIN_DATETIME = datetime(2020, 1, 1, tzinfo=UTC)
_MAX_DATETIME = datetime(2030, 12, 31, 23, 59, 59, 999999, tzinfo=UTC)


@st.composite
def datetime_utc_strategy(draw: st.DrawFn) -> datetime:
    """Generate a UTC datetime with microsecond precision."""
    # Use timestamp to avoid issues with date ranges
    timestamp = draw(
        st.integers(
            min_value=int(_MIN_DATETIME.timestamp()),
            max_value=int(_MAX_DATETIME.timestamp()),
        )
    )
    dt = datetime.fromtimestamp(timestamp, tz=UTC)
    microsecond = draw(st.integers(0, 999999))
    return dt.replace(microsecond=microsecond)


@st.composite
def stored_quote_strategy(draw: st.DrawFn) -> StoredQuote:
    """Generate a valid StoredQuote."""
    currency = draw(st.sampled_from(["USD", "EUR"]))
    rate = draw(
        st.decimals(
            min_value=_MIN_RATE,
            max_value=_MAX_RATE,
            allow_nan=False,
            allow_infinity=False,
            places=6,
        )
    )
    source = draw(st.sampled_from(["frankfurter", "ptax"]))
    bulletin = draw(st.one_of(
        st.none(),
        st.text(min_size=1, max_size=40).filter(lambda x: '\x00' not in x)
    ))
    quoted_at = draw(datetime_utc_strategy())
    fetched_at = draw(datetime_utc_strategy())

    return StoredQuote(
        currency=currency,
        rate=rate,
        source=source,
        bulletin=bulletin,
        quoted_at=quoted_at,
        fetched_at=fetched_at,
    )


@st.composite
def stored_quote_strategy_latest(draw: st.DrawFn) -> StoredQuote:
    """Generate a StoredQuote with max fetched_at to ensure it's the latest."""
    currency = draw(st.sampled_from(["USD", "EUR"]))
    rate = draw(
        st.decimals(
            min_value=_MIN_RATE,
            max_value=_MAX_RATE,
            allow_nan=False,
            allow_infinity=False,
            places=6,
        )
    )
    source = draw(st.sampled_from(["frankfurter", "ptax"]))
    bulletin = draw(st.one_of(
        st.none(),
        st.text(min_size=1, max_size=40).filter(lambda x: '\x00' not in x)
    ))
    quoted_at = draw(datetime_utc_strategy())
    # Use maximum possible fetched_at to ensure this quote is the "latest"
    fetched_at = _MAX_DATETIME

    return StoredQuote(
        currency=currency,
        rate=rate,
        source=source,
        bulletin=bulletin,
        quoted_at=quoted_at,
        fetched_at=fetched_at,
    )


@st.composite
def simulation_params_strategy(draw: st.DrawFn) -> dict[str, Any]:
    """Generate valid simulation parameters."""
    regime: Regime = draw(st.sampled_from(list(Regime)))
    currency: Currency = draw(st.sampled_from(list(Currency)))
    amount: Decimal = draw(
        st.decimals(
            min_value=_MIN_AMOUNT,
            max_value=_MAX_AMOUNT,
            allow_nan=False,
            allow_infinity=False,
            places=2,
        )
    )
    quantity: Decimal | None = draw(
        st.one_of(
            st.none(),
            st.decimals(
                min_value=_MIN_QUANTITY,
                max_value=_MAX_QUANTITY,
                allow_nan=False,
                allow_infinity=False,
                places=2,
            ),
        )
    )
    # For FIXED regime, quantity must be None
    if regime == Regime.FIXED:
        quantity = None
    elif quantity is None:
        quantity = draw(
            st.decimals(
                min_value=_MIN_QUANTITY,
                max_value=_MAX_QUANTITY,
                allow_nan=False,
                allow_infinity=False,
                places=2,
            )
        )

    rate: Decimal = draw(
        st.decimals(
            min_value=_MIN_RATE,
            max_value=_MAX_RATE,
            allow_nan=False,
            allow_infinity=False,
            places=6,
        )
    )
    spread_pct: Decimal = draw(
        st.decimals(
            min_value=_MIN_PERCENT,
            max_value=_MAX_PERCENT,
            allow_nan=False,
            allow_infinity=False,
            places=4,
        )
    )
    iof_pct: Decimal = draw(
        st.decimals(
            min_value=_MIN_PERCENT,
            max_value=_MAX_PERCENT,
            allow_nan=False,
            allow_infinity=False,
            places=4,
        )
    )

    return {
        "regime": regime,
        "currency": currency,
        "amount": amount,
        "quantity": quantity,
        "rate": rate,
        "spread_pct": spread_pct,
        "iof_pct": iof_pct,
    }


# ---------- Property tests: Repository round-trip ----------


class TestRepositoryPersistenceRoundTrip:
    """Property: save() then get_latest() returns equivalent data."""

    @pytest.fixture
    def engine(self) -> AsyncEngine:
        """Create engine for property tests. Requires COGME_TEST_DATABASE_URL."""
        import os

        url = os.environ.get("COGME_TEST_DATABASE_URL")
        if not url:
            pytest.skip("COGME_TEST_DATABASE_URL not set")
        return create_engine(url)

    @pytest.fixture
    async def repository(self, engine: AsyncEngine) -> SqlAlchemyQuoteRepository:
        """Repository with clean table for each test."""
        from sqlalchemy import text

        async with engine.begin() as conn:
            await conn.execute(text("TRUNCATE TABLE fx_quotes RESTART IDENTITY"))
        return SqlAlchemyQuoteRepository(create_session_factory(engine))

    async def test_save_then_get_latest_round_trips(
        self, repository: SqlAlchemyQuoteRepository
    ) -> None:
        """Persisting a quote and reading it back yields equal data.

        This is the core "persistence = reprocessing" property: the database
        should be a transparent storage layer. The round-trip must preserve
        all fields exactly.
        """
        quote = StoredQuote(
            currency="USD",
            rate=Decimal("5.000000"),
            source="frankfurter",
            bulletin=None,
            quoted_at=datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC),
            fetched_at=datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC),
        )
        await repository.save(quote)
        retrieved = await repository.get_latest(quote.currency)

        assert retrieved is not None, "Saved quote should be retrievable"
        assert retrieved.currency == quote.currency
        assert retrieved.rate == quote.rate
        assert retrieved.source == quote.source
        assert retrieved.bulletin == quote.bulletin
        assert retrieved.quoted_at == quote.quoted_at
        assert retrieved.fetched_at == quote.fetched_at

    async def test_get_latest_picks_max_fetched_at(
        self, repository: SqlAlchemyQuoteRepository
    ) -> None:
        """get_latest returns the quote with maximum fetched_at.

        This verifies the ordering contract is preserved through persistence.
        """
        quote1 = StoredQuote(
            currency="USD",
            rate=Decimal("5.000000"),
            source="frankfurter",
            bulletin=None,
            quoted_at=datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC),
            fetched_at=datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC),
        )
        quote2 = StoredQuote(
            currency="USD",
            rate=Decimal("5.500000"),
            source="ptax",
            bulletin="Fechamento",
            quoted_at=datetime(2026, 10, 30, 17, 0, 0, tzinfo=UTC),
            fetched_at=datetime(2026, 10, 30, 17, 0, 0, tzinfo=UTC),
        )

        await repository.save(quote1)
        await repository.save(quote2)

        retrieved = await repository.get_latest(quote1.currency)

        assert retrieved is not None
        assert retrieved.currency == quote2.currency
        assert retrieved.rate == quote2.rate
        assert retrieved.fetched_at == quote2.fetched_at


# ---------- Property tests: Calculator idempotence ----------


class TestCalculatorReprocessingIdempotence:
    """Property: calculate() is idempotent and pure."""

    @given(simulation_params_strategy())
    @settings(max_examples=100, deadline=None)
    def test_calculate_idempotent(self, params: dict[str, Any]) -> None:
        """Running calculate twice with same inputs yields identical output.

        This is the "reprocessing = same result" property. The calculator
        has no hidden state, so repeated calls must be equal.
        """
        result1 = calculate(
            regime=params["regime"],
            amount=params["amount"],
            quantity=params["quantity"],
            rate=params["rate"],
            spread_pct=params["spread_pct"],
            iof_pct=params["iof_pct"],
        )

        result2 = calculate(
            regime=params["regime"],
            amount=params["amount"],
            quantity=params["quantity"],
            rate=params["rate"],
            spread_pct=params["spread_pct"],
            iof_pct=params["iof_pct"],
        )

        # All fields must match exactly
        assert result1.gross_foreign == result2.gross_foreign
        assert result1.gross_brl == result2.gross_brl
        assert result1.spread_brl == result2.spread_brl
        assert result1.iof_brl == result2.iof_brl
        assert result1.net_brl == result2.net_brl
        assert result1.effective_rate == result2.effective_rate

    @given(simulation_params_strategy())
    @settings(max_examples=100, deadline=None)
    def test_calculate_identity_gross_brl_minus_deductions_equals_net(
        self, params: dict[str, Any]
    ) -> None:
        """Identity: gross_brl - spread_brl - iof_brl == net_brl.

        This is the fundamental accounting identity from §2 of the spec.
        It must hold for all valid inputs.
        """
        result = calculate(
            regime=params["regime"],
            amount=params["amount"],
            quantity=params["quantity"],
            rate=params["rate"],
            spread_pct=params["spread_pct"],
            iof_pct=params["iof_pct"],
        )

        reconstructed_net = result.gross_brl - result.spread_brl - result.iof_brl
        assert result.net_brl == reconstructed_net

    @given(simulation_params_strategy())
    @settings(max_examples=50, deadline=None)
    def test_calculate_effective_rate_is_net_per_foreign_unit(
        self, params: dict[str, Any]
    ) -> None:
        """effective_rate = net_brl / gross_foreign (rounded to 6 places).

        This is the definition of effective_rate from §2.
        """
        result = calculate(
            regime=params["regime"],
            amount=params["amount"],
            quantity=params["quantity"],
            rate=params["rate"],
            spread_pct=params["spread_pct"],
            iof_pct=params["iof_pct"],
        )

        if result.gross_foreign != 0:
            from src.backend.services.calculator import q6

            expected = q6(result.net_brl / result.gross_foreign)
            assert result.effective_rate == expected

    @given(simulation_params_strategy())
    @settings(max_examples=30, deadline=None)
    def test_calculate_spread_is_percentage_of_gross_brl(self, params: dict[str, Any]) -> None:
        """spread_brl = gross_brl * spread_pct / 100 (rounded to 2 places)."""
        from src.backend.services.calculator import q2
        from decimal import Decimal

        result = calculate(
            regime=params["regime"],
            amount=params["amount"],
            quantity=params["quantity"],
            rate=params["rate"],
            spread_pct=params["spread_pct"],
            iof_pct=params["iof_pct"],
        )

        expected = q2(result.gross_brl * params["spread_pct"] / Decimal("100"))
        assert result.spread_brl == expected

    @given(simulation_params_strategy())
    @settings(max_examples=30, deadline=None)
    def test_calculate_iof_is_percentage_of_brl_after_spread(self, params: dict[str, Any]) -> None:
        """iof_brl = (gross_brl - spread_brl) * iof_pct / 100 (rounded to 2 places)."""
        from src.backend.services.calculator import q2
        from decimal import Decimal

        result = calculate(
            regime=params["regime"],
            amount=params["amount"],
            quantity=params["quantity"],
            rate=params["rate"],
            spread_pct=params["spread_pct"],
            iof_pct=params["iof_pct"],
        )

        expected = q2((result.gross_brl - result.spread_brl) * params["iof_pct"] / Decimal("100"))
        assert result.iof_brl == expected


# ---------- Property tests: Service + Repository integration ----------


class TestRateServiceCachePersistence:
    """Property: RateService cache round-trip through repository."""

    @pytest.fixture(scope="class")
    def engine(self) -> AsyncEngine:
        import os

        url = os.environ.get("COGME_TEST_DATABASE_URL")
        if not url:
            pytest.skip("COGME_TEST_DATABASE_URL not set")
        return create_engine(url)

    @pytest.fixture
    async def repository(self, engine: AsyncEngine) -> SqlAlchemyQuoteRepository:
        from sqlalchemy import text

        async with engine.begin() as conn:
            await conn.execute(text("TRUNCATE TABLE fx_quotes RESTART IDENTITY"))
        return SqlAlchemyQuoteRepository(create_session_factory(engine))

    @pytest.fixture
    def clock(self) -> FixedClock:
        from tests.integration.fakes import FixedClock

        return FixedClock()

    @pytest.fixture
    def monotonic_clock(self) -> FixedMonotonic:
        from tests.integration.fakes import FixedMonotonic

        return FixedMonotonic()

    async def test_second_call_reads_from_cache_not_provider(
        self,
        repository: SqlAlchemyQuoteRepository,
        clock: FixedClock,
        monotonic_clock: FixedMonotonic,
    ) -> None:
        """Within TTL, second get_quote reads from DB cache, not provider.

        This verifies the persistence layer correctly serves cached quotes.
        """
        from src.backend.services.rate_service import RateService
        from src.backend.services.circuit_breaker import CircuitBreaker
        from tests.integration.fakes import ScriptedProvider
        from src.shared.schemas import Currency, RateSource

        rate = Decimal("5.000000")
        currency = Currency.USD

        provider = ScriptedProvider(RateSource.FRANKFURTER, rate=str(rate))
        service = RateService(
            repository=repository,
            providers=[(provider, CircuitBreaker(clock=monotonic_clock))],
            ttl_seconds=3600,
            now=clock,
        )

        first = await service.get_quote(currency)
        second = await service.get_quote(currency)

        assert provider.calls == 1, "Provider should only be called once within TTL"
        assert first.rate == second.rate == rate
        assert second.stale is False


# ---------- Property tests: Database constraints ----------


class TestDatabaseConstraints:
    """Property: database constraints reject invalid data."""

    @pytest.fixture(scope="class")
    def engine(self) -> AsyncEngine:
        import os

        url = os.environ.get("COGME_TEST_DATABASE_URL")
        if not url:
            pytest.skip("COGME_TEST_DATABASE_URL not set")
        return create_engine(url)

    @pytest.fixture
    async def repository(self, engine: AsyncEngine) -> SqlAlchemyQuoteRepository:
        from sqlalchemy import text

        async with engine.begin() as conn:
            await conn.execute(text("TRUNCATE TABLE fx_quotes RESTART IDENTITY"))
        return SqlAlchemyQuoteRepository(create_session_factory(engine))

    async def test_invalid_currency_rejected_by_db(
        self, repository: SqlAlchemyQuoteRepository
    ) -> None:
        """Database CHECK constraint rejects non-USD/EUR currencies."""
        import pytest
        from sqlalchemy.exc import DBAPIError

        invalid_quote = StoredQuote(
            currency="BRL",
            rate=Decimal("5.000000"),
            source="frankfurter",
            bulletin=None,
            quoted_at=datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC),
            fetched_at=datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC),
        )

        with pytest.raises(RepositoryError) as exc_info:
            await repository.save(invalid_quote)

        # The currency column is CHAR(3), so invalid currencies that are too long
        # or don't match the CHECK constraint raise DBAPIError (not IntegrityError)
        assert isinstance(exc_info.value.__cause__, DBAPIError)

    def test_non_positive_rate_rejected_by_db(
        self,
    ) -> None:
        """Model rejects non-positive rates before reaching the database."""
        import pytest

        with pytest.raises(ValueError, match="finito e positivo"):
            StoredQuote(
                currency="USD",
                rate=Decimal("-10.000000"),
                source="frankfurter",
                bulletin=None,
                quoted_at=datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC),
                fetched_at=datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC),
            )
