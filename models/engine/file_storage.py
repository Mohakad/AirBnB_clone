#!/usr/bin/python3
"""serializes and deserializes"""
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances and deserializes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets with key id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obfile = FileStorage.__objects
        obdict = {obj: obfile[obj].to_dict() for obj in obfile.keys()}
        with open(FileStorage.__file_path, "w") as savef:
            json.dump(obdict, savef)

    def reload(self):
        """deserialize JSON file"""
        try:
            with open(FileStorage.__file_path) as jfl:
                jdict = json.load(jfl)
                for data in jdict.values():
                    cname = data["__class__"]
                    del data["__class__"]
                    self.new(eval(cname)(**data))
        except OSError:
            pass
