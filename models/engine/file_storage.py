#!/usr/bin/python3

"""
    This module contains the file storage mechanism of
    the AirBnB clone
"""
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
        This class Serializes class instances to JSON
        file and deserializes the JSON file to instances

        Arg(s):
            __file_path - JSON file
            __objects - instances to be added to JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key
            <obj class name>.id
        """
        FileStorage.__objects["{}.{}".
                              format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
            Serializes __objects to the JSON file
            (path: __file_path)
        """
        try:
            my_obj = {}

            for key, value in FileStorage.__objects.items():
                my_obj[key] = value.to_dict()

            with open(FileStorage.__file_path, 'w') as f:
                json.dump(my_obj, f)
        except TypeError:
            pass

    def reload(self):
        """
            Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = value
        except Exception:
            pass
