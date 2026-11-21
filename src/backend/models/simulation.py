"""Modelo ORM da tabela ``simulations`` (SPEC-020 / future wave).

Simulações salvas para histórico de invoices.
Ratificado por CCB/GP em RAT-2026-11-14-INVOICES.
"""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    BIGINT,
    BOOLEAN,
    CHAR,
    CheckConstraint,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    Numeric,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.models.database import Base


class Simulation(Base):
    """Simulação salva para histórico de invoices.

    Atributos:
        id: Chave primária.
        owner_user_id: Usuário dono da simulação (FK → users.id).
        client_id: Cliente (FK → clients.id, opcional).
        name: Nome da simulação.
        regime: Regime de cobrança.
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
        created_at: Criação do registro.
        updated_at: Última atualização.
    """

    __tablename__ = "simulations"
    __table_args__ = (
        CheckConstraint(
            "regime IN ('hourly','daily','weekly','monthly','fixed')",
            name="chk_simulations_regime",
        ),
        CheckConstraint("currency IN ('USD','EUR')", name="chk_simulations_currency"),
        # Identity check: gross_brl - spread_brl - iof_brl = net_brl
        CheckConstraint(
            "gross_brl - spread_brl - iof_brl = net_brl",
            name="chk_simulation_identity",
        ),
        ForeignKeyConstraint(
            ["owner_user_id"], ["users.id"], name="fk_simulations_owner", ondelete="CASCADE"
        ),
        ForeignKeyConstraint(
            ["client_id"], ["clients.id"], name="fk_simulations_client", ondelete="SET NULL"
        ),
    )

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    owner_user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    client_id: Mapped[int | None] = mapped_column(
        BIGINT, ForeignKey("clients.id", ondelete="SET NULL"), nullable=True
    )
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    regime: Mapped[str] = mapped_column(String(16), nullable=False)
    currency: Mapped[str] = mapped_column(CHAR(3), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    quantity: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    spread_pct: Mapped[Decimal] = mapped_column(Numeric(6, 4), nullable=False)
    iof_pct: Mapped[Decimal] = mapped_column(Numeric(6, 4), nullable=False)
    gross_foreign: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    gross_brl: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    spread_brl: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    iof_brl: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    net_brl: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    effective_rate: Mapped[Decimal] = mapped_column(Numeric(18, 6), nullable=False)
    quote_rate: Mapped[Decimal] = mapped_column(Numeric(18, 6), nullable=False)
    quote_source: Mapped[str] = mapped_column(String(20), nullable=False)
    quote_bulletin: Mapped[str | None] = mapped_column(String(40), nullable=True)
    quoted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    stale: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, default=False)
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=lambda: datetime.now().astimezone()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=lambda: datetime.now().astimezone()
    )

    # Relationships (lazy='raise' para evitar N+1 acidental)
    # owner = relationship("User", lazy="raise")
    # client = relationship("Client", lazy="raise")


# Índices para listagem
Index("ix_simulations_owner_created", Simulation.owner_user_id, Simulation.created_at)
Index("ix_simulations_client", Simulation.client_id)
Index("ix_simulations_stale", Simulation.stale)
