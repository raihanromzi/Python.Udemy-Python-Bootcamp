"""
A Very simple script
Testing Code using Pylint
Error check using pylint : pylint [filename.py] - r y
Error check using Unittest
"""
# Unittest Library

import unittest
import test_cap

# def my_function():
#     """
#     A simple function
#     :return: First and second
#     """
#     first = 1
#     second = 2

#     print(first)
#     print(second)


# my_function()

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        # memanggil fungsi yang ada di file cap di fungsi TestCap
        result = test_cap.cap_text(text)
        # Check if hasilnya sama dengan 'Python' apabila masuk ke fungsi yang ada di TestCap()
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = test_cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')


# Hanya bisa dijalankan di file ini
if __name__ == '__main__':
    unittest.main()
