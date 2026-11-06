"""Testes focados para cobrir linhas missing do relatório de cobertura."""

from datetime import datetime

import pytest

from src.backend.config import Settings
from src.backend.main import _message_for


def test_config_log_level_not_string():
    with pytest.raises(ValueError, match="O nível de log deve ser um texto"):
        Settings.model_validate({
            "database_url": "postgresql+asyncpg://localhost/db",
            "log_level": 123})


def test_config_log_level_invalid():
    with pytest.raises(ValueError, match="Nível de log inválido"):
        Settings.model_validate({
            "database_url": "postgresql+asyncpg://localhost/db",
            "log_level": "BOGUS"})


def test_message_for_custom_message():
    assert _message_for("meu_tipo_personalizado", "erro customizado") == "erro customizado"


def test_rate_service_repository_timeout_budget():
    from src.backend.services.rate_service import RateService
    with pytest.raises(ValueError, match="orçamento do repositório"):
        RateService(
            repository=None,
            providers=[],
            ttl_seconds=60,
            now=None,
            repository_timeout=10,
            total_timeout=20,
        )


def test_accept_rate_rejects():
    from decimal import Decimal, InvalidOperation
    from src.backend.services.rate_providers import _accept_rate
    assert _accept_rate(Decimal("5.5")) == Decimal("5.5")
    with pytest.raises(Exception):
        _accept_rate("não é decimal")
    with pytest.raises(Exception):
        _accept_rate(Decimal("Infinity"))
    with pytest.raises(Exception):
        _accept_rate(Decimal("999999999"))


def test_accept_bulletin_rejects():
    from src.backend.services.rate_providers import _accept_bulletin
    assert _accept_bulletin("2024-01-15") == "2024-01-15"
    with pytest.raises(Exception):
        _accept_bulletin(123)
    with pytest.raises(Exception):
        _accept_bulletin("x" * 200)
    with pytest.raises(Exception):
        _accept_bulletin("\x00")


def test_brasilia_to_utc():
    from src.backend.services.rate_providers import _brasilia_to_utc
    from datetime import datetime
    result = _brasilia_to_utc("2024-01-15T10:00:00")
    assert isinstance(result, datetime)
    with pytest.raises(Exception):
        _brasilia_to_utc("2024-01-15T10:00:00+00:00")


def test_handle_http_error_400():
    import asyncio
    from starlette.exceptions import HTTPException
    from src.backend.main import _handle_http_error
    from starlette.requests import Request
    scope = {"type": "http", "method": "GET", "path": "/x", "headers": [], "query_string": b"", "client": None, "server": None}
    req = Request(scope)
    resp = asyncio.run(_handle_http_error(req, HTTPException(status_code=400, detail="bad")))
    assert resp.status_code == 400


def test_gross_period_requires_quantity():
    from decimal import Decimal
    from src.backend.services.calculator import _gross
    from src.shared.schemas import Regime
    with pytest.raises(ValueError, match="Regime por período exige quantidade"):
        _gross("periodo", Decimal("10"), None)


def test_refusing_url_fetcher():
    from src.backend.services.invoice_service import _RefusingUrlFetcher
    with pytest.raises(ValueError, match="Busca de recurso externo recusada"):
        _RefusingUrlFetcher()("http://example.com/x")


def test_as_utc_naive_rejected():
    from datetime import datetime
    from src.shared.schemas import _as_utc
    with pytest.raises(Exception):
        _as_utc(datetime(2024, 1, 15, 10, 0, 0))
