"""Modelo ORM da tabela ``account_lifecycle_events`` (SPEC-022).

Auditoria de ciclo de vida da conta (sem PII).
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import (
    BIGINT,
    CHAR,
    CheckConstraint,
    DateTime,
    Enum as SAEnum,
    ForeignKey,
    Index,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.models.database import Base


class LifecycleEventType(str, PyEnum):
    """Tipos de evento de ciclo de vida (SPEC-022 §3.1)."""

    CREATED = "CREATED"
    ACTIVATED = "ACTIVATED"
    DORMANT_AUTO = "DORMANT_AUTO"
    DORMANT_MANUAL = "DORMANT_MANUAL"
    REACTIVATED = "REACTIVATED"
    DELETED = "DELETED"
    ANONYMIZED = "ANONYMIZED"


class AccountLifecycleEvent(Base):
    """Evento de ciclo de vida da conta (auditoria sem PII)."""

    __tablename__ = "account_lifecycle_events"
    __table_args__ = (
        CheckConstraint(
            "event_type IN ('CREATED','ACTIVATED','DORMANT_AUTO','DORMANT_MANUAL','REACTIVATED','DELETED','ANONYMIZED')",
            name="chk_lifecycle_event_type",
        ),
        CheckConstraint(
            "from_status IN ('active','dormant','deleted')",
            name="chk_lifecycle_from_status",
        ),
        CheckConstraint(
            "to_status IN ('active','dormant','deleted')",
            name="chk_lifecycle_to_status",
        ),
        Index("ix_lifecycle_user_created", "user_id", "created_at"),
        Index("ix_lifecycle_type", "event_type"),
    )

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    event_type: Mapped[LifecycleEventType] = mapped_column(
        SAEnum(LifecycleEventType, name="lifecycle_event_type", create_constraint=False),
        nullable=False,
    )
    from_status: Mapped[str | None] = mapped_column(
        CHAR(16), nullable=True
    )
    to_status: Mapped[str] = mapped_column(
        CHAR(16), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now().astimezone(),
    )