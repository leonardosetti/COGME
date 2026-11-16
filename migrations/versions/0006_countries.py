"""Seed tabela ``countries`` (ISO 3166-1) para validação de ``country_code`` (AI-03).

Tabela usada por SPEC-019 (cliente fictício exige country_code), SPEC-020
(emenda invoices.client_country_code) e SPEC-021 (derivação locale BR→pt-BR).

Migração criada em 2026-11-16 para cumprir AI-03 (padrão do item 8 da
ratificação Gate 1 CR-002, docs/decisoes/ccb-auditoria-CR-002.md:64).

A lista abaixo contém os códigos mais usados; completar com os 249 códigos
ISO 3166-1 antes da produção (AI-03 prazo 2026-11-22, responsável agent-dba).
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0006_countries"
down_revision = "0005_invoices"
branch_labels = None
depends_on = None

# ISO 3166-1 alpha-2 (parcial — completar com os 249 códigos oficiais).
_COUNTRIES: list[tuple[str, str]] = [
    ("BR", "Brazil"),
    ("US", "United States"),
    ("AR", "Argentina"),
    ("CL", "Chile"),
    ("CO", "Colombia"),
    ("PE", "Peru"),
    ("MX", "Mexico"),
    ("PT", "Portugal"),
    ("ES", "Spain"),
    ("FR", "France"),
    ("DE", "Germany"),
    ("IT", "Italy"),
    ("GB", "United Kingdom"),
    ("CA", "Canada"),
    ("AU", "Australia"),
    ("JP", "Japan"),
    ("KR", "Korea, Republic of"),
    ("CN", "China"),
    ("IN", "India"),
    ("CH", "Switzerland"),
    ("NL", "Netherlands"),
    ("BE", "Belgium"),
    ("AT", "Austria"),
    ("SE", "Sweden"),
    ("NO", "Norway"),
    ("DK", "Denmark"),
    ("FI", "Finland"),
    ("PL", "Poland"),
    ("CZ", "Czechia"),
    ("HU", "Hungary"),
    ("RO", "Romania"),
    ("GR", "Greece"),
    ("TR", "Türkiye"),
    ("IL", "Israel"),
    ("AE", "United Arab Emirates"),
    ("SA", "Saudi Arabia"),
    ("ZA", "South Africa"),
    ("NZ", "New Zealand"),
    ("SG", "Singapore"),
    ("HK", "Hong Kong"),
    ("KR", "Korea, Republic of"),
]


def upgrade() -> None:
    op.create_table(
        "countries",
        sa.Column("code", sa.CHAR(2), nullable=False),
        sa.Column("name", sa.String(120), nullable=False),
        sa.PrimaryKeyConstraint("code", name="pk_countries"),
    )
    op.create_index("ix_countries_code", "countries", ["code"], unique=True)

    for code, name in _COUNTRIES:
        op.execute(
            sa.text("INSERT INTO countries (code, name) VALUES (:c, :n) "
                    "ON CONFLICT (code) DO NOTHING"),
            {"c": code, "n": name},
        )


def downgrade() -> None:
    op.drop_index("ix_countries_code", table_name="countries")
    op.drop_table("countries")
