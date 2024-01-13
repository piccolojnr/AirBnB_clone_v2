#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

all_classes = {
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
    "User": User,
    "BaseModel": BaseModel,
}
all_tables = {
    "states": State,
    "cities": City,
}

HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")


storage = None

if HBNB_TYPE_STORAGE == "db":
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
