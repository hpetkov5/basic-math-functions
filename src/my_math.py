'''
This module contains the MyMath class, which provides basic mathematical operations.
'''


class MyMath:
    '''
    This class contains 4 functions (addition, subtraction, multiplication, division).
    '''

    @staticmethod
    def addition(num1: int, num2: int) -> int:
        '''
        This function takes 2 integers and adds them together.
        :param num1: The first integer to be added.
        :param num2: The second integer to be added.
        :return: The sum of num1 and num2.
        '''
        return num1 + num2

    @staticmethod
    def subtraction(num1: int, num2: int) -> int:
        '''
        This function takes the 2 integers and subtracts num2 from num1.
        :param num1: The first integer to be subtracted from.
        :param num2: The second integer to be subtracted.
        :return: The difference of num1 and num2.
        '''
        return num1 - num2

    @staticmethod
    def multiplication(num1: int, num2: int) -> int:
        '''
        This function multiplies the 2 integers.
        :param num1: The first integer to be multiplied.
        :param num2: The second integer to be multiplied.
        :return: The product of num1 and num2.
        '''
        return num1 * num2

    @staticmethod
    def division(num1: int, num2: int) -> float:
        '''
        This function divides num1 by num2.
        :param num1: The first integer to be divided.
        :param num2: The second integer to be divided by.
        :return: The quotient of num1 and num2.
        '''
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
