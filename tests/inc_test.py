""" content of calculator.py#"""
import calculator.calculator as calc
# pylint: disable=too-few-public-methods


def test_answer():
    """This Tests the function"""
    assert calc.inc(4) == 5