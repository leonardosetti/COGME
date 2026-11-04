"""Simulação de recebimento: cotação mais cálculo (spec backend-mvp-v1, §2, §3; REQ-02, REQ-03)."""

from __future__ import annotations

from src.backend.services.calculator import calculate
from src.backend.services.rate_service import RateService
from src.shared.schemas import SimulationRequest, SimulationResponse


async def simulate(request: SimulationRequest, rate_service: RateService) -> SimulationResponse:
    """Calcula o detalhamento da simulação com a cotação vigente.

    Args:
        request: Entrada validada pelo contrato.
        rate_service: Fonte da cotação.

    Returns:
        O detalhamento, a cotação usada e o aviso constante.

    Raises:
        RatesUnavailableError: Sem fonte disponível e sem cache.
    """
    quote = await rate_service.get_quote(request.currency)
    breakdown = calculate(
        regime=request.regime,
        amount=request.amount,
        quantity=request.quantity,
        rate=quote.rate,
        spread_pct=request.spread_pct,
        iof_pct=request.iof_pct,
    )
    return SimulationResponse(
        currency=request.currency,
        regime=request.regime,
        gross_foreign=breakdown.gross_foreign,
        gross_brl=breakdown.gross_brl,
        spread_brl=breakdown.spread_brl,
        iof_brl=breakdown.iof_brl,
        net_brl=breakdown.net_brl,
        effective_rate=breakdown.effective_rate,
        spread_pct=request.spread_pct,
        iof_pct=request.iof_pct,
        quote=quote,
    )
