"""Testes de unidade para handlers de conta (account.py) chamando funções diretamente.

Cobrem delete_account e reactivate_account passando um SessionData falso
diretamente para as funções, evitando conflito de loop de eventos do anyio.
"""

from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal
from types import SimpleNamespace

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

from fastapi import HTTPException

from starlette.requests import Request

from src.backend.models.database import create_session_factory
from src.backend.models.user import User, UserStatus
from src.backend.middleware.session import SessionData
from src.backend.routers.account import delete_account, reactivate_account


@pytest.fixture
def engine() -> AsyncEngine:
    engine = create_async_engine(
        "postgresql+asyncpg://cogme:dummy-test-local@127.0.0.1:5434/cogme_test",
        echo=False,
    )
    yield engine


@pytest.fixture
async def session_factory(engine: AsyncEngine):
    yield create_session_factory(engine)


@pytest.fixture
async def clean_tables(session_factory: async_sessionmaker[AsyncSession]):
    async with session_factory() as db, db.begin():
        await db.execute(text("DELETE FROM users"))
    yield


@pytest.fixture
async def usuario(session_factory: async_sessionmaker[AsyncSession], clean_tables) -> int:
    async with session_factory() as db, db.begin():
        db.add(
            User(
                id=1,
                internal_username_hash="hash-teste",
                name="Usuário Teste",
                email="teste@exemplo.com",
                password_hash="hash",
                status="active",
            )
        )
    yield 1


@pytest.fixture
def session_data() -> SessionData:
    return SessionData(user_id=1, session_id=1)


@pytest.fixture
def fake_request() -> SimpleNamespace:
    return SimpleNamespace(app=SimpleNamespace(state=SimpleNamespace()))


@pytest.fixture
def fake_request() -> Request:
    scope = {
        "type": "http",
        "method": "POST",
        "path": "/v1/account",
        "headers": [],
        "query_string": b"",
        "client": ("testclient", 50000),
        "server": ("testserver", 80),
        "app": SimpleNamespace(state=SimpleNamespace()),
    }
    return Request(scope)


@pytest.mark.asyncio
async def test_delete_account_sem_sessao(session_factory, session_data, fake_request):
    """delete_account sem sessão deve retornar 401."""
    from src.backend.routers.account import delete_account as del_fn
    with pytest.raises(HTTPException) as exc:
        await del_fn(fake_request, None, session_factory)
    assert exc.value.status_code == 401


@pytest.mark.asyncio
async def test_delete_account_usuario_nao_encontrado(session_factory, session_data, fake_request):
    """delete_account com usuário inexistente deve retornar 404."""
    from src.backend.routers.account import delete_account as del_fn
    sess_data = SessionData(user_id=999, session_id=1)
    with pytest.raises(HTTPException) as exc:
        await del_fn(fake_request, sess_data, session_factory)
    assert exc.value.status_code == 404


@pytest.mark.asyncio
async def test_reactivate_sem_sessao(session_factory, session_data, fake_request):
    """reactivate_account sem sessão deve retornar 401."""
    from src.backend.routers.account import reactivate_account as rea_fn
    with pytest.raises(HTTPException) as exc:
        await rea_fn(
            type("Payload", (), {"identifier": "x@y.com", "password": "s"})(),
            fake_request,
            session_factory,
        )
    assert exc.value.status_code == 401
