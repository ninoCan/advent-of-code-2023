from inspect import getsourcefile
from pathlib import Path
from typing import List

import pytest

from advent_of_code_2023.day2.bag import Bag
from advent_of_code_2023.day2.cube_conundrum import (
    sum_ids_of_possible_games_with_constraint,
    sum_of_minimum_power,
    find_color_maxes,
)
from advent_of_code_2023.day2.game import Game


@pytest.fixture
def provide_list_of_games() -> List[str]:
    source_folder = (
        Path(getsourcefile(sum_ids_of_possible_games_with_constraint))
        .resolve()
        .parent
    )
    source_path = source_folder / "cube_conundrum.md"
    with source_path.open("r") as file:
        return [line.strip() for line in file.readlines()[29:34]]
        # return [
        #     line.strip() for line in file.readlines() if '  Game' in line[:8]
        # ]


def test_sum_ids_of_possible_games_with_constraint(provide_list_of_games):
    actual = sum_ids_of_possible_games_with_constraint(provide_list_of_games)
    expected = 8
    assert actual == expected


def test_sum_of_minimum_power(provide_list_of_games):
    actual = sum_of_minimum_power(provide_list_of_games)
    expected = 2286
    assert actual == expected


def test_find_color_maxes(provide_list_of_games):
    games = [Game(game_string) for game_string in provide_list_of_games]
    actual = [find_color_maxes(game.matches, Bag(0, 0, 0)) for game in games]
    expected = (
        Bag(4, 2, 6),
        Bag(1, 3, 4),
        Bag(20, 13, 6),
        Bag(14, 3, 15),
        Bag(6, 3, 2),
    )
    for i in range(5):
        assert actual[i] == expected[i]
