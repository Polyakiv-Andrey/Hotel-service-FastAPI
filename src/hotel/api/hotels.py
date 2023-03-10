from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from starlette import status

from ..models.hotels import ListHotel, CreateHotel, DetailHotel, UpdateHotel
from ..services.hotels import HotelService

router = APIRouter(
    prefix="/hotels",
)


@router.get("/", response_model=List[ListHotel])
def get_list_hotels(
        service: HotelService = Depends(),
        hotel_name: Optional[str] = None
):
    return service.get_list(hotel_name)


@router.get("/{hotel_id}", response_model=DetailHotel)
def get_hotel_detail_page(
        hotel_id: int,
        service: HotelService = Depends()
):
    return service.get(hotel_id)


@router.post("/", response_model=CreateHotel)
def add_new_hotel(
    hotel_data: CreateHotel,
    service: HotelService = Depends(),
):
    return service.create(hotel_data)


@router.put("/{hotel_id}", response_model=UpdateHotel)
def update_hotel_info(
        hotel_id: int,
        hotel_data: UpdateHotel,
        service: HotelService = Depends(),
):
    return service.update(hotel_id=hotel_id, hotel_data=hotel_data)


@router.delete("/{hotel_id}")
def hotel_delete(
        hotel_id: int,
        service: HotelService = Depends(),
):
    service.delete(hotel_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
