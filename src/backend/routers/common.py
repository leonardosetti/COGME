"""Peças compartilhadas pelos routers: dependência do serviço, respostas de erro e leitura do corpo.

O ``json.loads`` padrão converte literais como ``30.1000000000000000000001`` em ``float`` antes
de o schema vê-los, e o valor chegaria arredondado. :class:`DecimalJsonRoute` troca a leitura do
corpo por uma que usa ``Decimal`` e impõe o limite de tamanho, sem mudar o OpenAPI: o corpo
continua declarado pelo schema do parâmetro.
"""

from __future__ import annotations

import json
from collections.abc import Callable, Coroutine
from decimal import Decimal
from typing import Annotated, Any, Final, NoReturn

from fastapi import Depends, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute

from src.backend.services.rate_service import RateService
from src.shared.schemas import ErrorResponse

MAX_BODY_BYTES: Final[int] = 64 * 1024

VALIDATION_ERROR_RESPONSE: Final[dict[int | str, dict[str, Any]]] = {
    400: {"model": ErrorResponse, "description": "Dados inválidos (validation_error)."},
}
RATES_UNAVAILABLE_RESPONSE: Final[dict[int | str, dict[str, Any]]] = {
    503: {
        "model": ErrorResponse,
        "description": "Cotação indisponível (rates_unavailable).",
    },
}
INTERNAL_ERROR_RESPONSE: Final[dict[int | str, dict[str, Any]]] = {
    500: {"model": ErrorResponse, "description": "Erro inesperado (internal_error)."},
}


def get_rate_service(request: Request) -> RateService:
    """Entrega o ``RateService`` montado no ``lifespan``.

    Args:
        request: Requisição corrente.

    Returns:
        O serviço guardado em ``app.state``.
    """
    rate_service: RateService = request.app.state.rate_service
    return rate_service


RateServiceDep = Annotated[RateService, Depends(get_rate_service)]


class BodyTooLargeError(Exception):
    """O corpo da requisição passou de :data:`MAX_BODY_BYTES`."""


def _refuse_constant(constant: str) -> NoReturn:
    """Recusa ``NaN``, ``Infinity`` e ``-Infinity`` no JSON.

    Args:
        constant: Literal encontrado; não é usado nem repetido.

    Raises:
        json.JSONDecodeError: Sempre.
    """
    raise json.JSONDecodeError("Constante numérica não permitida.", "", 0)


class DecimalJsonRequest(Request):
    """Requisição que lê o corpo com limite de tamanho e o JSON com ``Decimal``."""

    async def body(self) -> bytes:
        """Lê o corpo até :data:`MAX_BODY_BYTES`, sem guardar mais que isso na memória.

        Returns:
            O corpo completo.

        Raises:
            BodyTooLargeError: Se o corpo passar do limite.
        """
        if not hasattr(self, "_body"):
            declared = self.headers.get("content-length", "")
            if declared.isdecimal() and int(declared) > MAX_BODY_BYTES:
                raise BodyTooLargeError
            chunks: list[bytes] = []
            size = 0
            async for chunk in self.stream():
                size += len(chunk)
                if size > MAX_BODY_BYTES:
                    raise BodyTooLargeError
                chunks.append(chunk)
            self._body = b"".join(chunks)
        return self._body

    async def json(self) -> Any:
        """Interpreta o corpo como JSON, com decimais exatos.

        Returns:
            O valor JSON; números com ponto ou expoente chegam como ``Decimal``.

        Raises:
            json.JSONDecodeError: Se o JSON for inválido, usar ``NaN``/``Infinity``, tiver
                inteiro gigante ou aninhamento excessivo. O texto do corpo nunca é repetido.
        """
        if not hasattr(self, "_json"):
            body = await self.body()
            try:
                self._json = json.loads(
                    body,
                    parse_float=Decimal,
                    parse_constant=_refuse_constant,
                )
            except json.JSONDecodeError:
                raise
            except (ValueError, RecursionError):
                # Inteiro acima do limite de dígitos, UTF-8 inválido ou aninhamento profundo.
                raise json.JSONDecodeError("JSON inválido.", "", 0) from None
        return self._json


class DecimalJsonRoute(APIRoute):
    """Rota cujo corpo JSON é lido por :class:`DecimalJsonRequest`."""

    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        """Embrulha o tratador padrão do FastAPI com a leitura própria do corpo.

        Returns:
            O tratador da rota.
        """
        original = super().get_route_handler()

        async def handler(request: Request) -> Response:
            decimal_request = DecimalJsonRequest(request.scope, request.receive)
            try:
                await decimal_request.body()
            except BodyTooLargeError:
                raise RequestValidationError(
                    [
                        {
                            "type": "body_too_large",
                            "loc": ("body",),
                            "msg": "O corpo da requisição excede o limite de 64 KiB.",
                        },
                    ],
                ) from None
            return await original(decimal_request)

        return handler
