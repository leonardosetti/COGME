"""Testes de unidade para handlers de clientes (clients.py) chamando funções diretamente.

Cobrem CRUD de clientes passando um SessionData falso diretamente para as
funções, evitando conflito de loop de eventos do anyio do TestClient.
"""

from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal
from types import SimpleNamespace

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from starlette.requests import Request

from src.backend.models.database import create_session_factory
from src.backend.models.user import User
from src.backend.models.client import Client
from src.backend.middleware.session import SessionData
from src.backend.routers.clients import (
    ClientRequest,
    create_client,
    get_client,
    list_clients,
    update_client,
    deactivate_client,
    activate_client,
)


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
        await db.execute(text("DELETE FROM clients"))
        await db.execute(text("DELETE FROM users"))
        await db.execute(text("DELETE FROM countries"))
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
def fake_request() -> Request:
    scope = {
        "type": "http",
        "method": "POST",
        "path": "/v1/clients",
        "headers": [],
        "query_string": b"",
        "client": ("testclient", 50000),
        "server": ("testserver", 80),
        "app": SimpleNamespace(state=SimpleNamespace()),
    }
    return Request(scope)


async def _ensure_country(session_factory: async_sessionmaker[AsyncSession]) -> None:
    async with session_factory() as db, db.begin():
        await db.execute(
            text("INSERT INTO countries (code, name) VALUES ('BR', 'Brasil') ON CONFLICT (code) DO NOTHING")
        )


@pytest.mark.asyncio
async def test_create_client(session_factory, usuario, session_data, fake_request):
    await _ensure_country(session_factory)
    payload = ClientRequest(
        name="Cliente Teste",
        tax_id="12345678901",
        tax_id_type="cpf",
        email="cliente@exemplo.com",
        country_code="BR",
    )
    resp = await create_client(
        payload, fake_request, session_data, session_factory
    )
    assert resp is not None
    assert resp.name == "Cliente Teste"
    assert resp.status == "active"


@pytest.mark.asyncio
async def test_get_client(session_factory, usuario, session_data, fake_request):
    await _ensure_country(session_factory)
    async with session_factory() as db, db.begin():
        db.add(
            Client(
                id=1,
                owner_user_id=1,
                name="Cliente A",
                tax_id_digits=None,
                tax_id_type="foreign",
                country_code="BR",
                status="active",
            )
        )
    resp = await get_client(1, fake_request, session_data, session_factory)
    assert resp is not None
    assert resp.name == "Cliente A"


@pytest.mark.asyncio
async def test_list_clients(session_factory, usuario, session_data, fake_request):
    await _ensure_country(session_factory)
    async with session_factory() as db, db.begin():
        db.add_all(
            [
                Client(
                    id=1, owner_user_id=1, name="Cliente A",
                    tax_id_digits=None, tax_id_type="foreign",
                    country_code="BR", status="active",
                ),
                Client(
                    id=2, owner_user_id=1, name="Cliente B",
                    tax_id_digits=None, tax_id_type="foreign",
                    country_code="BR", status="active",
                ),
            ]
        )
    resp = await list_clients(fake_request, session_data, session_factory, 50, 0)
    assert len(resp) == 2


@pytest.mark.asyncio
async def test_deactivate_and_activate_client(session_factory, usuario, session_data, fake_request):
    await _ensure_country(session_factory)
    async with session_factory() as db, db.begin():
        db.add(
            Client(
                id=1,
                owner_user_id=1,
                name="Cliente A",
                tax_id_digits=None,
                tax_id_type="foreign",
                country_code="BR",
                status="active",
            )
        )
    resp = await deactivate_client(1, fake_request, session_data, session_factory)
    assert resp["message"] == "Cliente inativado."
    resp = await activate_client(1, fake_request, session_data, session_factory)
    assert resp["message"] == "Cliente reativado."


@pytest.mark.asyncio
async def test_update_client(session_factory, usuario, session_data, fake_request):
    await _ensure_country(session_factory)
    async with session_factory() as db, db.begin():
        db.add(
            Client(
                id=1,
                owner_user_id=1,
                name="Cliente Antigo",
                tax_id_digits=None,
                tax_id_type="foreign",
                country_code="BR",
                status="active",
            )
        )
    payload = ClientRequest(name="Cliente Novo", country_code="BR")
    resp = await update_client(1, payload, fake_request, session_data, session_factory)
    assert resp.name == "Cliente Novo"
