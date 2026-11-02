"""Provedores públicos de cotação: Frankfurter e PTAX (spec backend-mvp-v1, §4; REQ-01).

Todo conteúdo recebido é não confiável. Qualquer falha da fonte vira :class:`ProviderError`,
cuja mensagem é só um código ou o nome do tipo da falha, nunca URL, payload ou valor. Por isso
as exceções originais são descartadas com ``from None``.

Taxas nunca passam por ``float``: o JSON é lido com ``parse_float`` e ``parse_int`` em
``Decimal``.
"""

from __future__ import annotations

import asyncio
import json
from collections.abc import Callable, Mapping
from datetime import UTC, date, datetime, time, timedelta
from decimal import Decimal, InvalidOperation
from typing import Any, Final, NoReturn, Protocol
from urllib.parse import quote, urlencode
from zoneinfo import ZoneInfo

import httpx
from pydantic import ValidationError

from src.backend.services.calculator import q6
from src.shared.schemas import Currency, RateQuote, RateSource

_FRANKFURTER_URL: Final[str] = "https://api.frankfurter.dev/v1/latest"
_PTAX_URL: Final[str] = (
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
    "CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,"
    "dataFinalCotacao=@dataFinalCotacao)"
)

_BRASILIA: Final[ZoneInfo] = ZoneInfo("America/Sao_Paulo")
_PTAX_WINDOW: Final[timedelta] = timedelta(days=7)
_PTAX_DATE_FORMAT: Final[str] = "%m-%d-%Y"

_MAX_RATE: Final[Decimal] = Decimal("1000")
# Tamanho de fx_quotes.bulletin: boletim maior é falha da fonte, não erro no banco.
_MAX_BULLETIN_LENGTH: Final[int] = 40

_TRANSPORT_FAILURES: Final[tuple[type[Exception], ...]] = (httpx.HTTPError, TimeoutError)
# RecursionError: JSON aninhado demais. UnicodeDecodeError e JSONDecodeError são ValueError.
_DECODING_FAILURES: Final[tuple[type[Exception], ...]] = (
    InvalidOperation,
    RecursionError,
    ValueError,
)
# OverflowError: data no limite do calendário ao converter para UTC.
_PAYLOAD_FAILURES: Final[tuple[type[Exception], ...]] = (
    InvalidOperation,
    KeyError,
    OverflowError,
    TypeError,
    ValidationError,
    ValueError,
)


class ProviderError(Exception):
    """Falha de uma fonte de cotação, inclusive timeout e aceite reprovado.

    A mensagem é um código ou nome de tipo, seguro para log.
    """


class RateProvider(Protocol):
    """Fonte de cotação usada pelo ``RateService``.

    Attributes:
        name: Identificação da fonte.
    """

    name: RateSource

    async def fetch(self, currency: Currency) -> RateQuote:
        """Obtém a cotação atual da moeda.

        Args:
            currency: Moeda estrangeira.

        Returns:
            A cotação aprovada no aceite, com ``stale=False``.

        Raises:
            ProviderError: Em toda falha da fonte.
        """
        ...


def _reject_json_constant(name: str) -> NoReturn:
    """Recusa ``NaN``, ``Infinity`` e ``-Infinity``, que o ``json`` aceitaria.

    Args:
        name: Constante encontrada.

    Raises:
        ValueError: Sempre.
    """
    raise ValueError("Constante JSON não aceita.")


