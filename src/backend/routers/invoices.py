"""Rota da invoice em PDF (spec backend-mvp-v1, §3 e §6; REQ-04)."""

from __future__ import annotations

from typing import Any, Final

from fastapi import APIRouter, Response

from src.backend.routers.common import (
    INTERNAL_ERROR_RESPONSE,
    VALIDATION_ERROR_RESPONSE,
    DecimalJsonRoute,
    RateServiceDep,
)
from src.backend.services.invoice_service import render_invoice
from src.shared.schemas import ErrorResponse, InvoiceRequest

router = APIRouter(prefix="/v1", tags=["invoice"], route_class=DecimalJsonRoute)

_RESPONSES: Final[dict[int | str, dict[str, Any]]] = {
    200: {
        "description": "PDF da invoice, enviado como anexo.",
        "content": {"application/pdf": {"schema": {"type": "string", "format": "binary"}}},
    },
    **VALIDATION_ERROR_RESPONSE,
    **INTERNAL_ERROR_RESPONSE,
    503: {
        "model": ErrorResponse,
        "description": "Cotação ou PDF indisponível (rates_unavailable, pdf_unavailable).",
    },
}


@router.post(
    "/invoice",
    response_class=Response,
    summary="Gera a invoice em PDF",
    responses=_RESPONSES,
)
async def post_invoice(payload: InvoiceRequest, rate_service: RateServiceDep) -> Response:
    """Recalcula a simulação no servidor e devolve a invoice em PDF.

    Os dados pessoais da requisição não são gravados nem registrados em log, e a resposta não
    pode ser guardada em cache.

    Args:
        payload: Entrada validada pelo contrato.
        rate_service: Serviço de cotações.

    Returns:
        O PDF como anexo ``invoice.pdf``.
    """
    pdf = await render_invoice(payload, rate_service)
    return Response(
        content=pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": 'attachment; filename="invoice.pdf"',
            "Cache-Control": "no-store",
        },
    )
