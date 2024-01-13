#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    @classmethod
    def setUpClass(cls):
        """setup class"""
        cls.value = BaseModel()
        cls.name = "BaseModel"

    @classmethod
    def tearDownClass(cls):
        """tear down"""
        del cls.value
        try:
            os.remove("file.json")
        except:
            pass


    def test_kwargs(self):
        """ """
        i = self.value
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)


    def test_str(self):
        """ """
        i = self.value
        self.assertEqual(str(i), "[{}] ({}) {}".format(self.name, i.id, i.__dict__))

    def test_todict(self):
        """ """
        i = self.value
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
        
        self.assertTrue("__class__" in n)
        self.assertIsInstance(n["__class__"], str)
        self.assertTrue("id" in n)
        self.assertIsInstance(n["id"], str)
        self.assertTrue("created_at" in n)
        self.assertIsInstance(n["created_at"], str)
        self.assertTrue("updated_at" in n)
        self.assertIsInstance(n["updated_at"], str)
        i.test = 10
        n = i.to_dict()
        self.assertTrue("test" in n)
    
    def test_fromdict(self):
        """
            test instance retrival from a dictionary
        """
        new = self.value
        new.test = 10
        test_instance = BaseModel(**new.to_dict())
        self.assertTrue("__class__" not in test_instance.__dict__)
        self.assertTrue(hasattr(test_instance, "id"))
        self.assertTrue(hasattr(test_instance, "created_at"))
        self.assertTrue(hasattr(test_instance, "updated_at"))
        self.assertTrue(hasattr(test_instance, "test"))
        self.assertIsInstance(test_instance.created_at, datetime.datetime)
        self.assertIsInstance(test_instance.updated_at, datetime.datetime)
        self.assertEqual(test_instance.created_at, new.created_at)
        self.assertEqual(test_instance.updated_at, new.updated_at)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value
        self.assertIsInstance(new, BaseModel)
        self.assertIsInstance(new.id, str)
        self.assertEqual(type(new.id), str)
    
    def test_unique_id(self):
        """        """
        val_1 = BaseModel()
        val_2 = BaseModel()
        self.assertNotEqual(val_1.id, val_2.id)
        del val_1
        del val_2

    def test_created_at(self):
        """ """
        new = self.value
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == "__main__":
    unittest.main()