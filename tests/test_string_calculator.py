import pytest
from src.string_calculator import StringCalculator


def test_empty_string():
    assert StringCalculator.add("") == 0


def test_single_number():
    assert StringCalculator.add("1") == 1


def test_two_numbers():
    assert StringCalculator.add("2,4") == 6


def test_multiple_numbers():
    assert StringCalculator.add("1,2,3,4") == 10


def test_newline_as_delimiter():
    assert StringCalculator.add("1\n2,3") == 6


def test_custom_delimiter():
    assert StringCalculator.add("//;\n1;2") == 3
    assert StringCalculator.add("//|\n2|3|4") == 9
    assert StringCalculator.add("//-\n10-5-2") == 17


def test_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed -3"):
        StringCalculator.add("1,-3,5")


def test_multiple_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed -6,-2"):
        StringCalculator.add("1,-6,5,-2")

