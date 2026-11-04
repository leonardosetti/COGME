"""Domain exceptions of the COGME backend.

This module depends only on the standard library, so the domain layer stays free of
FastAPI. The HTTP handlers in ``main.py`` translate these exceptions into the canonical
error model. Messages are fixed and in PT-BR: they never carry user data.
"""

from __future__ import annotations

from typing import Final

_HTTP_SERVICE_UNAVAILABLE: Final[int] = 503


class DomainError(Exception):
    """Base class for failures the API reports to its clients.

    Attributes:
        key: Stable machine-readable error key, in EN.
        message: User-facing message, in PT-BR, free of user data.
        http_status: HTTP status the handler must answer with.
    """

    def __init__(self, key: str, message: str, http_status: int) -> None:
        """Initialize the error.

        Args:
            key: Stable machine-readable error key, in EN.
            message: User-facing message, in PT-BR, free of user data.
            http_status: HTTP status the handler must answer with.
        """
        super().__init__(message)
        self.key = key
        self.message = message
        self.http_status = http_status


class RatesUnavailableError(DomainError):
    """No exchange rate source answered and the cache has no quote."""

    def __init__(self) -> None:
        """Initialize the error with its fixed key, message and status."""
        super().__init__(
            key="rates_unavailable",
            message="Cotação indisponível no momento. Tente novamente mais tarde.",
            http_status=_HTTP_SERVICE_UNAVAILABLE,
        )


class PdfUnavailableError(DomainError):
    """The PDF engine is missing or the rendering failed."""

    def __init__(self) -> None:
        """Initialize the error with its fixed key, message and status."""
        super().__init__(
            key="pdf_unavailable",
            message="Geração de PDF indisponível no momento. Tente novamente mais tarde.",
            http_status=_HTTP_SERVICE_UNAVAILABLE,
        )
