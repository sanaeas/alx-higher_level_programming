#!/usr/bin/python3
"""Define the Base class"""
import json


class Base:
    """the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if not list_objs:
                f.write("[]")
                return
            a_list = []
            for obj in list_objs:
                a_list.append(obj.to_dictionary())
            f.write(cls.to_json_string(a_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        inst = cls(1, 1, 1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = f.read()
                instance_list = cls.from_json_string(data)
                instances = []
                for instance_dict in instance_list:
                    instance = cls.create(**instance_dict)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
