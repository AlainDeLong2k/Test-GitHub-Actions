from src.math_operations import add, subtract, multiply, divide
from src import DIVIDE_ERROR
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(4, 3) == 1
    assert subtract(3, 3) == 0
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(1, 2) == 1 * 2
    assert multiply(2, 3) == 2 * 3
    assert multiply(4, 5) == 4 * 5


def test_divide():
    with pytest.raises(ValueError, match=DIVIDE_ERROR):
        divide(1, 0)
    with pytest.raises(ValueError, match=DIVIDE_ERROR):
        divide(10, 0)
    with pytest.raises(ValueError, match=DIVIDE_ERROR):
        divide(100, 0)

    assert divide(2, 1) == 2 / 1
    assert divide(3, 2) == 1.5
    assert divide(1, 3) == 1 / 3
