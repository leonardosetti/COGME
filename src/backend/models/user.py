"""Modelo ORM da tabela ``users`` (SPEC-017, SPEC-022).

Identidade, autenticação e ciclo de vida da conta.
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
    Index,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.models.database import Base


class UserStatus(str, PyEnum):
    """Estados do ciclo de vida da conta (SPEC-022)."""

    ACTIVE = "active"
    DORMANT = "dormant"
    DELETED = "deleted"


class User(Base):
    """Usuário do sistema (identidade + ciclo de vida).

    Atributos:
        id: Chave primária.
        internal_username_hash: Hash HMAC-SHA256 opaco (não expõe CPF/email).
        name: Nome completo.
        email: Email (único, imutável, lowercase).
        phone: Telefone (opcional).
        cpf: CPF só dígitos (único, imutável, 11 dígitos).
        password_hash: Hash Argon2id da senha.
        status: Estado da conta (active/dormant/deleted).
        dormant_since: Timestamp da dormência automática.
        last_login_at: Último login bem-sucedido.
        created_at: Criação do registro.
        updated_at: Última atualização.
    """

    __tablename__ = "users"
    __table_args__ = (
        CheckConstraint(
            "status IN ('active','dormant','deleted')", name="chk_users_status"
        ),
        UniqueConstraint("email", name="uq_users_email"),
        UniqueConstraint("cpf", name="uq_users_cpf"),
        UniqueConstraint("internal_username_hash", name="uq_users_internal_username"),
        Index("ix_users_email", "email"),
        Index("ix_users_cpf", "cpf"),
        Index("ix_users_status", "status"),
        Index("ix_users_last_login", "last_login_at"),
    )

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    internal_username_hash: Mapped[str] = mapped_column(
        String(64), nullable=False
    )  # HMAC-SHA256 hex
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(
        String(16), nullable=False, default=UserStatus.ACTIVE
    )
    dormant_since: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    last_login_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
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


class UserLoginIdentifierKind(str, PyEnum):
    """Tipo de identificador de login."""

    EMAIL = "email"
    CPF = "cpf"
    CNPJ = "cnpj"


class UserLoginIdentifier(Base):
    """Identificadores de login (email, CPF, CNPJ) protegidos por HMAC.

    Permite login por qualquer um dos três, sem expor o valor real em logs
    ou permitir enumeração via hash simples.
    """

    __tablename__ = "user_login_identifiers"
    __table_args__ = (
        UniqueConstraint("kind", "lookup_hmac", name="uq_user_login_kind_hmac"),
        # Partial unique index for active (non-retired) identifiers per user+kind
        # Matches migration: CREATE UNIQUE INDEX uq_user_login_user_kind_active
        # ON user_login_identifiers (user_id, kind) WHERE retired_at IS NULL
        Index("ix_user_login_user_kind", "user_id", "kind"),
        Index("ix_user_login_hmac", "lookup_hmac"),
        Index(
            "uq_user_login_user_kind_active",
            "user_id",
            "kind",
            unique=True,
            postgresql_where="retired_at IS NULL",
        ),
    )

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    kind: Mapped[str] = mapped_column(
        String(16), nullable=False
    )
    lookup_hmac: Mapped[str] = mapped_column(
        String(64), nullable=False
    )  # HMAC-SHA256 hex
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now().astimezone(),
    )
    retired_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )


class UserSession(Base):
    """Sessão de usuário (token opaco, revogável, expirável)."""

    __tablename__ = "user_sessions"
    __table_args__ = (
        UniqueConstraint("token_hash", name="uq_user_sessions_token"),
        Index("ix_user_sessions_user", "user_id"),
        Index("ix_user_sessions_expires", "expires_at"),
        Index("ix_user_sessions_revoked", "revoked_at"),
    )

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    token_hash: Mapped[str] = mapped_column(
        String(64), nullable=False
    )  # SHA-256 hex
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now().astimezone(),
    )
    last_seen_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now().astimezone(),
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    revoked_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )


class PasswordResetToken(Base):
    """Token de recuperação de senha (single-use, TTL curto)."""

    __tablename__ = "password_reset_tokens"
    __table_args__ = (
        UniqueConstraint("token_hash", name="uq_pwd_reset_token"),
        Index("ix_pwd_reset_user", "user_id"),
        Index("ix_pwd_reset_expires", "expires_at"),
    )

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    token_hash: Mapped[str] = mapped_column(
        String(64), nullable=False
    )  # SHA-256 hex
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now().astimezone(),
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    used_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
