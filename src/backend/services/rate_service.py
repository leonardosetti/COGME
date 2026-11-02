"""Obtenção de cotações com cache e cadeia de fontes (spec backend-mvp-v1, §4; REQ-01, REQ-07).

O cache não é crítico para responder: falha ao ler segue para as fontes e falha ao gravar não
derruba uma cotação válida. Os logs trazem só o nome da fonte e o tipo da falha.

Orçamento de uma requisição, para caber nos 2 s de REQ-01 (padrões do ``__init__``):

    leitura 0,3 + releitura 0,3 + cadeia até t=1,6 + gravação 0,3 = 1,9 s no pior caso

Cada etapa respeita o prazo total contado da chegada, inclusive a espera na fila da moeda. A
cadeia termina 0,3 s antes dele para a gravação caber, e a releitura só ocorre se a primeira
leitura funcionou. Os 0,1 s restantes ficam para rota, serialização e rede local.

Concorrência: uma requisição por moeda percorre a cadeia. Quem esperou herda o desfecho sem
tocar no banco nem nas fontes, seja sucesso ou falha, e assim a fila não vira uma série de
cadeias.

Banco fora do ar: um circuito próprio pula o repositório depois de falhas seguidas. Cortar a
chamada não basta, porque a consulta de DNS de um banco parado segue ocupando o pool do libuv
(uvloop) e atrasa o DNS das fontes. Aberto o circuito, só uma sonda por vez toca o banco.
"""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Callable, Coroutine
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Any, Final, NamedTuple, TypeVar

from pydantic import ValidationError

from src.backend.errors import RatesUnavailableError
from src.backend.models.repository import QuoteRepository, RepositoryError, StoredQuote
from src.backend.services.circuit_breaker import CircuitBreaker
from src.backend.services.rate_providers import ProviderError, RateProvider
from src.shared.schemas import Currency, RateQuote, RateSource

logger = logging.getLogger(__name__)

_T = TypeVar("_T")

_REPOSITORY_FAILURE_THRESHOLD: Final[int] = 3
_REPOSITORY_RESET_SECONDS: Final[float] = 5.0


class _CachedQuote(NamedTuple):
    """Linha do cache aprovada pelo contrato.

    Attributes:
        quote: Cotação com ``stale=False``.
        fetched_at: Instante de obtenção, do qual conta a idade.
    """

    quote: RateQuote
    fetched_at: datetime


class _CacheRead(NamedTuple):
    """Resultado de uma leitura do cache.

    Attributes:
        row: Linha aprovada pelo contrato, ou ``None``.
        reachable: ``False`` se a leitura falhou ou foi pulada; reler só gastaria orçamento.
    """

    row: _CachedQuote | None
    reachable: bool


@dataclass(slots=True)
class _Flight:
    """Estado do single-flight de uma moeda, dentro de um único event loop.

    Attributes:
        lock: Garante uma cadeia de fontes por vez.
        completed: Cadeias concluídas; quem vê o número mudar herda ``outcome``.
        outcome: Desfecho da última cadeia concluída; ``None`` se todas as fontes falharam.
    """

    lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    completed: int = 0
    outcome: RateQuote | None = None


def _utc_now() -> datetime:
    """Devolve o instante atual em UTC.

    Returns:
        O instante atual, com fuso.
    """
    return datetime.now(UTC)


def _to_contract(stored: StoredQuote) -> RateQuote:
    """Converte uma linha do cache para o contrato, com ``stale=False``.

    Args:
        stored: Linha lida do repositório.

    Returns:
        A cotação equivalente.

    Raises:
        ValueError: Se a moeda ou a fonte não pertencerem ao contrato.
        pydantic.ValidationError: Se a linha violar o contrato.
    """
    return RateQuote(
        currency=Currency(stored.currency),
        rate=stored.rate,
        source=RateSource(stored.source),
        quoted_at=stored.quoted_at,
        bulletin=stored.bulletin,
        stale=False,
    )


def _failure_cause(error: Exception) -> str:
    """Nomeia a falha de uma operação do repositório, sem o texto dela.

    Args:
        error: ``RepositoryError``, cuja causa fica em ``__cause__``, ou ``TimeoutError``.

    Returns:
        O nome do tipo da causa, seguro para log.
    """
    if isinstance(error, RepositoryError):
        return type(error.__cause__).__name__
    return type(error).__name__


def _fallback(row: _CachedQuote | None) -> RateQuote:
    """Resolve a requisição sem cotação nova: cache vencido ou indisponibilidade.

    Args:
        row: Última linha conhecida do cache.

    Returns:
        A linha com ``stale=True``.

    Raises:
        RatesUnavailableError: Se não houver linha.
    """
    if row is None:
        raise RatesUnavailableError()
    return row.quote.model_copy(update={"stale": True})


