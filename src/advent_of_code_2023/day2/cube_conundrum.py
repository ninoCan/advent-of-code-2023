from pathlib import Path

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


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    result = sum_ids_of_possible_games_with_constraint(lines)
    print(result)
