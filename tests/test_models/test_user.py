#!/usr/bin/python3
""" """
import unittest
from models.user import User


class test_User(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.value = User()
        cls.value.email = "tests@test.com"
        cls.value.password = "pass"
        cls.value.first_name = "john"
        cls.value.last_name = "doe"

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.value

    def test_first_name(self):
        """ """
        new = self.value
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value
        self.assertEqual(type(new.password), str)
        
if __name__ == "__main__":
    unittest.main()
