from datetime import UTC, datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column


class CreatedAtModelMixin:
    """Mixin for models that have a creation date"""

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now(UTC))
