#!/usr/bin/python3

import email
from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    '''User class that inherits from base model'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''                                     
