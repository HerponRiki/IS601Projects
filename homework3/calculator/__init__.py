from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(_a,_b):
        calculation = Calculation(_a, _b, add)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def subtract(_a,_b):
        calculation = Calculation(_a, _b, subtract)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def multiply (_a,_b):
        calculation = Calculation(_a, _b, multiply)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def divide(_a,_b):
        calculation = Calculation(_a, _b, divide)  # Pass the add function from calculator.operations
        return calculation.get_result()