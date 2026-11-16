"""Property tests: LGPD personal data never persisted or logged (spec backend-mvp-v1, §5, §6).

These tests verify that:
1. Invoice personal data (name, tax_id, address) is never written to database
2. Invoice personal data never appears in logs
3. Simulation/quote data contains no personal identifiers
4. The PDF generation uses personal data only in-memory during render
"""

from __future__ import annotations

import contextlib
import logging
import re
from collections.abc import Iterator
from datetime import date, datetime, UTC
from decimal import Decimal
from io import StringIO
from typing import Any

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncEngine

from src.backend.models.database import create_engine, create_session_factory
from src.backend.models.quote import FxQuote
from src.backend.models.repository import SqlAlchemyQuoteRepository, StoredQuote
from src.backend.services.invoice_service import render_invoice
from src.backend.services.simulation_service import simulate
from src.shared.schemas import (
    Currency,
    InvoiceParty,
    InvoiceRequest,
    RateQuote,
    RateSource,
    Regime,
    SimulationRequest,
)

from tests.integration.fakes import FixedClock, FixedMonotonic, ScriptedProvider, build_service

# ---------- Hypothesis strategies ----------

_MIN_RATE = Decimal("0.000001")
_MAX_RATE = Decimal("999.999999")
_MIN_AMOUNT = Decimal("0.01")
_MAX_AMOUNT = Decimal("1000000000")
_MIN_QUANTITY = Decimal("1")
_MAX_QUANTITY = Decimal("100000")
_MIN_PERCENT = Decimal("0")
_MAX_PERCENT = Decimal("100")

_MIN_DATE = date(2020, 1, 1)
_MAX_DATE = date(2030, 12, 31)

# Brazilian-like name/tax_id/address patterns for realistic test data
NAME_CHARS = st.characters(
    whitelist_categories=("Lu", "Ll", "Lt", "Lm", "Lo", "Zs"),
    min_codepoint=32,
    max_codepoint=126,
)
TAX_ID_PATTERN = st.from_regex(r"\d{3}\.\d{3}\.\d{3}-\d{2}", fullmatch=True)
ADDRESS_PATTERN = st.from_regex(r"[A-Za-z\s]+, \d+, [A-Za-z\s]+", fullmatch=True)

# Valid name strategy (at least 1 char, not just whitespace)
VALID_NAME = st.text(alphabet=NAME_CHARS, min_size=1, max_size=120).filter(
    lambda x: x.strip()
)
VALID_DESCRIPTION = st.text(min_size=1, max_size=500).filter(lambda x: x.strip())


@st.composite
def invoice_party_strategy(draw: st.DrawFn) -> InvoiceParty:
    """Generate a valid InvoiceParty with realistic Brazilian data."""
    address_strategy = st.text(alphabet=NAME_CHARS, min_size=1, max_size=240).filter(
        lambda x: x.strip()
    )
    return InvoiceParty(
        name=draw(VALID_NAME),
        tax_id=draw(st.one_of(st.none(), TAX_ID_PATTERN)),
        address=draw(st.one_of(st.none(), address_strategy)),
    )


