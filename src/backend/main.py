"""Aplicação FastAPI do COGME: lifespan, rotas e tratadores de erro (spec backend-mvp-v1, §3, §8).

``create_app`` não lê ``Settings`` nem o ambiente: quem lê é o ``lifespan``, na subida. Assim
os testes constroem a aplicação sem variáveis de ambiente. Todo erro sai no modelo canônico
(``ErrorResponse``), com mensagens em PT-BR que nunca repetem o que o cliente enviou.
Não há CORS: o frontend é servido na mesma origem.
"""

from __future__ import annotations

import logging
from collections.abc import AsyncIterator, Sequence
from contextlib import asynccontextmanager
from typing import Any, Final, get_args

import httpx
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic_core import core_schema
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import ClientDisconnect
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from src.backend.config import get_settings
from src.backend.errors import DomainError
from src.backend.models.database import create_engine, create_session_factory
from src.backend.models.repository import SqlAlchemyQuoteRepository
from src.backend.routers import health, invoices, rates, simulations
from src.backend.services.circuit_breaker import CircuitBreaker
from src.backend.services.rate_providers import FrankfurterProvider, PtaxProvider
from src.backend.services.rate_service import RateService
from src.shared.schemas import ErrorBody, ErrorDetail, ErrorKey, ErrorResponse

logger = logging.getLogger(__name__)

_USER_AGENT: Final[str] = "cogme-backend"
_VALIDATION_MESSAGE: Final[str] = "Dados inválidos."
_BODY_FIELD: Final[str] = "body"
_GENERIC_FIELD_MESSAGE: Final[str] = "Valor inválido."

# Mensagens PT-BR dos erros nativos da Pydantic, por ``type``. Só o tipo é lido: ``input`` e
# ``ctx`` trazem o valor enviado e nunca são usados.
_NATIVE_MESSAGES: Final[dict[str, str]] = {
    "missing": "Campo obrigatório.",
    "extra_forbidden": "Campo não permitido.",
    "enum": "Valor não permitido para este campo.",
    "literal_error": "Valor não permitido para este campo.",
    "string_type": "Informe um texto.",
    "string_too_long": "Texto acima do tamanho máximo permitido.",
    "string_too_short": "Texto curto demais; preencha o campo.",
    "date_type": "Informe uma data no formato AAAA-MM-DD.",
    "date_parsing": "Informe uma data válida no formato AAAA-MM-DD.",
    "date_from_datetime_parsing": "Informe uma data válida no formato AAAA-MM-DD.",
    "date_from_datetime_inexact": "Informe somente a data, no formato AAAA-MM-DD.",
    "datetime_type": "Informe uma data e hora válidas.",
    "datetime_parsing": "Informe uma data e hora válidas.",
    "decimal_type": "Informe um número decimal válido.",
    "decimal_parsing": "Informe um número decimal válido.",
    "decimal_max_places": "Número de casas decimais acima do permitido.",
    "decimal_max_digits": "Número com dígitos demais.",
    "decimal_whole_digits": "Número com dígitos demais.",
    "int_type": "Informe um número inteiro.",
    "int_parsing": "Informe um número inteiro.",
    "float_type": "Informe um número válido.",
    "float_parsing": "Informe um número válido.",
    "bool_type": "Informe verdadeiro ou falso.",
    "bool_parsing": "Informe verdadeiro ou falso.",
    "none_required": "Este campo deve ficar vazio.",
    "json_invalid": "JSON inválido.",
    "json_type": "JSON inválido.",
    "model_type": "Informe um objeto JSON.",
    "model_attributes_type": "Envie um objeto JSON com Content-Type application/json.",
    "dict_type": "Informe um objeto JSON.",
    "list_type": "Informe uma lista.",
    "too_long": "Lista longa demais.",
    "too_short": "Lista curta demais.",
}
# Erros em que a chave enviada pode estar no ``loc``: o campo não ecoa o que o cliente mandou.
_ECHOING_LOC_TYPES: Final[frozenset[str]] = frozenset({"extra_forbidden", "json_invalid"})
# Tipos que a Pydantic define. Os demais vêm de ``PydanticCustomError`` do schema, cuja
# mensagem já está em PT-BR e é preservada.
_NATIVE_TYPES: Final[frozenset[str]] = frozenset(get_args(core_schema.ErrorType))

_NOT_FOUND_MESSAGE: Final[str] = "Recurso não encontrado."
_METHOD_NOT_ALLOWED_MESSAGE: Final[str] = "Método não permitido para este recurso."
_INTERNAL_ERROR_MESSAGE: Final[str] = "Erro interno. Tente novamente mais tarde."


