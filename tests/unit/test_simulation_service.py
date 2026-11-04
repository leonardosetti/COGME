"""Testes unitários de services/simulation_service.py (spec backend-mvp-v1, §2, §3; REQ-02, REQ-03).

``simulate`` combina a cotação do RateService com o cálculo puro. Aqui o RateService é
um dublê que devolve cotação configurada, sem rede. Os números esperados saem da §2.
"""

from __future__ import annotations

from typing import Any

from src.backend.services.simulation_service import simulate
from src.shared.schemas import (
    NOTICE,
    Currency,
    RateQuote,
    SimulationRequest,
    SimulationResponse,
)

NOTICE_TEXT = (
    "Simulação de caráter informativo; spread e IOF foram informados pelo usuário "
    "e não substituem a orientação de um profissional habilitado."
)


class FakeRateService:
    """Dublê do RateService: devolve a cotação configurada e registra as moedas pedidas.

    Attributes:
        calls: Moedas pedidas, na ordem das chamadas.
    """

    def __init__(self, quote: RateQuote) -> None:
        self._quote = quote
        self.calls: list[Currency] = []

    async def get_quote(self, currency: Currency) -> RateQuote:
        """Registra a moeda pedida e devolve a cotação configurada.

        Args:
            currency: Moeda pedida.

        Returns:
            A cotação configurada.
        """
        self.calls.append(currency)
        return self._quote


def _quote(make_rate_quote: Any, *, stale: bool = False) -> RateQuote:
    """Cotação sintética de 5,000000 BRL por USD.

    Args:
        make_rate_quote: Fábrica de RateQuote da conftest.
        stale: Marca a cotação como vinda de cache vencido.

    Returns:
        RateQuote pronta para o dublê.
    """
    return make_rate_quote(rate="5.000000", source="frankfurter", stale=stale)


async def test_simulate_builds_response_from_section2_example(make_rate_quote: Any) -> None:
    """Exemplo da §2 pela camada de serviço: valores exatos, cotação e aviso corretos."""
    quote = _quote(make_rate_quote)
    rate_service = FakeRateService(quote)
    request = SimulationRequest.model_validate(
        {
            "currency": "USD",
            "regime": "hourly",
            "amount": "30.00",
            "quantity": "160",
            "spread_pct": "2",
            "iof_pct": "0.38",
        }
    )

    response = await simulate(request, rate_service)

    assert isinstance(response, SimulationResponse)
    assert rate_service.calls == [Currency.USD]
    assert str(response.gross_foreign) == "4800.00"
    assert str(response.gross_brl) == "24000.00"
    assert str(response.spread_brl) == "480.00"
    assert str(response.iof_brl) == "89.38"
    assert str(response.net_brl) == "23430.62"
    assert str(response.effective_rate) == "4.881379"
    assert response.spread_pct == request.spread_pct
    assert response.iof_pct == request.iof_pct
    assert response.quote == quote


async def test_response_carries_the_constant_notice(make_rate_quote: Any) -> None:
    """O aviso é o texto constante da §3, idêntico ao NOTICE do schema."""
    request = SimulationRequest.model_validate(
        {
            "currency": "USD",
            "regime": "hourly",
            "amount": "30",
            "quantity": "160",
            "spread_pct": "2",
            "iof_pct": "0.38",
        }
    )

    response = await simulate(request, FakeRateService(_quote(make_rate_quote)))

    assert response.notice == NOTICE_TEXT
    assert response.notice == NOTICE


async def test_stale_quote_propagates_to_response(make_rate_quote: Any) -> None:
    """Cotação de cache vencido chega à resposta com stale=true (§4)."""
    request = SimulationRequest.model_validate(
        {
            "currency": "USD",
            "regime": "hourly",
            "amount": "30",
            "quantity": "160",
            "spread_pct": "2",
            "iof_pct": "0.38",
        }
    )

    response = await simulate(request, FakeRateService(_quote(make_rate_quote, stale=True)))

    assert response.quote.stale is True


async def test_fixed_regime_uses_amount_as_gross_section2(make_rate_quote: Any) -> None:
    """Regime fixed: bruto é o amount; IOF 18,715 sobre 4925 arredonda para 18,72 (HALF_EVEN).

    Conferido à mão: 1000 × 5 = 5000; spread 1,5 % = 75,00; (5000 − 75) × 0,38 % = 18,715.
    """
    request = SimulationRequest.model_validate(
        {
            "currency": "EUR",
            "regime": "fixed",
            "amount": "1000.00",
            "spread_pct": "1.5",
            "iof_pct": "0.38",
        }
    )

    response = await simulate(request, FakeRateService(_quote(make_rate_quote)))

    assert str(response.gross_foreign) == "1000.00"
    assert str(response.gross_brl) == "5000.00"
    assert str(response.spread_brl) == "75.00"
    assert str(response.iof_brl) == "18.72"
    assert str(response.net_brl) == "4906.28"
    assert str(response.effective_rate) == "4.906280"


async def test_response_serialises_money_as_plain_strings(make_rate_quote: Any) -> None:
    """A resposta sai com decimais como texto simples no JSON (§3)."""
    request = SimulationRequest.model_validate(
        {
            "currency": "USD",
            "regime": "hourly",
            "amount": "30",
            "quantity": "160",
            "spread_pct": "2",
            "iof_pct": "0.38",
        }
    )
    response = await simulate(request, FakeRateService(_quote(make_rate_quote)))

    dumped = response.model_dump(mode="json")

    assert dumped["gross_brl"] == "24000.00"
    assert dumped["effective_rate"] == "4.881379"
    assert dumped["quote"]["rate"] == "5.000000"