class RateService:
    """Resolve a cotação: cache fresco, fontes, cache vencido, nessa ordem."""

    def __init__(
        self,
        repository: QuoteRepository,
        providers: list[tuple[RateProvider, CircuitBreaker]],
        ttl_seconds: int,
        now: Callable[[], datetime] = _utc_now,
        repository_timeout: float = 0.3,
        total_timeout: float = 1.9,
        repository_breaker: CircuitBreaker | None = None,
    ) -> None:
        """Cria o serviço.

        Args:
            repository: Acesso às cotações persistidas.
            providers: Fontes em ordem de preferência, cada uma com seu circuito.
            ttl_seconds: Idade máxima, em segundos, de uma cotação fresca.
            now: Relógio em UTC.
            repository_timeout: Limite, em segundos, de cada chamada ao repositório.
            total_timeout: Prazo, em segundos, de uma requisição inteira; fica abaixo dos 2 s
                de REQ-01 para sobrar tempo à resposta HTTP.
            repository_breaker: Circuito do repositório. Sem ele, abre após 3 falhas seguidas e
                admite uma sonda a cada 5 s.

        Raises:
            ValueError: Se leitura, releitura e gravação não deixarem tempo para as fontes.
        """
        if not 0 < 3 * repository_timeout < total_timeout:
            raise ValueError("O orçamento do repositório não deixa tempo para as fontes.")
        self._repository = repository
        self._providers = providers
        self._ttl = timedelta(seconds=ttl_seconds)
        self._now = now
        self._repository_timeout = repository_timeout
        self._total_timeout = total_timeout
        # Criados aqui porque o serviço nasce no lifespan: os locks ficam no loop da aplicação.
        self._flights = {currency: _Flight() for currency in Currency}
        self._abandoned: set[asyncio.Task[Any]] = set()
        if repository_breaker is None:
            repository_breaker = CircuitBreaker(
                failure_threshold=_REPOSITORY_FAILURE_THRESHOLD,
                reset_seconds=_REPOSITORY_RESET_SECONDS,
            )
        self._repository_breaker = repository_breaker
        self._repository_skipped = False
        self._repository_failure = ""

    async def get_quote(self, currency: Currency) -> RateQuote:
        """Devolve a cotação da moeda conforme o fluxo da §4.

        Args:
            currency: Moeda estrangeira.

        Returns:
            A cotação; ``stale=True`` somente quando vem de cache vencido, após falha geral.

        Raises:
            RatesUnavailableError: Sem fonte disponível e sem cache.
        """
        deadline = asyncio.get_running_loop().time() + self._total_timeout
        flight = self._flights[currency]
        # Lido antes do cache: uma cadeia concluída depois deste ponto vale para esta requisição.
        seen = flight.completed
        first = await self._read_cache(currency, deadline)
        fresh = self._fresh_quote(first.row)
        if fresh is not None:
            return fresh

        try:
            async with asyncio.timeout_at(deadline):
                await flight.lock.acquire()
        except TimeoutError:
            logger.warning("quote_flight_wait_expired")
            return _fallback(first.row)
        try:
            if flight.completed != seen:
                quote, row = flight.outcome, first.row
            else:
                quote, row = await self._lead(currency, first, deadline)
                flight.outcome = quote
                flight.completed += 1
        finally:
            flight.lock.release()

        return quote if quote is not None else _fallback(row)

    def _fresh_quote(self, row: _CachedQuote | None) -> RateQuote | None:
        """Devolve a cotação da linha se ela estiver dentro do TTL.

        Args:
            row: Linha do cache.

        Returns:
            A cotação fresca, ou ``None``.
        """
        if row is not None and self._now() - row.fetched_at <= self._ttl:
            return row.quote
        return None

    async def _lead(
        self,
        currency: Currency,
        first: _CacheRead,
        deadline: float,
    ) -> tuple[RateQuote | None, _CachedQuote | None]:
        """Resolve a moeda com o lock em mãos: relê o cache, percorre as fontes e grava.

        A gravação fica dentro do lock: quem chega durante ela espera e herda o desfecho, em
        vez de não achar a linha e repetir a cadeia.

        Args:
            currency: Moeda estrangeira.
            first: Primeira leitura do cache, feita antes do lock.
            deadline: Prazo da requisição, no relógio do event loop.

        Returns:
            A cotação, ou ``None`` se nenhuma fonte responder, e a linha mais recente do cache.
        """
        row = first.row
        if first.reachable:
            again = await self._read_cache(currency, deadline)
            if again.row is not None:
                row = again.row
            fresh = self._fresh_quote(again.row)
            if fresh is not None:
                return fresh, row
        quote = await self._fetch_from_providers(currency, deadline - self._repository_timeout)
        if quote is not None:
            await self._write_cache(quote, deadline)
        return quote, row

    def _repository_allowed(self) -> bool:
        """Informa se o repositório pode ser chamado, conforme o circuito dele.

        Quem recebe ``True`` deve chamar :meth:`_bounded` em seguida, sem ceder o controle, pois
        é ele que registra o desfecho. O salto é registrado uma vez por queda, não por requisição.

        Returns:
            ``True`` se a chamada foi admitida; no meio-aberto, ela é a sonda.
        """
        if self._repository_breaker.allow():
            return True
        if not self._repository_skipped:
            self._repository_skipped = True
            logger.warning("quote_cache_skipped cause=%s", self._repository_failure)
        return False

    async def _bounded(self, operation: Coroutine[Any, Any, _T], deadline: float) -> _T:
        """Executa uma chamada ao repositório dentro do orçamento e registra o desfecho.

        ``shield`` existe porque o cancelamento não basta: ao sair por cancelamento, a sessão
        ainda fecha a conexão, e essa limpeza prende quem espera se o banco estiver travado. A
        operação vencida é cancelada e segue sozinha até o fim, limitada pelos timeouts do
        driver.

        Falha e estouro contam contra o circuito. Cancelamento e erro inesperado só liberam a
        sonda: não dizem nada sobre o banco, e sem o registro ela bloquearia o circuito.

        Args:
            operation: Corrotina do repositório.
            deadline: Prazo da requisição, no relógio do event loop.

        Returns:
            O resultado da operação.

        Raises:
            TimeoutError: Se o orçamento acabar.
            RepositoryError: Se a operação falhar.
        """
        limit = asyncio.get_running_loop().time() + self._repository_timeout
        task = asyncio.create_task(operation)
        try:
            async with asyncio.timeout_at(min(limit, deadline)):
                result = await asyncio.shield(task)
        except BaseException as error:
            if not task.done():
                task.cancel()
                self._abandoned.add(task)
                task.add_done_callback(self._abandoned.discard)
            if isinstance(error, RepositoryError | TimeoutError):
                self._repository_failure = _failure_cause(error)
                self._repository_breaker.record_failure()
            else:
                self._repository_breaker.record_release()
            raise
        self._repository_breaker.record_success()
        if self._repository_skipped:
            self._repository_skipped = False
            logger.info("quote_cache_recovered")
        return result

    async def _read_cache(self, currency: Currency, deadline: float) -> _CacheRead:
        """Lê a última cotação da moeda, tratando falha, estouro e salto como ausência de cache.

        Args:
            currency: Moeda estrangeira.
            deadline: Prazo da requisição, no relógio do event loop.

        Returns:
            A linha aprovada pelo contrato, ou nenhuma se não houver linha utilizável.
        """
        if not self._repository_allowed():
            return _CacheRead(None, reachable=False)
        try:
            stored = await self._bounded(self._repository.get_latest(currency.value), deadline)
        except (RepositoryError, TimeoutError) as error:
            logger.warning("quote_cache_read_failed cause=%s", _failure_cause(error))
            return _CacheRead(None, reachable=False)
        if stored is None:
            return _CacheRead(None, reachable=True)
        try:
            return _CacheRead(_CachedQuote(_to_contract(stored), stored.fetched_at), reachable=True)
        except (ValidationError, ValueError) as error:
            logger.warning("quote_cache_row_rejected cause=%s", type(error).__name__)
            return _CacheRead(None, reachable=True)

    async def _fetch_from_providers(
        self, currency: Currency, deadline: float
    ) -> RateQuote | None:
        """Percorre a cadeia de fontes até o prazo, pulando as de circuito aberto.

        Toda chamada admitida registra um desfecho no circuito; sem o registro, a tentativa
        meio-aberta bloquearia a fonte para sempre. Cancelamento e corte pelo prazo da cadeia
        liberam a tentativa sem penalizar: a fonte não falhou, só ficou sem tempo. Penalizá-la
        abriria o circuito da PTAX por culpa de uma Frankfurter lenta.

        Args:
            currency: Moeda estrangeira.
            deadline: Fim da cadeia, no relógio do event loop.

        Returns:
            A primeira cotação obtida, ou ``None`` se nenhuma fonte responder.
        """
        loop = asyncio.get_running_loop()
        for provider, breaker in self._providers:
            if loop.time() >= deadline or not breaker.allow():
                continue
            scope = asyncio.timeout_at(deadline)
            try:
                async with scope:
                    quote = await provider.fetch(currency)
            except ProviderError as error:
                breaker.record_failure()
                logger.warning(
                    "rate_provider_failed provider=%s reason=%s",
                    provider.name.value,
                    error,
                )
                continue
            except TimeoutError:
                if not scope.expired():
                    breaker.record_failure()
                    raise
                breaker.record_release()
                logger.warning("rate_chain_deadline provider=%s", provider.name.value)
                continue
            except asyncio.CancelledError:
                breaker.record_release()
                raise
            except BaseException:
                breaker.record_failure()
                raise
            breaker.record_success()
            return quote
        return None

    async def _write_cache(self, quote: RateQuote, deadline: float) -> None:
        """Grava a cotação recém-obtida; falha, estouro ou salto não impedem devolvê-la.

        Args:
            quote: Cotação aprovada no aceite.
            deadline: Prazo da requisição, no relógio do event loop.
        """
        if not self._repository_allowed():
            return
        stored = StoredQuote(
            currency=quote.currency.value,
            rate=quote.rate,
            source=quote.source.value,
            bulletin=quote.bulletin,
            quoted_at=quote.quoted_at,
            fetched_at=self._now(),
        )
        try:
            await self._bounded(self._repository.save(stored), deadline)
        except (RepositoryError, TimeoutError) as error:
            logger.warning("quote_cache_write_failed cause=%s", _failure_cause(error))
