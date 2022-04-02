from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from datetime import date
from enum import Enum

class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'

class OperationBase(BaseModel):
    data: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]

class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True

class OperationCreate(OperationBase):
    pass

class OperationUpdate(OperationBase):
    pass