"""Modelo ORM da tabela ``invoices`` (DEC-04, DEC-05, DEC-06, DEC-07).

Snapshot completo (Opção A) para reprodutibilidade total.
Ratificado por CCB/GP em RAT-2026-11-14-INVOICES.
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    BIGINT,
    BOOLEAN,
    CHAR,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Numeric,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.models.database import Base


class Invoice(Base):
    """Invoice persistida (snapshot completo para reprodutibilidade).

    Atributos:
        id: Chave primária.
        owner_user_id: Usuário dono da invoice (FK → users.id).
        client_id: Cliente (FK → clients.id, opcional).
        simulation_id: Simulação origem (FK → simulations.id, opcional).
        invoice_number: Número único (formato INV-YYYYMM-SEQ, DEC-06).
        status: ``draft`` ou ``finalized`` (DEC-05).
        locale: ``pt-BR`` ou ``en`` (DEC-07: país→locale).
        client_country_code: ISO 3166-1 do cliente (DEC-07).
        issuer_name: Nome do emitente (NOT NULL).
        issuer_tax_id_digits: CPF/CNPJ do emitente só dígitos (NOT NULL).
        issuer_address: Endereço do emitente (NULLable, DEC-03).
        client_name: Nome do cliente (NOT NULL).
        client_tax_id_digits: CPF/CNPJ do cliente só dígitos (NOT NULL).
        client_address: Endereço do cliente (NULLable, DEC-03).
        banco: Banco do emitente (NULLable, DEC-03).
        agencia: Agência (NULLable, DEC-03).
        conta_com_digito: Conta com dígito (NULLable, DEC-03).
        pix_key: Chave PIX (NULLable, DEC-03).
        periodo_inicio: Início do período de prestação (NOT NULL).
        periodo_fim: Fim do período de prestação (NOT NULL).
        description: Descrição do serviço (NOT NULL).
        regime: Regime de cobrança (NOT NULL).
        currency: Moeda estrangeira (USD/EUR).
        amount: Valor por unidade do regime.
        quantity: Quantidade de unidades (NULL em regime fixed).
        spread_pct: Spread informado pelo usuário (%).
        iof_pct: IOF informado pelo usuário (%).
        gross_foreign: Bruto na moeda estrangeira (snapshot).
        gross_brl: Bruto em BRL (snapshot).
        spread_brl: Spread em BRL (snapshot).
        iof_brl: IOF em BRL (snapshot).
        net_brl: Líquido em BRL (snapshot).
        effective_rate: Taxa efetiva BRL/unidade estrangeira (snapshot, 6 casas).
        quote_rate: Cotação usada (crítico para reprodutibilidade).
        quote_source: Fonte da cotação (frankfurter/ptax).
        quote_bulletin: Boletim PTAX (opcional).
        quoted_at: Instante da cotação informado pela fonte.
        stale: Se a cotação veio de cache vencido.
        finalized_at: Instante da finalização (só em finalized).
        supersedes_invoice_id: Invoice anterior no clone (FK auto-ref, SET NULL).
        created_at: Criação do registro.
        updated_at: Última atualização.
    """

    __tablename__ = "invoices"
    __table_args__ = (
        CheckConstraint("status IN ('draft','finalized')", name="chk_invoices_status"),
        CheckConstraint("locale IN ('pt-BR','en')", name="chk_invoices_locale"),
        CheckConstraint(
            "regime IN ('hourly','daily','weekly','monthly','fixed')",
            name="chk_invoices_regime",
        ),
        CheckConstraint("currency IN ('USD','EUR')", name="chk_invoices_currency"),
        # Identity check: gross_brl - spread_brl - iof_brl = net_brl
        CheckConstraint(
            "gross_brl - spread_brl - iof_brl = net_brl",
            name="chk_invoice_identity",
        ),
        UniqueConstraint("invoice_number", name="uq_invoices_invoice_number"),
    )

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    owner_user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )
    client_id: Mapped[int | None] = mapped_column(
        BIGINT, ForeignKey("clients.id", ondelete="RESTRICT"), nullable=True
    )
    simulation_id: Mapped[int | None] = mapped_column(
        BIGINT, ForeignKey("simulations.id", ondelete="RESTRICT"), nullable=True
    )
    invoice_number: Mapped[str] = mapped_column(String(32), nullable=False)
    status: Mapped[str] = mapped_column(String(16), nullable=False, default="finalized")
    locale: Mapped[str] = mapped_column(String(8), nullable=False, default="pt-BR")
    client_country_code: Mapped[str] = mapped_column(CHAR(2), nullable=False)

    # Partes
    issuer_name: Mapped[str] = mapped_column(String(120), nullable=False)
    issuer_tax_id_digits: Mapped[str] = mapped_column(CHAR(14), nullable=False)
    issuer_address: Mapped[str | None] = mapped_column(String(240), nullable=True)
    client_name: Mapped[str] = mapped_column(String(120), nullable=False)
    client_tax_id_digits: Mapped[str] = mapped_column(CHAR(14), nullable=False)
    client_address: Mapped[str | None] = mapped_column(String(240), nullable=True)

    # Bancários opcionais (DEC-03)
    banco: Mapped[str | None] = mapped_column(String(80), nullable=True)
    agencia: Mapped[str | None] = mapped_column(String(20), nullable=True)
    conta_com_digito: Mapped[str | None] = mapped_column(String(30), nullable=True)
    pix_key: Mapped[str | None] = mapped_column(String(80), nullable=True)

    # Período e descrição
    periodo_inicio: Mapped[date] = mapped_column(Date(), nullable=False)
    periodo_fim: Mapped[date] = mapped_column(Date(), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)

    # Parâmetros de cálculo
    regime: Mapped[str] = mapped_column(String(16), nullable=False)
    currency: Mapped[str] = mapped_column(CHAR(3), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    quantity: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    spread_pct: Mapped[Decimal] = mapped_column(Numeric(6, 4), nullable=False)
    iof_pct: Mapped[Decimal] = mapped_column(Numeric(6, 4), nullable=False)

    # Valores calculados (snapshot)
    gross_foreign: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    gross_brl: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    spread_brl: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    iof_brl: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    net_brl: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    effective_rate: Mapped[Decimal] = mapped_column(Numeric(18, 6), nullable=False)

    # Cotação usada
    quote_rate: Mapped[Decimal] = mapped_column(Numeric(18, 6), nullable=False)
    quote_source: Mapped[str] = mapped_column(String(20), nullable=False)
    quote_bulletin: Mapped[str | None] = mapped_column(String(40), nullable=True)
    quoted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    stale: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, default=False)

    # Lifecycle
    finalized_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    supersedes_invoice_id: Mapped[int | None] = mapped_column(
        BIGINT, ForeignKey("invoices.id", ondelete="SET NULL"), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=lambda: datetime.now().astimezone()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=lambda: datetime.now().astimezone()
    )

    # Relationships (lazy='raise' para evitar N+1 acidental)
    # client = relationship("Client", lazy="raise")
    # simulation = relationship("Simulation", lazy="raise")
    # supersedes = relationship("Invoice", remote_side=[id], lazy="raise")


# Índices para listagem e erase
Index(
    "ix_invoices_owner_created",
    Invoice.owner_user_id,
    Invoice.created_at,
)
Index("ix_invoices_status", Invoice.status)
Index("ix_invoices_client", Invoice.client_id)
Index("ix_invoices_invoice_number", Invoice.invoice_number)
Index("ix_invoices_finalized_at", Invoice.finalized_at)


class InvoiceSequence(Base):
    """Sequência de numeração por emissor/mês (DEC-06).

    Chave composta: (issuer_tax_id_digits, year_month).
    year_month formato: 'YYYY-MM' (ex.: '2026-11').
    """

    __tablename__ = "invoice_sequences"
    __table_args__ = ()

    issuer_tax_id_digits: Mapped[str] = mapped_column(CHAR(14), primary_key=True)
    year_month: Mapped[str] = mapped_column(CHAR(7), primary_key=True)
    last_number: Mapped[int] = mapped_column(nullable=False, default=0)
