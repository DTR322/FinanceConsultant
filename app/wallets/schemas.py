from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class SWallet(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    name: str
    type: str
    balance: Decimal
    interest_rate: Decimal
    min_payment: Decimal
