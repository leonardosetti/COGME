"""Alter users.cpf to nullable (email registrations don't have CPF).

Fixes unique constraint violation when multiple users register with email only.
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0008_alter_users_cpf_nullable"
down_revision = "0007_create_provider_tables"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Alter cpf column to be nullable
    op.alter_column("users", "cpf", existing_type=sa.CHAR(11), nullable=True)


def downgrade() -> None:
    # Revert to NOT NULL (will fail if there are NULL values)
    op.alter_column("users", "cpf", existing_type=sa.CHAR(11), nullable=False)
