#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from os import getenv

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if (HBNB_TYPE_STORAGE == 'db'):
        __tablename__ = "users"
        email  = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
