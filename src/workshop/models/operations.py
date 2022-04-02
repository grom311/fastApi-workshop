from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from datetime import date
from enum import Enum

class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class Operation(BaseModel):
    id: int
    data: date
    kind: OperationKind
    amount: Decimal
    descriptions: Optional[str]

    class Config:
        orm_mode = True
