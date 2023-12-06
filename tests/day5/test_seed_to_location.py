from collections import OrderedDict
from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from src.advent_of_code_2023.day5.seed_to_location import (
    calculate_minimum_location,
    parse,
    reroute_point,
    parse_digits,
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
) -> OrderedDict[str, List[str]]:
    return parse(provide_test_lines)


def test_reroute_point(provide_seed_maps_dict):
    expected = [81, 14, 57, 13]
    seeds = provide_seed_maps_dict["seeds"]
    map_stub = provide_seed_maps_dict["seed-to-soil"]
    actual = [
        reroute_point(map_stub, seed) for seed in parse_digits(str(seeds))
    ]
    assert actual == expected


def test_calculate_minimum_location(provide_seed_maps_dict):
    expected = [82, 43, 86, 35]
    actual = calculate_minimum_location(provide_seed_maps_dict)
    assert actual == expected
