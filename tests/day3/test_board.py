from typing import List

import numpy as np
import pytest

from advent_of_code_2023.day3.board import Board
from tests.day3.test_gear_ratios import provide_test_lines


def make_array(arr: List[str]) -> np.chararray:
    return np.char.array(arr, unicode=True)


def are_arrays_equal(left: np.chararray, right: np.chararray) -> bool:
    return np.all(np.array_equal(left, right))


def test_get_neighbors_of_cell(provide_test_lines):
    under_test = Board(provide_test_lines)
    actual = under_test.get_neighbors_of_cell
    assert are_arrays_equal(actual(0, 0), make_array(['6']))
    assert actual(2, 0).shape == (0,)
    assert are_arrays_equal(actual(2, 2), make_array(['*', '5']))
