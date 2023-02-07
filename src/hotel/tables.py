import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Country(Base):
    __tablename__ = "country"
    id = sa.Column(sa.Integer, primary_key=True)
    country_name = sa.Column(sa.String)
    hotels = relationship("Hotel")


class Hotel(Base):
    __tablename__ = "hotels"
    id = sa.Column(sa.Integer, primary_key=True)
    hotel_name = sa.Column(sa.String)
    description = sa.Column(sa.Text)
    country = sa.Column(sa.Integer, sa.ForeignKey("country.id"))
    price_for_day = sa.Column(sa.Numeric(10, 2))
    rate = sa.Column(sa.Integer)

