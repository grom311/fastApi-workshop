from typing import List
from fastapi import APIRouter
from models.operations import Operation
from fastapi import Depends

from services.operations import OperationsService

router = APIRouter(
    prefix='/operations',
)

@router.get('/', response_model=List[Operation])
def get_operations(service: OperationsService = Depends()):
    return service.get_list()
    