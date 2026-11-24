"""Testes de unidade para handlers de provedor (provider.py) sem sessão."""
from __future__ import annotations

from types import SimpleNamespace

import pytest
from fastapi import HTTPException
from starlette.requests import Request


@pytest.fixture
def fake_request() -> Request:
    scope = {
        "type": "http",
        "method": "GET",
        "path": "/v1/provider/profile",
        "headers": [],
        "query_string": b"",
        "client": ("testclient", 50000),
        "server": ("testserver", 80),
        "app": SimpleNamespace(state=SimpleNamespace()),
    }
    return Request(scope)


@pytest.fixture
def session_data() -> SimpleNamespace:
    return SimpleNamespace(user_id=1, session_id=1)


@pytest.mark.asyncio
async def test_get_profile_sem_sessao(fake_request, session_data) -> None:
    from src.backend.routers.provider import get_profile as gp_fn
    with pytest.raises(HTTPException) as exc:
        await gp_fn(fake_request, None, None)
    assert exc.value.status_code == 401


@pytest.mark.asyncio
async def test_put_profile_sem_sessao(fake_request, session_data) -> None:
    from src.backend.routers.provider import put_profile as pp_fn
    with pytest.raises(HTTPException) as exc:
        await pp_fn(fake_request, None, None)
    assert exc.value.status_code == 401


@pytest.mark.asyncio
async def test_list_bank_accounts_sem_sessao(fake_request, session_data) -> None:
    from src.backend.routers.provider import list_bank_accounts as lba_fn
    with pytest.raises(HTTPException) as exc:
        await lba_fn(fake_request, None, None)
    assert exc.value.status_code == 401
