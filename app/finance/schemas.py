from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class STransaction(BaseModel):
    # Эта настройка позволяет Pydantic читать данные прямо из моделей SQLAlchemy
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    wallet_id: int
    category_id: int
    amount: Decimal
    transaction_type: str
    quantity: Decimal
    unit: str
    is_essential: bool
    created_at: datetime
    updated_at: datetime

class STransactionCreate(BaseModel):
    # То, что реально нужно при создании (без ID и дат)
    wallet_id: int
    category_id: int
    amount: Decimal = Field(gt=0)
    transaction_type: str = Field(pattern="^(income|expense)$")
    quantity: Decimal = Field(default=Decimal("1.0"), gt=0)
    unit: str = Field(default="unit")
    is_essential: bool = Field(default=True)
