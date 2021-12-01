"""
A Very simple script
Testing Code using Pylint
Error check using pylint : pylint [filename.py] - r y
Error check using Unittest
"""
# Unittest Library

import unittest
import cap


def my_function():
    """
    A simple function
    :return: First and second
    """
    first = 1
    second = 2

    print(first)
    print(second)


my_function()


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.TestCap(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.TestCap(text)
        self.assertEqual(result, 'Monty Python')


if __name__ == '__main__':
    unittest.main()


