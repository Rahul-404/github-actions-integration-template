from __future__ import annotations

def divide(a: int, b: int) -> float:
    """
    Divide two integers and return the result.

    :param a: The numerator.
    :param b: The denominator.
    :return: The result of the division as a float.
    :raises ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b