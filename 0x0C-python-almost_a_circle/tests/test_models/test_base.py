import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittests for testing the Base class."""

    def tearDown(self):
        filenames = ["Base.json", "Base.csv"]
        for filename in filenames:
            if os.path.exists(filename):
                os.remove(filename)

    def test_init(self):
        b1 = Base()
        b2 = Base(15)
        b3 = Base(None)
        self.assertEqual(b1.id, b3.id - 1)
        self.assertEqual(b2.id, 15)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_public_id(self):
        b = Base(10)
        b.id = 15
        self.assertEqual(b.id, 15)

    def test_private_nb_instances(self):
        b = Base(12)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"x": 1, "y": 2}]),
                         '[{"x": 1, "y": 2}]')

        r1 = Rectangle(4, 5, 5, 19, 10)
        r2 = Rectangle(6, 3, 4, 1, 11)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        json_str = '[{"id": 10, "width": 4, "height": 5, "x": 5, "y": 19}, \
{"id": 11, "width": 6, "height": 3, "x": 4, "y": 1}]'
        self.assertEqual(Base.to_json_string(list_dicts), json_str)

        s1 = Square(5, 6, 4, 3)
        s2 = Square(6, 4, 20, 4)
        list_dicts2 = [s1.to_dictionary(), s2.to_dictionary()]
        json_str2 = '[{"id": 3, "size": 5, "x": 6, "y": 4}, \
{"id": 4, "size": 6, "x": 4, "y": 20}]'
        self.assertEqual(Base.to_json_string(list_dicts2), json_str2)

    def test_to_json_string_wrong_numof_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"x": 1, "y": 2}]'),
                         [{"x": 1, "y": 2}])
        with self.assertRaises(TypeError):
            Base.from_json_string()
        with self.assertRaises(TypeError):
            Base.from_json_string([], 3)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 19)
        r2 = Rectangle(2, 4, 0, 0, 20)
        Rectangle.save_to_file([r1, r2])
        json_str = '[{"id": 19, "width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 20, "width": 2, "height": 4, "x": 0, "y": 0}]'
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertEqual(content, json_str)

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_wrong_numof_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_load_from_file_no_file(self):
        output = Base.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        loaded_list = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(loaded_list[0]))

        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        loaded_squares = Square.load_from_file()
        self.assertEqual(str(s2), str(loaded_squares[1]))

    def test_load_from_file_with_args(self):
        with self.assertRaises(TypeError):
            Square.load_from_file([])

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

        a_dict = {'size': 5, 'id': 33, 'x': 2, 'y': 4}
        s = Square.create(**a_dict)
        self.assertEqual("[Square] (33) 2/4 - 5", str(s))

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv(self):
        rect1 = Rectangle(1, 2, 1, 2, 6)
        rect2 = Rectangle(3, 4, 0, 0, 7)
        obj_list = [rect1, rect2]
        Rectangle.save_to_file_csv(obj_list)
        with open("Rectangle.csv", "r") as f:
            content = f.read()
            expected_content = "6,1,2,1,2\n7,3,4,0,0\n"
            self.assertEqual(content, expected_content)

        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_wrong_numof_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

    def test_load_from_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_no_file(self):
        output = Base.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_wrong_numof_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == '__main__':
    unittest.main()
