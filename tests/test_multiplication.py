import pytest
from calculator.multiplication import multiply

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12

def test_multiply_negative_numbers():
    assert multiply(-2, -5) == 10

def test_multiply_mixed_sign_numbers():
    assert multiply(-3, 6) == -18
    assert multiply(3, -6) == -18

def test_multiply_with_zero():
    assert multiply(0, 5) == 0
    assert multiply(7, 0) == 0
    assert multiply(0, 0) == 0

def test_multiply_with_one():
    assert multiply(1, 9) == 9
    assert multiply(9, 1) == 9
