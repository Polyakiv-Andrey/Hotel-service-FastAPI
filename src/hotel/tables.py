import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Hotel(Base):
    __tablename__ = "hotels"
    id = sa.Column(sa.Integer, primary_key=True)
    hotel_name = sa.Column(sa.String)
    description = sa.Column(sa.Text)
    price_for_day = sa.Column(sa.Numeric(10, 2))
    rate = sa.Column(sa.Integer)

