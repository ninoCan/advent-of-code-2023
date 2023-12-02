import pytest

from src.advent_of_code_2023.day1.trebuchet import sum_all_digits_in_file


def test_sum_all_digits_in_file():
    input_prompt = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    actual: int = sum_all_digits_in_file(input_prompt.split('\n'))
    expected: int = 142
    assert actual == expected
    


