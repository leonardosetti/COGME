"""Invoices persistence: CRUD + erase + clone + finalize (DEC-04, DEC-05, DEC-06, DEC-07).

Testes de integração com banco real (PostgreSQL via COGME_TEST_DATABASE_URL)
e property tests de reprocessamento (persistência = reprocesso).
"""

from __future__ import annotations

import itertools
import os
from datetime import date, datetime, UTC
from decimal import Decimal

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncEngine

from src.backend.main import app
from src.backend.models.database import create_session_factory
from src.backend.models.invoice_repository import (
    InvoiceRepository,
    SqlAlchemyInvoiceRepository,
)
from src.backend.middleware.session import SessionData
from src.backend.services.rate_service import RateService
from src.shared.schemas import RateSource, Regime

from .fakes import FixedClock, FixedMonotonic, ScriptedProvider, build_service, SPEC_EXAMPLE_BODY

pytestmark = [
    pytest.mark.postgres,
    pytest.mark.skipif(
        not os.environ.get("COGME_TEST_DATABASE_URL"),
        reason="COGME_TEST_DATABASE_URL não definida: teste de PostgreSQL pulado.",
    ),
]

INVOICES = "/v1/invoices"
OWNER_USER_ID = 1
BASE_INSTANT = datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC)

# Ids únicos para invoices criadas nos testes (a tabela não tem auto-incremento).
_invoice_id = itertools.count(1)


@pytest.fixture
async def invoice_repo(engine: AsyncEngine) -> InvoiceRepository:
    return SqlAlchemyInvoiceRepository(create_session_factory(engine))


@pytest.fixture
def rate_service(clock: FixedClock, monotonic_clock: FixedMonotonic) -> RateService:
    return build_service(
        providers=[
            ScriptedProvider(RateSource.FRANKFURTER, rate="5.000000"),
            ScriptedProvider(RateSource.PTAX, rate="5.420600", bulletin="Fechamento"),
        ],
        clock=clock,
        monotonic=monotonic_clock,
    )


@pytest.fixture
def client(serve_rates: callable, rate_service: RateService) -> TestClient:
    serve_rates(rate_service)
    return TestClient(app)


def _make_invoice_payload(
    owner_user_id: int = OWNER_USER_ID,
    **overrides
) -> dict:
    payload = {
        "simulation": SPEC_EXAMPLE_BODY,
        "issuer": {
            "name": "Pessoa Fictícia da Silva",
            "tax_id": "000.000.000-00",
            "address": "Rua Exemplo, 123, Cidade Fictícia",
        },
        "client": {
            "name": "Example Fictional LLC",
            "tax_id": None,
            "address": "1 Sample Street, Nowhere",
        },
        "invoice_number": "INV-202611-0001",
        "issue_date": "2026-01-15",
        "description": "Serviços fictícios de desenvolvimento de software.",
    }
    payload.update(overrides)
    return payload

# ---------- Teste: Property persistence = reprocessing ----------


