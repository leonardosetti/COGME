"""Testes de unidade dos helpers puros dos routers (sem banco).

Cobrem ``_require_session`` (provider, clients, account) e ``_to_response``
(clients). São funções puras: não acessam banco nem rede.
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest
from fastapi import HTTPException
from starlette import status

from src.backend.routers.account import _require_session as account_require_session
from src.backend.routers.clients import (
    ClientResponse,
    _require_session as clients_require_session,
    _to_response,
)
from src.backend.routers.provider import (
    _require_session as provider_require_session,
)


# ---------- _require_session ----------


def _fake_session() -> SimpleNamespace:
    return SimpleNamespace(user_id="usr-1", session_id="sess-1")


@pytest.mark.parametrize(
    "fn",
    [provider_require_session, clients_require_session, account_require_session],
)
def test_require_session_sem_sessao_leva_401(fn) -> None:
    with pytest.raises(HTTPException) as exc:
        fn(None)
    assert exc.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert "autenticado" in exc.value.detail
    assert exc.value.headers.get("WWW-Authenticate") == "Cookie"


@pytest.mark.parametrize(
    "fn",
    [provider_require_session, clients_require_session, account_require_session],
)
def test_require_session_com_sessao_retorna_a_sessao(fn) -> None:
    sessao = _fake_session()
    assert fn(sessao) is sessao


# ---------- _to_response ----------


def test_to_response_converte_row_em_client_response() -> None:
    row = SimpleNamespace(
        id=7,
        name="Cliente Exemplo",
        tax_id_digits="12345678901",
        tax_id_type="cpf",
        email="cliente@exemplo.com",
        phone="+5511999999999",
        address="Rua X, 1",
        country_code="BR",
        status="active",
    )
    resp = _to_response(row)
    assert isinstance(resp, ClientResponse)
    assert resp.id == 7
    assert resp.name == "Cliente Exemplo"
    assert resp.tax_id == "12345678901"
    assert resp.tax_id_type == "cpf"
    assert resp.email == "cliente@exemplo.com"
    assert resp.phone == "+5511999999999"
    assert resp.address == "Rua X, 1"
    assert resp.country_code == "BR"
    assert resp.status == "active"
