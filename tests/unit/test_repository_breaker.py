"""Circuito do repositório no RateService (spec backend-mvp-v1, §4; REQ-01, REQ-07).

Abre após 3 falhas (estouro ou ``RepositoryError``); aberto, leitura e gravação não tocam no
banco e a cotação vem das fontes; meio-aberto admite uma sonda; sucesso fecha; cancelamento não
penaliza. O relógio do circuito é falso e nenhum teste dorme. O único prazo real é o do estouro,
de 0,02 s, aplicado pelo event loop: um repositório que trava sempre estoura, então o resultado
não depende de carga.
"""

from __future__ import annotations

import asyncio
import logging
from collections.abc import Callable
from typing import Any

import pytest

from src.backend.errors import RatesUnavailableError
from src.backend.models.repository import RepositoryError, StoredQuote
from src.backend.services.circuit_breaker import CircuitBreaker
from src.backend.services.rate_providers import ProviderError
from src.backend.services.rate_service import RateService
from src.shared.schemas import Currency, RateQuote, RateSource

SERVICE_LOGGER = "src.backend.services.rate_service"
HANG_TIMEOUT = 0.02  # estouro real; só o repositório que trava o usa
SAFE_TIMEOUT = 0.5  # folga para que atraso do host não vire falha
SAFE_TOTAL = 2.0
RESET_SECONDS = 5.0
RATE = "5.734219"  # valor sintético; não pode aparecer em log
CAUSE_TEXT = "texto sintético da causa, que nunca deve ir para o log"
CONCURRENT_REQUESTS = 50


class ScriptedRepository:
    """Repositório que conta chamadas e responde, falha ou trava conforme ``mode``.

    Attributes:
        mode: ``ok``, ``error`` (``RepositoryError``) ou ``hang`` (nunca responde).
        gate: Se definido, ``get_latest`` espera este evento antes de responder.
        reads: Chamadas a ``get_latest``.
        writes: Chamadas a ``save``.
    """

    def __init__(self) -> None:
        self.mode = "ok"
        self.gate: asyncio.Event | None = None
        self.reads = 0
        self.writes = 0

    async def _respond(self) -> None:
        if self.mode == "error":
            raise RepositoryError("Falha simulada do repositório.") from ConnectionError(
                CAUSE_TEXT
            )
        if self.mode == "hang":
            await asyncio.Event().wait()

    async def get_latest(self, currency: str) -> StoredQuote | None:
        """Conta a leitura e responde conforme ``mode``; o cache fica sempre vazio."""
        self.reads += 1
        if self.gate is not None:
            await self.gate.wait()
        await self._respond()
        return None

    async def save(self, quote: StoredQuote) -> None:
        """Conta a gravação e responde conforme ``mode``."""
        self.writes += 1
        await self._respond()


class QuietProvider:
    """Fonte que devolve a cotação ou levanta o erro, e conta as chamadas.

    Cede o controle uma vez, como uma rede real: as requisições seguintes chegam à fila da
    moeda enquanto a cadeia ainda corre, e herdam o desfecho do líder.

    Attributes:
        calls: Chamadas a ``fetch``.
    """

    name = RateSource.FRANKFURTER

    def __init__(self, quote: RateQuote | None = None, error: Exception | None = None) -> None:
        self.calls = 0
        self._quote = quote
        self._error = error

    async def fetch(self, currency: Currency) -> RateQuote:
        """Conta a chamada, cede o controle uma vez e devolve a cotação ou levanta o erro."""
        self.calls += 1
        await asyncio.sleep(0)
        if self._error is not None:
            raise self._error
        assert self._quote is not None
        return self._quote


async def _wait_until(predicate: Callable[[], bool]) -> None:
    """Cede o controle ao event loop até o predicado valer; sem relógio real."""
    for _ in range(1000):
        if predicate():
            return
        await asyncio.sleep(0)
    raise AssertionError("a condição esperada não ocorreu")


def _breaker(mono_clock: Any) -> CircuitBreaker:
    """Circuito do repositório com os parâmetros padrão da §4 e relógio falso."""
    return CircuitBreaker(failure_threshold=3, reset_seconds=RESET_SECONDS, clock=mono_clock)


def _trip(breaker: CircuitBreaker) -> None:
    """Leva o circuito ao estado aberto com três falhas consecutivas."""
    for _ in range(3):
        breaker.record_failure()


def _service(
    repository: ScriptedRepository,
    provider: QuietProvider,
    breaker: CircuitBreaker,
    mono_clock: Any,
    repository_timeout: float = SAFE_TIMEOUT,
) -> RateService:
    """Monta o serviço com uma fonte, o circuito do repositório injetado e prazos seguros."""
    return RateService(
        repository=repository,
        providers=[(provider, CircuitBreaker(clock=mono_clock))],
        ttl_seconds=3600,
        repository_timeout=repository_timeout,
        total_timeout=SAFE_TOTAL,
        repository_breaker=breaker,
    )


