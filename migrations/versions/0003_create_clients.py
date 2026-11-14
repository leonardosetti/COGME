"""Create clients table (SPEC-019 / future wave).

Clients directory for invoice issuance.
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0003_clients"
down_revision = "0002_user_identity"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "clients",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("owner_user_id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(120), nullable=False),
        sa.Column("tax_id_digits", sa.CHAR(14), nullable=False),
        sa.Column("tax_id_type", sa.String(16), nullable=False),  # cpf, cnpj
        sa.Column("email", sa.String(255), nullable=True),
        sa.Column("phone", sa.String(30), nullable=True),
        sa.Column("address", sa.String(240), nullable=True),
        sa.Column("country_code", sa.CHAR(2), nullable=False, server_default=sa.text("'BR'")),
        sa.Column("status", sa.String(16), nullable=False, server_default=sa.text("'active'")),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
        sa.PrimaryKeyConstraint("id", name="pk_clients"),
        sa.CheckConstraint(
            "status IN ('active','inactive')", name="chk_clients_status"
        ),
        sa.UniqueConstraint("owner_user_id", "tax_id_digits", name="uq_clients_owner_tax"),
        sa.ForeignKeyConstraint(
            ["owner_user_id"], ["users.id"], name="fk_clients_owner", ondelete="CASCADE"
        ),
    )

    op.create_index("ix_clients_owner", "clients", ["owner_user_id"])
    op.create_index("ix_clients_tax_id", "clients", ["tax_id_digits"])
    op.create_index("ix_clients_status", "clients", ["status"])

    # Trigger para updated_at
    op.execute(
        """
        CREATE TRIGGER trigger_clients_updated_at
        BEFORE UPDATE ON clients
        FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS trigger_clients_updated_at ON clients")
    op.drop_index("ix_clients_status", table_name="clients")
    op.drop_index("ix_clients_tax_id", table_name="clients")
    op.drop_index("ix_clients_owner", table_name="clients")
    op.drop_table("clients")
