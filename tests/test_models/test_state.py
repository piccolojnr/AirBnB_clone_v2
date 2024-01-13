#!/usr/bin/python3
""" """
from models.state import State
import unittest

class test_state(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.value = State()
        cls.value.name = "tests"

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.value

    def test_name3(self):
        """ """
        new = self.value
        self.assertEqual(type(new.name), str)


if __name__ =="__main__":
    unittest.main()