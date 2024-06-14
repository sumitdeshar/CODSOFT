import pytest
import math
from calculator import calculator

def test_addition():
    assert calculator('+', 5, 3) == "5 + 3 = 8"
    assert calculator('+', -5, 3) == "-5 + 3 = -2"

def test_subtraction():
    assert calculator('-', 5, 3) == "5 - 3 = 2"
    assert calculator('-', 5, -3) == "5 - -3 = 8"

def test_multiplication():
    assert calculator('*', 5, 3) == "5 * 3 = 15"
    assert calculator('*', 5, 0) == "5 * 0 = 0"

def test_division():
    assert calculator('/', 6, 3) == "6 / 3 = 2.0"
    assert calculator('/', 5, 2) == "5 / 2 = 2.5"
    assert calculator('/', 5, 0) == "Divided by zero"

def test_remainder():
    assert calculator('%', 5, 3) == "5 % 3 = 2"
    assert calculator('%', 5, 0) == "Divided by zero"

def test_power():
    assert calculator('**', 2, 3) == "2 ** 3 = 8"
    assert calculator('**', 5, 0) == "5 ** 0 = 1"

def test_square_root():
    assert math.sqrt(9) == 3
    assert math.sqrt(0) == 0
    assert math.sqrt(16) == 4

def test_trigonometric():
    assert math.sin(math.radians(0)) == 0
    assert math.cos(math.radians(0)) == 1
    assert math.tan(math.radians(45)) == pytest.approx(1, rel=1e-9)

def test_logarithm():
    assert math.log(1) == 0
    assert math.log(8, 2) == 3
    assert math.log(100, 10) == 2

if __name__ == "__main__":
    pytest.main()
