#!/usr/bin/python3
""" initialization, serialization and deserialization of your future instances"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ initialization, serialization and deserialization"""

    def __init__(self, *args, **kwargs):
        """initialize

        Args:
            *args : Unused.
            **kwargs : argument
        """
        
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) == 0:
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = v

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        dformat = {}
        dformat["__class__"] = self.__class__.__name__
        for key, cont in self.__dict__.items():
            if isinstance(cont, datetime):
                dformat[key] = cont.isoformat()
            else:
                dformat[key] = cont
        return dformat

    def __str__(self):
        """dictionery representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
