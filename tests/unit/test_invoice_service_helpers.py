"""Testes de unidade para funções puras de src/backend/services/invoice_service.py."""
from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal

from src.backend.services.invoice_service import (
    _number_br,
    brl,
    date_br,
    datetime_br,
    money_br,
    percent_br,
    rate_br,
)


def test_number_br_two_places() -> None:
    assert _number_br(Decimal("100.00"), 2) == "100,00"


def test_number_br_three_places() -> None:
    assert _number_br(Decimal("5.000000"), 6) == "5,000000"


def test_brl() -> None:
    assert brl(Decimal("100.00")) == "R$ 100,00"


def test_money_br() -> None:
    assert money_br(Decimal("500.00")) == "500,00"


def test_rate_br() -> None:
    assert rate_br(Decimal("5.000000")) == "5,000000"


def test_percent_br() -> None:
    assert percent_br(Decimal("2.00")) == "2,00 %"


def test_date_br() -> None:
    d = date(2026, 1, 31)
    assert date_br(d) == "31/01/2026"


def test_datetime_br() -> None:
    dt = datetime(2026, 1, 31, 16, 0, 0)
    assert datetime_br(dt) == "31/01/2026 16:00 UTC"
