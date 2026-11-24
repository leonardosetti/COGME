"""Testes de unidade para src/backend/middleware/authorization.py."""
from __future__ import annotations

from src.backend.middleware.authorization import require_owner


def test_require_owner_returns_callable() -> None:
    dep = require_owner("invoice")
    assert callable(dep)
    dep2 = require_owner("client", resource_id_param="client_id")
    assert callable(dep2)
