"""Lifespan da aplicação com ``TestClient`` em ``with`` (spec backend-mvp-v1, §7; REQ-01).

Ao contrário do restante da integração, aqui o lifespan roda: lê ``COGME_DATABASE_URL``, cria o
engine, o cliente HTTP e o ``RateService``. Não há rede nem banco: o engine só conecta no
primeiro uso, e ``/v1/health`` não consulta nada. A URL é sintética e aponta para uma porta
local sem servidor; se algo tentasse conectar, falharia em vez de sair para fora.

O cache de ``get_settings`` é limpo antes e depois de cada teste, e o nível do logger ``src``,
que o lifespan ajusta, é restaurado.
"""

from __future__ import annotations

import logging
from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from src.backend.config import get_settings
from src.backend.main import app
from src.backend.services.rate_service import RateService

DATABASE_VAR = "COGME_DATABASE_URL"
# Credencial sintética; a URL não usa o padrão de senha que o scanner do CI rejeita.
SECRET = "segredo-sintetico-do-teste"
VALID_URL = f"postgresql+asyncpg://cogme_teste:{SECRET}@127.0.0.1:1/cogme_teste"
WRONG_SCHEME_URL = f"mysql://cogme_teste:{SECRET}@127.0.0.1:1/cogme_teste"


@pytest.fixture(autouse=True)
def _isolated_settings() -> Iterator[None]:
    """Limpa o cache de ``Settings`` antes e depois, e restaura o nível do logger ``src``."""
    level = logging.getLogger("src").level
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()
    logging.getLogger("src").setLevel(level)


def test_startup_builds_rate_service_and_health_answers(monkeypatch: pytest.MonkeyPatch) -> None:
    """Com a URL do banco, o lifespan monta o RateService e ``/v1/health`` responde."""
    monkeypatch.setenv(DATABASE_VAR, VALID_URL)

    with TestClient(app) as client:
        assert isinstance(app.state.rate_service, RateService)
        response = client.get("/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_missing_database_url_fails_startup(monkeypatch: pytest.MonkeyPatch) -> None:
    """Sem ``COGME_DATABASE_URL`` a subida falha (fail-closed) e o erro aponta só o campo."""
    monkeypatch.delenv(DATABASE_VAR, raising=False)

    with pytest.raises(ValidationError) as info:
        with TestClient(app):
            pass

    assert [error["type"] for error in info.value.errors()] == ["missing"]
    assert info.value.errors()[0]["loc"] == ("database_url",)


def test_invalid_database_url_fails_startup_without_echo(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """URL com driver errado falha a subida, e nem a URL nem a credencial aparecem no erro."""
    monkeypatch.setenv(DATABASE_VAR, WRONG_SCHEME_URL)

    with pytest.raises(ValidationError) as info:
        with TestClient(app):
            pass

    text = f"{info.value}\n{info.value!r}"
    assert SECRET not in text
    assert WRONG_SCHEME_URL not in text
    assert "mysql://" not in text
