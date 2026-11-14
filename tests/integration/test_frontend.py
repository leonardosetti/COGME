"""Testes de renderização do serviço front da simulação."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx
import pytest
from fastapi.testclient import TestClient

import src.frontend.app as frontend_app


@dataclass
class FakeResponse:
    """Resposta mínima da API usada pelo proxy interno do front."""

    status_code: int
    payload: dict[str, Any]

    def json(self) -> dict[str, Any]:
        """Devolve o corpo JSON simulado."""
        return self.payload


class FakeBackClient:
    """Cliente assíncrono que registra o payload enviado ao back."""

    def __init__(self, response: FakeResponse) -> None:
        self.response = response
        self.calls: list[tuple[str, dict[str, Any]]] = []
        self.error: httpx.RequestError | None = None

    async def post(self, url: str, *, json: dict[str, Any]) -> FakeResponse:
        """Registra a chamada e devolve a resposta configurada."""
        self.calls.append((url, json))
        if self.error is not None:
            raise self.error
        return self.response


@pytest.fixture
def front_client(
    monkeypatch: pytest.MonkeyPatch,
) -> tuple[TestClient, FakeBackClient]:
    """Conecta o front a uma resposta simulada do back."""
    response = FakeResponse(
        status_code=200,
        payload={
            "currency": "USD",
            "regime": "hourly",
            "gross_foreign": "4800.00",
            "gross_brl": "24000.00",
            "spread_brl": "480.00",
            "iof_brl": "89.38",
            "net_brl": "23430.62",
            "effective_rate": "4.881379",
            "spread_pct": "2.0000",
            "iof_pct": "0.3800",
            "quote": {
                "currency": "USD",
                "rate": "5.000000",
                "source": "frankfurter",
                "quoted_at": "2026-01-01T00:00:00Z",
                "bulletin": None,
                "stale": False,
            },
            "notice": "Aviso canônico.",
        },
    )
    back = FakeBackClient(response)
    monkeypatch.setattr(frontend_app, "_client", back)
    return TestClient(frontend_app.app), back


def test_index_does_not_load_legacy_invoice_script(
    front_client: tuple[TestClient, FakeBackClient],
) -> None:
    """A tela de simulação não executa o JavaScript exclusivo de invoice."""
    client, _ = front_client

    response = client.get("/")

    assert response.status_code == 200
    assert "/static/js/app.js" not in response.text
    assert "fetch('/v1/simulate'" in response.text


def test_server_side_simulation_renders_result(
    front_client: tuple[TestClient, FakeBackClient],
) -> None:
    """O fallback sem JavaScript mostra o resultado enviado pelo back."""
    client, _ = front_client

    response = client.post(
        "/simulate",
        data={
            "currency": "USD",
            "regime": "hourly",
            "amount": "30",
            "quantity": "160",
            "spread_pct": "2",
            "iof_pct": "0.38",
        },
    )

    assert response.status_code == 200
    assert "card result-card visible" in response.text
    assert "4.800,00 USD" in response.text
    assert "R$ 23.430,62" in response.text
    assert "5,000000 BRL/USD" in response.text
    assert "01/01/2026, 00:00:00 UTC" in response.text


def test_server_side_fixed_regime_drops_quantity(
    front_client: tuple[TestClient, FakeBackClient],
) -> None:
    """O regime fixed não envia quantidade ao contrato que a proíbe."""
    client, back = front_client

    response = client.post(
        "/simulate",
        data={
            "currency": "USD",
            "regime": "fixed",
            "amount": "30",
            "quantity": "160",
            "spread_pct": "2",
            "iof_pct": "0.38",
        },
    )

    assert response.status_code == 200
    assert back.calls[-1][1]["quantity"] is None


def test_server_side_simulation_renders_error(
    front_client: tuple[TestClient, FakeBackClient],
) -> None:
    """O fallback sem JavaScript mostra uma falha global da API."""
    client, back = front_client
    back.response.status_code = 503
    back.response.payload = {
        "error": {
            "key": "rates_unavailable",
            "message": "Cotação indisponível.",
            "details": [],
        }
    }

    response = client.post(
        "/simulate",
        data={
            "currency": "USD",
            "regime": "hourly",
            "amount": "30",
            "quantity": "160",
            "spread_pct": "2",
            "iof_pct": "0.38",
        },
    )

    assert response.status_code == 503
    assert "Não foi possível simular" in response.text
    assert "<p>Cotação indisponível.</p>" in response.text


def test_server_side_validation_details_and_values_are_preserved(
    front_client: tuple[TestClient, FakeBackClient],
) -> None:
    """O fallback mostra detalhes canônicos e mantém os dados digitados."""
    client, back = front_client
    back.response.status_code = 400
    back.response.payload = {
        "error": {
            "key": "validation_error",
            "message": "Dados inválidos.",
            "details": [
                {"field": "amount", "message": "O valor deve ser maior que 0."}
            ],
        }
    }

    response = client.post(
        "/simulate",
        data={
            "currency": "EUR",
            "regime": "fixed",
            "amount": "0",
            "quantity": "160",
            "spread_pct": "3",
            "iof_pct": "1",
        },
    )

    assert response.status_code == 400
    assert 'href="#amount"' in response.text
    assert "O valor deve ser maior que 0." in response.text
    assert '<option value="EUR" selected>' in response.text
    assert '<option value="fixed" selected>' in response.text
    assert 'class="field hidden" id="qty-wrap"' in response.text
    assert 'id="amount" name="amount" class="input" step="0.01" min="0.01"' in response.text
    assert 'value="0" required' in response.text
    assert 'value="3" required' in response.text
    assert 'value="1" required' in response.text


def test_server_side_connection_error_keeps_values(
    front_client: tuple[TestClient, FakeBackClient],
) -> None:
    """Uma conexão recusada vira erro 503 sem perder o formulário."""
    client, back = front_client
    back.error = httpx.ConnectError("backend indisponível")

    response = client.post(
        "/simulate",
        data={
            "currency": "USD",
            "regime": "hourly",
            "amount": "42",
            "quantity": "160",
            "spread_pct": "2",
            "iof_pct": "0.38",
        },
    )

    assert response.status_code == 503
    assert "Não foi possível conectar ao serviço de simulação" in response.text
    assert 'value="42" required' in response.text


def test_decimal_format_preserves_large_values() -> None:
    """A formatação pt-BR não converte centavos para float."""
    assert (
        frontend_app._br_number("10000000000000000.01", 2)
        == "10.000.000.000.000.000,01"
    )
