"""Add email_verification_tokens table for email verification (duplo opt-in).

Revision ID: 0012_email_verification_tokens
Revises: 0011_invoice_number_unique_per_issuer
Create Date: 2026-11-18
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0012_email_verification_tokens"
down_revision = "0009_fix_users_nullable"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # email_verification_tokens
    op.create_table(
        "email_verification_tokens",
        sa.Column("id", sa.BIGINT, primary_key=True),
        sa.Column(
            "user_id",
            sa.BIGINT,
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("token_hash", sa.String(64), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "expires_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),
        sa.Column("used_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index(
        "ix_email_verification_user",
        "email_verification_tokens",
        ["user_id"],
    )
    op.create_index(
        "ix_email_verification_expires",
        "email_verification_tokens",
        ["expires_at"],
    )
    op.create_unique_constraint(
        "uq_email_verification_token",
        "email_verification_tokens",
        ["token_hash"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "uq_email_verification_token", "email_verification_tokens", type_="unique"
    )
    op.drop_index("ix_email_verification_expires", table_name="email_verification_tokens")
    op.drop_index("ix_email_verification_user", table_name="email_verification_tokens")
    op.drop_table("email_verification_tokens")