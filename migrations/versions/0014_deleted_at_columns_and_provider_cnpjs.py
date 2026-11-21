"""Add deleted_at columns for soft delete and backfill provider_cnpjs.

Revision ID: 0014_deleted_at_columns_and_provider_cnpjs
Revises: 0013_email_verified_at
Create Date: 2026-11-18
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0014_deleted_at_provider_cnpjs"
down_revision = "0013_email_verified_at"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Backfill provider_cnpjs from provider_profiles.cnpj (legacy)
    op.execute("""
        INSERT INTO provider_cnpjs (user_id, cnpj, is_primary, status, created_at, updated_at)
        SELECT user_id, cnpj, TRUE, 'active', NOW(), NOW()
        FROM provider_profiles
        WHERE cnpj IS NOT NULL AND cnpj <> ''
        ON CONFLICT (cnpj) DO NOTHING;
    """)

    # deleted_at columns (idempotent)
    op.execute("ALTER TABLE clients ADD COLUMN IF NOT EXISTS deleted_at TIMESTAMPTZ")
    op.execute("ALTER TABLE simulations ADD COLUMN IF NOT EXISTS deleted_at TIMESTAMPTZ")
    op.execute("ALTER TABLE provider_profiles ADD COLUMN IF NOT EXISTS deleted_at TIMESTAMPTZ")
    op.execute("ALTER TABLE invoices ADD COLUMN IF NOT EXISTS deleted_at TIMESTAMPTZ")


def downgrade() -> None:
    # Drop columns
    op.drop_column("invoices", "deleted_at")
    op.drop_column("provider_profiles", "deleted_at")
    op.drop_column("simulations", "deleted_at")
    op.drop_column("clients", "deleted_at")