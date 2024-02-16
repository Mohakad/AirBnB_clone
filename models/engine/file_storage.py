#!/usr/bin/python3
"""serializes and deserializes"""
import json
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.user import User


class FileStorage:
    """serializes instances and deserializes"""
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                  "Amenity": Amenity, "Place": Place, "City": City,
                  "Review": Review}

    def all(self):
        """return the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets with key id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        my_dic = {}
        for key, obj in self.__objects.items():
            my_dic[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(my_dic, f)

    def reload(self):
        """deserialize JSON file"""
        try:
            with open(self.__file_path, "r") as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
