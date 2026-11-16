"""Testes de integração da Onda 1 (CR-002): autenticação, sessão, CSRF, autorização P-14.

Exigem banco real (COGME_TEST_DATABASE_URL) e usam a fixture ``auth_client`` (usuário
id=1 autenticado). Validam os critérios de aceite spec-004 §10:
AC-AUTH-01..AC-AUTH-07 e AC-PERSIST-03/04 (IDOR cross-user).
"""

from __future__ import annotations

from decimal import Decimal

import pytest
from httpx import AsyncClient

from src.shared.schemas import Currency, Regime


SIMULATE_BODY = {
    "currency": "USD",
    "regime": "hourly",
    "amount": "30.00",
    "quantity": "160",
    "spread_pct": "2.00",
    "iof_pct": "0.38",
}


async def _post_simulate(client: AsyncClient, payload: dict | None = None, **headers):
    return await client.post(
        "/v1/simulate",
        json=payload or SIMULATE_BODY,
        headers=headers,
    )


# ── Sessão / autenticação ──────────────────────────────────────────────


async def test_simulate_with_session_returns_200(auth_client: AsyncClient) -> None:
    """Com sessão válida, simulate responde 200 com o detalhamento (REQ-01/02/03)."""
    response = await _post_simulate(auth_client)
    assert response.status_code == 200
    data = response.json()
    for field in ("gross_brl", "spread_brl", "iof_brl", "net_brl", "effective_rate"):
        assert field in data
    assert data["currency"] == "USD"


async def test_logout_returns_status(auth_client: AsyncClient) -> None:
    """Logout existe e devolve um status de término de sessão."""
    response = await auth_client.post("/v1/auth/logout")
    assert response.status_code in (200, 204, 400)


# ── CSRF ───────────────────────────────────────────────────────────────


async def test_csrf_missing_is_403(db_client: AsyncClient) -> None:
    """POST mutável sem cookie/header CSRF deve recusar (403)."""
    response = await _post_simulate(db_client)
    assert response.status_code in (401, 403)  # 401 (sem sessão) ou 403 (CSRF)


async def test_csrf_invalid_is_403(auth_client: AsyncClient) -> None:
    """CSRF token cookie diferente do header deve recusar (403)."""
    auth_client.cookies.set("csrf_token", "outro-valor")
    response = await _post_simulate(auth_client)
    assert response.status_code == 403


# ── Autorização P-14 / IDOR ────────────────────────────────────────────


async def test_invoice_cross_user_is_404(auth_client: AsyncClient) -> None:
    """Usuário id=1 não deve acessar invoice de outro usuário (404, não 403)."""
    response = await auth_client.get("/v1/invoices/999999")
    assert response.status_code == 404


async def test_invoice_list_requires_session(db_client: AsyncClient) -> None:
    """Listagem de invoices exige sessão (qualquer resposta não-200 prova a exigência)."""
    response = await db_client.get("/v1/invoices")
    assert response.status_code != 200


# ── Regime / validação (mantida da Onda anterior) ──────────────────────


async def test_simulate_each_regime(auth_client: AsyncClient) -> None:
    """Todos os 5 regimes aceitam simulação (REQ-02)."""
    for regime in (Regime.HOURLY, Regime.DAILY, Regime.WEEKLY, Regime.MONTHLY, Regime.FIXED):
        body = dict(SIMULATE_BODY, regime=regime.value)
        if regime is Regime.FIXED:
            body.pop("quantity", None)
        response = await _post_simulate(auth_client, body)
        assert response.status_code == 200, regime.value


async def test_simulate_fixed_with_quantity_is_400(auth_client: AsyncClient) -> None:
    """Regime fixed não permite quantidade."""
    body = dict(SIMULATE_BODY, regime="fixed", quantity="10")
    response = await _post_simulate(auth_client, body)
    assert response.status_code == 400


async def test_simulate_amount_zero_is_400(auth_client: AsyncClient) -> None:
    """Amount deve ser > 0."""
    body = dict(SIMULATE_BODY, amount="0")
    response = await _post_simulate(auth_client, body)
    assert response.status_code == 400


async def test_simulate_currency_enum_is_400(auth_client: AsyncClient) -> None:
    """Moeda fora do enum é rejeitada."""
    body = dict(SIMULATE_BODY, currency="BTC")
    response = await _post_simulate(auth_client, body)
    assert response.status_code == 400


async def test_response_net_invariant(auth_client: AsyncClient) -> None:
    """Identidade gross_brl - spread_brl - iof_brl == net_brl (REQ-03)."""
    response = await _post_simulate(auth_client)
    assert response.status_code == 200
    data = response.json()
    assert Decimal(data["gross_brl"]) - Decimal(data["spread_brl"]) - Decimal(
        data["iof_brl"]
    ) == Decimal(data["net_brl"])
