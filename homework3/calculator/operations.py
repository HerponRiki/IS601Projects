from decimal import Decimal
# Define the functions with type hints
def add(_a: Decimal, _b: Decimal) -> Decimal:
    return _a + _b

def subtract(_a: Decimal, _b: Decimal) -> Decimal:
    return _a - _b

def multiply(_a: Decimal, _b: Decimal) -> Decimal:
    return _a * _b

def divide(_a: Decimal, _b: Decimal) -> Decimal:
    if _b == 0:
        raise ValueError("Cannot divide by zero")
    return _a / _b