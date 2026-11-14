"""Rotas de invoices: listagem, recuperação, finalização, clone e erase
(DEC-04, DEC-05, DEC-06, DEC-07).

Implementa:
- GET /v1/invoices (listagem paginada)
- GET /v1/invoices/{id} (recupera + renderiza PDF)
- POST /v1/invoices/{id}/finalize (draft → finalized, DEC-05)
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
    RepositoryError,
    SqlAlchemyInvoiceRepository,
)
from src.backend.routers.common import get_rate_service
from src.backend.services.invoice_service import render_invoice
from src.backend.services.rate_service import RateService
from src.shared.schemas import (
    Currency,
    InvoiceParty,
    InvoiceRequest,
    RateQuote,
    RateSource,
    Regime,
    SimulationRequest,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/v1", tags=["invoices"])


# ---------- Original Invoice PDF Generation (REQ-04) ----------


from src.backend.routers.common import (
    INTERNAL_ERROR_RESPONSE,
    VALIDATION_ERROR_RESPONSE,
    DecimalJsonRoute,
    RateServiceDep,
)
from src.shared.schemas import ErrorResponse


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


# ---------- Dependencies ----------


def get_invoice_repo(request: Request) -> InvoiceRepository:
    """Entrega o repository de invoices com session_factory do app.state."""
    from src.backend.models.database import create_session_factory

    engine = request.app.state.engine
    session_factory = create_session_factory(engine)
    return SqlAlchemyInvoiceRepository(session_factory)


# ---------- Schemas ----------


class InvoiceListItem(BaseModel):
    """Item da listagem de invoices."""

    id: int
    invoice_number: str
    status: str
    locale: str
    client_name: str
    client_tax_id_digits: str
    regime: str
    currency: str
    net_brl: str  # Decimal as string
    created_at: str  # ISO 8601
    finalized_at: str | None


class InvoiceListResponse(BaseModel):
    """Resposta paginada da listagem."""

    items: list[InvoiceListItem]
    total: int
    page: int
    page_size: int
    total_pages: int


class FinalizeRequest(BaseModel):
    """Request para finalizar invoice (draft → finalized)."""

    pass  # sem body; finalized_at = agora


class CloneResponse(BaseModel):
    """Resposta do clone: novo invoice draft."""

    id: int
    invoice_number: str
    status: str  # sempre 'draft'
    supersedes_invoice_id: int


class InvoiceDetailResponse(BaseModel):
    """Detalhes completos da invoice (para visualização/debug)."""

    id: int
    invoice_number: str
    status: str
    locale: str
    client_country_code: str
    issuer: InvoiceParty
    client: InvoiceParty
    banco: str | None
    agencia: str | None
    conta_com_digito: str | None
    pix_key: str | None
    periodo_inicio: str
    periodo_fim: str
    description: str
    regime: str
    currency: str
    amount: str
    quantity: str | None
    spread_pct: str
    iof_pct: str
    gross_foreign: str
    gross_brl: str
    spread_brl: str
    iof_brl: str
    net_brl: str
    effective_rate: str
    quote_rate: str
    quote_source: str
    quote_bulletin: str | None
    quoted_at: str
    stale: bool
    finalized_at: str | None
    supersedes_invoice_id: int | None
    created_at: str
    updated_at: str


# ---------- Helpers ----------


def _to_detail_response(invoice: Any) -> InvoiceDetailResponse:
    return InvoiceDetailResponse(
        id=invoice.id,
        invoice_number=invoice.invoice_number,
        status=invoice.status,
        locale=invoice.locale,
        client_country_code=invoice.client_country_code,
        issuer=InvoiceParty(
            name=invoice.issuer_name,
            tax_id=invoice.issuer_tax_id_digits,
            address=invoice.issuer_address,
        ),
        client=InvoiceParty(
            name=invoice.client_name,
            tax_id=invoice.client_tax_id_digits,
            address=invoice.client_address,
        ),
        banco=invoice.banco,
        agencia=invoice.agencia,
        conta_com_digito=invoice.conta_com_digito,
        pix_key=invoice.pix_key,
        periodo_inicio=invoice.periodo_inicio.isoformat(),
        periodo_fim=invoice.periodo_fim.isoformat(),
        description=invoice.description,
        regime=invoice.regime,
        currency=invoice.currency,
        amount=str(invoice.amount),
        quantity=str(invoice.quantity) if invoice.quantity is not None else None,
        spread_pct=str(invoice.spread_pct),
        iof_pct=str(invoice.iof_pct),
        gross_foreign=str(invoice.gross_foreign),
        gross_brl=str(invoice.gross_brl),
        spread_brl=str(invoice.spread_brl),
        iof_brl=str(invoice.iof_brl),
        net_brl=str(invoice.net_brl),
        effective_rate=str(invoice.effective_rate),
        quote_rate=str(invoice.quote_rate),
        quote_source=invoice.quote_source,
        quote_bulletin=invoice.quote_bulletin,
        quoted_at=invoice.quoted_at.isoformat(),
        stale=invoice.stale,
        finalized_at=invoice.finalized_at.isoformat() if invoice.finalized_at else None,
        supersedes_invoice_id=invoice.supersedes_invoice_id,
        created_at=invoice.created_at.isoformat(),
        updated_at=invoice.updated_at.isoformat(),
    )


def _to_list_item(invoice: Any) -> InvoiceListItem:
    return InvoiceListItem(
        id=invoice.id,
        invoice_number=invoice.invoice_number,
        status=invoice.status,
        locale=invoice.locale,
        client_name=invoice.client_name,
        client_tax_id_digits=invoice.client_tax_id_digits,
        regime=invoice.regime,
        currency=invoice.currency,
        net_brl=str(invoice.net_brl),
        created_at=invoice.created_at.isoformat(),
        finalized_at=invoice.finalized_at.isoformat() if invoice.finalized_at else None,
    )


# ---------- Routes ----------


@router.get("/invoices", response_model=InvoiceListResponse)
async def list_invoices(
    status: str | None = Query(None, pattern="^(draft|finalized)$"),
    client_id: int | None = Query(None, ge=1),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    repo: InvoiceRepository = Depends(get_invoice_repo),
    # TODO: substituir por get_current_user quando auth estiver pronto
    owner_user_id: int = Query(
        1, alias="owner_user_id", description="Temporário: owner_user_id fixo até auth"
    ),
) -> InvoiceListResponse:
    """Lista invoices do owner com paginação e filtros."""
    try:
        items, total = await repo.list_by_owner(
            owner_user_id=owner_user_id,
            status=status,
            client_id=client_id,
            page=page,
            page_size=page_size,
        )
    except RepositoryError as e:
        logger.error(
            "list_invoices_failed owner_user_id=%d error=%s",
            owner_user_id,
            type(e).__name__,
        )
        raise HTTPException(status_code=500, detail="Falha ao listar invoices") from e

    return InvoiceListResponse(
        items=[_to_list_item(i) for i in items],
        total=total,
        page=page,
        page_size=page_size,
        total_pages=(total + page_size - 1) // page_size,
    )


@router.get("/invoices/{invoice_id}", response_model=None)
async def get_invoice(
    invoice_id: int,
    repo: InvoiceRepository = Depends(get_invoice_repo),
    owner_user_id: int = Query(1, alias="owner_user_id"),
    as_pdf: bool = Query(
        False, description="Se true, retorna PDF (Content-Disposition: attachment)"
    ),
    rate_service: RateService = Depends(get_rate_service),
) -> Response | InvoiceDetailResponse:
    """Recupera invoice. Se as_pdf=true, renderiza e retorna PDF."""
    try:
        invoice = await repo.get_by_id(invoice_id, owner_user_id)
    except RepositoryError as e:
        logger.error(
            "get_invoice_failed invoice_id=%d owner_user_id=%d error=%s",
            invoice_id,
            owner_user_id,
            type(e).__name__,
        )
        raise HTTPException(status_code=500, detail="Falha ao buscar invoice") from e

    if invoice is None:
        raise HTTPException(status_code=404, detail="Invoice não encontrada")

    if not as_pdf:
        return _to_detail_response(invoice)

    # Renderiza PDF usando o template conforme locale (DEC-07)
    try:
        # Reconstrói InvoiceRequest a partir da invoice persistida para render_invoice
        # NOTA: Aqui usamos a cotação original persistida (reprodutibilidade)
        quote = RateQuote(
            currency=Currency(invoice.currency),
            rate=invoice.quote_rate,
            source=RateSource(invoice.quote_source),
            bulletin=invoice.quote_bulletin,
            stale=invoice.stale,
            quoted_at=invoice.quoted_at,
        )

        sim_request = SimulationRequest(
            currency=Currency(invoice.currency),
            regime=Regime(invoice.regime),
            amount=invoice.amount,
            quantity=invoice.quantity,
            spread_pct=invoice.spread_pct,
            iof_pct=invoice.iof_pct,
        )

        invoice_request = InvoiceRequest(
            simulation=sim_request,
            issuer=InvoiceParty(
                name=invoice.issuer_name,
                tax_id=invoice.issuer_tax_id_digits,
                address=invoice.issuer_address,
            ),
            client=InvoiceParty(
                name=invoice.client_name,
                tax_id=invoice.client_tax_id_digits,
                address=invoice.client_address,
            ),
            invoice_number=invoice.invoice_number,
            issue_date=invoice.periodo_fim,  # usa fim do período como data de emissão
            description=invoice.description,
        )

        # Mock rate_service para devolver a cotação persistida (não buscar nova)
        class CachedRateService:
            async def get_quote(self, currency: Currency) -> RateQuote:
                return quote

        pdf_bytes = await render_invoice(
            invoice_request, CachedRateService()  # type: ignore[arg-type]
        )

        filename = f"invoice-{invoice.invoice_number}.pdf"
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f'attachment; filename="{filename}"',
                "Cache-Control": "no-store",
            },
        )
    except Exception as e:
        logger.error(
            "invoice_pdf_render_failed invoice_id=%d error=%s",
            invoice_id,
            type(e).__name__,
        )
        raise HTTPException(status_code=500, detail="Falha ao gerar PDF") from e


@router.post("/invoices/{invoice_id}/finalize", response_model=InvoiceDetailResponse)
async def finalize_invoice(
    invoice_id: int,
    _req: FinalizeRequest,
    repo: InvoiceRepository = Depends(get_invoice_repo),
    owner_user_id: int = Query(1, alias="owner_user_id"),
) -> InvoiceDetailResponse:
    """Transição draft → finalized (DEC-05). Imutável após finalize."""
    from datetime import datetime, UTC

    try:
        updated = await repo.update_status(
            invoice_id=invoice_id,
            owner_user_id=owner_user_id,
            status="finalized",
            finalized_at=datetime.now(UTC),
        )
    except RepositoryError as e:
        logger.error(
            "finalize_invoice_failed invoice_id=%d owner_user_id=%d error=%s",
            invoice_id,
            owner_user_id,
            type(e).__name__,
        )
        raise HTTPException(status_code=500, detail="Falha ao finalizar invoice") from e

    if updated is None:
        raise HTTPException(status_code=404, detail="Invoice não encontrada ou não autorizada")

    if updated.status != "finalized":
        raise HTTPException(status_code=409, detail="Invoice não está em status draft")

    return _to_detail_response(updated)


@router.post(
    "/invoices/{invoice_id}/clone", response_model=CloneResponse, status_code=status.HTTP_201_CREATED
)
async def clone_invoice(
    invoice_id: int,
    repo: InvoiceRepository = Depends(get_invoice_repo),
    owner_user_id: int = Query(1, alias="owner_user_id"),
) -> CloneResponse:
    """Clona invoice finalizada → novo draft (DEC-05, US-017).

    O clone:
    - Recebe novo número único (via next_invoice_number, DEC-06)
    - Status = 'draft'
    - supersedes_invoice_id = invoice_id original
    - Copia todos os campos de cálculo e partes
    """
    from datetime import datetime, UTC

    # 1. Busca original
    try:
        original = await repo.get_by_id(invoice_id, owner_user_id)
    except RepositoryError as e:
        logger.error(
            "clone_invoice_fetch_failed invoice_id=%d owner_user_id=%d error=%s",
            invoice_id,
            owner_user_id,
            type(e).__name__,
        )
        raise HTTPException(status_code=500, detail="Falha ao buscar invoice original") from e

    if original is None:
        raise HTTPException(status_code=404, detail="Invoice não encontrada")

    if original.status != "finalized":
        raise HTTPException(status_code=409, detail="Só é permitido clonar invoices finalizadas")

    # 2. Gera novo número
    try:
        new_number = await repo.get_next_number(original.issuer_tax_id_digits)
    except RepositoryError as e:
        logger.error(
            "clone_invoice_number_failed issuer=%s error=%s",
            original.issuer_tax_id_digits,
            type(e).__name__,
        )
        raise HTTPException(status_code=500, detail="Falha ao gerar número de invoice") from e

    # 3. Cria clone (draft)
    now = datetime.now(UTC)
    clone = type(original)(
        id=0,  # será preenchido pelo DB (BIGSERIAL)
        owner_user_id=original.owner_user_id,
        client_id=original.client_id,
        simulation_id=original.simulation_id,
        invoice_number=new_number,
        status="draft",
        locale=original.locale,
        client_country_code=original.client_country_code,
        issuer_name=original.issuer_name,
        issuer_tax_id_digits=original.issuer_tax_id_digits,
        issuer_address=original.issuer_address,
        client_name=original.client_name,
        client_tax_id_digits=original.client_tax_id_digits,
        client_address=original.client_address,
        banco=original.banco,
        agencia=original.agencia,
        conta_com_digito=original.conta_com_digito,
        pix_key=original.pix_key,
        periodo_inicio=original.periodo_inicio,
        periodo_fim=original.periodo_fim,
        description=original.description,
        regime=original.regime,
        currency=original.currency,
        amount=original.amount,
        quantity=original.quantity,
        spread_pct=original.spread_pct,
        iof_pct=original.iof_pct,
        gross_foreign=original.gross_foreign,
        gross_brl=original.gross_brl,
        spread_brl=original.spread_brl,
        iof_brl=original.iof_brl,
        net_brl=original.net_brl,
        effective_rate=original.effective_rate,
        quote_rate=original.quote_rate,
        quote_source=original.quote_source,
        quote_bulletin=original.quote_bulletin,
        quoted_at=original.quoted_at,
        stale=original.stale,
        finalized_at=None,
        supersedes_invoice_id=original.id,
        created_at=now,
        updated_at=now,
    )

    try:
        await repo.save(clone)
    except RepositoryError as e:
        logger.error(
            "clone_invoice_save_failed new_number=%s error=%s",
            new_number,
            type(e).__name__,
        )
        raise HTTPException(status_code=500, detail="Falha ao salvar clone") from e

    return CloneResponse(
        id=clone.id,
        invoice_number=clone.invoice_number,
        status=clone.status,
        supersedes_invoice_id=original.id,
    )


@router.delete("/invoices/{invoice_id}", status_code=status.HTTP_204_NO_CONTENT)
async def erase_invoice(
    invoice_id: int,
    repo: InvoiceRepository = Depends(get_invoice_repo),
    owner_user_id: int = Query(1, alias="owner_user_id"),
) -> Response:
    """Erase LGPD art. 18: hard delete + log auditoria (sem PII) (DEC-04).

    Remove a invoice permanentemente. Backups são limpos por job separado (30 dias).
    """
    try:
        deleted = await repo.delete(invoice_id, owner_user_id)
    except RepositoryError as e:
        logger.error(
            "erase_invoice_failed invoice_id=%d owner_user_id=%d error=%s",
            invoice_id,
            owner_user_id,
            type(e).__name__,
        )
        raise HTTPException(status_code=500, detail="Falha ao apagar invoice") from e

    if not deleted:
        raise HTTPException(status_code=404, detail="Invoice não encontrada ou não autorizada")

    # Log auditoria (sem PII)
    logger.info("invoice_erased invoice_id=%d owner_user_id=%d", invoice_id, owner_user_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
