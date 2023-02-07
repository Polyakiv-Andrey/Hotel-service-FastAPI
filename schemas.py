import datetime
from datetime import date
from pydantic import BaseModel, Field, validator


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
    date_of_settlement: date
    date_of_departure: date

    @classmethod
    @validator("date_of_settlement", "date_of_departure")
    def date_of_settlement_validation(cls, **field_value):
        if field_value["date_of_settlement"] < datetime.datetime.now() or \
                field_value["date_of_departure"] < datetime.datetime.now():
            raise ValueError("You can't buy a ticket for the past")
        if field_value["date_of_settlement"] > field_value["date_of_departure"]:
            raise ValueError("date_of_departure mast be latest then date_of_settlement")
        return field_value


