"""Rota de simulação (spec backend-mvp-v1, §3; REQ-02, REQ-03) e simulações salvas (SPEC-020)."""

from __future__ import annotations

from decimal import Decimal
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.middleware.rate_limit import limiter
from src.backend.routers.common import (
    CurrentSession,
    INTERNAL_ERROR_RESPONSE,
    RATES_UNAVAILABLE_RESPONSE,
    SessionFactoryDep,
    VALIDATION_ERROR_RESPONSE,
    DecimalJsonRoute,
    RateServiceDep,
    get_session_factory,
)
from src.backend.models.simulation import Simulation
from src.backend.services.calculator import calculate
from src.backend.services.simulation_service import simulate
from src.shared.schemas import Currency, Regime, SimulationRequest, SimulationResponse

router = APIRouter(prefix="/v1", tags=["simulações"], route_class=DecimalJsonRoute)


class SimulationSaveRequest(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    currency: str = Field(pattern=r"^(USD|EUR)$")
    regime: str = Field(pattern=r"^(hourly|daily|weekly|monthly|fixed)$")
    amount: str = Field(description="Valor por unidade do regime (texto decimal).")
    quantity: str | None = Field(default=None, description="Quantidade de unidades (texto decimal).")
    spread_pct: str = Field(description="Spread informado pelo usuário, em % (texto decimal).")
    iof_pct: str = Field(description="IOF informado pelo usuário, em % (texto decimal).")


class SimulationSavedResponse(BaseModel):
    id: int
    owner_user_id: int
    name: str
    regime: str
    currency: str
    amount: str
    quantity: str | None = None
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
    quote_bulletin: str | None = None
    quoted_at: str
    stale: bool


def _require_session(session: CurrentSession):
    if session is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não autenticado",
            headers={"WWW-Authenticate": "Cookie"},
        )
    return session


def _to_saved_response(row: Simulation) -> SimulationSavedResponse:
    return SimulationSavedResponse(
        id=row.id,
        owner_user_id=row.owner_user_id,
        name=row.name,
        regime=row.regime,
        currency=row.currency,
        amount=str(row.amount),
        quantity=str(row.quantity) if row.quantity is not None else None,
        spread_pct=str(row.spread_pct),
        iof_pct=str(row.iof_pct),
        gross_foreign=str(row.gross_foreign),
        gross_brl=str(row.gross_brl),
        spread_brl=str(row.spread_brl),
        iof_brl=str(row.iof_brl),
        net_brl=str(row.net_brl),
        effective_rate=str(row.effective_rate),
        quote_rate=str(row.quote_rate),
        quote_source=row.quote_source,
        quote_bulletin=row.quote_bulletin,
        quoted_at=row.quoted_at.isoformat(),
        stale=row.stale,
    )


async def _session_factory(request: Request) -> async_sessionmaker[AsyncSession]:
    return get_session_factory(request)


@router.post(
    "/simulations",
    response_model=SimulationSavedResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Salva uma simulação (opt-in, SPEC-020)",
)
@limiter.limit("20/minute")
async def save_simulation(
    payload: SimulationSaveRequest,
    request: Request,
    session: CurrentSession,
    rate_service: RateServiceDep,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> SimulationSavedResponse:
    """Calcula e persiste uma simulação para histórico do usuário."""
    sess = _require_session(session)
    regime = Regime(payload.regime)
    amount = Decimal(payload.amount)
    quantity = Decimal(payload.quantity) if payload.quantity is not None else None
    spread_pct = Decimal(payload.spread_pct)
    iof_pct = Decimal(payload.iof_pct)
    quote = await rate_service.get_quote(Currency(payload.currency))
    breakdown = calculate(regime, amount, quantity, quote.rate, spread_pct, iof_pct)
    async with sf() as db, db.begin():
        row = Simulation(
            owner_user_id=sess.user_id,
            name=payload.name,
            regime=payload.regime,
            currency=payload.currency,
            amount=amount,
            quantity=quantity,
            spread_pct=spread_pct,
            iof_pct=iof_pct,
            gross_foreign=breakdown.gross_foreign,
            gross_brl=breakdown.gross_brl,
            spread_brl=breakdown.spread_brl,
            iof_brl=breakdown.iof_brl,
            net_brl=breakdown.net_brl,
            effective_rate=breakdown.effective_rate,
            quote_rate=quote.rate,
            quote_source=quote.source,
            quote_bulletin=quote.bulletin,
            quoted_at=quote.quoted_at,
            stale=quote.stale,
        )
        db.add(row)
        await db.flush()
        await db.refresh(row)
        return _to_saved_response(row)


@router.get(
    "/simulations",
    response_model=list[SimulationSavedResponse],
    summary="Lista simulações salvas do usuário",
)
async def list_simulations(
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
) -> list[SimulationSavedResponse]:
    sess = _require_session(session)
    async with sf() as db:
        rows = (
            await db.execute(
                select(Simulation)
                .where(Simulation.owner_user_id == sess.user_id)
                .order_by(Simulation.created_at.desc())
                .limit(limit)
                .offset(offset)
            )
        ).scalars().all()
    return [_to_saved_response(r) for r in rows]


@router.get(
    "/simulations/{simulation_id}",
    response_model=SimulationSavedResponse,
    summary="Detalha simulação salva",
)
async def get_simulation(
    simulation_id: int,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> SimulationSavedResponse:
    sess = _require_session(session)
    async with sf() as db:
        row = (
            await db.execute(
                select(Simulation).where(
                    Simulation.id == simulation_id,
                    Simulation.owner_user_id == sess.user_id,
                )
            )
        ).scalar_one_or_none()
        if row is None:
            raise HTTPException(status_code=404, detail="Simulação não encontrada")
        return _to_saved_response(row)


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
@limiter.limit("20/minute")
async def post_simulation(
    payload: SimulationRequest,
    request: Request,
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
