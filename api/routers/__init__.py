from fastapi import APIRouter
from api.routers import finances , income , expenses

router = APIRouter(prefix="/api")

router.include_router(router=finances.router, prefix="/finances" , tags=["Finances"]) 
router.include_router(router=income.router, prefix="/income", tags=["Income"]) 
router.include_router(router=expenses.router, prefix="/expenses", tags=["Expenses"]) 
