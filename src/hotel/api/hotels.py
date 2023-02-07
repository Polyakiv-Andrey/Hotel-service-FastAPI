from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends

from ..models.hotels import Hotel
from ..services.hotels import HotelService

router = APIRouter(
    prefix="/hotels",
)


@router.get("/", response_model=List[Hotel])
def get_list_hotels(
        service: HotelService = Depends(),
        hotel_name: Optional[str] = None
):
    return service.get_list(hotel_name)

