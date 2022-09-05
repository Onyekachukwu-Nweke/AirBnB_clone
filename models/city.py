#!/usr/bin/python3
"""
    This module shows the city
"""
from models.base_model import BaseModel


class City(BaseModel):
    '''City class which inherits from BaseModel Class'''

    state_id = ''
    name = ''
