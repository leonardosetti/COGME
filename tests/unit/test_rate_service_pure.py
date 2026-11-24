"""Testes de unidade para funções puras de src/backend/services/rate_service.py."""
from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal

from src.backend.models.repository import StoredQuote
from src.backend.services.rate_service import _to_contract
from src.shared.schemas import RateQuote, RateSource


def test_to_contract_maps_all_fields() -> None:
    row = StoredQuote(
        currency="USD",
        rate=Decimal("5.123456"),
        source="frankfurter",
        bulletin=None,
        quoted_at=datetime(2026, 1, 1, tzinfo=UTC),
        fetched_at=datetime(2026, 1, 2, tzinfo=UTC),
    )
    q = _to_contract(row)
    assert q.currency == "USD"
    assert q.rate == Decimal("5.123456")
    assert q.source == RateSource.FRANKFURTER
    assert q.bulletin is None


def test_to_contract_with_bulletin() -> None:
    row = StoredQuote(
        currency="EUR",
        rate=Decimal("6.000000"),
        source="ptax",
        bulletin="Fechamento",
        quoted_at=datetime(2026, 2, 1, tzinfo=UTC),
        fetched_at=datetime(2026, 2, 2, tzinfo=UTC),
    )
    q = _to_contract(row)
    assert q.currency == "EUR"
    assert q.rate == Decimal("6.000000")
    assert q.source == RateSource.PTAX
    assert q.bulletin == "Fechamento"
