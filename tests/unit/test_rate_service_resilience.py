"""Latência e concorrência do RateService (spec backend-mvp-v1, §4; REQ-01).

Banco travado, cadeia cortada pelo prazo, single-flight por moeda e cancelamento. Repositório e
provedores são falsos. Os prazos são mínimos e reais, pois quem os aplica é o event loop: um
corte que falte faz o teste travar, em vez de só medir um tempo maior.
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any

import pytest

from src.backend.errors import RatesUnavailableError
from src.backend.models.repository import StoredQuote
from src.backend.services.circuit_breaker import CircuitBreaker
from src.backend.services.rate_providers import ProviderError
from src.backend.services.rate_service import RateService
from src.shared.schemas import Currency, RateQuote, RateSource

SERVICE_LOGGER = "src.backend.services.rate_service"
REPOSITORY_TIMEOUT = 0.02
TOTAL_TIMEOUT = 0.2
CONCURRENT_REQUESTS = 100


class HungRepository:
    """Repositório que nunca responde, como um banco sob ``docker pause``."""

    async def get_latest(self, currency: str) -> StoredQuote | None:
        """Espera para sempre."""
        await asyncio.Event().wait()
        return None

    async def save(self, quote: StoredQuote) -> None:
        """Espera para sempre."""
        await asyncio.Event().wait()


class StuckCleanupRepository(HungRepository):
    """Repositório cuja limpeza trava depois do cancelamento, como a sessão ao fechar conexão."""

    def __init__(self) -> None:
        self.release_cleanup = asyncio.Event()

    async def get_latest(self, currency: str) -> StoredQuote | None:
        """Espera para sempre e, cancelado, só termina quando o teste liberar."""
        try:
            await asyncio.Event().wait()
        finally:
            await self.release_cleanup.wait()
        return None


class ScriptedProvider:
    """Provedor que cede o controle e devolve a cotação, levanta o erro ou trava.

    Attributes:
        name: Fonte que o provedor representa.
        quote: Cotação devolvida; sem ela e sem erro, ``fetch`` trava.
        calls: Chamadas a ``fetch``.
    """

    def __init__(
        self,
        name: RateSource = RateSource.FRANKFURTER,
        *,
        quote: RateQuote | None = None,
        error: Exception | None = None,
    ) -> None:
        self.name = name
        self.quote = quote
        self.calls = 0
        self._error = error

    async def fetch(self, currency: Currency) -> RateQuote:
        """Conta a chamada e responde conforme configurado; sem resposta, trava."""
        self.calls += 1
        await asyncio.sleep(0.001)
        if self._error is not None:
            raise self._error
        if self.quote is None:
            await asyncio.Event().wait()
        assert self.quote is not None
        return self.quote


def _service(
    repository: Any,
    providers: list[ScriptedProvider],
    breakers: list[CircuitBreaker] | None = None,
    repository_breaker: CircuitBreaker | None = None,
) -> RateService:
    """Monta o serviço com prazos mínimos."""
    circuits = breakers or [CircuitBreaker() for _ in providers]
    return RateService(
        repository=repository,
        providers=list(zip(providers, circuits, strict=True)),
        ttl_seconds=3600,
        repository_timeout=REPOSITORY_TIMEOUT,
        total_timeout=TOTAL_TIMEOUT,
        repository_breaker=repository_breaker,
    )


def _half_open(mono_clock: Any) -> CircuitBreaker:
    """Devolve um circuito aberto cujo prazo já venceu."""
    breaker = CircuitBreaker(clock=mono_clock)
    for _ in range(3):
        breaker.record_failure()
    mono_clock.advance(60)
    return breaker


async def test_hung_database_does_not_block_the_quote_req01(
    make_rate_quote: Any, caplog: pytest.LogCaptureFixture
) -> None:
    """REQ-01: banco travado vira cache ausente e gravação ignorada; a fonte responde."""
    provider = ScriptedProvider(quote=make_rate_quote(rate="5.420600"))
    service = _service(HungRepository(), [provider])

    with caplog.at_level(logging.WARNING, logger=SERVICE_LOGGER):
        quote = await service.get_quote(Currency.USD)

    assert str(quote.rate) == "5.420600"
    assert quote.stale is False
    assert "quote_cache_read_failed cause=TimeoutError" in caplog.text
    assert "quote_cache_write_failed cause=TimeoutError" in caplog.text


async def test_stuck_cleanup_does_not_extend_the_budget_req01(make_rate_quote: Any) -> None:
    """REQ-01: operação cancelada que demora a limpar não segura a resposta."""
    repository = StuckCleanupRepository()
    service = _service(repository, [ScriptedProvider(quote=make_rate_quote())])

    quote = await asyncio.wait_for(service.get_quote(Currency.USD), timeout=1)
    repository.release_cleanup.set()
    await asyncio.sleep(0)

    assert quote.stale is False


async def test_chain_deadline_does_not_penalize_the_source_req01(
    repository: Any, mono_clock: Any
) -> None:
    """REQ-01: a fonte cortada pelo prazo da cadeia não acumula falha; o resultado é 503."""
    breaker = CircuitBreaker(failure_threshold=1, clock=mono_clock)
    hung = ScriptedProvider()
    service = _service(repository, [hung], [breaker])

    with pytest.raises(RatesUnavailableError):
        await service.get_quote(Currency.USD)

    assert hung.calls == 1
    assert breaker.allow() is True


async def test_cold_cache_burst_makes_one_call_and_one_row_req07(
    repository: Any, make_rate_quote: Any
) -> None:
    """REQ-07: requisições concorrentes com cache frio geram uma chamada e uma linha."""
    provider = ScriptedProvider(quote=make_rate_quote(rate="5.100000"))
    # Os 0,02 s do orçamento expiram por atraso do event loop com 100 requisições, não por
    # falha do banco. O circuito fica acima do número de operações do teste (no máximo 102),
    # para não abrir e pular a gravação; as asserções seguem as mesmas.
    service = _service(
        repository,
        [provider],
        repository_breaker=CircuitBreaker(failure_threshold=10 * CONCURRENT_REQUESTS),
    )

    quotes = await asyncio.gather(
        *(service.get_quote(Currency.USD) for _ in range(CONCURRENT_REQUESTS))
    )

    assert provider.calls == 1
    assert len(repository.saved) == 1
    assert {str(quote.rate) for quote in quotes} == {"5.100000"}


async def test_hung_database_burst_shares_the_quote_req01(make_rate_quote: Any) -> None:
    """REQ-01: sem cache para consultar, os seguidores herdam a cotação do líder."""
    provider = ScriptedProvider(quote=make_rate_quote(rate="5.100000"))
    service = _service(HungRepository(), [provider])

    quotes = await asyncio.gather(
        *(service.get_quote(Currency.USD) for _ in range(CONCURRENT_REQUESTS))
    )

    assert provider.calls == 1
    assert {str(quote.rate) for quote in quotes} == {"5.100000"}


async def test_followers_inherit_failure_without_repeating_the_chain_req01(
    repository: Any,
) -> None:
    """REQ-01: falha do líder chega aos seguidores sem que repitam a cadeia em série."""
    provider = ScriptedProvider(error=ProviderError("falha simulada da fonte"))
    service = _service(repository, [provider])

    results = await asyncio.gather(
        *(service.get_quote(Currency.USD) for _ in range(CONCURRENT_REQUESTS)),
        return_exceptions=True,
    )

    assert provider.calls == 1
    assert all(isinstance(result, RatesUnavailableError) for result in results)


async def test_cancelled_leader_releases_probe_and_lock_req01(
    repository: Any, make_rate_quote: Any, mono_clock: Any
) -> None:
    """Cancelamento libera a tentativa meio-aberta e a fila; a próxima requisição resolve."""
    breaker = _half_open(mono_clock)
    provider = ScriptedProvider()
    service = _service(repository, [provider], [breaker])
    leader = asyncio.create_task(service.get_quote(Currency.USD))
    while provider.calls == 0:
        await asyncio.sleep(0)

    leader.cancel()
    with pytest.raises(asyncio.CancelledError):
        await leader

    provider.quote = make_rate_quote(rate="5.100000")
    quote = await service.get_quote(Currency.USD)

    assert str(quote.rate) == "5.100000"
    assert provider.calls == 2


def test_record_release_frees_the_probe_without_penalty(mono_clock: Any) -> None:
    """``record_release`` libera a tentativa sem reabrir o prazo nem zerar a contagem."""
    breaker = _half_open(mono_clock)
    assert breaker.allow() is True
    assert breaker.allow() is False

    breaker.record_release()

    assert breaker.allow() is True

    closed = CircuitBreaker(failure_threshold=2, clock=mono_clock)
    closed.record_failure()
    closed.record_release()
    closed.record_failure()
    assert closed.allow() is False
