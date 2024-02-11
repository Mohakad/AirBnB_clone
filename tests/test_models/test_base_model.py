#!/usr/bin/python3
"""unittest for base_model.py"""
import unittest
import models
from models.base_model import BaseModel
import os
from datetime import datetime


class Test_init(unittest.TestCase):
    def test_new_obj(self):
        self.assertIn(BaseModel(), models.storage.all().values())
    def test_id_uniq(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1, id2)

if __name__ == "__main__":
    unittest.main()