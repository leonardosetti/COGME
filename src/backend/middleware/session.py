"""Extração e validação de sessão a partir do cookie (spec-004 §6; SPEC-017).

A sessão é um token opaco de 32 bytes armazenado como hash SHA-256(pepper) na
tabela ``user_sessions``. Não há JWT: o servidor é a única fonte de verdade e a
revogação é imediata (logout, outro login, exclusão de conta).
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.models.user import UserSession

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
    expira após 24h sem atividade e é revogada em logout/exclusão.

    Args:
        request: Requisição FastAPI (tem ``cookies``).
        session_factory: Fábrica de sessões do SQLAlchemy.
        pepper: Secreto de HMAC (do ``Settings.login_pepper``).

    Returns:
        ``SessionData(user_id, session_id)`` se a sessão for válida, senão ``None``.
    """

    token = request.cookies.get(SESSION_COOKIE_NAME)
    if not token:
        return None

    token_hash = _token_hash(token, pepper)
    now = datetime.now(timezone.utc)

    async with session_factory() as session, session.begin():
        row = (
            await session.execute(
                select(UserSession).where(
                    UserSession.token_hash == token_hash,
                    UserSession.revoked_at.is_(None),
                    UserSession.expires_at > now,
                )
            )
        ).scalar_one_or_none()
        if row is None:
            return None
        # Sliding expiration.
        row.last_seen_at = now
        return SessionData(user_id=row.user_id, session_id=row.id)