@pytest.mark.parametrize("mode", ["error", "hang"])
async def test_opens_after_three_failures(
    mode: str, mono_clock: Any, make_rate_quote: Any
) -> None:
    """Três falhas seguidas, por RepositoryError ou por estouro, abrem o circuito."""
    repository = ScriptedRepository()
    repository.mode = mode
    timeout = HANG_TIMEOUT if mode == "hang" else SAFE_TIMEOUT
    breaker = _breaker(mono_clock)
    provider = QuietProvider(quote=make_rate_quote(rate=RATE))
    service = _service(repository, provider, breaker, mono_clock, timeout)

    await service.get_quote(Currency.USD)  # leitura falha (1) e gravação falha (2)
    assert repository.reads == 1
    assert breaker.allow() is True

    await service.get_quote(Currency.USD)  # leitura falha (3) e abre o circuito
    assert repository.reads == 2
    assert breaker.allow() is False


async def test_open_breaker_skips_repository_and_serves_source(
    mono_clock: Any, make_rate_quote: Any
) -> None:
    """Aberto, leitura e gravação não tocam no banco; a cotação vem da fonte."""
    repository = ScriptedRepository()
    repository.mode = "error"
    provider = QuietProvider(quote=make_rate_quote(rate=RATE))
    service = _service(repository, provider, _breaker(mono_clock), mono_clock)
    await service.get_quote(Currency.USD)
    await service.get_quote(Currency.USD)  # abre o circuito
    reads, writes = repository.reads, repository.writes

    for _ in range(3):
        quote = await service.get_quote(Currency.USD)
        assert str(quote.rate) == RATE
        assert quote.stale is False

    assert (repository.reads, repository.writes) == (reads, writes)
    assert provider.calls == 5


async def test_open_breaker_without_sources_or_cache_is_unavailable(
    mono_clock: Any,
) -> None:
    """Aberto, com as fontes fora e sem cache, a resposta é RatesUnavailableError."""
    repository = ScriptedRepository()
    breaker = _breaker(mono_clock)
    _trip(breaker)
    provider = QuietProvider(error=ProviderError("falha simulada da fonte"))
    service = _service(repository, provider, breaker, mono_clock)

    with pytest.raises(RatesUnavailableError):
        await service.get_quote(Currency.USD)

    assert (repository.reads, repository.writes) == (0, 0)


async def test_half_open_admits_one_probe_under_concurrency(
    mono_clock: Any, make_rate_quote: Any
) -> None:
    """Meio-aberto: só a sonda toca no banco, as demais herdam a cotação; sucesso fecha."""
    repository = ScriptedRepository()
    repository.gate = asyncio.Event()
    breaker = _breaker(mono_clock)
    _trip(breaker)
    mono_clock.advance(RESET_SECONDS)
    provider = QuietProvider(quote=make_rate_quote(rate=RATE))
    service = _service(repository, provider, breaker, mono_clock)

    tasks = [
        asyncio.create_task(service.get_quote(Currency.USD))
        for _ in range(CONCURRENT_REQUESTS)
    ]
    await _wait_until(lambda: all(task.done() for task in tasks[1:]))

    assert repository.reads == 1
    assert repository.writes == 0
    assert provider.calls == 1

    repository.gate.set()
    quotes = await asyncio.gather(*tasks)

    assert {str(quote.rate) for quote in quotes} == {RATE}
    assert breaker.allow() is True


async def test_cancelled_reads_do_not_open_the_circuit(
    mono_clock: Any, make_rate_quote: Any
) -> None:
    """Cancelamento não conta como falha: três leituras canceladas não abrem o circuito."""
    repository = ScriptedRepository()
    repository.mode = "hang"
    breaker = _breaker(mono_clock)
    provider = QuietProvider(quote=make_rate_quote(rate=RATE))
    service = _service(repository, provider, breaker, mono_clock)

    for attempt in range(3):
        task = asyncio.create_task(service.get_quote(Currency.USD))
        await _wait_until(lambda: repository.reads == attempt + 1)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task

    assert breaker.allow() is True
    reads_before = repository.reads
    repository.mode = "ok"
    quote = await service.get_quote(Currency.USD)

    assert repository.reads == reads_before + 2  # leitura e releitura do líder: não foram puladas
    assert str(quote.rate) == RATE


async def test_transition_logs_appear_once_and_carry_no_values(
    mono_clock: Any, make_rate_quote: Any, caplog: pytest.LogCaptureFixture
) -> None:
    """Os logs de queda e de recuperação saem uma vez por transição, sem valores financeiros."""
    caplog.set_level(logging.INFO, logger=SERVICE_LOGGER)
    repository = ScriptedRepository()
    repository.mode = "error"
    provider = QuietProvider(quote=make_rate_quote(rate=RATE))
    service = _service(repository, provider, _breaker(mono_clock), mono_clock)

    await service.get_quote(Currency.USD)
    await service.get_quote(Currency.USD)  # abre o circuito
    for _ in range(3):
        await service.get_quote(Currency.USD)

    assert caplog.text.count("quote_cache_skipped") == 1
    assert "quote_cache_skipped cause=ConnectionError" in caplog.text
    assert "quote_cache_recovered" not in caplog.text

    mono_clock.advance(RESET_SECONDS)
    repository.mode = "ok"
    await service.get_quote(Currency.USD)  # sonda com sucesso fecha o circuito
    await service.get_quote(Currency.USD)

    assert caplog.text.count("quote_cache_recovered") == 1

    repository.mode = "error"
    for _ in range(3):  # reabre e registra uma nova queda
        await service.get_quote(Currency.USD)

    assert caplog.text.count("quote_cache_skipped") == 2
    assert RATE not in caplog.text
    assert CAUSE_TEXT not in caplog.text
