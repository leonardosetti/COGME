"""Testes de unidade para middlewares - funções diretas."""
from __future__ import annotations

from src.backend.middleware.authorization import require_owner
from src.backend.middleware.csrf import CSRFMiddleware
from src.backend.middleware.rate_limit import rate_limit_exceeded_handler
from src.backend.middleware.session import SessionData, _token_hash


def test_token_hash_returns_sha256_hex() -> None:
    h = _token_hash("token", "pepper")
    assert len(h) == 64
    int(h, 16)


def test_token_hash_is_deterministic() -> None:
    assert _token_hash("token", "pepper") == _token_hash("token", "pepper")


def test_require_owner_returns_callable() -> None:
    dep = require_owner("invoice")
    assert callable(dep)
    dep2 = require_owner("client", resource_id_param="client_id")
    assert callable(dep2)


def test_csrf_middleware_exists() -> None:
    from src.backend.middleware.csrf import CSRFMiddleware

    class FakeApp:
        async def __call__(self, scope, receive, send):
            pass

    mw = CSRFMiddleware(FakeApp())
    assert mw is not None


def test_rate_limit_exceeded_handler_is_callable() -> None:
    from src.backend.middleware.rate_limit import rate_limit_exceeded_handler

    assert callable(rate_limit_exceeded_handler)