async def _get_json(
    client: httpx.AsyncClient,
    url: str,
    params: Mapping[str, str],
    timeout: float,
) -> Any:
    """Faz o GET e decodifica o JSON sem passar por ``float``.

    O ``timeout`` do httpx vale por fase e, na leitura, por bloco recebido. ``asyncio.timeout``
    limita a chamada inteira, para o orçamento do provedor valer de fato (§4).

    A query é montada aqui, com ``%20``, porque ``params`` do httpx codifica espaço como ``+``,
    que a PTAX não decodifica: ela recusa ``$orderby`` com HTTP 400.

    Args:
        client: Cliente HTTP compartilhado.
        url: Endereço da fonte.
        params: Parâmetros da query.
        timeout: Tempo máximo, em segundos.

    Returns:
        O corpo decodificado.

    Raises:
        ProviderError: Em falha de transporte, status fora de 2xx ou corpo que não é JSON.
    """
    target = f"{url}?{urlencode(params, quote_via=quote)}"
    try:
        async with asyncio.timeout(timeout):
            response = await client.get(target, timeout=timeout)
        response.raise_for_status()
    except _TRANSPORT_FAILURES as error:
        raise ProviderError(type(error).__name__) from None
    try:
        return json.loads(
            response.content,
            parse_float=Decimal,
            parse_int=Decimal,
            parse_constant=_reject_json_constant,
        )
    except _DECODING_FAILURES as error:
        raise ProviderError(type(error).__name__) from None


def _accept_rate(raw: object) -> Decimal:
    """Aplica o aceite da §4 sobre a taxa já na escala final.

    A checagem vem depois do arredondamento: ``999.9999999`` viraria ``1000.000000`` e
    ``0.0000001`` viraria zero, ambos fora do aceite.

    Args:
        raw: Valor lido do JSON.

    Returns:
        A taxa com 6 casas, finita e em ``0 < taxa < 1000``.

    Raises:
        ProviderError: Se o valor não for um decimal finito dentro do aceite.
        decimal.InvalidOperation: Se o valor for grande demais para arredondar.
    """
    if not isinstance(raw, Decimal) or not raw.is_finite():
        raise ProviderError("rate_rejected")
    rate = q6(raw)
    if not 0 < rate < _MAX_RATE:
        raise ProviderError("rate_rejected")
    return rate


def _accept_bulletin(raw: object) -> str:
    """Valida o boletim antes que ele chegue ao banco ou à invoice.

    Args:
        raw: Valor de ``tipoBoletim``.

    Returns:
        O boletim recebido.

    Raises:
        ProviderError: Se não for texto imprimível de até 40 caracteres.
    """
    if (
        not isinstance(raw, str)
        or len(raw.strip()) > _MAX_BULLETIN_LENGTH
        or not raw.isprintable()
    ):
        raise ProviderError("bulletin_rejected")
    return raw


def _brasilia_to_utc(raw: str) -> datetime:
    """Converte ``dataHoraCotacao``, em horário de Brasília, para UTC.

    Usa ``fromisoformat`` porque a fração de segundo aparece com menos de 6 dígitos.

    Args:
        raw: Data e hora sem fuso, como ``2026-10-30 13:04:18.706316``.

    Returns:
        O mesmo instante em UTC.

    Raises:
        ProviderError: Se o texto trouxer fuso, o que contraria o formato documentado.
        TypeError: Se o valor não for texto.
        ValueError: Se o texto não for uma data válida.
        OverflowError: Se a conversão sair do calendário.
    """
    local = datetime.fromisoformat(raw)
    if local.tzinfo is not None:
        raise ProviderError("timestamp_rejected")
    return local.replace(tzinfo=_BRASILIA).astimezone(UTC)


def _today_in_brasilia() -> date:
    """Devolve a data corrente em Brasília, referência dos boletins da PTAX.

    Returns:
        A data local de Brasília, independente do fuso do servidor.
    """
    return datetime.now(_BRASILIA).date()


