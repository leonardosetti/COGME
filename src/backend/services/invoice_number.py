"""Serviço de numeração de invoices (DEC-06).

Wrapper da function PL/pgSQL `next_invoice_number` atômica.
"""

from __future__ import annotations

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.models.invoice_repository import RepositoryError


class InvoiceNumberService:
    """Gera números de invoice sequenciais por emissor/mês."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def generate(self, issuer_tax_id_digits: str) -> str:
        """Chama function PL/pgSQL atômica; retorna 'INV-202611-0001'.

        A function garante:
        - Sequencial por (issuer_tax_id_digits, year_month)
        - Sem gaps visíveis (retry em race condition)
        - Atômica via UPDATE ... RETURNING + INSERT ON CONFLICT
        """
        try:
            result = await self._session.execute(
                text("SELECT next_invoice_number(:issuer)"),
                {"issuer": issuer_tax_id_digits},
            )
            return str(result.scalar_one())
        except SQLAlchemyError as error:
            raise RepositoryError("Falha ao gerar número de invoice.") from error
