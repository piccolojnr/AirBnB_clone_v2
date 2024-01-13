#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """State class"""

    if HBNB_TYPE_STORAGE == "db":
        __tablename__ = "states"
        
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """
            Returns the list of City instances with
            state_id equals to the current State.id
            """
            from models import storage
            from models.city import City

            cities = storage.all(City)
            list_cities = []
            for city in cities.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
