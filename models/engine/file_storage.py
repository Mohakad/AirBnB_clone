#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes"""

import json
class FileStorage:
    """file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dict"""
        return FileStorage.__objects
    
    def new(self, obj):
        """ sets in __objects the obj with key"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__ , obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        data = FileStorage.__objects
        with open(FileStorage.__file_path, "w") as fil:
            json.dump(data, fil)
    
    def reload(self):
        """deserializ JSON file"""
        with open(FileStorage.__file_path) as jfile:
            data = json.load(jfile)
            for jd in data.values():
                cname = jd["__class__"]
                del jd["__class__"]
                self.new(eval(cname)(**jd))
