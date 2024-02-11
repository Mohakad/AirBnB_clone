#!/usr/bin/python3
"""unittest for base_model.py"""
import unittest
import models
from models.base_model import BaseModel
import os
from datetime import datetime


class test_init(unittest.TestCase):
    """test initializatio BaseModel"""
    def test_new_obj(self):
        self.assertIn(BaseModel(), models.storage.all().values())
    def test_id_uniq(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1, id2)
    def test_id_publ(self):
        self.assertEqual(str, type(BaseModel().id))
    def test_str(self):
        dtt = datetime.now()
        dtr = repr(dtt)
        bsm = BaseModel()
        bsm.id = "111111"
        bsm.created_at = bsm.updated_at = dtt
        bmstr = bsm.__str__()
        self.assertIn("[BaseModel] (111111)", bmstr)
        self.assertIn("'id': '111111'", bmstr)
        self.assertIn("'created_at': " + dtr, bmstr)
        self.assertIn("'updated_at': " + dtr, bmstr)
if __name__ == "__main__":
    unittest.main()