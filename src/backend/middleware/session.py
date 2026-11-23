"""Extração e validação de sessão a partir do cookie (spec-004 §6; SPEC-017).

A sessão é um token opaco de 32 bytes armazenado como hash SHA-256(pepper) na
tabela ``user_sessions``. Não há JWT: o servidor é a única fonte de verdade e a
revogação é imediata (logout, outro login, exclusão de conta, dormência).
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.models.user import User, UserSession, UserStatus

# Cookie de sessão (HttpOnly, Secure, SameSite=Lax; sliding 24h).
SESSION_COOKIE_NAME: str = "session"
_SESSION_TTL: timedelta = timedelta(hours=24)


@dataclass(frozen=True, slots=True)
class SessionData:
    """Dados da sessão válida, sem PII."""

    user_id: int
    session_id: int


def _token_hash(token: str, pepper: str) -> str:
    """Hash SHA-256 do token com pepper; nunca guarda o token puro."""

    return hashlib.sha256((token + pepper).encode()).hexdigest()


async def get_current_session(
    request,
    session_factory: async_sessionmaker[AsyncSession],
    pepper: str,
) -> SessionData | None:
    """Extrai e valida a sessão do cookie; retorna ``SessionData`` ou ``None``.

    Aplica sliding expiration: ao validar, atualiza ``last_seen_at``. A sessão
    expira após 24h sem atividade e é revogada em logout/exclusão/dormência.

    Args:
        request: Requisição FastAPI (tem ``cookies``).
        session_factory: Fábrica de sessões do SQLAlchemy.
        pepper: Secreto de HMAC (do ``Settings.login_pepper``).

    Returns:
        ``SessionData(user_id, session_id)`` se a sessão for válida e o usuário
        estiver ``ACTIVE``, senão ``None``.
    """

    token = request.cookies.get(SESSION_COOKIE_NAME)
    if not token:
        return None

    token_hash = _token_hash(token, pepper)
    now = datetime.now(timezone.utc)

    async with session_factory() as session, session.begin():
        row = (
            await session.execute(
                select(UserSession, User.status)
                .join(User, User.id == UserSession.user_id)
                .where(
                    UserSession.token_hash == token_hash,
                    UserSession.revoked_at.is_(None),
                    UserSession.expires_at > now,
                    User.status == UserStatus.ACTIVE,
                )
            )
        ).first()
        if row is None:
            return None
        user_session, user_status = row
        # Sliding expiration: estende last_seen_at e expires_at.
        user_session.last_seen_at = now
        user_session.expires_at = now + _SESSION_TTL
        return SessionData(user_id=user_session.user_id, session_id=user_session.id)


async def revoke_user_sessions(
    session_factory: async_sessionmaker[AsyncSession],
    user_id: int,
) -> int:
    """Revoga todas as sessões ativas de um usuário.

    Usado quando o usuário entra em dormência, é excluído ou altera a senha.

    Args:
        session_factory: Fábrica de sessões do SQLAlchemy.
        user_id: ID do usuário cujas sessões serão revogadas.

    Returns:
        Número de sessões revogadas.
    """
    now = datetime.now(timezone.utc)
    async with session_factory() as session, session.begin():
        result = await session.execute(
            update(UserSession)
            .where(
                UserSession.user_id == user_id,
                UserSession.revoked_at.is_(None),
            )
            .values(revoked_at=now)
        )
        return result.rowcount
