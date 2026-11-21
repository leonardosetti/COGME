"""Make users.email and users.cpf nullable (login via user_login_identifiers).

The user_login_identifiers table is the source of truth for login identifiers.
The users table email/cpf columns are kept for backward compatibility but
are nullable since users can register with email, CPF, or CNPJ.
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0009_fix_users_nullable"
down_revision = "0008_alter_users_cpf_nullable"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Make email nullable
    op.alter_column("users", "email", existing_type=sa.String(255), nullable=True)
    
    # Make cpf nullable
    op.alter_column("users", "cpf", existing_type=sa.CHAR(11), nullable=True)
    
    # Drop unique constraints since they're now nullable and we use user_login_identifiers for uniqueness
    op.drop_constraint("uq_users_email", "users", type_="unique")
    op.drop_constraint("uq_users_cpf", "users", type_="unique")
    
    # Create partial unique indexes for non-null values
    op.execute("""
        CREATE UNIQUE INDEX uq_users_email_partial
        ON users (email)
        WHERE email IS NOT NULL;
    """)
    op.execute("""
        CREATE UNIQUE INDEX uq_users_cpf_partial
        ON users (cpf)
        WHERE cpf IS NOT NULL;
    """)


def downgrade() -> None:
    # Drop partial indexes
    op.execute("DROP INDEX IF EXISTS uq_users_email_partial")
    op.execute("DROP INDEX IF EXISTS uq_users_cpf_partial")
    
    # Restore unique constraints (will fail if there are NULLs)
    op.create_unique_constraint("uq_users_email", "users", ["email"])
    op.create_unique_constraint("uq_users_cpf", "users", ["cpf"])
    
    # Make columns NOT NULL again
    op.alter_column("users", "email", existing_type=sa.String(255), nullable=False)
    op.alter_column("users", "cpf", existing_type=sa.CHAR(11), nullable=False)
