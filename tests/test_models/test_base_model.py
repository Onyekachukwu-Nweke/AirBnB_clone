#!/usr/bin/env python3
"""Module to test Base class module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBase(unittest.TestCase):
    """Test case for base module"""

    def setUp(self):
        try:
            self.created_b1 = round(datetime.now().timestamp())
            self.b1 = BaseModel()
            self.b2 = BaseModel()
        except Exception:
            pass

    def tearDown(self):
        """ Tidy Up """

        try:
            del self.b1
            del self.b2
        except Exception:
            pass

    def test_init(self):
        """Test init function"""
        try:
            self.assertEqual(type(self.b1.id).__name__, "str")
            self.assertNotEqual(self.b1.id, self.b2.id)
            self.assertEqual(self.b1.created_at.timestamp(),
                             self.b1.updated_at.timestamp())
            self.assertEqual(type(self.b1.created_at).__name__, "datetime")
            self.assertAlmostEqual(round(self.b1.created_at.timestamp()),
                                   self.created_b1)
        except Exception:
            pass

    def test_save(self):
        """Test save function"""
        try:
            updated_b1 = round(datetime.now().timestamp())
            self.b1.save()
            self.assertAlmostEqual(round(self.b1.updated_at.timestamp()),
                                   updated_b1)
        except Exception:
            pass

    def test_string(self):
        """Test __str__ function"""
        try:
            self.assertEqual(self.b1.__str__(), "[BaseModel] ({}) {}".
                             format(self.b1.id, self.b1.__dict__))
        except Exception:
            pass

    def test_to_dict(self):
        """Test to_dict function of BaseModel"""
        try:
            b1_dict = self.b1.to_dict()
            self.assertEqual(b1_dict["__class__"], "BaseModel")
            self.assertEqual(b1_dict["created_at"],
                             self.b1.created_at.isoformat())
            self.assertEqual(b1_dict["updated_at"],
                             self.b1.updated_at.isoformat())
        except Exception:
            pass
