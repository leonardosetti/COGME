"""Testes unitários de services/rate_providers.py (spec backend-mvp-v1, §4; REQ-01).

Sem rede: cada teste usa httpx.MockTransport com respostas gravadas à mão.
Payloads sintéticos, no formato real das APIs (Frankfurter e PTAX/BCB OData).
"""

from __future__ import annotations

import re
from collections.abc import Callable
from datetime import UTC, date, datetime, timedelta
from decimal import Decimal

import httpx
import pytest

from src.backend.services.rate_providers import (
    FrankfurterProvider,
    PtaxProvider,
    ProviderError,
)
from src.shared.schemas import Currency, RateSource

TODAY = date(2026, 10, 30)
TIMEOUT = 0.9
FRANKFURTER_OK = '{"amount":1.0,"base":"USD","date":"2026-10-30","rates":{"BRL":5.4325}}'
PTAX_OK = (
    '{"value":[{"paridadeCompra":1.00000,"paridadeVenda":1.00000,'
    '"cotacaoCompra":5.42060,"cotacaoVenda":5.42120,'
    '"dataHoraCotacao":"2026-10-30 13:04:18.706316","tipoBoletim":"Fechamento"}]}'
)


def _frankfurter_body(brl: str) -> str:
    """Monta o corpo Frankfurter com o valor de BRL informado como texto JSON literal.

    Args:
        brl: Valor literal de BRL (aceita NaN e Infinity para o teste de recusa).

    Returns:
        Corpo JSON bruto.
    """
    return '{"amount":1.0,"base":"USD","date":"2026-10-30","rates":{"BRL":%s}}' % brl


def _ptax_body(compra: str, venda: str = "5.42120") -> str:
    """Monta o corpo PTAX com os valores informados como texto JSON literal.

    Args:
        compra: Valor literal de cotacaoCompra.
        venda: Valor literal de cotacaoVenda.

    Returns:
        Corpo JSON bruto.
    """
    return (
        '{"value":[{"paridadeCompra":1.00000,"paridadeVenda":1.00000,'
        '"cotacaoCompra":%s,"cotacaoVenda":%s,'
        '"dataHoraCotacao":"2026-10-30 13:04:18.706316","tipoBoletim":"Fechamento"}]}'
    ) % (compra, venda)


def _client(
    body: str = "",
    *,
    status: int = 200,
    exc: Exception | None = None,
    seen: list[httpx.Request] | None = None,
) -> httpx.AsyncClient:
    """Cria um cliente HTTP falso que responde ao que o teste pediu.

    Args:
        body: Corpo bruto da resposta.
        status: Status HTTP da resposta.
        exc: Exceção a levantar no lugar da resposta, se houver.
        seen: Lista que recebe cada requisição feita, para inspeção.

    Returns:
        AsyncClient apoiado em MockTransport, sem rede.
    """

    def handler(request: httpx.Request) -> httpx.Response:
        if seen is not None:
            seen.append(request)
        if exc is not None:
            raise exc
        return httpx.Response(status, content=body.encode("utf-8"))

    return httpx.AsyncClient(transport=httpx.MockTransport(handler))


def _ptax(client: httpx.AsyncClient) -> PtaxProvider:
    """Instancia o provedor PTAX com data de hoje fixa.

    Args:
        client: Cliente HTTP falso.

    Returns:
        PtaxProvider pronto para uso.
    """
    return PtaxProvider(client, TIMEOUT, today=lambda: TODAY)


def _frankfurter(client: httpx.AsyncClient) -> FrankfurterProvider:
    """Instancia o provedor Frankfurter.

    Args:
        client: Cliente HTTP falso.

    Returns:
        FrankfurterProvider pronto para uso.
    """
    return FrankfurterProvider(client, TIMEOUT)


def _param(request: httpx.Request, name: str) -> str:
    """Lê um parâmetro OData da query, sem as aspas do literal.

    Args:
        request: Requisição capturada.
        name: Nome do parâmetro, com o arroba quando for OData.

    Returns:
        Valor do parâmetro sem aspas simples.
    """
    return request.url.params[name].strip("'")


