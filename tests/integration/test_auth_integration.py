"""Testes de integração para rotas de autenticação (auth.py).

Cobrem os handlers de register, login e logout que ainda não têm cobertura
no relatório de cobertura. Usam o banco de teste efêmero PostgreSQL.
Cada teste é isolado (um endpoint por teste) para evitar conflito de loop
de eventos do anyio entre requisições sequenciais.
"""

from __future__ import annotations

from decimal import Decimal
from datetime import datetime, timezone

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from src.backend.main import app
from src.backend.models.database import create_session_factory
from src.backend.config import get_settings


@pytest.fixture
def client() -> TestClient:
    """TestClient configurado com engine de banco de teste."""
    engine = create_async_engine(
        "postgresql+asyncpg://cogme:dummy-test-local@127.0.0.1:5434/cogme_test",
        echo=False,
    )
    session_factory = create_session_factory(engine)

    app.state.engine = engine
    app.state.session_factory = session_factory
    app.state.login_pepper = get_settings().login_pepper

    yield TestClient(app)


def test_register_email(client: TestClient) -> None:
    """Cadastro usando email como identificador."""
    register_payload = {
        "identifier": "register.teste@exemplo.com",
        "password": "SenhaForte123",
        "name": "Usuário Registro",
    }
    response = client.post("/v1/auth/register", json=register_payload)
    assert response.status_code in (201, 409), response.text


def test_register_cpf(client: TestClient) -> None:
    """Cadastro usando CPF como identificador."""
    register_payload = {
        "identifier": "12345678902",
        "password": "SenhaForte123",
        "name": "Usuário CPF",
    }
    response = client.post("/v1/auth/register", json=register_payload)
    assert response.status_code in (201, 409), response.text


def test_login_invalid_credentials(client: TestClient) -> None:
    """Login com credenciais inválidas deve retornar 401."""
    login_payload = {
        "identifier": "nao.existe@exemplo.com",
        "password": "senhaerrada",
    }
    response = client.post("/v1/auth/login", json=login_payload)
    assert response.status_code == 401, response.text


def test_logout_without_session(client: TestClient) -> None:
    """Logout sem sessão deve retornar 401 (não autenticado) ou 403 (CSRF)."""
    response = client.post("/v1/auth/logout")
    assert response.status_code in (401, 403), response.text


def test_me_without_session(client: TestClient) -> None:
    """GET /me sem sessão deve retornar 401."""
    response = client.get("/v1/auth/me")
    assert response.status_code == 401, response.text


def test_aliases_without_session(client: TestClient) -> None:
    """GET /aliases sem sessão deve retornar 401."""
    response = client.get("/v1/auth/aliases")
    assert response.status_code == 401, response.text


def test_reset_request(client: TestClient) -> None:
    """Solicitação de reset de senha deve retornar 200 (mesmo se não existir)."""
    payload = {
        "identifier": "qualquer@exemplo.com",
    }
    response = client.post("/v1/auth/password/reset-request", json=payload)
    assert response.status_code == 200, response.text


def test_email_resend(client: TestClient) -> None:
    """Reenvio de verificação deve retornar 200 (mesmo se não existir)."""
    payload = {
        "identifier": "qualquer@exemplo.com",
    }
    response = client.post("/v1/auth/email/resend", json=payload)
    assert response.status_code == 200, response.text


def test_reset_confirm_invalid_token(client: TestClient) -> None:
    """Reset confirm com token inválido deve retornar 403."""
    payload = {
        "token": "token-invalido-xyz",
        "new_password": "NovaSenha123",
    }
    response = client.post("/v1/auth/password/reset-confirm", json=payload)
    assert response.status_code == 403, response.text


def test_email_verify_invalid_token(client: TestClient) -> None:
    """Email verify com token inválido deve retornar 400."""
    payload = {
        "token": "token-invalido-xyz",
    }
    response = client.post("/v1/auth/email/verify", json=payload)
    assert response.status_code == 400, response.text


def test_me_and_aliases_with_session(client: TestClient) -> None:
    """Login, depois acessa /me e /aliases com sessão ativa."""
    # Cadastro
    register_payload = {
        "identifier": "session.teste@exemplo.com",
        "password": "SenhaForte123",
        "name": "Usuário Sessão",
    }
    client.post("/v1/auth/register", json=register_payload)

    # Login (deve definir cookie de sessão)
    login_payload = {
        "identifier": "session.teste@exemplo.com",
        "password": "SenhaForte123",
    }
    login_resp = client.post("/v1/auth/login", json=login_payload)
    assert login_resp.status_code == 200, login_resp.text

    # /me com sessão
    me_resp = client.get("/v1/auth/me")
    assert me_resp.status_code == 200, me_resp.text

    # /aliases com sessão
    aliases_resp = client.get("/v1/auth/aliases")
    assert aliases_resp.status_code == 200, aliases_resp.text
