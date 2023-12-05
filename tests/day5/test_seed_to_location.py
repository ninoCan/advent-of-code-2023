import copy
from inspect import getsourcefile
from pathlib import Path
from typing import List, Dict

import numpy as np
import pytest

from src.advent_of_code_2023.day5.seed_to_location import (
    calculate_minimum_location,
    swap_columns,
    parse,
    assemble_matrix,
    multiply_map_matrices,
)


@pytest.fixture
def provide_test_lines() -> List[str]:
    source_path = (
        Path(getsourcefile(calculate_minimum_location)).resolve().parent
    ) / 'If_You_Give_A_Seed_A_Fertilizer.md'
    with source_path.open("r") as file:
        return [line.strip() for line in file.readlines()[37:70]]


@pytest.fixture
def expected_matrix() -> np.array:
    to_be_swapped = [*range(50), *range(52, 52 + 48), *range(50, 52)]
    matrix_size = len(to_be_swapped)
    cols_to_swap = list(zip(range(matrix_size), to_be_swapped))
    return swap_columns(cols_to_swap)


@pytest.fixture
def provide_seed_maps_dict(
    provide_test_lines: List[str],
) -> Dict[str, List[List[int]]]:
    return parse(provide_test_lines)


def test_multiply_map_matrices(provide_seed_maps_dict):
    test_dict = copy.deepcopy(provide_seed_maps_dict)
    seeds = np.array(test_dict.pop("seeds"))
    expected = [82, 43, 86, 35]
    under_test = multiply_map_matrices(test_dict)
    actual = np.dot(seeds, multiply_map_matrices(test_dict))
    assert actual == expected


def test_assemble_matrix(provide_seed_maps_dict, expected_matrix):
    actual = assemble_matrix(provide_seed_maps_dict["seed-to-soil"])
    assert actual == expected_matrix
