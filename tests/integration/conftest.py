"""Fixtures de tests/integration/: cliente HTTP com o RateService real e fontes falsas.

O ``TestClient`` padrão é criado sem ``with``: assim o ``lifespan`` não roda,
e a API não abre banco, não lê ``COGME_DATABASE_URL`` nem cria cliente HTTP real.
A dependência ``get_rate_service`` é substituída por um ``RateService`` montado
com dublês. Sem rede e sem relógio real.

Para testes que precisam de banco real, use o fixture ``db_client``.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Callable, Iterator
import hashlib
import os
from datetime import datetime, timedelta, timezone
import secrets

import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine

from src.backend.main import app
from src.backend.models.database import create_engine, create_session_factory
from src.backend.models.user import UserSession
from src.backend.routers.common import get_rate_service
from src.backend.services.rate_service import RateService
from src.shared.schemas import RateSource

from .fakes import FixedClock, FixedMonotonic, ScriptedProvider, build_service


# ----- Shared fixtures for integration tests with PostgreSQL -----

def _alembic_config():
    from alembic.config import Config
    from pathlib import Path
    config = Config()
    script_location = Path(__file__).resolve().parents[2] / "migrations"
    config.set_main_option("script_location", str(script_location))
    return config


@pytest.fixture(scope="module")
def migrated() -> None:
    """Run migrations and create test user (id=1)."""
    from alembic import command
    config = _alembic_config()
    with pytest.MonkeyPatch.context() as patch:
        patch.setenv("COGME_DATABASE_URL", os.environ["COGME_TEST_DATABASE_URL"])
        command.upgrade(config, "head")
    # Create test user
    from src.backend.models.user import User, UserStatus
    import asyncio

    async def create_test_user():
        engine = create_engine(os.environ["COGME_TEST_DATABASE_URL"])
        session_factory = create_session_factory(engine)
        async with session_factory() as session:
            from sqlalchemy import select
            result = await session.execute(select(User).where(User.id == 1))
            user = result.scalar_one_or_none()
            if user is None:
                test_user = User(
                    id=1,
                    internal_username_hash="a" * 64,
                    name="Test User",
                    email="test@example.com",
                    cpf="00000000000",
                    password_hash="dummy_hash",
                    status=UserStatus.ACTIVE.value,
                )
                session.add(test_user)
                await session.commit()
        await engine.dispose()

    asyncio.run(create_test_user())
    yield
    with pytest.MonkeyPatch.context() as patch:
        patch.setenv("COGME_DATABASE_URL", os.environ["COGME_TEST_DATABASE_URL"])
        command.downgrade(config, "base")


@pytest.fixture
async def engine(migrated: None) -> AsyncIterator[AsyncEngine]:
    """Database engine with clean tables per test."""
    url = os.environ["COGME_TEST_DATABASE_URL"]
    eng = create_engine(url)
    async with eng.begin() as conn:
        await conn.execute(
            text("TRUNCATE TABLE invoices, invoice_sequences RESTART IDENTITY CASCADE")
        )
    yield eng
    await eng.dispose()


# ----- Common fixtures -----

@pytest.fixture
def clock() -> FixedClock:
    """Relógio UTC falso, começando em 2026-10-30 16:00 UTC."""
    return FixedClock()


@pytest.fixture
def monotonic_clock() -> FixedMonotonic:
    """Relógio monotônico falso dos circuitos."""
    return FixedMonotonic()


@pytest.fixture
def serve_rates() -> Iterator[Callable[[RateService], None]]:
    """Troca o ``RateService`` que a API usa; desfaz a troca ao fim do teste."""

    def _serve(service: RateService) -> None:
        app.dependency_overrides[get_rate_service] = lambda: service

    yield _serve
    app.dependency_overrides.clear()


@pytest.fixture
def rates_service(clock: FixedClock, monotonic_clock: FixedMonotonic) -> RateService:
    """Serviço padrão: Frankfurter responde 5.000000 (primária), PTAX é reserva, cache vazio."""
    return build_service(
        providers=[
            ScriptedProvider(RateSource.FRANKFURTER, rate="5.000000"),
            ScriptedProvider(RateSource.PTAX, rate="5.420600", bulletin="Fechamento"),
        ],
        clock=clock,
        monotonic=monotonic_clock,
    )


@pytest.fixture
def client(serve_rates: Callable[[RateService], None], rates_service: RateService) -> TestClient:
    """Cliente da API já ligado ao serviço padrão (sem banco - lifespan não roda)."""
    serve_rates(rates_service)
    return TestClient(app)


@pytest.fixture
async def db_client(
    serve_rates: Callable[[RateService], None],
    rates_service: RateService,
    engine,  # shared fixture from conftest
) -> AsyncIterator[AsyncClient]:
    """Cliente HTTP async com banco real (configura engine/session_factory no app.state).

    Usa ``AsyncClient`` + ``ASGITransport`` para rodar o app ASGI no mesmo loop de
    eventos do teste pytest-asyncio, evitando ``Event loop is closed``.
    """
    import os

    serve_rates(rates_service)
    # Configura o app com o engine do teste ANTES de criar o cliente
    # para evitar que o lifespan tente ler settings
    app.state.engine = engine
    app.state.session_factory = create_session_factory(engine)
    # Set env var so lifespan doesn't fail if it runs
    os.environ["COGME_DATABASE_URL"] = os.environ["COGME_TEST_DATABASE_URL"]
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as c:
        yield c
    # Cleanup
    app.state.engine = None
    app.state.session_factory = None


# ----- Sessão autenticada (Onda 1 CR-002: P-14 isolamento por proprietário) -----

async def _create_session_for_user(engine: AsyncEngine, user_id: int = 1) -> str:
    """Cria uma sessão válida para ``user_id`` e devolve o token puro."""
    session_factory = create_session_factory(engine)
    token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256((token + os.environ.get("COGME_LOGIN_PEPPER", "")).encode()).hexdigest()
    now = datetime.now(timezone.utc)
    async with session_factory() as session:
        session.add(
            UserSession(
                user_id=user_id,
                token_hash=token_hash,
                created_at=now,
                last_seen_at=now,
                expires_at=now + timedelta(hours=24),
                revoked_at=None,
            )
        )
        await session.commit()
    return token


@pytest.fixture
async def auth_client(db_client: AsyncClient, engine: AsyncEngine) -> AsyncClient:
    """Cliente autenticado como usuário id=1 (sessão + cookie CSRF para rotas mutáveis)."""

    token = await _create_session_for_user(engine)
    # Cookie de sessão + cookie CSRF (mesmo valor, para rotas mutáveis passarem CSRF).
    db_client.cookies.set("session", token)
    db_client.cookies.set("csrf_token", token)
    db_client.headers["X-CSRF-Token"] = token
    return db_client

