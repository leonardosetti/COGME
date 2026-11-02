"""Rota de simulação (spec backend-mvp-v1, §3; REQ-02, REQ-03)."""

from __future__ import annotations

from fastapi import APIRouter

from src.backend.routers.common import (
    INTERNAL_ERROR_RESPONSE,
    RATES_UNAVAILABLE_RESPONSE,
    VALIDATION_ERROR_RESPONSE,
    DecimalJsonRoute,
    RateServiceDep,
)
from src.backend.services.simulation_service import simulate
from src.shared.schemas import SimulationRequest, SimulationResponse

router = APIRouter(prefix="/v1", tags=["simulações"], route_class=DecimalJsonRoute)


@router.post(
    "/simulate",
    response_model=SimulationResponse,
    summary="Simula o recebimento em BRL",
    responses={
        **VALIDATION_ERROR_RESPONSE,
        **INTERNAL_ERROR_RESPONSE,
        **RATES_UNAVAILABLE_RESPONSE,
    },
)
async def post_simulation(
    payload: SimulationRequest,
    rate_service: RateServiceDep,
) -> SimulationResponse:
    """Calcula o detalhamento da simulação com a cotação vigente.

    Args:
        payload: Entrada validada pelo contrato.
        rate_service: Serviço de cotações.

    Returns:
        O detalhamento, a cotação usada e o aviso constante.
    """
    return await simulate(payload, rate_service)