def _error_response(
    key: ErrorKey | str,
    message: str,
    status_code: int,
    details: Sequence[ErrorDetail] = (),
    headers: dict[str, str] | None = None,
) -> JSONResponse:
    """Monta a resposta no modelo canônico de erro.

    Args:
        key: Chave estável do erro.
        message: Mensagem em PT-BR, sem dados do usuário.
        status_code: Status HTTP.
        details: Campos inválidos.
        headers: Cabeçalhos extras, como ``Allow``.

    Returns:
        A resposta JSON.
    """
    body = ErrorResponse(
        error=ErrorBody(key=ErrorKey(key), message=message, details=list(details)),
    )
    return JSONResponse(
        status_code=status_code,
        content=body.model_dump(mode="json"),
        headers=headers,
    )


def _field_name(error_type: str, loc: Sequence[Any]) -> str:
    """Nomeia o campo de um erro de validação.

    Args:
        error_type: ``type`` do erro da Pydantic.
        loc: ``loc`` do erro, com o prefixo ``body`` quando vem do corpo.

    Returns:
        O caminho do campo, como ``simulation.amount``; ``body`` para o corpo inteiro e para
        chave extra, cujo nome vem do cliente e não deve ser ecoado.
    """
    if error_type in _ECHOING_LOC_TYPES:
        return _BODY_FIELD
    parts = [str(part) for part in loc]
    if parts and parts[0] == _BODY_FIELD:
        parts = parts[1:]
    return ".".join(parts) or _BODY_FIELD


def _message_for(error_type: str, custom_message: object) -> str:
    """Escolhe a mensagem PT-BR de um erro de validação.

    Args:
        error_type: ``type`` do erro da Pydantic.
        custom_message: ``msg`` do erro; só é usada quando o tipo é do schema do projeto.

    Returns:
        A mensagem traduzida, a do schema, ou o texto genérico.
    """
    translated = _NATIVE_MESSAGES.get(error_type)
    if translated is not None:
        return translated
    if error_type not in _NATIVE_TYPES and isinstance(custom_message, str):
        return custom_message
    return _GENERIC_FIELD_MESSAGE


def translate_validation_errors(errors: Sequence[Any]) -> list[ErrorDetail]:
    """Converte os erros da Pydantic em ``details`` do modelo canônico.

    Lê somente ``type``, ``loc`` e ``msg``; ``input`` e ``ctx`` são ignorados.

    Args:
        errors: Resultado de ``RequestValidationError.errors()``.

    Returns:
        Um ``ErrorDetail`` por erro, em PT-BR e sem o valor enviado.
    """
    details: list[ErrorDetail] = []
    for error in errors:
        error_type = str(error.get("type", ""))
        details.append(
            ErrorDetail(
                field=_field_name(error_type, error.get("loc", ())),
                message=_message_for(error_type, error.get("msg")),
            ),
        )
    return details


async def _handle_domain_error(_: Request, error: Exception) -> JSONResponse:
    """Responde uma falha de domínio com o status e a chave que ela carrega.

    Args:
        _: Requisição (não usada).
        error: Um ``DomainError``.

    Returns:
        A resposta canônica.
    """
    assert isinstance(error, DomainError)
    return _error_response(error.key, error.message, error.http_status)


async def _handle_validation_error(_: Request, error: Exception) -> JSONResponse:
    """Responde 400 ``validation_error`` no lugar do 422 do FastAPI.

    Args:
        _: Requisição (não usada).
        error: Um ``RequestValidationError``.

    Returns:
        A resposta canônica, com um detalhe por campo inválido.
    """
    assert isinstance(error, RequestValidationError)
    return _error_response(
        ErrorKey.VALIDATION_ERROR,
        _VALIDATION_MESSAGE,
        400,
        translate_validation_errors(error.errors()),
    )


async def _handle_http_error(_: Request, error: Exception) -> JSONResponse:
    """Traduz as exceções HTTP do Starlette para o modelo canônico.

    404 e 405 viram ``not_found``. Para 405 a chave ``validation_error`` seria semanticamente
    errada (a requisição está bem formada, o recurso é que não aceita o método), então a chave
    é ``not_found`` e o cabeçalho ``Allow`` é preservado. O 400 que o FastAPI levanta ao falhar
    ao ler o corpo vira ``validation_error``. Qualquer outro status é tratado como erro interno.

    Args:
        _: Requisição (não usada).
        error: Uma ``StarletteHTTPException``.

    Returns:
        A resposta canônica.
    """
    assert isinstance(error, StarletteHTTPException)
    if error.status_code == 404:
        return _error_response(ErrorKey.NOT_FOUND, _NOT_FOUND_MESSAGE, 404)
    if error.status_code == 405:
        allow = error.headers.get("Allow") if error.headers else None
        return _error_response(
            ErrorKey.NOT_FOUND,
            _METHOD_NOT_ALLOWED_MESSAGE,
            405,
            headers={"Allow": allow} if allow else None,
        )
    if error.status_code == 400:
        return _error_response(ErrorKey.VALIDATION_ERROR, _VALIDATION_MESSAGE, 400)
    return _error_response(ErrorKey.INTERNAL_ERROR, _INTERNAL_ERROR_MESSAGE, 500)


