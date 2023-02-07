from typing import List

from fastapi import Depends

from src.hotel import tables
from src.hotel.database import get_session
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
