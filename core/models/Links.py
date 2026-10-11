from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.sql import func

from core.models.Base import Base



class Links(Base):
    __tablename__ = "links"
    
    original_url: Mapped[str] = mapped_column()
    short_code: Mapped[str] = mapped_column(unique=True, index=True)
    clicks: Mapped[int] = mapped_column(default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())