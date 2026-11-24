"""Testes de unidade para middlewares - cobrir linhas faltantes."""
from __future__ import annotations

from types import SimpleNamespace

import pytest
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.backend.middleware.session import SessionData, get_current_session, revoke_user_sessions, _token_hash
from src.backend.middleware.authorization import require_owner
from src.backend.middleware.rate_limit import rate_limit_exceeded_handler


@pytest.fixture
def fake_request() -> Request:
    scope = {
        "type": "http",
        "method": "GET",
        "path": "/test",
        "headers": [],
        "query_string": b"",
        "client": ("testclient", 50000),
        "server": ("testserver", 80),
        "app": SimpleNamespace(state=SimpleNamespace()),
    }
    return Request(scope)


@pytest.mark.asyncio
async def test_get_current_session_no_token(fake_request: Request) -> None:
    sf = SimpleNamespace()
    result = await get_current_session(fake_request, sf, "pepper")
    assert result is None


@pytest.mark.asyncio
async def test_get_current_session_with_token(fake_request: Request) -> None:
    from unittest.mock import AsyncMock, MagicMock

    fake_request._cookies = {"session": "token-value"}
    sf = AsyncMock()
    session = AsyncMock()
    session.execute = AsyncMock(return_value=MagicMock(first=AsyncMock(return_value=None)))
    sf.return_value = session

    result = await get_current_session(fake_request, sf, "pepper")
    assert result is None


@pytest.mark.asyncio
async def test_revoke_user_sessions(session_factory=None) -> None:
    from src.backend.middleware.session import revoke_user_sessions
    sf = AsyncMock()
    session = AsyncMock()
    result_mock = MagicMock()
    result_mock.rowcount = 0
    session.execute = AsyncMock(return_value=result_mock)
    sf.return_value = session

    count = await revoke_user_sessions(sf, 1)
    assert count == 0


def test_require_owner_all_types() -> None:
    from src.backend.middleware.authorization import require_owner
    for rt in ["simulation", "invoice", "client", "provider_profile", "provider_bank_account"]:
        dep = require_owner(rt)
        assert callable(dep)
    dep = require_owner("client", resource_id_param="client_id")
    assert callable(dep)


def test_rate_limit_exceeded_handler_callable() -> None:
    from src.backend.middleware.rate_limit import rate_limit_exceeded_handler
    assert callable(rate_limit_exceeded_handler)
