#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Defines the blueprint of saving and retrieving objects.

    Attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Sets an object in the __objects dictionary with a key of <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def all(self, cls=None):
        """Returns the list of objects of one type of class."""
        if cls is None:
            return list(FileStorage.__objects.values())
        else:
            return [obj for obj in FileStorage.__objects.values() if isinstance(obj, cls)]

    def save(self):
        """Serializes the __objects dictionary into JSON format and saves it to the file specified by __file_path."""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file."""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside."""
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]

