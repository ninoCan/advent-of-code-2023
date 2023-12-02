from typing import Iterable

from advent_of_code_2023.day2.bag import Bag


class Game:
    id: int
    matches: Iterable[Bag]

    def __init__(self, game_string):
        header, all_matches = game_string.split(": ")
        self.id = int(header.split()[1])
        self.matches = (
            Bag.init_from_string(extraction)
            for extraction in all_matches.split("; ")
        )

    def is_possible(self, constraint: Bag) -> bool:
        return all(
            extraction.satisfy_constraint(constraint)
            for extraction in self.matches
        )
