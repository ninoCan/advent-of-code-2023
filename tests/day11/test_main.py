from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from advent_of_code_2023.day11.Universe import Universe
from src.advent_of_code_2023.day11.main import (
    main,
    part_two_main,
)


@pytest.fixture
def lines_stub() -> List[str]:
    source_path = Path(getsourcefile(main)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(18, 28)
        return [line.strip() for line in file.readlines()[example_slice]]


@pytest.fixture
def expected_universe() -> Universe:
    source_path = Path(getsourcefile(main)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(56, 68)
        return Universe.init_from_string_list(
            [line.strip() for line in file.readlines()[example_slice]]
        )


def test_main(lines_stub) -> None:
    expected = 374
    actual = main(lines_stub)
    assert actual == expected


def test_expand_universe(lines_stub, expected_universe) -> None:
    universe_stub = Universe.init_from_string_list(lines_stub)
    actual = universe_stub.expand()
    assert actual == expected_universe


def test_part_two_main(lines_stub) -> None:
    expected = "placeholder"
    actual = part_two_main(lines_stub)
    assert actual == expected
