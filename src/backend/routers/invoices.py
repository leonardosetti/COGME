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
from dataclasses import asdict
from datetime import datetime
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
    CurrentSession,
    RateServiceDep,
    SessionFactoryDep,
    SessionData,
    require_owner,
)
from src.backend.services.invoice_service import render_invoice, render_pdf_from_stored
from src.shared.schemas import (
    ErrorResponse,
    InvoiceRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/v1", tags=["invoices"])


def get_invoice_repo(
    session_factory: SessionFactoryDep,
) -> InvoiceRepository:
    return SqlAlchemyInvoiceRepository(session_factory)


async def _require_session(session: CurrentSession) -> SessionData:
    if session is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não autenticado",
            headers={"WWW-Authenticate": "Cookie"},
        )
    return session


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


def get_invoice_repo(
    session_factory: SessionFactoryDep,
) -> InvoiceRepository:
    return SqlAlchemyInvoiceRepository(session_factory)


@router.get(
    "/invoices",
    responses={
        200: {"description": "Lista de invoices"},
        401: {"description": "Não autenticado", "model": ErrorResponse},
    },
)
async def list_invoices(
    request: Request,
    session: CurrentSession,
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    status: str | None = Query(None, pattern="^(draft|finalized)$"),
    repo: InvoiceRepository = Depends(get_invoice_repo),
) -> list[dict[str, Any]]:
    """Lista invoices do usuário com paginação."""
    sess = await _require_session(session)
    page = (offset // limit) + 1 if limit else 1
    invoices, _total = await repo.list_by_owner(
        sess.user_id, status=status, page=page, page_size=limit
    )
    return [asdict(inv) for inv in invoices]


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
    rate_service: RateServiceDep,
    session: CurrentSession,
    repo: InvoiceRepository = Depends(get_invoice_repo),
) -> Response:
    """Recupera invoice e renderiza PDF."""
    sess = await _require_session(session)
    invoice = await repo.get_by_id(invoice_id, sess.user_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")

    pdf_bytes = await render_pdf_from_stored(invoice, rate_service)

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
    session: CurrentSession,
    repo: InvoiceRepository = Depends(get_invoice_repo),
) -> dict[str, Any]:
    """Finaliza invoice: draft -> finalized (DEC-05)."""
    sess = await _require_session(session)
    invoice = await repo.get_by_id(invoice_id, sess.user_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    if invoice.status != "draft":
        raise HTTPException(
            status_code=409,
            detail="Invoice não está em status draft",
        )

    updated = await repo.update_status(
        invoice_id, sess.user_id, "finalized", datetime.now().astimezone()
    )
    if updated is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return asdict(updated)


@router.post(
    "/invoices/{invoice_id}/clone",
    response_model=CloneResponse,
    status_code=status.HTTP_201_CREATED,
)
async def clone_invoice(
    invoice_id: int,
    session: CurrentSession,
    repo: InvoiceRepository = Depends(get_invoice_repo),
) -> CloneResponse:
    """Clona invoice finalizada -> novo draft (DEC-05, US-017)."""
    sess = await _require_session(session)
    invoice = await repo.get_by_id(invoice_id, sess.user_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    if invoice.status != "finalized":
        raise HTTPException(status_code=409, detail="Invoice não está em status finalized")

    cloned = await repo.clone(invoice_id, sess.user_id)
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
    session: CurrentSession,
    repo: InvoiceRepository = Depends(get_invoice_repo),
) -> Response:
    """Apaga invoice (erase LGPD art. 18, DEC-04).

    Apenas invoices em status 'draft' podem ser apagadas.
    """
    sess = await _require_session(session)
    invoice = await repo.get_by_id(invoice_id, sess.user_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")

    if invoice.status != "draft":
        raise HTTPException(
            status_code=409, detail="Invoice não pode ser apagada (status finalized)"
        )

    await repo.delete(invoice_id, sess.user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
