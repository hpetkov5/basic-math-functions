'''
Unit tests for MyMath class.

This module uses Python's unittest framework to validate the correctness of MyMath's functions.

'''

import unittest
from src.my_math import MyMath


class TestAddition(unittest.TestCase):

    def test_adding_two_positive_integers(self):
        expected_result = 4
        actual_result = MyMath.addition(2, 2)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")

    def test_adding_two_negative_integers(self):
        expected_result = -20
        actual_result = MyMath.addition(-5, -15)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")

    def test_adding_positive_and_negative_integer(self):
        expected_result = 10
        actual_result = MyMath.addition(15, -5)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")

class TestSubtraction(unittest.TestCase):

    def test_subtracting_two_positive_integers(self):
        expected_result = 10
        actual_result = MyMath.subtraction(15, 5)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")

    def test_subtracting_two_negative_integers(self):
        expected_result = 10
        actual_result = MyMath.subtraction(-5, -15)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")

    def test_subtracting_one_positive_and_one_negative_integer(self):
        expected_result = 20
        actual_result = MyMath.subtraction(15, -5)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")

    def test_subtracting_one_negative_and_one_positive_integer(self):
        expected_result = -20
        actual_result = MyMath.subtraction(-15, 5)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")


class TestMultiplication(unittest.TestCase):

    def test_multiplying_two_positive_integers(self):
        expected_result = 75
        actual_result = MyMath.multiplication(5, 15)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")

    def test_multiplying_two_negative_integers(self):
        expected_result = 75
        actual_result = MyMath.multiplication(-5, -15)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")

    def test_multiplying_one_positive_and_one_negative_integer(self):
        expected_result = -75
        actual_result = MyMath.multiplication(5, -15)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")


class TestDivision(unittest.TestCase):

    def test_dividing_two_positive_integers(self):
        expected_result = 3
        actual_result = MyMath.division(15, 5)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")

    def test_dividing_two_negative_integers(self):
        expected_result = 3
        actual_result = MyMath.division(-15, -5)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")

    def test_dividing_one_positive_and_one_negative_integer(self):
        expected_result = -3
        actual_result = MyMath.division(15, -5)
        self.assertEqual(expected_result, actual_result, f"Expected {expected_result}, received {actual_result}.")


if __name__ == '__main__':
    unittest.main()
