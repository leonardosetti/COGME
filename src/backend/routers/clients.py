"""Rotas do diretório de clientes (spec-004 §4.4; SPEC-019).

Todas exigem sessão e isolamento por proprietário (P-14): o repo filtra por
``owner_user_id`` da sessão.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, status
from pydantic import BaseModel, Field
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.routers.common import (
    CurrentSession,
    SessionFactoryDep,
    get_session_factory,
)
from src.backend.models.client import Client

router = APIRouter(prefix="/v1/clients", tags=["clientes"])


async def _session_factory(request: Request) -> async_sessionmaker[AsyncSession]:
    return get_session_factory(request)


def _require_session(session: CurrentSession):
    if session is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não autenticado",
            headers={"WWW-Authenticate": "Cookie"},
        )
    return session


# ── Schemas ───────────────────────────────────────────────────────────


class ClientRequest(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    tax_id: str = Field(pattern=r"^\d{11}$|^\d{14}$")
    address: str | None = Field(default=None, max_length=500)
    country_code: str = Field(default="BR", max_length=2)


class ClientResponse(BaseModel):
    id: int
    name: str
    tax_id: str
    tax_id_type: str
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    country_code: str
    status: str


# ── CRUD ──────────────────────────────────────────────────────────────


@router.get("", response_model=list[ClientResponse], summary="Lista clientes")
async def list_clients(
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
) -> list[ClientResponse]:
    sess = _require_session(session)
    async with sf() as db:
        rows = (
            await db.execute(
                select(Client)
                .where(Client.owner_user_id == sess.user_id)
                .order_by(Client.created_at.desc())
                .limit(limit)
                .offset(offset)
            )
        ).scalars().all()
    return [_to_response(r) for r in rows]


@router.post("", response_model=ClientResponse, status_code=status.HTTP_201_CREATED, summary="Cadastra cliente")
async def create_client(
    payload: ClientRequest,
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> ClientResponse:
    sess = _require_session(session)
    tax_id_digits = "".join(ch for ch in payload.tax_id if ch.isdigit())
    tax_id_type = "cpf" if len(tax_id_digits) == 11 else "cnpj"
    async with sf() as db, db.begin():
        row = Client(
            owner_user_id=sess.user_id,
            name=payload.name,
            tax_id_digits=tax_id_digits,
            tax_id_type=tax_id_type,
            address=payload.address,
            country_code=payload.country_code,
            status="active",
        )
        db.add(row)
        await db.flush()
        await db.refresh(row)
        return _to_response(row)


@router.get("/{client_id}", response_model=ClientResponse, summary="Detalha cliente")
async def get_client(
    client_id: int,
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> ClientResponse:
    sess = _require_session(session)
    async with sf() as db:
        row = (
            await db.execute(
                select(Client).where(
                    Client.id == client_id, Client.owner_user_id == sess.user_id
                )
            )
        ).scalar_one_or_none()
        if row is None:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        return _to_response(row)


@router.put("/{client_id}", response_model=ClientResponse, summary="Atualiza cliente")
async def update_client(
    client_id: int,
    payload: ClientRequest,
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> ClientResponse:
    sess = _require_session(session)
    async with sf() as db, db.begin():
        row = (
            await db.execute(
                select(Client).where(
                    Client.id == client_id, Client.owner_user_id == sess.user_id
                )
            )
        ).scalar_one_or_none()
        if row is None:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        # tax_id e owner são imutáveis.
        row.name = payload.name
        row.address = payload.address
        row.country_code = payload.country_code
        return _to_response(row)


@router.post("/{client_id}/deactivate", summary="Inativa cliente")
async def deactivate_client(
    client_id: int,
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> dict[str, str]:
    return await _set_status(client_id, session, sf, "inactive")


@router.post("/{client_id}/activate", summary="Reativa cliente")
async def activate_client(
    client_id: int,
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> dict[str, str]:
    return await _set_status(client_id, session, sf, "active")


async def _set_status(
    client_id: int,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession],
    status_value: str,
) -> dict[str, str]:
    sess = _require_session(session)
    async with sf() as db, db.begin():
        row = (
            await db.execute(
                select(Client).where(
                    Client.id == client_id, Client.owner_user_id == sess.user_id
                )
            )
        ).scalar_one_or_none()
        if row is None:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")
        row.status = status_value
    return {"message": f"Cliente {'reativado' if status_value == 'active' else 'inativado'}."}


def _to_response(row: Client) -> ClientResponse:
    return ClientResponse(
        id=row.id,
        name=row.name,
        tax_id=row.tax_id_digits,
        tax_id_type=row.tax_id_type,
        email=row.email,
        phone=row.phone,
        address=row.address,
        country_code=row.country_code,
        status=row.status,
    )
