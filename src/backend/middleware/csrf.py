"""Proteção CSRF double-submit (spec-004 §7; ADR-019 §4.6).

Para métodos mutáveis (POST/PUT/PATCH/DELETE) fora dos endpoints de auth,
exige o cookie ``csrf_token`` igual ao header ``X-CSRF-Token``. Os endpoints
de auth estão isentos (login gera o cookie).
"""

from __future__ import annotations

import hmac
from typing import Callable

from fastapi import Request, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from starlette.types import ASGIApp, Message, Receive, Scope, Send

CSRF_EXEMPT_PATHS: frozenset[str] = frozenset(
    {
        "/v1/auth/register",
        "/v1/auth/login",
        "/v1/auth/logout",
        "/v1/auth/password/reset-request",
        "/v1/auth/password/reset-confirm",
        "/v1/simulate",
        "/v1/invoice",
    }
)
CSRF_COOKIE_NAME: str = "csrf_token"
CSRF_HEADER_NAME: str = "X-CSRF-Token"


def _generate_csrf_token() -> str:
    import secrets

    return secrets.token_urlsafe(32)


class CSRFMiddleware:
    """Middleware ASGI de proteção CSRF double-submit."""

    def __init__(self, app: ASGIApp) -> None:
        self._app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self._app(scope, receive, send)
            return

        request = Request(scope, receive)

        async def send_wrapper(message: Message) -> None:
            if message["type"] == "http.response.start":
                # Seta cookie CSRF se ainda não existe.
                if CSRF_COOKIE_NAME not in request.cookies:
                    headers = message.setdefault("headers", [])
                    headers.append(
                        (
                            b"set-cookie",
                            f"{CSRF_COOKIE_NAME}={_generate_csrf_token()}; "
                            "HttpOnly; Secure; SameSite=Lax; Path=/".encode(),
                        )
                    )
            await send(message)

        if request.method in ("POST", "PUT", "PATCH", "DELETE") and request.url.path not in CSRF_EXEMPT_PATHS:
            cookie_token = request.cookies.get(CSRF_COOKIE_NAME)
            header_token = request.headers.get(CSRF_HEADER_NAME)
            if not cookie_token or not header_token:
                await _json_error(send, 403, "AUTH_CSRF_MISSING", "CSRF token ausente.")
                return
            if not hmac.compare_digest(cookie_token, header_token):
                await _json_error(send, 403, "AUTH_CSRF_INVALID", "CSRF token inválido.")
                return

        await self._app(scope, receive, send_wrapper)


async def _json_error(send: Send, status: int, code: str, message: str) -> None:
    import json

    body = json.dumps({"error": {"key": code, "message": message, "details": []}}).encode()
    await send(
        {
            "type": "http.response.start",
            "status": status,
            "headers": [
                (b"content-type", b"application/json"),
                (b"content-length", str(len(body)).encode()),
            ],
        }
    )
    await send({"type": "http.response.body", "body": body})
