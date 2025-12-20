from datetime import UTC, datetime

from sqlalchemy import TIMESTAMP, Index, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import ChatEntityModelMixin, CreatedAtModelMixin


class User(ChatEntityModelMixin, CreatedAtModelMixin, Base):
    """Represents a user"""

    username: Mapped[str] = mapped_column(
        String(20), unique=True, nullable=False, index=True
    )
    email_hash: Mapped[str] = mapped_column(
        String(60), unique=True, nullable=False, index=True
    )
    public_key: Mapped[str] = mapped_column(Text, nullable=False)
    device_ids: Mapped[dict] = mapped_column(JSONB, nullable=False, default=list)
    last_seen: Mapped[datetime] = mapped_column(
        TIMESTAMP, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )

    __table_args__ = (
        Index("idx_username_lookup", "username"),
        Index("idx_email_lookup", "email_hash"),
    )
