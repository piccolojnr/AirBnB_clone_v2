#!/usr/bin/python3
"""DBStorage"""
import os
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from sqlalchemy.orm import sessionmaker, scoped_session
import models


HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST")
HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")


class DBStorage:
    """DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """DBStorage"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB,
            )
        )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all"""
        res = {}
        if cls:
            rows = self.__session.query(cls).all()
            for row in rows:
                key = cls.__name__ + "." + row.id
                res[key] = row.to_dict()  # Serialize the object to a dictionary
        else:
            for clss in models.all_tables.values():
                rows = self.__session.query(clss).all()
                for row in rows:
                    key = clss.__name__ + "." + row.id
                    res[key] = row.to_dict()  # Serialize the object to a dictionary
        return res

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scope = scoped_session(session_factory)
        self.__session = Scope()

    def close(self):
        """display our HBNB data"""
        self.__session.__class__.close(self.__session)
        self.reload()
