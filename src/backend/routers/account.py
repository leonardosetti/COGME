"""Rotas de ciclo de vida da conta (spec-004 §4.7; SPEC-022).

- DELETE /v1/account    exclusão definitiva (agenda erase, LGPD art. 18)
- POST /v1/account/reactivate  reativação de conta dormente

Isolamento por proprietário (P-14): opera sobre o usuário da sessão.
"""

from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.routers.common import (
    CurrentSession,
    SessionFactoryDep,
    get_session_factory,
)
from src.backend.models.account_lifecycle import AccountLifecycleEvent, LifecycleEventType
from src.backend.models.user import User, UserSession, UserStatus

router = APIRouter(prefix="/v1/account", tags=["conta"])


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


@router.delete("", status_code=status.HTTP_204_NO_CONTENT, summary="Exclusão definitiva da conta (erase LGPD)")
async def delete_account(
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> Response:
    """Marca a conta como excluída, revoga sessões e audita o evento (sem PII)."""

    sess = _require_session(session)
    now = datetime.now(timezone.utc)
    async with sf() as db, db.begin():
        user = (
            await db.execute(select(User).where(User.id == sess.user_id))
        ).scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        if user.status == UserStatus.DELETED:
            raise HTTPException(status_code=409, detail="Conta já excluída")
        user.status = UserStatus.DELETED
        # Anonimiza identificadores pessoais (direito ao esquecimento, sem PII).
        user.email = ""
        user.cpf = "00000000000"
        user.name = "excluído"
        user.internal_username_hash = ""
        user.password_hash = ""
        # Revoga todas as sessões.
        await db.execute(
            update(UserSession)
            .where(UserSession.user_id == sess.user_id, UserSession.revoked_at.is_(None))
            .values(revoked_at=now)
        )
        db.add(
            AccountLifecycleEvent(
                user_id=sess.user_id,
                event_type=LifecycleEventType.DELETED,
                from_status=user.status if user.status != UserStatus.DELETED else None,
                to_status=UserStatus.DELETED,
            )
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post(
    "/reactivate",
    summary="Reativação de conta dormente (reset + verificação)",
)
async def reactivate_account(
    request: Request,
    session: CurrentSession,
    sf: async_sessionmaker[AsyncSession] = Depends(_session_factory),
) -> dict[str, str]:
    """Reativa uma conta dormente para ``active``."""

    sess = _require_session(session)
    async with sf() as db, db.begin():
        user = (
            await db.execute(select(User).where(User.id == sess.user_id))
        ).scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        if user.status != UserStatus.DORMANT:
            raise HTTPException(status_code=409, detail="Conta não está dormente")
        user.status = UserStatus.ACTIVE
        user.dormant_since = None
        db.add(
            AccountLifecycleEvent(
                user_id=sess.user_id,
                event_type=LifecycleEventType.REACTIVATED,
                from_status=UserStatus.DORMANT,
                to_status=UserStatus.ACTIVE,
            )
        )
    return {"message": "Conta reativada."}
