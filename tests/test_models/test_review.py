#!/usr/bin/python3
""" """
import unittest
from models.review import Review
from models.place import Place
from models.user import User


class test_review(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.value = Review()
        cls.value.text = "test"
        cls.value.user_id = User().id
        cls.value.place_id = Place().id

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.value

    def test_place_id(self):
        """ """
        new = self.value
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value
        self.assertEqual(type(new.text), str)

if __name__ == "__main__":
    unittest.main()