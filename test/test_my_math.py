'''
Unit tests for MyMath class.

This module uses Python's unittest framework to validate the correctness of MyMath's functions.

'''

import unittest
from src.my_math import MyMath

class TestAddition(unittest.TestCase):
    '''
    Unit test class for validating the behavior of addition function
    '''
    def test_adding_integers(self):
        '''
        Verify the addition function returns 20 when provided with 2 valid positive integers (a = 5, b = 15).
        '''
        test_object = MyMath()
        result = test_object.addition(5,15)
        assert result == 20, "Expected 20, received {0}.".format(result)

    def test_adding_floats(self):
        '''
        Verify the addition function returns 15.2 when provided with 2 valid positive floats (a = 6.3, b = 8.9).
        '''
        test_object = MyMath()
        result = test_object.addition(6.3, 8.9)
        assert result == 15.2, "Expected 15.2, received {0}.".format(result)

    def test_adding_strings(self):
        '''
        Verify the addition function returns "Hello World" when provided with 2 valid strings (a = "Hello ", b = "World").
        '''
        test_object = MyMath()
        result = test_object.addition("Hello ", "World")
        assert result == "Hello World", "Expected 'Hello World', received {0}.".format(result)

    def test_adding_lists(self):
        '''
        Verify the addition function returns [1, 2, 3, 4, 5] when provided with 2 valid lists (a = [1, 2], b = [3, 4, 5]).
        '''
        test_object = MyMath()
        result = test_object.addition([1, 2], [3, 4, 5])
        assert result == [1, 2, 3, 4, 5], "Expected [1, 2, 3, 4, 5], received {0}.".format(result)
    
    def test_adding_boolean(self):
        '''
        Verify the addition function returns 2 when provided with 2 valid booleans (a = True, b = True).
        '''
        test_object = MyMath()
        result = test_object.addition(True, True)
        assert result == 2, "Expected 2, received {0}.".format(result)



if __name__ == '__main__':
    unittest.main()