async def test_persistence_roundtrip_equals_reprocess(
    invoice_repo: InvoiceRepository,
) -> None:
    """Persistir invoice e ler de volta == reprocessar valores originais.

    Valida a propriedade central: persistência não transforma dados.
    """
    from src.backend.services.invoice_number import InvoiceNumberService

    # Cria invoice via repository
    async with invoice_repo.session_factory() as session:
        number_service = InvoiceNumberService(session)
        invoice_number = await number_service.generate("00000000000000")

    from datetime import datetime, UTC
    now = datetime.now(UTC)

    stored = type('StoredInvoice', (), {
        'id': next(_invoice_id),
        'owner_user_id': OWNER_USER_ID,
        'client_id': None,
        'simulation_id': None,
        'invoice_number': invoice_number,
        'status': 'finalized',
        'locale': 'pt-BR',
        'client_country_code': 'US',
        'issuer_name': 'Pessoa Fictícia da Silva',
        'issuer_tax_id_digits': '00000000000000',
        'issuer_address': 'Rua Exemplo, 123',
        'client_name': 'Example Fictional LLC',
        'client_tax_id_digits': '11111111111111',
        'client_address': '1 Sample Street',
        'banco': None,
        'agencia': None,
        'conta_com_digito': None,
        'pix_key': None,
        'periodo_inicio': date(2026, 1, 1),
        'periodo_fim': date(2026, 1, 31),
        'description': 'Serviços fictícios',
        'regime': 'hourly',
        'currency': 'USD',
        'amount': Decimal('30.00'),
        'quantity': Decimal('160'),
        'spread_pct': Decimal('2'),
        'iof_pct': Decimal('0.38'),
        'gross_foreign': Decimal('4800.00'),
        'gross_brl': Decimal('24000.00'),
        'spread_brl': Decimal('480.00'),
        'iof_brl': Decimal('89.38'),
        'net_brl': Decimal('23430.62'),
        'effective_rate': Decimal('4.881379'),
        'quote_rate': Decimal('5.000000'),
        'quote_source': 'frankfurter',
        'quote_bulletin': None,
        'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
        'stale': False,
        'finalized_at': now,
        'supersedes_invoice_id': None,
        'created_at': now,
        'updated_at': now,
    })()

    await invoice_repo.save(stored)

    # Lê de volta
    retrieved = await invoice_repo.get_by_id(stored.id, OWNER_USER_ID)
    assert retrieved is not None

    # Reprocessa valores originais
    from src.backend.services.calculator import calculate
    recalc = calculate(
        regime=Regime.HOURLY,
        amount=Decimal('30.00'),
        quantity=Decimal('160'),
        rate=Decimal('5.000000'),
        spread_pct=Decimal('2'),
        iof_pct=Decimal('0.38'),
    )

    # Compara: persistido == reprocessado
    assert retrieved.gross_foreign == recalc.gross_foreign
    assert retrieved.gross_brl == recalc.gross_brl
    assert retrieved.spread_brl == recalc.spread_brl
    assert retrieved.iof_brl == recalc.iof_brl
    assert retrieved.net_brl == recalc.net_brl
    assert retrieved.effective_rate == recalc.effective_rate

    # Identity check
    assert retrieved.gross_brl - retrieved.spread_brl - retrieved.iof_brl == retrieved.net_brl

# ---------- Teste: Listagem ----------


