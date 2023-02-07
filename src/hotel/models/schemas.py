from pydantic import BaseModel, Field


class Hotel(BaseModel):
    id: int
    hotel_name: str
    description: str
    price_for_day: float
    rate: int = Field(..., ge=1, le=5)

    class Config:
        orm_mode = True
