#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes"""
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON 
    file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obfile = FileStorage.__objects
        obdict = {obj: obfile[obj].to_dict() for obj in obfile.keys()}
        with open(FileStorage.__file_path, "w") as savef:
            json.dump(obdict, savef)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists"""
        try:
            with open(FileStorage.__file_path) as jfl:
                jdict = json.load(jfl)
                for data in jdict.values():
                    cname = data["__class__"]
                    del data["__class__"]
                    self.new(eval(cname)(**data))
        except:
            return

    __classes = {
        'BaseModel': BaseModel,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        # Add other classes as needed
    }
