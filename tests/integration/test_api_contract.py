"""Contrato HTTP de /v1: respostas de sucesso e erros de domínio (spec backend-mvp-v1, §2, §3).

Os valores esperados saem das fórmulas da §2 e foram conferidos à mão; nenhum foi copiado da
saída do código. Decimais são strings exatas. Validação e erros de corpo estão em
``test_api_validation.py``.
"""

from __future__ import annotations

import logging
from typing import Any

import pytest
from fastapi.testclient import TestClient

from src.backend.main import app
from src.backend.services.rate_service import RateService
from src.shared.schemas import NOTICE, RateSource

from .fakes import (
    SIMULATE,
    SPEC_EXAMPLE_BODY,
    FixedClock,
    FixedMonotonic,
    ScriptedProvider,
    build_service,
    error_of,
    failing_provider,
)

SPEC_NOTICE = (
    "Simulação de caráter informativo; spread e IOF foram informados pelo usuário "
    "e não substituem a orientação de um profissional habilitado."
)
UNAVAILABLE_MESSAGE = "Cotação indisponível no momento. Tente novamente mais tarde."
INTERNAL_MESSAGE = "Erro interno. Tente novamente mais tarde."
SECRET_TEXT = "segredo sintético que não pode vazar"

SPEC_QUOTE: dict[str, Any] = {
    "currency": "USD",
    "rate": "5.000000",
    "source": "frankfurter",
    "quoted_at": "2026-10-30T00:00:00Z",
    "bulletin": None,
    "stale": False,
}


def test_health_answers_ok(client: TestClient) -> None:
    """GET /v1/health responde 200 com status ok, sem tocar em cotação (§3)."""
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_rates_returns_exact_quote_fields_req01(client: TestClient) -> None:
    """REQ-01: GET /v1/rates/USD devolve a cotação com decimal como string exata (§3)."""
    response = client.get("/v1/rates/USD")
    assert response.status_code == 200
    assert response.json() == SPEC_QUOTE
    assert isinstance(response.json()["rate"], str)


def test_simulate_spec_section2_example_gives_exact_strings_req02(client: TestClient) -> None:
    """REQ-02: exemplo da §2 com cotação 5,000000 produz exatamente os valores da especificação."""
    response = client.post(SIMULATE, json=SPEC_EXAMPLE_BODY)
    assert response.status_code == 200
    assert response.json() == {
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
        "quote": SPEC_QUOTE,
        "notice": SPEC_NOTICE,
    }
    assert NOTICE == SPEC_NOTICE


# Cotação 5,000000, spread 2 %, IOF 0,38 %, em todos os regimes. Valores conferidos à mão:
# daily: 2500,00 − 50,00 − 9,31 = 2440,69; 2440,69 / 500 = 4,88138.
# weekly: 5000,00 − 100,00 − 18,62 = 4881,38; 4881,38 / 1000 = 4,88138.
# monthly: 60000,00 − 1200,00 − 223,44 = 58576,56; 58576,56 / 12000 = 4,88138.
# fixed: 5000,00 − 100,00 − 18,62 = 4881,38; 4881,38 / 1000 = 4,88138.
@pytest.mark.parametrize(
    ("body", "expected"),
    [
        (
            {"regime": "hourly", "amount": "30", "quantity": "160"},
            ("4800.00", "24000.00", "480.00", "89.38", "23430.62", "4.881379"),
        ),
        (
            {"regime": "daily", "amount": "100", "quantity": "5"},
            ("500.00", "2500.00", "50.00", "9.31", "2440.69", "4.881380"),
        ),
        (
            {"regime": "weekly", "amount": "250", "quantity": "4"},
            ("1000.00", "5000.00", "100.00", "18.62", "4881.38", "4.881380"),
        ),
        (
            {"regime": "monthly", "amount": "1000", "quantity": "12"},
            ("12000.00", "60000.00", "1200.00", "223.44", "58576.56", "4.881380"),
        ),
        (
            {"regime": "fixed", "amount": "1000"},
            ("1000.00", "5000.00", "100.00", "18.62", "4881.38", "4.881380"),
        ),
    ],
    ids=["hourly", "daily", "weekly", "monthly", "fixed"],
)
def test_simulate_each_of_the_five_regimes_req02(
    client: TestClient,
    body: dict[str, str],
    expected: tuple[str, str, str, str, str, str],
) -> None:
    """REQ-02/REQ-03: os cinco regimes geram o bruto, o spread, o IOF e o líquido da §2."""
    payload = {"currency": "USD", "spread_pct": "2", "iof_pct": "0.38", **body}
    response = client.post(SIMULATE, json=payload)
    assert response.status_code == 200
    data = response.json()
    gross_foreign, gross_brl, spread_brl, iof_brl, net_brl, effective = expected
    assert data["gross_foreign"] == gross_foreign
    assert data["gross_brl"] == gross_brl
    assert data["spread_brl"] == spread_brl
    assert data["iof_brl"] == iof_brl
    assert data["net_brl"] == net_brl
    assert data["effective_rate"] == effective
    for name in ("gross_foreign", "gross_brl", "spread_brl", "iof_brl", "net_brl"):
        assert isinstance(data[name], str), name


