"""Falhas do repositório de cotações sob o RateService (spec backend-mvp-v1, §4; REQ-01, REQ-07).

Regras: falha ao ler o cache equivale a cache ausente e segue para as fontes; falha ao gravar
não impede devolver a cotação válida; linha de cache fora do contrato é tratada como ausência.
Repositório, provedores e relógios são falsos. Os logs trazem só o tipo da causa.
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta
from typing import Any

import pytest

from src.backend.errors import RatesUnavailableError
from src.backend.models.repository import RepositoryError, StoredQuote
from src.backend.services.circuit_breaker import CircuitBreaker
from src.backend.services.rate_providers import ProviderError
from src.backend.services.rate_service import RateService
from src.shared.schemas import Currency, RateQuote, RateSource

TTL_SECONDS = 3600
SERVICE_LOGGER = "src.backend.services.rate_service"
_SECRET_CAUSE_TEXT = "texto sintético da causa, que nunca deve ir para o log"


class FailingRepository:
    """Repositório falso que falha sob demanda, com a causa real em ``__cause__``.

    Attributes:
        rows: Linhas existentes; ``get_latest`` devolve a de maior ``fetched_at``.
        saved: Gravações concluídas.
    """

    def __init__(
        self,
        rows: list[StoredQuote] | None = None,
        *,
        fail_read: bool = False,
        fail_write: bool = False,
    ) -> None:
        self.rows: list[StoredQuote] = list(rows or [])
        self.saved: list[StoredQuote] = []
        self._fail_read = fail_read
        self._fail_write = fail_write

    async def get_latest(self, currency: str) -> StoredQuote | None:
        """Falha se configurado; senão devolve a linha mais recente da moeda."""
        if self._fail_read:
            raise RepositoryError("Falha ao ler a cotação.") from OSError(_SECRET_CAUSE_TEXT)
        matching = [quote for quote in self.rows if quote.currency == currency]
        if not matching:
            return None
        return max(reversed(matching), key=lambda quote: quote.fetched_at)

    async def save(self, quote: StoredQuote) -> None:
        """Falha se configurado; senão registra a gravação."""
        if self._fail_write:
            raise RepositoryError("Falha ao gravar a cotação.") from OSError(_SECRET_CAUSE_TEXT)
        self.rows.append(quote)
        self.saved.append(quote)


class ForcedRowRepository:
    """Repositório que devolve sempre a mesma linha, para simular cache fora do contrato."""

    def __init__(self, row: StoredQuote) -> None:
        self._row = row
        self.saved: list[StoredQuote] = []

    async def get_latest(self, currency: str) -> StoredQuote | None:
        """Devolve a linha fixa, qualquer que seja a moeda pedida."""
        del currency
        return self._row

    async def save(self, quote: StoredQuote) -> None:
        """Registra a gravação."""
        self.saved.append(quote)


class FakeProvider:
    """Provedor falso: devolve a cotação configurada ou levanta o erro configurado.

    Attributes:
        name: Fonte que o provedor representa.
        calls: Chamadas a ``fetch``.
    """

    def __init__(
        self,
        name: RateSource,
        *,
        quote: RateQuote | None = None,
        error: Exception | None = None,
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


def _ok(name: RateSource, make_rate_quote: Any, rate: str) -> FakeProvider:
    """Provedor que sempre responde com uma cotação sintética de ``rate``."""
    return FakeProvider(name, quote=make_rate_quote(rate=rate, source=name.value))


def _failing(name: RateSource) -> FakeProvider:
    """Provedor que sempre falha com ProviderError."""
    return FakeProvider(name, error=ProviderError("falha simulada da fonte"))


def _service(
    repository: Any,
    providers: list[FakeProvider],
    utc_clock: Any,
    mono_clock: Any,
) -> RateService:
    """Monta o RateService com circuitos novos e relógios falsos."""
    circuits = [
        CircuitBreaker(failure_threshold=3, reset_seconds=60.0, clock=mono_clock)
        for _ in providers
    ]
    return RateService(
        repository=repository,
        providers=list(zip(providers, circuits, strict=True)),
        ttl_seconds=TTL_SECONDS,
        now=utc_clock,
    )


async def test_read_failure_falls_through_to_providers_req07(
    make_rate_quote: Any,
    utc_clock: Any,
    mono_clock: Any,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """REQ-07: falha ao ler o cache segue para a fonte, devolve a cotação e grava (§4)."""
    repository = FailingRepository(fail_read=True)
    frankfurter = _ok(RateSource.FRANKFURTER, make_rate_quote, "5.420600")
    service = _service(repository, [frankfurter], utc_clock, mono_clock)

    with caplog.at_level(logging.WARNING, logger=SERVICE_LOGGER):
        quote = await service.get_quote(Currency.USD)

    assert frankfurter.calls == 1
    assert str(quote.rate) == "5.420600"
    assert quote.stale is False
    assert [str(saved.rate) for saved in repository.saved] == ["5.420600"]
    assert "quote_cache_read_failed cause=OSError" in caplog.text
    assert _SECRET_CAUSE_TEXT not in caplog.text


async def test_read_failure_with_all_providers_down_is_unavailable_req01(
    make_rate_quote: Any,
    utc_clock: Any,
    mono_clock: Any,
) -> None:
    """REQ-01: falha de leitura conta como cache ausente; sem fonte, vira 503 e nada é gravado."""
    repository = FailingRepository(fail_read=True)
    service = _service(
        repository,
        [_failing(RateSource.FRANKFURTER), _failing(RateSource.PTAX)],
        utc_clock,
        mono_clock,
    )

    with pytest.raises(RatesUnavailableError):
        await service.get_quote(Currency.USD)
    assert repository.saved == []


async def test_write_failure_still_returns_the_valid_quote_req07(
    make_rate_quote: Any,
    utc_clock: Any,
    mono_clock: Any,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """REQ-07: falha ao gravar não derruba a cotação válida obtida da fonte (§4)."""
    repository = FailingRepository(fail_write=True)
    frankfurter = _ok(RateSource.FRANKFURTER, make_rate_quote, "5.430000")
    service = _service(repository, [frankfurter], utc_clock, mono_clock)

    with caplog.at_level(logging.WARNING, logger=SERVICE_LOGGER):
        quote = await service.get_quote(Currency.USD)

    assert str(quote.rate) == "5.430000"
    assert quote.source == RateSource.FRANKFURTER
    assert quote.stale is False
    assert frankfurter.calls == 1
    assert repository.saved == []
    assert "quote_cache_write_failed cause=OSError" in caplog.text
    assert _SECRET_CAUSE_TEXT not in caplog.text


async def test_read_and_write_failure_together_still_quote_req01(
    make_rate_quote: Any,
    utc_clock: Any,
    mono_clock: Any,
) -> None:
    """REQ-01: com leitura e gravação quebradas, a fonte ainda responde ao cliente."""
    repository = FailingRepository(fail_read=True, fail_write=True)
    ptax = _ok(RateSource.PTAX, make_rate_quote, "5.440000")
    service = _service(
        repository,
        [_failing(RateSource.FRANKFURTER), ptax],
        utc_clock,
        mono_clock,
    )

    quote = await service.get_quote(Currency.USD)

    assert quote.source == RateSource.PTAX
    assert str(quote.rate) == "5.440000"
    assert ptax.calls == 1


@pytest.mark.parametrize(
    "row_overrides",
    [
        {"currency": "GBP"},
        {"source": "outra"},
        {"rate": "4.1234567"},
        {"rate": "1000.000000"},
    ],
    ids=["moeda_fora_do_enum", "fonte_fora_do_enum", "taxa_com_7_casas", "taxa_no_teto"],
)
async def test_out_of_contract_row_is_treated_as_absent_req07(
    row_overrides: dict[str, str],
    make_stored_quote: Any,
    make_rate_quote: Any,
    utc_clock: Any,
    mono_clock: Any,
    now: datetime,
) -> None:
    """REQ-07: linha de cache fora do contrato, mesmo fresca, é ausência: a fonte é consultada.

    A cotação que sai é a da fonte; a linha ruim não aparece no resultado nem é gravada de novo.
    """
    bad_row = make_stored_quote(fetched_at=now, **row_overrides)
    repository = ForcedRowRepository(bad_row)
    frankfurter = _ok(RateSource.FRANKFURTER, make_rate_quote, "5.450000")
    service = _service(repository, [frankfurter], utc_clock, mono_clock)

    quote = await service.get_quote(Currency.USD)

    assert frankfurter.calls == 1
    assert str(quote.rate) == "5.450000"
    assert quote.stale is False


@pytest.mark.parametrize(
    "row_overrides",
    [{"currency": "GBP"}, {"rate": "4.1234567"}],
    ids=["moeda_fora_do_enum", "taxa_com_7_casas"],
)
async def test_out_of_contract_row_is_never_served_as_stale_req01(
    row_overrides: dict[str, str],
    make_stored_quote: Any,
    utc_clock: Any,
    mono_clock: Any,
    now: datetime,
) -> None:
    """REQ-01: linha inválida não vira cotação vencida; sem fonte, a resposta é 503."""
    bad_row = make_stored_quote(fetched_at=now - timedelta(hours=5), **row_overrides)
    repository = ForcedRowRepository(bad_row)
    service = _service(
        repository,
        [_failing(RateSource.FRANKFURTER), _failing(RateSource.PTAX)],
        utc_clock,
        mono_clock,
    )

    with pytest.raises(RatesUnavailableError):
        await service.get_quote(Currency.USD)
    assert repository.saved == []
