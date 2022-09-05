#!/usr/bin/python3
"""
This shows past reviews of the apartment
"""
from models.base_model import BaseModel


class Review(BaseModel):
    '''Review class which inherits from BaseModel Class'''

    place_id = ''
    user_id = ''
    text = ''
