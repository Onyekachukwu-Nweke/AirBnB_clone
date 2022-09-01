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

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            self.id = kwargs["id"]
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])

    def __str__(self):
        """ Returns the string representation of the instance """

        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ This updates the time anytime a change is made """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns the dictionary representation of the instance """

        return_dict = self.__dict__.copy()
        return_dict["__class__"] = self.__class__.__name__
        return_dict["created_at"] = \
            self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return_dict["updated_at"] = \
            self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return return_dict
