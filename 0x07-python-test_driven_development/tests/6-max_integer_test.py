#!/usr/bin/python3
"""Unittest for max_integer function"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases"""
    def test_default(self):
        """Regular list with positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10]), 10)

    def test_no_list(self):
        """Calling the function without providing a list"""
        self.assertIsNone(max_integer())

    def test_empty(self):
        """Empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative(self):
        """List with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -7]), -1)

    def test_mixed(self):
        """List with a mix of positive and negative integers"""
        self.assertEqual(max_integer([1, -5, 0, -10]), 1)

    def test_float(self):
        """List with float numbers"""
        self.assertEqual(max_integer([2, 4.5, 4.2, 5.8]), 5.8)

    def test_str(self):
        """List with a string value"""
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])

    def test_nolist(self):
        """Using an int instead of a list"""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == '__main__':
    unittest.main()
