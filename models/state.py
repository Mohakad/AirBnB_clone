#!/usr/bin/python3
"""inherit from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """user state
    Attributes:
    (str) name: state name
    """

    name = ""
