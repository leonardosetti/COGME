"""Allow tax_id_digits nullable and VARCHAR(32) para clientes internacionais.

Clientes do tipo ``foreign`` não têm documento brasileiro, então
``tax_id_digits`` passa a ser opcional e de tamanho variável (até 32 chars).
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0016_clients_tax_id_nullable"
down_revision = "0015_invoice_unique"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        "clients",
        "tax_id_digits",
        existing_type=sa.CHAR(14),
        type_=sa.VARCHAR(32),
        nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        "clients",
        "tax_id_digits",
        existing_type=sa.VARCHAR(32),
        type_=sa.CHAR(14),
        nullable=False,
    )
