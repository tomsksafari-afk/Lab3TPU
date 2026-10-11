from sqlalchemy.orm import Mapped, mapped_column

from core.models.Base import Base



class Users(Base):
    __tablename__ = "users"
    
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True) 
    password: Mapped[str] = mapped_column(nullable=False)
