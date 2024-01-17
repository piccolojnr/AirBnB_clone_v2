#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
from os import getenv

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")


if HBNB_TYPE_STORAGE == "db":
    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False,
        ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False,
        ),
    )


class Place(BaseModel, Base):
    """A place to stay"""

    if HBNB_TYPE_STORAGE == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", back_populates="place")
        amenity_ids = []
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            back_populates="place_amenities",
            viewonly=False,
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter function for reviews attribute"""
            result = []
            temp = models.all_classes["Review"]
            for r in models.storage.all(temp).values():
                if r.place_id == self.id:
                    result.append(r)
            return result

        @property
        def amenities(self):
            """getter function for amenity attribute"""
            result = []
            temp = models.all_classes["Amenity"]
            for a in models.storage.all(temp).values():
                if a in self.amenity_ids:
                    result.append(a)
            return result

        @amenities.setter
        def amenities(self, obj):
            """setter for amenities class"""
            temp = models.all_classes["Amenity"]
            if isinstance(obj, models.storage.all(temp)):
                self.amenity_ids.append(obj.id)
