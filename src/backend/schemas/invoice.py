"""Schemas de invoice persistida (spec-004 §5.5; SPEC-020, SPEC-021)."""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Literal
from uuid import UUID

from pydantic import Field

from src.shared.schemas import _Schema


class InvoiceCreateDraft(_Schema):
    """Entrada para criar uma invoice em status draft (SPEC-020)."""

    client_id: UUID | None = Field(
        default=None,
        description="Cliente do diretório. None = cliente fictício.",
    )
    client_fictitious: dict | None = Field(
        default=None,
        description="Dados do cliente fictício. Obrigatório se client_id=None.",
    )
    simulation_id: UUID | None = Field(
        default=None,
        description="Simulação origem (snapshot).",
    )
    locale: Literal["pt-BR", "en"] = Field(default="pt-BR")
    client_country_code: str = Field(default="BR", max_length=2)
    issuer_name: str = Field(min_length=1, max_length=120)
    issuer_tax_id_digits: str = Field(min_length=1, max_length=14)
    issuer_address: str | None = Field(default=None, max_length=240)
    client_name: str = Field(min_length=1, max_length=120)
    client_tax_id_digits: str = Field(min_length=1, max_length=14)
    client_address: str | None = Field(default=None, max_length=240)
    banco: str | None = Field(default=None, max_length=80)
    agencia: str | None = Field(default=None, max_length=20)
    conta_com_digito: str | None = Field(default=None, max_length=30)
    pix_key: str | None = Field(default=None, max_length=80)
    periodo_inicio: date
    periodo_fim: date
    description: str = Field(min_length=1, max_length=500)
    regime: str
    currency: str
    amount: Decimal
    quantity: Decimal | None = None
    spread_pct: Decimal
    iof_pct: Decimal
    gross_foreign: Decimal
    gross_brl: Decimal
    spread_brl: Decimal
    iof_brl: Decimal
    net_brl: Decimal
    effective_rate: Decimal
    quote_rate: Decimal
    quote_source: str
    quote_bulletin: str | None = None
    quoted_at: datetime
    stale: bool = False


class InvoiceUpdate(_Schema):
    """Campos atualizáveis de uma invoice draft (SPEC-020)."""

    client_id: UUID | None = None
    client_fictitious: dict | None = None
    issuer_name: str | None = Field(default=None, min_length=1, max_length=120)
    issuer_tax_id_digits: str | None = Field(default=None, max_length=14)
    issuer_address: str | None = Field(default=None, max_length=240)
    client_name: str | None = Field(default=None, min_length=1, max_length=120)
    client_tax_id_digits: str | None = Field(default=None, max_length=14)
    client_address: str | None = Field(default=None, max_length=240)
    banco: str | None = Field(default=None, max_length=80)
    agencia: str | None = Field(default=None, max_length=20)
    conta_com_digito: str | None = Field(default=None, max_length=30)
    pix_key: str | None = Field(default=None, max_length=80)
    periodo_inicio: date | None = None
    periodo_fim: date | None = None
    description: str | None = Field(default=None, min_length=1, max_length=500)


class InvoiceResponse(_Schema):
    """Resposta de invoice (SPEC-020)."""

    id: int
    owner_user_id: int
    client_id: int | None
    simulation_id: int | None
    invoice_number: str
    status: Literal["draft", "finalized"]
    locale: Literal["pt-BR", "en"]
    client_country_code: str
    finalized_at: datetime | None = None
    supersedes_invoice_id: int | None = None
    number: str
    issuer_name: str
    issuer_tax_id_digits: str
    issuer_address: str | None = None
    client_name: str
    client_tax_id_digits: str
    client_address: str | None = None
    banco: str | None = None
    agencia: str | None = None
    conta_com_digito: str | None = None
    pix_key: str | None = None
    periodo_inicio: date
    periodo_fim: date
    description: str
    regime: str
    currency: str
    amount: Decimal
    quantity: Decimal | None = None
    spread_pct: Decimal
    iof_pct: Decimal
    gross_foreign: Decimal
    gross_brl: Decimal
    spread_brl: Decimal
    iof_brl: Decimal
    net_brl: Decimal
    effective_rate: Decimal
    quote_rate: Decimal
    quote_source: str
    quote_bulletin: str | None = None
    quoted_at: datetime
    stale: bool
    created_at: datetime
    updated_at: datetime
