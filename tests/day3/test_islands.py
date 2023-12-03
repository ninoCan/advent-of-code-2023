from typing import List, Tuple

import pytest

from advent_of_code_2023.day3 import islands
from advent_of_code_2023.day3.board import Coords


@pytest.fixture
def points_stub() -> List[Coords]:
    return [
        Coords(0, 1),
        Coords(0, 3),
        Coords(0, 4),
        Coords(0, 5),
        Coords(1, 2),
        Coords(1, 3),
        Coords(2, 1),
        Coords(2, 2),
        Coords(3, 1),
        Coords(3, 2),
        Coords(3, 3),
        Coords(3, 5),
    ]


@pytest.fixture
def expected() -> List[List[Tuple[int, Coords]]]:
    return [
        [(0, Coords(0, 1))],
        [(1, Coords(0, 3)), (2, Coords(0, 4)), (3, Coords(0, 5))],
        [(4, Coords(1, 2)), (5, Coords(1, 3))],
        [(6, Coords(2, 1)), (7, Coords(2, 2))],
        [(8, Coords(3, 1)), (9, Coords(3, 2)), (10, Coords(3, 3))],
        [(11, Coords(3, 5))],
    ]


def test_cluster_coordinates_and_enumerate(points_stub, expected):
    actual = islands.cluster_coordinates_and_enumerate(points_stub)
    assert type(actual) == type(expected)
    assert actual == expected
