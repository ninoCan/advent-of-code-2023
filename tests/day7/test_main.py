""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from src.advent_of_code_2023.day7.main import (
    main,
    part_two_main,
    order_by_rank,
)


@pytest.fixture
def provide_test_lines() -> List[str]:
    source_path = Path(getsourcefile(main)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(82, 87)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_main(provide_test_lines: List[str]) -> None:
    expected = 6440
    actual = main(provide_test_lines)
    assert actual == expected


def test_part_two_main(provide_test_lines: List[str]) -> None:
    expected = "placeholder"
    actual = part_two_main(provide_test_lines)
    assert actual == expected


@pytest.mark.parametrize(
    'stub_cards_bids, expected',
    [
        (("AAAAA 3", "TK987 1", "TTKK9 2"), ('AAAAA 3', 'TTKK9 2', 'TK987 1')),
        (("QQQ89 1", "TTTT2 3", "KKK22 2"), ("TTTT2 3", "KKK22 2", "QQQ89 1")),
    ],
)
def test_order_by_rank(stub_cards_bids, expected) -> None:
    actual = order_by_rank(stub_cards_bids)
    assert expected == actual
