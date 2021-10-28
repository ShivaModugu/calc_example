# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class Calculator:
    """ This is the Calculator class"""

    result = 0
    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result
    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result
    def multiply_numbers(self, value_a, value_b):
        """ multiply two numbers and get result"""
        self.result = value_a * value_b
        return self.result
    def divide_numbers(self, value_a, value_b):
        """ divide two numbers and get result"""
        try:
            self.result = value_a / value_b
        except ZeroDivisionError:
            print("A number cannot be divided by zero")
        return self.result
