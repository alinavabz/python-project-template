import pytest

from src.calculator import add, divide, multiply, subtract


def test_add():
    result = add(2, 5)
    assert result == 7
    result = add(7.1, 3.9)
    assert result == 11.0


def test_subtract():
    result = subtract(10, 7)
    assert result == 3
    result = subtract(98765, 2190)
    assert result > 50000
    result = subtract(3.5, 1.2)
    assert result == 2.3


def test_multiply():
    result = multiply(3, 4)
    assert result == 12
    result = multiply(2.5, 4)
    assert result == 10.0
    result = multiply(-2, 6)
    assert result == -12


def test_divide():
    result = divide(8, 2)
    assert result == 4
    result = divide(7.5, 2.5)
    assert result == 3.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
