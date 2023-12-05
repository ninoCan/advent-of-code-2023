from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from src.advent_of_code_2023.day5.seed_to_location import (
    calculate_minimum_location,
)


@pytest.fixture
def provide_test_lines() -> List[str]:
    source_path = (
        Path(getsourcefile(calculate_minimum_location)).resolve().parent
    ) / 'If_You_Give_A_Seed_A_Fertilizer.md'
    with source_path.open("r") as file:
        return [line.strip() for line in file.readlines()[37:70]]


def test_calculate_minimum_location():
    assert False
