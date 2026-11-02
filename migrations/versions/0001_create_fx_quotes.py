"""Cria a tabela fx_quotes (cache de cotações de câmbio).

Revision ID: 0001
Revises:
Create Date: 2026-10-31

LGPD: somente cotações públicas; nenhum dado pessoal. Sem caminho de
esquecimento necessário. A retenção das linhas será tratada em manutenção
futura (spec backend-mvp-v1, §5).

Rollback: ``downgrade`` remove o índice e a tabela. É destrutivo para as
cotações em cache, que são reobtidas das fontes públicas.
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Cria ``fx_quotes`` com CHECKs e o índice (currency, fetched_at DESC)."""
    op.create_table(
        "fx_quotes",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("currency", sa.CHAR(length=3), nullable=False),
        sa.Column("rate", sa.Numeric(precision=18, scale=6), nullable=False),
        sa.Column("source", sa.String(length=20), nullable=False),
        sa.Column("bulletin", sa.String(length=40), nullable=True),
        sa.Column("quoted_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("fetched_at", sa.DateTime(timezone=True), nullable=False),
        sa.CheckConstraint(
            "currency IN ('USD', 'EUR')",
            name=op.f("ck_fx_quotes_currency_valid"),
        ),
        sa.CheckConstraint(
            "rate > 0", name=op.f("ck_fx_quotes_rate_positive")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_fx_quotes")),
    )
    op.create_index(
        "ix_fx_quotes_currency_fetched_at",
        "fx_quotes",
        ["currency", sa.literal_column("fetched_at DESC")],
    )


def downgrade() -> None:
    """Remove o índice e a tabela ``fx_quotes``."""
    op.drop_index("ix_fx_quotes_currency_fetched_at", table_name="fx_quotes")
    op.drop_table("fx_quotes")
