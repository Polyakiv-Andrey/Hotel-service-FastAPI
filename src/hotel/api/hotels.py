from typing import List

from fastapi import APIRouter

from .. import tables
from ..database import Session
from ..models.schemas import Hotel

router = APIRouter(
    prefix="/hotels",
)


@router.get("/", response_model=List[Hotel])
def get_list_hotels():
    session = Session()
    hotels = (session.query(tables.Hotel).all())
    return hotels

