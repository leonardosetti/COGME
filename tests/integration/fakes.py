"""Dublês dos testes de integração: provedores, repositório em memória e relógios falsos.

Tudo sintético. Nenhum dublê acessa rede, arquivo ou relógio real. O ``RateService`` usado nos
testes é o real; só as fontes externas e o repositório são substituídos.
"""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from decimal import Decimal
from typing import Any

from src.backend.models.repository import StoredQuote
from src.backend.services.circuit_breaker import CircuitBreaker
from src.backend.services.rate_providers import ProviderError
from src.backend.services.rate_service import RateService
from src.shared.schemas import Currency, RateQuote, RateSource

SYNTHETIC_NOW: datetime = datetime(2026, 10, 30, 16, 0, 0, tzinfo=UTC)
SYNTHETIC_QUOTED_AT: datetime = datetime(2026, 10, 30, 0, 0, 0, tzinfo=UTC)

SIMULATE: str = "/v1/simulate"

# Exemplo da §2 (USD, hourly, 30 × 160, cotação 5, spread 2, IOF 0,38), como texto JSON.
SPEC_EXAMPLE_BODY: dict[str, Any] = {
    "currency": "USD",
    "regime": "hourly",
    "amount": "30",
    "quantity": "160",
    "spread_pct": "2",
    "iof_pct": "0.38",
}


def error_of(response: Any, status: int, key: str, message: str) -> dict[str, Any]:
    """Confere o envelope canônico de erro e devolve o conteúdo de ``error``.

    Args:
        response: Resposta HTTP.
        status: Status esperado.
        key: Chave esperada.
        message: Mensagem PT-BR esperada.

    Returns:
        O dicionário ``error`` da resposta.
    """
    assert response.status_code == status
    body = response.json()
    assert set(body) == {"error"}
    assert set(body["error"]) == {"key", "message", "details"}
    assert body["error"]["key"] == key
    assert body["error"]["message"] == message
    return dict(body["error"])


class FixedClock:
    """Relógio UTC falso, chamável como ``RateService.now``; avança só por ``advance``."""

    def __init__(self, start: datetime = SYNTHETIC_NOW) -> None:
        self.current = start

    def __call__(self) -> datetime:
        """Devolve o instante falso."""
        return self.current

    def advance(self, seconds: float) -> None:
        """Avança o relógio falso."""
        self.current += timedelta(seconds=seconds)


class FixedMonotonic:
    """Relógio monotônico falso, chamável como ``time.monotonic``; avança só por ``advance``."""

    def __init__(self) -> None:
        self.seconds = 0.0

    def __call__(self) -> float:
        """Devolve o instante falso, em segundos."""
        return self.seconds

    def advance(self, seconds: float) -> None:
        """Avança o relógio falso."""
        self.seconds += seconds


class ScriptedProvider:
    """Provedor que devolve uma taxa fixa ou levanta um erro, e conta as chamadas.

    Attributes:
        name: Fonte que o provedor representa.
        calls: Número de chamadas a ``fetch``; é a medida de tráfego de rede.
    """

    def __init__(
        self,
        name: RateSource,
        *,
        rate: str = "5.000000",
        bulletin: str | None = None,
        error: Exception | None = None,
    ) -> None:
        self.name = name
        self.calls = 0
        self._rate = rate
        self._bulletin = bulletin
        self._error = error

    async def fetch(self, currency: Currency) -> RateQuote:
        """Conta a chamada e devolve a cotação sintética ou levanta o erro configurado."""
        self.calls += 1
        if self._error is not None:
            raise self._error
        return RateQuote(
            currency=currency,
            rate=Decimal(self._rate),
            source=self.name,
            quoted_at=SYNTHETIC_QUOTED_AT,
            bulletin=self._bulletin,
            stale=False,
        )


def failing_provider(name: RateSource) -> ScriptedProvider:
    """Provedor que sempre falha com ``ProviderError``, como uma fonte fora do ar."""
    return ScriptedProvider(name, error=ProviderError("falha simulada da fonte"))


class MemoryRepository:
    """Repositório em memória que cumpre o contrato ``QuoteRepository``.

    Attributes:
        rows: Linhas existentes.
        saved: Gravações feitas por ``save``, na ordem em que ocorreram.
    """

    def __init__(self, rows: list[StoredQuote] | None = None) -> None:
        self.rows: list[StoredQuote] = list(rows or [])
        self.saved: list[StoredQuote] = []

    async def get_latest(self, currency: str) -> StoredQuote | None:
        """Devolve a linha de maior ``fetched_at`` da moeda; em empate vence a última gravada."""
        matching = [row for row in self.rows if row.currency == currency]
        if not matching:
            return None
        return max(reversed(matching), key=lambda row: row.fetched_at)

    async def save(self, quote: StoredQuote) -> None:
        """Registra a gravação."""
        self.rows.append(quote)
        self.saved.append(quote)


def stored_quote(**overrides: object) -> StoredQuote:
    """Monta uma linha de cache sintética; ``fetched_at`` padrão é ``SYNTHETIC_NOW``.

    Args:
        **overrides: Campos a trocar em relação ao padrão.

    Returns:
        A linha de cache.
    """
    values: dict[str, object] = {
        "currency": "USD",
        "rate": Decimal("5.000000"),
        "source": "frankfurter",
        "bulletin": None,
        "quoted_at": SYNTHETIC_QUOTED_AT,
        "fetched_at": SYNTHETIC_NOW,
    }
    values.update(overrides)
    return StoredQuote(**values)  # type: ignore[arg-type]


def build_service(
    *,
    repository: MemoryRepository | None = None,
    providers: list[ScriptedProvider] | None = None,
    clock: FixedClock | None = None,
    monotonic: FixedMonotonic | None = None,
    ttl_seconds: int = 3600,
) -> RateService:
    """Monta o ``RateService`` real com dublês; cada provedor ganha um circuito novo.

    Args:
        repository: Repositório falso; vazio por padrão.
        providers: Fontes na ordem de preferência; Frankfurter com taxa 5.000000 por padrão.
        clock: Relógio UTC falso.
        monotonic: Relógio monotônico falso dos circuitos.
        ttl_seconds: Idade máxima do cache.

    Returns:
        O serviço pronto para uso.
    """
    mono = monotonic or FixedMonotonic()
    chosen = providers if providers is not None else [ScriptedProvider(RateSource.FRANKFURTER)]
    return RateService(
        repository=repository or MemoryRepository(),
        providers=[
            (provider, CircuitBreaker(failure_threshold=3, reset_seconds=60.0, clock=mono))
            for provider in chosen
        ],
        ttl_seconds=ttl_seconds,
        now=clock or FixedClock(),
    )
