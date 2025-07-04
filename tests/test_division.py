import pytest
from calculator.division import divide

def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0

def test_divide_negative_numbers():
    assert divide(-9, -3) == 3.0

def test_divide_mixed_sign_numbers():
    assert divide(-12, 4) == -3.0
    assert divide(12, -4) == -3.0

def test_divide_by_one():
    assert divide(7, 1) == 7.0

def test_divide_result_as_float():
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        divide(10, 0)
