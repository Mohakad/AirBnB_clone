#!/usr/bin/python3
"""create a unique FileStorage instance"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

storage = FileStorage()
storage.reload()
