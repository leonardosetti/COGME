"""Testes de unidade para rate_limit_exceeded_handler (apenas existência)."""
from __future__ import annotations

from src.backend.middleware.rate_limit import rate_limit_exceeded_handler


def test_rate_limit_exceeded_handler_is_callable() -> None:
    assert callable(rate_limit_exceeded_handler)
