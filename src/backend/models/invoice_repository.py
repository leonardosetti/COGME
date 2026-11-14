"""Repositório de invoices (DEC-04, DEC-05, DEC-06, DEC-07).

Contrato de acesso usado pela camada de serviços. Implementação concreta
usa SQLAlchemy assíncrono com sessão por operação.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Final, Protocol

from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.models.invoice import Invoice

# Falhas de armazenamento que o repositório traduz para RepositoryError
_STORAGE_FAILURES: Final[tuple[type[Exception], ...]] = (
    SQLAlchemyError,
    OSError,
    ValueError,
)


class RepositoryError(Exception):
    """Falha ao acessar invoices persistidas.

    Mantém os serviços livres de SQLAlchemy. A exceção original fica em ``__cause__``.
    """


@dataclass(frozen=True, slots=True)
class StoredInvoice:
    """Invoice persistida, independente do ORM."""

    id: int
    owner_user_id: int
    client_id: int | None
    simulation_id: int | None
    invoice_number: str
    status: str  # 'draft' | 'finalized'
    locale: str  # 'pt-BR' | 'en'
    client_country_code: str
    issuer_name: str
    issuer_tax_id_digits: str
    issuer_address: str | None
    client_name: str
    client_tax_id_digits: str
    client_address: str | None
    banco: str | None
    agencia: str | None
    conta_com_digito: str | None
    pix_key: str | None
    periodo_inicio: date
    periodo_fim: date
    description: str
    regime: str
    currency: str
    amount: Decimal
    quantity: Decimal | None
    spread_pct: Decimal
    iof_pct: Decimal
    gross_foreign: Decimal
    gross_brl: Decimal
    spread_brl: Decimal
    iof_brl: Decimal
    net_brl: Decimal
    effective_rate: Decimal
    quote_rate: Decimal
    quote_source: str
    quote_bulletin: str | None
    quoted_at: datetime
    stale: bool
    finalized_at: datetime | None
    supersedes_invoice_id: int | None
    created_at: datetime
    updated_at: datetime


class InvoiceRepository(Protocol):
    """Contrato de acesso às invoices usado pela camada de serviços."""

    async def get_by_id(self, invoice_id: int, owner_user_id: int) -> StoredInvoice | None:
        """Devolve a invoice se pertencer ao owner_user_id."""
        ...

    async def list_by_owner(
        self,
        owner_user_id: int,
        *,
        status: str | None = None,
        client_id: int | None = None,
        page: int = 1,
        page_size: int = 20,
    ) -> tuple[list[StoredInvoice], int]:
        """Lista invoices do owner com paginação.

        Returns:
            (items, total_count)
        """
        ...

    async def save(self, invoice: StoredInvoice) -> None:
        """Grava uma invoice nova (insert)."""
        ...

    async def update_status(
        self, invoice_id: int, owner_user_id: int, status: str, finalized_at: datetime | None = None
    ) -> StoredInvoice | None:
        """Atualiza status (draft → finalized) e finalized_at."""
        ...

    async def delete(self, invoice_id: int, owner_user_id: int) -> bool:
        """Hard delete (LGPD art. 18). Returns True se deletou."""
        ...

    async def get_next_number(self, issuer_tax_id_digits: str) -> str:
        """Chama function PL/pgSQL next_invoice_number (DEC-06)."""
        ...


class SqlAlchemyInvoiceRepository:
    """Implementação de :class:`InvoiceRepository` sobre PostgreSQL."""

    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self._session_factory = session_factory

    async def get_by_id(self, invoice_id: int, owner_user_id: int) -> StoredInvoice | None:
        stmt = select(Invoice).where(
            Invoice.id == invoice_id, Invoice.owner_user_id == owner_user_id
        )
        try:
            async with self._session_factory() as session:
                row = (await session.execute(stmt)).scalar_one_or_none()
                if row is None:
                    return None
                return self._to_stored(row)
        except _STORAGE_FAILURES as error:
            raise RepositoryError("Falha ao ler invoice.") from error

    async def list_by_owner(
        self,
        owner_user_id: int,
        *,
        status: str | None = None,
        client_id: int | None = None,
        page: int = 1,
        page_size: int = 20,
    ) -> tuple[list[StoredInvoice], int]:
        stmt = select(Invoice).where(Invoice.owner_user_id == owner_user_id)
        if status:
            stmt = stmt.where(Invoice.status == status)
        if client_id:
            stmt = stmt.where(Invoice.client_id == client_id)
        stmt = stmt.order_by(Invoice.created_at.desc())

        # Count total
        count_stmt = select(func.count()).select_from(stmt.subquery())

        # Pagination
        stmt = stmt.limit(page_size).offset((page - 1) * page_size)

        try:
            async with self._session_factory() as session:
                total = (await session.execute(count_stmt)).scalar_one()
                rows = (await session.execute(stmt)).scalars().all()
                return [self._to_stored(r) for r in rows], total
        except _STORAGE_FAILURES as error:
            raise RepositoryError("Falha ao listar invoices.") from error

    async def save(self, invoice: StoredInvoice) -> None:
        row = Invoice(
            id=invoice.id,
            owner_user_id=invoice.owner_user_id,
            client_id=invoice.client_id,
            simulation_id=invoice.simulation_id,
            invoice_number=invoice.invoice_number,
            status=invoice.status,
            locale=invoice.locale,
            client_country_code=invoice.client_country_code,
            issuer_name=invoice.issuer_name,
            issuer_tax_id_digits=invoice.issuer_tax_id_digits,
            issuer_address=invoice.issuer_address,
            client_name=invoice.client_name,
            client_tax_id_digits=invoice.client_tax_id_digits,
            client_address=invoice.client_address,
            banco=invoice.banco,
            agencia=invoice.agencia,
            conta_com_digito=invoice.conta_com_digito,
            pix_key=invoice.pix_key,
            periodo_inicio=invoice.periodo_inicio,
            periodo_fim=invoice.periodo_fim,
            description=invoice.description,
            regime=invoice.regime,
            currency=invoice.currency,
            amount=invoice.amount,
            quantity=invoice.quantity,
            spread_pct=invoice.spread_pct,
            iof_pct=invoice.iof_pct,
            gross_foreign=invoice.gross_foreign,
            gross_brl=invoice.gross_brl,
            spread_brl=invoice.spread_brl,
            iof_brl=invoice.iof_brl,
            net_brl=invoice.net_brl,
            effective_rate=invoice.effective_rate,
            quote_rate=invoice.quote_rate,
            quote_source=invoice.quote_source,
            quote_bulletin=invoice.quote_bulletin,
            quoted_at=invoice.quoted_at,
            stale=invoice.stale,
            finalized_at=invoice.finalized_at,
            supersedes_invoice_id=invoice.supersedes_invoice_id,
            created_at=invoice.created_at,
            updated_at=invoice.updated_at,
        )
        try:
            async with self._session_factory() as session, session.begin():
                session.add(row)
        except _STORAGE_FAILURES as error:
            raise RepositoryError("Falha ao gravar invoice.") from error

    async def update_status(
        self, invoice_id: int, owner_user_id: int, status: str, finalized_at: datetime | None = None
    ) -> StoredInvoice | None:
        stmt = select(Invoice).where(
            Invoice.id == invoice_id, Invoice.owner_user_id == owner_user_id
        )
        try:
            async with self._session_factory() as session, session.begin():
                row = (await session.execute(stmt)).scalar_one_or_none()
                if row is None:
                    return None
                row.status = status
                if finalized_at is not None:
                    row.finalized_at = finalized_at
                row.updated_at = datetime.now().astimezone()
                return self._to_stored(row)
        except _STORAGE_FAILURES as error:
            raise RepositoryError("Falha ao atualizar status da invoice.") from error

    async def delete(self, invoice_id: int, owner_user_id: int) -> bool:
        stmt = select(Invoice).where(
            Invoice.id == invoice_id, Invoice.owner_user_id == owner_user_id
        )
        try:
            async with self._session_factory() as session, session.begin():
                row = (await session.execute(stmt)).scalar_one_or_none()
                if row is None:
                    return False
                await session.delete(row)
                return True
        except _STORAGE_FAILURES as error:
            raise RepositoryError("Falha ao apagar invoice.") from error

    async def get_next_number(self, issuer_tax_id_digits: str) -> str:
        """Chama function PL/pgSQL next_invoice_number (DEC-06)."""
        from sqlalchemy import text

        try:
            async with self._session_factory() as session:
                result = await session.execute(
                    text("SELECT next_invoice_number(:issuer)"),
                    {"issuer": issuer_tax_id_digits},
                )
                return str(result.scalar_one())
        except _STORAGE_FAILURES as error:
            raise RepositoryError("Falha ao gerar número de invoice.") from error

    def _to_stored(self, row: Invoice) -> StoredInvoice:
        return StoredInvoice(
            id=row.id,
            owner_user_id=row.owner_user_id,
            client_id=row.client_id,
            simulation_id=row.simulation_id,
            invoice_number=row.invoice_number,
            status=row.status,
            locale=row.locale,
            client_country_code=row.client_country_code,
            issuer_name=row.issuer_name,
            issuer_tax_id_digits=row.issuer_tax_id_digits,
            issuer_address=row.issuer_address,
            client_name=row.client_name,
            client_tax_id_digits=row.client_tax_id_digits,
            client_address=row.client_address,
            banco=row.banco,
            agencia=row.agencia,
            conta_com_digito=row.conta_com_digito,
            pix_key=row.pix_key,
            periodo_inicio=row.periodo_inicio,
            periodo_fim=row.periodo_fim,
            description=row.description,
            regime=row.regime,
            currency=row.currency,
            amount=row.amount,
            quantity=row.quantity,
            spread_pct=row.spread_pct,
            iof_pct=row.iof_pct,
            gross_foreign=row.gross_foreign,
            gross_brl=row.gross_brl,
            spread_brl=row.spread_brl,
            iof_brl=row.iof_brl,
            net_brl=row.net_brl,
            effective_rate=row.effective_rate,
            quote_rate=row.quote_rate,
            quote_source=row.quote_source,
            quote_bulletin=row.quote_bulletin,
            quoted_at=row.quoted_at,
            stale=row.stale,
            finalized_at=row.finalized_at,
            supersedes_invoice_id=row.supersedes_invoice_id,
            created_at=row.created_at,
            updated_at=row.updated_at,
        )
