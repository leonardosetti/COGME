"""Unique (issuer_tax_id_digits, invoice_number) em invoices (B-04).

Substitui o unique global uq_invoices_invoice_number por um único composto
por emissor, permitindo o mesmo número de invoice para emissores distintos
no mesmo mês (next_invoice_number já é por issuer_tax_id_digits).
"""

from __future__ import annotations

from alembic import op

# revision identifiers, used by Alembic.
revision = "0015_invoice_unique"
down_revision = "0014_deleted_at_provider_cnpjs"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint("uq_invoices_invoice_number", "invoices", type_="unique")
    op.create_unique_constraint(
        "uq_invoices_issuer_number",
        "invoices",
        ["issuer_tax_id_digits", "invoice_number"],
    )


def downgrade() -> None:
    op.drop_constraint("uq_invoices_issuer_number", "invoices", type_="unique")
    op.create_unique_constraint("uq_invoices_invoice_number", "invoices", ["invoice_number"])
