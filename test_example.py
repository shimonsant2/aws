# pytest example
import random


def func(x):
    return x + 1


def test_answer1():
    assert random.choice([3, 3]) == 3


def test_answer2():
    assert func(3) == 4


def test_answer3():
    assert func(3) == 4


def test_answer4():
    assert func(44) == 45


def test_answer5():
    assert func(44) == 45
