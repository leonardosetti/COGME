"""Testes de unidade para handlers de simulações (simulations.py) chamando funções diretamente."""
from __future__ import annotations

from types import SimpleNamespace

import pytest
from fastapi import HTTPException
from starlette.requests import Request

from src.backend.middleware.session import SessionData
from src.backend.routers.simulations import _require_session, _to_saved_response


@pytest.fixture
def fake_request() -> Request:
    scope = {
        "type": "http",
        "method": "POST",
        "path": "/v1/simulate",
        "headers": [],
        "query_string": b"",
        "client": ("testclient", 50000),
        "server": ("testserver", 80),
        "app": SimpleNamespace(state=SimpleNamespace()),
    }
    return Request(scope)


@pytest.fixture
def session_data() -> SessionData:
    return SessionData(user_id=1, session_id=1)


@pytest.mark.asyncio
async def test_require_session_sem_sessao(fake_request) -> None:
    from src.backend.routers.simulations import _require_session as rs_fn
    with pytest.raises(HTTPException) as exc:
        await rs_fn(None)
    assert exc.value.status_code == 401


@pytest.mark.asyncio
async def test_to_saved_response() -> None:
    from src.backend.models.simulation import Simulation
    from datetime import UTC, datetime
    from decimal import Decimal

    row = Simulation(
        id=1,
        owner_user_id=1,
        name="Simulação Teste",
        currency="USD",
        regime="hourly",
        amount=Decimal("100.00"),
        quantity=Decimal("1.0"),
        spread_pct=Decimal("2.00"),
        iof_pct=Decimal("0.38"),
        gross_foreign=Decimal("100.00"),
        gross_brl=Decimal("500.00"),
        spread_brl=Decimal("10.00"),
        iof_brl=Decimal("1.86"),
        net_brl=Decimal("488.14"),
        effective_rate=Decimal("4.881400"),
        quote_rate=Decimal("5.000000"),
        quote_source="frankfurter",
        quote_bulletin=None,
        quoted_at=datetime(2026, 1, 1, tzinfo=UTC),
        stale=False,
    )
    resp = _to_saved_response(row)
    assert resp is not None
    assert resp.id == 1
    assert resp.name == "Simulação Teste"
    assert resp.currency == "USD"
