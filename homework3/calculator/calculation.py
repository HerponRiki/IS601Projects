class Calculation:
    def __init__(self, _a, _b, operation):
        self._a = _a
        self._b = _b
        self.operation = operation  # Store the operation function

    def get_result(self):
        # Call the stored operation with a and b
        return self.operation(self._a, self._b)