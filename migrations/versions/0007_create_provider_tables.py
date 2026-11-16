"""Create provider_profiles and provider_bank_accounts tables (SPEC-018 / future wave).

Ratificado por CCB/GP em RAT-2026-11-14-INVOICES.
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0007_create_provider_tables"
down_revision = "0006_countries"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ---------- Tabela provider_profiles ----------
    op.create_table(
        "provider_profiles",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("legal_name", sa.String(255), nullable=False),
        sa.Column("category", sa.String(16), nullable=False),
        sa.Column("cnpj", sa.CHAR(14), nullable=True),
        sa.Column("address", sa.String(500), nullable=True),
        sa.Column("city", sa.String(100), nullable=True),
        sa.Column("state", sa.CHAR(2), nullable=True),
        sa.Column("postal_code", sa.CHAR(8), nullable=True),
        sa.Column("country_code", sa.CHAR(2), nullable=False, server_default=sa.text("'BR'")),
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
        sa.PrimaryKeyConstraint("id", name="pk_provider_profiles"),
        sa.CheckConstraint(
            "category IN ('mei','legal_entity')", name="chk_provider_category"
        ),
        sa.UniqueConstraint("cnpj", name="uq_provider_cnpj"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_provider_user", ondelete="CASCADE"
        ),
    )

    op.create_index("ix_provider_user", "provider_profiles", ["user_id"])

    # ---------- Tabela provider_bank_accounts ----------
    op.create_table(
        "provider_bank_accounts",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("account_type", sa.String(16), nullable=False),
        sa.Column("bank_code", sa.CHAR(3), nullable=False),  # COMPE
        sa.Column("bank_name", sa.String(100), nullable=False),
        sa.Column("branch", sa.String(10), nullable=False),
        sa.Column("account_number", sa.String(20), nullable=False),
        sa.Column("account_digit", sa.String(2), nullable=False),
        sa.Column("swift_bic", sa.String(11), nullable=True),
        sa.Column("iban", sa.String(34), nullable=True),
        sa.Column("account_holder", sa.String(255), nullable=False),
        sa.Column("currency", sa.CHAR(3), nullable=False, server_default=sa.text("'BRL'")),
        sa.Column("is_primary", sa.Boolean(), nullable=False, server_default=sa.text("FALSE")),
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
        sa.PrimaryKeyConstraint("id", name="pk_provider_bank_accounts"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_provider_bank_account_user", ondelete="CASCADE"
        ),
    )

    op.create_index("ix_provider_bank_account_user", "provider_bank_accounts", ["user_id"])
    op.create_index(
        "ix_provider_bank_account_primary",
        "provider_bank_accounts",
        ["user_id", "is_primary"],
        postgresql_where=sa.text("is_primary = true"),
    )

    # Trigger para updated_at em provider_profiles
    op.execute(
        """
        CREATE TRIGGER trigger_provider_profiles_updated_at
        BEFORE UPDATE ON provider_profiles
        FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
        """
    )

    # Trigger para updated_at em provider_bank_accounts
    op.execute(
        """
        CREATE TRIGGER trigger_provider_bank_accounts_updated_at
        BEFORE UPDATE ON provider_bank_accounts
        FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS trigger_provider_bank_accounts_updated_at ON provider_bank_accounts")
    op.execute("DROP TRIGGER IF EXISTS trigger_provider_profiles_updated_at ON provider_profiles")

    op.drop_index("ix_provider_bank_account_primary", table_name="provider_bank_accounts")
    op.drop_index("ix_provider_bank_account_user", table_name="provider_bank_accounts")
    op.drop_index("ix_provider_user", table_name="provider_profiles")

    op.drop_table("provider_bank_accounts")
    op.drop_table("provider_profiles")
