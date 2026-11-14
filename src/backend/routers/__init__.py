"""Roteadores da API v1."""

from __future__ import annotations

from src.backend.routers import health, invoices, rates, simulations

__all__ = [
    "health",
    "invoices",
    "rates",
    "simulations",
]