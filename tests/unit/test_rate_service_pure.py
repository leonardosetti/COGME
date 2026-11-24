"""Testes de unidade para funcoes puras de src/backend/services/rate_service.py."""
from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal

from src.backend.models.repository import StoredQuote
from src.backend.services.rate_service import _to_contract
from src.shared.schemas import RateQuote, RateSource


def test_to_contract_maps_fields() -> None:
    row = StoredQuote(
        currency="USD",
        rate=Decimal("5.123456"),
        source="frankfurter",
        bulletin=None,
        quoted_at=datetime(2026, 1, 1, tzinfo=UTC),
        fetched_at=datetime(2026, 1, 2, tzinfo=UTC),
    )
    result = _to_contract(row)
    assert result.currency == "USD"
    assert result.rate == Decimal("5.123456")
    assert result.source == RateSource.FRANKFURTER


def test_to_contract_with_bulletin() -> None:
    row = StoredQuote(
        currency="EUR",
        rate=Decimal("6.000000"),
        source="ptax",
        bulletin="Fechamento",
        quoted_at=datetime(2026, 2, 1, tzinfo=UTC),
        fetched_at=datetime(2026, 2, 2, tzinfo=UTC),
    )
    result = _to_contract(row)
    assert result.currency == "EUR"
    assert result.rate == Decimal("6.000000")
    assert result.source == RateSource.PTAX
    assert result.bulletin == "Fechamento"
