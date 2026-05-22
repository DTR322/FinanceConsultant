from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, int_pk, str_uniq  # используем твой str_uniq для email


class User(Base):
    """Пользователь системы"""
    id: Mapped[int_pk]
    email: Mapped[str_uniq]
    password: Mapped[str] = mapped_column(nullable=False)

    is_demo_user: Mapped[bool] = mapped_column(default=True, server_default="true", nullable=False)
    is_full_user: Mapped[bool] = mapped_column(default=False, server_default="false", nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default="false", nullable=False)

    extend_existing = True

    def __repr__(self):
        return f"User(id={self.id}, email={self.email})"