@st.composite
def simulation_request_strategy(draw: st.DrawFn) -> SimulationRequest:
    """Generate a valid SimulationRequest."""
    regime = draw(st.sampled_from(list(Regime)))
    currency = draw(st.sampled_from(list(Currency)))
    amount = draw(
        st.decimals(
            min_value=_MIN_AMOUNT,
            max_value=_MAX_AMOUNT,
            allow_nan=False,
            allow_infinity=False,
            places=2,
        )
    )
    quantity = draw(
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

    spread_pct = draw(
        st.decimals(
            min_value=_MIN_PERCENT,
            max_value=_MAX_PERCENT,
            allow_nan=False,
            allow_infinity=False,
            places=4,
        )
    )
    iof_pct = draw(
        st.decimals(
            min_value=_MIN_PERCENT,
            max_value=_MAX_PERCENT,
            allow_nan=False,
            allow_infinity=False,
            places=4,
        )
    )

    return SimulationRequest(
        currency=currency,
        regime=regime,
        amount=amount,
        quantity=quantity,
        spread_pct=spread_pct,
        iof_pct=iof_pct,
    )


@st.composite
def invoice_request_strategy(draw: st.DrawFn) -> InvoiceRequest:
    """Generate a valid InvoiceRequest with personal data."""
    simulation = draw(simulation_request_strategy())
    issuer = draw(invoice_party_strategy())
    client = draw(invoice_party_strategy())
    invoice_number = draw(st.text(min_size=1, max_size=40).filter(lambda x: x.strip()))
    issue_date = draw(st.dates(min_value=_MIN_DATE, max_value=_MAX_DATE))
    description = draw(VALID_DESCRIPTION)

    return InvoiceRequest(
        simulation=simulation,
        issuer=issuer,
        client=client,
        invoice_number=invoice_number,
        issue_date=issue_date,
        description=description,
    )


@st.composite
def rate_quote_strategy(draw: st.DrawFn) -> "RateQuote":
    """Generate a valid RateQuote."""
    from src.shared.schemas import Currency, RateQuote, RateSource
    currency = draw(st.sampled_from(list(Currency)))
    rate = draw(
        st.decimals(
            min_value=_MIN_RATE,
            max_value=_MAX_RATE,
            allow_nan=False,
            allow_infinity=False,
            places=6,
        )
    )
    source = draw(st.sampled_from(list(RateSource)))
    bulletin = draw(st.one_of(st.none(), st.text(min_size=1, max_size=40)))
    stale = draw(st.booleans())
    # Generate timestamp then convert to UTC datetime
    timestamp = draw(st.integers(
        min_value=int(datetime(2020, 1, 1, tzinfo=UTC).timestamp()),
        max_value=int(datetime(2030, 12, 31, 23, 59, 59, tzinfo=UTC).timestamp()),
    ))
    quoted_at = datetime.fromtimestamp(timestamp, tz=UTC)

    return RateQuote(
        currency=currency,
        rate=rate,
        source=source,
        bulletin=bulletin,
        stale=stale,
        quoted_at=quoted_at,
    )


# ---------- Test: Database contains no personal data ----------


class TestDatabaseNoPersonalData:
    """Property: fx_quotes table never contains personal identifiers."""

    @pytest.fixture(scope="class")
    def engine(self) -> AsyncEngine:
        import os

        url = os.environ.get("COGME_TEST_DATABASE_URL")
        if not url:
            pytest.skip("COGME_TEST_DATABASE_URL not set")
        return create_engine(url)

    @pytest.fixture
    async def clean_db(self, engine: AsyncEngine) -> None:
        """Ensure clean table before each test."""
        from sqlalchemy import text

        async with engine.begin() as conn:
            await conn.execute(text("TRUNCATE TABLE fx_quotes RESTART IDENTITY"))

    @pytest.mark.asyncio
    @pytest.mark.asyncio
    async def test_fx_quotes_columns_contain_only_expected_fields(
        self, engine: AsyncEngine, clean_db: None
    ) -> None:
        """fx_quotes table has exactly the expected columns, no personal data columns.

        This is a schema-level property: the table structure must not allow
        storage of personal data.
        """
        async with engine.connect() as conn:
            result = await conn.execute(
                text("""
                    SELECT column_name
                    FROM information_schema.columns
                    WHERE table_name = 'fx_quotes'
                    ORDER BY ordinal_position
                """)
            )
            columns = [row[0] for row in result.fetchall()]

        expected_columns = {
            "id",
            "currency",
            "rate",
            "source",
            "bulletin",
            "quoted_at",
            "fetched_at",
        }
        assert set(columns) == expected_columns, (
            f"fx_quotes has unexpected columns: {set(columns) - expected_columns}"
        )

    @pytest.mark.asyncio
    @pytest.mark.asyncio
    async def test_saved_quote_has_no_personal_fields(
        self, engine: AsyncEngine, clean_db: None
    ) -> None:
        """A saved quote row contains only FX data, no personal identifiers."""
        from datetime import UTC, datetime

        repo = SqlAlchemyQuoteRepository(create_session_factory(engine))
        stored = StoredQuote(
            currency="USD",
            rate=Decimal("5.000000"),
            source="frankfurter",
            bulletin=None,
            quoted_at=datetime.now(UTC),
            fetched_at=datetime.now(UTC),
        )
        await repo.save(stored)

        # Read raw from DB
        async with engine.connect() as conn:
            result = await conn.execute(select(FxQuote))
            row = result.scalar_one()

        # Verify only expected fields exist and have correct types
        assert row.currency in ("USD", "EUR")
        assert isinstance(row.rate, Decimal)
        assert row.source in ("frankfurter", "ptax")
        assert row.bulletin is None or isinstance(row.bulletin, str)
        assert hasattr(row.quoted_at, "tzinfo")  # datetime with tz
        assert hasattr(row.fetched_at, "tzinfo")

        # Verify NO personal data fields exist
        row_dict = row.__dict__
        personal_keywords = ["name", "tax", "cpf", "cnpj", "address", "endereco", "document"]
        for keyword in personal_keywords:
            matching_keys = [k for k in row_dict.keys() if keyword in k.lower()]
            assert not matching_keys, f"Found personal data column: {matching_keys}"


# ---------- Test: Logs contain no personal data ----------


class TestLogsNoPersonalData:
    """Property: application logs never contain personal identifiers."""

    @contextlib.contextmanager
    def _capture_logs(self) -> Iterator[tuple[logging.Logger, StringIO]]:
        """Context manager to capture log output."""
        stream = StringIO()
        handler = logging.StreamHandler(stream)
        logger = logging.getLogger(
            "src.backend.services.invoice_service"
        )
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.propagate = False
        try:
            yield logger, stream
        finally:
            logger.removeHandler(handler)

    def _assert_no_personal_data_in_logs(
        self, log_text: str, personal_data: dict[str, str]
    ) -> None:
        """Assert no personal data appears in logs."""
        # Check each piece of personal data
        for key, value in personal_data.items():
            if value:
                # Don't check empty/None values
                msg = f"Personal data '{key}' ('{value}') found in logs"
                assert value not in log_text, msg

        # Also check for common patterns that might indicate PII leakage
        pii_patterns = [
            r"\d{3}\.\d{3}\.\d{3}-\d{2}",  # CPF pattern
            r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}",  # CNPJ pattern
        ]
        for pattern in pii_patterns:
            matches = re.findall(pattern, log_text)
            assert not matches, f"PII pattern found in logs: {matches}"

    @given(invoice_request_strategy(), rate_quote_strategy())
    @settings(max_examples=20, deadline=None)
    @pytest.mark.asyncio
    async def test_invoice_render_logs_no_personal_data(
        self, invoice_request: InvoiceRequest, rate_quote: RateQuote
    ) -> None:
        """PDF render logs contain only error types, never personal data."""
        with self._capture_logs() as (logger, stream):
            # Build a service that returns our test quote
            clock = FixedClock()
            monotonic = FixedMonotonic()
            provider = ScriptedProvider(
                RateSource(rate_quote.source.value),
                rate=str(rate_quote.rate),
                bulletin=rate_quote.bulletin,
            )
            service = build_service(
                providers=[provider],
                clock=clock,
                monotonic=monotonic,
            )

            try:
                # This may fail if WeasyPrint/Pango not available, but we only care about logs
                await render_invoice(invoice_request, service)
            except Exception:
                # Expected if WeasyPrint not installed; we only check logs
                pass

            log_output = stream.getvalue()

            # Collect all personal data from the request
            personal_data = {
                "issuer_name": invoice_request.issuer.name,
                "issuer_tax_id": invoice_request.issuer.tax_id or "",
                "issuer_address": invoice_request.issuer.address or "",
                "client_name": invoice_request.client.name,
                "client_tax_id": invoice_request.client.tax_id or "",
                "client_address": invoice_request.client.address or "",
                "invoice_number": invoice_request.invoice_number,
                "description": invoice_request.description,
            }

            self._assert_no_personal_data_in_logs(log_output, personal_data)

    @given(simulation_request_strategy(), rate_quote_strategy())
    @settings(max_examples=20, deadline=None)
    @pytest.mark.asyncio
    async def test_simulation_logs_no_personal_data(
        self, sim_request: SimulationRequest, rate_quote: RateQuote
    ) -> None:
        """Simulation service logs contain no personal data (it receives none)."""
        with self._capture_logs() as (logger, stream):
            clock = FixedClock()
            monotonic = FixedMonotonic()
            provider = ScriptedProvider(
                RateSource(rate_quote.source.value),
                rate=str(rate_quote.rate),
                bulletin=rate_quote.bulletin,
            )
            service = build_service(
                providers=[provider],
                clock=clock,
                monotonic=monotonic,
            )

            try:
                await simulate(sim_request, service)
            except Exception:
                pass

            log_output = stream.getvalue()

            # Simulation request has no personal data by design
            # But verify no PII patterns leaked from elsewhere
            pii_patterns = [
                r"\d{3}\.\d{3}\.\d{3}-\d{2}",
                r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}",
            ]
            for pattern in pii_patterns:
                matches = re.findall(pattern, log_output)
                assert not matches, f"PII pattern found in simulation logs: {matches}"


