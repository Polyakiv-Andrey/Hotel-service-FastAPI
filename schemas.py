from datetime import date
from pydantic import BaseModel, Field


class Country(BaseModel):
    country_name: str


class Hotel(BaseModel):
    hotel_name: str
    description: str
    country: Country
    price_for_day: float
    rate: int = Field(..., ge=1, le=5)


class User(BaseModel):
    first_name: str
    last_name: str
    mail: str
    age: int = Field(..., ge=18, le=100)


class Order(BaseModel):
    hotel: Hotel
    user: User
    Date_of_settlement: date
    date_of_departure: date


