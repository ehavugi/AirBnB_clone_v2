#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def delete(self, obj=None):
        """Delete obj from __objectss if it is inside.
        if obj is None, do nothing.
        """
        if obj:
            del_key = obj.__class__.__name__ + "." + obj.id
            if (FileStorage.__objects.get(del_key, None)):
                del FileStorage.__objects[del_key]

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if (cls):
            clsName = cls.__name__
            objx = {}
            for key, value in self.__objects.items():
                if key.split(".")[0] == clsName:
                    objx[key] = value
            return objx
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        self.save()

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                value = val.to_dict()
                if '_sa_instance_state' in value.keys():
                    del value['_sa_instance_state']
                temp[key] = value
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """call reload method for deserializing file JSON to objects"""
        self.reload()
