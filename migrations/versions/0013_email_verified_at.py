"""Add email_verified_at column to users table.

Revision ID: 0013_email_verified_at
Revises: 0012_email_verification_tokens
Create Date: 2026-11-18
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0013_email_verified_at"
down_revision = "0012_email_verification_tokens"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("email_verified_at", sa.DateTime(timezone=True), nullable=True),
    )
    # Grandfather existing users with email: set email_verified_at = created_at
    op.execute(
        "UPDATE users SET email_verified_at = created_at WHERE email IS NOT NULL AND email_verified_at IS NULL"
    )


def downgrade() -> None:
    op.drop_column("users", "email_verified_at")