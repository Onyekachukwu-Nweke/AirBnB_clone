#!/usr/bin/python3
"""
    This file creates a base class upon other classes will be built
    will be built upon
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
        This class is the base class that defines what all other
        classes will use
    """

    def __init__(self, *args, **kwargs):
        """ Initializes the instance """
        if kwargs:
            for key, arg in kwargs.items():
                if key != '__class__':
                    setattr(self, key, arg)
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns the string representation of the instance """
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))

    def save(self):
        """
        This updates the time anytime a change is made
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns the dictionary representation of the instance """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
