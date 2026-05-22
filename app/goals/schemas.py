from decimal import Decimal
from datetime import date
from pydantic import BaseModel, ConfigDict

class SGoal(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    title: str
    target_amount: Decimal
    accumulated_amount: Decimal
    deadline: date
    priority: int
