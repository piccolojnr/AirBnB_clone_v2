#!/usr/bin/python3
"""test for console to make it start working"""
import unittest
from io import StringIO
from console import HBNBCommand
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """ """

    def test_exists(self):
        """ """
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    @classmethod
    def get_S(cls):
        """ """
        temp_out = StringIO()
        sys.stdout = temp_out
        return temp_out.getvalue()

    def test_create_error(self):
        """ """
        temp_out = StringIO()
        sys.stdout = temp_out

        HBNBCommand().do_create(None)
        self.assertEqual(temp_out.getvalue(), "** class name missing **\n")
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        HBNBCommand().do_create("base")
        self.assertEqual(temp_out.getvalue(), "** class doesn't exist **\n")
        temp_out.close()

        temp_out = StringIO()
        sys.stdout = temp_out
        HBNBCommand().do_create("BaseModel")
        self.assertEqual(temp_out.getvalue(), "** class doesn't exist **\n")
        temp_out.close()
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
