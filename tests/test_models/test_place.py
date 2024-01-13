#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.user import User

import unittest

class test_Place(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.value = Place()
        cls.value.city_id = City().id
        cls.value.user_id = User().id
        cls.value.name = "test"
        cls.value.description = "testing"
        cls.value.number_rooms = 1
        cls.value.number_bathrooms = 1
        cls.value.max_guest = 1
        cls.value.price_by_night = 1
        cls.value.latitude = 1.0
        cls.value.longitude = 1.0
        cls.value.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.value

    def test_city_id(self):
        """ """
        new = self.value
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()