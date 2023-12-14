""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from src.advent_of_code_2023.day14.main import (
    main,
    part_two_main,
)


@pytest.fixture
def provide_test_lines() -> List[str]:
    source_path = Path(getsourcefile(main)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(32, 42)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_main(provide_test_lines: List[str]) -> None:
    expected = 136
    actual = main(provide_test_lines)
    assert actual == expected


def test_part_two_main(provide_test_lines: List[str]) -> None:
    expected = "placeholder"
    actual = part_two_main(provide_test_lines)
    assert actual == expected
