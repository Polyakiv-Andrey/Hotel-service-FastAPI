from pydantic import BaseModel, Field


class BaseHotel(BaseModel):
    hotel_name: str
    description: str
    price_for_day: float
    rate: int = Field(..., ge=1, le=5)

    class Config:
        orm_mode = True


class ListHotel(BaseHotel):
    id: int


class DetailHotel(BaseHotel):
    id: int


class CreateHotel(BaseHotel):
    pass
