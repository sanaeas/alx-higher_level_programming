import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_with_diff_numof_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 2, 4)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r2.id, r3.id - 1)

        r4 = Rectangle(10, 2, 0, 0, 7)
        self.assertEqual(r4.id, 7)

    def test_getters(self):
        r = Rectangle(10, 8)
        self.assertIsNotNone(r.id)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_setters_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2, 3, 4)
        with self.assertRaises(TypeError):
            Rectangle(1, [2, 3], 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3.5, 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {"4": 4})

        with self.assertRaises(ValueError):
            Rectangle(0, 2, 3, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, 0, 3, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -2, 4)
        with self.assertRaises(ValueError):
            Rectangle(3, 1, 2, -4)

    def test_area(self):
        r1 = Rectangle(11, 2)
        self.assertEqual(r1.area(), 22)
        r2 = Rectangle(100009, 466531, 0, 0, 1000)
        self.assertEqual(r2.area(), 46657298779)

    def test_update(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 2)

        r.update(width=10, height=5, x=3, y=4)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 2)

    def test_to_dictionary(self):
        r = Rectangle(10, 5, 2, 3, 1)
        output_dict = {
            'id': 1,
            'width': 10,
            'height': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(r.to_dictionary(), output_dict)

    def test_str_repr(self):
        r = Rectangle(10, 5, 2, 3, 1)
        expected_str = "[Rectangle] (1) 2/3 - 10/5"
        self.assertEqual(str(r), expected_str)


if __name__ == '__main__':
    unittest.main()
