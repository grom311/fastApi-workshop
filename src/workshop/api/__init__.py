from fastapi import APIRouter
from .operations import router as op_router

router = APIRouter()
router.include_router(op_router)
