from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base, int_pk, str_indexed, decimal_14_2



class Wallet(Base):
    """Накопления и долги (Вклады, Кредиты, Наличные)"""
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)

    name: Mapped[str_indexed]  # "Ипотека", "Вклад Тинькофф"
    # Тип: asset (накопление) или liability (долг)
    type: Mapped[str] = mapped_column(server_default=text("'asset'"), index=True)

    balance: Mapped[decimal_14_2]  # Текущий остаток или сумма долга
    interest_rate: Mapped[decimal_14_2]  # Доходность или % по кредиту

    # Для долгов: сколько МИНИМУМ нужно платить в месяц
    min_payment: Mapped[decimal_14_2] = mapped_column(server_default=text("0.0"))