"""Testes unitários de services/rate_service.py (spec backend-mvp-v1, §4; REQ-01, REQ-07).

Fluxo: cache com idade ≤ TTL (contada de fetched_at) → Frankfurter → PTAX, pulando
circuito aberto → cache vencido com stale=true → RatesUnavailableError.
Provedores e repositório são falsos e em memória; os relógios são falsos.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

import pytest

from src.backend.errors import RatesUnavailableError
from src.backend.services.circuit_breaker import CircuitBreaker
from src.backend.services.rate_providers import ProviderError
from src.backend.services.rate_service import RateService
from src.shared.schemas import Currency, RateQuote, RateSource

TTL_SECONDS = 3600


class FakeProvider:
    """Provedor falso: devolve a cotação configurada ou levanta o erro configurado.

    Attributes:
        name: Fonte que o provedor representa.
        calls: Chamadas a ``fetch``; é a medida de tráfego de rede.
    """

    def __init__(
        self, name: RateSource, *, quote: RateQuote | None = None, error: Exception | None = None
    ) -> None:
        self.name = name
        self.calls = 0
        self._quote = quote
        self._error = error

    async def fetch(self, currency: Currency) -> RateQuote:
        """Conta a chamada; devolve a cotação ou levanta o erro configurado."""
        del currency
        self.calls += 1
        if self._error is not None:
            raise self._error
        assert self._quote is not None, "o fake precisa de cotação ou de erro"
        return self._quote


def _ok(name: RateSource, make_rate_quote: Any, rate: str = "5.100000") -> FakeProvider:
    """Provedor que sempre responde com uma cotação sintética de ``rate``."""
    return FakeProvider(name, quote=make_rate_quote(rate=rate, source=name.value))


def _failing(name: RateSource) -> FakeProvider:
    """Provedor que sempre falha com ProviderError."""
    return FakeProvider(name, error=ProviderError("falha simulada da fonte"))


def _breaker(mono_clock: Any) -> CircuitBreaker:
    """Circuito com os padrões da §8.1 e relógio falso."""
    return CircuitBreaker(failure_threshold=3, reset_seconds=60.0, clock=mono_clock)


def _service(
    repository: Any,
    providers: list[FakeProvider],
    utc_clock: Any,
    mono_clock: Any,
    breakers: list[CircuitBreaker] | None = None,
) -> RateService:
    """Monta o RateService com um circuito por provedor, salvo quando informado."""
    circuits = breakers or [_breaker(mono_clock) for _ in providers]
    return RateService(
        repository=repository,
        providers=list(zip(providers, circuits, strict=True)),
        ttl_seconds=TTL_SECONDS,
        now=utc_clock,
    )


async def test_fresh_cache_skips_network_req07(
    repository: Any, make_stored_quote: Any, make_rate_quote: Any,
    utc_clock: Any, mono_clock: Any, now: datetime,
) -> None:
    """REQ-07: cache fresco devolve sem chamar nenhum provedor."""
    fetched = now - timedelta(minutes=10)
    repository.rows.append(make_stored_quote(rate="4.900000", fetched_at=fetched))
    frankfurter = _ok(RateSource.FRANKFURTER, make_rate_quote, "5.000000")
    ptax = _ok(RateSource.PTAX, make_rate_quote)
    service = _service(repository, [frankfurter, ptax], utc_clock, mono_clock)

    quote = await service.get_quote(Currency.USD)

    assert str(quote.rate) == "4.900000"
    assert quote.stale is False
    assert frankfurter.calls == 0
    assert ptax.calls == 0


@pytest.mark.parametrize(
    ("age_seconds", "fresh"),
    [(3599, True), (3600, True), (3601, False)],
    ids=["abaixo_do_ttl", "no_limite", "acima_do_ttl"],
)
async def test_cache_age_boundary_is_inclusive_req07(
    repository: Any, make_stored_quote: Any, make_rate_quote: Any,
    utc_clock: Any, mono_clock: Any, now: datetime, age_seconds: int, fresh: bool,
) -> None:
    """REQ-07: a idade conta de fetched_at; exatamente o TTL ainda é fresco (§4)."""
    repository.rows.append(
        make_stored_quote(rate="4.900000", fetched_at=now - timedelta(seconds=age_seconds))
    )
    frankfurter = _ok(RateSource.FRANKFURTER, make_rate_quote, "5.500000")
    service = _service(repository, [frankfurter], utc_clock, mono_clock)

    quote = await service.get_quote(Currency.USD)

    assert frankfurter.calls == (0 if fresh else 1)
    assert str(quote.rate) == ("4.900000" if fresh else "5.500000")


async def test_expired_cache_fetches_and_saves_req07(
    repository: Any, make_stored_quote: Any, make_rate_quote: Any,
    utc_clock: Any, mono_clock: Any, now: datetime,
) -> None:
    """REQ-07: TTL expirado busca na fonte e grava com fetched_at atual."""
    repository.rows.append(make_stored_quote(rate="4.900000", fetched_at=now - timedelta(hours=2)))
    frankfurter = _ok(RateSource.FRANKFURTER, make_rate_quote, "5.500000")
    service = _service(repository, [frankfurter], utc_clock, mono_clock)

    quote = await service.get_quote(Currency.USD)

    assert frankfurter.calls == 1
    assert str(quote.rate) == "5.500000"
    assert quote.stale is False
    assert len(repository.saved) == 1
    assert repository.saved[0].fetched_at == now
    assert str(repository.saved[0].rate) == "5.500000"


async def test_falls_back_from_frankfurter_to_ptax_req01(
    repository: Any, make_rate_quote: Any, utc_clock: Any, mono_clock: Any,
) -> None:
    """REQ-01: Frankfurter falha, a PTAX responde e só a PTAX é gravada (§4)."""
    frankfurter = _failing(RateSource.FRANKFURTER)
    ptax = _ok(RateSource.PTAX, make_rate_quote, "5.420600")
    service = _service(repository, [frankfurter, ptax], utc_clock, mono_clock)

    quote = await service.get_quote(Currency.USD)

    assert quote.source == RateSource.PTAX
    assert (frankfurter.calls, ptax.calls) == (1, 1)
    assert [saved.source for saved in repository.saved] == ["ptax"]


async def test_first_provider_success_stops_the_chain_req01(
    repository: Any, make_rate_quote: Any, utc_clock: Any, mono_clock: Any,
) -> None:
    """REQ-01: com a primária disponível, a PTAX não é chamada."""
    frankfurter = _ok(RateSource.FRANKFURTER, make_rate_quote, "5.000000")
    ptax = _ok(RateSource.PTAX, make_rate_quote)
    service = _service(repository, [frankfurter, ptax], utc_clock, mono_clock)

    await service.get_quote(Currency.USD)

    assert ptax.calls == 0


async def test_provider_with_open_circuit_is_skipped_req01(
    repository: Any, make_rate_quote: Any, utc_clock: Any, mono_clock: Any,
) -> None:
    """REQ-01: provedor com circuito aberto é pulado sem ser chamado (§4)."""
    frankfurter = _ok(RateSource.FRANKFURTER, make_rate_quote, "5.000000")
    ptax = _ok(RateSource.PTAX, make_rate_quote)
    tripped = _breaker(mono_clock)
    for _ in range(3):
        tripped.record_failure()
    service = _service(
        repository, [frankfurter, ptax], utc_clock, mono_clock,
        breakers=[tripped, _breaker(mono_clock)],
    )

    quote = await service.get_quote(Currency.USD)

    assert frankfurter.calls == 0
    assert quote.source == RateSource.PTAX


async def test_three_failed_requests_open_circuit_req01(
    repository: Any, make_rate_quote: Any, utc_clock: Any, mono_clock: Any,
) -> None:
    """REQ-01: três falhas seguidas da primária abrem o circuito; a quarta a pula."""
    frankfurter = _failing(RateSource.FRANKFURTER)
    ptax = _ok(RateSource.PTAX, make_rate_quote)
    service = _service(repository, [frankfurter, ptax], utc_clock, mono_clock)
    for _ in range(3):
        utc_clock.advance(TTL_SECONDS + 1)
        await service.get_quote(Currency.USD)
    assert frankfurter.calls == 3

    utc_clock.advance(TTL_SECONDS + 1)
    await service.get_quote(Currency.USD)

    assert (frankfurter.calls, ptax.calls) == (3, 4)


async def test_all_sources_failing_returns_stale_cache_req01(
    repository: Any, make_stored_quote: Any, utc_clock: Any, mono_clock: Any, now: datetime,
) -> None:
    """Falha geral devolve a última linha do cache com stale=true, sem regravar (§4)."""
    repository.rows.append(make_stored_quote(rate="4.900000", fetched_at=now - timedelta(hours=5)))
    service = _service(
        repository, [_failing(RateSource.FRANKFURTER), _failing(RateSource.PTAX)],
        utc_clock, mono_clock,
    )

    quote = await service.get_quote(Currency.USD)

    assert quote.stale is True
    assert str(quote.rate) == "4.900000"
    assert quote.quoted_at == repository.rows[0].quoted_at
    assert repository.saved == []


async def test_no_cache_and_all_sources_failing_raises_unavailable_req01(
    repository: Any, utc_clock: Any, mono_clock: Any,
) -> None:
    """Sem cache e sem fonte: RatesUnavailableError (503), nada gravado (§4)."""
    service = _service(
        repository, [_failing(RateSource.FRANKFURTER), _failing(RateSource.PTAX)],
        utc_clock, mono_clock,
    )

    with pytest.raises(RatesUnavailableError):
        await service.get_quote(Currency.USD)
    assert repository.saved == []


async def test_rejected_quote_is_never_saved_req01(
    repository: Any, make_rate_quote: Any, utc_clock: Any, mono_clock: Any,
) -> None:
    """Cotação reprovada no aceite vira falha da fonte e não é gravada (§4, §8.1)."""
    rejected = FakeProvider(RateSource.FRANKFURTER, error=ProviderError("fora do aceite"))
    service = _service(repository, [rejected, _failing(RateSource.PTAX)], utc_clock, mono_clock)

    with pytest.raises(RatesUnavailableError):
        await service.get_quote(Currency.USD)
    assert repository.saved == []

    ptax = _ok(RateSource.PTAX, make_rate_quote, "5.420600")
    fallback = _service(repository, [rejected, ptax], utc_clock, mono_clock)
    await fallback.get_quote(Currency.USD)
    assert [saved.source for saved in repository.saved] == ["ptax"]


async def test_ten_requests_within_ttl_cut_network_calls_by_half_req07(
    repository: Any, make_rate_quote: Any, utc_clock: Any, mono_clock: Any,
) -> None:
    """REQ-07: 10 requisições no TTL cortam as chamadas de rede em pelo menos 50 %.

    A linha de base esvazia o repositório antes de cada requisição, então todas
    chegam à fonte, como aconteceria sem cache.
    """
    baseline = _ok(RateSource.FRANKFURTER, make_rate_quote, "5.000000")
    no_cache = _service(repository, [baseline], utc_clock, mono_clock)
    for _ in range(10):
        repository.clear()
        await no_cache.get_quote(Currency.USD)

    cached = _ok(RateSource.FRANKFURTER, make_rate_quote, "5.000000")
    with_cache = _service(repository, [cached], utc_clock, mono_clock)
    repository.clear()
    for _ in range(10):
        await with_cache.get_quote(Currency.USD)

    assert baseline.calls == 10
    assert cached.calls <= baseline.calls * 0.5, (
        f"esperado redução de pelo menos 50 %; sem cache {baseline.calls} chamadas, "
        f"com cache {cached.calls}"
    )
