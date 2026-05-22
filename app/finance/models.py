from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional

from app.database import Base, int_pk, str_indexed, decimal_14_2


class Category(Base):

    __tablename__ = "categories"
    """Категории с поддержкой вложенности"""
    id: Mapped[int_pk]
    name: Mapped[str_indexed]
    # parent_id позволит делать структуру "Еда -> Рестораны"
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("categories.id"), nullable=True)

    # Отношение для дерева категорий
    subcategories: Mapped[list["Category"]] = relationship("Category")


class Transaction(Base):
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), index=True)
    # Ссылка на твой Wallet из другого модуля
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"), index=True)

    amount: Mapped[decimal_14_2]
    # "income" или "expense"
    transaction_type: Mapped[str] = mapped_column(index=True)

    # Поля для личной инфляции
    quantity: Mapped[decimal_14_2] = mapped_column(server_default="1.0")
    unit: Mapped[str] = mapped_column(server_default="unit")

    is_essential: Mapped[bool] = mapped_column(server_default="true", index=True)


