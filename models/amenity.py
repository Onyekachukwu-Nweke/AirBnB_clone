#!/usr/bin/python3
"""
This shows the resources of the place
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' Amenity class which inherits from BaseModel class '''
    name = ''
