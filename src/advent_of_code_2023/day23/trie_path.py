from dataclasses import dataclass

from advent_of_code_2023.day3.board import Coords


@dataclass
class TriePath:
    paths: dict[int, list[Coords]]

    @property
    def max_length(self) -> int:
        return max(self.paths.keys())
