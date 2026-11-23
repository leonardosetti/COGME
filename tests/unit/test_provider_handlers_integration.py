"""Testes de unidade para handlers de provedor (provider.py) chamando funções diretamente.

Cobrem handlers que exigem sessão, passando um SessionData falso diretamente
para a função (sem TestClient, evitando conflito de loop de eventos do anyio).
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest
from fastapi import HTTPException
from starlette.requests import Request

from src.backend.routers.provider import (
    get_profile,
    put_profile,
    list_bank_accounts,
    create_bank_account,
    update_bank_account,
    delete_bank_account,
)


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


@pytest.fixture
def fake_request() -> Request:
    scope = {
        "type": "http",
        "method": "POST",
        "path": "/v1/provider",
        "headers": [],
        "query_string": b"",
        "client": ("testclient", 50000),
        "server": ("testserver", 80),
        "app": SimpleNamespace(state=SimpleNamespace()),
    }
    return Request(scope)


@pytest.mark.asyncio
async def test_get_profile_sem_sessao(fake_request, session_data):
    """get_profile sem sessão deve retornar 401."""
    from src.backend.routers.provider import get_profile as gp_fn
    with pytest.raises(HTTPException) as exc:
        await gp_fn(fake_request, None, None)
    assert exc.value.status_code == 401


@pytest.mark.asyncio
async def test_put_profile_sem_sessao(fake_request, session_data):
    """put_profile sem sessão deve retornar 401."""
    from src.backend.routers.provider import put_profile as pp_fn
    with pytest.raises(HTTPException) as exc:
        await pp_fn(fake_request, None, None)
    assert exc.value.status_code == 401


@pytest.mark.asyncio
async def test_list_bank_accounts_sem_sessao(fake_request, session_data):
    """list_bank_accounts sem sessão deve retornar 401."""
    from src.backend.routers.provider import list_bank_accounts as lba_fn
    with pytest.raises(HTTPException) as exc:
        await lba_fn(fake_request, None, None)
    assert exc.value.status_code == 401


@pytest.mark.asyncio
async def test_list_bank_accounts_sem_sessao(fake_request, session_data):
    """list_bank_accounts sem sessão deve retornar 401."""
    from src.backend.routers.provider import list_bank_accounts as lba_fn
    with pytest.raises(HTTPException) as exc:
        await lba_fn(fake_request, None, None)
    assert exc.value.status_code == 401
