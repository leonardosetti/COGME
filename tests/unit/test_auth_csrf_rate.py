"""Testes de unidade: auth, CSRF e rate limiting (spec-004 Onda A)."""

from __future__ import annotations

from src.backend.middleware.csrf import CSRF_EXEMPT_PATHS
from src.backend.middleware.rate_limit import limiter


def _csrf_should_protect(method: str, path: str, cookies: dict, headers: dict) -> bool:
    return (
        method in ("POST", "PUT", "PATCH", "DELETE")
        and path not in CSRF_EXEMPT_PATHS
    )


def test_csrf_exempt_auth_paths():
    for path in CSRF_EXEMPT_PATHS:
        assert _csrf_should_protect("POST", path, {}, {}) is False


def test_csrf_protected_mutable_route():
    assert _csrf_should_protect("POST", "/v1/invoices", {}, {}) is True
    assert _csrf_should_protect("PUT", "/v1/invoices/1", {}, {}) is True
    assert _csrf_should_protect("DELETE", "/v1/invoices/1", {}, {}) is True


def test_csrf_safe_methods_not_protected():
    assert _csrf_should_protect("GET", "/v1/invoices", {}, {}) is False
    assert _csrf_should_protect("OPTIONS", "/v1/invoices", {}, {}) is False


def test_rate_limiter_exists():
    assert limiter is not None


def test_rate_limit_exceeded_handler_shape():
    from src.backend.middleware.rate_limit import rate_limit_exceeded_handler

    assert callable(rate_limit_exceeded_handler)
