import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for Square class"""
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_with_diff_numof_args(self):
        s1 = Square(1)
        s2 = Square(10, 2)
        s3 = Square(2, 2, 4)
        self.assertEqual(s1.id, s2.id - 1)
        self.assertEqual(s2.id, s3.id - 1)

        s4 = Square(10, 2, 0, 7)
        self.assertEqual(s4.id, 7)

    def test_getters(self):
        s = Square(10)
        self.assertIsNotNone(s.id)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_size_property(self):
        sq = Square(5)
        self.assertEqual(sq.size, 5)
        sq.size = 10
        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 10)

        with self.assertRaises(TypeError):
            sq.size = "invalid"
        with self.assertRaises(ValueError):
            sq.size = 0

    def test_setters_validation(self):
        with self.assertRaises(TypeError):
            Square("1", 2, 3)
        with self.assertRaises(TypeError):
            Square(1, [2, 3], 4)
        with self.assertRaises(TypeError):
            Square(1, 2, 3.5)

        with self.assertRaises(ValueError):
            Square(0, 2, 3)
        with self.assertRaises(ValueError):
            Square(1, 1, -2)
        with self.assertRaises(ValueError):
            Square(3, 2, -4)

    def test_area(self):
        s = Square(11)
        self.assertEqual(s.area(), 121)

    def test_update(self):
        sq = Square(1, 1, 1, 1)
        sq.update(2, 2, 2, 2)
        self.assertEqual(sq.width, 2)
        self.assertEqual(sq.height, 2)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 2)
        self.assertEqual(sq.id, 2)

        sq.update(size=10, x=3, y=4)
        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 10)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 4)
        self.assertEqual(sq.id, 2)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        output_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(s.to_dictionary(), output_dict)

    def test_str_repr(self):
        s = Square(5, 2, 3, 1)
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(s), expected_str)


if __name__ == '__main__':
    unittest.main()
