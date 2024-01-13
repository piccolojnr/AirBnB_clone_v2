#!/usr/bin/python3
""" """
from models.amenity import Amenity
import unittest


class test_Amenity(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.value = Amenity()
        cls.value.name = "test"

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.value


    def test_name2(self):
        """ """
        new = self.value
        self.assertEqual(type(new.name), str)
        
if __name__ == "__main__":
    unittest.main()
