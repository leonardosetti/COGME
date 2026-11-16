"""Modelos ORM de prestadora e contas bancárias (SPEC-018 / future wave).

Ratificado por CCB/GP em RAT-2026-11-14-INVOICES.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import (
    BIGINT,
    CHAR,
    CheckConstraint,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.models.database import Base


class ProviderCategory(str, PyEnum):
    MEI = "mei"
    LEGAL_ENTITY = "legal_entity"


class AccountType(str, PyEnum):
    CHECKING = "checking"
    SAVINGS = "savings"
    PAYMENT = "payment"


class ProviderProfile(Base):
    """Perfil da prestadora (um por usuário)."""

    __tablename__ = "provider_profiles"
    __table_args__ = (
        CheckConstraint(
            "category IN ('mei','legal_entity')", name="chk_provider_category"
        ),
        UniqueConstraint("cnpj", name="uq_provider_cnpj"),
        Index("ix_provider_user", "user_id"),
    )

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True
    )
    legal_name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(16), nullable=False)
    cnpj: Mapped[str | None] = mapped_column(CHAR(14), nullable=True)
    address: Mapped[str | None] = mapped_column(String(500), nullable=True)
    city: Mapped[str | None] = mapped_column(String(100), nullable=True)
    state: Mapped[str | None] = mapped_column(CHAR(2), nullable=True)
    postal_code: Mapped[str | None] = mapped_column(CHAR(8), nullable=True)
    country_code: Mapped[str] = mapped_column(CHAR(2), nullable=False, default="BR")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now().astimezone(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now().astimezone(),
        onupdate=lambda: datetime.now().astimezone(),
    )


class ProviderBankAccount(Base):
    """Conta bancária da prestadora (dados sensíveis criptografados no banco)."""

    __tablename__ = "provider_bank_accounts"
    __table_args__ = (
        ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_provider_bank_account_user", ondelete="CASCADE"
        ),
        Index("ix_provider_bank_account_user", "user_id"),
        Index("ix_provider_bank_account_primary", "user_id", "is_primary",
              postgresql_where="is_primary = true"),
    )

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    account_type: Mapped[str] = mapped_column(String(16), nullable=False)
    bank_code: Mapped[str] = mapped_column(CHAR(3), nullable=False)  # COMPE
    bank_name: Mapped[str] = mapped_column(String(100), nullable=False)
    branch: Mapped[str] = mapped_column(String(10), nullable=False)
    account_number: Mapped[str] = mapped_column(String(20), nullable=False)
    account_digit: Mapped[str] = mapped_column(String(2), nullable=False)
    swift_bic: Mapped[str | None] = mapped_column(String(11), nullable=True)
    iban: Mapped[str | None] = mapped_column(String(34), nullable=True)
    account_holder: Mapped[str] = mapped_column(String(255), nullable=False)
    currency: Mapped[str] = mapped_column(CHAR(3), nullable=False, default="BRL")
    is_primary: Mapped[bool] = mapped_column(nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now().astimezone(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now().astimezone(),
        onupdate=lambda: datetime.now().astimezone(),
    )
