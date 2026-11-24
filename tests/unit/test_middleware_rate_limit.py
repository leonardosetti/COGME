"""Testes de unidade para src/backend/middleware/rate_limit.py."""
from __future__ import annotations

from src.backend.middleware.rate_limit import limiter


def test_limiter_exists() -> None:
    assert limiter is not None


def test_rate_limit_exceeded_handler_exists() -> None:
    from src.backend.middleware.rate_limit import rate_limit_exceeded_handler
    assert callable(rate_limit_exceeded_handler)