async def test_list_invoices_empty(auth_client: AsyncClient) -> None:
    """Lista vazia retorna 200 com lista vazia."""
    response = await auth_client.get(f"{INVOICES}?owner_user_id={OWNER_USER_ID}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data == []


async def test_list_invoices_with_data(
    auth_client: AsyncClient, invoice_repo: InvoiceRepository
) -> None:
    """Lista invoices com filtros status e client_id."""
    from datetime import datetime, UTC
    from src.backend.services.invoice_number import InvoiceNumberService

    async def _create_invoice(status: str, client_id: int | None = None):
        async with invoice_repo.session_factory() as session:
            number_service = InvoiceNumberService(session)
            invoice_number = await number_service.generate("00000000000000")

        stored = type('StoredInvoice', (), {
            'id': next(_invoice_id), 'owner_user_id': OWNER_USER_ID, 'client_id': client_id,
            'simulation_id': None, 'invoice_number': invoice_number,
            'status': status, 'locale': 'pt-BR', 'client_country_code': 'US',
            'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',
            'issuer_address': None, 'client_name': 'Cliente',
            'client_tax_id_digits': '11111111111111',
            'client_address': None, 'banco': None, 'agencia': None,
            'conta_com_digito': None, 'pix_key': None,
            'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
            'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
            'amount': Decimal('10'), 'quantity': Decimal('10'),
            'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
            'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
            'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
            'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
            'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
            'quote_bulletin': None,
            'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
            'stale': False, 'finalized_at': datetime.now(UTC) if status == 'finalized' else None,
            'supersedes_invoice_id': None,
            'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
        })()
        await invoice_repo.save(stored)
        return stored.id

    # Cria 2 finalized, 1 draft
    await _create_invoice('finalized')
    await _create_invoice('finalized')
    draft_id = await _create_invoice('draft')

    # Lista todas
    response = await auth_client.get(f"{INVOICES}?owner_user_id={OWNER_USER_ID}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3

    # Filtra finalized
    response = await auth_client.get(f"{INVOICES}?owner_user_id={OWNER_USER_ID}&status=finalized")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2

    # Filtra draft
    response = await auth_client.get(f"{INVOICES}?owner_user_id={OWNER_USER_ID}&status=draft")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["id"] == draft_id

# ---------- Teste: GET / PDF ----------


async def test_get_invoice_detail(auth_client: AsyncClient, invoice_repo: InvoiceRepository) -> None:
    """GET /v1/invoices/{id} retorna detalhes completos."""
    from datetime import datetime, UTC
    from src.backend.services.invoice_number import InvoiceNumberService

    async with invoice_repo.session_factory() as session:
        number_service = InvoiceNumberService(session)
        invoice_number = await number_service.generate("00000000000000")

    stored = type('StoredInvoice', (), {
        'id': next(_invoice_id), 'owner_user_id': OWNER_USER_ID, 'client_id': None,
        'simulation_id': None, 'invoice_number': invoice_number,
        'status': 'finalized', 'locale': 'pt-BR', 'client_country_code': 'US',
        'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',
        'issuer_address': 'Rua A', 'client_name': 'Cliente',
        'client_tax_id_digits': '11111111111111',
        'client_address': 'Rua B', 'banco': None, 'agencia': None,
        'conta_com_digito': None, 'pix_key': None,
        'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
        'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
        'amount': Decimal('10'), 'quantity': Decimal('10'),
        'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
        'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
        'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
        'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
        'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
        'quote_bulletin': None,
        'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
        'stale': False, 'finalized_at': datetime.now(UTC),
        'supersedes_invoice_id': None,
        'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
    })()
    await invoice_repo.save(stored)
    inv_id = stored.id

    response = await auth_client.get(f"{INVOICES}/{inv_id}?owner_user_id={OWNER_USER_ID}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert response.content.startswith(b"%PDF-")
    assert f'invoice_{invoice_number}.pdf' in response.headers["content-disposition"]


async def test_get_invoice_pdf(auth_client: AsyncClient, invoice_repo: InvoiceRepository) -> None:
    """GET /v1/invoices/{id}?as_pdf=true retorna PDF (Content-Disposition attachment)."""
    from datetime import datetime, UTC
    from src.backend.services.invoice_number import InvoiceNumberService

    async with invoice_repo.session_factory() as session:
        number_service = InvoiceNumberService(session)
        invoice_number = await number_service.generate("00000000000000")

    stored = type('StoredInvoice', (), {
        'id': next(_invoice_id), 'owner_user_id': OWNER_USER_ID, 'client_id': None,
        'simulation_id': None, 'invoice_number': invoice_number,
        'status': 'finalized', 'locale': 'pt-BR', 'client_country_code': 'US',
        'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',
        'issuer_address': None, 'client_name': 'Cliente',
        'client_tax_id_digits': '11111111111111',
        'client_address': None, 'banco': None, 'agencia': None,
        'conta_com_digito': None, 'pix_key': None,
        'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
        'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
        'amount': Decimal('10'), 'quantity': Decimal('10'),
        'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
        'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
        'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
        'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
        'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
        'quote_bulletin': None,
        'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
        'stale': False, 'finalized_at': datetime.now(UTC),
        'supersedes_invoice_id': None,
        'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
    })()
    await invoice_repo.save(stored)
    inv_id = stored.id

    response = await auth_client.get(f"{INVOICES}/{inv_id}?owner_user_id={OWNER_USER_ID}&as_pdf=true")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert "attachment" in response.headers["content-disposition"]
    assert "INV-" in response.headers["content-disposition"]


async def test_get_invoice_not_found(auth_client: AsyncClient) -> None:
    """GET invoice inexistente retorna 404."""
    response = await auth_client.get(f"{INVOICES}/999999?owner_user_id={OWNER_USER_ID}")
    assert response.status_code == 404
    assert response.json()["error"]["key"] == "not_found"


async def test_get_invoice_forbidden(

    auth_client: AsyncClient, invoice_repo: InvoiceRepository, engine
) -> None:
    """GET invoice de outro owner retorna 404 (não 403 para não

    vazar existência)."""

    # Create user 2 first
    from src.backend.models.user import User, UserStatus
    from src.backend.models.database import create_session_factory
    session_factory = create_session_factory(engine)
    async with session_factory() as session:
        from sqlalchemy import select
        result = await session.execute(select(User).where(User.id == 2))
        if result.scalar_one_or_none() is None:
            user2 = User(
                id=2,
                internal_username_hash="b" * 64,
                name="Test User 2",
                email="test2@example.com",
                cpf="11111111111",
                password_hash="dummy_hash",
                status=UserStatus.ACTIVE.value,
            )
            session.add(user2)
            await session.commit()

    async def _create():
        from src.backend.services.invoice_number import InvoiceNumberService

        async with invoice_repo.session_factory() as session:
            number_service = InvoiceNumberService(session)
            invoice_number = await number_service.generate("00000000000000")

        stored = type('StoredInvoice', (), {
            'id': next(_invoice_id), 'owner_user_id': 2, 'client_id': None,

            'simulation_id': None, 'invoice_number': invoice_number,

            'status': 'finalized', 'locale': 'pt-BR', 'client_country_code': 'US',

            'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',

            'issuer_address': None, 'client_name': 'Cliente',

            'client_tax_id_digits': '11111111111111',

            'client_address': None, 'banco': None, 'agencia': None,

            'conta_com_digito': None, 'pix_key': None,

            'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),

            'description': 'Test', 'regime': 'hourly', 'currency': 'USD',

            'amount': Decimal('10'), 'quantity': Decimal('10'),

            'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),

            'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),

            'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),

            'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),

            'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',

            'quote_bulletin': None,

            'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),

            'stale': False, 'finalized_at': datetime.now(UTC),

            'supersedes_invoice_id': None,

            'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),

        })()

        await invoice_repo.save(stored)

        return stored.id

    inv_id = await _create()

    try:
        # Acessa com outro owner (isolamento): deve retornar 404, não vazar existência
        response = await auth_client.get(f"{INVOICES}/{inv_id}")

        assert response.status_code == 404
    finally:
        # Cleanup: delete the invoice to avoid FK violation in teardown
        from src.backend.models.invoice import Invoice as InvoiceModel
        from sqlalchemy import delete
        async with session_factory() as session:
            await session.execute(delete(InvoiceModel).where(InvoiceModel.id == inv_id))
            await session.commit()

# ---------- Teste: Finalize (DEC-05) ----------


# ---------- Teste: Finalize (DEC-05) ----------

async def test_finalize_invoice_draft_to_finalized(
    auth_client: AsyncClient, invoice_repo: InvoiceRepository
) -> None:
    """POST /finalize transiciona draft → finalized com finalized_at."""

    async def _create_draft():
        from datetime import datetime, UTC
        from src.backend.services.invoice_number import InvoiceNumberService

        async with invoice_repo.session_factory() as session:
            number_service = InvoiceNumberService(session)
            invoice_number = await number_service.generate("00000000000000")

        stored = type('StoredInvoice', (), {
            'id': next(_invoice_id), 'owner_user_id': OWNER_USER_ID, 'client_id': None,
            'simulation_id': None, 'invoice_number': invoice_number,
            'status': 'draft', 'locale': 'pt-BR', 'client_country_code': 'US',
            'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',
            'issuer_address': None, 'client_name': 'Cliente',
            'client_tax_id_digits': '11111111111111',
            'client_address': None, 'banco': None, 'agencia': None,
            'conta_com_digito': None, 'pix_key': None,
            'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
            'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
            'amount': Decimal('10'), 'quantity': Decimal('10'),
            'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
            'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
            'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
            'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
            'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
            'quote_bulletin': None,
            'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
            'stale': False, 'finalized_at': None,
            'supersedes_invoice_id': None,
            'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
        })()
        await invoice_repo.save(stored)
        return stored.id

    inv_id = await _create_draft()

    response = await auth_client.post(
        f"{INVOICES}/{inv_id}/finalize?owner_user_id={OWNER_USER_ID}",
        json={},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "finalized"
    assert data["finalized_at"] is not None


async def test_finalize_not_draft_returns_409(
    auth_client: AsyncClient, invoice_repo: InvoiceRepository
) -> None:
    """Finalizar invoice já finalized retorna 409."""

    async def _create_finalized():
        from datetime import datetime, UTC
        from src.backend.services.invoice_number import InvoiceNumberService

        async with invoice_repo.session_factory() as session:
            number_service = InvoiceNumberService(session)
            invoice_number = await number_service.generate("00000000000000")

        stored = type('StoredInvoice', (), {
            'id': next(_invoice_id), 'owner_user_id': OWNER_USER_ID, 'client_id': None,
            'simulation_id': None, 'invoice_number': invoice_number,
            'status': 'finalized', 'locale': 'pt-BR', 'client_country_code': 'US',
            'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',
            'issuer_address': None, 'client_name': 'Cliente',
            'client_tax_id_digits': '11111111111111',
            'client_address': None, 'banco': None, 'agencia': None,
            'conta_com_digito': None, 'pix_key': None,
            'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
            'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
            'amount': Decimal('10'), 'quantity': Decimal('10'),
            'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
            'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
            'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
            'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
            'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
            'quote_bulletin': None,
            'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
            'stale': False, 'finalized_at': datetime.now(UTC),
            'supersedes_invoice_id': None,
            'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
        })()
        await invoice_repo.save(stored)
        return stored.id

    inv_id = await _create_finalized()

    from fastapi import HTTPException
    from src.backend.routers.invoices import finalize_invoice

    with pytest.raises(HTTPException) as exc:
        await finalize_invoice(inv_id, SessionData(OWNER_USER_ID, 1), invoice_repo)
    assert exc.value.status_code == 409
    assert "não está em status draft" in exc.value.detail

# ---------- Teste: Clone (DEC-05, US-017) ----------


async def test_clone_invoice_creates_new_draft(
    auth_client: AsyncClient, invoice_repo: InvoiceRepository
) -> None:
    """POST /clone cria novo draft com novo número e supersedes_invoice_id."""

    async def _create_finalized():
        from datetime import datetime, UTC
        from src.backend.services.invoice_number import InvoiceNumberService

        async with invoice_repo.session_factory() as session:
            number_service = InvoiceNumberService(session)
            invoice_number = await number_service.generate("00000000000000")

        stored = type('StoredInvoice', (), {
            'id': next(_invoice_id), 'owner_user_id': OWNER_USER_ID, 'client_id': None,
            'simulation_id': None, 'invoice_number': invoice_number,
            'status': 'finalized', 'locale': 'pt-BR', 'client_country_code': 'US',
            'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',
            'issuer_address': 'Rua A', 'client_name': 'Cliente',
            'client_tax_id_digits': '11111111111111',
            'client_address': 'Rua B', 'banco': None, 'agencia': None,
            'conta_com_digito': None, 'pix_key': None,
            'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
            'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
            'amount': Decimal('10'), 'quantity': Decimal('10'),
            'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
            'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
            'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
            'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
            'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
            'quote_bulletin': None,
            'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
            'stale': False, 'finalized_at': datetime.now(UTC),
            'supersedes_invoice_id': None,
            'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
        })()
        await invoice_repo.save(stored)
        return stored.id, invoice_number

    original_id, original_number = await _create_finalized()

    response = await auth_client.post(
        f"{INVOICES}/{original_id}/clone?owner_user_id={OWNER_USER_ID}",
    )
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "draft"
    assert data["supersedes_invoice_id"] == original_id
    assert data["invoice_number"] != original_number
    assert data["invoice_number"].startswith("INV-")


async def test_clone_only_finalized_allowed(
    auth_client: AsyncClient, invoice_repo: InvoiceRepository
) -> None:
    """Clonar draft retorna 409 (somente invoices finalizadas podem ser clonadas)."""

    async def _create_draft():
        from datetime import datetime, UTC
        from src.backend.services.invoice_number import InvoiceNumberService

        async with invoice_repo.session_factory() as session:
            number_service = InvoiceNumberService(session)
            invoice_number = await number_service.generate("00000000000000")

        stored = type('StoredInvoice', (), {
            'id': next(_invoice_id), 'owner_user_id': OWNER_USER_ID, 'client_id': None,
            'simulation_id': None, 'invoice_number': invoice_number,
            'status': 'draft', 'locale': 'pt-BR', 'client_country_code': 'US',
            'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',
            'issuer_address': None, 'client_name': 'Cliente',
            'client_tax_id_digits': '11111111111111',
            'client_address': None, 'banco': None, 'agencia': None,
            'conta_com_digito': None, 'pix_key': None,
            'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
            'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
            'amount': Decimal('10'), 'quantity': Decimal('10'),
            'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
            'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
            'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
            'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
            'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
            'quote_bulletin': None,
            'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
            'stale': False, 'finalized_at': None,
            'supersedes_invoice_id': None,
            'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
        })()
        await invoice_repo.save(stored)
        return stored.id

    from fastapi import HTTPException
    from src.backend.routers.invoices import clone_invoice

    inv_id = await _create_draft()
    with pytest.raises(HTTPException) as exc:
        await clone_invoice(inv_id, SessionData(OWNER_USER_ID, 1), invoice_repo)
    assert exc.value.status_code == 409
    assert "Invoice não está em status finalized" in exc.value.detail

# ---------- Teste: Erase LGPD art. 18 (DEC-04) ----------


async def test_erase_invoice_hard_delete(
    db_client: TestClient, invoice_repo: InvoiceRepository
) -> None:
    """DELETE /v1/invoices/{id} remove permanentemente (LGPD art. 18)."""

    async def _create():
        from datetime import datetime, UTC
        from src.backend.services.invoice_number import InvoiceNumberService

        async with invoice_repo.session_factory() as session:
            number_service = InvoiceNumberService(session)
            invoice_number = await number_service.generate("00000000000000")

        stored = type('StoredInvoice', (), {
            'id': next(_invoice_id), 'owner_user_id': OWNER_USER_ID, 'client_id': None,
            'simulation_id': None, 'invoice_number': invoice_number,
            'status': 'draft', 'locale': 'pt-BR', 'client_country_code': 'US',
            'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',
            'issuer_address': None, 'client_name': 'Cliente',
            'client_tax_id_digits': '11111111111111',
            'client_address': None, 'banco': None, 'agencia': None,
            'conta_com_digito': None, 'pix_key': None,
            'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
            'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
            'amount': Decimal('10'), 'quantity': Decimal('10'),
            'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
            'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
            'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
            'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
            'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
            'quote_bulletin': None,
            'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
            'stale': False, 'finalized_at': None,
            'supersedes_invoice_id': None,
            'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
        })()
        await invoice_repo.save(stored)
        return stored.id

    from src.backend.routers.invoices import erase_invoice

    inv_id = await _create()

    # Deleta (somente drafts podem ser apagadas)
    response = await erase_invoice(inv_id, SessionData(OWNER_USER_ID, 1), invoice_repo)
    assert response.status_code == 204

    # Confirma que não existe mais
    assert await invoice_repo.get_by_id(inv_id, OWNER_USER_ID) is None


async def test_erase_invoice_not_found(auth_client: AsyncClient) -> None:
    """Erase invoice inexistente retorna 404."""
    response = await auth_client.delete(
        f"{INVOICES}/999999?owner_user_id={OWNER_USER_ID}"
    )
    assert response.status_code == 404


async def test_erase_invoice_forbidden(
    auth_client: AsyncClient, invoice_repo: InvoiceRepository, engine
) -> None:
    """Erase invoice de outro owner retorna 404."""

    # Create user 2 first
    from src.backend.models.user import User, UserStatus
    from src.backend.models.database import create_session_factory
    session_factory = create_session_factory(engine)
    async with session_factory() as session:
        from sqlalchemy import select
        result = await session.execute(select(User).where(User.id == 2))
        if result.scalar_one_or_none() is None:
            user2 = User(
                id=2,
                internal_username_hash="b" * 64,
                name="Test User 2",
                email="test2@example.com",
                cpf="11111111111",
                password_hash="dummy_hash",
                status=UserStatus.ACTIVE.value,
            )
            session.add(user2)
            await session.commit()

    async def _create():
        from datetime import datetime, UTC
        from src.backend.services.invoice_number import InvoiceNumberService

        async with invoice_repo.session_factory() as session:
            number_service = InvoiceNumberService(session)
            invoice_number = await number_service.generate("00000000000000")

        stored = type('StoredInvoice', (), {
            'id': next(_invoice_id), 'owner_user_id': 2, 'client_id': None,
            'simulation_id': None, 'invoice_number': invoice_number,
            'status': 'finalized', 'locale': 'pt-BR', 'client_country_code': 'US',
            'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',
            'issuer_address': None, 'client_name': 'Cliente',
            'client_tax_id_digits': '11111111111111',
            'client_address': None, 'banco': None, 'agencia': None,
            'conta_com_digito': None, 'pix_key': None,
            'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
            'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
            'amount': Decimal('10'), 'quantity': Decimal('10'),
            'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
            'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
            'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
            'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
            'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
            'quote_bulletin': None,
            'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
            'stale': False, 'finalized_at': datetime.now(UTC),
            'supersedes_invoice_id': None,
            'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
        })()
        await invoice_repo.save(stored)
        return stored.id

    inv_id = await _create()

    try:
        response = await auth_client.delete(
            f"{INVOICES}/{inv_id}?owner_user_id=2"
        )
        assert response.status_code == 404  # invoice not found for this user
    finally:
        # Cleanup: delete the invoice to avoid FK violation in teardown
        from src.backend.models.invoice import Invoice as InvoiceModel
        from sqlalchemy import delete
        async with session_factory() as session:
            await session.execute(delete(InvoiceModel).where(InvoiceModel.id == inv_id))
            await session.commit()

# ---------- Teste: Bilingual templates (DEC-07) ----------


async def test_template_pt_br_renders_brl_format(
    auth_client: AsyncClient, invoice_repo: InvoiceRepository
) -> None:
    """Template pt-BR usa formatação brasileira (R$ 1.234,56)."""

    async def _create():
        from datetime import datetime, UTC
        from src.backend.services.invoice_number import InvoiceNumberService

        async with invoice_repo.session_factory() as session:
            number_service = InvoiceNumberService(session)
            invoice_number = await number_service.generate("00000000000000")

        stored = type('StoredInvoice', (), {
            'id': next(_invoice_id), 'owner_user_id': OWNER_USER_ID, 'client_id': None,
            'simulation_id': None, 'invoice_number': invoice_number,
            'status': 'finalized', 'locale': 'pt-BR', 'client_country_code': 'BR',
            'issuer_name': 'Emitente', 'issuer_tax_id_digits': '00000000000000',
            'issuer_address': None, 'client_name': 'Cliente',
            'client_tax_id_digits': '11111111111111',
            'client_address': None, 'banco': None, 'agencia': None,
            'conta_com_digito': None, 'pix_key': None,
            'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
            'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
            'amount': Decimal('10'), 'quantity': Decimal('10'),
            'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
            'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
            'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
            'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
            'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
            'quote_bulletin': None,
            'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
            'stale': False, 'finalized_at': datetime.now(UTC),
            'supersedes_invoice_id': None,
            'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
        })()
        await invoice_repo.save(stored)
        return stored.id

    inv_id = await _create()

    response = await auth_client.get(f"{INVOICES}/{inv_id}?owner_user_id={OWNER_USER_ID}&as_pdf=true")
    assert response.status_code == 200
    # Verifica se o PDF foi gerado (conteúdo binário)
    assert response.content.startswith(b"%PDF-")


async def test_template_en_renders_en_format(
    auth_client: AsyncClient, invoice_repo: InvoiceRepository
) -> None:
    """Template en usa formatação inglesa (1,234.56 BRL)."""

    async def _create():
        from datetime import datetime, UTC
        from src.backend.services.invoice_number import InvoiceNumberService

        async with invoice_repo.session_factory() as session:
            number_service = InvoiceNumberService(session)
            invoice_number = await number_service.generate("00000000000000")

        stored = type('StoredInvoice', (), {
            'id': next(_invoice_id), 'owner_user_id': OWNER_USER_ID, 'client_id': None,
            'simulation_id': None, 'invoice_number': invoice_number,
            'status': 'finalized', 'locale': 'en', 'client_country_code': 'US',
            'issuer_name': 'Issuer', 'issuer_tax_id_digits': '00000000000000',
            'issuer_address': None, 'client_name': 'Client',
            'client_tax_id_digits': '11111111111111',
            'client_address': None, 'banco': None, 'agencia': None,
            'conta_com_digito': None, 'pix_key': None,
            'periodo_inicio': date(2026, 1, 1), 'periodo_fim': date(2026, 1, 31),
            'description': 'Test', 'regime': 'hourly', 'currency': 'USD',
            'amount': Decimal('10'), 'quantity': Decimal('10'),
            'spread_pct': Decimal('1'), 'iof_pct': Decimal('0.38'),
            'gross_foreign': Decimal('100'), 'gross_brl': Decimal('500'),
            'spread_brl': Decimal('5'), 'iof_brl': Decimal('1.89'),
            'net_brl': Decimal('493.11'), 'effective_rate': Decimal('4.9311'),
            'quote_rate': Decimal('5.000000'), 'quote_source': 'frankfurter',
            'quote_bulletin': None,
            'quoted_at': datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC),
            'stale': False, 'finalized_at': datetime.now(UTC),
            'supersedes_invoice_id': None,
            'created_at': datetime.now(UTC), 'updated_at': datetime.now(UTC),
        })()
        await invoice_repo.save(stored)
        return stored.id

    inv_id = await _create()

    response = await auth_client.get(f"{INVOICES}/{inv_id}?owner_user_id={OWNER_USER_ID}&as_pdf=true")
    assert response.status_code == 200
    assert response.content.startswith(b"%PDF-")

# ---------- Teste: Numeração sequencial (DEC-06) ----------


async def test_next_invoice_number_sequential_per_issuer_month(
    invoice_repo: InvoiceRepository,
) -> None:
    """next_invoice_number gera sequencial por emissor/mês (sem gaps visíveis)."""
    import uuid
    # Use unique issuer to avoid sequence conflicts across test runs
    unique_issuer = f"99{uuid.uuid4().hex[:12]}"
    numbers = []
    for _ in range(5):
        num = await invoice_repo.get_next_number(unique_issuer)
        numbers.append(num)

    # Todos começam com INV-202611-
    assert all(n.startswith("INV-") for n in numbers)
    # Sequenciais
    suffixes = [int(n.split("-")[-1]) for n in numbers]
    assert suffixes == list(range(1, 6))


async def test_next_invoice_number_different_issuers_independent(
    invoice_repo: InvoiceRepository,
) -> None:
    """Emissores diferentes têm sequências independentes."""
    import uuid
    issuer1 = f"11{uuid.uuid4().hex[:12]}"
    issuer2 = f"22{uuid.uuid4().hex[:12]}"

    num1_a = await invoice_repo.get_next_number(issuer1)
    num1_b = await invoice_repo.get_next_number(issuer1)
    num2_a = await invoice_repo.get_next_number(issuer2)

    assert num1_a.endswith("-0001")
    assert num1_b.endswith("-0002")
    assert num2_a.endswith("-0001")  # independente
