# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
"""
class Calculator:
     #This is the Calculator class

    result = 0
    def get_result(self):
     #Get Result of Calculation
        return self.result

    def add_number(self, value_a):
      #adds number to result
        self.result = self.result + value_a
        return self.result
    def subtract_number(self, value_a):
       #subtract number from result
        self.result = self.result - value_a
        return self.result
    def multiply_numbers(self, value_a, value_b):
        #multiply two numbers and get result
        self.result = value_a * value_b
        return self.result
    def divide_numbers(self, value_a, value_b):
         divide two numbers and get result
        try:
            self.result = value_a / value_b
        except ZeroDivisionError:
            print("A number cannot be divided by zero")
        return self.result
"""
""" This is the increment function"""
from calculator.history.calcualtions import Calculations

#the calculator class just contains the methods to calculate
class Calculator:
    """ This is the Calculator class"""
    #the calculator class just calls methods on Calculations class
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()
    @staticmethod
    #tuple allows me to pass in as many values as a I want
    def add_numbers(tuple_values: tuple):
        """ adds list of numbers"""
        Calculations.add_addition_calculation(tuple_values)
        return True
    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True
    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiplication number from result"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True
