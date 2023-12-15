""" This is a template file do not use it directly.
"""
import re
from inspect import getsourcefile
from pathlib import Path

import pytest

from src.advent_of_code_2023.day15.main import (
    hasher,
    main,
    part_two_main,
)


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(main)).resolve().parent / "README.md"
    with source_path.open("r") as file:
        example_slice = slice(92, 93)
        return [line.strip() for line in file.readlines()[example_slice]]


def provide_subtest_line() -> list[str]:
    source_path = Path(getsourcefile(main)).resolve().parent / "README.md"
    with source_path.open("r") as file:
        example_slice = slice(97, 108)
        return [line.strip() for line in file.readlines()[example_slice]]


@pytest.fixture(scope="function")
def input_stub(request: str) -> str:
    string_to_hash = re.compile(r"`(\w+)`")
    return string_to_hash.search(request)[1]


@pytest.fixture(scope="function")
def expected_hash(request: str) -> int:
    pattern_result = re.compile(r"\*`(\d+)`\*")
    return int(pattern_result.search(request)[1])


@pytest.mark.parametrize(
    "input_stub, expected_hash",
    [*provide_subtest_line()],
    indirect=["input_stub", "expected_hash"],
)
def test_hasher(input_stub, expected_hash) -> None:
    actual = hasher(input_stub)
    assert actual == expected_hash


def test_main(provide_test_lines: list[str]) -> None:
    expected = 1320
    actual = main(provide_test_lines)
    assert actual == expected


def test_part_two_main(provide_test_lines: list[str]) -> None:
    expected = "placeholder"
    actual = part_two_main(provide_test_lines)
    assert actual == expected