class FrankfurterProvider:
    """Fonte primária: Frankfurter (taxas de referência do BCE).

    Attributes:
        name: Identificação da fonte.
    """

    name: RateSource = RateSource.FRANKFURTER

    def __init__(self, client: httpx.AsyncClient, timeout: float) -> None:
        """Cria o provedor.

        Args:
            client: Cliente HTTP compartilhado.
            timeout: Tempo máximo de cada chamada, em segundos.
        """
        self._client = client
        self._timeout = timeout

    async def fetch(self, currency: Currency) -> RateQuote:
        """Obtém a cotação mais recente da moeda em BRL.

        Args:
            currency: Moeda estrangeira.

        Returns:
            Cotação com ``quoted_at`` à meia-noite UTC da data informada e sem boletim.

        Raises:
            ProviderError: Em toda falha da fonte.
        """
        payload = await _get_json(
            self._client,
            _FRANKFURTER_URL,
            {"base": currency.value, "symbols": "BRL"},
            self._timeout,
        )
        try:
            return self._parse(payload, currency)
        except _PAYLOAD_FAILURES as error:
            raise ProviderError(type(error).__name__) from None

    def _parse(self, payload: Any, currency: Currency) -> RateQuote:
        """Monta a cotação a partir da resposta.

        Args:
            payload: Corpo decodificado.
            currency: Moeda pedida.

        Returns:
            A cotação aprovada no aceite.

        Raises:
            ProviderError: Se a resposta não for da moeda pedida, for para outra quantidade
                de unidades ou a taxa for reprovada.
        """
        if payload["base"] != currency.value:
            raise ProviderError("base_mismatch")
        # A taxa vale para `amount` unidades; outro valor erraria a cotação sem sair do aceite.
        if payload["amount"] != 1:
            raise ProviderError("amount_mismatch")
        quoted_on = date.fromisoformat(payload["date"])
        return RateQuote(
            currency=currency,
            rate=_accept_rate(payload["rates"]["BRL"]),
            source=self.name,
            quoted_at=datetime.combine(quoted_on, time.min, tzinfo=UTC),
            bulletin=None,
            stale=False,
        )


class PtaxProvider:
    """Fonte de reserva: PTAX do Banco Central do Brasil (OData Olinda).

    Attributes:
        name: Identificação da fonte.
    """

    name: RateSource = RateSource.PTAX

    def __init__(
        self,
        client: httpx.AsyncClient,
        timeout: float,
        today: Callable[[], date] = _today_in_brasilia,
    ) -> None:
        """Cria o provedor.

        Args:
            client: Cliente HTTP compartilhado.
            timeout: Tempo máximo de cada chamada, em segundos.
            today: Devolve a data final da janela de consulta.
        """
        self._client = client
        self._timeout = timeout
        self._today = today

    async def fetch(self, currency: Currency) -> RateQuote:
        """Obtém o boletim mais recente da moeda nos últimos 7 dias.

        Usa ``cotacaoCompra``, pois o profissional vende a moeda estrangeira.

        Args:
            currency: Moeda estrangeira.

        Returns:
            Cotação com ``quoted_at`` em UTC e o tipo do boletim.

        Raises:
            ProviderError: Em toda falha da fonte, inclusive janela sem linhas.
        """
        final = self._today()
        initial = final - _PTAX_WINDOW
        payload = await _get_json(
            self._client,
            _PTAX_URL,
            {
                "@moeda": f"'{currency.value}'",
                "@dataInicial": f"'{initial.strftime(_PTAX_DATE_FORMAT)}'",
                "@dataFinalCotacao": f"'{final.strftime(_PTAX_DATE_FORMAT)}'",
                "$top": "1",
                "$orderby": "dataHoraCotacao desc",
                "$format": "json",
            },
            self._timeout,
        )
        try:
            return self._parse(payload, currency)
        except _PAYLOAD_FAILURES as error:
            raise ProviderError(type(error).__name__) from None

    def _parse(self, payload: Any, currency: Currency) -> RateQuote:
        """Monta a cotação a partir da primeira linha da resposta.

        Args:
            payload: Corpo decodificado.
            currency: Moeda pedida.

        Returns:
            A cotação aprovada no aceite.

        Raises:
            ProviderError: Se a janela vier vazia ou algum campo for reprovado.
        """
        rows = payload["value"]
        if not rows:
            raise ProviderError("empty_window")
        row = rows[0]
        return RateQuote(
            currency=currency,
            rate=_accept_rate(row["cotacaoCompra"]),
            source=self.name,
            quoted_at=_brasilia_to_utc(row["dataHoraCotacao"]),
            bulletin=_accept_bulletin(row["tipoBoletim"]),
            stale=False,
        )
