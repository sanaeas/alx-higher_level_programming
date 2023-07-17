#!/usr/bin/python3
"""Define the Base class"""
import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="UTF-8", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, "r", encoding="UTF-8", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        inst = cls(int(row[1]), int(row[2]), int(row[3]),
                                   int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        inst = cls(int(row[1]), int(row[2]), int(row[3]),
                                   int(row[0]))
                    instances.append(inst)
        except FileNotFoundError:
            return []
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draws all the Rectangles and Squares"""
        screen = turtle.Screen()
        screen.setup(800, 600)
        screen.bgcolor("black")

        pen = turtle.Turtle()
        pen.pensize(3)
        pen.shape("turtle")

        pen.color("red")
        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)

        pen.color("blue")
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)
            pen.forward(square.size)
            pen.left(90)

        turtle.done()
