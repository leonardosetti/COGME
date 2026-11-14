"""Rotas de invoices: listagem, recuperação, finalização, clone e erase
(DEC-04, DEC-05, DEC-06, DEC-07).

Implementa:
- GET /v1/invoices (listagem paginada)
- GET /v1/invoices/{id} (recupera + renderiza PDF)
- POST /v1/invoices/{id}/finalize (draft -> finalized, DEC-05)
- POST /v1/invoices/{id}/clone (clone cria novo draft, DEC-05)
- DELETE /v1/invoices/{id} (erase LGPD art. 18, DEC-04)
"""

from __future__ import annotations

import logging
from typing import Any, Final

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, status
from pydantic import BaseModel

from src.backend.models.invoice_repository import (
    InvoiceRepository,
    SqlAlchemyInvoiceRepository,
)
from src.backend.routers.common import (
    INTERNAL_ERROR_RESPONSE,
    VALIDATION_ERROR_RESPONSE,
    RateServiceDep,
)
from src.backend.services.invoice_service import render_invoice
from src.shared.schemas import (
    ErrorResponse,
    InvoiceRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/v1", tags=["invoices"])


# ---------- Original Invoice PDF Generation (REQ-04) -->


# Keep the original route class and responses for backward compatibility
_ORIGINAL_RESPONSES: Final[dict[int | str, dict[str, Any]]] = {
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
    summary="Gera a invoice em PDF (endpoint original REQ-04)",
    responses=_ORIGINAL_RESPONSES,
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


# ---------- Expanded Invoice Routes (SPEC-020) ----------


class CloneResponse(BaseModel):
    """Response para clone de invoice."""

    invoice_id: int
    invoice_number: str
    status: str
    supersedes_invoice_id: int


def get_invoice_repo() -> InvoiceRepository:
    return SqlAlchemyInvoiceRepository()


@router.get(
    "/invoices",
    responses={
        200: {"description": "Lista de invoices"},
        401: {"description": "Não autenticado", "model": ErrorResponse},
    },
)
async def list_invoices(
    request: Request,
    owner_user_id: int = Query(1, alias="owner_user_id"),
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    status: str | None = Query(None, regex="^(draft|finalized)$"),
    repo: InvoiceRepository = Depends(get_invoice_repo),
) -> list[dict[str, Any]]:
    """Lista invoices do usuário com paginação."""
    invoices = repo.list_invoices(owner_user_id, limit=limit, offset=offset, status=status)
    return [inv.to_dict() for inv in invoices]


@router.get(
    "/invoices/{invoice_id}",
    responses={
        200: {"description": "PDF da invoice"},
        401: {"description": "Não autenticado", "model": ErrorResponse},
        404: {"description": "Invoice not found", "model": ErrorResponse},
    },
)
async def get_invoice_pdf(
    invoice_id: int,
    repo: InvoiceRepository = Depends(get_invoice_repo),
    owner_user_id: int = Query(1, alias="owner_user_id"),
) -> Response:
    """Recupera invoice e renderiza PDF."""
    invoice = repo.get_invoice(invoice_id, owner_user_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    pdf_bytes = render_invoice(invoice)

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="invoice_{invoice.invoice_number}.pdf"'
        },
    )


@router.post(
    "/invoices/{invoice_id}/finalize",
    responses={
        200: {"description": "Invoice finalizada"},
        401: {"description": "Não autenticado", "model": ErrorResponse},
        404: {"description": "Invoice not found", "model": ErrorResponse},
        409: {
            "description": "Invoice não está em status draft",
            "model": ErrorResponse,
        },
    },
)
async def finalize_invoice(
    invoice_id: int,
    repo: InvoiceRepository = Depends(get_invoice_repo),
    owner_user_id: int = Query(1, alias="owner_user_id"),
) -> dict[str, Any]:
    """Finaliza invoice: draft -> finalized (DEC-05)."""
    invoice = repo.get_invoice(invoice_id, owner_user_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    if invoice.status != "draft":
        raise HTTPException(status_code=409, detail="Invoice não está em status draft")

    updated = repo.finalize(invoice_id, owner_user_id)
    return updated.to_dict()


@router.post(
    "/invoices/{invoice_id}/clone",
    response_model=CloneResponse,
    status_code=status.HTTP_201_CREATED,
)
async def clone_invoice(
    invoice_id: int,
    repo: InvoiceRepository = Depends(get_invoice_repo),
    owner_user_id: int = Query(1, alias="owner_user_id"),
) -> CloneResponse:
    """Clona invoice finalizada -> novo draft (DEC-05, US-017).

    O clone:
    - Recebe novo número único (via next_invoice_number, DEC-06)
    - Status = 'draft'
    - supersedes_invoice_id = invoice_id original
    """
    invoice = repo.get_invoice(invoice_id, owner_user_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    if invoice.status != "finalized":
        raise HTTPException(status_code=409, detail="Invoice não está em status finalized")

    cloned = repo.clone(invoice_id, owner_user_id)
    return CloneResponse(
        invoice_id=cloned.id,
        invoice_number=cloned.invoice_number,
        status=cloned.status,
        supersedes_invoice_id=invoice_id,
    )


@router.delete(
    "/invoices/{invoice_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Invoice apagada (erase LGPD)"},
        401: {"description": "Não autenticado", "model": ErrorResponse},
        404: {"description": "Invoice not found", "model": ErrorResponse},
        409: {
            "description": "Invoice não pode ser apagada (status finalized)",
            "model": ErrorResponse,
        },
    },
)
async def erase_invoice(
    invoice_id: int,
    repo: InvoiceRepository = Depends(get_invoice_repo),
    owner_user_id: int = Query(1, alias="owner_user_id"),
) -> Response:
    """Apaga invoice (erase LGPD art. 18, DEC-04).

    Apenas invoices em status 'draft' podem ser apagadas.
    """
    invoice = repo.get_invoice(invoice_id, owner_user_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    if invoice.status != "draft":
        raise HTTPException(
            status_code=409, detail="Invoice não pode ser apagada (status finalized)"
        )

    repo.erase(invoice_id, owner_user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
