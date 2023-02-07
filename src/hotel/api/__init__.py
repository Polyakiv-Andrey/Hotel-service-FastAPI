from fastapi import APIRouter
from .hotels import router as hotel_router


router = APIRouter()
router.include_router(hotel_router)
