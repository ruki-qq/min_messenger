import uuid
from datetime import UTC, datetime, timedelta

from sqlalchemy import TIMESTAMP, ForeignKey, Index, LargeBinary, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import CreatedAtModelMixin


class PendingMessage(CreatedAtModelMixin, Base):
    """Represents a pending message"""

    sender_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    recipient_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True
    )
    encrypted_payload: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    message_type: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # text, audio, photo, video
    expires_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, default=lambda: datetime.now(UTC) + timedelta(days=30)
    )

    __table_args__ = (
        Index("idx_recipient_messages", "recipient_id", "created_at"),
        Index("idx_expires_at", "expires_at"),
    )
