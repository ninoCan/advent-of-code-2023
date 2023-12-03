from typing import List, Tuple

import pytest

from advent_of_code_2023.day3 import islands
from advent_of_code_2023.day3.board import Coords, Board
from tests.day3.test_gear_ratios import provide_test_lines


@pytest.fixture
def digits_stub() -> List[int]:
    return [(el + 1) % 10 for el in range(12)]


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
def expected_indexed_coordinate_cluster() -> List[List[Tuple[int, Coords]]]:
    return [
        [(0, Coords(0, 1))],
        [(1, Coords(0, 3)), (2, Coords(0, 4)), (3, Coords(0, 5))],
        [(4, Coords(1, 2)), (5, Coords(1, 3))],
        [(6, Coords(2, 1)), (7, Coords(2, 2))],
        [(8, Coords(3, 1)), (9, Coords(3, 2)), (10, Coords(3, 3))],
        [(11, Coords(3, 5))],
    ]


def test_cluster_coordinates_and_enumerate(
    points_stub, expected_indexed_coordinate_cluster
):
    actual = islands.cluster_coordinates_and_enumerate(points_stub)
    assert type(actual) == type(expected_indexed_coordinate_cluster)
    assert actual == expected_indexed_coordinate_cluster


@pytest.fixture
def expected_island_values(provide_test_lines) -> List[int]:
    return [
        int(item)
        for line in provide_test_lines
        for item in line.replace("*", "")
        .replace("$", "")
        .replace("#", "")
        .replace("+", "")
        .split(".")
        if item
    ]


def test_find_islands(provide_test_lines, expected_island_values):
    under_test = islands.find_islands(Board(provide_test_lines))
    actual = [island.value for island in under_test]
    assert actual == expected_island_values


@pytest.fixture
def expected_value_coords_pair_cluster():
    return [
        [(1, Coords(0, 1))],
        [(2, Coords(0, 3)), (3, Coords(0, 4)), (4, Coords(0, 5))],
        [(5, Coords(1, 2)), (6, Coords(1, 3))],
        [(7, Coords(2, 1)), (8, Coords(2, 2))],
        [(9, Coords(3, 1)), (0, Coords(3, 2)), (1, Coords(3, 3))],
        [(2, Coords(3, 5))],
    ]


def test_assemble_value_coord_cluster_from_coord_cluster(
    digits_stub,
    expected_indexed_coordinate_cluster,
    expected_value_coords_pair_cluster,
):
    actual = islands.assemble_value_points_pair_cluster(
        digits_stub, expected_indexed_coordinate_cluster
    )
    assert actual == expected_value_coords_pair_cluster
