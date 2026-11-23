"""Reconciliar modelos ORM com estado do banco (drift do alembic check).

Ajusta índices e constraints para que ``alembic check`` não detecte
operações pendentes, e aumenta o tamanho de alembic_version.version_num
para acomodar revision IDs mais longas que 32 caracteres.

1. Remove ix_countries_code (redundante com PK pk_countries de countries.code).
2. Adiciona coluna encrypted_data em provider_bank_accounts (presente no modelo, ausente na tabela).
3. Remove índice parcial uq_provider_cnpjs_primary (sobrante da migração 0007).
4. Adiciona constraint uq_provider_cnpjs_user_cnpj
   (user_id, cnpj) — já no modelo ProviderCnpj.
5. Adiciona constraint uq_provider_profiles_user_id
   (user_id) — já no modelo ProviderProfile (unique=True).
6. Remove índices parciais uq_users_email_partial / uq_users_cpf_partial
   (sobrantes da migração 0009; a unicidade de login agora é gerenciada por
   user_login_identifiers).
7. Altera alembic_version.version_num de VARCHAR(32) para VARCHAR(64).

Revision ID: 0017_reconcile_models
Revises: 0016_clients_tax_id_nullable
Create Date: 2026-11-23
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0017_reconcile_models"
down_revision = "0016_clients_tax_id_nullable"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1. ix_countries_code é redundante com a PK pk_countries (code é PK).
    op.drop_index("ix_countries_code", table_name="countries")

    # 2. Coluna encrypted_data existe no modelo ProviderBankAccount mas não na tabela.
    op.add_column(
        "provider_bank_accounts",
        sa.Column("encrypted_data", sa.Text(), nullable=True),
    )

    # 3. Índice parcial sobrante da migração 0007.
    op.execute("DROP INDEX IF EXISTS uq_provider_cnpjs_primary")

    # 4. Constraint única (user_id, cnpj) já declarada no modelo ProviderCnpj.
    op.create_unique_constraint(
        "uq_provider_cnpjs_user_cnpj",
        "provider_cnpjs",
        ["user_id", "cnpj"],
    )

    # 5. Constraint única (user_id) já declarada no modelo ProviderProfile (unique=True).
    op.create_unique_constraint(
        "uq_provider_profiles_user_id",
        "provider_profiles",
        ["user_id"],
    )

    # 6. Índices parciais sobrantes da migração 0009; unicidade de login agora é
    # gerenciada por user_login_identifiers.
    op.execute("DROP INDEX IF EXISTS uq_users_email_partial")
    op.execute("DROP INDEX IF EXISTS uq_users_cpf_partial")

    # 7. version_num é VARCHAR(32); revision IDs mais longas que 32 chars falham.
    op.alter_column(
        "alembic_version",
        "version_num",
        existing_type=sa.VARCHAR(32),
        type_=sa.VARCHAR(64),
        existing_nullable=False,
    )


def downgrade() -> None:
    # Reverte 7.
    op.alter_column(
        "alembic_version",
        "version_num",
        existing_type=sa.VARCHAR(64),
        type_=sa.VARCHAR(32),
        existing_nullable=False,
    )

    # Reverte 6.
    op.execute(
        """
        CREATE UNIQUE INDEX uq_users_email_partial
        ON users (email) WHERE email IS NOT NULL;
        """
    )
    op.execute(
        """
        CREATE UNIQUE INDEX uq_users_cpf_partial
        ON users (cpf) WHERE cpf IS NOT NULL;
        """
    )

    # Reverte 5.
    op.drop_constraint("uq_provider_profiles_user_id", "provider_profiles", type_="unique")

    # Reverte 4.
    op.drop_constraint("uq_provider_cnpjs_user_cnpj", "provider_cnpjs", type_="unique")

    # Reverte 3.
    op.execute(
        """
        CREATE UNIQUE INDEX uq_provider_cnpjs_primary
        ON provider_cnpjs (user_id)
        WHERE is_primary AND status = 'active';
        """
    )

    # Reverte 2.
    op.drop_column("provider_bank_accounts", "encrypted_data")

    # Reverte 1.
    op.create_index("ix_countries_code", "countries", ["code"], unique=True)
