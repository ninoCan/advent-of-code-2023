from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from src.advent_of_code_2023.day10.main import (
    main,
    part_two_main,
)


@pytest.fixture
def provide_test_lines() -> List[str]:
    source_path = Path(getsourcefile(main)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = [
            # slice(53, 58),
            slice(65, 70),
            slice(80, 85),
            slice(89, 94),
        ]
        return [
            a_line.strip()
            for a_slice in example_slice
            for a_line in file.readlines()[a_slice]
        ]


@pytest.mark.parametrize(
    'a_slice, expected',
    [
        (slice(0, 6), 4),
        (slice(0, 6), 4),
        (slice(0, 6), 8),
        (slice(0, 6), 8),
    ],
)
def test_main(provide_test_lines, a_slice, expected) -> None:
    actual = main(provide_test_lines[a_slice])
    assert actual == expected


def test_part_two_main(provide_test_lines: List[str]) -> None:
    expected = "placeholder"
    actual = part_two_main(provide_test_lines)
    assert actual == expected
