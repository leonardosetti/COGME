"""Modelo ORM da tabela ``clients`` (SPEC-019 / future wave).

Diretório de clientes para emissão de invoices.
Ratificado por CCB/GP em RAT-2026-11-14-INVOICES.
"""

from __future__ import annotations

from datetime import datetime

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
    VARCHAR,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.models.database import Base


class Client(Base):
    """Cliente para emissão de invoices.

    Atributos:
        id: Chave primária.
        owner_user_id: Usuário dono do cliente (FK → users.id).
        name: Nome do cliente.
        tax_id_digits: CPF/CNPJ só dígitos. Nullable: clientes internacionais
            (tipo ``foreign``) não têm documento brasileiro.
        tax_id_type: Tipo do documento (cpf, cnpj, foreign).
        email: E-mail do cliente (opcional).
        phone: Telefone do cliente (opcional).
        address: Endereço do cliente (opcional).
        country_code: Código do país ISO 3166-1 (padrão BR).
        status: Status do cliente (active, inactive).
        created_at: Criação do registro.
        updated_at: Última atualização.
    """

    __tablename__ = "clients"
    __table_args__ = (
        CheckConstraint("status IN ('active','inactive')", name="chk_clients_status"),
        UniqueConstraint("owner_user_id", "tax_id_digits", name="uq_clients_owner_tax"),
        ForeignKeyConstraint(
            ["owner_user_id"], ["users.id"], name="fk_clients_owner", ondelete="CASCADE"
        ),
    )

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    owner_user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    tax_id_digits: Mapped[str | None] = mapped_column(VARCHAR(32), nullable=True)
    tax_id_type: Mapped[str] = mapped_column(String(16), nullable=False)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    address: Mapped[str | None] = mapped_column(String(240), nullable=True)
    country_code: Mapped[str] = mapped_column(CHAR(2), nullable=False, default="BR")
    status: Mapped[str] = mapped_column(String(16), nullable=False, default="active")
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


# Índices para listagem
Index("ix_clients_owner", Client.owner_user_id)
Index("ix_clients_tax_id", Client.tax_id_digits)
Index("ix_clients_status", Client.status)


class Country(Base):
    """País (ISO 3166-1 alpha-2), tabela ``countries`` (migração 0006).

    Usado para validar o ``country_code`` de clientes internacionais.
    """

    __tablename__ = "countries"
    code: Mapped[str] = mapped_column(CHAR(2), primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
