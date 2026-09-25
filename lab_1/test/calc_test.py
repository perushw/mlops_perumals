import pytest
from src import calculator as calc

def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-1, 1) == -2
    assert calc.subtract(0, 0) == 0

def test_multiply():
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(0, 0) == 0

def test_divide():
    assert calc.divide(6, 3) == 2
    assert calc.divide(-6, 3) == -2
    assert calc.divide(0, 1) == 0

    with pytest.raises(ValueError):
        calc.divide(1, 0)

def test_square_root():
    assert calc.square_root(4) == 2
    assert calc.square_root(0) == 0

    with pytest.raises(ValueError):
        calc.square_root(-4)
        