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
from src.backend.schemas.invoice import (
    InvoiceCreateDraft,
    InvoiceResponse,
    InvoiceUpdate,
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


# ---------- Invoice draft: criar, atualizar, baixar PDF (SPEC-020, SPEC-021) ----------


def _to_invoice_response(inv) -> InvoiceResponse:
    return InvoiceResponse(
        id=inv.id,
        owner_user_id=inv.owner_user_id,
        client_id=inv.client_id,
        simulation_id=inv.simulation_id,
        invoice_number=inv.invoice_number,
        status=inv.status,
        locale=inv.locale,
        client_country_code=inv.client_country_code,
        finalized_at=inv.finalized_at,
        supersedes_invoice_id=inv.supersedes_invoice_id,
        number=inv.invoice_number,
        issuer_name=inv.issuer_name,
        issuer_tax_id_digits=inv.issuer_tax_id_digits,
        issuer_address=inv.issuer_address,
        client_name=inv.client_name,
        client_tax_id_digits=inv.client_tax_id_digits,
        client_address=inv.client_address,
        banco=inv.banco,
        agencia=inv.agencia,
        conta_com_digito=inv.conta_com_digito,
        pix_key=inv.pix_key,
        periodo_inicio=inv.periodo_inicio,
        periodo_fim=inv.periodo_fim,
        description=inv.description,
        regime=inv.regime,
        currency=inv.currency,
        amount=inv.amount,
        quantity=inv.quantity,
        spread_pct=inv.spread_pct,
        iof_pct=inv.iof_pct,
        gross_foreign=inv.gross_foreign,
        gross_brl=inv.gross_brl,
        spread_brl=inv.spread_brl,
        iof_brl=inv.iof_brl,
        net_brl=inv.net_brl,
        effective_rate=inv.effective_rate,
        quote_rate=inv.quote_rate,
        quote_source=inv.quote_source,
        quote_bulletin=inv.quote_bulletin,
        quoted_at=inv.quoted_at,
        stale=inv.stale,
        created_at=inv.created_at,
        updated_at=inv.updated_at,
    )


@router.post(
    "/invoices",
    response_model=InvoiceResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria invoice em draft (SPEC-020)",
    responses={
        400: {"model": ErrorResponse, "description": "Dados inválidos."},
        401: {"description": "Não autenticado", "model": ErrorResponse},
        409: {"model": ErrorResponse, "description": "Conflito de numeração."},
    },
)
async def create_invoice(
    payload: InvoiceCreateDraft,
    session: CurrentSession,
    repo: InvoiceRepository = Depends(get_invoice_repo),
) -> InvoiceResponse:
    """Cria uma invoice em status draft com número sequencial (DEC-06)."""

    sess = await _require_session(session)

    # DEC-07: cliente fictício exige country_code.
    if payload.client_id is None and not payload.client_fictitious:
        raise HTTPException(
            status_code=400,
            detail="Informe client_id ou client_fictitious.",
        )

    invoice_number = await repo.get_next_number(payload.issuer_tax_id_digits)

    from src.backend.models.invoice_repository import StoredInvoice
    from datetime import datetime as _dt

    now = _dt.now().astimezone()
    stored = StoredInvoice(
        id=0,
        owner_user_id=sess.user_id,
        client_id=payload.client_id,
        simulation_id=payload.simulation_id,
        invoice_number=invoice_number,
        status="draft",
        locale=payload.locale,
        client_country_code=payload.client_country_code,
        issuer_name=payload.issuer_name,
        issuer_tax_id_digits=payload.issuer_tax_id_digits,
        issuer_address=payload.issuer_address,
        client_name=payload.client_name,
        client_tax_id_digits=payload.client_tax_id_digits,
        client_address=payload.client_address,
        banco=payload.banco,
        agencia=payload.agencia,
        conta_com_digito=payload.conta_com_digito,
        pix_key=payload.pix_key,
        periodo_inicio=payload.periodo_inicio,
        periodo_fim=payload.periodo_fim,
        description=payload.description,
        regime=payload.regime,
        currency=payload.currency,
        amount=payload.amount,
        quantity=payload.quantity,
        spread_pct=payload.spread_pct,
        iof_pct=payload.iof_pct,
        gross_foreign=payload.gross_foreign,
        gross_brl=payload.gross_brl,
        spread_brl=payload.spread_brl,
        iof_brl=payload.iof_brl,
        net_brl=payload.net_brl,
        effective_rate=payload.effective_rate,
        quote_rate=payload.quote_rate,
        quote_source=payload.quote_source,
        quote_bulletin=payload.quote_bulletin,
        quoted_at=payload.quoted_at,
        stale=payload.stale,
        finalized_at=None,
        supersedes_invoice_id=None,
        created_at=now,
        updated_at=now,
    )
    await repo.save(stored)
    stored = await repo.get_by_number(invoice_number, sess.user_id)
    if stored is None:
        raise HTTPException(status_code=409, detail="Não foi possível criar a invoice.")
    return _to_invoice_response(stored)


@router.put(
    "/invoices/{invoice_id}",
    response_model=InvoiceResponse,
    summary="Atualiza invoice draft (SPEC-020)",
    responses={
        400: {"model": ErrorResponse, "description": "Invoice finalizada é imutável."},
        401: {"description": "Não autenticado", "model": ErrorResponse},
        404: {"description": "Invoice not found", "model": ErrorResponse},
    },
)
async def update_invoice(
    invoice_id: int,
    payload: InvoiceUpdate,
    session: CurrentSession,
    repo: InvoiceRepository = Depends(get_invoice_repo),
) -> InvoiceResponse:
    """Atualiza campos de uma invoice draft (finalized é imutável)."""

    sess = await _require_session(session)
    invoice = await repo.get_by_id(invoice_id, sess.user_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    if invoice.status != "draft":
        raise HTTPException(
            status_code=409,
            detail="Invoice finalizada é imutável",
        )

    from src.backend.models.invoice_repository import StoredInvoice

    updates: dict[str, Any] = {}
    for field in (
        "client_id",
        "client_fictitious",
        "issuer_name",
        "issuer_tax_id_digits",
        "issuer_address",
        "client_name",
        "client_tax_id_digits",
        "client_address",
        "banco",
        "agencia",
        "conta_com_digito",
        "pix_key",
        "periodo_inicio",
        "periodo_fim",
        "description",
    ):
        value = getattr(payload, field, None)
        if value is not None:
            updates[field] = value

    if not updates:
        return _to_invoice_response(invoice)

    updated = StoredInvoice(
        id=invoice.id,
        owner_user_id=invoice.owner_user_id,
        client_id=updates.get("client_id", invoice.client_id),
        simulation_id=invoice.simulation_id,
        invoice_number=invoice.invoice_number,
        status=invoice.status,
        locale=invoice.locale,
        client_country_code=invoice.client_country_code,
        issuer_name=updates.get("issuer_name", invoice.issuer_name),
        issuer_tax_id_digits=updates.get(
            "issuer_tax_id_digits", invoice.issuer_tax_id_digits
        ),
        issuer_address=updates.get("issuer_address", invoice.issuer_address),
        client_name=updates.get("client_name", invoice.client_name),
        client_tax_id_digits=updates.get(
            "client_tax_id_digits", invoice.client_tax_id_digits
        ),
        client_address=updates.get("client_address", invoice.client_address),
        banco=updates.get("banco", invoice.banco),
        agencia=updates.get("agencia", invoice.agencia),
        conta_com_digito=updates.get("conta_com_digito", invoice.conta_com_digito),
        pix_key=updates.get("pix_key", invoice.pix_key),
        periodo_inicio=updates.get("periodo_inicio", invoice.periodo_inicio),
        periodo_fim=updates.get("periodo_fim", invoice.periodo_fim),
        description=updates.get("description", invoice.description),
        regime=invoice.regime,
        currency=invoice.currency,
        amount=invoice.amount,
        quantity=invoice.quantity,
        spread_pct=invoice.spread_pct,
        iof_pct=invoice.iof_pct,
        gross_foreign=invoice.gross_foreign,
        gross_brl=invoice.gross_brl,
        spread_brl=invoice.spread_brl,
        iof_brl=invoice.iof_brl,
        net_brl=invoice.net_brl,
        effective_rate=invoice.effective_rate,
        quote_rate=invoice.quote_rate,
        quote_source=invoice.quote_source,
        quote_bulletin=invoice.quote_bulletin,
        quoted_at=invoice.quoted_at,
        stale=invoice.stale,
        finalized_at=invoice.finalized_at,
        supersedes_invoice_id=invoice.supersedes_invoice_id,
        created_at=invoice.created_at,
        updated_at=invoice.updated_at,
    )
    await repo.save(updated)
    return _to_invoice_response(updated)


@router.get(
    "/invoices/{invoice_id}/download",
    responses={
        200: {
            "description": "PDF da invoice para download.",
            "content": {"application/pdf": {"schema": {"type": "string", "format": "binary"}}},
        },
        401: {"description": "Não autenticado", "model": ErrorResponse},
        404: {"description": "Invoice not found", "model": ErrorResponse},
        503: {"model": ErrorResponse, "description": "PDF indisponível (pdf_unavailable)."},
    },
)
async def download_invoice_pdf(
    invoice_id: int,
    session: CurrentSession,
    rate_service: RateServiceDep,
    repo: InvoiceRepository = Depends(get_invoice_repo),
) -> Response:
    """Baixa o PDF de uma invoice já persistida (snapshot reprodutível, SPEC-021)."""

    sess = await _require_session(session)
    invoice = await repo.get_by_id(invoice_id, sess.user_id)
    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")

    pdf_bytes = await render_pdf_from_stored(invoice, rate_service)

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="invoice_{invoice.invoice_number}.pdf"',
            "Cache-Control": "no-store",
        },
    )
