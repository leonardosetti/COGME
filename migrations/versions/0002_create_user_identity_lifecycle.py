"""Create user identity tables + account_lifecycle_events (SPEC-017, SPEC-022).

SPEC-017: users, user_login_identifiers, user_sessions, password_reset_tokens
SPEC-022: account_lifecycle_events, users.status/dormant_since/last_login_at
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0002_user_identity"
down_revision = "0001_create_fx_quotes"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ---------- Tabela users ----------
    op.create_table(
        "users",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("internal_username_hash", sa.String(64), nullable=False),
        sa.Column("name", sa.String(120), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("phone", sa.String(30), nullable=True),
        sa.Column("cpf", sa.CHAR(11), nullable=False),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column(
            "status",
            sa.String(16),
            nullable=False,
            server_default=sa.text("'active'"),
        ),
        sa.Column("dormant_since", sa.DateTime(timezone=True), nullable=True),
        sa.Column("last_login_at", sa.DateTime(timezone=True), nullable=True),
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
        sa.PrimaryKeyConstraint("id", name="pk_users"),
        sa.CheckConstraint(
            "status IN ('active','dormant','deleted')", name="chk_users_status"
        ),
        sa.UniqueConstraint("email", name="uq_users_email"),
        sa.UniqueConstraint("cpf", name="uq_users_cpf"),
        sa.UniqueConstraint("internal_username_hash", name="uq_users_internal_username"),
    )

    op.create_index("ix_users_email", "users", ["email"])
    op.create_index("ix_users_cpf", "users", ["cpf"])
    op.create_index("ix_users_status", "users", ["status"])
    op.create_index("ix_users_last_login", "users", ["last_login_at"])

    # ---------- Tabela user_login_identifiers ----------
    op.create_table(
        "user_login_identifiers",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column(
            "kind",
            sa.String(16),
            nullable=False,
        ),
        sa.Column("lookup_hmac", sa.String(64), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
        sa.Column("retired_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id", name="pk_user_login_identifiers"),
        sa.UniqueConstraint("kind", "lookup_hmac", name="uq_user_login_kind_hmac"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_user_login_user", ondelete="CASCADE"
        ),
    )

    op.create_index("ix_user_login_user_kind", "user_login_identifiers", ["user_id", "kind"])
    op.create_index("ix_user_login_hmac", "user_login_identifiers", ["lookup_hmac"])
    # Partial unique index for active (non-retired) identifiers per user+kind
    op.execute(
        """
        CREATE UNIQUE INDEX uq_user_login_user_kind_active
        ON user_login_identifiers (user_id, kind)
        WHERE retired_at IS NULL;
        """
    )

    # ---------- Tabela user_sessions ----------
    op.create_table(
        "user_sessions",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("token_hash", sa.String(64), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
        sa.Column(
            "last_seen_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("revoked_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id", name="pk_user_sessions"),
        sa.UniqueConstraint("token_hash", name="uq_user_sessions_token"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_sessions_user", ondelete="CASCADE"
        ),
    )

    op.create_index("ix_user_sessions_user", "user_sessions", ["user_id"])
    op.create_index("ix_user_sessions_expires", "user_sessions", ["expires_at"])
    op.create_index("ix_user_sessions_revoked", "user_sessions", ["revoked_at"])

    # ---------- Tabela password_reset_tokens ----------
    op.create_table(
        "password_reset_tokens",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("token_hash", sa.String(64), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("used_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id", name="pk_password_reset_tokens"),
        sa.UniqueConstraint("token_hash", name="uq_pwd_reset_token"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_pwd_reset_user", ondelete="CASCADE"
        ),
    )

    op.create_index("ix_pwd_reset_user", "password_reset_tokens", ["user_id"])
    op.create_index("ix_pwd_reset_expires", "password_reset_tokens", ["expires_at"])

    # ---------- Tabela account_lifecycle_events ----------
    op.create_table(
        "account_lifecycle_events",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("event_type", sa.String(32), nullable=False),
        sa.Column("from_status", sa.CHAR(16), nullable=True),
        sa.Column("to_status", sa.CHAR(16), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
        sa.PrimaryKeyConstraint("id", name="pk_account_lifecycle_events"),
        sa.CheckConstraint(
            "event_type IN ('CREATED','ACTIVATED','DORMANT_AUTO','DORMANT_MANUAL',"
            "'REACTIVATED','DELETED','ANONYMIZED')",
            name="chk_lifecycle_event_type",
        ),
        sa.CheckConstraint(
            "from_status IN ('active','dormant','deleted')",
            name="chk_lifecycle_from_status",
        ),
        sa.CheckConstraint(
            "to_status IN ('active','dormant','deleted')",
            name="chk_lifecycle_to_status",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_lifecycle_user", ondelete="CASCADE"
        ),
    )

    op.create_index(
        "ix_lifecycle_user_created",
        "account_lifecycle_events",
        ["user_id", "created_at"],
    )
    op.create_index("ix_lifecycle_type", "account_lifecycle_events", ["event_type"])

    # ---------- Trigger para updated_at em users ----------
    op.execute(
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER LANGUAGE plpgsql AS $$
        BEGIN
            NEW.updated_at = NOW();
            RETURN NEW;
        END;
        $$;
        """
    )
    op.execute(
        """
        CREATE TRIGGER trigger_users_updated_at
        BEFORE UPDATE ON users
        FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
        """
    )


def downgrade() -> None:
    # Drop trigger
    op.execute("DROP TRIGGER IF EXISTS trigger_users_updated_at ON users")
    op.execute("DROP FUNCTION IF EXISTS update_updated_at_column()")

    # Drop indexes
    op.drop_index("ix_lifecycle_type", table_name="account_lifecycle_events")
    op.drop_index("ix_lifecycle_user_created", table_name="account_lifecycle_events")
    op.drop_index("ix_pwd_reset_expires", table_name="password_reset_tokens")
    op.drop_index("ix_pwd_reset_user", table_name="password_reset_tokens")
    op.drop_index("ix_user_sessions_revoked", table_name="user_sessions")
    op.drop_index("ix_user_sessions_expires", table_name="user_sessions")
    op.drop_index("ix_user_sessions_user", table_name="user_sessions")
    op.drop_index("ix_user_login_hmac", table_name="user_login_identifiers")
    op.drop_index("ix_user_login_user_kind", table_name="user_login_identifiers")
    op.drop_index("ix_users_last_login", table_name="users")
    op.drop_index("ix_users_status", table_name="users")
    op.drop_index("ix_users_cpf", table_name="users")
    op.drop_index("ix_users_email", table_name="users")

    # Drop tables (FKs handled by drop order)
    op.drop_table("account_lifecycle_events")
    op.drop_table("password_reset_tokens")
    op.drop_table("user_sessions")
    op.drop_table("user_login_identifiers")
    op.drop_table("users")