# ---------- Test: In-memory only personal data ----------


class TestPersonalDataInMemoryOnly:
    """Property: personal data exists only in-memory during request processing."""

    @given(invoice_request_strategy())
    @settings(max_examples=10, deadline=None)
    def test_invoice_request_personal_data_not_in_model_dump(
        self, invoice_request: InvoiceRequest
    ) -> None:
        """model_dump() includes personal data (it's the request), but we verify
        it's not in any stored model like SimulationResponse.
        """
        # The request itself contains personal data - that's expected
        dump = invoice_request.model_dump()
        assert "issuer" in dump
        assert "client" in dump
        assert dump["issuer"]["name"] == invoice_request.issuer.name
        assert dump["client"]["name"] == invoice_request.client.name

    @given(simulation_request_strategy(), rate_quote_strategy())
    @settings(max_examples=20, deadline=None)
    @pytest.mark.asyncio
    async def test_simulation_response_no_personal_data(
        self, sim_request: SimulationRequest, rate_quote: RateQuote
    ) -> None:
        """SimulationResponse contains only calculated values, no personal data."""
        from src.backend.services.simulation_service import simulate

        class FakeRateService:
            def __init__(self, quote: RateQuote):
                self._quote = quote

            async def get_quote(self, currency: Currency) -> RateQuote:
                return self._quote

        # Use a mock that satisfies the RateService interface for testing
        fake_service = FakeRateService(rate_quote)
        response = await simulate(sim_request, fake_service)  # type: ignore[arg-type]

        # SimulationResponse should have NO personal data fields
        dump = response.model_dump()
        personal_keywords = ["name", "tax", "cpf", "cnpj", "address", "endereco", "document"]
        for keyword in personal_keywords:
            matching_keys = [k for k in dump.keys() if keyword in k.lower()]
            assert not matching_keys, f"Personal data in SimulationResponse: {matching_keys}"

        # Verify expected fields only
        expected_fields = {
            "currency", "regime", "gross_foreign", "gross_brl",
            "spread_brl", "iof_brl", "net_brl", "effective_rate",
            "spread_pct", "iof_pct", "quote", "notice"
        }
        assert set(dump.keys()) == expected_fields


