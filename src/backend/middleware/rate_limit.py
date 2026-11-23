"""Rate limiting (spec-004 §8; ADR-019 §7).

Limiter em memória por IP/identificador, exposto em ``app.state.limiter``.
Os endpoints de auth recebem limites mais rígidos (5/min login, 3/h reset).
"""

from __future__ import annotations

from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)


def rate_limit_exceeded_handler(request, exc):
    from starlette.responses import JSONResponse

    from src.shared.schemas import ErrorResponse

    body = ErrorResponse(
        error={
            "key": "auth_rate_limit_login",
            "message": "Muitas tentativas. Tente novamente mais tarde.",
            "details": [],
        }
    )
    return JSONResponse(
        status_code=429,
        content=body.model_dump(mode="json"),
    )
