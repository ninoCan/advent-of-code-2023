from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from src.advent_of_code_2023.day12.main import (
    main,
    part_two_main,
    parse,
    count_arrangements,
)


@pytest.fixture
def provide_test_lines() -> List[str]:
    source_path = Path(getsourcefile(main)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(68, 74)
        return [line.strip() for line in file.readlines()[example_slice]]


@pytest.mark.parametrize(
    ['line', 'expected'],
    [
        (0, 1),
        (1, 4),
        (2, 1),
        (3, 1),
        (4, 4),
        (5, 10),
    ],
)
def test_count_arrangements(line, expected, provide_test_lines):
    line_stub = parse([provide_test_lines[line]])
    actual = count_arrangements(*line_stub.keys(), *line_stub.values())
    assert actual == expected


def test_main(provide_test_lines: List[str]) -> None:
    expected = 21
    actual = main(provide_test_lines)
    assert actual == expected


def test_part_two_main(provide_test_lines: List[str]) -> None:
    expected = "placeholder"
    actual = part_two_main(provide_test_lines)
    assert actual == expected
