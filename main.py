def calculate_remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    return dividend % divisor