async def test_frankfurter_parses_latest_rate_req01() -> None:
    """Frankfurter: taxa BRL, fonte, meia-noite UTC da data e boletim nulo (§4)."""
    seen: list[httpx.Request] = []
    async with _client(FRANKFURTER_OK, seen=seen) as client:
        quote = await _frankfurter(client).fetch(Currency.USD)
    assert quote.rate == Decimal("5.432500")
    assert quote.source == RateSource.FRANKFURTER
    assert quote.quoted_at == datetime(2026, 10, 30, tzinfo=UTC)
    assert quote.bulletin is None
    assert quote.stale is False
    assert quote.currency == Currency.USD


async def test_frankfurter_request_targets_latest_endpoint_with_timeout() -> None:
    """Frankfurter: URL de /v1/latest com base e symbols, e timeout de 0,9 s (§4)."""
    seen: list[httpx.Request] = []
    async with _client(FRANKFURTER_OK, seen=seen) as client:
        await _frankfurter(client).fetch(Currency.USD)
    request = seen[0]
    assert request.url.host == "api.frankfurter.dev"
    assert request.url.path == "/v1/latest"
    assert request.url.params["base"] == "USD"
    assert request.url.params["symbols"] == "BRL"
    assert request.extensions["timeout"]["read"] == TIMEOUT


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("5.432501", "5.432501"), ("5.43250049", "5.432500"), ("5.4325", "5.432500")],
)
async def test_rate_is_exact_decimal_quantized_to_six_places(raw: str, expected: str) -> None:
    """Taxa vem como Decimal exato, quantizada a 6 casas antes de montar a cotação (§4, §8.1)."""
    async with _client(_frankfurter_body(raw)) as client:
        quote = await _frankfurter(client).fetch(Currency.USD)
    assert str(quote.rate) == expected
    assert quote.rate == Decimal(expected)


async def test_ptax_uses_buy_quote_not_sell_quote_req01() -> None:
    """PTAX: usa cotacaoCompra (5,42060) e não cotacaoVenda (5,42120) (§4)."""
    async with _client(PTAX_OK) as client:
        quote = await _ptax(client).fetch(Currency.USD)
    assert quote.rate == Decimal("5.420600")
    assert quote.rate != Decimal("5.42120")
    assert quote.source == RateSource.PTAX
    assert quote.bulletin == "Fechamento"
    assert quote.stale is False


async def test_ptax_converts_brasilia_time_to_utc_req01() -> None:
    """PTAX: 13:04:18 em Brasília (UTC−3) vira 16:04:18 UTC, microssegundos preservados (§4)."""
    async with _client(PTAX_OK) as client:
        quote = await _ptax(client).fetch(Currency.USD)
    assert quote.quoted_at == datetime(2026, 10, 30, 16, 4, 18, 706316, tzinfo=UTC)
    assert quote.quoted_at.utcoffset() == timedelta(0)


async def test_ptax_query_window_is_seven_days_in_mm_dd_yyyy() -> None:
    """PTAX: janela de 7 dias, datas MM-DD-YYYY, USD, top 1 ordenado por data desc (§4)."""
    seen: list[httpx.Request] = []
    async with _client(PTAX_OK, seen=seen) as client:
        await _ptax(client).fetch(Currency.USD)
    request = seen[0]
    assert _param(request, "@moeda") == "USD"
    initial_raw = _param(request, "@dataInicial")
    final_raw = _param(request, "@dataFinalCotacao")
    assert re.fullmatch(r"\d{2}-\d{2}-\d{4}", initial_raw)
    assert re.fullmatch(r"\d{2}-\d{2}-\d{4}", final_raw)
    initial = datetime.strptime(initial_raw, "%m-%d-%Y").date()
    final = datetime.strptime(final_raw, "%m-%d-%Y").date()
    assert final == TODAY
    assert final - initial == timedelta(days=7)
    assert request.url.params["$top"] == "1"
    assert request.url.params["$format"] == "json"
    assert "dataHoraCotacao desc" in request.url.params["$orderby"]


async def test_ptax_query_encodes_spaces_as_percent_20_req01() -> None:
    """PTAX: a query sai com %20 em $orderby e nunca com +, que a API real recusa (HTTP 400, §4).

    Lê a query crua: ``request.url.params`` já decodificaria o ``+`` e esconderia o defeito.
    """
    seen: list[httpx.Request] = []
    async with _client(PTAX_OK, seen=seen) as client:
        await _ptax(client).fetch(Currency.USD)
    raw_query = seen[0].url.query
    assert b"%24orderby=dataHoraCotacao%20desc" in raw_query
    assert b"+" not in raw_query


