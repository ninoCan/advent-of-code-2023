from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from src.advent_of_code_2023.day3.gear_ratios import (
    identify_and_sum_relevant_numbers,
)


@pytest.fixture
def provide_test_lines() -> List[str]:
    source_path = (
        Path(getsourcefile(identify_and_sum_relevant_numbers)).resolve().parent
    )
    with source_path.open("r") as file:
        return [line.strip() for line in file.readlines()[30:40]]


def test_identify_and_sum_relevant_numbers(provide_test_lines):
    actual = identify_and_sum_relevant_numbers(provide_test_lines)
    expected = 4361
    assert actual == expected
