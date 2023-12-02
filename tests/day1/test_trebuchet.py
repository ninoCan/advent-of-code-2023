import pytest

from src.advent_of_code_2023.day1.trebuchet import sum_all_digits_in_file


def test_sum_all_digits_in_file():
    input_prompt = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
    
    actual: int = sum_all_digits_in_file(input_prompt.split('\n'))
    expected: int = 281
    assert actual == expected
