#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """BaseModel that defines all common attributes/methods for other classes"""
    def __init__(self):
        """initialization"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of dict"""
        DicFormat = {}
        DicFormat["__class__"] = self.__class__.__name__

        for key, cont in self.__dict__.items():
             """convert to string"""
             if isinstance(cont, datetime):
                 DicFormat[key] = cont.isoformat()
             else:
                 DicFormat[key] =  cont
        return DicFormat
