from typing import List

from fastapi import Depends, HTTPException
from starlette import status

from src.hotel import tables
from src.hotel.database import get_session
from src.hotel.models.hotels import CreateHotel
from src.hotel.tables import Hotel


class HotelService:
    def __init__(self, session=Depends(get_session)):
        self.session = session

    def get_list(self, hotel_name: str = None) -> List[Hotel]:
        query = self.session.query(tables.Hotel)
        if hotel_name:
            query = query.filter_by(hotel_name=hotel_name)
        hotels = query.all()
        return hotels

    def get(self, hotel_id: tables.Hotel.id) -> Hotel:
        hotel = self.session.query(
            tables.Hotel
        ).filter_by(id=hotel_id).first()
        if not hotel:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return hotel

    def create(self, hotel_data: CreateHotel) -> tables.Hotel:
        hotel = tables.Hotel(**hotel_data.dict())
        self.session.add(hotel)
        self.session.commit()
        return hotel


