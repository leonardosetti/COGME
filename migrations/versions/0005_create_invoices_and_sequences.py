"""Create invoices table + invoice_sequences (DEC-04, DEC-05, DEC-06, DEC-07).

Ratificado por CCB/GP em RAT-2026-11-14-INVOICES (consolida DEC-04..07).
Base: Opção A (Snapshot Completo) do RELATORIO-PERSISTENCIA-RECUPERACAO-INVOICES.
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0005_invoices"
down_revision = "0004_simulations"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ---------- Tabela invoice_sequences (DEC-06: numeração sem SEQUENCE) ----------
    op.create_table(
        "invoice_sequences",
        sa.Column("issuer_tax_id_digits", sa.CHAR(14), nullable=False),
        sa.Column("year_month", sa.CHAR(7), nullable=False),  # '2026-11'
        sa.Column("last_number", sa.Integer(), nullable=False, server_default=sa.text("0")),
        sa.PrimaryKeyConstraint("issuer_tax_id_digits", "year_month", name="pk_invoice_sequences"),
    )

    # Function atômica: next_invoice_number(issuer_tax_id_digits) → 'INV-202611-0001'
    op.execute(
        """
        CREATE OR REPLACE FUNCTION next_invoice_number(p_issuer_tax_id_digits CHAR(14))
        RETURNS TEXT LANGUAGE plpgsql AS $$
        DECLARE
            v_ym        CHAR(7) := to_char(NOW(), 'YYYY-MM');
            v_next      INT;
            v_number    TEXT;
        BEGIN
            LOOP
                UPDATE invoice_sequences
                   SET last_number = last_number + 1
                 WHERE issuer_tax_id_digits = p_issuer_tax_id_digits
                   AND year_month = v_ym
                RETURNING last_number INTO v_next;
                IF FOUND THEN
                    v_number := 'INV-' || replace(v_ym, '-', '') || '-' ||
                        lpad(v_next::TEXT, 4, '0');
                    RETURN v_number;
                END IF;
                -- Race condition: tenta inserir nova linha
                BEGIN
                    INSERT INTO invoice_sequences (issuer_tax_id_digits, year_month, last_number)
                    VALUES (p_issuer_tax_id_digits, v_ym, 0)
                    ON CONFLICT (issuer_tax_id_digits, year_month) DO NOTHING;
                EXCEPTION WHEN unique_violation THEN
                    -- Outra transação inseriu; loop continua
                END;
            END LOOP;
        END;
        $$;
        """
    )

    # ---------- Tabela invoices (Opção A: Snapshot Completo) ----------
    op.create_table(
        "invoices",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("owner_user_id", sa.BigInteger(), nullable=False),
        sa.Column("client_id", sa.BigInteger(), nullable=True),
        sa.Column("simulation_id", sa.BigInteger(), nullable=True),
        sa.Column("invoice_number", sa.String(32), nullable=False),
        sa.Column("status", sa.String(16), nullable=False, server_default=sa.text("'finalized'")),
        sa.Column("locale", sa.String(8), nullable=False, server_default=sa.text("'pt-BR'")),
        sa.Column("client_country_code", sa.CHAR(2), nullable=False),
        # Partes (DEC-03: endereço/bancários NULLable)
        sa.Column("issuer_name", sa.String(120), nullable=False),
        sa.Column("issuer_tax_id_digits", sa.CHAR(14), nullable=False),
        sa.Column("issuer_address", sa.String(240), nullable=True),
        sa.Column("client_name", sa.String(120), nullable=False),
        sa.Column("client_tax_id_digits", sa.CHAR(14), nullable=False),
        sa.Column("client_address", sa.String(240), nullable=True),
        # Bancários opcionais (DEC-03)
        sa.Column("banco", sa.String(80), nullable=True),
        sa.Column("agencia", sa.String(20), nullable=True),
        sa.Column("conta_com_digito", sa.String(30), nullable=True),
        sa.Column("pix_key", sa.String(80), nullable=True),
        # Período e descrição
        sa.Column("periodo_inicio", sa.Date(), nullable=False),
        sa.Column("periodo_fim", sa.Date(), nullable=False),
        sa.Column("description", sa.String(500), nullable=False),
        # Parâmetros de cálculo
        sa.Column("regime", sa.String(16), nullable=False),
        sa.Column("currency", sa.CHAR(3), nullable=False),
        sa.Column("amount", sa.Numeric(18, 2), nullable=False),
        sa.Column("quantity", sa.Numeric(10, 2), nullable=True),
        sa.Column("spread_pct", sa.Numeric(6, 4), nullable=False),
        sa.Column("iof_pct", sa.Numeric(6, 4), nullable=False),
        # Valores calculados (snapshot para reprodutibilidade)
        sa.Column("gross_foreign", sa.Numeric(18, 2), nullable=False),
        sa.Column("gross_brl", sa.Numeric(18, 2), nullable=False),
        sa.Column("spread_brl", sa.Numeric(18, 2), nullable=False),
        sa.Column("iof_brl", sa.Numeric(18, 2), nullable=False),
        sa.Column("net_brl", sa.Numeric(18, 2), nullable=False),
        sa.Column("effective_rate", sa.Numeric(18, 6), nullable=False),
        # Cotação usada (crítico para reprodutibilidade)
        sa.Column("quote_rate", sa.Numeric(18, 6), nullable=False),
        sa.Column("quote_source", sa.String(20), nullable=False),
        sa.Column("quote_bulletin", sa.String(40), nullable=True),
        sa.Column("quoted_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("stale", sa.Boolean(), nullable=False, server_default=sa.text("FALSE")),
        # Lifecycle
        sa.Column("finalized_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("supersedes_invoice_id", sa.BigInteger(), nullable=True),
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
        # Constraints
        sa.PrimaryKeyConstraint("id", name="pk_invoices"),
        sa.CheckConstraint(
            "status IN ('draft','finalized')",
            name="chk_invoices_status",
        ),
        sa.CheckConstraint(
            "locale IN ('pt-BR','en')",
            name="chk_invoices_locale",
        ),
        sa.CheckConstraint(
            "regime IN ('hourly','daily','weekly','monthly','fixed')",
            name="chk_invoices_regime",
        ),
        sa.CheckConstraint(
            "currency IN ('USD','EUR')",
            name="chk_invoices_currency",
        ),
        # Identity check: gross_brl - spread_brl - iof_brl = net_brl (reprodutibilidade)
        sa.CheckConstraint(
            "gross_brl - spread_brl - iof_brl = net_brl",
            name="chk_invoice_identity",
        ),
        # Foreign Keys
        sa.ForeignKeyConstraint(
            ["owner_user_id"], ["users.id"],
            name="fk_invoices_owner_user", ondelete="RESTRICT"
        ),
        sa.ForeignKeyConstraint(
            ["client_id"], ["clients.id"],
            name="fk_invoices_client", ondelete="RESTRICT"
        ),
        sa.ForeignKeyConstraint(
            ["simulation_id"], ["simulations.id"],
            name="fk_invoices_simulation", ondelete="RESTRICT"
        ),
        sa.ForeignKeyConstraint(
            ["supersedes_invoice_id"], ["invoices.id"],
            name="fk_invoices_supersedes", ondelete="SET NULL"
        ),
        # Unique
        sa.UniqueConstraint("invoice_number", name="uq_invoices_invoice_number"),
    )

    # Índices para listagem e erase
    op.create_index("ix_invoices_owner_created", "invoices", ["owner_user_id", "created_at"])
    op.create_index("ix_invoices_status", "invoices", ["status"])
    op.create_index("ix_invoices_client", "invoices", ["client_id"])
    op.create_index("ix_invoices_invoice_number", "invoices", ["invoice_number"])
    op.create_index("ix_invoices_finalized_at", "invoices", ["finalized_at"])


def downgrade() -> None:
    # Drop indexes
    op.drop_index("ix_invoices_finalized_at", table_name="invoices")
    op.drop_index("ix_invoices_invoice_number", table_name="invoices")
    op.drop_index("ix_invoices_client", table_name="invoices")
    op.drop_index("ix_invoices_status", table_name="invoices")
    op.drop_index("ix_invoices_owner_created", table_name="invoices")

    # Drop tables (FKs handled by drop order)
    op.drop_table("invoices")
    op.drop_table("invoice_sequences")

    # Drop function
    op.execute("DROP FUNCTION IF EXISTS next_invoice_number(CHAR(14))")
