"""Repositório de cotações (spec backend-mvp-v1, §5).

A camada de serviços depende apenas de :class:`QuoteRepository` e de
:class:`StoredQuote`, ambos livres de SQLAlchemy. A implementação concreta
(:class:`SqlAlchemyQuoteRepository`) é a única que conhece o ORM.

Escolha de transação: **sessão por operação**. Cada chamada abre uma sessão
nova, executa e a encerra; ``save`` faz commit próprio ao sair do bloco.
Não há sessão compartilhada entre requisições, o que evita estado oculto e
vazamento de transação em código assíncrono concorrente.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Final, Protocol

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.backend.models.quote import FxQuote

# O SQLAlchemy não traduz falha de rede ao conectar: asyncpg entrega OSError puro, como
# ConnectionRefusedError ou TimeoutError. ValueError vem de StoredQuote ao ler linha inválida.
_STORAGE_FAILURES: Final[tuple[type[Exception], ...]] = (
    SQLAlchemyError,
    OSError,
    ValueError,
)


class RepositoryError(Exception):
    """Falha ao acessar as cotações persistidas.

    Mantém os serviços livres de SQLAlchemy. A mensagem é fixa; a exceção original fica em
    ``__cause__``, e só o nome do tipo dela pode ir para log, pois o texto pode trazer SQL.
    """


@dataclass(frozen=True, slots=True)
class StoredQuote:
    """Cotação persistida, independente do ORM.

    Attributes:
        currency: Código da moeda (``USD`` ou ``EUR``).
        rate: Cotação em BRL por 1 unidade estrangeira (finita e positiva).
        source: Fonte da cotação (``frankfurter`` ou ``ptax``).
        bulletin: Tipo de boletim da PTAX, ou ``None``.
        quoted_at: Instante da cotação informado pela fonte; com fuso.
        fetched_at: Instante em que a cotação foi obtida; com fuso. A idade
            do cache conta a partir dele.
    """

    currency: str
    rate: Decimal
    source: str
    bulletin: str | None
    quoted_at: datetime
    fetched_at: datetime

    def __post_init__(self) -> None:
        """Rejeita valores que o banco não conseguiria garantir sozinho.

        Raises:
            ValueError: Se ``rate`` não for finito e positivo (o PostgreSQL
                aceita ``NaN`` em ``numeric``) ou se alguma data não tiver
                fuso horário.
        """
        if not self.rate.is_finite() or self.rate <= 0:
            raise ValueError("A cotação deve ser um número finito e positivo.")
        if self.quoted_at.tzinfo is None or self.fetched_at.tzinfo is None:
            raise ValueError("As datas da cotação devem conter fuso horário.")


class QuoteRepository(Protocol):
    """Contrato de acesso às cotações usado pela camada de serviços."""

    async def get_latest(self, currency: str) -> StoredQuote | None:
        """Devolve a cotação mais recente (por ``fetched_at``) da moeda.

        Args:
            currency: Código da moeda (``USD`` ou ``EUR``).

        Returns:
            A cotação mais recente, ou ``None`` se não houver nenhuma.

        Raises:
            RepositoryError: Se a leitura falhar.
        """
        ...

    async def save(self, quote: StoredQuote) -> None:
        """Grava uma cotação e confirma a transação.

        Args:
            quote: Cotação já validada pelo serviço.

        Raises:
            RepositoryError: Se a gravação falhar.
        """
        ...


class SqlAlchemyQuoteRepository:
    """Implementação de :class:`QuoteRepository` sobre PostgreSQL."""

    def __init__(
        self, session_factory: async_sessionmaker[AsyncSession]
    ) -> None:
        """Cria o repositório.

        Args:
            session_factory: Fábrica de sessões; uma sessão é aberta e
                fechada a cada operação.
        """
        self._session_factory = session_factory

    async def get_latest(self, currency: str) -> StoredQuote | None:
        """Devolve a cotação mais recente (por ``fetched_at``) da moeda.

        Args:
            currency: Código da moeda (``USD`` ou ``EUR``).

        Returns:
            A cotação mais recente, ou ``None`` se não houver nenhuma.

        Raises:
            RepositoryError: Se a leitura falhar ou a linha for inválida.
        """
        statement = (
            select(FxQuote)
            .where(FxQuote.currency == currency)
            .order_by(FxQuote.fetched_at.desc(), FxQuote.id.desc())
            .limit(1)
        )
        try:
            async with self._session_factory() as session:
                row = (await session.execute(statement)).scalar_one_or_none()
                if row is None:
                    return None
                return StoredQuote(
                    currency=row.currency,
                    rate=row.rate,
                    source=row.source,
                    bulletin=row.bulletin,
                    quoted_at=row.quoted_at,
                    fetched_at=row.fetched_at,
                )
        except _STORAGE_FAILURES as error:
            raise RepositoryError("Falha ao ler a cotação.") from error

    async def save(self, quote: StoredQuote) -> None:
        """Grava uma cotação em sessão própria, com commit ao final.

        Se ocorrer erro (por exemplo violação de CHECK), a transação sofre
        rollback.

        Args:
            quote: Cotação já validada pelo serviço.

        Raises:
            RepositoryError: Se a gravação falhar.
        """
        row = FxQuote(
            currency=quote.currency,
            rate=quote.rate,
            source=quote.source,
            bulletin=quote.bulletin,
            quoted_at=quote.quoted_at,
            fetched_at=quote.fetched_at,
        )
        try:
            async with self._session_factory() as session, session.begin():
                session.add(row)
        except _STORAGE_FAILURES as error:
            raise RepositoryError("Falha ao gravar a cotação.") from error
