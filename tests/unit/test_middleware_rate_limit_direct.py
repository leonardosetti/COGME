"""Testes de unidade diretos para rate_limit_exceeded_handler."""
from __future__ import annotations

from types import SimpleNamespace

import pytest


def test_rate_limit_exceeded_handler_is_callable() -> None:
    from src.backend.middleware.rate_limit import rate_limit_exceeded_handler

    assert callable(rate_limit_exceeded_handler)


def test_rate_limit_exceeded_handler_returns_429(monkeypatch: pytest.MonkeyPatch) -> None:
    import asyncio

    from src.backend.middleware.rate_limit import rate_limit_exceeded_handler

    class FakeRequest:
        pass

    async def main() -> None:
        exc = Exception("rate limited")
        resp = await rate_limit_exceeded_handler(FakeRequest(), exc)
        # Mesmo com mock, o retorno deve ser uma resposta HTTP 429
        assert hasattr(resp, "status_code")
        assert resp.status_code == 429

    asyncio.run(main())
