from datetime import date
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base, int_pk, str_indexed, decimal_14_2


class Goal(Base):
    """Твои цели: Досрочное погашение, Квартира и т.д."""
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)

    title: Mapped[str_indexed]
    target_amount: Mapped[decimal_14_2]
    # Сколько уже "виртуально" выделено под эту цель
    accumulated_amount: Mapped[decimal_14_2] = mapped_column(server_default=text("0.0"))

    deadline: Mapped[date]
    priority: Mapped[int] = mapped_column(server_default=text("1"), index=True)