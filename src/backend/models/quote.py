"""Modelo ORM da tabela ``fx_quotes`` (spec backend-mvp-v1, §5).

Guarda somente cotações públicas de câmbio (REQ-01, REQ-07). Nenhum dado
pessoal ou de simulação é persistido (LGPD).
"""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    CHAR,
    BigInteger,
    CheckConstraint,
    DateTime,
    Index,
    Numeric,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.models.database import Base


class FxQuote(Base):
    """Cotação de câmbio (BRL por 1 unidade estrangeira) obtida de uma fonte.

    Attributes:
        id: Chave primária autoincrementada.
        currency: Código ISO 4217 da moeda estrangeira (``USD`` ou ``EUR``).
        rate: Cotação em BRL, positiva, com 6 casas decimais.
        source: Fonte da cotação (``frankfurter`` ou ``ptax``).
        bulletin: Tipo de boletim da PTAX; ``None`` nas demais fontes.
        quoted_at: Instante da cotação informado pela fonte (UTC).
        fetched_at: Instante em que o backend obteve a cotação (UTC); a idade
            do cache conta a partir dele.
    """

    __tablename__ = "fx_quotes"
    __table_args__ = (
        CheckConstraint("currency IN ('USD', 'EUR')", name="currency_valid"),
        CheckConstraint("rate > 0", name="rate_positive"),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    currency: Mapped[str] = mapped_column(CHAR(3), nullable=False)
    rate: Mapped[Decimal] = mapped_column(Numeric(18, 6), nullable=False)
    source: Mapped[str] = mapped_column(String(20), nullable=False)
    bulletin: Mapped[str | None] = mapped_column(String(40), nullable=True)
    quoted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    fetched_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )


# Serve a consulta "última cotação da moeda" (get_latest).
Index(
    "ix_fx_quotes_currency_fetched_at",
    FxQuote.currency,
    FxQuote.fetched_at.desc(),
)
