from dataclasses import fields
from functools import reduce
from pathlib import Path
from typing import List

from advent_of_code_2023.day2.bag import Bag
from advent_of_code_2023.day2.game import Game


def sum_ids_of_possible_games_with_constraint(
    games: list[str],
    constraint: Bag = Bag(12, 13, 14),
) -> int:
    """Determine which games are possible, given a constraint. Then, sum their ids.
    The default constraint is (12,13,14)"""
    all_games = [Game(game) for game in games]
    possible_game_ids = [
        game.id for game in all_games if game.is_possible(constraint)
    ]
    return sum(possible_game_ids)


def sum_of_minimum_power(games: list[str]) -> int:
    """Determine the sum of minimum power for all games"""
    return sum([minimum_power(Game(game)) for game in games])


def minimum_power(game: Game) -> int:
    maximal_bag = find_color_maxes(game.matches, Bag(0, 0, 0))
    return reduce(
        lambda x, y: x * y,
        [getattr(maximal_bag, field.name) for field in fields(Bag)],
        1,
    )


def find_color_maxes(matches: List[Bag], prev_max: Bag) -> Bag:
    if len(matches) == 0:
        return prev_max
    current, *rest = matches
    max_is_smaller = any(
        [
            getattr(prev_max, field.name) < getattr(current, field.name)
            for field in fields(Bag)
        ]
    )
    if max_is_smaller:
        new = {
            color.name: max(
                getattr(prev_max, color.name), getattr(current, color.name)
            )
            for color in fields(Bag)
        }
        return find_color_maxes(rest, Bag(**new))
    return find_color_maxes(rest, prev_max)


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    result = sum_ids_of_possible_games_with_constraint(lines)
    new_result = sum_of_minimum_power(lines)
    print(new_result)
