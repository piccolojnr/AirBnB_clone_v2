#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv
from models.place import place_amenity

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    if HBNB_TYPE_STORAGE == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary=place_amenity, back_populates="amenities"
        )
    else:
        name = ""