class InternalErrorMiddleware:
    """Converte qualquer exceção inesperada em 500 ``internal_error``, sem traceback.

    Usa um middleware em vez de ``add_exception_handler(Exception, ...)`` porque, nesse caso, o
    Starlette responde e levanta a exceção de novo, e o servidor despeja o traceback no log. Aqui
    a exceção é consumida e só o tipo dela e a rota vão para o log, nunca o corpo nem a mensagem.
    """

    def __init__(self, app: ASGIApp) -> None:
        """Guarda a aplicação embrulhada.

        Args:
            app: Aplicação ASGI interna.
        """
        self._app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """Repassa a chamada e responde 500 se algo inesperado escapar.

        Args:
            scope: Escopo ASGI.
            receive: Canal de entrada.
            send: Canal de saída.
        """
        if scope["type"] != "http":
            await self._app(scope, receive, send)
            return
        started = False

        async def tracking_send(message: Message) -> None:
            nonlocal started
            if message["type"] == "http.response.start":
                started = True
            await send(message)

        try:
            await self._app(scope, receive, tracking_send)
        except ClientDisconnect:
            # O cliente fechou o socket no meio do corpo: não é falha do servidor e não há a
            # quem responder. Só a rota vai para o log, sem corpo nem mensagem.
            route = getattr(scope.get("route"), "path", "-")
            logger.info("client_disconnect route=%s", route)
        except Exception as error:
            route = getattr(scope.get("route"), "path", "-")
            logger.error("unhandled_exception type=%s route=%s", type(error).__name__, route)
            if started:
                raise
            response = _error_response(ErrorKey.INTERNAL_ERROR, _INTERNAL_ERROR_MESSAGE, 500)
            await response(scope, receive, send)


def _configure_logging(level: str) -> None:
    """Ajusta o logging do projeto ao nível da configuração.

    Args:
        level: Nível padrão do ``logging`` (``INFO``, ``DEBUG`` ...).
    """
    logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s %(message)s")
    logging.getLogger("src").setLevel(level)


@asynccontextmanager
async def _lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Monta e desmonta os recursos do processo: engine, cliente HTTP e ``RateService``.

    Args:
        app: Aplicação que recebe ``app.state.rate_service``.

    Yields:
        Nada; a aplicação atende requisições enquanto o bloco está aberto.
    """
    settings = get_settings()
    _configure_logging(settings.log_level)
    engine = create_engine(settings.database_url)
    client = httpx.AsyncClient(follow_redirects=False, headers={"User-Agent": _USER_AGENT})
    try:
        timeout = settings.provider_timeout_seconds
        app.state.rate_service = RateService(
            repository=SqlAlchemyQuoteRepository(create_session_factory(engine)),
            providers=[
                (FrankfurterProvider(client, timeout), CircuitBreaker()),
                (PtaxProvider(client, timeout), CircuitBreaker()),
            ],
            ttl_seconds=settings.rate_ttl_seconds,
        )
        yield
    finally:
        await client.aclose()
        await engine.dispose()


def _build_openapi(app: FastAPI) -> dict[str, Any]:
    """Gera o OpenAPI sem o 422 que o FastAPI declara por padrão.

    A validação responde 400 com ``ErrorResponse``, então o 422 e seus schemas seriam ruído.

    Args:
        app: Aplicação a documentar.

    Returns:
        O documento OpenAPI, guardado em cache na aplicação.
    """
    if app.openapi_schema is None:
        schema = FastAPI.openapi(app)
        for path_item in schema.get("paths", {}).values():
            for operation in path_item.values():
                operation.get("responses", {}).pop("422", None)
        for name in ("HTTPValidationError", "ValidationError"):
            schema.get("components", {}).get("schemas", {}).pop(name, None)
        app.openapi_schema = schema
    return app.openapi_schema


def create_app() -> FastAPI:
    """Cria a aplicação, sem ler configuração nem abrir conexões (isso é do ``lifespan``).

    Returns:
        A aplicação FastAPI com rotas ``/v1`` e tratadores de erro.
    """
    app = FastAPI(
        title="COGME API",
        version="1.0.0",
        description="Simulador de recebimentos do exterior em BRL e gerador de invoice.",
        lifespan=_lifespan,
    )
    app.add_exception_handler(DomainError, _handle_domain_error)
    app.add_exception_handler(RequestValidationError, _handle_validation_error)
    app.add_exception_handler(StarletteHTTPException, _handle_http_error)
    app.add_middleware(InternalErrorMiddleware)
    for module in (health, rates, simulations, invoices):
        app.include_router(module.router)
    app.openapi = lambda: _build_openapi(app)  # type: ignore[method-assign]
    return app


app = create_app()