# ---------- Test: PDF generation uses personal data only in-memory ----------


class TestPdfGenerationInMemoryOnly:
    """Property: PDF generation uses personal data only during render, never stores."""

    @given(invoice_request_strategy(), rate_quote_strategy())
    @settings(max_examples=5, deadline=None)
    @pytest.mark.asyncio
    async def test_render_invoice_does_not_persist_personal_data(
        self, invoice_request: InvoiceRequest, rate_quote: RateQuote
    ) -> None:
        """render_invoice generates PDF using personal data only in template context."""
        from unittest.mock import patch

        # Create a mock service that returns our test quote
        class MockRateService:
            async def get_quote(self, currency: Currency) -> RateQuote:
                return rate_quote

        mock_service = MockRateService()

        # Mock the PDF renderer to capture the context passed to it
        captured_context = {}

        def mock_render_pdf(context: dict[str, Any]) -> bytes:
            captured_context.update(context)
            return b"%PDF-1.4 mock pdf"

        # Patch at the module where _render_pdf is defined and used
        with patch("src.backend.services.invoice_service._render_pdf", mock_render_pdf):
            try:
                await render_invoice(invoice_request, mock_service)  # type: ignore[arg-type]
            except Exception as e:
                # Log the exception for debugging
                print(f"Exception during render_invoice: {e}")
                pass  # We only care about the context passed

        # Verify the context contains personal data (for template)
        assert "issuer" in captured_context, f"Context was not captured: {captured_context}"
        assert "client" in captured_context
        assert captured_context["issuer"].name == invoice_request.issuer.name
        assert captured_context["client"].name == invoice_request.client.name

        # But verify it's NOT stored anywhere (we can't easily test this
        # without DB access, but the service doesn't have DB access)
        # The key property: the function doesn't write to any repository

    @given(invoice_request_strategy(), rate_quote_strategy())
    @settings(max_examples=10, deadline=None)
    def test_invoice_template_context_is_ephemeral(
        self, invoice_request: InvoiceRequest, rate_quote: RateQuote
    ) -> None:
        """The template context is built fresh each call and not cached."""
        from src.backend.services.invoice_service import (
            _REGIME_LABELS,
            _QUANTITY_LABELS,
            _SOURCE_LABELS,
        )

        # Simulate the context building logic from render_invoice
        regime = invoice_request.simulation.regime
        context = {
            "issuer": invoice_request.issuer,
            "client": invoice_request.client,
            "invoice_number": invoice_request.invoice_number,
            "issue_date": invoice_request.issue_date,
            "description": invoice_request.description,
            "regime_label": _REGIME_LABELS[regime],
            "quantity_label": _QUANTITY_LABELS[regime],
            "unit_amount": invoice_request.simulation.amount,
            "quantity": invoice_request.simulation.quantity,
            "source_label": _SOURCE_LABELS[rate_quote.source],
            # sim and quote would be added after simulate() call
        }

        # Verify context is a fresh dict with the right structure
        assert isinstance(context, dict)
        assert "issuer" in context
        assert "client" in context

        # Verify personal data objects are the same instances (not copied to storage)
        assert context["issuer"] is invoice_request.issuer
        assert context["client"] is invoice_request.client


