"""Testes de unitários de services/invoice_number.py (DEC-06).

Usa AsyncSession falso para não depender de PL/pgSQL nem de banco real.
"""

from __future__ import annotations

from typing import Any

import pytest
from sqlalchemy.exc import SQLAlchemyError

from src.backend.models.invoice_repository import RepositoryError
from src.backend.services.invoice_number import InvoiceNumberService


class _FakeResult:
    """Resultado falso de session.execute: devolve um escalar fixo."""

    def __init__(self, scalar: str) -> None:
        self._scalar = scalar

    def scalar_one(self) -> str:
        return self._scalar


class _FakeSession:
    """Sessão falsa que registra a chamada e devolve o escalar configurado."""

    def __init__(self, scalar: str = "INV-202611-0001") -> None:
        self._scalar = scalar
        self.calls: list[tuple[str, dict[str, str]]] = []

    async def execute(
        self, sql: Any, params: dict[str, str]
    ) -> _FakeResult:
        """Registra a chamada e devolve o resultado falso."""
        self.calls.append((str(sql), dict(params)))
        return _FakeResult(self._scalar)


@pytest.fixture
def session() -> _FakeSession:
    """Sessão falsa limpa."""
    return _FakeSession()


@pytest.fixture
def service(session: _FakeSession) -> InvoiceNumberService:
    """Serviço com sessão falsa."""
    return InvoiceNumberService(session)


async def test_generate_devolve_numero_formatado(
    service: InvoiceNumberService, session: _FakeSession
) -> None:
    """generate() chama a function PL/pgSQL e devolve o número formatado."""
    numero = await service.generate("12345678000195")
    assert numero == "INV-202611-0001"
    assert len(session.calls) == 1
    sql, params = session.calls[0]
    assert "next_invoice_number" in sql
    assert params == {"issuer": "12345678000195"}


async def test_generate_repassa_issuer_tax_id(
    service: InvoiceNumberService, session: _FakeSession
) -> None:
    """generate() repassa o issuer_tax_id_digits como parâmetro :issuer."""
    await service.generate("98765432000100")
    sql, params = session.calls[0]
    assert params == {"issuer": "98765432000100"}


async def test_generate_sqlalchemy_error_via_repository_error(
    service: InvoiceNumberService, session: _FakeSession
) -> None:
    """SQLAlchemyError é traduzido para RepositoryError."""

    async def explodir(*args: Any, **kwargs: Any) -> _FakeResult:
        raise SQLAlchemyError("banco fora do ar")

    session.execute = explodir  # type: ignore[method-assign]
    with pytest.raises(RepositoryError):
        await service.generate("12345678000195")


async def test_generate_varios_emissores_sao_independentes(
    service: InvoiceNumberService, session: _FakeSession
) -> None:
    """Chamadas para emissores diferentes são registradas separadamente."""
    await service.generate("11111111000111")
    await service.generate("22222222000222")
    assert len(session.calls) == 2
    assert session.calls[0][1] == {"issuer": "11111111000111"}
    assert session.calls[1][1] == {"issuer": "22222222000222"}
