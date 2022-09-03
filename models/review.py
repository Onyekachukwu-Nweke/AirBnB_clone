#!/usr/bin/python3
from base_model import BaseModel


class Review(BaseModel):
    '''Review class which inherits from BaseModel Class'''

    place_id = ''
    user_id = ''
    text = ''
