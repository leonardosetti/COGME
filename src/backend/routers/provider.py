"""Rotas de prestadora e contas bancárias (spec-004 §4.3; SPEC-018).

Todas exigem sessão e isolamento por proprietário (P-14): o repo filtra por
``user_id`` da sessão, então nunca devolve recurso de outro usuário (404).

Endpoints:
- GET /v1/provider/profile            perfil da prestadora
- PUT /v1/provider/profile            atualiza perfil (categoria imutável)
- GET /v1/provider/bank-accounts      lista contas bancárias
- POST /v1/provider/bank-accounts     cria conta (criptografar sensíveis no PG)
- PUT /v1/provider/bank-accounts/{id} atualiza conta
- DELETE /v1/provider/bank-accounts/{id} remove conta (não primária única)

shortcut: dados bancários gravados em texto simples até o pgcrypto (AES-256-GCM)
do ADR-010/ADR-018 estar disponível no container; então migrar campos sensíveis.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, status
from pydantic import BaseModel, Field
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.middleware.rate_limit import limiter
from src.backend.routers.common import (
    CurrentSession,
    SessionFactoryDep,
    get_session_factory,
)
from src.backend.models.provider import (
    ProviderBankAccount,
    ProviderCategory,
    ProviderProfile,
)

router = APIRouter(prefix="/v1/provider", tags=["prestadora"])


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


class ProviderProfileRequest(BaseModel):
    legal_name: str = Field(min_length=1, max_length=255)
    category: str = Field(pattern=r"^(mei|legal_entity)$")
    cnpj: str | None = Field(default=None, max_length=14)
    address: str | None = Field(default=None, max_length=500)
    city: str | None = Field(default=None, max_length=100)
    state: str | None = Field(default=None, max_length=2)
    postal_code: str | None = Field(default=None, max_length=8)
    country_code: str = Field(default="BR", max_length=2)


class ProviderProfileResponse(BaseModel):
    user_id: int
    legal_name: str
    category: str
    cnpj: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    postal_code: str | None = None
    country_code: str


class BankAccountRequest(BaseModel):
    account_type: str = Field(pattern=r"^(checking|savings|payment)$")
    bank_code: str = Field(pattern=r"^\d{3}$")
    bank_name: str = Field(min_length=1, max_length=100)
    branch: str = Field(min_length=1, max_length=10)
    account_number: str = Field(min_length=1, max_length=20)
    account_digit: str = Field(min_length=1, max_length=2)
    swift_bic: str | None = Field(default=None, max_length=11)
    iban: str | None = Field(default=None, max_length=34)
    account_holder: str = Field(min_length=1, max_length=255)
    currency: str = Field(default="BRL", max_length=3)
    is_primary: bool = False


class BankAccountResponse(BaseModel):
    id: int
    account_type: str
    bank_code: str
    bank_name: str
    branch: str
    account_number: str
    account_digit: str
    swift_bic: str | None = None
    iban: str | None = None
    account_holder: str
    currency: str
    is_primary: bool


# ── Profile ───────────────────────────────────────────────────────────


@router.get("/profile", response_model=ProviderProfileResponse, summary="Perfil da prestadora")
async def get_profile(
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> ProviderProfileResponse:
    sess = _require_session(session)
    async with sf() as db:
        row = (
            await db.execute(
                select(ProviderProfile).where(ProviderProfile.user_id == sess.user_id)
            )
        ).scalar_one_or_none()
        if row is None:
            raise HTTPException(status_code=404, detail="Perfil não encontrado")
        return ProviderProfileResponse(
            user_id=row.user_id,
            legal_name=row.legal_name,
            category=row.category,
            cnpj=row.cnpj,
            address=row.address,
            city=row.city,
            state=row.state,
            postal_code=row.postal_code,
            country_code=row.country_code,
        )


@router.put("/profile", response_model=ProviderProfileResponse, summary="Atualiza perfil")
async def put_profile(
    payload: ProviderProfileRequest,
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> ProviderProfileResponse:
    sess = _require_session(session)
    async with sf() as db, db.begin():
        row = (
            await db.execute(
                select(ProviderProfile).where(ProviderProfile.user_id == sess.user_id)
            )
        ).scalar_one_or_none()
        if row is None:
            raise HTTPException(status_code=404, detail="Perfil não encontrado")
        # Categoria é imutável depois de definida.
        if row.category and row.category != payload.category:
            raise HTTPException(
                status_code=409, detail="Categoria da prestadora não pode ser alterada"
            )
        if payload.category == "legal_entity" and not payload.cnpj:
            raise HTTPException(
                status_code=400,
                detail="CNPJ obrigatório para categoria pessoa jurídica",
            )
        row.legal_name = payload.legal_name
        row.cnpj = payload.cnpj
        row.address = payload.address
        row.city = payload.city
        row.state = payload.state
        row.postal_code = payload.postal_code
        row.country_code = payload.country_code
        return ProviderProfileResponse(
            user_id=row.user_id,
            legal_name=row.legal_name,
            category=row.category,
            cnpj=row.cnpj,
            address=row.address,
            city=row.city,
            state=row.state,
            postal_code=row.postal_code,
            country_code=row.country_code,
        )


# ── Bank accounts ─────────────────────────────────────────────────────


@router.get(
    "/bank-accounts",
    response_model=list[BankAccountResponse],
    summary="Lista contas bancárias",
)
async def list_bank_accounts(
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> list[BankAccountResponse]:
    sess = _require_session(session)
    async with sf() as db:
        rows = (
            await db.execute(
                select(ProviderBankAccount).where(
                    ProviderBankAccount.user_id == sess.user_id
                )
            )
        ).scalars().all()
    return [BankAccountResponse(**{c.name: getattr(r, c.name) for c in r.__table__.columns}) for r in rows]


@router.post(
    "/bank-accounts",
    response_model=BankAccountResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria conta bancária",
)
@limiter.limit("20/minute")
async def create_bank_account(
    payload: BankAccountRequest,
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> BankAccountResponse:
    sess = _require_session(session)
    async with sf() as db, db.begin():
        row = ProviderBankAccount(
            user_id=sess.user_id,
            account_type=payload.account_type,
            bank_code=payload.bank_code,
            bank_name=payload.bank_name,
            branch=payload.branch,
            account_number=payload.account_number,
            account_digit=payload.account_digit,
            swift_bic=payload.swift_bic,
            iban=payload.iban,
            account_holder=payload.account_holder,
            currency=payload.currency,
            is_primary=payload.is_primary,
        )
        db.add(row)
        await db.flush()
        await db.refresh(row)
        return BankAccountResponse(**{c.name: getattr(row, c.name) for c in row.__table__.columns})


@router.put(
    "/bank-accounts/{account_id}",
    response_model=BankAccountResponse,
    summary="Atualiza conta bancária",
)
@limiter.limit("20/minute")
async def update_bank_account(
    account_id: int,
    payload: BankAccountRequest,
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> BankAccountResponse:
    sess = _require_session(session)
    async with sf() as db, db.begin():
        row = (
            await db.execute(
                select(ProviderBankAccount).where(
                    ProviderBankAccount.id == account_id,
                    ProviderBankAccount.user_id == sess.user_id,
                )
            )
        ).scalar_one_or_none()
        if row is None:
            raise HTTPException(status_code=404, detail="Conta não encontrada")
        row.account_type = payload.account_type
        row.bank_code = payload.bank_code
        row.bank_name = payload.bank_name
        row.branch = payload.branch
        row.account_number = payload.account_number
        row.account_digit = payload.account_digit
        row.swift_bic = payload.swift_bic
        row.iban = payload.iban
        row.account_holder = payload.account_holder
        row.currency = payload.currency
        row.is_primary = payload.is_primary
        return BankAccountResponse(**{c.name: getattr(row, c.name) for c in row.__table__.columns})


@router.delete(
    "/bank-accounts/{account_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remove conta bancária",
)
@limiter.limit("20/minute")
async def delete_bank_account(
    account_id: int,
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> Response:
    sess = _require_session(session)
    async with sf() as db, db.begin():
        row = (
            await db.execute(
                select(ProviderBankAccount).where(
                    ProviderBankAccount.id == account_id,
                    ProviderBankAccount.user_id == sess.user_id,
                )
            )
        ).scalar_one_or_none()
        if row is None:
            raise HTTPException(status_code=404, detail="Conta não encontrada")
        if row.is_primary:
            # Não permite remover a única conta primária.
            primary_count = (
                await db.execute(
                    select(ProviderBankAccount).where(
                        ProviderBankAccount.user_id == sess.user_id,
                        ProviderBankAccount.is_primary == True,  # noqa: E712
                    )
                )
            ).scalars().all()
            if len(primary_count) <= 1:
                raise HTTPException(
                    status_code=409, detail="Não é possível remover a conta primária única"
                )
        await db.execute(delete(ProviderBankAccount).where(ProviderBankAccount.id == account_id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
