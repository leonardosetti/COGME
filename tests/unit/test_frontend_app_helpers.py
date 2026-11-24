"""Testes de unidade para src/frontend/app.py (funções puras de formatação)."""
from __future__ import annotations

from decimal import Decimal
from datetime import UTC, datetime

from src.frontend.app import _br_number, _br_datetime


def test_br_number_two_places() -> None:
    assert _br_number("100.00", 2) == "100,00"


def test_br_number_three_places() -> None:
    assert _br_number("5.000000", 6) == "5,000000"


def test_br_number_integer() -> None:
    assert _br_number("100", 2) == "100,00"


def test_br_datetime() -> None:
    assert _br_datetime("2026-01-31T16:00:00+00:00") == "31/01/2026, 16:00:00 UTC"


def test_br_datetime_utc_suffix() -> None:
    assert _br_datetime("2026-01-31T16:00:00Z") == "31/01/2026, 16:00:00 UTC"
