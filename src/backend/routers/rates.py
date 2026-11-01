"""Rota de cotações (spec backend-mvp-v1, §3; REQ-01)."""

from __future__ import annotations

from fastapi import APIRouter

from src.backend.routers.common import (
    INTERNAL_ERROR_RESPONSE,
    RATES_UNAVAILABLE_RESPONSE,
    VALIDATION_ERROR_RESPONSE,
    RateServiceDep,
)
from src.shared.schemas import Currency, RateQuote

router = APIRouter(prefix="/v1", tags=["cotações"])


@router.get(
    "/rates/{currency}",
    response_model=RateQuote,
    summary="Cotação vigente da moeda em BRL",
    responses={
        **VALIDATION_ERROR_RESPONSE,
        **INTERNAL_ERROR_RESPONSE,
        **RATES_UNAVAILABLE_RESPONSE,
    },
)
async def get_rate(currency: Currency, rate_service: RateServiceDep) -> RateQuote:
    """Devolve a cotação da moeda.

    Args:
        currency: Moeda estrangeira (``USD`` ou ``EUR``).
        rate_service: Serviço de cotações.

    Returns:
        A cotação; ``stale`` é verdadeiro quando vem de cache vencido.
    """
    return await rate_service.get_quote(currency)
