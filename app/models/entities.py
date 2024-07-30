from sqlalchemy import Uuid, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[Uuid] = mapped_column(Uuid, primary_key=True)
