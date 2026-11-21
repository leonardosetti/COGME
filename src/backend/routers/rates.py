"""Rota de cotações (spec backend-mvp-v1, §3; REQ-01)."""

from __future__ import annotations

import logging

from fastapi import APIRouter, HTTPException, Request

from src.backend.errors import RatesUnavailableError
from src.backend.middleware.rate_limit import limiter
from src.backend.routers.common import (
    INTERNAL_ERROR_RESPONSE,
    RATES_UNAVAILABLE_RESPONSE,
    VALIDATION_ERROR_RESPONSE,
    RateServiceDep,
)
from src.shared.schemas import Currency, RateQuote

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/v1", tags=["cotações"])


@limiter.limit("20/minute")
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
async def get_rate(
    currency: Currency,
    request: Request,
    rate_service: RateServiceDep,
) -> RateQuote:
    """Devolve a cotação da moeda.

    Args:
        currency: Moeda estrangeira (``USD`` ou ``EUR``).
        rate_service: Serviço de cotações.

    Returns:
        A cotação; ``stale`` é verdadeiro quando vem de cache vencido.
    """
    try:
        return await rate_service.get_quote(currency)
    except RatesUnavailableError:
        raise
    except Exception as exc:
        logger.error("Unhandled exception: %s", type(exc).__name__)
        raise HTTPException(status_code=500, detail="Erro interno. Tente novamente mais tarde.")
