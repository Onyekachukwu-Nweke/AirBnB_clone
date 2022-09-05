#!/usr/bin/python3
"""
Shows the user details
"""
import email
from models.base_model import BaseModel
from models.__init__ import storage


class User(BaseModel):
    '''User class that inherits from base model'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
