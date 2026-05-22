from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class RBWalletFilter(BaseModel):

    name: str | None = Field(None, description="Поиск по названию")
    type: str | None = Field(None, description="поиск по типу")
    min_balance: Decimal | None = Field(None, ge=0, description="Минимальный баланс")

    def to_dict(self) -> dict:
        return self.model_dump(exclude_none=True)


class RBWalletCreate(BaseModel):

    name: str = Field(..., description="имя кошелька")
    type: str = Field(..., description="Тип: карта, вклад, кредит")
    balance: Decimal = Field(default=0.0, ge=0)
    interest_rate: Decimal | None = Field(..., description="процентная ставка, для вкладов, кредитов и инвестиций")
    min_payment: Decimal | None = Field(..., description="минимальный платёж, если это кредит")


class RBWalletUpdate(BaseModel):

    name: str | None = None
    type: str | None = None
    balance: Decimal | None = None
    interest_rate: Decimal | None = None
    min_payment: Decimal | None = None