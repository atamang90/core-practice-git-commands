import pytest


def always_returns_true():
    print(True)
    print("It's always true Tazmeen!")
    return True


def test_always_returns_true():
    assert always_returns_true()
