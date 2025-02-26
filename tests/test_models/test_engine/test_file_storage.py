#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.dummy = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy

    def test_attrs(self):
        """
            attribute tests
        """
        self.assertTrue(hasattr(self.dummy, "_FileStorage__objects"))
        self.assertTrue(isinstance(self.dummy._FileStorage__objects, dict))
        self.assertTrue(hasattr(self.dummy, "_FileStorage__file_path"))
        self.assertTrue(isinstance(self.dummy._FileStorage__file_path, str))

    
        
        
if __name__ == "__main__":
    unittest.main()