def test_fixed_regime_without_quantity_is_accepted_req02(client: TestClient) -> None:
    """REQ-02: o regime fixed dispensa quantidade e converte o valor unitário (§2)."""
    response = client.post(
        SIMULATE,
        json={"currency": "EUR", "regime": "fixed", "amount": "1000", "spread_pct": "1.5",
              "iof_pct": "0.38"},
    )
    assert response.status_code == 200
    assert response.json()["currency"] == "EUR"
    assert response.json()["gross_brl"] == "5000.00"


def test_unknown_route_is_404_not_found(client: TestClient) -> None:
    """Rota inexistente responde 404 no modelo canônico, sem eco do caminho (§3)."""
    response = client.get("/v1/rota-que-nao-existe")
    error_of(response, 404, "not_found", "Recurso não encontrado.")
    assert "rota-que-nao-existe" not in response.text


def test_wrong_method_is_405_with_allow_header(client: TestClient) -> None:
    """Método errado responde 405 com cabeçalho Allow e chave not_found, não validation_error."""
    response = client.get(SIMULATE)
    error_of(response, 405, "not_found", "Método não permitido para este recurso.")
    assert response.headers["allow"] == "POST"


def test_rates_unavailable_without_cache_is_503_req01(
    serve_rates: Any, clock: FixedClock, monotonic_clock: FixedMonotonic,
) -> None:
    """REQ-01: sem fonte e sem cache, /v1/rates responde 503 rates_unavailable (§3)."""
    serve_rates(
        build_service(
            providers=[
                failing_provider(RateSource.FRANKFURTER),
                failing_provider(RateSource.PTAX),
            ],
            clock=clock,
            monotonic=monotonic_clock,
        ),
    )
    response = TestClient(app).get("/v1/rates/USD")
    error = error_of(response, 503, "rates_unavailable", UNAVAILABLE_MESSAGE)
    assert error["details"] == []


def test_simulate_rates_unavailable_is_503_req01(
    serve_rates: Any, clock: FixedClock, monotonic_clock: FixedMonotonic,
) -> None:
    """REQ-01: a simulação também responde 503 quando não há cotação, sem gravar nada."""
    serve_rates(
        build_service(
            providers=[
                failing_provider(RateSource.FRANKFURTER),
                failing_provider(RateSource.PTAX),
            ],
            clock=clock,
            monotonic=monotonic_clock,
        ),
    )
    response = TestClient(app).post(SIMULATE, json=SPEC_EXAMPLE_BODY)
    error_of(response, 503, "rates_unavailable", UNAVAILABLE_MESSAGE)


class _ExplodingRateService:
    """Serviço que falha com uma mensagem sensível, para provar que ela não sai na resposta."""

    async def get_quote(self, currency: Any) -> Any:
        """Levanta erro inesperado com texto que não pode vazar."""
        del currency
        raise RuntimeError(SECRET_TEXT)


def test_unexpected_error_is_500_internal_error_without_leaks(
    serve_rates: Any, caplog: pytest.LogCaptureFixture,
) -> None:
    """500 internal_error: sem traceback, sem a mensagem da exceção; o log guarda só o tipo."""
    serve_rates(_ExplodingRateService())  # type: ignore[arg-type]
    with caplog.at_level(logging.ERROR):
        response = TestClient(app).get("/v1/rates/USD")

    assert response.status_code == 500
    assert response.json() == {
        "error": {"key": "internal_error", "message": INTERNAL_MESSAGE, "details": []},
    }
    assert SECRET_TEXT not in response.text
    assert "Traceback" not in response.text
    assert "unhandled_exception type=RuntimeError" in caplog.text
    assert SECRET_TEXT not in caplog.text


def test_second_request_within_ttl_uses_cache_req07(
    serve_rates: Any, clock: FixedClock, monotonic_clock: FixedMonotonic,
) -> None:
    """REQ-07: a segunda chamada dentro do TTL é servida pelo cache, sem nova chamada de fonte."""
    frankfurter = ScriptedProvider(RateSource.FRANKFURTER, rate="5.000000")
    service: RateService = build_service(
        providers=[frankfurter], clock=clock, monotonic=monotonic_clock,
    )
    serve_rates(service)
    client = TestClient(app)

    first = client.get("/v1/rates/USD")
    second = client.get("/v1/rates/USD")

    assert first.json() == second.json() == SPEC_QUOTE
    assert frankfurter.calls == 1
