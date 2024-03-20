#!/usr/bin/python3

import json
import os  # Add this line to import the os module
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    FileStorage class for storing, serializing, deserializing, and deleting data
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Sets an object in the __objects dictionary with a key of
        <obj class name>.id.
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self, cls=None):
        """
        Returns a dictionary of objects of one type of class if cls is specified,
        with keys representing object IDs. If cls is None, it provides access
        to all the stored objects.
        """
        if cls is None:
            return FileStorage.__objects.copy()
        else:
            return {key: obj for key, obj in FileStorage.__objects.items() if isinstance(obj, cls)}

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it exists.
        If obj is equal to None, the method does nothing.
        """
        if obj is None:
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]

    def save(self):
        """
        Serializes the __objects dictionary into JSON format
        and saves it to the file specified by __file_path.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            obj_dict = {}
            for obj in FileStorage.__objects.values():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj.to_dict()
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file and reloads objects into memory.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = globals().get(class_name)
                        if cls:
                            instance = cls(**value)
                            FileStorage.__objects[key] = instance
                        else:
                            raise ValueError(f"Class {class_name} not found")
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                except ValueError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

