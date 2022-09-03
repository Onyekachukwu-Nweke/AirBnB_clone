#!/usr/bin/python3

import email
from base_model import BaseModel
from models import storage

class User(BaseModel):
    '''User class that inherits from base model'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
    
    def __init__(self, *args, **kwargs):
        '''Instantiation Method'''
        super().__init__(*args, **kwargs)
                                                
