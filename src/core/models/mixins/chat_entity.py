from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class ChatEntityModelMixin:
    """Mixin for chat-like models"""

    bio: Mapped[str] = mapped_column(String(100), nullable=True, default="")
    avatar_url: Mapped[str] = mapped_column(String(512), nullable=True)
