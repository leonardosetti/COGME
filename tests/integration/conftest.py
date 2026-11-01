"""Fixtures de tests/integration/: cliente HTTP com o RateService real e fontes falsas.

O ``TestClient`` é criado sem ``with``: assim o ``lifespan`` não roda, e a API não abre banco,
não lê ``COGME_DATABASE_URL`` nem cria cliente HTTP real. A dependência ``get_rate_service`` é
substituída por um ``RateService`` montado com dublês. Sem rede e sem relógio real.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator

import pytest
from fastapi.testclient import TestClient

from src.backend.main import app
from src.backend.routers.common import get_rate_service
from src.backend.services.rate_service import RateService
from src.shared.schemas import RateSource

from .fakes import FixedClock, FixedMonotonic, ScriptedProvider, build_service


@pytest.fixture
def clock() -> FixedClock:
    """Relógio UTC falso, começando em 2026-10-30 16:00 UTC."""
    return FixedClock()


@pytest.fixture
def monotonic_clock() -> FixedMonotonic:
    """Relógio monotônico falso dos circuitos."""
    return FixedMonotonic()


@pytest.fixture
def serve_rates() -> Iterator[Callable[[RateService], None]]:
    """Troca o ``RateService`` que a API usa; desfaz a troca ao fim do teste."""

    def _serve(service: RateService) -> None:
        app.dependency_overrides[get_rate_service] = lambda: service

    yield _serve
    app.dependency_overrides.clear()


@pytest.fixture
def rates_service(clock: FixedClock, monotonic_clock: FixedMonotonic) -> RateService:
    """Serviço padrão: Frankfurter responde 5.000000 (primária), PTAX é reserva, cache vazio."""
    return build_service(
        providers=[
            ScriptedProvider(RateSource.FRANKFURTER, rate="5.000000"),
            ScriptedProvider(RateSource.PTAX, rate="5.420600", bulletin="Fechamento"),
        ],
        clock=clock,
        monotonic=monotonic_clock,
    )


@pytest.fixture
def client(serve_rates: Callable[[RateService], None], rates_service: RateService) -> TestClient:
    """Cliente da API já ligado ao serviço padrão."""
    serve_rates(rates_service)
    return TestClient(app)
