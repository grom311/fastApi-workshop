from typing import List, Optional
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_session
import tables
from models.operations import OperationUpdate, OperationKind, OperationCreate


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, operation_id: int) -> tables.Operation:
        operation = (self.session.query(tables.Operation)
        .filter_by(id=operation_id, user_id=user_id)
        .first())
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation
        
    def get_list(self, user_id: int, kind: Optional[OperationKind] = None)-> List[tables.Operation]:
        query = self.session.query(tables.Operation).filter_by(user_id=user_id)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations
        
    def create(self, user_id: int, operation_data: OperationCreate) -> tables.Operation:
        operration = tables.Operation(
            **operation_data.dict(),
            user_id=user_id)
        self.session.add(operration)
        self.session.commit()
        return operration

    def get(self, user_id: int, operation_id: int) -> tables.Operation:
        return self._get(user_id, operation_id)

    def update(self, user_id: int, operation_id: int,  operation_data: OperationUpdate) -> tables.Operation:
        operation = self._get(user_id, operation_id)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, user_id: int, operation_id: int):
        operation = self._get(user_id, operation_id)
        self.session.delete(operation)
        
