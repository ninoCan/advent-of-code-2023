from pathlib import Path
from typing import List

from .bag import Bag


def sum_ids_of_possible_games_with_constraint(games: List[str], constraint: Bag=Bag(12, 13, 14)) -> int:
    """ Determine which games are possible, given a constraint. Then, sum their ids.
    The default constraint is (12,13,14)"""


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()
    result = sum_ids_of_possible_games_with_constraint(lines)
    print(result)