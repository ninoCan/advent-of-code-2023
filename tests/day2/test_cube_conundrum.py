from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from advent_of_code_2023.day2.cube_conundrum import sum_ids_of_possible_games_with_constraint


@pytest.fixture
def provide_list_of_games() -> List[str]:
    source_folder = Path(getsourcefile(sum_ids_of_possible_games_with_constraint)).resolve().parent
    source_path = source_folder / "cube_conundrum.md"
    with source_path.open("r") as file:
        return [line.strip() for line in file.readlines() if 'Game' in line[:8]]


def test_sum_ids_of_possible_games_with_constraint(provide_list_of_games):
    games = provide_list_of_games
    actual = sum_ids_of_possible_games_with_constraint(provide_list_of_games)
    expected = 8
    assert actual == expected
