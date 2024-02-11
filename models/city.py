#!/usr/bin/python3
"""city"""
from models.base_model import BaseModel


class City(BaseModel):
    """user city
    
    Attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    state_id = ""
    name = ""