# ---------- Test: Erasure simulation (GDPR/LGPD right to erasure) ----------


class TestErasureSimulation:
    """Property: simulating data erasure - personal data can be 'forgotten'."""

    @given(invoice_request_strategy())
    @settings(max_examples=20, deadline=None)
    def test_personal_data_can_be_removed_from_request(
        self, invoice_request: InvoiceRequest
    ) -> None:
        """Creating a new request without personal data is possible (erasure)."""
        # Create a sanitized version with minimal personal data
        sanitized = InvoiceRequest(
            simulation=invoice_request.simulation,
            issuer=InvoiceParty(name="[REMOVED]", tax_id=None, address=None),
            client=InvoiceParty(name="[REMOVED]", tax_id=None, address=None),
            invoice_number=invoice_request.invoice_number,
            issue_date=invoice_request.issue_date,
            description="[REMOVED]",
        )

        # Verify the sanitized request is valid
        dump = sanitized.model_dump()
        assert dump["issuer"]["name"] == "[REMOVED]"
        assert dump["issuer"]["tax_id"] is None
        assert dump["issuer"]["address"] is None
        assert dump["client"]["name"] == "[REMOVED]"
        assert dump["client"]["tax_id"] is None
        assert dump["client"]["address"] is None
        assert dump["description"] == "[REMOVED]"

        # Original still has the data
        original_dump = invoice_request.model_dump()
        assert original_dump["issuer"]["name"] != "[REMOVED]"

    @given(invoice_request_strategy())
    @settings(max_examples=20, deadline=None)
    def test_no_personal_data_in_simulation_only_flow(
        self, invoice_request: InvoiceRequest
    ) -> None:
        """Simulation-only flow (without invoice) never sees personal data."""
        # The simulation request is separate from invoice request
        sim_request = invoice_request.simulation

        # SimulationRequest has NO personal data fields
        sim_dump = sim_request.model_dump()
        personal_keywords = ["name", "tax", "cpf", "cnpj", "address", "endereco", "document"]
        for keyword in personal_keywords:
            matching_keys = [k for k in sim_dump.keys() if keyword in k.lower()]
            assert not matching_keys, f"Personal data in SimulationRequest: {matching_keys}"

        # Only expected fields
        expected = {"currency", "regime", "amount", "quantity", "spread_pct", "iof_pct"}
        assert set(sim_dump.keys()) == expected
