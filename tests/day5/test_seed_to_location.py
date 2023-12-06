import copy
from inspect import getsourcefile
from pathlib import Path
from typing import List, Dict

import numpy as np
import pytest

from src.advent_of_code_2023.day5.seed_to_location import (
    calculate_minimum_location,
    parse,
    create_translation_table,
    chain_translations,
)


@pytest.fixture
def provide_test_lines() -> List[str]:
    source_path = (
        Path(getsourcefile(calculate_minimum_location)).resolve().parent
    ) / 'If_You_Give_A_Seed_A_Fertilizer.md'
    with source_path.open("r") as file:
        return [line.strip() for line in file.readlines()[37:70]]


@pytest.fixture
def provide_seed_maps_dict(
    provide_test_lines: List[str],
) -> Dict[str, List[List[int]]]:
    return parse(provide_test_lines)


def test_parse(provide_test_lines):
    actual = parse(provide_test_lines)
    assert actual is dict
    assert len(actual.keys()) == 8
    assert "seeds" in actual.keys()
    assert len(actual["seeds"]) == 4
    actual.pop("seeds")
    for _, value in actual.items():
        assert len(value) == 3


def test_chain_translations(provide_seed_maps_dict):
    test_dict = copy.deepcopy(provide_seed_maps_dict)
    seeds = np.array(test_dict.pop("seeds"))
    expected = [82, 43, 86, 35]
    actual = chain_translations(test_dict, seeds)
    assert actual == expected


def test_create_translation_table(provide_seed_maps_dict, expected_matrix):
    to_be_swapped = [*range(50), *range(52, 52 + 48), *range(50, 52)]
    expected = list(zip(range(len(to_be_swapped)), to_be_swapped))
    actual = create_translation_table(provide_seed_maps_dict["seed-to-soil"])
    assert actual == expected_matrix
