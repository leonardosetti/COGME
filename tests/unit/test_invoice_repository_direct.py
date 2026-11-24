"""Testes de unidade para invoice_repository.py com banco de teste efêmero."""
from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal
from types import SimpleNamespace

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

from src.backend.models.database import create_session_factory
from src.backend.models.invoice import Invoice
from src.backend.models.invoice_repository import (
    InvoiceRepository,
    SqlAlchemyInvoiceRepository,
)
from src.backend.models.user import User


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
        await db.execute(text("DELETE FROM invoices"))
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


from src.backend.middleware.session import SessionData


async def _insert_invoice(
    session_factory: async_sessionmaker[AsyncSession],
    owner_user_id: int,
    invoice_id: int,
    invoice_number: str,
    status: str = "draft",
) -> None:
    async with session_factory() as db, db.begin():
        await db.execute(
            text("""
                INSERT INTO invoices (
                    id, owner_user_id, invoice_number, status, locale,
                    client_country_code, issuer_name, issuer_tax_id_digits,
                    client_name, client_tax_id_digits, regime, currency,
                    amount, quantity, spread_pct, iof_pct, gross_foreign,
                    gross_brl, spread_brl, iof_brl, net_brl, effective_rate,
                    quote_rate, quote_source, quoted_at, stale,
                    periodo_inicio, periodo_fim, description,
                    created_at, updated_at
                ) VALUES (
                    :id, :owner_user_id, :invoice_number, :status, 'pt-BR',
                    'BR', 'Empresa Teste', '12345678901',
                    'Cliente Teste', '', 'hourly', 'USD',
                    100.00, 1.0, 2.00, 0.38, 100.00,
                    500.00, 10.00, 1.86, 488.14, 4.881400,
                    5.000000, 'frankfurter', '2026-01-01 00:00:00+00', false,
                    '2026-01-01 00:00:00+00', '2026-01-31 00:00:00+00', 'Teste',
                    '2026-01-01 00:00:00+00', '2026-01-01 00:00:00+00'
                )
            """),
            {
                "id": invoice_id,
                "owner_user_id": owner_user_id,
                "invoice_number": invoice_number,
                "status": status,
            },
        )


@pytest.mark.asyncio
async def test_get_by_id(session_factory, usuario):
    repo = SqlAlchemyInvoiceRepository(session_factory)
    await _insert_invoice(session_factory, usuario, 1, "INV-001")
    result = await repo.get_by_id(1, usuario)
    assert result is not None
    assert result.invoice_number == "INV-001"


@pytest.mark.asyncio
async def test_get_by_id_not_found(session_factory, usuario):
    repo = SqlAlchemyInvoiceRepository(session_factory)
    result = await repo.get_by_id(999, usuario)
    assert result is None


@pytest.mark.asyncio
async def test_get_by_number(session_factory, usuario):
    repo = SqlAlchemyInvoiceRepository(session_factory)
    await _insert_invoice(session_factory, usuario, 2, "INV-002")
    result = await repo.get_by_number("INV-002", usuario)
    assert result is not None
    assert result.invoice_number == "INV-002"


@pytest.mark.asyncio
async def test_update_status(session_factory, usuario):
    repo = SqlAlchemyInvoiceRepository(session_factory)
    await _insert_invoice(session_factory, usuario, 3, "INV-003", "draft")
    resultado = await repo.update_status(3, usuario, "finalized")
    assert resultado is not None
    assert resultado.status == "finalized"


@pytest.mark.asyncio
async def test_delete(session_factory, usuario):
    repo = SqlAlchemyInvoiceRepository(session_factory)
    await _insert_invoice(session_factory, usuario, 4, "INV-004")
    resultado = await repo.delete(4, usuario)
    assert resultado is True

    resultado2 = await repo.delete(4, usuario)
    assert resultado2 is False


@pytest.mark.asyncio
async def test_get_next_number(session_factory, usuario):
    repo = SqlAlchemyInvoiceRepository(session_factory)
    numero = await repo.get_next_number("12345678901")
    assert numero is not None
    assert isinstance(numero, str)