async def test_ptax_request_timeout_is_provider_timeout() -> None:
    """PTAX: o timeout do provedor (0,9 s, §4) vale para a requisição."""
    seen: list[httpx.Request] = []
    async with _client(PTAX_OK, seen=seen) as client:
        await _ptax(client).fetch(Currency.USD)
    assert seen[0].extensions["timeout"]["read"] == TIMEOUT


@pytest.mark.parametrize("brl", ["0.000001", "999.999999"])
async def test_frankfurter_accepts_rate_at_acceptance_edges(brl: str) -> None:
    """Aceite: 0 < rate < 1000; os dois extremos internos são aceitos (§4)."""
    async with _client(_frankfurter_body(brl)) as client:
        quote = await _frankfurter(client).fetch(Currency.USD)
    assert quote.rate == Decimal(brl)


@pytest.mark.parametrize("brl", ["0", "-5.4", "1000", "1000.5", "NaN", "Infinity", "-Infinity"])
async def test_frankfurter_rejects_rate_outside_acceptance_req01(brl: str) -> None:
    """Fora de 0 < rate < 1000, ou não finito, vira ProviderError (§4)."""
    async with _client(_frankfurter_body(brl)) as client:
        with pytest.raises(ProviderError):
            await _frankfurter(client).fetch(Currency.USD)


@pytest.mark.parametrize("compra", ["0", "-5.4", "1000", "NaN", "Infinity"])
async def test_ptax_rejects_rate_outside_acceptance_req01(compra: str) -> None:
    """PTAX: mesma regra de aceite, aplicada a cotacaoCompra (§4)."""
    async with _client(_ptax_body(compra)) as client:
        with pytest.raises(ProviderError):
            await _ptax(client).fetch(Currency.USD)


async def test_ptax_empty_value_window_is_source_failure() -> None:
    """PTAX: `value` vazio (janela sem linhas) é falha da fonte (§4)."""
    async with _client('{"value":[]}') as client:
        with pytest.raises(ProviderError):
            await _ptax(client).fetch(Currency.USD)


@pytest.mark.parametrize(
    "body",
    [
        '{"value":[{"dataHoraCotacao":"2026-10-30 13:04:18.706316","cotacaoVenda":5.42120}]}',
        '{"value":[{"cotacaoCompra":5.42060,"cotacaoVenda":5.42120}]}',
    ],
    ids=["sem_cotacaoCompra", "sem_dataHoraCotacao"],
)
async def test_ptax_missing_field_is_provider_error(body: str) -> None:
    """PTAX: campo obrigatório ausente vira ProviderError (§4)."""
    async with _client(body) as client:
        with pytest.raises(ProviderError):
            await _ptax(client).fetch(Currency.USD)


async def test_frankfurter_missing_rates_key_is_provider_error() -> None:
    """Frankfurter: payload sem `rates` ou sem BRL vira ProviderError (§4)."""
    async with _client('{"amount":1.0,"base":"USD","date":"2026-10-30"}') as client:
        with pytest.raises(ProviderError):
            await _frankfurter(client).fetch(Currency.USD)
    async with _client('{"rates":{"EUR":0.9}}') as client:
        with pytest.raises(ProviderError):
            await _frankfurter(client).fetch(Currency.USD)


SOURCE_FAILURES: dict[str, dict[str, object]] = {
    "http_500": {"status": 500, "body": "{}"},
    "timeout": {"exc": httpx.ReadTimeout("tempo esgotado")},
    "connect_error": {"exc": httpx.ConnectError("sem conexão")},
    "invalid_json": {"body": '{"rates":'},
}


@pytest.mark.parametrize("factory", [_frankfurter, _ptax], ids=["frankfurter", "ptax"])
@pytest.mark.parametrize("failure", list(SOURCE_FAILURES))
async def test_source_failures_become_provider_error_req01(
    factory: Callable[[httpx.AsyncClient], FrankfurterProvider | PtaxProvider],
    failure: str,
) -> None:
    """HTTP 500, timeout, falha de conexão e JSON inválido viram ProviderError (§8.1)."""
    async with _client(**SOURCE_FAILURES[failure]) as client:
        with pytest.raises(ProviderError):
            await factory(client).fetch(Currency.USD)
