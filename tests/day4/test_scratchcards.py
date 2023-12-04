from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from src.advent_of_code_2023.day4.scratchcards import (
    calculate_victory_points,
    calculate_row_points,
    calculate_row_matches,
    parse_row,
)


@pytest.fixture
def provide_test_lines() -> List[str]:
    source_path = (
        Path(getsourcefile(calculate_victory_points)).resolve().parent
    ) / 'gear_ratios.md'
    with source_path.open("r") as file:
        return [line.strip() for line in file.readlines()[43:49]]


def test_calculate_victory_points(provide_test_lines):
    actual = calculate_victory_points(provide_test_lines)
    expected = 13
    assert actual == expected


@pytest.mark.parametrize(
    'matches, expected_points',
    [
        (4, 8),
        (2, 2),
        (1, 1),
        (0, 0),
    ],
)
def test_calculate_row_points(matches, expected_points):
    actual = calculate_row_points(matches)
    assert actual == expected_points


def test_calculate_row_matches(provide_test_lines, expected_points):
    expected_matches = [4, 2, 2, 1, 0, 0]
    actual = [
        calculate_row_matches(card, winning_numbers)
        for line in provide_test_lines
        for card, winning_numbers in parse_row(line)
    ]
    assert actual == expected_points
