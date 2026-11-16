"""Sessão, autorização e CSRF (spec-004 §6, §7; P-14, ADR-019)."""

from __future__ import annotations

from src.backend.middleware.authorization import (
    SessionData,
    get_current_session,
    require_owner,
)
from src.backend.middleware.session import SESSION_COOKIE_NAME
from src.backend.middleware.csrf import CSRFMiddleware

__all__ = [
    "SessionData",
    "get_current_session",
    "require_owner",
    "SESSION_COOKIE_NAME",
    "CSRFMiddleware",
]
