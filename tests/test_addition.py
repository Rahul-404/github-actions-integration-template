import pytest
from calculator.addition import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -4) == -5

def test_add_mixed_sign_numbers():
    assert add(-3, 7) == 4

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0
