from pathlib import Path
from typing import Set

from .bag import Bag


def sum_ids_of_possible_games_with_constraint(
    games: list[str],
    constraint: Bag = Bag(12, 13, 14),
) -> int:
    """Determine which games are possible, given a constraint. Then, sum their ids.
    The default constraint is (12,13,14)"""


def parse_game(game: str) -> (int, Set[Bag]):
    """Return a list of Bag describing the matches of a Game"""

    header, all_matches = game.split(": ")
    game_id = header.split()[1]
    matches = all_matches.split("; ")
    return (game_id, set((Bag.init_from_string(match) for match in matches)))


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    result = sum_ids_of_possible_games_with_constraint(lines)
    print(result)
