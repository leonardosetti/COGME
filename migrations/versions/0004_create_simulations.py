"""Create simulations table (SPEC-020 / future wave).

Saved simulations for invoice history.
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0004_simulations"
down_revision = "0003_clients"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "simulations",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("owner_user_id", sa.BigInteger(), nullable=False),
        sa.Column("client_id", sa.BigInteger(), nullable=True),
        sa.Column("name", sa.String(120), nullable=False),
        sa.Column("regime", sa.String(16), nullable=False),
        sa.Column("currency", sa.CHAR(3), nullable=False),
        sa.Column("amount", sa.Numeric(18, 2), nullable=False),
        sa.Column("quantity", sa.Numeric(10, 2), nullable=True),
        sa.Column("spread_pct", sa.Numeric(6, 4), nullable=False),
        sa.Column("iof_pct", sa.Numeric(6, 4), nullable=False),
        sa.Column("gross_foreign", sa.Numeric(18, 2), nullable=False),
        sa.Column("gross_brl", sa.Numeric(18, 2), nullable=False),
        sa.Column("spread_brl", sa.Numeric(18, 2), nullable=False),
        sa.Column("iof_brl", sa.Numeric(18, 2), nullable=False),
        sa.Column("net_brl", sa.Numeric(18, 2), nullable=False),
        sa.Column("effective_rate", sa.Numeric(18, 6), nullable=False),
        sa.Column("quote_rate", sa.Numeric(18, 6), nullable=False),
        sa.Column("quote_source", sa.String(20), nullable=False),
        sa.Column("quote_bulletin", sa.String(40), nullable=True),
        sa.Column("quoted_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("stale", sa.Boolean(), nullable=False, server_default=sa.text("FALSE")),
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
        sa.PrimaryKeyConstraint("id", name="pk_simulations"),
        sa.CheckConstraint(
            "regime IN ('hourly','daily','weekly','monthly','fixed')",
            name="chk_simulations_regime",
        ),
        sa.CheckConstraint(
            "currency IN ('USD','EUR')", name="chk_simulations_currency"
        ),
        sa.CheckConstraint(
            "gross_brl - spread_brl - iof_brl = net_brl",
            name="chk_simulation_identity",
        ),
        sa.ForeignKeyConstraint(
            ["owner_user_id"], ["users.id"], name="fk_simulations_owner", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["client_id"], ["clients.id"], name="fk_simulations_client", ondelete="SET NULL"
        ),
    )

    op.create_index("ix_simulations_owner_created", "simulations", ["owner_user_id", "created_at"])
    op.create_index("ix_simulations_client", "simulations", ["client_id"])
    op.create_index("ix_simulations_stale", "simulations", ["stale"])

    # Trigger para updated_at
    op.execute(
        """
        CREATE TRIGGER trigger_simulations_updated_at
        BEFORE UPDATE ON simulations
        FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS trigger_simulations_updated_at ON simulations")
    op.drop_index("ix_simulations_stale", table_name="simulations")
    op.drop_index("ix_simulations_client", table_name="simulations")
    op.drop_index("ix_simulations_owner_created", table_name="simulations")
    op.drop_table("simulations")
