"""Rotas de ciclo de vida da conta (spec-004 4.7; SPEC-022).

- DELETE /v1/account    exclusao definitiva (agenda erase, LGPD art. 18)
- POST /v1/account/reactivate  reativacao de conta dormente

Isolamento por proprietario (P-14): opera sobre o usuario da sessao.
"""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.middleware.rate_limit import limiter
from src.backend.routers.common import (
    CurrentSession,
    SessionFactoryDep,
    get_session_factory,
)
from src.backend.models.account_lifecycle import AccountLifecycleEvent, LifecycleEventType
from src.backend.models.user import User, UserLoginIdentifier, UserSession, UserStatus
from src.backend.models.client import Client
from src.backend.models.simulation import Simulation
from src.backend.models.invoice import Invoice
from src.backend.models.provider import ProviderProfile, ProviderCnpj
from src.backend.schemas.auth import ReactivateRequest

router = APIRouter(prefix="/v1/account", tags=["conta"])


async def _session_factory(request: Request) -> async_sessionmaker[AsyncSession]:
    return get_session_factory(request)


def _require_session(session: CurrentSession):
    if session is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nao autenticado",
            headers={"WWW-Authenticate": "Cookie"},
        )
    return session


@limiter.limit("5/minute")
@router.delete("", status_code=status.HTTP_204_NO_CONTENT, summary="Exclusao definitiva da conta (erase LGPD)")
async def delete_account(
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> Response:
    """Exclui conta com anonimizacao LGPD-compliant e retencao de 5 anos + 6 meses.

    - Anonimiza identificadores pessoais (NULL/valores unicos compativeis com indices)
    - Aposenta identificadores de login (retired_at)
    - Soft delete de dados relacionados com retencao 5 anos + 6 meses
    - Auditoria completa sem PII
    - Captura from_status ANTES da mudanca
    """

    sess = _require_session(session)
    now = datetime.now(timezone.utc)
    async with sf() as db, db.begin():
        user = (
            await db.execute(select(User).where(User.id == sess.user_id))
        ).scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404, detail="Usuario nao encontrado")
        if user.status == UserStatus.DELETED:
            raise HTTPException(status_code=409, detail="Conta ja excluida")

        # Capturar from_status ANTES de qualquer mudanca
        from_status = user.status

        # 1. Anonimizar identificadores pessoais (NULL compativel com indices parciais)
        user.email = None
        user.cpf = None
        user.name = "excluido"
        user.internal_username_hash = f"deleted-{now.timestamp()}-{user.id}"
        user.password_hash = ""
        user.status = UserStatus.DELETED

        # 2. Aposentar identificadores de login
        await db.execute(
            update(UserLoginIdentifier)
            .where(
                UserLoginIdentifier.user_id == sess.user_id,
                UserLoginIdentifier.retired_at.is_(None),
            )
            .values(retired_at=now)
        )

        # 3. Revogar todas as sessoes
        await db.execute(
            update(UserSession)
            .where(UserSession.user_id == sess.user_id, UserSession.revoked_at.is_(None))
            .values(revoked_at=now)
        )

        # 4. Soft delete dados relacionados (retencao 5 anos + 6 meses)
        # Clients: marcar como inactive (status so aceita active/inactive), manter dados para retencao fiscal
        await db.execute(
            update(Client)
            .where(Client.owner_user_id == sess.user_id)
            .values(
                status="inactive",
                deleted_at=now,
                # Dados mantidos para retencao 5a+6m
            )
        )

        # Simulations: marcar como deleted (soft delete via deleted_at only)
        await db.execute(
            update(Simulation)
            .where(Simulation.owner_user_id == sess.user_id)
            .values(deleted_at=now)
        )

        # Invoices: finalizadas nao mudam (imutaveis, retencao 5a+6m)
        # Drafts: soft delete via deleted_at only (status so aceita draft/finalized)
        await db.execute(
            update(Invoice)
            .where(Invoice.owner_user_id == sess.user_id, Invoice.status == "draft")
            .values(deleted_at=now)
        )

        # Provider profile: marcar como deleted, anonimizar dados bancarios
        await db.execute(
            update(ProviderProfile)
            .where(ProviderProfile.user_id == sess.user_id)
            .values(
                legal_name="excluido",
                category="mei",
                cnpj=None,
                deleted_at=now,
            )
        )

        # Provider CNPJs: marcar como inactive
        await db.execute(
            update(ProviderCnpj)
            .where(ProviderCnpj.user_id == sess.user_id, ProviderCnpj.status == "active")
            .values(
                status="inactive",
                deleted_at=now,
            )
        )

        # 5. Auditoria completa (from_status capturado ANTES)
        db.add(
            AccountLifecycleEvent(
                user_id=sess.user_id,
                event_type=LifecycleEventType.DELETED,
                from_status=from_status,
                to_status=UserStatus.DELETED,
            )
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@limiter.limit("5/minute")
@router.post(
    "/reactivate",
    summary="Reativacao de conta dormente (publica: identificador + senha)",
)
async def reactivate_account(
    payload: ReactivateRequest,
    request: Request,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> dict[str, str]:
    """Reativa uma conta dormente para ``active`` usando identificador + senha.

    Endpoint publico (sem sessao), mesmo rate limit do login.
    """
    from src.backend.routers.auth import _normalize_identifier, _find_login_identifier, _verify_password
    from src.backend.config import get_settings

    normalized, kind = _normalize_identifier(payload.identifier)
    pepper = get_settings().login_pepper

    async with sf() as db, db.begin():
        row, _ = await _find_login_identifier(db, kind, normalized, pepper)
        if row is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais invalidas.",
            )
        user = (
            await db.execute(select(User).where(User.id == row.user_id))
        ).scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404, detail="Usuario nao encontrado")
        if not _verify_password(payload.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais invalidas.",
            )
        if user.status != UserStatus.DORMANT:
            raise HTTPException(status_code=409, detail="Conta nao esta dormente")
        user.status = UserStatus.ACTIVE
        user.dormant_since = None
        db.add(
            AccountLifecycleEvent(
                user_id=user.id,
                event_type=LifecycleEventType.REACTIVATED,
                from_status=UserStatus.DORMANT,
                to_status=UserStatus.ACTIVE,
            )
        )
    return {"message": "Conta reativada."}
