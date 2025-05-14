import pytest
from functions.add import execute as add
from functions.sub import execute as sub
from functions.multiplication import execute as multiplication
from functions.division import execute as division

def test_add():
    assert add(2, 3) == 5, "Soma de 2 e 3 deve ser 5"
    assert add(-1, 1) == 0, "Soma de -1 e 1 deve ser 0"
    assert add(0, 0) == 0, "Soma de 0 e 0 deve ser 0"
    assert add(-5, -3) == -8, "Soma de -5 e -3 deve ser -8"

def test_sub():
    assert sub(5, 3) == 2, "Subtração de 5 por 3 deve ser 2"
    assert sub(3, 5) == -2, "Subtração de 3 por 5 deve ser -2"
    assert sub(0, 0) == 0, "Subtração de 0 por 0 deve ser 0"
    assert sub(-2, -3) == 1, "Subtração de -2 por -3 deve ser 1"

def test_multiplication():
    assert multiplication(4, 5) == 20
    assert multiplication(10, 10) == 100
    assert multiplication(3, 5) == 15
    assert multiplication(7, 8) == 56

def test_division():
    assert division(10, 2) == 5
    assert division(10, 10) == 1
    assert division(20, 2) == 10
    assert division(25, 5) == 5



