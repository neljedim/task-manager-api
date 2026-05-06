from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class TaskORM(Base):
    __tablename__ = "tasks"
    
    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default = False)