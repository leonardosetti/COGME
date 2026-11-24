"""Testes de unidade para src/backend/middleware/session.py."""
from __future__ import annotations

from src.backend.middleware.session import SESSION_COOKIE_NAME, SessionData


def test_session_cookie_name() -> None:
    assert SESSION_COOKIE_NAME == "session"


def test_session_data_fields() -> None:
    sd = SessionData(user_id=1, session_id=2)
    assert sd.user_id == 1
    assert sd.session_id == 2
