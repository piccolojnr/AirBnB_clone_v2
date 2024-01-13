#!/usr/bin/python3
""" """
from models.city import City
from models.state import State
import unittest


class test_City(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.value = City()
        cls.value.name = "test"
        cls.value.state_id = State().id

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.value


    def test_state_id(self):
        """ """
        new = self.value
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()