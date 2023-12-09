""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from src.advent_of_code_2023.day9.main import (
    main,
    part_two_main,
    predict_next_value,
    parse_integers,
)


@pytest.fixture
def provide_test_lines() -> List[str]:
    source_path = Path(getsourcefile(main)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(28, 31)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_main(provide_test_lines: List[str]) -> None:
    expected = 114
    actual = main(provide_test_lines)
    assert actual == expected


def test_part_two_main(provide_test_lines: List[str]) -> None:
    expected = 2
    actual = part_two_main(provide_test_lines)
    assert actual == expected


@pytest.mark.parametrize('input_index, expected', [(0, 18), (1, 28), (2, 68)])
def test_predict_next_value(provide_test_lines, input_index, expected) -> None:
    line_stub = provide_test_lines[input_index]
    actual = predict_next_value(line_stub)
    assert actual == expected


@pytest.mark.parametrize('input_index, expected', [(0, -3), (1, 2), (2, 5)])
def test_predict_previous_value(
    provide_test_lines, input_index, expected
) -> None:
    line_stub = provide_test_lines[input_index]
    actual = predict_next_value(line_stub)
    assert actual == expected


@pytest.mark.parametrize(
    'stub_line, expected',
    [
        ("-2 0 2 4 6", [-2, 0, 2, 4, 6]),
        ("0 -1 1 3 8", [0, -1, 1, 3, 8]),
        ("1 2 3 4 5", [1, 2, 3, 4, 5]),
    ],
)
def test_parse_integers(stub_line, expected) -> None:
    actual = parse_integers(stub_line)
    assert actual == expected
